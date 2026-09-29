# Methods record

This is the reproducibility record for the study, not a project-status note. A blocked reconstruction is a result: the public source did not contain enough information to reproduce the headline. The fixed question is unchanged.

When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

## Current objective

The study is two linked parts. Part I keeps every historical case that was audited, including the ones that cannot be rerun. Part II compares only models that pass the eligibility rules in [benchmark-eligibility.md](benchmark-eligibility.md). Those rules were fixed before the search for further runnable models.

Kornuta remains the positive control. Its constant end-of-year cash flows reproduce the seven printed NPVs closely, and the rates of return of those same flows round to the printed table. It is eligible for Part II. Sowers, Charania, Jones, Blair, and Pelech stay in Part I and are not benchmark-eligible on the public record audited here.

## Comparison gate

Cross-model benchmark experiments may begin only when at least two independently reconstructed models can evaluate the same explicitly defined decision quantity without introducing unsupported model logic.

The shared quantity does not have to be each model's native headline. If a cash-flow stream has been faithfully reconstructed, NPV at a declared discount rate is a transparent transformation of that stream. Inventing the stream so that a reported IRR or price is hit is not.

Numerical benchmark values stay unset. The empty schema is [benchmark-schema.json](benchmark-schema.json).

## Two families

Models are compared inside a family. Differences between families are reported as different questions, not as a spread in one dollar-per-kilogram variable.

| Family | Cases | What would make a pair |
|---|---|---|
| Financial and business | Kornuta; Sowers, if its cash flows are recovered; Charania, if its financing schedule is recovered; Blair, if the workbook or an equivalent calculation is recovered | Two explicit cash-flow or price calculations that answer one stated estimand |
| Program and campaign cost | Jones 2020; Bennett only as a descendant of a parent, not as another vote | A reconstructed campaign ledger, still not forced into the Kornuta NPV |

One admissible finding is that much of the apparent disagreement cannot be represented as disagreement over a common dependent variable, because the studies answer different decision questions.

## Dispositions

| Case | Disposition | Why this is evidence |
|---|---|---|
| Kornuta 2018 report, `kornuta2019` | Baseline for NPV | End-of-year cash flows match the table's signs. Start-of-year timing flips the Moon case positive, so that alternative is ruled out by the published numbers. The cost year is still unresolved. |
| Jones 2020 | Separate campaign-cost track | The native quantity is an undiscounted cumulative cost ratio. The campaign ledger is missing, so the ratio stays unresolved. It is not an input to the Kornuta experiment. |
| Sowers NIAC 2020 | Static cost chain recovered; company IRR blocked | See the sufficiency proof below. |
| Charania 2007 | Blocked on the required price | Table 2 subtotals match their rows. The zero-NPV price is not tabulated. Page 6 states the headline prices at 22.7% WACC and Table 4 states 21.7% for the same prices. No debt schedule is guessed. |
| Pelech 2019 | Conditional | No legal open full text. It does not enter a claimed reconstruction. |
| Blair 2002 | Conditional | The public download is the report PDF. The Excel toolkit has not been found. The report is not treated as the workbook. |
| Bennett; Metzger 2023 | Not independent votes | Descendants and a critique. Sparse reconstructable baselines make double-counting them more misleading, not less. |

## Sowers IRR: the public packet is not sufficient

Milestone: reproduce the reported company IRRs (8.84%, 15.8%, 15.4%) from an explicit annual cash-flow table, or show that the public packet cannot supply that table.

What the NIAC report does tabulate, in Table 4.9.3 and the Section 4.8 cost build-up: development, production, and transportation totals; annual operations; a surface price of $500/kg; annual revenue; NASA investment totals; and the IRRs. Ground rules on pages 81–82 add a four-year full-scale development and production span, an 18-month deployment, a ten-year operating life, and Mars demand from the third operating year. Page 82 also describes earlier public phases as ranges: several winners, award bands, and an unquantified cost match, then one to two winners over a five-year full-scale phase.

What it does not tabulate: annual or quarterly investment, the split of development versus production inside the four years, milestone weights, the company's share of any cost match, replacement events, taxes, depreciation, debt draws, or a terminal value. Figures 4.9.5 and 4.9.9 plot cumulative cash. They are not data tables and were not digitized. The report's own prose says IRR is a function of the time-dependent cash streams.

Those duration windows do not identify one IRR. `models/sowers_niac2020/timing_nonuniqueness.py` applies three schedules that all stay inside the stated windows. They are demonstrations, not reproductions.

| Schedule inside the stated windows | Commercial IRR | Lunar PPP IRR | Lunar/Mars IRR |
|---|---:|---:|---:|
| Uniform across each window | 8.4359% | 14.9249% | 14.8641% |
| Front-loaded inside each window | 7.2902% | 13.3563% | 13.3618% |
| Back-loaded inside each window | 10.1517% | no single IRR | no single IRR |
| Table 4.9.3 | 8.84% | 15.8% | 15.4% |

The uniform and front-loaded schedules both have a unique company IRR, and those IRRs differ. Neither matches the table. The back-loaded public-private schedules change sign more than once, so a single IRR is not even defined. The published IRR is therefore not recoverable from the printed totals plus the stated durations.

Artifact search on 2026-09-29, aimed at workbooks rather than another narrative paper:

- The Mines release page links the NIAC PDF only. Grant 80NSSC19K0964 has no public supplemental workbook in that search.
- Shishko's 2019 ICEAA note describes sheet names for a thermal-mining workbook, including cash flow, and does not publish the annual series or the file.
- No public `.xlsx` or `.xls` for this business case was found.

**Result:** `sowers_niac2020` company IRR is blocked. The static cost and revenue chain remains a partial reconstruction. An NPV at a common discount rate will not be computed until an explicit cash-flow table is in hand. Obtaining that table requires the workbook or another primary tabulation, not a fitted schedule.

## Fork result

The public artifact search is recorded in [artifact-search.md](artifact-search.md). Sowers 2021 repeats the NIAC IRR table and does not add annual cash flows. Shishko 2019 names workbook sheets and does not publish them. Blair's report prints Version 5 statements and a toolkit primer; the Excel file is not public, so those statements cannot be rerun and do not open the gate. Charania's financing file was not found.

Part I is that reproducibility audit. The findings are in [reproducibility-findings.md](reproducibility-findings.md). `py -3 -m unittest tests/test_reproductions.py` regenerates the checks. Part II does not reopen these cases by inventing their missing schedules. It looks for other lunar-propellant models that already can be rerun. Pelech still waits on lawful full text.

The two 2019 Jones papers were checked as campaign-cost sources, not as a way to fill `jones2020`. The lunar-surface paper prices plants and landers with unpublished PCEC response surfaces. The cis-lunar paper prices elements with PCEC and PRICE-H. Neither file is public, so neither case is coded. Their reported headlines stay reported.
