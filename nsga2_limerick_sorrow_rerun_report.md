# NSGA-II + Limerick + Sorrow (Rerun) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `nsga2_limerick_Sorrow_3971360e` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-10-20 |
| **Start Time** | 15:23:53 IST |
| **Completion Time** | 15:26:05 IST |
| **Time to Final Poem** | 2m 12s (132s wall-clock, 15:23:53 → 15:26:05) |
| **Algorithm** | NSGA-II (non-dominated sorting on two objectives: Quality and Rhyme) |
| **Poem Type** | Limerick (5 lines, AABBA rhyme scheme) |
| **Target Emotion** | Sorrow |
| **Scenario** | A soldier saying goodbye at the train station, not knowing if he'll return |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 5-line chunking, with candidate line-count logging) |
| **Run Status / Validity** | `superseded - presented poem was not from the final Pareto front` |
| **Historical Comparison Tag** | Earlier runs (`nsga2_limerick_Sorrow_29d9cad1`, `ga_limerick_Sorrow_102c8c40`, `ga_limerick_Sorrow_9d2d8814`, etc.) tagged as `pre-fix parser` |

---

## 1. Winning Poem (Accepted by Human)

```text
At twilight the whistle sighs soft and bleak
A soldier bends, his oath now torn and weak
Steam veils the night
His eyes lose the light
And the tracks hum onward with grief’s quiet streak
```

| Metric | Value |
|---|---|
| **Poem ID** | `ac65cdcc-853` |
| **Composite Fitness ($F$)** | **0.8115** |
| **Quality ($\bar{Q}$)** | **0.8000** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.6462** |
| **Rhyme Scheme** | AABBA — *bleak* / *weak* / *night* / *light* / *streak* |
| **Pareto Rank** | Rank 0 (Non-dominated) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts on two search objectives: Quality ($\bar{Q}$) and Rhyme ($R$). Structure is a feasibility constraint ($S \ge 0.30$), not a search objective. Composite $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ is tracked for stopping and logging only.

Every candidate in Generation 0 was parsed cleanly into exactly 5 lines. Zero candidates were discarded.

### Candidate 1 (Batch 1, Candidate #1)

```text
On the platform the wind sighs soft low
He waves his hand, his eyes full of woe
His coat clings tight to rain
Footsteps fade, the grief turns pain
And the train rolls away, leaving hearts ever low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.833 | 0.678 | 0.728 | 5 | No (0 discarded) | Dominated by #2 on Quality ($\bar{Q}=0.700 < 0.800$) |

### Candidate 2 (Batch 1, Candidate #2) — Gen 0 NSGA-II Elite (ID: `f87edc7c-852`)

```text
At dusk the whistle moans mournful and low
A soldier bows, his promise turned to woe
Steam clouds veil the sky
Tears blur the goodbye
And the rails stretch onward, humming grief’s low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.833 | 0.708 | 0.785 | 5 | No (0 discarded) | **Rank 0 — Non-dominated front member. Selected as elite parent for mutation.** |

### Candidate 3 (Batch 1, Candidate #3)

