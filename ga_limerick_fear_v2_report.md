# GA + Limerick + Fear (v2 Run) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_limerick_Fear_5e93427d` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-07 |
| **Start Time** | 18:48:18 IST (13:18:18 UTC) |
| **Completion Time** | 18:52:24 IST (13:22:24 UTC) |
| **Verdict Logged Time** | 18:54:43 IST (2026-11-07T13:24:43.666889+00:00 UTC) |
| **Time to Final Poem** | 4m 06s (246s wall-clock, 18:48:18 → 18:52:24 IST) |
| **Total Rate-Limit Pause Time** | 3m 43.8s (223.80s waiting across 14 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **22.20s** (246.0s gross wall-clock − 223.80s rate-limit waits) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
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
| **Run Status / Validity** | `valid - presented poem confirmed as Gen 3/4 elite with highest F` |
| **Elitism Status** | **Yes** — The presented poem (`10b32759-9f5`) was generated in Gen 3 (Variant 3), confirmed as elite of Gen 3 ($F=0.8798$), preserved as elite in Gen 4 via elitism, and presented as the winning poem. |
| **Historical Comparison Tag** | First valid GA Limerick Fear run under post-fix parser with full ID and pause logging. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
When thunder cracked the night and shook the floor,
He hid beneath the springs, his pulse a roar,
A shiver, a hiss—
A stare from abyss—
A phantom smiled, its teeth like jagged shore.
```

| Metric | Value |
|---|---|
| **Poem ID** | `10b32759-9f5` |
| **Composite Fitness ($F$)** | **0.8798** (displayed as 0.880) |
| **Quality ($\bar{Q}$)** | **0.8500** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.8191** |
| **Rhyme Scheme** | AABBA — *floor* / *roar* / *hiss* / *abyss* / *shore* |
| **Line Count** | 5 (target: 5) |
| **Generation Created** | Generation 3 (Variant 3) |
| **Elite Status** | **Yes** — Elite of Gen 3 ($F = 0.8798$), preserved as Elite in Gen 4 |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling required 2 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 18:48:22 IST):** Generated Candidates 1–4 (5 lines each) plus 1 incomplete line (`When clouds`) cleanly discarded by the parser.
- **Batch 2 (Call 2, 18:48:24 IST):** Generated Candidates 5 and 6 (both 5 lines each).

All 6 evaluated candidates in Generation 0 had exactly 5 lines.

### Candidate 1 (Batch 1, Candidate #1) — ID: `8aa54ffc-4b3`

```text
When thunder crashed and the night gave fear
A nervous man dove under bed fear
He felt a cold breath near
And heard a soft, low sigh
He found eyes gleaming, terror grew fear
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.500 | 0.000 | 0.882 | 0.471 | 5 | No (0 discarded) | Evaluated; $F=0.471$ |

### Candidate 2 (Batch 1, Candidate #2) — ID: `161e956a-b99`

```text
When lightning split the sky with a scream
A trembling soul slipped beneath his dream
A whisper crept tight
A shadow took flight
And claws brushed his cheek with silent scream
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.833 | 0.874 | 0.777 | 5 | No (0 discarded) | Evaluated; $F=0.777$ |

### Candidate 3 (Batch 1, Candidate #3) — ID: `cd5d9d07-214`

```text
When rain hammered like drums on the roof
A shaky heart hid where dust lay aloof
A shiver took hold
A hiss turned to cold
And eyes blinked awake in the dark, uncouth
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.750 | 0.667 | 0.819 | 0.747 | 5 | No (0 discarded) | Evaluated; $F=0.747$ |

### Candidate 4 (Batch 1, Candidate #4) — ID: `602c71d8-f38`

```text
When winds howled and the shutters did quake
A fearful man curled where the floorboards break
A rustle did rise
A gasp filled his eyes
And a growl answered from beneath the quake
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.650 | 0.833 | 0.819 | 0.738 | 5 | No (0 discarded) | Evaluated; $F=0.738$ |

### Candidate 5 (Batch 2, Candidate #1) — Gen 0 GA Elite (ID: `c466b080-96d`)

```text
When thunder roared and the lights went dark all
He slipped beneath his bed, his pulse a frantic thrall
A hiss, a glow—
A whisper low—
And something waited there, unseen, to maul.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 1.000 | 0.623 | 0.806 | 5 | No (0 discarded) | **Gen 0 Elite (Highest $F=0.8057$). Selected as Gen 0 Elite parent.** |

### Candidate 6 (Batch 2, Candidate #2) — ID: `ad0bbac5-449`

```text
In the storm he hid where shadows crawl
His heart beat fast, his thoughts a frantic brawl
A claw, a snarl—
A ghostly whorl—
And terror rose from the dark beneath the hall.
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.800 | 0.500 | 0.716 | 0.704 | 5 | No (0 discarded) | Evaluated; $F=0.704$ |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | GA Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `8aa54ffc-4b3` | 0.500 | 0.000 | 0.882 | 0.471 | 5 | 0 | Evaluated |
| 2 | `161e956a-b99` | 0.700 | 0.833 | 0.874 | 0.777 | 5 | 0 | Evaluated |
| 3 | `cd5d9d07-214` | 0.750 | 0.667 | 0.819 | 0.747 | 5 | 0 | Evaluated |
| 4 | `602c71d8-f38` | 0.650 | 0.833 | 0.819 | 0.738 | 5 | 0 | Evaluated |
| 5 | `c466b080-96d` | 0.800 | 1.000 | 0.623 | 0.806 | 5 | 0 | **Gen 0 Elite (Highest $F=0.8057$)** |
| 6 | `ad0bbac5-449` | 0.800 | 0.500 | 0.716 | 0.704 | 5 | 0 | Evaluated |

* **Gen 0 Elite Selected:** Candidate 5 (`c466b080-96d`, $F=0.8057$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation GA Evolution

### Generation 1

Elite parent `c466b080-96d` ($\bar{Q}=0.800, R=1.000, S=0.623, F=0.8057$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `25c0aa74-7a4` | *"When thunder boomed and the lights went out,"* | 0.700 | 1.000 | 0.796 | 0.799 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 2 | `d78280f9-4d4` | *"When lightning cracked and the night grew black,"* | 0.650 | 1.000 | 0.716 | 0.754 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 3 | `d406708e-c0c` | *"When storm clouds rolled and the shutters shivered,"* | 0.650 | 0.833 | 0.739 | 0.718 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 4 | `4a129bb7-008` | *"When rain hammered hard and the room went dim,"* | 0.700 | 1.000 | 0.740 | 0.785 | 5 | Evaluated ($F < \text{Parent}$) |
| Variant 5 | `cf367f27-c4b` | *"When thunder rattled the house’s thin wall,"* | 0.700 | 1.000 | 0.628 | 0.757 | 5 | Evaluated ($F < \text{Parent}$) |
| **Parent** | `c466b080-96d` | *"When thunder roared and the lights went dark all"* | **0.800** | **1.000** | **0.623** | **0.8057** | 5 | **Retained Elite (Elitism)** |

* **Gen 1 Elite Selected:** Parent `c466b080-96d` retained ($F=0.8057$) via elitism because no variant exceeded parent fitness.
* **$\Delta F$:** `0.0000` ($0.8057 - 0.8057$). Convergence patience counter increments to 1.

---

### Generation 2

Elite parent `c466b080-96d` ($\bar{Q}=0.800, R=1.000, S=0.623, F=0.8057$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `88667099-013` | *"When lightning cracked the night in fierce display,"* | 0.850 | 1.000 | 0.708 | 0.852 | 5 | Evaluated ($F > \text{Parent}$) |
| Variant 2 | `c12ccd7d-8d4` | *"When thunder’s growl shook walls and shutters clanged,"* | 0.850 | 0.500 | 0.684 | 0.721 | 5 | Evaluated |
| Variant 3 | `0fd40e22-ef4` | *"When storm clouds throbbed and rain beat drums of dread,"* | 0.850 | 0.667 | 0.764 | 0.783 | 5 | Evaluated |
| Variant 4 | `1f30c265-9af` | *"When skies unleashed a roar that split the dark,"* | **0.850** | **1.000** | **0.764** | **0.866** | 5 | **Gen 2 Elite (Highest $F=0.8660$)** |
| Variant 5 | `1db7418d-6c4` | *"When bolts of fire tore the heavens wide,"* | 0.750 | 1.000 | 0.764 | 0.816 | 5 | Evaluated |

* **Gen 2 Elite Selected:** Variant 4 (`1f30c265-9af`, $F=0.8660$) selected as parent for Generation 3.
* **$\Delta F$:** $+0.0603$ ($0.8660 - 0.8057 = 0.0603 \ge 0.01$). Convergence patience counter resets to 0.

---

### Generation 3

Elite parent `1f30c265-9af` ($\bar{Q}=0.850, R=1.000, S=0.764, F=0.8660$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `c03508fb-c51` | *"He slipped beneath the mattress, heart a drum,"* | 0.800 | 0.667 | 0.764 | 0.758 | 5 | Evaluated |
| Variant 2 | `95e9ffb0-3c5` | *"Beneath the bed he curled as thunder roared,"* | 0.700 | 0.667 | 0.591 | 0.664 | 5 | Evaluated |
| Variant 3 | `10b32759-9f5` | *"When thunder cracked the night and shook the floor,"* | **0.850** | **1.000** | **0.819** | **0.880** | 5 | **Gen 3 Elite (Highest $F=0.8798$)** |
| Variant 4 | `0f94c81b-b55` | *"He dove beneath the sheets as clouds did scream,"* | 0.850 | 0.500 | 0.684 | 0.721 | 5 | Evaluated |
| Variant 5 | `61a15d2f-1d7` | *"The storm erupted, fierce, and he withdrew,"* | 0.650 | 1.000 | 0.740 | 0.760 | 5 | Evaluated |

* **Gen 3 Elite Selected:** Variant 3 (`10b32759-9f5`, $F=0.8798$) selected as parent for Generation 4.
* **$\Delta F$:** $+0.0138$ ($0.8798 - 0.8660 = 0.0138 \ge 0.01$). Convergence patience counter remains at 0.

---

### Generation 4 (Final Generation)

Elite parent `10b32759-9f5` ($\bar{Q}=0.850, R=1.000, S=0.819, F=0.8798$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 4 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `cf3f07c6-088` | *"When lightning split the sky and cracked the pane,"* | 0.900 | 0.667 | 0.819 | 0.822 | 5 | Evaluated |
| Variant 2 | `b37e9baf-abf` | *"As thunder drummed the night with booming roar,"* | 0.850 | 1.000 | 0.764 | 0.866 | 5 | Evaluated |
| Variant 3 | `78231ded-e91` | *"When storm clouds tore the dark with flashing spears,"* | 0.700 | 0.667 | 0.660 | 0.682 | 5 | Evaluated |
| Variant 4 | `f08c0fd0-d89` | *"While rain hammered roofs and wind began to wail,"* | 0.750 | 1.000 | 0.651 | 0.788 | 5 | Evaluated |
| Variant 5 | `33d18e0d-ab7` | *"When booming thunder shook the quiet room,"* | 0.650 | 1.000 | 0.684 | 0.746 | 5 | Evaluated |
| **Parent** | `10b32759-9f5` | *"When thunder cracked the night and shook the floor,"* | **0.850** | **1.000** | **0.819** | **0.880** | 5 | **Retained Elite & Winning Poem** |

* **Final Generation Elite:** Parent `10b32759-9f5` maintained highest fitness ($F=0.8798$) and was retained via elitism.
* **Final Presentation Selection:** Selected elite `10b32759-9f5` ($F=0.880$).
* **$\Delta F$:** `0.0000` ($0.8798 - 0.8798$).
* **Stopping:** Generation cap reached (5 generations completed: Gen 0, 1, 2, 3, 4).

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8057 | 0.8000 | 1.0000 | 0.6227 | — | 0 | Continue |
| 1 | 0.8057 | 0.8000 | 1.0000 | 0.6227 | 0.0000 | 1 | Continue (requires 2 consecutive flat generations) |
| 2 | 0.8660 | 0.8500 | 1.0000 | 0.7639 | +0.0603 | 0 | Continue (patience reset by $>0.01$ jump) |
| 3 | 0.8798 | 0.8500 | 1.0000 | 0.8191 | +0.0138 | 0 | Continue (patience remains 0 by $>0.01$ jump) |
| 4 | 0.8798 | 0.8500 | 1.0000 | 0.8191 | 0.0000 | 1 | **STOP — Reached max generation 5** |

### Note on Stopping Rule Execution:
In Generation 1, $\Delta F = 0.0000 < 0.01$, incrementing the patience counter to 1. In Generation 2, Variant 4 jumped to $F=0.8660$ ($\Delta F = +0.0603 \ge 0.01$), resetting patience to 0. In Generation 3, Variant 3 jumped further to $F=0.8798$ ($\Delta F = +0.0138 \ge 0.01$), keeping patience at 0. In Generation 4, no variant surpassed the parent, so patience reached 1 while simultaneously hitting the hard cap of 5 generations.
The search progressed through all 5 permitted generations (Generations 0 through 4), halting cleanly at the generation cap.

**Verbatim Log Confirmation:**
```text
18:52:24 | INFO    | src.ea.ga |   Gen 4 | Best F=0.880 | Poem(id=10b32759-9f5, F=0.880, Q̄=0.850, R=1.000, S=0.819)
18:52:24 | INFO    | src.ea.common | Stopping: reached max generation 5
18:52:24 | INFO    | src.ea.ga |   Final presentation: selected elite -> 10b32759-9f5 (F=0.880)
18:52:24 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_limerick_Fear_5e93427d ═══ Generations: 5 | Final F=0.880
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–2 + 4 Mutation rounds) | 6 | 2,050 | 3,401 | **5,451** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 20 mutation variants) | 26 | 10,140 | 1,165 | **11,305** |
| **Total** | | **32** | **12,190** | **4,566** | **16,756** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 14 pauses totaling **223.80 seconds** (~3m 43.8s):
- **Waiting on `qwen/qwen3.8-27b`:** 11 pauses totaling **166.20s** (enforcing 6,000 TPM limit).
- **Waiting on `openai/gpt-oss-120b`:** 3 pauses totaling **57.60s** (enforcing 6,000 TPM limit).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 18:48:27 | 52.3s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5715/6000 |
| 2 | 18:49:20 | 2.8s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4840/6000 |
| 3 | 18:49:24 | 1.6s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5475/6000 |
| 4 | 18:49:31 | 49.2s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4909/6000 |
| 5 | 18:50:21 | 2.5s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5854/6000 |
| 6 | 18:50:24 | 0.8s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5483/6000 |
| 7 | 18:50:25 | 1.7s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 8 | 18:50:27 | 3.7s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 9 | 18:50:32 | 48.5s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5866/6000 |
| 10 | 18:51:21 | 2.8s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5495/6000 |
| 11 | 18:51:24 | 1.0s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5493/6000 |
| 12 | 18:51:25 | 5.6s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5485/6000 |
| 13 | 18:51:32 | 48.4s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 14 | 18:52:21 | 2.9s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5485/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 18:48:18 → Completion 18:52:24):** 246.0s (4m 06s)
- **Total Rate-Limit Pause Time:** 223.80s (3m 43.8s)
- **Time to Final Poem excluding pauses:** **22.20s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Rows 55–59)

