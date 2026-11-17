"""
Statistical grid runner (Section 8).

Runs poem types × emotions × EAs × replicates, with no human in the loop.
Uses GPT-OSS-120B (Groq) for generation and Qwen3.8-27B (Groq) as judge.

Scenarios
---------
Phase 1 (default): one fixed description per emotion from
    data/prompts/fixed_descriptions.yaml.
Phase 2 (EA_PHASE=2): the six Phase I scenarios, one per poem type × emotion,
    from data/prompts/phase1_scenarios.yaml — the same inputs the Phase I
    interactive runs used. Both EAs always receive the same scenario for a
    cell, so the comparison isolates the algorithm.

Order and resuming
------------------
Replicates are the OUTER loop: replicate 1 of every cell is finished before
replicate 2 starts, so an interrupted grid always holds complete, balanced
sets (every GA run has its NSGA-II partner). Runs already logged as "ok" in
grid_runs.csv are skipped, so the same command can simply be started again
the next day. When a daily API limit is reached the grid stops cleanly.
"""

import logging
import yaml

from src.config import (
    POEM_TYPES, EMOTIONS, EA_TYPES, GRID_RUNS_PER_CELL, DATA_DIR,
    PHASE2, PHASE2_SCENARIOS_PATH, JUDGE_REPEATS, NORMALIZE_APOSTROPHES, LOGS_DIR,
)
from src.ea.ga import run_ga
from src.ea.nsga2 import run_nsga2
from src.ea.common import generate_run_id
from src.api.groq_client import generate_poem_groq
from src.api.client import get_client
from src.config import GPT_OSS_120B, QWEN_27B
from src.logging_.csv_logger import (
    log_all_generations, log_run_summary,
    log_grid_run, log_grid_candidates, count_completed_grid_runs,
)

logger = logging.getLogger(__name__)

# Fixed descriptions per emotion (Section 5) — Phase 1 grid
FIXED_DESCRIPTIONS_PATH = DATA_DIR / "prompts" / "fixed_descriptions.yaml"


