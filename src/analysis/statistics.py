"""
Statistical analysis: Mann-Whitney U test and correlation analysis.

- Mann-Whitney U: GA vs NSGA-II final F scores per poem type (non-parametric, n=5)
- Spearman correlation: F score vs expert 1-5 rating
"""

import csv
import logging
from collections import defaultdict

from scipy import stats
from tabulate import tabulate

from src.config import (
    CSV_PER_RUN_SUMMARY, CSV_EXPERT_REVIEW, CSV_HUMAN_FEEDBACK,
    POEM_TYPES, EA_TYPES,
)

logger = logging.getLogger(__name__)


def load_run_summaries() -> list[dict]:
    """Load per_run_summary.csv into a list of dicts."""
    if not CSV_PER_RUN_SUMMARY.exists():
        logger.warning("per_run_summary.csv not found")
        return []

    with open(CSV_PER_RUN_SUMMARY, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_expert_reviews() -> list[dict]:
    """Load expert_review.csv into a list of dicts."""
    if not CSV_EXPERT_REVIEW.exists():
        logger.warning("expert_review.csv not found")
        return []

    with open(CSV_EXPERT_REVIEW, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_mann_whitney_u() -> dict:
    """
    Mann-Whitney U test: GA vs NSGA-II final F scores.

    Runs separately for each poem type. Non-parametric — appropriate
    for n=5 per group.

    Returns dict: {poem_type: {statistic, p_value, ga_median, nsga2_median, significant}}
    """
    summaries = load_run_summaries()
    if not summaries:
        logger.warning("No run summaries available for Mann-Whitney U test")
        return {}

    results = {}

    for poem_type in POEM_TYPES:
        ga_scores = [
            float(row["final_F"])
            for row in summaries
            if row["ea"] == "ga" and row["poem_type"] == poem_type
        ]
        nsga2_scores = [
            float(row["final_F"])
            for row in summaries
            if row["ea"] == "nsga2" and row["poem_type"] == poem_type
        ]

        if len(ga_scores) < 2 or len(nsga2_scores) < 2:
            logger.warning(
                f"Not enough data for Mann-Whitney U ({poem_type}): "
                f"GA={len(ga_scores)}, NSGA-II={len(nsga2_scores)}"
            )
            continue

        stat, p_value = stats.mannwhitneyu(
            ga_scores, nsga2_scores, alternative='two-sided'
        )

        import statistics
        results[poem_type] = {
            "statistic": stat,
            "p_value": p_value,
            "ga_median": statistics.median(ga_scores),
            "ga_mean": statistics.mean(ga_scores),
            "ga_n": len(ga_scores),
            "nsga2_median": statistics.median(nsga2_scores),
            "nsga2_mean": statistics.mean(nsga2_scores),
            "nsga2_n": len(nsga2_scores),
            "significant": p_value < 0.05,
        }

        logger.info(
            f"Mann-Whitney U ({poem_type}): "
            f"U={stat:.2f}, p={p_value:.4f} "
            f"({'significant' if p_value < 0.05 else 'not significant'}) | "
            f"GA median={results[poem_type]['ga_median']:.3f}, "
            f"NSGA-II median={results[poem_type]['nsga2_median']:.3f}"
        )

    return results


def run_fitness_expert_correlation() -> dict | None:
    """
    Spearman rank correlation between F score and expert 1-5 rating.

    Tests whether the automatic fitness function tracks real human
    judgment — the validation check from Section 10.

    Returns dict: {correlation, p_value, n, significant} or None
    """
    reviews = load_expert_reviews()
    if not reviews:
        logger.warning("No expert reviews available for correlation analysis")
        return None

    f_scores = []
    expert_ratings = []

    for row in reviews:
        try:
            f_scores.append(float(row["F_score"]))
            expert_ratings.append(int(row["expert_rating"]))
        except (ValueError, KeyError):
            continue

    if len(f_scores) < 3:
        logger.warning(
            f"Too few data points for correlation: {len(f_scores)}"
        )
        return None

    corr, p_value = stats.spearmanr(f_scores, expert_ratings)

    result = {
        "correlation": corr,
        "p_value": p_value,
        "n": len(f_scores),
        "significant": p_value < 0.05,
    }

    logger.info(
        f"Spearman correlation (F vs expert): "
        f"r={corr:.3f}, p={p_value:.4f}, n={len(f_scores)} "
        f"({'significant' if p_value < 0.05 else 'not significant'})"
    )

    return result


def build_comparison_table() -> str:
    """
    Build the final comparison table: F, Q̄, Rhyme, Structure — by EA × poem type.

    Returns a formatted table string.
    """
    summaries = load_run_summaries()
    if not summaries:
        return "No data available for comparison table."

    # Load per-generation data for extra metrics
    gen_data = []
    from src.config import CSV_PER_GENERATION
    if CSV_PER_GENERATION.exists():
        with open(CSV_PER_GENERATION, "r", encoding="utf-8") as f:
            gen_data = list(csv.DictReader(f))

    # Group by (ea, poem_type)
    groups = defaultdict(list)
    for row in summaries:
        key = (row["ea"], row["poem_type"])
        groups[key].append(row)

    table_data = []
    for (ea, poem_type), rows in sorted(groups.items()):
        f_scores = [float(r["final_F"]) for r in rows]
        gens = [int(r["generations_used"]) for r in rows]

        import statistics
        table_data.append([
            ea.upper(),
            poem_type.capitalize(),
            len(rows),
            f"{statistics.mean(f_scores):.3f} ± {statistics.stdev(f_scores):.3f}" if len(f_scores) > 1 else f"{f_scores[0]:.3f}",
            f"{statistics.mean(gens):.1f}",
        ])

    headers = ["EA", "Poem Type", "N", "F (mean ± std)", "Avg Gens"]
    return tabulate(table_data, headers=headers, tablefmt="grid")


def print_full_analysis() -> None:
    """Run and print all analysis results."""
    print("\n" + "="*60)
    print("STATISTICAL ANALYSIS RESULTS")
    print("="*60)

    # Mann-Whitney U
    print("\n── Mann-Whitney U Test (GA vs NSGA-II) ──\n")
    mwu_results = run_mann_whitney_u()
    if mwu_results:
        for poem_type, result in mwu_results.items():
            sig_marker = "**" if result["significant"] else ""
            print(f"  {poem_type.capitalize()}:")
            print(f"    U = {result['statistic']:.2f}, p = {result['p_value']:.4f} {sig_marker}")
            print(f"    GA:      mean={result['ga_mean']:.3f}, median={result['ga_median']:.3f} (n={result['ga_n']})")
            print(f"    NSGA-II: mean={result['nsga2_mean']:.3f}, median={result['nsga2_median']:.3f} (n={result['nsga2_n']})")
            print()
    else:
        print("  No data available.\n")

    # Fitness-expert correlation
    print("── Fitness vs Expert Correlation ──\n")
    corr = run_fitness_expert_correlation()
    if corr:
        sig_marker = "**" if corr["significant"] else ""
        print(f"  Spearman r = {corr['correlation']:.3f}, p = {corr['p_value']:.4f} {sig_marker}")
        print(f"  n = {corr['n']}")
    else:
        print("  No expert review data available.")

    # Comparison table
    print("\n── Comparison Table ──\n")
    print(build_comparison_table())
    print()
