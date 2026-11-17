# NSGA-II + Haiku + Sorrow (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_haiku_Sorrow_d885a208` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-10 |
| **Start Time** | 10:57:00 IST (05:27:00 UTC; IST minus 5h30m) |
| **Completion Time** | 11:01:06 IST (05:31:06 UTC; IST minus 5h30m) |
| **Verdict Logged Time** | 11:15:03 IST (2026-11-10T05:45:03.250867+00:00 UTC; IST minus 5h30m) |
| **Time to Final Poem** | 4m 06s (246.0s gross wall-clock, 10:57:00 → 11:01:06 IST) |
| **Total Rate-Limit Pause Time** | 3m 40.5s (220.50s across 11 rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **25.50s** (246.0s gross wall-clock − 220.50s rate-limit waits) |
| **Algorithm** | NSGA-II (non-dominated sorting on Quality $\bar{Q}$ and Rhyme $R$; Structure $S \ge 0.30$ feasibility constraint) |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ (scalar composite tracked for convergence & tie-breaking) |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable target) |
| **Target Emotion** | Sorrow |
| **Scenario** | an old photograph curling at the edges in a drawer nobody opens anymore |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Generations Executed** | 5 (Gen 0, 1, 2, 3, 4) |
| **Termination Reason** | Reached maximum generation cap 5 (`Stopping: reached max generation 5`) |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as sole Front 0 member of final pool` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`9b04d3ac-306`) was confirmed as the sole member of Front 0 in the final generation pool (`Final pool Front 0 members: [9b04d3ac-306 (F=0.821, Q̄=0.950, R=0.500)]`). |
| **Presented Poem vs. CSV Tracker Discrepancy** | **Discrepancy Documented:** The presented poem is `9b04d3ac-306` ($F=0.8206, \bar{Q}=0.9500, R=0.5000, S=0.8824$), selected as the non-dominated Front 0 member of the final generation pool. The CSV's last row (`per_generation.csv` Gen 4, line 102) records `2a5d704c-719` ($F=0.8250, \bar{Q}=0.9000, R=0.5000, S=1.0000$), because `per_generation.csv` tracks historical `best_poem_overall` across all generations (where $0.8250 > 0.8206$), whereas `winning_poem` is selected from Front 0 of the final active generation pool. |
| **Crowding Distance Provenance** | Pareto rank 0 membership is recorded in log lines; individual crowding distance numerical values were **computed afterwards from code** (`src/ea/nsga2.py::compute_crowding_distance`) as the application log outputs front memberships but not raw crowding distance floats. |
| **Historical Comparison Tag** | **Redo of pre-fix run `nsga2_haiku_Sorrow_96240585`** under post-fix code with full candidate IDs, pause tracking, and parser verification. Pre-fix run data remains completely untouched. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Memory’s thin skin
Edges curl, a quiet gasp
Drawer stays shut, cold
```

| Metric | Value |
|---|---|
| **Poem ID** | `9b04d3ac-306` |
| **Composite Fitness ($F$)** | **0.8206** (displayed as 0.821) |
| **Quality ($\bar{Q}$)** | **0.9500** (displayed as 0.950) |
| **Rhyme ($R$)** | **0.5000** (displayed as 0.500; unrhymed haiku baseline) |
| **Structure ($S$)** | **0.8824** (displayed as 0.882; syllables [6, 7, 4]) |
| **Syllables per line** | Line 1: 6 (*Me-mo-ry’s thin skin*)<br>Line 2: 7 (*Ed-ges curl, a qui-et gasp*)<br>Line 3: 4 (*Draw-er stays shut, cold*) |
| **Line Count** | 3 (target: 3) |
| **Feasible ($S \ge 0.30$)** | **Yes** ($S = 0.8824 \ge 0.30$) |
| **Generation Created** | Generation 3 (Variant 4) |
| **Pareto Rank in Final Pool** | **Rank 0** (Non-dominated; confirmed in log: `Final pool Front 0 members: [9b04d3ac-306 (F=0.821, Q̄=0.950, R=0.500)]`) |
| **Crowding Distance in Final Pool** | $\infty$ (`inf`; computed afterwards from code via `compute_crowding_distance`; boundary point of single-member Front 0) |
| **Selection Rule** | Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`, confirmed in `src/ea/nsga2.py` lines 309–313) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts candidates on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is enforced as a feasibility constraint ($S \ge 0.30$). Composite fitness $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for convergence stopping and within-front selection.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 10:57:03 IST / 05:27:03 UTC):** Generated Candidates 1–5 (all 3 lines each).
- **Batch 2 (Call 2, 10:57:03 IST / 05:27:03 UTC):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 were feasible ($S \ge 0.30$) and had unrhymed baseline ($R = 0.5000$).

### Candidate 1 (Batch 1, Candidate #1) — ID: `56d55f51-5b1`

```text
Faded smiles whisper
Edges curl like wilted leaves
Drawer stays closed
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 0.882 | 0.7456 | Yes | 3 | [5, 7, 3] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 3 & 4 on $\bar{Q}$ |

