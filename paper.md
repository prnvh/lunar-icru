# Research Specification

Model selection, reproduction grades, and the reconstruction procedure are specified in [research/model-selection-and-reconstruction.md](research/model-selection-and-reconstruction.md). The reproducibility record, comparison gate, and the decision that benchmark values stay unset are in [research/methods-record.md](research/methods-record.md). Those documents govern if this file disagrees with them on selection, grades, or which outputs may enter a comparison. The experiment design below remains the design for a comparison that has not yet opened. The write-up of the closed search is [research/manuscript.md](research/manuscript.md).

## 1. Working title

**Model or Assumption? A Reproducible Intercomparison of Lunar-Propellant Techno-Economic Models**

## 2. Research objective

Reconstruct major published lunar-propellant economic models, verify that the reconstructions reproduce their published results, and subject the validated models to identical benchmark scenarios in order to determine how much disagreement between studies results from:

1. Different numerical inputs.
2. Different physical or mission architectures.
3. Different economic, accounting, and model-form rules.

The validated models will then be evaluated across a common modern reusable-spaceflight parameter space to determine which historical conclusions remain robust.

## 3. Primary research question

**When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?**

The same wording is used in the project rules and the selection specification. Disagreement is attributed to inputs, architecture, and model or accounting structure only after the comparison is shown to ask the same question.

## 4. Secondary research questions

1. Can the major published lunar-propellant economic models be independently reproduced from publicly available information?

2. How large is the disagreement between the models under their original assumptions?

3. How much of that disagreement disappears when major exogenous assumptions are harmonized?

4. How much additional disagreement disappears when physical and transportation architectures are harmonized?

5. What disagreement remains because of accounting conventions, financing assumptions, scaling rules, replacement treatment, cost allocation, or other model-form choices?

6. Which model parameters dominate the result within each model?

7. Under what modern reusable-launch and reusable-cislunar-transport conditions do the models agree that lunar propellant is competitive?

8. Under what conditions do the models agree that lunar propellant is not competitive?

9. In what regions of parameter space does the economic conclusion depend strongly on which model is used?

## 5. Central hypothesis

The published disagreement in lunar-propellant economics is expected to result from both different assumed worlds and different model structures.

The study will test whether harmonizing external assumptions substantially reduces the spread in model results.

No assumption will be made beforehand that the models should converge.

## 6. Null interpretation

A possible result is:

**Once common inputs and architectures are imposed, the models produce substantially similar conclusions.**

This would indicate that most historical disagreement arose from different assumptions rather than fundamentally different economic models.

## 7. Alternative interpretation

A second possible result is:

**Substantial disagreement remains after common inputs and architectures are imposed.**

This would indicate economically important model-form uncertainty.

Both results constitute valid findings.

## 8. Unit of analysis

The principal unit of analysis is a versioned decision case: one source edition, one decision question, one native metric, and one system boundary.

An author name is not a case. Separate editions and campaign questions stay separate. Descendant reanalyses and later critiques are not additional baselines. The target size is about four to six baselines, chosen so that each adds a distinct decision problem.

The current roster, grades, and exclusions are maintained in the selection specification, not in this section.

## 9. Model inclusion criteria

A case is included only when all four gates in the selection specification pass:

1. The principal published result is identified and is not a digitization of a figure.
2. The central economic calculation can be recomputed from the obtainable source.
3. The case is structurally distinct from baselines already included.
4. The product, customer, location, and cost boundary can be stated.

A case whose central calculation cannot be reconstructed even approximately remains in the evidence map. A partial reconstruction may be documented and may contribute only the named outputs that were actually recovered.

## 10. Conceptual decomposition

Differences between studies will be classified into four levels.

### Level 1 — External inputs

Examples:

- Earth launch cost
- Discount rate
- Annual demand
- Resource concentration
- Hardware lifetime
- Production rate
- Power-system performance
- Vehicle performance
- Technology efficiency

### Level 2 — Physical architecture

Examples:

- Mining method
- Processing architecture
- Propellant type
- Destination
- Transportation chain
- Depot architecture
- Reusable versus expendable vehicles
- Number of transportation stages
- Power architecture
- Hardware replacement architecture

### Level 3 — Economic and accounting structure

Examples:

- Development-cost treatment
- Capital expenditure treatment
- Amortization
- Depreciation
- Financing
- Discounted cash flow
- Replacement treatment
- Cost scaling
- Learning curves
- Fixed versus variable costs
- Residual value
- Infrastructure allocation
- Government versus commercial cost treatment

### Level 4 — Decision metric

Examples:

- Delivered cost per kilogram
- Break-even price
- Net present value
- Internal rate of return
- Opportunity cost
- Lifecycle cost
- Government program cost
- Undiscounted cumulative cost ratio

