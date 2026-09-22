---
name: ive-fit-verifier-custom
description: FIT Verifier gate for IVE ventures. Takes R1 cost structure and R2 value ceiling, runs the financial margin of safety calculation, and returns a verdict before F2 design begins. Failed architectures are diagnosed and returned to the Architecture Generator.
---

# IVE FIT Verifier

## Architecture discipline — assess only from confirmed challenges

**Only assess cost floor, value ceiling, and viability using inputs grounded in challenges formally completed (marked ✓) at or before the current point in the IVE sequence.**

Do not include value claims or cost assumptions from mechanisms not yet established. If a value driver or cost input requires a later challenge, flag it as `[REQUIRES C[N]+]` and exclude it from the verdict calculation. The FIT Verifier assesses the architecture as it exists now — not as it will exist when fully designed.

---

Gates the transition from F1 (neutralise the value barrier) to F2 (normalise the customer routine). Runs immediately after R1, R2, and R3 are designed — before any F2 work begins.

**The test:** Does the gap between what it costs to deliver the workaround (cost floor, from R1) and what the customer can pay (price ceiling, from R2) clear a 25% financial margin of safety?

If yes: proceed to F2.
If no: the architecture fails the fundamental viability test. Diagnose which lever is off. Return to R1 or R2 before designing anything in F2.

---

## Where this fits in the IVE sequence

```
PCO → R1 (cost floor) → R2 (value ceiling) → R3 (scaling)
                                                    ↓
                                          ★ FIT VERIFIER GATE ★
                                          Pass → F2 begins (R4–R7)
                                          Fail → back to R1 or R2
```

This is not a model-building exercise. It is a check. It takes five to ten minutes. Do not skip it.

---

## The FIT diagnostic

**F — Financial Margin of Safety (FMOS)**
The gap between the low-point estimate of customers' willingness to pay and the high-point estimate of total unit costs (including cost of capital), expressed as a percentage of the high-point unit cost estimate. Source: Simanis, *Built to Hold* (Jan 2025, p. 7).

`FMOS = (Price Ceiling − Cost Floor) / Cost Floor`

A 50% FMOS means the venture remains profitable even if total unit costs rise 50% above the high-end cost estimate (or if unit prices fall 33% below the low-end price estimate). The average cost overrun for complex engineering projects is 62% (Flyvbjerg & Gardner, 2023) — so ≥60% is the IVE target before Phase II.

Gate thresholds — **TWO gates** (canonical single source: `04-Projects/TMTH_Venture_Studio/Forge/WS1/criteria-registry.md`). Apply the gate that matches what you are running:

**Per-requirement / F1→F2 early-warning gate** — this is the gate the design loop runs after each requirement:
- **≥ 25%**: PASS — clears the per-requirement minimum. Proceed.
- **15–24%**: BORDERLINE — proceed only with the gap logged as a critical Phase II assumption.
- **< 15%**: FAIL — return to R1 or R2.

**Phase II capital gate** — after all 10 requirements, the go/no-go for Phase II capital:
- **≥ 60%**: PASS — clears the IVE Phase II target (avg complex-project overrun is 62%, Flyvbjerg & Gardner 2023).
- **25–59%**: BORDERLINE — viable but below target; tighten toward ≥ 60% or carry as the critical assumption Phase II fieldwork tests first.
- **< 25%**: FAIL.

**Corner set — the "residue at its legal minimum" corner (VA-149, RD-035 (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30)).** Wherever the cost floor carries a statutory or licensed line — hours a rule reserves to a licensed person, a filing, a regulated assessment — the verifier runs one more corner. That corner is the floor with the line at the minimum the law fixes, read from the statute or regulator text R1 cited, not from the hours the profession spends. The margin is reported at that corner beside the others. Testing the neighbourhood of an assumed figure (a fee line, a rate, a client count) and never the figure itself is the defect a loop-back of 17 September 2026 found. `[evidence: VA-149]` A floor that carries such a line with no R1 source for the minimum is reported as **unverifiable at this corner**, and the verdict is capped at PROVISIONAL.

Always report FMOS against **both**: the per-requirement verdict AND the gap to the 60% Phase II target. (This reconciles the prior single-band scheme, which FAILed a 20% venture that design-loop and AOM correctly call BORDERLINE.)

