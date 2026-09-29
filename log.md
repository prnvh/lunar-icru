# Decision and activity log

**Purpose:** Maintain an auditable record of consequential research actions, decisions, results, and concise rationales. This log records outcomes and evidence; it does not expose private chain-of-thought or verbatim hidden reasoning.

## 2026-09-29 — Initial repository review and research

### Repository review

- Inspected the complete top-level repository and Git state. The repository is on `main`, one initial commit exists, and the working tree initially contained untracked `paper.md`, `rules.md`, and an empty `log.md`; the tracked `README.md` was a one-line title.
- Read the research specification and project rules. The fixed subject is a reproducible intercomparison of lunar-propellant techno-economic models; the repo did not yet contain model code, source files, benchmark data, analysis, or results.
- **Decision:** Preserve `paper.md` and `rules.md`; create a separate evidence review and make `README.md` a navigation/status page. **Rationale:** those untracked files contain substantive user-authored project work, while the literature review is an evidence artifact that can evolve without rewriting the agreed study design.

### Delegated research

- Started three Astra research workstreams: (1) Jones, Kornuta, and Pelech source/model evidence; (2) Charania–DePasquale, Bennett, and Sowers source/model evidence; (3) methods and current lunar technology/transport evidence.
- **Decision:** Ask agents for primary sources, reconstruction details, ambiguities, and inclusion assessments, without repository edits. **Rationale:** parallel source review broadens coverage while keeping evidence and responsibility for repository changes with this task.
- Consolidated their findings in [the initial literature review](research/initial-literature-review.md). Agent observations in that review are treated as preliminary source research and still need page/figure-level checks during actual implementation.

### Research and model-selection decisions

- **Decision:** Treat a specific, versioned model and decision case—not an author name—as the unit of candidate selection. **Rationale:** Jones has separate cislunar, lunar-surface, and Moon/Mars cases; Bennett's papers reuse Jones, Kornuta, and Charania; Sowers has a thermal-mining report and a later journal case.
- **Decision:** Preserve native metrics and require a metric-compatibility gate before a cross-model comparison. **Rationale:** company NPV/IRR, campaign cost per delivered kilogram, required sale price, and opportunity-cost ratios answer different questions. Converting all of them to one `$ / kg` measure could alter their meaning.
- **Decision:** Treat Bennett's Jones re-analysis as a model descendant/architecture variant, not an independent “vote”; keep the GTO service and parity-pricing papers as related extensions. **Rationale:** their own publications describe reconstruction or reuse of earlier model inputs and economics.
- **Decision:** Treat Metzger (2023) as a significant analytical critique and comparator, not as a neutral adjudicator. **Rationale:** it makes explicit model-form claims about earlier studies and also advances a general result about lunar-propellant competitiveness; independently verify its mapping and equations.
- **Decision:** Keep Blair et al. (2002) on the candidate list pending a search for its announced Excel toolkit. **Rationale:** it is an early private-investment model with documented demand, architecture, and finance, but full report access does not demonstrate that the original workbook is retrievable.
- **Decision:** Make Pelech (2019) conditional for a complete replication until the full paper/model is available. **Rationale:** the primary abstract and introduction are accessible, but this research pass did not find an open full text or model artifact.
- **Decision:** Record source-level inconsistencies rather than repair them silently. **Rationale:** Charania's WACC is 21.7% in its tables/plots versus 22.7% in prose; Sowers's NIAC report has scenario-label and revenue/scaling inconsistencies in a printed table. A reconstruction must keep original values and identify alternatives.
- **Decision:** Version-lock Jones papers separately. **Rationale:** the 2019 cislunar study, 2019 lunar-surface study, and 2020 Moon/Mars extension use different campaign questions and source detail; the 2020 cost-estimating relationships should not be backfilled into a 2019 replication.
- **Evidence anchors from primary-source review:** Charania reports FY2006 required prices of $26,845/kg (surface), $133,947/kg (LLO), and $7,053,265/kg (GEO); Kornuta's report supports a close DCF reconstruction (30,000 kg mine, $4.05B initial investment, 10-year horizon, 10% discount, source-reported case NPVs); Jones 2019 reports six architecture-case costs but relies on cost-model artifacts not located in this pass; Jones 2020 publishes plant-sizing and cost-estimating relationships; Sowers's NIAC report has source-table inconsistencies verified against its page image. These are review anchors, not reproduced model outputs.
- **Decision:** Keep Pelech conditional for a replication claim. **Rationale:** no open full text or executable model was found in this pass, so the published opportunity-cost calculation cannot yet be independently checked beyond accessible abstract/introduction evidence.

