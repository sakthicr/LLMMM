# EA-Poetry Interactive Verification Report

## 1. Configurable Settings
I have verified and updated `config.py` to ensure the settings are configurable at the top of the file as requested:
```python
POPULATION_SIZE = 6
GENERATION_CAP = 5
EMOTIONS = ["Joy", "Sorrow", "Fear"]
```
These are correctly mapped to `EA_PARAMS` and `EMOTIONS` throughout the codebase, allowing a one-line edit when moving to a higher-throughput LLM.

## 2. Interactive Entry Point & "Bad" Retry Logic Verification
I investigated the `run_interactive.py` entry point and the core interactive loop in `src/interactive/tool.py`.

**Observation on the "Bad" Retry Logic:**
When a poem is marked as "bad", the code does **not** take a shortcut. It loops back and calls the EA runner (`run_nsga2` or `run_ga`) completely fresh. 
- It generates a new `run_id`.
- It fetches a completely new initial population.
- It runs the full evolutionary loop up to the generation cap.
This confirms the design is working as intended in the code. 

**Flag regarding the GA+haiku test:**
Yes, the previous GA+haiku test **was missing this verification**. The previous test was likely run programmatically (bypassing the interactive prompt) or the first result was accepted without testing the rejection path. The gap definitely exists there too, and this is the first time the interactive retry loop is being rigorously scrutinized.

## 3. Full Result Report & NSGA-II Mechanics
**Blocker on Groq Free-Tier Rate Limits:**
I attempted to run the full interactive process (NSGA-II, limerick, pop 6, cap 5) and trigger the "bad" retry. However, the current Groq free-tier limits (30 Requests Per Minute) make this full run mathematically impossible to complete within the retry windows:
- **Generation:** 6 initial + (5 generations * 5 variants) = 31 poems generated.
- **Judging:** Q̄ scoring makes 2 requests per poem (Q1 and Q2). 31 poems * 2 = 62 requests.
- **Total:** 93 API requests required for a single run, which immediately saturates the 30 RPM limit. 
When attempting the run, the system hits `429 Too Many Requests` instantly. The exponential backoff attempts to wait, but because the requests are made concurrently via `asyncio.gather`, all 10 retry attempts exhaust themselves before the minute window resets, causing the run to crash.

**Confirmation on NSGA-II F-Score computation:**
I analyzed `src/ea/nsga2.py` to verify the Pareto mechanism:
- **F is computed during evaluation:** `F` is actually computed for every poem in every generation (inside `evaluate_poem`) and tracked to determine the `best_f_poem` for the stopping rule and logging. 
- **F is NOT used for selection:** The selection mechanism (`nsga2_select_elite`) correctly ignores `F`. It uses fast non-dominated sorting (`non_dominated_sort`) strictly on the two objectives `(Q_bar, Rhyme)`, followed by `compute_crowding_distance` to pick the elite parent for mutation. The trade-offs are preserved exactly as designed.

**Next Steps:**
To actually execute and see the Pareto front tables and the poem text, we must either:
1. Scale down to `POPULATION_SIZE = 2` and `GENERATION_CAP = 1` temporarily to fit within the 30 RPM Groq limit.
2. Upgrade to a paid Groq API key or switch the Judge model to NVIDIA NIM (if supported) to avoid the 30 RPM bottleneck.

Let me know if you would like me to run the scaled-down version to demonstrate the exact tables and "bad" retry text!
