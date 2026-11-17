# NSGA-II + Haiku + Joy (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_haiku_Joy_51d79af3` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-09 |
| **Start Time** | 21:55:09 IST (16:25:09 UTC) |
| **Completion Time** | 21:58:25 IST (16:28:25 UTC) |
| **Verdict Logged Time** | 21:59:31 IST (2026-11-09T16:29:31.740364+00:00 UTC) |
| **Time to Final Poem** | 3m 16s (196.0s gross wall-clock, 21:55:09 → 21:58:25 IST) |
| **Total Rate-Limit Pause Time** | 1m 53.9s (113.90s waiting across 6 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **82.10s** (196.0s gross wall-clock − 113.90s rate-limit waits; active evaluation also included two transient 503 retry delays totaling 4.1s) |
| **Algorithm** | NSGA-II (non-dominated sorting on Quality $\bar{Q}$ and Rhyme $R$; Structure $S \ge 0.30$ feasibility constraint) |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ (scalar composite tracked for convergence & tie-breaking) |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable target) |
| **Target Emotion** | Joy |
| **Scenario** | a child running barefoot through dewy grass as morning sunlight spills over the hilltop. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as Front 0 member of final pool with highest composite F` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`994e2aee-8ae`) was confirmed as the sole member of Front 0 of the final generation pool with composite fitness $F = 0.8000$. |
| **Historical Comparison Tag** | First valid NSGA-II Haiku Joy run under post-fix parser with full candidate ID, crowding distance provenance, and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Soft dew hugs each step
Hilltop glows with laughing eyes
Sun dances, carefree
```

| Metric | Value |
|---|---|
| **Poem ID** | `994e2aee-8ae` |
| **Composite Fitness ($F$)** | **0.8000** (displayed as 0.800) |
| **Quality ($\bar{Q}$)** | **0.8500** (displayed as 0.850) |
| **Rhyme ($R$)** | **0.5000** (displayed as 0.500; unrhymed haiku baseline) |
| **Structure ($S$)** | **1.0000** (displayed as 1.000; exact 5-7-5 syllables) |
| **Syllables per line** | Line 1: 5 (*Soft dew hugs each step*)<br>Line 2: 7 (*Hill-top glows with laugh-ing eyes*)<br>Line 3: 5 (*Sun dan-ces, care-free*) |
| **Line Count** | 3 (target: 3) |
| **Feasible ($S \ge 0.30$)** | **Yes** ($S = 1.0000 \ge 0.30$) |
| **Generation Created** | Generation 1 (Variant 4) |
| **Pareto Rank in Final Pool** | Rank 0 (Non-dominated; confirmed in log line: `Final pool Front 0 members: [994e2aee-8ae (F=0.800, Q̄=0.850, R=0.500)]`) |
| **Crowding Distance in Final Pool** | $\infty$ (`inf`; computed afterwards from code via `compute_crowding_distance`; not recorded in logs) |
| **Front 0 Member with Highest $F$** | **Yes** (Sole member of Front 0 in Gen 3 pool) |
| **Selection Rule** | Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`, confirmed in `src/ea/nsga2.py` lines 311–313) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts candidates on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is enforced as a feasibility constraint ($S \ge 0.30$). Composite fitness $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for convergence stopping and within-front selection.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 21:55:11 IST):** Generated Candidates 1–5 (all 3 lines each).
- **Batch 2 (Call 2, 21:55:12 IST):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 were feasible ($S \ge 0.30$), had exact 5-7-5 syllable structure ($S = 1.0000$), and unrhymed baseline ($R = 0.5000$).

### Candidate 1 (Batch 1, Candidate #1) — ID: `e398e86e-4f1`

```text
Dawn laughs on soft grass
Bare feet chase the golden glow
Joy spills like sunrise
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 0.500 | 1.000 | 0.700 | Yes | 3 | [5, 7, 5] | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 2, 3, 5 on $\bar{Q}$ |

