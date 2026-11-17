# NSGA-II + Limerick + Fear (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_limerick_Fear_f8e80f06` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-07 |
| **Start Time** | 19:57:30 IST (14:27:30 UTC) |
| **Completion Time** | 20:01:07 IST (14:31:07 UTC) |
| **Verdict Logged Time** | 20:02:06 IST (2026-11-07T14:32:06.446950+00:00 UTC) |
| **Time to Final Poem** | 3m 37s (217s wall-clock, 19:57:30 → 20:01:07 IST) |
| **Total Rate-Limit Pause Time** | 2m 44.5s (164.50s waiting across 8 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **52.50s** (217.0s gross wall-clock − 164.50s rate-limit waits) |
| **Algorithm** | NSGA-II (non-dominated sorting on Quality $\bar{Q}$ and Rhyme $R$; Structure $S \ge 0.30$ feasibility constraint) |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ (scalar composite tracked for convergence & tie-breaking) |
| **Poem Type** | Limerick (5 lines, AABBA rhyme scheme) |
| **Target Emotion** | Fear |
| **Scenario** | a nervous man who hides under the bed during a thunderstorm, only to find something else already hiding there. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 5-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as Front 0 member of final pool with highest composite F` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`a63d13eb-742`) is the sole member of Front 0 of the final pool with composite fitness $F = 0.9106$. |
| **Historical Comparison Tag** | First valid NSGA-II Limerick Fear run under post-fix parser with full candidate ID and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
When thunder cracked loud through the night,
He slid beneath sheets, trembling with fright,
A soft rustle near,
A cold, hollow sneer,
And a pale hand clasped his wrist in the light.
```

| Metric | Value |
|---|---|
| **Poem ID** | `a63d13eb-742` |
| **Composite Fitness ($F$)** | **0.9106** (displayed as 0.911) |
| **Quality ($\bar{Q}$)** | **0.9000** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.8426** (displayed as 0.843) |
| **Rhyme Scheme** | AABBA — *night* / *fright* / *near* / *sneer* / *light* |
| **Line Count** | 5 (target: 5) |
| **Feasible ($S \ge 0.30$)** | **Yes** ($S = 0.8426 \ge 0.30$) |
| **Generation Created** | Generation 1 (Variant 1) |
| **Pareto Rank in Final Pool** | Rank 0 (Non-dominated) |
| **Crowding Distance in Final Pool** | $\infty$ (`inf`) |
| **Front 0 Member with Highest $F$** | **Yes** (Sole member of Front 0 in final pool) |
| **Selection Rule** | Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts candidates on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is enforced as a feasibility constraint ($S \ge 0.30$). Composite fitness $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for convergence stopping and within-front selection.

Initial population sampling required 3 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 19:57:33 IST):** Consumed 1,200 completion reasoning tokens; returned empty content string (0 candidates).
- **Batch 2 (Call 2, 19:57:34 IST):** Generated Candidates 1–5 (all 5 lines each).
- **Batch 3 (Call 3, 19:57:37 IST):** Generated Candidate 6 (5 lines).

All 6 evaluated candidates in Generation 0 were feasible ($S \ge 0.30$) and had exactly 5 lines.

### Candidate 1 (Batch 2, Candidate #1) — ID: `12c0c3db-1ef`

```text
In the dark when the thunder did roll,
A trembling man slid beneath his old bowl,
He heard claws,
He felt jaws,
And froze as the shadows took hold.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.667 | 0.684 | 0.688 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated by Candidate 5 on Rhyme ($0.667 < 1.000$) |

### Candidate 2 (Batch 2, Candidate #2) — ID: `158d09f8-f40`

```text
When lightning flashed bright through the night,
He shivered and hid in the bed’s tight fright,
A whisper,
A hiss, sir,
The darkness replied with a snarl.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.167 | 0.708 | 0.494 | Yes | 5 | 0 | Rank 2 | $\infty$ | Dominated by Candidate 1 and Candidate 5 |

### Candidate 3 (Batch 2, Candidate #3) — ID: `1bb450f4-af5`

