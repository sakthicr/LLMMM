"""
Entry point: Human-poem calibration (Section 10).

Runs the calibration fitness pipeline on reference human poems to verify
that F scores are sane before trusting them on generated output.

Calibration mode uses 4-dimension Q_bar (no emotion_alignment).
Also runs negative controls and reports token usage.

Usage:
    python run_calibration.py
    python run_calibration.py --emotion sorrow
"""

import argparse
import asyncio
import logging
import statistics
import sys

# Fix Windows console encoding — cp1252 cannot handle Q̄, ══, ── etc.
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.api.client import close_all_clients
from src.fitness.rhyme import _get_last_word


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("output/logs/calibration.log", mode="a", encoding="utf-8"),
        ],
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def _print_poem_section(label: str, items: list[dict], poem_type: str):
    """Print a section of poem results."""
    print(f"\n── {label} ──")
    if not items:
        print("  (none)")
        return

    for item in items:
        title = item.get("title", "Untitled")
        text = item.get("text", "")
        mark = ""
        if poem_type == "limerick":
            lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
            if len(lines) >= 5:
                w1 = _get_last_word(lines[0])
                w5 = _get_last_word(lines[4])
                if w1 and w5 and w1 == w5:
                    mark = " (*identical L1/L5 end words)"
                    
        print(
            f"  {title[:40]:<42} "
            f"F={item['F']:.3f}  "
            f"Q̄={item['Q_bar']:.3f}  "
            f"R={item['Rhyme']:.3f}  "
            f"S={item['Structure']:.3f}{mark}"
        )

    f_scores = [item["F"] for item in items]
    f_std = statistics.stdev(f_scores) if len(f_scores) > 1 else 0.0
    print(f"\n  Summary F: mean={statistics.mean(f_scores):.3f}, "
          f"std={f_std:.3f}, "
          f"range=[{min(f_scores):.3f}, {max(f_scores):.3f}]")

    q_scores = [item["Q_bar"] for item in items]
    q_std = statistics.stdev(q_scores) if len(q_scores) > 1 else 0.0
    print(f"  Summary Q̄: mean={statistics.mean(q_scores):.3f}, "
          f"std={q_std:.3f}, "
          f"range=[{min(q_scores):.3f}, {max(q_scores):.3f}]")


async def async_main(emotion: str):
    from src.analysis.calibration import run_calibration

    try:
        cal = await run_calibration(target_emotion=emotion)

        results = cal["results"]
        negative_results = cal["negative_results"]
        token_usage = cal["token_usage"]

        print(f"\n{'='*60}")
        print("CALIBRATION RESULTS  (Q̄ = 4-dim, no emotion_alignment)")
        print(f"{'='*60}")

        for poem_type in ["haiku", "limerick"]:
            items = results.get(poem_type, [])
            _print_poem_section(
                f"{poem_type.capitalize()} Reference ({len(items)} poems)",
                items,
                poem_type
            )

            neg_items = negative_results.get(poem_type, [])
            if neg_items:
                _print_poem_section(
                    f"{poem_type.capitalize()} Negative Controls ({len(neg_items)} poems)",
                    neg_items,
                    poem_type
                )
                
            if items and neg_items:
                from scipy.stats import mannwhitneyu
                f_ref = [x["F"] for x in items]
                f_neg = [x["F"] for x in neg_items]
                q_ref = [x["Q_bar"] for x in items]
                q_neg = [x["Q_bar"] for x in neg_items]
                
                print(f"\n  ── {poem_type.capitalize()} Statistical Tests ──")
                print(f"  Q-bar: Ref mean={statistics.mean(q_ref):.3f} vs Neg mean={statistics.mean(q_neg):.3f}")
                q_stat, q_pval = mannwhitneyu(q_ref, q_neg, alternative='two-sided')
                print(f"         Mann-Whitney U: U={q_stat:.1f}, p={q_pval:.4f}")
                
                print(f"  F:     Ref mean={statistics.mean(f_ref):.3f} vs Neg mean={statistics.mean(f_neg):.3f}")
                f_stat, f_pval = mannwhitneyu(f_ref, f_neg, alternative='two-sided')
                print(f"         Mann-Whitney U: U={f_stat:.1f}, p={f_pval:.4f}")

        # Token usage
        print(f"\n{'─'*60}")
        print(f"Token usage: {token_usage['total_requests']} judge calls, "
              f"{token_usage['total_tokens']} total tokens "
              f"(prompt={token_usage['prompt_tokens']}, "
              f"completion={token_usage['completion_tokens']}), "
              f"{token_usage['avg_tokens_per_call']} avg tokens/call")
        print(f"{'─'*60}")

    finally:
        await close_all_clients()


def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Run calibration on reference human poems"
    )
    parser.add_argument(
        "--emotion", default="joy",
        help="Ignored in calibration mode (kept for CLI compatibility)"
    )
    args = parser.parse_args()

    try:
        asyncio.run(async_main(args.emotion))
    except KeyboardInterrupt:
        print("\nInterrupted.")


if __name__ == "__main__":
    main()
