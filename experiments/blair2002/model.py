"""Accounting checks on Blair 2002 Table 4.4.

The numbers are the printed statement, read from word positions on the report
page. They are not a rerun of the missing workbook. The stated project NPV is
compared, outside this module, with the present value of the net-income row.
"""
from __future__ import annotations

import json
from pathlib import Path


def _present_value(cashflows, rate):
    """First listed year is undiscounted. Later years are discounted from it."""
    return sum(amount / (1 + rate) ** index for index, amount in enumerate(cashflows))


def _net_income_irr_is_not_a_project_return(cashflows):
    """The net-income row changes sign once, but its root is not a meaningful
    project return: the first losses are a few million dollars and later
    profits are billions, so the root is far above any stated hurdle."""
    return None


def run():
    statement = json.loads(Path(__file__).with_name("statement.json").read_text(encoding="utf-8"))
    rate = statement["stated_discount_rate"]
    architectures = {}
    for name, rows in statement["architectures"].items():
        assets = rows["total_assets"]
        liabilities = rows["liabilities"]
        equity = rows["shareholder_equity"]
        retained = rows["retained_earnings"]
        gap = [a - (liability + owner + earnings)
               for a, liability, owner, earnings in zip(assets, liabilities, equity, retained)]
        net_income = rows["net_income"]
        architectures[name] = {
            "revenue_sum": sum(rows["revenues"]),
            "revenue_cumulative_printed": rows["revenues_cumulative"],
            "net_income_sum": sum(net_income),
            "retained_earnings_final": retained[-1],
            "balance_sheet_gap_by_year": gap,
            "npv_of_net_income_at_stated_rate": _present_value(net_income, rate),
            "project_rate_of_return": _net_income_irr_is_not_a_project_return(net_income),
        }
    return {
        "discount_convention": "The first statement year is the present. The stated rate is 10 percent.",
        "project_rate_of_return_status": "unresolved",
        "architectures": architectures,
        "workbook": "not public; these checks do not accept a new price or demand",
    }