### Modern-scenario evidence decisions

- **Decision:** Frame modern technology as a parameter space of evidence classes rather than one vendor forecast. **Rationale:** NASA demonstrator tests and engineering studies support specific subsystem anchors, while mine-scale resource grade, plant life, service costs, and orbital propellant transfer remain prospective or uncertain.
- Checked NASA and USGS source material on lunar water and ISRU demonstrations and the July 2026 GAO major-project review. The sources distinguish remote evidence for water from mine-ready deposit characterization; a 2025 NASA vacuum test demonstrated oxygen extraction from simulant rather than an integrated production plant; GAO reported that a critical orbital storage/transfer technology in SpaceX's lunar plan had not yet been demonstrated as of May 2026.
- **Decision:** Do not derive probability distributions from scenario ranges unless evidence or explicit expert elicitation supports them. **Rationale:** the cited engineering sweep values and design goals are not probability samples.

### Repository changes made

- Replaced the one-line `README.md` with project navigation and an accurate status statement.
- Added `research/initial-literature-review.md` with the literature map, source links, preliminary reconstruction notes, comparability rules, current-evidence boundary, and next actions.
- Added this log. `paper.md` and `rules.md` remain unchanged.
- No model code or scientific results were added, and no tests were run because this documentation-only research task did not request testing.

### Next decisions requiring evidence

- Choose four to six versioned model cases after inspecting full source packets and companion artifacts.
- Decide whether Blair (2002) is reconstructable enough for the main set.
- Acquire complete Pelech text before claiming a reproduction.
- Set a predeclared functional unit, common service/destination, system boundary, cost year, and currency convention before running harmonized scenarios.
- Freeze an evidence-backed benchmark version and distinguish reported measurements, engineering extrapolations, program targets, and analyst stress cases.
- If implementation reveals material gaps or ambiguities, add the resolution, rationale, source location, and affected model version here before changing an input or equation.

## 2026-09-29 — Model reconstruction and controlled comparison

- Continued from the evidence review into independent Jones 2020, Kornuta 2019, and Sowers NIAC 2020 implementations, using separate model directories and source-specific parameter files. The user explicitly asked for Astra agents and autonomous continuation; each workstream is constrained to one model and to source-supported inputs.
- **Decision:** Keep an action/decision/evidence log with concise rationales, not verbatim hidden reasoning. **Rationale:** the repository can audit what changed and why while preserving private chain-of-thought.
- **Decision:** Keep downloaded primary-source PDFs and rendered page images as local inspection material; commit source manifests, citations, source-derived parameter records and model code instead. **Rationale:** retain source traceability without redistributing complete copyrighted papers or screenshots.
- **Source correction:** Removed the NTRS identifier 20190004974 from the Kornuta citation after retrieval showed that it identifies Cohen et al.'s _Lunar Flashlight_. The model uses the matching USRA repository PDF and DOI instead. **Rationale:** only a verified matching source can support parameter extraction.
- **Reconstruction boundary:** Jones 2020's published plant total mass does not uniquely provide the subsystem allocations needed by its published cost-estimating relationships. Do not synthesize the missing campaign cost from assumed allocation. Return identifiable physical and cost intermediates and expose the unresolved native total.
- **Reconstruction boundary:** Sowers NIAC report's source case labels and arithmetic do not reconcile, and annual cash flows/IRR timing are not tabulated. Keep each printed result distinct and do not calibrate invented annual phasing to force an IRR match.
- The controlled experiment will be frozen only after confirming shared meaning and source support for each adapter field. Native metrics remain primary; a model pair that cannot answer the same product/customer/boundary question will be marked non-comparable for that metric rather than force-converted.