### Candidate 2 (Batch 1, Candidate #2) — ID: `68bf887f-701`

```text
Dust clings to old joy
Curling corners weep soft in
Silence fills the void
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 1.000 | 0.7750 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | 0.0 (computed from code) | Dominated by Candidates 3 & 4 on $\bar{Q}$ |

### Candidate 3 (Batch 1, Candidate #3) — Gen 0 NSGA-II Elite (ID: `e3cc6a72-5fb`)

```text
Greyed faces slip out
Edges curl, time's cold hand still
Drawer stays shut still
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.850** | **0.500** | **0.941** | **0.7853** | **Yes** | 3 | [5, 7, 4] | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated Front 0 member. Selected Gen 0 Elite.** |

### Candidate 4 (Batch 1, Candidate #4) — ID: `2d2fa324-49e`

```text
Lost laughter dies slow
Curling paper sighs alone
Empty drawer weeps
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.850** | **0.500** | **0.941** | **0.7853** | **Yes** | 3 | [5, 7, 4] | 0 | **Rank 0** (computed from code) | $\infty$ (computed from code) | **Non-dominated Front 0 co-member** |

### Candidate 5 (Batch 1, Candidate #5) — ID: `804e1128-f30`

```text
Sunlight never finds
Edges brown, memories fray
Sorrow stays inside
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 0.500 | 1.000 | 0.6750 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Ranks 0 & 1 |

### Candidate 6 (Batch 2, Candidate #1) — ID: `c8ce688b-6d5`

