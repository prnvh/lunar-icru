# lunar-icru

This repository is a research project on the reproducible intercomparison of lunar-propellant techno-economic models.

## Revised paper

The revised paper is a seven-page LaTeX article, including references, using the Elsevier `elsarticle` two-column layout. It contains three tables and two quantitative figures:

- [LaTeX-built PDF](research/final-manuscript.pdf)
- [Standalone LaTeX source](research/final-manuscript.tex)
- [Editable article template](research/journal-manuscript.tex)
- [Case-level audit supplement](research/supplement-audit-tables.md)
- [Dated search supplement](research/supplement-search-record.md)

Regenerate the numeric results with the commands below, then run `py -3 analysis/build_journal_paper.py` and `tectonic --keep-logs --outdir research research/final-manuscript.tex`. Edit the article template to revise the text. The builder inserts tables and native TikZ plots from `results/kornuta_reproduction.csv`, `results/surface_offtake_bounds.json`, and `results/surface_offtake_sensitivity.csv`, producing a self-contained LaTeX source. `analysis/build_latex_paper.py` and `research/build_manuscript_tex.py` are compatibility entry points for the same builder. Earlier Markdown drafts and the ReportLab preview builder are retained as superseded work and do not control the final paper.

## Run the papers

```text
py -3 analysis/run_papers.py
py -3 -m unittest discover -s tests -v
py -3 analysis/plot_results.py
```

The numeric pipeline needs only Python's standard library; the optional plot needs matplotlib. Use `python` in place of `py -3` on other systems. Read [executed results](results/summary.md) and [recovery methods](research/recovery-methods.md).

The new recovery phase adds two executable equation investigations and a bounded financial comparison:

- **Harry W. Jones 2021:** forward calculations recover 12 of 16 Table 1 process/rate rows. Literal equations, dimensional repairs and inferred table behavior are separate branches. Some recovered behavior contains probable unit errors.
- **Metzger 2023:** the baseline table and sector equations are now executable. The three terminal launch costs reproduce within 0.54%; the full orbital crossing-year headline remains unresolved.
- **Sowers/Kornuta:** 60 conditional surface-offtake cases and analytic bounds across allowed Sowers spending schedules. Unknown currency years and product equivalence still prevent a strict harmonized historical benchmark.

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
| Part I, historical reproducibility audit | Frozen. Kornuta NPV is executable. Sowers, Charania, and Jones are partial. Blair is outputs only. Pelech is inaccessible. Write-up: [research/manuscript.md](research/manuscript.md). |
| Part II, benchmark-eligible models | The original strict benchmark remains unrun. The search has reopened through executable candidate investigations and conditional bounds; see [recovery methods](research/recovery-methods.md). |

## Current state

Four historical cases remain in `models/`. New recovery investigations live in `experiments/`, with explicit assumptions and generated comparisons in `results/`. Native metrics are preserved; a conditional result is not labeled a reproduced historical headline. Full architecture harmonization and a validated modern model ensemble remain unresolved.

| Case | Native metric | Reproduction status | Run |
|---|---|---|---|
| [Jones 2020](models/jones2020/notes.md) | Undiscounted cumulative ISRU/Earth cost ratio, FY2019 MUSD | Partial. Identifiable sizing and cost equations run; the campaign ratio is unresolved. | `py -3 models/jones2020/model.py` |
| [Kornuta 2019 family](models/kornuta2019/notes.md) | Mining-company NPV at 10% over 10 years | Close match to the seven displayed Table 14 NPVs from the 2018 report's constant cash-flow description. The original workbook was not recovered. | `py -3 models/kornuta2019/model.py` |
| [Sowers NIAC 2020](models/sowers_niac2020/notes.md) | Company IRR, with a static cost and revenue build-up | Static cost chain reconstructs. Original annual phasing and IRRs are unresolved. | `py -3 models/sowers_niac2020/model.py --case commercial` |
| [Charania 2007](models/charania2007/notes.md) | Required sale price at zero NPV, FY2006 USD | Table 2 subtotals match their rows. The price solver is unresolved. | `py -3 models/charania2007/model.py` |

`py -3` is the interpreter on this machine; `python` may be unavailable. Downloaded papers and page images stay local and are gitignored.

Regenerate the reproduction checks with:

```text
py -3 -m unittest tests/test_reproductions.py
```

- [Research specification](paper.md)
- [Model selection and reconstruction specification](research/model-selection-and-reconstruction.md)
- [Project rules](rules.md)
- [Initial literature and evidence review](research/initial-literature-review.md)
- [Comparability crosswalk](research/comparability-crosswalk.md)
- [Published-result validation](research/published-result-validation.md)
- [Methods record](research/methods-record.md)
- [Artifact search](research/artifact-search.md)
- [Reproducibility findings](research/reproducibility-findings.md)
- [Manuscript](research/manuscript.md)
- [Benchmark eligibility](research/benchmark-eligibility.md)
- [Benchmark-model search](research/benchmark-search.md)
- [Benchmark schema, values unset](research/benchmark-schema.json)
- [Decision and activity log](log.md)

The literature review remains an evidence map. Kornuta NPV is the historical financial baseline; Jones 2020 and Sowers NIAC 2020 are partial, and Charania 2007 lacks its price solver. The new Harry W. Jones 2021 experiment is distinct from Christopher Jones's earlier studies. Recovery findings supersede the earlier blanket search closure without retroactively admitting unverified experiments to the historical benchmark.
