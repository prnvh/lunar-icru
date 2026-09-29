"""Regenerate the published-result checks. No network and no source PDFs."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReproductionTests(unittest.TestCase):
    def test_kornuta_npv_signs_and_rates_of_return(self):
        model = load("kornuta", ROOT / "models" / "kornuta2019" / "model.py")
        result = model.run({})
        signs = {1: False, 2: True, 3: False, 4: True, 5: True, 6: True, 7: True}
        for key, positive in signs.items():
            scenario = result["scenarios"][str(key)]
            self.assertEqual(scenario["nonnegative_npv"], positive)
            self.assertTrue(scenario["ror_rounds_to_reported"])
        moon = result["scenarios"]["1"]["native_npv_usd"]
        self.assertAlmostEqual(moon, -234_223_827.35739374, delta=1.0)

    def test_jones_campaign_ratio_stays_unresolved(self):
        model = load("jones", ROOT / "models" / "jones2020" / "model.py")
        inputs = json.loads((ROOT / "models" / "jones2020" / "original_inputs.json").read_text(encoding="utf-8"))
        result = model.run(inputs)
        self.assertIsNone(result["cumulative_cost_ratio"])
        pre = result["phases"][0]["demand_only_sizing"]
        self.assertAlmostEqual(pre["table5_linear_mass_kg"], 2262.7, places=1)
        self.assertAlmostEqual(pre["required_power_kwe"], 10.4958, places=4)

    def test_sowers_static_chain_and_blocked_irr(self):
        model = load("sowers", ROOT / "models" / "sowers_niac2020" / "model.py")
        base = json.loads((ROOT / "models" / "sowers_niac2020" / "original_inputs.json").read_text(encoding="utf-8"))
        expected = {"commercial": 2155.5, "ppp_lunar": 3125.6, "ppp_lunar_mars": 5046.9}
        for case, net in expected.items():
            document = json.loads(json.dumps(base))
            document["case"] = case
            result = model.run(document)
            got = result["selected_case"]["company_lifetime_undiscounted_net_cash_usd"] / 1e6
            self.assertAlmostEqual(got, net, places=1)
            self.assertIsNone(result["published_irr_reproduction"]["company_calculated_percent"])

    def test_charania_subtotals_match_and_price_is_null(self):
        model = load("charania", ROOT / "models" / "charania2007" / "model.py")
        here = ROOT / "models" / "charania2007"
        result = model.run({
            "original_inputs": json.loads((here / "original_inputs.json").read_text(encoding="utf-8")),
            "reported_outputs": json.loads((here / "reported_outputs.json").read_text(encoding="utf-8")),
        })
        self.assertIsNone(result["calculated_required_price_usd_per_kg"])
        for group in result["derived_cost_stack_sums_fy2006_musd"].values():
            self.assertTrue(group["rows_match_printed_subtotal"])


if __name__ == "__main__":
    unittest.main()
