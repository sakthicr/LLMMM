"""
NSGA-II (Non-dominated Sorting Genetic Algorithm II).

The one true difference from GA:
- Non-dominated sorting + crowding distance on TWO objectives: [Q̄, Rhyme]
- Structure is a hard constraint (reject/penalize violations), NOT a third objective
- After Pareto ranking, the elite for mutation is picked by rank → crowding distance
- F is computed identically to GA but used ONLY for the final comparison table,
  never for search/selection during evolution

Shared mechanics (identical to GA):
- Population: 10, mutation only (5 variants), elitism, same stopping rule
"""

import logging
import math
from typing import Callable, Awaitable

from src.config import EA_PARAMS
from src.ea.common import Poem, GenerationLog, RunResult, generate_run_id, check_stopping_rule
from src.ea.mutation import generate_initial_population, mutate_poem, GeneratorFunc
from src.fitness.fitness import evaluate_poem, compute_fitness_from_components

logger = logging.getLogger(__name__)

# ── Structure penalty threshold ──────────────────────────────────────────────
# Poems with Structure < this threshold are penalized during NSGA-II selection
# (treated as constraint-violating solutions)
STRUCTURE_PENALTY_THRESHOLD = 0.3


def _dominates(a: Poem, b: Poem) -> bool:
    """
    Check if poem `a` dominates poem `b` on the two objectives [Q̄, Rhyme].

    `a` dominates `b` iff:
    - a is >= b on ALL objectives, AND
    - a is strictly > b on AT LEAST ONE objective
    """
    objs_a = (a.Q_bar, a.Rhyme)
    objs_b = (b.Q_bar, b.Rhyme)

    at_least_one_better = False
    for va, vb in zip(objs_a, objs_b):
        if va < vb:
            return False
        if va > vb:
            at_least_one_better = True

    return at_least_one_better


def non_dominated_sort(population: list[Poem]) -> list[list[Poem]]:
    """
    Fast non-dominated sorting (Deb et al. 2002).

    Separates the population into Pareto fronts.
    Front 0 = non-dominated set, Front 1 = dominated only by Front 0, etc.
    """
    n = len(population)
    domination_count = [0] * n   # how many solutions dominate solution i
    dominated_set = [[] for _ in range(n)]  # solutions dominated by solution i
    fronts = [[]]

    for i in range(n):
        for j in range(i + 1, n):
            if _dominates(population[i], population[j]):
                dominated_set[i].append(j)
                domination_count[j] += 1
            elif _dominates(population[j], population[i]):
                dominated_set[j].append(i)
                domination_count[i] += 1

    # Build front 0 (non-dominated)
    for i in range(n):
        if domination_count[i] == 0:
            population[i].rank = 0
            fronts[0].append(population[i])

    # Build subsequent fronts
    front_idx = 0
    while fronts[front_idx]:
        next_front = []
        for poem in fronts[front_idx]:
            i = population.index(poem)
            for j in dominated_set[i]:
                domination_count[j] -= 1
                if domination_count[j] == 0:
                    population[j].rank = front_idx + 1
                    next_front.append(population[j])
        front_idx += 1
        fronts.append(next_front)

    # Remove trailing empty front
    if not fronts[-1]:
        fronts.pop()

    return fronts


def compute_crowding_distance(front: list[Poem]) -> None:
    """
    Compute crowding distance for each solution in a Pareto front.

    Crowding distance measures how isolated a solution is in objective space.
    Solutions at the boundary get infinite distance (always selected).
    """
    n = len(front)
    if n <= 2:
        for poem in front:
            poem.crowding_distance = float('inf')
        return

    for poem in front:
        poem.crowding_distance = 0.0

    # For each objective: [Q̄, Rhyme]
    for obj_fn in [lambda p: p.Q_bar, lambda p: p.Rhyme]:
        front.sort(key=obj_fn)

        # Boundary solutions get infinite distance
        front[0].crowding_distance = float('inf')
        front[-1].crowding_distance = float('inf')

        obj_min = obj_fn(front[0])
        obj_max = obj_fn(front[-1])
        obj_range = obj_max - obj_min

        if obj_range == 0:
            continue

        for i in range(1, n - 1):
            front[i].crowding_distance += (
                (obj_fn(front[i + 1]) - obj_fn(front[i - 1])) / obj_range
            )


def nsga2_select_elite(population: list[Poem]) -> Poem:
    """
    Select the elite individual using NSGA-II ranking:
    1. Non-dominated sort
    2. Crowding distance within each front
    3. Best = lowest rank, then highest crowding distance

    This is used to pick the parent for mutation.
    """
    # Apply structure constraint: penalize violators
    feasible = []
    infeasible = []
    for poem in population:
        if poem.Structure >= STRUCTURE_PENALTY_THRESHOLD:
            feasible.append(poem)
        else:
            infeasible.append(poem)

    # If all are infeasible, work with what we have
    candidates = feasible if feasible else infeasible

    fronts = non_dominated_sort(candidates)
    for front in fronts:
        compute_crowding_distance(front)

    # Sort: rank ascending, then crowding distance descending
    candidates.sort(key=lambda p: (p.rank, -p.crowding_distance))
    return candidates[0]


