> Superseded draft. The current journal-format paper is `final-manuscript.pdf`; its editable source is `journal-manuscript.tex`, with the standalone compiled source in `final-manuscript.tex`.

# Reproducibility and Comparability of Lunar-Propellant Economic Models

Pranav Harikumar, Biswa Ranjan Panda, and Adwik Shankdharan

Independent Researcher, Toram Labs

## Abstract

Published lunar-propellant studies report different economic quantities, often from incomplete public calculations. Before testing whether these models converge under common assumptions, this study audits whether their principal results can be independently reproduced and meaningfully compared. Cases are defined by document version, decision metric, and system boundary. Historical inputs are preserved; missing schedules are bounded rather than fitted to reported results. In the examined record, the Kornuta commercial model is the only independent historical case with a changeable, rerunnable headline: seven reconstructed net present values agree within 0.096%, and all seven internal rates of return round to the reported percentages. Other cases support partial arithmetic checks, diagnostic equation branches, or conditional timing bounds. A surface-offtake experiment gives a Sowers net-present-value interval that crosses zero, demonstrating that unspecified spending timing can affect the decision. However, unresolved currency years, product equivalence, and cost boundaries prevent a strict benchmark. The audit therefore identifies barriers to intercomparison; it does not establish convergence, divergence, or lunar-propellant competitiveness.

**Keywords:** lunar propellant; ISRU; techno-economic models; reproducibility; cash-flow timing; model comparison

## 1. Introduction

The project's research question is: **When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?** Answering it requires two prior tests: each model must reproduce its historical case, and the models must evaluate compatible decision quantities.

The literature spans investor net present value (NPV), company internal rate of return (IRR), government campaign-cost ratios, and break-even sale prices [1-7]. These quantities describe different decisions. A profitable supplier need not minimize a government's campaign cost, and a sale price cannot be compared with delivered cost without specifying product, destination, and financial treatment.

This paper reports the reconstruction stage of the planned intercomparison. It separates **input differences** (numerical assumptions), **architecture differences** (physical systems and mission structure), and **model/accounting differences** (equations, financing, replacement, and valuation). These categories guide interpretation; the present evidence does not support an additive numerical decomposition of their effects.

The contribution is a bounded audit of what the examined publications determine. Successful calculations, unresolved outputs, and conditional experiments are reported separately. Reproducing arithmetic tests fidelity to a publication; it does not validate a future mine, market, or transportation system.

<!-- PAGE -->

## 2. Methods

### 2.1 Case definition and comparability

A case is one source version, economic question, native metric, and system boundary. The 2018 Kornuta report is the financial baseline; its 2019 article belongs to the same lineage [1,2]. Related implementations are not counted as independent evidence. Christopher A. Jones's campaign model [3] and Harry W. Jones's life-cycle analysis [8] are distinct cases.

Before pairing models, we record the decision-maker, metric, product, delivery point, included costs, valuation date, horizon, financing, and cash-flow convention. Differences must be reconciled from documented calculations. Converting every headline to dollars per kilogram is insufficient if doing so requires a new schedule or boundary.

<!-- FIGURE workflow -->

**Figure 1. Audit and comparison sequence.** A missing calculation leads to a partial result or conditional experiment. It does not automatically qualify a case for comparison under common assumptions.

### 2.2 Reconstruction and grading

Historical parameters are kept separate from equations. Forward implementations are checked against published intermediates and final outputs; missing values are not chosen to force agreement. When source equations and units conflict, literal, dimensionally consistent, and inferred table-behavior branches remain separate. Reported targets are comparison data, not fitted forward inputs.

| Grade | Requirement for the named comparison set |
|---|---|
| Exact | Reconstructable intermediates and the named headline round to the printed digits. |
| Close | The stated calculation chain reproduces each tested quantity within 1% or half the last displayed unit, under a documented convention not fitted to the target. |
| Approximate | Structure and direction agree; larger discrepancies are stated and bounded. No case receives this grade here. |
| Partial | At least one equation or table reproduces, while the principal economic output remains unresolved. |
| Unresolved | Available information does not independently determine the central result. Containment in an interval is not reproduction. |

**Table 1. Reproduction grades.** A grade applies to a specified output, not automatically to the entire model. Sign agreement is checked separately from numerical error.

### 2.3 Scope and stopping rule

