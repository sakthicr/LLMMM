"""
Single-objective Genetic Algorithm (GA).

Ranks and selects using the scalar composite fitness F directly.
This is the "simpler" baseline — it lacks NSGA-II's multi-objective
Pareto handling, isolating that as the single design variable under test.

Shared mechanics (identical to NSGA-II):
- Population: 10 initial candidates
- Variation: mutation only (5 variants from elite per generation)
- Elitism: single best-F poem carries forward unchanged
- Stopping: ΔF < 0.01 for 2 consecutive generations, or generation 10
"""

import logging
from typing import Callable, Awaitable

from src.config import EA_PARAMS
from src.ea.common import Poem, GenerationLog, RunResult, generate_run_id, check_stopping_rule
from src.ea.mutation import generate_initial_population, mutate_poem, GeneratorFunc
from src.fitness.fitness import evaluate_poem

logger = logging.getLogger(__name__)


async def run_ga(
    poem_type: str,
    emotion: str,
    description: str,
    generator_fn: GeneratorFunc,
    run_id: str | None = None,
) -> RunResult:
    """
    Run the full GA process:
    1. Generate initial population
    2. Evaluate fitness for all candidates
    3. Select elite (best F)
    4. Mutate elite → new variants
    5. Evaluate variants, merge with elite
    6. Repeat until stopping rule triggers

    Returns a RunResult with the best poem and full generation logs.
    """
    if run_id is None:
        run_id = generate_run_id("ga", poem_type, emotion)

    logger.info(f"═══ GA RUN {run_id} ═══")
    logger.info(f"  Poem type: {poem_type} | Emotion: {emotion}")

    # ── Step 1: Generate initial population ──
    population = await generate_initial_population(
        poem_type, emotion, description, generator_fn, run_id=run_id
    )

    # ── Step 2: Evaluate initial population ──
    for poem in population:
        result = await evaluate_poem(poem.text, poem_type, emotion)
        poem.F = result["F"]
        poem.Q_bar = result["Q_bar"]
        poem.Rhyme = result["Rhyme"]
        poem.Structure = result["Structure"]
        poem.sub_scores = result["sub_scores"]
        poem.judge_model = result["judge_model"]
        poem.generation = 0
        logger.info(
            f"  Candidate evaluated | id={poem.poem_id} | gen=0 | "
            f"F={poem.F:.3f} (Q_bar={poem.Q_bar:.3f}, R={poem.Rhyme:.3f}, S={poem.Structure:.3f})"
        )

    # Sort by F descending — GA's core mechanism
    population.sort(key=lambda p: p.F, reverse=True)
    elite = population[0]

    generation_logs = []
    all_poems = list(population)

    # Log generation 0
    gen_log = GenerationLog(
        run_id=run_id,
        ea="ga",
        poem_type=poem_type,
        emotion=emotion,
        generation=0,
        F=elite.F,
        Q_bar=elite.Q_bar,
        Rhyme=elite.Rhyme,
        Structure=elite.Structure,
        best_poem=elite.text,
    )
    generation_logs.append(gen_log)
    logger.info(f"  Gen 0 | Best F={elite.F:.3f} | {elite}")

    # ── Steps 3-6: Evolutionary loop ──
    for gen in range(1, EA_PARAMS.max_generations + 1):
        # Check stopping rule
        if check_stopping_rule(generation_logs, gen):
            break

        # Mutate the elite
        variants = await mutate_poem(
            elite, poem_type, emotion, description, generator_fn, run_id=run_id
        )

        if len(variants) == 0:
            logger.warning(
                f"  Gen {gen} FAILED (0 variants) — generation not counted toward stopping rule."
            )
            continue

        # Evaluate variants
        for poem in variants:
            result = await evaluate_poem(poem.text, poem_type, emotion)
            poem.F = result["F"]
            poem.Q_bar = result["Q_bar"]
            poem.Rhyme = result["Rhyme"]
            poem.Structure = result["Structure"]
            poem.sub_scores = result["sub_scores"]
            poem.judge_model = result["judge_model"]
            poem.generation = gen
            logger.info(
                f"  Candidate evaluated | id={poem.poem_id} | gen={gen} | "
                f"F={poem.F:.3f} (Q_bar={poem.Q_bar:.3f}, R={poem.Rhyme:.3f}, S={poem.Structure:.3f})"
            )

        all_poems.extend(variants)

        # Elitism: keep the current elite, add variants, pick new best
        candidates = [elite] + variants
        candidates.sort(key=lambda p: p.F, reverse=True)
        elite = candidates[0]

        # Log this generation
        gen_log = GenerationLog(
            run_id=run_id,
            ea="ga",
            poem_type=poem_type,
            emotion=emotion,
            generation=gen,
            F=elite.F,
            Q_bar=elite.Q_bar,
            Rhyme=elite.Rhyme,
            Structure=elite.Structure,
            best_poem=elite.text,
        )
        generation_logs.append(gen_log)
        logger.info(f"  Gen {gen} | Best F={elite.F:.3f} | {elite}")

    logger.info(
        f"  Final presentation: selected elite -> "
        f"{elite.poem_id} (F={elite.F:.3f})"
    )

    logger.info(
        f"═══ GA COMPLETE {run_id} ═══ "
        f"Generations: {len(generation_logs)} | Final F={elite.F:.3f}"
    )

    return RunResult(
        run_id=run_id,
        ea="ga",
        poem_type=poem_type,
        emotion=emotion,
        description=description,
        best_poem=elite,
        generations_used=len(generation_logs),
        generation_logs=generation_logs,
        all_poems=all_poems,
    )
