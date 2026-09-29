"""Sowers February-2020 NIAC thermal-mining business-case reconstruction.

Pure standard library. ``run(document)`` accepts original_inputs.json directly.
Select a case/variant/timing with document['case'], ['variant'], ['timing'];
optional document['overrides'] replaces selected economic parameters.
No annual source cash-flow data were published: default IRR is unresolved.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


def _error(actual: float, reported: float) -> dict:
    return {
        "calculated": actual,
        "reported": reported,
        "difference": actual - reported,
        "relative_error_percent": 100 * (actual - reported) / reported if reported else None,
    }


def _npv(cash: list[float], rate: float) -> float:
    if rate <= -1:
        raise ValueError("discount rate must exceed -1")
    return sum(value / (1 + rate) ** period for period, value in enumerate(cash))


def _irr(cash: list[float]) -> tuple[float | None, str]:
    # A single sign change implies one economically meaningful root, if it exists.
    nonzero = [value for value in cash if value != 0]
    changes = sum(a * b < 0 for a, b in zip(nonzero, nonzero[1:]))
    if changes != 1:
        return None, "IRR not selected: cash flow does not have exactly one sign change"
    low, high = -0.9, 1.0
    left, right = _npv(cash, low), _npv(cash, high)
    while left * right > 0 and high < 1e6:
        high = 2 * high + 1
        right = _npv(cash, high)
    if left * right > 0:
        return None, "No IRR bracket found over -90% through the numerical upper bound"
    for _ in range(160):
        middle = (low + high) / 2
        center = _npv(cash, middle)
        if left * center <= 0:
            high = middle
        else:
            low, left = middle, center
    return (low + high) / 2, "unique root for this explicitly specified cash-flow schedule"


def _allocate(total: float, weights: list[float], periods: int) -> list[float]:
    if len(weights) > periods or any(w < 0 for w in weights):
        raise ValueError("cost/payment weights must be nonnegative and fit the horizon")
    if not math.isclose(sum(weights), 1.0, abs_tol=1e-10):
        raise ValueError("cost/payment weights must sum to one")
    return [total * (weights[i] if i < len(weights) else 0) for i in range(periods)]


def run(inputs: dict) -> dict:
    """Return source-native static economics and, only if selected, timed cash flows.

    All monetary outputs carry explicit units. Default revenue_mode='printed_table'
    deliberately retains the source's inconsistent Mars revenue. Alternatives are
    listed in the input artifact. Overrides never change source-reported records.
    """
    case_key = inputs.get("case", "commercial")
    variant_key = inputs.get("variant", "reported_table")
    case = copy.deepcopy(inputs["cases"][case_key])
    variant = inputs["variants"][variant_key]
    params = copy.deepcopy(inputs["parameters"])
    params.update(case["parameters"])
    params.update(variant.get("overrides", {}))
    params.update(inputs.get("overrides", {}))
    for key in ("operating_years", "plant_mass_kg", "surface_price_usd_per_kg"):
        if params[key] <= 0:
            raise ValueError(f"{key} must be positive")
    if int(params["operating_years"]) != params["operating_years"]:
        raise ValueError("operating_years must be a whole number")

    development = []
    for row in inputs["development_subsystems"]:
        cost = row.get("fixed_cost_usd", row["unit_mass_kg"] * row["cost_usd_per_kg"])
        development.append({"name": row["name"], "cost_usd": cost})
    development_total = sum(row["cost_usd"] for row in development)

    production = []
    slope = params["learning_curve_ratio"]
    if not 0 < slope <= 1:
        raise ValueError("learning_curve_ratio must be in (0, 1]")
    exponent = math.log2(slope)
    for row in inputs["production_subsystems"]:
        first = row.get("fixed_first_unit_cost_usd", row["unit_mass_kg"] * row["cost_usd_per_kg"])
        cost = first * sum(unit ** exponent for unit in range(1, row["units"] + 1))
        production.append({"name": row["name"], "first_unit_cost_usd": first,
                           "units": row["units"], "cost_usd": cost,
                           "printed_total_comparison_usd": _error(cost, row["reported_total_usd"])})
    production_total = sum(row["cost_usd"] for row in production)
    launch = inputs["launch"]
    single = launch["single_capacity_kg"] * launch["surface_cost_usd_per_kg"]
    dual = 2 * single * (1 + launch["dual_launch_premium_fraction"])
    deployment = single * launch["fully_charged_single_launches"] + dual * (
        launch["fully_charged_dual_launches"] + launch["shared_dual_mining_payload_kg"] / launch["dual_capacity_kg"])
    base_operations = params["plant_mass_kg"] * params["operations_usd_per_kg_year"]

    segments = copy.deepcopy(case["demand_segments"])
    demand_multiplier = params.get("demand_multiplier", 1.0)
    if demand_multiplier < 0:
        raise ValueError("demand_multiplier must be nonnegative")
    for segment in segments:
        segment["surface_demand_tonnes_year"] *= demand_multiplier
    years = int(params["operating_years"])
    surface_by_year = [sum(s["surface_demand_tonnes_year"] for s in segments
                           if y >= s["first_operating_year"]) for y in range(1, years + 1)]
    # Installed design capacity is not reduced merely by a shorter accounting horizon.
    max_surface = sum(s["surface_demand_tonnes_year"] for s in segments)
    demand_revenue = [q * 1000 * params["surface_price_usd_per_kg"] for q in surface_by_year]
    revenue_mode = params["revenue_mode"]
    if revenue_mode == "demand_rows":
        revenue = demand_revenue
    elif revenue_mode == "printed_table":
        # Preserve the printed steady-state revenue, scaled only for explicit price changes.
        price_ratio = params["surface_price_usd_per_kg"] / case["reported"]["price_usd_per_kg"]
        plateau = params.get("annual_revenue_musd", case["reported"]["revenue_musd_year"]) * 1e6 * price_ratio * demand_multiplier
        revenue = [plateau if y >= params["full_demand_first_operating_year"] else demand_revenue[y - 1]
                   for y in range(1, years + 1)]
    else:
        raise ValueError("revenue_mode must be printed_table or demand_rows")

    mode = params["cost_mode"]
    reported = case["reported"]
    if mode == "reported_table":
        costs = {name: reported[name + "_musd"] * 1e6
                 for name in ("development", "production", "transportation")}
        annual_operations = reported["operations_musd_year"] * 1e6
        scale = None
    elif mode in ("prose_scale", "demand_ratio_scale"):
        scale = params["reported_cost_scale"] if mode == "prose_scale" else max_surface / params["base_production_tonnes_year"]
        costs = {"development": development_total * scale,
                 "production": production_total * scale,
                 "transportation": deployment + params["extra_dual_launches"] * dual}
        annual_operations = base_operations * scale
    else:
        raise ValueError("unknown cost_mode")
    multiplier = params["nonrecurring_cost_multiplier"]
    costs = {key: value * multiplier for key, value in costs.items()}
    capex = sum(costs.values())
    investment = params["nasa_investment_musd"] * 1e6
    operating_cash = [value - annual_operations for value in revenue]

    nasa = inputs["nasa_savings"]
    surface_saving = nasa["surface_propellant_tonnes_year"] * 1000 * (
        nasa["earth_surface_propellant_usd_per_kg"] - params["surface_price_usd_per_kg"])
    gateway_saving = nasa["avoided_gateway_missions_year"] * nasa["gateway_mission_cost_musd"] * 1e6
    lunar_saving = surface_saving + gateway_saving
    mars_earth_cost = (nasa["mars_hardware_tonnes_year"] + nasa["mars_propellant_tonnes_year"]) * 1000 * nasa["sls_cislunar_usd_per_kg"]
    mars_lunar_cost = (nasa["mars_hardware_tonnes_year"] * nasa["lunar_fueled_hardware_delivery_usd_per_kg"]
                       + nasa["mars_propellant_tonnes_year"] * nasa["lunar_propellant_cislunar_usd_per_kg"]) * 1000
    mars_saving_derived = mars_earth_cost - mars_lunar_cost
    mars_saving = nasa["reported_mars_incremental_savings_musd_year"] * 1e6 if params["nasa_savings_mode"] == "printed" else mars_saving_derived
    nasa_benefits = [(lunar_saving if params["has_nasa_lunar"] else 0) +
                     (mars_saving if params["has_nasa_mars"] and y >= params["mars_first_operating_year"] else 0)
                     for y in range(1, years + 1)]

    output = {
        "model_id": inputs["model_id"], "case": case_key, "variant": variant_key,
        "cost_mode": mode, "revenue_mode": revenue_mode,
        "status": "Static reconstruction; original annual phasing and IRRs unresolved",
        "reported_source_values": reported,
        "baseline_subsystem_calculations": {
            "development": development, "production": production,
            "learning_unit_cost_exponent": exponent,
            "development_total_usd": development_total, "production_total_usd": production_total,
            "single_launch_usd": single, "dual_launch_usd": dual,
            "deployment_total_usd": deployment, "operations_usd_year": base_operations,
            "capex_total_usd": development_total + production_total + deployment,
            "comparisons": {
                "development_usd": _error(development_total, 883e6),
                "production_table_4_8_7_usd": _error(production_total, 613471000),
                "launch_table_4_8_9_usd": _error(deployment, 1062e6),
                "capex_table_4_8_10_usd": _error(development_total + production_total + deployment, 2559e6),
            },
        },
        "selected_case": {
            "cost_scale_applied": scale, "costs_usd": costs, "capex_usd": capex,
            "operations_usd_year": annual_operations, "nasa_investment_usd": investment,
            "surface_demand_tonnes_by_operating_year": surface_by_year,
            "revenue_usd_by_operating_year": revenue,
            "revenue_from_demand_usd_by_operating_year": demand_revenue,
            "company_operating_cash_usd_by_operating_year": operating_cash,
            "company_lifetime_undiscounted_net_cash_usd": sum(operating_cash) - capex + investment,
            "nasa_benefit_usd_by_operating_year": nasa_benefits,
            "nasa_lifetime_undiscounted_net_savings_usd": sum(nasa_benefits) - investment,
        },
        "source_consistency": {
            "printed_scenario_label": case["printed_scenario_label"],
            "prose_scenario_label": case["prose_scenario_label"],
            "reported_scale": params["reported_cost_scale"],
            "scale_from_surface_demand": max_surface / params["base_production_tonnes_year"],
            "revenue_from_demand_vs_printed_usd_year": _error(max_surface * 1000 * params["surface_price_usd_per_kg"], reported["revenue_musd_year"] * 1e6),
            "nasa_mars_incremental_savings_derived_usd_year": mars_saving_derived,
            "nasa_mars_incremental_savings_printed_usd_year": nasa["reported_mars_incremental_savings_musd_year"] * 1e6,
        },
        "timed_cash_flow": None,
        "published_irr_reproduction": {
            "company_reported_percent": reported["irr_percent"],
            "company_calculated_percent": None, "relative_error_percent": None,
            "reason": "Source lacks numeric annual cost, payment and production phasing; no calibrated schedule is inserted.",
        },
    }
    timing_key = inputs.get("timing")
    if timing_key is not None:
        timing = copy.deepcopy(inputs["timing_alternatives"][timing_key])
        timing.update(inputs.get("timing_overrides", {}))
        start = int(timing["first_operation_period"])
        periods = start + years
        if start < 0:
            raise ValueError("first_operation_period must be nonnegative")
        dev = _allocate(costs["development"], timing["development_weights"], periods)
        prod = _allocate(costs["production"], timing["production_weights"], periods)
        transport = _allocate(costs["transportation"], timing["transportation_weights"], periods)
        nasa_payments = _allocate(investment, timing["nasa_investment_weights"], periods)
        company_cash = [nasa_payments[t] - dev[t] - prod[t] - transport[t] +
                        (operating_cash[t - start] if t >= start else 0) for t in range(periods)]
        government_cash = [-nasa_payments[t] + (nasa_benefits[t - start] if t >= start else 0)
                           for t in range(periods)]
        company_irr, irr_status = _irr(company_cash)
        government_irr, government_irr_status = _irr(government_cash)
        cumulative, government_cumulative = [], []
        for t in range(periods):
            cumulative.append(company_cash[t] + (cumulative[-1] if cumulative else 0))
            government_cumulative.append(government_cash[t] + (government_cumulative[-1] if government_cumulative else 0))
        output["timed_cash_flow"] = {
            "timing_alternative": timing_key, "timing_provenance": timing["provenance"],
            "periods": list(range(periods)), "figure_style_year_labels": list(range(1, periods + 1)),
            "company_cash_usd": company_cash, "company_cumulative_cash_usd": cumulative,
            "nasa_cash_usd": government_cash, "nasa_cumulative_cash_usd": government_cumulative,
            "company_irr_percent": company_irr * 100 if company_irr is not None else None,
            "nasa_irr_percent": government_irr * 100 if government_irr is not None else None,
            "company_irr_status": irr_status, "nasa_irr_status": government_irr_status,
            "company_irr_vs_reported_percentage_points": company_irr * 100 - reported["irr_percent"] if company_irr is not None else None,
            "validation_status": "Illustrative timing alternative; not a reproduction of unpublished cash-flow phasing",
        }
        discount_rate = inputs.get("discount_rate", params.get("discount_rate"))
        if discount_rate is not None:
            output["timed_cash_flow"]["company_npv_usd"] = _npv(company_cash, discount_rate)
            output["timed_cash_flow"]["discount_rate"] = discount_rate
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="?", type=Path, default=Path(__file__).with_name("original_inputs.json"))
    parser.add_argument("--case", choices=("commercial", "ppp_lunar", "ppp_lunar_mars"))
    parser.add_argument("--variant")
    parser.add_argument("--timing")
    args = parser.parse_args()
    document = json.loads(args.inputs.read_text(encoding="utf-8"))
    for name in ("case", "variant", "timing"):
        if getattr(args, name) is not None:
            document[name] = getattr(args, name)
    print(json.dumps(run(document), indent=2, allow_nan=False))
