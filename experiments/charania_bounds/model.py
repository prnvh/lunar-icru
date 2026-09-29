"""Zero-NPV price interval for Charania 2007 from the printed cost stack.

The annual schedule is not tabulated and is not read off the cash-flow charts.
The charts do label the years 2013-2031, and the prose places operations in
2022-2031. This module treats 2013-2021 as the widest pre-operation window
those labels allow. Capital is a fixed total placed anywhere in that window.
That interval can contain the printed price without identifying the schedule.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _capital(costs, case):
    total = 0.0
    for group in ("ddte", "acquisition", "transportation_to_lunar_surface"):
        total += costs[group]["printed_subtotal"][case]
    return total


def price_interval(capital_musd, operations_musd_per_year, kg_per_year, rate,
                   capital_years, operation_years):
    if rate < 0 or kg_per_year <= 0:
        raise ValueError("Need a nonnegative discount rate and positive sales")
    quantity = sum(kg_per_year / (1 + rate) ** year for year in operation_years)
    operations = sum(operations_musd_per_year / (1 + rate) ** year for year in operation_years)
    early = min(capital_years)
    late = max(capital_years)
    high = (capital_musd / (1 + rate) ** early + operations) * 1_000_000 / quantity
    low = (capital_musd / (1 + rate) ** late + operations) * 1_000_000 / quantity
    return low, high


def run():
    source = json.loads((ROOT / "models/charania2007/original_inputs.json").read_text(encoding="utf-8"))
    costs = source["cost_lines_fy2006_musd"]
    operations = source["operations"]["mission_operations_musd_per_year"]
    # End-of-year index: 2013 is t=1. Shifting the index does not change the
    # price, because it scales cost and sales by the same discount factor.
    capital_years = list(range(1, 10))       # 2013-2021
    operation_years = list(range(10, 20))    # 2022-2031
    demands = {"case_1": 49_400, "case_2": 21_000, "case_3": 450}
    rates = {
        "table_and_figure": source["wacc"]["table_and_figure_rate"],
        "prose_headline": source["wacc"]["prose_headline_rate"],
    }
    intervals = {}
    for case, kg in demands.items():
        capital = _capital(costs, case)
        intervals[case] = {"capital_fy2006_musd": capital, "sales_kg_per_year": kg, "by_wacc": {}}
        for label, rate in rates.items():
            low, high = price_interval(capital, operations, kg, rate, capital_years, operation_years)
            intervals[case]["by_wacc"][label] = {
                "wacc": rate,
                "price_usd_per_kg_lower": low,
                "price_usd_per_kg_upper": high,
            }
    inflation = source["wacc"]["inflation_rate"]
    capital = _capital(costs, "case_1")
    sales_kg = demands["case_1"] * 10
    inflated = {}
    for capital_year, label in ((2013, "earliest"), (2021, "latest")):
        nominal_capital = capital * (1 + inflation) ** (capital_year - 2006)
        nominal_operations = sum(operations * (1 + inflation) ** (year - 2006) for year in range(2022, 2032))
        inflated[label] = (nominal_capital + nominal_operations) * 1_000_000 / sales_kg
    return {
        "calculated_required_price_usd_per_kg": None,
        "window": {
            "capital_calendar_years": "2013-2021",
            "operation_calendar_years": "2022-2031",
            "basis": "Figure year labels and the stated 2022-2031 operating window. Chart amounts were not read.",
        },
        "intervals": intervals,
        "case_1_inflation_only_usd_per_kg": inflated,
        "historical_schedule": "unresolved",
    }