## 2026-09-29 — Reconstruction checkpoint

- Re-ran the three implementations with Python 3.14 via `py -3`. Outputs match the reconstruction notes.
  - Jones 2020 returns `partial_unresolved`. The campaign ratio is null. The selected Duke case at 17 t/year gives Table 5 mass 2,262.7 kg and power 10.4958 kWe. Integrated customer demand is 170 t on the surface and 826 t cislunar. The MREE/Duke specific-mass ratio is 8.340.
  - Kornuta's seven scenarios keep the published NPV signs. Using printed Table 14 revenue, the largest absolute gap versus the displayed NPV is about $3.35 million on the all-customers case.
  - Sowers commercial, lunar PPP, and lunar/Mars PPP cases return the static reconstruction. Timed cash flow and calculated IRR stay null.
- **Decision:** Commit the specification, rules, model code, parameter records, manifests, and notes, and exclude local PDFs, page images, and extracted full text. **Rationale:** the checkpoint is reproducible from the parameter records; the inspection copies are copyrighted sources and are not needed in git.
- **Decision:** Do not start a common-input experiment in this checkpoint. **Rationale:** Jones's campaign ledger, Sowers's cash-flow timing, and Kornuta's cost year are still unresolved, so converting the three native metrics into one dollar-per-kilogram headline would compare different questions.
- Started three parallel Opus 5.5 reviews: an implementation audit, a comparability crosswalk, and a Charania 2007 reconstruction-feasibility brief that also checks Pelech full text and the Blair toolkit. Their findings are not part of this checkpoint.

## 2026-09-29 — Selection and reconstruction specification

- **Decision:** Replace author-level inclusion and percentage-band reproduction thresholds with a versioned-case specification. **Rationale:** the implemented modules already show that one author can contain several decision cases, that a close NPV can sit beside an unresolved IRR, and that a single relative-error cutoff would either reject a rounding-level NPV match or admit an unresolved campaign ratio.
- **Decision:** Admit `kornuta2019` as a baseline for printed-revenue NPV only; keep `jones2020` and `sowers_niac2020` partial; queue `charania2007`; leave Pelech, Blair, Jones 2019, and Sowers 2021 conditional; exclude Bennett and Metzger from the baseline vote. **Rationale:** each admitted or queued row adds a different decision problem, and the excluded rows reuse or critique those problems.
- **Decision:** Forbid harmonized comparison of Jones's cost ratio, Kornuta's NPV, and Sowers's IRR until a metric-compatibility gate says the quantities are the same question. **Rationale:** the three reconstructions do not share a product location, time structure, or decision metric.
- Updated `paper.md` so the experiment design points at the new specification instead of author names, YAML layouts, and retired percentage grades. `rules.md` keeps the conduct rules and defers to the specification where selection is more specific.
- The Opus reviews started in the previous entry had not returned findings used here. This roster is based on the executed modules and the evidence review.

## 2026-09-29 — Audit and comparability follow-up

- Incorporated the independent implementation audit and the comparability crosswalk. The Charania feasibility review had not returned.
- **Decision:** Keep Jones's campaign ratio unresolved and the case partial. The audit's "unresolved" grade refers to that native ratio. Recovered sizing equations stay cited as partial outputs. **Rationale:** a null ratio is not a failed arithmetic check of Table 5.
- **Decision:** Do not digitize Sowers Figures 4.9.5 or 4.9.9 to invent annual phasing. **Rationale:** the selection specification forbids figure digitization as a reproduction target, and fitting a schedule to the published IRR would be calibration.
- **Fix:** `mars_first_operating_year` now moves delayed company demand, printed plateau revenue, and NASA Mars savings together. Historical case totals are unchanged: commercial net cash $2,155.5 million, lunar PPP $3,125.6 million, lunar/Mars $5,046.9 million.
- **Checks added to the Kornuta module, using the existing cash flows:** rates of return round to 9%, 19%, 4%, 28%, 37%, 40%, and 56%. Start-of-year discounting makes the Moon NPV about +$147.35 million. The $128 million component cost does not round to the printed NPVs. Primary path remains end-of-year timing and $129 million.
- Recorded the Table 6 discontinuity at 15,000 kg, the unused spare-launch rule, Sowers's comparison with Jones et al. (2019) rather than Jones 2020, the two-winner investment wording, full operating cost before Mars demand, and illustrative NASA IRRs of 25.48% and 52.26% against 27% and 54%.
- Saved the three-case comparability record. No pair shares a native question, so no common benchmark was opened.

