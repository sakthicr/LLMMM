# NSGA-II + Limerick + Joy (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_limerick_Joy_43c13e81` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-07 |
| **Start Time** | 20:49:04 IST (15:19:04 UTC) |
| **Completion Time** | 20:52:08 IST (15:22:08 UTC) |
| **Verdict Logged Time** | 20:55:14 IST (2026-11-07T15:25:14.959411+00:00 UTC) |
| **Time to Final Poem** | 3m 04s (184.0s wall-clock, 20:49:04 → 20:52:08 IST) |
| **Total Rate-Limit Pause Time** | 2m 44.5s (164.50s waiting across 6 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **19.50s** (184.0s gross wall-clock − 164.50s rate-limit waits) |
| **Algorithm** | NSGA-II (non-dominated sorting on Quality $\bar{Q}$ and Rhyme $R$; Structure $S \ge 0.30$ feasibility constraint) |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ (scalar composite tracked for convergence & tie-breaking) |
| **Poem Type** | Limerick (5 lines, AABBA rhyme scheme) |
| **Target Emotion** | Joy |
| **Scenario** | a clumsy baker whose wedding cake collapses just before the guests arrive, but the happy mess becomes the most loved dessert of the night. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 5-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as Front 0 member of final pool with highest composite F` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`dc1f4208-832`) was confirmed as a Front 0 member of the final generation pool and selected as having the highest composite fitness $F = 0.8070$ ($0.807 > 0.803$). |
| **Historical Comparison Tag** | First valid NSGA-II Limerick Joy run under post-fix parser with full candidate ID, crowding distance provenance, and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Bumbling baker, his whisk a wild kite,
Raised a cake that could out‑shine any light.
It toppled with cheer,
A sweet avalanche near,
And the guests ate the joy, every bite pure delight.
```

| Metric | Value |
|---|---|
| **Poem ID** | `dc1f4208-832` |
| **Composite Fitness ($F$)** | **0.8070** (displayed as 0.807) |
| **Quality ($\bar{Q}$)** | **0.8000** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.6280** (displayed as 0.628) |
| **Rhyme Scheme** | AABBA — *kite* / *light* / *cheer* / *near* / *delight* |
| **Line Count** | 5 (target: 5) |
| **Feasible ($S \ge 0.30$)** | **Yes** ($S = 0.6280 \ge 0.30$) |
| **Generation Created** | Generation 2 (Variant 5) |
| **Pareto Rank in Final Pool** | Rank 0 (Non-dominated; confirmed in log line: `Final pool Front 0 members: [f2e4fcff-76d ..., dc1f4208-832 ...]`) |
| **Crowding Distance in Final Pool** | $\infty$ (`inf`; computed afterwards from code via `compute_crowding_distance`; not recorded in logs) |
| **Front 0 Member with Highest $F$** | **Yes** (Selected over Front 0 co-member `f2e4fcff-76d`, $F=0.8070 > 0.8030$) |
| **Selection Rule** | Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`, confirmed in `src/ea/nsga2.py` lines 311–313) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts candidates on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is enforced as a feasibility constraint ($S \ge 0.30$). Composite fitness $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for convergence stopping and within-front selection.

Initial population sampling required 3 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 20:49:06 IST):** Generated Candidates 1–5 (all 5 lines each).
- **Batch 2 (Call 2, 20:49:09 IST):** Consumed 1,200 completion reasoning tokens; returned empty content string (0 candidates).
- **Batch 3 (Call 3, 20:49:10 IST):** Generated Candidate 6 (5 lines).

All 6 evaluated candidates in Generation 0 were feasible ($S \ge 0.30$) and had exactly 5 lines.

### Candidate 1 (Batch 1, Candidate #1) — Gen 0 NSGA-II Elite (ID: `17120c79-f78`)

```text
A clumsy baker named Finn, so bright
He set up the tier with all his might
It fell with a sigh
A sweet, gooey sky
And guests cheered the mess through the night
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 1.000 | 0.953 | 0.838 | Yes | 5 | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole member of Front 0. Gen 0 Elite.** |

### Candidate 2 (Batch 1, Candidate #2) — ID: `4a69f452-6f7`

```text
There once was a chef who would tumble
When he plated the cake, it would crumble
The frosting did slip
But gave every sip
A delight that made all hearts rumble
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.300 | 1.000 | 0.851 | 0.613 | Yes | 5 | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 1, 4, 3 on $\bar{Q}$ |

### Candidate 3 (Batch 1, Candidate #3) — ID: `6bbe4023-b2d`

```text
A nervous baker with flour on his cheek
Placed the cake, then it sagged—so unique!
The guests all did grin
As the crumbs danced within
And sang for the joy that they’d seek
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.350 | 1.000 | 0.794 | 0.624 | Yes | 5 | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 1 and Candidate 4 on $\bar{Q}$ |

### Candidate 4 (Batch 1, Candidate #4) — ID: `ecb8f53a-cbd`

```text
A jittery baker, his hands in a flurry
Saw the wedding cake wobble, then worry
It splashed like a dream
In a chocolatey stream
And the crowd ate it, all happy and merry
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 0.667 | 0.590 | 0.639 | Yes | 5 | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Non-dominated against Candidate 5; dominated by Candidate 1 |

### Candidate 5 (Batch 1, Candidate #5) — ID: `266cd8cc-d29`

```text
A bumbling baker, his steps out of sync
Watched the tier tumble quicker than blink
The frosting did pour
Like rain on the floor
Yet love rose anew in each tasty drink
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 1.000 | 0.763 | 0.741 | Yes | 5 | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Non-dominated against Candidate 4; dominated by Candidate 1 |

### Candidate 6 (Batch 3, Candidate #1) — ID: `19baad08-20b`

```text
There once was a baker named Lee,
His wedding cake fell just before glee,
Guests laughed, what a treat,
Sweet mess couldn't be beat,
And love rose high with frosting glee
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.500 | 0.833 | 0.953 | 0.697 | Yes | 5 | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated by Candidate 1 and Candidate 5 |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | NSGA-II Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `17120c79-f78` | **0.700** | **1.000** | **0.953** | **0.838** | **Yes** | 5 | 0 | **Rank 0** (from log) | $\infty$ (computed from code) | **Gen 0 Elite (Sole Front 0)** |
| 2 | `4a69f452-6f7` | 0.300 | 1.000 | 0.851 | 0.613 | Yes | 5 | 0 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| 3 | `6bbe4023-b2d` | 0.350 | 1.000 | 0.794 | 0.624 | Yes | 5 | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| 4 | `ecb8f53a-cbd` | 0.650 | 0.667 | 0.590 | 0.639 | Yes | 5 | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated |
| 5 | `266cd8cc-d29` | 0.600 | 1.000 | 0.763 | 0.741 | Yes | 5 | 0 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated |
| 6 | `19baad08-20b` | 0.500 | 0.833 | 0.953 | 0.697 | Yes | 5 | 0 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs** (the logger records only `rank=0` and Front 0 membership). All crowding distance values in this table were **computed afterwards from the code** using `compute_crowding_distance` from `src/ea/nsga2.py`. Because all fronts contained $\le 2$ members, boundary assignment assigned $\infty$ (`inf`) to all solutions.

* **Generation 0 Front 0 Members:** Candidate 1 (`17120c79-f78`).
* **Gen 0 Elite Selected:** Candidate 1 (`17120c79-f78`, $F=0.8382$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `17120c79-f78` ($\bar{Q}=0.700, R=1.000, S=0.953, F=0.8382$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Pareto Rank | Crowding Dist | Pareto Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `d3544139-691` | *"A baker named Milo, clumsy yet bright"* | 0.550 | 1.000 | 0.843 | 0.736 | Yes | 5 | Rank 4 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 2 | `cecd5df2-935` | *"Young baker Miss Tess, with a wobble and"* | 0.650 | 1.000 | 0.706 | 0.752 | Yes | 5 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 3 | `87a44674-a98` | *"Jolly chef Marco, his steps out of sync,"* | **0.750** | **1.000** | **0.628** | **0.782** | **Yes** | 5 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Sole Front 0. Gen 1 Elite.** |
| Variant 4 | `668db754-fe4` | *"Merry baker Elise, with flour on her che"* | 0.600 | 1.000 | 0.725 | 0.731 | Yes | 5 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 5 | `52c65a31-179` | *"Cheerful cook Owen, his hands slightly s"* | 0.600 | 1.000 | 0.628 | 0.707 | Yes | 5 | Rank 3 (computed from code) | $\infty$ (computed from code) | Dominated |
| Parent | `17120c79-f78` | *"A clumsy baker named Finn, so bright"* | 0.700 | 1.000 | 0.953 | 0.8382 | Yes | 5 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Variant 3 on $\bar{Q}$ ($0.700 < 0.750$) |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`), which assigned $\infty$ (`inf`) to all solutions. Pareto Rank 0 for `87a44674-a98` is confirmed directly from the log line (`NSGA-II elite: Poem(id=87a44674-a98, ...) (rank=0)`); ranks for subsequent fronts were computed from code via `non_dominated_sort`.