**I — Intrinsic Performance Capability**
Does the BFF have a built-in cost-reduction mechanism, or does it rely on operational efficiency? A BFF that is cheap only when run perfectly is not IVE-grade architecture.

**T — Theorem-Driven Design**
Is the Workaround Strategy grounded in a proven theory (social learning, peer accountability, process substitution)? Architecture without a mechanism of action is a guess.

This skill runs all three checks. F is quantitative. I and T are qualitative.

---

## Step 1: Establish context

Ask the user:

1. **What is the venture?** One sentence.
2. **What is the unit of transaction?** (e.g. "one loan disbursed", "one dispute resolved", "one month of service")
3. **What is the target scale?** Units per year at the scale the architecture is designed for.
4. **What are the three reference volumes?** Pilot (launch cohort, units/month), Ramp (intermediate — typically 20–30% of at-scale, units/month), At-scale (design scale, units/month). These become the three columns in the unit economics table.

Do not proceed without these four. They frame every number that follows.

---

## Step 2: Collect the R1 cost floor

The cost floor is the total cost to deliver one unit across **all four cost layers**. FMOS calculated on only some layers is always too optimistic — and will clear a gate that the full architecture fails.

**The four layers (PVC → RC → SC → IC):**

| Layer | What it includes | Expressed per unit as |
|---|---|---|
| **PVC** (Product Variable Cost) | Cost of goods — upfront capital committed per unit before revenue | £X per unit |
| **RC** (Running Cost) | Direct labor (all activities) + general operating (rent, software, comms) | £X per unit |
| **SC** (Startup & Scaling Cost) | CapEx + Development & launch + **customer acquisition** (SC is usually significant — often larger than RC per unit) | SC total ÷ investment period ÷ annual volume |
| **IC** (Investment Cost) | Debt cost + equity cost (required IRR on capital); includes two types of WC — see below | Cost of capital × capital at risk |

**Two types of working capital — keep separate:**
- **WC to fill losses** — cash needed to fund operational losses during the ramp from zero to at-scale customer base → IC
- **WC for customer financing** — cash tied up in the gap between cash-out (commitment per unit) and cash-in (settlement received); formula: `cost_of_goods × (cost_of_capital/12) × weighted_avg_months_to_resolution` → IC, and typically the **dominant cost driver** for capital-commitment models, microfinance being the published example `[evidence: CS-10]`

Both types of WC are IC, not RC. Do not treat them as operating costs.

Ask:

> "What does it cost to deliver one unit at your target scale across all four layers — PVC, RC, SC, and IC? If you've run `/ive-fin-sim-custom`, give me the 'total costs per unit' line from the unit economics summary, confirming it includes SC and IC."

If they haven't run the fin-sim yet, collect:
- **PVC per unit** — cost of goods committed per unit
- **RC per unit** — direct labor (all activities, including pre-purchase activities at the right volume driver) + consumables + general opex per unit
- **SC per unit** — CapEx + Dev/Launch + customer acquisition costs ÷ (investment period months × monthly volume at scale). If SC is not yet designed (R3 not complete), flag it as `[REQUIRES R3]` and proceed with PVC + RC only — but note the FMOS verdict is optimistic until SC is included
- **IC per unit** — WC for customer financing + cost of capital on equity. WC for customer financing = PVC × (cost_of_capital/12) × weighted_avg_months_to_resolution
- **Any mechanism cost** (from R3 scaling design, if applicable)

Confirm the total. Label it: **Cost Floor (£X per unit — [layers included])**.

If the user has only rough numbers, proceed — flag that the verdict is indicative until the fin-sim is run.

**Individual line items (for unit economics table — collect alongside layer totals):**

For each cost component within the four layers, collect:
- **Name** — short label (e.g. "LMU specialist labour", "Platform technology")
- **Layer** — PVC / RC / SC / IC
- **Behaviour** — variable / semi-fixed / fixed (allocated)
- **Cost per unit at each of the three reference volumes** — if fixed or allocated, show the dilution across pilot / ramp / at-scale
- **Driver description** — one sentence explaining what drives this cost and the formula behind it (e.g. "265 min/claim × £20/hr blended rate including employer on-costs")

