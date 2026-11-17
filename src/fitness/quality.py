"""
LLM-judged quality scoring (Q̄).

Sends the poem to Qwen3.8-27B (the Judge model) and extracts
5 sub-dimension ratings (1-5), averages them, and normalizes to [0, 1].

Dimensions: emotion alignment, imagery, literary devices, originality, coherence.
"""

import json
import re
import logging
from typing import Optional

from src.api.groq_client import judge_poem_groq
from src.prompts.judge import build_judge_prompt

logger = logging.getLogger(__name__)

QUALITY_DIMENSIONS = [
    "emotion_alignment",
    "imagery",
    "literary_devices",
    "originality",
    "coherence",
]


def _parse_judge_response(raw: str) -> dict[str, int]:
    """
    Parse the judge model's JSON response into a dict of dimension → score.

    Handles common model quirks: markdown fences, trailing text, etc.
    """
    text = raw.strip()

    # Strip markdown code fences
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines).strip()

    # Try direct JSON parse first
    try:
        data = json.loads(text)
        return _validate_scores(data)
    except json.JSONDecodeError:
        pass

    # Try to extract JSON object from surrounding text
    match = re.search(r'\{[^{}]+\}', text, re.DOTALL)
    if match:
        try:
            data = json.loads(match.group())
            return _validate_scores(data)
        except json.JSONDecodeError:
            pass

    # Last resort: regex extraction of individual scores
    scores = {}
    for dim in QUALITY_DIMENSIONS:
        pattern = rf'"{dim}"\s*:\s*(\d+)'
        m = re.search(pattern, text)
        if m:
            scores[dim] = int(m.group(1))

    if scores:
        return _validate_scores(scores)

    logger.warning(f"Failed to parse judge response: {text[:200]}")
    # Return neutral scores
    return {dim: 3 for dim in QUALITY_DIMENSIONS}


def _validate_scores(data: dict) -> dict[str, int]:
    """Ensure all dimension scores are present and in [1, 5]."""
    result = {}
    for dim in QUALITY_DIMENSIONS:
        val = data.get(dim, 3)
        try:
            val = int(val)
        except (ValueError, TypeError):
            val = 3
        result[dim] = max(1, min(5, val))
    return result


def compute_q_bar(scores: dict[str, int]) -> float:
    """
    Compute Q̄ — the average of all dimension scores, normalized to [0, 1].

    Each sub-score is 1-5, so Q̄ = (mean - 1) / 4.
    """
    values = [scores.get(dim, 3) for dim in QUALITY_DIMENSIONS]
    mean = sum(values) / len(values)
    q_bar = (mean - 1.0) / 4.0  # Normalize 1-5 → 0-1
    return round(q_bar, 4)


async def score_quality(
    poem_text: str,
    poem_type: str,
    target_emotion: str,
) -> tuple[float, dict[str, int], str]:
    """
    Score a poem's quality using the LLM judge.

    Args:
        poem_text: The poem to score
        poem_type: 'haiku' or 'limerick'
        target_emotion: The target emotion

    Returns:
        (q_bar, sub_scores_dict, served_model_id)
    """
    messages = build_judge_prompt(poem_text, poem_type, target_emotion)

    raw_response, served_model, usage = await judge_poem_groq(
        messages=messages,
        temperature=0.3,
        max_tokens=256,
    )

    sub_scores = _parse_judge_response(raw_response)
    q_bar = compute_q_bar(sub_scores)

    logger.debug(
        f"Q_bar={q_bar:.3f} | sub-scores={sub_scores} | "
        f"judge={served_model} | tokens={usage.get('total_tokens', '?')}"
    )

    return q_bar, sub_scores, served_model


# ── Calibration mode (no emotion_alignment) ─────────────────────────────────

CALIBRATION_DIMENSIONS = [
    "imagery",
    "literary_devices",
    "originality",
    "coherence",
]


def compute_q_bar_calibration(scores: dict[str, int]) -> float:
    """
    Compute Q̄ for calibration — average of 4 dimensions (no emotion),
    normalized to [0, 1].

    Each sub-score is 1-5, so Q̄ = (mean - 1) / 4.
    """
    values = [scores.get(dim, 3) for dim in CALIBRATION_DIMENSIONS]
    mean = sum(values) / len(values)
    q_bar = (mean - 1.0) / 4.0
    return round(q_bar, 4)


async def score_quality_calibration(
    poem_text: str,
    poem_type: str,
) -> tuple[float, dict[str, int], str]:
    """
    Score a poem's quality in calibration mode (no emotion_alignment).

    Uses a 4-dimension judge prompt that omits emotion alignment since
    reference poems have no target emotion.

    Returns:
        (q_bar, sub_scores_dict, served_model_id)
    """
    from src.prompts.judge import build_calibration_judge_prompt

    messages = build_calibration_judge_prompt(poem_text, poem_type)

    raw_response, served_model, usage = await judge_poem_groq(
        messages=messages,
        temperature=0.3,
        max_tokens=256,
    )

    sub_scores = _parse_judge_response(raw_response)
    q_bar = compute_q_bar_calibration(sub_scores)

    logger.debug(
        f"Q_bar(cal)={q_bar:.3f} | sub-scores={sub_scores} | "
        f"judge={served_model} | tokens={usage.get('total_tokens', '?')}"
    )

    return q_bar, sub_scores, served_model
