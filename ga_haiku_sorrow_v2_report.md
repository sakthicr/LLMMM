# GA + Haiku + Sorrow (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_haiku_Sorrow_d790fd4d` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-10 |
| **Start Time** | 10:27:15 IST (04:57:15 UTC) |
| **Completion Time** | 10:29:21 IST (04:59:21 UTC) |
| **Verdict Logged Time** | 10:29:57 IST (2026-11-10T04:59:57.777995+00:00 UTC) |
| **Time to Final Poem** | 2m 06s (126.0s gross wall-clock, 10:27:15 → 10:29:21 IST) |
| **Total Rate-Limit Pause Time** | 1m 50.2s (110.20s across 7 rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **15.80s** (126.0s gross wall-clock − 110.20s rate-limit waits) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable structure) |
| **Target Emotion** | Sorrow |
| **Scenario** | an old photograph curling at the edges in a drawer nobody opens anymore |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Generations Executed** | 3 (Gen 0, 1, 2) |
| **Termination Reason** | Convergence rule ($\Delta F < 0.01$ for 2 consecutive generations: `['0.0000', '0.0000']`) |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking) |
| **Elitism Status** | Yes (`d51ae41b-c18` Gen 0 elite preserved through Gen 1 and Gen 2 via elitism) |
| **Historical Comparison Tag** | **Redo of pre-fix run `ga_haiku_Sorrow_ffac0b64`** (and counterpart `nsga2_haiku_Sorrow_96240585`) under post-fix code with full candidate IDs, pause tracking, and parser verification. Pre-fix run data remains completely untouched. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Winter in a box
Photograph weeps at each seam
Drawer stays closed still
```

| Metric | Value |
|---|---|
| **Poem ID** | `d51ae41b-c18` |
| **Composite Fitness ($F$)** | **0.8353** (displayed as 0.835) |
| **Quality ($\bar{Q}$)** | **0.9500** (displayed as 0.950) |
| **Rhyme ($R$)** | **0.5000** (displayed as 0.500; unrhymed haiku baseline) |
| **Structure ($S$)** | **0.9412** (displayed as 0.941) |
| **Syllables per line** | Line 1: 5 (*Win-ter in a box*)<br>Line 2: 7 (*Pho-to-graph weeps at each seam*)<br>Line 3: 4 (*Draw-er stays closed still*) |
| **Line Count** | 3 (target: 3) |
| **Generation Created** | Generation 0 (Batch 1, Candidate #5) |
| **Elite Status** | **Yes** — Elite of Gen 0 ($F = 0.8353$), preserved as Elite in Gen 1 and Gen 2 via elitism |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Initial Population (All 6 Candidates)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 10:27:18 IST):** Generated Candidates 1–5 (3 lines each).
- **Batch 2 (Call 2, 10:27:19 IST):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 had exactly 3 lines.

### Candidate 1 (Batch 1, Candidate #1) — ID: `6b45b17e-092`

```text
Faded smiles whisper
Edges curl like wilted leaves
Drawer stays silent
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.850 | 0.500 | 0.941 | 0.7853 | [5, 7, 4] | Discarded |

### Candidate 2 (Batch 1, Candidate #2) — ID: `9df658dd-253`

```text
Dust cloaks the cracked frame
Time folds the corners inward
Heartbeats fade away
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.500 | 1.000 | 0.7500 | [5, 7, 5] | Discarded |

### Candidate 3 (Batch 1, Candidate #3) — ID: `78395cf8-67e`

```text
Quiet wood creaks low
Forgotten smiles curl and blur
Drawer sighs unseen
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.850 | 0.500 | 0.941 | 0.7853 | [5, 7, 4] | Discarded |

### Candidate 4 (Batch 1, Candidate #4) — ID: `282636a0-d6d`

```text
Yellowed light leaks thin
Edges curl like mournful sighs
Memory folds down
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 1.000 | 0.7750 | [5, 7, 5] | Discarded |

### Candidate 5 (Batch 1, Candidate #5) — Gen 0 GA Elite (ID: `d51ae41b-c18`)

```text
Winter in a box
Photograph weeps at each seam
Drawer stays closed still
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| **0.950** | **0.500** | **0.941** | **0.8353** | [5, 7, 4] | **Gen 0 Elite (Selected Parent for Gen 1)** |

### Candidate 6 (Batch 2, Candidate #1) — ID: `b679b506-9ef`