## 2026-09-29 — Charania packet and validation record

- Retrieved IAC-07-A5.1.03 from the SEI archive: 17 pages, SHA-256 `bc411652c5646059b01d5b8ab6e4c5bbf126c8b574317500dce28c8accb32bdb`. The PDF stays out of git. Tables 2–4 were read from page word positions.
- **Decision:** Change `charania2007` from queued to blocked for the required price. **Rationale:** Table 2's component rows sum exactly to the printed subtotals, but the zero-NPV price depends on untabulated cash flows. Page 6 states the headline prices at 22.7% WACC and Table 4 states 21.7% for the same prices. Beta and the market premium are not numeric. Cash-flow figures were not digitized.
- **Check:** Case 2 DDT&E is 2.25 times Case 1. Case 1A's price is 3.66 times its inflation-only cost, against the paper's “approximately four times.” Probabilistic means are 13.5% and 14.2% above the 1A and 2A deterministic prices, against “approximately 14%.”
- Wrote the published-result validation record for the four coded cases. Common benchmark, cross-model experiments, modern sweeps, and the paper remain unstarted because no pair of native headlines asks the same question.

## 2026-09-29 — Timed-out source review

- The delegated Charania feasibility review timed out and returned no findings.
- **Decision:** Do not rerun that review. **Rationale:** the public paper is already the `charania2007` packet, and the required price stays unresolved.
- **Pelech 2019:** no legal open full text was found. The case stays conditional. Shadow-library copies are not sources.
- **Blair 2002:** the Space Resources Roundtable download `https://isruinfo.com/public/docs/LDEM_Draft4-updated.pdf` is a PDF. The former Mines draft URL returns 404. The Excel toolkit remains unrecovered, so the case stays conditional.

## 2026-09-29 — Sowers IRR blocked; comparison gate set

- **Decision:** Change the immediate objective from six reconstructions to a second model that can answer a decision question commensurable with Kornuta NPV. **Rationale:** Kornuta is the only operational financial baseline, and the other coded headlines are different questions or missing their solving schedules.
- **Decision:** Adopt the comparison gate. Benchmark experiments start only when two reconstructed models can evaluate the same explicit quantity without unsupported logic. A recovered cash-flow stream may be reported as NPV at a declared discount rate. An invented stream may not. Benchmark values stay unset; the schema is `research/benchmark-schema.json`.
- **Decision:** Keep two families. Financial cases are Kornuta, Sowers, Charania, and Blair. Campaign-cost cases are Jones and Bennett descendants. Cross-family differences are different questions.
- **Sowers milestone:** The NIAC packet does not contain an annual cash-flow table. Three schedules that obey the stated four-year build, two-year deployment window, and five-year NASA funding window produce commercial IRRs of 8.4359%, 7.2902%, and 10.1517%, against the reported 8.84%. The back-loaded public-private schedules have no single IRR. Figures were not digitized. Mines, the grant number, and a workbook-oriented web search did not produce an `.xlsx`. Shishko 2019 names cash-flow sheets and does not publish the series.
- **Decision:** Mark `sowers_niac2020` company IRR blocked. Keep the static cost chain as a partial reconstruction. **Rationale:** the published IRR is not identified by the tabulated totals plus the stated durations, so calculating NPV from a chosen schedule would invent the comparison.

