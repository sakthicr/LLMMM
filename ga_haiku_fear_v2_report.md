# GA + Haiku + Fear (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_haiku_Fear_aba15568` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-09 |
| **Start Time** | 22:11:43 IST (16:21:43 UTC) |
| **Completion Time** | 22:14:49 IST (16:24:49 UTC) |
| **Verdict Logged Time** | 22:15:51 IST (2026-11-09T16:45:50.989481+00:00 UTC) |
| **Time to Final Poem** | 3m 06s (186.0s gross wall-clock, 22:11:43 → 22:14:49 IST) |
| **Total Rate-Limit Pause Time** | 2m 45.5s (165.50s across 6 rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **20.50s** (186.0s gross wall-clock − 165.50s rate-limit waits) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
| **Poem Type** | Haiku (3 lines, 5-7-5 syllable structure) |
| **Target Emotion** | Fear |
| **Scenario** | Walking alone down an unlit street, hearing footsteps that match your pace exactly. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Generations Executed** | 4 (Gen 0, 1, 2, 3) |
| **Termination Reason** | Convergence rule ($\Delta F < 0.01$ for 2 consecutive generations: `['0.0000', '0.0000']`) |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 3-line chunking) |
| **Elitism Status** | Yes (`cbbead3b-583` Gen 1 elite preserved through Gen 2 and Gen 3 via elitism) |
| **Historical Comparison Tag** | **Redo of pre-fix run `ga_haiku_Fear_144a75a8`** under post-fix code with full candidate IDs, pause tracking, and parser verification. Pre-fix run data remains completely untouched. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
Empty lane, breath held
Shadow steps echo my stride
Darkness leans closer
```

| Metric | Value |
|---|---|
| **Poem ID** | `cbbead3b-583` |
| **Composite Fitness ($F$)** | **0.8000** (displayed as 0.800) |
| **Quality ($\bar{Q}$)** | **0.8500** (displayed as 0.850) |
| **Rhyme ($R$)** | **0.5000** (displayed as 0.500; unrhymed haiku baseline) |
| **Structure ($S$)** | **1.0000** (displayed as 1.000; exact 5-7-5 syllables) |
| **Syllables per line** | Line 1: 5 (*Emp-ty lane, breath held*)<br>Line 2: 7 (*Sha-dow steps ech-o my stride*)<br>Line 3: 5 (*Dark-ness leans clo-ser*) |
| **Line Count** | 3 (target: 3) |
| **Generation Created** | Generation 1 (Variant 1) |
| **Elite Status** | **Yes** — Elite of Gen 1 ($F = 0.8000$), preserved as Elite in Gen 2 and Gen 3 via elitism |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Initial Population (All 6 Candidates)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 22:11:44 IST):** Generated Candidates 1–5 (3 lines each).
- **Batch 2 (Call 2, 22:11:45 IST):** Generated Candidate 6 (3 lines).

All 6 evaluated candidates in Generation 0 had exactly 3 lines.

### Candidate 1 (Batch 1, Candidate #1) — ID: `32f4ad09-e2f`

```text
Dark lane, breath held tight
Echo steps fall in my stride
Shadows close, unseen
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 1.000 | 0.775 | [5, 7, 5] | Discarded |

### Candidate 2 (Batch 1, Candidate #2) — Gen 0 GA Elite (ID: `73784a2b-cc2`)

```text
Midnight street, heart thuds
Twin footfalls mimic my tread
Night’s whisper grows cold
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| **0.850** | **0.500** | **0.941** | **0.785** | [5, 7, 6] | **Gen 0 Elite (Selected Parent for Gen 1)** |

### Candidate 3 (Batch 1, Candidate #3) — ID: `e44134ef-a19`

```text
Alone, the lamp’s gone out
Footsteps mirror each slow pace
Fear walks side by side
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 0.882 | 0.746 | [7, 7, 5] | Discarded |

### Candidate 4 (Batch 1, Candidate #4) — ID: `20828f0e-68c`

```text
Silent road, moonless black
Every step a twin reply
Dread drapes every sound
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.850 | 0.500 | 0.824 | 0.756 | [6, 8, 6] | Discarded |

### Candidate 5 (Batch 1, Candidate #5) — ID: `5d5b808a-fdc`

```text
Empty path, eyes unseen
Footsteps echo, match my beat
Panic’s pulse repeats
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 0.882 | 0.746 | [6, 7, 6] | Discarded |

### Candidate 6 (Batch 2, Candidate #1) — ID: `65bbb7a1-7d7`

