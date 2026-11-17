"""
CSV logging for all four output files.

POEM_ID CONSISTENCY (Section 11, user requirement #3):
The poem_id is generated once in ea/common.py (Poem.poem_id) using a UUID.
That same poem_id is written to BOTH human_feedback.csv AND expert_review.csv,
so accepted poems can be cross-referenced between the two files.

All writers are append-safe: they create headers on first write, then append.
"""

import csv
import logging
from datetime import datetime, timezone
from pathlib import Path

from src.config import (
    CSV_PER_GENERATION,
    CSV_PER_RUN_SUMMARY,
    CSV_HUMAN_FEEDBACK,
    CSV_EXPERT_REVIEW,
)
from src.ea.common import GenerationLog, Poem

logger = logging.getLogger(__name__)


def _ensure_csv(path: Path, headers: list[str]) -> None:
    """Create the CSV file with headers if it doesn't exist."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
        logger.info(f"Created CSV: {path}")


# ── Per-generation log ───────────────────────────────────────────────────────

PER_GENERATION_HEADERS = [
    "run_id", "ea", "poem_type", "emotion", "generation",
    "F", "Q_bar", "Rhyme", "Structure", "best_poem",
]


def log_generation(gen_log: GenerationLog) -> None:
    """Append one generation entry to per_generation.csv."""
    _ensure_csv(CSV_PER_GENERATION, PER_GENERATION_HEADERS)

    with open(CSV_PER_GENERATION, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            gen_log.run_id,
            gen_log.ea,
            gen_log.poem_type,
            gen_log.emotion,
            gen_log.generation,
            f"{gen_log.F:.4f}",
            f"{gen_log.Q_bar:.4f}",
            f"{gen_log.Rhyme:.4f}",
            f"{gen_log.Structure:.4f}",
            gen_log.best_poem.replace("\n", " | "),
        ])


def log_all_generations(gen_logs: list[GenerationLog]) -> None:
    """Append all generation entries from a run."""
    for gen_log in gen_logs:
        log_generation(gen_log)
    logger.info(f"Logged {len(gen_logs)} generations for run {gen_logs[0].run_id}")


# ── Per-run summary ─────────────────────────────────────────────────────────

PER_RUN_SUMMARY_HEADERS = [
    "run_id", "ea", "poem_type", "emotion", "final_F",
    "generations_used", "best_poem",
]


def log_run_summary(
    run_id: str,
    ea: str,
    poem_type: str,
    emotion: str,
    final_f: float,
    generations_used: int,
    best_poem: str,
) -> None:
    """Append one run summary entry."""
    _ensure_csv(CSV_PER_RUN_SUMMARY, PER_RUN_SUMMARY_HEADERS)

    with open(CSV_PER_RUN_SUMMARY, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            run_id, ea, poem_type, emotion,
            f"{final_f:.4f}",
            generations_used,
            best_poem.replace("\n", " | "),
        ])
    logger.info(f"Logged run summary: {run_id} | F={final_f:.4f}")


# ── Human feedback log ───────────────────────────────────────────────────────

HUMAN_FEEDBACK_HEADERS = [
    "timestamp", "poem_id", "poem_type", "ea", "emotion", "description",
    "attempt_number", "verdict", "poem_text", "F_score", "notes",
]


def log_human_feedback(
    poem: Poem,
    ea: str,
    attempt_number: int,
    verdict: str,  # "good" or "bad"
    notes: str = "",
) -> None:
    """
    Append one human feedback entry.

    Uses poem.poem_id — the SAME ID that will appear in expert_review.csv
    when this poem is later reviewed by an expert.
    """
    _ensure_csv(CSV_HUMAN_FEEDBACK, HUMAN_FEEDBACK_HEADERS)

    with open(CSV_HUMAN_FEEDBACK, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            poem.poem_id,       # ← consistent ID
            poem.poem_type,
            ea,
            poem.emotion,
            poem.description,
            attempt_number,
            verdict,
            poem.text.replace("\n", " | "),
            f"{poem.F:.4f}",
            notes,
        ])
    logger.info(
        f"Human feedback: poem={poem.poem_id} | verdict={verdict} | "
        f"attempt={attempt_number}"
    )


# ── Expert review log ────────────────────────────────────────────────────────

EXPERT_REVIEW_HEADERS = [
    "timestamp", "poem_id", "poem_type", "ea", "emotion",
    "poem_text", "F_score", "expert_rating", "comment",
]


def log_expert_review(
    poem_id: str,
    poem_type: str,
    ea: str,
    emotion: str,
    poem_text: str,
    f_score: float,
    expert_rating: int,
    comment: str,
) -> None:
    """
    Append one expert review entry.

    poem_id here is the SAME poem_id written to human_feedback.csv,
    enabling cross-referencing between the two files.
    """
    _ensure_csv(CSV_EXPERT_REVIEW, EXPERT_REVIEW_HEADERS)

    with open(CSV_EXPERT_REVIEW, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            poem_id,            # ← same ID as in human_feedback.csv
            poem_type,
            ea,
            emotion,
            poem_text.replace("\n", " | "),
            f"{f_score:.4f}",
            expert_rating,
            comment,
        ])
    logger.info(f"Expert review: poem={poem_id} | rating={expert_rating}")


# ── Utilities ────────────────────────────────────────────────────────────────

def read_accepted_poems(
) -> list[dict]:
    """
    Read all "good"-verdict poems from human_feedback.csv.

    Returns a list of dicts with poem_id, poem_type, ea, emotion,
    poem_text, F_score — ready for the expert review workflow.
    """
    if not CSV_HUMAN_FEEDBACK.exists():
        logger.warning("human_feedback.csv not found")
        return []

    accepted = []
    with open(CSV_HUMAN_FEEDBACK, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("verdict", "").strip().lower() == "good":
                accepted.append({
                    "poem_id": row["poem_id"],
                    "poem_type": row["poem_type"],
                    "ea": row["ea"],
                    "emotion": row["emotion"],
                    "poem_text": row["poem_text"].replace(" | ", "\n"),
                    "F_score": float(row["F_score"]),
                })
    return accepted


def get_reviewed_poem_ids() -> set[str]:
    """
    Get the set of poem_ids already reviewed in expert_review.csv.
    Prevents duplicate reviews.
    """
    if not CSV_EXPERT_REVIEW.exists():
        return set()

    reviewed = set()
    with open(CSV_EXPERT_REVIEW, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            reviewed.add(row["poem_id"])
    return reviewed


def log_raw_generator(run_id: str, call_type: str, raw_text: str) -> None:
    """
    Log full raw generator response to output/logs/raw_generator.log.
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    log_file = Path("output/logs/raw_generator.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"=== [{timestamp}] run_id={run_id} | call_type={call_type} ===\n")
        f.write(raw_text.rstrip("\n") + "\n\n")