```csv
ga_limerick_Fear_5e93427d,ga,limerick,Fear,0,0.8057,0.8,1.0,0.6227,"When thunder roared and the lights went dark all | He slipped beneath his bed, his pulse a frantic thrall | A hiss, a glow— | A whisper low— | And something waited there, unseen, to maul."
ga_limerick_Fear_5e93427d,ga,limerick,Fear,1,0.8057,0.8,1.0,0.6227,"When thunder roared and the lights went dark all | He slipped beneath his bed, his pulse a frantic thrall | A hiss, a glow— | A whisper low— | And something waited there, unseen, to maul."
ga_limerick_Fear_5e93427d,ga,limerick,Fear,2,0.866,0.85,1.0,0.7639,"When skies unleashed a roar that split the dark, | He sank beneath the frame, his pulse a stark, | A crackle, a flash— | A shadow’s lash— | And something lay in wait, its grin a shark."
ga_limerick_Fear_5e93427d,ga,limerick,Fear,3,0.8798,0.85,1.0,0.8191,"When thunder cracked the night and shook the floor, | He hid beneath the springs, his pulse a roar, | A shiver, a hiss— | A stare from abyss— | A phantom smiled, its teeth like jagged shore."
ga_limerick_Fear_5e93427d,ga,limerick,Fear,4,0.8798,0.85,1.0,0.8191,"When thunder cracked the night and shook the floor, | He hid beneath the springs, his pulse a roar, | A shiver, a hiss— | A stare from abyss— | A phantom smiled, its teeth like jagged shore."
```

