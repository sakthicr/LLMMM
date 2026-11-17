"""
LLM-based mutation operator.

Each generation, the current elite produces `mutations_per_generation`
variants via the Generator model, prompted to preserve core theme/imagery
while revising rhyme/emotion/word choice.

No crossover — matches the base paper's own validated design.
"""

import logging
from typing import Callable, Awaitable

from src.config import EA_PARAMS
from src.ea.common import Poem
from src.prompts.generator import build_generation_prompt, build_mutation_prompt, parse_multiple_poems
from src.logging_.csv_logger import log_raw_generator

logger = logging.getLogger(__name__)

# Type for a generator function: takes messages, returns (content, model, usage)
GeneratorFunc = Callable[
    [list[dict[str, str]], float, int | None],
    Awaitable[tuple[str, str, dict]]
]


async def generate_initial_population(
    poem_type: str,
    emotion: str,
    description: str,
    generator_fn: GeneratorFunc,
    population_size: int | None = None,
    run_id: str | None = None,
) -> list[Poem]:
    """
    Generate the initial population of poem candidates.

    Makes multiple API calls if needed to reach the target population size.
    Each call asks for multiple poems to reduce API overhead.
    Enforces a strict safety cap of 6 batches per population to prevent
    infinite loops, and guarantees exactly target poems are produced.
    """
    target = population_size or EA_PARAMS.population_size
    poems = []

    # Generate in batches of 5 (reasonable for a single prompt)
    batch_size = min(5, target)
    max_batches = 6
    batch_count = 0

    while len(poems) < target:
        batch_count += 1
        if batch_count > max_batches:
            raise RuntimeError(
                f"Failed to generate initial population: reached safety cap of {max_batches} "
                f"generator batches, but only obtained {len(poems)}/{target} valid poems."
            )

        remaining = target - len(poems)
        count = min(batch_size, remaining)

        messages = build_generation_prompt(poem_type, emotion, description, count)
        raw_output, served_model, usage = await generator_fn(
            messages, 0.9, None  # Higher temperature for diversity
        )

        log_raw_generator(
            run_id=run_id or "unknown",
            call_type=f"initial_population_batch_{batch_count}",
            raw_text=raw_output,
        )

        new_poems = parse_multiple_poems(
            raw_output,
            poem_type=poem_type,
            expected_count=count,
        )
        for text in new_poems:
            if len(poems) >= target:
                break
            poem = Poem(
                text=text,
                poem_type=poem_type,
                emotion=emotion,
                description=description,
                generation=0,
                generator_model=served_model,
            )
            poems.append(poem)
            logger.debug(f"Generated initial poem: {poem.poem_id}")

    if len(poems) < target:
        raise RuntimeError(
            f"Failed to obtain required population size: {len(poems)}/{target} poems."
        )

    logger.info(
        f"Initial population: {len(poems)} {poem_type}s | "
        f"emotion={emotion} | model={poems[0].generator_model if poems else 'N/A'}"
    )
    return poems


async def mutate_poem(
    elite: Poem,
    poem_type: str,
    emotion: str,
    description: str,
    generator_fn: GeneratorFunc,
    count: int | None = None,
    run_id: str | None = None,
) -> list[Poem]:
    """
    Generate mutated variants of the elite poem.

    Asks the LLM to produce `count` revisions of the elite,
    preserving core theme/imagery while varying phrasing/rhyme/emotion.
    """
    target_count = count or EA_PARAMS.mutations_per_generation

    messages = build_mutation_prompt(
        poem_text=elite.text,
        poem_type=poem_type,
        emotion=emotion,
        description=description,
        count=target_count,
    )

    max_attempts = 3
    variants = []
    served_model = "unknown"

    for attempt in range(1, max_attempts + 1):
        raw_output, served_model, usage = await generator_fn(
            messages, 0.8, None
        )

        log_raw_generator(
            run_id=run_id or "unknown",
            call_type="mutation",
            raw_text=raw_output,
        )

        new_poems_text = parse_multiple_poems(
            raw_output,
            poem_type=poem_type,
            expected_count=target_count,
        )
        variants = [
            Poem(
                text=text,
                poem_type=poem_type,
                emotion=emotion,
                description=description,
                generator_model=served_model,
            )
            for text in new_poems_text[:target_count]
        ]

        if len(variants) > 0:
            if attempt > 1:
                logger.info(
                    f"Mutation succeeded on attempt {attempt}/{max_attempts} with {len(variants)} variants."
                )
            break

        if attempt < max_attempts:
            logger.warning(
                f"Mutation returned 0 valid variants (attempt {attempt}/{max_attempts}). Retrying..."
            )
        else:
            logger.error(
                f"Mutation FAILED after {max_attempts} attempts: 0 valid variants obtained."
            )

    logger.info(
        f"Mutated elite {elite.poem_id} → {len(variants)} variants | "
        f"model={served_model}"
    )
    return variants
