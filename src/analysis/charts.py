"""
Convergence charts and comparison visualizations.

- Convergence chart: F over generations, both EAs (for RQ3)
- Box plots: GA vs NSGA-II final F scores per poem type
"""

import csv
import logging
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns

from src.config import CSV_PER_GENERATION, CSV_PER_RUN_SUMMARY, CHARTS_DIR

logger = logging.getLogger(__name__)

# Style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    "figure.figsize": (10, 6),
    "figure.dpi": 150,
    "font.size": 11,
})


def plot_convergence_chart(output_path: Path | None = None) -> Path:
    """
    Plot F over generations for both EAs, averaged across runs.

    This is the RQ3 visualization: does the stopping rule support or
    contradict the base paper's 3-generation assumption?
    """
    if not CSV_PER_GENERATION.exists():
        logger.warning("per_generation.csv not found")
        return Path()

    # Load data
    data = []
    with open(CSV_PER_GENERATION, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            data.append(row)

    if not data:
        logger.warning("No generation data available for convergence chart")
        return Path()

    # Group by (ea, poem_type, generation) → list of F values
    groups = defaultdict(list)
    for row in data:
        key = (row["ea"], row["poem_type"], int(row["generation"]))
        groups[key].append(float(row["F"]))

    # Create separate charts for each poem type
    poem_types = sorted(set(row["poem_type"] for row in data))
    eas = sorted(set(row["ea"] for row in data))

    fig, axes = plt.subplots(1, len(poem_types), figsize=(7 * len(poem_types), 6))
    if len(poem_types) == 1:
        axes = [axes]

    colors = {"ga": "#E74C3C", "nsga2": "#3498DB"}
    labels = {"ga": "GA", "nsga2": "NSGA-II"}

    for ax, poem_type in zip(axes, poem_types):
        for ea in eas:
            gens = sorted(set(
                g for (e, pt, g) in groups if e == ea and pt == poem_type
            ))
            means = []
            stds = []
            for g in gens:
                values = groups.get((ea, poem_type, g), [])
                if values:
                    import statistics
                    means.append(statistics.mean(values))
                    stds.append(statistics.stdev(values) if len(values) > 1 else 0)

            if means:
                ax.plot(
                    gens[:len(means)], means,
                    color=colors.get(ea, "#666"),
                    label=labels.get(ea, ea),
                    linewidth=2,
                    marker="o",
                    markersize=5,
                )
                ax.fill_between(
                    gens[:len(means)],
                    [m - s for m, s in zip(means, stds)],
                    [m + s for m, s in zip(means, stds)],
                    alpha=0.2,
                    color=colors.get(ea, "#666"),
                )

        ax.set_xlabel("Generation")
        ax.set_ylabel("Fitness (F)")
        ax.set_title(f"{poem_type.capitalize()}: Convergence")
        ax.legend()

        # Add vertical line at generation 3 (base paper's fixed limit)
        ax.axvline(x=3, color="#95A5A6", linestyle="--", alpha=0.7, label="Base paper limit (gen 3)")

    plt.tight_layout()

    if output_path is None:
        output_path = CHARTS_DIR / "convergence.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    logger.info(f"Convergence chart saved: {output_path}")
    return output_path


def plot_boxplot_comparison(output_path: Path | None = None) -> Path:
    """
    Box plot: GA vs NSGA-II final F scores, per poem type.
    """
    if not CSV_PER_RUN_SUMMARY.exists():
        logger.warning("per_run_summary.csv not found")
        return Path()

    data = []
    with open(CSV_PER_RUN_SUMMARY, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            data.append({
                "EA": "GA" if row["ea"] == "ga" else "NSGA-II",
                "Poem Type": row["poem_type"].capitalize(),
                "Final F": float(row["final_F"]),
            })

    if not data:
        logger.warning("No data for box plot")
        return Path()

    import pandas as pd
    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
        data=df, x="Poem Type", y="Final F", hue="EA",
        palette={"GA": "#E74C3C", "NSGA-II": "#3498DB"},
        ax=ax,
    )
    ax.set_title("GA vs NSGA-II: Final Fitness Scores")
    ax.set_ylabel("Fitness Score (F)")
    plt.tight_layout()

    if output_path is None:
        output_path = CHARTS_DIR / "boxplot_comparison.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    logger.info(f"Box plot saved: {output_path}")
    return output_path


def plot_component_breakdown(output_path: Path | None = None) -> Path:
    """
    Stacked bar chart: breakdown of F into Q̄, Rhyme, Structure components.
    """
    if not CSV_PER_RUN_SUMMARY.exists():
        return Path()

    # Load generation data for component scores
    if not CSV_PER_GENERATION.exists():
        return Path()

    data = []
    with open(CSV_PER_GENERATION, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            data.append(row)

    if not data:
        return Path()

    # Get the final generation for each run
    last_gen = {}
    for row in data:
        key = row["run_id"]
        gen = int(row["generation"])
        if key not in last_gen or gen > last_gen[key]["generation"]:
            last_gen[key] = {
                "generation": gen,
                "ea": row["ea"],
                "poem_type": row["poem_type"],
                "Q_bar": float(row["Q_bar"]),
                "Rhyme": float(row["Rhyme"]),
                "Structure": float(row["Structure"]),
            }

    # Group by (ea, poem_type)
    groups = defaultdict(lambda: {"Q_bar": [], "Rhyme": [], "Structure": []})
    for info in last_gen.values():
        key = (info["ea"], info["poem_type"])
        groups[key]["Q_bar"].append(info["Q_bar"])
        groups[key]["Rhyme"].append(info["Rhyme"])
        groups[key]["Structure"].append(info["Structure"])

    import statistics
    labels = []
    q_means = []
    r_means = []
    s_means = []

    for (ea, pt), scores in sorted(groups.items()):
        labels.append(f"{'GA' if ea == 'ga' else 'NSGA-II'}\n{pt.capitalize()}")
        q_means.append(statistics.mean(scores["Q_bar"]) * 0.5)   # weighted
        r_means.append(statistics.mean(scores["Rhyme"]) * 0.25)
        s_means.append(statistics.mean(scores["Structure"]) * 0.25)

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(labels))
    width = 0.5

    ax.bar(x, q_means, width, label="Q̄ (×0.5)", color="#3498DB")
    ax.bar(x, r_means, width, bottom=q_means, label="Rhyme (×0.25)", color="#2ECC71")
    ax.bar(x, s_means, width,
           bottom=[q + r for q, r in zip(q_means, r_means)],
           label="Structure (×0.25)", color="#E67E22")

    ax.set_ylabel("Weighted Contribution to F")
    ax.set_title("Fitness Component Breakdown")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()

    if output_path is None:
        output_path = CHARTS_DIR / "component_breakdown.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    logger.info(f"Component breakdown chart saved: {output_path}")
    return output_path


def generate_all_charts() -> list[Path]:
    """Generate all analysis charts."""
    paths = []

    p = plot_convergence_chart()
    if p and p.exists():
        paths.append(p)

    p = plot_boxplot_comparison()
    if p and p.exists():
        paths.append(p)

    p = plot_component_breakdown()
    if p and p.exists():
        paths.append(p)

    logger.info(f"Generated {len(paths)} charts")
    return paths
