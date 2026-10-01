# Supplement S1. Comparison sets for the reproducibility audit

This supplement is the comparison record for the manuscript. Each section states the source edition, the native decision quantity, the inputs used in the forward calculation, the printed targets, and the grade under the manuscript rules. Reported numbers are comparison targets. They are not inputs to the forward code. A null headline is unresolved. An interval that contains a printed headline is not a reproduction of that headline.

The grade rules are those in the manuscript subsection on reconstruction and numerical comparison. Exact means every quantity in the declared comparison set rounds to the printed digits. Close means every such quantity is within 1 percent of the printed value, or within half a unit of the last displayed digit, and the residual comes from a rounding or timing convention that was not chosen to shrink the error. Partial means at least one named equation or table meets exact or close, and the principal result stays unresolved. Unresolved means the central calculation cannot be recomputed.

Currency years that the source does not state are left unresolved. No inflation conversion is applied across those years. Chart curves were not digitized.

## S1.1 Kornuta and colleagues, 2018 report

**Source.** LPI Contribution No. 2142, printed pages 106–109, Table 14 [1]. The 2019 journal article [2] is the related publication. The journal spreadsheet was not recovered. The grade applies to the report.

**Native quantity.** Investor net present value of a mining company, source dollars, cost year unresolved, and the internal rate of return of the same cash flows.

**Inputs, fixed before comparison.**

| Input | Value | Role |
|---|---:|---|
| Hardware mass | 30,000 kg | Printed |
| Hardware factor | 100,000 USD/kg | Printed for the financial case |
| Delivery factor | 35,000 USD/kg | Printed |
| Initial outlay | 4,050,000,000 USD | Product of the three lines above |
| Recurring cost | 129,000,000 USD/year | Printed aggregate. Not replaced by the component sum |
| Discount rate | 10 percent | Printed |
| Life | 10 years | Printed |
| Cash-flow convention | End of each year, t = 1..10 | Required for the printed signs |
| Annuity factor | 6.144567 | Computed from the rate and life |
| Annual revenue | Table 14 printed revenue, held constant | Not fitted |

**Comparison set.** Millions of source dollars. Difference is reconstructed minus printed. The solved rate is the internal rate of the same end-of-year series. The full scenario table is the manuscript subsection on reproduction of the Kornuta financial case. The largest relative gap is 0.096 percent (Moon). Three scenarios, LEO + Moon, EML1 + LEO, and all customers, miss the displayed million by more than half a unit.

**Checks that are not the historical default.**

| Check | Result | Disposition |
|---|---|---|
| Start-of-year discounting, Moon | +147.35 million | Rejected. The printed Moon value is negative |
| Component recurring cost, 20 million + 800 kg × 135,000 USD/kg | 128 million per year; Moon NPV about −228 million | Not the historical cost. Does not round to −234 million |
| Quantity times printed average price, scenarios 4–7 | Net present values round to the displayed millions | Rounding diagnostic. Not substituted for printed revenue |
| Bennett and Dempster finance sheet, LEO [11] | XNPV −972.87 million; XIRR 4.06 percent | Same lineage. Printed LEO is −972 million and 4 percent |

**Grade.** Close for net present value on the printed-revenue path. Not exact. The seven rates round to the printed rates. The cost year is unresolved.

## S1.2 Jones and colleagues, 2020

**Source.** AIAA 2020-4041 [3]. The selected point is a selection inside the paper’s sweep, not a unique baseline: 17 t/year surface demand on the Duke plant, then the paper’s cislunar phase, a three-year plant life, and an inert-mass fraction of 0.25.

**Native quantity.** Undiscounted cumulative in-situ cost divided by cumulative Earth-delivery cost, fiscal-year 2019 million dollars.

**Comparison set.**

| Quantity | Reconstructed | Printed target | Absolute difference | Grade for this quantity |
|---|---:|---:|---:|---|
| Table 5 plant mass at 17 t/year | 2,262.7 kg | 2,262.7 kg | 0 | Exact |
| Power at the same rate | 10.4958 kWe | 10.4958 kWe | 0 | Exact |
| Development cost, all four Table 7 subsystems present | 552.6 to 614.3 million | Not a printed campaign total | Span 61.7 million | Not a headline |
| Production cost, same mass span | 113.9 to 136.3 million | Not a printed campaign total | Span 22.4 million | Not a headline |
| Campaign cost ratio | null | Printed only as a sweep result | — | Unresolved |

**Grade.** Partial. Mass and power meet the exact rule at the selected rate. The ratio stays unresolved because the event ledger, loader count, lander sizing, and the choice between Table 5 mass and a 40 kWe reactor count are not in the public paper. The mass-allocation span is too small to supply that ledger.

## S1.3 Sowers, 2020 NIAC report and 2021 article

