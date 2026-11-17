# NSGA-II + Limerick + Sorrow (v2 Rerun) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_limerick_Sorrow_de5ca899` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-06 |
| **Start Time** | 14:46:49 IST |
| **Completion Time** | 14:49:52 IST |
| **Verdict Logged Time** | 14:59:12 IST (2026-11-06T09:29:12.066625+00:00 UTC) |
| **Time to Final Poem** | 3m 03s (183s wall-clock, 14:46:49 → 14:49:52) |
| **Algorithm** | NSGA-II (non-dominated sorting on two search objectives: Quality and Rhyme) |
| **Poem Type** | Limerick (5 lines, AABBA rhyme scheme) |
| **Target Emotion** | Sorrow |
| **Scenario** | A soldier saying goodbye at the train station, not knowing if he'll return. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 5-line chunking, with candidate line-count logging) |
| **Run Status / Validity** | `valid - presented poem confirmed as Front 0 member of final pool with highest composite F` |
| **Front 0 Selection Status** | **Yes** — The presented poem (`da3255a0-d29`) is a member of Front 0 of the final pool with the highest composite fitness ($F = 0.8766$). |
| **Historical Comparison Tag** | Rerun 1 (`nsga2_limerick_Sorrow_3971360e`) was superseded due to presenting a non-final-pool candidate; earlier runs (`nsga2_limerick_Sorrow_29d9cad1`, `ga_limerick_Sorrow_102c8c40`, etc.) were pre-fix parser. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Steam curled like ghosts as the night grew dim,
He whispered his oath on a trembling limb,
The rails sang a moan,
His heart turned to stone,
And the station awoke to a mournful hymn.
```

| Metric | Value |
|---|---|
| **Poem ID** | `da3255a0-d29` |
| **Composite Fitness ($F$)** | **0.8766** |
| **Quality ($\bar{Q}$)** | **0.9000** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.7064** |
| **Rhyme Scheme** | AABBA — *dim* / *limb* / *moan* / *stone* / *hymn* |
| **Line Count** | 5 (target: 5) |
| **Generation Created** | Generation 2 (Variant 3) |
| **Pareto Rank in Final Pool** | Rank 0 (Non-dominated) |
| **Front 0 Member with Highest $F$** | **Yes** ($F=0.8766$ vs co-member Variant 5 $F=0.8628$) |
| **Selection Rule** | Front-0-of-final-pool rule (`max(front_0, key=lambda p: p.F)`) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is a feasibility constraint ($S \ge 0.30$), not a search objective. Composite $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for stopping and logging only.

Initial population sampling required 4 API calls:
- **Batch 1 (Call 1, 14:46:52):** Returned 0 complete poem lines (`raw_generator.log` line 351).
- **Batch 2 (Call 2, 14:46:54):** Generated Candidates 1–5 (all 5 lines each).
- **Batch 3 (Call 3, 14:46:57):** Returned 4 lines; cleanly discarded by the parser.
- **Batch 4 (Call 4, 14:46:59):** Generated Candidate 6 (5 lines).

All 6 evaluated candidates in Generation 0 had exactly 5 lines.

### Candidate 1 (Batch 2, Candidate #1) — Gen 0 NSGA-II Elite (ID: `24593df6-e69`)

```text
On the platform they whispered goodbye,
As the steam rose and clouded the sky,
His eyes met the rail,
A soft, trembling wail,
And the night swallowed hope with a sigh.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 1.000 | 0.906 | 0.876 | 5 | No (0 discarded) | **Rank 0 — Non-dominated. Highest $F$ in Front 0. Selected as Gen 0 Elite parent.** |

### Candidate 2 (Batch 2, Candidate #2) — (ID: `not recorded`)

