# Model selection and reconstruction specification

This document governs which versioned cases enter the study and how each one is reconstructed. It is more specific than the experiment design in [paper.md](../paper.md) and the conduct rules in [rules.md](../rules.md). If those files disagree on the unit of selection, inclusion, reproduction grades, or what may enter a harmonized comparison, this document governs. The fixed research question does not change:

When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

The contribution remains a reproducible intercomparison of existing models. A new lunar-propellant model, a vendor-specific vehicle study, or a general ISRU review is out of scope.

## 1. Unit of selection

The unit is a **versioned decision case**: one source edition, one decision question, one native metric, and one system boundary.

An author name is not a model. Jones 2019 cislunar, Jones 2019 lunar-surface, and Jones 2020 Moon/Mars are different cases. The Sowers NIAC Phase I report and the later Sowers journal business case are different cases until a source audit shows they implement the same calculation. A directory may carry a literature-family name, but `notes.md` must name the exact document, edition, and result being reproduced. A second edition gets its own directory.

Select about four to six baselines. Prefer one strong case per decision problem over several weak cases from the same family.

## 2. What does not count as another baseline

These may be used. They do not count as additional independent votes in a model-agreement claim.

| Role | Treatment |
|---|---|
| Descendant or reanalysis | Bennett's papers reuse Jones, Kornuta, and Charania. Record them as architecture or accounting variants of the parent case, with shared-source provenance. |
| Analytical critique | Metzger (2023) is a comparator. Verify its mapping of earlier studies. Do not treat it as a neutral adjudicator or as a member of the matched benchmark set. |
| Same calculation, new prose | A later paper that republishes an earlier case without a new equation set stays attached to the earlier case. |
| Illustrative timing or rounding branch | A declared alternative inside a reconstruction is not a new model. |

## 3. Inclusion gates

Include a case only when all four gates pass. A failed gate is a recorded finding, not a prompt to invent the missing piece.

1. **Primary-result recoverability.** The principal published result is identified, including its units, cost year, and the table, equation, or prose location. A figure without a numeric table is not a reproduction target. Do not digitize a graph to create one.
2. **Calculation recoverability.** The central economic calculation can be recomputed from published equations, tables, or an obtainable workbook. Component masses, costs, and financing rules needed by that calculation are either stated or explicitly unresolved. Proprietary packages that cannot be obtained (CABAM, StageSizer, ProbWorks, PCEC, PRICE-H, an unreleased workbook) limit the claim to what the paper itself supports.
3. **Distinctiveness.** The case adds a decision problem, physical architecture, or accounting structure not already represented by an included baseline.
4. **Documented boundary.** The product, customer, sale or delivery location, and cost boundary can be stated. Quantities that only look similar to another case are marked non-equivalent.

Approximate reconstruction is allowed. A case whose central calculation cannot be reconstructed even approximately stays in the evidence map and out of the baseline set.

## 4. Decision problems to cover

The target set is one baseline for each row that passes the gates. Do not add a second baseline that only repeats a row.

| Decision problem | Native question | Preferred case | Why this case |
|---|---|---|---|
| Government campaign cost ratio | Is cumulative ISRU architecture cost below cumulative Earth-delivery cost? | Jones 2020, and only for outputs its sources support | Published plant-sizing and cost-estimating relationships. The 2019 papers are separate cases, not backfill for 2020. |
| Delivered campaign cost | What is architecture cost per net kilogram delivered? | Jones 2019 cislunar, if the published costs can be recomputed without the missing cost-model artifacts | Different metric and campaign from Jones 2020. |
| Commercial mining-company value | Does the mine have positive NPV at the stated discount rate? | Kornuta family, 2018 report economic section | Constant cash-flow NPV is documented and has been reconstructed. |
| Required customer price | What price must be charged for the financed venture to clear its hurdle? | Charania and DePasquale 2007, if a cash-flow schedule is obtained | The public paper states the prices and the cost stack. It does not tabulate the NPV calculation, so this row is not yet filled. |
| Thermal-mining production company | What are the company's cost, revenue, and return under commercial and public-private cases? | Sowers NIAC 2020 for the static cost and revenue chain | Distinct architecture and PPP boundary. The journal case is not automatically the same model. |
| Opportunity cost | What is given up relative to launching the same resource from Earth? | Pelech, Roesler, and Saydam 2019, if the full text is obtained | The metric is not NPV, IRR, or price. |
| Early private-investment pro forma | What investor return does a lunar ice venture show under the toolkit's finance? | Blair et al. 2002, if the report's equations suffice | Historical precursor. The announced Excel toolkit is not yet shown to be public. |

## 5. Current roster

Status values: **baseline** (native metric may be cited), **partial** (named recovered outputs only), **queued** (next reconstruction, not yet coded), **conditional** (blocked on a source), **not a baseline**.

