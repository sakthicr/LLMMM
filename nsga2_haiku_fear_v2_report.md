# NSGA-II + Haiku + Fear (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_haiku_Fear_7e2df52b` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-09 (Run executed) / 2026-11-10 (Verdict recorded) |
| **Start Time** | 22:30:20 IST (17:00:20 UTC; IST minus 5h30m) |
| **Completion Time** | 22:34:25 IST (17:04:25 UTC; IST minus 5h30m) |
| **Verdict Logged Time** | 09:57:41 IST (2026-11-10T04:27:41.839461+00:00 UTC; IST minus 5h30m) |
| **Time to Final Poem** | 4m 05s (245.0s gross wall-clock, 22:30:20 → 22:34:25 IST) |
| **Total Rate-Limit Pause Time** | 2m 36.7s (156.70s across 10 rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **88.30s** (245.0s gross wall-clock − 156.70s rate-limit waits; active evaluation also included two transient 503 retry delays totaling 2.4s) |
| **Algorithm** | NSGA-II (non-dominated sorting on Quality $\bar{Q}$ and Rhyme $R$; Structure $S \ge 0.30$ feasibility constraint) |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ (scalar composite tracked for convergence & tie-breaking) |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable target) |
| **Target Emotion** | Fear |
| **Scenario** | Walking alone down an unlit street, hearing footsteps that match your pace exactly. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Generations Executed** | 5 (Gen 0, 1, 2, 3, 4) |
| **Termination Reason** | Reached maximum generation cap 5 (`Stopping: reached max generation 5`) |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as Front 0 member of final pool with highest composite F` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`a32548bc-8c4`) was confirmed as a Front 0 member of the final generation pool and selected as having the highest composite fitness $F = 0.7853$ (tied on Front 0 with co-members `eaec77f5-857` and `857f8a00-304`). |
| **Historical Comparison Tag** | **Redo of pre-fix runs `nsga2_haiku_Fear_ad80ed04` (rejected) and `nsga2_haiku_Fear_24f3cf25` (accepted)** under post-fix code with full candidate IDs, pause tracking, and parser verification. Pre-fix run data remains completely untouched. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Street empties, eyes blind
Footfalls mirror trembling beat
Silence shatters now
```

| Metric | Value |
|---|---|
| **Poem ID** | `a32548bc-8c4` |
| **Composite Fitness ($F$)** | **0.7853** (displayed as 0.785) |
| **Quality ($\bar{Q}$)** | **0.8500** (displayed as 0.850) |
| **Rhyme ($R$)** | **0.5000** (displayed as 0.500; unrhymed haiku baseline) |
| **Structure ($S$)** | **0.9412** (displayed as 0.941) |
| **Syllables per line** | Line 1: 5 (*Street emp-ties, eyes blind*)<br>Line 2: 8 (*Foot-falls mir-ror trem-bling beat*)<br>Line 3: 5 (*Si-lence shat-ters now*) |
| **Line Count** | 3 (target: 3) |
| **Feasible ($S \ge 0.30$)** | **Yes** ($S = 0.9412 \ge 0.30$) |
| **Generation Created** | Generation 0 (Candidate 2) |
| **Pareto Rank in Final Pool** | Rank 0 (Non-dominated; confirmed in log line: `Final pool Front 0 members: [a32548bc-8c4 (F=0.785, Q̄=0.850, R=0.500), eaec77f5-857 (F=0.785, Q̄=0.850, R=0.500), 857f8a00-304 (F=0.785, Q̄=0.850, R=0.500)]`) |
| **Crowding Distance in Final Pool** | $\infty$ (`inf`; computed afterwards from code via `compute_crowding_distance`; not recorded in logs) |
| **Front 0 Member with Highest $F$** | **Yes** (Tied on highest $F=0.7853$ in Front 0; selected as the elite parent preserved across all generations) |
| **Selection Rule** | Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`, confirmed in `src/ea/nsga2.py` lines 311–313) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts candidates on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is enforced as a feasibility constraint ($S \ge 0.30$). Composite fitness $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for convergence stopping and within-front selection.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 22:30:23 IST / 17:00:23 UTC):** Generated Candidates 1–5 (all 3 lines each).
- **Batch 2 (Call 2, 22:30:24 IST / 17:00:24 UTC):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 were feasible ($S \ge 0.30$) and had unrhymed baseline ($R = 0.5000$).

### Candidate 1 (Batch 1, Candidate #1) — ID: `4d797f46-26a`

```text
Lamplight gone, breath tight
Shadow steps keep pulse racing
Fear walks beside me
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 0.500 | 1.000 | 0.675 | Yes | 3 | [5, 7, 5] | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 2, 4, 5 on $\bar{Q}$ |