The historical sample was selected for influence and structural diversity. The subsequent search, dated 29 September 2026, sought at least three independent, rerunnable models that could be paired on a common quantity, or a documented record yielding fewer than three. Seven eligibility checks cover version, boundary, metric, equations, baseline inputs, reproducible headline, and changeable inputs. The search found one eligible lineage. It was not an exhaustive database review; venues, queries, exclusions, and candidate dispositions are retained in Supplement S2.

<!-- PAGE -->

## 3. Audit results

### 3.1 What can be reconstructed?

Table 2 summarizes five historical cases and three related recovery investigations. Only Kornuta passes the rerunnable-headline gate in the examined record. This does not make it a complete common benchmark: an independent compatible partner is still required, and the source currency year remains unresolved.

| Case and native metric | Recovered evidence | Remaining obstacle |
|---|---|---|
| Kornuta 2018/2019 [1,2]: commercial NPV and IRR | Close NPV reproduction; all seven IRRs match after rounding; inputs changeable | No independent compatible partner; currency year unresolved |
| C.A. Jones 2020 [3]: campaign-cost ratio | Plant sizing and cost equations | Incomplete campaign event ledger and subsystem conventions |
| Sowers 2020/2021 [4,5]: company IRR | Static costs, revenue, and undiscounted totals | Annual spending and cash-flow schedule not uniquely specified |
| Charania 2007 [6]: zero-NPV sale price | Capital subtotals | Expenditure and debt timing; conflicting capital-cost rates |
| Blair 2002 [7]: project NPV and return | Accounting identities; present value of a printed income row | Original workbook and return calculation unavailable |
| H.W. Jones 2021 [8]: life-cycle cost | 12 of 16 table rows on an inferred computational branch | Unit/equation conflicts; matching branch not author-confirmed |
| Metzger 2023 [9]: economic crossing years | Three terminal launch-cost intermediates within 0.54% | Inconsistent crossing-year targets and ambiguous replacement term |
| Birch/ROXY 2026 [10]: project IRR | Compatibility intervals under stated timing assumptions | Nonpublic cash-flow data; related life-support customer boundary |

**Table 2. Evidence map.** The final three rows are diagnostic investigations, not additional validated historical benchmark models. Details and per-output provenance are in Supplement S1.

### 3.2 Why a shared topic is not a shared metric

Figure 2 shows the distinction between a physical supply chain and an economic decision boundary. Surface sale, orbital delivery, supplier profitability, and campaign savings can all concern lunar propellant while including different transport, infrastructure, and financing costs. Labels such as “LEO” in a customer scenario do not by themselves establish that a supplier's price includes delivery to low Earth orbit.

<!-- FIGURE boundary -->

**Figure 2. Physical flow and economic boundaries (schematic).** Transport after a surface sale can belong to a different actor. The diagram explains possible boundaries; it is not a reconstructed architecture shared by all audited studies.

<!-- PAGE -->

## 4. Kornuta: a reproducible financial baseline

The 2018 report describes ten operating years, a 10% discount rate, constant annual recurring cost, and end-of-year cash flows [1]. Initial hardware mass is 30,000 kg; hardware and delivery factors are $100,000/kg and $35,000/kg. The initial outlay is therefore $4.05 billion. With annual revenue R and the printed recurring cost of $129 million/year, the reconstructed calculation is:

<!-- EQUATION kornuta -->

The IRR is the discount rate that makes this same cash-flow series' NPV zero. Table 3 uses printed annual revenues rather than adjusting revenue to recover the displayed NPV. Monetary values are millions of source dollars; no inflation conversion is imposed.

| Customer scenario | Revenue/year | Printed NPV | Reconstructed NPV | IRR: solved / printed |
|---|---:|---:|---:|---:|
| Moon | 750 | -234 | -234.22 | 8.64% / 9% |
| EML1 | 1,050 | 1,609 | 1,609.15 | 18.62% / 19% |
| LEO | 630 | -972 | -971.57 | 4.07% / 4% |
| LEO + Moon | 1,380 | 3,639 | 3,636.85 | 28.34% / 28% |
| EML1 + LEO | 1,680 | 5,481 | 5,480.22 | 36.60% / 37% |
| Moon + EML1 | 1,800 | 6,218 | 6,217.57 | 39.81% / 40% |
| All customers | 2,430 | 10,092 | 10,088.65 | 56.16% / 56% |

**Table 3. Kornuta reproduction.** EML1 is Earth-Moon Lagrange point 1; LEO is low Earth orbit. Scenario labels describe customer markets. The mining company's sale boundary is the lunar surface.