**Source.** NIAC Phase I final report [4]. The 2021 article [5] repeats the company rates and does not add an annual table.

**Native quantity.** Company internal rate of return. A separate NASA-savings view is reported and is not the company rate.

**Static comparison, printed-revenue branch.** Million source dollars. These totals are the arithmetic of the printed cost and revenue rows. They are not a cash-flow schedule.

| Case | Undiscounted company net cash | Printed company IRR |
|---|---:|---:|
| Commercial | 2,155.5 | 8.84 percent |
| Lunar public-private | 3,125.6 | 15.8 percent |
| Lunar plus Mars | 5,046.9 | 15.4 percent |

Mars revenue is retained in both forms the report supports: 971 million printed, and 941 million from 1,882 t/year at 500 source dollars per kilogram.

**Schedules inside the stated windows.** The report states four years of development and production, an 18-month deployment, a ten-year life, and Mars demand from operating year 3. It does not state the annual weights. The three schedules below stay inside those windows. They were not adjusted toward the printed rates. Company internal rate of return, percent:

| Schedule | Commercial | Lunar public-private | Lunar plus Mars |
|---|---:|---:|---:|
| Uniform | 8.436 | 14.925 | 14.864 |
| Front-loaded | 7.290 | 13.356 | 13.362 |
| Back-loaded | 10.152 | undefined | undefined |

Undefined means the cash flow changes sign more than once, so a single conventional rate is not defined. None of these rates is the historical headline.

**Conditional net-present-value bounds.** Scenario stored before comparison: 1,100 t/year surface offtake, 500 source currency per kilogram, ten operating years, 10 percent discount, valuation at commissioning.

| Quantity | Result |
|---|---:|
| Kornuta modified-case net present value | −1,463.14 million |
| Sowers net present value over admissible allocations | [−681.78, +23.78] million |
| Kornuta break-even surface price | 716.47 per kg |
| Sowers break-even surface price | [496.48, 600.87] per kg |

**Grade.** Close for static totals that match the printed rows within rounding. Unresolved for the historical company rate. The interval is not that rate, and the cost year is unresolved.

## S1.4 Charania and DePasquale, 2007

**Source.** IAC-07-A5.1.03 [6]. Operations are stated at 35 million dollars per year for 2022–2031. Both 21.7 percent and 22.7 percent are printed as the capital cost attached to the same prices. Equity beta and the market premium are not numeric, so neither rate is recomputed.

**Native quantity.** Sale price that sets net present value to zero.

**Subtotal comparison.** Million fiscal-year 2006 dollars. Each header equals the sum of its component rows.

| Case | Component rows | Sum and printed subtotal | Difference |
|---|---|---:|---:|
| 1 | 957 + 319 + 1,445 | 2,721 | 0 |
| 2 | 2,157 + 1,019 + 2,220 | 5,396 | 0 |
| 3 | 2,557 + 1,044 + 2,240 | 5,841 | 0 |

**Price interval, not a point price.** Capital may fall in any year the chart labels before operations, 2013–2021, with operations in 2022–2031. Chart amounts were not read. End-of-year discounting at 21.7 percent. Shifting the whole index by one year does not change the price.

| Case | Demand | Printed price, USD/kg | Interval, USD/kg | Printed price inside the interval |
|---|---:|---:|---|---|
| Surface | 49.4 t/year | 26,845 | 14,612 to 67,611 | Yes |
| Low lunar orbit | 21.0 t/year | 133,947 | 66,526 to 313,768 | Yes |
| GEO | 0.45 t/year | 7,053,265 | 3,354,152 to 15,843,653 | Yes |

Inflating the surface stack at the stated 2.1 percent, with capital in 2013 or in 2021, gives 7,457 to 8,610 USD/kg. The printed inflation-only cost is 7,327 USD/kg, below that interval.

**Grade.** Exact for the three subtotals. Unresolved for a unique historical price. The historical module returns no point price.

## S1.5 Metzger, 2023, equation 18 only

**Source.** Acta Astronautica [9]. Author estimates in the baseline table are inputs to this equation. They are not a crossing-year schedule.

**Comparison set.** Terminal launch cost from equation 18.

| Terminal market fraction | Printed | Equation 18 | Absolute difference | Relative error |
|---|---:|---:|---:|---:|
| 1 | 30 | 30.0178 | 0.0178 | 0.059 percent |
| 0.1 | 119 | 119.6332 | 0.6332 | 0.532 percent |
| 0.01 | 436 | 437.3721 | 1.3721 | 0.315 percent |

**Grade for these three intermediates.** Close. All three are within 1 percent. **Grade for the crossing-year headline.** Unresolved. Section 5.1 states optimistic low-Earth-orbit year 15. Table 1 states year 19. The reliability equation and the preceding sentence disagree on development cost versus fabrication cost in the replacement term. Both readings are executed. Neither is selected to match a year.

