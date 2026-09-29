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

## Pass of 2026-09-29, later the same day

| Candidate | Why it was looked at | Disposition |
|---|---|---|
| Metzger, Acta Astronautica 2023, DOI 10.1016/j.actaastro.2023.03.014, arXiv:2303.09011 | Sector cost-ratio model with equations. Table 1 states years until lunar propellant is cheaper: for the optimistic, moderate, and pessimistic markets, lunar surface, low lunar orbit, and EML1 are year 1; GEO is year 2; DRO is year 3; GTO is years 6, 7, and 7; LEO is years 19, 21, and 23. | Not admitted. Those years are a headline, but they come from a 30-year calculation whose baseline inputs are Table A-1. The appendix says several of those inputs were estimated or taken approximately from other papers' figures. The supplementary discussion is not a calculation file. The extracted parameter table is not clean enough to code. Filling the gaps would invent the model. |
| Bennett and Dempster, Planetary and Space Science 2020, DOI 10.1016/j.pss.2020.104843 | The paper says it reconstructed the Kornuta economic model and applied it to a GTO impulse market. | Retrieved. Mendeley Data 10.17632/ghzjtxzhdf.1, `GTOPaperDataAll.ods`, 161,227 bytes, SHA-256 `de63d2a3ab2d6d0b6b6cc8ec61561575a3413e84ce061d0c7c87e5fd716c934b`, licence CC BY-NC 3.0. The finance sheet is titled “Kornuta Financial Model.” The LEO check is the published $630 million revenue case: −$4.05 billion, then ten years of +$501 million. Dated XNPV at 10% is about −$972.87 million and XIRR is 4.06%, against Table 14's −$972 million and 4%. Not a second lineage. The GTO rows are that same model with a different market. The file stays out of git. |
| Sommariva, Gori, Chizzolini, and Pianorsi, Acta Astronautica 2020, DOI 10.1016/j.actaastro.2020.01.042, and Sommariva et al. 2023, DOI 10.1016/j.actaastro.2023.01.004 | Lunar mining and on-orbit refueling economics, including a Monte Carlo case built on Colorado School of Mines data. | Not admitted. The 2023 university record has no attached file. The papers were not in hand. They may reuse the Mines cost case, which would make them the Sowers or Blair lineage rather than a new one. |
| `open-energy-transition/pypsa-moon` | Public lunar energy-system model with transport costs and ISRU loads. | Out. The decision is a power system for a settlement, not lunar-propellant cost or value. |
| Sercel, Lunar-Polar Propellant Mining Outpost; Kuhns et al., Earth and Space 2021 | Named lunar-propellant concepts. | No public economic workbook found. The public Sercel material that was seen is a thermal-physics model. |

Eligible count remains one: Kornuta. The stopping rule is not met.

## Pass of 2026-09-29, archives and cost equations

| Candidate | Why it was looked at | Disposition |
|---|---|---|
| OSF search for lunar propellant, lunar ice, or ISRU NPV/IRR | Named archive in the search scope | No lunar-propellant economic model in the results. Terrestrial energy and mining projects are out. |
| Sommariva et al. 2020, Bocconi repository | Possible lawful preprint | The repository lists the preprint as private. Not used. |
| Open Lunar Foundation public repositories | Named lunar organization | Trajectory and flight-software tools. No economic model. |
| Cilliers, Rasera, and Hadler, Planetary and Space Science 2020, DOI 10.1016/j.pss.2019.104749 | Open Imperial copy. Lunar oxygen demand. | Out. The result is a regolith mining rate, about 30 kg/h for 1,000 kg/year of oxygen, and 65 kg/h at 95% confidence. It is not a cost, price, or value. |
| Harry W. Jones, ICES-2021-147, NTRS 20210019592 | Public paper. Life-cycle cost of lunar oxygen, hydrogen, and water from mining, Earth supply, or recycling. Oxygen and hydrogen are propellant. This is not Christopher Jones 2020. | Not admitted. The Earth-supply column of Table 1 matches equation 18: for 10, 30, 100, and 300 t/year over 10 years the container costs are 7,447, 14,239, 28,971, and 55,394 million 2021 dollars, and the launch costs are 1,300, 3,900, 13,000, and 39,000. The oxygen-mining plant costs do not. Equation 17 prints 34 times (mass in kg times 2.2) to the power 0.66. For the equation 5 plant at 10 t/year, 10.9 t, that is about 26,400, against the table's 93. Equation 14 with the paper's own coefficients gives about 10,300 for that plant. The mining headline is not regenerated. |

Eligible count remains one: Kornuta. The stopping rule is not met.

## Pass of 2026-09-29, open economic papers

| Candidate | Why it was looked at | Disposition |
|---|---|---|
| Birch, Seidel, and coauthors, Aerospace 2026, 13, 86, “Economic Analysis of a ROXY Pilot Plant” | Open paper. Lunar oxygen and metal plant. Reference case IRR 47.4% with metals and 19.9% for oxygen only. | Not admitted. The plant mass, production, consumables, power, labor, regolith rule, transport prices, and the rounded 200 M€ development cost are printed. The yearly cash flows are Figures 5 and 6. The data statement says the datasets are confidential. A uniform or single-year development spend, using only the printed annual amounts, does not regenerate 19.9% or 47.4%. The development schedule and the 4% carrying-cost treatment are not stated. The mass-reduced development costs in Table 5 are not the Table 3 cost equation either. |
| Pelech, PhD thesis, UNSW, 2023, DOI 10.26190/unsworks/25059 | Open thesis. Lunar water project appraisal by a propellant payback ratio. | Not admitted. Equation 7.16 is PPR = mined product divided by the forgone Earth-launch quantity. The reported lunar results are a cumulative PPR of 0.08 over 40 years for strip mining and 0.33 over 22 years for sublimation. Those results use the demand curve in Figure 7.7 and a mine schedule that is not tabulated. The comet cases are out of scope. |
| “A framework for the economic evaluation of lunar mining projects,” Space and Planetary Resources, 2026 | Open DCF discussion of lunar mining. | Out. The paper states that it does not estimate a project NPV. |
| ISRULib (Technical University of Munich); Space Resources LEIA | Public lunar oxygen process models. | Out. Both estimate mass, power, or energy. Neither states a cost, price, or investment result. |
| Paulson, Balchanos, and Mavris, AIAA 2026-2788 | Lunar water ISRU versus Earth resupply, with a stated 30-year payback. | Not admitted from the abstract. The simulation is described as custom. The full calculation was not in hand. |

Eligible count remains one: Kornuta. The stopping rule is not met.

## Still to search

A lawful Sommariva full text, if one appears. Johnson, ICES-2025-284, if a lawful full text appears; the habitation breakeven numbers in secondary write-ups are not a model. Eligible count remains one.