All seven NPV signs agree. The maximum relative NPV error is 0.0957%, and the maximum absolute difference is $3.35 million. Three cases differ by more than half the displayed million, so the result is **close**, not exact. All seven solved IRRs round to the published integer percentages.

### 4.1 Timing and precision checks

Moving the same operating flows to the start of each year changes the Moon NPV from approximately -$234.22 million to +$147.35 million. This timing alternative contradicts the report's end-of-year convention and is rejected. It nevertheless shows why valuation rules must be preserved in any comparison.

The recurring-cost components sum to $128 million/year, whereas the report prints $129 million/year. Substituting the component sum moves the Moon NPV to about -$228 million. A separate quantity-times-average-price revenue diagnostic recovers all seven NPVs to their printed millions, suggesting an effect of source precision. Neither diagnostic replaces the declared printed-revenue baseline.

### 4.2 Interpretation

The reconstruction demonstrates that a simple public financial description can be sufficient to regenerate and perturb a principal result without recovering the original workbook. It does not establish realistic future revenue or cost. A later public financial sheet associated with Bennett and Dempster [11] reuses the Kornuta lineage and therefore does not provide an independent second model.

<!-- PAGE -->

## 5. Partial reconstructions and diagnostic branches

### 5.1 Missing schedules and campaign structure

**C.A. Jones [3].** At 17 tonnes/year, the Duke plant equations give 2,262.7 kg and 10.4958 kWe. Assigning that mass among the four printed subsystem cost relationships bounds development cost at $552.6-614.3 million in FY2019 dollars. This does not recover the campaign-cost ratio: launch and replacement events, lander sizing, and subsystem conventions remain incompletely specified.

**Sowers [4,5].** The three static company branches yield undiscounted net cash of $2,155.5 million, $3,125.6 million, and $5,046.9 million. Totals and durations do not uniquely determine the reported IRRs of 8.84%, 15.8%, and 15.4%. Alternative permitted schedules produce different returns. Multiple cash-flow sign changes can also permit multiple IRR roots; they do not by themselves prove that multiple roots exist. Printed and demand-derived Mars revenues of $971 million and $941 million are retained as distinct readings.

**Charania and DePasquale [6].** The Table 2 components sum to $2.721 billion, $5.396 billion, and $5.841 billion in FY2006 dollars. The zero-NPV price calculation additionally depends on capital timing, debt treatment, and a weighted average cost of capital reported as both 21.7% and 22.7%. At 21.7%, timing bounds contain all three published prices, but do not recover a unique schedule. For surface sale, the interval is $14,612-67,611/kg, containing the reported $26,845/kg.

**Blair [7].** Printed accounts balance within $1 million, and retained earnings equal cumulative net income. Discounting the income row at 10%, with the first year undiscounted, gives 4,155.6 and 4,134.4 million against printed NPVs of 4,156 and 4,134 million. This arithmetic agreement does not identify the calculation behind the reported project returns or provide a model that can respond to a new price.

### 5.2 Equation recovery does not validate a whole model

**H.W. Jones [8].** An inferred branch reproduces 12 of 16 process/rate rows within the printed $0.5 million precision. It reverses a mass conversion, treats hydrogen power numerals printed in MW as kW, and omits recycling-container procurement. These are hypotheses about table arithmetic, not physically justified corrections. All cost cells at 100 and 300 tonnes/year match on this branch, although 100 tonnes/year oxygen lies outside the stated production-fit domain. At 300 tonnes/year, inferred oxygen life-cycle cost is $1,907.10 million; dimensionally consistent alternatives yield approximately $92,717 million or $114,677 million, depending on plant/reactor cost allocation. None is certified here as the preferred engineering estimate.

**Metzger [9].** The launch-cost equation gives 30.0178, 119.6332, and 437.3721 against printed terminal costs of 30, 119, and 436, with relative errors of 0.059%, 0.532%, and 0.315%. These intermediate matches do not reproduce the complete orbital crossing-year result. An optimistic LEO case is identified as year 15 in the text and year 19 in the table; the replacement-cost term also admits alternative readings.

**Birch/ROXY [10].** This related pilot-plant study serves early life-support demand, so its customer boundary is distinct. When transport is paid in the delay year, moving development spending within its stated window gives IRR intervals of 19.8-24.6% for oxygen and 41.1-64.3% with metals. These contain the reported 19.9% and 47.4%. Moving transport to the first operating year raises the oxygen lower bound to 22.7%, excluding 19.9%. Compatibility identifies a timing condition, not the original confidential schedule.

