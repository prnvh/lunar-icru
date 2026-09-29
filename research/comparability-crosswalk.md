# Comparability crosswalk

This record compares the three coded cases on the questions they actually ask. It is not a common benchmark and it does not authorize a shared dollar-per-kilogram headline. It was prepared from the reconstruction notes and parameter files. Primary PDFs were not re-opened for this crosswalk, so a null here can still be filled later from a source page.

# Terminology and comparability crosswalk: Jones 2020, Kornuta 2019 family, Sowers NIAC 2020

**Scope:** The three versioned reconstructions in `models/` only. No invented benchmark values and no common scenario. Every number below comes from a reconstruction note or an `original_inputs.json` file.

**Citation keys:**
- **[J: section]** means `models/jones2020/notes.md`; **[J-in: field]** means `models/jones2020/original_inputs.json`.
- **[K: section]** means `models/kornuta2019/notes.md`; **[K-in: field]** means `models/kornuta2019/original_inputs.json`.
- **[S: section]** means `models/sowers_niac2020/notes.md`, with "Eq. n" for the numbered items under *Equations and source mapping*; **[S-in: field]** means `models/sowers_niac2020/original_inputs.json`.
- **[R: principle]** means `rules.md`.

**Headline finding:** All three models ask whether lunar-derived propellant is economically worthwhile. But each asks it for a **different decision-maker, with a different cost boundary and a different time rule**:
- **Jones:** a government architecture owner, measured by an undiscounted cumulative cost ratio.
- **Kornuta:** a private mining company, measured by NPV at 10%.
- **Sowers:** a private mining company plus a separate NASA view, measured by company IRR and NASA net savings/IRR.

So at the level of native metrics, **no pair asks the same question**. A few *sub-quantities* are candidates for sharing, but each carries a named ambiguity (Sections 2 and 4).

---

## 1. Per-model native profile

### 1.1 Jones et al. 2020 (AIAA 2020-4041, the Moon-to-Mars model)

| Field | Content | Source |
|---|---|---|
| Version identity | The November 2020 Moon-to-Mars model. It is *not* the AIAA 2019-1372 Mars-only model, and no 2019 parameters were imported. | [J: Source and version] |
| Native decision question | Does an ISRU architecture cost less, over the campaign, than delivering the same propellant from Earth? The paper counts "breakeven" when the end-of-campaign ratio is below 1. | [J: Native question and accounting] |
| Native metric and units | Cumulative ISRU architecture cost ÷ cumulative Earth propellant-delivery architecture cost. Dimensionless. The comparison is strict (< 1). A first crossing below 1 does not guarantee a sustained advantage. | [J: Native question and accounting]; [J-in: native_metric] |
| Currency year | FY2019 million USD (the cost estimating relationships, or CERs, and launch prices are stated in FY2019 MUSD). | [J: Native question and accounting]; [J-in: cost_year, launch_vehicles.units] |
| Real/nominal | The notes say "FY2019 million USD, undiscounted, no inflation conversion." A single fiscal-year label implies constant-year dollars, but the notes never say "real" explicitly. **Treat as implied constant FY2019; confirm.** | [J: Native question and accounting] |
| Discounting | None. The cumulative totals are undiscounted. | [J: Native question and accounting] |
| Product | Lunar in-situ propellant, with abundant accessible ice assumed. The product composition is **not stated in the notes (null)**. | [J: Source exclusions] |
| Where delivered | Two demand phases. Pre-transition demand is at the lunar surface (17 t/yr). Post-transition demand is in cislunar space (59 t/yr). The specific cislunar node is **not stated (null)**. | [J: Native question and accounting]; [J-in: pre_surface_demand_tpy, post_cislunar_demand_tpy] |
| Customer | Human missions to the Moon and Mars (from the paper title), i.e. a government campaign. There is no market sale or price. | [J: Source and version] |
| Inside the cost boundary | Lander development and production (Eq. 1 / Table 6 CERs); plant subsystem development and production (Table 7: structures, tanks, thermal, ECLS, excavation, nuclear); launches (SLS or commercial, per launch); launch cost of spares mass; replacement of limited-life systems; surface nuclear power. | [J: Implemented equations; Source exclusions] |
| Outside the cost boundary | Technology maturation, lead time, annual operations, spare *fabrication*, and maintenance operations. The source excludes these by rule; this is not a claim that they cost zero. Propellant loss is set to 0 as a native assumption. | [J: Source exclusions]; [J-in: included_annual_operations_cost, included_spare_fabrication_cost, propellant_loss_fraction] |
| Time structure | Selected point: 10 pre-transition years (from a 5–15 year sweep) plus 14 post-transition years, 24 years in total. ISRU lifetime is 3 years (from a 1–5 year sweep), i.e. 36 months. The lander lasts 5 flights (a mission count, not years). Spares are 0.1 kg/(kg·yr). The paper is a parameter sweep with no single privileged baseline. | [J: Native question and accounting; Missing information item 5]; [J-in: pre_transition_years, isru_lifetime_years, vehicle_flights_before_replacement] |
| Reproduction status | "Partial reconstruction; native campaign reproduction unresolved." The native ratio is `null`, and its errors are **null, not zero**. Intermediate checks do work: 170 t and 826 t integrated demand, a Duke Table 5 mass of 2,262.7 kg, and an MREE/Duke specific-mass ratio of about 8.34 (the paper says about 8.3). | [J: header; Actual reconstruction output and error] |

### 1.2 Kornuta family (2018 LPI Contribution 2142 report; the directory is named for the 2019 journal paper)

