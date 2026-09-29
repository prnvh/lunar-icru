# Benchmark eligibility

**Recovery-phase update, 2026-09-29:** The user requested further executable reconstruction. Candidate implementations and uncertainty bounds may now be developed in `experiments/` before admission. The seven checks below still govern claims of historical benchmark eligibility; they do not prohibit writing the code needed to perform those checks. The prior search did not prove that no other runnable calculation exists. See [recovery methods](recovery-methods.md) for the Harry W. Jones 2021, Metzger 2023 and Sowers-bound results. The earlier audit below is preserved as a dated record.

This file was written before the search for additional runnable models. It governs Part II. The historical audit in Part I is frozen and is not revised to make a case eligible.

The fixed question is unchanged: when major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

## Two parts

The initial historical sample was selected for influence and structural diversity, not for reproducibility. The reconstruction audit showed that most of those studies cannot be independently rerun from the public record. Controlled intercomparison is therefore restricted to models that meet the rules below. The failed historical cases stay in the results. They are evidence about the literature. They are not dropped, and they are not repaired by invented schedules.

Part I is the reproducibility audit. Part II is the controlled intercomparison, and it uses only benchmark-eligible models.

## Part I, frozen

| Model | Historical importance | Baseline arithmetic check | Headline reproducible | Inputs changeable | Benchmark eligible | Why it stops |
|---|---|---|---|---|---|---|
| Kornuta, 2018 report (`kornuta2019`) | High | Yes | Yes, for NPV | Yes | Yes. Positive control. | The report states a flat yearly cost, ten years, and a 10% discount rate. Cost year is still unresolved. The journal spreadsheet was not recovered. |
| Sowers NIAC 2020 | High | Yes, static totals | No, company IRR | No | No | Totals and durations do not identify one yearly cash-flow table. |
| Sowers 2021 | Restatement of the NIAC case | Same totals | No | No | No | Repeats the IRR table. Not a second model. |
| Charania 2007 | High | Yes, Table 2 subtotals | No, required price | No | No | The zero-NPV schedule is not tabulated. Two WACC figures are printed. |
| Jones 2020 | High | Partial, plant mass and power | No, campaign ratio | No, for the headline | No | Subsystem masses, lander sizing, and the event ledger are missing. |
| Jones 2019 cis-lunar | Separate influential case | No | No | No | No | Costs come from PCEC and PRICE-H. Those tools are not in the paper. |
| Jones 2019 lunar surface | Separate influential case | No | No | No | No | Costs come from unpublished PCEC response surfaces. |
| Blair 2002 | Historical precursor | Printed statements only | No | No | No | The Excel toolkit is not public. |
| Pelech 2019 | Distinct metric, if the text exists | Not checked | No | No | No | No legal open full text in the 2026-09-29 search. |
| Bennett 2020 and 2022 | Descendant | Not an independent model | — | — | No | Reuses parent studies. Not a separate lineage. |
| Metzger 2023 | Critique | Not a baseline model | — | — | No | Comparator. Not a member of the benchmark set. |

Kornuta is the historical positive control. It shows that a published lunar-propellant financial model can be reconstructed and rerun. Its unresolved cost year is a comparability issue when it is paired with another model. It does not remove Kornuta from Part I or from the eligible set.

A later public workbook can move Sowers, Charania, Blair, or a Jones case from this table into Part II. That move requires the file and a log entry. It does not happen by choosing a schedule that hits the printed headline.

## Part II eligibility

A model is benchmark-eligible when an independent researcher can change the inputs and regenerate the model's principal economic output from publicly available information.

Public source code is sufficient when it is the model's calculation, not a plot or a data dump. A complete spreadsheet is sufficient. A paper is sufficient when its equations and baseline parameters are complete enough to rerun the headline without hidden logic. A GitHub repository is not, by itself, a reason to include or exclude a model.

Screen in this order:

1. Relevance. The model addresses lunar propellant, lunar or cislunar resource supply, or a space-resource business case that can answer the lunar-propellant question without being rewritten.
2. Structural distinctiveness. Prefer an independent lineage. Three repositories that implement the same Kornuta architecture count as one model.
3. The reproducibility gate below.
4. The economic-comparability gate, applied per pair, before any shared scenario is run.

### Reproducibility gate

All seven must be true. A miss is recorded. The missing piece is not invented.

1. Identifiable model version: one edition, one date, one file or equation set.
2. Explicit system boundary: product, customer, delivery or sale location, and what costs are inside.
3. Known decision metric: NPV, IRR, price, cost ratio, or another named output, with units.
4. Recoverable calculation: equations, a spreadsheet, or code that a reader can execute. A proprietary tool that is not obtainable fails this item.
5. Recoverable baseline parameters for the published case.
6. The published headline can be regenerated from those parameters.
7. Inputs can be changed and the same calculation returns a new headline. A printed table with no calculation path fails this item.

### Economic-comparability gate

Passing the reproducibility gate does not put a model on the benchmark. For each pair, record whether the product, destination, customer or counterfactual, and economic metric are the same or can be transformed without new model logic. A cash-flow stream that has already been recovered may be reported as NPV at a declared discount rate. A stream inferred from a printed IRR or price may not.

Mars ISRU, asteroid mining, and generic launch-cost code stay outside the primary benchmark unless the public model already answers the lunar-propellant question. Extending them into lunar propellant would be a new model.

### Count and stopping rule

Part II aims at three to five runnable models. Three structurally different models are enough. The search stops when either of these is written down:

- at least three independent models have passed the reproducibility gate and can be paired under the comparability gate, or
- a documented search, covering the sources listed in the search log, finds fewer than three publicly rerunnable lunar-propellant models.

The second condition is the one that occurred. The search log records one eligible model, Kornuta. No pair was formed, and no common benchmark was run.

Kornuta counts as one of the three. The search log is [benchmark-search.md](benchmark-search.md). Candidate code and explicitly conditional outputs belong in `experiments/`; admission to `models/` as a reproduced historical case requires a documented review of the seven items.
