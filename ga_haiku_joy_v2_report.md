# GA + Haiku + Joy (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Attempt 1 (Rejected) | Attempt 2 (Accepted) |
|---|---|---|
| **Run ID** | `ga_haiku_Joy_84a00f21` | `ga_haiku_Joy_7fca053d` |
| **Attempt Number** | 1 of 3 | 2 of 3 |
| **Status / Verdict** | `bad` (User rejected live) | `good` (Accepted by human live) |
| **Date** | 2026-11-08 | 2026-11-08 |
| **Start Time** | 07:58:23 IST (02:28:23 UTC) | 08:03:24 IST (02:33:24 UTC) |
| **Completion Time** | 08:02:27 IST (02:32:27 UTC) | 08:06:27 IST (02:36:27 UTC) |
| **Verdict Logged Time** | 08:03:24 IST (2026-11-08T02:33:24.145179+00:00 UTC) | 08:08:07 IST (2026-11-08T02:38:07.670454+00:00 UTC) |
| **Time to Final Poem** | 4m 04s (244.0s wall-clock) | 3m 03s (183.0s wall-clock) |
| **Total Rate-Limit Pause Time** | 3m 38.3s (218.30s across 10 pauses) | 2m 50.9s (170.90s across 6 pauses) |
| **Time to Final Poem excluding pauses** | **25.70s** (244.0s − 218.30s) | **12.10s** (183.0s − 170.90s) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable structure) | Haiku (3 lines, 5-7-5 syllable structure) |
| **Target Emotion** | Joy | Joy |
| **Scenario** | a child running barefoot through dewy grass as morning sunlight spills over the hilltop. | a child running barefoot through dewy grass as morning sunlight spills over the hilltop. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 | 6 |
| **Generation Cap** | 5 | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent | 5 variants from elite parent |
| **Generations Executed** | 5 (Gen 0, 1, 2, 3, 4) | 4 (Gen 0, 1, 2, 3) |
| **Termination Reason** | Reached max generation 5 | Convergence rule ($\Delta F < 0.01$ for 2 consecutive gens) |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking) | post-fix (hierarchical: '---' → blank lines → 3-line chunking) |
| **Elitism Status** | Yes (`9701be3c-0a7` Gen 2 elite preserved through Gen 3 and 4) | Yes (`39c5b5fe-204` Gen 1 elite preserved through Gen 2 and 3) |
| **Historical Comparison Tag** | First valid GA Haiku Joy run under post-fix parser with full candidate ID and pause logging. | First valid GA Haiku Joy run under post-fix parser with full candidate ID and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

### Attempt 2 Winning Poem (Accepted)

```text
First light on the rise
Bare feet splash through silvered grass
Cheer blooms on the wind
```

| Metric | Value |
|---|---|
| **Poem ID** | `39c5b5fe-204` |
| **Composite Fitness ($F$)** | **0.7750** (displayed as 0.775) |
| **Quality ($\bar{Q}$)** | **0.8000** |
| **Rhyme ($R$)** | **0.5000** (Haiku unrhymed baseline) |
| **Structure ($S$)** | **1.0000** (Perfect 5-7-5 syllable structure) |
| **Line Count** | 3 (target: 3) |
| **Generation Created** | Generation 1 (Variant 5) |
| **Elite Status** | **Yes** — Elite of Gen 1 ($F = 0.7750$), preserved as Elite in Gen 2 and Gen 3 via elitism |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 2 of 3) |

---

### Attempt 1 Rejected Poem (Verdict: `bad`)

```text
Morning gold spills bright
Tiny toes dance on soft grass
Hearts lift with the light
```

| Metric | Value |
|---|---|
| **Poem ID** | `9701be3c-0a7` |
| **Composite Fitness ($F$)** | **0.7917** (displayed as 0.792) |
| **Quality ($\bar{Q}$)** | **0.7500** |
| **Rhyme ($R$)** | **0.6667** (Partial end rhyme: *bright* / *light*) |
| **Structure ($S$)** | **1.0000** (Perfect 5-7-5 syllable structure) |
| **Line Count** | 3 (target: 3) |
| **Generation Created** | Generation 2 (Variant 2) |
| **Human Verdict** | `bad` (Attempt 1 of 3; triggered automated retry for Attempt 2) |

---

## 2. Generation 0 — Full Population (Attempt 2 Accepted Run)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling for Attempt 2 required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 08:03:26 IST):** Generated Candidates 1–5 (3 lines each).
- **Batch 2 (Call 2, 08:04:25 IST):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 had exactly 3 lines.

