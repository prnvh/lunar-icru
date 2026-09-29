# lunar-icru

This repository is a research project on the reproducible intercomparison of lunar-propellant techno-economic models.

## Research question

When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

## Current state

Three versioned reconstructions are implemented as separate modules. Each keeps its original assumptions in a parameter file and its equations in `model.py`. No common benchmark, architecture harmonization, or modern scenario has been run. Native metrics are preserved, and a result stays unresolved when the source does not supply the missing quantity.

| Case | Native metric | Reproduction status | Run |
|---|---|---|---|
| [Jones 2020](models/jones2020/notes.md) | Undiscounted cumulative ISRU/Earth cost ratio, FY2019 MUSD | Partial. Identifiable sizing and cost equations run; the campaign ratio is unresolved. | `py -3 models/jones2020/model.py` |
| [Kornuta 2019 family](models/kornuta2019/notes.md) | Mining-company NPV at 10% over 10 years | Close match to the seven displayed Table 14 NPVs from the 2018 report's constant cash-flow description. The original workbook was not recovered. | `py -3 models/kornuta2019/model.py` |
| [Sowers NIAC 2020](models/sowers_niac2020/notes.md) | Company IRR, with a static cost and revenue build-up | Static cost chain reconstructs. Original annual phasing and IRRs are unresolved. | `py -3 models/sowers_niac2020/model.py --case commercial` |

`py -3` is the interpreter on this machine; `python` may be unavailable. Downloaded papers and page images stay local and are gitignored.

- [Research specification](paper.md)
- [Model selection and reconstruction specification](research/model-selection-and-reconstruction.md)
- [Project rules](rules.md)
- [Initial literature and evidence review](research/initial-literature-review.md)
- [Comparability crosswalk](research/comparability-crosswalk.md)
- [Decision and activity log](log.md)

The literature review remains an evidence map. The selection specification is the current roster: Kornuta NPV is a baseline, Jones 2020 and Sowers NIAC 2020 are partial, and Charania 2007 is queued. Pelech, Blair, and the other Jones editions stay conditional.
