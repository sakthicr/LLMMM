# GA + Haiku + Fear — Full Diagnostic Report

## Run Metadata

| Field | Value |
|-------|-------|
| Run ID | `ga_haiku_Fear_144a75a8` |
| Attempt | 1 of 3 (Accepted) |
| Date | 2026-10-15 |
| Algorithm | Genetic Algorithm (GA) — Single-objective elitist selection on composite fitness $F$ |
| Poem Type | Haiku (3 lines, 5-7-5 syllable structure) |
| Target Emotion | Fear |
| Scenario | Walking alone down an unlit street, hearing footsteps that match your pace exactly. |
| Generator Model | `openai/gpt-oss-120b` via Groq (reasoning_effort: low) |
| Judge Model | `qwen/qwen3.8-27b` via Groq |
| Population Size | 6 |
| Generation Cap | 5 |
| Convergence Rule | Stop if best $F$ improves by less than 0.01 for 2 consecutive generations |
| Mutations Per Gen | 5 variants from single elite parent |
| Fitness Formulation | $F = 0.50 \cdot \bar{Q} + 0.25 \cdot R + 0.25 \cdot S$ |
| **Time to Final Poem** | **2m 12s** (132s wall-clock, 12:39:25 → 12:41:37) |

---

## 1. Winning Poem & Human Feedback

```
Dark lane, silent pulse
Footsteps mirror my own tread
Heart drums in the void
```

| Metric | Value |
|--------|-------|
| Poem ID | `89670b66-c27` |
| Composite Fitness ($F$) | 0.8000 |
| Quality ($\bar{Q}$) | 0.8500 |
| Rhyme ($R$) | 0.5000 (unrhymed haiku baseline) |
| Structure ($S$) | 1.0000 (perfect 5-7-5) |
| Human Verdict | **good** (Accepted at Attempt 1) |

---

## 2. Generation 0 — Initial Population (All 6 Candidates)

| # | Individual / ID | $\bar{Q}$ | Rhyme | Structure | Composite $F$ | Selection Status |
|:-:|:---|:---:|:---:|:---:|:---:|:---|
| 1 | Candidate 1 | 0.6000 | 0.5000 | 0.4412 | 0.5353 | Discarded |
| 2 | Candidate 2 | 0.7500 | 0.5000 | 1.0000 | 0.7500 | Discarded |
| 3 | **Candidate 3 (`89670b66-c27`)** | **0.8500** | **0.5000** | **1.0000** | **0.8000** | **Selected Elite Parent** |
| 4 | Candidate 4 | 0.8500 | 0.5000 | 0.8235 | 0.7559 | Discarded |
| 5 | Candidate 5 | 0.8500 | 0.5000 | 0.9412 | 0.7853 | Discarded |
| 6 | Candidate 6 | 0.6500 | 0.5000 | 0.8824 | 0.6706 | Discarded |

### Gen 0 Elite Analysis
Candidate 3 (`89670b66-c27`) achieved the highest composite fitness $F = 0.8000$ in the initial pool with perfect syllable structure ($S = 1.0000$), haiku-standard rhyme ($R = 0.5000$), and strong emotional alignment ($\bar{Q} = 0.8500$). Selected as the elite parent for mutation.

---

## 3. Generation-by-Generation Evolution

### Generation 1
Elite `89670b66-c27` ($F=0.8000$) was mutated into 5 variants.

| Individual | $\bar{Q}$ | Rhyme | Structure | Composite $F$ | Outcome |
|:---|:---:|:---:|:---:|:---:|:---|
| **Parent Elite (`89670b66-c27`)** | **0.8500** | **0.5000** | **1.0000** | **0.8000** | **Retained as Best** |
| Variant 1 | 0.8500 | 0.5000 | 1.0000 | 0.8000 | Tied with parent |
| Variant 2 | 0.8500 | 0.5000 | 1.0000 | 0.8000 | Tied with parent |
| Variant 3 | 0.7500 | 0.5000 | 1.0000 | 0.7500 | Inferior to parent |
| Variant 4 | 0.8500 | 0.5000 | 0.9412 | 0.7853 | Inferior to parent |
| Variant 5 | 0.8500 | 0.5000 | 1.0000 | 0.8000 | Tied with parent |

- **Best $F$:** 0.8000 (held by parent `89670b66-c27`)
- **$\Delta F$:** 0.0000
- **Stall Counter:** 1 / 2

---

### Generation 2
Elite `89670b66-c27` ($F=0.8000$) was mutated into 5 variants.

