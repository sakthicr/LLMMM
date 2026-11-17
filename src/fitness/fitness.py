"""
Composite fitness function: F = 0.5 * Q̄ + 0.25 * Rhyme + 0.25 * Structure

Matches the base paper's F(H) = 0.5·Emotion + 0.25·Rhyme + 0.25·Syllable
weighting exactly. The soft term (Q̄) is the only upgrade — from lexicon-based
TextBlob to multi-dimensional LLM-judged quality.
"""

import logging

from src.config import FITNESS_WEIGHT_Q, FITNESS_WEIGHT_RHYME, FITNESS_WEIGHT_STRUCTURE
from src.fitness.structure import score_structure
from src.fitness.rhyme import score_rhyme
from src.fitness.quality import score_quality

logger = logging.getLogger(__name__)


def compute_fitness_from_components(
    q_bar: float,
    rhyme_score: float,
    structure_score: float,
) -> float:
    """
    Compute composite fitness F from pre-computed component scores.

    F = 0.5 * Q̄ + 0.25 * Rhyme + 0.25 * Structure
    """
    f = (
        FITNESS_WEIGHT_Q * q_bar +
        FITNESS_WEIGHT_RHYME * rhyme_score +
        FITNESS_WEIGHT_STRUCTURE * structure_score
    )
    return round(f, 4)


async def evaluate_poem(
    poem_text: str,
    poem_type: str,
    target_emotion: str,
) -> dict:
    """
    Full fitness evaluation of a single poem.

    Computes all three components and the aggregate F score.

    Returns dict with:
        - F: composite fitness score
        - Q_bar: LLM-judged quality (0-1)
        - Rhyme: rhyme compliance (0-1)
        - Structure: structural compliance (0-1)
        - sub_scores: individual judge dimension scores
        - judge_model: actual model ID served for judging
    """
    # Rule-based components (no API calls)
    structure_score = score_structure(poem_text, poem_type)
    rhyme_score = score_rhyme(poem_text, poem_type)

    # LLM-judged component (API call to judge model)
    q_bar, sub_scores, judge_model = await score_quality(
        poem_text, poem_type, target_emotion
    )

    # Composite fitness
    f = compute_fitness_from_components(q_bar, rhyme_score, structure_score)

    result = {
        "F": f,
        "Q_bar": q_bar,
        "Rhyme": rhyme_score,
        "Structure": structure_score,
        "sub_scores": sub_scores,
        "judge_model": judge_model,
    }

    logger.info(
        f"F={f:.3f} (Q_bar={q_bar:.3f}, R={rhyme_score:.3f}, S={structure_score:.3f}) "
        f"| {poem_type} | judge={judge_model}"
    )

    return result


async def evaluate_poem_calibration(
    poem_text: str,
    poem_type: str,
) -> dict:
    """
    Calibration-mode fitness evaluation of a single poem.

    Uses 4-dimension Q̄ (no emotion_alignment) since reference poems
    have no target emotion. Otherwise identical to evaluate_poem().

    Returns dict with:
        - F: composite fitness score
        - Q_bar: calibration-mode quality (0-1, 4 dimensions)
        - Rhyme: rhyme compliance (0-1)
        - Structure: structural compliance (0-1)
        - sub_scores: individual judge dimension scores
        - judge_model: actual model ID served for judging
    """
    from src.fitness.quality import score_quality_calibration

    # Rule-based components (no API calls)
    structure_score = score_structure(poem_text, poem_type)
    rhyme_score = score_rhyme(poem_text, poem_type)

    # LLM-judged component (API call, calibration mode — no emotion dim)
    q_bar, sub_scores, judge_model = await score_quality_calibration(
        poem_text, poem_type,
    )

    # Composite fitness
    f = compute_fitness_from_components(q_bar, rhyme_score, structure_score)

    result = {
        "F": f,
        "Q_bar": q_bar,
        "Rhyme": rhyme_score,
        "Structure": structure_score,
        "sub_scores": sub_scores,
        "judge_model": judge_model,
    }

    logger.info(
        f"F={f:.3f} (Q_bar_cal={q_bar:.3f}, R={rhyme_score:.3f}, S={structure_score:.3f}) "
        f"| {poem_type} | judge={judge_model} [calibration]"
    )

    return result
