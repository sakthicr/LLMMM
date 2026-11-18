"""Build the three paper figures (PDF for LaTeX, PNG at 300 dpi for the website)."""
import csv, json, statistics as st
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Okabe-Ito, colour-blind safe
BLUE, ORANGE, GREEN, GREY, VERM = "#0072B2", "#E69F00", "#009E73", "#6E6E6E", "#D55E00"
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8.5,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.5,
    "figure.dpi": 300, "savefig.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})
S = json.load(open("stats.json"))
NOISE_F = S["noise"]["sd_contribution_to_F_single_reading"]

def save(fig, name):
    fig.savefig(f"{name}.pdf"); fig.savefig(f"{name}.png"); plt.close(fig)
    print("wrote", name)

# ---------------------------------------------------------------- Figure 1
CELLS = [("Limerick", "Fear", 0.8798, 0.9106), ("Limerick", "Joy", 0.8516, 0.8070),
         ("Limerick", "Sorrow", 0.8792, 0.8766), ("Haiku", "Fear", 0.8000, 0.7853),
         ("Haiku", "Joy", 0.7750, 0.8000), ("Haiku", "Sorrow", 0.8353, 0.8353)]
labels = [e for _, e, _, _ in CELLS]
ga = [c[2] for c in CELLS]; ns = [c[3] for c in CELLS]
x = np.arange(len(CELLS)); w = 0.36
fig, ax = plt.subplots(figsize=(3.45, 2.25))
ax.bar(x - w / 2, ga, w, label="GA", color=BLUE, yerr=NOISE_F, capsize=2,
       error_kw=dict(lw=0.7, ecolor="0.25"))
ax.bar(x + w / 2, ns, w, label="NSGA-II", color=ORANGE, yerr=NOISE_F, capsize=2,
       error_kw=dict(lw=0.7, ecolor="0.25"))
mg, mn = st.mean(ga), st.mean(ns)
ax.axhline(mg, color="black", ls="-.", lw=0.8, zorder=1)
ax.text(4.35, 0.928, f"dash-dot: both means $\\approx$ {mg:.3f}\n(GA {mg:.4f}, NSGA-II {mn:.4f})",
        ha="center", va="center", fontsize=6.8)
ax.axvline(2.5, color="0.75", lw=0.7, ls="-", zorder=0)
ax.set_ylim(0.70, 0.96); ax.set_xticks(x); ax.set_xticklabels(labels)
for xpos, name in ((1, "Limerick"), (4, "Haiku")):
    ax.text(xpos, -0.155, name, transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=8)
ax.set_ylabel("final fitness $F$ (corrected)")
ax.set_title(f"Error bars are judge noise ($\\pm${NOISE_F:.3f} in $F$)")
ax.legend(loc="upper left", frameon=False, ncol=2, handlelength=1.2)
save(fig, "fig_ga_vs_nsga")

# ---------------------------------------------------------------- Figure 2
rows = list(csv.DictReader(open("judge_validation.csv")))
per = defaultdict(list)
for r in rows:
    per[(r["group"], r["poem_type"], r["title"])].append(float(r["q_bar_4dim"]))
def means(g, f, accepted_only=True):
    return [st.mean(v) for k, v in per.items() if k[0] == g and k[1] == f
            and not (accepted_only and "REJECTED" in k[2])]
GROUPS = [("B_negative_control", "bad", VERM),
          ("A_human_reference", "human", GREY),
          ("C_ea_generated", "EA", GREEN)]
fig, axes = plt.subplots(1, 2, figsize=(3.45, 2.1), sharey=True)
rng = np.random.default_rng(0)
for ax, form in zip(axes, ("haiku", "limerick")):
    for i, (g, lab, col) in enumerate(GROUPS):
        v = means(g, form)
        ax.scatter(i + rng.uniform(-0.13, 0.13, len(v)), v, s=11, color=col,
                   alpha=0.85, edgecolor="none", zorder=3)
        m = st.mean(v)
        ax.hlines(m, i - 0.28, i + 0.28, color="black", lw=1.1, zorder=4)
        ax.text(i, 0.985, f"{m:.2f}", ha="center", va="top", fontsize=7.5)
    ax.set_xticks(range(3)); ax.set_xticklabels([l for _, l, _ in GROUPS])
    ax.set_xlim(-0.55, 2.55); ax.set_ylim(0, 1.0)
    ax.set_title(form.capitalize(), pad=3)
axes[0].set_ylabel("judge quality score $\\bar{Q}$ (one scale)")
fig.suptitle("One judge, one prompt: bad $<$ published human $<$ EA", y=1.02, fontsize=8.5)
save(fig, "fig_judge_groups")

# ---------------------------------------------------------------- Figure 3
sds = np.array([st.stdev(v) for v in per.values()])
step = 0.0625
fig, ax = plt.subplots(figsize=(3.45, 1.95))
ax.hist(sds, bins=np.arange(0, 0.165, 0.0125), color=BLUE, edgecolor="white", linewidth=0.5)
ax.axvline(sds.mean(), color=VERM, lw=1.1,
           label=f"mean s.d. = {sds.mean():.4f} ({sds.mean()/step:.2f} judge steps)")
ax.axvline(step, color="black", ls="--", lw=0.9, label=f"one judge step = {step}")
n_unst = int((sds > 1e-9).sum())
ax.set_ylim(0, 30)
ax.set_xlabel("within-poem standard deviation of $\\bar{Q}$ over 3 readings")
ax.set_ylabel("number of poems")
ax.set_title(f"{n_unst} of {len(sds)} poems changed score between readings")
ax.legend(frameon=False, loc="upper right", fontsize=7)
save(fig, "fig_judge_noise")

# values quoted in the text, so the caption and prose cannot drift
print(json.dumps({"fig1_mean_ga": round(mg, 4), "fig1_mean_ns": round(mn, 4),
                  "noise_band_F": NOISE_F, "n_unstable": n_unst, "n_poems": len(sds),
                  "ea_haiku_accepted_mean": round(st.mean(means('C_ea_generated','haiku')), 4),
                  "ea_limerick_mean": round(st.mean(means('C_ea_generated','limerick')), 4),
                  "rejected_poem_mean": round(st.mean([st.mean(v) for k, v in per.items() if 'REJECTED' in k[2]]), 4),
                  "accepted_ga_haiku_joy_mean": round(st.mean([st.mean(v) for k, v in per.items() if k[2] == 'GA haiku Joy [accepted]']), 4)}, indent=1))