* **Generation 1 Front 0 Members:** `87a44674-a98`.
* **NSGA-II Selection:** Variant 3 (`87a44674-a98`, $\bar{Q}=0.7500, R=1.0000$) strictly dominated parent `17120c79-f78` ($\bar{Q}=0.7000, R=1.0000$) and all other variants on Quality while holding perfect Rhyme ($R=1.0000$). Selected as elite parent for Generation 2.
* **Best-F Tracker & $\Delta F$:** In Generation 0, best-F was $0.8382$. In Generation 1, best candidate $F$ was $0.8382$ (retained by parent). Thus $\Delta F = 0.0000 < 0.01$. Convergence patience counter increments to 1.

---

### Generation 2 (Final Generation)

Elite parent `87a44674-a98` ($\bar{Q}=0.750, R=1.000, S=0.628, F=0.782$) was mutated to produce 5 variants.
- Mutation retries: **1** (Attempt 1 returned empty content string; Attempt 2 succeeded with 5 valid variants).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Pareto Rank | Crowding Dist | Pareto Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `9b191a4c-d88` | *"A clumsy baker in tux, floured his shoes,"* | 0.650 | 0.500 | 0.651 | 0.613 | Yes | 5 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 2 | `22075434-b80` | *"In a rush the baker twirled, whisk in his"* | 0.550 | 1.000 | 0.651 | 0.688 | Yes | 5 | Rank 2 (computed from code) | $\infty$ (computed from code) | Dominated |
| Variant 3 | `3733964f-3d9` | *"The baker, all jittery, set layers with "* | 0.750 | 1.000 | 0.519 | 0.755 | Yes | 5 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Variant 4 & 5 |
| Variant 4 | `f2e4fcff-76d` | *"A nervous confectioner, apron askew,"* | **0.800** | **1.000** | **0.613** | **0.803** | **Yes** | 5 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member.** |
| Variant 5 | `dc1f4208-832` | *"Bumbling baker, his whisk a wild kite,"* | **0.800** | **1.000** | **0.628** | **0.807** | **Yes** | 5 | **Rank 0** (from log) | $\infty$ (computed from code) | **Non-dominated. Front 0 co-member & Winning Poem.** |
| Parent | `87a44674-a98` | *"Jolly chef Marco, his steps out of sync,"* | 0.750 | 1.000 | 0.628 | 0.782 | Yes | 5 | Rank 1 (computed from code) | $\infty$ (computed from code) | Dominated by Variant 4 & 5 on $\bar{Q}$ ($0.750 < 0.800$) |

