"""Independent identities and boundary checks for paper recovery experiments."""
import importlib.util
import itertools
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_"), ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RecoveryChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load("experiments/metzger2023/model.py")
        cls.b = load("experiments/sowers_bounds/model.py")

    def test_launch_curve_independent_published_endpoints(self):
        rows = self.m.run()["rows"]
        for fraction, printed in ((1, 30), (0.1, 119), (0.01, 436)):
            row = next(x for x in rows if x["market_fraction"] == fraction and x["elapsed_industry_year"] == 30)
            # Source input and endpoint values are rounded. A1% tolerance was
            # the repository's pre-existing very-close reproduction threshold.
            self.assertLess(abs(row["launch_usd_per_kg"] / printed - 1), 0.01)

    def test_zero_interest_financing_identity(self):
        result = self.m.run({"discount_initial": 0, "discount_final": 0})
        p = result["parameters"]
        row = result["rows"][0]
        explicit_total = (row["capital_cost_usd"] + row["capital_transport_cost_usd"]
                          + p["annual_operations_usd"] * (p["buildup_years"] + p["operating_years"]))
        self.assertAlmostEqual(row["surface_lrac_usd_per_kg"], explicit_total /
                               (p["annual_product_kg"] * p["operating_years"]), places=8)
        self.assertAlmostEqual(row["cost_components"]["interest_usd_per_kg_product"], 0, places=8)

    def test_cost_partition_and_reliability_optimum(self):
        result = self.m.run()
        for row in result["rows"]:
            self.assertAlmostEqual(sum(row["cost_components"].values()), row["surface_lrac_usd_per_kg"], places=7)
        p = result["parameters"]
        r, replacement, best = self.m.optimize_reliability(120000, 40000, 12000, p)
        for candidate in (0.2, 0.4, 0.6, 0.8, 0.9):
            value = (120000 + replacement / candidate) * self.m.reliability_factor(candidate, p) + 12000 / candidate
            self.assertLessEqual(best, value)
        self.assertTrue(0 < r < 1)

    def test_rocket_zero_burn_and_impossible_payload(self):
        self.assertAlmostEqual(self.m.gear_ratio(0, 0, 450, 0.1), 1)
        with self.assertRaises(ValueError):
            self.m.gear_ratio(20000, 20000, 450, 0.1)

    def test_bound_extrema_against_all_vertices(self):
        costs = {"a": 100, "b": 30, "c": 7}
        windows = {"a": [-5, -2], "b": [-1, 0], "c": [-4, 0]}
        low, high, _ = self.b.cost_pv_bounds(costs, windows, 0.1)
        vertices = [sum(costs[key] * 1.1 ** -time for key, time in zip(costs, times))
                    for times in itertools.product(*(windows[key] for key in costs))]
        self.assertAlmostEqual(low, min(vertices))
        self.assertAlmostEqual(high, max(vertices))

    def test_zero_discount_bounds_collapse_to_source_net_cash(self):
        result = self.b.run({"discount_rate": 0})
        s = result["sowers_partial_identification"]
        self.assertAlmostEqual(s["npv_lower"], 2155.5e6, delta=1e-5)
        self.assertAlmostEqual(s["npv_upper"], s["npv_lower"], delta=1e-5)

    def test_price_sensitivity_equals_discounted_sales(self):
        low = self.b.run({"sale_price_per_kg": 500})["sowers_partial_identification"]
        high = self.b.run({"sale_price_per_kg": 501})["sowers_partial_identification"]
        expected = 1100000 * sum(1.1 ** -year for year in range(1, 11))
        self.assertAlmostEqual(high["npv_lower"] - low["npv_lower"], expected, delta=1e-5)
        self.assertAlmostEqual(high["npv_upper"] - low["npv_upper"], expected, delta=1e-5)

    def test_jones2021_forward_reproduction_at_in_domain_rate(self):
        model = load("experiments/harry_jones2021/model.py")
        row = model.run({"rates_t_per_year": [300]})["rows"][0]
        reported = json.loads((ROOT / "experiments/harry_jones2021/reported_outputs.json").read_text())
        for process, key in (("oxygen_production", "oxygen"), ("hydrogen", "hydrogen"), ("recycling", "recycling")):
            values = row["processes"][process]["branches"]["table_behavior_inference"]
            for metric in ("plant", "launch", "operations", "lcc"):
                self.assertAlmostEqual(values[metric + "_musd"], reported[key][metric][-1], delta=0.5)
        self.assertTrue(row["processes"]["oxygen_production"]["source_fit_in_range"])

    def test_jones2021_power_unit_diagnostic(self):
        model = load("experiments/harry_jones2021/model.py")
        h = model.run({"rates_t_per_year": [300]})["rows"][0]["processes"]["hydrogen"]
        inferred = h["branches"]["table_behavior_inference"]["inferred_reactor_mass_t"]
        self.assertAlmostEqual(h["reactor_mass_t"] / inferred, 1000 ** 0.5, places=10)


if __name__ == "__main__":
    unittest.main()
