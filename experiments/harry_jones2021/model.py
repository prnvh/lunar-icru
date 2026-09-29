"""Auditable experiments with ICES-2021-147. Standard library only.

python model.py writes JSON to stdout. No table output is an input to any
forward branch. This is NOT an author-validated correction of the paper.
"""
from pathlib import Path
import json
import math


def amcm(mass_kg, quantity=1.0, difficulty=0.0, inflation=1.601):
    """Eq 14 with the printed 2021 assumptions; million 2021 USD."""
    return (5.65e-4 * quantity**0.59 * (mass_kg * 2.2)**0.66
            * 80.6**2.39 * (3.81e-55)**(1 / (2040 - 1900))
            * 1**-0.36 * 1.57**difficulty * inflation)


def run(inputs=None):
    p = json.loads(Path(__file__).with_name("inputs.json").read_text(encoding="utf-8"))
    if inputs:
        unknown = set(inputs) - set(p)
        if unknown:
            raise ValueError("Unknown inputs: " + ", ".join(sorted(unknown)))
        p.update(inputs)
    if any(not math.isfinite(float(x)) or x <= 0 for x in p["rates_t_per_year"]):
        raise ValueError("Rates must be positive and finite")
    for name in ("years", "launch_musd_per_t", "operations_fraction_per_year",
                 "inflation_1999_to_2021"):
        if not math.isfinite(float(p[name])) or p[name] < 0:
            raise ValueError(name + " must be finite and nonnegative")

    results = {"status": "experimental_partial_reconstruction", "inputs": p,
               "cost_unit": "million 2021 USD", "rows": [],
               "limitations": [
                   "No authoritative correction or original worksheet obtained.",
                   "Both oxygen regimes are returned; no undocumented switching threshold imposed.",
                   "Combined and separate CER allocations are returned for literal/repaired equations.",
                   "Recycling procurement is separated because Table 1 appears to omit it.",
                   "The inferred-table branch encodes probable unit errors, not recommended economics."]}
    for r in p["rates_t_per_year"]:
        masses = {
            "oxygen_pilot": (4.05 * r / 12 + 6.6, 71.1 * r / 12 + 22.8, "kW", 12 <= r <= 60),
            "oxygen_production": (.217 * r + 8.73, 2.95 * r + 27.7, "kW", 144 <= r <= 1500),
            "hydrogen": (2.64 * r + 10.8, .122 * r + .021, "MW", None),
            "recycling": (.0604 * r, .039 * r, "kW", None)}
        row = {"rate_t_per_year": r, "processes": {}}
        for name, (plant, power, power_unit, in_range) in masses.items():
            power_kw = power * (1000 if power_unit == "MW" else 1)
            reactor_t = math.sqrt(power_kw)  # Eq15: 1000 sqrt(kW) kg.
            diagnostic_reactor_t = math.sqrt(power)  # Deliberate MW-as-kW error for H2.
            logistics_t = .038 * r * p["years"] if name == "recycling" else 0
            delivered_t = plant + reactor_t + logistics_t
            literal_cost = lambda m: 34 * (m * 1000 * 2.2)**.66
            repaired_cost = lambda m: amcm(m * 1000, inflation=p["inflation_1999_to_2021"])
            branches = {}
            for label, cer in (("literal_eq17", literal_cost), ("eq14_dimensional_repair", repaired_cost)):
                for allocation in ("combined", "separate"):
                    dev = cer(plant + reactor_t) if allocation == "combined" else cer(plant) + cer(reactor_t)
                    launch = delivered_t * p["launch_musd_per_t"]
                    operations = dev * p["years"] * p["operations_fraction_per_year"]
                    branches[label + "_" + allocation] = {
                        "plant_musd": dev, "launch_musd": launch, "operations_musd": operations,
                        "lcc_excluding_recycling_procurement_musd": dev + launch + operations}
            inferred_mass = plant + diagnostic_reactor_t
            dev = 34 * (inferred_mass / 2.2)**.66
            launch = (inferred_mass + logistics_t) * p["launch_musd_per_t"]
            operations = dev * p["years"] * p["operations_fraction_per_year"]
            branches["table_behavior_inference"] = {
                "plant_musd": dev, "launch_musd": launch, "operations_musd": operations,
                "lcc_musd": dev + launch + operations,
                "inferred_reactor_mass_t": diagnostic_reactor_t,
                "inferred_total_installed_mass_t": inferred_mass}
            row["processes"][name] = {
                "source_fit_in_range": in_range, "plant_mass_t": plant,
                "power_source_value": power, "power_source_unit": power_unit,
                "power_kw": power_kw, "reactor_mass_t": reactor_t,
                "logistics_mass_t": logistics_t, "branches": branches}
            if name == "recycling":
                row["processes"][name]["unresolved_logistics_cost"] = {
                    "explanation": "Prose says treat similarly to Earth supply; Table 1 behavior omits container procurement and packaging launch mass.",
                    "eq18_if_applied_musd": 492 * logistics_t**.59,
                    "additional_container_launch_if_applied_musd": .3 * logistics_t * p["launch_musd_per_t"]}
        q = r * p["years"]
        launch = 1.3 * q * p["launch_musd_per_t"]
        row["processes"]["earth_supply"] = {
            "container_quantity_continuous": q, "container_cost_eq18_musd": 492 * q**.59,
            "container_cost_eq14_musd": amcm(300, q, -1.5, p["inflation_1999_to_2021"]),
            "launch_musd": launch, "lcc_eq18_musd": 492 * q**.59 + launch}
        results["rows"].append(row)
    results["eq14_derived_coefficient"] = amcm(1 / 2.2, inflation=p["inflation_1999_to_2021"])
    results["printed_eq17_coefficient"] = 34
    return results


if __name__ == "__main__":
    import sys
    supplied = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) > 1 else {}
    print(json.dumps(run(supplied), indent=2, allow_nan=False))
