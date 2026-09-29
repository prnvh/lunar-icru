# Harry W. Jones 2021: runnable equation audit

This experiment reopens a candidate previously rejected after one oxygen cost mismatch. It contains a **forward reconstruction of most Table 1 results**, together with literal and dimensionally repaired calculations. It does not claim an author-approved correction or alter the historical benchmark modules.

## Source and inspection

Harry W. Jones, *Should Oxygen, Hydrogen, and Water on the Moon Be Provided by Earth Supply, Life Support Recycling, or Regolith Mining?*, ICES-2021-147, 50th International Conference on Environmental Systems, 12–15 July 2021. [NASA record](https://ntrs.nasa.gov/citations/20210019592), [NASA PDF](https://ntrs.nasa.gov/api/citations/20210019592/downloads/ICES-2021-147.pdf).

Printed pages 3, 5, 6, 7, and 8 were rendered locally and visually inspected. In particular, equation 17 really prints `34 * (Mass(kg) * 2.2)^0.66`. The discrepancy is **not text extraction**. Equations 14 and 17 disagree within the paper. The locally retained PDFs, extracted text and images in `sources/` are inspection aids, not redistribution artifacts; the manifest records checksums.

A related primary paper, Jones, *Estimating the Life Cycle Cost of Space Systems*, ICES-2015-041, [NASA PDF](https://ntrs.nasa.gov/api/citations/20160001190/downloads/20160001190.pdf), printed pp. 4–5, independently confirms the AMCM mass unit (pounds), output unit (million FY1999 dollars), and numerical coefficients. It gives more digits (quantity exponent .5941, mass exponent .6604, etc.) but those were **not imported** into the 2021 implementation. Jones's [ICES-2019-17](https://ntrs.nasa.gov/api/citations/20190027610/downloads/20190027610.pdf), p. 6 equation 3 and p. 7 Tables 6–7, likewise confirms the pounds convention. Neither supplies an erratum for 2021.

## Run and API

Run `python experiments/harry_jones2021/reproduce.py` from the repository root. It executes the source case and writes `forward_results.json` and `comparison.json`. No test suite was added or run. The model was executed as the requested reconstruction.

`model.run(inputs=None)` is standard-library only. It loads defaults from `inputs.json`; `input_provenance.json` records source locations, units, and status separately. `native_case.json` is the explicit historical run. Supported overrides are rates, duration, launch cost, annual operations fraction, and inflation factor. It returns all oxygen regimes and cost variants, so there is no hidden regime-selection assumption. `reported_outputs.json` is separate and is read only by the comparison script, **never by the forward model**.

All costs are million 2021 dollars. The native metric is undiscounted life-cycle cost (development + launch + operations), not selling price or NPV. Calendar-year spending profiles are unnecessary for this particular metric.

## Source equations and units

Let `r` be annual production in tonnes, `T` years, `L` million dollars per delivered tonne, and `f` annual operations as a fraction of development.

| Quantity | Formula | Source |
|---|---|---|
| Pilot oxygen plant mass, t | `4.05*r/12 + 6.6` | p.3 Eq2; fit applies at 1–5 t/month (12–60 t/year) |
| Pilot oxygen power, kW | `71.1*r/12 + 22.8` | p.3 Eq4 |
| Production oxygen plant mass, t | `.217*r + 8.73` | p.3 Eq5; fit applies at 144–1500 t/year |
| Production oxygen power, kW | `2.95*r + 27.7` | p.4 Eq7 |
| Hydrogen plant mass, t | `2.64*r + 10.8` | p.4 Eq8 |
| Hydrogen power, MW | `.122*r + .021` | p.4 Eq9 |
| Recycling plant mass, t | `.0604*r` | p.5 Eq11 |
| Recycling logistics, t | `.038*r*T` | p.5 Eq12 |
| Recycling power, kW | `.039*r` | p.5 Eq13 |
| Nuclear reactor mass, t | `sqrt(power_kW)` | p.6 Eq15, after kg-to-t conversion |
| Development, million 1999 dollars | `5.65e-4*Q^.59*M_lb^.66*80.6^S*(3.81e-55)^(1/(IOC-1900))*B^(-.36)*1.57^D` | p.5 Eq14 |
| Printed simplified development, million 2021 dollars | `34*(mass_kg*2.2)^.66` | p.6 Eq17 |
| Earth containers, million 2021 dollars | `492*(r*T)^.59` | p.7 Eq18; each carries 1 t, dry mass .3 t |
| Earth launch | `1.3*r*T*L` | p.4 Eq10, p.6 launch cost |
| Operations | `development*f*T` | p.6 section VII.D |

Reported common values: `T=10`, `L=10`, `f=.1`, `Q=1` for installed plants, `S=2.39`, `IOC=2040`, `B=1`, `D=0` for plants, `D=-1.5` for containers, inflation multiplier `1.601`, and `2.2 lb/kg`. No additional margins: source plant equations already include 30%. Eq3 and Eq6 already include Eagle power architectures; they are not added to Eq15, which would double-count power.

## Three distinct calculations

1. **Literal printed simplified equation:** use Eq17 with kilograms and multiplication by 2.2; correctly convert Eq9 MW to kW. Since the paper says AMCM costs mining and power plants but does not state unequivocally whether their masses are aggregated, return both `combined` and `separate` allocation variants. Costs remain grossly inconsistent with Table 1.
2. **Equation-14 dimensional repair:** use Eq14, pounds, and the stated 1.601 inflation factor. Algebra gives **13.3006495572**, not 34, multiplying `(mass_kg*2.2)^.66`. This is a correction of the reduction from Eq14 to Eq17, not proof of the author's intended economics. Both cost allocations remain visible. The separate branch follows the explicit component categories; neither is fitted to the table.
3. **Inferred table behavior:** apply `34*(total_installed_mass_t/2.2)^.66`, then launch installed mass plus recycling logistics, and charge operations at 10% of development per year. For hydrogen only, feed the *MW numerical value* directly into the reactor formula requiring kW. This is a deliberately labeled implementation of apparent unit errors. Recycling logistics receive launch cost but no container procurement or extra tank launch mass, consistent with the observed table, despite its ambiguous resupply prose.

The inferred CER uses the published 34, 2.2 and .66 without fitting coefficients. Its forensic identification came from masses implied by Table 1 launch costs. **Those implied masses are excluded from forward reconstruction and grading.** The model obtains every mass from production rate and source equations. The reproduction therefore provides stronger evidence than merely correlating two columns of the same table.

## Reproduction actually obtained

The criterion is every reported cost cell in a process/rate row within ±0.5 million dollars, the table's integer rounding precision. The forward inferred branch regenerates:

| Process | Annual rates with every cost cell reproduced | Unreproduced rates |
|---|---|---|
| Oxygen, production equations | 100, 300 t/year | 10, 30 |
| Hydrogen | 30, 100, 300 t/year | 10 |
| Recycling | 30, 100, 300 t/year | 10 |
| Earth supply, literal Eq18 | 10, 30, 100, 300 t/year | none |

Thus **all four alternatives and all 15 reported cost cells at both 100 and 300 t/year reproduce independently**. The 100 t/year oxygen result extrapolates Eq5/7 below their stated 144 t/year domain; this is recorded and must not be called an in-domain physical validation. The 300 t/year complete comparison has no such oxygen-domain issue. Across the entire table, 12 of 16 process/rate rows reproduce completely. These are not sixteen independent economic models.

Examples of residuals (calculated minus reported, million dollars): production oxygen at 100: plant +.4818, launch -.0615, operations +.4818, LCC -.0979; hydrogen at 300: plant -.4582, launch -.4847, operations -.4582, LCC -.4010. Full unrounded outputs and errors are machine-readable.

At 10 t/year inferred forward hydrogen launch is **383.1400**, versus 381; LCC is **831.3958**, versus 828. Recycling launch is **50.2850**, versus 60; LCC **96.5761**, versus 128. Neither oxygen branch explains its 101 launch figure: pilot gives **190.3315**, production **184.6307**. At 30 t/year oxygen pilot launch gives **308.8657**, production **260.1961**, versus 287. These residuals are not fixed by a global units conversion. No manual mass substitutions are made.

## Why this matters for model comparison

The paper can now be **run** as a conditional reconstruction. The matching table branch and the Eq14 repair represent substantially different cost conventions, so harmonization must expose that difference. It is inappropriate to silently label the table branch dimensionally correct or treat the original mismatch as proof that no runnable economic model exists.

The source appears internally inconsistent in several independently evidenced ways:

- Eq17 does not follow numerically from Eq14's stated parameters.
- The inferred table CER uses tonnes and reverses the kg-to-pound conversion. This is strong computational evidence, not an author-confirmed erratum.
- Hydrogen launch entries at 30/100/300 reproduce when MW is passed as kW. Correct conversion produces launch costs 1506.7125/3853.4863/9941.6614 instead of 919/2783/8089. This could reflect a wrong Eq9 label or omitted conversion; reference checking has not resolved author intent.
- At p.4 the prose changes the annual oxygen slope .217 into a monthly .0180 by dividing by 12. Dimensional conversion would multiply by 12. The code uses the equations in their printed units and does not use that prose conversion.
- The 10 t/year column and 30 t/year oxygen entry retain additional discrepancies. There is no justified single interpolation/switching rule across the stated oxygen domains; both regimes remain returned.
- Recycling prose says logistics are treated similarly to Earth resupply; Table 1 at 30/100/300 behaves as if only logistics mass is launched. Applying Eq18 additionally would add container procurement, plus .3 tonnes packaging per tonne of logistics. Those optional additions are exposed numerically, not silently imposed.

No unpublished spreadsheet, source code, or author clarification was obtained. No reverse-fitted costs, imported assumptions, price escalation beyond the printed factor, spares, replacement schedules, discounting, or revenue model were introduced.
