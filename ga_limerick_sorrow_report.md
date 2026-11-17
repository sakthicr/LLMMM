# GA + Limerick + Sorrow — Full Diagnostic Report (Attempts 1 & 2)

> [!IMPORTANT]
> ### Researcher Context & Metric Footnote Notice
> * **Attempt 1 (`102c8c40`):** The `"bad"` verdict was submitted specifically to test and verify that the automated retry mechanism functions correctly in the live interactive loop — not as a genuine quality rejection. The researcher independently considered Attempt 1's poem (*"At twilight’s hush the whistle cries..."*, $F=0.8824$) to be of good quality.
> * **Attempt 2 (`9d2d8814`):** The `"good"` verdict was given primarily to complete this combination and advance the project, not because Attempt 2 was judged superior to Attempt 1.
> * **Grid Metric Flag:** When computing "attempts to acceptance" across the full experimental grid, **this specific run must be footnoted or excluded from that count**, since its recorded "2 attempts" does not reflect genuine quality-driven retries — both poems were considered acceptable by the researcher. Both poems' full data and scores are preserved below.

---

## Run Metadata

| Field | Attempt 1 | Attempt 2 |
|---|---|---|
| Run ID | `ga_limerick_Sorrow_102c8c40` | `ga_limerick_Sorrow_9d2d8814` |
| Attempt Number | 1 of 3 | 2 of 3 |
| Date | 2026-10-14 | 2026-10-14 |
| Algorithm | Genetic Algorithm (GA) — Elitist selection | Genetic Algorithm (GA) — Elitist selection |
| Poem Type | Limerick (5 lines, AABBA) | Limerick (5 lines, AABBA) |
| Target Emotion | Sorrow | Sorrow |
| Scenario | A soldier saying goodbye at the train station, not knowing if he'll return. | A soldier saying goodbye at the train station, not knowing if he'll return. |
| Generator Model | `openai/gpt-oss-120b` via Groq | `openai/gpt-oss-120b` via Groq |
| Judge Model | `qwen/qwen3.8-27b` via Groq | `qwen/qwen3.8-27b` via Groq |
| Population Size | 6 | 6 |
| Generation Cap | 5 | 5 |
| Convergence Rule | Stop if best $F$ improves $< 0.01$ for 2 gen | Stop if best $F$ improves $< 0.01$ for 2 gen |
| Generations Run | 3 (Gens 0, 1, 2) | 5 (Gens 0, 1, 2, 3, 4) |
| Termination Reason | Convergence rule ($\Delta F = 0.000$ in Gens 1, 2) | Hit Generation Cap (5 generations) |
| **Time to Final Poem** | **2m 17s** (137s wall-clock, 13:04:08 → 13:06:25) | **5m 25s** (325s wall-clock, 13:08:07 → 13:13:32) |
| Recorded Verdict | `bad` (Verification test) | `good` (Accepted to conclude combination) |
| Researcher Assessment | Acceptable / Good | Acceptable / Good |

---

## 1. Poems & Scores Comparison

### Attempt 1 Poem (`412de90c-5c4`)
```
At twilight’s hush the whistle cries,
A soldier's kiss beneath grey skies,
His pulse now thin,
His thoughts within,
The train departs with whispered sighs.
```

| Metric | Attempt 1 Value |
|---|---|
| Poem ID | `412de90c-5c4` |
| Composite Fitness ($F$) | **0.8824** |
| Quality ($\bar{Q}$) | 0.8000 |
| Rhyme ($R$) | 1.0000 |
| Structure ($S$) | 0.9295 |
| Rhyme Scheme | AABBA (cries / skies / thin / within / sighs) |
| Verdict in CSV | `bad` (Verification test of retry loop) |

### Attempt 2 Poem (`313ccfb3-bbb`)
```
Beneath waning light the platform did weep,
Grey smoke rose, a veil for the deep,
He folded his coat,
With a tremor of throat,
As the iron beast thundered, his promise to keep.
```

| Metric | Attempt 2 Value |
|---|---|
| Poem ID | `313ccfb3-bbb` |
| Composite Fitness ($F$) | **0.8562** |
| Quality ($\bar{Q}$) | 0.8500 |
| Rhyme ($R$) | 1.0000 |
| Structure ($S$) | 0.7249 |
| Rhyme Scheme | AABBA (weep / deep / coat / throat / keep) |
| Verdict in CSV | `good` (Concluded combination) |