### Candidate 1 (Batch 1, Candidate #1) — Gen 0 GA Elite (ID: `214425a0-dd6`)

```text
Bright dawn on green hills
Little feet splash dew‑kissed grass
Laughter lifts the light
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.500 | 1.000 | 0.750 | 3 | No (0 discarded) | **Gen 0 Elite (Highest $F=0.7500$). Selected as Gen 0 Elite parent.** |

### Candidate 2 (Batch 1, Candidate #2) — ID: `8cc524fe-648`

```text
Sun spills gold on blades
Barefoot sprint, joy in each step
Morning sings with cheer
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.500 | 1.000 | 0.650 | 3 | No (0 discarded) | Evaluated; $F=0.650$ |

### Candidate 3 (Batch 1, Candidate #3) — ID: `839adc7d-acf`

```text
Dawn’s soft glow embraces
Child runs, grass sings underfoot
Joy blooms in the light
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.500 | 0.882 | 0.621 | 3 | No (0 discarded) | Evaluated; $F=0.621$ |

### Candidate 4 (Batch 1, Candidate #4) — ID: `69893bcd-5f9`

```text
Hilltop sunrise glows
Tiny toes dance on wet grass
Heart sings with the day
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 1.000 | 0.725 | 3 | No (0 discarded) | Evaluated; $F=0.725$ |

### Candidate 5 (Batch 1, Candidate #5) — ID: `6e0e5406-03c`

```text
Morning light cascades
Bare feet race through sparkling dew
Pure delight runs free
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 1.000 | 0.725 | 3 | No (0 discarded) | Evaluated; $F=0.725$ |

### Candidate 6 (Batch 2, Candidate #1) — ID: `8be1963b-5e7`

```text
Morning dew beneath
Barefoot child laughs on hill
Sunlight spills bright gold
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.500 | 0.941 | 0.735 | 3 | No (0 discarded) | Evaluated; $F=0.735$ |

### Gen 0 Summary Table (Attempt 2)

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | GA Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `214425a0-dd6` | 0.750 | 0.500 | 1.000 | 0.750 | 3 | 0 | **Gen 0 Elite (Highest $F=0.7500$)** |
| 2 | `8cc524fe-648` | 0.550 | 0.500 | 1.000 | 0.650 | 3 | 0 | Evaluated |
| 3 | `839adc7d-acf` | 0.550 | 0.500 | 0.882 | 0.621 | 3 | 0 | Evaluated |
| 4 | `69893bcd-5f9` | 0.700 | 0.500 | 1.000 | 0.725 | 3 | 0 | Evaluated |
| 5 | `6e0e5406-03c` | 0.700 | 0.500 | 1.000 | 0.725 | 3 | 0 | Evaluated |
| 6 | `8be1963b-5e7` | 0.750 | 0.500 | 0.941 | 0.735 | 3 | 0 | Evaluated |

