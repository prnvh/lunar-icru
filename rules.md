Write the research question before doing any modeling.
Use one fixed question throughout the project:
When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

Define the contribution narrowly.
The paper is a reproducible intercomparison of existing models. It is not primarily a new lunar-propellant model, a Starship economics paper, or a general review of lunar ISRU.

Define the three sources of disagreement before examining results.
Classify differences as:
input differences, meaning different numerical assumptions;
architecture differences, meaning different physical systems or mission structures; and
model/accounting differences, meaning different equations, cost treatment, financing, replacement, scaling, or decision metrics.

Write a formal inclusion rule for selecting models.
A model should be included only if it contains enough quantitative information to reconstruct its central economic calculation and represents an important or structurally distinct approach in the literature. The operational rule, the versioned roster, and the reproduction grades are in `research/model-selection-and-reconstruction.md`. That file governs selection and reconstruction where it is more specific than this list.

Select approximately four to six models.
Favor structural diversity over model count. A smaller number of well-reconstructed models is better than six weak reconstructions. Select versioned decision cases, not author names.

Acquire every original source associated with each model.
Collect the main paper, appendices, conference papers, theses, reports, supplementary files, spreadsheets, presentations, and earlier papers that define equations or assumptions.

Create one evidence folder for each model.
Keep the original literature separate from your interpretation. Never overwrite or modify source material.

Create a model reconstruction record for every study.
Record every equation, parameter, unit, cost year, physical assumption, architecture assumption, economic rule, output metric, and unclear or missing quantity.

Create a terminology crosswalk.
Determine when different papers use different names for equivalent quantities and when apparently similar quantities are actually different.

Do not harmonize anything during reconstruction.
The first implementation of each model must represent the original study as faithfully as possible, including assumptions that appear outdated, unusual, or inconsistent with other studies.

Build every model as an independent implementation.
Keep separate computational modules such as jones_model, kornuta_model, pelech_model, and so forth. Do not initially force them into one universal equation set.

Separate inputs from equations in the software.
A model implementation should contain the calculation logic, while its original study assumptions should reside in a separate parameter file.

Preserve native model outputs.
If a study evaluates NPV, preserve NPV. If another evaluates delivered cost, opportunity cost, break-even price, IRR, or government program cost, retain that metric. Do not prematurely convert every model into $/kg.

Document every reconstruction judgment.
Whenever the original paper is ambiguous, record what interpretation you used, why you selected it, and how sensitive the reproduction is to that decision.

Never silently invent a missing parameter.
If a required value is absent, classify it explicitly as inferred, derived, obtained from another source, or unresolved.

Reproduce the original published case before doing any comparison.
Run each reconstructed model using its own original assumptions and attempt to reproduce the paper's reported result.

Define reproduction tolerances before evaluating success.
Establish categories such as exact reproduction, close reproduction, approximate reproduction, and unresolved reproduction. Apply the same standard consistently.

Compare intermediate values where possible.
Do not validate a model only because its final answer matches. Check mass flows, transportation quantities, capital costs, operating costs, replacement quantities, production rates, and other intermediate outputs.

Investigate accidental agreement.
Two compensating errors can produce the correct final number. A model is credibly reproduced only when its internal calculation chain is also reasonable.

Report failed reproductions.
If a published result cannot be reconstructed from available information, that is a research finding. Explain exactly what information is missing rather than forcing a match.

Freeze the reconstructed models after validation.
Once a model reproduces its original study, create a tagged or archived version. Any later modifications must be clearly separated from the faithful reconstruction.

Create a common benchmark specification.
Define a single machine-readable scenario containing quantities such as Earth launch cost, annual demand, production rate, plant lifetime, destination, propellant product, transport performance, discount rate, infrastructure assumptions, and analysis period.

Define every benchmark quantity precisely.
For example, do not write simply "launch cost." State whether it means marginal price, fully burdened cost, price to LEO, cost including tanker flights, or another quantity.

Fix units and currency conventions.
Choose a common currency year, real or nominal treatment, mass units, energy units, annualization method, and discounting convention.

Build an adapter between the common scenario and each model.
The adapter should translate the benchmark into quantities that the original model understands without rewriting the model itself.

Record parameters that cannot be standardized.
Some models may require concepts that others do not contain. Mark these explicitly instead of pretending the models are more comparable than they are.