<!-- PAGE -->

## 6. What timing bounds can establish

For a nonnegative cost C incurred at an unknown time t within [a, b], and discount rate r at least zero, present value decreases with later payment:

<!-- EQUATION bounds -->

For independently placeable costs, summing their endpoint extrema gives the exact interval over the declared timing class. If procurement or sequencing couples expenditures, the same calculation is an outer bound: its endpoints may not be jointly feasible. These intervals are neither confidence intervals nor recovered historical schedules. Additional unreported cash flows fall outside the calculation.

### 6.1 Conditional surface-offtake experiment

The stored scenario specifies 1,100 tonnes/year of surface offtake, 500 currency units/kg, ten operating years, 10% discounting, and valuation at commissioning. Each model retains its historical cost totals and included cost categories. Sowers spending can move within explicitly defined annual construction windows. The comparison assumes a common unit of account; it does not assert that the source dollars have a common purchasing power.

<!-- FIGURE intervals -->

**Figure 3. Conditional NPV at commissioning.** The Sowers interval spans all nonnegative spending allocations in the declared windows. The Kornuta marker is a modified scenario result. Neither is a new reproduction of a historical headline. Values come from the generated surface-offtake calculation.

| Output | Kornuta modified case | Sowers timing class |
|---|---:|---:|
| NPV, million common account units | -1,463.14 | [-681.78, +23.78] |
| Break-even surface price, account units/kg | 716.47 | [496.48, 600.87] |

**Table 4. Conditional comparison.** Break-even prices set each scenario's NPV to zero. They are not harmonized estimates of delivered propellant cost.

Sowers's NPV changes sign across the allowed schedules, so missing timing is decision-relevant in this experiment. Kornuta remains negative at the stated price. The numerical gap cannot be attributed solely to accounting: plant designs, source cost years, product equivalence, construction costs, and system boundaries are not fully aligned. Sixty rate/price/cost-multiplier sensitivity cases are provided in the repository; the multipliers are stress assumptions, not estimated inflation adjustments.

### 6.2 Status of the planned benchmark

No independent compatible pair passed both gates. Consequently, no controlled common-input convergence test, architectural harmonization, or validated modern model-agreement map is reported. The conditional experiment establishes what a declared set of timing assumptions permits. It does not rank the historical studies or establish Earth-versus-lunar competitiveness.

<!-- PAGE -->

## 7. Discussion and limitations

### 7.1 What the audit explains

The examined record reveals obstacles that arise before a shared economic comparison. Kornuta makes the effect of cash-flow timing explicit. Sowers lacks the schedule needed to identify IRR. Charania's reproducible capital totals do not determine a financed sale price. Jones's subsystem equations do not determine a campaign ledger. Blair's accounting statement does not expose a changeable investment model. The recovery investigations further distinguish unit ambiguity, intermediate equation agreement, and timing compatibility.

These findings identify sources of potential disagreement, but cannot measure how much disagreement would remain after common inputs and architecture. Empirical uncertainties concern quantities such as productivity, demand, and hardware life. Methodological uncertainties concern valuation, allocation, and cost boundaries. Neither category can be ranked across models from the present audit alone.

### 7.2 Limits of the evidence

The search is a documented screening exercise, not a systematic review of all publications. Scopus, Web of Science, and IEEE Xplore were not queried; hit counts were not retained. A candidate absent from the screening record was not adjudicated. “Unavailable” means not recovered in that record, not proof that a file does not exist. New public artifacts could change eligibility after a documented re-audit.

Several reconstructions depend on rounded tables rather than original workbooks. Chart curves were not digitized, source cost years were not invented, and ambiguous branches were not reconciled by fitting. Timing extrema apply only to the declared schedule classes. An inferred branch that matches a table is not an author-approved erratum. The pilot-plant investigation also has a different early customer from a bulk propellant market.

### 7.3 Requirements for a controlled intercomparison

A useful model release should provide executable equations or a workbook, machine-readable baseline inputs, source units and currency year, annual cash flows, and an event ledger for development, deployment, operations, replacement, and financing. Product, delivery location, customer, and included infrastructure should be explicit. Publishing a principal result together with intermediate checks would help distinguish arithmetic reproduction from compensating errors.

With a second independent compatible model, a pairwise test becomes possible; the original search target remains at least three. The next steps would preserve native metrics, harmonize exogenous inputs, align architecture where defensible, and test accounting substitutions. Interactions should be reported rather than forcing input, architecture, and accounting effects into an exact additive split.