> [!NOTE]
> **Crowding Distance Provenance:** Individual crowding distances are **not recorded in the application logs**. Values were **computed afterwards from the code** using `compute_crowding_distance` (`src/ea/nsga2.py`), which assigned $\infty$ (`inf`) to all solutions. Front 0 membership of `f2e4fcff-76d` and `dc1f4208-832` is confirmed verbatim in the log line (`Final pool Front 0 members: [f2e4fcff-76d (F=0.803, Q̄=0.800, R=1.000), dc1f4208-832 (F=0.807, Q̄=0.800, R=1.000)]`).

* **Final Pool Front 0 Members:**
  1. `f2e4fcff-76d`: $\bar{Q}=0.8000, R=1.0000, S=0.6130, F=0.8030$
  2. `dc1f4208-832`: $\bar{Q}=0.8000, R=1.0000, S=0.6280, F=0.8070$
* **Why `dc1f4208-832` was chosen:**
  - Both `f2e4fcff-76d` and `dc1f4208-832` have identical objective coordinates $(\bar{Q}=0.8000, R=1.0000)$ and form Front 0.
  - Per NSGA-II final presentation rule (`winning_poem = max(front_0, key=lambda p: p.F)`), `dc1f4208-832` was selected because its higher structure score ($S=0.6280$ vs $0.6130$) yielded the higher composite fitness ($F=0.8070 > 0.8030$).