Run the first controlled experiment using common exogenous inputs.
Give every model the same external economic and physical environment while preserving each model's original architecture and accounting logic.

Measure the resulting cross-model dispersion.
Compare outputs using common observable quantities wherever legitimate, while continuing to report native model metrics.

Quantify how much disagreement disappears after input harmonization.
This measures the portion of historical disagreement attributable primarily to different numerical assumptions.

Perform a second harmonization focused on physical architecture.
Where technically possible, align destination, product, transportation chain, reuse assumptions, production scale, infrastructure boundaries, and other physical architecture choices.

Measure the change in dispersion again.
Compare the result with the common-input experiment. This gives evidence about the importance of architecture differences.

Identify remaining model-form disagreement.
Examine differences in capital treatment, development cost, amortization, replacement, depreciation, scaling laws, learning effects, financing, discounting, residual value, infrastructure allocation, and operations treatment.

Do not assume the three effects are perfectly additive.
Inputs, architecture, and accounting rules can interact. Report interaction effects where relevant rather than claiming a false exact decomposition.

Use controlled substitutions to identify important structural causes.
Where practical, change one accounting or modeling rule at a time and observe how much the result moves.

Create a model-feature matrix.
Show which models include development cost, financing, hardware replacement, reusable transport, infrastructure replacement, nonlinear scaling, demand growth, learning curves, residual value, and other important mechanisms.

Distinguish a different answer from a different question.
If one model estimates investor NPV while another estimates government break-even delivered cost, explain that the disagreement partly arises because the models evaluate different decision problems.

Create a standardized reporting layer.
Calculate common comparison outputs only when they can be derived without changing the original meaning of the model.

Define the modern scenario as ranges rather than a single vehicle forecast.
Use ranges for Earth-to-orbit cost, tanker requirements, orbital refueling performance, cislunar transport reuse, lunar lander reuse, ISRU productivity, power-system performance, plant lifetime, and demand.

Keep manufacturer-specific assumptions secondary.
A particular vehicle such as Starship may be represented as one point in the parameter space, but the paper should not depend on one company's projected price or performance.

Run all validated models across the same modern parameter space.
Each model should encounter identical scenario points wherever its structure permits.

Find break-even boundaries for each model.
Determine combinations of demand, plant lifetime, transportation cost, production efficiency, reuse, and other variables at which conclusions change.

Construct model-agreement maps.
Identify regions where all models agree lunar propellant is competitive, regions where all agree it is not, and regions where model choice changes the conclusion.

Treat disagreement regions as a major result.
These regions show where better modeling, empirical data, or clearer accounting conventions are most important.

Run sensitivity analysis within each model.
Determine which parameters drive each model's result and whether different models are sensitive to different variables.

Run uncertainty analysis if the available data permit it.
Use consistent probability distributions or bounded parameter ranges across models and compare distributions of outputs rather than only deterministic point estimates.

Test robustness to benchmark choices.
Repeat the intercomparison using several reasonable common scenarios so the conclusion is not an artifact of one selected benchmark.

Keep historical reproduction separate from modern reinterpretation.
Never replace an old parameter with a modern one inside the replication experiment. Modernization belongs only after successful reproduction.

Maintain a complete provenance trail.
Every numerical input in the repository should indicate whether it came directly from a source, was calculated from source values, was inferred, or was introduced by your benchmark.

Use version control from the beginning.
Preserve model versions, benchmark versions, analysis scripts, figures, and parameter files so every paper result can be regenerated from a specific commit.

Automate the complete analysis pipeline.
One command or script should ideally regenerate the replication tables, benchmark comparisons, sensitivity runs, modern scenarios, and major figures from the underlying model files.

Write tests for equations and unit conversions.
Check rocket-equation calculations, discounted cash flows, mass conversions, annualization, replacement schedules, cost-year adjustments, and other reusable components.

Have another person inspect at least one reconstruction.
Independent checking is particularly valuable because faithful reproduction requires many judgment calls that the original implementer may stop noticing.

Contact original authors when a critical ambiguity cannot be resolved from the literature.
Record the question, response, and resulting model change. Do not make author communication a requirement for inclusion, but use it where it materially improves fidelity.

Do not tune models to produce convergence.
The objective is to discover whether they converge, not to make them converge.

Do not tune models to maximize disagreement either.
Benchmark assumptions should be chosen independently of which conclusion they produce.

