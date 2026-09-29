# Metzger 2023: executable sector equations

Run `py -3 experiments/metzger2023/model.py`, optionally with a JSON override file. The implementation uses only the standard library. `inputs.json` separates source values and reconstruction conventions; `source_manifest.json` identifies the exact arXiv v1 PDF and checksum.

The previous search treated a garbled text extraction as an obstacle to coding. Visual inspection of page 50 resolves the baseline Table A-1:25 t surface capital,5 t space capital,120k/kg development,40k/kg fabrication,50M annual operations,5-year build,10-year life,500 t/year production, all costs in2022 USD. These are the original author's assumed baseline, not measured performance. An author's estimated input is still usable when reproducing that author's calculation.

## Executed equations

- Equations 2–3: transport gear ratio, including the paper's effective inert mass for return propellant.
- Equations 11–12: reliability factor and bounded cost minimization.
- Equations 13–16: experience, scale and scope factors, with explicit initial-experience and development-scaling conventions.
- Equations 17–19: exponential market/up-mass trajectories and exact integrated learning curves.
- Section 4.13: uniform end-of-year buildup spending, debt accumulated to commissioning, and level annual repayment over operational life. Output is the source's long-run average cost and lunar/Earth cost ratio.

The default output covers the lunar surface. It preserves the distinction between the industry date and the separate life of a project starting at that date. A representative plant's output stays at the baseline capacity while unit costs respond to the industry scale, as in the sector approach; it is not an optimized physical plant design.

## Reproduction and unresolved choices

Equation 18 independently returns terminal launch costs 30.0178,119.6332 and437.3721 for the three market sizes, versus printed 30,119 and436. Errors are 0.0594%,0.5321%,0.3147%. This is a close reproduction of an intermediate economic calculation, not the full paper's headline.

The complete Table 1 crossing-year result remains unresolved. The paper's section5.1 says the SEP optimistic case reaches LEO in year 15, while Table 1 says19. Those cannot be treated as one unambiguous target. The initial lunar cumulative-production quantity S(0), the precise orbital curve construction, and application of learning to development versus fabrication are insufficiently explicit for an exact trajectory claim.

Visually confirmed page 13 equation 12 repeats development cost in the replacement term. The preceding sentence instead uses fabrication cost. The default `prose_fabrication` interpretation follows that sentence; `printed_development` executes the printed equation. Neither is silently substituted. The source baseline R0 = .78 and effort = .5 are used without fitting. The cost optimum uses a bounded numerical minimization; sparse independent candidate points and cost identities are checked in the tests.

The `lunar_prior_output_years` value 1 is an analyst initial-experience convention, and alternatives 0.25/5 are sensitivity cases. `scale_development` is also explicit. The generated interpretation-sensitivity CSV runs both reliability expressions, both development treatments, and all three experience choices. These ranges are not probabilities or empirically established uncertainty intervals.

Financing is implemented from section 4.13's uniform-payment/future-value and annuity-repayment prescription. Buildup labor is explicitly charged. Cost decomposition includes that labor separately from interest; summing components reproduces total cost. There is no tuning to the paper's financing-share figures.

The transport helper preserves equation 2 exactly. Its inert-mass definition should be independently assessed before substituting a vehicle specification. No modern vendor performance or tariff is asserted.
