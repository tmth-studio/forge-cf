---
name: balm-challenge-6-custom
description: IVE R6 — Circumvent the Cash Flow Constraint (Buy Block). Identifies the timing mismatch between when the customer must pay and when they receive value or have cash available. Produces an Amortisation Strategy that aligns payment with the customer's cash flow reality.
---

# BALM R6 — Circumvent the Cash Flow Constraint

**Purpose:** Identify the structural reason why customers who want the product (R4 solved) and can use it (R5 solved) cannot sustain payment for it. Produce an Amortisation Strategy that aligns payment with the customer's cash flow reality — not one that merely reduces the per-payment amount.

**When to run:** After R5 is solved. R5 addresses whether customers can activate the product in their routine. R6 addresses whether they can pay for it sustainably once they are using it. Do not conflate price sensitivity (a value perception problem, addressed at R2/R4) with cash flow constraint (a timing problem, addressed at R6).

**Output:** Key Customer Segments & Current Routines, Amortisation Strategy, Gateway Partner (introduced). Together these constitute the R6 component of the new Business Form Factor.

**Handoff to:** R7 (Activate Gateway Partners) — which addresses who controls access to customers at scale and how the venture reaches them.

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: Simanis, E. et al. (2021), Cornell SC Johnson College of Business.

**Three nested levels of commercial architecture:**

| Level | What it is |
|-------|-----------|
| **Core Business Architecture (CBA)** | The logic that sets both the cost curve and value curve for an industry. No single company owns it. |
| **Business Form Factor (BFF)** | The essential shape product and operations take given a CBA. The default way the product is made, sold, delivered, and paid for. |
| **Business Model** | A company's unique strategy for outcompeting others within a shared BFF. |

IVE intervenes at the CBA/BFF level. Business model thinking comes after.

**The full sequence:**

```
PCO — Prime Commercial Opportunity (scope-setter; runs before all requirements)
│
├── F1 — Neutralise the Value Barrier
│   ├── R1: Circumvent At-scale Cost Bottleneck       [P&L — sets the cost floor]
│   ├── R2: Eliminate Customers' Value Bottleneck      [value ceiling — what customers pay]
│   └── R3: Circumvent Scaling Cost Bottleneck         [balance sheet — working capital at scale]
│
├── F2 — Normalise the Customer Routine
│   ├── R4: Circumvent Customer Doubt about Value
│   ├── R5: Eliminate the Biggest Learning Disruption
│   ├── R6: Circumvent the Cash Flow Constraint
│   └── R7: Activate Gateway Partners
│
└── F3 — Lock In the Market Position
    ├── R8: Create a Switching Cost
    ├── R9: Manufacture a Resource Moat
    └── R10: Manufacture Replaceability of the Key Supplier Input
```

**→ This skill: R6 — Circumvent the Cash Flow Constraint** (F2, third requirement; requires solved R5)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints are sequencing problems, not architecture problems.

---

## R6 definition

> Identify and eliminate the structural reason why customers who want the product and can use it cannot sustain payment for it. The Buy Block is a payment timing problem — it is not about price or affordability in aggregate, but about cash flow availability at the moment payment is required. It lives in Phase 3 (Paying) of the Customer Transformation Model.

R6 is not a pricing problem. A customer who cannot pay £50 this week may be able to pay £50 next week when their salary arrives. The structural barrier is the mismatch between the payment cycle the venture requires and the cash flow rhythm the customer actually operates on.

**R6 vs R2 distinction:** R2 identifies the Key Monetizable Cost — the value the customer is escaping and, by extension, their aggregate willingness to pay. R6 identifies the payment architecture — the mechanism by which payment is structured and timed. A customer can agree on value (R2) while still facing a Buy Block (R6) if the payment structure does not align with their cash flow reality.

---

## The Buy Block — two structural types

| Type | What it is | What it looks like |
|------|-----------|-------------------|
| **Timing mismatch** | The customer's income or cash flow arrives at a different frequency or timing than the payment cycle the venture requires. The customer is not poor — they are illiquid at the payment moment. | A farmer with seasonal income cannot sustain monthly subscription payments during the planting season when cash is depleted. A freelancer paid on 90-day terms cannot pay a monthly SaaS fee in month one or two. |
| **Lumpiness** | The payment required at any single moment is too large relative to the customer's available liquidity, even if they could afford the total cost over time. | A smallholder farmer who can afford £150 for seed over an entire season cannot access £150 in a single payment at the point of purchase. A household that can afford £10 per week cannot access £500 upfront for an appliance, even though they would pay more in total over 12 months. |

**Diagnosis discipline:** identify the primary type before designing the Amortisation Strategy. A strategy designed to solve a timing mismatch (pay after income arrives) will not resolve a lumpiness problem (no single moment when sufficient liquidity exists). The two types require different architectural responses.

---

## Why instalment plans are not R6

Standard BNPL (buy now, pay later) or instalment finance reduces the lumpiness of payment — it does not create a new BFF. Any incumbent can offer instalments. R6 requires a payment architecture that is structurally different from what incumbents provide.

The test: does the Amortisation Strategy require a new BFF, or could an incumbent adopt it without changing their architecture? If an incumbent could adopt it, it is not R6.