| Individual | $\bar{Q}$ | Rhyme | Structure | Composite $F$ | Outcome |
|:---|:---:|:---:|:---:|:---:|:---|
| **Parent Elite (`89670b66-c27`)** | **0.8500** | **0.5000** | **1.0000** | **0.8000** | **Retained as Best** |
| Variant 1 | 0.8500 | 0.5000 | 1.0000 | 0.8000 | Tied with parent |
| Variant 2 | 0.8500 | 0.5000 | 1.0000 | 0.8000 | Tied with parent |
| Variant 3 | 0.7500 | 0.5000 | 0.9412 | 0.7353 | Inferior to parent |
| Variant 4 | 0.6500 | 0.5000 | 1.0000 | 0.7000 | Inferior to parent |
| Variant 5 | 0.8000 | 0.5000 | 1.0000 | 0.7750 | Inferior to parent |

- **Best $F$:** 0.8000 (held by parent `89670b66-c27`)
- **$\Delta F$:** 0.0000
- **Stall Counter:** 2 / 2 $\rightarrow$ **Stopping Rule Triggered**

---

## 4. Stopping Rule Audit

| Generation | Best $F$ | $\Delta F$ from Prior Gen | Consecutive Stall Generations | Status |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0.8000 | — | 0 | Baseline established |
| 1 | 0.8000 | 0.0000 | 1 | Patience counter incremented |
| 2 | 0.8000 | 0.0000 | 2 | **Stopping condition met ($\Delta F < 0.01$ for 2 consecutive rounds)** |

**Audit Conclusion:**
- The run concluded at **Generation 2** (3 generations evaluated total: 0, 1, 2).
- It stopped because the convergence rule triggered, **not** because it hit the generation cap of 5.
- Log record:
  ```
  12:41:37 | INFO | src.ea.common | Stopping: F improved by less than 0.01 for 2 consecutive generations (deltas: ['0.0000', '0.0000'])
  12:41:37 | INFO | src.ea.ga | ═══ GA COMPLETE ga_haiku_Fear_144a75a8 ═══ Generations: 3 | Final F=0.800
  ```

---

## 5. Token Usage Summary

| Model | Role | Call Count | Prompt Tokens | Completion Tokens | Total Tokens |
|-------|------|:---:|:---:|:---:|:---:|
| `openai/gpt-oss-120b` | Initial Pop (2 calls) + Mutations (2 calls) | 4 | 1,164 | 2,672 | 3,836 |
| `qwen/qwen3.8-27b` | Judge (6 Gen 0 + 5 Gen 1 + 5 Gen 2) | 16 | 5,769 | 824 | 6,593 |
| **Total** | | **20** | **6,933** | **3,496** | **10,429** |

---

## 6. Verbatim CSV Records

### `per_generation.csv`
```csv
run_id,ea,poem_type,emotion,generation,F,Q_bar,Rhyme,Structure,best_poem
ga_haiku_Fear_144a75a8,ga,haiku,Fear,0,0.8000,0.8500,0.5000,1.0000,Dark lane, silent pulse | Footsteps mirror my own tread | Heart drums in the void
ga_haiku_Fear_144a75a8,ga,haiku,Fear,1,0.8000,0.8500,0.5000,1.0000,Dark lane, silent pulse | Footsteps mirror my own tread | Heart drums in the void
ga_haiku_Fear_144a75a8,ga,haiku,Fear,2,0.8000,0.8500,0.5000,1.0000,Dark lane, silent pulse | Footsteps mirror my own tread | Heart drums in the void
```

### `per_run_summary.csv`
```csv
run_id,ea,poem_type,emotion,final_F,generations_used,best_poem
ga_haiku_Fear_144a75a8,ga,haiku,Fear,0.8000,3,Dark lane, silent pulse | Footsteps mirror my own tread | Heart drums in the void
```

### `human_feedback.csv`
```csv
timestamp,poem_id,poem_type,ea,emotion,description,attempt_number,verdict,poem_text,F_score,notes
2026-10-15T07:16:28...,89670b66-c27,haiku,ga,Fear,"Walking alone down an unlit street, hearing footsteps that match your pace exactly.",1,good,Dark lane, silent pulse | Footsteps mirror my own tread | Heart drums in the void,0.8000,
```

---

## 7. Observations

- **Immediate convergence:** The Gen 0 elite poem was strong enough ($F=0.800$) that no mutation across 10 variants (5 per generation × 2 generations) was able to surpass it. Several tied at $F=0.800$ (achieving the same $\bar{Q}=0.850$, $R=0.500$, $S=1.000$) but none exceeded it.
- **Structure dominance:** 10 out of 16 evaluated haikus achieved perfect $S=1.000$ (5-7-5 syllable count). The generator is highly reliable at producing structurally valid haikus.
- **Quality ceiling:** $\bar{Q}=0.850$ appears to be a local quality ceiling for this scenario/emotion combination — multiple distinct variants independently scored exactly 0.850.
- **Haiku rhyme baseline:** As expected, all haikus scored $R=0.500$ (the unrhymed haiku baseline). This is by design — haikus don't typically rhyme, and the fitness formulation accounts for this.
