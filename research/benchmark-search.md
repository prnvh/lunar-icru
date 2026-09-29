# Benchmark-model search

Eligibility rules are frozen in [benchmark-eligibility.md](benchmark-eligibility.md). This log starts after that freeze. A repository, paper, or spreadsheet is not eligible because it was found. It is eligible only after the seven reproducibility items and, for any pair, the comparability gate.

## What is in scope

Search for lunar ISRU techno-economic models, space-resource business models, cislunar propellant supply models, and open space-logistics models that already contain a lunar-production calculation. Look in papers, dissertations, Zenodo, GitHub, OSF, and archived NASA, ESA, and university calculation files.

Code, a spreadsheet, or a fully specified equation set can pass. A GitHub link alone does not.

## What is out of scope for the primary benchmark

Mars-only ISRU, asteroid mining, and generic launch economics, unless the public model already answers the lunar-propellant question. Kornuta reimplementations are the Kornuta lineage, not additional models. Bennett stays out as a descendant.

## Stopping rule

Stop when three independent models pass and can be paired, or when this log shows that fewer than three publicly rerunnable lunar-propellant models exist. Kornuta counts as one.

The search is not finished. One model, Kornuta, is eligible. No second model has been admitted.

## Pass of 2026-09-29

Screened for relevance first. Nothing below was coded.

| Candidate | Why it was looked at | Disposition |
|---|---|---|
| Kornuta 2018 report | Positive control already reconstructed | Eligible. Counts as one. |
| Metzger, arXiv:2303.09011 (2023), lunar-propellant cost ratio | Directly about lunar propellant versus Earth launch. The paper writes sector equations, including a cost ratio. No public code or spreadsheet was found. | Not admitted. Part I keeps the critique role. A later pass may test whether the printed equations and a named baseline regenerate one headline. That test has not been done. One calibrated bootstrapping repository (`aniemerg/metzger-bootstrapping-repro`) is a different model, about industry seed mass, and is out. |
| Imperial College / ESA lunar ISRU value-chain model | Cash-flow NPV and IRR for lunar water, oxygen, and propellant | Not eligible now. The project page says the Excel model is internal and will not be published. A Python port is described as planned. |
| `ethene/lunar-horizon-optimizer` | Repository text mentions NPV, IRR, and an ISRU scenario | Not admitted. No published lunar-propellant baseline was identified. A repository is not a model-selection criterion. |
| `dogum/selene-isru` | Lunar industrial-chain simulator with public TypeScript and Python | Out. The repository states it is not a cost model. |
| Steinert et al., Frontiers in Space Technologies, 2024, DOI 10.3389/frspt.2024.1352213, with a public repository | Lunar oxygen plant and delivery to a depot | Not admitted. The published result is a location comparison in mass cost, not a rerun financial headline. Left for a later look only if the repository's calculation is an economic model rather than a map. |
| Zenodo record 22715084, cislunar logistics sustainability, 2026 | Public campaign simulator and CSV inputs | Not admitted. The metric is campaign sustainability, not lunar-propellant cost or value. No lunar-production cost module was identified in the record description. |
| `nickgollins/Space-Mission-Optimization-with-Discrete-Uncertainties-` | Open campaign scheduler | Out. Launch-schedule optimization, not a lunar-propellant business model. |
| Blair, ICEAA 2020, "Cost and Market Modeling for Lunar Mining and Drilling" | Slides name NAFCOM, SOCM, and financial statements | Same Blair lineage as the 2002 report. The slides do not include the workbook. Not a new model. |
| Shishko, ICEAA 2019 | Already in the Part I artifact search | Workbook named, not published. Does not newly qualify Sowers. |

## Still to search

Dissertations with attached workbooks, OSF records, and university or agency archives not covered by the queries above. Sommariva and Cilliers were queried and did not return a public calculation file in this pass. That absence is not yet a completed search of those authors.
