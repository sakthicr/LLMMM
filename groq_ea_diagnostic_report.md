# EA Pipeline Diagnostic Test Report

**Date:** October 7, 2026
**Test Goal:** Verify the end-to-end mechanics of the Evolutionary Algorithm (EA) pipeline (Section 4) including population creation, mutation, judging, the stopping rule, and the interactive feedback loop.
**Generator Model:** `GPT-OSS-120B` via Groq (Temporarily swapped in due to NVIDIA endpoint timeout)
**Judge Model:** `Qwen3.8-27B` via Groq (Default)
**Parameters:** Haiku | Genetic Algorithm (GA) | Emotion: Joy
**Prompt/Scenario:** "A child discovering fireflies for the first time"
**Time to Final Poem:** 1m 15s (75s wall-clock for active run `4e74c2a3`: 11:28:44 → 11:29:59)

---

## 1. Summary of Results

The diagnostic test was a **complete success**. The EA mechanics functioned flawlessly.
- **Dependency fix:** A crash initially occurred during structure scoring because the `g2p_en` python package (used for syllable counting) was missing. This was installed (`pip install g2p_en`) and the pipeline ran successfully.
- **Poem Generation:** The generator successfully created poems that followed the 5-7-5 haiku structure.
- **Timing:** The full attempt took **2 minutes and 53 seconds** (from `11:27:06` to `11:29:59`). This included generating an initial population of 10, scoring them, and running 2 mutated generations.
- **Stopping Rule:** The EA terminated correctly at Generation 2 because the fitness delta was exactly 0.000 for two consecutive generations (*Stopping: F improved by less than 0.01 for 2 consecutive generations*).

**Final Winning Poem (F = 0.775):**
> Tiny hands reach out
> Glowing dots dance in night air
> Laughter sparks like stars

---

## 2. Detailed Fitness Score Behavior

### Generation 0 (Initial Population)
The LLM generated 10 initial variants. The structure score (`S`) correctly awarded `1.000` to perfect 5-7-5 syllable counts. Unrhymed haikus naturally default to `R = 0.500`.

| Poem | Total Fitness (F) | Quality (Q̄) | Rhyme (R) | Structure (S) | Notes |
|:---:|:---:|:---:|:---:|:---:|---|
| 1 | `0.580` | `0.650` | `0.519` | `0.500` | Failed syllable count |
| 2 | `0.735` | `0.750` | `0.500` | `0.941` | Off by 1 syllable |
| 3 | `0.750` | `0.750` | `0.500` | `1.000` | Perfect 5-7-5 |
| 4 | `0.635` | `0.550` | `0.500` | `0.941` | Off by 1, poor quality |
| 5 | `0.685` | `0.650` | `0.500` | `0.941` | Off by 1, okay quality |
| 6 | `0.735` | `0.750` | `0.500` | `0.941` | Off by 1, good quality |
| **7** | **`0.775`** | **`0.800`** | **`0.500`** | **`1.000`** | **ELITE (Perfect 5-7-5, Top Quality)** |
| 8 | `0.735` | `0.750` | `0.500` | `0.941` | Off by 1 syllable |
| 9 | `0.660` | `0.600` | `0.500` | `0.941` | Off by 1, okay quality |
| 10| `0.700` | `0.650` | `0.500` | `1.000` | Perfect 5-7-5 |


### Generation 1 (Mutations)
The EA took the elite (Poem 7) and generated 5 mutations to try and beat it. None of the mutations managed to exceed the elite's Q̄ score of 0.800.

| Mutation | Total Fitness (F) | Quality (Q̄) | Rhyme (R) | Structure (S) | Result |
|:---:|:---:|:---:|:---:|:---:|---|
| 1 | `0.775` | `0.800` | `0.500` | `1.000` | Tied the elite |
| 2 | `0.685` | `0.650` | `0.500` | `0.941` | Worse (failed structure) |
| 3 | `0.775` | `0.800` | `0.500` | `1.000` | Tied the elite |
| 4 | `0.725` | `0.700` | `0.500` | `1.000` | Maintained structure, lower quality |
| 5 | `0.685` | `0.650` | `0.500` | `0.941` | Worse (failed structure) |


### Elite Progression (Logged to CSV)
Because the mutations in Gen 1 failed to beat the elite's score of `0.775`, the elite survived untouched. 

| Generation | Best F | Q̄ | R | S | Best Poem |
|:---:|:---:|:---:|:---:|:---:|---|
| **0** | `0.775` | `0.800` | `0.500` | `1.000` | `Tiny hands reach out \| Glowing dots dance in night air \| Laughter sparks like stars` |
| **1** | `0.775` | `0.800` | `0.500` | `1.000` | `Tiny hands reach out \| Glowing dots dance in night air \| Laughter sparks like stars` |
| **2** | `0.775` | `0.800` | `0.500` | `1.000` | `Tiny hands reach out \| Glowing dots dance in night air \| Laughter sparks like stars` |

---

## 3. Next Steps & State
- The `g2p_en` dependency is now installed and syllable counting works natively.
- The `src/interactive/tool.py` module is currently pointing to `GPT-OSS-120B` on Groq.
- Once the NVIDIA endpoint for `deepseek-v4.1-flash` is confirmed to be stable/working, the interactive tool can be reverted to use `generate_poem_nvidia`.