## 2026-09-29 — Public artifact search closed on the financial pair

- Checked Sowers 2021 (DOI 10.1089/space.2020.0045 and the SMAD PDF). Table 9 repeats 8.84%, 15.8%, and 15.4%. No annual cash-flow table.
- Shishko's 2019 ICEAA slides name cash-flow sheets and do not publish the workbook or the annual series.
- Charania: no CABAM or financing workbook found beyond the SEI paper already packeted.
- Blair: the NSS and ISRU copies are PDFs. Table 4.4 prints Version 5 statements and Appendix 3 describes the toolkit. The Excel file was not found. **Decision:** those printed lines do not open the comparison gate. **Rationale:** they are output of the missing workbook under a stack of relaxed assumptions, and they cannot be rerun for a common scenario.
- **Decision:** Close the first fork on the reproducibility branch. **Rationale:** no second re-runnable financial model is in the public record. Findings and the search log are in `research/reproducibility-findings.md` and `research/artifact-search.md`. Regression checks are `tests/test_reproductions.py`.

## 2026-09-29 — Jones 2019 papers do not open a campaign reconstruction

- Read the public IAC 2019 lunar-surface paper (NTRS 20200002704). Plant and lander costs are PCEC response surfaces. The coefficients are not in the paper. Contour figures were not digitized. **Decision:** `jones2019_surface` stays conditional, and this paper does not fill the `jones2020` ledger.
- Read the public AIAA 2019-1372 cis-lunar paper. Element costs use PCEC and PRICE-H. The paper reports $40,000/kg, $46,000/kg, and $78,000/kg. Those numbers were not recomputed. **Decision:** `jones2019_cislunar` stays conditional. **Rationale:** the costing tools are not in the public packet.
- **Decision:** Write the closed comparison as `research/manuscript.md`. **Rationale:** the numerical benchmark cannot be opened from the public record, and the manuscript states that limit instead of filling it.

## 2026-09-29 — Two-part design; Part II eligibility frozen before the next search

- **Decision:** Keep every audited historical case in Part I. Do not drop Sowers, Charania, Jones, Blair, or Pelech because their headlines cannot be rerun. Kornuta stays the positive control and is benchmark-eligible. **Rationale:** the audit is a result about the literature, not a list of failures to discard.
- **Decision:** Freeze Part II eligibility in `research/benchmark-eligibility.md` before searching for further models. A model must let an independent researcher change inputs and regenerate the principal output. Code, a spreadsheet, or a complete equation set can pass. A public repository is not itself a criterion. Relevance and an independent lineage are screened first. Economic comparability is a separate pair-wise gate. Mars-only, asteroid, and generic launch models stay out unless they already answer the lunar-propellant question.
- **Decision:** Stop the Part II search at three independent eligible models that can be paired, or when the search log shows fewer than three publicly rerunnable lunar-propellant models. Kornuta counts as one. **Rationale:** three runnable models are enough, and the count is not to be filled by Kornuta clones or by unfinished reconstructions.
- The candidate log `research/benchmark-search.md` starts empty. No new model is coded in this step.

## 2026-09-29 — First Part II search pass; nothing new admitted

- Screened public repositories and papers for a second runnable lunar-propellant model. Relevance first. A GitHub link was not treated as eligibility.
- **Not admitted:** Metzger arXiv:2303.09011 has sector equations and no located code or spreadsheet. The equation completeness check was not run. The bootstrapping reproduction repository is a different question and is out. Imperial/ESA says its Excel model will not be published. `selene-isru` states it is not a cost model. `lunar-horizon-optimizer` has no identified published baseline. Steinert 2024 and Zenodo 22715084 were left out of the financial benchmark on the metrics described in their public pages. Blair 2020 slides and Shishko 2019 stay on the Blair and Sowers lineages.
- **Decision:** Do not code any of these in this pass. **Rationale:** none has yet passed the seven reproducibility items. Kornuta remains the only eligible model. The stopping rule is not met, and the search is not closed.