```text
Midnight shadows creep
Footsteps echo my own stride
Heart races in dark
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Syllables | Status |
|:---:|:---:|:---:|:---:|:---:|---|
| 0.600 | 0.500 | 1.000 | 0.675 | [5, 7, 5] | Discarded |

### Gen 0 Summary Table

| # | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | Discarded Lines | GA Status |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `32f4ad09-e2f` | *"Dark lane, breath held tight"* | 0.800 | 0.500 | 1.000 | 0.7750 | 3 | [5, 7, 5] | 0 | Discarded |
| 2 | `73784a2b-cc2` | *"Midnight street, heart thuds"* | **0.850** | **0.500** | **0.941** | **0.7853** | 3 | [5, 7, 6] | 0 | **Gen 0 Elite (Selected Parent)** |
| 3 | `e44134ef-a19` | *"Alone, the lamp’s gone out"* | 0.800 | 0.500 | 0.882 | 0.7456 | 3 | [7, 7, 5] | 0 | Discarded |
| 4 | `20828f0e-68c` | *"Silent road, moonless black"* | 0.850 | 0.500 | 0.824 | 0.7559 | 3 | [6, 8, 6] | 0 | Discarded |
| 5 | `5d5b808a-fdc` | *"Empty path, eyes unseen"* | 0.800 | 0.500 | 0.882 | 0.7456 | 3 | [6, 7, 6] | 0 | Discarded |
| 6 | `65bbb7a1-7d7` | *"Midnight shadows creep"* | 0.600 | 0.500 | 1.000 | 0.6750 | 3 | [5, 7, 5] | 0 | Discarded |

* **Gen 0 Elite Selected:** Candidate 2 (`73784a2b-cc2`, $F = 0.7853$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation Evolution

### Generation 1

Elite parent `73784a2b-cc2` ($\bar{Q}=0.850, R=0.500, S=0.941, F=0.7853$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | GA Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `cbbead3b-583` | *"Empty lane, breath held"* | **0.850** | **0.500** | **1.000** | **0.8000** | 3 | [5, 7, 5] | **New Elite (Highest $F$)** |
| Variant 2 | `e63883fd-450` | *"Lonely road, night sighs"* | 0.650 | 0.500 | 1.000 | 0.7000 | 3 | [5, 7, 5] | Discarded |
| Variant 3 | `78507966-a3e` | *"Silent black, pulse quick"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Co-highest $F$ |
| Variant 4 | `3758eb55-2cd` | *"Gloomed alley, heart drums"* | 0.800 | 0.500 | 1.000 | 0.7750 | 3 | [5, 7, 5] | Discarded |
| Variant 5 | `a2637b79-bc2` | *"Midnight veil, breath stalls"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 8, 5] | Discarded |
| Parent | `73784a2b-cc2` | *"Midnight street, heart thuds"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [5, 7, 6] | Replaced by Variant 1 |

* **Elite Selection:** Variant 1 (`cbbead3b-583`, $F = 0.8000$) achieved higher fitness than the parent ($0.8000 > 0.7853$) due to perfect 5-7-5 structure ($S = 1.0000$ vs $0.9412$) while maintaining maximum Quality ($\bar{Q} = 0.8500$). Selected as elite parent for Generation 2.
* **Best-F Tracker & $\Delta F$:** In Gen 0, best-F was $0.7853$. In Gen 1, best-F improved to $0.8000$. Thus $\Delta F = +0.0147 \ge 0.01$. Patience counter reset to 0.

---

### Generation 2

Elite parent `cbbead3b-583` ($\bar{Q}=0.850, R=0.500, S=1.000, F=0.8000$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | GA Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `0c10592c-764` | *"Midnight road, heart thuds"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Tied on highest $F$ |
| Variant 2 | `085d289f-0ce` | *"Lonely lane, shadows grin"* | 0.850 | 0.500 | 0.941 | 0.7853 | 3 | [6, 7, 5] | Discarded |
| Variant 3 | `04ae07f6-17f` | *"Dark alley, pulse drums"* | 0.700 | 0.500 | 1.000 | 0.7250 | 3 | [5, 7, 5] | Discarded |
| Variant 4 | `ef89b1e0-0bf` | *"Silent street, dread climbs"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 8, 5] | Discarded |
| Variant 5 | `84644615-230` | *"Cold dusk, breath freezes"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Tied on highest $F$ |
| Parent | `cbbead3b-583` | *"Empty lane, breath held"* | **0.850** | **0.500** | **1.000** | **0.8000** | 3 | [5, 7, 5] | **Retained as Elite** |

* **Elite Selection:** Parent `cbbead3b-583` retained as elite ($F = 0.8000$).
* **Best-F Tracker & $\Delta F$:** Best $F$ remained $0.8000$. Thus $\Delta F = 0.0000 < 0.01$. Patience counter incremented to **1**.

---

### Generation 3 (Final Generation)

Elite parent `cbbead3b-583` ($\bar{Q}=0.850, R=0.500, S=1.000, F=0.8000$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (Elite Parent + 5 Variants):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Syllables | GA Selection Status |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `8cfa525a-c77` | *"Dark road, heart pounds"* | 0.750 | 0.500 | 0.941 | 0.7353 | 3 | [4, 7, 5] | Discarded |
| Variant 2 | `33fd3530-b3e` | *"Silent street, dread climbs"* | 0.800 | 0.500 | 0.941 | 0.7603 | 3 | [5, 8, 5] | Discarded |
| Variant 3 | `19624185-620` | *"Dark lane, pulse thuds fast"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Tied on highest $F$ |
| Variant 4 | `67962e5e-1bd` | *"Curb void, breath freezes"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Tied on highest $F$ |
| Variant 5 | `93a7be2b-6ed` | *"Alone, pulse rattles"* | 0.850 | 0.500 | 1.000 | 0.8000 | 3 | [5, 7, 5] | Tied on highest $F$ |
| Parent | `cbbead3b-583` | *"Empty lane, breath held"* | **0.850** | **0.500** | **1.000** | **0.8000** | 3 | [5, 7, 5] | **Retained as Elite & Winning Poem** |

* **Elite Selection & Presentation:** Parent `cbbead3b-583` retained as elite ($F = 0.8000$).
* **Best-F Tracker & Stopping:** Best $F$ remained $0.8000$. Thus $\Delta F = 0.0000 < 0.01$ for the second consecutive generation (`deltas: ['0.0000', '0.0000']`). Patience counter reached **2**, cleanly triggering the convergence stopping rule.

---

## 4. Stopping Rule Audit

| Generation | Best $F$ Tracked | Best $\bar{Q}$ in Pool | Best $R$ in Pool | Best $S$ in Pool | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.7853 | 0.8500 | 0.5000 | 1.0000 | — | 0 | Continue |
| 1 | 0.8000 | 0.8500 | 0.5000 | 1.0000 | +0.0147 | 0 | Continue ($\Delta F \ge 0.01$; counter reset to 0) |
| 2 | 0.8000 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 1 | Continue (patience reaches 1; requires 2 consecutive) |
| 3 | 0.8000 | 0.8500 | 0.5000 | 1.0000 | 0.0000 | 2 | **STOP — Convergence rule triggered ($\Delta F < 0.01$ for 2 gens)** |

**Verbatim Log Confirmation:**
```text
22:14:49 | INFO    | src.ea.ga |   Gen 3 | Best F=0.800 | Poem(id=cbbead3b-583, F=0.800, Q̄=0.850, R=0.500, S=1.000)
22:14:49 | INFO    | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
22:14:49 | INFO    | src.ea.ga |   Final presentation: selected elite -> cbbead3b-583 (F=0.800)
22:14:49 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_haiku_Fear_aba15568 ═══ Generations: 4 | Final F=0.800
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 3 Mutation calls across 3 gens) | 5 | 1,471 | 3,429 | **4,900** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 15 mutation variants across 3 gens) | 21 | 7,562 | 957 | **8,519** |
| **Total** | | **26** | **9,033** | **4,386** | **13,419** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 6 pauses totaling **165.50 seconds** (~2m 45.5s):
- **Waiting on `qwen/qwen3.8-27b`:** 4 pauses totaling **109.80s** (enforcing TPM/RPM limits).
- **Waiting on `openai/gpt-oss-120b`:** 2 pauses totaling **55.70s** (enforcing TPM/RPM limits).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 22:11:51 | 53.8s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5515/6000 |
| 2 | 22:12:48 | 2.2s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5790/6000 |
| 3 | 22:12:50 | 54.5s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4709/6000 |
| 4 | 22:13:49 | 1.2s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5255/6000 |
| 5 | 22:13:54 | 51.8s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5630/6000 |
| 6 | 22:14:46 | 2.0s | `qwen/qwen3.8-27b` | RPM=9/25 TPM=5796/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 22:11:43 → Completion 22:14:49):** 186.0s (3m 06s)
- **Total Rate-Limit Pause Time:** 165.50s (2m 45.5s)
- **Time to Final Poem excluding pauses:** **20.50s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Lines 86–89)