| Field | Content | Source |
|---|---|---|
| Version identity | Reconstructs the **2018 detailed report**, pp. 106–109. It is *not* a verified copy of the 2019 journal spreadsheet. The NTRS 20190004974 link is the wrong document and is excluded. | [K: Scope and source identity] |
| Native decision question | Does investing in a lunar propellant mining company give a positive NPV at a given discount rate? It does not estimate government program cost. | [K: Decision problem and boundary] |
| Native metric and units | NPV in source USD for each of seven customer scenarios. The ROR values in Table 14 (9% to 56%) are **kept but not reconstructed**. | [K: Decision problem; Reported and reconstructed NPVs] |
| Currency year | **Unresolved.** Values are kept as "source USD". | [K: Decision problem and boundary]; [K-in: currency_convention] |
| Real/nominal | **Unresolved.** No inflation conversion is applied. | [K-in: currency_convention] |
| Discounting | r = 0.10 per year. Annuity factor A(10%, 10) = 6.14456710570468. | [K: Equations and reconstruction choices] |
| Product | "Lunar propellant". The composition is **not stated in the notes (null)**. | [K: Scope] |
| Where sold | **At the lunar surface.** The surface quantity includes production needed to serve more distant markets. These are *not* quantities delivered into LEO or EML1. | [K: Decision problem and boundary] |
| Customer | Seven combinations: Moon, EML1, LEO, LEO+Moon, EML1+LEO, Moon+EML1, and all. "Moon" includes the reusable lunar cycler that serves lunar orbit. | [K: Decision problem and boundary]; [K-in: scenarios.*.customers] |
| Inside the cost boundary | Initial investment I = M(c_h + c_l) = 30,000 kg × ($100,000 + $35,000)/kg = $4.05B. This is mining/processing hardware development plus delivery to the surface. Recurring cost C = $129M/yr, an operations-plus-replacement aggregate. | [K: Equations; Decision problem] |
| Outside the cost boundary | Taxes, debt, depreciation, construction phasing, salvage, ramp-up, and replacement-event schedules. Also outside: recalculation of delivery losses, transport performance, power, plant sizing, and customer willingness to pay. | [K: Decision problem and boundary]; [K-in: unsupported_fields] |
| Time structure | I is paid at t = 0, and constant (R − C) arrives at the end of years 1–10. **This timing is an inferred interpretation.** The spreadsheet was not recovered. Mine life N = 10. Revenue is constant, with no growth. | [K: Equations and reconstruction choices]; [K-in: initial_outlay_time_year, operating_payment_time] |
| Reproduction status | All 7 NPVs match in sign, with absolute error ≤ 0.096%. Scenarios 4, 5 and 7 differ by more than $0.5M under the primary revenue path. Under the "quantity × printed price" alternative, all 7 round to the printed values; this is evidence of a spreadsheet precision convention, not proof of it. No project-wide grade has been assigned. ROR is not reconstructed. | [K: Reported and reconstructed NPVs] |

### 1.3 Sowers NIAC Phase I, February 2020

| Field | Content | Source |
|---|---|---|
| Version identity | NIAC Phase I Final Report, cover dated February 2020 and released 2020-03-11. The retrieved PDF has 135 pages. | [S: Source and scope] |
| Native decision question | (a) Is a thermal-mining **production company** financially attractive under three cases: commercial, lunar public–private partnership (PPP), and lunar+Mars PPP? (b) Separately, what does NASA save relative to Earth-supplied alternatives? | [S: header; Eq. 8] |
| Native metric and units | Company IRR, printed as 8.84%, 15.8% and 15.4%. NASA IRR, printed as 27% and 54%. NASA net savings in source USD. **No prescribed NPV discount rate.** | [S: Interface; Original IRRs remain unresolved] |
| Currency year | **Unresolved** (`currency_year: null`). | [S: Source and scope]; [S-in: source.currency_year] |
| Real/nominal | **Unresolved.** Printed dollars are used unadjusted. | [S-in: source.real_or_nominal] |
| Discounting | Only implicit, through IRR. A `discount_rate` is used only if a timing scenario is selected. Without timing, NPV "cannot be produced legitimately". | [S: Interface] |
| Product | Water-derived propellant (purification/electrolysis and liquefaction subsystems). Composition is **not stated in the notes (null)**. **Excess oxygen and other byproducts earn no revenue.** | [S: Eq. 6]; [S-in: development_subsystems] |
| Where sold | The company sells **at the lunar surface** at $500/kg to a separate transportation business. Point-of-sale demand and prices (LEO, approximately GTO, EML2, lunar surface) belong to that transportation business. | [S: Source and scope]; [S-in: cases.*.demand_segments] |
| Customer | The transportation company, which serves Commercial LEO, Gateway, Landers, and (in the Mars case) Mars propellant and Mars hardware-transport propellant. In the PPP cases NASA is also a capital contributor. | [S: Source and scope; Interface]; [S-in: cases] |
| Inside the cost boundary | Development (Table 4.8.6 plus $20M ground system); production with inferred 90% unit learning; deployment launches (3 singles, 2 duals, and 1/12 of a shared dual; Mars adds one dual); operations at $3,000/(kg·yr) × 26,200 kg = $78.6M/yr, which covers maintenance and repair. NASA capital is counted once, as funding and not revenue. | [S: Eqs. 1–5, 7] |
| Outside the cost boundary | Exploration, prospecting and some initial technology development (assigned to government); the landing pad (assigned to the transportation company, apart from the 1/12 share); the transport fleet; taxes, debt, depreciation, residual value and insurance; a separate replacement schedule. | [S: Source and scope] |
| Time structure | 4 years of development/build, about 18 months of deployment, a 5-year public funding period, and 10 operating years. Mars demand starts in operating year 3. **The numeric annual and milestone schedules are absent.** | [S: Eq. 6; Original IRRs remain unresolved] |
| Reproduction status | The static cost chain is reproduced: development 0%, production +0.0000451%, deployment −0.031%, capital −0.034%, operations 0%. Commercial and lunar PPP revenue match at 0%. Lunar/Mars revenue is **−3.09%** ($941M derived against $971M printed). **Original IRRs are unresolved** and `timed_cash_flow` is null. The notes say the model "should not enter an intercomparison as though its original timed financial outputs had been reproduced". | [S: Numerical reconstruction results; Original IRRs; Preserved discrepancies] |

---

## 2. Comparability matrix

Four labels are used:
- **Same question:** the quantity plays the same role in each model and could be compared directly once the listed ambiguities are resolved.
- **Same concept, different definition:** related, but it needs a documented translation, which is the adapter's job and not something to do during reconstruction.
- **Non-comparable:** a different decision problem or a different quantity [R: Distinguish a different answer from a different question].
- **Blocked:** potentially comparable, but a named ambiguity prevents it now.

### 2.1 Jones vs. Kornuta

| Quantity | Status | Why |
|---|---|---|
| Native metric (cost ratio vs. NPV) | **Non-comparable** | One is a government cost-minimization ratio, undiscounted over 24 years, with no revenue. The other is investor value at 10% over 10 years, driven by revenue. [J: Native question]; [K: Decision problem] |
| Decision-maker / perspective | **Non-comparable** | Architecture owner vs. mining-company investor. |
| Earth-to-Moon transport cost | **Same concept, different definition** | Jones prices per launch to TLI ($1,000M for 40 t on SLS; $200M for 15 t commercial) and needs a lander chain that is unresolved [J-in: launch_vehicles, lander_inert_mass_kg]. Kornuta uses a single $35,000/kg Earth-to-lunar-surface factor [K-in: lunar_delivery_cost_usd_per_kg]. A mapping would need Jones's lander payload, which is **blocked**. |
| Demand | **Same concept, different definition** | Jones gives *customer* demand at the surface and in cislunar space (17 and 59 t/yr). Kornuta gives *surface sale quantity*, which includes the production needed for distant markets (100–1,640 t/yr). Different measurement points. [J: Implemented equations]; [K: Decision problem] |
| Hardware capital | **Same concept, different definition** | Jones uses nonlinear lander CERs and per-subsystem linear plant CERs with separate development and production events. Kornuta uses one combined $100,000/kg hardware/development factor on 30,000 kg. [J: Implemented equations]; [K: Equations] |
| Operations | **Non-comparable as native quantities** | Jones excludes operations by rule. Kornuta includes a $129M/yr aggregate. [J: Source exclusions]; [K: Aggregate recurring cost discrepancy] |
| Currency | **Blocked** | Jones is FY2019. Kornuta's cost year is unresolved. |
| Time horizon | **Non-comparable as native definitions** | A 24-year campaign with a 3-year hardware life vs. a 10-year mine life that is also the cash-flow horizon. |

