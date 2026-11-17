# GA + Limerick + Joy (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_limerick_Joy_7356698e` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-07 |
| **Start Time** | 20:14:40 IST (14:44:40 UTC) |
| **Completion Time** | 20:17:49 IST (14:47:49 UTC) |
| **Verdict Logged Time** | 20:20:15 IST (2026-11-07T14:50:15.655421+00:00 UTC) |
| **Time to Final Poem** | 3m 09s (189.0s wall-clock, 20:14:40 → 20:17:49 IST) |
| **Total Rate-Limit Pause Time** | 2m 46.6s (166.60s waiting across 11 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **22.40s** (189.0s gross wall-clock − 166.60s rate-limit waits) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
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
| **Run Status / Validity** | `valid - presented poem confirmed as Gen 1 elite with highest F preserved through Gen 2 and Gen 3` |
| **Elitism Status** | **Yes** — The presented poem (`ebe241d6-b99`) was generated in Gen 1 (Variant 1), confirmed as elite of Gen 1 ($F=0.8516$), preserved as elite in Gen 2 and Gen 3 via elitism, and presented as the winning poem. |
| **Historical Comparison Tag** | First valid GA Limerick Joy run under post-fix parser with full ID and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
A clumsy baker in wedding attire,
Set his tiered marvel to rise higher.
It tumbled, then sang,
A sweet, joyous clang,
Now guests cheer the crumble, their hearts on fire.
```

| Metric | Value |
|---|---|
| **Poem ID** | `ebe241d6-b99` |
| **Composite Fitness ($F$)** | **0.8516** (displayed as 0.852) |
| **Quality ($\bar{Q}$)** | **0.8500** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.7064** |
| **Rhyme Scheme** | AABBA — *attire* / *higher* / *sang* / *clang* / *fire* |
| **Line Count** | 5 (target: 5) |
| **Generation Created** | Generation 1 (Variant 1) |
| **Elite Status** | **Yes** — Elite of Gen 1 ($F = 0.8516$), preserved as Elite in Gen 2 and Gen 3 |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling required 3 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 20:14:43 IST):** Generated Candidates 1–5 (5 lines each).
- **Batch 2 (Call 2, 20:14:46 IST):** Returned 4 lines (`There once was a baker quite tumble... They ate crumbs`), cleanly discarded by the parser because limerick requires exactly 5 lines.
- **Batch 3 (Call 3, 20:14:48 IST):** Generated Candidate 6 (5 lines).

All 6 evaluated candidates in Generation 0 had exactly 5 lines.

### Candidate 1 (Batch 1, Candidate #1) — ID: `bbc3b544-7a7`

```text
There once was a baker named Lee bright
He built a tall cake that shone so bright
But the floor gave a sigh
And frosting fell with sigh
Yet guests all cheered the sweet mess so bright
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.300 | 0.000 | 0.882 | 0.371 | 5 | No (0 discarded) | Evaluated; $F=0.371$ |

### Candidate 2 (Batch 1, Candidate #2) — ID: `449edafd-26b`

```text
A clumsy chef named Sue took a bite
She set a grand tier for wedding night bright
The cake hit the floor
It crumbled once more
And lovers declared it the best delight bright
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.300 | 0.833 | 0.763 | 0.549 | 5 | No (0 discarded) | Evaluated; $F=0.549$ |

### Candidate 3 (Batch 1, Candidate #3) — Gen 0 GA Elite (ID: `40dc0ae9-d71`)

```text
Old Marco the baker, quite spry and bright
Placed his masterpiece high in the light
A wobble, a crash
Turned crumbs into cash
Now all shout, “More of that happy bite bright!”
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.450 | 0.833 | 0.819 | 0.638 | 5 | No (0 discarded) | **Gen 0 Elite (Highest $F=0.6381$). Selected as Gen 0 Elite parent.** |

### Candidate 4 (Batch 1, Candidate #4) — ID: `25465335-bfc`

```text
Young Nina prepared layers so neat and bright
When the timer rang, the cake took a flight
It splashed on the floor
But guests asked for more
And they sang for the mess, joy complete bright
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.450 | 0.833 | 0.708 | 0.610 | 5 | No (0 discarded) | Evaluated; $F=0.610$ |

### Candidate 5 (Batch 1, Candidate #5) — ID: `1975608e-1f4`

```text
Chef Benny’s dessert was set to excite bright
When the guests came, it fell with a fright
The frosting did slide
Into bowls far and wide
Now laughter erupts over each sugary bite bright
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.833 | 0.589 | 0.630 | 5 | No (0 discarded) | Evaluated; $F=0.630$ |

### Candidate 6 (Batch 3, Candidate #1) — ID: `7e62ef65-558`

```text
There once was a baker, quite clumsy
His cake tottered, then fell—clumsy
Guests gasped at the sight, pure delight
Then crumbs turned sweet, pure delight
And love was served in a mess—still clumsy
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.350 | 0.000 | 0.684 | 0.346 | 5 | No (0 discarded) | Evaluated; $F=0.346$ |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | GA Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `bbc3b544-7a7` | 0.300 | 0.000 | 0.882 | 0.371 | 5 | 0 | Evaluated |
| 2 | `449edafd-26b` | 0.300 | 0.833 | 0.763 | 0.549 | 5 | 0 | Evaluated |
| 3 | `40dc0ae9-d71` | 0.450 | 0.833 | 0.819 | 0.638 | 5 | 0 | **Gen 0 Elite (Highest $F=0.6381$)** |
| 4 | `25465335-bfc` | 0.450 | 0.833 | 0.708 | 0.610 | 5 | 0 | Evaluated |
| 5 | `1975608e-1f4` | 0.550 | 0.833 | 0.589 | 0.630 | 5 | 0 | Evaluated |
| 6 | `7e62ef65-558` | 0.350 | 0.000 | 0.684 | 0.346 | 5 | 0 | Evaluated |

* **Gen 0 Elite Selected:** Candidate 3 (`40dc0ae9-d71`, $F=0.6381$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation GA Evolution

### Generation 1

Elite parent `40dc0ae9-d71` ($\bar{Q}=0.450, R=0.833, S=0.819, F=0.6381$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `ebe241d6-b99` | *"A clumsy baker in wedding attire,"* | **0.850** | **1.000** | **0.706** | **0.852** | 5 | **Gen 1 Elite (Highest $F=0.8516$)** |
| Variant 2 | `c1249f83-88e` | *"The baker, all flour, slipped on a sigh,"* | 0.400 | 0.833 | 0.898 | 0.633 | 5 | Evaluated |
| Variant 3 | `1edf017b-a26` | *"In tuxedo he whisked, a bright grin,"* | 0.550 | 1.000 | 0.819 | 0.730 | 5 | Evaluated |
| Variant 4 | `daa7d114-64c` | *"He pranced with a whisk, eyes all alight"* | 0.650 | 0.500 | 0.898 | 0.674 | 5 | Evaluated |
| Variant 5 | `99fdfeef-b28` | *"A baker, all clumsy, yet keen,"* | 0.550 | 1.000 | 0.953 | 0.763 | 5 | Evaluated |
| Parent | `40dc0ae9-d71` | *"Old Marco the baker, quite spry and bright"* | 0.450 | 0.833 | 0.819 | 0.6381 | 5 | Evaluated ($F < \text{Variant 1}$) |

* **Gen 1 Elite Selected:** Variant 1 (`ebe241d6-b99`, $F=0.8516$) selected as parent for Generation 2.
* **$\Delta F$:** $+0.2135$ ($0.8516 - 0.6381 = 0.2135 \ge 0.01$). Convergence patience counter remains at 0.

---

### Generation 2

Elite parent `ebe241d6-b99` ($\bar{Q}=0.850, R=1.000, S=0.706, F=0.8516$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `d0a2acdb-304` | *"A clumsy baker in a tux so bright"* | 0.500 | 0.333 | 0.717 | 0.512 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 2 | `0c799da1-b82` | *"A jittery chef in his wedding tuxedo"* | 0.750 | 0.500 | 0.534 | 0.633 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 3 | `f64bf5eb-371` | *"A bumbling baker dressed up for the vows"* | 0.750 | 0.667 | 0.684 | 0.713 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 4 | `ad43308f-335` | *"A nervous pastry man in crisp white suit"* | 0.800 | 0.500 | 0.605 | 0.676 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 5 | `a2b4c11b-a53` | *"A goofy baker in his tux of pearl white"* | 0.800 | 0.667 | 0.739 | 0.751 | 5 | Evaluated ($F < \text{Parent}$) |
| **Parent** | `ebe241d6-b99` | *"A clumsy baker in wedding attire,"* | **0.850** | **1.000** | **0.706** | **0.8516** | 5 | **Retained Elite (Elitism)** |

* **Gen 2 Elite Selected:** Parent `ebe241d6-b99` retained ($F=0.8516$) via elitism because no variant exceeded parent fitness.
* **$\Delta F$:** `0.0000$ ($0.8516 - 0.8516$). Convergence patience counter increments to 1.

---

### Generation 3 (Final Generation)

Elite parent `ebe241d6-b99` ($\bar{Q}=0.850, R=1.000, S=0.706, F=0.8516$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `93bc6b25-0f0` | *"A baker in tux slipped on frosting, then fled,"* | 0.850 | 1.000 | 0.519 | 0.805 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 2 | `11be2d3b-94b` | *"In a suit the baker did wobble, cake sway,"* | 0.650 | 0.667 | 0.557 | 0.631 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 3 | `e5161d8e-af9` | *"The clumsy chef in his tux did misplace,"* | 0.700 | 1.000 | 0.670 | 0.767 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 4 | `b798de8f-b95` | *"A tuxed‑clad baker tripped on his own glaze,"* | 0.750 | 0.667 | 0.590 | 0.689 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 5 | `425b9382-2f1` | *"Dressed sharp, the baker slipped, cake gave a sigh,"* | 0.800 | 0.500 | 0.651 | 0.688 | 5 | Evaluated ($F < \text{Parent}$) |
| **Parent** | `ebe241d6-b99` | *"A clumsy baker in wedding attire,"* | **0.850** | **1.000** | **0.706** | **0.8516** | 5 | **Retained Elite & Winning Poem** |

* **Final Generation Elite:** Parent `ebe241d6-b99` maintained highest fitness ($F=0.8516$) and was retained via elitism.
* **Final Presentation Selection:** Selected elite `ebe241d6-b99` ($F=0.852$).
* **$\Delta F$:** `0.0000` ($0.8516 - 0.8516$).
* **Stopping:** Convergence criterion met — $F$ improved by less than 0.01 for 2 consecutive generations (`deltas: ['0.0000', '0.0000']`).

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.6381 | 0.4500 | 0.8333 | 0.8191 | — | 0 | Continue |
| 1 | 0.8516 | 0.8500 | 1.0000 | 0.7064 | +0.2135 | 0 | Continue ($\ge 0.01$ improvement) |
| 2 | 0.8516 | 0.8500 | 1.0000 | 0.7064 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 3 | 0.8516 | 0.8500 | 1.0000 | 0.7064 | 0.0000 | 2 | **STOP — Convergence triggered ($\Delta F < 0.01$ for 2 gens)** |

### Note on Stopping Rule Execution:
In Generation 1, Variant 1 improved fitness significantly from $F=0.6381$ to $F=0.8516$ ($\Delta F = +0.2135 \ge 0.01$). In Generation 2, no variant surpassed the parent ($F=0.8516$), yielding $\Delta F = 0.0000 < 0.01$ and incrementing the patience counter to 1. In Generation 3, no variant surpassed the parent, again yielding $\Delta F = 0.0000 < 0.01$. The patience counter reached 2, triggering the early stopping rule:
`Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])`.

**Verbatim Log Confirmation:**
```text
20:17:49 | INFO    | src.ea.ga |   Gen 3 | Best F=0.852 | Poem(id=ebe241d6-b99, F=0.852, Q̄=0.850, R=1.000, S=0.706)
20:17:49 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
20:17:49 | INFO    | src.ea.ga |   Final presentation: selected elite -> ebe241d6-b99 (F=0.852)
20:17:49 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_limerick_Joy_7356698e ═══ Generations: 4 | Final F=0.852
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–3 + 3 Mutation rounds) | 6 | 2,061 | 4,929 | **6,990** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 15 mutation variants) | 21 | 8,169 | 858 | **9,027** |
| **Total** | | **27** | **10,230** | **5,787** | **16,017** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 11 pauses totaling **166.60 seconds** (~2m 46.6s):
- **Waiting on `qwen/qwen3.8-27b`:** 8 pauses totaling **110.80s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 3 pauses totaling **55.80s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 20:14:50 | 51.1s | `qwen/qwen3.8-27b` | RPM=5/25 TPM=5496/6000 |
| 2 | 20:15:44 | 2.0s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4863/6000 |
| 3 | 20:15:47 | 2.0s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5498/6000 |
| 4 | 20:15:50 | 0.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 5 | 20:15:50 | 51.1s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 6 | 20:16:42 | 2.4s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4914/6000 |
| 7 | 20:16:48 | 2.2s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5475/6000 |
| 8 | 20:16:50 | 0.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5481/6000 |
| 9 | 20:16:51 | 51.4s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5483/6000 |
| 10 | 20:17:44 | 1.4s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5877/6000 |
| 11 | 20:17:46 | 2.0s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5494/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 20:14:40 → Completion 20:17:49):** 189.0s (3m 09s)
- **Total Rate-Limit Pause Time:** 166.60s (2m 46.6s)
- **Time to Final Poem excluding pauses:** **22.40s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 66–69)

```csv
ga_limerick_Joy_7356698e,ga,limerick,Joy,0,0.6381,0.4500,0.8333,0.8191,"Old Marco the baker, quite spry and bright | Placed his masterpiece high in the light | A wobble, a crash | Turned crumbs into cash | Now all shout, “More of that happy bite bright!”"
ga_limerick_Joy_7356698e,ga,limerick,Joy,1,0.8516,0.8500,1.0000,0.7064,"A clumsy baker in wedding attire, | Set his tiered marvel to rise higher. | It tumbled, then sang, | A sweet, joyous clang, | Now guests cheer the crumble, their hearts on fire."
ga_limerick_Joy_7356698e,ga,limerick,Joy,2,0.8516,0.8500,1.0000,0.7064,"A clumsy baker in wedding attire, | Set his tiered marvel to rise higher. | It tumbled, then sang, | A sweet, joyous clang, | Now guests cheer the crumble, their hearts on fire."
ga_limerick_Joy_7356698e,ga,limerick,Joy,3,0.8516,0.8500,1.0000,0.7064,"A clumsy baker in wedding attire, | Set his tiered marvel to rise higher. | It tumbled, then sang, | A sweet, joyous clang, | Now guests cheer the crumble, their hearts on fire."
```

### `output/logs/per_run_summary.csv` (Line 19)

```csv
ga_limerick_Joy_7356698e,ga,limerick,Joy,0.8516,4,"A clumsy baker in wedding attire, | Set his tiered marvel to rise higher. | It tumbled, then sang, | A sweet, joyous clang, | Now guests cheer the crumble, their hearts on fire."
```

### `output/logs/human_feedback.csv` (Line 16 / Index 14)

```csv
2026-11-07T14:50:15.655421+00:00,ebe241d6-b99,limerick,ga,Joy,"a clumsy baker whose wedding cake collapses just before the guests arrive, but the happy mess becomes the most loved dessert of the night.",1,good,"A clumsy baker in wedding attire, | Set his tiered marvel to rise higher. | It tumbled, then sang, | A sweet, joyous clang, | Now guests cheer the crumble, their hearts on fire.",0.8516,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `1` (Genetic Algorithm / GA)
   - Emotion: `1` (Joy)
   - Description: *"a clumsy baker whose wedding cake collapses just before the guests arrive, but the happy mess becomes the most loved dessert of the night."*
3. **Execution:** Full evolutionary process ran over 4 generations (Gen 0 through Gen 3) in **3m 09s** gross wall-clock time (20:14:40 to 20:17:49 IST), with net generation active time of **22.40s** excluding pauses.
4. **Presentation & Selection:** Winning poem `ebe241d6-b99` ($F=0.8516$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: limerick` (inferred from code, not observed) due to the ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `ga` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `good` live at 20:20:15 IST (`2026-11-07T14:50:15.655421+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `ebe241d6-b99` and verdict `good`.
8. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool exited cleanly.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).

All generator outputs produced clean poetic lines without appending extraneous rhyme-scheme labels.

### Parser Discard Event (Batch 2, Generation 0)
At 20:14:46 IST during initial population generation, API call 2 returned 4 lines (`There once was a baker quite tumble... They ate crumbs`):
```text
20:14:46 | INFO    | src.prompts.generator | Parser discarded 4 incomplete line(s) that did not meet exact target of 5 lines for limerick
```
The generator automatically triggered Batch 3 (Call 3), which returned Candidate 6 with exactly 5 lines, completing the required population of 6.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `20:14:43 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='There once was a baker named Lee bright'`
  - `20:14:43 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='A clumsy chef named Sue took a bite'`
  - `20:14:43 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Old Marco the baker, quite spry and brig'`
  - `20:14:43 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Young Nina prepared layers so neat and b'`
  - `20:14:43 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Chef Benny’s dessert was set to excite b'`
  - `20:14:48 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='There once was a baker, quite clumsy'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded:** 4 incomplete lines from Batch 2.

- **Generation 1 (Mutation Variants):**
  - `20:15:47 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A clumsy baker in wedding attire,'`
  - `20:15:47 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The baker, all flour, slipped on a sigh,'`
  - `20:15:47 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='In tuxedo he whisked, a bright grin,'`
  - `20:15:47 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='He pranced with a whisk, eyes all alight'`
  - `20:15:47 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='A baker, all clumsy, yet keen,'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `20:16:47 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A clumsy baker in a tux so bright'`
  - `20:16:47 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='A jittery chef in his wedding tuxedo'`
  - `20:16:47 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='A bumbling baker dressed up for the vows'`
  - `20:16:47 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='A nervous pastry man in crisp white suit'`
  - `20:16:47 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='A goofy baker in his tux of pearl white'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `20:17:44 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='A baker in tux slipped on frosting, then'`
  - `20:17:44 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='In a suit the baker did wobble, cake swa'`
  - `20:17:44 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The clumsy chef in his tux did misplace,'`
  - `20:17:44 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='A tuxed‑clad baker tripped on his own gl'`
  - `20:17:44 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Dressed sharp, the baker slipped, cake g'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 3 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1199–1236)
- `initial_population_batch_2` (Lines 1238–1242)
- `initial_population_batch_3` (Lines 1244–1249)
- `mutation` Gen 1 (Lines 1251–1288)
- `mutation` Gen 2 (Lines 1290–1319)
- `mutation` Gen 3 (Lines 1321–1358)

