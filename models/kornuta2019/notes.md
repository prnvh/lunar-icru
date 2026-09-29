# Kornuta-family mining-company cash-flow reconstruction

## Fixed research question

When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

## Scope and source identity

This module reconstructs the constant annual cash-flow calculation in the **2018 detailed report**, not an independently verified copy of the 2019 journal spreadsheet. The directory name identifies the Kornuta 2019 model family. The source is *Commercial Lunar Propellant Architecture: A Collaborative Study of Lunar Propellant Production*, LPI Contribution 2142, published by United Launch Alliance. Economic Analysis section authors are Erica Otto and David Kornuta. The related journal DOI is [10.1016/j.reach.2019.100026](https://doi.org/10.1016/j.reach.2019.100026).

Official source: [USRA report PDF](https://www.lpi.usra.edu/lpi/contribution_docs/LPI-002142.pdf), [archive record](https://repository.hou.usra.edu/handle/20.500.11753/1245). Printed pages 106-109 are PDF pages 124-127 of 189. Figure 71 and Table 14 were checked as rendered page images. `original_inputs.json` includes the retrieval date, SHA-256 checksum, exact page pointers, units, and provenance classifications. Source PDFs and rendered images are local inspection aids outside this directory; no source copies are redistributed here.

**Source correction:** NTRS citation 20190004974, formerly identified in project research as Kornuta full text, actually downloads *Lunar Flashlight: Illuminating the Lunar South Pole*. It is excluded from this reconstruction.

## Decision problem and boundary

The native question is whether investment in a lunar propellant mining company produces positive NPV at a given discount rate. It does not calculate government program cost or demonstrate mining technology performance. The seven customer combinations are Moon, EML1, LEO, LEO + Moon, EML1 + LEO, Moon + EML1, and all customers. The source's Moon category also covers its reusable lunar-cycler customer servicing lunar orbit.

Quantities and sale prices in the financial scenarios are **at the lunar surface**, including surface production required to serve more distant customer markets. They are not quantities delivered into LEO/EML1. The financial calculation takes these quantity/price pairs as inputs; it does not recalculate delivery losses, transport performance, power, plant sizing, or customer willingness to pay.

The reported capital outlay covers mining/processing hardware development and its delivery to the lunar surface. Recurring costs cover the report's operations/replacement aggregate. The cash-flow model has no separately recovered schedule for taxes, debt, depreciation, construction, salvage, plant ramp-up, or replacement events. No such schedule is invented. The report's source currency year and real/nominal convention remain unresolved; values are preserved as source USD.

## Equations and reconstruction choices

Let M be initial hardware mass, c_h its hardware/development factor, c_l Earth-to-lunar-surface delivery cost, I the initial investment, C the annual recurring aggregate, R_s annual revenue in scenario s, r the discount rate, and N the mine life.

```text
I = M * (c_h + c_l)
  = 30,000 * (100,000 + 35,000) = 4,050,000,000 USD
A(r,N) = sum((1+r)^(-t), t=1,...,N)
NPV_s = -I + (R_s - C) * A(r,N)
```

Original r = 0.10, N = 10, and C = 129,000,000 USD/year. The resulting annuity factor is 6.14456710570468. The initial outlay at t=0 followed by receipts/payments at the end of years 1-10 is a documented reconstruction interpretation of the simple DCF description on p.106. The spreadsheet was not recovered.

The primary revenue path uses Table 14's printed annual revenues as a constant schedule. No unreported growth or timing is fitted. The source also provides a weighted-price relation on p.107:

```text
average_price = sum(quantity_i * price_i) / sum(quantity_i)
annual_revenue = annual_sale_quantity * average_price
```

The printed average prices and annual revenues have different rounding precision. The module therefore also returns a **separate historical rounding diagnostic** using quantity times the printed average price. That diagnostic is calculated with the original historical parameters even when an override experiment is run. It is not silently substituted for the primary revenue path.

### Aggregate recurring cost discrepancy

Figure 71 visibly reports $129M/year. Applying the listed hardware and delivery factors to 800 kg/year replacement parts, then adding $20M/year operations, gives:

```text
20,000,000 + 800 * (100,000 + 35,000) = 128,000,000 USD/year
```

The source does not expose the missing $1M/year component. This expression is a diagnostic inference, not a recovered replacement-cost equation. Native runs retain the printed $129M. Changing to $128M would increase every ten-year NPV by $6.144567M; this is not used to improve agreement. Component replacement or operations overrides are unsupported until the aggregate is reconciled; the explicitly reported annual aggregate itself can be overridden.

## Reported and reconstructed NPVs

All figures below are millions of source USD. Difference is reconstructed minus reported. These are reconstruction calculations, not software tests or empirical validation. Historical parameter and revenue choices were retained without optimizing against target outputs.

| Scenario | Customers | Reported NPV | Primary reconstruction | Difference | Absolute error (%) |
|---|---|---:|---:|---:|---:|
| 1 | Moon | -234 | -234.223827 | -0.223827 | 0.095653 |
| 2 | EML1 | 1,609 | 1,609.146304 | 0.146304 | 0.009093 |
| 3 | LEO | -972 | -971.571880 | 0.428120 | 0.044045 |
| 4 | LEO + Moon | 3,639 | 3,636.853449 | -2.146551 | 0.058987 |
| 5 | EML1 + LEO | 5,481 | 5,480.223581 | -0.776419 | 0.014166 |
| 6 | Moon + EML1 | 6,218 | 6,217.571634 | -0.428366 | 0.006889 |
| 7 | All | 10,092 | 10,088.648910 | -3.351090 | 0.033205 |

Both negative-NPV scenarios and all five positive-NPV scenarios reproduce in sign. Scenarios 4, 5, and 7 differ by more than half of the displayed $1M NPV increment when the rounded reported annual revenue is used. No project-wide reproduction grade is assigned here; shared grading criteria belong in the parent analysis.

The source-supported alternative R = quantity times printed price changes annual revenue from $1,380M to $1,380.4M (scenario 4), $1,680M to $1,680.14M (5), $1,800M to $1,800.06M (6), and $2,430M to $2,430.48M (7). Its NPVs are respectively $3,639.311276M, $5,481.083820M, $6,217.940308M, and $10,091.598302M. Each rounds to the source's displayed NPV. Scenarios 1-3 have unchanged revenue. Thus all seven results are consistent with displayed NPV rounding under this alternative; it is evidence of a plausible spreadsheet precision convention, **not proof of the original workbook's internal formula precision**.

Table 14's ROR values (9%, 19%, 4%, 28%, 37%, 40%, 56%) are preserved in the evidence file but not independently reconstructed by this NPV module.

## Separate derived break-even price

Since annual surface sale quantities are recoverable, a separate output computes the constant average surface price required for zero NPV with fixed annual quantity Q:

```text
p_break_even = (I / A(r,N) + C) / Q
```

This is an added reporting quantity, not a replacement for native NPV and not a published claim. It is not a delivered-LEO price, a marginal production cost, or a route-specific price schedule. For a mixture of customers it is an average price over the stated surface quantity. The original-case values are $7,881.19, $2,814.71, $625.49, $579.50, $511.77, $2,074.00, and $480.56/kg for scenarios 1-7. Quantity zero returns null rather than a finite break-even price.

## API and controlled overrides

`model.py` uses only Python's standard library. `run(inputs: dict) -> dict` accepts an **override dictionary**, reads its unchanged native source values from `original_inputs.json`, and returns all seven scenarios. Use `run({})` for the historical reconstruction. The returned dictionary includes supported and unsupported fields, source and parameter provenance, explicitly labelled analyst overrides, per-year undiscounted/discounted cash flows, and reported-versus-reconstructed NPV differences.

Supported global keys:

- `discount_rate`: nonnegative fractional annual rate.
- `mine_life_years`: positive integer number of operating years.
- `initial_investment_usd`: explicit initial capital aggregate. This does not imply a new plant-mass or performance relationship.
- `annual_cost_usd`: constant annual recurring aggregate; the source's $129M default remains intact.
- `scenario_overrides`: dictionary keyed by strings `"1"` through `"7"`.

Within each scenario, supported keys are `annual_sale_quantity_kg`, `sale_price_usd_per_kg`, and `annual_revenue_usd`. Quantities are surface sale quantities. With a quantity-only override, the historical implied price R/Q is held fixed. A price override uses R=Q*p; a direct revenue override supplies R. Price and direct revenue cannot be specified together. With no revenue/price/quantity override, the reported revenue remains authoritative. A quantity override does **not** resize equipment or change costs; it is a fixed-plant revenue experiment whose operational feasibility must be assessed separately.

Example, importing `model.py` with the Python module-loading mechanism of the caller:

```python
historical = run({})
modified = run({
    "discount_rate": 0.12,
    "scenario_overrides": {
        "3": {"annual_sale_quantity_kg": 1260000, "sale_price_usd_per_kg": 600}
    }
})
```

Command-line entry point from repository root:

```text
python models/kornuta2019/model.py
python models/kornuta2019/model.py path/to/overrides.json
```

The command-line file is an override dictionary, not `original_inputs.json`. Unknown keys are rejected. Modified-scenario differences from the source are labelled as comparisons, not reproduction errors. Source rounding diagnostics always retain historical parameters. This module does not provide architecture, launch-performance, productivity, finance, inflation, or dynamic production scaling adapters.

## Source-label issues and unresolved evidence

- Prose on pp.108-109 calls the negative cases scenarios 1 and 2 and associates the second with LEO. The explicit scenario definitions and Table 14 instead make LEO scenario **3**, while scenario 2 is profitable EML1. This module follows the table and explicit definitions, and records the prose inconsistency.
- The source calls Table 14 a subsidy table, but the columns report revenue, NPV and ROR. `minimum_time_zero_subsidy_usd = max(0,-NPV)` is a derived consequence of a time-zero grant, reflecting the interpretation discussed on p.107; it is not a subsidy delivery schedule.
- The report's mine-sizing section uses a different development factor; p.107 explicitly doubles it to $100,000/kg for the financial scenarios. No lower factor is substituted.
- The same initial plant and recurring aggregate are used for all seven scenarios. No source-supported nonlinear plant or power scaling is reconstructed here.
- No original Excel workbook, annual construction schedule, cost-year definition, or explanation of the $1M annual cost discrepancy was recovered. These limit claims of exact replication and downstream harmonization.
- The source supports a simple central economic calculation; faithful matching of its displayed financial results does not establish that the assumed market, plant lifetime, production throughput or replacement mass is physically achievable.
