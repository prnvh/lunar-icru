"""Sharp NPV bounds over nonnegative cost allocations in declared time windows.

This analysis does not recover a unique historical cash flow or fit the printed
IRR. For fixed total costs and time windows, discounted cost is a linear
functional. Its extrema put each cost at an endpoint, so there is no sampling
error and no need to pick an invented spending profile.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_model(name):
    path = ROOT / "models" / name / "model.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cost_pv_bounds(costs, windows, rate):
    if not math.isfinite(rate) or rate < 0:
        raise ValueError("rate must be finite and nonnegative")
    low = high = 0.0
    endpoints = {}
    for key, cost in costs.items():
        start, end = windows[key]
        if cost < 0 or not math.isfinite(cost) or start > end or end > 0:
            raise ValueError("Need nonnegative cost and ordered pre-commissioning window")
        early, late = cost / (1 + rate) ** start, cost / (1 + rate) ** end
        low += late
        high += early
        endpoints[key] = {"earliest_time": start, "latest_time": end,
                          "pv_if_early": early, "pv_if_late": late}
    return low, high, endpoints


def run(overrides=None):
    scenario = json.loads(Path(__file__).with_name("scenario.json").read_text(encoding="utf-8"))
    permitted = {"discount_rate", "sale_price_per_kg", "cost_multiplier_sowers"}
    if set(overrides or {}) - permitted:
        raise ValueError("Only rate, price, and explicit Sowers relative-cost multiplier can change")
    scenario.update(overrides or {})
    rate = scenario["discount_rate"]
    price = scenario["sale_price_per_kg"]
    multiplier = scenario["cost_multiplier_sowers"]
    if not math.isfinite(rate) or rate < 0:
        raise ValueError("rate must be finite and nonnegative")
    if not math.isfinite(price) or price < 0 or not math.isfinite(multiplier) or multiplier <= 0:
        raise ValueError("Invalid price or cost multiplier")
    quantity, years = scenario["annual_sale_quantity_kg"], scenario["operating_years"]
    annuity = math.fsum((1 + rate) ** -t for t in range(1, years + 1))
    source = json.loads((ROOT / "models/sowers_niac2020/original_inputs.json").read_text(encoding="utf-8"))
    source["case"] = "commercial"
    selected = load_model("sowers_niac2020").run(source)["selected_case"]
    costs = {key: value * multiplier for key, value in selected["costs_usd"].items()}
    opex = selected["operations_usd_year"] * multiplier
    minimum_cost, maximum_cost, endpoints = cost_pv_bounds(
        costs, scenario["sowers_cost_windows_relative_to_commissioning"], rate)
    operating_pv = (quantity * price - opex) * annuity
    low, high = operating_pv - maximum_cost, operating_pv - minimum_cost
    k = load_model("kornuta2019").run({
        "discount_rate": rate, "mine_life_years": years,
        "scenario_overrides": {"1": {"annual_sale_quantity_kg": quantity,
                                      "sale_price_usd_per_kg": price}}
    })
    ks = k["scenarios"]["1"]
    k_npv = ks["native_npv_usd"]
    status = "all_admissible_schedules_negative" if high < 0 else (
        "all_admissible_schedules_nonnegative" if low >= 0 else "sign_depends_on_schedule")
    return {
        "status": scenario["status"], "scenario": scenario,
        "kornuta_modified_surface_offtake": {
            "npv_source_currency": k_npv,
            "break_even_surface_price": (k["initial_investment_usd"] / annuity + k["annual_cost_usd"]) / quantity,
            "historical_reproduction": False,
        },
        "sowers_partial_identification": {
            "npv_lower": low, "npv_upper": high, "sign_classification": status,
            "break_even_surface_price_lower": (minimum_cost / annuity + opex) / quantity,
            "break_even_surface_price_upper": (maximum_cost / annuity + opex) / quantity,
            "cost_pv_lower": minimum_cost, "cost_pv_upper": maximum_cost,
            "cost_endpoints": endpoints,
            "bound_scope": "All nonnegative cost allocations inside declared annual windows, conditional on fixed source totals and no other cash flows",
            "historical_irr_reproduction": False,
        },
        "conditional_difference_sowers_minus_kornuta": [low - k_npv, high - k_npv],
        "strict_physical_and_currency_comparability_gate": False,
        "interpretation": "Conditional financial comparison only. Missing currency normalization and product equivalence prevent a fully harmonized historical-model ranking.",
    }


def sweep():
    scenario = json.loads(Path(__file__).with_name("scenario.json").read_text(encoding="utf-8"))
    rows = []
    for rate, price, multiplier in itertools.product(
        scenario["sensitivity_rates"], scenario["sensitivity_prices"],
        scenario["sensitivity_relative_cost_multipliers"]
    ):
        result = run({"discount_rate": rate, "sale_price_per_kg": price,
                      "cost_multiplier_sowers": multiplier})
        s = result["sowers_partial_identification"]
        k = result["kornuta_modified_surface_offtake"]
        rows.append({"rate": rate, "price": price, "relative_cost_multiplier_sowers": multiplier,
                     "kornuta_npv": k["npv_source_currency"],
                     "sowers_npv_lower": s["npv_lower"], "sowers_npv_upper": s["npv_upper"],
                     "sowers_sign": s["sign_classification"],
                     "kornuta_break_even_price": k["break_even_surface_price"],
                     "sowers_break_even_price_lower": s["break_even_surface_price_lower"],
                     "sowers_break_even_price_upper": s["break_even_surface_price_upper"]})
    return rows


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