---

## 2. Attempt 1 Detailed Progression (`102c8c40`)

### Generation 0 — Initial Population (6 Candidates)

| # | Individual / ID | $\bar{Q}$ | Rhyme | Structure | Composite $F$ | Selection Status |
|:-:|:---|:---:|:---:|:---:|:---:|:---|
| 1 | Candidate 1 | 0.6500 | 0.6667 | 0.9533 | 0.7300 | Discarded |
| 2 | **Candidate 2 (`412de90c-5c4`)** | **0.8000** | **1.0000** | **0.9295** | **0.8824** | **Selected Elite Parent** |
| 3 | Candidate 3 | 0.6500 | 1.0000 | 0.9533 | 0.8133 | Discarded |
| 4 | Candidate 4 | 0.7500 | 0.6667 | 0.9295 | 0.7741 | Discarded |
| 5 | Candidate 5 | 0.7000 | 0.5000 | 0.9767 | 0.7192 | Discarded |
| 6 | Candidate 6 | 0.5500 | 0.5000 | 0.7174 | 0.5794 | Discarded |

### Generation-by-Generation Progression
* **Gen 0:** Best $F = 0.8824$ (`412de90c-5c4`, $\bar{Q}=0.8000, R=1.0000, S=0.9295$)
* **Gen 1:** Mutated 5 variants. Best $F = 0.8824$ (Parent retained; best variant $F=0.8515$). Stall counter = 1/2.
* **Gen 2:** Mutated 5 variants. Best $F = 0.8824$ (Parent retained; best variant $F=0.8113$). Stall counter = 2/2 $\rightarrow$ **Stopping Rule Triggered**.

### Attempt 1 Stopping Rule Audit
* Concluded at **Generation 2** (3 generations total: 0, 1, 2).
* Halted because $\Delta F < 0.01$ for 2 consecutive generations (`['0.0000', '0.0000']`).

### Attempt 1 Token Usage
| Model | Call Count | Prompt Tokens | Completion Tokens | Total Tokens |
|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | 5 | 1,513 | 2,928 | 4,441 |
| `qwen/qwen3.8-27b` | 16 | 6,211 | 676 | 6,887 |
| **Total Attempt 1** | **21** | **7,724** | **3,604** | **11,328** |

---

## 3. Attempt 2 Detailed Progression (`9d2d8814`)

### Generation 0 — Initial Population (6 Candidates)

| # | Individual / ID | $\bar{Q}$ | Rhyme | Structure | Composite $F$ | Selection Status |
|:-:|:---|:---:|:---:|:---:|:---:|:---|
| 1 | Candidate 1 | 0.6500 | 0.3333 | 0.5288 | 0.5405 | Discarded |
| 2 | **Candidate 2 (`a4597424-c9e`)** | **0.6500** | **1.0000** | **0.5577** | **0.7144** | **Selected Elite Parent** |
| 3 | Candidate 3 | 0.7500 | 0.5000 | 0.3200 | 0.5800 | Discarded |
| 4 | Candidate 4 | 0.4500 | 0.5000 | 0.4300 | 0.4575 | Discarded |
| 5 | Candidate 5 | 0.4500 | 0.0000 | 0.3810 | 0.3203 | Discarded |
| 6 | Candidate 6 | 0.5500 | 0.0000 | 0.6600 | 0.4400 | Discarded |

### Generation-by-Generation Progression
* **Gen 0:** Best $F = 0.7144$ (`a4597424-c9e`, $\bar{Q}=0.6500, R=1.0000, S=0.5577$)
* **Gen 1:** Mutated 5 variants. Best $F = 0.8084$ (`3ae89551-604`, $\bar{Q}=0.8500, R=1.0000, S=0.5334$). $\Delta F = +0.0940$.
* **Gen 2:** Mutated 5 variants. Best $F = 0.8207$ (`91aeb8b3-d9e`, $\bar{Q}=0.8000, R=1.0000, S=0.6829$). $\Delta F = +0.0123$.
* **Gen 3:** Mutated 5 variants. Best $F = 0.8562$ (`313ccfb3-bbb`, $\bar{Q}=0.8500, R=1.0000, S=0.7249$). $\Delta F = +0.0355$.
* **Gen 4:** Mutated 5 variants. Best $F = 0.8562$ (Parent retained; best variant $F=0.8160$). $\Delta F = 0.0000$. Max generation cap reached.