### Candidate 2 (Batch 1, Candidate #2) — Gen 0 NSGA-II Elite (ID: `15ef6e22-3bc`)

```text
Morning dew kisses
Little steps paint bright laughter
Hill sings with sunshine
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member. Gen 0 Elite.** |

### Candidate 3 (Batch 1, Candidate #3) — ID: `45830be2-57c`

```text
Sunlight drapes the hill
Bare toes dance in silver mist
Laughter lifts the air
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | Rank 0 (computed from code) | 0.0 (computed from code) | Non-dominated. Front 0 co-member (interior point). |

### Candidate 4 (Batch 1, Candidate #4) — ID: `313b7338-f2c`

```text
Dewdrops sparkle bright
Child runs, heart a drumbeat wild
Joy erupts sunrise
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.500 | 1.000 | 0.750 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 2, 3, 5 on $\bar{Q}$ |

### Candidate 5 (Batch 1, Candidate #5) — ID: `3df5b0dd-a5e`

```text
Hilltop glows with gold
Barefoot child leaps, clouds applaud
Morning sings of joy
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | Rank 0 (computed from code) | $\infty$ (computed from code) | Non-dominated. Front 0 co-member. |

### Candidate 6 (Batch 2, Candidate #1) — ID: `75e440ef-a12`

```text
Bare feet kiss cool grass
Morning sun spills over hills
Joy leaps with each step
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Candidates 2, 3, 4, 5 on $\bar{Q}$ |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Discarded | Pareto Rank | Crowding Dist | NSGA-II Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `e398e86e-4f1` | 0.650 | 0.500 | 1.000 | 0.700 | Yes | 3 | [5, 7, 5] | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| 2 | `15ef6e22-3bc` | **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Gen 0 Elite (Front 0 member)** |
| 3 | `45830be2-57c` | **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | Rank 0 (computed from code) | 0.0 (computed from code) | Front 0 co-member |
| 4 | `313b7338-f2c` | 0.750 | 0.500 | 1.000 | 0.750 | Yes | 3 | [5, 7, 5] | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated |
| 5 | `3df5b0dd-a5e` | **0.800** | **0.500** | **1.000** | **0.775** | **Yes** | 3 | [5, 7, 5] | 0 | Rank 0 (computed from code) | $\infty$ (computed from code) | Front 0 co-member |
| 6 | `75e440ef-a12` | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs** (the logger records only `rank=0` and Front 0 membership). All crowding distance values in this table were **computed afterwards from the code** using `compute_crowding_distance` from `src/ea/nsga2.py`. Because Candidates 2, 3, and 5 had identical coordinates $(\bar{Q}=0.800, R=0.500)$, boundary assignment gave $\infty$ to Candidates 2 and 5, and 0.0 to Candidate 3. Candidate 2 (`15ef6e22-3bc`) was selected as the elite parent for Gen 1.

* **Generation 0 Front 0 Members:** Candidate 2 (`15ef6e22-3bc`), Candidate 3 (`45830be2-57c`), Candidate 5 (`3df5b0dd-a5e`).
* **Gen 0 Elite Selected:** Candidate 2 (`15ef6e22-3bc`, $F=0.7750$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `15ef6e22-3bc` ($\bar{Q}=0.800, R=0.500, S=1.000, F=0.775$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `95a4f3b3-d83` | *"Dew clings to tiny feet"* | 0.750 | 0.500 | 0.941 | 0.735 | Yes | 3 | [6, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 2 | `74eb15b8-261` | *"Bare toes kiss the green"* | 0.700 | 0.500 | 1.000 | 0.725 | Yes | 3 | [5, 7, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 3 | `a4643efe-84a` | *"Grass whispers beneath"* | 0.550 | 0.500 | 1.000 | 0.650 | Yes | 3 | [5, 7, 5] | Rank 4 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 4 | `994e2aee-8ae` | *"Soft dew hugs each step"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole Front 0. Gen 1 Elite.** |
| Variant 5 | `e2ec2a63-d49` | *"Footfalls stir the mist"* | 0.550 | 0.500 | 1.000 | 0.650 | Yes | 3 | [5, 7, 5] | Rank 4 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `15ef6e22-3bc` | *"Morning dew kisses"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Variant 4 on $\bar{Q}$ ($0.800 < 0.850$) |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`), which assigned $\infty$ (`inf`) to all solutions. Pareto Rank 0 for `994e2aee-8ae` is confirmed directly from the log line (`NSGA-II elite: Poem(id=994e2aee-8ae, ...) (rank=0)`); ranks for subsequent fronts were computed from code via `non_dominated_sort`.