```text
Beneath the bed where the dust lay deep,
He felt something stir and then creep,
A low growl,
A cold howl,
His heart thumped like drums in a sweep.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 1.000 | 0.819 | 0.780 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated by Candidate 5 on Quality ($0.650 < 0.800$) |

### Candidate 4 (Batch 2, Candidate #4) — ID: `520bdee7-7a3`

```text
The storm roared loud, the floorboards did quake,
He pressed his cheek to the mattress for brake,
A soft sigh,
A cold eye,
And eyes glowed where the darkness did wake.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 1.000 | 0.717 | 0.754 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated by Candidate 5 on Quality ($0.650 < 0.800$) |

### Candidate 5 (Batch 2, Candidate #5) — Gen 0 NSGA-II Elite (ID: `ca869cc3-6f9`)

```text
When rain hammered hard on the pane,
He curled in the shadows, fearing the pain,
A whispering breath,
A scent of death,
And something unseen clutched at his chain.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 1.000 | 0.874 | 0.869 | Yes | 5 | 0 | **Rank 0** | $\infty$ | **Non-dominated. Sole member of Front 0. Gen 0 Elite.** |

### Candidate 6 (Batch 3, Candidate #1) — ID: `2114d77a-a44`

```text
When thunder cracked the night, he fled in fright
He slipped beneath the bed, his pulse a fright
But eyes glowed cold, they stared
A hiss replied, “I’ve always stared.”
Now terror grins, his heart still tight with fright
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 0.000 | 0.568 | 0.442 | Yes | 5 | 0 | Rank 2 | $\infty$ | Dominated ($R=0.000$, low Quality) |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Discarded | Pareto Rank | Crowding Dist | NSGA-II Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `12c0c3db-1ef` | 0.700 | 0.667 | 0.684 | 0.688 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated |
| 2 | `158d09f8-f40` | 0.550 | 0.167 | 0.708 | 0.494 | Yes | 5 | 0 | Rank 2 | $\infty$ | Dominated |
| 3 | `1bb450f4-af5` | 0.650 | 1.000 | 0.819 | 0.780 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated |
| 4 | `520bdee7-7a3` | 0.650 | 1.000 | 0.717 | 0.754 | Yes | 5 | 0 | Rank 1 | $\infty$ | Dominated |
| 5 | `ca869cc3-6f9` | **0.800** | **1.000** | **0.874** | **0.869** | **Yes** | 5 | 0 | **Rank 0** | $\infty$ | **Gen 0 Elite (Front 0)** |
| 6 | `2114d77a-a44` | 0.600 | 0.000 | 0.568 | 0.442 | Yes | 5 | 0 | Rank 2 | $\infty$ | Dominated |