### 2.2 Jones vs. Sowers

| Quantity | Status | Why |
|---|---|---|
| Jones ratio vs. Sowers company IRR | **Non-comparable** | Government cost ratio vs. private rate of return. |
| Jones ratio vs. Sowers NASA net savings / NASA IRR | **Closest in question, but different boundary** | Both ask whether a government benefits from lunar propellant compared with Earth-supplied propellant. But in Jones the government **owns and pays for the whole ISRU architecture**. In Sowers, NASA **buys at a price and contributes capital**, and the company carries the remaining capital and operations [S: Eq. 8; Source and scope]. A ratio is also not a difference. At most, the *sign* of the verdict ("government is better off") can be set side by side, and only with the boundary difference stated. **Blocked** anyway, because Jones's ratio is null and Sowers's NASA headlines are unverified ($3.925B/$45.005B derived vs. the printed "> $4B" and "$47B") [S: Preserved discrepancies]. |
| Earth-delivered alternative cost | **Same concept, different definition** | Jones models an explicit Earth-delivery architecture (launches plus landers). Sowers uses per-kg avoided-cost factors: $35,000/kg to the surface, $46,000/kg SLS cislunar, and $5,000 and $1,100/kg for lunar-fuelled delivery [S-in: nasa_savings]. |
| Demand | **Same concept, different definition** | Jones gives customer demand (17/59 t/yr). Sowers gives both point-of-sale and surface demand; its NASA savings use 5 t/yr surface propellant, 47 t/yr Mars propellant and 75 t/yr Mars hardware [S-in: nasa_savings]. The NASA-customer segment is closer to Jones's scale than the company totals, but the delivery nodes differ. |
| Operations | **Non-comparable as native quantities** | Jones excludes operations. Sowers includes a mass-based allowance covering maintenance and repair. |
| Power / plant | **Same concept, different architecture** | Nuclear 40-kWe units (Jones) vs. solar with a capture tent (Sowers). This is an architecture difference, not an input difference [R: three sources of disagreement]. |
| Discounting | **Non-comparable** | Jones is explicitly undiscounted. Sowers's metrics are IRR, with a timing profile that has not been recovered. |
| Currency | **Blocked** | FY2019 vs. unresolved. |

### 2.3 Kornuta vs. Sowers

| Quantity | Status | Why |
|---|---|---|
| Decision-maker | **Same question family** | Both concern a surface-selling propellant company deciding whether to invest. The Sowers `commercial` case (no NASA capital) is the closest analogue to Kornuta, which has no public capital, only a derived time-zero subsidy [K: Source-label issues]; [S: Interface]. |
| Native metric (NPV at 10% vs. IRR) | **Non-comparable as reported** | Different metrics. Turning Sowers into an NPV requires timing, which is **blocked** [S: Interface]. Kornuta's ROR has the same name as Sowers's IRR, but it is **not reconstructed** [K: Reported and reconstructed NPVs]. Whether Kornuta's "ROR" equals an IRR on the same cash-flow convention is **unresolved**. |
| Point of sale | **Same question** | Both sell at the lunar surface, and surface quantity includes production needed for distant markets [K: Decision problem]; [S: Source and scope]. |
| Surface price | **Same concept, different construction** | Kornuta uses a scenario-specific weighted average surface price ($500–$7,500/kg) [K-in: printed_average_price_usd_per_kg]. Sowers uses one flat $500/kg surface price, with customer-facing prices belonging to the transportation company [S-in: surface_price_usd_per_kg]. |
| Earth-to-surface delivery $/kg | **Candidate same quantity; blocked** | Both use $35,000/kg to the lunar surface [K-in: lunar_delivery_cost_usd_per_kg]; [S-in: launch.surface_cost_usd_per_kg]. Sowers adds a 10% dual-launch premium and discrete launch allocation [S: Eq. 3]. The equal number does **not** prove the two are the same definition (price vs. burdened cost), and both cost years are unresolved. |
| Capital | **Same concept, different definition** | Kornuta: one combined hardware/development factor × mass, plus delivery. Sowers: separate development $/kg, production $/kg with learning, and discrete launches. |
| Operations / replacement | **Same concept, different definition** | Kornuta: a $129M/yr aggregate, whose components ($20M ops plus 800 kg/yr replacement) sum to $128M, leaving a $1M gap. Sowers: $3,000/(kg·yr), including maintenance and repair, with no separate replacement. |
| Operating horizon | **Same value; timing not the same** | Both use 10 operating years. Kornuta's (inferred) timing puts all capital at t = 0. Sowers has about 4 years of build plus 18 months of deployment before operations. The pre-operations phasing is part of the accounting, so it must not be aligned during reconstruction [R: Do not harmonize during reconstruction]. |
| Undiscounted company net cash | **Possible diagnostic, not native, not a headline** | Kornuta's model returns per-year undiscounted cash flows [K: API]. Sowers gives derived undiscounted totals [S: Numerical reconstruction results]. This is allowed only as a labelled secondary diagnostic, because the currency year is unresolved for both and PPP support is included in Sowers's cash. |
| Currency | **Blocked** | Both unresolved. |

### 2.4 All three together

| Quantity | Status |
|---|---|
| Native conclusion metric | **Non-comparable.** Undiscounted cumulative cost ratio, NPV at 10%, and IRR (company) or undiscounted net savings and IRR (NASA). |
| Verdict sign ("favourable or not") | Can only be *set side by side*, each labelled with its own metric and perspective. It cannot be pooled into one agreement statistic without stating that three different questions were asked. It is currently blocked for Jones (null) and for the Sowers IRRs (unresolved). |
| Shared-concept inputs | Earth-to-lunar-surface transport cost, customer vs. surface demand, operating horizon, hardware capital, operations. All are "same concept, different definition". None may be shared until the Section 4 ambiguities are resolved. |
| Architecture | Nuclear ISRU (Jones, Duke/MREE) vs. an unspecified mining plant (Kornuta, 30 t) vs. solar thermal mining (Sowers, 26.2 t). These are architecture differences. |