### Attempt 2 Stopping Rule Audit
* Concluded at **Generation 4** (5 generations total: 0, 1, 2, 3, 4).
* Halted because it reached the **generation cap of 5** (convergence rule did not trigger because Gen 1, 2, 3 each improved by $>0.01$).

### Attempt 2 Token Usage
| Model | Call Count | Prompt Tokens | Completion Tokens | Total Tokens |
|---|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | 12 | 4,163 | 9,865 | 14,028 |
| `qwen/qwen3.8-27b` | 26 | 10,800 | 1,152 | 11,952 |
| **Total Attempt 2** | **38** | **14,963** | **11,017** | **25,980** |

---

## 4. Verbatim CSV Records

### `per_run_summary.csv`
```csv
run_id,ea,poem_type,emotion,final_F,generations_used,best_poem
ga_limerick_Sorrow_102c8c40,ga,limerick,Sorrow,0.8824,3,"At twilight's hush the whistle cries, | A soldier's kiss beneath grey skies, | His pulse now thin, | His thoughts within, | The train departs with whispered sighs."
ga_limerick_Sorrow_9d2d8814,ga,limerick,Sorrow,0.8562,5,"Beneath waning light the platform did weep, | Grey smoke rose, a veil for the deep, | He folded his coat, | With a tremor of throat, | As the iron beast thundered, his promise to keep."
```

### `human_feedback.csv`
```csv
timestamp,poem_id,poem_type,ea,emotion,description,attempt_number,verdict,poem_text,F_score,notes
2026-10-14T07:38:06.976174+00:00,412de90c-5c4,limerick,ga,Sorrow,"A soldier saying goodbye at the train station, not knowing if he'll return.",1,bad,"At twilight's hush the whistle cries, | A soldier's kiss beneath grey skies, | His pulse now thin, | His thoughts within, | The train departs with whispered sighs.",0.8824,"Verification retry test - poem judged acceptable by researcher"
2026-10-14T07:43:32.000000+00:00,313ccfb3-bbb,limerick,ga,Sorrow,"A soldier saying goodbye at the train station, not knowing if he'll return.",2,good,"Beneath waning light the platform did weep, | Grey smoke rose, a veil for the deep, | He folded his coat, | With a tremor of throat, | As the iron beast thundered, his promise to keep.",0.8562,"Accepted to conclude combination - not judged superior to Attempt 1"
```

---

## 5. Comparative Notes: NSGA-II vs. GA Attempts 1 & 2

| Dimension | NSGA-II (`29d9cad1`) | GA Attempt 1 (`102c8c40`) | GA Attempt 2 (`9d2d8814`) |
|---|---|---|---|
| **Search Paradigm** | Multi-objective Pareto rank on $[\bar{Q}, \text{Rhyme}]$, Structure constraint | Single-objective scalar composite $F$ | Single-objective scalar composite $F$ |
| **Generations Run** | 4 (Gens 0, 1, 2, 3) | 3 (Gens 0, 1, 2) | 5 (Gens 0, 1, 2, 3, 4) |
| **Convergence Trigger** | Gen 3 ($\Delta F < 0.01$ in Gens 2, 3) | Gen 2 ($\Delta F < 0.01$ in Gens 1, 2) | Gen 4 (Hit Generation Cap = 5) |
| **Best $F$ Score** | 0.8407 | **0.8824** | 0.8562 |
| **Best Quality ($\bar{Q}$)** | 0.8000 (0.8500 on Pareto elite) | 0.8000 | **0.8500** |
| **Best Rhyme ($R$)** | 1.0000 | 1.0000 | 1.0000 |
| **Best Structure ($S$)** | 0.7627 | **0.9295** | 0.7249 |
| **Wall-Clock Time** | **3m 34s** | **2m 17s** | **5m 25s** |
| **Total Tokens** | 18,158 | 11,328 | 25,980 |
| **CSV Verdict** | `good` (Attempt 1) | `bad` (Attempt 1) | `good` (Attempt 2) |
| **Researcher Context** | Accepted | Independently judged acceptable (retry verification) | Accepted to conclude combination |
