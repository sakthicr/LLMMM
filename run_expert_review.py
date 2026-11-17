"""
Entry point: Expert review collection script (Section 9).

Reads the human-feedback log, filters to "good"-verdict poems,
displays each one, captures a 1-5 rating + comment from the expert,
and writes to the expert-review log.

This is a dedicated collection script — not just the CSV schema existing.

Usage:
    python run_expert_review.py
"""

import logging
import sys

# Fix Windows console encoding — cp1252 cannot handle Unicode symbols
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

from src.logging_.csv_logger import (
    read_accepted_poems,
    get_reviewed_poem_ids,
    log_expert_review,
)

logger = logging.getLogger(__name__)
console = Console()


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("output/logs/expert_review.log", mode="a", encoding="utf-8"),
        ],
    )


def run_expert_review():
    """
    Interactive expert review workflow.

    1. Reads all "good"-verdict poems from human_feedback.csv
    2. Filters out already-reviewed poems (using expert_review.csv)
    3. Displays each poem and collects expert rating + comment
    4. Writes to expert_review.csv with the SAME poem_id
    """
    console.print(Panel(
        "[bold]Expert Review Collection[/bold]\n\n"
        "Rate each accepted poem on a scale of 1-5:\n"
        "  1 = Poor    2 = Below Average    3 = Average\n"
        "  4 = Good    5 = Excellent\n\n"
        "Add a brief comment explaining your rating.",
        border_style="blue",
    ))

    # Load accepted poems
    accepted = read_accepted_poems()
    if not accepted:
        console.print("[yellow]No accepted poems found in human_feedback.csv.[/yellow]")
        console.print("Run the interactive tool first to generate and accept poems.")
        return

    # Filter out already-reviewed poems
    reviewed_ids = get_reviewed_poem_ids()
    pending = [p for p in accepted if p["poem_id"] not in reviewed_ids]

    console.print(
        f"\nFound [bold]{len(accepted)}[/bold] accepted poems, "
        f"[bold]{len(reviewed_ids)}[/bold] already reviewed, "
        f"[bold green]{len(pending)}[/bold green] pending review.\n"
    )

    if not pending:
        console.print("[green]All accepted poems have been reviewed![/green]")
        return

    for i, poem_data in enumerate(pending, 1):
        console.print(f"\n{'─'*60}")
        console.print(
            f"[bold cyan]Poem {i}/{len(pending)}[/bold cyan] | "
            f"ID: {poem_data['poem_id']}"
        )

        # Show metadata
        info = Table(show_header=False, box=None, padding=(0, 2))
        info.add_row("Type:", poem_data["poem_type"].capitalize())
        info.add_row("EA:", poem_data["ea"].upper())
        info.add_row("Emotion:", poem_data["emotion"].capitalize())
        info.add_row("F Score:", f"{poem_data['F_score']:.4f}")
        console.print(info)

        # Show the poem
        poem_text = poem_data["poem_text"]
        console.print(Panel(
            poem_text,
            border_style="cyan",
            padding=(1, 3),
        ))

        # Collect rating
        rating = IntPrompt.ask(
            "[bold]Expert rating (1-5)[/bold]",
            choices=["1", "2", "3", "4", "5"],
        )

        # Collect comment
        comment = Prompt.ask(
            "[bold]Brief comment[/bold]",
            default="No comment",
        )

        # Log to expert_review.csv (using the SAME poem_id)
        log_expert_review(
            poem_id=poem_data["poem_id"],    # ← same ID as human_feedback.csv
            poem_type=poem_data["poem_type"],
            ea=poem_data["ea"],
            emotion=poem_data["emotion"],
            poem_text=poem_text,
            f_score=poem_data["F_score"],
            expert_rating=rating,
            comment=comment,
        )

        console.print(
            f"[green]✓ Saved: rating={rating}, poem_id={poem_data['poem_id']}[/green]"
        )

        # Option to stop early
        if i < len(pending):
            cont = Prompt.ask(
                "\n[dim]Continue to next poem?[/dim]",
                choices=["yes", "no"],
                default="yes",
            )
            if cont == "no":
                console.print(
                    f"\n[yellow]Stopped early. "
                    f"{len(pending) - i} poems remaining for review.[/yellow]"
                )
                break

    console.print(f"\n[bold green]Expert review session complete![/bold green]")


def main():
    setup_logging()
    try:
        run_expert_review()
    except KeyboardInterrupt:
        print("\nInterrupted. Partial reviews are saved.")


if __name__ == "__main__":
    main()