### 2.5 Prohibited conversions (binding)

1. **Do not convert Jones's undiscounted cumulative cost ratio, Kornuta's NPV, and Sowers's IRR into one $/kg headline**, nor into any other shared scalar. This follows [R: Preserve native model outputs] and [R: Make the decision metric explicit in every major figure].
2. **Do not treat Kornuta's derived break-even surface price** ($480.56–$7,881.19/kg) **as its native result, or as a delivered-LEO price or marginal cost** [K: Separate derived break-even price]. Jones and Sowers have no equivalent output, so it must not be paired with anything as a common metric.
3. **Do not compute a Sowers NPV or IRR** from the `illustrative_uniform_annual` timing and present it as the Sowers result [S: Original IRRs remain unresolved].
4. **Do not rescale Jones's ratio into dollars** by multiplying by an assumed Earth-architecture cost. Its numerator and denominator are both null [J: Actual reconstruction output].
5. **Do not compare Jones's ratio < 1 with Kornuta's NPV > 0 as "agreement"** without stating that the perspective, discounting and boundary all differ.

---

## 3. Terminology crosswalk

### 3.1 Similar words, different quantities

| Term | Jones | Kornuta | Sowers | Consequence |
|---|---|---|---|---|
| **Launch cost** | $ per *launch* to TLI, by vehicle (SLS $1,000M for 40 t; commercial $200M for 15 t), FY2019 [J-in: launch_vehicles]. Which vehicle a given figure uses is unresolved. | $35,000 per kg *delivered to the lunar surface*, applied to hardware and replacement mass [K-in: lunar_delivery_cost_usd_per_kg]. | $35,000 per kg to the surface, turned into discrete launches ($140M single for 4 t; $308M dual for 12 t with a 10% premium) [S: Eq. 3]. The NASA view also uses $46,000/kg SLS cislunar [S-in: nasa_savings]. | Three different quantities: per launch to TLI, per kg to the surface, and per kg in discrete lots. They are not interchangeable [R: Define every benchmark quantity precisely]. |
| **Propellant** | Customer propellant demand, product unspecified. Zero loss [J-in: propellant_loss_fraction]. | Surface sale quantity, product unspecified. | Water-derived product. Excess O₂ is not valued [S: Eq. 6]. | Do not assume a shared product or mixture ratio (null in all three). |
| **Demand** | Customer demand rate at the *use location* (surface or cislunar) [J-in]. It is **not** production. | *Surface sale quantity* covering distant markets [K: Decision problem]. | Two quantities: *point-of-sale demand* and *surface demand* [S-in: demand_segments]. | Jones's "demand" is roughly Sowers's point-of-sale demand. Kornuta's "quantity" is roughly Sowers's surface demand. Jones deliberately has no mined-to-delivered factor [J: Implemented equations]. |
| **Price** | None; there is no market. | Scenario-weighted *average surface price* [K: Equations]. | One flat *surface price* ($500/kg). Point-of-sale prices are the transport company's [S-in]. | Kornuta's price varies by market mix; Sowers's does not. A "price" from Kornuta and one from Sowers are not the same construct. |
| **Capital** | Development and production events from CERs, plus launches. Replacements are production events without new development [J: Implemented equations]. | I = M(c_h + c_l), all at t = 0 (inferred) [K: Equations]. | Development, production (with learning) and deployment, phased over about 5.5 years (schedule not recovered) [S: Eqs. 1–3]. | Different composition and different phasing. |
| **Operations** | Excluded [J: Source exclusions]. | $20M/yr (a diagnostic inside the $129M aggregate) [K: Aggregate recurring cost discrepancy]. | $3,000/(kg·yr) × plant mass, including maintenance and repair [S: Eq. 4]. | "Operations" covers nothing, part of recurring cost, or recurring cost including repair, depending on the model. |
| **Replacement / spares** | Explicit: limited-life replacement, 10%/yr spares mass, launch of spares included, fabrication excluded [J: Source exclusions; J-in: spares_fraction_per_year]. | 800 kg/yr × $135,000/kg inside the aggregate (diagnostic) [K]. | No separate schedule; folded into operations [S: Source and scope]. | Structural (accounting) difference. |
| **Breakeven** | End-of-campaign ratio < 1 (native) [J: Native question]. | Analyst-derived zero-NPV constant surface price (not native) [K: Separate derived break-even price]. | Not a native output. | Only Jones's breakeven is native. The word covers different mathematical objects. |
| **Lifetime** | ISRU *hardware* design life, 1–5 years (3 selected), inside a 24-year campaign. The lander lasts 5 *flights* [J-in]. | *Mine life* N = 10 years, which is also the cash-flow horizon [K-in: mine_life_years]. | *Operational life* of 10 years after about 4 years of build and 18 months of deployment [S: Eq. 6; Original IRRs]. | Jones's "lifetime" drives replacement; Kornuta's and Sowers's set the analysis horizon. Do not share this field under a single name. |
| **Subsidy / public investment** | Not applicable (government owns everything). | A derived `minimum_time_zero_subsidy_usd = max(0, −NPV)`. The Table 14 "subsidy" title does not match its contents [K: Source-label issues]. | NASA capital contribution ($800M / $1,200M) counted once as funding. `nasa_investment_musd = 0` removes funding but keeps NASA as a customer [S: Interface]. | Kornuta's subsidy is a derived deficit; Sowers's is a native input. |
| **Rate of return** | None. | "ROR" (Table 14), not reconstructed. | "IRR" (Table 4.9.3), not reproduced. | Same name. Whether they are the same object depends on unrecovered timing in both. |
| **Development cost factor** | CERs (nonlinear for landers, linear per subsystem). | $100,000/kg, a combined hardware/development factor doubled for the financial scenarios [K: Source-label issues]. | Development $/kg and production $/kg per subsystem, listed separately [S-in]. | Kornuta's single factor is not Sowers's development factor. |
| **"Moon" customer** | Surface demand for human missions. | Includes the reusable lunar cycler serving lunar orbit [K: Decision problem]. | "Landers" segment at the lunar surface (5 t/yr). | Same label, different customer set. |
| **Scenario numbers** | Not applicable (parameter sweep). | Table and definitions make LEO scenario 3; the prose calls it 2 [K: Source-label issues]. | The table prints 1, 3, 4; the prose uses 1, 2, 3 [S: Preserved discrepancies]. | Always use semantic case keys, never bare numbers. |

### 3.2 Different names for equivalent ideas

