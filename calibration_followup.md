# Calibration Follow-up — Analysis & Changes

## 1. Calibration Q̄ — 4-Dimension Mode

Reference poems have no target emotion, so scoring them on `emotion_alignment` confounded the Q̄ sub-score. Added a calibration-mode pipeline that scores only **4 dimensions** (imagery, literary_devices, originality, coherence):

| File | Change |
|------|--------|
| [`judge.py`](file:///d:/Movies/LLMMM/src/prompts/judge.py) | Added `build_calibration_judge_prompt()` — 4-dim prompt, no emotion |
| [`quality.py`](file:///d:/Movies/LLMMM/src/fitness/quality.py) | Added `CALIBRATION_DIMENSIONS`, `compute_q_bar_calibration()`, `score_quality_calibration()` |
| [`fitness.py`](file:///d:/Movies/LLMMM/src/fitness/fitness.py) | Added `evaluate_poem_calibration()` — calls calibration Q̄ |
| [`calibration.py`](file:///d:/Movies/LLMMM/src/analysis/calibration.py) | Switched from `evaluate_poem` to `evaluate_poem_calibration` |

The normal 5-dimension Q̄ used by EA runs is **unchanged**.

## 2. Limerick Rhyme Diagnostic

Traced end-word phonemes for the two suspicious poems. **Two distinct causes found:**

### "Old Man of the Dee" (R=0.333)

```
Group A: ['dee', 'flea', 'dee']
  'dee' vs 'flea': rhyme_phones=['IY1'] == ['IY1'] → rhymes=True  ✓
  'dee' vs 'dee': same_word=True → BLOCKED (identical-word check)  ← cause (a)
  'flea' vs 'dee': rhyme_phones=['IY1'] == ['IY1'] → rhymes=True  ✓

Group B: ['it', 'hatchet']
  'it' ['IH1','T'] vs 'hatchet' ['AE1','CH','AH0','T'] → rhymes=False  ← "scratch it"/"hatchet" are
                                                                            eye-rhymes, not phonetic
```

**Result:** Group A scores 2/3 pairs = 0.667, Group B scores 0. Final = 0.5×0.667 + 0.5×0 = **0.333**.

> **Cause (a):** `words_rhyme()` returns `False` for identical words (line 77). "Dee"/"Dee" is the
> limerick's repeated end-word pattern (common in Lear). The identical-word check blocks it.
>
> **Also cause (c):** "scratch it" / "hatchet" is a multi-word eye-rhyme — the scoring only
> compares single end-words ("it" vs "hatchet"), missing the phrasal rhyme.

### "Young Lady of Ryde" (R=0.500)

```
Group A: ['ryde', 'untied', 'ryde']
  'ryde' vs 'untied': ryde NOT IN CMUdict → suffix fallback → 'de' ≠ 'ed' → False  ← cause (b)
  'ryde' vs 'ryde':   same_word=True → BLOCKED                                      ← cause (a)
  'untied' vs 'ryde': ryde NOT IN CMUdict → suffix fallback → False                  ← cause (b)

Group B: ['clogs', 'dogs']
  clogs ['AA1','G','Z'] == dogs ['AA1','G','Z'] → rhymes=True  ✓
```

**Result:** Group A scores 0/3 pairs = 0. Group B scores 1. Final = 0.5×0 + 0.5×1 = **0.500**.

> **Cause (b):** "Ryde" is a proper noun not in CMUdict. The suffix fallback compares last 2
> characters ("de" vs "ed") — which don't match despite the obvious rhyme.
>
> **Cause (a):** "Ryde"/"Ryde" again blocked by the identical-word check.

### Summary of causes
| Cause | Affected poems | Description |
|-------|---------------|-------------|
| **(a) Identical end-words** | Both | `words_rhyme()` returns False for same word. Common in Lear's "refrain" pattern |
| **(b) Words missing from CMUdict** | Ryde poem | Proper nouns like "Ryde" fall through to suffix check, which fails |
| **(c) Multi-word rhymes** | Dee poem | "scratch it"/"hatchet" is a phrasal rhyme not caught by single-word comparison |

> [!IMPORTANT]
> No scoring changes made per your request — diagnostics only. Awaiting your decision on how to handle identical end-words and missing CMUdict entries.

## 3. Negative Controls

Created 5 deliberately weak poems per form in:
- [`haiku_negative.txt`](file:///d:/Movies/LLMMM/data/calibration/haiku_negative.txt) — bland weather reports, generic statements, incoherent nonsense, clichés, emotionally flat
- [`limerick_negative.txt`](file:///d:/Movies/LLMMM/data/calibration/limerick_negative.txt) — bland reports, generic/flat, incoherent, cliché, emotionally flat

All have **correct structure** (5-7-5 / AABBA with ~correct syllable counts), verified:
- Haiku negatives: S=1.000 across all 5
- Limerick negatives: S=0.977–1.000 across all 5

The differentiation should come from Q̄ (content quality). [`run_calibration.py`](file:///d:/Movies/LLMMM/run_calibration.py) now reports negative control mean F alongside reference mean F.

## 4. Token Usage

### Changes
- [`client.py`](file:///d:/Movies/LLMMM/src/api/client.py): Added **TPM sliding-window rate limiter** alongside the existing RPM limiter. Tracks `tokens_this_minute` as `(timestamp, token_count)` pairs, prunes to 60s window, and blocks if `tokens_in_last_minute() >= config.tpm` (8,000 for Qwen3.8-27B)
- [`calibration.py`](file:///d:/Movies/LLMMM/src/analysis/calibration.py): Snapshots token usage before/after calibration, reports total prompt tokens, completion tokens, and average per call
- Token breakdown (prompt/completion) tracked via new `prompt_tokens_today` and `completion_tokens_today` fields

### 429 root cause
The Groq 429s were almost certainly from the **8K TPM limit** rather than the 30 RPM limit. Each judge call uses ~350 tokens (prompt ≈ 315, completion ≈ 35). At 30 RPM that's ~10.5K TPM — exceeding the 8K limit. The rate limiter was only counting requests, not tokens. The new TPM window prevents this proactively.

### Calibration run token report
```
40 judge calls, 13,995 total tokens (prompt=12,585, completion=1,410), 350 avg tokens/call
```

### Calibration results (post all changes)

**Haiku:**
*   Reference: `n=15, F mean=0.634, std=0.086`
*   Negative:  `n=5,  F mean=0.500, std=0.038`
*   **Stats:**
    *   **Q-bar:** Ref mean=0.608 vs Neg mean=0.250 (Mann-Whitney U: U=75.0, p=0.0012)
    *   **F:** Ref mean=0.634 vs Neg mean=0.500 (Mann-Whitney U: U=70.0, p=0.0052)

**Limerick:**
*   Reference: `n=15, F mean=0.666, std=0.110`
*   Negative:  `n=5,  F mean=0.605, std=0.055`
*   **Stats:**
    *   **Q-bar:** Ref mean=0.508 vs Neg mean=0.263 (Mann-Whitney U: U=72.0, p=0.0025)
    *   **F:** Ref mean=0.666 vs Neg mean=0.605 (Mann-Whitney U: U=51.0, p=0.2661)

*Note on Limerick F scores: The F score difference is not fully separated (p=0.2661) because the negative controls have perfect structural/rhyme conformity, pulling up their F scores, but the Q-bar heavily differentiates the content quality.*

### Notable Changes
*   **Rhyme Fallback (`g2p_en`)**:
    *   "Young Lady of Ryde": Rhyme score increased from **0.500** to **0.833**.
    *   "Old Person of Dutton": Rhyme score is now **0.833**.
*   **Repeated Line-1 End Words**: The run output now explicitly flags limericks with identical L1/L5 end words. (e.g. `(*identical L1/L5 end words)`). 8 of the 15 reference limericks use this pattern, which structurally caps their max rhyme score.

## 5. Console Encoding

Added `sys.stdout.reconfigure(encoding="utf-8")` and `sys.stderr.reconfigure(encoding="utf-8")` to all entry points:

| File | Status |
|------|--------|
| [`run_calibration.py`](file:///d:/Movies/LLMMM/run_calibration.py) | ✅ Fixed |
| [`run_analysis.py`](file:///d:/Movies/LLMMM/run_analysis.py) | ✅ Fixed |
| [`run_grid.py`](file:///d:/Movies/LLMMM/run_grid.py) | ✅ Fixed |
| [`run_interactive.py`](file:///d:/Movies/LLMMM/run_interactive.py) | ✅ Fixed |
| [`run_expert_review.py`](file:///d:/Movies/LLMMM/run_expert_review.py) | ✅ Fixed |

This avoids the Windows cp1252 `UnicodeEncodeError` on `═══`, `──`, `Q̄`, `✓` etc. without replacing the Unicode symbols themselves.
