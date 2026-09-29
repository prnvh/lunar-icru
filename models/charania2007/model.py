"""Charania and DePasquale 2007 source-packet checks.

The published required prices are outputs of an untabulated cash-flow model.
This module sums printed cost lines and checks published ratios. It does not
solve for a zero-NPV price.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


def _sum_case(rows: list[dict], case: str) -> float:
    return float(sum(row[case] for row in rows if row[case] is not None))


def _ratio(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return numerator / denominator


def run(inputs: dict) -> dict:
    """Return printed prices as reported, and null for the unpublished price solver."""
    data = copy.deepcopy(inputs)
    reported = data["reported_outputs"]
    costs = data["original_inputs"]["cost_lines_fy2006_musd"]
    stacks = {}
    for group in ("ddte", "acquisition", "transportation_to_lunar_surface"):
        summed = {
            case: _sum_case(costs[group]["rows"], case)
            for case in ("case_1", "case_2", "case_3")
        }
        printed = costs[group]["printed_subtotal"]
        stacks[group] = {
            "sum_of_rows": summed,
            "printed_subtotal": printed,
            "rows_match_printed_subtotal": all(summed[case] == printed[case] for case in summed),
        }
    ddte_ratio = stacks["ddte"]["sum_of_rows"]["case_2"] / stacks["ddte"]["sum_of_rows"]["case_1"]
    price_cost_ratios = {}
    for case_id, case in reported["cases"].items():
        price = case.get("propellant_price_usd_per_kg")
        cost = case.get("inflation_only_cost_usd_per_kg")
        if price is not None and cost is not None:
            price_cost_ratios[case_id] = price / cost
    probabilistic = reported["probabilistic_means_page_7"]
    return {
        "model_id": "charania2007",
        "reproduction_grade_for_required_price": "unresolved",
        "calculated_required_price_usd_per_kg": None,
        "reported_prices_usd_per_kg": {
            case_id: case.get("propellant_price_usd_per_kg")
            for case_id, case in reported["cases"].items()
        },
        "derived_cost_stack_sums_fy2006_musd": stacks,
        "case_2_over_case_1_ddte": ddte_ratio,
        "case_2_ddte_more_than_twice_case_1": ddte_ratio > 2,
        "price_over_inflation_only_cost": price_cost_ratios,
        "probabilistic_over_deterministic": {
            "1A": _ratio(probabilistic["1A_usd_per_kg"], reported["cases"]["1A"]["propellant_price_usd_per_kg"]),
            "2A": _ratio(probabilistic["2A_usd_per_kg"], reported["cases"]["2A"]["propellant_price_usd_per_kg"]),
        },
        "ltv_consumed_over_delivered": (
            data["original_inputs"]["ltv_delivery"]["propellant_consumed_mt"]
            / data["original_inputs"]["ltv_delivery"]["propellant_delivered_to_llo_mt"]
        ),
        "recomputed_wacc": None,
        "blockers": [
            "Annual cash flows, debt draws, and equity timing are not tabulated.",
            "Equity beta and the market premium are not numeric, so 21.7% and 22.7% cannot be recomputed.",
            "CABAM, StageSizer, and the Monte Carlo workbook are not in the paper.",
            "Cash-flow figures are not digitized into a schedule.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    inputs = {
        "original_inputs": json.loads((here / "original_inputs.json").read_text(encoding="utf-8")),
        "reported_outputs": json.loads((here / "reported_outputs.json").read_text(encoding="utf-8")),
    }
    print(json.dumps(run(inputs), indent=2))
