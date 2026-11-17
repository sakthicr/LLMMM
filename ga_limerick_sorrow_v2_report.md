# GA + Limerick + Sorrow (v2 Rerun) — Full Diagnostic Report

## Run Metadata

| Field | Value |
|---|---|
| **Run ID** | `ga_limerick_Sorrow_18dd12e2` |
| **Attempt Number** | 1 of 3 |
| **Status / Verdict** | `good` (Accepted by human live) |
| **Date** | 2026-11-06 |
| **Start Time** | 22:16:36 IST (16:46:36 UTC) |
| **Completion Time** | 22:20:44 IST (16:50:44 UTC) |
| **Verdict Logged Time** | 22:23:04 IST (2026-11-06T16:53:04.417828+00:00 UTC) |
| **Time to Final Poem** | 4m 08s (248s wall-clock, 22:16:36 → 22:20:44 IST) |
| **Total Rate-Limit Pause Time** | 3m 43.5s (223.50s waiting across 19 account rate-limit pauses) |
| **Time to Final Poem excluding pauses** | **24.50s** (248.0s gross wall-clock − 223.50s rate-limit waits) |
| **Algorithm** | Genetic Algorithm (GA) with elitism on composite scalar fitness $F$ |
| **Fitness Formulation** | $F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$ |
| **Poem Type** | Limerick (5 lines, AABBA rhyme scheme) |
| **Target Emotion** | Sorrow |
| **Scenario** | A soldier saying goodbye at the train station, not knowing if he'll return. |
| **Generator Model** | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| **Served Judge Model ID** | `qwen/qwen3.8-27b` via Groq |
| **Population Size** | 6 |
| **Generation Cap** | 5 |
| **Convergence Rule** | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| **Mutations Per Gen** | 5 variants from elite parent |
| **Parser Version** | post-fix (hierarchical: '---' → blank lines → 5-line chunking, with trailing rhyme label strip & standalone capital warning detection) |
| **Run Status / Validity** | `valid - presented poem confirmed as Gen 4 elite with highest F` |
| **Elitism Status** | **Yes** — The presented poem (`e9a71228-c53`) is confirmed as the exact elite of the final generation (Gen 4) with $F = 0.8710$. |
| **Historical Comparison Tag** | Previous run `ga_limerick_Sorrow_93cbbf7c` was invalidated due to generator emitting rhyme-scheme labels (`', A'`) corrupting rhyme and structure scoring; this run `ga_limerick_Sorrow_18dd12e2` is clean, complete, and verified. |

---

## 1. Winning Poem (Presented & Accepted by Human)

```text
The rails sang low, a dirge of steel and rain,
A weary clasp let go, a silent pain,
The shadows fell,
His story’s knell,
Will daylight’s echo answer his refrain?
```

