"""
Interactive CLI tool for human-in-the-loop poem generation (Section 4).

RETRY BEHAVIOR (confirmed): When a poem is marked "bad," this calls the
FULL EA process again — a completely fresh population through ea/ga.py or
ea/nsga2.py, running through the normal stopping rule (ΔF < 0.01 for 2
consecutive generations, or generation 10). This is NOT a single quick
regeneration. Capped at 3 full EA attempts. If still rejected after 3,
log as a rejection and stop.

Uses the NVIDIA-hosted generator (DeepSeek-V4.1-Flash) for quality-critical generation.
"""

import asyncio
import logging
import sys

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from src.config import EA_PARAMS, EMOTIONS, POEM_TYPES, EA_TYPES
from src.ea.ga import run_ga
from src.ea.nsga2 import run_nsga2
from src.ea.common import generate_run_id
from src.api.groq_client import generate_poem_groq
from src.api.client import close_all_clients
from src.logging_.csv_logger import log_human_feedback, log_all_generations, log_run_summary

logger = logging.getLogger(__name__)
console = Console()


def _display_poem(poem, attempt: int, max_attempts: int) -> None:
    """Display the generated poem in a styled panel."""
    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_row("Type:", poem.poem_type.capitalize())
    info_table.add_row("Emotion:", poem.emotion.capitalize())
    info_table.add_row("EA:", "NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type)
    info_table.add_row("Fitness (F):", f"{poem.F:.3f}")
    info_table.add_row("Q̄:", f"{poem.Q_bar:.3f}")
    info_table.add_row("Rhyme:", f"{poem.Rhyme:.3f}")
    info_table.add_row("Structure:", f"{poem.Structure:.3f}")
    info_table.add_row("Attempt:", f"{attempt}/{max_attempts}")

    console.print()
    console.print(Panel(
        poem.text,
        title=f"[bold cyan]Generated {poem.poem_type.capitalize()}[/bold cyan]",
        subtitle=f"[dim]Poem ID: {poem.poem_id}[/dim]",
        border_style="cyan",
        padding=(1, 3),
    ))
    console.print(info_table)
    console.print()


async def _run_single_session(
    poem_type: str,
    ea_type: str,
    emotion: str,
    description: str,
) -> None:
    """
    Run a single interactive session.

    On "bad" verdict: reruns the FULL EA process (fresh population →
    generations → stopping rule). NOT a single regeneration.
    Capped at max_interactive_attempts (3) full EA runs.
    """
    max_attempts = EA_PARAMS.max_interactive_attempts

    # Choose the EA runner
    if ea_type == "ga":
        ea_runner = run_ga
    elif ea_type == "nsga2":
        ea_runner = run_nsga2
    else:
        console.print(f"[red]Unknown EA type: {ea_type}[/red]")
        return

    for attempt in range(1, max_attempts + 1):
        console.print(
            f"\n[bold yellow]━━━ Attempt {attempt}/{max_attempts} ━━━[/bold yellow]"
        )
        console.print(
            f"[dim]Running full {ea_type.upper()} process "
            f"(fresh population → evolution → stopping rule)...[/dim]"
        )

        # ── Run the FULL EA process ──────────────────────────────────────
        # This is a complete run: new population, full evolutionary loop,
        # normal stopping rule. Each "bad" retry starts completely fresh.
        run_id = generate_run_id(ea_type, poem_type, emotion)
        result = await ea_runner(
            poem_type=poem_type,
            emotion=emotion,
            description=description,
            generator_fn=generate_poem_groq,
            run_id=run_id,
        )

        best_poem = result.best_poem

        # Log generation data
        log_all_generations(result.generation_logs)
        log_run_summary(
            run_id=result.run_id,
            ea=ea_type,
            poem_type=poem_type,
            emotion=emotion,
            final_f=best_poem.F,
            generations_used=result.generations_used,
            best_poem=best_poem.text,
        )

        # Display the poem
        _display_poem(best_poem, attempt, max_attempts)

        # Get human verdict
        verdict = Prompt.ask(
            "[bold]Is this poem good?[/bold]",
            choices=["good", "bad"],
            default="good",
        )

        # Log the feedback (using poem's consistent poem_id)
        log_human_feedback(
            poem=best_poem,
            ea=ea_type,
            attempt_number=attempt,
            verdict=verdict,
        )

        if verdict == "good":
            console.print(
                f"[bold green]✓ Poem accepted![/bold green] "
                f"(ID: {best_poem.poem_id}, eligible for expert review)"
            )
            return

        # If bad and not last attempt
        if attempt < max_attempts:
            console.print(
                f"[yellow]Poem rejected. Will run a completely fresh "
                f"{ea_type.upper()} process...[/yellow]"
            )
        else:
            console.print(
                f"[bold red]✗ Maximum attempts ({max_attempts}) reached. "
                f"Logging as final rejection.[/bold red]"
            )


async def run_interactive_tool() -> None:
    """
    Main interactive loop.

    Presents 4 selections: poem type, EA type, emotion, description.
    Runs the selected EA's full process and handles good/bad feedback.
    """
    console.print(Panel(
        "[bold]EA-Poetry Interactive Tool[/bold]\n"
        "Compare GA vs NSGA-II for LLM-guided poem generation.\n"
        "Each attempt runs the FULL evolutionary process.",
        border_style="blue",
    ))

    while True:
        console.print("\n[bold cyan]─── New Session ───[/bold cyan]\n")

        # 1. Poem type
        console.print("[bold]Available poem types:[/bold]")
        for i, pt in enumerate(POEM_TYPES, 1):
            console.print(f"  {i}. {pt.capitalize()}")
        pt_idx = IntPrompt.ask(
            "Select poem type",
            choices=[str(i) for i in range(1, len(POEM_TYPES) + 1)],
        )
        poem_type = POEM_TYPES[pt_idx - 1]

        # 2. EA type
        console.print("\n[bold]Available algorithms:[/bold]")
        ea_labels = {"ga": "Genetic Algorithm (GA)", "nsga2": "NSGA-II"}
        for i, ea in enumerate(EA_TYPES, 1):
            console.print(f"  {i}. {ea_labels[ea]}")
        ea_idx = IntPrompt.ask(
            "Select algorithm",
            choices=[str(i) for i in range(1, len(EA_TYPES) + 1)],
        )
        ea_type = EA_TYPES[ea_idx - 1]

        # 3. Emotion
        console.print("\n[bold]Available emotions:[/bold]")
        for i, em in enumerate(EMOTIONS, 1):
            console.print(f"  {i}. {em.capitalize()}")
        em_idx = IntPrompt.ask(
            "Select emotion",
            choices=[str(i) for i in range(1, len(EMOTIONS) + 1)],
        )
        emotion = EMOTIONS[em_idx - 1]

        # 4. Description
        description = Prompt.ask(
            "\n[bold]Enter a description/scenario[/bold]"
        )

        if not description.strip():
            console.print("[red]Description cannot be empty.[/red]")
            continue

        # Run the session
        console.print(
            f"\n[bold]Running {ea_labels[ea_type]} for "
            f"{poem_type.capitalize()} | Emotion: {emotion.capitalize()}[/bold]"
        )

        await _run_single_session(poem_type, ea_type, emotion, description)

        # Continue?
        again = Prompt.ask(
            "\n[bold]Generate another poem?[/bold]",
            choices=["yes", "no"],
            default="yes",
        )
        if again == "no":
            break

    console.print("\n[bold blue]Session complete. Goodbye![/bold blue]")
