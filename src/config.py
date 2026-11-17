"""
Central configuration for the EA-Poetry project.

All settings, model configs, rate limits, and paths are defined here.
API keys are loaded from .env file.
"""

import os
from pathlib import Path
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()

# ── Configurable Budget Settings ──────────────────────────────────────────────
# These settings are sized for the CURRENT free-tier Groq budget, not a
# permanent choice. Switching back later should be a one-line edit each.
# Revert POPULATION_SIZE to 10 if a paid/higher-throughput LLM becomes available.
POPULATION_SIZE = 6
# Revert GENERATION_CAP to 10 under the same condition.
GENERATION_CAP = 5
# Expand toward Anger, Love first if budget allows.
EMOTIONS = ["Joy", "Sorrow", "Fear"]

# ── Experiment phase switch ───────────────────────────────────────────────────
# Phase 1 (default): the pipeline exactly as used for the Phase I report.
# Phase 2: set the environment variable EA_PHASE=2 (run_grid.py --phase2 and
# run_interactive.py --phase2 do this for you). Phase 2 changes ONLY the
# measurement, never the algorithms:
#   1. the judge scores each poem JUDGE_REPEATS times and the scores are averaged
#   2. curly apostrophes are normalised before syllable and rhyme scoring
#   3. logs are written to output/logs_phase2/ so Phase I logs stay untouched
EXPERIMENT_PHASE = os.getenv("EA_PHASE", "1").strip()
PHASE2 = EXPERIMENT_PHASE == "2"
JUDGE_REPEATS = max(1, int(os.getenv("JUDGE_REPEATS", "3" if PHASE2 else "1")))
NORMALIZE_APOSTROPHES = os.getenv(
    "NORMALIZE_APOSTROPHES", "1" if PHASE2 else "0"
).strip() == "1"

# ── Paths ────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
LOGS_DIR = OUTPUT_DIR / ("logs_phase2" if PHASE2 else "logs")
CHARTS_DIR = OUTPUT_DIR / "charts"
TABLES_DIR = OUTPUT_DIR / "tables"

# Ensure output dirs exist
for d in [LOGS_DIR, CHARTS_DIR, TABLES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ── API Keys ─────────────────────────────────────────────────────────────────

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# ── Model Configurations ────────────────────────────────────────────────────

@dataclass(frozen=True)
class ModelConfig:
    """Configuration for a single API model."""
    name: str                   # Human-readable label
    model_id: str               # The `model` field sent in the API call
    endpoint: str               # Base URL
    api_key_env: str            # Which key to use
    rpm: int                    # Requests per minute
    rpd: int                    # Requests per day
    tpm: int                    # Tokens per minute
    tpd: int                    # Tokens per day
    max_output_tokens: int = 2048

    @property
    def api_key(self) -> str:
        if self.api_key_env == "NVIDIA_API_KEY":
            return NVIDIA_API_KEY
        elif self.api_key_env == "GROQ_API_KEY":
            return GROQ_API_KEY
        return ""


# ── NVIDIA Generator Model (quality-critical, interactive tool, Section 4) ───
NVIDIA_GENERATOR_MODEL_ID = "deepseek-ai/deepseek-v4.1-flash"

NVIDIA_GENERATOR = ModelConfig(
    name="NVIDIA Generator",
    model_id=NVIDIA_GENERATOR_MODEL_ID,
    endpoint="https://integrate.api.nvidia.com/v1",
    api_key_env="NVIDIA_API_KEY",
    rpm=40,
    rpd=5000,        # conservative estimate on credit pool
    tpm=100_000,     # NVIDIA doesn't enforce TPM the same way; generous estimate
    tpd=5_000_000,
    max_output_tokens=300,
)

# Generator — bulk (statistical grid, Section 8)
GPT_OSS_120B = ModelConfig(
    name="GPT-OSS-120B (Groq)",
    model_id="openai/gpt-oss-120b",
    endpoint="https://api.groq.com/openai/v1",
    api_key_env="GROQ_API_KEY",
    rpm=30,
    rpd=1000,
    tpm=8000,
    tpd=200_000,
    max_output_tokens=1200,
)

# Judge (Q̄ scoring, both layers)
QWEN_27B = ModelConfig(
    name="Qwen3.8-27B (Groq)",
    model_id="qwen/qwen3.8-27b",
    endpoint="https://api.groq.com/openai/v1",
    api_key_env="GROQ_API_KEY",
    rpm=30,
    rpd=1000,
    tpm=8000,
    tpd=1_000_000,
    max_output_tokens=1024,
)


# ── EA Parameters (Section 3) ───────────────────────────────────────────────

@dataclass(frozen=True)
class EAParams:
    """Evolutionary algorithm parameters — shared between GA and NSGA-II."""
    population_size: int = POPULATION_SIZE
    mutations_per_generation: int = 5
    max_generations: int = GENERATION_CAP
    convergence_threshold: float = 0.01
    convergence_patience: int = 2      # consecutive stall generations before stopping
    max_interactive_attempts: int = 3  # max retries on "bad" verdict


EA_PARAMS = EAParams()

# ── Fitness Weights (Section 7) ──────────────────────────────────────────────

FITNESS_WEIGHT_Q = 0.50
FITNESS_WEIGHT_RHYME = 0.25
FITNESS_WEIGHT_STRUCTURE = 0.25

# ── Emotions (Section 5) ─────────────────────────────────────────────────────

# EMOTIONS defined at the top of the file.

# ── Poem Types (Section 2) ───────────────────────────────────────────────────

POEM_TYPES = ["haiku", "limerick"]

# ── EA Types (Section 3) ─────────────────────────────────────────────────────

EA_TYPES = ["ga", "nsga2"]

# ── Grid Parameters (Section 8) ──────────────────────────────────────────────

GRID_RUNS_PER_CELL = 5
# Phase 2 grid: the six Phase I scenarios (one per poem type x emotion)
PHASE2_SCENARIOS_PATH = DATA_DIR / "prompts" / "phase1_scenarios.yaml"

# ── Haiku Structural Rules ───────────────────────────────────────────────────

HAIKU_SYLLABLES = [5, 7, 5]
HAIKU_RHYME_BASELINE = 0.5  # unrhymed haiku gets 0.5; rhyming can reach 1.0

# ── Limerick Structural Rules ────────────────────────────────────────────────

LIMERICK_LINE_COUNT = 5
LIMERICK_BEAT_PATTERN = [3, 3, 2, 2, 3]  # metrical feet per line (anapestic)
LIMERICK_SYLLABLE_TARGET = [8, 8, 5, 5, 8]  # expected syllable counts (~2.67 syl/foot)
# Rhyme scheme AABBA — lines 1,2,5 rhyme; lines 3,4 rhyme

# ── CSV File Paths ────────────────────────────────────────────────────────────

CSV_PER_GENERATION = LOGS_DIR / "per_generation.csv"
CSV_PER_RUN_SUMMARY = LOGS_DIR / "per_run_summary.csv"
CSV_HUMAN_FEEDBACK = LOGS_DIR / "human_feedback.csv"
CSV_EXPERT_REVIEW = LOGS_DIR / "expert_review.csv"
CSV_GRID_RUNS = LOGS_DIR / "grid_runs.csv"
CSV_GRID_CANDIDATES = LOGS_DIR / "grid_candidates.csv"
