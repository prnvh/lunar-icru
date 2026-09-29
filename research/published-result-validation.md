# Published-result validation

Executed with Python 3.14 on 2026-09-29. Grades follow the selection specification. A reported number that the module only echoes is not a reproduction.

| Case | Named output | Grade | Evidence |
|---|---|---|---|
| `kornuta2019` | Seven Table 14 NPVs, printed revenue, end-of-year cash flows | Close | Signs match. Largest absolute gap about $3.35 million on the all-customers case. |
| `kornuta2019` | Seven Table 14 rates of return | Close | Roots of those cash flows round to 9%, 19%, 4%, 28%, 37%, 40%, and 56%. |
| `jones2020` | Campaign cost ratio | Unresolved | Returned null. No numeric source target. |
| `jones2020` | Duke Table 5 mass and power at 17 t/year | Partial | 2,262.7 kg and 10.4958 kWe. MREE/Duke specific-mass ratio 8.340 against the printed “approximately 8.3.” |
| `sowers_niac2020` | Development, production, deployment, operations, and the consistent revenues | Close | Independent sums match the printed cost tables within rounding. |
| `sowers_niac2020` | Company and NASA IRR | Blocked | No annual table. Schedules inside the stated duration windows do not identify the published IRRs. See the methods record. |
| `charania2007` | Table 2 cost subtotals | Exact | Component rows sum to the printed DDT&E, acquisition, and transportation subtotals for all three cases. |
| `charania2007` | Required sale price | Unresolved | The zero-NPV solver is not in the paper. Prices are stored as reported outputs only. |

Checks that discriminate Kornuta's accounting, and are not alternate historical defaults: start-of-year discounting flips the Moon NPV to about +$147 million, and the $128 million component cost does not round to the printed NPVs.

Charania page-7 claims checked against Table 4, without turning them into a price model: Case 2 DDT&E is 2.25 times Case 1. Case 1A price is 3.66 times its inflation-only cost, against “approximately four times.” Probabilistic means are 13.5% and 14.2% above the 1A and 2A deterministic prices, against “approximately 14%.”

No case has been tuned to a target. No common-benchmark output is validated here because that experiment has not been run.
