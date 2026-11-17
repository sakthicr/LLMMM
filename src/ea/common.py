"""
Shared EA dataclasses, population initialization, and stopping rule.

Both GA and NSGA-II use these common components to ensure the only
difference between them is the selection mechanism.
"""

import uuid
import logging
from dataclasses import dataclass, field
from typing import Optional

from src.config import EA_PARAMS

logger = logging.getLogger(__name__)


@dataclass
class Poem:
    """
    A single poem candidate in the population.

    poem_id is a globally unique identifier used consistently across
    human_feedback.csv and expert_review.csv for cross-referencing.
    """
    poem_id: str = field(default_factory=lambda: str(uuid.uuid4())[:12])
    text: str = ""
    poem_type: str = ""        # 'haiku' or 'limerick'
    emotion: str = ""
    description: str = ""

    # Fitness components
    F: float = 0.0
    Q_bar: float = 0.0
    Rhyme: float = 0.0
    Structure: float = 0.0
    sub_scores: dict = field(default_factory=dict)

    # Metadata
    generation: int = 0
    generator_model: str = ""
    judge_model: str = ""

    # NSGA-II specific (set during non-dominated sorting)
    rank: int = 0                 # Pareto front rank (0 = non-dominated)
    crowding_distance: float = 0.0

    def __repr__(self) -> str:
        return (
            f"Poem(id={self.poem_id}, F={self.F:.3f}, "
            f"Q̄={self.Q_bar:.3f}, R={self.Rhyme:.3f}, S={self.Structure:.3f})"
        )


@dataclass
class GenerationLog:
    """Log entry for one generation of an EA run."""
    run_id: str
    ea: str
    poem_type: str
    emotion: str
    generation: int
    F: float
    Q_bar: float
    Rhyme: float
    Structure: float
    best_poem: str


@dataclass
class RunResult:
    """Final result of a complete EA run."""
    run_id: str
    ea: str
    poem_type: str
    emotion: str
    description: str
    best_poem: Poem
    generations_used: int
    generation_logs: list[GenerationLog] = field(default_factory=list)
    all_poems: list[Poem] = field(default_factory=list)


def generate_run_id(ea: str, poem_type: str, emotion: str) -> str:
    """Generate a unique run ID encoding the experiment parameters."""
    short_uuid = str(uuid.uuid4())[:8]
    return f"{ea}_{poem_type}_{emotion}_{short_uuid}"


def check_stopping_rule(
    generation_logs: list[GenerationLog],
    current_generation: int,
) -> bool:
    """
    Evidence-based stopping rule (Section 3):

    Stop when best F improves by less than 0.01 for 2 consecutive
    generations, OR at generation max_generations, whichever comes first.

    Returns True if the EA should stop.
    """
    if current_generation >= EA_PARAMS.max_generations:
        logger.info(f"Stopping: reached max generation {EA_PARAMS.max_generations}")
        return True

    if len(generation_logs) < EA_PARAMS.convergence_patience + 1:
        return False

    # Check last `convergence_patience` improvements
    recent = generation_logs[-(EA_PARAMS.convergence_patience + 1):]
    improvements = []
    for i in range(1, len(recent)):
        delta = recent[i].F - recent[i - 1].F
        improvements.append(delta)

    if all(abs(imp) < EA_PARAMS.convergence_threshold for imp in improvements):
        logger.info(
            f"Stopping: F improved by less than {EA_PARAMS.convergence_threshold} "
            f"for {EA_PARAMS.convergence_patience} consecutive generations "
            f"(deltas: {[f'{d:.4f}' for d in improvements]})"
        )
        return True

    return False
