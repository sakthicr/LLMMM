# GA + Haiku + Sorrow — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_haiku_Sorrow_ffac0b64` |
| **Attempt Number** | 1 of 3 (Accepted) |
| **Status / Verdict** | `good` (User accepted at Attempt 1) |
| **Date** | 2026-10-15 |
| **Start Time** | 15:33:40 IST |
| **Completion Time** | 15:35:44 IST |
| **Wall-Clock Duration** | 2m 04s (124s) |
| **Time to Final Poem** | **2m 04s** |
| **Algorithm** | Genetic Algorithm (GA) — Single-objective elitist selection on composite fitness $F$ |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable structure) |
| **Target Emotion** | Sorrow |
| **Scenario Prompt** | *"an old photograph curling at the edges in a drawer nobody opens anymore"* |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Judge Model** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Generations Executed** | 3 (Gen 0, Gen 1, Gen 2) |
| **Stopping Rule** | Convergence ($\Delta F < 0.01$ for 2 consecutive generations) |
| **Mutation Integrity Note** | Pre-fix parser: Gen 1 produced only 1 variant |
| **Mutations Per Gen** | 5 variants from single elite parent |
| **Fitness Formulation** | $F = 0.50 \cdot \bar{Q} + 0.25 \cdot R + 0.25 \cdot S$ |

---

## 1. Winning Poem & Human Feedback

```text
Faded frame lies still
Edges curl like quiet tears
Forgotten drawer sighs
```

| Metric | Score | Detail |
|---|---|---|
| **Poem ID** | `a68b93f3-7fc` | Attempt 1 of 3 |
| **Composite Fitness ($F$)** | **0.8000** | $0.50 \times 0.8500 + 0.25 \times 0.5000 + 0.25 \times 1.0000$ |
| **Quality ($\bar{Q}$)** | **0.8500** | Evaluated via `qwen/qwen3.8-27b` |
| **Rhyme ($R$)** | **0.5000** | Haiku baseline (unrhymed) |
| **Structure ($S$)** | **1.0000** | Perfect 5-7-5 syllable count compliance |
| **Human Verdict** | **good** | Accepted at Attempt 1 (Logged 15:37:51 IST) |

---

## 2. Evolutionary Trajectory

- **Generation 0 (15:34:41 IST):** Best $F = 0.8000$ ($\bar{Q}=0.8500, R=0.5000, S=1.0000$) — Elite parent selected: `a68b93f3-7fc`. Initial population candidate scores ranged from $F=0.7000$ to $F=0.8000$.
- **Generation 1 (15:34:44 IST):** Best $F = 0.8000$ ($\bar{Q}=0.8500, R=0.5000, S=1.0000$) — Elite `a68b93f3-7fc` retained; mutation variant scored $F=0.5250$; $\Delta F = 0.0000$.
- **Generation 2 (15:35:44 IST):** Best $F = 0.8000$ ($\bar{Q}=0.8500, R=0.5000, S=1.0000$) — Elite `a68b93f3-7fc` retained; mutation variants scored up to $F=0.7850$; $\Delta F = 0.0000$.
- **Stopping Rule Triggered:** Convergence criterion satisfied after 2 consecutive stall generations ($\Delta F < 0.01$, `deltas: ['0.0000', '0.0000']`). Loop halted at generation 2.

---

## 3. Data Integrity & System Logging

- **`output/logs/per_run_summary.csv`:** Run logged with final $F=0.8000$, 3 generations.
- **`output/logs/per_generation.csv`:** Generations 0, 1, 2 logged with best individual tracking.
- **`output/logs/human_feedback.csv`:** Logged with timestamp `2026-10-15T10:07:51.293054+00:00`, verdict `good`, eligible for expert review.
