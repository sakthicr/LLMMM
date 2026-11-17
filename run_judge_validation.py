"""
Entry point: Judge validation (same-exam comparison).

PURPOSE
-------
Q_bar for the EA runs was produced by the 5-dimension judge prompt
(imagery, literary_devices, originality, coherence + emotion_alignment),
while the human reference poems and the negative controls were scored by
the 4-dimension CALIBRATION prompt (no emotion_alignment).

Those two numbers are therefore NOT comparable: the EA poems answered an
extra question they were purpose-built to do well on.

This script re-scores all three groups with the SAME 4-dimension
calibration prompt, so the quality numbers finally sit on one scale:

    Group A  human reference poems  (data/calibration/*_reference.txt)
    Group B  negative controls      (data/calibration/*_negative.txt)
    Group C  the EA-produced poems  (output/logs/human_feedback.csv)

NOTHING EXISTING IS MODIFIED. This script only imports the existing
scoring functions and writes to a new folder, output/validation/.
No scoring code is changed, no existing log or CSV is touched.

With --reps > 1 each poem is scored several times, which also measures how
noisy the judge is (the same poem scored twice should give the same number).

Usage:
    python run_judge_validation.py              # 1 pass  (~53 judge calls, ~19k tokens)
    python run_judge_validation.py --reps 3     # 3 passes (~159 calls, ~56k tokens)
    python run_judge_validation.py --skip-reference   # only the EA poems
"""

import argparse
import asyncio
import csv
import logging
import statistics
import sys
from pathlib import Path

# Fix Windows console encoding — cp1252 cannot handle Q̄, ══, ── etc.
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.api.client import close_all_clients, get_client
from src.config import DATA_DIR, QWEN_27B
from src.fitness.quality import score_quality_calibration
from src.analysis.calibration import _load_reference_poems

OUT_DIR = Path("output/validation")
HUMAN_FEEDBACK = Path("output/logs/human_feedback.csv")

# The 12 accepted post-fix runs, plus the one rejected attempt.
EA_POEMS = {
    "10b32759-9f5": ("GA",      "limerick", "Fear",   "accepted"),
    "a63d13eb-742": ("NSGA-II", "limerick", "Fear",   "accepted"),
    "ebe241d6-b99": ("GA",      "limerick", "Joy",    "accepted"),
    "dc1f4208-832": ("NSGA-II", "limerick", "Joy",    "accepted"),
    "e9a71228-c53": ("GA",      "limerick", "Sorrow", "accepted"),
    "da3255a0-d29": ("NSGA-II", "limerick", "Sorrow", "accepted"),
    "cbbead3b-583": ("GA",      "haiku",    "Fear",   "accepted"),
    "a32548bc-8c4": ("NSGA-II", "haiku",    "Fear",   "accepted"),
    "39c5b5fe-204": ("GA",      "haiku",    "Joy",    "accepted"),
    "994e2aee-8ae": ("NSGA-II", "haiku",    "Joy",    "accepted"),
    "d51ae41b-c18": ("GA",      "haiku",    "Sorrow", "accepted"),
    "9b04d3ac-306": ("NSGA-II", "haiku",    "Sorrow", "accepted"),
    "9701be3c-0a7": ("GA",      "haiku",    "Joy",    "REJECTED (attempt 1)"),
}


