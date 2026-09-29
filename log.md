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