A difference at this level is a different question until the metric-compatibility gate says otherwise. It is not automatically model-form disagreement, and it is not removed by converting every output to one dollar-per-kilogram figure.

## 11. Required software architecture

Each historical model must exist as an independent computational implementation.

Example structure:

```text
/models
    /jones2020
        model.py
        original_inputs.json
        reported_outputs.json
        reproduction.json
        source_manifest.json
        notes.md
    /kornuta2019
        ...
    /sowers_niac2020
        ...
```

Parameters live with the case, in JSON. A second edition is a new directory. Cases do not import one another.

The historical models must not initially be rewritten into one common mathematical model.

## 12. Separation of components

Each implementation should distinguish:

```text
Model equations
        +
Parameter set
        +
Architecture definition
        +
Output adapter
```

This separation enables controlled substitution during later experiments.

## 13. Phase I — Source reconstruction

For each model:

1. Obtain all relevant papers and supplementary material.

2. Extract equations.

3. Extract numerical inputs.

4. Extract architecture assumptions.

5. Extract economic/accounting rules.

6. Identify the original output metric.

7. Identify the principal published numerical result.

8. Record all ambiguities.

9. Record all undocumented assumptions required for implementation.

10. Create a source-to-parameter traceability table.

## 14. Provenance requirement

Every numerical parameter must be classified as one of:

- Directly reported.
- Derived from reported values.
- Taken from another cited publication.
- Inferred from figures or text.
- Assumed by the reconstruction.
- Unresolved.

No undocumented values may silently enter a model.

## 15. Phase II — Historical replication

For each model:

```text
Original model logic
+
Original study inputs
=
Reconstructed original result
```

The reconstruction should reproduce both final and intermediate published values wherever those values are available.

## 16. Reproduction metric

For each named output, report the absolute error in source units and the relative error

\[
E = \frac{|R_{reconstructed}-R_{published}|}
{|R_{published}|}
\]

when the published value is not zero or small enough to make \(E\) misleading. Also report whether the sign or the inequality direction matches. Relative error is a reported number, not the grade.

Grades apply to one named output: exact, close, approximate, partial, or unresolved, as defined in the selection specification. Percentage bands are not used as pass thresholds. A matching headline with an unchecked intermediate chain is not accepted as exact or close.

## 17. Replication acceptance rule

Native results may be displayed at any grade, with the grade visible. Unresolved headlines stay unresolved.

A named output may enter a common-input, architecture, or model-form comparison only when its grade is exact, close, or approximate, and the metric-compatibility gate says the compared cases are answering the same question. A partial case may contribute a recovered relationship, such as a published sizing equation, only through an adapter field that does not fill a recorded blocker.

Do not tune equations, allocations, or unstated schedules to move a case across that threshold.

## 18. Phase III — Parameter crosswalk

Construct a cross-model parameter matrix.

Example fields:

| Concept | Case A | Case B | Same quantity? | If not, why |
|---|---|---|---|---|
| Launch cost | ... | ... | no, until destination and burden match | surface delivery price versus Earth-to-orbit price |
| Lifetime | ... | ... | no, until the clock is the same | flight counts versus operating years |
| Demand | ... | ... | no, until location matches | surface sale quantity versus delivered mass |
| Discount rate | ... | ... | only if both models discount | an undiscounted campaign has no rate to harmonize |

The crosswalk records a common definition only where the meanings match. It must not assign one dollar-per-kilogram definition to metrics that answer different questions.

## 19. Phase IV — Common benchmark

Define at least one reference scenario.

The benchmark must specify:

### Economic environment

- Currency year
- Real or nominal costing
- Discount rate
- Analysis duration
- Demand
- Demand growth

### Product

- Propellant type
- Product state
- Delivery location
- Required delivered quantity

### Lunar production system

- Resource concentration
- Production rate
- Plant mass
- Plant life
- Availability
- Power demand
- Replacement assumptions

### Transportation system

- Earth-to-orbit cost
- Vehicle performance
- Refueling assumptions
- Cislunar transfer performance
- Lunar ascent/descent performance
- Reuse counts
- Propellant losses

## 20. Benchmark rule

Benchmark values must be chosen before examining the comparative model results.

They should not be selected to maximize either convergence or disagreement.

## 21. Phase V — Experiment A: Native studies

Run:

```text
Model_i + NativeInputs_i + NativeArchitecture_i
```

Purpose:

Establish the original cross-study disagreement.

## 22. Phase VI — Experiment B: Common external inputs

Run:

```text
Model_i + CommonInputs + NativeArchitecture_i
```

Purpose:

Measure how much disagreement remains after differences in exogenous assumptions are removed.