```text
Faded smiles decay
Edges curl like wilted leaves
Drawer stays shut, mute
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.900 | 0.500 | 0.941 | 0.8103 | [5, 7, 4] | Discarded |

### Gen 0 Summary Table

| # | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Discarded Lines | GA Status |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `6b45b17e-092` | *"Faded smiles whisper"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | 0 | Discarded |
| 2 | `9df658dd-253` | *"Dust cloaks the cracked frame"* | 0.750 | 0.500 | 1.000 | 0.7500 | 3 | [5, 7, 5] | 0 | Discarded |
| 3 | `78395cf8-67e` | *"Quiet wood creaks low"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | 0 | Discarded |
| 4 | `282636a0-d6d` | *"Yellowed light leaks thin"* | 0.800 | 0.500 | 1.000 | 0.7750 | 3 | [5, 7, 5] | 0 | Discarded |
| 5 | `d51ae41b-c18` | *"Winter in a box"* | **0.950** | **0.500** | **0.941** | **0.8353** | 3 | [5, 7, 4] | 0 | **Gen 0 Elite (Selected Parent)** |
| 6 | `b679b506-9ef` | *"Faded smiles decay"* | 0.900 | 0.500 | 0.941 | 0.8103 | 3 | [5, 7, 4] | 0 | Discarded |

* **Gen 0 Elite Selected:** Candidate 5 (`d51ae41b-c18`, $F = 0.8353$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Evolution

### Generation 1

Elite parent `d51ae41b-c18` ($\bar{Q}=0.950, R=0.500, S=0.941, F=0.8353$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | GA Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `374854e0-f44` | *"Faded smile frays,"* | 0.950 | 0.500 | 0.882 | 0.8206 | 3 | [4, 7, 4] | Discarded |
| Variant 2 | `d4a69d29-435` | *"Dusty frame trembles,"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | Discarded |
| Variant 3 | `e88cc28f-a05` | *"Old grin folds inward,"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | Discarded |
| Variant 4 | `36636918-caa` | *"Bent photo weeps soft,"* | 0.750 | 0.500 | 0.941 | 0.7353 | 3 | [5, 7, 4] | Discarded |
| Variant 5 | `e85a3f4b-9eb` | *"Crumpled memory,"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 4] | Discarded |
| Parent | `d51ae41b-c18` | *"Winter in a box"* | **0.950** | **0.500** | **0.941** | **0.8353** | 3 | [5, 7, 4] | **Retained as Elite** |

* **Elite Selection:** Parent `d51ae41b-c18` ($F = 0.8353$) was strictly superior to all 5 mutation variants (highest variant was `374854e0-f44` at $F = 0.8206$). Retained as elite parent for Generation 2 via elitism.
* **Best-F Tracker & $\Delta F$:** In Gen 0, best-F was $0.8353$. In Gen 1, best-F remained $0.8353$. Thus $\Delta F = 0.0000 < 0.01$. Patience counter incremented to **1**.

---

### Generation 2 (Final Generation)

Elite parent `d51ae41b-c18` ($\bar{Q}=0.950, R=0.500, S=0.941, F=0.8353$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | GA Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `d047eb0f-724` | *"Faded frame sighs low"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Discarded |
| Variant 2 | `c6d44171-c99` | *"Dusty picture weeps"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 8, 5] | Discarded |
| Variant 3 | `32ef9700-5c5` | *"Old photo, torn edge"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Discarded |
| Variant 4 | `0886b7a2-a19` | *"Crumpled smile fades out"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Discarded |
| Variant 5 | `ea07d93b-d46` | *"Worn image trembling"* | 0.850 | 0.500 | 0.882 | 0.7706 | 3 | [6, 7, 4] | Discarded |
| Parent | `d51ae41b-c18` | *"Winter in a box"* | **0.950** | **0.500** | **0.941** | **0.8353** | 3 | [5, 7, 4] | **Retained as Elite & Winning Poem** |

* **Elite Selection & Presentation:** Parent `d51ae41b-c18` ($F = 0.8353$) was again strictly superior to all 5 mutation variants (highest variants were $F = 0.8000$). Retained as elite and selected as final presentation poem.
* **Best-F Tracker & Stopping:** Best $F$ remained $0.8353$. Thus $\Delta F = 0.0000 < 0.01$ for the second consecutive generation (`deltas: ['0.0000', '0.0000']`). Patience counter reached **2**, cleanly triggering the convergence stopping rule.

---

## 4. Stopping Rule Audit

| Generation | Best $F$ Tracked | Best $\bar{Q}$ in Pool | Best $R$ in Pool | Best $S$ in Pool | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8353 | 0.9500 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.8353 | 0.9500 | 0.5000 | 0.9412 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 2 | 0.8353 | 0.9500 | 0.5000 | 1.0000 | 0.0000 | 2 | **STOP — Convergence rule triggered ($\Delta F < 0.01$ for 2 gens)** |

**Verbatim Log Confirmation:**
```text
10:29:21 | INFO    | src.ea.ga |   Gen 2 | Best F=0.835 | Poem(id=d51ae41b-c18, F=0.835, Q̄=0.950, R=0.500, S=0.941)
10:29:21 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
10:29:21 | INFO    | src.ea.ga |   Final presentation: selected elite -> d51ae41b-c18 (F=0.835)
10:29:21 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_haiku_Sorrow_d790fd4d ═══ Generations: 3 | Final F=0.835
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 2 Mutation calls across 2 gens) | 4 | 1,154 | 1,354 | **2,508** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 10 mutation variants across 2 gens) | 16 | 5,797 | 729 | **6,526** |
| **Total** | | **20** | **6,951** | **2,083** | **9,034** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 7 pauses totaling **110.20 seconds** (~1m 50.2s):
- **Waiting on `qwen/qwen3.8-27b`:** 5 pauses totaling **56.70s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 2 pauses totaling **53.50s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 10:27:25 | 51.0s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5506/6000 |
| 2 | 10:28:16 | 1.8s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4648/6000 |
| 3 | 10:28:20 | 0.5s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5784/6000 |
| 4 | 10:28:21 | 3.1s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5785/6000 |
| 5 | 10:28:25 | 51.7s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4699/6000 |
| 6 | 10:29:17 | 1.5s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5612/6000 |
| 7 | 10:29:20 | 0.6s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5784/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 10:27:15 → Completion 10:29:21):** 126.0s (2m 06s)
- **Total Rate-Limit Pause Time:** 110.20s (1m 50.2s)
- **Time to Final Poem excluding pauses:** **15.80s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 95–97)