```text
Faded paper weeps
Edges curl in drawer's dust
Forgotten smiles fade
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 0.941 | 0.7603 | Yes | 3 | [5, 6, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 3 & 4 on $\bar{Q}$ |

### Gen 0 Summary Table

| # | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Pareto Rank | Crowding Dist | Status |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `56d55f51-5b1` | *"Faded smiles whisper"* | 0.800 | 0.500 | 0.882 | 0.7456 | 3 | [5, 7, 3] | Rank 1 (code) | $\infty$ (code) | Dominated |
| 2 | `68bf887f-701` | *"Dust clings to old joy"* | 0.800 | 0.500 | 1.000 | 0.7750 | 3 | [5, 7, 5] | Rank 1 (code) | 0.0 (code) | Dominated |
| 3 | `e3cc6a72-5fb` | *"Greyed faces slip out"* | **0.850** | **0.500** | **0.941** | **0.7853** | 3 | [5, 7, 4] | **Rank 0** (log) | $\infty$ (code) | **Selected Gen 0 Elite (Front 0)** |
| 4 | `2d2fa324-49e` | *"Lost laughter dies slow"* | **0.850** | **0.500** | **0.941** | **0.7853** | 3 | [5, 7, 4] | **Rank 0** (code) | $\infty$ (code) | Front 0 co-member |
| 5 | `804e1128-f30` | *"Sunlight never finds"* | 0.600 | 0.500 | 1.000 | 0.6750 | 3 | [5, 7, 5] | Rank 2 (code) | $\infty$ (code) | Dominated |
| 6 | `c8ce688b-6d5` | *"Faded paper weeps"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 6, 5] | Rank 1 (code) | $\infty$ (code) | Dominated |

* **Gen 0 Front 0 Members:** `e3cc6a72-5fb` and `2d2fa324-49e` (both $\bar{Q}=0.8500, R=0.5000$).
* **Gen 0 Elite Selected:** Candidate 3 (`e3cc6a72-5fb`, Rank 0, $F = 0.7853$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Evolution

### Generation 1

Elite parent `e3cc6a72-5fb` was mutated into 5 variants.
- Mutation retries: **0** (5 valid variants returned on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Mutation Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Pareto Rank | Crowding Dist | NSGA-II Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `e3cc6a72-5fb` | *"Greyed faces slip out"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | **Rank 0** (log) | $\infty$ (code) | **Retained as NSGA-II Elite** |
| Variant 1 | `691a91a8-cd4` | *"Faded smile fades slow"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 0 (code) | 0.0 (code) | Front 0 member; new best-F ($0.8000$) |
| Variant 2 | `62325d8e-b8f` | *"Silent portrait weeps"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 8, 5] | Rank 1 (code) | $\infty$ (code) | Dominated on $\bar{Q}$ |
| Variant 3 | `98819525-3de` | *"Dusty grin decays"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 0 (code) | 0.0 (code) | Front 0 member; tied best-F |
| Variant 4 | `e3408e1f-271` | *"Aged photo trembles"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 0 (code) | 0.0 (code) | Front 0 member; tied best-F |
| Variant 5 | `afb9bf1c-98d` | *"Forgotten smile cracks"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 0 (code) | $\infty$ (code) | Front 0 member; tied best-F |

* **Elite Selection:** Parent `e3cc6a72-5fb` retained as elite (`rank=0`).
* **Front 0 Members:** 5 individuals (`e3cc6a72-5fb`, `691a91a8-cd4`, `98819525-3de`, `e3408e1f-271`, `afb9bf1c-98d`; all $\bar{Q}=0.8500, R=0.5000$).
* **Best-F Tracker & $\Delta F$:** Best-F improved from $0.7853$ to $0.8000$ (`691a91a8-cd4`). $\Delta F = +0.0147 \ge 0.01$. Patience counter reset to 0.

---

### Generation 2

Elite parent `e3cc6a72-5fb` was mutated into 5 variants.
- **Mutation retries: 1**
  - Attempt 1 (10:59:04 IST): Returned 0 valid variants (empty API completion).
  - Attempt 2 (10:59:06 IST): Succeeded on attempt 2/3 with 5 valid variants.
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Mutation Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Pareto Rank | Crowding Dist | NSGA-II Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `e3cc6a72-5fb` | *"Greyed faces slip out"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | Rank 1 (code) | $\infty$ (code) | Dominated by Variant 5 on $\bar{Q}$ |
| Variant 1 | `eff97983-ef4` | *"Faded smiles decay"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 1 (code) | 0.0 (code) | Dominated by Variant 5 on $\bar{Q}$ |
| Variant 2 | `1ed09d56-913` | *"Dusty portrait sighs"* | 0.750 | 0.500 | 1.000 | 0.7500 | 3 | [5, 7, 5] | Rank 2 (code) | $\infty$ (code) | Dominated |
| Variant 3 | `7fff060b-9cd` | *"Sunken eyes stare mute"* | 0.750 | 0.500 | 1.000 | 0.7500 | 3 | [5, 7, 5] | Rank 2 (code) | $\infty$ (code) | Dominated |
| Variant 4 | `e18005f1-e8f` | *"Forgotten smile wanes"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 1 (code) | $\infty$ (code) | Dominated by Variant 5 on $\bar{Q}$ |
| Variant 5 | `2a5d704c-719` | *"Ghost of youth crumpled"* | **0.900** | **0.500** | **1.000** | **0.8250** | 3 | [5, 7, 5] | **Rank 0** (log) | $\infty$ (code) | **Sole Front 0 member. New NSGA-II Elite.** |

* **Elite Selection:** Variant 5 (`2a5d704c-719`) achieved $\bar{Q} = 0.9000$, strictly dominating all other candidates in the pool. Selected as the new NSGA-II elite parent for Generation 3.
* **Front 0 Members:** Sole member `2a5d704c-719` ($\bar{Q}=0.9000, R=0.5000$).
* **Best-F Tracker & $\Delta F$:** Best-F improved from $0.8000$ to $0.8250$ (`2a5d704c-719`). $\Delta F = +0.0250 \ge 0.01$. Patience counter reset to 0.

---

### Generation 3

Elite parent `2a5d704c-719` ($\bar{Q}=0.900, R=0.500, S=1.000, F=0.8250$) was mutated into 5 variants.
- Mutation retries: **0** (5 valid variants returned on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Mutation Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Pareto Rank | Crowding Dist | NSGA-II Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `2a5d704c-719` | *"Ghost of youth crumpled"* | 0.900 | 0.500 | 1.000 | 0.8250 | 3 | [5, 7, 5] | Rank 1 (code) | $\infty$ (code) | Dominated by Variant 4 on $\bar{Q}$ |
| Variant 1 | `01fd79c5-0f3` | *"Faded faces fold"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | Rank 2 (code) | $\infty$ (code) | Dominated |
| Variant 2 | `38dbbe01-7bd` | *"Dust‑kissed portrait sighs"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 2 (code) | 0.0 (code) | Dominated |
| Variant 3 | `9cc0bfd0-aff` | *"Old glass eyes crease up"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 8, 5] | Rank 2 (code) | $\infty$ (code) | Dominated |
| Variant 4 | `9b04d3ac-306` | *"Memory’s thin skin"* | **0.950** | **0.500** | **0.882** | **0.8206** | 3 | [6, 7, 4] | **Rank 0** (log) | $\infty$ (code) | **Sole Front 0 member. New NSGA-II Elite.** |
| Variant 5 | `c550d6d4-cb1` | *"Worn photograph bends"* | 0.900 | 0.500 | 1.000 | 0.8250 | 3 | [5, 7, 5] | Rank 1 (code) | $\infty$ (code) | Dominated by Variant 4 on $\bar{Q}$ |

* **Elite Selection:** Variant 4 (`9b04d3ac-306`) achieved $\bar{Q} = 0.9500$, strictly dominating all other candidates in the pool. Selected as the new NSGA-II elite parent for Generation 4 despite slightly lower composite $F$ ($0.8206 < 0.8250$).
* **Front 0 Members:** Sole member `9b04d3ac-306` ($\bar{Q}=0.9500, R=0.5000$).
* **Best-F Tracker & $\Delta F$:** Best-F remained $0.8250$ (`2a5d704c-719` tied with `c550d6d4-cb1`). $\Delta F = 0.0000 < 0.01$. Patience counter incremented to **1**.

---

### Generation 4 (Final Generation)

Elite parent `9b04d3ac-306` ($\bar{Q}=0.950, R=0.500, S=0.882, F=0.8206$) was mutated into 5 variants.
- Mutation retries: **0** (5 valid variants returned on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Mutation Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Pareto Rank | Crowding Dist | NSGA-II Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `9b04d3ac-306` | *"Memory’s thin skin"* | **0.950** | **0.500** | **0.882** | **0.8206** | 3 | [6, 7, 4] | **Rank 0** (log) | $\infty$ (code) | **Sole Front 0 member. Retained as Elite & Presented Poem** |
| Variant 1 | `eb1fedb5-229` | *"Faded smile unspools"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [6, 7, 5] | Rank 1 (code) | $\infty$ (code) | Dominated on $\bar{Q}$ |
| Variant 2 | `ced7fc8c-6f8` | *"Dusty frame breathes low"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 1 (code) | 0.0 (code) | Dominated on $\bar{Q}$ |
| Variant 3 | `843203b6-ad6` | *"Old portrait weeps soft"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Rank 1 (code) | 0.0 (code) | Dominated on $\bar{Q}$ |
| Variant 4 | `008ba5d7-d74` | *"Time’s ink blurs and bends"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [6, 7, 5] | Rank 1 (code) | $\infty$ (code) | Dominated on $\bar{Q}$ |
| Variant 5 | `90e38528-49e` | *"Cracked photo sighs cold"* | 0.800 | 0.500 | 1.000 | 0.7750 | 3 | [5, 7, 5] | Rank 2 (code) | $\infty$ (code) | Dominated |

* **Final Pool Front 0 Members:** Logged as `[9b04d3ac-306 (F=0.821, Q̄=0.950, R=0.500)]`.
* **Final Presentation Selection:** Selected highest-$F$ poem from Front 0 $\rightarrow$ `9b04d3ac-306` ($F = 0.8206$).
* **Stopping:** Reached maximum generation cap 5 (`Stopping: reached max generation 5`).

---

## 4. Stopping Rule & Best Front Quality Audit

### Trajectory of Best Front Quality Across Generations

| Generation | Best Front Quality ($\max \bar{Q}_{\text{Front 0}}$) | Best $F$ Tracked (All-time) | Front 0 Members Count | $\Delta F$ Tracker | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8500 | 0.7853 | 2 (`e3cc6a72-5fb`, `2d2fa324-49e`) | — | 0 | Continue |
| 1 | 0.8500 | 0.8000 | 5 (`e3cc6a72-5fb`, `691a91a8-cd4`, `98819525-3de`, `e3408e1f-271`, `afb9bf1c-98d`) | +0.0147 | 0 | Continue ($\Delta F \ge 0.01$; patience reset to 0) |
| 2 | **0.9000** | 0.8250 | 1 (`2a5d704c-719`) | +0.0250 | 0 | Continue ($\Delta F \ge 0.01$; quality rose to 0.900) |
| 3 | **0.9500** | 0.8250 | 1 (`9b04d3ac-306`) | 0.0000 | 1 | Continue (patience reaches 1; quality rose to 0.950) |
| 4 | **0.9500** | 0.8250 | 1 (`9b04d3ac-306`) | 0.0000 | 2 | **STOP — Reached max generation 5** |

### Audit of Quality Trajectory vs Termination

- **Did the run stop while the best front's quality was still rising?**
  - **No.** Best front quality rose steadily from Gen 0 (0.8500) $\rightarrow$ Gen 1 (0.8500) $\rightarrow$ Gen 2 (0.9000) $\rightarrow$ Gen 3 (0.9500), and remained at peak quality (0.9500) through Gen 4.
  - The run terminated at Generation 4 because it reached the generation cap of 5 (`Stopping: reached max generation 5`). Peak quality $\bar{Q} = 0.9500$ was preserved into the final pool.

**Verbatim Log Confirmation:**
```text
11:01:06 | INFO    | src.ea.nsga2 |   Gen 4 | NSGA-II elite: Poem(id=9b04d3ac-306, F=0.821, Q̄=0.950, R=0.500, S=0.882) (rank=0) | Best-F: 0.825
11:01:06 | INFO    | src.ea.common | Stopping: reached max generation 5
11:01:06 | INFO    | src.ea.nsga2 |   Final pool Front 0 members: [9b04d3ac-306 (F=0.821, Q̄=0.950, R=0.500)]
11:01:06 | INFO    | src.ea.nsga2 |   Final presentation: selected highest-F poem from Front 0 -> 9b04d3ac-306 (F=0.821)
11:01:06 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_haiku_Sorrow_d885a208 ═══ Generations: 5 | Final F=0.821
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 5 Mutation calls across 4 gens) | 7 | 2,073 | 4,013 | **6,086** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 20 mutation variants across 4 gens) | 26 | 9,409 | 1,194 | **10,603** |
| **Total** | | **33** | **11,482** | **5,207** | **16,689** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 11 pauses totaling **220.50 seconds** (~3m 40.5s):
- **Waiting on `qwen/qwen3.8-27b`:** 7 pauses totaling **111.10s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 4 pauses totaling **109.40s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 10:57:09 | 51.3s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5504/6000 |
| 2 | 10:58:01 | 2.1s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4645/6000 |
| 3 | 10:58:07 | 1.6s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5786/6000 |
| 4 | 10:58:09 | 52.4s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5246/6000 |
| 5 | 10:59:07 | 1.8s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5621/6000 |
| 6 | 10:59:09 | 52.4s | `openai/gpt-oss-120b` | RPM=7/25 TPM=5621/6000 |
| 7 | 11:00:02 | 2.3s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5620/6000 |
| 8 | 11:00:06 | 0.7s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5787/6000 |
| 9 | 11:00:07 | 2.5s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4704/6000 |
| 10 | 11:00:11 | 51.3s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5614/6000 |
| 11 | 11:01:03 | 2.1s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5786/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 10:57:00 → Completion 11:01:06):** 246.0s (4m 06s)
- **Total Rate-Limit Pause Time:** 220.50s (3m 40.5s)
- **Time to Final Poem excluding pauses:** **25.50s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 98–102)

