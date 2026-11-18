"""Recompute every statistic used in the paper, straight from the logged data.

Inputs : judge_validation.csv (159 rows = 53 poems x 3 judge readings)
         cells.py            (the 12 accepted runs, transcribed from the workbook)
Outputs : stats.json  + printed report
Nothing here calls an API; nothing is invented.
"""
import csv, json, statistics as st
from collections import defaultdict
from scipy.stats import mannwhitneyu, wilcoxon

# ----------------------------------------------------------------- Phase I grid
# Transcribed from ea_poetry_results_v2.xlsx, sheets "Final Results" / "GA vs NSGA-II".
CELLS = [
    # form, emotion, GA(Q,R,S,F,Fcorr), NSGA(Q,R,S,F,Fcorr)
    ("Limerick", "Fear",   (0.85, 1.0, 0.8191, 0.8798, 0.8798), (0.90, 1.0, 0.8426, 0.9106, 0.9106)),
    ("Limerick", "Joy",    (0.85, 1.0, 0.7064, 0.8516, 0.8516), (0.80, 1.0, 0.6280, 0.8070, 0.8070)),
    ("Limerick", "Sorrow", (0.90, 1.0, 0.6840, 0.8710, 0.8792), (0.90, 1.0, 0.7064, 0.8766, 0.8766)),
    ("Haiku",    "Fear",   (0.85, 0.5, 1.0000, 0.8000, 0.8000), (0.85, 0.5, 0.9412, 0.7853, 0.7853)),
    ("Haiku",    "Joy",    (0.80, 0.5, 1.0000, 0.7750, 0.7750), (0.85, 0.5, 1.0000, 0.8000, 0.8000)),
    ("Haiku",    "Sorrow", (0.95, 0.5, 0.9412, 0.8353, 0.8353), (0.95, 0.5, 0.8824, 0.8206, 0.8353)),
]
out = {}

# check F = 0.5Q + 0.25R + 0.25S for every cell
fmax = 0.0
for form, emo, ga, ns in CELLS:
    for tag, v in (("GA", ga), ("NSGA-II", ns)):
        f = 0.5 * v[0] + 0.25 * v[1] + 0.25 * v[2]
        fmax = max(fmax, abs(f - v[3]))
out["F_formula_max_abs_error"] = round(fmax, 6)

ga_f  = [c[2][3] for c in CELLS]; ns_f  = [c[3][3] for c in CELLS]
ga_fc = [c[2][4] for c in CELLS]; ns_fc = [c[3][4] for c in CELLS]
ga_q  = [c[2][0] for c in CELLS]; ns_q  = [c[3][0] for c in CELLS]
ga_s  = [c[2][2] for c in CELLS]; ns_s  = [c[3][2] for c in CELLS]

def pair(a, b, name):
    d = [y - x for x, y in zip(a, b)]          # NSGA-II minus GA
    r = {"mean_GA": st.mean(a), "mean_NSGA": st.mean(b),
         "mean_diff": st.mean(d), "diffs": [round(x, 4) for x in d],
         "max_abs_diff": max(abs(x) for x in d),
         "GA_wins": sum(1 for x in d if x < -5e-4),
         "NSGA_wins": sum(1 for x in d if x > 5e-4),
         "ties": sum(1 for x in d if abs(x) <= 5e-4)}
    nz = [x for x in d if abs(x) > 1e-12]
    r["n_pairs_total"] = len(d)
    r["n_pairs_untied"] = len(nz)            # zero differences are dropped by the test
    r["min_attainable_two_sided_p"] = 2.0 / (2 ** len(nz)) if nz else None
    try:   # exact Wilcoxon signed-rank, two-sided, on the untied pairs only
        w = wilcoxon(a, b)
        r["wilcoxon_p"] = float(w.pvalue); r["wilcoxon_W"] = float(w.statistic)
    except Exception as e:
        r["wilcoxon_p"] = None; r["wilcoxon_note"] = str(e)
    out[name] = r
    return r

pair(ga_f, ns_f, "F_as_logged")
pair(ga_fc, ns_fc, "F_corrected")
pair(ga_q, ns_q, "Q_only")
pair(ga_s, ns_s, "S_only")

# ------------------------------------------------- judge validation (53 poems x 3)
rows = list(csv.DictReader(open("judge_validation.csv")))
assert len(rows) == 159, len(rows)
DIMS = ["imagery", "literary_devices", "originality", "coherence"]
per_read = defaultdict(list)          # poem key -> list of q_bar per reading
per_dim  = defaultdict(lambda: defaultdict(list))
meta     = {}
for r in rows:
    k = (r["group"], r["poem_type"], r["title"])
    per_read[k].append(float(r["q_bar_4dim"]))
    for d in DIMS:
        per_dim[k][d].append(float(r[d]))
    meta[k] = r
n_poems = len(per_read)
out["n_poems"] = n_poems
out["n_readings"] = len(rows)
assert all(len(v) == 3 for v in per_read.values())

