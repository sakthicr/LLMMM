"""
Entry point: Run all analysis — statistics, charts, comparison tables.

Usage:
    python run_analysis.py
"""

import logging
import sys

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("output/logs/analysis.log", mode="a", encoding="utf-8"),
        ],
    )
    logging.getLogger("matplotlib").setLevel(logging.WARNING)


def main():
    setup_logging()

    from src.analysis.statistics import print_full_analysis
    from src.analysis.charts import generate_all_charts

    print_full_analysis()

    print("\nGenerating charts...")
    paths = generate_all_charts()
    for p in paths:
        print(f"  ✓ {p}")

    if not paths:
        print("  (no charts generated — run the grid first)")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
