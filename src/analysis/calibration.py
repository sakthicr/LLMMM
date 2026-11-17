"""
Human-poem calibration (Section 10).

Before trusting F on generated poems, run the same Structure + Q_bar pipeline
on ~15 real human haikus and ~15 real human limericks and confirm scores
look sane.

Calibration mode uses a 4-dimension Q_bar (imagery, literary_devices,
originality, coherence) — omitting emotion_alignment since reference
poems have no target emotion.

Also includes negative controls: deliberately weak poems to ensure
the scoring separates quality tiers.
"""

import asyncio
import logging
import statistics

from src.fitness.fitness import evaluate_poem_calibration
from src.api.client import get_client
from src.config import DATA_DIR, QWEN_27B

logger = logging.getLogger(__name__)

HAIKU_REFERENCE = DATA_DIR / "calibration" / "haiku_reference.txt"
LIMERICK_REFERENCE = DATA_DIR / "calibration" / "limerick_reference.txt"
HAIKU_NEGATIVE = DATA_DIR / "calibration" / "haiku_negative.txt"
LIMERICK_NEGATIVE = DATA_DIR / "calibration" / "limerick_negative.txt"


def _load_reference_poems(path, poem_type: str) -> list[dict]:
    """
    Load reference poems from a file.

    Expected format: poems separated by blank lines.
    Lines starting with # are metadata (title/author) — stored but
    not included in the poem text for scoring.
    """
    if not path.exists():
        logger.warning(f"Reference file not found: {path}")
        return []

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split on double newlines
    raw_poems = content.strip().split("\n\n")
    poems = []

    for raw in raw_poems:
        lines = raw.strip().split("\n")
        metadata_lines = [l for l in lines if l.startswith("#")]
        poem_lines = [l for l in lines if not l.startswith("#")]
        poem_text = "\n".join(poem_lines).strip()

        if poem_text:
            # Extract title/author from metadata
            title = ""
            for ml in metadata_lines:
                title = ml.lstrip("# ").strip()
                break

            poems.append({
                "title": title,
                "text": poem_text,
                "poem_type": poem_type,
            })

    return poems


def _get_token_usage() -> dict:
    """Get current cumulative token usage from the judge model client."""
    client = get_client(QWEN_27B)
    return {
        "requests_today": client.usage.requests_today,
        "tokens_today": client.usage.tokens_today,
        "prompt_tokens_today": client.usage.prompt_tokens_today,
        "completion_tokens_today": client.usage.completion_tokens_today,
    }


async def run_calibration(
    target_emotion: str = "joy",
) -> dict:
    """
    Run the calibration check on reference poems.

    Uses calibration-mode Q_bar (4 dimensions, no emotion_alignment)
    since reference poems have no target emotion.

    Also runs negative controls if available, and reports token usage.

    Args:
        target_emotion: Ignored in calibration mode (kept for CLI compat).
    """
    logger.info("=== CALIBRATION RUN ===")

    # Snapshot token usage before calibration
    pre_usage = _get_token_usage()

    results = {"haiku": [], "limerick": []}
    negative_results = {"haiku": [], "limerick": []}

    # ── Reference haikus ──
    haiku_refs = _load_reference_poems(HAIKU_REFERENCE, "haiku")
    logger.info(f"Loaded {len(haiku_refs)} reference haikus")

    for ref in haiku_refs:
        scores = await evaluate_poem_calibration(ref["text"], "haiku")
        results["haiku"].append({
            "title": ref["title"],
            "text": ref["text"],
            **scores,
        })
        logger.info(
            f"  Haiku '{ref['title']}': F={scores['F']:.3f} "
            f"(Q_bar={scores['Q_bar']:.3f}, R={scores['Rhyme']:.3f}, S={scores['Structure']:.3f})"
        )

    # ── Reference limericks ──
    limerick_refs = _load_reference_poems(LIMERICK_REFERENCE, "limerick")
    logger.info(f"Loaded {len(limerick_refs)} reference limericks")

    for ref in limerick_refs:
        scores = await evaluate_poem_calibration(ref["text"], "limerick")
        results["limerick"].append({
            "title": ref["title"],
            "text": ref["text"],
            **scores,
        })
        logger.info(
            f"  Limerick '{ref['title']}': F={scores['F']:.3f} "
            f"(Q_bar={scores['Q_bar']:.3f}, R={scores['Rhyme']:.3f}, S={scores['Structure']:.3f})"
        )

    # ── Negative controls ──
    for poem_type, neg_path in [("haiku", HAIKU_NEGATIVE), ("limerick", LIMERICK_NEGATIVE)]:
        neg_refs = _load_reference_poems(neg_path, poem_type)
        if neg_refs:
            logger.info(f"Loaded {len(neg_refs)} negative-control {poem_type}s")
            for ref in neg_refs:
                scores = await evaluate_poem_calibration(ref["text"], poem_type)
                negative_results[poem_type].append({
                    "title": ref["title"],
                    "text": ref["text"],
                    **scores,
                })
                logger.info(
                    f"  NEG {poem_type} '{ref['title']}': F={scores['F']:.3f} "
                    f"(Q_bar={scores['Q_bar']:.3f}, R={scores['Rhyme']:.3f}, S={scores['Structure']:.3f})"
                )

    # ── Summary statistics ──
    for poem_type, items in results.items():
        if items:
            f_scores = [item["F"] for item in items]
            f_std = statistics.stdev(f_scores) if len(f_scores) > 1 else 0.0
            logger.info(
                f"  {poem_type.capitalize()} reference: "
                f"n={len(items)}, "
                f"F mean={statistics.mean(f_scores):.3f}, "
                f"F std={f_std:.3f}, "
                f"F range=[{min(f_scores):.3f}, {max(f_scores):.3f}]"
            )

        neg_items = negative_results.get(poem_type, [])
        if neg_items:
            neg_f = [item["F"] for item in neg_items]
            neg_std = statistics.stdev(neg_f) if len(neg_f) > 1 else 0.0
            logger.info(
                f"  {poem_type.capitalize()} negative:  "
                f"n={len(neg_items)}, "
                f"F mean={statistics.mean(neg_f):.3f}, "
                f"F std={neg_std:.3f}, "
                f"F range=[{min(neg_f):.3f}, {max(neg_f):.3f}]"
            )

    # ── Token usage report ──
    post_usage = _get_token_usage()
    total_requests = post_usage["requests_today"] - pre_usage["requests_today"]
    total_tokens = post_usage["tokens_today"] - pre_usage["tokens_today"]
    prompt_tokens = post_usage["prompt_tokens_today"] - pre_usage["prompt_tokens_today"]
    completion_tokens = post_usage["completion_tokens_today"] - pre_usage["completion_tokens_today"]
    avg_tokens = total_tokens / total_requests if total_requests > 0 else 0

    logger.info(
        f"  Token usage: {total_requests} judge calls, "
        f"{total_tokens} total tokens "
        f"(prompt={prompt_tokens}, completion={completion_tokens}), "
        f"{avg_tokens:.0f} avg tokens/call"
    )

    logger.info("=== CALIBRATION COMPLETE ===")

    return {
        "results": results,
        "negative_results": negative_results,
        "token_usage": {
            "total_requests": total_requests,
            "total_tokens": total_tokens,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "avg_tokens_per_call": round(avg_tokens, 1),
        },
    }