| Metric | Value |
|---|---|
| **Poem ID** | `e9a71228-c53` |
| **Composite Fitness ($F$)** | **0.8710** |
| **Quality ($\bar{Q}$)** | **0.9000** |
| **Rhyme ($R$)** | **1.0000** |
| **Structure ($S$)** | **0.6840** |
| **Rhyme Scheme** | AABBA — *rain* / *pain* / *fell* / *knell* / *refrain* |
| **Line Count** | 5 (target: 5) |
| **Generation Created** | Generation 4 (Variant 4) |
| **Elite in Final Generation** | **Yes** ($F = 0.8710$ vs next highest in Gen 4 $F = 0.8150$) |
| **Selection Rule** | Elitism (`winning_poem = elite`, confirmed in `src/ea/ga.py` line 149 & 164) |
| **Human Verdict** | `good` (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

The Genetic Algorithm evaluates each candidate by scalar composite fitness:
$$F = 0.50 \times \bar{Q} + 0.25 \times R + 0.25 \times S$$
The candidate with the highest $F$ in Generation 0 is chosen as the elite parent for Generation 1.

Initial population sampling required 3 API calls to `openai/gpt-oss-120b`:
- **Batch 1 (Call 1, 22:16:39 IST):** Generated Candidates 1–5 (all 5 lines each).
- **Batch 2 (Call 2, 22:16:42 IST):** Consumed 1,200 completion reasoning tokens; returned empty content string (0 candidates).
- **Batch 3 (Call 3, 22:16:45 IST):** Generated Candidate 6 (5 lines).

All 6 evaluated candidates in Generation 0 had exactly 5 lines.

### Candidate 1 (Batch 1, Candidate #1) — ID: `9eb91e5d-21c`

```text
On platform dusk, the rails sigh soft low
A soldier waves with a trembling hand low
His heart beats in a hush
While trains roar and fade away hush
Will he return? The night drapes hope low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.000 | 0.659 | 0.440 | 5 | No (0 discarded) | Evaluated; $F=0.440$ |

### Candidate 2 (Batch 1, Candidate #2) — ID: `82c239db-5e3`

```text
At midnight’s chill, the whistle cries low
The farewells linger, heavy as snow low
His eyes wet with rain
The tracks hum a sad refrain
Will he come back? The stars dim the glow low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.550 | 0.500 | 0.685 | 0.571 | 5 | No (0 discarded) | Evaluated; $F=0.571$ |

### Candidate 3 (Batch 1, Candidate #3) — Gen 0 GA Elite (ID: `879c12b6-758`)

```text
By lantern’s glow, the crowd stands still low
A soldier’s kiss slips like a thin snow low
Dreams flicker, then fade
His promise, a whispered braid
Will he return? The wind steals his echo low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.700 | 0.500 | 0.573 | 0.618 | 5 | No (0 discarded) | **Gen 0 Elite (Highest $F=0.6181$). Selected as Gen 0 Elite parent.** |

### Candidate 4 (Batch 1, Candidate #4) — ID: `546c6053-a1f`

```text
Through foggy mist, the platform sighs low
A lone salute lifts, trembling and slow low
His pulse thuds, then stills
The engine moans, sorrow fills
Will he come back? The night seals the vow low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.450 | 0.500 | 0.684 | 0.521 | 5 | No (0 discarded) | Evaluated; $F=0.521$ |

### Candidate 5 (Batch 1, Candidate #5) — ID: `f9813172-929`

```text
When dawn awakes, the shutters close low
A soldier departs, his eyes a soft glow low
Hope trembles, then dies
The rails hum low goodbyes
Will he return? The silence keeps him low
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.450 | 0.500 | 0.739 | 0.535 | 5 | No (0 discarded) | Evaluated; $F=0.535$ |

### Candidate 6 (Batch 3, Candidate #1) — ID: `f3c106bd-aa0`

```text
At dusk the platform sighs with deep grief
A soldier bows, his heart a deep grief
The train sighs, its doors close
He steps into fog, doors close
Will he return? The rails hold deep grief
```

| $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Parser Discarded | GA Status |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 0.350 | 0.000 | 0.827 | 0.382 | 5 | No (0 discarded) | Evaluated; $F=0.382$ |

### Gen 0 Summary Table

| # | Poem ID | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | Discarded Lines | GA Status |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `9eb91e5d-21c` | 0.550 | 0.000 | 0.659 | 0.440 | 5 | 0 | Evaluated |
| 2 | `82c239db-5e3` | 0.550 | 0.500 | 0.685 | 0.571 | 5 | 0 | Evaluated |
| 3 | `879c12b6-758` | 0.700 | 0.500 | 0.573 | 0.618 | 5 | 0 | **Gen 0 Elite (Highest $F=0.6181$)** |
| 4 | `546c6053-a1f` | 0.450 | 0.500 | 0.684 | 0.521 | 5 | 0 | Evaluated |
| 5 | `f9813172-929` | 0.450 | 0.500 | 0.739 | 0.535 | 5 | 0 | Evaluated |
| 6 | `f3c106bd-aa0` | 0.350 | 0.000 | 0.827 | 0.382 | 5 | 0 | Evaluated |

* **Gen 0 Elite Selected:** Candidate 3 (`879c12b6-758`, $F=0.6181$) selected as parent for Generation 1.

---

## 3. Generation-by-Generation GA Evolution

### Generation 1

Elite parent `879c12b6-758` ($\bar{Q}=0.700, R=0.500, S=0.573, F=0.618$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 1 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `3f6cd5a7-202` | *"By the platform’s sigh, the night drapes low,"* | 0.750 | 1.000 | 0.590 | 0.772 | 5 | Evaluated |
| Variant 2 | `73cc6ca9-b1e` | *"At dusk the tracks hum, a mournful refrain,"* | 0.700 | 1.000 | 0.740 | 0.785 | 5 | Evaluated |
| Variant 3 | `8e54b774-dd9` | *"The whistle’s lament cries through the steel,"* | **0.800** | **1.000** | **0.590** | **0.797** | 5 | **Gen 1 Elite (Highest $F=0.7974$)** |
| Variant 4 | `19b3e472-b57` | *"Steam curls like sighs on the cold iron line,"* | 0.700 | 1.000 | 0.684 | 0.771 | 5 | Evaluated |
| Variant 5 | `ad2d18b3-a17` | *"Midnight’s cold lantern flickers, a hush,"* | 0.650 | 1.000 | 0.628 | 0.732 | 5 | Evaluated |

* **Gen 1 Elite Selected:** Variant 3 (`8e54b774-dd9`, $F=0.7974$) selected as parent for Generation 2.
* **$\Delta F$:** $+0.1793$ ($0.7974 - 0.6181$). Convergence patience counter remains at 0.

---

### Generation 2

Elite parent `8e54b774-dd9` ($\bar{Q}=0.800, R=1.000, S=0.590, F=0.797$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 2 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `959efe34-c4a` | *"The iron rails sigh as dusk settles low,"* | 0.750 | 1.000 | 0.566 | 0.767 | 5 | Evaluated |
| Variant 2 | `5e8cdb56-3e0` | *"The platform’s lantern flickers, dim and pale,"* | 0.750 | 1.000 | 0.604 | 0.776 | 5 | Evaluated |
| Variant 3 | `7b9021a8-a24` | *"A whistle wails through mist, a mournful sound,"* | 0.750 | 1.000 | 0.684 | 0.796 | 5 | Evaluated |
| Variant 4 | `c8cb9043-a77` | *"The tracks stretch onward, cloaked in sorrow’s veil,"* | 0.750 | 1.000 | 0.683 | 0.796 | 5 | Evaluated |
| Variant 5 | `5ea7ad68-5ad` | *"Steel wheels humming a dirge beneath the sky,"* | **0.800** | **1.000** | **0.623** | **0.806** | 5 | **Gen 2 Elite (Highest $F=0.8057$)** |

* **Gen 2 Elite Selected:** Variant 5 (`5ea7ad68-5ad`, $F=0.8057$) selected as parent for Generation 3.
* **$\Delta F$:** $+0.0083$ ($0.8057 - 0.7974 = 0.0083 < 0.01$). Convergence patience counter increments to 1.

---

### Generation 3

Elite parent `5ea7ad68-5ad` ($\bar{Q}=0.800, R=1.000, S=0.623, F=0.806$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 3 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `ab3800ed-247` | *"The iron rails sang a mournful hymn in grey,"* | 0.750 | 0.500 | 0.604 | 0.651 | 5 | Evaluated |
| Variant 2 | `300d4da8-33a` | *"The steel‑kissed tracks crooned low beneath the dusk,"* | 0.700 | 0.667 | 0.772 | 0.710 | 5 | Evaluated |
| Variant 3 | `8e9aabe6-b0f` | *"The locomotive’s moan rose soft and bleak,"* | **0.850** | **1.000** | **0.684** | **0.846** | 5 | **Gen 3 Elite (Highest $F=0.8460$)** |
| Variant 4 | `1df6b343-638` | *"The carriage rattled like a funeral drum,"* | 0.850 | 1.000 | 0.604 | 0.826 | 5 | Evaluated |
| Variant 5 | `cc28c3eb-c1d` | *"The railway’s sigh breathed sorrow through the rain,"* | 0.750 | 0.500 | 0.510 | 0.627 | 5 | Evaluated |

* **Gen 3 Elite Selected:** Variant 3 (`8e9aabe6-b0f`, $F=0.8460$) selected as parent for Generation 4.
* **$\Delta F$:** $+0.0403$ ($0.8460 - 0.8057 = 0.0403 > 0.01$). Convergence patience counter resets to 0.

---

### Generation 4 (Final Generation)

Elite parent `8e9aabe6-b0f` ($\bar{Q}=0.850, R=1.000, S=0.684, F=0.846$) was mutated to produce 5 variants.
- Mutation retries: **0** (5 valid variants produced on first call).
- FAILED generations: **0** (none).

**Candidate Pool (5 Variants evaluated against Parent):**

| Individual | Poem ID | Full First Line | $\bar{Q}$ | Rhyme | Structure | $F$ | Line Count | GA Status in Gen 4 Pool |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Variant 1 | `cf0042d2-495` | *"The whistle sighed, a mournful, hollow sound,"* | 0.700 | 1.000 | 0.604 | 0.751 | 5 | Evaluated |
| Variant 2 | `8d24ba35-432` | *"The engine’s wail cut through the dusk’s dim haze,"* | 0.750 | 1.000 | 0.566 | 0.767 | 5 | Evaluated |
| Variant 3 | `984fdad4-372` | *"The iron beast exhaled a sigh of grief,"* | 0.700 | 0.167 | 0.660 | 0.557 | 5 | Evaluated |
| Variant 4 | `e9a71228-c53` | *"The rails sang low, a dirge of steel and rain,"* | **0.900** | **1.000** | **0.684** | **0.871** | 5 | **Gen 4 Elite & Winning Poem (Highest $F=0.8710$)** |
| Variant 5 | `69d27592-fec` | *"The train’s lament rose slow across the gloom,"* | 0.800 | 1.000 | 0.660 | 0.815 | 5 | Evaluated |

* **Final Generation Elite:** `e9a71228-c53` (Variant 4) achieved $\bar{Q}=0.9000, R=1.0000, S=0.6840, F=0.8710$.
* **Final Presentation Selection:** Selected elite `e9a71228-c53` ($F=0.871$).
* **$\Delta F$:** $+0.0250$ ($0.8710 - 0.8460$).
* **Stopping:** Generation cap reached (5 generations completed: Gen 0, 1, 2, 3, 4).

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | Best $\bar{Q}$ | Best $R$ | Best $S$ | $\Delta F$ | Patience Counter | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0.6181 | 0.7000 | 0.5000 | 0.5725 | — | 0 | Continue |
| 1 | 0.7974 | 0.8000 | 1.0000 | 0.5898 | +0.1793 | 0 | Continue |
| 2 | 0.8057 | 0.8000 | 1.0000 | 0.6227 | +0.0083 | 1 | Continue (requires 2 consecutive flat generations) |
| 3 | 0.8460 | 0.8500 | 1.0000 | 0.6840 | +0.0403 | 0 | Continue (patience reset by $>0.01$ jump) |
| 4 | 0.8710 | 0.9000 | 1.0000 | 0.6840 | +0.0250 | 0 | **STOP — Reached max generation 5** |

### Note on Stopping Rule Execution:
In Generation 2, $\Delta F = +0.0083 < 0.01$, incrementing the patience counter to 1. However, in Generation 3, Variant 3 jumped to $F=0.8460$ ($\Delta F = +0.0403 \ge 0.01$), resetting patience to 0. Generation 4 further improved $F$ to $0.8710$ ($\Delta F = +0.0250$). 
Because the convergence condition (2 consecutive flat generations) was never satisfied, the search progressed through all 5 permitted generations (Generations 0 through 4), halting at the hard generation cap.

**Verbatim Log Confirmation:**
```text
22:20:44 | INFO    | src.ea.ga |   Gen 4 | Best F=0.871 | Poem(id=e9a71228-c53, F=0.871, Q̄=0.900, R=1.000, S=0.684)
22:20:44 | INFO    | src.ea.common | Stopping: reached max generation 5
22:20:44 | INFO    | src.ea.ga |   Final presentation: selected elite -> e9a71228-c53 (F=0.871)
22:20:44 | INFO    | src.ea.ga | ═══ GA COMPLETE ga_limerick_Sorrow_18dd12e2 ═══ Generations: 5 | Final F=0.871
```

---

## 5. Total Token Usage & Rate-Limit Pause Breakdown

### Token Usage by Model

| Model | Role | Calls | Prompt Tokens | Completion Tokens | Total Tokens |
|---|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Generator (Initial Population batches 1–3 + 4 Mutation rounds) | 7 | 2,266 | 4,309 | **6,575** |
| `qwen/qwen3.8-27b` | Judge (Scoring 6 initial + 20 mutation variants) | 26 | 10,216 | 1,153 | **11,369** |
| **Total** | | **33** | **12,482** | **5,462** | **17,944** |

---

### Rate-Limit Pauses Audit

Account rate limiting enforced 19 pauses totaling **223.50 seconds** (~3m 43.5s):
- **Waiting on `qwen/qwen3.8-27b`:** 15 pauses totaling **165.40s** (enforcing 6,000 TPM limit).
- **Waiting on `openai/gpt-oss-120b`:** 4 pauses totaling **58.10s** (enforcing 6,000 TPM limit).

| # | Timestamp | Wait Duration | Model | Limit Status Enforced |
|:---:|:---:|:---:|:---|:---|
| 1 | 22:16:49 | 47.9s | `qwen/qwen3.8-27b` | RPM=6/25 TPM=5986/6000 |
| 2 | 22:17:38 | 2.1s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5704/6000 |
| 3 | 22:17:40 | 2.6s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4851/6000 |
| 4 | 22:17:44 | 1.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5494/6000 |
| 5 | 22:17:46 | 0.6s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5490/6000 |
| 6 | 22:17:48 | 49.7s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5489/6000 |
| 7 | 22:18:38 | 2.3s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4918/6000 |
| 8 | 22:18:42 | 1.6s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5844/6000 |
| 9 | 22:18:44 | 0.8s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5484/6000 |
| 10 | 22:18:45 | 1.5s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5486/6000 |
| 11 | 22:18:47 | 0.6s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5488/6000 |
| 12 | 22:18:47 | 50.8s | `openai/gpt-oss-120b` | RPM=7/25 TPM=4915/6000 |
| 13 | 22:19:39 | 1.6s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5837/6000 |
| 14 | 22:19:41 | 2.3s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5476/6000 |
| 15 | 22:19:44 | 0.7s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5471/6000 |
| 16 | 22:19:45 | 2.4s | `openai/gpt-oss-120b` | RPM=8/25 TPM=5468/6000 |
| 17 | 22:19:49 | 50.2s | `qwen/qwen3.8-27b` | RPM=7/25 TPM=5821/6000 |
| 18 | 22:20:39 | 1.9s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5467/6000 |
| 19 | 22:20:42 | 2.4s | `qwen/qwen3.8-27b` | RPM=8/25 TPM=5465/6000 |

### Net Execution Time
- **Gross Wall-Clock Duration (Start 22:16:36 → Completion 22:20:44):** 248.0s (4m 08s)
- **Total Rate-Limit Pause Time:** 223.50s (3m 43.5s)
- **Time to Final Poem excluding pauses:** **24.50s**

---

## 6. Verbatim CSV Records

### `output/logs/per_generation.csv` (Rows 50–54)

```csv
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,0,0.6181,0.7,0.5,0.5725,"By lantern’s glow, the crowd stands still low | A soldier’s kiss slips like a thin snow low | Dreams flicker, then fade | His promise, a whispered braid | Will he return? The wind steals his echo low"
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,1,0.7974,0.8,1.0,0.5898,"The whistle’s lament cries through the steel, | A lover’s hand trembles, the goodbye is real, | Stars dim the night, | His shadow takes flight, | Will he return, or fade where the shadows kneel?"
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,2,0.8057,0.8,1.0,0.6227,"Steel wheels humming a dirge beneath the sky, | A shaking hand lets go, a quiet sigh, | Stars lose their glow, | He rides below, | Will he be seen again, or fade where shadows lie?"
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,3,0.846,0.85,1.0,0.684,"The locomotive’s moan rose soft and bleak, | A weary hand let go, a whisper meek, | The moon grew cold, | His story untold, | Will he be found when sunrise starts to speak?"
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,4,0.871,0.9,1.0,0.684,"The rails sang low, a dirge of steel and rain, | A weary clasp let go, a silent pain, | The shadows fell, | His story’s knell, | Will daylight’s echo answer his refrain?"
```

### `output/logs/per_run_summary.csv` (Row 14)

```csv
ga_limerick_Sorrow_18dd12e2,ga,limerick,Sorrow,0.871,5,"The rails sang low, a dirge of steel and rain, | A weary clasp let go, a silent pain, | The shadows fell, | His story’s knell, | Will daylight’s echo answer his refrain?"
```

### `output/logs/human_feedback.csv` (Row 12)

```csv
2026-11-06T16:53:04.417828+00:00,e9a71228-c53,limerick,ga,Sorrow,"A soldier saying goodbye at the train station, not knowing if he'll return.",1,good,"The rails sang low, a dirge of steel and rain, | A weary clasp let go, a silent pain, | The shadows fell, | His story’s knell, | Will daylight’s echo answer his refrain?",0.871,
```

---

## 7. Interactive Tool Lifecycle

1. **Launch:** Interactive CLI started in unbuffered mode (`python -u run_interactive.py`).
2. **Interactive Choices (Live):**
   - Poem Type: `2` (Limerick)
   - Algorithm: `1` (Genetic Algorithm / GA)
   - Emotion: `2` (Sorrow)
   - Description: *"A soldier saying goodbye at the train station, not knowing if he'll return."*
3. **Execution:** Full evolutionary process ran over 5 generations (Gen 0 through Gen 4) in **4m 08s** gross wall-clock time (22:16:36 to 22:20:44 IST), with net generation active time of **24.50s** excluding pauses.
4. **Presentation & Selection:** Winning poem `e9a71228-c53` ($F=0.8710$) was displayed in styled Rich panel; tool paused at `Is this poem good? [good/bad] (good):`.
5. **Display Audit Note:** Result panel showed `EA: limerick` (inferred from code, not observed) due to the ternary bug in `_display_poem` (`src/interactive/tool.py` line 40: `"NSGA-II" if poem.poem_type == "nsga2" else poem.poem_type`). The actual algorithm was verified as `ga` in run ID, logs, and CSVs.
6. **Verdict Entry:** User entered `good` live at 22:23:04 IST (`2026-11-06T16:53:04.417828+00:00` UTC).
7. **Logging:** Feedback logged to `human_feedback.csv` with UUID `e9a71228-c53` and verdict `good`.
8. **Exit:** Tool prompted `Generate another poem? [yes/no] (yes):`; input `no` submitted; tool exited cleanly.

---

## 8. Parser Audit

### Trailing Label Stripping & Warning Audit
- **Stripped trailing rhyme-scheme label events:** **0** (no lines matched the trailing label pattern `, [A-E]`).
- **Warning log events (standalone capital or bracketed letter):** **0** (no unstripped suspicious endings detected).

All generator outputs produced clean poetic lines without appending extraneous rhyme-scheme labels.

### Per-Generation Candidate Line Counts (from `interactive.log`)

- **Generation 0:**
  - `22:16:39 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='On platform dusk, the rails sigh soft lo'`
  - `22:16:39 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='At midnight’s chill, the whistle cries l'`
  - `22:16:39 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='By lantern’s glow, the crowd stands stil'`
  - `22:16:39 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Through foggy mist, the platform sighs l'`
  - `22:16:39 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='When dawn awakes, the shutters close low'`
  - `22:16:45 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='At dusk the platform sighs with deep gri'`
  - **Gen 0 Evaluated Candidates:** 6 candidates, all exactly 5 lines.
  - **Gen 0 Discarded Lines:** 0.

- **Generation 1 (Mutation Variants):**
  - `22:17:44 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='By the platform’s sigh, the night drapes'`
  - `22:17:44 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='At dusk the tracks hum, a mournful refra'`
  - `22:17:44 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The whistle’s lament cries through the s'`
  - `22:17:44 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='Steam curls like sighs on the cold iron '`
  - `22:17:44 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Midnight’s cold lantern flickers, a hush'`
  - **Gen 1 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 1 Discarded Lines:** 0.

- **Generation 2 (Mutation Variants):**
  - `22:18:42 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='The iron rails sigh as dusk settles low,'`
  - `22:18:42 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The platform’s lantern flickers, dim and'`
  - `22:18:42 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='A whistle wails through mist, a mournful'`
  - `22:18:42 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='The tracks stretch onward, cloaked in so'`
  - `22:18:42 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='Steel wheels humming a dirge beneath the'`
  - **Gen 2 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 2 Discarded Lines:** 0.

- **Generation 3 (Mutation Variants):**
  - `22:19:39 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='The iron rails sang a mournful hymn in g'`
  - `22:19:39 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The steel‑kissed tracks crooned low bene'`
  - `22:19:39 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The locomotive’s moan rose soft and blea'`
  - `22:19:39 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='The carriage rattled like a funeral drum'`
  - `22:19:39 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The railway’s sigh breathed sorrow throu'`
  - **Gen 3 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 3 Discarded Lines:** 0.

- **Generation 4 (Mutation Variants):**
  - `22:19:49 | INFO | src.prompts.generator | Parsed candidate poem #1 | lines=5 (target=5) | first_line='The whistle sighed, a mournful, hollow s'`
  - `22:19:49 | INFO | src.prompts.generator | Parsed candidate poem #2 | lines=5 (target=5) | first_line='The engine’s wail cut through the dusk’s'`
  - `22:19:49 | INFO | src.prompts.generator | Parsed candidate poem #3 | lines=5 (target=5) | first_line='The iron beast exhaled a sigh of grief,'`
  - `22:19:49 | INFO | src.prompts.generator | Parsed candidate poem #4 | lines=5 (target=5) | first_line='The rails sang low, a dirge of steel and'`
  - `22:19:49 | INFO | src.prompts.generator | Parsed candidate poem #5 | lines=5 (target=5) | first_line='The train’s lament rose slow across the '`
  - **Gen 4 Evaluated Candidates:** 5 variants, all exactly 5 lines.
  - **Gen 4 Discarded Lines:** 0.

### Pointer to Raw Generator Responses

All verbatim API completions from `openai/gpt-oss-120b` for this run are logged in:
[output/logs/raw_generator.log](file:///d:/Movies/LLMMM/output/logs/raw_generator.log)
- `initial_population_batch_1` (Lines 672–701)
- `initial_population_batch_2` (Lines 703–704)
- `initial_population_batch_3` (Lines 706–711)
- `mutation` Gen 1 (Lines 713–750)
- `mutation` Gen 2 (Lines 752–789)
- `mutation` Gen 3 (Lines 791–820)
- `mutation` Gen 4 (Lines 822–859)