## 23. Phase VII — Experiment C: Common inputs and physical architecture

Where technically possible, run:

```text
Model_i
+
CommonInputs
+
CommonArchitecture
```

Purpose:

Determine how much additional disagreement arises from differences in physical architecture.

Not every model will necessarily support every architecture.

Unsupported combinations must be marked rather than forced.

## 24. Phase VIII — Model-form investigation

Examine the disagreement remaining after the preceding harmonization.

Candidate structural causes include:

- Development cost
- Discounting
- Financing
- Hardware replacement
- Nonlinear scaling
- Learning
- Infrastructure treatment
- Fixed/variable cost treatment
- Capacity utilization
- Residual value
- Revenue treatment
- Amortization
- Cost allocation

## 25. Structural substitution experiments

Where the model architecture permits it, replace one rule at a time.

Example:

```text
Original case
        ↓
replace one stated rule
        ↓
observe the change in that case's own metric
```

Repeat for major structural rules.

This establishes causal evidence about which model features generate disagreement.

## 26. Interaction effects

The study must not assume:

```text
Total disagreement
=
input effect
+
architecture effect
+
model effect
```

because the terms may interact.

Interaction effects should be reported when material.

If feasible, use factorial, permutation, or Shapley-style decomposition to estimate contributions without depending entirely on one substitution order.

## 27. Primary intercomparison outputs

At minimum report:

1. Native model result.
2. Reconstructed original result.
3. Reproduction error.
4. Common-input result.
5. Common-input/common-architecture result where possible.
6. Comparable standardized output.
7. Native decision metric.
8. Difference from ensemble median or other non-evaluative reference statistic.
9. Sensitivity to principal variables.

## 28. Cross-model disagreement metric

Use multiple dispersion measures where appropriate.

Possible measures:

- Range
- Interquartile range
- Standard deviation
- Coefficient of variation
- Maximum/minimum ratio

For outputs that cross zero, avoid misleading ratio-based statistics.

## 29. Phase IX — Sensitivity analysis

For each model, identify sensitivity to:

- Launch cost
- Demand
- Plant life
- Production rate
- Plant mass
- Resource concentration
- Power cost/mass
- Transportation reuse
- Discount rate
- Hardware replacement
- Capacity utilization

Use identical parameter ranges where the models permit identical interpretation.

## 30. Phase X — Modern reusable-spaceflight experiment

Define a modern scenario space instead of one single forecast.

Candidate dimensions include:

- Earth-to-LEO cost
- Launch cadence
- Reusable upper-stage assumptions
- Orbital refueling
- Cislunar tug reuse
- Lunar lander reuse
- Propellant boiloff
- ISRU productivity
- Plant lifetime
- Power-system specific mass
- Annual demand

## 31. Modern scenario principle

Manufacturer-specific systems may be included as named reference cases, but the principal analysis should use technology/performance ranges rather than depend on one manufacturer's projected economics.

## 32. Break-even analysis

For each model identify critical surfaces such as:

\[
C_{launch}^{*}
\]

\[
D^{*}
\]

\[
L_{plant}^{*}
\]

where the economic conclusion changes.

Compare these break-even boundaries across models.

## 33. Model-agreement analysis

For every sampled scenario classify the ensemble response.

Possible categories:

```text
Strong agreement: lunar-derived propellant competitive
Strong agreement: Earth-supplied propellant competitive
Mixed model result
Model not applicable
```

The exact agreement threshold should be predefined.

## 34. Core visualization

Produce model-agreement maps.

Example:

```text
                    Plant lifetime
                         ↑

              lunar agreement
                    ███████
                 ██████████
              ░░███████████
            ░░░░░██████████
          Earth   mixed

                         → demand
```

The important result is the location and size of the disagreement region.

## 35. Robustness tests

Repeat the main analysis under:

- Multiple benchmark scenarios.
- Alternative plausible interpretations of ambiguous historical parameters.
- Alternative currency/cost-year treatment where appropriate.
- Different modern technology ranges.
- Different demand assumptions.
- Different model inclusion sets.

## 36. Required main-paper tables

### Table 1
Selected studies and their objectives.

### Table 2
Model architecture comparison.

### Table 3
Economic/accounting rule comparison.

### Table 4
Parameter crosswalk.

### Table 5
Published versus reconstructed results.

### Table 6
Common benchmark results.

### Table 7
Attribution of major differences.

### Table 8
Modern break-even results.

## 37. Required main-paper figures

### Figure 1
Research architecture.

### Figure 2
Calculation architecture for each reconstructed model.

### Figure 3
Original versus reproduced results.

### Figure 4
Cross-model dispersion under native assumptions.