| Idea | Jones | Kornuta | Sowers |
|---|---|---|---|
| Earth-supplied counterfactual | "Earth propellant-delivery architecture" (the denominator) | Implicit, through the customer's willingness to pay; not modelled | "NASA savings" relative to Earth-launched alternatives [S: Eq. 8] |
| Surface production to sell | Gross surface production `q` (for cislunar, needs an unresolved multiplier) | "Annual sale quantity at the lunar surface" | "Surface demand" / "production t/yr" |
| Plant mass as a cost driver | Table 5 specific mass × q | Hardware mass M = 30,000 kg | Plant mass 26,200 kg |
| Horizon over which value accrues | Campaign duration | Mine life | Operational life |

---

## 4. Adapter fields that must not be shared yet

Each item below names a field and the ambiguity blocking it. Filling it with a shared value before resolution would be silent harmonization [R: Do not harmonize during reconstruction; Never silently invent a missing parameter].

**Jones: allocating plant mass across the costed subsystems**
- `plant_subsystem_masses_kg` (structures/tanks/thermal/ECLS). Table 5 gives only a total; the CER slopes and intercepts differ, so the sum cannot be costed [J: Missing information item 2].
- `plant_capital_cost`, or any shared "$/kg hardware" factor mapped onto Jones. Blocked by the same allocation problem.
- `table5_mass_includes_power` and `nuclear_unit_count_per_plant`. One 40-kWe unit weighs 6,960 kg, against 2,262.7 kg of Table 5 mass [J: Implemented equations; Missing information item 4].
- `excavation_unit_count_per_plant`: the scaling is absent [J: Missing information item 3].
- `lander_inert_mass_kg`, `lander_surface_payload_capacity_kg`, and therefore any **Earth-to-surface $/kg mapped onto Jones** [J: Missing information item 1].
- `gross_production_per_cislunar_delivery`. It prevents sharing a "production" field with Kornuta or Sowers [J: Implemented equations].
- `selected_launch_vehicle`: unresolved for each figure [J-in].
- `native_cost_events` and the development-charge convention for replacement and transition plants [J: Missing information items 5–6].
- `isru_lifetime_years = ∞`: the p. 12 "effectively infinite" wording is unresolved and must not become a default [J: Missing information].

**Sowers: cash-flow timing**
- `discount_rate`, `npv_*`, `irr_*` (company or NASA), `timed_cash_flow`, and phase weights for development, production, deployment and NASA funding. The schedules are absent, and 4 years / 18 months / 5 years do not uniquely determine them [S: Original IRRs remain unresolved].
- `nasa_net_savings_lifetime`: printed and derived values differ ($3.925B vs. "> $4B"; $45.005B vs. "$47B") [S: Preserved discrepancies].
- `annual_revenue_lunar_mars`: $971M printed vs. $941M derived [S: Preserved discrepancies].
- `cost_scale_factor`: 1.625 printed vs. 1.7109 implied by demand [S: Preserved discrepancies].
- `learning_curve_exponent`: "0.9 exponent" in the prose vs. the inferred log₂(0.9) [S: Eq. 2; Preserved discrepancies].
- `currency_year` and `real_or_nominal`: null.

**Kornuta: cost year, the $1M discrepancy, and timing**
- `currency_year`, `real_or_nominal`, and any CPI or deflator conversion, including any alignment with Jones's FY2019 [K: Decision problem; Source-label issues].
- `lunar_delivery_cost_usd_per_kg` shared with Sowers's $35,000/kg. The numbers match, but the definition (price vs. burdened cost) and both cost years are unresolved.
- `operations_cost_usd_per_year`, `replacement_mass_kg_per_year`, `replacement_cost_usd_per_kg`. Component overrides stay unsupported until the gap between $129M and $128M is reconciled. Only the aggregate `annual_cost_usd` may be overridden [K: Aggregate recurring cost discrepancy].
- `cash_flow_timing` (t = 0 outlay, end-of-year receipts). This is inferred, and must not be imposed on Sowers or taken from Sowers [K-in: initial_outlay_time_year].
- `ror` / `irr`: not reconstructed [K: Reported and reconstructed NPVs].
- `revenue_precision_convention`: printed revenue vs. quantity × printed price. Both are kept; neither is proven [K: Reported and reconstructed NPVs].

---

## 5. Recommended machine-readable structure

### 5.1 Conventions
- Every leaf value is an object: `{value, units, status, source, reason}`.
- `status` must be one of `reported`, `derived`, `inferred`, `assumed_selection`, `reconstruction_choice`, `analyst_derived`, `unresolved`, or `not_applicable`. This follows [R: Never silently invent a missing parameter] and [R: Maintain a complete provenance trail].
- If `value` is null, `reason` is required.
- `comparability` entries record relationships between models, not values.