```text
By the tracks he knelt, his hand on the rail,
While the whistle sang mournful and pale,
A tear slipped down,
A silent town,
And his heart beat slow like a frail.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 1.000 | 0.851 | 0.788 | 5 | No (0 discarded) | **Rank 1 — Dominated** by Candidate 1 on Quality ($\bar{Q}=0.650 < 0.800$, same $R=1.000$) |

### Candidate 3 (Batch 2, Candidate #3) — (ID: `not recorded`)

```text
The soldier bowed low to the train’s iron face,
His coat brushed the dust of the place,
He whispered, “I’ll—”
A breath, a still—
Then vanished like smoke in the space.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.850 | 0.500 | 0.804 | 0.751 | 5 | No (0 discarded) | **Rank 0 — Non-dominated.** Trade-off solution: higher $\bar{Q}$ (0.850 vs 0.800), lower $R$ (0.500 vs 1.000). |

### Candidate 4 (Batch 2, Candidate #4) — (ID: `not recorded`)

```text
At the station the crowds turned away,
Their shadows grew longer that day,
He clutched his last kiss,
In the fog’s cold abyss,
And the rails hummed a mournful lay.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 1.000 | 0.898 | 0.875 | 5 | No (0 discarded) | **Rank 0 — Non-dominated.** Tied with Candidate 1 on $(\bar{Q}, R)$; lower Structure (0.898 vs 0.906). |

### Candidate 5 (Batch 2, Candidate #5) — (ID: `not recorded`)

```text
The locomotive roared, cold and austere,
While his promise dissolved in thin air,
He left with a sigh,
A tear in his eye,
And the silence returned, stark and bare.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 0.667 | 0.874 | 0.685 | 5 | No (0 discarded) | **Rank 2 — Dominated** by Candidates 1 and 4 on both $\bar{Q}$ and $R$. |

### Candidate 6 (Batch 4, Candidate #1) — (ID: `not recorded`)

