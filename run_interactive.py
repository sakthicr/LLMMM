"""
Entry point: Interactive CLI tool for human-in-the-loop poem generation.

Usage:
    python run_interactive.py
"""

import asyncio
import logging
import sys

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from src.api.client import close_all_clients


def setup_logging():
    """Configure logging for interactive mode."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("output/logs/interactive.log", mode="a", encoding="utf-8"),
        ],
    )
    # Reduce noise from httpx
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


async def async_main():
    from src.interactive.tool import run_interactive_tool
    try:
        await run_interactive_tool()
    finally:
        await close_all_clients()


def main():
    setup_logging()
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")


if __name__ == "__main__":
    main()
