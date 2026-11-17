# NSGA-II + Haiku + Sorrow — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_haiku_Sorrow_96240585` |
| **Attempt Number** | 1 of 3 (Accepted) |
| **Status / Verdict** | `good` (User accepted at Attempt 1) |
| **Date** | 2026-10-15 |
| **Start Time** | 15:44:39 IST |
| **Completion Time** | 15:45:49 IST |
| **Wall-Clock Duration** | 1m 10s (70s) |
| **Time to Final Poem** | **1m 10s** |
| **Algorithm** | NSGA-II (Multi-objective non-dominated sorting on $(\bar{Q}, R)$ with crowding distance) |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable structure) |
| **Target Emotion** | Sorrow |
| **Scenario Prompt** | *"an old photograph curling at the edges in a drawer nobody opens anymore"* |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Judge Model** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Generations Executed** | 3 (Gen 0, Gen 1, Gen 2) |
| **Stopping Rule** | Convergence ($\Delta F < 0.01$ for 2 consecutive generations) |
| **Mutation Integrity Note** | Pre-fix parser: Gen 1 produced only 1 variant, Gen 2 produced only 1 variant |
| **Fitness Formulation** | $F = 0.50 \cdot \bar{Q} + 0.25 \cdot R + 0.25 \cdot S$ |

---

## 1. Winning Poem & Human Feedback

```text
Paper curls like tears,
forgotten faces linger,
loneliness folds.
```

| Metric | Score | Detail |
|---|---|---|
| **Poem ID** | `c1804d52-57a` | Attempt 1 of 3 |
| **Composite Fitness ($F$)** | **0.7853** | $0.50 \times 0.8500 + 0.25 \times 0.5000 + 0.25 \times 0.9412$ |
| **Quality ($\bar{Q}$)** | **0.8500** | Evaluated via `qwen/qwen3.8-27b` |
| **Rhyme ($R$)** | **0.5000** | Haiku baseline (unrhymed) |
| **Structure ($S$)** | **0.9412** | Near-perfect syllable structure (5-7-4) |
| **Pareto Rank** | **Rank 0** | Elite non-dominated individual |
| **Human Verdict** | **good** | Accepted at Attempt 1 (Logged 15:46:39 IST) |

---

## 2. Evolutionary Trajectory

- **Generation 0 (15:45:40 IST):** Best $F = 0.7853$ ($\bar{Q}=0.8500, R=0.5000, S=0.9412$) — NSGA-II elite selected: `c1804d52-57a` (Rank 0). Initial population candidates ranged from $F=0.5100$ to $F=0.7853$.
- **Generation 1 (15:45:47 IST):** Best $F = 0.7853$ ($\bar{Q}=0.8500, R=0.5000, S=0.9412$) — Elite `c1804d52-57a` retained; mutation variant scored $F=0.5100$; $\Delta F = 0.0000$.
- **Generation 2 (15:45:49 IST):** Best $F = 0.7853$ ($\bar{Q}=0.8500, R=0.5000, S=0.9412$) — Elite `c1804d52-57a` retained; mutation variant scored $F=0.4350$; $\Delta F = 0.0000$.
- **Stopping Rule Triggered:** Convergence criterion satisfied after 2 consecutive stall generations ($\Delta F < 0.01$, `deltas: ['0.0000', '0.0000']`). Loop halted at generation 2.

---

## 3. Comparison: GA vs NSGA-II (Haiku + Sorrow)

Matched pair executed sequentially on identical scenario:
> *"an old photograph curling at the edges in a drawer nobody opens anymore"*

| Metric | GA Run | NSGA-II Run |
|---|---|---|
| **Run ID** | `ga_haiku_Sorrow_ffac0b64` | `nsga2_haiku_Sorrow_96240585` |
| **Poem ID** | `a68b93f3-7fc` | `c1804d52-57a` |
| **Composite Fitness ($F$)** | **0.8000** | **0.7853** |
| **Quality ($\bar{Q}$)** | 0.8500 | 0.8500 |
| **Rhyme ($R$)** | 0.5000 | 0.5000 |
| **Structure ($S$)** | 1.0000 (5-7-5) | 0.9412 (5-7-4) |
| **Time to Final Poem** | **2m 04s** (124s) | **1m 10s** (70s) |
| **Total Generations** | 3 (Gens 0-2) | 3 (Gens 0-2) |
| **Stopping Reason** | Convergence ($\Delta F < 0.01 \times 2$) | Convergence ($\Delta F < 0.01 \times 2$) |
| **Verdict** | `good` (Attempt 1) | `good` (Attempt 1) |
| **Acceptance Rate** | 1 of 1 | 1 of 1 |