## 8. Conclusion

Within the examined public record, Kornuta is the only independent historical case whose principal financial calculation can be regenerated and rerun with changed inputs under the stated gate. Other studies yield useful partial checks, diagnostic branches, and timing bounds, but not a second compatible historical headline. The planned convergence question therefore remains open. The defensible result is an evidence map of what the publications determine and what further disclosure is needed to compare them.

### Reproducibility and supporting material

Run `py -3 analysis/run_papers.py`, then `py -3 -m unittest discover -s tests -v`. The numeric pipeline uses Python's standard library; all 17 tests passed during this revision. Generated results and input/code hashes are in `results/`. Supplement S1 contains case-level audit tables; Supplement S2 preserves the dated search record. The LaTeX source is generated by `analysis/build_latex_paper.py` and compiled from `research/final-manuscript.tex`.

<!-- PAGE -->

## References

[1] D. Kornuta et al., Commercial Lunar Propellant Architecture: A Collaborative Study of Lunar Propellant Production. LPI Contribution 2142, Lunar and Planetary Institute, 2018. https://repository.hou.usra.edu/handle/20.500.11753/1245

[2] D. Kornuta et al., Commercial lunar propellant architecture: a collaborative study of lunar propellant production. REACH 13 (2019), 100026. https://doi.org/10.1016/j.reach.2019.100026

[3] C.A. Jones, A.R. Pensado, M.A. Clark, M.L. Grande, M.L. Ivanco, E.L. Judd, J.J. Klovstad, D.M. Reeves, Cost breakeven analysis of lunar in-situ propellant production for human missions to the Moon and Mars. ASCEND 2020, AIAA 2020-4041. https://doi.org/10.2514/6.2020-4041

[4] G.F. Sowers, Thermal Mining of Ices on Cold Solar System Bodies. NIAC Phase I Final Report, Colorado School of Mines, 2020. https://space.mines.edu/wp-content/uploads/sites/134/2020/03/Thermal-Mining-NIAC-Phase-I-final-report.pdf

[5] G.F. Sowers, The business case for lunar ice mining. New Space 9 (2021), 77-94. https://doi.org/10.1089/space.2020.0045

[6] A.C. Charania, D. DePasquale, Economic analysis of a lunar in-situ resource utilization (ISRU) propellant services market. 58th International Astronautical Congress, 2007, IAC-07-A5.1.03. https://www.sei.aero/archive/IAC-07-A5.1.03.pdf

[7] B.R. Blair, J. Diaz, M.B. Duke, E. Lamassoure, R. Easter, M. Oderman, M. Vaucher, Space Resource Economic Analysis Toolkit: The Case for Commercial Lunar Ice Mining. Final report to the NASA Exploration Team, 20 December 2002. https://nss.org/wp-content/uploads/2017/07/2002-Case-For-Commercial-Lunar-Ice-Mining.pdf

[8] H.W. Jones, Should oxygen, hydrogen, and water on the Moon be provided by Earth supply, life support recycling, or regolith mining? 50th International Conference on Environmental Systems, 2021, ICES-2021-147. https://ntrs.nasa.gov/citations/20210019592

[9] P.T. Metzger, Economics of in-space industry and competitiveness of lunar-derived rocket propellant. Acta Astronautica 207 (2023), 425-444. https://doi.org/10.1016/j.actaastro.2023.03.014

[10] T.F. Birch, A. Seidel, J.E. Johnson, G. Poehle, U. Pal, Economic analysis of a ROXY pilot plant supporting early lunar mission architectures. Aerospace 13 (2026), 86. https://doi.org/10.3390/aerospace13010086

[11] N.J. Bennett, A.G. Dempster, Geosynchronous transfer orbits as a market for impulse delivered by lunar sourced propellant. Planetary and Space Science 193 (2020), 104843. https://doi.org/10.1016/j.pss.2020.104843

### Supplements

**S1. Case-level audit tables.** `research/supplement-audit-tables.md` records inputs, named comparison outputs, discrepancies, and unresolved quantities.

**S2. Dated search record.** `research/supplement-search-record.md` preserves the prior manuscript's search appendix, including its full candidate roster and bibliography cross-reference to Pelech et al. (2019), Acta Astronautica 162, 388-404, https://doi.org/10.1016/j.actaastro.2019.06.030. Numerical labels in S2 refer to the original audit bibliography.
