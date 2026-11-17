"""
Entry point: Statistical grid runner (Section 8).

Runs 2 poem types × 5 emotions × 2 EAs × 5 runs = 100 total runs.
Uses GPT-OSS-120B via Groq for bulk generation.

Usage:
    python run_grid.py                    # Full grid (100 runs)
    python run_grid.py --test             # Quick test (1 type × 1 emotion × 2 EAs × 1 run)
    python run_grid.py --poem-type haiku  # Only haiku
    python run_grid.py --ea ga            # Only GA
"""

import argparse
import asyncio
import logging
import sys

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.api.client import close_all_clients
from src.config import POEM_TYPES, EMOTIONS, EA_TYPES


def setup_logging():
    """Configure logging for grid mode."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("output/logs/grid.log", mode="a", encoding="utf-8"),
        ],
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run the EA-Poetry statistical grid"
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
        help="Override runs per cell (default: 5)"
    )
    return parser.parse_args()


async def async_main(args):
    from src.grid.runner import run_grid

    poem_types = [args.poem_type] if args.poem_type else None
    ea_types = [args.ea] if args.ea else None
    emotions = [args.emotion] if args.emotion else None
    runs = args.runs

    if args.test:
        poem_types = ["haiku"]
        emotions = ["joy"]
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
        print(f"GRID COMPLETE: {len(successes)} succeeded, {len(failures)} failed")
        print(f"{'='*60}")

        if failures:
            print("\nFailed runs:")
            for f in failures:
                print(f"  {f['run_id']}: {f.get('error', 'unknown error')}")

        if args.test:
            from src.api.client import _clients
            print(f"\n{'='*60}")
            print("TOKEN USAGE SUMMARY")
            print(f"{'='*60}")
            for key, client in _clients.items():
                name = client.config.name
                calls = client.usage.requests_today
                if calls > 0:
                    avg_p = client.usage.prompt_tokens_today / calls
                    avg_c = client.usage.completion_tokens_today / calls
                    print(f"  {name}: {calls} calls, {avg_p:.1f} avg prompt, {avg_c:.1f} avg completion")

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