* **Gen 0 Elite Selected:** Candidate 1 (`214425a0-dd6`, $F=0.7500$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation GA Evolution (Attempt 2 Accepted Run)

### Generation 1

Elite parent `214425a0-dd6` ($\bar{Q}=0.750, R=0.500, S=1.000, F=0.7500$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `7b4a1aef-0d6` | *"Sunlit hills awake"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated ($F = \text{Parent}$) |
| Variant 2 | `4f88e9dc-fd5` | *"Morning gold spreads wide"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated ($F = \text{Parent}$) |
| Variant 3 | `7907b1f9-cc6` | *"Dawn paints the meadow"* | 0.800 | 0.500 | 0.882 | 0.746 | 3 | Evaluated ($F < \text{Parent}$) |
| Variant 4 | `a1339241-cbb` | *"Golden hills aglow"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated ($F = \text{Parent}$) |
| Variant 5 | `39c5b5fe-204` | *"First light on the rise"* | **0.800** | **0.500** | **1.000** | **0.775** | 3 | **Gen 1 Elite (Highest $F=0.7750$)** |
| Parent | `214425a0-dd6` | *"Bright dawn on green hills"* | 0.750 | 0.500 | 1.000 | 0.7500 | 3 | Evaluated ($F < \text{Variant 5}$) |

* **Gen 1 Elite Selected:** Variant 5 (`39c5b5fe-204`, $F=0.7750$) selected as parent for Generation 2.
* **$\Delta F$:** $+0.0250$ ($0.7750 - 0.7500 = 0.0250 \ge 0.01$). Convergence patience counter remains at 0.

---

### Generation 2

Elite parent `39c5b5fe-204` ($\bar{Q}=0.800, R=0.500, S=1.000, F=0.7750$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `ffd94ebf-d7d` | *"Sunlit hills awake"* | 0.800 | 0.500 | 1.000 | 0.775 | 3 | Evaluated (Tied highest $F$) |
| Variant 2 | `e76f060b-839` | *"Dawn paints gold on blades"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| Variant 3 | `95ee6f74-4f5` | *"Morning light spills wide"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| Variant 4 | `6163a62c-583` | *"Golden rays unfold"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| Variant 5 | `ca91b049-d52` | *"Hilltop glows anew"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| **Parent** | `39c5b5fe-204` | *"First light on the rise"* | **0.800** | **0.500** | **1.000** | **0.7750** | 3 | **Retained Elite (Elitism)** |

* **Gen 2 Elite Selected:** Parent `39c5b5fe-204` retained ($F=0.7750$) via elitism.
* **$\Delta F$:** `0.0000` ($0.7750 - 0.7750$). Convergence patience counter increments to 1.

---

### Generation 3 (Final Generation)

Elite parent `39c5b5fe-204` ($\bar{Q}=0.800, R=0.500, S=1.000, F=0.7750$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `40d77a11-14c` | *"Dawn spills gold on hills"* | 0.800 | 0.500 | 1.000 | 0.775 | 3 | Evaluated (Tied highest $F$) |
| Variant 2 | `17db18b4-066` | *"Morning crowns the hill"* | 0.700 | 0.500 | 1.000 | 0.725 | 3 | Evaluated |
| Variant 3 | `d9c22277-0c1` | *"Sunlit hills arise"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| Variant 4 | `8de33cd1-e1a` | *"Golden glow paints earth"* | 0.700 | 0.500 | 1.000 | 0.725 | 3 | Evaluated |
| Variant 5 | `6c07f91e-7f0` | *"Hilltop drenched in light"* | 0.750 | 0.500 | 1.000 | 0.750 | 3 | Evaluated |
| **Parent** | `39c5b5fe-204` | *"First light on the rise"* | **0.800** | **0.500** | **1.000** | **0.7750** | 3 | **Retained Elite & Winning Poem** |

* **Final Generation Elite:** Parent `39c5b5fe-204` maintained highest fitness ($F=0.7750$) and was retained via elitism.
* **Final Presentation Selection:** Selected elite `39c5b5fe-204` ($F=0.775$).
* **$\Delta F$:** `0.0000` ($0.7750 - 0.7750$).
* **Stopping:** Convergence criterion met — $F$ improved by less than 0.01 for 2 consecutive generations (`deltas: ['0.0000', '0.0000']`).

---

## 4. Stopping Rule Audit

### Attempt 2 (Accepted Run)

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7500 | 0.7500 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.7750 | 0.8000 | 0.5000 | 1.0000 | +0.0250 | 0 | Continue ($\ge 0.01$ improvement) |
| 2 | 0.7750 | 0.8000 | 0.5000 | 1.0000 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 3 | 0.7750 | 0.8000 | 0.5000 | 1.0000 | 0.0000 | 2 | **STOP — Convergence triggered ($\Delta F < 0.01$ for 2 gens)** |

**Verbatim Log Confirmation (Attempt 2):**
```text
08:06:27 | INFO    | src.ea.ga |   Gen 3 | Best F=0.775 | Poem(id=39c5b5fe-204, F=0.775, Q̄=0.800, R=0.500, S=1.000)
08:06:27 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
08:06:27 | INFO    | src.ea.ga |   Final presentation: selected elite -> 39c5b5fe-204 (F=0.775)
08:06:27 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_haiku_Joy_7fca053d ═══ Generations: 4 | Final F=0.775
```

---

### Attempt 1 (Rejected Run)

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7250 | 0.7000 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.7750 | 0.8000 | 0.5000 | 1.0000 | +0.0500 | 0 | Continue |
| 2 | 0.7917 | 0.7500 | 0.6667 | 1.0000 | +0.0167 | 0 | Continue |
| 3 | 0.7917 | 0.7500 | 0.6667 | 1.0000 | 0.0000 | 1 | Continue (patience reaches 1) |
| 4 | 0.7917 | 0.7500 | 0.6667 | 1.0000 | 0.0000 | 2 | **STOP — Reached max generation 5** |

**Verbatim Log Confirmation (Attempt 1):**
```text
08:02:26 | INFO    | src.ea.ga |   Gen 4 | Best F=0.792 | Poem(id=9701be3c-0a7, F=0.792, Q̄=0.750, R=0.667, S=1.000)
08:02:26 | INFO    | src.ea.common | Stopping: reached max generation 5
08:02:26 | INFO    | src.ea.ga |   Final presentation: selected elite -> 9701be3c-0a7 (F=0.792)
08:02:26 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_haiku_Joy_84a00f21 ═══ Generations: 5 | Final F=0.792
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model (Attempt 2 Accepted Run)

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 3 Mutation rounds) | 5 | 1,487 | 1,505 | **2,992** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 15 mutation variants) | 21 | 7,562 | 1,005 | **8,567** |
| **Total (Attempt 2)** | | **26** | **9,049** | **2,510** | **11,559** |

---

### Rate-Limit Pauses Audit (Attempt 2 Accepted Run)

Account rate limiting enforced 6 pauses totaling **170.90 seconds** (~2m 50.9s):
- **Waiting on `qwen/qwen3.8-27b`:** 4 pauses totaling **113.10s**.
- **Waiting on `openai/gpt-oss-120b`:** 2 pauses totaling **57.80s**.

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 08:03:28 | 56.7s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5520/6000 |
| 2 | 08:04:25 | 1.0s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4654/6000 |
| 3 | 08:04:28 | 56.8s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4709/6000 |
| 4 | 08:05:25 | 0.7s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5635/6000 |
| 5 | 08:05:30 | 55.0s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5635/6000 |
| 6 | 08:06:26 | 0.7s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5794/6000 |

### Net Execution Time (Attempt 2 Accepted Run)
- **Gross Wall-Clock Duration (Start 08:03:24 → Completion 08:06:27):** 183.0s (3m 03s)
- **Total Rate-Limit Pause Time:** 170.90s (2m 50.9s)
- **Time to Final Poem excluding pauses:** **12.10s**

---

### Attempt 1 Resource Summary (For Completeness)
- **Calls & Tokens:** 6 GPT calls (4,349 tokens) + 26 Qwen calls (10,638 tokens) = 32 calls, 14,987 total tokens.
- **Rate-Limit Pauses:** 10 pauses totaling **218.30s** (Qwen: 159.10s across 6 pauses; GPT: 59.20s across 4 pauses).
- **Net Execution Time:** 244.0s gross wall-clock − 218.30s pauses = **25.70s**.
- **Combined Session Usage (Attempts 1 + 2):** 58 API calls, 26,546 total tokens, 16 rate-limit pauses totaling 389.20s (~6m 29.2s).

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 73–81)

```csv
ga_haiku_Joy_84a00f21,ga,haiku,Joy,0,0.7250,0.7000,0.5000,1.0000,Barefoot child laughs bright | Dewy grass sings at sunrise | Hilltop glows with joy
ga_haiku_Joy_84a00f21,ga,haiku,Joy,1,0.7750,0.8000,0.5000,1.0000,Golden rays cascade | Tiny feet sprint through cool dew | Hilltop hums with mirth
ga_haiku_Joy_84a00f21,ga,haiku,Joy,2,0.7917,0.7500,0.6667,1.0000,Morning gold spills bright | Tiny toes dance on soft grass | Hearts lift with the light
ga_haiku_Joy_84a00f21,ga,haiku,Joy,3,0.7917,0.7500,0.6667,1.0000,Morning gold spills bright | Tiny toes dance on soft grass | Hearts lift with the light
ga_haiku_Joy_84a00f21,ga,haiku,Joy,4,0.7917,0.7500,0.6667,1.0000,Morning gold spills bright | Tiny toes dance on soft grass | Hearts lift with the light
ga_haiku_Joy_7fca053d,ga,haiku,Joy,0,0.7500,0.7500,0.5000,1.0000,Bright dawn on green hills | Little feet splash dew‑kissed grass | Laughter lifts the light
ga_haiku_Joy_7fca053d,ga,haiku,Joy,1,0.7750,0.8000,0.5000,1.0000,First light on the rise | Bare feet splash through silvered grass | Cheer blooms on the wind
ga_haiku_Joy_7fca053d,ga,haiku,Joy,2,0.7750,0.8000,0.5000,1.0000,First light on the rise | Bare feet splash through silvered grass | Cheer blooms on the wind
ga_haiku_Joy_7fca053d,ga,haiku,Joy,3,0.7750,0.8000,0.5000,1.0000,First light on the rise | Bare feet splash through silvered grass | Cheer blooms on the wind
```

### `output/logs/per_run_summary.csv` (Lines 21–22)

```csv
ga_haiku_Joy_84a00f21,ga,haiku,Joy,0.7917,5,Morning gold spills bright | Tiny toes dance on soft grass | Hearts lift with the light
ga_haiku_Joy_7fca053d,ga,haiku,Joy,0.7750,4,First light on the rise | Bare feet splash through silvered grass | Cheer blooms on the wind
```

### `output/logs/human_feedback.csv` (Lines 18–19 / Indices 16–17)

```csv
2026-11-08T02:33:24.145179+00:00,9701be3c-0a7,haiku,ga,Joy,a child running barefoot through dewy grass as morning sunlight spills over the hilltop.,1,bad,Morning gold spills bright | Tiny toes dance on soft grass | Hearts lift with the light,0.7917,
2026-11-08T02:38:07.670454+00:00,39c5b5fe-204,haiku,ga,Joy,a child running barefoot through dewy grass as morning sunlight spills over the hilltop.,2,good,First light on the rise | Bare feet splash through silvered grass | Cheer blooms on the wind,0.7750,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `1` (Genetic Algorithm / GA)
   - Emotion: `1` (Joy)
   - Description: *"a child running barefoot through dewy grass as morning sunlight spills over the hilltop."*
3. **Attempt 1 Evolution:** Ran over 5 generations (Gen 0 through Gen 4) in **4m 04s** gross wall-clock time (07:58:23 to 08:02:27 IST).
4. **Attempt 1 Presentation & Verdict:** Candidate `9701be3c-0a7` ($F=0.7917$) displayed. User entered `bad` live at 08:03:24 IST (`2026-11-08T02:33:24.145179+00:00` UTC).
5. **Automated Fresh Retry Triggered:** As specified in `src/interactive/tool.py` line 144–148, `verdict == "bad"` initiated a completely fresh full GA process (fresh population → generations → stopping rule) as **Attempt 2/3**.
6. **Attempt 2 Evolution:** Ran over 4 generations (Gen 0 through Gen 3) in **3m 03s** gross wall-clock time (08:03:24 to 08:06:27 IST), with net generation active time of **12.10s** excluding pauses.
7. **Attempt 2 Presentation & Verdict:** Winning poem `39c5b5fe-204` ($F=0.7750$) was displayed in styled Rich panel; user entered `good` live at 08:08:07 IST (`2026-11-08T02:38:07.670454+00:00` UTC).
8. **Logging:** Feedback logged to `human_feedback.csv` with UUID `39c5b5fe-204` and verdict `good`.
9. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool printed `Session complete. Goodbye!` and exited cleanly.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Discarded incomplete lines:** **0**. All batches in both attempts returned complete 3-line haikus.

### Per-Generation Candidate Line Counts (from `interactive.log`)

#### Attempt 2 (Accepted Run):
- **Generation 0:**
  - `08:03:26 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Bright dawn on green hills'`
  - `08:03:26 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Sun spills gold on blades'`
  - `08:03:26 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dawn’s soft glow embraces'`
  - `08:03:26 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Hilltop sunrise glows'`
  - `08:03:26 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Morning light cascades'`
  - `08:04:25 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Morning dew beneath'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `08:04:27 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Sunlit hills awake'`
  - `08:04:27 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Morning gold spreads wide'`
  - `08:04:27 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dawn paints the meadow'`
  - `08:04:27 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Golden hills aglow'`
  - `08:04:27 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='First light on the rise'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `08:05:27 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Sunlit hills awake'`
  - `08:05:27 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dawn paints gold on blades'`
  - `08:05:27 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Morning light spills wide'`
  - `08:05:27 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Golden rays unfold'`
  - `08:05:27 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Hilltop glows anew'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `08:05:30 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Dawn spills gold on hills'`
  - `08:05:30 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Morning crowns the hill'`
  - `08:05:30 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Sunlit hills arise'`
  - `08:05:30 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Golden glow paints earth'`
  - `08:05:30 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Hilltop drenched in light'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 3 Discarded Lines:** 0.

---

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)

**Attempt 1 (`ga_haiku_Joy_84a00f21`):**
- `initial_population_batch_1`: Lines 1486–1505
- `initial_population_batch_2`: Lines 1507–1510
- `mutation` Gen 1: Lines 1512–1535
- `mutation` Gen 2: Lines 1537–1564
- `mutation` Gen 3: Lines 1566–1585
- `mutation` Gen 4: Lines 1587–1614

**Attempt 2 (`ga_haiku_Joy_7fca053d`):**
- `initial_population_batch_1`: Lines 1616–1635
- `initial_population_batch_2`: Lines 1637–1640
- `mutation` Gen 1: Lines 1642–1669
- `mutation` Gen 2: Lines 1671–1698
- `mutation` Gen 3: Lines 1700–1727