| Case id | Status | Native metric | What may be cited now |
|---|---|---|---|
| `kornuta2019` | baseline for NPV | NPV of a constant 10-year cash flow, source USD, cost year unresolved | Seven scenario NPVs from the printed revenue path. The quantity-times-printed-price path is a rounding diagnostic, not a silent replacement. ROR is not reconstructed. Break-even price in the module is a derived report, not a published result. |
| `jones2020` | partial | Undiscounted cumulative ISRU/Earth cost ratio, FY2019 million USD | Phase demand, Table 5 mass and power at a stated rate, and cost-estimating relationships when their own subsystem masses are supplied. The campaign ratio is unresolved. |
| `sowers_niac2020` | partial | Company IRR; static costs in source USD, cost year unresolved | Component development, production, deployment, operations, and stated revenues, with printed inconsistencies kept as separate branches. Calculated IRR is unresolved. Illustrative uniform timing is not a reproduction. |
| `charania2007` | blocked on the price solver | Required sale price, FY2006 USD | Source packet recorded from the public 17-page paper. Table 2 subtotals match the sum of their rows. The zero-NPV price is unresolved: cash flows are not tabulated, and both 21.7% and 22.7% WACC are printed for the same prices. Not a baseline. |
| `jones2019_cislunar` | conditional | Reported cost per net delivered kilogram, FY2018 USD | Not coded. Include only if the central cost can be recomputed without the unrecovered PCEC/PRICE-H artifacts. Do not import 2020 cost-estimating relationships. |
| `jones2019_surface` | conditional | Cumulative campaign cost and breakeven | Not coded. Distinct from both other Jones cases. Include only after its own source packet passes the gates. |
| `pelech2019` | conditional | Opportunity cost versus direct Earth launch | Not coded. No open full text was available in the evidence review. |
| `blair2002` | conditional | Investor NPV/IRR and related pro-forma results | Not coded. The report is public; the Excel toolkit has not been shown to be public. |
| `sowers2021` | conditional | Journal business case; confirm before equating with the NIAC report | Not a second copy of `sowers_niac2020`. |
| Bennett 2020 and 2022 | not a baseline | Descendant metrics | Use only as labeled variants of a parent. |
| Metzger 2023 | not a baseline | Analytical critique | Comparator. |

Changing a status requires a log entry stating the gate that changed and the source location.

## 6. Reproduction grades

Grade **one named output**, not an author. Report absolute error in source units and relative error. Relative error alone is not a grade when the published value is zero or small. Sign agreement is reported separately from magnitude error.

Declare the comparison set before inspecting the reconstructed numbers. The categories below are the project standard. The older percentage bands in earlier drafts of `paper.md` are retired.

| Grade | Meaning |
|---|---|
| Exact | Intermediates that the source reports, and the named headline, match within the source's own rounding. |
| Close | The calculation chain is the published one, and the gap is explained by displayed rounding or a stated timing convention that was not fitted to the target. |
| Approximate | The structure and the direction of the result match, and a material numerical gap is explained and bounded. |
| Partial | Some named equations or tables reproduce, and the native headline stays unresolved because a required input is missing. |
| Unresolved | The central calculation cannot be recomputed from the available source. |

Current grades, from the executed modules:

- Kornuta NPV, printed-revenue path: **close**. All seven signs match. The largest absolute gap versus the displayed NPV is about $3.35 million on the all-customers case. The same cash flows' rates of return round to all seven printed Table 14 rates. Start-of-year discounting flips the Moon case from negative to about +$147 million, so that timing is ruled out. The $128 million component cost does not round to the printed NPVs.
- Jones 2020 campaign ratio: **partial**. Demand totals, Duke Table 5 mass 2,262.7 kg, and power 10.4958 kWe at 17 t/year are recovered. The ratio is null.
- Sowers NIAC component totals: **close** where the independent arithmetic matches the printed table within rounding. Company and NASA IRRs: **unresolved**. The Mars revenue inconsistency stays unresolved in either direction.

A failed or partial reproduction is reported. It is not repaired by tuning.

## 7. Admission to experiments

| Experiment | Who may enter | On what |
|---|---|---|
| Native display | Any coded case | Its graded outputs, with the grade visible. Unresolved headlines are shown as unresolved. |
| Common exogenous inputs | Baselines, plus a partial case only through a named recovered relationship | A metric that is graded exact, close, or approximate, and that passes the compatibility gate. |
| Architecture harmonization and model-form swaps | Same as common inputs | Only rules the original model actually contains. Unsupported combinations are marked, not forced. |
| Modern parameter space | Cases that passed a historical reproduction for the output being swept | Modern values never replace historical inputs inside the reproduction experiment. |