### Candidate 2 (Batch 1, Candidate #2) — Gen 0 NSGA-II Elite (ID: `a32548bc-8c4`)

```text
Street empties, eyes blind
Footfalls mirror trembling beat
Silence shatters now
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole Front 0 member. Gen 0 Elite.** |

### Candidate 3 (Batch 1, Candidate #3) — ID: `052594e0-91c`

```text
Midnight wind holds breath
Steps fall in rhythm, twin beat
Cold dread clings to soles
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 2 |

### Candidate 4 (Batch 1, Candidate #4) — ID: `4f80cce6-456`

```text
Alley yawns, dark drips
Footsteps sync, a hidden chase
Panic lights the night
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 2 on $\bar{Q}$ |

### Candidate 5 (Batch 1, Candidate #5) — ID: `3c25f00a-d85`

```text
Night's veil swallows sound
Echoes match my stride, unseen
Heart drums in the dark
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 2 on $\bar{Q}$ |

### Candidate 6 (Batch 2, Candidate #1) — ID: `43cfb4a0-131`

```text
Midnight street, alone
Echo steps fall in my stride
Shadow breathes behind
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 2 |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | NSGA-II Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `4d797f46-26a` | 0.600 | 0.500 | 1.000 | 0.675 | Yes | 3 | [5, 7, 5] | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| 2 | `a32548bc-8c4` | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Gen 0 Elite (Sole Front 0 Member)** |
| 3 | `052594e0-91c` | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| 4 | `4f80cce6-456` | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated |
| 5 | `3c25f00a-d85` | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated |
| 6 | `43cfb4a0-131` | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs** (the logger records only `rank=0` and Front 0 membership). All crowding distance values in this table were **computed afterwards from the code** using `compute_crowding_distance` from `src/ea/nsga2.py`. Because Candidate 2 was the sole member of Front 0, it received $\infty$ (`inf`).

* **Generation 0 Front 0 Members:** Candidate 2 (`a32548bc-8c4`).
* **Gen 0 Elite Selected:** Candidate 2 (`a32548bc-8c4`, $F=0.7853$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `a32548bc-8c4` ($\bar{Q}=0.850, R=0.500, S=0.941, F=0.7853$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `7161422c-dee` | *"Midnight lane, breath held"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Parent |
| Variant 2 | `5c59687c-2e9` | *"Empty curb, night veiled"* | 0.800 | 0.500 | 0.941 | 0.760 | Yes | 3 | [5, 8, 5] | Rank 1 (computed from code) | 0.0 (computed from code) | Dominated by Parent |
| Variant 3 | `33cb96bf-b22` | *"Dark road, lanterns none"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Parent |
| Variant 4 | `583e3584-d93` | *"Silent block, breath cold"* | 0.750 | 0.500 | 1.000 | 0.750 | Yes | 3 | [5, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 5 | `9ae68306-bbe` | *"Moonless path, shadows"* | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `a32548bc-8c4` | *"Street empties, eyes blind"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole Front 0. Gen 1 Elite.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`). Rank 0 for `a32548bc-8c4` is confirmed directly from the log line (`NSGA-II elite: Poem(id=a32548bc-8c4, ...) (rank=0)`).