**Worked contrast — agricultural inputs:**
- **Not R6:** a 12-instalment payment plan for seed and fertilizer.
- **R6:** payment collected as a fixed percentage of the crop sale — automatically deducted at the point the farmer receives income from their harvest. The payment structure is designed around the income event, not an arbitrary calendar cycle. This requires a new BFF (payment processing at the point of sale for the farmer's output), and incumbents cannot adopt it without fundamentally changing how they integrate into the agricultural value chain.

The first solution reduces lumpiness. The second aligns payment with the income event itself. That is the R6 distinction.

---

## R6 and working capital — the R3 interaction

When R6 shifts payment to a different point in the cycle, the working capital calculation from R3 changes. Payment timing directly affects how long the venture must carry costs before revenue arrives.

**If R6 delays payment** (customers pay after they receive value): working capital requirements increase. Flag for R3 update — the balance sheet model must reflect the new receivables cycle.

**If R6 prepays or bundles payment** (customers pay before they use): working capital requirements decrease. This may also improve R3's model, reducing the venture's dependence on external capital during scaling.

**Requirement:** whenever R6 changes the payment timing, update R3's working capital model to reflect the new receivables and payables cycle. The two requirements are not independent.

---

## This skill IS a design loop

Running R6 is not a four-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.**

The four steps map onto this skill's existing structure:
- **Diagnose** — the diagnostic sub-requirements (SR1 Interim Value Lifecycle, SR2 Critical Value Threshold — isolating the Buy Block).
- **Theorize** — the Amortisation Theory of Change (SR3); named mechanism, prescriptive not descriptive.
- **Productize** — the Amortisation Strategy + BFF (C1–C6) + the CTM/AOM update (the design decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure (it is how Calmly's first floor omitted the guarantee payout).

### Simulate — the gate with teeth (mandatory; do not skip on illustrative data)

A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R6 has not been designed, only described.

1. **Use the correct FMOS formula — cost denominator.**
   `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7).
   Do **not** use `(Price − Cost) / Price` (gross-margin / price denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling; Cost_high = the AOM high-point unit cost.
   **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on? (For Calmly: dispute rate, in-house dispute-risk cost/txn.)
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* A sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

### Loop-back and the pivot discipline

- **FAIL or BORDERLINE → return to Diagnose** (not to a tweak). Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why R6 will not clear and what decision is needed.
- **Close criterion.** Mark R6 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## How this skill runs

Open by showing the user this checklist:

```
R6 sub-requirements — we will step through each in order:

[ ] 1. Interim Product Value Lifecycle + Lifecycle Diagram
[ ] 2. Critical Value Threshold
[ ] 3. Amortisation Theory of Change
[ ] 4. Amortisation Strategy
[ ] 5. Business Form Factor (C1–C6)
```

Then work through each sub-requirement one at a time. Show the name and definition, ask the user to answer it, confirm the answer, mark it complete, then move to the next. Do not proceed until the current sub-requirement is confirmed.

---

## Sub-requirement 1: Interim Product Value Lifecycle

**Definition:** *A description of when and how the product creates value for the customer across the full consumption period — specifically whether value delivery is continuous, progressive, or punctuated.*

**Note:** map the full lifecycle for each customer party — typically both sides of the exchange (e.g. claimant and defendant, buyer and seller). For each party, identify: the stages of use, which stages are active vs passive, when perceived value rises, and where payment falls relative to value delivery. The Buy Block diagnosis in SR2 depends on this lifecycle — without a clear map of when value lands, you cannot identify whether the constraint is timing, lumpiness, or reference point.

**Diagnostic questions:**
- What does the customer do at each stage? Which steps require active effort from them and which are passive?
- When does value first arrive for the customer — and when does it fully materialise?
- Is the value delivery event a point in time (punctuated), a gradual accumulation (progressive), or ongoing (continuous)?
- Is there a gap between when the customer must commit (payment, effort, sign-up) and when value arrives? How long is it?
- For each party: what does "receiving value" look like? Is it financial, relational, operational, psychological?

**State as:** a stage-by-stage description for each customer party, identifying the type of each stage (active, passive, decision point, value delivery, persistent resolution) and the moment at which perceived value materially changes.

---

### SR1 mandatory output: Inline Lifecycle Diagram

After confirming the value lifecycle prose for all parties, **always produce an inline lifecycle diagram** embedded directly in the SR1 answer cell of the design memo. Do not link to a separate file. The diagram is the SR1 answer — it is not supplementary.

**Diagram structure (HTML + inline SVG):**

The diagram must contain two visual components per customer party:

**1. Stage grid** — a horizontal row of stage tiles, one per stage, rendered as a CSS grid. Each tile contains:
- Stage number/label (e.g. "Step 1", "D0")
- Stage title (bold, 14px)
- Stage description (12px, 2–3 lines)
- Timing note (e.g. "~20–30 min", "Point event", "Passive")
- A stage-type tag, colour-coded as follows:

| Stage type | Background | Border-top | Tag colour |
|------------|-----------|------------|------------|
| Active | `var(--accent-light)` | `var(--accent)` | Blue tag |
| Passive | `#f5f4f1` | `#b0b8c4` | Grey tag |
| Decision point | `var(--warning-bg)` | `var(--warning-border)` | Yellow tag |
| Value delivered | `var(--green-bg)` | `var(--green-text)` | Green tag |
| Retained | `var(--green-bg)` | `var(--green-text)` | Green tag |
| Forced engagement | `var(--accent-light)` | `var(--accent)` | Blue tag |

**2. Value curve** — a `<svg viewBox="0 0 900 80">` below the stage grid for each party showing:
- A horizontal zero line (perceived value baseline)
- A polyline tracing how perceived value changes across stages — low/zero during passive waiting, rising toward value delivery, sustained post-resolution
- Dashed red/amber segments where the customer bears deferred cost or unquantified exposure (pre-engagement, ignoring phase)
- A vertical dashed green line marking the Critical Value Threshold (SR2 answer, added here as annotation)
- Stage labels on the zero line, aligned to the polyline

**3. Threshold and buy block cards** — two `threshold-card` components below each party's diagram:
- Left card: "Critical value threshold" — when and why the threshold is crossed
- Right card: "Buy block type" — whether the constraint is timing, lumpiness, or reference point (not cash flow, contingent payoff, certainty premium, etc.)

**CSS variables to use** (standard design system):
```css
--accent: #1f4fa8; --accent-light: #e8eef8; --green-bg: #e6f4ec;
--green-text: #166534; --green-border: #a7d4b8; --warning-bg: #fff8e6;
--warning-border: #d4820a; --border: #dde1e7; --text: #0f1923;
--text-secondary: #4a5568; --text-muted: #718096; --panel-bg: #0f2744;
```

**Grid column proportions:** set `grid-template-columns` to reflect relative stage duration — passive waiting stages should be proportionally wider than point events. Use fractions (e.g. `1fr 2.5fr 1fr 1.5fr 1.5fr`).

**Where the diagram goes:** inline in the design memo, inside the `<td class="req-answer">` cell for SR1. The cell contains the diagram HTML followed by (or preceded by) a short prose summary of the lifecycle structure.

---

## Sub-requirement 2: Critical Value Threshold

**Definition:** *The specific point in the value lifecycle at which value delivered materially exceeds the customer's payment or commitment, creating the conditions for willingness to proceed.*

**Note:** the threshold is not necessarily the moment value is fully delivered — it is the moment the customer's forward-looking calculation tips positive. For contingent or punctuated value delivery, the threshold is often crossed before any value is received, at a moment of sufficient conviction that the payoff will materialise. State this precisely: the specific trigger event, the comparison the customer is making, and why the comparison tips in the product's favour at that moment.

**Apply to all parties.** In multi-party products, each party faces a structurally different threshold — the comparison they are making, and the trigger event that tips it, will differ. Identify each party's threshold separately: state the trigger event, what comparison they are making at that moment, and why it tips positive for them. Do not assume the threshold is the same event for both sides.

**Diagnostic questions:**
- At what point does the customer's expected net payoff from proceeding first exceed the expected net payoff from the best alternative?
- What information or event triggers that calculation — and is it available at the right moment in the lifecycle?
- Is the comparison the customer makes at the threshold moment concrete and quantified, or vague and estimated?
- For contingent payoffs: what makes the future value credible enough to act on now?

**State as:** trigger event, the comparison being made, and why the comparison tips positive at that moment — for each party.

---

## Sub-requirement 3: Amortisation Theory of Change

**Definition:** *The class of problem the cash flow constraint represents and the theory/ies most effective in explaining how to solve it.*

Run `/theory-of-change-custom` (invoke as "R6 Amortisation"). It will produce the Amortisation Theory of Change in CMO format (Pawson & Tilley, 1997).

**Format (four fields):**
- **Class of problem:** the structural mechanism producing the Buy Block (timing mismatch, lumpiness, reference point anchoring, contingent payoff uncertainty, certainty premium resistance, etc.)
- **Theory:** cite the peer-reviewed theory that predicts how addressing this mechanism changes payment behaviour
- **Current state:** how the Buy Block currently manifests — specific and observable
- **Desired state:** the state after the Buy Block is circumvented — stated as a completed state

**Discipline:** theory section contains only established, citable findings. The design claim belongs in Sub-requirement 4.

Confirm the Amortisation ToC before moving to Sub-requirement 4.

---

## Sub-requirement 4: Amortisation Strategy

**Definition:** *The best way to operationalize the Amortisation TOC for spreading out payment in line with the Critical Value Threshold.*

⚠ **MANDATORY — before writing the Amortisation Strategy, complete these three steps in order:**

**Step 4a — Baseline honestly.** State where the current BFF stands on the Buy Block / cash flow constraint. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 4b — Generate ≥2 candidate BFF mutations.** Structural changes (not features) that could align payment with the customer's cash flow rhythm materially better than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 4c until two real mutations exist on the table.

**Step 4c — Evaluate and decide.** For each candidate: does it require a new BFF or could an incumbent adopt it without structural change? Does it change when payment fires relative to the customer's income event? What does it cost in coherence with R1–R5? Record the decision. Adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Amortisation Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R6
baseline: [one sentence: what the current BFF does on this dimension and what it leaves unresolved]
mutation_A: [structural change] | reason_considered: [why it could do better] | verdict: adopted/rejected | reason_verdict: [why]
mutation_B: [structural change] | reason_considered: [why it could do better] | verdict: adopted/rejected | reason_verdict: [why]
[mutation_C if generated]
differsFromBaseline: true/false
justificationModeFlag: true/false  ← set true if zero genuine mutations were produced
adoptedMutation: [name of adopted mutation, or "baseline_held"]
evolvedBFF: [one-sentence cumulative BFF incorporating the adopted mutation, or restatement of current BFF if held]
synthesisCheck: [real business analogue] for [domain], because [shared mechanism] — or "synthesis not yet earned"
```

If `justificationModeFlag: true` — stop. Do not write the strategy. Return to Step 4a and genuinely attempt mutations.

Only after the contract block is emitted, write the Amortisation Strategy.

**Note:** the BALM framework calls this an "Amortisation Strategy" — not a cash flow strategy or payment strategy. The question it answers is: how does the payment structure align with the customer's actual cash flow rhythm so that the absence of a pre-existing budget line item does not prevent purchase? Must be stated as a strategy, not just payment terms.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

**Critical constraints:**
- Must work within the BFF the Workaround Strategy from R1 established
- Must not violate the R1 cost floor
- Must flag the R3 interaction — if payment timing changes, the working capital model must be updated

**Quality tests:**
- Does the strategy align with the customer's actual cash flow rhythm — or with a payment schedule the venture finds convenient?
- Is it stated as a strategy (a direction of architectural intervention), not as easier payment terms?
- Does it require a new BFF — or could an incumbent adopt it without changing their architecture?
- Does the payment structure change the R3 working capital model? If so, flag for R3 update.

**Diagnostic questions:**
- What would it mean to design payment around the customer's income event rather than a calendar cycle?
- Who in the customer's value chain controls the moment when cash arrives? Could that actor become the payment collection point?
- Does the Amortisation Strategy change how much the customer is effectively willing to pay (R2 interaction) — because restructured payment changes the customer's perception of affordability?

---

## Sub-requirement 4b: Gateway Partner (embedded in SR4)

**Definition:** *The partner who plays a role in the payment or distribution mechanism for this challenge — introduced here as part of the C6 context before being fully elaborated in C7.*

**Note:** C6 introduces the gateway partner in the context of how the product reaches and is paid for by the customer. The full gateway partner theory and strategy are developed in C7. At C6, confirm two things only: who is the gateway partner, and what role do they play in the payment mechanism?

**Diagnostic questions:**
- Who already sits at the point where the customer's cash arrives? (e.g., employer, aggregator, retailer, platform, bank)
- Does the Amortisation Strategy require this actor to collect or route payment — and if so, what is their role?
- Is this the same partner who will control customer access at scale (R7), or a different one?

**State as:** partner name/type and their role in the R6 payment mechanism. Keep this focused — full elaboration comes at R7.

---

## Productizing R6 — Strategy → BFF

The Amortisation Strategy names the payment structure that aligns with the customer's cash flow reality. Productizing it means shaping the Payment Product so collection is triggered automatically by an event in the customer's routine — not managed through a separate collection process.

**Target product component:** Payment Product (Using — payment trigger)

Work through these three questions before writing the cumulative BFF:

**1. Trigger in the architecture.** Is payment collection built into the delivery mechanism — triggered by a product use event, an income event, or a routine the customer already performs — or does it require a separate collection step? A collection step that lives outside the product appears in the AOM as a recurring cost that grows with scale. The payment trigger should be a property of the product form, not a process the venture runs.

**2. Accumulation.** Does the payment architecture sit compatibly within the BFF shape R1–R5 established? Specifically: does the payment trigger align with the point in the customer's use routine where value has been realised (R2) and the product has been activated (R5)? Payment triggered too early (before value is realised) drives abandonment. Payment triggered too late (after the customer has moved on) drives collection cost. Confirm the timing is right for the architecture already established.

**3. R3 interaction.** Does this payment architecture change the working capital model? If the Amortisation Strategy shifts when cash arrives relative to when it is spent, the R3 BFF may need updating. Flag any timing changes for the R3 Scaling Architecture and note them explicitly in the BFF statement.

**4. At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A BFF that requires founding-team bandwidth, managed-by-exception operations, or pilot-only concessions is a launch-phase design, not an architecture. Name the at-scale volume explicitly. If the mechanism breaks before reaching it, return to Diagnose.

When all three are confirmed, identify the architectural spine before writing anything.

**Step 0 — Find the architectural spine.** The architectural spine is the single mechanism that runs through all prior requirements — the element whose removal would cascade failures across the most of C1 through C6. Every BFF has one. Finding it before writing forces the statement to be an architecture, not a list.

Diagnostic question: what would break first if you removed one core element from the design? The mechanism that cascades failures across the most requirements is the spine.

Write the opening sentence of the BFF around it. If the opening sentence could be "A product that does X (C1); does Y (C2); does Z (C3)..." — the spine has not been found. Go back and find it.

Write the cumulative BFF (C1–C6).

⛔ **MANDATORY HANDOFF — BFF C1–C6 CONFIRMED. DO NOT EDIT THE VDR. DO NOT PROCEED TO R7.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "BFF C1–C6 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## Sub-requirement 5: Business Form Factor (C1–C6)

**Definition:** *A cumulative statement of the venture's form factor incorporating all solutions from C1 through C6.*

Ask the user to state the updated BFF — a single coherent description that incorporates the Amortisation Strategy and gateway partner role alongside the solutions from R1 through R5.

**The test for a BFF statement vs a list:** remove the challenge labels (C1, C2, C3...) and read it cold. Does it describe a product? Or a checklist? If a checklist, the architectural spine has not been found. A properly constructed BFF reads as a description of one coherent product — the challenge labels appear as parenthetical citations, not as the structural joints holding the sentence together.

---

## R6 output format

```
SUMMARY
  Amortisation Strategy: [strategy in one sentence — the architectural direction]
  Buy Block type: [timing / lumpiness / reference point / contingent payoff / certainty premium]
  Critical Value Threshold: [the trigger event at which each party's calculation tips positive]
  R3 working capital impact: [flagged / not applicable]

R6 — CASH FLOW CONSTRAINT (BUY BLOCK)
---
INTERIM PRODUCT VALUE LIFECYCLE
  [Inline lifecycle diagram — HTML/SVG, embedded in design memo SR1 cell]
  Claimant lifecycle: [stage-by-stage summary — active, passive, value delivery, retained]
  Defendant/secondary lifecycle: [stage-by-stage summary]
  Value structure type: [punctuated / progressive / continuous — per party]

CRITICAL VALUE THRESHOLD
  Claimant: [trigger event + comparison + why it tips positive]
  Defendant/secondary: [trigger event + comparison + why it tips positive]
  Buy block type (per party): [timing / lumpiness / reference point / contingent payoff / certainty premium]

AMORTISATION THEORY OF CHANGE
  Class of problem: [named mechanism]
  Theory: [citation — peer-reviewed, citable]
  Current state: [specific and observable]
  Desired state: [completed state after Buy Block is eliminated]

AMORTISATION STRATEGY
  [One to three sentences — the architectural direction]
  Payment trigger: [the event in the customer's routine that fires collection]
  R2 interaction: [does restructured payment change effective willingness to pay?]
  R3 interaction: [does this affect working capital?]

GATEWAY PARTNER (introduced here — elaborated in C7)
  Partner: [who]
  Role in payment mechanism: [what they do at C6 stage]

BUSINESS FORM FACTOR (C1–C6)
  [cumulative BFF statement]

CONSIDERED / NOT CHOSEN (VA-4 — show your working)
  Baseline on this dimension: [honest current position of the BFF]
  Candidate mutations / options:
    A. [structural change or option] → [why it could do better] → [adopted / rejected because…]
    B. [structural change or option] → [why it could do better] → [adopted / rejected because…]
  Decision: [adopted mutation X — evolved BFF restated / held current BFF; alternatives rejected for reasons above]

SYNTHESIS CHECK (VA-1)
  Real-business analogue: [the venture now looks like [business], because [mechanism]]
  If none: [flag — parts not yet cohered; what is missing]

QUALITY CHECK
  Does the value lifecycle diagram appear inline in the design memo SR1 cell? [Yes / No]
  Is the Buy Block type correctly diagnosed (not conflated with price sensitivity)? [Yes / No]
  Is the Amortisation Strategy architectural (not just easier payment terms)? [Yes / No]
  Could an incumbent adopt it without changing their BFF? [Yes — rethink / No — good]
  Has the R3 working capital impact been flagged? [Yes / Not applicable]
  Confidence: [High / Medium / Low]
  What would increase confidence? [one specific check]
```

---

## Common failure patterns at R6

| Failure | What it looks like | What it means |
|---------|-------------------|---------------|
| Instalment plans as R6 | Standard BNPL or 12-month instalment finance is proposed as the Amortisation Strategy | Any incumbent can offer instalments. R6 requires a payment architecture that requires a new BFF. The test: could an incumbent adopt it without changing their architecture? |
| Price reduction as R6 | Lowering the price is proposed to solve the payment problem | Price reduction addresses affordability in aggregate, not cash flow timing. A customer who cannot pay £50 this week may be able to pay £50 next week when their salary arrives. The problem is timing, not level. |
| Ignoring working capital implications | R6 shifts payment timing without updating R3 | Payment timing directly affects working capital. If R6 delays payment, the venture carries costs longer before revenue arrives. R3 must be updated to reflect the new receivables cycle. |
| Designed for average income | The Amortisation Strategy is built around an assumed average income rhythm | The cash flow map must reflect the actual income rhythm of the target customer — including the outliers and seasonal extremes — not a convenient average. The strategy that works for the median customer fails for the customers who need it most. |
| Conflating R6 with R2 | The Buy Block is attributed to price sensitivity rather than cash flow timing | R2 addresses what customers are willing to pay in aggregate (value perception). R6 addresses whether they can pay when required (cash flow timing). Solve both separately. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

**Sequence:**
- **R5** (prerequisite) → solves the Use Block; proves customers can activate and consistently use the product
- **R6** → solves the Buy Block; ensures customers who are using the product can pay for it sustainably
- **R7** → addresses gateway partners; who controls access to customers at scale

**R6 vs R2 distinction:** R2 sets the height of the value ceiling — the maximum the customer will pay, determined by the Key Monetizable Cost. R6 addresses the payment architecture — how and when that payment is collected. A customer can accept the value proposition (R2) while still facing a Buy Block (R6) if the payment structure does not match their cash flow reality. Solve both independently.

**R6 → R3 link:** any change to payment timing in R6 directly affects the working capital model from R3. If R6 delays collection, the venture must carry costs for longer before revenue arrives — increasing working capital requirements. If R6 moves to prepayment or income-event collection, working capital requirements may decrease. Flag the interaction and update R3 when R6 is finalised.

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `method/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles the cash flow constraint (the Buy Block). It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on the cash flow constraint (the Buy Block)? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on the cash flow constraint (the Buy Block) than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on the cash flow constraint (the Buy Block) vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
5. **Decide and record** — adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

**VA-4 — show your working.** The candidates considered and rejected are not scratch work. Record them in the "considered / not chosen" block of the output format so the choice is auditable. Where a sub-requirement selects among options, first consider 2–3 — across the relevant customers/partners — then record which won and why the others lost.

**VA-1 — synthesis test.** When the (possibly evolved) BFF is stated, anchor it: "this now looks like [real business], because [shared mechanism]." If no clean analogue exists, flag it — the parts have not yet cohered into one business.

---

## Process discipline

These rules apply to every session working through this skill's sub-requirements.

### 1 — One field at a time, strictly gated

For each sub-requirement, the sequence is fixed:
1. **Display the definition** — output the sub-requirement number, name, and its full definition verbatim as a blockquote, exactly as written in this skill document
2. **Then ask** — only after the definition is shown, invite the user to respond
3. **Never reverse this order** — do not propose a solution, suggest an answer, or ask a question until the definition has been displayed

Do not move to the next sub-requirement until the current one is confirmed by the user. If the user drifts into the next sub-requirement, name the drift and complete the current one first.

### 2 — No design solutions until the Theory of Change is complete

The Strategy cell is locked until class of problem, theory, context, and outcome are all confirmed. Do not propose mechanisms, tactics, or architectural moves during Diagnose or Theorize. Design thinking before theory produces solutions without foundations.

### 3 — Theory stress-testing before acceptance

Before accepting any theory as the basis for a ToC, ask: has this been undermined by the replication crisis? Is there a Peters/ergodicity critique that reframes the finding as rational rather than biased? Peer-reviewed theories that have been substantially challenged should not be used as primary theoretical anchors. If a theory is contested, name the challenge and find a more robust alternative before proceeding.

### 4 — Cross-requirement elegance: check the sequencing

When claiming that a previous requirement's mechanism also solves the current one, verify that the mechanism actually reaches the customer at the right moment in their use routine. A mechanism that fires at the wrong time — after the decision point, or before the customer encounters the block — does not solve the current requirement, even if it addresses the same underlying problem.

### 5 — Distinguish three questions that challenge fields often conflate

When diagnosing any block or bottleneck, keep these three questions separate:
- **Where does it manifest?** — the specific step in the use routine or operating model where the block appears
- **What is the main factor causing it?** — the underlying factor, not the location
- **What class of problem does it represent?** — the theoretical category that determines which body of research applies

These belong in different fields. Collapsing them produces vague diagnoses and mismatched theories.

### 6 — No forward references (VA-80)

Solve this challenge with what exists at this challenge: the PCO and the solutions of the challenges before it. Do not use a later challenge's mechanism, actor or vocabulary to close a gap here. If a condition cannot be met with what exists, record it as a residual carried to the later requirement by number, and say nothing about how that requirement solves it. A cell that names an actor or mechanism the architecture has not yet introduced is not complete; it is borrowing.

### 7 — Credibility mechanisms: name the receiver, the instrument and the supplier (VA-81)

Whenever a cell relies on an element whose job is to make an actor believe something — an endorsement, a certification, a signal, a warranty, a published record, a guarantee, "independent" anything — the cell is not complete until it states, in this order:

1. **Receiver.** The named actor whose belief changes, and the decision that belief changes (settle sooner; buy the portfolio; integrate the product).
2. **Proposition.** The one thing the receiver must accept as true.
3. **Instrument in use today.** What that receiver relies on now to accept propositions of this kind, with evidence. Their routine of trust, not ours.
4. **Instrument test.** The element must be that instrument, or a substitute the receiver already accepts. A signal the receiver cannot read is not a signal: it must be costly to fake and cheap for *that receiver* to read (Spence).
5. **Supplier test.** At least one named organisation sells or issues that instrument today, shown from public record *before* the element is admitted. If none does, the element is a component the venture must build and cost, not a partner to be found; write it as such.
6. **Re-derivation.** If a later challenge changes the receiver or the decision, the element is re-run at that challenge. It is never inherited by its label.

Properties of the provider — "independent", "no stake", "standing" — are necessary and never sufficient; "standing" has no meaning until the receiver is named. An element a later challenge depends on may not be deferred to "implementation".

*Failure this cures (Calmly C3, Aug 2026):* the cell required "an independent body with sufficient standing"; the shortlist chose CEDR by fit and speed; nobody asked which actor had to be convinced, what that actor reads, or whether CEDR sells the thing. C4 then moved the receiver from the defendant to the funder and the element was carried by label through C4–C10.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-challenge-6-custom/SKILL.md` to modify
- **Skill chain:** `/balm-challenge-5-custom` (R5) → `/balm-challenge-6-custom` (R6) → `/balm-challenge-7-custom` (R7)
- **R3 interaction:** R6's payment structure changes the working capital model — flag for R3 update if payment timing shifts
- **Related skills:** `/theory-of-change-custom` (ToC tool, invoke with "R6 Amortisation" if a formal ToC is required); `/ive-fit-verifier-custom` (FIT Verifier gate; runs after F1 is complete, not per F2 requirement)
- IVE source: Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–October 2025
- Customer Transformation Model (CTM) reference: Simanis (2021) — Phase 3 (Paying) is where the Buy Block lives

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** (Found on Calmly C1: "credible litigation backstop" — credibility is held by the defendant, and no product reached the defendant for three months.)

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R6 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R6 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `calmly-ctm-at-C6.html` |
| AOM | `[venture]-aom-at-C[N].html` | `calmly-aom-at-C6.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `calmly-fin-sim-at-C6.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user:
- "What product component does the Amortisation Strategy add or change?"
- Which CTM phase does it affect? **Phase 3 — Paying (payment trigger)**
- Which 4-D product delivers it? **Payment Product**
- What is the specific element? (e.g. "payment collected as a fixed percentage at the customer's income event — harvest sale, salary date")
- What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)

**R6 — update mode:** Add or modify only the affected Phase 3 rows in the existing CTM. The Amortisation Strategy adds or modifies the payment trigger mechanism in Phase 3 — Paying. Do not rebuild the whole document.

**Catch-up mode:** If the CTM does not yet exist (because prior challenges were run without this integrated structure), build it retrospectively from all confirmed strategies for R1 through R5, then add R6's payment mechanism.

**Diagram format:** follow `.claude/skills/shared/ctm-diagram-spec.md` exactly — horizontal swimlane flow diagram: sparse white state rectangles, coloured hexagon product nodes sitting *between* states on the transition arrows, decision diamonds where the journey forks, escalation box for formal/default tracks. No THINK/FEEL/DO matrix rows, no product tags inside state boxes. Read the spec before generating.

**File naming:** `[venture]-ctm-at-C[N].html` — label by challenge, not version number (per the naming table above).

**Execution route (mandatory — edit the model, generate the views):** the CTM lives as a model file, `[venture]-ctm-model-at-C[N].yaml`; the HTML record and the layered draw.io view are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed strategy as edits to states / transitions / component IDs (Flow Register format, e.g. `WP-2`). Reference implementation: `ventures/FinTech_Justice/calmly-ctm-model-at-C10.yaml`.
2. Generate both views:
   `python3 .claude/skills/shared/generators/generate_ctm_html.py <path>/[venture]-ctm-model-at-C[N].yaml`
   `python3 .claude/skills/shared/generators/generate_ctm_drawio.py <same YAML>`
3. The generators self-check and REFUSE to write on an incoherent model (a transition with no component and no flag, an unknown state, a malformed component ID). Fix the YAML — never hand-edit a generated file, never weaken the check.
4. **Catch-up:** if no model file exists yet (venture predates the model-file pattern), build the YAML from the current CTM record first, generate, confirm the output matches the record, then apply this challenge's changes.

Before proceeding to Section 6, confirm the CTM file has been written.

---

### Section 6 — AOM Update *(gate: CTM written)*

Ask the user:
- Which stream? **Using** (payment collection is a Using-phase activity — the customer uses the product and payment fires)
- Which level? (LMU / Territory / HQ)
- What role manages the payment collection trigger?
- How long does it take per unit?
- What is the volume driver? (per unit / per inquiry at X% conversion / per stage at Y% probability / fixed per LMU)

**Check for common errors before writing:**
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if the delivery role requires supervision or QA?
- Has a new HQ function been added if this solution requires central support (e.g. income-event payment processing at HQ)?

**LMU sizing check:**
1. Is this LMU large enough to be economically viable? (Enough volume to cover fixed LMU costs?)
2. Is this LMU small enough to replicate fast? (Can we stand up another one in weeks, not months?)
If both YES → PASS. If either NO → FLAG before proceeding.

**R6 — update mode:** Add or modify only the affected Using stream activity rows. Do not rebuild the whole AOM.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R6.

**R3 interaction:** If R6 changes payment timing (earlier or later), flag the working capital impact — the R3 fin-sim model may need updating. Note explicitly in the AOM whether this is cash-positive (earlier collection) or cash-negative (later collection) relative to the R3 baseline.

**Diagram format:** follow `.claude/skills/shared/aom-diagram-spec.md` exactly — Ops Map + flow diagram, not a table. Build the Ops Map first; activities are derived from flows, not invented.

**File naming:** `[venture]-aom-at-C[N].html` — label by challenge, not version number.

**Execution route (mandatory — edit the model, generate the views):** the AOM lives as a model file, `[venture]-aom-model-at-C[N].yaml` (actors · organisation with FTE and work drivers · components with allocations and DRIs · product/information/money flows per the IFC three-flow decomposition · spine order · waypoints). The views are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed changes. Reference implementation: `ventures/FinTech_Justice/calmly-aom-model-at-C10.yaml`.
2. Generate the views:
   `python3 .claude/skills/shared/generators/generate_aom_html.py <path>/[venture]-aom-model-at-C[N].yaml` (the Op Model Map)
   `python3 .claude/skills/shared/generators/generate_aom_drawio.py <same YAML>` (layered draw.io / Lucid view)
   `python3 .claude/skills/shared/generators/generate_aom_sysml.py <same YAML>` (machine-checkable SysML v2 — optional but recommended)
3. The generators self-check and REFUSE to write on an incoherent model (a component with no flow, an allocation to a non-existent function, a flow endpoint that resolves to nothing). Fix the YAML — never hand-edit a generated file, never weaken the check.
4. **Catch-up:** if no model file exists yet, build the YAML from the current AOM record first, generate, confirm equivalence, then apply this challenge's changes.

Before proceeding to Section 7, confirm the AOM file has been written.

---

### Section 7 — Fin-Sim Update *(gate: AOM written)*

Identify which AOM activity streams and levels were updated in Section 6. Then:

1. Map those activities to the financial model's cost lines:
   - **Using stream at LMU level** → drives COGS (payment collection activities per unit)
   - **Payment timing change** → updates working capital model (earlier collection reduces WC requirement; later collection increases it)
   - **Using stream at HQ level** → drives fixed overheads

2. Update the financial simulation with the new activity costs and timing.
   - If a fin-sim exists: update the relevant cost lines and the working capital timing. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM and any revised working capital structure.

---

### Section 8 — FIT Verifier Gate *(gate: fin-sim updated)*

Run the financial margin of safety calculation. Display it in this format:

```
COST FLOOR (from AOM)           £[X] / unit
REQUIRED PRICE (25% FMOS)       £[Y] / unit    ← cost floor ÷ (1 − 0.25)
PRICE CEILING (KMC from R2)     £[Z] / unit

HEADROOM                        £[W] / unit    ← ceiling minus required price
FMOS                            [X]%           ← (ceiling − floor) ÷ FLOOR

VERDICT: [PASS / BORDERLINE / FAIL]
```

⚠ **FMOS uses the cost denominator: `FMOS = (ceiling − floor) ÷ floor` = `(WTP_low − Cost_high) / Cost_high`** (Simanis, *Built to Hold*, p.7). Do **not** divide by the ceiling/price — `(ceiling − floor) ÷ ceiling` is the gross-margin metric, a different and incompatible figure that understates FMOS. WTP_low = R2 KMC / price ceiling; Cost_high = AOM high-point unit cost.

**For R6:** Use the R2 KMC as the price ceiling. The cost floor updates with the new AOM additions from R6 (payment collection activities). Note any working capital delta from the R3 baseline.

**Verdicts:**
- **PASS (≥25%):** Proceed to Section 9.
- **BORDERLINE (15–24%):** Surface the conditions. Ask user: accept and proceed, or revise? If they accept, note the conditions as critical assumptions.
- **FAIL (<15%):** Return to Section 2 (Buy Block diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Amortisation Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)

---

### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines, any working capital delta)
- Current FMOS and verdict
- Mark **R6 complete** (or fail) on the status board
- Route to **R7** (Activate Gateway Partners)

### WS1 Feedback Capture *(optional — prompted at every close)*

Before routing, ask:

> "Quick WS1 capture? (y / skip)"

If **y**, ask these four questions in sequence and append the responses to `FEEDBACK.md` using this format:

```
---
## R[N] · [venture name] · [date]

**1. Genuine mutations?** Did this challenge produce ≥2 genuine BFF mutations, or did it justify the existing design?

**2. Criteria signal:** Which registry criterion was most useful? Which should have fired but didn't?

**3. Correction needed?** Did the output require significant human correction? [yes/no — if yes, what]

**4. One change:** What would improve this challenge skill?
```

If **skip**, route immediately — no friction.


---

## ⛔ VDR completeness contract (added 28 Aug 2026, Tom's ruling — logged VA-73)

The VDR section this challenge produces must contain **every sub-requirement of this skill, labelled SR by SR**, each either completed in full or explicitly marked **OPEN with an owner**. The reference standard for the field set is the Calmly VDR (`calmlyresolve-venture-design-record-v12-2026-09-01.html`) — every challenge there carries its complete sub-requirement structure.

**A compressed section is not a completed challenge.** Diagnosis-plus-strategy prose that "covers the ground implicitly" fails this contract, whatever its quality: the sub-requirements are the method's decomposition, and an output that does not show them cannot be checked against them. The logged failure (28 Aug 2026): a full C4–C10 run delivered one diagnosis, one theory citation, one mutation gate and one strategy per challenge — and skipped every named sub-requirement in between. It read complete and was not.

**Rule:** sub-requirements not specified = the challenge is not done. Run `/verify-balm-custom` before declaring any multi-challenge run complete — completeness per sub-requirement is exactly what it checks.