```csv
ga_haiku_Sorrow_d790fd4d,ga,haiku,Sorrow,0,0.8353,0.9500,0.5000,0.9412,Winter in a box | Photograph weeps at each seam | Drawer stays closed still
ga_haiku_Sorrow_d790fd4d,ga,haiku,Sorrow,1,0.8353,0.9500,0.5000,0.9412,Winter in a box | Photograph weeps at each seam | Drawer stays closed still
ga_haiku_Sorrow_d790fd4d,ga,haiku,Sorrow,2,0.8353,0.9500,0.5000,0.9412,Winter in a box | Photograph weeps at each seam | Drawer stays closed still
```

### `output/logs/per_run_summary.csv` (Line 26)

```csv
ga_haiku_Sorrow_d790fd4d,ga,haiku,Sorrow,0.8353,3,Winter in a box | Photograph weeps at each seam | Drawer stays closed still
```

### `output/logs/human_feedback.csv` (Line 23 / Index 21)

```csv
2026-11-10T04:59:57.777995+00:00,d51ae41b-c18,haiku,ga,Sorrow,an old photograph curling at the edges in a drawer nobody opens anymore,1,good,Winter in a box | Photograph weeps at each seam | Drawer stays closed still,0.8353,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `1` (Genetic Algorithm - GA)
   - Emotion: `2` (Sorrow)
   - Description: *"an old photograph curling at the edges in a drawer nobody opens anymore"*
3. **Execution:** Full evolutionary process ran over 3 generations (Gen 0 through Gen 2) in **2m 06s** gross wall-clock time (10:27:15 to 10:29:21 IST), with net generation active time of **15.80s** excluding pauses.
4. **Presentation & Selection:** Winning poem `d51ae41b-c18` ($F=0.8353, \bar{Q}=0.9500, R=0.5000, S=0.9412$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live at 10:29:57 IST (`2026-11-10T04:59:57.777995+00:00` UTC).
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `d51ae41b-c18` and verdict `good`.
7. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; user input `no` submitted; tool exited cleanly with `Session complete. Goodbye!`.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Parser warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).
- **Mutation retry warning event:** **0** (no mutation failures; all mutation calls returned 5 valid variants on first attempt).

### Parser Discard Events
- **Discarded incomplete lines:** **0**. All parsed batches produced complete 3-line haikus.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `10:27:18 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smiles whisper'`
  - `10:27:18 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dust cloaks the cracked frame'`
  - `10:27:18 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Quiet wood creaks low'`
  - `10:27:18 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Yellowed light leaks thin'`
  - `10:27:18 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Winter in a box'`
  - `10:27:19 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smiles decay'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `10:28:19 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded smile frays,'`
  - `10:28:19 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dusty frame trembles,'`
  - `10:28:19 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Old grin folds inward,'`
  - `10:28:19 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Bent photo weeps soft,'`
  - `10:28:19 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Crumpled memory,'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `10:29:17 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Faded frame sighs low'`
  - `10:29:17 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Dusty picture weeps'`
  - `10:29:17 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Old photo, torn edge'`
  - `10:29:17 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Crumpled smile fades out'`
  - `10:29:17 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Worn image trembling'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 2037–2057; 5 candidates)
- `initial_population_batch_2` (Lines 2058–2062; 1 candidate)
- `mutation` Gen 1 (Lines 2063–2091; 5 variants)
- `mutation` Gen 2 (Lines 2092–2120; 5 variants)