* **Generation 1 Front 0 Members:** `a32548bc-8c4`.
* **NSGA-II Selection:** Parent `a32548bc-8c4` strictly dominated all 5 variants on Quality ($\bar{Q}=0.8500 > 0.8000$) with identical Rhyme ($R=0.5000$). Retained as elite parent for Generation 2.
* **Best-F Tracker & $\Delta F$:** In Gen 0, best-F was $0.7853$. In Gen 1, best-F remained $0.7853$. Thus $\Delta F = 0.0000 < 0.01$. Patience counter incremented to **1**.

---

### Generation 2

Elite parent `a32548bc-8c4` ($\bar{Q}=0.850, R=0.500, S=0.941, F=0.7853$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `e531e4fb-1ce` | *"Midnight lane, heart pounds"* | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 2 | `207ae122-237` | *"Dark road, lone footsteps"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (computed from code) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member.** |
| Variant 3 | `f5f93f7a-ecb` | *"Silent curb, pulse thuds"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Front 0 |
| Variant 4 | `3d5ea57c-8c9` | *"Empty lane, eyes shut"* | 0.800 | 0.500 | 0.941 | 0.760 | Yes | 3 | [5, 8, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Front 0 |
| Variant 5 | `d28edf15-414` | *"Night veil, heart stalls low"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (computed from code) | 0.0 (computed from code) | **Non-dominated. Front 0 co-member.** |
| Parent | `a32548bc-8c4` | *"Street empties, eyes blind"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member & Elite Parent.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`). Because Variants 2, 5, and the parent share identical objective coordinates $(\bar{Q}=0.850, R=0.500)$, boundary assignment gave $\infty$ to `207ae122-237` and `a32548bc-8c4`, and 0.0 to `d28edf15-414`. `a32548bc-8c4` was selected as elite parent for Gen 3.

* **Generation 2 Front 0 Members:** `207ae122-237`, `d28edf15-414`, and `a32548bc-8c4`.
* **Selection:** All three Front 0 members have identical objective coordinates $(\bar{Q}=0.850, R=0.500)$. Tied on boundary crowding distance ($\infty$), `a32548bc-8c4` was retained as the elite parent for Gen 3.
* **Best-F Tracker & $\Delta F$:** In Gen 2, Variant 2 (`207ae122-237`) achieved composite $F = 0.8000$, improving the global Best-F tracker from $0.7853 \to 0.8000$. Because $\Delta F = +0.0147 \ge 0.01$, the convergence patience counter **reset to 0**.

---

### Generation 3

Elite parent `a32548bc-8c4` ($\bar{Q}=0.850, R=0.500, S=0.941, F=0.7853$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `3110f2da-593` | *"Midnight lane, breath held"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Front 0 |
| Variant 2 | `c1a5ab65-a08` | *"Dark cobblestones sigh"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (computed from code) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member.** |
| Variant 3 | `2a6fcc7c-bfc` | *"Silent street inhales"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (computed from code) | 0.0 (computed from code) | **Non-dominated. Front 0 co-member.** |
| Variant 4 | `c9a9c20f-8dc` | *"Night veil drapes alone"* | 0.600 | 0.500 | 0.941 | 0.660 | Yes | 3 | [5, 8, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 5 | `cdff28a1-da2` | *"Gloom road swallows sound"* | 0.750 | 0.500 | 1.000 | 0.750 | Yes | 3 | [5, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `a32548bc-8c4` | *"Street empties, eyes blind"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member & Elite Parent.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`).

* **Generation 3 Front 0 Members:** `c1a5ab65-a08`, `2a6fcc7c-bfc`, and `a32548bc-8c4`.
* **Selection:** All three Front 0 members share identical objective coordinates $(\bar{Q}=0.850, R=0.500)$. `a32548bc-8c4` was retained as the elite parent for Gen 4.
* **Best-F Tracker & $\Delta F$:** Best-F remained $0.8000$. Thus $\Delta F = 0.0000 < 0.01$. Patience counter incremented to **1**.

---

### Generation 4 (Final Generation)

Elite parent `a32548bc-8c4` ($\bar{Q}=0.850, R=0.500, S=0.941, F=0.7853$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 4 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `eaec77f5-857` | *"Midnight lane, breath tight"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member.** |
| Variant 2 | `79d82c3c-473` | *"Alley whispers freeze"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Front 0 |
| Variant 3 | `dbe83c3a-aee` | *"Shadows hug the night"* | 0.750 | 0.500 | 0.941 | 0.735 | Yes | 3 | [5, 8, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 4 | `f9d288e3-906` | *"Empty curb, cold breath"* | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 5 | `857f8a00-304` | *"Night road holds its breath"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 6, 5] | **Rank 0** (from log) | 0.0 (computed from code) | **Non-dominated. Front 0 co-member.** |
| Parent | `a32548bc-8c4` | *"Street empties, eyes blind"* | **0.850** | **0.500** | **0.941** | **0.785** | **Yes** | 3 | [5, 8, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member & Winning Poem.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`). All three Front 0 members (`a32548bc-8c4`, `eaec77f5-857`, and `857f8a00-304`) are listed verbatim in the log line (`Final pool Front 0 members: [a32548bc-8c4 (F=0.785, Q̄=0.850, R=0.500), eaec77f5-857 (F=0.785, Q̄=0.850, R=0.500), 857f8a00-304 (F=0.785, Q̄=0.850, R=0.500)]`).

* **Final Pool Front 0 Members:**
  1. `a32548bc-8c4`: $\bar{Q}=0.8500, R=0.5000, S=0.9412, F=0.7853$
  2. `eaec77f5-857`: $\bar{Q}=0.8500, R=0.5000, S=0.9412, F=0.7853$
  3. `857f8a00-304`: $\bar{Q}=0.8500, R=0.5000, S=0.9412, F=0.7853$
* **Why `a32548bc-8c4` was chosen:**
  - All three members of Front 0 in the final pool share identical objective coordinates $(\bar{Q}=0.8500, R=0.5000)$ and identical composite fitness $F=0.7853$.
  - Per the presentation tie-break rule (`winning_poem = max(front_0, key=lambda p: p.F)`), `a32548bc-8c4` was selected as the first candidate evaluated with the maximal composite fitness.
* **Termination Reason:** Generation 4 reached the generation cap of 5 (Gen 0 through Gen 4 = 5 generations). The run terminated with `Stopping: reached max generation 5`.

---

## 4. Stopping Rule Audit & Quality Trajectory Analysis

| Generation | Best $F$ Tracked | Best $\bar{Q}$ in Pool | Best Front Quality ($\bar{Q}_{\text{Front } 0}$) | Best $R$ in Pool | Best $S$ in Pool | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7853 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.7853 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 2 | 0.8000 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | +0.0147 | 0 | Continue ($\Delta F \ge 0.01$; counter reset to 0) |
| 3 | 0.8000 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 4 | 0.8000 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 2 | **STOP — Reached maximum generation cap 5** |

### Best Front Quality Trajectory:
- **Did the best front's quality stop while still rising?**
  - **No.** Based strictly on the logged numbers:
    - In Generation 0, the highest Quality in Front 0 was **0.8500** (`a32548bc-8c4`).
    - In Generation 1, the highest Quality in Front 0 was **0.8500** (`a32548bc-8c4`).
    - In Generation 2, the highest Quality in Front 0 was **0.8500** (`207ae122-237`, `d28edf15-414`, `a32548bc-8c4`).
    - In Generation 3, the highest Quality in Front 0 was **0.8500** (`c1a5ab65-a08`, `2a6fcc7c-bfc`, `a32548bc-8c4`).
    - In Generation 4, the highest Quality in Front 0 was **0.8500** (`a32548bc-8c4`, `eaec77f5-857`, `857f8a00-304`).
  - Thus, the best front's Quality was completely constant at **0.8500** across all 5 generations. Quality was **not** rising when the run stopped.

### Note on Discrepancy between `per_generation.csv` and Presented Poem:
- In `src/ea/nsga2.py`, `per_generation.csv` records the global cumulative `best_poem_overall` (the poem with the highest composite $F$ ever evaluated up to that point):
  - In Gen 2, candidate `207ae122-237` achieved $F = 0.8000$, becoming `best_poem_overall`.
  - In Gens 2, 3, and 4, `per_generation.csv` logged `207ae122-237` ($F = 0.8000$).
  - However, `207ae122-237` was dropped from the candidate pool after Gen 2 because `a32548bc-8c4` was chosen as the single elite parent to mutate into Gen 3 and Gen 4.
  - At the end of Gen 4, the final presentation rule selected the highest-$F$ poem from Front 0 of the **active Generation 4 pool**, which was `a32548bc-8c4` ($F = 0.7853$).
  - Both poems were logged accurately according to their respective roles in the codebase.

**Verbatim Log Confirmation:**
```text
22:34:25 | INFO    | src.ea.nsga2 |   Gen 4 | NSGA-II elite: Poem(id=a32548bc-8c4, F=0.785, Q̄=0.850, R=0.500, S=0.941) (rank=0) | Best-F: 0.800
22:34:25 | INFO    | src.ea.common | Stopping: reached max generation 5
22:34:25 | INFO    | src.ea.nsga2 |   Final pool Front 0 members: [a32548bc-8c4 (F=0.785, Q̄=0.850, R=0.500), eaec77f5-857 (F=0.785, Q̄=0.850, R=0.500), 857f8a00-304 (F=0.785, Q̄=0.850, R=0.500)]
22:34:25 | INFO    | src.ea.nsga2 |   Final presentation: selected highest-F poem from Front 0 -> a32548bc-8c4 (F=0.785)
22:34:25 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_haiku_Fear_7e2df52b ═══ Generations: 5 | Final F=0.785
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 4 Mutation calls across Gens 1–4) | 6 | 1,782 | 4,699 | **6,481** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 20 mutation variants across 4 gens) | 26 | 9,359 | 1,202 | **10,561** |
| **Total** | | **32** | **11,141** | **5,901** | **17,042** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 10 pauses totaling **156.70 seconds** (~2m 36.7s):
- **Waiting on `qwen/qwen3.8-27b`:** 6 pauses totaling **45.70s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 4 pauses totaling **111.00s** (enforcing TPM/RPM limits).

| # | Timestamp (IST) | Timestamp (UTC = IST − 5h30m) | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | 22:31:00 | 17:01:00 | 20.2s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5516/6000 |
| 2 | 22:31:22 | 17:01:22 | 1.8s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5194/6000 |
| 3 | 22:31:27 | 17:01:27 | 1.1s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5792/6000 |
| 4 | 22:31:29 | 17:01:29 | 52.4s | `openai/gpt-oss-120b` | RPM=9/25 TPM=5789/6000 |
| 5 | 22:32:25 | 17:02:25 | 1.5s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5793/6000 |
| 6 | 22:32:27 | 17:02:27 | 1.4s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5793/6000 |
| 7 | 22:33:00 | 17:03:00 | 22.4s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4713/6000 |
| 8 | 22:33:26 | 17:03:26 | 34.4s | `openai/gpt-oss-120b` | RPM=9/25 TPM=5791/6000 |
| 9 | 22:34:02 | 17:04:02 | 20.4s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5627/6000 |
| 10 | 22:34:24 | 17:04:24 | 1.1s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5791/6000 |

### Server Errors & Retries Audit
During evaluation, the judge endpoint returned two transient 503 errors that were automatically retried and recovered:
- `22:30:58 | WARNING | src.api.client | [Qwen3.8-27B (Groq)] Server error (503), retrying in 1.2s (attempt 1/50)` (Gen 0 Candidate 4)
- `22:32:58 | WARNING | src.api.client | [Qwen3.8-27B (Groq)] Server error (503), retrying in 1.2s (attempt 1/50)` (Gen 2 Candidate 5)

### Net Execution Time
- **Gross Wall-Clock Duration (Start 22:30:20 → Completion 22:34:25 IST):** 245.0s (4m 05s)
- **Total Rate-Limit Pause Time:** 156.70s (2m 36.7s)
- **Time to Final Poem excluding pauses:** **88.30s** (includes ~2.4s of 503 connection backoff/retry elapsed time)

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 90–94)

