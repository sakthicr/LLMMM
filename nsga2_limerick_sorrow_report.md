# NSGA-II + Limerick + Sorrow — Full Diagnostic Report

## Run Metadata

| Field | Value |
|-------|-------|
| Run ID | `nsga2_limerick_Sorrow_29d9cad1` |
| Date | 2026-10-14 |
| Algorithm | NSGA-II (non-dominated sorting on two objectives: Quality and Rhyme) |
| Poem Type | Limerick (5 lines, AABBA rhyme scheme) |
| Target Emotion | Sorrow |
| Scenario | A soldier saying goodbye at the train station, not knowing if he'll return |
| Generator Model | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| Judge Model | `qwen/qwen3.8-27b` via Groq |
| Population Size | 6 |
| Generation Cap | 5 |
| Convergence Rule | Stop if best F improves by less than 0.01 for 2 consecutive generations |
| Mutations Per Gen | 5 variants from elite parent |
| Run Status / Validity | `superseded - presented poem was not from the final Pareto front` |
| Parser Version | pre-fix parser |
| Time to Final Poem | 3m 34s (214s wall-clock, 12:23:14 → 12:26:48) |


---

## 1. Winning Poem (Accepted by Human)

```
By the tracks the dusk draped its gray veil
He clasped a torn letter, his breath turned pale
No words left to speak
No tears left to leak
The engine's sigh mourned the sorrowful rail
```

| Metric | Value |
|--------|-------|
| Poem ID | `3dd4642f-fb3` |
| Composite Fitness (F) | 0.8407 |
| Quality (Q-bar) | 0.8000 |
| Rhyme (R) | 1.0000 |
| Structure (S) | 0.7627 |
| Rhyme Scheme | AABBA — veil / pale / speak / leak / rail |
| Human Verdict | good (Attempt 1 of 3) |

---

## 2. Generation 0 — Full Population (All 6 Candidates)

NSGA-II sorts on two objectives: Quality (Q-bar) and Rhyme (R). Structure is a feasibility constraint (S >= 0.30), not a search objective. Composite F = 0.50 * Q-bar + 0.25 * R + 0.25 * S is tracked for stopping/logging only.

### Candidate 1

```
Cold iron rails hum a lonely good-bye
As soldiers pack gear under clouds in the sky
The engine's loud roar
Shakes the station's damp floor
And kisses are stolen before whistles cry
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.550 | 0.000 | 0.651 | 0.438 | Dominated (R=0.000, beaten by #6 on both objectives) |

### Candidate 2

```
A soldier in uniform turns to embrace
The tears in his mother's frail, sorrowful face
The luggage is stacked
Though his courage is cracked
He steps on the train with a measured slow pace
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.350 | 0.000 | 0.410 | 0.278 | Dominated (Lowest Q-bar in population, R=0.000) |

### Candidate 3