```text
At the cold platform we stood, hearts gray
He whispered goodbye as night fell gray
All the clocks stopped, sighs fell
Dreams drift low, night shadows fell
He boarded the train, his hope turned gray
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.500 | 0.000 | 0.827 | 0.457 | 5 | No (0 discarded) | **Rank 3 — Dominated** ($R=0.000$, lowest $\bar{Q}=0.500$). |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | Pareto Rank |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `24593df6-e69` | 0.800 | 1.000 | 0.906 | 0.876 | 5 | 0 | **Rank 0 (Elite — Highest $F$)** |
| 2 | `not recorded` | 0.650 | 1.000 | 0.851 | 0.788 | 5 | 0 | Rank 1 |
| 3 | `not recorded` | 0.850 | 0.500 | 0.804 | 0.751 | 5 | 0 | **Rank 0** |
| 4 | `not recorded` | 0.800 | 1.000 | 0.898 | 0.875 | 5 | 0 | **Rank 0** |
| 5 | `not recorded` | 0.600 | 0.667 | 0.874 | 0.685 | 5 | 0 | Rank 2 |
| 6 | `not recorded` | 0.500 | 0.000 | 0.827 | 0.457 | 5 | 0 | Rank 3 |

* **Generation 0 Front 0 Members:** Candidate 1 (`24593df6-e69`), Candidate 3, Candidate 4.
* **Gen 0 Elite Selected:** Candidate 1 (`24593df6-e69`) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `24593df6-e69` ($\bar{Q}=0.800, R=1.000, S=0.906, F=0.876$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Pareto Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Parent (Gen 0) | `24593df6-e69` | *"On the platform they whispered goodbye,"* | 0.800 | 1.000 | 0.906 | **0.8765** | 5 | **Rank 0 — Retained Elite (Highest $F$)** |
| Variant 1 | `not recorded` | *"On the cold rails his promise fell mute,"* | 0.700 | 1.000 | 0.929 | 0.8322 | 5 | Rank 2 — Dominated by parent on $\bar{Q}$ |
| Variant 2 | `not recorded` | *"The platform held echoes of sorrow,"* | 0.750 | 0.667 | 0.706 | 0.7182 | 5 | Rank 2 — Dominated by parent on $\bar{Q}$ and $R$ |
| Variant 3 | `not recorded` | *"Beneath iron arches the wind sighed,"* | 0.750 | 1.000 | 0.763 | 0.8158 | 5 | Rank 1 — Dominated by parent on $\bar{Q}$ |
| Variant 4 | `not recorded` | *"The station’s lamp flickered, forlorn,"* | 0.800 | 1.000 | 0.898 | 0.8745 | 5 | **Rank 0** — Non-dominated (tied on $\bar{Q}, R$; lower $S$) |
| Variant 5 | `not recorded` | *"Steam rose like ghosts from the line,"* | 0.800 | 1.000 | 0.796 | 0.8490 | 5 | **Rank 0** — Non-dominated (tied on $\bar{Q}, R$; lower $S$) |

* **Generation 1 Front 0 Members:** `24593df6-e69` (Parent), Variant 4, Variant 5.
* **NSGA-II Selection:** Parent `24593df6-e69` maintains highest $F$ (0.8765) in Front 0 and is retained as elite parent for Generation 2.
* **Best-$F$ Poem:** `24593df6-e69` ($F=0.8765$).
* **$\Delta F$:** `0.0000` — Convergence patience counter increments to 1.

---

### Generation 2 (Final Generation)

Elite parent `24593df6-e69` was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Pareto Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `not recorded` | *"On the cold rails his farewell did sigh,"* | 0.800 | 0.667 | 0.929 | 0.7989 | 5 | Rank 2 — Dominated |
| Variant 2 | `not recorded` | *"The night train exhaled a grey, heavy sigh,"* | 0.750 | 1.000 | 0.843 | 0.8358 | 5 | Rank 2 — Dominated |
| Variant 3 | `da3255a0-d29` | *"Steam curled like ghosts as the night grew dim,"* | **0.900** | **1.000** | 0.706 | **0.8766** | 5 | **Rank 0 — Non-dominated. Highest $F$. Winning Poem.** |
| Variant 4 | `not recorded` | *"Beneath lanterns the farewells were hushed,"* | 0.800 | 0.667 | 0.874 | 0.7852 | 5 | Rank 2 — Dominated |
| Variant 5 | `not recorded` | *"The platform stood still as the clouds bled gray,"* | **0.900** | **1.000** | 0.651 | 0.8628 | 5 | **Rank 0 — Non-dominated.** (Lower $S$ than Variant 3) |
| Parent (Gen 0) | `24593df6-e69` | *"On the platform they whispered goodbye,"* | 0.800 | 1.000 | 0.906 | 0.8765 | 5 | Rank 1 — Strictly dominated by Variant 3 & Variant 5 on $\bar{Q}$ ($0.800 < 0.900$) |

* **Final Pool Front 0 Members:**
  1. `da3255a0-d29` (Variant 3): $\bar{Q}=0.900, R=1.000, S=0.7064, F=0.8766$
  2. Variant 5 (`not recorded`): $\bar{Q}=0.900, R=1.000, S=0.6510, F=0.8628$
* **Why `da3255a0-d29` was chosen:**
  - Both Variant 3 (`da3255a0-d29`) and Variant 5 achieved $\bar{Q}=0.900$ and $R=1.000$, strictly dominating the incoming parent `24593df6-e69` ($\bar{Q}=0.800, R=1.000$).
  - In accordance with the post-fix NSGA-II rule (`winning_poem = max(front_0, key=lambda p: p.F)`), `da3255a0-d29` was chosen from Front 0 of the final pool because its higher Structure score ($S = 0.7064$ vs $0.6510$) gave it the highest composite fitness ($F = 0.8766$ vs $0.8628$).
* **$\Delta F$:** `+0.0001` ($0.87661 - 0.87650 = 0.00011 < 0.01$). Convergence patience counter increments to 2. **Stopping rule triggered.**

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8765 | 0.8000 | 1.0000 | 0.9060 | — | 0 | Continue |
| 1 | 0.8765 | 0.8000 | 1.0000 | 0.9060 | 0.0000 | 1 | Continue (requires 2 consecutive flat generations) |
| 2 | 0.8766 | 0.9000 | 1.0000 | 0.7064 | 0.0001 | 2 | **STOP — Convergence rule triggered** |

### Note on Objective Dynamics vs. Flat Composite $F$:
In Generation 2, the search successfully discovered higher-quality solutions: Quality $\bar{Q}$ jumped from **0.8000 to 0.9000** (+0.1000) while maintaining perfect Rhyme ($R = 1.0000$). 

However, because Structure dropped from **0.9060 to 0.7064** (-0.1996), the composite fitness $F$ remained virtually flat:
$$\Delta F = (0.50 \times +0.1000) + (0.25 \times 0.0000) + (0.25 \times -0.1996) = +0.0500 - 0.0499 = +0.0001$$
Because $\Delta F = 0.0001 < 0.01$, the convergence patience counter reached 2 and the run stopped naturally after Generation 2 (3 total generations evaluated: Gen 0, 1, 2) without reaching the generation cap of 5.

**Verbatim Log Confirmation:**
```text
14:49:52 | INFO    | src.ea.nsga2 |   Gen 2 | NSGA-II elite: Poem(id=da3255a0-d29, F=0.877, Q̄=0.900, R=1.000, S=0.706) (rank=0) | Best-F: 0.877
14:49:52 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0001'])
14:49:52 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_limerick_Sorrow_de5ca899 ═══ Generations: 3 | Final F=0.877
```

---

## 5. Total Token Usage

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–4 + 2 Mutation rounds) | 6 | 1,860 | 4,557 | **6,417** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 10 mutation variants) | 16 | 6,267 | 641 | **6,908** |
| **Total** | | **22** | **8,127** | **5,198** | **13,325** |

*Note: Account rate limiting enforced two pauses on Qwen3.8-27B during evaluation (49.4s at 14:47:00, and 51.7s at 14:47:59) to respect the 6,000 TPM limit.*

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Rows 44–46)

```csv
nsga2_limerick_Sorrow_de5ca899,nsga2,limerick,Sorrow,0,0.8765,0.8000,1.0000,0.9060,"On the platform they whispered goodbye, | As the steam rose and clouded the sky, | His eyes met the rail, | A soft, trembling wail, | And the night swallowed hope with a sigh."
nsga2_limerick_Sorrow_de5ca899,nsga2,limerick,Sorrow,1,0.8765,0.8000,1.0000,0.9060,"On the platform they whispered goodbye, | As the steam rose and clouded the sky, | His eyes met the rail, | A soft, trembling wail, | And the night swallowed hope with a sigh."
nsga2_limerick_Sorrow_de5ca899,nsga2,limerick,Sorrow,2,0.8766,0.9000,1.0000,0.7064,"Steam curled like ghosts as the night grew dim, | He whispered his oath on a trembling limb, | The rails sang a moan, | His heart turned to stone, | And the station awoke to a mournful hymn."
```

### `output/logs/per_run_summary.csv` (Row 14)

```csv
nsga2_limerick_Sorrow_de5ca899,nsga2,limerick,Sorrow,0.8766,3,"Steam curled like ghosts as the night grew dim, | He whispered his oath on a trembling limb, | The rails sang a moan, | His heart turned to stone, | And the station awoke to a mournful hymn."
```

### `output/logs/human_feedback.csv` (Row 12)

```csv
2026-11-06T09:29:12.066625+00:00,da3255a0-d29,limerick,nsga2,Sorrow,"A soldier saying goodbye at the train station, not knowing if he'll return.",1,good,"Steam curled like ghosts as the night grew dim, | He whispered his oath on a trembling limb, | The rails sang a moan, | His heart turned to stone, | And the station awoke to a mournful hymn.",0.8766,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in terminal by user (`python run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `2` (Sorrow)
   - Description: *"A soldier saying goodbye at the train station, not knowing if he'll return."*
3. **Execution:** Full evolutionary process ran over 3 generations (Gen 0, 1, 2) in **3m 03s** wall-clock time (14:46:49 to 14:49:52 IST).
4. **Presentation & Selection:** Winning poem `da3255a0-d29` ($F=0.8766$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: Limerick` due to a ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `nsga2` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `good` live at 14:59:12 IST (`2026-11-06T09:29:12.066625+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `da3255a0-d29`.
8. **Line "Final presentation: selected highest-F poem from Front 0":** `not recorded` (logic in `src/ea/nsga2.py` executed this selection, but no `logger.info()` statement was coded for that string).

---

## 8. Parser Audit

### Parser Discard Event (Batch 3, Generation 0)
At 14:46:57 IST during initial population generation, API call 3 returned an incomplete 4-line snippet:
```text
At the platform the night winds did rain
He bowed to his love, his heart in rain
Will he return, or stay?
The train rolls on,
```
**Verbatim Log Line (Line 2592):**
```text
14:46:57 | INFO    | src.prompts.generator | Parser discarded 4 incomplete line(s) that did not meet exact target of 5 lines for limerick
```
The generator automatically triggered Batch 4 (Call 4), which returned Candidate 6 with exactly 5 lines, completing the population of 6.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `14:46:54 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='On the platform they whispered goodbye,'`
  - `14:46:54 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='By the tracks he knelt, his hand on the '`
  - `14:46:54 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The soldier bowed low to the train’s iro'`
  - `14:46:54 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='At the station the crowds turned away,'`
  - `14:46:54 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The locomotive roared, cold and austere,'`
  - `14:46:57 | INFO | src.prompts.generator | Parser discarded 4 incomplete line(s) that did not meet exact target of 5 lines for limerick`
  - `14:46:59 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='At the cold platform we stood, hearts gr'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded:** 1 incomplete 4-line snippet from Batch 3.

- **Generation 1 (Mutation Variants):**
  - `14:47:58 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='On the cold rails his promise fell mute,'`
  - `14:47:58 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The platform held echoes of sorrow,'`
  - `14:47:58 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Beneath iron arches the wind sighed,'`
  - `14:47:58 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='The station’s lamp flickered, forlorn,'`
  - `14:47:58 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Steam rose like ghosts from the line,'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `14:48:56 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='On the cold rails his farewell did sigh,'`
  - `14:48:56 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The night train exhaled a grey, heavy si'`
  - `14:48:56 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='Steam curled like ghosts as the night gr'`
  - `14:48:56 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Beneath lanterns the farewells were hush'`
  - `14:48:56 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The platform stood still as the clouds b'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Line 351)
- `initial_population_batch_2` (Lines 354–376)
- `initial_population_batch_3` (Lines 378–384)
- `initial_population_batch_4` (Lines 386–393)
- `mutation` Gen 1 (Lines 395–424)
- `mutation` Gen 2 (Lines 426–457)

---

## Addendum: Comprehensive Rate-Limit Pause Audit & Net Execution Time

To match the accounting methodology of the GA report (auditing all account limiter events rather than only major multi-second throttles), the complete execution log of run `nsga2_limerick_Sorrow_de5ca899` in `output/logs/interactive.log` was audited for all limiter events.

### Complete Rate-Limit Pauses (Run `nsga2_limerick_Sorrow_de5ca899`)

Account rate limiting enforced 7 pauses totaling **160.70 seconds** (~2m 40.7s):
- **Waiting on `qwen/qwen3.8-27b`:** 6 pauses totaling **158.30s** (enforcing 6,000 TPM limit).
- **Waiting on `openai/gpt-oss-120b`:** 1 pause totaling **2.40s** (enforcing 6,000 TPM limit).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 14:47:00 | 49.4s | `qwen/qwen3.8-27b` | RPM=4/25 TPM=5696/6000 |
| 2 | 14:47:55 | 2.4s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4825/6000 |
| 3 | 14:47:59 | 51.7s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5461/6000 |
| 4 | 14:48:51 | 3.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5463/6000 |
| 5 | 14:48:56 | 1.6s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5819/6000 |
| 6 | 14:48:58 | 0.6s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5462/6000 |
| 7 | 14:48:59 | 51.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5464/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (14:46:49 → 14:49:52 IST):** 183.0s (3m 03s)
- **Total Rate-Limit Pause Time:** 160.70s (2m 40.7s)
- **Time to Final Poem excluding pauses:** **22.30s**
