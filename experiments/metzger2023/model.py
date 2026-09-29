"""Executable Metzger arXiv v1 equations; conditional, not Table 1 replication.

Standard library only. All default data and interpretation choices are external.
The default output is lunar-surface LRAC, preserving the source metric. No NPV
or historical source-model identity is imposed on this analytical sector model.
"""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path


def annuity_pv(rate, years):
    return sum((1 + rate) ** -t for t in range(1, years + 1))


def gear_ratio(delta_v_out, delta_v_return, isp, inert_fraction, gravity=9.8):
    """Equations 2-3, retaining the paper's definition of inert fraction."""
    if min(delta_v_out, delta_v_return, inert_fraction) < 0 or isp <= 0 or gravity <= 0:
        raise ValueError("Invalid transport input")
    effective = inert_fraction * math.exp(delta_v_return / (gravity * isp))
    delivered = (1 + effective) * math.exp(-delta_v_out / (gravity * isp)) - effective
    if delivered <= 0:
        raise ValueError("No positive delivered payload under equations 2-3")
    return 1 / delivered


def launch_cost(t, p, market_fraction=1.0):
    """Equations 17-18, exact integral of exponential up-mass."""
    if market_fraction <= 0:
        raise ValueError("market_fraction must be positive")
    growth = math.log(p["launch_final_kg_per_year"] * market_fraction /
                      p["launch_initial_kg_per_year"]) / p["projection_years"]
    cumulative = p["launch_initial_kg_per_year"] * (
        math.expm1(growth * t) / growth if growth else t)
    return p["launch_initial_usd_per_kg"] * math.exp(growth * t * (
        p["launch_scale_exponent"] - 1)) * (1 + cumulative / p["launch_prior_kg"]) ** math.log2(
            p["launch_learning_ratio"])


def reliability_factor(reliability, p):
    exponent = (1 - p["reliability_effort"]) * (
        reliability - p["reliability_baseline"]) / (1 - reliability)
    return math.exp(exponent) if exponent < 700 else math.inf


def optimize_reliability(development_rate, fabrication_rate, transport_rate, p):
    """Bounded minimization of Eq.12, with separately named literal/prose forms."""
    replacement_rate = (development_rate if p["reliability_equation"] ==
                        "printed_development" else fabrication_rate)

    def objective(r):
        return ((development_rate + replacement_rate / r) * reliability_factor(r, p)
                + transport_rate / r)

    left, right = 1e-6, 1 - 1e-6
    golden = (math.sqrt(5) - 1) / 2
    x1, x2 = right - golden * (right - left), left + golden * (right - left)
    f1, f2 = objective(x1), objective(x2)
    for _ in range(120):
        if f1 > f2:
            left, x1, f1 = x1, x2, f2
            x2 = left + golden * (right - left)
            f2 = objective(x2)
        else:
            right, x2, f2 = x2, x1, f1
            x1 = right - golden * (right - left)
            f1 = objective(x1)
    r = (left + right) / 2
    return r, replacement_rate, objective(r)


