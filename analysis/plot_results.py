"""Optional publication-style figures from already generated numeric results."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def main():
    with (RESULTS / "surface_offtake_sensitivity.csv").open(encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle)
                if float(row["relative_cost_multiplier_sowers"]) == 1 and float(row["price"]) == 500]
    rates = [100 * float(row["rate"]) for row in rows]
    lower = [float(row["sowers_break_even_price_lower"]) for row in rows]
    upper = [float(row["sowers_break_even_price_upper"]) for row in rows]
    kornuta = [float(row["kornuta_break_even_price"]) for row in rows]
    fig, ax = plt.subplots(figsize=(8.5, 5.2), layout="constrained")
    ax.fill_between(rates, lower, upper, color="#438a9e", alpha=0.25,
                    label="Sowers: all allocations within declared windows")
    ax.plot(rates, lower, color="#26728a", linewidth=1)
    ax.plot(rates, upper, color="#26728a", linewidth=1)
    ax.plot(rates, kornuta, marker="o", color="#9e423a", label="Kornuta: source timing, modified offtake")
    ax.axhline(500, color="#333333", linestyle="--", linewidth=1, label="Scenario sale price")
    ax.set(xlabel="Annual discount rate (%)", ylabel="Break-even surface price (scenario currency/kg)",
           title="Conditional financing comparison at 1,100 tonnes/year")
    ax.grid(alpha=0.18)
    ax.legend(fontsize=8, loc="upper left")
    fig.supxlabel("10 operating years; valuation at commissioning; cost multiplier=1.\n"
                  "Source price years and product equivalence unresolved. Not an Earth-versus-lunar cost comparison.", fontsize=8)
    fig.savefig(RESULTS / "surface_offtake_bounds.png", dpi=180)
    fig.savefig(RESULTS / "surface_offtake_bounds.svg")
    plt.close(fig)
    print("Wrote results/surface_offtake_bounds.png and .svg")


if __name__ == "__main__":
    main()