## 2026-09-29 — Metzger headline is numeric; the parameter table is not a license to code

- Metzger 2023 Table 1 gives years to absolute advantage. LEO is year 19, 21, or 23 as the market is cut by factors of ten. GTO is years 6, 7, and 7. **Decision:** Do not admit or code the model from the text extract. **Rationale:** Table A-1 is the input set, the appendix marks some of those inputs as estimated or approximated from figures, and there is no calculation file. A garbled table is not a baseline.
- Bennett and Dempster 2020 say they reconstructed Kornuta. A dataset description says the finance spreadsheet was archived. **Decision:** Treat it as Kornuta lineage, not as model two. **Rationale:** the paper says the economic model is Kornuta's. The file was not retrieved in this pass. It is the next file to inspect because it may contain yearly cash flows.
- Sommariva 2020 and 2023 are relevant and have no attached file on the record that was checked. `pypsa-moon` is a lunar power model and is out. Sercel and Kuhns did not yield a public economic workbook.
- Eligible count remains one. The search stays open.

## 2026-09-29 — Bennett spreadsheet retrieved; it is Kornuta's model

- Downloaded Mendeley Data 10.17632/ghzjtxzhdf.1, `GTOPaperDataAll.ods`, SHA-256 `de63d2a3ab2d6d0b6b6cc8ec61561575a3413e84ce061d0c7c87e5fd716c934b`. The file stays out of git.
- **Decision:** Do not count Bennett and Dempster 2020 as a second benchmark model. **Rationale:** the finance sheet is labeled as a Kornuta model. Its LEO check uses the published $630 million revenue, an outlay of $4.05 billion, and ten nets of $501 million. Dated XNPV is about −$972.87 million and XIRR is 4.06%, against Table 14's −$972 million and 4%. The GTO cases change the market, not the calculation lineage.
- **Decision:** Do not replace the Kornuta reconstruction with this file. **Rationale:** it confirms the annuity for the cases checked. It is not the original workbook, and it does not supply a different historical schedule.

## 2026-09-29 — Harry W. Jones 2021 cost table does not fully regenerate

- Retrieved ICES-2021-147 from NTRS, 507,814 bytes, local only. This is Harry W. Jones, not Christopher Jones 2020.
- Earth-supply costs in Table 1 match equation 18 and the stated $10 million per tonne launch cost, including the 1.3 container factor over ten years.
- **Decision:** Do not admit the paper as a benchmark model. **Rationale:** the oxygen-mining plant cost does not follow equation 17 or equation 14 applied to the printed plant mass. Equation 17 gives about 26,400 for a 10.9 t plant, and equation 14 gives about 10,300, against the table's 93.
- Cilliers, Rasera, and Hadler 2020 is a mining-rate paper, not a cost model. OSF and the Open Lunar repositories did not produce a lunar-propellant economic file. Eligible count remains one.

## 2026-09-29 — ROXY pilot-plant IRR is not regenerable from the printed cash-flow rules

- Read the open Aerospace 2026 ROXY pilot-plant paper. Reference results are 19.9% IRR for oxygen only and 47.4% with metals.
- **Decision:** Do not admit it. **Rationale:** the annual cost ingredients are printed, but the development schedule is not, the cash flows are figures, and the authors say the datasets are confidential. Using only the printed annual amounts, neither a single upfront development payment nor a uniform five-year payment reproduces those IRRs. Pelech’s 2023 propellant-payback results depend on an untabulated demand curve. The 2026 lunar-mining framework does not compute a project value. Eligible count remains one.

## 2026-09-29 — The runnable-model search stops at Kornuta

- Johnson, ICES-2025-284, is public through the Texas Tech repository. **Decision:** Do not admit it. **Rationale:** the paper says the calculation is an Excel file, that file is not released, and the customer is an early habitat.
- **Decision:** Close the Part II search without a common benchmark. **Rationale:** the logged search found one model that can be rerun and changed, Kornuta. Three runnable lunar-propellant models were not found. Inventing a second model would break the eligibility rules.
- The manuscript states that result. Benchmark values stay null.