### Figure 5
Cross-model dispersion after common inputs.

### Figure 6
Cross-model dispersion after architecture harmonization.

### Figure 7
Sensitivity comparison.

### Figure 8
Modern parameter-space agreement map.

### Figure 9
Break-even boundary comparison.

## 38. Main paper structure

1. Introduction
2. Previous lunar-propellant economic studies
3. Research design
4. Model selection
5. Reconstruction methodology
6. Reproduction results
7. Common benchmark definition
8. Controlled model intercomparison
9. Attribution of disagreement
10. Modern reusable-spaceflight scenarios
11. Robustness and uncertainty
12. Discussion
13. Limitations
14. Conclusions

## 39. Main contribution statement

The intended contribution is:

**A validated computational intercomparison of independently reconstructed lunar-propellant economic models that separates disagreement caused by external assumptions from disagreement caused by physical architecture and economic model structure.**

## 40. Minimum publishable result

The study succeeds if it can:

1. Reconstruct at least three structurally different versioned cases, with a grade on each named output.

2. Report unresolved headlines as unresolved rather than forcing them into the comparison.

3. Run the outputs that pass the compatibility gate under at least one predeclared common benchmark.

4. Show how the spread of those comparable outputs changes after harmonization.

5. Identify specific structural reasons for important remaining disagreements, including disagreements that are different questions rather than different answers.

The project does not require lunar propellant to be found economically favorable.

## 41. Strong-result criterion

The strongest version additionally provides:

1. Four to six validated models.
2. Multiple common benchmarks.
3. Quantitative decomposition of disagreement.
4. Sensitivity and uncertainty analysis.
5. Modern reusable-spaceflight parameter sweeps.
6. Break-even surfaces.
7. Model-agreement maps.
8. Fully open computational implementations.

## 42. Reproducibility requirement

All headline results must be regenerable from public code and parameter files.

Repository should contain:

```text
/models/<case_id>/     equations, native parameters, manifests, notes
/research/             evidence map, selection specification, later crosswalks
/benchmarks/           only after the compatibility gate is filled
/tests/
/analysis/
/figures/
```

Parameter files stay inside each case directory so a historical default cannot be confused with a benchmark.

## 43. Required metadata for every parameter

Each parameter should contain:

```text
name
symbol
value
units
source
source location
cost year if applicable
interpretation
confidence
native/common status
```

## 44. Quality-control rules

1. No silent assumptions.
2. No changing equations to improve agreement.
3. No changing benchmark values after seeing results without documenting the change.
4. No conversion between economic metrics without documenting the transformation.
5. No comparison of quantities with materially different system boundaries without warning.
6. No claim of exact decomposition when interaction effects remain.
7. No use of modern assumptions during historical reproduction.
8. No model declared incorrect merely because it disagrees with another model.

## 45. Principal validity threats

The study must explicitly discuss:

### Reconstruction uncertainty
The original study may not provide enough implementation detail.

### Definition mismatch
Nominally identical variables may represent different concepts.

### Architecture incompatibility
Some models may be inseparable from their original physical system.

### Metric incompatibility
NPV, opportunity cost, government cost, and delivered price do not represent identical decisions.

### Historical-data quality
Older technology assumptions may be poorly documented.

### Modern-scenario uncertainty
Future reusable-system cost and performance remain uncertain.

### Researcher discretion
Model reconstruction may involve judgment calls.

## 46. Mitigation strategy

Address these threats through:

- Full provenance.
- Explicit crosswalks.
- Alternative reconstruction cases.
- Sensitivity analysis.
- Independent code checking.
- Public source code.
- Clear distinction between native and standardized outputs.
- Predefined benchmark scenarios.

## 47. Final analytical question

After all experiments, the paper should be able to answer:

**When apparently contradictory lunar-propellant economic studies are required to describe the same physical and economic world, how much disagreement survives, and exactly where does that disagreement come from?**

## 48. Final deliverables

The completed research project should produce:

1. A peer-reviewed paper.
2. Four to six independently reconstructed models if feasible.
3. Historical reproduction results.
4. A model-definition and parameter crosswalk.
5. Common benchmark specifications.
6. Cross-model comparison results.
7. Structural disagreement analysis.
8. Modern reusable-spaceflight sensitivity results.
9. Break-even and agreement maps.
10. Open-source model implementations.
11. Machine-readable input files.
12. Complete reproduction instructions.

## 49. Project success condition

The project is complete when another researcher can:

```text
download repository
        ↓
run historical models
        ↓
reproduce published-study comparisons
        ↓
run common benchmark
        ↓
reproduce cross-model disagreement
        ↓
change assumptions
        ↓
regenerate the main conclusions
```

without needing undocumented information from the author.