```text
By the tracks the shadows stretch thin and low
He kisses a mother, his voice hushed with woe
Bags weigh down his heart
Dreams and duties part
And the locomotive sighs, bearing sorrow’s low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.833 | 0.595 | 0.757 | 5 | No (0 discarded) | Rank 0 co-member (same $\bar{Q}$ and $R$ as #2; lower Structure) |

### Candidate 4 (Batch 1, Candidate #4)

```text
Under lanterns the night breathes cold and low
A soldier’s salute drifts with lingering woe
Letters tucked in coat
Hope’s whisper cannot float
And the carriage departs, echoing tears’ low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.833 | 0.535 | 0.742 | 5 | No (0 discarded) | Rank 0 co-member (same $\bar{Q}$ and $R$ as #2; lower Structure) |

### Candidate 5 (Batch 1, Candidate #5)

```text
Midnight rain drums a rhythm bleak and low
He steps aboard, his future shrouded in woe
Boots tap the steel floor
Silence seals the lore
And the engine roars onward, mourning hearts low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.833 | 0.651 | 0.746 | 5 | No (0 discarded) | Dominated by #2, #3, #4 on Quality ($\bar{Q}=0.750 < 0.800$) |

### Candidate 6 (Batch 2, Candidate #1)

```text
From the platform he bowed, tears soft in eyes
His love left behind, a promise in his eyes
Steam hisses low, tracks sigh
He steps onto fate's cold sigh
Will he return? The night swallows his eyes
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | NSGA-II Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.000 | 0.605 | 0.426 | 5 | No (0 discarded) | Dominated ($R=0.000$ and lowest $\bar{Q}$ in population) |

### Gen 0 Summary Table

| # | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | Pareto Rank |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.700 | 0.833 | 0.678 | 0.728 | 5 | 0 | Dominated |
| 2 | 0.800 | 0.833 | 0.708 | 0.785 | 5 | 0 | **Rank 0 (Elite)** |
| 3 | 0.800 | 0.833 | 0.595 | 0.757 | 5 | 0 | **Rank 0** |
| 4 | 0.800 | 0.833 | 0.535 | 0.742 | 5 | 0 | **Rank 0** |
| 5 | 0.750 | 0.833 | 0.651 | 0.746 | 5 | 0 | Dominated |
| 6 | 0.550 | 0.000 | 0.605 | 0.426 | 5 | 0 | Dominated |

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite parent `f87edc7c-852` ($\bar{Q}=0.800, R=0.833$) was mutated to produce 5 variants.

**Candidate Pool (Elite + 5 Variants):**

| Individual | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Pareto Status |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| `ac65cdcc-853` (Variant 1) | *"At twilight the whistle sighs soft and bleak"* | 0.800 | 1.000 | 0.646 | **0.8115** | 5 | Non-dominated ($R=1.000$). **Overall Best-$F$ poem** |
| Variant 2 | *"When dusk drapes the platform in shadows of gray"* | 0.800 | 1.000 | 0.533 | 0.7832 | 5 | Dominated by Variant 4 on Quality ($\bar{Q}$) |
| Variant 3 | *"By evening the whistle wails low, mournful, austere"* | 0.800 | 1.000 | 0.477 | 0.7692 | 5 | Dominated by Variant 4 on Quality ($\bar{Q}$) |
| `dccfd13a-08f` (Variant 4) | *"At nightfall the engine’s cry drifts mournful and thin"* | **0.850** | **1.000** | 0.459 | 0.7898 | 5 | **Rank 0 — New NSGA-II Elite** |
| Variant 5 | *"When the sun dips, the whistle moans hollow and sad"* | 0.800 | 1.000 | 0.458 | 0.7645 | 5 | Dominated by Variant 4 on Quality ($\bar{Q}$) |
| `f87edc7c-852` (Original Elite) | *"At dusk the whistle moans mournful and low"* | 0.800 | 0.833 | 0.708 | 0.7852 | 5 | Dominated by `ac65cdcc-853` on Rhyme ($R$) |

**The NSGA-II Selection Mechanism:**
- **NSGA-II Selected Elite:** `dccfd13a-08f` ($\bar{Q}=0.850, R=1.000, S=0.459, F=0.790$) strictly dominates all other individuals on the two search objectives ($\bar{Q}, R$), so it is selected as the parent for Generation 2.
- **Overall Best-$F$ Poem:** `ac65cdcc-853` ($\bar{Q}=0.800, R=1.000, S=0.646, F=0.8115$) achieves higher composite fitness because its higher Structure score ($S=0.646$ vs $0.459$) outweighs the 0.05 Quality difference in the weighted composite score. This poem is tracked as the candidate to present to the human.

### Generation 2

Elite `dccfd13a-08f` ($\bar{Q}=0.850, R=1.000$) was mutated to produce 5 variants.

**Candidate Pool:**

| Individual | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Pareto Status |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 (*"On platform the whistle sighs like rain"*) | 0.500 | 0.000 | 0.827 | 0.457 | 5 | Dominated |
| Variant 2 (*"By dusk the train’s low moan drifts cold as rain"*) | 0.500 | 0.500 | 0.437 | 0.484 | 5 | Dominated |
| Variant 3 (*"At twilight the engine weeps a mournful rain"*) | 0.500 | 0.500 | 0.436 | 0.484 | 5 | Dominated |
| Variant 4 (*"When shadows stretch, the whistle cries like rain"*) | 0.550 | 0.500 | 0.497 | 0.524 | 5 | Dominated |
| Variant 5 (*"In evening’s chill the locomotive sighs rain"*) | 0.500 | 0.500 | 0.535 | 0.509 | 5 | Dominated |
| `dccfd13a-08f` (Retained Elite) | **0.850** | **1.000** | 0.459 | 0.790 | 5 | **Rank 0 — Retained as Elite** |

- **Pareto Front:** `dccfd13a-08f` retained as sole Rank 0 solution.
- **Best-$F$ Poem:** `ac65cdcc-853` remains overall best at $F=0.8115$.
- **$\Delta F$:** $0.0000$ — Convergence patience counter increments to 1.

### Generation 3

Elite `dccfd13a-08f` ($\bar{Q}=0.850, R=1.000$) was mutated. The generator API call completed with 1200 completion tokens, but no valid formatted poem variants were generated (`Mutated elite dccfd13a-08f → 0 variants`).

- **Pareto Front:** `dccfd13a-08f` retained as sole Rank 0 solution.
- **Best-$F$ Poem:** `ac65cdcc-853` remains overall best at $F=0.8115$.
- **$\Delta F$:** $0.0000$ — Convergence patience counter increments to 2. **Stopping rule triggered.**

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7852 | — | 0 | Continue |
| 1 | 0.8115 | +0.0263 | 0 (reset) | Continue |
| 2 | 0.8115 | 0.0000 | 1 | Continue (requires 2 consecutive flat generations) |
| 3 | 0.8115 | 0.0000 | 2 | **STOP — Convergence rule triggered** |

**Conclusion:** The run stopped after Generation 3 (4 total generations evaluated: Gen 0, 1, 2, 3) because best $F$ improved by less than 0.01 for 2 consecutive generations. It terminated naturally via convergence without reaching the generation cap of 5.

**Verbatim Log Confirmation:**
```text
15:26:05 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
15:26:05 | INFO    | src.ea.nsga2 | ═══ NSGA-II COMPLETE nsga2_limerick_Sorrow_3971360e ═══ Generations: 4 | Final F=0.811
```

---

## 5. Total Token Usage

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population + 3 Mutation rounds) | 5 | 1,642 | 4,294 | **5,936** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 10 mutation variants) | 16 | 6,289 | 743 | **7,032** |
| **Total** | | **21** | **7,931** | **5,037** | **12,968** |

