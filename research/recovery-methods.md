# Recovering runnable paper calculations

This phase reopens the search at the user's request. The earlier audit records remain useful, but their blanket conclusion that no further calculations could be run was too strong. A missing spreadsheet, an OCR failure, an inconsistent formula and a genuinely unidentified cash-flow schedule require different responses.

## Working distinction

| Evidence situation | Executable approach | Permitted claim |
|---|---|---|
| Complete equations and baseline parameters | Independent forward implementation | Reproduction when published targets agree |
| Conflicting source equations or units | Separately named literal, dimensional, and inferred-computation branches | Reproduction of identified table behavior; no author-confirmed correction |
| Aggregate costs and allowed timing windows | Bounds over every nonnegative spending allocation in the windows | Partial identification conditional on those constraints |
| Unspecified initial experience or economic scaling | Exposed parameter and finite interpretation sensitivity | Conditional model run, not historical headline validation |
| Proprietary cost logic with no equations or observable constraints | Retain unresolved output | No fabricated reproduction |

Candidate code belongs in `experiments/` until its claims are established. Coding an auditable candidate is part of checking reproducibility. The previous rule requiring a headline to be regenerated before any candidate code existed was circular. Admission to the strict historical benchmark still requires evidence; exploratory runs do not automatically qualify.

## Harry W. Jones 2021

The source is [ICES-2021-147](https://ntrs.nasa.gov/citations/20210019592), a different author/model from Christopher Jones2020. The [experiment notes](../experiments/harry_jones2021/notes.md) document page-level equations, units and related primary references.

An Astra source audit and independent forward execution explain most Table 1 calculations. Twelve of sixteen process/rate rows reproduce within the printed 0.5-million-dollar precision. Every cost entry at 100 and 300 t/year matches;100 t/year oxygen extrapolates below the source fit's144 t/year lower bound, whereas300 t/year is in its domain.

The successful branch uses `34*(installed_mass_t/2.2)^0.66`, alongside hydrogen MW numerals used as kW and omission of recycling-container procurement. This is evidence about probable computational behavior. It is not evidence that those units are physically correct, nor an author-approved erratum. No reported cost enters the forward calculations. Expected results are read only by a separate comparison stage.

The model also executes literal Eq. 17 and Eq. 14 with consistent units, with separate combined/separate plant-reactor cost allocation. At300 t/year, the inferred table oxygen LCC is1907.10 MUSD; Eq. 14 gives92716.61 MUSD for combined costing or114676.58 MUSD for separate costing. These changes expose important source-model uncertainty. They do not establish a preferred engineering cost estimate. The printed 10 t/year column and30 t/year oxygen retain discrepancies.

## Metzger 2023

The [arXiv v1 source](https://arxiv.org/abs/2303.09011) contains a legible baseline table on page 50. Original author estimates are legitimate inputs to reproduction, although they remain estimates when evaluating empirical credibility. Full source code is not necessary to execute explicit equations.

The new module runs the reliability, experience, scale, scope, launch and financing equations. Equation 18 reproduces the three reported terminal launch costs within 0.54%. The lunar trajectory remains conditional on exposed initial-experience and scaling choices. The printed Eq. 12/prose discrepancy is preserved as two branches. Table 1 orbital crossing years are not claimed reproduced; the source itself states year 15 in the SEP discussion and 19 in the table for optimistic LEO access. See [implementation notes](../experiments/metzger2023/notes.md).

## Sowers: turn missing timing into a bounded result

For total nonnegative cost `C_j` allocated inside time window `[a_j,b_j]`, its value at commissioning is bounded by:

```text
C_j/(1+r)^b_j <= PV(C_j) <= C_j/(1+r)^a_j, for r >= 0.
```

Summing these independent extrema and subtracting from discounted operating cash gives the exact NPV interval over this class of schedules. A linear objective attains its extrema at the endpoints; a sampled guess is unnecessary. This interval does not assert the historical schedule or reproduce the 8.84% IRR.

Only cost totals and time windows constrain this class. Its endpoints need not be feasible engineering schedules once detailed procurement dependencies are added. The bounds are conservative for any such more constrained schedule inside the same windows; unreported additional cash flows can invalidate that scope.

The scenario was stored in [scenario.json](../experiments/sowers_bounds/scenario.json) before its first comparison execution. It fixes1100 t/year surface offtake,500 source currency/kg,10 operating years,10% discounting and commissioning-date valuation. It retains each historical cost structure. Sowers's construction/deployment windows use the explicit annual-grid interpretation already examined in the prior timing audit. Partial production years, other cash flows, currency normalization and physical product equivalence remain outside the established bounds.

Under those conditions Kornuta's modified NPV is −1463.14M; Sowers's interval is [−681.78,+23.78]M. Break-even prices are 716.47/kg and [496.48,600.87]/kg respectively. This makes the missing Sowers schedule decision-relevant, while leaving its historical headline unresolved.

This is a **conditional financial comparison**, not the formerly proposed fully harmonized physical benchmark. Both source price years are unknown. A shared currency scalar is declared for the comparison, and 0.8/1/1.2 relative cost multipliers are stress cases, not inflation estimates. Native cost boundaries and plant designs remain different. The result does not establish delivered LEO cost, Earth-versus-lunar competitiveness, or the share of historical disagreement caused by model form.

## Reproduce

```text
py -3 analysis/run_papers.py
py -3 -m unittest discover -s tests -v
py -3 analysis/plot_results.py
```

The numerical pipeline and tests use the standard library. The optional plotting step needs matplotlib. `python` can replace `py -3` on systems with a Python3 interpreter under that command. Numeric execution is offline, and source PDF copies are not required. Inputs, code, outputs, targets, source checksums and source-page provenance are retained. Outputs and comparisons are in [results/summary.md](../results/summary.md).