# group-level stats over ALL readings (reproduces the run log's table)
grp = defaultdict(list)
for r in rows:
    grp[(r["group"], r["poem_type"])].append(float(r["q_bar_4dim"]))
out["groups_all_readings"] = {
    f"{g}|{f}": {"n": len(v), "mean": round(st.mean(v), 4),
                 "sd": round(st.stdev(v), 4), "min": min(v), "max": max(v)}
    for (g, f), v in sorted(grp.items())}

# group-level stats over PER-POEM MEANS (the unit used for the tests)
pm = defaultdict(list)
for k, v in per_read.items():
    pm[(k[0], k[1])].append(st.mean(v))
out["groups_poem_means"] = {
    f"{g}|{f}": {"n": len(v), "mean": round(st.mean(v), 4),
                 "sd": round(st.stdev(v), 4), "min": round(min(v), 4), "max": round(max(v), 4)}
    for (g, f), v in sorted(pm.items())}

def mw(a, b, label):
    u = mannwhitneyu(a, b, alternative="two-sided")
    # common-language effect size: P(a > b) + 0.5 P(tie)
    gt = sum(1 for x in a for y in b if x > y); eq = sum(1 for x in a for y in b if x == y)
    cles = (gt + 0.5 * eq) / (len(a) * len(b))
    allbeat = all(x > y for x in a for y in b)
    out[label] = {"n_a": len(a), "n_b": len(b), "mean_a": round(st.mean(a), 4),
                  "mean_b": round(st.mean(b), 4), "diff": round(st.mean(a) - st.mean(b), 4),
                  "U": float(u.statistic), "p": float(u.pvalue),
                  "CLES_a_over_b": round(cles, 4), "every_a_beats_every_b": allbeat}

for form in ("haiku", "limerick"):
    ea  = pm[("C_ea_generated", form)]
    hum = pm[("A_human_reference", form)]
    bad = pm[("B_negative_control", form)]
    mw(hum, bad, f"human_vs_control_{form}")
    mw(ea, bad, f"ea_vs_control_{form}")
    mw(ea, hum, f"ea_vs_human_{form}")

# dimension breakdown, EA vs human, per-poem means of the raw 1-5 sub-scores
for form in ("haiku", "limerick"):
    dd = {}
    for d in DIMS:
        ea  = [st.mean(per_dim[k][d]) for k in per_read if k[0] == "C_ea_generated"    and k[1] == form]
        hum = [st.mean(per_dim[k][d]) for k in per_read if k[0] == "A_human_reference" and k[1] == form]
        dd[d] = {"EA": round(st.mean(ea), 3), "human": round(st.mean(hum), 3),
                 "diff": round(st.mean(ea) - st.mean(hum), 3)}
    out[f"dimensions_{form}"] = dd

# judge noise
sds  = {k: st.stdev(v) for k, v in per_read.items()}
rngs = {k: max(v) - min(v) for k, v in per_read.items()}
unstable = [k for k in per_read if rngs[k] > 1e-9]
worst = max(sds, key=sds.get)
out["noise"] = {
    "n_poems": n_poems,
    "mean_within_poem_sd": round(st.mean(list(sds.values())), 4),
    "median_within_poem_sd": round(st.median(list(sds.values())), 4),
    "max_within_poem_sd": round(max(sds.values()), 4),
    "max_within_poem_sd_poem": f"{worst[0]} | {worst[1]} | {worst[2]}",
    "n_unstable": len(unstable),
    "pct_unstable": round(100 * len(unstable) / n_poems, 1),
    "mean_range": round(st.mean(list(rngs.values())), 4),
    "max_range": round(max(rngs.values()), 4),
    "judge_step_4dim": 0.0625,
    "mean_sd_in_judge_steps": round(st.mean(list(sds.values())) / 0.0625, 2),
    # a single reading of Q carries weight 0.5 in F
    "sd_contribution_to_F_single_reading": round(0.5 * st.mean(list(sds.values())), 4),
    "sd_contribution_to_F_mean_of_3": round(0.5 * st.mean(list(sds.values())) / (3 ** 0.5), 4),
}
# EA-subset noise only (the poems the EA actually optimised)
ea_sds = [sds[k] for k in per_read if k[0] == "C_ea_generated"]
out["noise"]["mean_within_poem_sd_EA_only"] = round(st.mean(ea_sds), 4)

# how many pairs would be needed to detect the observed |mean diff| in F
md = abs(out["F_corrected"]["mean_diff"])
sd_pair = 0.5 * st.mean(list(sds.values())) * (2 ** 0.5)   # sd of a GA-NSGA difference from judge noise alone
out["power"] = {"observed_mean_diff_F": round(md, 5),
                "assumed_sd_of_paired_diff": round(sd_pair, 5),
                "n_pairs_for_80pct_power": int(round((2.8 * sd_pair / md) ** 2)) if md > 0 else None}

json.dump(out, open("stats.json", "w"), indent=1)
for k, v in out.items():
    print(k, "=", json.dumps(v))
