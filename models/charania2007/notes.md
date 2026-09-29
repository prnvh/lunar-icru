# Charania and DePasquale 2007

Research question: When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?

Status: **source packet recorded; required-price calculation unresolved.** The public paper was retrieved on 2026-09-29 (17 pages, SHA-256 in `source_manifest.json`). Tables 2–4 were read from the page images. The PDF is not in git.

## Decision question

A commercial company sells lunar-derived LOX/LH2. The native metric is the price that sets company NPV to zero at a stated WACC. Currency is FY2006 USD. Operations run ten years, 2022–2031. Minimum cost in braces includes inflation only. Price adds financing and required return. Page 7 says that price is approximately four times the inflation-only cost.

## What the tables support

Table 2 gives DDT&E, acquisition, transportation, and a $35 million per year operations allowance for three architecture families, with triangular uncertainty ranges. Table 3 gives demands. Table 4 gives deterministic prices. Page 7 gives probabilistic means of $30,470/kg and $152,906/kg for cases 1A and 2A.

The section-header figures in Table 2 are printed subtotals. The component rows sum to those subtotals exactly: DDT&E $957 / $2,157 / $2,557 million, acquisition $319 / $1,019 / $1,044 million, and transportation $1,445 / $2,220 / $2,240 million. Case 2 DDT&E is 2.25 times Case 1, which matches the page 7 claim that it is more than twice. Where Table 4 prints both a price and an inflation-only cost, their ratio is returned. Case 1A is $26,845 / $7,327, about 3.66, against the prose “approximately four times.” The probabilistic means are about 13.5% and 14.2% above the 1A and 2A deterministic prices, against the prose “approximately 14%.” The lunar transfer vehicle statement, 25 MT consumed to deliver 21 MT, is returned as 25/21.

The excavation row is labeled “mass” and printed in the $M column. Both are preserved.

## What blocks the price

The price is found by varying dollars per kilogram until NPV is zero. The paper describes that procedure. It does not tabulate the annual costs, revenues, debt draws, or equity contributions. Figures 7 and 8 show cash-flow shapes and are not used as numeric targets. Equity beta and the market premium are named but not numbered, so the stated WACC cannot be recomputed.

Page 6 states the headline prices at 22.7% WACC. Table 4 and the figure captions state 21.7% for the same prices. Both rates are stored. Neither is selected.

CABAM, StageSizer, and the Monte Carlo workbook are not in the paper. No required price is calculated. The eight Table 4 propellant prices remain reported outputs.

## Inclusion

The case is structurally distinct: a financed zero-NPV sale price at the surface, in LLO, and in GEO. The calculation-recoverability gate fails for that price. It is not a baseline and it does not enter a comparison. `model.py` returns `calculated_required_price_usd_per_kg: null`.
