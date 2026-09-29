# Jones 2020 reconstruction record

Research question: **When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?**

Status: **partial reconstruction; native campaign reproduction unresolved**. The
module implements the identifiable equations and preserves missing inputs. It is
not a validated implementation of the paper's complete mission scheduler.

## Source and version

Jones, C. A., Pensado, A. R., Clark, M. A., Grande, M. L., Ivanco, M. L., Judd,
E. L., Klovstad, J. J., and Reeves, D. M. (2020), *Cost Breakeven Analysis of
Lunar In-Situ Propellant Production for Human Missions to the Moon and Mars*,
ASCEND 2020, AIAA 2020-4041. DOI: <https://doi.org/10.2514/6.2020-4041>.

- NASA record: <https://ntrs.nasa.gov/citations/20205007564>
- NASA PDF: <https://ntrs.nasa.gov/api/citations/20205007564/downloads/ISRU-Paper3-Final.pdf>
- Exact retrieved file checksum and page pointers: `source_manifest.json`.
- Printed and one-based PDF page numbers agree. Tables 5-7 were checked visually
  on the source's pages 8 and 10 after text extraction.
- `sources/` holds local inspection aids only. Do not stage its PDF, text, or PNGs.

This is the November 2020 Moon-to-Mars model. It is not Jones's AIAA 2019-1372
Mars-only model. No parameters from that earlier model have been imported.
The 2020 paper cites the IAC 2019 lunar-surface paper for earlier sizing methods;
that cross-reference is a research lead, not permission to silently substitute
either 2019 architecture's inputs.

## Files and execution

- `model.py`: standard-library-only equations, pure `run(inputs: dict) -> dict`,
  and command-line entry point.
- `original_inputs.json`: complete implemented parameter set, including units,
  source location, provenance status, and null unresolved inputs.
- `native_case.json`: selected native parameter-space point and its selection
  provenance. The paper has a sweep, not one uniquely privileged baseline.
- `reported_outputs.json`: source outputs/qualitative findings kept separate
  from calculations, with a tolerance policy declared before comparison.
- `reproduction.json`: saved actual default run, not a reported result.

From the repository root, with any Python 3.9+ interpreter:

```text
python models/jones2020/model.py
```

For programmatic use, load `original_inputs.json` and pass its dictionary to
`run`. Optional `inputs['overrides']` maps known parameter names to replacement
values or provenance records containing `value`. Input dictionaries are copied;
native defaults are not modified. Unknown override names raise `ValueError`.
Override provenance should be stored by the experiment caller. Changing a
reported assumption creates a separate experiment, not a new historical default.

## Native question and accounting

The native metric is cumulative ISRU architecture cost divided by cumulative
Earth propellant-delivery architecture cost (pp. 2-3, 11). The paper calls an
end-of-campaign ratio below one a breakeven case. This implementation uses that
strict comparison and separately returns the ratio; equality can be inspected
directly. A first crossing below one is not a guarantee of sustained advantage.

All costs stay in **FY2019 million USD**, undiscounted. No inflation conversion,
NPV, investor return, price, or levelized-cost transformation is applied.

Table 1 defines two constant-demand phases. The default point selects ten years
of 17 t/year surface demand followed by fourteen years of 59 t/year cislunar
demand, with surface demand dropping to zero. Ten years, Duke, a three-year ISRU
lifetime, and IMF 0.25 are explicitly marked selections within the published
parameter space, not universal baseline values. The figure-specific launch
vehicle is unresolved; both Table 3 options are retained.

## Implemented equations

For each phase, integrated customer demand is rate times phase duration. For a
known gross surface production rate `q` in t/year, Table 5 gives:

```text
Table 5 mass [kg] = 1000 * specific_mass [t/(t/year)] * q
required power [kWe] = specific_power [kWe/(t/year)] * q
```

Pre-transition customer demand alone determines `q=17` in the selected case.
It does not settle propellant used to deliver spares or replacement equipment.
For cislunar demand, the implementation requires an explicit gross-production
multiplier before sizing. It never assumes that one tonne mined equals one
tonne delivered to cislunar space.

If a lunar surface payload capacity is supplied, the minimum equal-plant
partition is conditionally `ceil(Table5_mass / payload_capacity)`. This implements
the p. 7-8 description only under a confirmed integrated-mass boundary and equal
partition. It does not prescribe how initial plants expand at the transition.

Power diagnostics report continuous mass `power * 174 kg/kWe` and a whole-unit
count `ceil(power/40 kWe)`. **Neither is added to Table 5 mass.** For the selected
surface case one whole unit would weigh 6,960 kg, while Table 5 gives 2,262.7 kg.
Thus discrete reactor treatment and the meaning of Table 5 mass must be resolved
before assembling a landable system or claiming a full cost. These diagnostics
show the issue; they do not choose between competing interpretations.

Equation 1 and Table 6 give lander development and production costs:

```text
C [FY2019 MUSD] = a*m^3 + b*m^2 + c*m + d, m in kg
```

The branch changes at 15,000 kg, with equality using the lower-mass branch. The
published coefficients are retained without smoothing, refitting, or repairing
their behavior at the branch boundary. Negative cost predictions are rejected
as unusable extrapolations. The published fit's full valid mass range is absent.