```csv
ga_haiku_Fear_aba15568,ga,haiku,Fear,0,0.7853,0.8500,0.5000,0.9412,"Midnight street, heart thuds | Twin footfalls mimic my tread | Night’s whisper grows cold"
ga_haiku_Fear_aba15568,ga,haiku,Fear,1,0.8000,0.8500,0.5000,1.0000,"Empty lane, breath held | Shadow steps echo my stride | Darkness leans closer"
ga_haiku_Fear_aba15568,ga,haiku,Fear,2,0.8000,0.8500,0.5000,1.0000,"Empty lane, breath held | Shadow steps echo my stride | Darkness leans closer"
ga_haiku_Fear_aba15568,ga,haiku,Fear,3,0.8000,0.8500,0.5000,1.0000,"Empty lane, breath held | Shadow steps echo my stride | Darkness leans closer"
```

### `output/logs/per_run_summary.csv` (Line 24)

```csv
ga_haiku_Fear_aba15568,ga,haiku,Fear,0.8000,4,"Empty lane, breath held | Shadow steps echo my stride | Darkness leans closer"
```

### `output/logs/human_feedback.csv` (Line 21 / Index 19)

```csv
2026-11-09T16:45:50.989481+00:00,cbbead3b-583,haiku,ga,Fear,"Walking alone down an unlit street, hearing footsteps that match your pace exactly.",1,good,"Empty lane, breath held | Shadow steps echo my stride | Darkness leans closer",0.8000,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python run_interactive.py`) with sandbox bypass.
2. **Interactive Choices (Live):**
   - Poem Type: `1` (Haiku)
   - Algorithm: `1` (Genetic Algorithm - GA)
   - Emotion: `3` (Fear)
   - Description: *"Walking alone down an unlit street, hearing footsteps that match your pace exactly."*
