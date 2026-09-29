"""Plant-cost interval from Jones 2020 Table 7, given only total plant mass.

Table 7 is linear in subsystem mass. With every listed subsystem present, the
intercepts are fixed and the uncertain split of a fixed mass puts all of that
mass on the lowest or highest slope. Excavation count and the campaign ratio
stay unresolved.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBSYSTEMS = ("structures", "tanks", "thermal", "ecls")


def _bounds(mass_kg, lifetime_months, coefficients):
    slopes = []
    fixed = 0.0
    for name in SUBSYSTEMS:
        slope, lifetime_slope, intercept = coefficients[name]
        slopes.append(slope)
        fixed += lifetime_slope * lifetime_months + intercept
    return {
        "lower": min(slopes) * mass_kg + fixed,
        "upper": max(slopes) * mass_kg + fixed,
        "fixed_if_all_subsystems_present": fixed,
    }


def run():
    source = json.loads((ROOT / "models/jones2020/original_inputs.json").read_text(encoding="utf-8"))
    parameters = source["parameters"]
    plant = parameters["plant_cer"]["value"]
    mass = 2262.7
    lifetime = parameters["isru_lifetime_years"]["value"] * 12
    development = {name: plant[name]["development"] for name in SUBSYSTEMS}
    production = {name: plant[name]["production"] for name in SUBSYSTEMS}
    return {
        "native_campaign_ratio": None,
        "plant_mass_kg": mass,
        "design_lifetime_months": lifetime,
        "mass_allocation": "unresolved; bounds assume the four Table 7 subsystems are all present and absorb the Duke Table 5 mass",
        "development_FY2019_MUSD": _bounds(mass, lifetime, development),
        "production_FY2019_MUSD": _bounds(mass, lifetime, production),
        "excavation_unit_count": None,
        "nuclear_unit_count": None,
        "blockers": [
            "Loader count is not a function of production in the paper.",
            "Table 5 mass and a 40 kWe reactor count are different power treatments.",
            "Launch, lander, and replacement events are not a closed ledger.",
        ],
    }