def setup_logging():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(OUT_DIR / "judge_validation.log", mode="a", encoding="utf-8"),
        ],
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def load_ea_poems() -> list[dict]:
    """Read the EA poems out of human_feedback.csv (read-only)."""
    if not HUMAN_FEEDBACK.exists():
        print(f"ERROR: {HUMAN_FEEDBACK} not found. Run from the project root.")
        return []

    by_id = {}
    with open(HUMAN_FEEDBACK, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            by_id[row["poem_id"]] = row

    poems = []
    for poem_id, (ea, poem_type, emotion, status) in EA_POEMS.items():
        row = by_id.get(poem_id)
        if row is None:
            print(f"  WARNING: poem {poem_id} not found in human_feedback.csv — skipped")
            continue
        # human_feedback.csv stores the poem with ' | ' between lines.
        text = row["poem_text"].replace(" | ", "\n")
        poems.append({
            "group": "C_ea_generated",
            "title": f"{ea} {poem_type} {emotion} [{status}]",
            "text": text,
            "poem_type": poem_type,
            "poem_id": poem_id,
            "logged_F": row.get("F_score", ""),
        })
    return poems


def load_calibration_poems() -> list[dict]:
    """Reference (known-good) and negative (known-bad) poems, same loader as calibration."""
    out = []
    sets = [
        ("A_human_reference", "haiku",    DATA_DIR / "calibration" / "haiku_reference.txt"),
        ("A_human_reference", "limerick", DATA_DIR / "calibration" / "limerick_reference.txt"),
        ("B_negative_control", "haiku",   DATA_DIR / "calibration" / "haiku_negative.txt"),
        ("B_negative_control", "limerick", DATA_DIR / "calibration" / "limerick_negative.txt"),
    ]
    for group, poem_type, path in sets:
        for p in _load_reference_poems(path, poem_type):
            out.append({
                "group": group,
                "title": p.get("title") or "untitled",
                "text": p["text"],
                "poem_type": poem_type,
                "poem_id": "",
                "logged_F": "",
            })
    return out


async def score_all(poems: list[dict], reps: int) -> list[dict]:
    """Score every poem `reps` times with the 4-dimension calibration judge."""
    results = []
    total = len(poems) * reps
    n = 0
    for rep in range(1, reps + 1):
        for p in poems:
            n += 1
            try:
                q_bar, subs, served = await score_quality_calibration(p["text"], p["poem_type"])
            except Exception as exc:                      # keep going on a single failure
                logging.getLogger(__name__).warning(f"scoring failed for {p['title']}: {exc}")
                continue
            results.append({
                "group": p["group"],
                "poem_type": p["poem_type"],
                "title": p["title"],
                "poem_id": p["poem_id"],
                "rep": rep,
                "q_bar_4dim": q_bar,
                "imagery": subs.get("imagery", ""),
                "literary_devices": subs.get("literary_devices", ""),
                "originality": subs.get("originality", ""),
                "coherence": subs.get("coherence", ""),
                "logged_F": p["logged_F"],
                "judge_model": served,
            })
            print(f"  [{n:>3}/{total}] rep{rep} {p['group']:<19} {p['poem_type']:<8} "
                  f"Q={q_bar:.3f}  {p['title'][:46]}")
    return results


def summarise(results: list[dict], reps: int):
    """Print the comparison that the whole exercise is for."""
    print("\n" + "=" * 78)
    print("QUALITY ON ONE SCALE — all groups scored by the SAME 4-dimension judge")
    print("=" * 78)
    print(f"\n{'group':<22}{'form':<10}{'n':>4}{'Q mean':>9}{'Q sd':>8}{'Q min':>8}{'Q max':>8}")
    print("-" * 69)

    means = {}
    for group in ("A_human_reference", "B_negative_control", "C_ea_generated"):
        for form in ("haiku", "limerick"):
            qs = [r["q_bar_4dim"] for r in results
                  if r["group"] == group and r["poem_type"] == form]
            if not qs:
                continue
            sd = statistics.stdev(qs) if len(qs) > 1 else 0.0
            means[(group, form)] = statistics.mean(qs)
            print(f"{group:<22}{form:<10}{len(qs):>4}{statistics.mean(qs):>9.3f}"
                  f"{sd:>8.3f}{min(qs):>8.3f}{max(qs):>8.3f}")

    print("\n--- THE ANSWER ---")
    for form in ("haiku", "limerick"):
        ref = means.get(("A_human_reference", form))
        ea = means.get(("C_ea_generated", form))
        neg = means.get(("B_negative_control", form))
        if ref is None or ea is None:
            continue
        verdict = ("EA poems score HIGHER than published human poems"
                   if ea > ref else "published human poems score higher than EA poems")
        print(f"  {form:<9} human {ref:.3f} | EA {ea:.3f} | bad-on-purpose "
              f"{neg if neg is None else f'{neg:.3f}'}  ->  {verdict} (gap {ea - ref:+.3f})")

    if reps > 1:
        print("\n--- JUDGE NOISE (same poem, scored several times) ---")
        per_poem = {}
        for r in results:
            per_poem.setdefault((r["group"], r["title"]), []).append(r["q_bar_4dim"])
        sds = [statistics.stdev(v) for v in per_poem.values() if len(v) > 1]
        unstable = sum(1 for v in per_poem.values() if len(v) > 1 and max(v) != min(v))
        if sds:
            print(f"  mean within-poem sd : {statistics.mean(sds):.4f}")
            print(f"  largest sd for one poem: {max(sds):.4f}")
            print(f"  poems that did NOT get the same score every time: "
                  f"{unstable}/{len(per_poem)}")
            print("  (one judge step = 0.0625 on this 4-dimension scale)")


async def main_async(args):
    try:
        await _run(args)
    finally:
        await close_all_clients()      # must close inside this event loop


async def _run(args):
    poems = []
    if not args.skip_reference:
        poems += load_calibration_poems()
    poems += load_ea_poems()

    if not poems:
        print("No poems loaded — nothing to do.")
        return

    calls = len(poems) * args.reps
    print(f"\nScoring {len(poems)} poems x {args.reps} rep(s) = {calls} judge calls "
          f"(~{calls * 350:,} tokens) with the 4-dimension calibration prompt.\n")

    results = await score_all(poems, args.reps)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = OUT_DIR / "judge_validation.csv"
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    summarise(results, args.reps)

    try:
        usage = get_client(QWEN_27B).usage
        print(f"\nJudge tokens used today: {usage.tokens_today} "
              f"(prompt={usage.prompt_tokens_today}, completion={usage.completion_tokens_today})")
    except Exception:
        pass

    print(f"\nWritten: {out_csv}")
    print(f"Written: {OUT_DIR / 'judge_validation.log'}")
    print("No existing file was modified.")


def main():
    ap = argparse.ArgumentParser(description="Re-score all poem groups with one identical judge prompt.")
    ap.add_argument("--reps", type=int, default=1,
                    help="how many times to score each poem (default 1; use 3 to measure judge noise)")
    ap.add_argument("--skip-reference", action="store_true",
                    help="score only the EA poems, not the reference/negative sets")
    args = ap.parse_args()

    setup_logging()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