*Note: Daily budget remaining on Groq after this run: ~194,000 / 200,000 TPD for GPT-OSS-120B and ~993,000 / 1,000,000 TPD for Qwen3.8-27B.*

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Rows 35–38)

```csv
nsga2_limerick_Sorrow_3971360e,nsga2,limerick,Sorrow,0,0.7852,0.8000,0.8333,0.7075,"At dusk the whistle moans mournful and low | A soldier bows, his promise turned to woe | Steam clouds veil the sky | Tears blur the goodbye | And the rails stretch onward, humming grief’s low"
nsga2_limerick_Sorrow_3971360e,nsga2,limerick,Sorrow,1,0.8115,0.8000,1.0000,0.6462,"At twilight the whistle sighs soft and bleak | A soldier bends, his oath now torn and weak | Steam veils the night | His eyes lose the light | And the tracks hum onward with grief’s quiet streak"
nsga2_limerick_Sorrow_3971360e,nsga2,limerick,Sorrow,2,0.8115,0.8000,1.0000,0.6462,"At twilight the whistle sighs soft and bleak | A soldier bends, his oath now torn and weak | Steam veils the night | His eyes lose the light | And the tracks hum onward with grief’s quiet streak"
nsga2_limerick_Sorrow_3971360e,nsga2,limerick,Sorrow,3,0.8115,0.8000,1.0000,0.6462,"At twilight the whistle sighs soft and bleak | A soldier bends, his oath now torn and weak | Steam veils the night | His eyes lose the light | And the tracks hum onward with grief’s quiet streak"
```

### `output/logs/per_run_summary.csv` (Row 12)

```csv
nsga2_limerick_Sorrow_3971360e,nsga2,limerick,Sorrow,0.8115,4,"At twilight the whistle sighs soft and bleak | A soldier bends, his oath now torn and weak | Steam veils the night | His eyes lose the light | And the tracks hum onward with grief’s quiet streak"
```

### `output/logs/human_feedback.csv` (Row 11)

```csv
2026-10-20T10:16:07.608360+00:00,ac65cdcc-853,limerick,nsga2,Sorrow,"A soldier saying goodbye at the train station, not knowing if he'll return.",1,good,"At twilight the whistle sighs soft and bleak | A soldier bends, his oath now torn and weak | Steam veils the night | His eyes lose the light | And the tracks hum onward with grief’s quiet streak",0.8115,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in background (`python -u run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `2` (NSGA-II)
   - Emotion: `2` (Sorrow)
   - Description: *"A soldier saying goodbye at the train station, not knowing if he'll return."*
3. **Execution:** Full evolutionary process ran over 4 generations (Gen 0 through Gen 3) in 2m 12s wall-clock time.
4. **Presentation & Verdict:** Winning poem `ac65cdcc-853` ($F=0.8115$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live.
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `ac65cdcc-853`.
7. **Current State:** The interactive session is currently paused at `Generate another poem? [yes/no] (yes):`.

---

## 8. Parser Audit

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `15:23:57 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5)`
  - `15:23:57 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5)`
  - `15:23:57 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5)`
  - `15:23:57 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5)`
  - `15:23:57 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5)`
  - `15:23:58 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5)`
  - **Gen 0 Discarded Lines:** 0
- **Generation 1 (Mutation Variants):**
  - `15:24:59 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5)`
  - `15:24:59 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5)`
  - `15:24:59 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5)`
  - `15:24:59 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5)`
  - `15:24:59 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5)`
  - **Gen 1 Discarded Lines:** 0
- **Generation 2 (Mutation Variants):**
  - `15:25:57 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5)`
  - `15:25:57 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5)`
  - `15:25:57 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5)`
  - `15:25:57 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5)`
  - `15:25:57 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5)`
  - **Gen 2 Discarded Lines:** 0
- **Generation 3 (Mutation Variants):**
  - Generator produced 0 valid variants.
  - **Gen 3 Discarded Lines:** 0

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1–31)
- `initial_population_batch_2` (Lines 32–38)
- `mutation` Gen 1 (Lines 39–77)
- `mutation` Gen 2 (Lines 78–116)
- `mutation` Gen 3 (Lines 117–120)
