# Sowers NIAC Phase I, February 2020

Research question: When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

This module reconstructs the report's thermal-mining **production-company** cost build-up and commercial/public-private-partnership cases. It preserves printed financial inputs, supplies explicitly named arithmetic alternatives, and leaves original IRR reproduction unresolved. It is not a modernized scenario or an adapter to a common model.

## Source and scope

Primary source: George Sowers, Colorado School of Mines, *Thermal Mining of Ices on Cold Solar System Bodies*, NIAC Phase I Final Report, February 2020 cover, [official PDF](https://space.mines.edu/wp-content/uploads/sites/134/2020/03/Thermal-Mining-NIAC-Phase-I-final-report.pdf). The Mines [release record](https://space.mines.edu/thermal-mining-niac-phase-i-final-report/) is dated 11 March 2020. `source_manifest.json` records retrieval, SHA-256 and page pointers. The retrieved file has 135 pages. Printed and one-based PDF page numbers coincide in the relevant section. Pages 83, 84 and 87 were rendered and visually inspected.

Source files and page images in `source/` are ignored local inspection aids. They are not redistribution artifacts. The input JSON is a source-derived numerical record with provenance, rather than a claim that the original financial workbook has been recovered.

The report assigns exploration/prospecting and some initial technology development to governments (p.81). A separate transportation business purchases propellant at the lunar surface and serves distant customers. The company's revenue therefore uses **surface demand and surface price**, not point-of-sale demand and price. Landing-pad construction belongs to the transportation company; the mine is charged only 1/12 of that shared dual launch (p.74). No additional taxes, debt, depreciation, residual value, insurance, prospecting charges, separate replacement schedule or transport-fleet costs are invented. Operations are a mass-based allowance intended to include routine operation, maintenance and repair. Currency year and real/nominal treatment remain unspecified.

## Interface

`model.py` uses only Python's standard library and exposes `run(inputs: dict) -> dict`. Pass the complete `original_inputs.json` document. The function does not mutate it or read files. The CLI is a convenience that loads that file and prints JSON:

```text
python models/sowers_niac2020/model.py --case commercial
python models/sowers_niac2020/model.py --case ppp_lunar_mars --variant demand_revenue
python models/sowers_niac2020/model.py --case ppp_lunar --timing illustrative_uniform_annual
```

The cases are `commercial`, `ppp_lunar` and `ppp_lunar_mars`. The default `reported_table` variant intentionally uses the inconsistent printed $971M Mars plateau revenue. Its first two operating years use $579M because Mars demand has not started. This is a transparent combination of the printed plateau and the prose onset, not a claim that the report's hidden workbook followed it.

Alternatives:

- `demand_revenue`: keep printed costs and derive revenue from demand times price.
- `prose_scaled_costs`: reconstruct component costs and apply the explicitly printed scale factors.
- `demand_ratio_scaled_costs`: apply the stated relative-production scaling rule using the actual demand ratios.

Controlled experiments can add `inputs['overrides']`, for example `{'surface_price_usd_per_kg': 1000}`, `{'nasa_investment_musd': 0}`, `{'operating_years': 15}`, `{'demand_multiplier': 0.8}`, or `{'nonrecurring_cost_multiplier': 1.25}`. These are changes to the historical case, not new source values. `annual_revenue_musd` overrides the full-demand revenue in `printed_table` mode at the source $500/kg price, before any explicit price/demand multipliers. `demand_multiplier` affects company purchases in each segment; the separate NASA mission-savings comparison retains its own documented mission inputs. Modify the `nasa_savings` block explicitly if that mission service changes.

Under `reported_table`, cost totals remain the printed totals when demand changes. Select a scaling variant to investigate the report's proportional cost rule. The model does not claim that a fixed plant can supply arbitrary demand, nor does it supply a capacity/scheduling optimizer. `nasa_investment_musd=0` removes public capital support while preserving NASA as a customer; use `commercial` for the source's commercial-only demand. There is no single generic "PPP off" switch that silently changes both funding and customers.

`discount_rate` can be supplied at document level or within `overrides`. It is used only when a timing scenario is selected. Without cash-flow timing, an NPV cannot be produced legitimately. The report's native financial metric is IRR, not a prescribed NPV discount rate.

## Equations and source mapping

1. **Development (p.72, Table 4.8.6):** subsystem cost is unit mass times its development $/kg factor, plus the $20M fixed ground-system amount. Ice-hauler development is included in GPV development.
2. **Production (pp.72-73, Table 4.8.7):** first-unit cost is mass times production $/kg factor. The reconstruction uses unit learning `C_n = C_1 n^b`, `b = log2(0.9)`, and sums units 1 through N. This matches each multi-unit table entry within its printed $1000 precision. The prose calls 0.9 an "exponent"; using 0.9 literally as the power of unit number would not reproduce the table. This is an explicitly inferred interpretation supported by multiple independent table rows. The four vehicle bases include the GPV base, whose upper hardware is a separate 500 kg production row.
3. **Launch (p.74, Tables 4.8.8-4.8.9):** single launch `4000 kg * $35000/kg = $140M`; dual launch `2 * $140M * 1.10 = $308M`. Charged deployment is `3 singles + 2 duals + (1000/12000) dual`. Mars adds one complete dual launch.
4. **Operations (p.75, Table 4.8.11):** `26200 kg * $3000/(kg year) = $78.6M/year`.
5. **Case scaling (p.83):** apply the selected scale to development, production and operations; launch allocation changes discretely. `reported_table` instead uses each printed case total directly. The unrounded component branch remains separate.
6. **Revenue (pp.81-82, Table 4.9.2):** annual revenue is surface tonnes times 1000 times surface $/kg. Commercial/lunar demand is constant for ten operating years; additional Mars demand begins in operating year three. No revenue is assigned to excess oxygen or other byproducts.
7. **Company undiscounted net cash:** sum annual revenue minus annual operating expenditure, minus development/production/deployment, plus NASA capital contribution. Public support is counted once and is not product revenue.
8. **NASA benefit (pp.85-87):** lunar annual savings are `5000*(35000-500) + 2*$150M = $472.5M`. Incremental Mars savings are `(75000+47000)*46000 - 75000*5000 - 47000*1100 = $5185.3M`, printed as $5185M. Subtract the NASA capital contribution for the government's net savings. The default retains the rounded $5185M; `nasa_savings_mode='derived'` exposes the unrounded alternative.
9. **Optional timed economics:** cash flow at period t is revenue minus operating and capital spending plus support. `NPV(r)=sum(CF_t/(1+r)^t)`; IRR is its zero. A bisection solver returns one root only for a one-sign-change cash-flow stream; otherwise it reports that an IRR has not been selected. Output money is in USD, with names identifying units. Period zero is the first figure-style year, and only the difference in timing matters for IRR.

## Numerical reconstruction results

These are model calculation results, not a software test suite. No tests were added or run. Errors below are calculated minus printed, divided by printed for relative error. Monetary totals are shown in millions of source dollars.

| Independent arithmetic | Printed | Calculated | Relative error |
|---|---:|---:|---:|
| Development, Table 4.8.6 | 883.000 | 883.000 | 0% |
| Production, Table 4.8.7 | 613.471 | 613.471276 | +0.0000451% |
| Deployment, Table 4.8.9 | 1062.000 | 1061.666667 | -0.0313873% |
| Capital total, Table 4.8.10 | 2559.000 | 2558.137943 | -0.0336873% |
| Annual operations, Table 4.8.11 | 78.600 | 78.600 | 0% |
| Commercial annual revenue | 550.000 | 550.000 | 0% |
| Lunar PPP annual revenue | 579.000 | 579.000 | 0% |
| Lunar/Mars PPP annual revenue | 971.000 | 941.000 | -3.08960% |

The capital summary differences mainly reflect the source's rounding conventions, which are not applied consistently across all tables. Reading a printed cost as an input and returning it is not independent reproduction; the component calculations above are the independent checks. The Mars revenue discrepancy remains an unresolved source inconsistency regardless of its percentage magnitude.

Using the printed financial cost table, ten operating years and the stated Mars onset gives the following undiscounted **derived** totals. These are not presented as exact reproduction of the graphs:

| Case | Company net cash, reported-revenue branch | Company net cash, demand-derived branch | NASA net savings, printed savings branch |
|---|---:|---:|---:|
| Commercial | 2155.5 | 2155.5 | 0 |
| Lunar PPP | 3125.6 | 3125.6 | 3925.0 |
| Lunar/Mars PPP | 5046.9 | 4806.9 | 45005.0 |

## Original IRRs remain unresolved

Table 4.9.3 reports company IRRs **8.84%, 15.8%, 15.4%**. Page 87 reports NASA IRRs **27% and 54%**. Numeric annual spending and milestone-payment schedules are absent. Four years of development/build, 18 months of deployment and a five-year funding period do not uniquely determine those schedules; partial initial/final production periods are also unclear. The default therefore returns `timed_cash_flow: null` and null calculated IRR/error, together with the published target and the reason. No unpublished timing profile was calibrated to those targets.

For illustration only, `illustrative_uniform_annual` allocates development/build uniformly to figure-style years 1-4, deployment equally to years 5-6, funding equally to years 1-5, and operations to years 7-16. This approximates the prose durations without claiming to recover the schedule in Figure 4.9.5. With printed case costs and printed plateau revenues, it produces:

| Case | Reported company IRR | Illustrative IRR | Difference, percentage points |
|---|---:|---:|---:|
| Commercial | 8.84% | 8.435871% | -0.404129 |
| Lunar PPP | 15.8% | 14.924946% | -0.875054 |
| Lunar/Mars PPP | 15.4% | 14.864124% | -0.535876 |

These differences quantify one explicit timing assumption; they do not validate the financial reproduction. The demand-derived Mars revenue lowers the illustrative IRR to 14.423978%. The variant that also uses the actual demand ratio gives 13.430324%. These changes are consequences of declared alternatives, not corrections justified by a hidden spreadsheet.

## Preserved discrepancies and ambiguities

- **Scenario labels:** Table 4.9.3 visually labels its columns 1, 3, 4. The prose, demand table, and sensitivity-figure captions use 1, 2, 3. Both label sets are stored; semantic case keys avoid conflating them.
- **Mars revenue:** 1882 t/year times 1000 times $500/kg is $941M/year, while Table 4.9.3 prints $971M/year. Default and demand-derived branches preserve both. The difference is $30M/year, or $240M over the eight Mars-demand years under the stated onset.
- **Scale factors:** page 83 prints 1.0, 1.052 and 1.625, whereas demands imply 1.0, 1.052727273 and 1.710909091. The 1.625 factor resembles the printed Mars cost rows, so the code does not replace it silently. The lunar cost rows also differ slightly from applying the rounded 1.052 factor. Both proportional alternatives are separate.
- **Production/capital summaries:** Table 4.8.7 reports $613.471M production; prose says $613M; Table 4.8.10 uses $614M; Table 4.9.3 uses $613.5M. Table 4.8.10 totals $2559M; adding Table 4.9.3 commercial rows gives $2558.5M. The exact shared launch allocation is $25.666667M, printed as $26M. Each representation has a distinct role; no single rounded number overwrites the others.
- **NASA lifetime headlines:** p.87 says lunar net savings exceed $4B and lunar/Mars savings are $47B. The printed annual savings, investment amounts, ten-year life and third-operating-year Mars onset give $3.925B and $45.005B. The graph's annual phasing and other adjustments are not available numerically, so these claims remain unverified rather than calibrated. NASA capital support is treated as the total in Table 4.9.3; whether additional early PMDev matching should be added is unresolved.
- **Learning curve:** inferred 90% unit learning reproduces the cost table, while the prose's description of 0.9 as an exponent is ambiguous. This inference is recorded rather than hidden.

This model is suitable for inspecting the source's static cost chain and the effects of the explicit alternatives. It is not yet a validated complete historical IRR reconstruction and should not enter an intercomparison as though its original timed financial outputs had been reproduced.

## Audit follow-up

`mars_first_operating_year` is the single onset for delayed demand segments, the printed revenue plateau, and NASA Mars savings. An override moves all three together. The historical lunar/Mars case is unchanged: lunar revenue of $579 million in operating years 1–2 and the printed $971 million plateau from year 3. Commercial and lunar-only cases still start in year 1.

Operating cost is charged in full in every operating year, including the two years before Mars demand. That choice is now explicit in the output. It was not a separately tabulated source schedule.

A surface-price override changes the lunar surface term in NASA savings. It does not change the $1,100/kg Mars cislunar price. Those prices are different source quantities.

Page 82 says one to two winners would each receive $400–800 million in scenario 2 or $800–1,200 million in scenario 3. The reconstruction uses Table 4.9.3's $800 million and $1,200 million. It does not multiply by two winners. Whether the table is one winner or an aggregate is unresolved.

Under `illustrative_uniform_annual`, NASA IRRs are 25.48% and 52.26%, against the reported 27% and 54%. They are part of the same non-reproduction as the company IRRs. The timing weights stay labeled as an analyst scenario. They are not adjusted toward the published IRRs, and the cumulative cash charts are not digitized to invent a schedule.

Table 4.9.5 compares this architecture with Jones et al. (2019), not with the 2020 Moon/Mars paper reconstructed in `models/jones2020`.
