# lunar-icru

This repository is a research project on the reproducible intercomparison of lunar-propellant techno-economic models.

## Research question

When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

## Pipeline

| Step | State |
|---|---|
| Research question, architecture, literature review, candidate identification, methodological rules | Done |
| Source packets | Done for Jones 2020, Kornuta 2018/2019, Sowers NIAC 2020, and Charania 2007. Jones 2019, Pelech, Blair, and Sowers 2021 are still conditional. |
| Versioned specifications and parameter extraction | Done for the four packets above. Each case has notes and a parameter file. |
| Model reconstruction | Kornuta NPV is a baseline. Jones 2020 and Sowers NIAC are partial. Charania's cost subtotals check, and its required price does not. |
| Published-result validation | Recorded in [research/published-result-validation.md](research/published-result-validation.md). |
| Common benchmark, cross-model experiments, disagreement attribution, modern sweeps, paper | Not opened. The comparison gate requires a second model that can answer a Kornuta-commensurable question. Benchmark fields exist and their values are unset. Sowers company IRR is blocked. |

## Current state

Four versioned cases are implemented as separate modules. No common benchmark, architecture harmonization, or modern scenario has been run. Native metrics are preserved, and a result stays unresolved when the source does not supply the missing quantity.

| Case | Native metric | Reproduction status | Run |
|---|---|---|---|
| [Jones 2020](models/jones2020/notes.md) | Undiscounted cumulative ISRU/Earth cost ratio, FY2019 MUSD | Partial. Identifiable sizing and cost equations run; the campaign ratio is unresolved. | `py -3 models/jones2020/model.py` |
| [Kornuta 2019 family](models/kornuta2019/notes.md) | Mining-company NPV at 10% over 10 years | Close match to the seven displayed Table 14 NPVs from the 2018 report's constant cash-flow description. The original workbook was not recovered. | `py -3 models/kornuta2019/model.py` |
| [Sowers NIAC 2020](models/sowers_niac2020/notes.md) | Company IRR, with a static cost and revenue build-up | Static cost chain reconstructs. Original annual phasing and IRRs are unresolved. | `py -3 models/sowers_niac2020/model.py --case commercial` |
| [Charania 2007](models/charania2007/notes.md) | Required sale price at zero NPV, FY2006 USD | Table 2 subtotals match their rows. The price solver is unresolved. | `py -3 models/charania2007/model.py` |

`py -3` is the interpreter on this machine; `python` may be unavailable. Downloaded papers and page images stay local and are gitignored.

- [Research specification](paper.md)
- [Model selection and reconstruction specification](research/model-selection-and-reconstruction.md)
- [Project rules](rules.md)
- [Initial literature and evidence review](research/initial-literature-review.md)
- [Comparability crosswalk](research/comparability-crosswalk.md)
- [Published-result validation](research/published-result-validation.md)
- [Methods record](research/methods-record.md)
- [Benchmark schema, values unset](research/benchmark-schema.json)
- [Decision and activity log](log.md)

The literature review remains an evidence map. The selection specification is the current roster: Kornuta NPV is a baseline, Jones 2020 and Sowers NIAC 2020 are partial, and Charania 2007 is blocked on its unpublished price solver. Pelech, Blair, and the other Jones editions stay conditional.
