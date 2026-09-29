"""Partial, provenance-preserving reconstruction of Jones et al. (2020).

Only Python's standard library is used. The published sizing/CER equations are
executable; the unpublished logistics schedule is an explicit required input.
Missing data produce null native economics, never a fitted or zero-cost answer.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


def _values(inputs: dict) -> dict:
    """Accept a provenance document or a flat dictionary of parameter values."""
    source = inputs.get("parameters", inputs)
    values = {
        key: copy.deepcopy(item["value"] if isinstance(item, dict) and "value" in item else item)
        for key, item in source.items()
    }
    for key, item in inputs.get("overrides", {}).items():
        if key not in values:
            raise ValueError(f"Unknown override: {key}")
        values[key] = copy.deepcopy(item["value"] if isinstance(item, dict) and "value" in item else item)
    return values


def _number(value, name: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    if not math.isfinite(value) or value < minimum:
        raise ValueError(f"{name} must be finite and >= {minimum}")
    return float(value)


def lander_cost(inert_mass_kg: float, parameters: dict) -> dict:
    """Equation 1 / Table 6. Mass is kg and cost is FY2019 million USD."""
    mass = _number(inert_mass_kg, "inert_mass_kg", 1e-12)
    branch = "le_threshold" if mass <= parameters["lander_cer_threshold_kg"] else "gt_threshold"
    out = {}
    for cost_type in ("development", "production"):
        a, b, c, d = parameters["lander_cer"][branch][cost_type]
        cost = ((a * mass + b) * mass + c) * mass + d
        if cost < 0:
            raise ValueError("Lander CER gives negative cost: outside a usable fit domain")
        out[cost_type + "_FY2019_MUSD"] = cost
    out["branch"] = branch
    return out


def plant_cost(subsystem_masses_kg: dict, design_lifetime_months: float,
               excavation_units: int, nuclear_units: int, parameters: dict) -> dict:
    """Table 7. No allocation of total plant mass to subsystems is invented."""
    lifetime = _number(design_lifetime_months, "design_lifetime_months", 1e-12)
    for name, count in (("excavation_units", excavation_units), ("nuclear_units", nuclear_units)):
        _number(count, name)
        if int(count) != count:
            raise ValueError(f"{name} must be an integer")
    by_subsystem = {}
    for subsystem in ("structures", "tanks", "thermal", "ecls"):
        mass = _number(subsystem_masses_kg[subsystem], subsystem + " mass", 1e-12)
        by_subsystem[subsystem] = {}
        for kind in ("development", "production"):
            mass_slope, lifetime_slope, intercept = parameters["plant_cer"][subsystem][kind]
            by_subsystem[subsystem][kind] = mass_slope * mass + lifetime_slope * lifetime + intercept
    for subsystem, count in (("excavation", excavation_units), ("nuclear", nuclear_units)):
        cer = parameters["plant_cer"][subsystem]
        by_subsystem[subsystem] = {
            "development": cer["development_fixed"] if count else 0.0,
            "production": cer["production_per_unit"] * count,
        }
    return {
        "development_FY2019_MUSD": sum(x["development"] for x in by_subsystem.values()),
        "production_FY2019_MUSD": sum(x["production"] for x in by_subsystem.values()),
        "components_FY2019_MUSD": by_subsystem,
    }


def _size(gross_rate_tpy: float, p: dict) -> dict:
    """Table 5 linear integrated-system sizing; power mass is diagnostic only."""
    rate = _number(gross_rate_tpy, "gross_rate_tpy")
    model = p["isru_models"][p["selected_isru_model"]]
    mass = rate * model["specific_mass_t_per_tpy"] * p["kg_per_tonne"]
    power = rate * model["specific_power_kwe_per_tpy"]
    continuous_power_mass = power * p["nuclear_specific_mass_kg_per_kwe"]
    power_units = math.ceil(power / p["nuclear_unit_power_kwe"]) if power else 0
    capacity = p.get("lander_surface_payload_capacity_kg")
    result = {
        "gross_propellant_production_tpy": rate,
        "table5_linear_mass_kg": mass,
        "required_power_kwe": power,
        "diagnostic_power_mass_continuous_kg": continuous_power_mass,
        "diagnostic_power_unit_ceiling": power_units,
        "diagnostic_power_mass_if_whole_units_kg": (
            power_units * p["nuclear_unit_power_kwe"] * p["nuclear_specific_mass_kg_per_kwe"]
        ),
        "power_mass_added_to_table5_mass": False,
        "plant_count_from_supplied_capacity": None,
        "equal_plant_rate_tpy": None,
    }
    if capacity is not None:
        capacity = _number(capacity, "lander_surface_payload_capacity_kg", 1e-12)
        count = math.ceil(mass / capacity) if mass else 0
        result["plant_count_from_supplied_capacity"] = count
        result["equal_plant_rate_tpy"] = rate / count if count else 0.0
        result["plant_count_status"] = "conditional: Table 5 mass boundary and equal allocation require confirmation"
    return result


def _cost_events(events: list, p: dict, total_years: float) -> list:
    """Cost an externally specified schedule; this does not generate logistics.

    Event keys: architecture ('isru'/'earth'), time_year, kind, quantity.
    launch: launch_vehicle; lander_*: inert_mass_kg; plant_*:
    subsystem_masses_kg, design_lifetime_months, excavation_units, nuclear_units.
    Explicit development events prevent silently charging each replacement DDT&E.
    """
    records = []
    for event in events:
        architecture = event["architecture"]
        if architecture not in ("isru", "earth"):
            raise ValueError("architecture must be isru or earth")
        when = _number(event["time_year"], "event time_year")
        if when > total_years:
            raise ValueError("Cost event is beyond campaign end")
        quantity = _number(event["quantity"], "event quantity")
        if int(quantity) != quantity:
            raise ValueError("Hardware/launch event quantities must be integers")
        kind = event["kind"]
        if kind == "launch":
            unit_cost = p["launch_vehicles"][event["launch_vehicle"]]["cost_FY2019_MUSD"]
        elif kind in ("lander_development", "lander_production"):
            cost_type = kind.removeprefix("lander_")
            unit_cost = lander_cost(event["inert_mass_kg"], p)[cost_type + "_FY2019_MUSD"]
        elif kind in ("plant_development", "plant_production"):
            cost_type = kind.removeprefix("plant_")
            unit_cost = plant_cost(
                event["subsystem_masses_kg"], event["design_lifetime_months"],
                event["excavation_units"], event["nuclear_units"], p,
            )[cost_type + "_FY2019_MUSD"]
        else:
            raise ValueError(f"Unsupported event kind: {kind}; no arbitrary cost fallbacks")
        records.append({
            "architecture": architecture, "time_year": when, "kind": kind,
            "quantity": quantity, "unit_cost_FY2019_MUSD": unit_cost,
            "cost_FY2019_MUSD": quantity * unit_cost,
            "provenance": event.get("provenance", "caller-supplied schedule; not source-verified"),
        })
    return sorted(records, key=lambda e: e["time_year"])


def run(inputs: dict) -> dict:
    """Return published intermediates and native cumulative cost ratio if known.

    Supply original_inputs.json directly. A flat dictionary must contain the same
    complete parameter set. The function does not read files, mutate inputs,
    tune coefficients, discount costs, or substitute assumptions from 2019.
    """
    p = _values(inputs)
    if p["selected_isru_model"] not in p["isru_models"]:
        raise ValueError("Unknown ISRU model")
    if p["included_annual_operations_cost"] or p["included_spare_fabrication_cost"]:
        raise ValueError("Those costs are excluded by the native 2020 model")
    if p["propellant_loss_fraction"] != 0:
        raise ValueError("Nonzero propellant losses need a non-native model extension")
    pre = _number(p["pre_transition_years"], "pre_transition_years")
    post = _number(p["post_transition_years"], "post_transition_years")
    lifetime = _number(p["isru_lifetime_years"], "isru_lifetime_years", 1e-12)
    phases = []
    blockers = []
    for phase, duration in (("pre", pre), ("post", post)):
        surface = _number(p[phase + "_surface_demand_tpy"], phase + " surface demand")
        cislunar = _number(p[phase + "_cislunar_demand_tpy"], phase + " cislunar demand")
        multiplier = p.get("gross_production_per_cislunar_delivery")
        gross = surface if cislunar == 0 else None
        if cislunar and multiplier is not None:
            multiplier = _number(multiplier, "gross_production_per_cislunar_delivery", 1.0)
            gross = surface + cislunar * multiplier
        phases.append({
            "phase": phase, "duration_years": duration,
            "surface_demand_tpy": surface, "cislunar_demand_tpy": cislunar,
            "surface_demand_total_t": surface * duration,
            "cislunar_demand_total_t": cislunar * duration,
            "demand_only_sizing": _size(gross, p) if gross is not None else None,
            "sizing_scope": "customer demand only; logistics/spares delivery propellant unresolved",
        })
    if any(x["demand_only_sizing"] is None for x in phases):
        blockers.append("Cislunar delivery burn/return/refuel calculation is not specified; gross production unknown.")
    if p.get("lander_inert_mass_kg") is None:
        blockers.append("Lander inert mass cannot be derived from IMF without the missing sizing/trajectory convention.")
    if p.get("plant_subsystem_masses_kg") is None:
        blockers.append("Structures, tanks, thermal, and ECLS masses are missing; Table 7 cannot cost a full plant.")
    if p.get("excavation_unit_count_per_plant") is None:
        blockers.append("Front-end loader/hauler count and its production-rate scaling are unresolved.")
    if p.get("table5_mass_includes_power") is None:
        blockers.append("Table 5 mass boundary versus discrete 40-kWe power units is not fully specified.")
    events = p.get("native_cost_events")
    if events is None:
        blockers.append("Native launch, deployment, expansion, spare-delivery and replacement event ledger is unavailable.")
    elif not p.get("event_ledger_complete"):
        blockers.append("Caller-supplied event ledger is not declared complete; native economics withheld.")
    results = {
        "model_id": "jones2020", "reconstruction_status": "partial_unresolved",
        "cost_basis": "FY2019 million USD, undiscounted campaign totals",
        "native_metric": "cumulative ISRU architecture cost / cumulative Earth-delivery architecture cost",
        "campaign_duration_years": pre + post,
        "isru_design_lifetime_months": lifetime * p["months_per_year"],
        "selected_isru_model": p["selected_isru_model"],
        "selected_launch_vehicle": p["selected_launch_vehicle"],
        "selected_imf": p["lander_imf"],
        "override_keys": list(inputs.get("overrides", {})),
        "MREE_to_Duke_specific_mass_ratio": (
            p["isru_models"]["MREE"]["specific_mass_t_per_tpy"]
            / p["isru_models"]["Duke"]["specific_mass_t_per_tpy"]
        ),
        "phases": phases,
        "lander_cost": None,
        "plant_cost": None,
        "cost_events": None,
        "cumulative_cost_history": None,
        "isru_total_cost_FY2019_MUSD": None,
        "earth_total_cost_FY2019_MUSD": None,
        "cumulative_cost_ratio": None,
        "breakeven_at_campaign_end": None,
        "first_breakeven_time_year": None,
        "blockers": blockers,
        "reported_output_comparison": {
            "status": "unresolved", "absolute_error": None, "relative_error": None,
            "reason": "No source numeric cost-ratio target has been digitized and native logistics are incomplete.",
        },
    }
    if p.get("lander_inert_mass_kg") is not None:
        results["lander_cost"] = lander_cost(p["lander_inert_mass_kg"], p)
    if (p.get("plant_subsystem_masses_kg") is not None
            and p.get("excavation_unit_count_per_plant") is not None
            and p.get("nuclear_unit_count_per_plant") is not None):
        results["plant_cost"] = plant_cost(
            p["plant_subsystem_masses_kg"], results["isru_design_lifetime_months"],
            p["excavation_unit_count_per_plant"], p["nuclear_unit_count_per_plant"], p,
        )
    if events is not None:
        records = _cost_events(events, p, pre + post)
        results["cost_events"] = records
        if p.get("event_ledger_complete"):
            cumulative = {"isru": 0.0, "earth": 0.0}
            history = []
            for when in sorted({event["time_year"] for event in records}):
                for event in records:
                    if event["time_year"] == when:
                        cumulative[event["architecture"]] += event["cost_FY2019_MUSD"]
                ratio = cumulative["isru"] / cumulative["earth"] if cumulative["earth"] else None
                history.append({"time_year": when, "isru_FY2019_MUSD": cumulative["isru"],
                                "earth_FY2019_MUSD": cumulative["earth"], "cost_ratio": ratio})
            if cumulative["earth"] <= 0:
                raise ValueError("Complete ledger needs positive Earth-delivery architecture cost")
            ratio = cumulative["isru"] / cumulative["earth"]
            results.update({
                "reconstruction_status": "conditional_caller_supplied_logistics",
                "cumulative_cost_history": history,
                "isru_total_cost_FY2019_MUSD": cumulative["isru"],
                "earth_total_cost_FY2019_MUSD": cumulative["earth"],
                "cumulative_cost_ratio": ratio,
                "breakeven_at_campaign_end": ratio < 1.0,
                "first_breakeven_time_year": next((x["time_year"] for x in history
                    if x["cost_ratio"] is not None and x["cost_ratio"] < 1.0), None),
            })
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="?", type=Path,
                        default=Path(__file__).with_name("original_inputs.json"))
    args = parser.parse_args()
    print(json.dumps(run(json.loads(args.inputs.read_text(encoding="utf-8"))), indent=2, allow_nan=False))
