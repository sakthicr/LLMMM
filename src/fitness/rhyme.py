"""
Rhyme scoring using CMUdict phoneme analysis.

- Haiku: unrhymed baseline 0.5, bonus up to 1.0 for rhyming end-words.
- Limerick: full AABBA rhyme scheme check.
"""

import re
import logging
from functools import lru_cache

import nltk

logger = logging.getLogger(__name__)

_cmudict: dict | None = None


def _ensure_cmudict():
    global _cmudict
    if _cmudict is None:
        try:
            _cmudict = nltk.corpus.cmudict.dict()
        except LookupError:
            nltk.download("cmudict", quiet=True)
            _cmudict = nltk.corpus.cmudict.dict()
    return _cmudict


def _get_last_word(line: str) -> str:
    """Extract the last word from a line, lowercased."""
    words = re.findall(r"[a-zA-Z']+", line)
    return words[-1].lower() if words else ""


@lru_cache(maxsize=10000)
def _get_rhyme_phonemes(word: str) -> list[str] | None:
    """
    Get the rhyming portion of a word (from the last stressed vowel onward).

    Returns None if the word isn't in CMUdict.
    """
    word = word.lower()
    cmu = _ensure_cmudict()

    if word not in cmu:
        return _get_rhyme_phonemes_g2p(word)

    phones = cmu[word][0]

    return _extract_rhyme_phones(phones)


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


def _get_rhyme_phonemes_g2p(word: str) -> list[str] | None:
    g2p = _get_g2p()
    phones = g2p(word)
    # g2p_en returns phones without stress marks for some vowels, but does include them for many.
    # Actually, g2p_en returns stress marks like 'AY1'.
    return _extract_rhyme_phones(phones)


def _extract_rhyme_phones(phones: list[str]) -> list[str] | None:
    # Find the last stressed vowel (stress >= 1)
    last_stressed_idx = -1
    for i, phone in enumerate(phones):
        if phone[-1].isdigit() and int(phone[-1]) >= 1:
            last_stressed_idx = i

    if last_stressed_idx == -1:
        # No stressed vowel found; use everything from the last vowel
        for i in range(len(phones) - 1, -1, -1):
            if phones[i][-1].isdigit():
                last_stressed_idx = i
                break

    if last_stressed_idx == -1:
        return None

    return phones[last_stressed_idx:]


def words_rhyme(word1: str, word2: str) -> bool:
    """
    Check whether two words rhyme using CMUdict phonemes.

    Two words rhyme if their rhyming portions (from last stressed vowel
    onward) match, and they are not the same word.
    """
    if word1.lower() == word2.lower():
        return False

    p1 = _get_rhyme_phonemes(word1)
    p2 = _get_rhyme_phonemes(word2)

    if p1 is None or p2 is None:
        return False

    return p1 == p2


# ── Rhyme scoring ───────────────────────────────────────────────────────────

def score_haiku_rhyme(lines: list[str]) -> float:
    """
    Score rhyme for a haiku.

    Haiku doesn't require rhyme, so unrhymed haiku gets the baseline of 0.5.
    Any detected end-word rhymes add a bonus up to 1.0.
    """
    from src.config import HAIKU_RHYME_BASELINE

    if len(lines) < 2:
        return HAIKU_RHYME_BASELINE

    end_words = [_get_last_word(line) for line in lines if line.strip()]
    end_words = [w for w in end_words if w]

    if len(end_words) < 2:
        return HAIKU_RHYME_BASELINE

    # Check all pairs for rhymes
    rhyme_count = 0
    pair_count = 0
    for i in range(len(end_words)):
        for j in range(i + 1, len(end_words)):
            pair_count += 1
            if words_rhyme(end_words[i], end_words[j]):
                rhyme_count += 1

    if pair_count == 0:
        return HAIKU_RHYME_BASELINE

    # Bonus proportional to rhyming pairs found
    bonus = 0.5 * (rhyme_count / pair_count)
    return round(min(1.0, HAIKU_RHYME_BASELINE + bonus), 4)


def score_limerick_rhyme(lines: list[str]) -> float:
    """
    Score the AABBA rhyme scheme for a limerick.

    Lines 1, 2, 5 should rhyme (group A).
    Lines 3, 4 should rhyme (group B).
    Each group contributes 0.5 to the score.
    """
    if len(lines) != 5:
        # Penalty for wrong line count, but still try
        if len(lines) < 2:
            return 0.0
        lines = lines[:5] if len(lines) > 5 else lines + [""] * (5 - len(lines))

    end_words = [_get_last_word(line) for line in lines]

    # Group A: lines 1, 2, 5 (indices 0, 1, 4)
    a_words = [end_words[i] for i in [0, 1, 4] if end_words[i]]
    a_score = 0.0
    if len(a_words) >= 2:
        a_pairs = 0
        a_rhymes = 0
        for i in range(len(a_words)):
            for j in range(i + 1, len(a_words)):
                a_pairs += 1
                if words_rhyme(a_words[i], a_words[j]):
                    a_rhymes += 1
        if a_pairs > 0:
            a_score = a_rhymes / a_pairs

    # Group B: lines 3, 4 (indices 2, 3)
    b_words = [end_words[i] for i in [2, 3] if end_words[i]]
    b_score = 0.0
    if len(b_words) == 2:
        b_score = 1.0 if words_rhyme(b_words[0], b_words[1]) else 0.0

    # Weighted: A group is slightly more important (3 lines vs 2)
    score = 0.5 * a_score + 0.5 * b_score
    return round(score, 4)


def score_rhyme(poem_text: str, poem_type: str) -> float:
    """
    Score a poem's rhyme compliance.

    Args:
        poem_text: Full poem text (lines separated by newlines)
        poem_type: 'haiku' or 'limerick'

    Returns:
        Float score in [0, 1].
    """
    lines = [line.strip() for line in poem_text.strip().split("\n") if line.strip()]

    if poem_type == "haiku":
        return score_haiku_rhyme(lines)
    elif poem_type == "limerick":
        return score_limerick_rhyme(lines)
    else:
        raise ValueError(f"Unknown poem type: {poem_type}")