Predefine the major benchmark cases before examining their comparative results.
This reduces the risk of choosing scenarios because they make the final story more dramatic.

Write the methods section before interpreting the modern results.
The reader should be able to understand exactly how the experiment works without knowing whether lunar or terrestrial propellant ultimately appears favorable.

Structure the results in the same order as the experiment.
First report reproduction fidelity. Then native-study differences. Then common-input results. Then architecture harmonization. Then model-form analysis. Only after those should you present modern reusable-spaceflight scenarios.

Make reproduction quality visible in the main paper.
Include a table comparing published outputs with reconstructed outputs and numerical reproduction errors.

Make assumptions visible rather than burying them in supplementary material.
Include a compact parameter crosswalk in the main paper and place the full crosswalk in supplementary files or the repository.

Show model structure visually.
Include architecture diagrams or calculation-flow diagrams so readers can see where one model fundamentally differs from another.

Use normalized comparison plots carefully.
Show absolute values when valid, but also consider normalized outputs such as each model's change relative to its own historical baseline.

Report uncertainty around reconstruction choices.
If an ambiguous interpretation changes a model's answer substantially, show both plausible interpretations.

Avoid declaring one historical author correct.
The objective is to identify why models differ and under what conditions their conclusions hold, not to rank authors.

Avoid treating disagreement as error automatically.
A structural difference may represent a legitimate difference in economic perspective rather than a mistake.

State the system boundary for every comparison.
Readers must know whether development, launch vehicles, depots, power systems, mining hardware, propellant losses, financing, replacements, and supporting infrastructure are inside or outside the cost boundary.

Make the decision metric explicit in every major figure.
A graph should never simply say "cost" if one model is reporting price, another levelized cost, and another opportunity cost.

Separate descriptive results from interpretation.
First state what changed numerically. Then explain which structural features appear responsible.

Do not overclaim the modern results.
The analysis can identify conditions under which lunar propellant becomes competitive according to these models. It cannot establish that future launch prices, demand, reliability, or resource performance will actually take those values.

Make the final conclusion conditional.
Prefer conclusions such as:
"Across the reconstructed models, conclusions are robust in these regions of parameter space and model-dependent in these regions."

Identify which uncertainties are empirical and which are methodological.
Empirical uncertainty concerns quantities such as lifetime, ice concentration, demand, or launch price. Methodological uncertainty concerns how models account for costs and value.

Report which additional data would reduce disagreement most.
If plant lifetime dominates uncertainty, say so. If accounting treatment dominates after physical uncertainties are harmonized, say that instead.

Release the code.
Publish every model implementation, parameter file, benchmark definition, analysis script, and plotting script required to reproduce the paper.

Release a machine-readable parameter crosswalk.
Do not leave the crosswalk only as a PDF table. Provide CSV, JSON, YAML, or equivalent structured files.

Include a README explaining exactly how to reproduce every headline result.
A new researcher should be able to clone the repository, run the documented commands, and regenerate the important tables and figures.

Preserve original-model implementations separately from experimental modifications.
Make it impossible for a reader to confuse a faithful reconstruction with one of your harmonized variants.

Archive the final repository permanently.
Use an archival repository that provides a persistent identifier in addition to ordinary version-control hosting.

Write the discussion around what the experiment teaches about the literature.
Explain whether disagreement primarily resulted from assumed worlds, physical architectures, economic accounting, or interactions among them.

Use the modern reusable-spaceflight analysis as the final stress test.
Ask which historical conclusions survive across plausible modern conditions rather than whether one specific future system "wins."

Finish with the model-agreement result.
The strongest conclusion should identify where model choice matters and where it does not.

Use this as the paper's final standard of success.
A reader should be able to answer four questions after reading the work:
Can the historical studies be reproduced? What happens when they model the same world? Why do they still disagree? Under what modern conditions do their conclusions remain robust?

Do not submit until every headline number is reproducible from the public code.
Every major table entry, plot, break-even point, and reported percentage should trace back automatically to a model, parameter file, and analysis script.

Do not judge the project by whether lunar propellant ultimately looks economical.
A finding that every model rejects it, every model supports it, or the models remain divided are all valid outcomes. The scientific contribution is determining why.

Judge the finished paper by one criterion.
If a future researcher wants to understand why the lunar-propellant economics literature disagrees, your paper and repository should become the place where they can inspect the answer rather than reconstructing the entire literature again.