"""Kornuta-family report mining-company DCF, using reported annual cash flows.

run({}) loads original_inputs.json. The input dictionary contains only the
documented overrides, not a second parameter document. All currency outputs
are source dollars; their price year and real/nominal convention are unresolved.
"""

import copy
import json
import math
from pathlib import Path


GLOBAL_OVERRIDES = {
    "discount_rate", "mine_life_years", "initial_investment_usd",
    "annual_cost_usd", "scenario_overrides",
}
SCENARIO_OVERRIDES = {
    "annual_sale_quantity_kg", "sale_price_usd_per_kg", "annual_revenue_usd",
}


def _number(value, name, minimum=0.0):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    if not math.isfinite(value) or value < minimum:
        raise ValueError(f"{name} must be finite and >= {minimum}")
    return float(value)


def run(inputs: dict) -> dict:
    """Calculate all seven scenarios with explicit, bounded override support.

    Global overrides: discount_rate (fraction, >= 0), mine_life_years (positive
    integer), initial_investment_usd, annual_cost_usd. Scenario overrides are
    keyed by source scenario IDs '1' ... '7', and support quantity, price, or
    revenue. Overriding quantity alone retains the source revenue/quantity
    ratio, avoiding the published rounded average price. Overriding price
    calculates revenue = quantity * price. A revenue override cannot be
    combined with a price override. No cost or equipment scaling is implied.
    """
    if not isinstance(inputs, dict):
        raise TypeError("inputs must be an override dictionary")
    unknown = set(inputs) - GLOBAL_OVERRIDES
    if unknown:
        raise ValueError(f"Unsupported override fields: {sorted(unknown)}")
    source = json.loads(Path(__file__).with_name("original_inputs.json").read_text(encoding="utf-8"))
    parameters = source["parameters"]

    def parameter(name):
        return inputs.get(name, parameters[name]["value"])

    rate = _number(parameter("discount_rate"), "discount_rate")
    years = parameter("mine_life_years")
    if isinstance(years, bool) or not isinstance(years, int) or years < 1:
        raise ValueError("mine_life_years must be a positive integer")
    capital = _number(parameter("initial_investment_usd"), "initial_investment_usd")
    annual_cost = _number(parameter("annual_cost_usd"), "annual_cost_usd")
    scenario_overrides = inputs.get("scenario_overrides", {})
    if not isinstance(scenario_overrides, dict):
        raise ValueError("scenario_overrides must be a dictionary keyed by source scenario ID")
    unknown_ids = set(scenario_overrides) - set(source["scenarios"])
    if unknown_ids:
        raise ValueError(f"Unknown scenario IDs: {sorted(unknown_ids)}")

    discount_factors = [(1.0 + rate) ** -year for year in range(1, years + 1)]
    annuity_factor = math.fsum(discount_factors)
    source_annuity_factor = math.fsum(
        (1.0 + parameters["discount_rate"]["value"]) ** -year
        for year in range(1, parameters["mine_life_years"]["value"] + 1)
    )
    results = {}
    for scenario_id, scenario in source["scenarios"].items():
        overrides = scenario_overrides.get(scenario_id, {})
        if not isinstance(overrides, dict):
            raise ValueError(f"Scenario {scenario_id} overrides must be a dictionary")
        unknown = set(overrides) - SCENARIO_OVERRIDES
        if unknown:
            raise ValueError(f"Unsupported scenario override fields: {sorted(unknown)}")
        if "annual_revenue_usd" in overrides and "sale_price_usd_per_kg" in overrides:
            raise ValueError("Override revenue or price, not both")
        original_quantity = scenario["annual_sale_quantity_kg"]["value"]
        original_revenue = scenario["annual_revenue_usd"]["value"]
        quantity = _number(overrides.get("annual_sale_quantity_kg", original_quantity), "annual_sale_quantity_kg")
        source_implied_price = original_revenue / original_quantity
        if "annual_revenue_usd" in overrides:
            revenue = _number(overrides["annual_revenue_usd"], "annual_revenue_usd")
            revenue_basis = "explicit_analyst_revenue_override"
        elif "sale_price_usd_per_kg" in overrides or "annual_sale_quantity_kg" in overrides:
            price = _number(overrides.get("sale_price_usd_per_kg", source_implied_price), "sale_price_usd_per_kg")
            revenue = quantity * price
            revenue_basis = "quantity_times_price_override_no_cost_scaling"
        else:
            revenue = original_revenue
            revenue_basis = "reported_table_14_annual_revenue"
        if quantity == 0 and revenue != 0:
            raise ValueError("Positive sale revenue requires positive annual sale quantity")
        annual_net_cash_flow = revenue - annual_cost
        npv = -capital + annual_net_cash_flow * annuity_factor
        reported_npv = scenario["reported_npv_usd"]["value"]
        difference = npv - reported_npv
        original_case = not any(key != "scenario_overrides" for key in inputs) and not overrides
        source_price_quantity_revenue = original_quantity * scenario["printed_average_price_usd_per_kg"]["value"]
        source_price_quantity_npv = -parameters["initial_investment_usd"]["value"] + (source_price_quantity_revenue - parameters["annual_cost_usd"]["value"]) * source_annuity_factor
        results[scenario_id] = {
            "customers": scenario["customers"],
            "annual_sale_quantity_kg_at_lunar_surface": quantity,
            "annual_revenue_usd": revenue,
            "annual_cost_usd": annual_cost,
            "annual_net_cash_flow_usd": annual_net_cash_flow,
            "revenue_basis": revenue_basis,
            "source_printed_average_price_usd_per_kg": scenario["printed_average_price_usd_per_kg"]["value"],
            "source_rounding_diagnostic": {
                "basis": "historical_parameters_quantity_times_printed_price_not_primary_revenue_path",
                "annual_revenue_usd": source_price_quantity_revenue,
                "npv_usd": source_price_quantity_npv,
                "difference_from_reported_npv_usd": source_price_quantity_npv - reported_npv,
            },
            "effective_average_sale_price_usd_per_kg": revenue / quantity if quantity else None,
            "native_npv_usd": npv,
            "reported_npv_usd": reported_npv,
            "difference_from_reported_npv_usd": difference,
            "absolute_difference_from_reported_npv_usd": abs(difference),
            "relative_absolute_difference_percent": 100 * abs(difference) / abs(reported_npv),
            "original_case_comparison": original_case,
            "comparison_status": "historical_reconstruction" if original_case else "modified_scenario_not_reproduction_error",
            "nonnegative_npv": npv >= 0,
            "minimum_time_zero_subsidy_usd": max(0.0, -npv),
            "derived_break_even_average_surface_price_usd_per_kg": (capital / annuity_factor + annual_cost) / quantity if quantity else None,
            "break_even_price_status": "separate_derived_constant_quantity_metric_not_native_reported_result",
            "cash_flows_usd": [-capital] + [annual_net_cash_flow] * years,
            "discounted_cash_flows_usd": [-capital] + [annual_net_cash_flow * factor for factor in discount_factors],
            "source_provenance": copy.deepcopy(scenario),
            "overrides": copy.deepcopy(overrides),
        }

    component_cost = parameters["operations_cost_usd_per_year"]["value"] + parameters["replacement_mass_kg_per_year"]["value"] * (parameters["hardware_cost_usd_per_kg"]["value"] + parameters["lunar_delivery_cost_usd_per_kg"]["value"])
    return {
        "model_id": source["model_id"],
        "implementation_scope": "constant_annual_cash_flow_reconstruction_of_2018_report_in_2019_model_family",
        "native_metric": "mining_company_npv_usd",
        "currency_convention": source["currency_convention"],
        "discount_rate": rate,
        "mine_life_years": years,
        "initial_investment_usd": capital,
        "annuity_present_value_factor": annuity_factor,
        "annual_cost_usd": annual_cost,
        "source_component_cost_diagnostic_usd_per_year": component_cost,
        "source_reported_minus_component_cost_usd_per_year": parameters["annual_cost_usd"]["value"] - component_cost,
        "supported_overrides": {"global": sorted(GLOBAL_OVERRIDES), "per_scenario": sorted(SCENARIO_OVERRIDES)},
        "unsupported_fields": source["unsupported_fields"],
        "parameter_provenance": parameters,
        "sources": source["sources"],
        "override_provenance": {"classification": "analyst_supplied_override_not_historical_source", "values": copy.deepcopy(inputs)},
        "scenarios": results,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        raise SystemExit("Usage: python model.py [overrides.json]")
    overrides = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) == 2 else {}
    print(json.dumps(run(overrides), indent=2, allow_nan=False))
