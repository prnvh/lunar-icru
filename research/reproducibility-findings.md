# Reproducibility findings

The first fork is closed. A second financial model that can be re-run under a stated scenario was not recovered from public sources. The matched benchmark stays shut. This document is the result of that search. It is not a claim about whether lunar propellant is economical.

## What can be regenerated

`py -3 -m unittest tests/test_reproductions.py` checks the following.

Kornuta's 2018-report cash flows are the only operational baseline. All seven scenario NPVs keep the published sign. The Moon case is about −$234.22 million against the displayed −$234 million. The rates of return of those flows round to the seven printed rates. Cost year remains unresolved. Start-of-year discounting is ruled out because it makes the Moon case positive.

Jones 2020 returns the Duke plant mass and power at 17 t/year, 2,262.7 kg and 10.4958 kWe. The campaign cost ratio is null. The missing ledger is a subsystem allocation, a lander sizing convention, and an event schedule. That case stays on the campaign-cost track.

Sowers NIAC static totals, using the printed revenue branch, give undiscounted company net cash of $2,155.5 million, $3,125.6 million, and $5,046.9 million. The default IRR is null.

Charania Table 2 component rows sum to the printed subtotals. The required price is null.

## What the public record does not determine

Sowers's company IRRs are 8.84%, 15.8%, and 15.4%. Schedules that obey the report's own duration windows produce other IRRs, including cases with no single IRR. The 2021 journal article repeats the table and the cumulative-cash figure. It does not add the missing years. The demonstration is `models/sowers_niac2020/timing_nonuniqueness.py`.

Charania's prices, $26,845/kg, $133,947/kg, and $7,053,265/kg, are outputs of an untabulated zero-NPV calculation. The paper attaches both 21.7% and 22.7% WACC to those prices. No debt schedule was inferred.

Blair's report prints Version 5 income, cash-flow, and balance-sheet lines and a toolkit primer. The workbook that generated them is not public. Those lines cannot be rerun when demand, price, or launch cost changes, so they are not a second baseline.

Pelech remains out until a lawful full text exists.

## What this says about the literature

The studies that could be checked do not share a dependent variable. Kornuta reports investor NPV. Jones reports an undiscounted government cost ratio. Sowers reports company IRR from a schedule that is not in the paper. Charania reports a financed sale price from a schedule that is not in the paper. Forcing those into one dollar-per-kilogram series would manufacture a comparison the sources do not support.

A blocked headline is a reproducibility result. It means a reader with the public packet cannot recompute that number. It does not mean the original authors were wrong.

## What would open a numerical comparison

One of these, obtained as a primary file rather than a new summary:

- Sowers or Shishko annual cash flows, after which NPV at a declared discount rate is a legitimate transform
- Charania's financing schedule, after which the zero-NPV price can be recomputed and the WACC contradiction resolved from the file rather than by choice
- Blair's workbook, after which the printed statements can be tied to equations that accept new inputs

Until one of those exists, benchmark values in `research/benchmark-schema.json` stay null.