* **Generation 1 Front 0 Members:** `994e2aee-8ae`.
* **NSGA-II Selection:** Variant 4 (`994e2aee-8ae`, $\bar{Q}=0.8500, R=0.5000$) strictly dominated parent `15ef6e22-3bc` ($\bar{Q}=0.8000, R=0.5000$) on Quality with perfect Structure ($S=1.0000$). Selected as elite parent for Generation 2.
* **Best-F Tracker & $\Delta F$:** In Generation 0, best-F was $0.7750$. In Generation 1, best candidate $F$ improved to $0.8000$ (achieved by `994e2aee-8ae`). Thus $\Delta F = +0.0250 \ge 0.01$. Convergence patience counter reset to 0.

---

### Generation 2

Elite parent `994e2aee-8ae` ($\bar{Q}=0.850, R=0.500, S=1.000, F=0.800$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `95be2bd7-520` | *"Soft dew kisses tiny feet"* | 0.700 | 0.500 | 0.882 | 0.696 | Yes | 3 | [7, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 2 | `926b2ee0-bf5` | *"Bare feet splash through mist"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Parent |
| Variant 3 | `f398c4d9-565` | *"Dawn's green carpet calls"* | 0.550 | 0.500 | 1.000 | 0.650 | Yes | 3 | [5, 7, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 4 | `e3d39978-f46` | *"Tiny toes touch sunrise"* | **0.800** | **0.667** | **0.941** | **0.802** | **Yes** | 3 | [6, 7, 5] | **Rank 0** (computed from code) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member (Rhyme specialist).** |
| Variant 5 | `4c4a6228-362` | *"Morning dew hugs soles"* | 0.550 | 0.500 | 0.941 | 0.635 | Yes | 3 | [5, 8, 5] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `994e2aee-8ae` | *"Soft dew hugs each step"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member & Gen 2 Elite.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`), which assigned $\infty$ (`inf`) to both boundary solutions of Front 0 (`e3d39978-f46` and `994e2aee-8ae`).

* **Generation 2 Front 0 Members:**
  1. `e3d39978-f46`: $\bar{Q}=0.8000, R=0.6667, S=0.9412, F=0.8020$
  2. `994e2aee-8ae`: $\bar{Q}=0.8500, R=0.5000, S=1.0000, F=0.8000$
* **Trade-Off & Elite Selection:**
  - `e3d39978-f46` achieved an internal end-rhyme between lines 1 and 3 (*sunrise* / *light*), giving $R=0.6667$, but had $\bar{Q}=0.8000$.
  - `994e2aee-8ae` had unrhymed $R=0.5000$, but higher Quality $\bar{Q}=0.8500$.
  - Neither dominated the other. In `src/ea/nsga2.py`, both were in Front 0. Tied on crowding distance ($\infty$), `994e2aee-8ae` was chosen as the elite parent for Gen 3.
* **Best-F Tracker & $\Delta F$:** Candidate `e3d39978-f46` achieved composite $F = 0.8020$, advancing the global Best-F tracker from $0.8000 \to 0.8020$. Because $\Delta F = +0.0020 < 0.01$, the convergence patience counter incremented to **1** (`delta: 0.0020`).

---

### Generation 3 (Final Generation)

Elite parent `994e2aee-8ae` ($\bar{Q}=0.850, R=0.500, S=1.000, F=0.800$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Syllables | Pareto Rank | Crowding Dist | Pareto Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `202baef4-ddb` | *"Morning grass tickles"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Parent |
| Variant 2 | `a4594370-75b` | *"Dew kisses small toes"* | 0.650 | 0.500 | 0.941 | 0.685 | Yes | 3 | [5, 7, 4] | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 3 | `23181860-5f7` | *"Grass glistens, child runs"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | 0.0 (computed from code) | Dominated by Parent |
| Variant 4 | `5d77cc1e-082` | *"Bare feet kiss cool dew"* | 0.800 | 0.500 | 1.000 | 0.775 | Yes | 3 | [5, 7, 5] | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Parent |
| Variant 5 | `07b96158-972` | *"Morning rush of joy"* | 0.750 | 0.500 | 1.000 | 0.750 | Yes | 3 | [5, 7, 5] | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `994e2aee-8ae` | *"Soft dew hugs each step"* | **0.850** | **0.500** | **1.000** | **0.800** | **Yes** | 3 | [5, 7, 5] | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole Front 0 & Winning Poem.** |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`). Sole member `994e2aee-8ae` in Front 0 received $\infty$ (`inf`). Front 0 membership is confirmed verbatim in the log line (`Final pool Front 0 members: [994e2aee-8ae (F=0.800, Q̄=0.850, R=0.500)]`).

* **Final Pool Front 0 Members:** `994e2aee-8ae` (sole member).
* **Why `994e2aee-8ae` was chosen:**
  - Parent `994e2aee-8ae` strictly dominated all 5 variants in Generation 3 on Quality ($\bar{Q}=0.8500 > 0.8000$) with identical Rhyme ($R=0.5000$).
  - Per NSGA-II final presentation rule (`winning_poem = max(front_0, key=lambda p: p.F)`), `994e2aee-8ae` was selected as the sole Front 0 member.
* **Best-F Tracker & Stopping:** Across generations, the best scalar fitness tracked was $0.8020$ (established in Gen 2 by `e3d39978-f46`). In Gen 3, the best candidate $F$ was $0.8000 \le 0.8020$. Consequently, $\Delta F = 0.0000 < 0.01$ for the second consecutive generation, advancing the patience counter to 2 and triggering convergence termination (`deltas: ['0.0020', '0.0000']`).

---

## 4. Stopping Rule Audit & Quality Trajectory Analysis

| Generation | Best $F$ Tracked | Best $\bar{Q}$ in Pool | Best Front Quality ($\bar{Q}_{\text{Front } 0}$) | Best $R$ in Pool | Best $S$ in Pool | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7750 | 0.8000 | 0.8000 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.8000 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | +0.0250 | 0 | Continue ($\Delta F \ge 0.01$) |
| 2 | 0.8020 | 0.8500 | 0.8500 | 0.6667 | 1.0000 | +0.0020 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 3 | 0.8020 | 0.8500 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 2 | **STOP — Convergence rule triggered ($\Delta F < 0.01$ for 2 gens)** |

### Best Front Quality Trajectory:
- **Did the best front's quality stop while still rising?**
  - **No.** Based strictly on the logged numbers:
    - In Generation 0, the highest Quality in Front 0 was **0.8000** (`15ef6e22-3bc`, `45830be2-57c`, `3df5b0dd-a5e`).
    - In Generation 1, the highest Quality in Front 0 rose to **0.8500** (`994e2aee-8ae`).
    - In Generation 2, the highest Quality in Front 0 was **0.8500** (`994e2aee-8ae`; Front 0 co-member `e3d39978-f46` offered higher Rhyme $R=0.6667$ but lower Quality $\bar{Q}=0.8000$).
    - In Generation 3, the highest Quality in Front 0 was **0.8500** (`994e2aee-8ae`).
  - Thus, the best front's Quality had already plateaued at **0.8500** across Generations 1, 2, and 3. Quality was **not** rising when the run stopped.

### Note on Discrepancy between `per_generation.csv` and Presented Poem:
- In `src/ea/nsga2.py`, `per_generation.csv` records the global cumulative `best_poem_overall` (the poem with the highest composite $F$ ever evaluated up to that point):
  - In Gen 2, candidate `e3d39978-f46` achieved $F = 0.8020$, becoming `best_poem_overall`.
  - In Gen 3, `per_generation.csv` logged `e3d39978-f46` ($F=0.8020$).
  - However, `e3d39978-f46` was dropped from the active candidate pool after Gen 2 because `994e2aee-8ae` was chosen as the single elite parent to mutate into Gen 3.
  - At the end of Gen 3, the final presentation rule selected the highest-$F$ poem from Front 0 of the **active Generation 3 pool**, which was `994e2aee-8ae` ($F = 0.8000$).
  - Both poems were logged accurately according to their respective roles in the codebase.

**Verbatim Log Confirmation:**
```text
21:58:25 | INFO    | src.ea.nsga2 |   Gen 3 | NSGA-II elite: Poem(id=994e2aee-8ae, F=0.800, Q̄=0.850, R=0.500, S=1.000) (rank=0) | Best-F: 0.802
21:58:25 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0020', '0.0000'])
21:58:25 | INFO    | src.ea.nsga2 |   Final pool Front 0 members: [994e2aee-8ae (F=0.800, Q̄=0.850, R=0.500)]
21:58:25 | INFO    | src.ea.nsga2 |   Final presentation: selected highest-F poem from Front 0 -> 994e2aee-8ae (F=0.800)
21:58:25 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_haiku_Joy_51d79af3 ═══ Generations: 4 | Final F=0.800
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 3 Mutation calls across 3 gens) | 5 | 1,477 | 2,922 | **4,399** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 15 mutation variants across 3 gens) | 21 | 7,568 | 1,019 | **8,587** |
| **Total** | | **26** | **9,045** | **3,941** | **12,986** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 6 pauses totaling **113.90 seconds** (~1m 53.9s):
- **Waiting on `qwen/qwen3.8-27b`:** 4 pauses totaling **57.40s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 2 pauses totaling **56.50s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 21:56:24 | 21.9s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5786/6000 |
| 2 | 21:56:46 | 32.4s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5786/6000 |
| 3 | 21:57:19 | 3.4s | `openai/gpt-oss-120b` | RPM=9/25 TPM=5787/6000 |
| 4 | 21:57:26 | 53.1s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5257/6000 |
| 5 | 21:58:21 | 1.4s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5639/6000 |
| 6 | 21:58:23 | 1.7s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5799/6000 |

### Server Errors & Retries Audit
During Generation 0 evaluation of Candidate 3 (`45830be2-57c`), the judge endpoint returned two transient 503 errors that were automatically retried and recovered:
- `21:55:44 | WARNING | src.api.client | [Qwen3.8-27B (Groq)] Server error (503), retrying in 1.5s (attempt 1/50)`
- `21:56:15 | WARNING | src.api.client | [Qwen3.8-27B (Groq)] Server error (503), retrying in 2.6s (attempt 2/50)`
- `21:56:18 | INFO | src.api.client | [Qwen3.8-27B (Groq)] Call complete` (attempt 3 succeeded).

### Net Execution Time
- **Gross Wall-Clock Duration (Start 21:55:09 → Completion 21:58:25):** 196.0s (3m 16s)
- **Total Rate-Limit Pause Time:** 113.90s (1m 53.9s)
- **Time to Final Poem excluding pauses:** **82.10s** (includes ~34s of 503 connection backoff/retry elapsed time)

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 82–85)

```csv
nsga2_haiku_Joy_51d79af3,nsga2,haiku,Joy,0,0.7750,0.8000,0.5000,1.0000,Morning dew kisses | Little steps paint bright laughter | Hill sings with sunshine
nsga2_haiku_Joy_51d79af3,nsga2,haiku,Joy,1,0.8000,0.8500,0.5000,1.0000,"Soft dew hugs each step | Hilltop glows with laughing eyes | Sun dances, carefree"
nsga2_haiku_Joy_51d79af3,nsga2,haiku,Joy,2,0.8020,0.8000,0.6667,0.9412,"Tiny toes touch sunrise | Hilltop glimmers, grass sings bright | Heart leaps with the light"
nsga2_haiku_Joy_51d79af3,nsga2,haiku,Joy,3,0.8020,0.8000,0.6667,0.9412,"Tiny toes touch sunrise | Hilltop glimmers, grass sings bright | Heart leaps with the light"
```

### `output/logs/per_run_summary.csv` (Line 23)

```csv
nsga2_haiku_Joy_51d79af3,nsga2,haiku,Joy,0.8000,4,"Soft dew hugs each step | Hilltop glows with laughing eyes | Sun dances, carefree"
```

### `output/logs/human_feedback.csv` (Line 20 / Index 18)

```csv
2026-11-09T16:29:31.740364+00:00,994e2aee-8ae,haiku,nsga2,Joy,a child running barefoot through dewy grass as morning sunlight spills over the hilltop.,1,good,"Soft dew hugs each step | Hilltop glows with laughing eyes | Sun dances, carefree",0.8000,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `1` (Joy)
   - Description: *"a child running barefoot through dewy grass as morning sunlight spills over the hilltop."*
3. **Execution:** Full evolutionary process ran over 4 generations (Gen 0 through Gen 3) in **3m 16s** gross wall-clock time (21:55:09 to 21:58:25 IST), with net generation active time of **82.10s** excluding pauses.
4. **Presentation & Selection:** Winning poem `994e2aee-8ae` ($F=0.8000, \bar{Q}=0.8500, R=0.5000, S=1.0000$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live at 21:59:31 IST (`2026-11-09T16:29:31.740364+00:00` UTC).
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `994e2aee-8ae` and verdict `good`.
7. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool exited cleanly with `Session complete. Goodbye!`.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Mutation retry warning event:** **0** (no mutation failures; all 3 mutation calls returned 5 valid variants on first attempt).

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All parsed batches produced complete 3-line haikus.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `21:55:11 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Dawn laughs on soft grass'`
  - `21:55:11 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Morning dew kisses'`
  - `21:55:11 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Sunlight drapes the hill'`
  - `21:55:11 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Dewdrops sparkle bright'`
  - `21:55:11 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Hilltop glows with gold'`
  - `21:55:12 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Bare feet kiss cool grass'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `21:56:23 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Dew clings to tiny feet'`
  - `21:56:23 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Bare toes kiss the green'`
  - `21:56:23 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Grass whispers beneath'`
  - `21:56:23 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Soft dew hugs each step'`
  - `21:56:23 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Footfalls stir the mist'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `21:57:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Soft dew kisses tiny feet'`
  - `21:57:24 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Bare feet splash through mist'`
  - `21:57:24 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dawn\'s green carpet calls'`
  - `21:57:24 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Tiny toes touch sunrise'`
  - `21:57:24 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Morning dew hugs soles'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `21:58:21 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Morning grass tickles'`
  - `21:58:21 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dew kisses small toes'`
  - `21:58:21 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Grass glistens, child runs'`
  - `21:58:21 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Bare feet kiss cool dew'`
  - `21:58:21 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Morning rush of joy'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 3 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1729–1749; 5 candidates)
- `initial_population_batch_2` (Lines 1750–1754; 1 candidate)
- `mutation` Gen 1 (Lines 1755–1783; 5 variants)
- `mutation` Gen 2 (Lines 1784–1804; 5 variants)
- `mutation` Gen 3 (Lines 1805–1825; 5 variants)