* **Best-F Tracker & Stopping:** Across generations, the best scalar fitness tracked was $0.8382$ (established in Gen 0). In Gen 2, best candidate $F$ was $0.8070 \le 0.8382$. Consequently, $\Delta F = 0.0000 < 0.01$ for the second consecutive generation, advancing the patience counter to 2 and triggering convergence termination (`deltas: ['0.0000', '0.0000']`).

---

## 4. Stopping Rule Audit

| Generation | Best $F$ Tracked | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8382 | 0.7000 | 1.0000 | 0.9530 | — | 0 | Continue |
| 1 | 0.8382 | 0.7000 | 1.0000 | 0.9530 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 2 | 0.8382 | 0.7000 | 1.0000 | 0.9530 | 0.0000 | 2 | **STOP — Convergence rule triggered ($\Delta F < 0.01$ for 2 gens)** |

### Note on Convergence Rule Execution:
In Generation 0, Candidate 1 set the global benchmark at $F=0.8382$. In Generation 1, the new elite variant achieved higher Quality ($\bar{Q}=0.7500$ vs $0.7000$) but a lower structure score, resulting in $F=0.7820 < 0.8382$, keeping best-F flat at $0.8382$ ($\Delta F = 0.0000$, patience = 1). In Generation 2, the new Front 0 variants reached $\bar{Q}=0.8000$, but composite fitness reached $F=0.8070 < 0.8382$, again keeping best-F flat at $0.8382$ ($\Delta F = 0.0000$, patience = 2).
The convergence condition was satisfied after Generation 2 (3 total generations: Gen 0, 1, 2), terminating the search cleanly before reaching the generation cap of 5.

**Verbatim Log Confirmation:**
```text
20:52:08 | INFO    | src.ea.nsga2 |   Gen 2 | NSGA-II elite: Poem(id=f2e4fcff-76d, F=0.803, Q̄=0.800, R=1.000, S=0.613) (rank=0) | Best-F: 0.838
20:52:08 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
20:52:08 | INFO    | src.ea.nsga2 |   Final pool Front 0 members: [f2e4fcff-76d (F=0.803, Q̄=0.800, R=1.000), dc1f4208-832 (F=0.807, Q̄=0.800, R=1.000)]
20:52:08 | INFO    | src.ea.nsga2 |   Final presentation: selected highest-F poem from Front 0 -> dc1f4208-832 (F=0.807)
20:52:08 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_limerick_Joy_43c13e81 ═══ Generations: 3 | Final F=0.807
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–3 + 3 Mutation calls across 2 gens) | 6 | 2,060 | 4,663 | **6,723** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 10 mutation variants) | 16 | 6,218 | 651 | **6,869** |
| **Total** | | **22** | **8,278** | **5,314** | **13,592** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 6 pauses totaling **164.50 seconds** (~2m 44.5s):
- **Waiting on `qwen/qwen3.8-27b`:** 5 pauses totaling **162.90s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 1 pause totaling **1.60s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 20:49:12 | 52.6s | `qwen/qwen3.8-27b` | RPM=5/25 TPM=5486/6000 |
| 2 | 20:50:08 | 1.6s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4836/6000 |
| 3 | 20:50:12 | 52.9s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5479/6000 |
| 4 | 20:51:05 | 2.3s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5481/6000 |
| 5 | 20:51:13 | 52.8s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5889/6000 |
| 6 | 20:52:06 | 2.3s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5890/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 20:49:04 → Completion 20:52:08):** 184.0s (3m 04s)
- **Total Rate-Limit Pause Time:** 164.50s (2m 44.5s)
- **Time to Final Poem excluding pauses:** **19.50s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 70–72)

```csv
nsga2_limerick_Joy_43c13e81,nsga2,limerick,Joy,0,0.8382,0.7000,1.0000,0.9530,"A clumsy baker named Finn, so bright | He set up the tier with all his might | It fell with a sigh | A sweet, gooey sky | And guests cheered the mess through the night"
nsga2_limerick_Joy_43c13e81,nsga2,limerick,Joy,1,0.8382,0.7000,1.0000,0.9530,"A clumsy baker named Finn, so bright | He set up the tier with all his might | It fell with a sigh | A sweet, gooey sky | And guests cheered the mess through the night"
nsga2_limerick_Joy_43c13e81,nsga2,limerick,Joy,2,0.8382,0.7000,1.0000,0.9530,"A clumsy baker named Finn, so bright | He set up the tier with all his might | It fell with a sigh | A sweet, gooey sky | And guests cheered the mess through the night"
```

### `output/logs/per_run_summary.csv` (Line 20)

```csv
nsga2_limerick_Joy_43c13e81,nsga2,limerick,Joy,0.8070,3,"Bumbling baker, his whisk a wild kite, | Raised a cake that could out‑shine any light. | It toppled with cheer, | A sweet avalanche near, | And the guests ate the joy, every bite pure delight."
```

### `output/logs/human_feedback.csv` (Line 17 / Index 15)

```csv
2026-11-07T15:25:14.959411+00:00,dc1f4208-832,limerick,nsga2,Joy,"a clumsy baker whose wedding cake collapses just before the guests arrive, but the happy mess becomes the most loved dessert of the night.",1,good,"Bumbling baker, his whisk a wild kite, | Raised a cake that could out‑shine any light. | It toppled with cheer, | A sweet avalanche near, | And the guests ate the joy, every bite pure delight.",0.8070,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `1` (Joy)
   - Description: *"a clumsy baker whose wedding cake collapses just before the guests arrive, but the happy mess becomes the most loved dessert of the night."*