```csv
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,0,0.7853,0.8500,0.5000,0.9412,"Street empties, eyes blind | Footfalls mirror trembling beat | Silence shatters now"
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,1,0.7853,0.8500,0.5000,0.9412,"Street empties, eyes blind | Footfalls mirror trembling beat | Silence shatters now"
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,2,0.8000,0.8500,0.5000,1.0000,"Dark road, lone footsteps | Each tread matches my slow stride | Night swallows my scream"
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,3,0.8000,0.8500,0.5000,1.0000,"Dark road, lone footsteps | Each tread matches my slow stride | Night swallows my scream"
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,4,0.8000,0.8500,0.5000,1.0000,"Dark road, lone footsteps | Each tread matches my slow stride | Night swallows my scream"
```

### `output/logs/per_run_summary.csv` (Line 25)

```csv
nsga2_haiku_Fear_7e2df52b,nsga2,haiku,Fear,0.7853,5,"Street empties, eyes blind | Footfalls mirror trembling beat | Silence shatters now"
```

### `output/logs/human_feedback.csv` (Line 22 / Index 20)

```csv
2026-11-10T04:27:41.839461+00:00,a32548bc-8c4,haiku,nsga2,Fear,"Walking alone down an unlit street, hearing footsteps that match your pace exactly.",1,good,"Street empties, eyes blind | Footfalls mirror trembling beat | Silence shatters now",0.7853,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `3` (Fear)
   - Description: *"Walking alone down an unlit street, hearing footsteps that match your pace exactly."*
3. **Execution:** Full evolutionary process ran over 5 generations (Gen 0 through Gen 4) in **4m 05s** gross wall-clock time (22:30:20 to 22:34:25 IST / 17:00:20 to 17:04:25 UTC), with net generation active time of **88.30s** excluding pauses.
4. **Presentation & Selection:** Winning poem `a32548bc-8c4` ($F=0.7853, \bar{Q}=0.8500, R=0.5000, S=0.9412$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live on Attempt 1.
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `a32548bc-8c4` and verdict `good`.
7. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; session concluded.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Mutation retry warning event:** **0** (no mutation failures; all 4 mutation calls returned 5 valid variants on first attempt).

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All parsed batches produced complete 3-line haikus.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `22:30:23 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Lamplight gone, breath tight'`
  - `22:30:23 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Street empties, eyes blind'`
  - `22:30:23 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Midnight wind holds breath'`
  - `22:30:23 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Alley yawns, dark drips'`
  - `22:30:23 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Night\'s veil swallows sound'`
  - `22:30:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight street, alone'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `22:31:26 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight lane, breath held'`
  - `22:31:26 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Empty curb, night veiled'`
  - `22:31:26 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dark road, lanterns none'`
  - `22:31:26 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Silent block, breath cold'`
  - `22:31:26 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Moonless path, shadows'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `22:32:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight lane, heart pounds'`
  - `22:32:24 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dark road, lone footsteps'`
  - `22:32:24 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Silent curb, pulse thuds'`
  - `22:32:24 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Empty lane, eyes shut'`
  - `22:32:24 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Night veil, heart stalls low'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `22:33:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight lane, breath held'`
  - `22:33:24 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dark cobblestones sigh'`
  - `22:33:24 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Silent street inhales'`
  - `22:33:24 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Night veil drapes alone'`
  - `22:33:24 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Gloom road swallows sound'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 3 Discarded Lines:** 0.

- **Generation 4 (Mutation Variants):**
  - `22:34:02 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight lane, breath tight'`
  - `22:34:02 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Alley whispers freeze'`
  - `22:34:02 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Shadows hug the night'`
  - `22:34:02 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Empty curb, cold breath'`
  - `22:34:02 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Night road holds its breath'`
  - **Gen 4 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 4 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1919–1939; 5 candidates)
- `initial_population_batch_2` (Lines 1940–1944; 1 candidate)
- `mutation` Gen 1 (Lines 1945–1965; 5 variants)
- `mutation` Gen 2 (Lines 1966–1986; 5 variants)
- `mutation` Gen 3 (Lines 1987–2015; 5 variants)
- `mutation` Gen 4 (Lines 2016–2036; 5 variants)

