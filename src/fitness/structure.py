"""
Structure scoring: syllable counting (CMUdict + fallback) and stress patterns.

- Haiku: 3 lines, syllables 5-7-5
- Limerick: 5 lines, stress pattern 3-3-2-2-3 beats
"""

import re

from src.fitness.textnorm import normalize_for_scoring
import logging
from functools import lru_cache

import nltk

logger = logging.getLogger(__name__)

# ── CMUdict loading ──────────────────────────────────────────────────────────

_cmudict: dict | None = None


def _ensure_cmudict():
    """Download CMUdict if not already available."""
    global _cmudict
    if _cmudict is None:
        try:
            _cmudict = nltk.corpus.cmudict.dict()
        except LookupError:
            nltk.download("cmudict", quiet=True)
            _cmudict = nltk.corpus.cmudict.dict()
    return _cmudict


# ── Syllable counting ───────────────────────────────────────────────────────

@lru_cache(maxsize=10000)
def count_syllables(word: str) -> int:
    """
    Count syllables for a word using CMUdict, with vowel-cluster fallback.

    CMUdict encodes stressed vowels with digits (0, 1, 2).
    Fallback: count runs of vowel characters.
    """
    word = word.lower().strip()
    word = re.sub(r"[^a-z']", "", word)  # keep only letters and apostrophes
    if not word:
        return 0

    cmu = _ensure_cmudict()
    if word in cmu:
        # Use the first pronunciation
        phones = cmu[word][0]
        return sum(1 for p in phones if p[-1].isdigit())

    # g2p_en fallback
    return _g2p_syllables(word)


_g2p_instance = None

def _get_g2p():
    global _g2p_instance
    if _g2p_instance is None:
        import nltk
        try:
            nltk.data.find('taggers/averaged_perceptron_tagger_eng')
        except LookupError:
            nltk.download('averaged_perceptron_tagger_eng', quiet=True)

        from g2p_en import G2p
        _g2p_instance = G2p()
    return _g2p_instance


def _g2p_syllables(word: str) -> int:
    """
    Syllable counter for words not in CMUdict using g2p_en.
    """
    g2p = _get_g2p()
    phones = g2p(word)
    count = sum(1 for p in phones if p[-1].isdigit())
    if count == 0:
        count = 1
    return count


def count_line_syllables(line: str) -> int:
    """Count total syllables in a line of text."""
    words = re.findall(r"[a-zA-Z']+", line)
    return sum(count_syllables(w) for w in words)


# ── Stress pattern analysis ─────────────────────────────────────────────────

@lru_cache(maxsize=10000)
def get_stress_pattern(word: str) -> list[int]:
    """
    Get the stress pattern for a word from CMUdict.

    Returns list of stress levels: 0=no stress, 1=primary, 2=secondary.
    Falls back to alternating 0-1 pattern for unknown words.
    """
    word = word.lower().strip()
    word = re.sub(r"[^a-z']", "", word)
    if not word:
        return []

    cmu = _ensure_cmudict()
    if word in cmu:
        phones = cmu[word][0]
        return [int(p[-1]) for p in phones if p[-1].isdigit()]

    # Fallback: g2p_en
    g2p = _get_g2p()
    phones = g2p(word)
    return [int(p[-1]) for p in phones if p[-1].isdigit()]


def count_strong_beats(line: str) -> int:
    """
    Count strong (stressed) beats in a line.

    A strong beat is a syllable with stress >= 1 in CMUdict.
    """
    words = re.findall(r"[a-zA-Z']+", line)
    beats = 0
    for word in words:
        stress = get_stress_pattern(word)
        beats += sum(1 for s in stress if s >= 1)
    return beats


# ── Structure scoring ────────────────────────────────────────────────────────

def score_haiku_structure(lines: list[str]) -> float:
    """
    Score a haiku's structural compliance.

    Target: 3 lines with syllables [5, 7, 5].
    Score is 1.0 minus a normalized penalty for deviations.
    """
    target = [5, 7, 5]

    if len(lines) != 3:
        # Severe penalty for wrong line count, but don't zero out
        line_penalty = 0.5 * min(abs(len(lines) - 3), 3) / 3
        # Still try to score what we have
        lines = lines[:3] if len(lines) > 3 else lines + [""] * (3 - len(lines))
    else:
        line_penalty = 0.0

    syllable_counts = [count_line_syllables(line) for line in lines]
    total_deviation = sum(abs(actual - expected)
                         for actual, expected in zip(syllable_counts, target))
    max_deviation = sum(target)  # theoretical maximum
    syllable_penalty = total_deviation / max_deviation

    score = max(0.0, 1.0 - line_penalty - syllable_penalty)
    return round(score, 4)


def score_limerick_structure(lines: list[str]) -> float:
    """
    Score a limerick's structural compliance.

    Target: 5 lines with syllable counts approximately [8, 8, 5, 5, 8],
    which correspond to the standard anapestic 3-3-2-2-3 foot pattern
    (~2.67 syllables per foot).

    Each line gets graded credit via a Gaussian falloff centred on its
    target syllable count, so a line that's off by 1 syllable still
    scores high. This mirrors the partial-credit approach Rhyme uses
    for partial AABBA matches.

    Note: the previous approach counted CMUdict stress marks as "beats",
    but CMUdict assigns primary stress to the sole vowel of every
    monosyllable (e.g. "was" → stress=1), so function words were
    being counted as strong beats, inflating line totals to 7-8 and
    collapsing all scores to near zero.
    """
    import math

    # Standard limerick syllable targets (anapestic meter)
    target_syllables = [8, 8, 5, 5, 8]

    if len(lines) != 5:
        line_penalty = 0.4 * min(abs(len(lines) - 5), 5) / 5
        lines = lines[:5] if len(lines) > 5 else lines + [""] * (5 - len(lines))
    else:
        line_penalty = 0.0

    actual_syllables = [count_line_syllables(line) for line in lines]

    # Graded per-line score: Gaussian centred on target, sigma=2.
    # A deviation of 0 → 1.0, ±1 → 0.88, ±2 → 0.61, ±3 → 0.32, etc.
    sigma = 2.0
    line_scores = []
    for actual, expected in zip(actual_syllables, target_syllables):
        deviation = abs(actual - expected)
        line_scores.append(math.exp(-(deviation ** 2) / (2 * sigma ** 2)))

    syllable_score = sum(line_scores) / len(line_scores)

    score = max(0.0, (1.0 - line_penalty) * syllable_score)
    return round(score, 4)


def score_structure(poem_text: str, poem_type: str) -> float:
    """
    Score a poem's structural compliance based on its type.

    Args:
        poem_text: The full poem text (lines separated by newlines)
        poem_type: 'haiku' or 'limerick'

    Returns:
        Float score in [0, 1].
    """
    poem_text = normalize_for_scoring(poem_text)
    lines = [line.strip() for line in poem_text.strip().split("\n") if line.strip()]

    if poem_type == "haiku":
        return score_haiku_structure(lines)
    elif poem_type == "limerick":
        return score_limerick_structure(lines)
    else:
        raise ValueError(f"Unknown poem type: {poem_type}")