## S1.6 Harry W. Jones, 2021

**Source.** ICES-2021-147, Table 1 [8]. This is not the Jones 2020 campaign model. Costs are million 2021 dollars. Life is 10 years. Launch cost is 10 million dollars per tonne. No printed cost enters the forward calculation.

**Three readings, kept separate.**

| Branch | What it computes | What it is not |
|---|---|---|
| Literal equation 17 | `34 × (mass in kg × 2.2)^0.66`, with megawatts converted to kilowatts | Not adjusted to the table |
| Dimensional repair of equation 14 | The longer equation in pounds, with the paper’s coefficients and the stated inflation factor | Not an author erratum |
| Inferred table behavior | `34 × (installed mass in tonnes / 2.2)^0.66`, hydrogen megawatt numerals passed into the kilowatt reactor formula, recycling-container procurement omitted | Not a claim that the printed equation is an author error |

A process-and-rate row counts as reproduced only when every cost cell is within 0.5 million dollars of the printed integer. The compact numerical comparison of literal, inferred, and printed values is in manuscript section 3.4. The row-level result for the inferred branch is:

| Process | 10 t/year | 30 t/year | 100 t/year | 300 t/year |
|---|---|---|---|---|
| Oxygen | No | No | Yes, below the stated fit domain | Yes, inside the fit domain |
| Hydrogen | No | Yes | Yes | Yes |
| Recycling | No | Yes | Yes | Yes |
| Earth supply, literal equation 18 | Yes | Yes | Yes | Yes |

That is 12 of 16 rows on the inferred branch. Literal equation 17 and the equation-14 repair do not meet the half-million rule on the mining rows. At 300 t/year the equation-14 repair gives an oxygen life-cycle cost of 92,717 if plant and reactor are costed together, or 114,677 if they are costed separately, against the printed 1,907. Earth supply matches the literal equation, not an inferred branch.

**Grade.** The inferred branch is a diagnostic comparison. It is not an exact or close reproduction of the printed equation, and it is not an author-confirmed correction. The case is not benchmark-eligible.

## S1.7 Blair and colleagues, 2002, Table 4.4

**Source.** Printed Version 5 statement for 2007–2016 [7]. Values were read from word positions in the table. The workbook is not public, so the statement cannot be rerun at a new price or demand.

**Native quantity.** Project net present value and project rate of return, million source dollars. Stated discount rate 10 percent.

| Check | Architecture 1 | Architecture 2 | Comparison |
|---|---:|---:|---|
| Printed project net present value | 4,156 | 4,134 | Target |
| Present value of the net-income row at 10 percent, 2007 undiscounted | 4,155.6 | 4,134.4 | Within 1 of the printed value |
| Sum of net income | Equals ending retained earnings | Equals ending retained earnings | Identity holds |
| Balance sheet, assets minus liabilities, equity, and retained earnings | Within 1 | Within 1 | Identity holds |
| Revenue years versus printed cumulative | 25,500 versus 25,501 | Same cumulative figure | Difference of 1 |
| Project rate of return of the net-income row | Not 12.8 percent | Not 12.6 percent | Printed rates are not this row |

**Grade.** The net-present-value identity is close to the printed project values under the stated discounting convention. The project rate of return is unresolved. The statements are not a model that accepts a new input.

## S1.8 Birch and colleagues, 2026

**Source.** Aerospace 13 (2026) 86 [10]. Development cost used here is the stated 200 million euros. Transport price, plant mass, oxygen revenue, and operating cost are the printed annual ingredients. The 4 percent carrying cost is named and not dated, so it is not applied. Figures 5 and 6 were not digitized. The dataset is not public.

**Native quantity.** Project internal rate of return. Printed reference values are 19.9 percent for oxygen only and 47.4 percent with metals.

Development of 200 million euros is paid entirely in one of the five development years. For a fixed outlay, the rate is extremal at the ends of that window. Interior schedules lie between those ends.

| Transport placement | Oxygen internal rate | Metals internal rate | Printed rate inside the interval |
|---|---|---|---|
| Delay year | 19.76 to 24.64 percent | 41.07 to 64.26 percent | 19.9 percent yes; 47.4 percent yes |
| First operating year | 22.68 to 32.07 percent | 45.19 to 98.19 percent | 19.9 percent no; 47.4 percent yes |

Undiscounted cumulative net from the same printed ingredients is 2,566.5 million euros for oxygen only, against the table’s 2.4 billion, and 8,341.5 million euros with metals, against 8.2 billion. No coefficient was changed to close that gap.

**Grade.** Unresolved as a unique historical schedule. The interval is conditional on the printed annual rules and on where transport is paid.