def load_fixed_descriptions() -> dict[str, str]:
    """
    Load the pre-written descriptions for each emotion (Phase 1 grid).

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


def load_phase2_scenarios() -> dict[str, dict[str, str]]:
    """Load the six Phase I scenarios: {poem_type: {emotion: description}}."""
    if not PHASE2_SCENARIOS_PATH.exists():
        raise FileNotFoundError(
            f"Phase 2 scenarios file not found: {PHASE2_SCENARIOS_PATH}"
        )
    with open(PHASE2_SCENARIOS_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_description(poem_type: str, emotion: str) -> str:
    """
    Return the scenario for one cell. Emotion lookup is case-insensitive
    (config uses "Joy", the YAML files use "joy").

    In Phase 2 a missing scenario is an error — the grid must never fall
    back silently to a made-up description.
    """
    key = emotion.lower()
    if PHASE2:
        scenarios = load_phase2_scenarios()
        try:
            return scenarios[poem_type][key]
        except KeyError:
            raise KeyError(
                f"No Phase 2 scenario for poem_type='{poem_type}', emotion='{emotion}' "
                f"in {PHASE2_SCENARIOS_PATH}"
            )
    descriptions = load_fixed_descriptions()
    lowered = {str(k).lower(): v for k, v in descriptions.items()}
    return lowered.get(key, f"a scene evoking {emotion}")


def _log_usage() -> None:
    for model in [GPT_OSS_120B, QWEN_27B]:
        logger.info(get_client(model).daily_usage_summary)


async def run_grid(
    poem_types: list[str] | None = None,
    emotions: list[str] | None = None,
    ea_types: list[str] | None = None,
    runs_per_cell: int | None = None,
) -> list[dict]:
    """
    Run the statistical grid.

    Args:
        poem_types: Override POEM_TYPES (default: ['haiku', 'limerick'])
        emotions: Override EMOTIONS (default: config.EMOTIONS)
        ea_types: Override EA_TYPES (default: ['ga', 'nsga2'])
        runs_per_cell: replicates per cell (default: GRID_RUNS_PER_CELL)

    Returns:
        List of result dicts for the runs executed in THIS invocation.
    """
    poem_types = poem_types or POEM_TYPES
    emotions = emotions or EMOTIONS
    ea_types = ea_types or EA_TYPES
    runs = runs_per_cell or GRID_RUNS_PER_CELL

    # Resolve every scenario up front so a missing one fails before any API call.
    scenario = {(pt, em): get_description(pt, em) for pt in poem_types for em in emotions}

    total_runs = len(poem_types) * len(emotions) * len(ea_types) * runs
    done = count_completed_grid_runs()
    already = sum(
        min(done.get((ea, pt, em.lower()), 0), runs)
        for pt in poem_types for em in emotions for ea in ea_types
    )

    logger.info(
        f"═══ GRID RUN: {len(poem_types)} types × {len(emotions)} emotions × "
        f"{len(ea_types)} EAs × {runs} replicates = {total_runs} runs "
        f"({already} already done, {total_runs - already} to do) ═══"
    )
    logger.info(
        f"  Phase={'2' if PHASE2 else '1'} | judge readings per poem={JUDGE_REPEATS} | "
        f"apostrophe normalisation={'on' if NORMALIZE_APOSTROPHES else 'off'} | logs={LOGS_DIR}"
    )
    for (pt, em), text in scenario.items():
        logger.info(f"  Scenario [{pt} | {em}]: {text}")

    _log_usage()

    results: list[dict] = []
    position = 0
    stop_reason = None

    for replicate in range(1, runs + 1):
        for poem_type in poem_types:
            for emotion in emotions:
                description = scenario[(poem_type, emotion)]

                for ea_type in ea_types:
                    position += 1
                    cell = (ea_type, poem_type, emotion.lower())

                    if done.get(cell, 0) >= replicate:
                        continue          # this replicate of this cell is already logged

                    ea_runner = run_ga if ea_type == "ga" else run_nsga2
                    run_id = generate_run_id(ea_type, poem_type, emotion)

                    logger.info(
                        f"\n{'─'*60}\n"
                        f"Grid run [{position}/{total_runs}]: "
                        f"{poem_type} | {emotion} | {ea_type} | replicate {replicate}/{runs}\n"
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
                    except RuntimeError as e:
                        msg = str(e)
                        logger.error(f"Run {run_id} failed: {msg}")
                        log_grid_run(
                            run_id=run_id, replicate=replicate, ea=ea_type,
                            poem_type=poem_type, emotion=emotion,
                            description=description, status="failed", error=msg,
                        )
                        results.append({
                            "run_id": run_id, "ea": ea_type, "poem_type": poem_type,
                            "emotion": emotion, "replicate": replicate,
                            "final_F": None, "error": msg,
                        })
                        if ("Daily" in msg and "limit" in msg) or "attempts failed" in msg:
                            stop_reason = msg
                            break
                        continue

                    best = result.best_poem

                    # Standard CSVs (same format as Phase I)
                    log_all_generations(result.generation_logs)
                    log_run_summary(
                        run_id=result.run_id,
                        ea=ea_type,
                        poem_type=poem_type,
                        emotion=emotion,
                        final_f=best.F,
                        generations_used=result.generations_used,
                        best_poem=best.text,
                    )
                    # Grid CSVs: one row per run, and every candidate that was scored
                    log_grid_run(
                        run_id=result.run_id, replicate=replicate, ea=ea_type,
                        poem_type=poem_type, emotion=emotion, description=description,
                        status="ok", best_poem=best,
                        generations_used=result.generations_used,
                        n_candidates=len(result.all_poems),
                    )
                    log_grid_candidates(
                        run_id=result.run_id, ea=ea_type, poem_type=poem_type,
                        emotion=emotion, all_poems=result.all_poems,
                        best_poem_id=best.poem_id,
                    )
                    done[cell] = done.get(cell, 0) + 1

                    results.append({
                        "run_id": result.run_id,
                        "ea": ea_type,
                        "poem_type": poem_type,
                        "emotion": emotion,
                        "replicate": replicate,
                        "final_F": best.F,
                        "Q_bar": best.Q_bar,
                        "Rhyme": best.Rhyme,
                        "Structure": best.Structure,
                        "generations_used": result.generations_used,
                        "best_poem": best.text,
                    })

                    _log_usage()

                if stop_reason:
                    break
            if stop_reason:
                break
        if stop_reason:
            break

    if stop_reason:
        logger.warning(
            f"═══ GRID STOPPED EARLY: {stop_reason}. "
            f"Run the same command again later to continue — finished runs are skipped. ═══"
        )
    else:
        logger.info(f"═══ GRID COMPLETE: {len(results)} runs executed this session ═══")

    return results
