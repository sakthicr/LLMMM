"""
Entry point: Statistical grid runner (Section 8).

Runs 2 poem types × 5 emotions × 2 EAs × 5 runs = 100 total runs.
Uses GPT-OSS-120B via Groq for bulk generation.

Usage:
    python run_grid.py                    # Phase 1 grid
    python run_grid.py --test             # Quick test (1 type × 1 emotion × 2 EAs × 1 run)
    python run_grid.py --poem-type haiku  # Only haiku
    python run_grid.py --ea ga            # Only GA

Phase 2 (averaged judge, apostrophe fix, six Phase I scenarios, separate logs):
    python run_grid.py --phase2 --test        # one haiku/Joy pair, to check everything works
    python run_grid.py --phase2 --runs 3      # 12 cells × 3 replicates = 36 runs
    The Phase 2 grid can be stopped and started again: finished runs are skipped.
"""

import argparse
import asyncio
import logging
import os
import sys

# --phase2 must take effect BEFORE src.config is imported, because the config
# reads the EA_PHASE environment variable when it is first loaded.
if "--phase2" in sys.argv:
    os.environ["EA_PHASE"] = "2"

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.api.client import close_all_clients
from src.config import POEM_TYPES, EMOTIONS, EA_TYPES, LOGS_DIR, PHASE2, JUDGE_REPEATS


def setup_logging():
    """Configure logging for grid mode."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOGS_DIR / "grid.log", mode="a", encoding="utf-8"),
        ],
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run the EA-Poetry statistical grid"
    )
    parser.add_argument(
        "--phase2", action="store_true",
        help="Phase 2 settings: judge averaged over several readings, apostrophe "
             "normalisation, the six Phase I scenarios, logs in output/logs_phase2"
    )
    parser.add_argument(
        "--test", action="store_true",
        help="Quick test mode: 1 type × 1 emotion × 2 EAs × 1 run"
    )
    parser.add_argument(
        "--poem-type", choices=POEM_TYPES,
        help="Run only this poem type"
    )
    parser.add_argument(
        "--ea", choices=EA_TYPES,
        help="Run only this EA"
    )
    parser.add_argument(
        "--emotion", choices=EMOTIONS,
        help="Run only this emotion"
    )
    parser.add_argument(
        "--runs", type=int, default=None,
        help="Replicates per cell (default: 5 in Phase 1, 3 in Phase 2)"
    )
    return parser.parse_args()


async def async_main(args):
    from src.grid.runner import run_grid

    poem_types = [args.poem_type] if args.poem_type else None
    ea_types = [args.ea] if args.ea else None
    emotions = [args.emotion] if args.emotion else None
    runs = args.runs
    if runs is None and PHASE2:
        runs = 3

    if args.test:
        poem_types = ["haiku"]
        emotions = ["Joy"]
        runs = 1
        logging.info("TEST MODE: 1 type × 1 emotion × 2 EAs × 1 run")

    try:
        results = await run_grid(
            poem_types=poem_types,
            emotions=emotions,
            ea_types=ea_types,
            runs_per_cell=runs,
        )

        # Print summary
        successes = [r for r in results if r.get("final_F") is not None]
        failures = [r for r in results if r.get("final_F") is None]

        print(f"\n{'='*60}")
        print(f"GRID SESSION FINISHED: {len(successes)} succeeded, {len(failures)} failed")
        print(f"Phase {'2' if PHASE2 else '1'} | judge readings per poem: {JUDGE_REPEATS} | logs: {LOGS_DIR}")
        print(f"{'='*60}")

        for r in successes:
            print(f"  {r['ea']:<6} {r['poem_type']:<9} {r['emotion']:<7} rep {r.get('replicate', '?')}: "
                  f"F={r['final_F']:.4f} (Q={r['Q_bar']:.4f}, R={r['Rhyme']:.3f}, S={r['Structure']:.3f}) "
                  f"gens={r['generations_used']}")

        if failures:
            print("\nFailed runs:")
            for f in failures:
                print(f"  {f['run_id']}: {f.get('error', 'unknown error')}")

        if args.test or PHASE2:
            from src.api.client import _clients
            print(f"\n{'='*60}")
            print("TOKEN USAGE THIS SESSION")
            print(f"{'='*60}")
            for key, client in _clients.items():
                name = client.config.name
                calls = client.usage.requests_today
                if calls > 0:
                    avg_p = client.usage.prompt_tokens_today / calls
                    avg_c = client.usage.completion_tokens_today / calls
                    print(f"  {name}: {calls} calls, {client.usage.tokens_today} tokens "
                          f"({avg_p:.1f} avg prompt, {avg_c:.1f} avg completion)")

    finally:
        await close_all_clients()


def main():
    setup_logging()
    args = parse_args()
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        print("\nInterrupted. Partial results are saved in the CSV logs.")


if __name__ == "__main__":
    main()
