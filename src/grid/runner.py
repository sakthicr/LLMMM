"""
Statistical grid runner (Section 8).

Runs 2 poem types × 5 emotions × 2 EAs × 5 runs = 100 total runs.

Uses GPT-OSS-120B (Groq) for bulk generation.
Same fixed description per emotion across all 5 runs per cell —
isolates algorithm variance, not prompt variance.
"""

import asyncio
import logging
import yaml
from pathlib import Path

from src.config import (
    POEM_TYPES, EMOTIONS, EA_TYPES, GRID_RUNS_PER_CELL, DATA_DIR
)
from src.ea.ga import run_ga
from src.ea.nsga2 import run_nsga2
from src.ea.common import generate_run_id
from src.api.groq_client import generate_poem_groq
from src.api.client import get_client, close_all_clients
from src.config import GPT_OSS_120B, QWEN_27B
from src.logging_.csv_logger import log_all_generations, log_run_summary

logger = logging.getLogger(__name__)

# Fixed descriptions per emotion (Section 5)
FIXED_DESCRIPTIONS_PATH = DATA_DIR / "prompts" / "fixed_descriptions.yaml"


def load_fixed_descriptions() -> dict[str, str]:
    """
    Load the pre-written descriptions for each emotion.

    These are authored by the researcher (not auto-generated),
    one per emotion, in casual style matching live typing.
    """
    if not FIXED_DESCRIPTIONS_PATH.exists():
        logger.warning(
            f"Fixed descriptions file not found at {FIXED_DESCRIPTIONS_PATH}. "
            f"Using fallback descriptions."
        )
        return {
            "joy": "a child's laughter echoing through a sunlit garden",
            "sorrow": "rain falling on an empty bench in autumn",
            "fear": "shadows moving at the edge of a dark forest",
            "anger": "a turbulent ocean crashing against jagged cliffs",
            "love": "two old hands intertwined on a quiet evening",
        }

    with open(FIXED_DESCRIPTIONS_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


async def run_grid(
    poem_types: list[str] | None = None,
    emotions: list[str] | None = None,
    ea_types: list[str] | None = None,
    runs_per_cell: int | None = None,
) -> list[dict]:
    """
    Run the full statistical grid.

    Args:
        poem_types: Override POEM_TYPES (default: ['haiku', 'limerick'])
        emotions: Override EMOTIONS (default: all 5)
        ea_types: Override EA_TYPES (default: ['ga', 'nsga2'])
        runs_per_cell: Override GRID_RUNS_PER_CELL (default: 5)

    Returns:
        List of result dicts for downstream analysis.
    """
    poem_types = poem_types or POEM_TYPES
    emotions = emotions or EMOTIONS
    ea_types = ea_types or EA_TYPES
    runs = runs_per_cell or GRID_RUNS_PER_CELL

    descriptions = load_fixed_descriptions()

    total_cells = len(poem_types) * len(emotions) * len(ea_types) * runs
    logger.info(
        f"═══ GRID RUN: {len(poem_types)} types × {len(emotions)} emotions × "
        f"{len(ea_types)} EAs × {runs} runs = {total_cells} total runs ═══"
    )

    # Pre-flight: log current API usage
    for model in [GPT_OSS_120B, QWEN_27B]:
        client = get_client(model)
        logger.info(client.daily_usage_summary)

    results = []
    completed = 0

    for poem_type in poem_types:
        for emotion in emotions:
            description = descriptions.get(emotion, f"a scene evoking {emotion}")

            for ea_type in ea_types:
                ea_runner = run_ga if ea_type == "ga" else run_nsga2

                for run_num in range(1, runs + 1):
                    run_id = generate_run_id(ea_type, poem_type, emotion)
                    completed += 1

                    logger.info(
                        f"\n{'─'*60}\n"
                        f"Grid cell [{completed}/{total_cells}]: "
                        f"{poem_type} | {emotion} | {ea_type} | run {run_num}/{runs}\n"
                        f"Run ID: {run_id}\n"
                        f"{'─'*60}"
                    )

                    try:
                        result = await ea_runner(
                            poem_type=poem_type,
                            emotion=emotion,
                            description=description,
                            generator_fn=generate_poem_groq,
                            run_id=run_id,
                        )

                        # Log to CSVs
                        log_all_generations(result.generation_logs)
                        log_run_summary(
                            run_id=result.run_id,
                            ea=ea_type,
                            poem_type=poem_type,
                            emotion=emotion,
                            final_f=result.best_poem.F,
                            generations_used=result.generations_used,
                            best_poem=result.best_poem.text,
                        )

                        results.append({
                            "run_id": result.run_id,
                            "ea": ea_type,
                            "poem_type": poem_type,
                            "emotion": emotion,
                            "final_F": result.best_poem.F,
                            "Q_bar": result.best_poem.Q_bar,
                            "Rhyme": result.best_poem.Rhyme,
                            "Structure": result.best_poem.Structure,
                            "generations_used": result.generations_used,
                            "best_poem": result.best_poem.text,
                        })

                        # Log usage after each run
                        for model in [GPT_OSS_120B, QWEN_27B]:
                            client = get_client(model)
                            logger.info(client.daily_usage_summary)

                    except RuntimeError as e:
                        logger.error(
                            f"Run {run_id} failed: {e}. "
                            f"This may be a rate limit — consider pausing."
                        )
                        results.append({
                            "run_id": run_id,
                            "ea": ea_type,
                            "poem_type": poem_type,
                            "emotion": emotion,
                            "final_F": None,
                            "error": str(e),
                        })

    logger.info(f"═══ GRID COMPLETE: {len(results)} runs ═══")
    return results