### 5.2 JSON Schema sketch

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "lunar-icru/crosswalk/v0",
  "title": "Native-metric and comparability crosswalk",
  "type": "object",
  "required": ["research_question", "models", "comparability", "terminology", "blocked_adapter_fields"],
  "$defs": {
    "status": {
      "enum": ["reported", "derived", "inferred", "assumed_selection", "reconstruction_choice",
               "analyst_derived", "unresolved", "not_applicable"]
    },
    "field": {
      "type": "object",
      "required": ["value", "status", "source"],
      "properties": {
        "value": {},
        "units": {"type": ["string", "null"]},
        "status": {"$ref": "#/$defs/status"},
        "source": {"type": "string", "description": "notes.md section or original_inputs.json field"},
        "reason": {"type": ["string", "null"]}
      },
      "if": {"properties": {"value": {"const": null}}},
      "then": {"required": ["reason"], "properties": {"reason": {"type": "string", "minLength": 1}}}
    },
    "model": {
      "type": "object",
      "required": ["model_id", "source_version", "decision_question", "perspective", "native_metrics",
                   "currency", "product", "point_of_delivery_or_sale", "customers",
                   "boundary", "time_structure", "reproduction"],
      "properties": {
        "model_id": {"type": "string"},
        "source_version": {"$ref": "#/$defs/field"},
        "decision_question": {"$ref": "#/$defs/field"},
        "perspective": {"enum": ["government_architecture_owner", "private_company_investor",
                                 "government_customer_and_co_investor"]},
        "native_metrics": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["metric_id", "definition", "units", "discounted", "perspective", "reproduced"],
            "properties": {
              "metric_id": {"type": "string"},
              "definition": {"type": "string"},
              "units": {"type": "string"},
              "discounted": {"type": ["boolean", "null"]},
              "perspective": {"type": "string"},
              "favourable_if": {"type": ["string", "null"]},
              "reproduced": {"enum": ["yes_sign_and_value", "intermediate_only", "not_reconstructed", "unresolved"]},
              "convertible_to_common_scalar": {"const": false}
            }
          }
        },
        "derived_reporting_outputs": {"type": "array", "items": {"$ref": "#/$defs/field"}},
        "currency": {
          "type": "object",
          "properties": {
            "cost_year": {"$ref": "#/$defs/field"},
            "real_or_nominal": {"$ref": "#/$defs/field"},
            "scale": {"$ref": "#/$defs/field"}
          }
        },
        "product": {"$ref": "#/$defs/field"},
        "point_of_delivery_or_sale": {"$ref": "#/$defs/field"},
        "customers": {"type": "array", "items": {"$ref": "#/$defs/field"}},
        "demand_definition": {"enum": ["customer_demand_at_use_location", "surface_sale_quantity",
                                       "point_of_sale_and_surface_demand"]},
        "boundary": {
          "type": "object",
          "properties": {
            "inside": {"type": "array", "items": {"type": "string"}},
            "outside": {"type": "array", "items": {"type": "string"}},
            "flags": {
              "type": "object",
              "description": "one entry per rules.md boundary item",
              "properties": {
                "development": {"$ref": "#/$defs/field"},
                "production_hardware": {"$ref": "#/$defs/field"},
                "earth_launch": {"$ref": "#/$defs/field"},
                "operations": {"$ref": "#/$defs/field"},
                "replacement_hardware": {"$ref": "#/$defs/field"},
                "spares_launch": {"$ref": "#/$defs/field"},
                "power_system": {"$ref": "#/$defs/field"},
                "customer_transport": {"$ref": "#/$defs/field"},
                "financing_tax_depreciation": {"$ref": "#/$defs/field"},
                "residual_value": {"$ref": "#/$defs/field"},
                "prospecting": {"$ref": "#/$defs/field"},
                "propellant_losses": {"$ref": "#/$defs/field"},
                "public_capital_support": {"$ref": "#/$defs/field"}
              }
            }
          }
        },
        "time_structure": {
          "type": "object",
          "properties": {
            "discount_rate": {"$ref": "#/$defs/field"},
            "analysis_horizon_years": {"$ref": "#/$defs/field"},
            "horizon_meaning": {"enum": ["campaign_duration", "mine_life_cashflow_horizon",
                                         "operating_life_after_build"]},
            "hardware_design_life": {"$ref": "#/$defs/field"},
            "pre_operations_phasing": {"$ref": "#/$defs/field"},
            "cash_flow_timing_convention": {"$ref": "#/$defs/field"},
            "demand_phases": {"type": "array", "items": {"$ref": "#/$defs/field"}}
          }
        },
        "reproduction": {
          "type": "object",
          "properties": {
            "status_statement": {"type": "string"},
            "native_metric_error": {"$ref": "#/$defs/field"},
            "intermediate_checks": {"type": "array", "items": {"$ref": "#/$defs/field"}},
            "project_grade": {"$ref": "#/$defs/field"}
          }
        }
      }
    },
    "pair": {
      "type": "object",
      "required": ["models", "quantity", "relation", "explanation", "source"],
      "properties": {
        "models": {"type": "array", "items": {"type": "string"}, "minItems": 2, "maxItems": 3},
        "quantity": {"type": "string"},
        "relation": {"enum": ["same_question", "same_concept_different_definition",
                              "non_comparable", "blocked", "diagnostic_only"]},
        "blocking_ambiguity_ids": {"type": "array", "items": {"type": "string"}},
        "explanation": {"type": "string"},
        "source": {"type": "string"}
      }
    },
    "term": {
      "type": "object",
      "required": ["term", "per_model", "hazard"],
      "properties": {
        "term": {"type": "string"},
        "per_model": {"type": "object", "additionalProperties": {"type": "string"}},
        "hazard": {"enum": ["same_word_different_quantity", "different_word_same_idea"]}
      }
    },
    "blocked_field": {
      "type": "object",
      "required": ["ambiguity_id", "model_id", "fields", "reason", "source", "resolution_needed"],
      "properties": {
        "ambiguity_id": {"type": "string"},
        "model_id": {"type": "string"},
        "fields": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
        "source": {"type": "string"},
        "resolution_needed": {"type": "string"}
      }
    }
  },
  "properties": {
    "research_question": {"type": "string"},
    "prohibited_conversions": {"type": "array", "items": {"type": "string"}},
    "models": {"type": "array", "items": {"$ref": "#/$defs/model"}},
    "comparability": {"type": "array", "items": {"$ref": "#/$defs/pair"}},
    "terminology": {"type": "array", "items": {"$ref": "#/$defs/term"}},
    "blocked_adapter_fields": {"type": "array", "items": {"$ref": "#/$defs/blocked_field"}}
  }
}
```

### 5.3 Partial instance, filled only with values already in the notes

```json
{
  "research_question": "When major lunar-propellant economic models are given the same physical and economic assumptions, do they converge on the same conclusion? If not, what causes the remaining disagreement?",
  "prohibited_conversions": [
    "jones2020 cumulative cost ratio, kornuta2019 NPV, and sowers_niac2020 IRR must not be converted into one $/kg headline or any common scalar",
    "kornuta2019 derived break-even surface price is not a native result, not delivered-LEO price, not marginal cost",
    "sowers_niac2020 illustrative_uniform_annual IRR/NPV must not be reported as the Sowers result"
  ],
  "models": [
    {
      "model_id": "jones2020",
      "source_version": {"value": "AIAA 2020-4041, Nov 2020 Moon-to-Mars model (not AIAA 2019-1372)", "status": "reported", "source": "jones2020/notes.md#Source and version"},
      "decision_question": {"value": "Is cumulative ISRU architecture cost below cumulative Earth propellant-delivery architecture cost at campaign end?", "status": "reported", "source": "jones2020/notes.md#Native question and accounting"},
      "perspective": "government_architecture_owner",
      "native_metrics": [
        {"metric_id": "cumulative_cost_ratio", "definition": "cumulative ISRU cost / cumulative Earth-delivery cost", "units": "dimensionless", "discounted": false, "perspective": "government_architecture_owner", "favourable_if": "< 1 at end of campaign (strict)", "reproduced": "unresolved", "convertible_to_common_scalar": false}
      ],
      "currency": {
        "cost_year": {"value": 2019, "units": "FY", "status": "reported", "source": "jones2020/original_inputs.json#cost_year"},
        "real_or_nominal": {"value": null, "status": "unresolved", "source": "jones2020/notes.md#Native question and accounting", "reason": "Single FY2019 label implies constant-year dollars; notes do not state real/nominal explicitly"},
        "scale": {"value": "million USD", "status": "reported", "source": "jones2020/notes.md#Native question and accounting"}
      },
      "product": {"value": null, "status": "unresolved", "source": "jones2020/notes.md#Source exclusions", "reason": "Notes state ice-derived propellant but not product composition"},
      "point_of_delivery_or_sale": {"value": "lunar surface (pre-transition); cislunar (post-transition)", "status": "reported", "source": "jones2020/original_inputs.json#pre_surface_demand_tpy,post_cislunar_demand_tpy", "reason": "Specific cislunar node not stated"},
      "customers": [{"value": "human Moon and Mars missions", "status": "reported", "source": "jones2020/notes.md#Source and version"}],
      "demand_definition": "customer_demand_at_use_location",
      "boundary": {
        "flags": {
          "operations": {"value": false, "status": "reported", "source": "jones2020/original_inputs.json#included_annual_operations_cost", "reason": "Excluded by source rule, not an estimate of zero cost"},
          "spares_launch": {"value": true, "status": "reported", "source": "jones2020/notes.md#Source exclusions"},
          "replacement_hardware": {"value": true, "status": "reported", "source": "jones2020/notes.md#Source exclusions", "reason": "Spare fabrication cost excluded"},
          "propellant_losses": {"value": 0, "units": "fraction", "status": "reported", "source": "jones2020/original_inputs.json#propellant_loss_fraction"},
          "development": {"value": "excluding technology maturation", "status": "reported", "source": "jones2020/notes.md#Source exclusions"}
        }
      },
      "time_structure": {
        "discount_rate": {"value": null, "status": "not_applicable", "source": "jones2020/notes.md#Native question and accounting", "reason": "Undiscounted by construction"},
        "analysis_horizon_years": {"value": 24, "units": "yr", "status": "assumed_selection", "source": "jones2020/notes.md#Actual reconstruction output and error", "reason": "10 pre-transition years is a selection from a 5-15 yr sweep"},
        "horizon_meaning": "campaign_duration",
        "hardware_design_life": {"value": 36, "units": "month", "status": "assumed_selection", "source": "jones2020/original_inputs.json#isru_lifetime_years", "reason": "3-yr branch of 1-5 yr sweep"},
        "cash_flow_timing_convention": {"value": null, "status": "unresolved", "source": "jones2020/notes.md#Missing information item 5", "reason": "Event timing, expansion, replacement phasing not specified"}
      },
      "reproduction": {
        "status_statement": "partial reconstruction; native campaign reproduction unresolved",
        "native_metric_error": {"value": null, "status": "unresolved", "source": "jones2020/notes.md#Actual reconstruction output and error", "reason": "Ratio null; error null, not zero"},
        "intermediate_checks": [
          {"value": 2262.7, "units": "kg", "status": "derived", "source": "jones2020/notes.md#Actual reconstruction output and error", "reason": "Duke Table 5 mass at 17 t/yr"},
          {"value": 8.34035, "units": "dimensionless", "status": "derived", "source": "jones2020/notes.md#Actual reconstruction output and error", "reason": "MREE/Duke specific-mass ratio; paper says about 8.3"}
        ],
        "project_grade": {"value": null, "status": "unresolved", "source": "jones2020/notes.md#Actual reconstruction output and error", "reason": "Unresolved under predefined policy"}
      }
    },
    {
      "model_id": "kornuta2019_report2018_company_dcf",
      "source_version": {"value": "LPI Contribution 2142 (2018) pp.106-109; not the 2019 journal spreadsheet", "status": "reported", "source": "kornuta2019/notes.md#Scope and source identity"},
      "perspective": "private_company_investor",
      "native_metrics": [
        {"metric_id": "npv", "definition": "-I + (R_s - C) * A(r,N)", "units": "source USD", "discounted": true, "perspective": "private_company_investor", "favourable_if": "> 0", "reproduced": "yes_sign_and_value", "convertible_to_common_scalar": false},
        {"metric_id": "ror", "definition": "Table 14 rate of return", "units": "fraction/yr", "discounted": null, "perspective": "private_company_investor", "favourable_if": null, "reproduced": "not_reconstructed", "convertible_to_common_scalar": false}
      ],
      "derived_reporting_outputs": [
        {"value": "break_even_surface_price_usd_per_kg", "status": "analyst_derived", "source": "kornuta2019/notes.md#Separate derived break-even price", "reason": "Not native; average surface price for zero NPV at fixed Q"},
        {"value": "minimum_time_zero_subsidy_usd", "status": "analyst_derived", "source": "kornuta2019/notes.md#Source-label issues", "reason": "max(0,-NPV); not a subsidy schedule"}
      ],
      "currency": {
        "cost_year": {"value": null, "status": "unresolved", "source": "kornuta2019/original_inputs.json#currency_convention", "reason": "Not stated in recovered source"},
        "real_or_nominal": {"value": null, "status": "unresolved", "source": "kornuta2019/original_inputs.json#currency_convention", "reason": "Not stated in recovered source"}
      },
      "product": {"value": null, "status": "unresolved", "source": "kornuta2019/notes.md#Scope and source identity", "reason": "Composition not recorded in notes"},
      "point_of_delivery_or_sale": {"value": "lunar surface", "status": "reported", "source": "kornuta2019/notes.md#Decision problem and boundary"},
      "demand_definition": "surface_sale_quantity",
      "time_structure": {
        "discount_rate": {"value": 0.10, "units": "fraction/yr", "status": "reported", "source": "kornuta2019/original_inputs.json#discount_rate"},
        "analysis_horizon_years": {"value": 10, "units": "yr", "status": "reported", "source": "kornuta2019/original_inputs.json#mine_life_years"},
        "horizon_meaning": "mine_life_cashflow_horizon",
        "cash_flow_timing_convention": {"value": "I at t=0; R-C at end of years 1..N", "status": "inferred", "source": "kornuta2019/original_inputs.json#initial_outlay_time_year", "reason": "Spreadsheet not recovered"},
        "pre_operations_phasing": {"value": null, "status": "unresolved", "source": "kornuta2019/notes.md#Decision problem and boundary", "reason": "No construction schedule recovered; none invented"}
      },
      "reproduction": {
        "status_statement": "all 7 NPVs reproduce in sign; abs error <= 0.096%; ROR not reconstructed; no project grade assigned",
        "project_grade": {"value": null, "status": "unresolved", "source": "kornuta2019/notes.md#Reported and reconstructed NPVs", "reason": "Shared grading criteria belong to parent analysis"}
      }
    },
    {
      "model_id": "sowers_niac2020",
      "perspective": "private_company_investor",
      "native_metrics": [
        {"metric_id": "company_irr", "definition": "IRR of company cash flow", "units": "percent", "discounted": null, "perspective": "private_company_investor", "favourable_if": null, "reproduced": "unresolved", "convertible_to_common_scalar": false},
        {"metric_id": "nasa_irr", "definition": "IRR of NASA investment vs savings", "units": "percent", "discounted": null, "perspective": "government_customer_and_co_investor", "favourable_if": null, "reproduced": "unresolved", "convertible_to_common_scalar": false},
        {"metric_id": "nasa_net_savings", "definition": "lifetime savings minus NASA capital contribution", "units": "source USD", "discounted": false, "perspective": "government_customer_and_co_investor", "favourable_if": "> 0", "reproduced": "unresolved", "convertible_to_common_scalar": false}
      ],
      "currency": {
        "cost_year": {"value": null, "status": "unresolved", "source": "sowers_niac2020/original_inputs.json#source.currency_year", "reason": "Not identified in reconstructed section"},
        "real_or_nominal": {"value": null, "status": "unresolved", "source": "sowers_niac2020/original_inputs.json#source.real_or_nominal", "reason": "Printed dollars retained unadjusted"}
      },
      "point_of_delivery_or_sale": {"value": "lunar surface, sold to transportation company", "status": "reported", "source": "sowers_niac2020/notes.md#Source and scope"},
      "demand_definition": "point_of_sale_and_surface_demand",
      "time_structure": {
        "discount_rate": {"value": null, "status": "not_applicable", "source": "sowers_niac2020/notes.md#Interface", "reason": "Native metric is IRR; NPV only with caller-supplied rate and timing"},
        "analysis_horizon_years": {"value": 10, "units": "operating yr", "status": "reported", "source": "sowers_niac2020/original_inputs.json#parameter_provenance.operating_years"},
        "horizon_meaning": "operating_life_after_build",
        "pre_operations_phasing": {"value": null, "status": "unresolved", "source": "sowers_niac2020/notes.md#Original IRRs remain unresolved", "reason": "4 yr build, 18 mo deployment, 5 yr funding do not uniquely determine schedule"}
      },
      "reproduction": {
        "status_statement": "static cost chain reproduced within ~0.034%; lunar/Mars revenue -3.09%; IRRs unresolved; not to enter intercomparison as timed-output reproduction"
      }
    }
  ],
  "comparability": [
    {"models": ["jones2020", "kornuta2019_report2018_company_dcf", "sowers_niac2020"], "quantity": "native conclusion metric", "relation": "non_comparable", "explanation": "Undiscounted cost ratio vs NPV@10% vs IRR/undiscounted savings; different decision-makers", "source": "all three notes.md"},
    {"models": ["kornuta2019_report2018_company_dcf", "sowers_niac2020"], "quantity": "Earth-to-lunar-surface delivery cost per kg", "relation": "blocked", "blocking_ambiguity_ids": ["K_cost_year", "S_cost_year", "delivery_cost_definition"], "explanation": "Both $35,000/kg; definition and cost years unresolved; Sowers adds dual premium and discrete launches", "source": "kornuta2019/original_inputs.json#lunar_delivery_cost_usd_per_kg; sowers_niac2020/notes.md#Eq.3"},
    {"models": ["jones2020", "sowers_niac2020"], "quantity": "government benefit vs Earth supply", "relation": "blocked", "blocking_ambiguity_ids": ["J_subsystem_allocation", "J_event_ledger", "S_nasa_headline"], "explanation": "Closest question, but different cost boundary (owner vs buyer+co-investor) and ratio vs difference", "source": "jones2020/notes.md#Native question; sowers_niac2020/notes.md#Eq.8"}
  ],
  "blocked_adapter_fields": [
    {"ambiguity_id": "J_subsystem_allocation", "model_id": "jones2020", "fields": ["plant_subsystem_masses_kg", "plant_capital_cost", "table5_mass_includes_power", "nuclear_unit_count_per_plant", "excavation_unit_count_per_plant"], "reason": "Table 5 total not allocated among Table 7 CERs; power boundary ambiguous", "source": "jones2020/notes.md#Missing information items 2-4", "resolution_needed": "Recovered allocation from original algorithm or author"},
    {"ambiguity_id": "J_lander_chain", "model_id": "jones2020", "fields": ["lander_inert_mass_kg", "lander_surface_payload_capacity_kg", "gross_production_per_cislunar_delivery", "earth_to_surface_cost_per_kg"], "reason": "IMF alone insufficient; trajectory/return conventions absent", "source": "jones2020/notes.md#Missing information item 1", "resolution_needed": "Sizing conventions (IAC 2019 lead is not permission to substitute)"},
    {"ambiguity_id": "S_cash_flow_timing", "model_id": "sowers_niac2020", "fields": ["discount_rate", "npv", "company_irr", "nasa_irr", "timed_cash_flow", "phase_weights"], "reason": "Annual/milestone schedules absent", "source": "sowers_niac2020/notes.md#Original IRRs remain unresolved", "resolution_needed": "Figure 4.9.5 numeric data or workbook"},
    {"ambiguity_id": "K_cost_year", "model_id": "kornuta2019_report2018_company_dcf", "fields": ["currency_year", "real_or_nominal", "any_deflator_conversion", "lunar_delivery_cost_usd_per_kg (shared)"], "reason": "Cost year and real/nominal not recovered", "source": "kornuta2019/notes.md#Source-label issues", "resolution_needed": "Journal spreadsheet or author confirmation"},
    {"ambiguity_id": "K_recurring_1M", "model_id": "kornuta2019_report2018_company_dcf", "fields": ["operations_cost_usd_per_year", "replacement_mass_kg_per_year", "replacement_cost_usd_per_kg"], "reason": "$129M printed vs $128M from components; only the aggregate annual_cost_usd is overridable", "source": "kornuta2019/notes.md#Aggregate recurring cost discrepancy", "resolution_needed": "Identify missing $1M/yr component"}
  ]
}
```

The same structure extends to the remaining Sowers ambiguities (the Mars revenue, scale factor, learning-curve wording and NASA headline items in Section 4). Those were left out of the instance only for length; they are recorded in [S: Preserved discrepancies].

---

**Caveats for the parent agent:**
- Where product composition, Jones's real or nominal treatment, or the specific cislunar node is null, the notes and inputs are silent. The primary PDFs may answer these. They were not re-opened for this crosswalk.
- The judgement that Jones's ratio is closest in question to Sowers's NASA view is my structural reading of [J: Native question] against [S: Eq. 8]. It is not a claim made by either note.

I'm now organizing the final write-up into the structured sections I've planned for both the Jones and Kornuta notes, making sure citations stay accurate as I lay out source identification, equations, reconstruction choices, and the reported versus reconstructed NPV comparisons.

