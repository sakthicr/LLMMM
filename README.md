# EA-Poetry: Comparative Study of GA vs NSGA-II for LLM-Guided Poem Generation

A Python project comparing two evolutionary algorithms — a **Genetic Algorithm (GA)** and **NSGA-II** — for LLM-guided poem generation, across two poem forms (**Haiku**, **Limerick**), using one shared fitness function and independent human + expert validation layers.

## Research Questions

- **RQ1**: Does NSGA-II's multi-objective search outperform a single-objective GA under a richer LLM-judged quality metric?
- **RQ2**: Does that answer hold consistently across two structurally different poem forms?
- **RQ3**: Does an evidence-based stopping rule support or contradict the base paper's untested 3-generation assumption?

## Quick Start

### 1. Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -e .

# Download NLTK data (CMUdict for syllable counting)
python -c "import nltk; nltk.download('cmudict')"
```

### 2. API Keys

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

| Key | Get it from |
|-----|------------|
| `NVIDIA_API_KEY` | [build.nvidia.com](https://build.nvidia.com) → API Keys (starts with `nvapi-`) |
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) → API Keys (starts with `gsk_`) |

### 3. Run

```bash
# Interactive tool (human-in-the-loop, uses NVIDIA generator)
python run_interactive.py

# Calibration check (score reference human poems)
python run_calibration.py

# Statistical grid (100 runs, uses Groq generator)
python run_grid.py              # Full grid
python run_grid.py --test       # Quick test (4 runs)

# Expert review collection
python run_expert_review.py

# Analysis (statistics + charts)
python run_analysis.py
```

## Project Structure

```
├── run_interactive.py          # Interactive tool entry point
├── run_grid.py                 # Statistical grid entry point
├── run_expert_review.py        # Expert review collection
├── run_analysis.py             # Statistics + charts
├── run_calibration.py          # Human-poem calibration
├── src/
│   ├── config.py               # All settings, model configs, rate limits
│   ├── api/                    # Async HTTP clients (NVIDIA, Groq)
│   ├── fitness/                # Structure, rhyme, quality (Q̄), composite F
│   ├── ea/                     # GA and NSGA-II engines
│   ├── prompts/                # LLM prompt templates
│   ├── interactive/            # CLI interactive tool
│   ├── grid/                   # Statistical grid runner
│   ├── analysis/               # Statistics, charts, calibration
│   └── logging_/               # CSV logging (4 output files)
├── data/
│   ├── prompts/                # Fixed descriptions per emotion
│   └── calibration/            # Reference human poems
└── output/
    ├── logs/                   # CSV output files
    ├── charts/                 # Generated charts
    └── tables/                 # Comparison tables
```

## Models

| Role | Model | Provider | Used for |
|------|-------|----------|----------|
| Generator (quality) | DeepSeek-V4.1-Flash | NVIDIA NIM | Interactive tool |
| Generator (bulk) | GPT-OSS-120B | Groq | Statistical grid |
| Judge | Qwen3.8-27B | Groq | Q̄ scoring everywhere |

## Fitness Function

```
F = 0.5 × Q̄ + 0.25 × Rhyme + 0.25 × Structure
```

- **Q̄** — LLM-judged quality (5 dimensions: emotion alignment, imagery, literary devices, originality, coherence)
- **Rhyme** — CMUdict-based phoneme matching (haiku: 0.5 baseline; limerick: AABBA scheme)
- **Structure** — Syllable/beat pattern compliance (haiku: 5-7-5; limerick: 3-3-2-2-3 beats)

## CSV Outputs

| File | Contents |
|------|----------|
| `per_generation.csv` | F, Q̄, Rhyme, Structure per generation per run |
| `per_run_summary.csv` | Final F and generations used per run |
| `human_feedback.csv` | Human good/bad verdicts with poem_id |
| `expert_review.csv` | Expert 1-5 ratings with same poem_id |

`poem_id` is consistent across `human_feedback.csv` and `expert_review.csv` for cross-referencing.

## License

Research use.