* **Generation 0 Front 0 Members:** Candidate 5 (`ca869cc3-6f9`).
* **Gen 0 Elite Selected:** Candidate 5 (`ca869cc3-6f9`, $F=0.8686$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `ca869cc3-6f9` ($\bar{Q}=0.800, R=1.000, S=0.874, F=0.8686$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Pareto Rank | Crowding Dist | Pareto Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `a63d13eb-742` | *"When thunder cracked loud through the night,"* | **0.900** | **1.000** | **0.843** | **0.9106** | **Yes** | 5 | **Rank 0** | $\infty$ | **Non-dominated. Sole Front 0. Gen 1 Elite.** |
| Variant 2 | `26a37ae5-a13` | *"The storm’s wild roar shook every wall,"* | 0.750 | 1.000 | 0.684 | 0.7960 | Yes | 5 | Rank 3 | $\infty$ | Dominated |
| Variant 3 | `f9e230cc-613` | *"Lightning flashed fierce across the sky,"* | 0.850 | 1.000 | 0.874 | 0.8935 | Yes | 5 | Rank 1 | $\infty$ | Dominated by Variant 1 on $\bar{Q}$ |
| Variant 4 | `7b44c53a-1ce` | *"Rain drummed a fierce beat on the roof,"* | 0.650 | 1.000 | 0.692 | 0.7480 | Yes | 5 | Rank 4 | $\infty$ | Dominated |
| Variant 5 | `a42216e3-d07` | *"The wind howled like wolves in the gloom,"* | 0.750 | 1.000 | 0.763 | 0.8158 | Yes | 5 | Rank 3 | $\infty$ | Dominated |
| Parent | `ca869cc3-6f9` | *"When rain hammered hard on the pane,"* | 0.800 | 1.000 | 0.874 | 0.8686 | Yes | 5 | Rank 2 | $\infty$ | Dominated by Variant 1 and Variant 3 |

* **Generation 1 Front 0 Members:** `a63d13eb-742`.
* **NSGA-II Selection:** Variant 1 (`a63d13eb-742`, $F=0.9106$) strictly dominates all candidates on Quality ($\bar{Q}=0.9000$) while maintaining perfect Rhyme ($R=1.0000$). Selected as elite parent for Generation 2.
* **$\Delta F$:** $+0.0420$ ($0.9106 - 0.8686$). Convergence patience counter remains at 0.

---

### Generation 2

Elite parent `a63d13eb-742` ($\bar{Q}=0.900, R=1.000, S=0.843, F=0.9106$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Pareto Rank | Crowding Dist | Pareto Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `a63d13eb-742` | *"When thunder cracked loud through the night,"* | **0.900** | **1.000** | **0.843** | **0.9106** | **Yes** | 5 | **Rank 0** | $\infty$ | **Non-dominated. Sole Front 0. Retained Elite.** |
| Variant 1 | `c30c12ad-5d0` | *"When storm clouds thundered loud through the night"* | 0.550 | 0.500 | 0.827 | 0.6068 | Yes | 5 | Rank 4 | $\infty$ | Dominated |
| Variant 2 | `6a21f9bc-e1e` | *"When lightning cracked the dark, fierce and bright"* | 0.800 | 0.500 | 0.841 | 0.7352 | Yes | 5 | Rank 2 | $\infty$ | Dominated |
| Variant 3 | `7a7e95b7-d87` | *"When thunder growled and split the quiet night"* | 0.800 | 0.500 | 0.764 | 0.7160 | Yes | 5 | Rank 2 | $\infty$ | Dominated |
| Variant 4 | `4503d4b9-52b` | *"When storm roars rumbled through the shadowed night"* | 0.800 | 1.000 | 0.717 | 0.8292 | Yes | 5 | Rank 1 | $\infty$ | Dominated by parent on $\bar{Q}$ |
| Variant 5 | `6c1d25ca-e23` | *"When heavens boomed and rattled every night"* | 0.700 | 0.500 | 0.708 | 0.6520 | Yes | 5 | Rank 3 | $\infty$ | Dominated |

* **Generation 2 Front 0 Members:** `a63d13eb-742`.
* **NSGA-II Selection:** Parent `a63d13eb-742` strictly dominates all variants on Quality ($\bar{Q}=0.9000$) and Rhyme ($R=1.0000$) and is retained as elite parent for Generation 3.
* **$\Delta F$:** `0.0000` ($0.9106 - 0.9106$). Convergence patience counter increments to 1.

---

### Generation 3 (Final Generation)

Elite parent `a63d13eb-742` was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Feasible | Line Count | Pareto Rank | Crowding Dist | Pareto Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Parent | `a63d13eb-742` | *"When thunder cracked loud through the night,"* | **0.900** | **1.000** | **0.843** | **0.9106** | **Yes** | 5 | **Rank 0** | $\infty$ | **Non-dominated. Winning Poem.** |
| Variant 1 | `c541b51f-af9` | *"When the sky split its roar in the dark,"* | 0.850 | 1.000 | 0.898 | 0.8995 | Yes | 5 | Rank 1 | $\infty$ | Dominated by parent on $\bar{Q}$ ($0.850 < 0.900$) |
| Variant 2 | `8fa1a95c-dab` | *"When the heavens unleashed a fierce blaze,"* | 0.700 | 1.000 | 0.763 | 0.7908 | Yes | 5 | Rank 3 | $\infty$ | Dominated |
| Variant 3 | `19f63ef1-346` | *"When the storm sang its thunderous chant,"* | 0.850 | 0.667 | 0.819 | 0.7965 | Yes | 5 | Rank 2 | $\infty$ | Dominated |
| Variant 4 | `4f097a7f-aaf` | *"When the clouds cracked with electric spite,"* | 0.800 | 1.000 | 0.794 | 0.8485 | Yes | 5 | Rank 2 | $\infty$ | Dominated |
| Variant 5 | `a1b8159b-b59` | *"When the rain drummed a wild, fierce beat,"* | 0.800 | 1.000 | 0.819 | 0.8548 | Yes | 5 | Rank 2 | $\infty$ | Dominated |

* **Final Pool Front 0 Members:**
  1. `a63d13eb-742` (Parent): $\bar{Q}=0.9000, R=1.0000, S=0.8426, F=0.9106$
* **Why `a63d13eb-742` was chosen:**
  - `a63d13eb-742` was the sole non-dominated solution in Front 0 of the final generation's pool ($(\bar{Q}=0.9000, R=1.0000)$ strictly dominates every variant).
  - Selected under the Front-0-of-final-pool rule (`winning_poem = max(front_0, key=lambda p: p.F)`).
* **$\Delta F$:** `0.0000` ($0.9106 - 0.9106$). Convergence patience counter increments to 2. **Stopping rule triggered.**

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8686 | 0.8000 | 1.0000 | 0.8743 | — | 0 | Continue |
| 1 | 0.9106 | 0.9000 | 1.0000 | 0.8426 | +0.0420 | 0 | Continue |
| 2 | 0.9106 | 0.9000 | 1.0000 | 0.8426 | 0.0000 | 1 | Continue (requires 2 consecutive flat generations) |
| 3 | 0.9106 | 0.9000 | 1.0000 | 0.8426 | 0.0000 | 2 | **STOP — Convergence rule triggered** |

### Note on Convergence Rule Execution:
In Generation 1, Variant 1 improved both Quality (0.9000 vs 0.8000) and composite fitness $F$ (0.9106 vs 0.8686). In Generations 2 and 3, no mutation variants dominated `a63d13eb-742` or exceeded its fitness. Consequently, $\Delta F$ remained `0.0000` for 2 consecutive generations (Generations 2 and 3), satisfying the convergence condition ($\Delta F < 0.01$ for 2 consecutive generations) and terminating the run after Generation 3 (4 total generations evaluated: Gen 0, 1, 2, 3) without needing the hard cap of 5.

**Verbatim Log Confirmation:**
```text
20:01:07 | INFO    | src.ea.nsga2 |   Gen 3 | NSGA-II elite: Poem(id=a63d13eb-742, F=0.911, Q̄=0.900, R=1.000, S=0.843) (rank=0) | Best-F: 0.911
20:01:07 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
20:01:07 | INFO    | src.ea.nsga2 |   Final pool Front 0 members: [a63d13eb-742 (F=0.911, Q̄=0.900, R=1.000)]
20:01:07 | INFO    | src.ea.nsga2 |   Final presentation: selected highest-F poem from Front 0 -> a63d13eb-742 (F=0.911)
20:01:07 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_limerick_Fear_f8e80f06 ═══ Generations: 4 | Final F=0.911
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–3 + 3 Mutation rounds) | 6 | 1,985 | 4,179 | **6,164** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 15 mutation variants) | 21 | 8,144 | 945 | **9,089** |
| **Total** | | **27** | **10,129** | **5,124** | **15,253** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 8 pauses totaling **164.50 seconds** (~2m 44.5s):
- **Waiting on `qwen/qwen3.8-27b`:** 6 pauses totaling **132.10s** (enforcing 6,000 TPM limit).
- **Waiting on `openai/gpt-oss-120b`:** 2 pauses totaling **32.40s** (enforcing 6,000 TPM limit).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 19:57:38 | 52.2s | `qwen/qwen3.8-27b` | RPM=5/25 TPM=5445/6000 |
| 2 | 19:58:31 | 2.0s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5693/6000 |
| 3 | 19:58:33 | 1.1s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4830/6000 |
| 4 | 19:58:36 | 2.3s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5464/6000 |
| 5 | 19:58:39 | 52.2s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5480/6000 |
| 6 | 20:00:09 | 22.1s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5495/6000 |
| 7 | 20:00:32 | 31.3s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4925/6000 |
| 8 | 20:01:05 | 1.3s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5488/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 19:57:30 → Completion 20:01:07 IST):** 217.0s (3m 37s)
- **Total Rate-Limit Pause Time:** 164.50s (2m 44.5s)
- **Time to Final Poem excluding pauses:** **52.50s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Rows 60–63)

```csv
nsga2_limerick_Fear_f8e80f06,nsga2,limerick,Fear,0,0.8686,0.8,1.0,0.8743,"When rain hammered hard on the pane, | He curled in the shadows, fearing the pain, | A whispering breath, | A scent of death, | And something unseen clutched at his chain."
nsga2_limerick_Fear_f8e80f06,nsga2,limerick,Fear,1,0.9106,0.9,1.0,0.8426,"When thunder cracked loud through the night, | He slid beneath sheets, trembling with fright, | A soft rustle near, | A cold, hollow sneer, | And a pale hand clasped his wrist in the light."
nsga2_limerick_Fear_f8e80f06,nsga2,limerick,Fear,2,0.9106,0.9,1.0,0.8426,"When thunder cracked loud through the night, | He slid beneath sheets, trembling with fright, | A soft rustle near, | A cold, hollow sneer, | And a pale hand clasped his wrist in the light."
nsga2_limerick_Fear_f8e80f06,nsga2,limerick,Fear,3,0.9106,0.9,1.0,0.8426,"When thunder cracked loud through the night, | He slid beneath sheets, trembling with fright, | A soft rustle near, | A cold, hollow sneer, | And a pale hand clasped his wrist in the light."
```

### `output/logs/per_run_summary.csv` (Row 16)

```csv
nsga2_limerick_Fear_f8e80f06,nsga2,limerick,Fear,0.9106,4,"When thunder cracked loud through the night, | He slid beneath sheets, trembling with fright, | A soft rustle near, | A cold, hollow sneer, | And a pale hand clasped his wrist in the light."
```

### `output/logs/human_feedback.csv` (Row 14 / Index 13)

```csv
2026-11-07T14:32:06.446950+00:00,a63d13eb-742,limerick,nsga2,Fear,"a nervous man who hides under the bed during a thunderstorm, only to find something else already hiding there.",1,good,"When thunder cracked loud through the night, | He slid beneath sheets, trembling with fright, | A soft rustle near, | A cold, hollow sneer, | And a pale hand clasped his wrist in the light.",0.9106,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `3` (Fear)
   - Description: *"a nervous man who hides under the bed during a thunderstorm, only to find something else already hiding there."*
3. **Execution:** Full evolutionary process ran over 4 generations (Gen 0 through Gen 3) in **3m 37s** gross wall-clock time (19:57:30 to 20:01:07 IST), with net generation active time of **52.50s** excluding pauses.
4. **Presentation & Selection:** Winning poem `a63d13eb-742` ($F=0.9106$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: limerick` (inferred from code, not observed) due to the ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `nsga2` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `good` live at 20:02:06 IST (`2026-11-07T14:32:06.446950+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `a63d13eb-742` and verdict `good`.
8. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user answered `no`; tool exited cleanly.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **API warning log events:** 1 transient server 503 retry at 20:00:01 IST:
  ```text
  20:00:01 | WARNING | src.api.client | [Qwen3.8-27B (Groq)] Server error (503), retrying in 1.4s (attempt 1/50)
  ```

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All batches in Gen 0 and all mutation calls returned complete 5-line poems.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `19:57:34 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='In the dark when the thunder did roll,'`
  - `19:57:34 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When lightning flashed bright through th'`
  - `19:57:34 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Beneath the bed where the dust lay deep,'`
  - `19:57:34 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='The storm roared loud, the floorboards d'`
  - `19:57:34 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When rain hammered hard on the pane,'`
  - `19:57:37 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When thunder cracked the night, he fled '`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `19:58:36 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When thunder cracked loud through the ni'`
  - `19:58:36 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The storm’s wild roar shook every wall,'`
  - `19:58:36 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Lightning flashed fierce across the sky,'`
  - `19:58:36 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Rain drummed a fierce beat on the roof,'`
  - `19:58:36 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The wind howled like wolves in the gloom'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `20:00:06 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When storm clouds thundered loud through'`
  - `20:00:06 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When lightning cracked the dark, fierce '`
  - `20:00:06 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When thunder growled and split the quiet'`
  - `20:00:06 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='When storm roars rumbled through the sha'`
  - `20:00:06 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When heavens boomed and rattled every ni'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `20:01:04 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When the sky split its roar in the dark,'`
  - `20:01:04 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When the heavens unleashed a fierce blaz'`
  - `20:01:04 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When the storm sang its thunderous chant'`
  - `20:01:04 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='When the clouds cracked with electric sp'`
  - `20:01:04 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When the rain drummed a wild, fierce bea'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 3 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1049–1050)
- `initial_population_batch_2` (Lines 1052–1081)
- `initial_population_batch_3` (Lines 1083–1088)
- `mutation` Gen 1 (Lines 1090–1127)
- `mutation` Gen 2 (Lines 1129–1166)
- `mutation` Gen 3 (Lines 1168–1205)

