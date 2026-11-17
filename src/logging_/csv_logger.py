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
    CSV_GRID_RUNS,
    CSV_GRID_CANDIDATES,
    LOGS_DIR,
    JUDGE_REPEATS,
    NORMALIZE_APOSTROPHES,
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
    Log full raw generator response to raw_generator.log in the active
    logs folder (output/logs in Phase 1, output/logs_phase2 in Phase 2).
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    log_file = LOGS_DIR / "raw_generator.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"=== [{timestamp}] run_id={run_id} | call_type={call_type} ===\n")
        f.write(raw_text.rstrip("\n") + "\n\n")


# ── Grid logs (statistical grid; one row per run, one row per candidate) ─────

GRID_RUNS_HEADERS = [
    "timestamp", "run_id", "replicate", "ea", "poem_type", "emotion",
    "description", "status", "final_F", "Q_bar", "Rhyme", "Structure",
    "generations_used", "best_poem_id", "best_poem", "n_candidates",
    "judge_repeats", "normalize_apostrophes", "error",
]

GRID_CANDIDATES_HEADERS = [
    "run_id", "ea", "poem_type", "emotion", "poem_id", "generation",
    "F", "Q_bar", "Rhyme", "Structure", "is_final", "poem_text",
]


def log_grid_run(
    run_id: str,
    replicate: int,
    ea: str,
    poem_type: str,
    emotion: str,
    description: str,
    status: str,            # "ok" or "failed"
    best_poem: Poem | None = None,
    generations_used: int | None = None,
    n_candidates: int | None = None,
    error: str = "",
) -> None:
    """Append one grid run (successful or failed) to grid_runs.csv."""
    _ensure_csv(CSV_GRID_RUNS, GRID_RUNS_HEADERS)

    with open(CSV_GRID_RUNS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            run_id, replicate, ea, poem_type, emotion, description, status,
            f"{best_poem.F:.4f}" if best_poem else "",
            f"{best_poem.Q_bar:.4f}" if best_poem else "",
            f"{best_poem.Rhyme:.4f}" if best_poem else "",
            f"{best_poem.Structure:.4f}" if best_poem else "",
            generations_used if generations_used is not None else "",
            best_poem.poem_id if best_poem else "",
            best_poem.text.replace("\n", " | ") if best_poem else "",
            n_candidates if n_candidates is not None else "",
            JUDGE_REPEATS,
            int(NORMALIZE_APOSTROPHES),
            error,
        ])


def log_grid_candidates(
    run_id: str,
    ea: str,
    poem_type: str,
    emotion: str,
    all_poems: list[Poem],
    best_poem_id: str,
) -> None:
    """Append every evaluated candidate of a run to grid_candidates.csv."""
    _ensure_csv(CSV_GRID_CANDIDATES, GRID_CANDIDATES_HEADERS)

    with open(CSV_GRID_CANDIDATES, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in all_poems:
            writer.writerow([
                run_id, ea, poem_type, emotion, p.poem_id, p.generation,
                f"{p.F:.4f}", f"{p.Q_bar:.4f}", f"{p.Rhyme:.4f}", f"{p.Structure:.4f}",
                int(p.poem_id == best_poem_id),
                p.text.replace("\n", " | "),
            ])


def count_completed_grid_runs() -> dict[tuple[str, str, str], int]:
    """
    Count successful grid runs already logged, per (ea, poem_type, emotion).

    Used to resume an interrupted grid without repeating finished runs.
    """
    counts: dict[tuple[str, str, str], int] = {}
    if not CSV_GRID_RUNS.exists():
        return counts
    with open(CSV_GRID_RUNS, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "ok":
                key = (row["ea"], row["poem_type"], row["emotion"].lower())
                counts[key] = counts.get(key, 0) + 1
    return counts
