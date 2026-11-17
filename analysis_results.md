# Limerick Structure Score Bug — Analysis & Fix

## Root Cause

The bug was in [`score_limerick_structure()`](file:///d:/Movies/LLMMM/src/fitness/structure.py#L161-L204) — it was using `count_strong_beats()` which counts **CMUdict stressed syllables** (stress ≥ 1) as "beats". 

The problem: **CMUdict assigns primary stress (1) to the sole vowel of every monosyllable.** Words like "there", "was", "an", "old", "man", "with" all get stress=1. So a line like *"There was an Old Man with a beard"* got **7 "beats"** instead of the target of 3.

| Line | Text | Expected beats | Actual CMUdict "beats" | Deviation |
|------|------|:-:|:-:|:-:|
| 1 | There was an Old Man with a beard | 3 | **7** | +4 |
| 2 | Who said it is just as I feared | 3 | **8** | +5 |
| 3 | Two Owls and a Hen | 2 | 3 | +1 |
| 4 | Four Larks and a Wren | 2 | 3 | +1 |
| 5 | Have all built their nests in my beard | 3 | **7** | +4 |

Total deviation = 15 out of max 13 → penalty > 1.0 → **score clamped to 0.077**

The target `[3,3,2,2,3]` represents **metrical feet** (anapestic groups), not raw stress counts. CMUdict stress is too granular for this — it doesn't distinguish metrically strong vs. weak positions.

## Fix Applied

Replaced the beat-counting approach with **syllable counting** against target `[8, 8, 5, 5, 8]` (the standard limerick syllable counts, ≈ 2.67 syllables per anapestic foot). Also switched from the harsh total-deviation penalty to **Gaussian graded scoring** per line (σ=2), mirroring how Rhyme already gives partial credit:

- Deviation 0 → 1.00
- Deviation ±1 → 0.88
- Deviation ±2 → 0.61
- Deviation ±3 → 0.32

## Before/After — All 15 Reference Limericks

| # | Poem | S (before) | S (after) |
|---|------|:---:|:---:|
| 1 | Old Man with a beard (Lear) | 0.077 | **1.000** |
| 2 | Young Lady of Ryde (Lear) | 0.508 | **0.977** |
| 3 | Old Man in a tree (Lear) | 0.077 | **0.906** |
| 4 | Old Man of Nantucket (Anon) | 0.138 | **0.906** |
| 5 | Wonderful bird pelican (Merritt) | 0.015 | **0.660** |
| 6 | Old Man who supposed (Lear) | 0.015 | **0.906** |
| 7 | Young Lady whose chin (Lear) | 0.385 | **0.977** |
| 8 | Man from Blackheath (Anon) | 0.000 | **0.977** |
| 9 | Old Person of Dutton (Lear) | 0.000 | **0.827** |
| 10 | Flea and a fly (Anon) | 0.262 | **0.906** |
| 11 | Old man from Peru (Anon) | 0.323 | **0.977** |
| 12 | Old Man of the coast (Lear) | 0.138 | **0.977** |
| 13 | Old Man of the Dee (Lear) | 0.000 | **0.874** |
| 14 | Young Lady of Norway (Lear) | 0.077 | **0.772** |
| 15 | Old Man on some rocks (Lear) | 0.000 | **0.929** |
| | **Mean** | **~0.10** | **0.905** |

## Calibration Results (post-fix, `--emotion joy`)

```
Haiku calibration:    n=15, F mean=0.582, std=0.082, range=[0.412, 0.735]
Limerick calibration: n=15, F mean=0.610, std=0.079, range=[0.427, 0.733]
```

Limerick F scores now sit in a comparable range to Haiku F scores, which is expected since both sets are canonical reference poems.

## Other Fix — f-string Crash

Fixed the crash at [`calibration.py` line ~120](file:///d:/Movies/LLMMM/src/analysis/calibration.py#L116-L123) and [`run_calibration.py` line ~63](file:///d:/Movies/LLMMM/run_calibration.py#L60-L65) where a conditional expression was embedded inside a `:.3f` format spec:

```diff
-f"F std={statistics.stdev(f_scores):.3f if len(f_scores) > 1 else 0:.3f}, "
+f_std = statistics.stdev(f_scores) if len(f_scores) > 1 else 0.0
+f"F std={f_std:.3f}, "
```

## Files Changed

| File | Change |
|------|--------|
| [`structure.py`](file:///d:/Movies/LLMMM/src/fitness/structure.py#L161-L204) | Replaced beat-counting with syllable-counting + Gaussian grading |
| [`calibration.py`](file:///d:/Movies/LLMMM/src/analysis/calibration.py#L116-L123) | Fixed f-string crash (conditional in format spec) |
| [`run_calibration.py`](file:///d:/Movies/LLMMM/run_calibration.py#L60-L65) | Same f-string fix |
| [`config.py`](file:///d:/Movies/LLMMM/src/config.py#L146-L149) | Added `LIMERICK_SYLLABLE_TARGET` constant |

> [!NOTE]
> The calibration run's `print()` output still crashes on Windows cp1252 when printing Unicode box-drawing characters (`──`, `═══`, `Q̄`). This is a cosmetic issue in the console output, not in the scoring logic. The file-based logger captured all results correctly.