Table 7 provides linear cost relationships for structures, tanks, thermal
control and ECLS. Each uses its own subsystem mass; thermal costs additionally
use design lifetime in **months**. The plant-cost function also accepts loader/
hauler and 40-kWe reactor unit counts. A development event is separately charged
from a production event so that replacement hardware does not automatically
incur new development cost. Counts of zero suppress an absent subsystem's fixed
development charge; native nuclear and excavation systems require positive
counts once their design is reconstructed.

`native_cost_events`, if supplied, is an explicit schedule. Supported events:

| Kind | Required event-specific inputs |
|---|---|
| `launch` | `launch_vehicle` (`SLS` or `commercial`) |
| `lander_development`, `lander_production` | `inert_mass_kg` |
| `plant_development`, `plant_production` | `subsystem_masses_kg` with `structures`, `tanks`, `thermal`, `ecls`; `design_lifetime_months`; `excavation_units`; `nuclear_units` |

All events also require `architecture` (`isru` or `earth`), `time_year`, and integer
`quantity`; `provenance` is recommended. There is no arbitrary dollar-cost event
that could hide fabricated costs. The code prices supplied events with the
source CERs and accumulates them chronologically. A complete external ledger can
enable a **conditional** campaign ratio, but is not certified as the native
logistics model. `event_ledger_complete` is false in original inputs. No native
schedule is generated from guesses.

## Missing information and reproduction limits

The default run returns null costs/ratio/breakeven and explicit blockers because:

1. IMF alone does not specify inert mass or landed payload. The 2020 text does
   not expose all trajectory, return, fuel, and tank-sizing conventions.
2. Table 5 does not allocate mass among the four Table 7 costed subsystems.
   Their different slopes and intercepts prevent costing their sum faithfully.
3. Loader/hauler count as a function of production is absent.
4. The boundary of Table 5 mass and integer reactor sizing is ambiguous.
5. Exact event timing, unused lander capacity, sharing of returning vehicles,
   capacity expansion at transition, spare deliveries, and lifetime replacement
   phasing are not fully specified. The five-flight life is a mission count,
   not a five-year life.
6. Development charges for multiple plant sizes, replacement plants, and
   transition redesigns require an explicit convention.
7. The source's output figures do not supply a numeric table of ratios. No graph
   values were guessed, digitized, or used to tune the calculation.

There is also an internal textual ambiguity: p. 12 explains a Figure 6 transition
feature using an "effectively infinite" ISRU lifetime although Figure 6 covers
one-, three-, and five-year lives. This should be resolved against the original
algorithm, not silently incorporated as an infinite-lifetime default.

## Source exclusions

Page 6 excludes technology-maturation cost, lead time to operational capability,
annual operations cost, spare fabrication cost and maintenance operations.
Launch cost for spare mass is included. Those exclusions are preserved as
accounting rules; they do not mean the real activities cost nothing. Zero
propellant loss, abundant accessible ice, and co-location with the relevant
human site are native assumptions. Surface nuclear power and replacement of
limited-life systems are part of the native architecture.

## Actual reconstruction output and error

The default run was executed once to generate `reproduction.json`; no tests were
added or run. It reports:

| Recoverable quantity | Calculation |
|---|---:|
| Pre-transition customer surface demand | 170 t |
| Post-transition customer cislunar demand | 826 t |
| Duke Table 5 mass for 17 t/year | 2,262.7 kg |
| Duke power for 17 t/year | 10.4958 kWe |
| ISRU design lifetime | 36 months |
| Campaign duration | 24 years |
| Native cumulative cost ratio | unresolved (`null`) |

The MREE/Duke Table 5 specific-mass ratio is about 8.34035, consistent with the
paper's approximate 8.3 statement on p. 11. That is an intermediate arithmetic
check, not reproduction of the economic conclusion. Native ratio absolute and
relative errors are **null, not zero**. The campaign ratio remains unresolved.
Recovered sizing quantities are a partial reconstruction, not a close economic
reproduction. No model has been tuned to a target or harmonized here.

## Audit checks that do not remove the blockers

Table 6 is discontinuous at the 15,000 kg branch. At 15,000 kg the retained
coefficients give development $16,195.9 million and unit production $4,127.2
million. At 15,001 kg they give $5,745.8 million and $763.3 million. The
heavier branch is rejected when it predicts a negative cost, which occurs by
60,000 kg. These magnitudes are properties of the published fit. They are not
smoothed.

The event ledger prices whole launch vehicles only. It cannot yet apply the
published spare-launch rule of 0.1 kg per kg of system per year. Stored Isp,
IMF, flight life, and spare-rate values are not read until a schedule exists.

Page 12 cites Jones et al. [4] for delivered payload falling to as low as 10%
of propellant produced. That citation is a lead to the 2019 cislunar paper. It
does not supply the 2020 trajectory. Sowers's NIAC Table 4.9.5 compares thermal
mining with Jones et al. (2019), including a stated 0.26 inert mass fraction,
75 kg/kW nuclear specific mass, and $101,000/kg in cislunar space. That table
is not a check of this 2020 case.