def point(t, p, market_fraction=1.0):
    """One industry-date snapshot, with a separate project financing calculation."""
    launch = launch_cost(t, p, market_fraction)
    growth = math.log(p["lunar_final_kg_per_year"] * market_fraction /
                      p["annual_product_kg"]) / p["projection_years"]
    scale = math.exp(t * growth)
    cumulative_ratio = 1 + (math.expm1(t * growth) / growth if growth else t) / p["lunar_prior_output_years"]
    learning = cumulative_ratio ** math.log2(p["lunar_learning_ratio"])
    metals_ratio = 0.3 * min(1, max(0, (t - 10) / 5))
    firm_scale = scale if p["firm_scale_limit_kg_per_year"] is None else min(
        scale, p["firm_scale_limit_kg_per_year"] / p["annual_product_kg"])
    scope = 1 - p["firm_scope_fraction"] * metals_ratio
    exponent = p["lunar_scale_exponent"] - 1
    equipment_scaling = ((scale * (1 + p["scope_overlap"] * metals_ratio)) ** (exponent / 2)
                         * firm_scale ** (exponent / 2) * scope * learning)
    labor_scaling = firm_scale ** exponent * scope * learning
    development = p["development_usd_per_kg"] * (equipment_scaling if p["scale_development"] else 1)
    fabrication = p["fabrication_usd_per_kg"] * equipment_scaling
    transportation = launch * p["capital_delivery_gear"]
    reliability, replacement_rate, _ = optimize_reliability(development, fabrication, transportation, p)
    equipment_mass = p["surface_capital_kg"] + p["space_capital_kg"]
    capital_cost = (development + replacement_rate / reliability) * reliability_factor(reliability, p) * equipment_mass
    transport_cost = transportation * equipment_mass / reliability
    annual_ops = p["annual_operations_usd"] * labor_scaling
    rate = p["discount_initial"] + (p["discount_final"] - p["discount_initial"]) * t / p["projection_years"]
    buildup, life = p["buildup_years"], p["operating_years"]
    # End-of-year uniform construction expenditure accumulated to commissioning.
    future_factor = sum((1 + rate) ** t for t in range(buildup))
    construction_labor = buildup * annual_ops
    debt = (capital_cost / buildup + annual_ops) * future_factor + transport_cost
    annual_debt_service = debt / annuity_pv(rate, life)
    price = (annual_debt_service + annual_ops) / p["annual_product_kg"]
    lifetime_output = p["annual_product_kg"] * life
    finance_interest = annual_debt_service * life - capital_cost - transport_cost - construction_labor
    components = {
        "equipment_usd_per_kg_product": capital_cost / lifetime_output,
        "capital_transport_usd_per_kg_product": transport_cost / lifetime_output,
        "labor_including_buildup_usd_per_kg_product": annual_ops * (life + buildup) / lifetime_output,
        "interest_usd_per_kg_product": finance_interest / lifetime_output,
    }
    return {
        "elapsed_industry_year": t, "market_fraction": market_fraction,
        "launch_usd_per_kg": launch, "industry_output_kg_per_year": p["annual_product_kg"] * scale,
        "learning_factor": learning, "equipment_scaling_factor": equipment_scaling,
        "labor_scaling_factor": labor_scaling, "optimal_reliability": reliability,
        "annual_discount_rate": rate, "capital_cost_usd": capital_cost,
        "capital_transport_cost_usd": transport_cost, "debt_at_commissioning_usd": debt,
        "surface_lrac_usd_per_kg": price,
        "earth_surface_usd_per_kg": launch * p["earth_surface_delivery_gear"],
        "surface_lunar_to_earth_cost_ratio": price / (launch * p["earth_surface_delivery_gear"]),
        "pre_delivery_cost_ratio": price / launch,
        "production_mass_ratio": lifetime_output / equipment_mass,
        "cost_components": components,
    }


def run(overrides=None):
    document = json.loads(Path(__file__).with_name("inputs.json").read_text(encoding="utf-8"))
    p = copy.deepcopy(document["parameters"])
    overrides = overrides or {}
    if set(overrides) - set(p):
        raise ValueError(f"Unknown parameters: {sorted(set(overrides) - set(p))}")
    p.update(overrides)
    if p["reliability_equation"] not in {"prose_fabrication", "printed_development"}:
        raise ValueError("Unknown reliability equation")
    for key, value in p.items():
        if value is not None and not isinstance(value, (str, bool)) and (not math.isfinite(value) or value <= 0):
            # Zero financing and zero G are useful controlled limits.
            if value != 0 or key not in {"discount_initial", "discount_final", "capital_delivery_gear",
                                        "space_capital_kg", "development_usd_per_kg", "fabrication_usd_per_kg",
                                        "annual_operations_usd", "scope_overlap", "firm_scope_fraction"}:
                raise ValueError(f"Invalid parameter: {key}")
    if type(p["scale_development"]) is not bool:
        raise ValueError("scale_development must be a boolean")
    for key in ("buildup_years", "operating_years", "projection_years"):
        if type(p[key]) is not int:
            raise ValueError(f"{key} must be a positive integer")
    for key in ("reliability_baseline", "reliability_effort", "launch_learning_ratio", "lunar_learning_ratio"):
        if not 0 < p[key] < 1:
            raise ValueError(f"{key} must be between zero and one")
    rows = [point(t, p, fraction) for fraction in (1, 0.1, 0.01)
            for t in range(p["projection_years"] + 1)]
    return {"status": "conditional_equation_implementation_not_headline_reproduction",
            "source": document["source"], "version": document["version"],
            "cost_basis": document["cost_basis"], "parameters": p,
            "provenance": document["provenance"], "overrides": overrides,
            "native_metric": "long_run_average_cost_and_lunar_to_earth_cost_ratio",
            "table_1_full_orbital_crossing_reproduction": None,
            "rows": rows}


if __name__ == "__main__":
    import sys
    override = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) > 1 else {}
    print(json.dumps(run(override), indent=2, allow_nan=False))
