"""IRR interval for the ROXY pilot plant over stated development timing.

Operating receipts and the transport payment are taken from the printed annual
rules. Only the 200 million euro development total moves inside the five-year
development window. Because that move is a fixed negative sum, the internal
rate of return is lowest when the whole sum is paid in the first year and
highest when it is paid in the last. The printed rate is not used to place it.
"""
from __future__ import annotations

import json
from pathlib import Path


def _irr(cashflows):
    low, high = -0.9, 5.0

    def value(rate):
        return sum(amount / (1 + rate) ** index for index, amount in enumerate(cashflows))

    if value(low) * value(high) > 0:
        return None
    for _ in range(80):
        mid = (low + high) / 2
        if value(low) * value(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def _flows(development_year, net, transport_year, inputs):
    years = inputs["development_years"] + 1 + inputs["operating_years"]
    cash = [0.0] * years
    cash[development_year] -= inputs["development_meur"]
    cash[inputs["development_years"]] -= inputs["holding_cost_meur"]
    cash[transport_year] -= inputs["transport_meur"]
    first_operation = inputs["development_years"] + 1
    for year in range(first_operation, years):
        cash[year] += net
    return cash


def run():
    inputs = json.loads(Path(__file__).with_name("inputs.json").read_text(encoding="utf-8"))
    operating = inputs["operating"]
    net = {
        "oxygen_only": operating["oxygen_revenue_meur"] - operating["opex_meur"],
        "oxygen_and_metals": operating["oxygen_revenue_meur"] * 2 - operating["opex_meur"],
    }
    bounds = {}
    for product, annual in net.items():
        bounds[product] = {}
        for transport_year in (inputs["development_years"], inputs["development_years"] + 1):
            rates = [_irr(_flows(year, annual, transport_year, inputs))
                     for year in range(inputs["development_years"])]
            bounds[product][f"transport_in_year_{transport_year}"] = {
                "irr_lower": min(rates),
                "irr_upper": max(rates),
            }
    undiscounted = {
        product: annual * inputs["operating_years"] - inputs["development_meur"]
        - inputs["holding_cost_meur"] - inputs["transport_meur"]
        for product, annual in net.items()
    }
    return {
        "historical_schedule": "unresolved",
        "explicit_interest": "not applied; the paper names 4 percent but does not say when it is paid",
        "annual_net_meur": net,
        "undiscounted_cumulative_net_meur": undiscounted,
        "irr_bounds": bounds,
    }