## 2026-09-29 — Reopened recovery: executable equations and bounded comparisons

- The user asked to find ways to run the papers after another attempted implementation failed. Reopened the prior search; no Grok code or error trace was supplied, so the work diagnoses source and reconstruction obstacles rather than claiming to diagnose that specific failure.
- **Decision:** Allow auditable candidate implementations in `experiments/` before admitting them to the strict historical benchmark. **Rationale:** requiring a successful computational reproduction before writing candidate code was circular. Experimental execution, historical reproduction and empirical validity remain distinct claims.
- **Decision:** Treat original-author assumed/estimated parameters as legitimate inputs to reproducing that author's model. **Rationale:** uncertain empirical inputs do not prevent faithful equation execution; their uncertainty belongs in provenance and sensitivity analysis.
- Continued the Astra workstream on Harry W. Jones 2021. Other earlier Astra workers had returned usage-limit errors; their files were preserved, and root continued integration and the other reconstructions.
- **Jones 2021 evidence:** Visual inspection and related 2015/2019 primary papers confirmed the source's cost units. A forward branch using the inferred mass conversion, hydrogen MW-as-kW behavior, and recycling treatment regenerates 12/16 complete Table 1 process/rate rows. All cost cells at 100 and 300 t/year match printed precision. No expected result is used as a forward input. The 100 t/year oxygen case extrapolates; 300 is in the stated production-fit domain.
- **Decision:** Preserve literal Eq17, Eq14 with consistent units, and inferred table behavior as separate branches. **Rationale:** reproducing a table containing probable errors does not authorize silently correcting it or asserting author intent. Remaining low-rate discrepancies stay visible.
- **Metzger evidence:** Downloaded arXiv v1, visually recovered Table A-1 and inspected Eq12. The arXiv source endpoint returned PDF, not code. Implemented reliability, scale, scope, experience, launch and financing equations with source parameters separated from explicit interpretation choices. Equation 18 returns 30.0178/119.6332/437.3721 versus printed 30/119/436; full orbital crossing years remain unresolved.
- **Decision:** Expose the Eq12 development/fabrication conflict, initial lunar experience and development-scaling choices. **Rationale:** these cannot be silently chosen to reproduce Table 1, especially when section 5.1 and Table 1 give different optimistic LEO crossing years.
- **Sowers decision:** Compute mathematically exact NPV extrema over nonnegative spending allocations inside declared annual windows. **Rationale:** aggregate costs can identify useful bounds even when they do not identify one historical cash-flow sequence. This does not calibrate an IRR or digitize a plot.
- **Comparison:** Froze surface-offtake scenario inputs before execution: 1,100 t/year, price 500/kg, ten operating years, 10% rate and commissioning valuation. With source cost totals, modified Kornuta NPV is -1,463.14M and Sowers spans [-681.78,+23.78]M. The bounds are conditional on the declared windows and omitted unknown flows. Missing currency years and product equivalence remain explicit barriers to a strict harmonized benchmark. Ran 60 financial stress cases and 12 Metzger interpretation combinations; none represents a probability distribution or modern vendor forecast.
- Added an offline standard-library pipeline, machine-readable outputs, code/input checksums, an optional standalone plot, and meaningful checks against independent published values, dimensional identities and all endpoint allocations. Updated README and marked the earlier manuscript/search closure as superseded by this recovery phase.
- **Executed checks:** All 13 tests passed, including the four existing historical checks, independent launch-cost targets, in-domain Jones 2021 table reproduction, hydrogen power-unit diagnosis, finance/cost identities and exhaustive endpoint extrema. The pipeline regenerated the native outputs and conditional comparisons. The generated plot was visually inspected for legible labels and visible qualification of its scope. `git diff --check` passed. These establish implementation/reproduction checks, not empirical validation of lunar hardware or markets.
- The manuscript's closing sections now record the recovery results. The first-pass claim that only Kornuta can be run is kept as history and is no longer the paper's conclusion.