### `output/logs/per_run_summary.csv` (Row 15)

```csv
ga_limerick_Fear_5e93427d,ga,limerick,Fear,0.8798,5,"When thunder cracked the night and shook the floor, | He hid beneath the springs, his pulse a roar, | A shiver, a hiss— | A stare from abyss— | A phantom smiled, its teeth like jagged shore."
```

### `output/logs/human_feedback.csv` (Row 13 / Index 12)

```csv
2026-11-07T13:24:43.666889+00:00,10b32759-9f5,limerick,ga,Fear,"a nervous man who hides under the bed during a thunderstorm, only to find something else already hiding there.",1,good,"When thunder cracked the night and shook the floor, | He hid beneath the springs, his pulse a roar, | A shiver, a hiss— | A stare from abyss— | A phantom smiled, its teeth like jagged shore.",0.8798,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `1` (Genetic Algorithm / GA)
   - Emotion: `3` (Fear)
   - Description: *"a nervous man who hides under the bed during a thunderstorm, only to find something else already hiding there."*
3. **Execution:** Full evolutionary process ran over 5 generations (Gen 0 through Gen 4) in **4m 06s** gross wall-clock time (18:48:18 to 18:52:24 IST), with net generation active time of **22.20s** excluding pauses.
4. **Presentation & Selection:** Winning poem `10b32759-9f5` ($F=0.8798$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: limerick` (inferred from code, not observed) due to the ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `ga` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `GOOD` live at 18:54:43 IST (`2026-11-07T13:24:43.666889+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `10b32759-9f5` and verdict `good`.
8. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; input `no` submitted; tool exited cleanly.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).

All generator outputs produced clean poetic lines without appending extraneous rhyme-scheme labels.

### Parser Discard Event (Batch 1, Generation 0)
At 18:48:22 IST during initial population generation, API call 1 returned 4 complete 5-line limericks followed by an incomplete fragment `When clouds`:
```text
18:48:22 | INFO    | src.prompts.generator | Parser discarded 1 incomplete line(s) that did not meet exact target of 5 lines for limerick
```
The generator automatically triggered Batch 2 (Call 2), which returned Candidates 5 and 6 with exactly 5 lines each, completing the population of 6.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `18:48:22 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When thunder crashed and the night gave '`
  - `18:48:22 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When lightning split the sky with a scre'`
  - `18:48:22 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When rain hammered like drums on the roo'`
  - `18:48:22 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='When winds howled and the shutters did q'`
  - `18:48:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When thunder roared and the lights went '`
  - `18:48:24 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='In the storm he hid where shadows crawl'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded:** 1 incomplete line from Batch 1.

- **Generation 1 (Mutation Variants):**
  - `18:49:24 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When thunder boomed and the lights went '`
  - `18:49:24 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When lightning cracked and the night gre'`
  - `18:49:24 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When storm clouds rolled and the shutter'`
  - `18:49:24 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='When rain hammered hard and the room wen'`
  - `18:49:24 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When thunder rattled the house’s thin wa'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `18:50:21 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When lightning cracked the night in fier'`
  - `18:50:21 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='When thunder’s growl shook walls and shu'`
  - `18:50:21 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When storm clouds throbbed and rain beat'`
  - `18:50:21 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='When skies unleashed a roar that split t'`
  - `18:50:21 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When bolts of fire tore the heavens wide'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `18:50:32 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='He slipped beneath the mattress, heart a'`
  - `18:50:32 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='Beneath the bed he curled as thunder roa'`
  - `18:50:32 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When thunder cracked the night and shook'`
  - `18:50:32 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='He dove beneath the sheets as clouds did'`
  - `18:50:32 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The storm erupted, fierce, and he withdr'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 3 Discarded Lines:** 0.

- **Generation 4 (Mutation Variants):**
  - `18:51:32 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='When lightning split the sky and cracked'`
  - `18:51:32 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='As thunder drummed the night with boomin'`
  - `18:51:32 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='When storm clouds tore the dark with fla'`
  - `18:51:32 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='While rain hammered roofs and wind began'`
  - `18:51:32 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When booming thunder shook the quiet roo'`
  - **Gen 4 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 4 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 861–886)
- `initial_population_batch_2` (Lines 888–899)
- `mutation` Gen 1 (Lines 901–938)
- `mutation` Gen 2 (Lines 940–969)
- `mutation` Gen 3 (Lines 971–1008)
- `mutation` Gen 4 (Lines 1010–1047)