```csv
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,0,0.7853,0.8500,0.5000,0.9412,"Greyed faces slip out | Edges curl, time's cold hand still | Drawer stays shut still"
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,1,0.8000,0.8500,0.5000,1.0000,Faded smile fades slow | Paper curls like wilted leaf | Drawer never opens
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,2,0.8250,0.9000,0.5000,1.0000,Ghost of youth crumpled | Paper curls like sighing wind | Drawer remains cold still
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,3,0.8250,0.9000,0.5000,1.0000,Ghost of youth crumpled | Paper curls like sighing wind | Drawer remains cold still
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,4,0.8250,0.9000,0.5000,1.0000,Ghost of youth crumpled | Paper curls like sighing wind | Drawer remains cold still
```

### `output/logs/per_run_summary.csv` (Line 27)

```csv
nsga2_haiku_Sorrow_d885a208,nsga2,haiku,Sorrow,0.8206,5,"Memory’s thin skin | Edges curl, a quiet gasp | Drawer stays shut, cold"
```

### `output/logs/human_feedback.csv` (Line 24 / Index 22)

```csv
2026-11-10T05:45:03.250867+00:00,9b04d3ac-306,haiku,nsga2,Sorrow,an old photograph curling at the edges in a drawer nobody opens anymore,1,good,"Memory’s thin skin | Edges curl, a quiet gasp | Drawer stays shut, cold",0.8206,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `2` (Sorrow)
   - Description: *"an old photograph curling at the edges in a drawer nobody opens anymore"*
3. **Execution:** Full evolutionary process ran over 5 generations (Gen 0 through Gen 4) in **4m 06s** gross wall-clock time (10:57:00 to 11:01:06 IST), with net generation active time of **25.50s** excluding pauses.
4. **Presentation & Selection:** Winning poem `9b04d3ac-306` ($F=0.8206, \bar{Q}=0.9500, R=0.5000, S=0.8824$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live at 11:15:03 IST (`2026-11-10T05:45:03.250867+00:00` UTC).
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `9b04d3ac-306` and verdict `good`.
7. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool exited cleanly with `Session complete. Goodbye!`.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Mutation retry warning event:** **1**
  - `10:59:04 | WARNING | src.ea.mutation | Mutation returned 0 valid variants (attempt 1/3). Retrying...`
  - Recovered on retry: `10:59:06 | INFO | src.ea.mutation | Mutation succeeded on attempt 2/3 with 5 variants.`

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All parsed batches produced complete 3-line haikus.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smiles whisper'`
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dust clings to old joy'`
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Greyed faces slip out'`
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Lost laughter dies slow'`
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Sunlight never finds'`
  - `10:57:03 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded paper weeps'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `10:58:05 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smile fades slow'`
  - `10:58:05 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Silent portrait weeps'`
  - `10:58:05 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dusty grin decays'`
  - `10:58:05 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Aged photo trembles'`
  - `10:58:05 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Forgotten smile cracks'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - Attempt 1: 0 variants (empty completion).
  - Attempt 2:
    - `10:59:06 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smiles decay'`
    - `10:59:06 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dusty portrait sighs'`
    - `10:59:06 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Sunken eyes stare mute'`
    - `10:59:06 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Forgotten smile wanes'`
    - `10:59:06 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Ghost of youth crumpled'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `11:00:02 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded faces fold'`
  - `11:00:02 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dust‑kissed portrait sighs'`
  - `11:00:02 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Old glass eyes crease up'`
  - `11:00:02 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Memory’s thin skin'`
  - `11:00:02 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Worn photograph bends'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 3 Discarded Lines:** 0.

- **Generation 4 (Mutation Variants):**
  - `11:00:11 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smile unspools'`
  - `11:00:11 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dusty frame breathes low'`
  - `11:00:11 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Old portrait weeps soft'`
  - `11:00:11 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Time’s ink blurs and bends'`
  - `11:00:11 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Cracked photo sighs cold'`
  - **Gen 4 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 4 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 2121–2149; 5 candidates)
- `initial_population_batch_2` (Lines 2150–2154; 1 candidate)
- `mutation` Gen 1 (Lines 2155–2183; 5 variants)
- `mutation` Gen 2 attempt 1 (Lines 2184–2186; 0 variants / blank retry)
- `mutation` Gen 2 attempt 2 (Lines 2187–2215; 5 variants)
- `mutation` Gen 3 (Lines 2216–2244; 5 variants)
- `mutation` Gen 4 (Lines 2245–2273; 5 variants)