```
Steam rises up from the platform so cold
As tight hands unclasp and the orders unfold
A trumpet plays low
Through the drifting white snow
For boys heading off to a fate left untold
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.650 | 0.500 | 0.340 | 0.535 | Dominated (R=0.500 and Q-bar=0.650 both beaten by #6) |

### Candidate 4

```
The platform is wet and the lamplight is bleak
He pulls his warm coat to his trembling cheek
The conductor's sharp bell
Rings a heavy farewell
As grief steals the words that neither can speak
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.550 | 0.000 | 0.739 | 0.460 | Dominated (R=0.000, beaten by #6 on both objectives) |

### Candidate 5

```
His fingers slip loose from her sorrowful hand
As soldiers prepare for a dangerous land
The wheels start to groan
Leaving loved ones alone
Across the damp tracks where the mourners still stand
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.750 | 1.000 | 0.644 | 0.786 | Dominated by #6 (Both have R=1.000, but Q-bar 0.750 < 0.800) |

### Candidate 6 — NSGA-II Elite (ID: `34e4ad16-2c4`)

```
The station grew silent as dusk turned to gray
He clutched his last letter, then turned away
No hope in his eyes
No tears left to rise
And the whistle blew softly, a lamenting lay
```

| Q-bar | Rhyme | Structure | F | NSGA-II Status |
|:-----:|:-----:|:---------:|:---:|----------------|
| 0.800 | 1.000 | 0.613 | 0.803 | **Rank 0 — Sole non-dominated solution. Selected as elite parent for mutation.** |

### Gen 0 Summary Table

| # | Q-bar | Rhyme | Structure | F | Pareto Rank |
|:-:|:-----:|:-----:|:---------:|:---:|:-----------:|
| 1 | 0.550 | 0.000 | 0.651 | 0.438 | Dominated |
| 2 | 0.350 | 0.000 | 0.410 | 0.278 | Dominated |
| 3 | 0.650 | 0.500 | 0.340 | 0.535 | Dominated |
| 4 | 0.550 | 0.000 | 0.739 | 0.460 | Dominated |
| 5 | 0.750 | 1.000 | 0.644 | 0.786 | Dominated |
| 6 | 0.800 | 1.000 | 0.613 | 0.803 | **Rank 0** |

**Why #6 dominates #5:** Both score R=1.000, but #6 has Q-bar=0.800 > 0.750. Since #6 is equal-or-better on all objectives and strictly better on at least one, it dominates #5.

**Why #6 is the sole Pareto member:** No other candidate achieves R >= 1.000 and Q-bar >= 0.800 simultaneously. Candidate #6 strictly dominates every other individual in the population on the two NSGA-II objectives.

---

## 3. Generation-by-Generation Pareto Front Evolution

### Generation 1

Elite `34e4ad16-2c4` (Q-bar=0.800, R=1.000) was mutated to produce 5 variants.

**Candidate pool (elite + 5 variants):**

| Individual | Q-bar | Rhyme | Structure | F | Pareto Status |
|:-----------|:-----:|:-----:|:---------:|:---:|:--------------|
| Variant 1 | 0.500 | 0.000 | 0.604 | 0.401 | Dominated |
| `3dd4642f-fb3` (Variant 2) | 0.800 | 1.000 | 0.763 | 0.841 | Dominated by `40cef18c-a11` on Q-bar |
| Variant 3 | 0.800 | 1.000 | 0.651 | 0.813 | Dominated by `40cef18c-a11` on Q-bar |
| `40cef18c-a11` (Variant 4) | **0.850** | **1.000** | 0.533 | 0.808 | **Rank 0 — New elite** |
| `34e4ad16-2c4` (original elite) | 0.800 | 1.000 | 0.613 | 0.803 | Dominated by `40cef18c-a11` on Q-bar |

**The NSGA-II trade-off explained:**

```
NSGA-II selected elite:  40cef18c-a11  (Q-bar=0.850, R=1.000, S=0.533, F=0.808)
Overall best-F tracker:  3dd4642f-fb3  (Q-bar=0.800, R=1.000, S=0.763, F=0.841)
```

These are two different poems serving two different roles:
- `40cef18c-a11` won on the NSGA-II search objectives (highest Q-bar at R=1.000) — this becomes the parent for next-generation mutation.
- `3dd4642f-fb3` won on composite F (because its superior Structure score S=0.763 outweighs the Q-bar gap in the weighted sum) — this is the poem presented to the human.

**Full text of the Gen 1 NSGA-II elite (`40cef18c-a11`):**

```
The station stands cold under shadows of gray
He folds up her letter, then turns him away
His heartbeat runs thin
As the soldiers march in
And sorrow hangs heavy along the iron way
```

**Full text of the Gen 1 best-F poem (`3dd4642f-fb3`):**

```
By the tracks the dusk draped its gray veil
He clasped a torn letter, his breath turned pale
No words left to speak
No tears left to leak
The engine's sigh mourned the sorrowful rail
```

### Generation 2

Elite `40cef18c-a11` (Q-bar=0.850, R=1.000) was mutated to produce 5 variants.

| Individual | Q-bar | Rhyme | Structure | F | Pareto Status |
|:-----------|:-----:|:-----:|:---------:|:---:|:--------------|
| Variant 1 | 0.500 | 0.500 | 0.763 | 0.566 | Dominated |
| Variant 2 | 0.550 | 0.500 | 0.590 | 0.547 | Dominated |
| Variant 3 | 0.550 | 0.500 | 0.613 | 0.553 | Dominated |
| Variant 4 | 0.550 | 0.500 | 0.613 | 0.553 | Dominated |
| Variant 5 | 0.650 | 0.500 | 0.651 | 0.613 | Dominated |

**Pareto front:** `40cef18c-a11` retained as sole Rank 0 (no variant exceeded Q-bar=0.850 at R=1.000).
**Best-F:** `3dd4642f-fb3` still holds at F=0.8407 (unchanged from Gen 1).
**Delta-F:** 0.0000 — Convergence patience counter increments to 1.

### Generation 3

Elite `40cef18c-a11` (Q-bar=0.850, R=1.000) was mutated to produce 5 variants.

| Individual | Q-bar | Rhyme | Structure | F | Pareto Status |
|:-----------|:-----:|:-----:|:---------:|:---:|:--------------|
| Variant 1 | 0.800 | 1.000 | 0.763 | 0.841 | Dominated (Q-bar < 0.850) |
| Variant 2 | 0.800 | 1.000 | 0.651 | 0.813 | Dominated |
| Variant 3 | 0.800 | 1.000 | 0.651 | 0.813 | Dominated |
| Variant 4 | 0.700 | 1.000 | 0.642 | 0.760 | Dominated |
| Variant 5 | 0.800 | 1.000 | 0.557 | 0.789 | Dominated |

**Pareto front:** `40cef18c-a11` retained as sole Rank 0 again.
**Best-F:** `3dd4642f-fb3` still holds at F=0.8407 (unchanged).
**Delta-F:** 0.0000 — Convergence patience counter increments to 2. **Stopping rule triggered.**

---

## 4. Stopping Rule Audit

| Generation | Best F | Delta-F | Patience Counter | Action |
|:----------:|:------:|:-------:|:----------------:|:-------|
| 0 | 0.8033 | — | 0 | Continue |
| 1 | 0.8407 | +0.0374 | 0 (reset) | Continue |
| 2 | 0.8407 | 0.0000 | 1 | Continue (need 2 consecutive) |
| 3 | 0.8407 | 0.0000 | 2 | **STOP — convergence rule triggered** |

**Conclusion:** The run stopped at Generation 3 (4 total generations evaluated: 0, 1, 2, 3) because the 2-consecutive-flat-generations convergence rule triggered. It did NOT hit the generation cap of 5.

**Log line confirming the stop:**
```
12:26:48 | INFO | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
12:26:48 | INFO | src.ea.nsga2 | NSGA-II COMPLETE nsga2_limerick_Sorrow_29d9cad1 — Generations: 4 | Final F=0.841
```

---

## 5. Total Token Usage

| Model | Role | Tokens Used |
|-------|------|:-----------:|
| openai/gpt-oss-120b | Generator (initial pop + 3 mutation rounds) | 8,721 |
| qwen/qwen3.8-27b | Judge (scoring 6 initial + 15 variants = 21 evaluations) | 9,437 |
| **Total** | | **18,158** |

Daily budget remaining after this run: approximately 191,000 / 200,000 TPD on gpt-oss-120b.

---

## 6. Verbatim CSV Records

### per_generation.csv (this run's 4 rows)

| run_id | ea | poem_type | emotion | generation | F | Q_bar | Rhyme | Structure | best_poem |
|--------|-----|-----------|---------|:----------:|:----:|:-----:|:-----:|:---------:|-----------|
| nsga2_limerick_Sorrow_29d9cad1 | nsga2 | limerick | Sorrow | 0 | 0.8033 | 0.8000 | 1.0000 | 0.6133 | The station grew silent as dusk turned to gray... |
| nsga2_limerick_Sorrow_29d9cad1 | nsga2 | limerick | Sorrow | 1 | 0.8407 | 0.8000 | 1.0000 | 0.7627 | By the tracks the dusk draped its gray veil... |
| nsga2_limerick_Sorrow_29d9cad1 | nsga2 | limerick | Sorrow | 2 | 0.8407 | 0.8000 | 1.0000 | 0.7627 | By the tracks the dusk draped its gray veil... |
| nsga2_limerick_Sorrow_29d9cad1 | nsga2 | limerick | Sorrow | 3 | 0.8407 | 0.8000 | 1.0000 | 0.7627 | By the tracks the dusk draped its gray veil... |

### per_run_summary.csv (this run's row)

| run_id | ea | poem_type | emotion | final_F | generations_used | best_poem |
|--------|-----|-----------|---------|:-------:|:----------------:|-----------|
| nsga2_limerick_Sorrow_29d9cad1 | nsga2 | limerick | Sorrow | 0.8407 | 4 | By the tracks the dusk draped its gray veil... |

### human_feedback.csv (this run's row)

| timestamp | poem_id | poem_type | ea | emotion | attempt | verdict | F_score |
|-----------|---------|-----------|-----|---------|:-------:|:-------:|:-------:|
| 2026-10-14T07:05:32Z | 3dd4642f-fb3 | limerick | nsga2 | Sorrow | 1 | good | 0.8407 |

---

## 7. Interactive Tool Lifecycle

1. After evolution completed, the tool displayed the winning poem and paused at the live prompt: `Is this poem good? [good/bad]`
2. Human entered: `good`
3. Tool logged the verdict: `Human feedback: poem=3dd4642f-fb3 | verdict=good | attempt=1`
4. Tool printed: `Poem accepted! (ID: 3dd4642f-fb3, eligible for expert review)`
5. Tool prompted: `Generate another poem? [yes/no]`
6. Response: `no`
7. Tool printed: `Session complete. Goodbye!`
8. Process exited with code 0 (clean exit).
9. **Current state:** Interactive tool is terminated. Ready for next session launch.
