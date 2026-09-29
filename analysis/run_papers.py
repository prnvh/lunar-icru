"""Regenerate native paper calculations and explicitly conditional experiments.

Run from any directory: py -3 analysis/run_papers.py
No network, PDFs or third-party packages are required for numeric results.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"


def load(relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(relative.replace("/", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def csv_save(name, rows):
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(exist_ok=True)
    native = {}
    native["kornuta2019"] = load("models/kornuta2019/model.py").run({})
    native["jones2020"] = load("models/jones2020/model.py").run(read("models/jones2020/original_inputs.json"))
    native["sowers_niac2020"] = {}
    for case in ("commercial", "ppp_lunar", "ppp_lunar_mars"):
        data = read("models/sowers_niac2020/original_inputs.json")
        data["case"] = case
        native["sowers_niac2020"][case] = load("models/sowers_niac2020/model.py").run(data)
    native["charania2007"] = load("models/charania2007/model.py").run({
        "original_inputs": read("models/charania2007/original_inputs.json"),
        "reported_outputs": read("models/charania2007/reported_outputs.json")})
    save("native_calculations.json", native)
    rows = []
    for scenario_id, scenario in native["kornuta2019"]["scenarios"].items():
        rows.append({"model": "kornuta2019_report2018", "scenario": scenario_id,
                     "reported_npv": scenario["reported_npv_usd"],
                     "calculated_npv": scenario["native_npv_usd"],
                     "relative_error_percent": scenario["relative_absolute_difference_percent"],
                     "calculated_ror_percent": 100 * scenario["rate_of_return"],
                     "currency": "source USD, price year unresolved"})
    csv_save("kornuta_reproduction.csv", rows)

    metzger = load("experiments/metzger2023/model.py")
    m = metzger.run()
    save("metzger_conditional.json", m)
    csv_save("metzger_conditional.csv", [{k: v for k, v in row.items() if not isinstance(v, dict)} for row in m["rows"]])
    targets = {1: 30, 0.1: 119, 0.01: 436}
    launch_rows = [{"market_fraction": row["market_fraction"], "reported_launch_cost": targets[row["market_fraction"]],
                    "calculated_launch_cost": row["launch_usd_per_kg"],
                    "relative_error_percent": 100 * abs(row["launch_usd_per_kg"] / targets[row["market_fraction"]] - 1)}
                   for row in m["rows"] if row["elapsed_industry_year"] == 30]
    csv_save("metzger_launch_reproduction.csv", launch_rows)
    # Finite interpretation set: no target-fitting or hidden choice of S(0).
    variants = []
    for equation in ("prose_fabrication", "printed_development"):
        for prior_years in (0.25, 1, 5):
            for scale_dev in (False, True):
                result = metzger.run({"reliability_equation": equation, "lunar_prior_output_years": prior_years,
                                      "scale_development": scale_dev})
                for row in result["rows"]:
                    if row["market_fraction"] == 1 and row["elapsed_industry_year"] in (0, 10, 30):
                        variants.append({"equation": equation, "prior_output_years": prior_years,
                                         "scale_development": scale_dev, "elapsed_year": row["elapsed_industry_year"],
                                         "surface_lrac_2022_usd_per_kg": row["surface_lrac_usd_per_kg"],
                                         "surface_lunar_earth_ratio": row["surface_lunar_to_earth_cost_ratio"]})
    csv_save("metzger_interpretation_sensitivity.csv", variants)

    bounds = load("experiments/sowers_bounds/model.py")
    b = bounds.run()
    save("surface_offtake_bounds.json", b)
    csv_save("surface_offtake_sensitivity.csv", bounds.sweep())
    extra = ROOT / "experiments/harry_jones2021/model.py"
    if extra.exists():
        h = load("experiments/harry_jones2021/model.py").run(read("experiments/harry_jones2021/native_case.json"))
        save("harry_jones2021.json", h)
        targets_h = read("experiments/harry_jones2021/reported_outputs.json")
        comparison_h = []
        for i, row in enumerate(h["rows"]):
            for name, target in (("oxygen_pilot", "oxygen"), ("oxygen_production", "oxygen"),
                                 ("hydrogen", "hydrogen"), ("recycling", "recycling")):
                process = row["processes"][name]
                branch = process["branches"]["table_behavior_inference"]
                for metric in ("plant", "launch", "operations", "lcc"):
                    observed = targets_h[target][metric][i]
                    calculated = branch[metric + "_musd"]
                    comparison_h.append({"rate_t_per_year": row["rate_t_per_year"], "process": name,
                        "metric": metric, "reported_musd": observed, "calculated_musd": calculated,
                        "difference_musd": calculated - observed,
                        "within_printed_half_musd": abs(calculated - observed) <= 0.5,
                        "source_fit_in_range": process["source_fit_in_range"]})
            earth = row["processes"]["earth_supply"]
            for metric, field in (("containers", "container_cost_eq18_musd"),
                                  ("launch", "launch_musd"), ("lcc", "lcc_eq18_musd")):
                target = targets_h["earth_supply"][metric][i]
                comparison_h.append({"rate_t_per_year": row["rate_t_per_year"], "process": "earth_supply",
                    "metric": metric, "reported_musd": target, "calculated_musd": earth[field],
                    "difference_musd": earth[field] - target,
                    "within_printed_half_musd": abs(earth[field] - target) <= 0.5,
                    "source_fit_in_range": None})
        csv_save("harry_jones2021_reproduction.csv", comparison_h)
    hashes = {}
    for directory in ("models", "experiments", "analysis"):
        for path in sorted((ROOT / directory).rglob("*")):
            if (path.is_file() and path.suffix in (".py", ".json")
                    and path.name not in {"forward_results.json", "comparison.json", "reproduction.json"}
                    and not {"source", "sources", "__pycache__"}.intersection(path.parts)):
                hashes[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    save("input_code_manifest.json", {"sha256": hashes, "command": "py -3 analysis/run_papers.py"})
    s = b["sowers_partial_identification"]
    k = b["kornuta_modified_surface_offtake"]
    charania = load("experiments/charania_bounds/model.py").run()
    blair = load("experiments/blair2002/model.py").run()
    jones_allocation = load("experiments/jones2020_allocation/model.py").run()
    roxy = load("experiments/roxy_bounds/model.py").run()
    save("charania_price_intervals.json", charania)
    save("blair_statement_checks.json", blair)
    save("jones2020_allocation.json", jones_allocation)
    save("roxy_irr_bounds.json", roxy)
    report = [
        "# Executed paper calculations", "",
        "Generated by `py -3 analysis/run_papers.py`. Numeric pipeline uses Python's standard library and needs no source downloads.", "",
        "## Historical reconstruction", "",
        "| Case | Executed result | Remaining boundary |", "|---|---|---|",
        f"| Kornuta report 2018 | Seven NPV/ROR cases; largest relative NPV discrepancy {max(x['relative_error_percent'] for x in rows):.4f}% | Source price year unresolved |",
        "| Jones 2020 | Published plant sizing and cost equations | Campaign cost ledger remains unresolved |",
        "| Sowers NIAC 2020 | Three static company cases | Original annual phasing and IRR remain unresolved |",
        "| Charania 2007 | Cost subtotal calculations | Required sale price solver remains unresolved |", "",
        "## Equation recovery: Harry W. Jones 2021", "",
        "The forward inference recovers 12 of 16 process/rate rows in Table 1, including every cost cell at 100 and 300 tonnes/year, within the printed half-million-dollar precision. The 100-tonne oxygen case is outside the stated production-fit range; 300 is inside. No reported cost is an input to the forward model.", "",
        "The matching branch requires a reversed mass conversion in the cost relationship, hydrogen MW values passed as kW, and the omission of recycling-container procurement. Those are inferred computational behaviors, not author-confirmed corrections. Literal equations and dimensional repairs are separate executable alternatives. Four process/rate rows retain discrepancies.", "",
        "The consequences are large: at 300 tonnes/year, inferred oxygen LCC is about 1,907 million 2021 USD. Equation 14 with consistent mass units gives about 92,717 million for combined plant/reactor costing, or 114,677 million for separate costing. These alternatives do not certify either cost estimate; they show why source-unit and cost-allocation decisions materially affect the conclusion.", "",
        "## Equation recovery: Metzger 2023", "",
        "The parameter table is visually recoverable. The new implementation runs the published sector equations and explicit financing procedure. Its future lunar trajectory is conditional on exposed choices for initial experience, equipment scaling, and a printed reliability-equation inconsistency.", "",
        "| Terminal market fraction | Published launch cost | Equation 18 result | Relative error |",
        "|---|---:|---:|---:|",
    ]
    report += [f"| {x['market_fraction']} | {x['reported_launch_cost']:.2f} | {x['calculated_launch_cost']:.4f} | {x['relative_error_percent']:.4f}% |" for x in launch_rows]
    report += ["", "These are intermediate launch-cost reproductions, not a reproduction of the full orbital crossing-year Table 1. The paper itself gives a LEO crossing at year 15 in section 5.1 and year 19 in Table 1; those targets must be distinguished.", "",
        "## Conditional surface-offtake comparison", "",
        "The frozen scenario uses 1,100 tonnes/year, price 500 per kg, 10 operating years and 10% discounting. Valuation is at commissioning. Historical cost totals and cost boundaries are preserved; Sowers costs may occur anywhere inside the declared construction windows.", "",
        "| Quantity | Result |", "|---|---:|",
        f"| Kornuta modified-case NPV | {k['npv_source_currency']/1e6:,.3f} million |",
        f"| Sowers NPV over all admissible allocations | [{s['npv_lower']/1e6:,.3f}, {s['npv_upper']/1e6:,.3f}] million |",
        f"| Kornuta break-even surface price | {k['break_even_surface_price']:.2f} per kg |",
        f"| Sowers break-even surface price interval | [{s['break_even_surface_price_lower']:.2f}, {s['break_even_surface_price_upper']:.2f}] per kg |", "",
        "The Sowers NPV sign depends on spending timing within these windows. Its endpoints are mathematically sharp for this declared model class; they do not identify the historical schedule. Sixty rate/price/cost-multiplier cases are in `surface_offtake_sensitivity.csv`.", "",
        "## Further bounds from printed constraints", "",
        (
            "Charania's zero-NPV price is an interval, not a point. At 21.7 percent, "
            f"surface sale spans {charania['intervals']['case_1']['by_wacc']['table_and_figure']['price_usd_per_kg_lower']:,.0f} to "
            f"{charania['intervals']['case_1']['by_wacc']['table_and_figure']['price_usd_per_kg_upper']:,.0f} dollars per kilogram, "
            f"low lunar orbit {charania['intervals']['case_2']['by_wacc']['table_and_figure']['price_usd_per_kg_lower']:,.0f} to "
            f"{charania['intervals']['case_2']['by_wacc']['table_and_figure']['price_usd_per_kg_upper']:,.0f}, and GEO "
            f"{charania['intervals']['case_3']['by_wacc']['table_and_figure']['price_usd_per_kg_lower']:,.0f} to "
            f"{charania['intervals']['case_3']['by_wacc']['table_and_figure']['price_usd_per_kg_upper']:,.0f}. "
            "The printed prices sit inside those intervals. The schedule is still missing. "
            f"Inflating the surface stack at 2.1 percent gives {charania['case_1_inflation_only_usd_per_kg']['earliest']:,.0f} to "
            f"{charania['case_1_inflation_only_usd_per_kg']['latest']:,.0f} dollars per kilogram, above the printed inflation-only cost of 7,327."
        ), "",
        (
            "Blair Table 4.4 balances within one million dollars, and ending retained earnings equal summed net income. "
            f"Discounting net income at 10 percent, with the first year undiscounted, gives "
            f"{blair['architectures']['architecture_1']['npv_of_net_income_at_stated_rate']:.1f} and "
            f"{blair['architectures']['architecture_2']['npv_of_net_income_at_stated_rate']:.1f}, "
            "against printed project net present values 4,156 and 4,134. The printed project rates of return are not that row's internal rate. The workbook is still absent."
        ), "",
        (
            "Jones 2020 campaign ratio stays null. Splitting the Duke plant mass across the four Table 7 subsystems moves development cost from "
            f"{jones_allocation['development_FY2019_MUSD']['lower']:.1f} to {jones_allocation['development_FY2019_MUSD']['upper']:.1f} million FY2019 dollars. "
            "That allocation is not the missing launch ledger."
        ), "",
        (
            "ROXY rates depend on when the facility is launched. With transport in the delay year, oxygen-only internal rates span "
            f"{100*roxy['irr_bounds']['oxygen_only']['transport_in_year_5']['irr_lower']:.1f} to "
            f"{100*roxy['irr_bounds']['oxygen_only']['transport_in_year_5']['irr_upper']:.1f} percent, "
            "and the metals case spans "
            f"{100*roxy['irr_bounds']['oxygen_and_metals']['transport_in_year_5']['irr_lower']:.1f} to "
            f"{100*roxy['irr_bounds']['oxygen_and_metals']['transport_in_year_5']['irr_upper']:.1f} percent. "
            f"Paying transport in the first operating year starts the oxygen interval at "
            f"{100*roxy['irr_bounds']['oxygen_only']['transport_in_year_6']['irr_lower']:.1f} percent, above the printed 19.9. "
            f"Undiscounted oxygen net from the printed ingredients is {roxy['undiscounted_cumulative_net_meur']['oxygen_only']/1000:.2f} billion euros, against the table's 2.4."
        ), "",
        "**Scope:** This is a conditional financial comparison. Unknown source price years, physical product equivalence, construction working costs and differing cost boundaries prevent admission as a fully harmonized historical benchmark. The same-unit-of-account assumption and annual timing windows are explicit. These outputs do not establish Earth-versus-lunar propellant competitiveness.", "",
        "See [recovery methods](../research/recovery-methods.md) for interpretation and source issues. Full numeric outputs and input/code SHA-256 hashes accompany this report.", "",
    ]
    (OUT / "summary.md").write_text("\n".join(report), encoding="utf-8")
    print("Wrote results/summary.md, native calculations, conditional sweeps and input/code manifest.")


if __name__ == "__main__":
    main()