async def run_nsga2(
    poem_type: str,
    emotion: str,
    description: str,
    generator_fn: GeneratorFunc,
    run_id: str | None = None,
) -> RunResult:
    """
    Run the full NSGA-II process:
    1. Generate initial population
    2. Evaluate fitness for all candidates
    3. Non-dominated sort + crowding distance on [Q̄, Rhyme]
    4. Select elite via NSGA-II ranking (not by F)
    5. Mutate elite → new variants
    6. Evaluate variants, merge with elite
    7. Repeat until stopping rule triggers

    F is computed identically to GA for the final comparison table,
    but is NEVER used for selection during evolution.
    """
    if run_id is None:
        run_id = generate_run_id("nsga2", poem_type, emotion)

    logger.info(f"═══ NSGA-II RUN {run_id} ═══")
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

    # ── Step 3: NSGA-II selection for elite ──
    elite = nsga2_select_elite(population)

    # Track best-F seen so far (for stopping rule + final comparison)
    best_f_poem = max(population, key=lambda p: p.F)

    generation_logs = []
    all_poems = list(population)

    # Log generation 0
    gen_log = GenerationLog(
        run_id=run_id,
        ea="nsga2",
        poem_type=poem_type,
        emotion=emotion,
        generation=0,
        F=best_f_poem.F,
        Q_bar=best_f_poem.Q_bar,
        Rhyme=best_f_poem.Rhyme,
        Structure=best_f_poem.Structure,
        best_poem=best_f_poem.text,
    )
    generation_logs.append(gen_log)
    logger.info(
        f"  Gen 0 | NSGA-II elite: {elite} (rank={elite.rank}) | "
        f"Best-F: {best_f_poem.F:.3f}"
    )

    final_pool = list(population)

    # ── Steps 4-7: Evolutionary loop ──
    for gen in range(1, EA_PARAMS.max_generations + 1):
        if check_stopping_rule(generation_logs, gen):
            break

        # Mutate the NSGA-II selected elite (NOT the best-F poem)
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

        # Merge: elite + variants form the candidate pool
        candidates = [elite] + variants
        final_pool = list(candidates)

        # NSGA-II selection on merged pool
        elite = nsga2_select_elite(candidates)

        # Update best-F tracker (for logging and stopping rule)
        for poem in variants:
            if poem.F > best_f_poem.F:
                best_f_poem = poem

        # Log this generation
        gen_log = GenerationLog(
            run_id=run_id,
            ea="nsga2",
            poem_type=poem_type,
            emotion=emotion,
            generation=gen,
            F=best_f_poem.F,
            Q_bar=best_f_poem.Q_bar,
            Rhyme=best_f_poem.Rhyme,
            Structure=best_f_poem.Structure,
            best_poem=best_f_poem.text,
        )
        generation_logs.append(gen_log)
        logger.info(
            f"  Gen {gen} | NSGA-II elite: {elite} (rank={elite.rank}) | "
            f"Best-F: {best_f_poem.F:.3f}"
        )

    # Per project spec: present highest-F poem from Front 0 (Rank 0) of the FINAL generation's candidate pool
    feasible_final = [p for p in final_pool if p.Structure >= STRUCTURE_PENALTY_THRESHOLD]
    front_candidates = feasible_final if feasible_final else final_pool
    fronts = non_dominated_sort(front_candidates)
    front_0 = fronts[0] if fronts else [elite]
    winning_poem = max(front_0, key=lambda p: p.F)

    front_0_str = ", ".join(f"{p.poem_id} (F={p.F:.3f}, Q̄={p.Q_bar:.3f}, R={p.Rhyme:.3f})" for p in front_0)
    logger.info(f"  Final pool Front 0 members: [{front_0_str}]")
    logger.info(
        f"  Final presentation: selected highest-F poem from Front 0 -> "
        f"{winning_poem.poem_id} (F={winning_poem.F:.3f})"
    )

    logger.info(
        f"═══ NSGA-II COMPLETE {run_id} ═══ "
        f"Generations: {len(generation_logs)} | Final F={winning_poem.F:.3f}"
    )

    return RunResult(
        run_id=run_id,
        ea="nsga2",
        poem_type=poem_type,
        emotion=emotion,
        description=description,
        best_poem=winning_poem,
        generations_used=len(generation_logs),
        generation_logs=generation_logs,
        all_poems=all_poems,
    )