3. **Execution:** Full evolutionary process ran over 4 generations (Gen 0 through Gen 3) in **3m 06s** gross wall-clock time (22:11:43 to 22:14:49 IST), with net generation active time of **20.50s** excluding pauses.
4. **Presentation & Selection:** Winning poem `cbbead3b-583` ($F=0.8000, \bar{Q}=0.8500, R=0.5000, S=1.0000$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Verdict Entry:** User entered `good` live at 22:15:51 IST (`2026-11-09T16:45:50.989481+00:00` UTC).
6. **Logging:** Feedback logged to `human_feedback.csv` with UUID `cbbead3b-583` and verdict `good`.
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
  - `22:11:44 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Dark lane, breath held tight'`
  - `22:11:44 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Midnight street, heart thuds'`
  - `22:11:44 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Alone, the lamp’s gone out'`
  - `22:11:44 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Silent road, moonless black'`
  - `22:11:44 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Empty path, eyes unseen'`
  - `22:11:45 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight shadows creep'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 3 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `22:12:47 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Empty lane, breath held'`
  - `22:12:47 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Lonely road, night sighs'`
  - `22:12:47 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Silent black, pulse quick'`
  - `22:12:47 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Gloomed alley, heart drums'`
  - `22:12:47 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Midnight veil, breath stalls'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `22:13:48 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Midnight road, heart thuds'`
  - `22:13:48 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Lonely lane, shadows grin'`
  - `22:13:48 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dark alley, pulse drums'`
  - `22:13:48 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Silent street, dread climbs'`
  - `22:13:48 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Cold dusk, breath freezes'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `22:13:54 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=3 (target=3) | first_line='Dark road, heart pounds'`
  - `22:13:54 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=3 (target=3) | first_line='Silent street, dread climbs'`
  - `22:13:54 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=3 (target=3) | first_line='Dark lane, pulse thuds fast'`
  - `22:13:54 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=3 (target=3) | first_line='Curb void, breath freezes'`
  - `22:13:54 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=3 (target=3) | first_line='Alone, pulse rattles'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 3 lines.
  - **Gen 3 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 1826–1846; 5 candidates)
- `initial_population_batch_2` (Lines 1847–1851; 1 candidate)
- `mutation` Gen 1 (Lines 1852–1876; 5 variants)
- `mutation` Gen 2 (Lines 1877–1897; 5 variants)
- `mutation` Gen 3 (Lines 1898–1918; 5 variants)