3. **Execution:** Full evolutionary process ran over 3 generations (Gen 0 through Gen 2) in **3m 04s** gross wall-clock time (20:49:04 to 20:52:08 IST), with net generation active time of **19.50s** excluding pauses.
4. **Presentation & Selection:** Winning poem `dc1f4208-832` ($F=0.8070$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: limerick` (inferred from code, not observed) due to the ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `nsga2` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `good` live at 20:55:14 IST (`2026-11-07T15:25:14.959411+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `dc1f4208-832` and verdict `good`.
8. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool exited cleanly with `Session complete. Goodbye!`.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Mutation retry warning event:** 1 event in Generation 2 at 20:51:11 IST:
  ```text
  20:51:11 | WARNING | src.ea.mutation | Mutation returned 0 valid variants (attempt 1/3). Retrying...
  ```
  Attempt 2 succeeded immediately at 20:51:12 IST with 5 valid variants:
  ```text
  20:51:12 | INFO    | src.ea.mutation | Mutation succeeded on attempt 2/3 with 5 variants.
  ```

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All parsed batches produced complete 5-line limericks.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `20:49:06 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A clumsy baker named Finn, so bright'`
  - `20:49:06 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='There once was a chef who would tumble'`
  - `20:49:06 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='A nervous baker with flour on his cheek'`
  - `20:49:06 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='A jittery baker, his hands in a flurry'`
  - `20:49:06 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='A bumbling baker, his steps out of sync'`
  - `20:49:10 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='There once was a baker named Lee,'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `20:50:11 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A baker named Milo, clumsy yet bright'`
  - `20:50:11 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='Young baker Miss Tess, with a wobble and'`
  - `20:50:11 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Jolly chef Marco, his steps out of sync,'`
  - `20:50:11 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Merry baker Elise, with flour on her che'`
  - `20:50:11 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Cheerful cook Owen, his hands slightly s'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `20:51:12 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A clumsy baker in tux, floured his shoes'`
  - `20:51:12 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='In a rush the baker twirled, whisk in hi'`
  - `20:51:12 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The baker, all jittery, set layers with '`
  - `20:51:12 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='A nervous confectioner, apron askew,'`
  - `20:51:12 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Bumbling baker, his whisk a wild kite,'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1360–1398)
- `initial_population_batch_2` (Lines 1399–1401; empty completion)
- `initial_population_batch_3` (Lines 1402–1408)
- `mutation` Gen 1 (Lines 1409–1443)
- `mutation` Gen 2 Attempt 1 (Lines 1444–1446; empty completion, retried)
- `mutation` Gen 2 Attempt 2 (Lines 1447–1485; 5 valid variants)