If the fin-sim has been run, pull the individual line items directly from the AOM output rather than re-collecting. If the AOM groups costs in ways that need splitting for the table, ask the user to confirm the split.

These line items are not used in the FMOS calculation — they exist solely to populate the drillable unit economics table in Step 8.

---

## Step 3: Collect the R2 price ceiling

The price ceiling is the maximum the customer can pay while still being better off than their current situation. It is bounded by the Key Monetizable Cost — the specific cost the customer currently bears that the venture eliminates or absorbs.

Ask:

> "What is the Key Monetizable Cost from R2? And what is the maximum price you can charge per unit — the point at which the customer is exactly indifferent between your venture and doing nothing?"

Collect:
- **Key Monetizable Cost** (the customer's current burden — the theoretical maximum transfer)
- **Price Ceiling** (the price at which the customer is indifferent — usually below the KMC to ensure the customer retains a surplus)

If the user is unsure of the price ceiling, prompt:

> "What share of the Key Monetizable Cost do you need to leave with the customer for them to choose you? The remainder is your price ceiling."

Label it: **Price Ceiling (£X per unit)**.

---

## Step 4: Run the FMOS calculation

> ⛔ **THE ARITHMETIC IS RUN BY A SCRIPT, NOT BY YOU (added 10 September 2026, Tom's ruling).**
> Write the inputs into a fit model file and run the checker. Do not add the layers yourself.
>
> ```
> python3 .claude/skills/shared/generators/fit_margin.py --template > <venture>-fit-model-at-C<N>.yaml
> # fill it in, then:
> python3 .claude/skills/shared/generators/fit_margin.py <venture>-fit-model-at-C<N>.yaml
> ```
>
> **The output block below is unprintable without the checker's output.** A verdict
> stated without it is not a verdict. If the checker refuses, the gate has no
> result — report the refusal and repair the model file. Never weaken the check.
>
> **Why the file, and not the four figures.** A formula whose inputs the run
> itself defines is judgement wearing arithmetic. The file makes every figure
> state its amount, its unit, its period, its scale state and its source, names
> the operating model and customer model it came from, and says whether a cost
> layer is derived from activities or asserted. The checker then refuses a mixed
> unit, a mixed scale state, a stored figure that contradicts the arithmetic
> beneath it, an asserted rate with no reason, a figure with no source, and a
> missing cost layer.
>
> **What it does not do.** It checks that the inputs are declared, dimensioned,
> sourced and consistent. It cannot check that any figure is true of the world.
> An empty model of the right shape passes every check in it.

The relation the script computes:

```
FMOS = (Price Ceiling − Cost Floor) / Cost Floor × 100%
```

The denominator is the **cost floor**, not the price ceiling. This expresses the margin as a markup over cost — consistent with Simanis (*Built to Hold*, Jan 2025, p. 7). A 50% FMOS means WTP = 1.5 × Cost, so costs can rise 50% before breaking even.

Then calculate the required price at 60% FMOS (the IVE Phase II target), and at 25% FMOS (the minimum gate), to show headroom or gap:

```
Required Price at 60% FMOS = Cost Floor × 1.60
Required Price at 25% FMOS = Cost Floor × 1.25
```

Show the working with full layer breakdown:

| | £ per unit | Notes |
|---|---|---|
| **PVC** | £X | Cost of goods per unit |
| **RC** | £X | Labor + operating costs |
| **SC** | £X | CapEx + dev + acquisition ÷ volume — or `[REQUIRES R3]` |
| **IC** | £X | WC (customer financing) + cost of capital |
| **Cost Floor (all layers)** | **£X** | Sum PVC + RC + SC + IC |
| Price Ceiling (R2) | £X | KMC × customer surplus fraction |
| Net contribution | £X | Price Ceiling − Cost Floor |
| **FMOS** | **X%** | Net contribution ÷ **Cost Floor** |
| Required price at 60% FMOS (target) | £X | Cost Floor × 1.60 |
| Required price at 25% FMOS (minimum gate) | £X | Cost Floor × 1.25 |
| Gap to price ceiling | £X | Clears by £X, or short by £X |

If SC is excluded (R3 not yet run), add a flag row: "⚠ SC layer not included — FMOS is indicative only."

**Paste the checker's own output beneath the table**, including its count of checks that reached a verdict. A green result that verified nothing reads identically to one that verified everything unless the count is shown (VA-105).

---

## Step 5: Run the I and T checks

### I — Intrinsic Performance Capability

Source: Simanis, *Built to Hold* (Jan 2025, p. 8). "A venture's intrinsic performance capability controls value conversion — the amount of customer value generated for every dollar of inputs deployed. It sets a ceiling on a venture's value curve and a floor on its cost curve."

Intrinsic performance capability is established at the **core strategy level** — the pivotal choices that forge the venture's DNA. To have high value conversion potential, core strategies must circumvent **both**:
1. The customer's **key value bottleneck** (KVB) — the factor responsible for the customer's pain with the highest monetizability
2. The venture's **key cost drivers** (KCDs) — the handful of factors behind operations responsible for a disproportionate share of full unit costs, across startup, scaling, and at-scale stages

The Airbnb example from the paper: the sunk-cost home asset circumvented the KVB (time scarcity for hosts) **and** the KCDs (skills verification cost + scaling/acquisition cost) simultaneously with one strategy. That is the I standard.

**Apply two sub-checks:**

**I-Value (value ceiling):** Does the core strategy directly target and circumvent the KVB? Does it raise the value ceiling structurally — not by adding features, but by removing the root cause of customer suffering?
- PASS: Strategy removes the KVB at the design level
- FLAG: Strategy reduces the KVB but doesn't circumvent it — customers still bear the root cost in part

**I-Cost (cost floor):** Does the core strategy directly target and circumvent the key cost drivers? Does it lower the cost floor structurally — not because the team operates well, but because of how the product is designed?
- PASS: Strategy removes a key cost driver at the design level. Cost floor is a design outcome.
- FLAG: Cost reduction depends on operational efficiency. Cost floor assumes good execution.

**Overall I verdict:**
- **PASS:** Both I-Value and I-Cost pass — the strategy achieves high value conversion (more customer value per dollar of input)
- **PARTIAL:** One passes, one flags — the architecture has an intrinsic ceiling or floor weakness
- **FAIL:** Both flag — the venture's economics depend on execution quality, not design quality

### T — Theorem-Driven Design

Source: Simanis, *Built to Hold* (Jan 2025, p. 10). "Unlike theories or hypotheses — which usually rest on little more than fuzzy intuition and anecdotes — theorems are statements whose veracity flows from a chain of logic made up of simpler, established truths."

A theorem has the form: *"If A and B are true, then C follows."* It is not a named theory applied to a context. It is a logical chain where each link is an established truth and the conclusion is unavoidable given the premises.

**Apply two sub-checks:**

**T-Chain:** Is the Workaround Strategy formulated as a theorem — a step-by-step chain of established causal logic — or as an analogy, a named theory, or an intuition?
- PASS: The strategy has an explicit logical chain. Each premise is individually defensible. The conclusion follows necessarily.
- FLAG: The strategy references a theory or precedent but the chain from theory to this specific context is not fully specified.
- FAIL: No chain. The strategy is a design choice stated as if its effect were obvious.

**T-Robustness:** Are the premises in the chain themselves reliable? Check whether any link relies on a finding with a known replication problem.

High-risk fields (replication failure common): social psychology, behavioural economics, educational psychology, positive psychology.
Lower-risk fields: economics (RCT-based), clinical medicine, evolutionary biology, cognitive psychology, game theory.

Known fragile results — flag immediately if cited: ego depletion (Baumeister) — large-scale replication failed; power posing (Cuddy) — effect size collapse; social priming (Bargh et al.) — largely failed; growth mindset at scale (Dweck) — weak classroom effects; stereotype threat generalisation — narrow conditions only; money priming (Vohs) — failed replication; IAT → behaviour link — weak predictor.

- PASS: All premises are from robust fields or have strong replication records
- FLAG: One or more premises are from high-risk fields or are known fragile results — mark as critical Phase II fieldwork assumptions
- FAIL: The chain rests primarily on fragile findings — the theorem cannot be relied upon

**Overall T verdict:**
- **PASS:** T-Chain pass + T-Robustness pass
- **FLAG:** T-Chain pass + T-Robustness flag — the logic is sound but the evidence base is uncertain
- **FAIL:** T-Chain fail (no chain) or T-Chain flag + T-Robustness fail

---

## Step 6: Verdict

**Which band applies:** the templates below are worded for the **Phase II capital gate** (≥ 60% PASS). When running the **per-requirement gate** (the design-loop SIMULATE step), use the per-requirement bands instead — PASS ≥ 25%, BORDERLINE 15–24%, FAIL < 15% — and keep the same prose. See the two-gate canonical in Step 4 / the criteria registry.

### PASS (FMOS ≥ 60%, I and T clear)

> **Verdict: PASS**
>
> The architecture clears the IVE Phase II target. FMOS is X% — the venture remains profitable even if unit costs run X% above the high-end estimate. The BFF has intrinsic cost-reduction capability. The Workaround Strategy is theory-grounded.
>
> **Proceed to F2.** Begin with R4 (Circumvent Customer Doubt about Value / Want Block).

### BORDERLINE (FMOS 25–59%)

> **Verdict: BORDERLINE — proceed with conditions**
>
> FMOS is X% — above the 25% minimum gate but below the 60% Phase II target. The architecture is viable at this cost structure, but a cost overrun of more than X% eliminates profitability. Given that average cost overruns on complex projects run at 62% (Flyvbjerg & Gardner, 2023), this is a meaningful risk.
>
> Before proceeding to F2, identify and resolve at least one of the following:
>
> - [Specific cost lever: e.g. "The working capital cost per unit must fall from £X to £Y — achievable if average resolution time falls from X months to Y months at scale"]
> - [Or: "The Key Monetizable Cost needs to be re-validated — the current price ceiling of £X produces only X% FMOS, which leaves limited room for cost overruns"]
>
> **Either tighten the architecture toward ≥60% before proceeding, or flag these as the critical assumptions Phase II fieldwork must test first.**

### FAIL — cost floor too high (FMOS < 25%, gap driven by cost)

> **Verdict: FAIL — return to R1**
>
> FMOS is X%. At the current cost floor of £X per unit, the required price to reach the 25% minimum gate is £[Cost Floor × 1.25] — which exceeds the price ceiling of £Z by £[gap]. The architecture cannot survive even modest cost overruns.
>
> **Diagnosis:** The BFF is too expensive. The Workaround Strategy does not achieve sufficient cost reduction relative to the conventional BFF.
>
> **Options before returning to R1:**
> 1. Is there a scaling mechanism in R3 that materially reduces the cost floor at volume? If so, re-run the calculation at the R3-adjusted cost.
> 2. Is the cost-of-goods component of the cost floor (working capital) dominant? A different BFF that reduces the capital commitment per unit may be the fix.
> 3. Does a different Workaround Strategy exist — one that bypasses the cost bottleneck more completely?
>
> **Do not proceed to F2. Return to R1 with this diagnosis.**

### FAIL — price ceiling too low (FMOS < 25%, gap driven by ceiling)

> **Verdict: FAIL — return to R2**
>
> FMOS is X%. The cost floor (£X) is reasonable, but the price ceiling (£Y) is too low — the customer's Key Monetizable Cost doesn't create enough headroom. Even at minimum gate (25%), the required price is £[Cost Floor × 1.25], and the ceiling only reaches £Y.
>
> **Diagnosis:** The venture is targeting a monetizable cost that isn't large enough to fund the workaround. Either the KMC is underestimated, or the wrong cost is being monetized.
>
> **Options before returning to R2:**
> 1. Is the KMC fully captured? Are there hidden costs (time, stress, downstream consequences) the customer currently bears that haven't been quantified?
> 2. Is there a larger cost further up or down the customer's value chain that the venture can address instead?
> 3. Is the customer segment right? A different segment may have the same problem but a larger KMC.
>
> **Do not proceed to F2. Return to R2 with this diagnosis.**

### FAIL — T check (no theorem)

> **Verdict: FAIL — architecture lacks a mechanism of action**
>
> The Workaround Strategy is a design choice without a grounded theory. The cost floor assumption is therefore unsupported — there is no reason to believe the BFF will produce the expected cost reduction in practice.
>
> **Return to R1.** Run `/theory-of-change-custom` as R1. Do not proceed until the Workaround Theory of Change is grounded in a named mechanism with analogical precedent.

---

## Step 5b: F3 barrier quantification (C8, C9, C10 only)

F3 challenges (R8–R10) require an additional quantified barrier test beyond F/I/T. Each challenge has its own scoring framework. Run the relevant one after F/I/T when verifying a completed F3 challenge.

---

### C8 — SCIS (Switching Cost Intensity Score)

Tests whether the switching cost clears an architecturally meaningful threshold. Source: Klemperer (1987, 1995) — SC Ratio as price umbrella test. Farrell & Klemperer (2007): switching costs of the order of one period's expenditure are economically significant. Above 1.0 = meaningful. Above 2.0 = very strong.

**SC Ratio = switching cost / annual spend with vendor**

**Three-dimension composite — max 7, threshold ≥5:**

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Magnitude** (SC Ratio) | <0.25 | 0.25–1.0 | 1.0–2.0 | >2.0 |
| **Portability** — can accumulated assets transfer to a competitor? | Fully portable | Partially portable | Non-portable | — |
| **Trajectory** — does switching cost grow materially in first 24 months? | Static | Moderate growth | Compounds (D&C asset mass efficiencies) | — |

**Verdict bands:**
- 6–7: Architecturally durable — competitor must offer multi-year value surplus to poach
- 4–5: Strong — significant price/quality advantage required to switch
- ≤3: Weak — overcome by modest competitor improvement

**Note:** Annual spend inputs are typically assumed at architecture stage. Flag all assumed inputs with † and note they require validation in operator conversations.

---

### C9 — FIS (Flywheel Intensity Score)

Tests whether the compounding accuracy advantage is durable and capital-independent. The flywheel is the mechanism by which the resource moat widens automatically: more claims → better calibration → better pricing → more volume → more claims (Arrow 1962 learning-by-doing).

**Three-dimension composite — max 7, threshold ≥5:**

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Compound rate** — how steeply does accuracy improve with volume? | Static — no compounding | Slow — marginal gains, flattens early | Moderate — meaningful improvement to ~10k claims | Strong — steep learning curve, multi-variable model improving continuously |
| **Replication lag** — how long for a competitor to reach flywheel maturity? | <12 months | 12–36 months | >36 months / structurally impossible | — |
| **Capital independence** — can the flywheel be replicated through investment? | Capital-replicable — can be bought, synthesised, or fast-tracked | Partially — can be accelerated but not fully replicated | Capital-independent — requires verified real-world outcomes that cannot be synthesised | — |

**Verdict bands:**
- 6–7: Architecturally durable flywheel — widens automatically, cannot be skipped with capital
- 4–5: Strong — meaningful lead but replication window exists
- ≤3: Weak — flywheel can be caught or bypassed

**Key test for capital independence:** would secondary market participants (insurers, buyout operators) price against synthetic or transferred data? If no, capital independence = 2. If uncertain, = 1.

---

### C10 — HRS (Hold-Up Risk Score)

Tests whether key suppliers can hold the architecture to ransom. Higher score = lower hold-up risk = better architecture. Run per supplier — score each independently, then identify the binding constraint.

**Three-dimension composite — max 7, threshold ≥5:**

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Asset ownership** — who holds the critical assets? | Supplier owns critical IP, data, or methodology | Shared — some assets with supplier, some with venture | Venture owns all critical assets — methodology, standards, data | — |
| **Alternative availability** — how many qualified replacements exist? | Single-source — no alternatives | Limited (1–2 alternatives, significant setup) | Multiple alternatives (3+, standardised onboarding) | Commodity — available from competitive market, minimal setup |
| **Replacement time** — time to restore full capacity if primary supplier withdraws | >12 months | 3–12 months | <3 months | — |

**Verdict bands:**
- 6–7: Low hold-up risk — supplier is structurally replaceable
- 4–5: Moderate risk — replacement feasible but disruptive; monitoring required
- ≤3: High hold-up risk — supplier has genuine leverage; architecture needs redesign

**NCR trigger:** any supplier scoring ≤3 is an architecture non-conformance — the leverage strategy (SR3) has not resolved the identified risk. Any supplier scoring 4–5 (borderline) where the architecture describes a fix but has not specified the design commitment (timing, minimum count, structural terms) → flag as open NCR pending design resolution.

---

## Step 7: Output a summary card

After the verdict, produce a one-page summary as an HTML file.

Save to: `04-Projects/{venture-slug}/fit-verifier-{date}.html`

Use the standard design system (DM Sans + Lora, #f5f4f1 background, #0f2744 navy panel). The card contains:

- **Venture** and **unit** at the top
- **FMOS calculation table** (Step 4 output)
- **I check** — PASS / FLAG with one-line note
- **T check** — PASS / FLAG / FAIL with one-line note
- **Verdict** in a navy panel — PASS (green border) / BORDERLINE (amber border) / FAIL (red border)
- **Routing instruction** — one sentence: what happens next
- **Date** and a footer: "FIT Verifier — IVE gate between F1 and F2"

Open in browser after saving.

---

## Step 8: Output a unit economics table

After the verdict card, produce a companion unit economics HTML file. This is a standard output at every gate — it shows the cost structure at the current challenge state, updates with each gate, and provides a drillable view of what drives every line item.

Save to: `04-Projects/{venture-slug}/{venture-slug}-unit-economics-{challenge}-{date}.html`

**Table structure:**

| Section | Contents |
|---|---|
| Header | Navy panel — venture name, challenge gate, date, exchange model note if applicable |
| Controls | "Show all drivers" toggle button (top right of table label row) |
| **PVC** | Individual variable cost items · cost per unit is volume-invariant |
| Total VC per unit | Subtotal row |
| **Whole costs / unit** | Unit sales per month (dim row) · "Cost categories" sub-label · individual RC/SC/IC items allocated per unit across three volumes |
| Subtotal | Total allocated whole costs / unit |
| **Required price vs ceiling** | Total cost per unit · Required price at target FMOS · Price ceiling (from R2) · dim note on excluded items (challenges not yet designed) |
| **Surplus / (deficit)** | Difference per unit with tags · Total difference per month (highlighted row) |
| Summary table | FMOS at ceiling per scenario · breakeven volumes |
| Footer note | What's excluded at this gate and why · source file reference |

**Drillable rows:**
- Every individual cost line item is clickable
- Clicking expands a driver row beneath it showing the formula/description collected in Step 2
- "Show all drivers" button expands/collapses all simultaneously; individual rows also toggle independently
- Driver rows styled with accent-blue left border and accent-light background

**Three columns:** pilot (launch cohort volume) / ramp (intermediate) / at-scale (design scale) — from Step 1 context.

**Currency:** whole numbers throughout. Percentages to whole numbers.

**Excluded items:** any cost not yet designed at this challenge gate (e.g. NTP fee at C3, defendant fee before C6) must appear in the dim footer note — not in the cost rows. Do not include `[REQUIRES C[N]+]` items in the table figures.

**Format authority:** the field list and gate structure stated in this skill. Do not read another venture's unit-economics page to learn the layout. `[evidence: VA-BS1]`

Open in browser after saving.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-fit-verifier-custom/SKILL.md` to modify
- **Runs after:** `/balm-challenge-1-custom` (R1), `/balm-challenge-2-custom` (R2), `/balm-challenge-3-custom` (R3)
- **If fin-sim has been run:** pull 'total costs per unit' directly from `{venture-slug}-fin-sim.html` rather than re-collecting cost components
- **On PASS:** next skill is the R4 requirement (F2 begins)
- **On FAIL:** route back to R1 (`/balm-challenge-1-custom`) or R2 (`/balm-challenge-2-custom`) with the diagnosis from Step 6
- **FMOS formula:** `(Price Ceiling − Cost Floor) / Cost Floor` — denominator is **cost**, not price. Source: Simanis, *Built to Hold* (Jan 2025, p. 7). A 50% FMOS = costs can overrun 50% before breaking even. Gate: ≥60% (Phase II target) / 25% (minimum). Do NOT use the gross margin formula `(P−C)/P` — that is a different metric and gives a materially lower number.
- **Related skills:** `/ive-fin-sim-custom` (full model), `/theory-of-change-custom` (R1/R2 ToC), `/verify-balm-custom` (completeness audit). Note: `/ive-ctm-custom` and `/ive-aom-custom` are deprecated — CTM/AOM update mode now lives inside each `balm-challenge-N-custom` skill (Sections 5 and 6). Diagram format specs: `.claude/skills/shared/ctm-diagram-spec.md` and `.claude/skills/shared/aom-diagram-spec.md`.