Jones's cost ratio, Kornuta's NPV, and Sowers's IRR are not converted into one dollar-per-kilogram headline. A standardized output is allowed only when it can be derived without changing the decision the model was built to answer, and it is labeled as derived.

## 8. Metric-compatibility gate

Before two cases are compared on a quantity, record:

- decision question
- native metric and units
- currency year, and whether the dollars are real or nominal
- product and its state
- customer
- where the product is sold or delivered
- system boundary, including development, transport, power, financing, replacement, and government support
- time structure: discounting, lifetime, and campaign phases

If any of those differ in meaning, the comparison is non-comparable for that quantity. Similar words are not enough. In the current cases, surface sale quantity is not delivered mass, launch price to the lunar surface is not Earth-to-orbit price, a five-flight lander life is not a five-year plant life, and breakeven as a cost ratio below one is not a zero-NPV price.

No common benchmark is frozen until this gate has been filled for every pair that the benchmark claims to compare. The current three-case record is [comparability-crosswalk.md](comparability-crosswalk.md). Its result is that no pair shares a native question. Kornuta and Sowers are the nearest company-side pair, and they remain blocked by cost year, the meaning of the shared $35,000/kg delivery figure, and cash-flow timing. Jones and Sowers's NASA savings ask related government questions across different ownership boundaries. Sowers Table 4.9.5 compares thermal mining with Jones et al. (2019), not with `jones2020`.

Do not digitize an unpublished cash-flow chart to manufacture the missing Sowers schedule. A figure is not a reproduction target. If the schedule cannot be recovered from tables, the IRR stays unresolved.

## 9. Reconstruction record

Each case lives in `models/<case_id>/` and is imported by no other case.

| File | Role |
|---|---|
| `model.py` | Equations only. Standard library. `run(inputs) -> dict` copies inputs, rejects unknown overrides, and returns null plus an explicit blocker for anything unresolved. |
| `original_inputs.json` | Historical values with units, source location, and provenance. This file is the native case. |
| `reported_outputs.json` | Published numbers kept separate from the calculation. |
| `reproduction.json` | Output of the historical run, written from an execution, not typed in as a target. |
| `source_manifest.json` | Retrieval date, URL, identifier, checksum, and page pointers. |
| `notes.md` | The reconstruction record: question, boundary, equations, ambiguities, grades, and exclusions. |
| `native_case.json` | Only when the paper is a sweep and the run must declare which published point was selected. |

Local PDFs, page images, and extracted full text stay untracked. They are inspection aids, not repository artifacts.

Provenance of every number is one of: directly reported, derived from reported values, taken from a cited source, inferred, analyst override, or unresolved. Unresolved stays null. An analyst override is a later experiment, never a new historical default.

## 10. Reconstruction conduct

1. Reproduce the published case before any harmonized scenario.
2. Check intermediates that the source actually reports: masses, component costs, revenues, and replacement quantities. A matching headline with an unchecked chain is not a credible reproduction.
3. Keep each printed inconsistency as its own branch. Do not average it away. Known examples are Charania's two WACC statements, Sowers's scenario labels, Mars revenue, and scale factors, and Kornuta's $129 million versus $128 million recurring-cost expressions.
4. Do not calibrate an unstated schedule, allocation, or learning exponent so that a published IRR, NPV, or cost ratio is hit. A learning rule or timing profile may be implemented only when several independent published rows support that interpretation, and the notes must say so. Sowers's 90% unit learning is that kind of inference; an IRR-matching spend profile is not.
5. Do not import another case's parameters to fill a gap. Jones 2020 cost-estimating relationships do not fill Jones 2019. A descendant must cite the parent value it reuses.
6. Do not treat a selected point inside a published sweep as the paper's universal baseline. Mark it as a selection.
7. Leave currency year and real/nominal treatment unresolved when the source does not state them.
8. Freeze a case by recording its grade and the commit that produced `reproduction.json`. Later edits are either corrections, with a log entry, or experiments outside the historical default.

## 11. Order of work

1. Keep the three existing modules inside the grades in section 6. Do not invent Jones's campaign ledger or Sowers's annual phasing.
2. `charania2007` is recorded and blocked. Do not invent its cash-flow schedule. A later workbook, if obtained, is a new reconstruction, not a silent fill of this one.
3. Decide `jones2019_cislunar`, `pelech2019`, and `blair2002` by applying section 3 to their source packets. Absence of a workbook or full text keeps the case conditional.
4. Write the metric-compatibility gate for every pair that a future benchmark would compare.
5. Only then freeze a common benchmark, before looking at comparative results.

## 12. Selection success

The selection succeeds when a reader can see which decision problems are represented, which cases were rejected or left conditional and why, and which named outputs are allowed into a comparison. It does not succeed by reaching six directories.
