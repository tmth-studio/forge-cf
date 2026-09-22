---
name: balm-challenge-5-custom
description: IVE R5 — Eliminate the Biggest Learning Disruption (Use Block). Identifies the single biggest barrier to customers activating the product in their routine after they have decided to try it. Produces an Adoption Strategy that eliminates the Use Block.
---

# BALM R5 — Eliminate the Biggest Learning Disruption

**Purpose:** Identify the structural reason why customers who have decided to try the product cannot successfully integrate it into their routine. Produce an Adoption Strategy that eliminates — not reduces — the biggest learning disruption between intention and consistent use.

**When to run:** After R4 is solved. R4 addresses why customers doubt the value enough to try. R5 addresses why customers who have formed the intention to try still fail to activate. Do not run R5 until R4's Conviction Strategy is in place — the populations are different and the structural problems are different.

**Output:** Required Product Use Routine, Key Learning Block, Adoption Theory of Change, Adoption Strategy. Together these constitute the R5 component of the new Business Form Factor.

**Handoff to:** R6 (Circumvent the Cash Flow Constraint) — which addresses whether customers who are using the product can sustain payment for it.

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: the IVE canon — Simanis, E. et al. (2021), Cornell SC Johnson College of Business, and the co-authored papers 2023–2025 (Simanis, Manuel et al. 2023; Simanis et al. 2024; Simanis 2025). Full list at the foot of this skill or in `architect-custom`.

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

**→ This skill: R5 — Eliminate the Biggest Learning Disruption** (F2, second requirement; requires solved R4)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design.

---

## R5 definition

> Identify and eliminate the structural reason why customers who have decided to try the product cannot successfully integrate it into their routine. The Use Block is an activation problem — it occurs after the intention to try is formed but before consistent use is established. It lives in Phase 2 (Consuming) of the Customer Transformation Model.

R5's impact shows up in activation rates and in the depth of product integration. A strong Adoption Strategy often also advances R8 (switching cost) — the deeper the integration required to activate the product, the harder it is for the customer to leave once they do.

**Design principle — architect for mainstream adoption.** R5 must be designed for the customer with median tolerance for disruption — not for early adopters. Early adopters have disproportionate willingness to work through activation barriers. The mainstream customer does not. Designing R5 for the enthusiast produces an architecture that breaks when the venture reaches scale.

---

## The Use Block — three structural causes

R5 begins with diagnosis. The Use Block has three distinct structural causes, and the Adoption Strategy must be designed to match the primary cause. Designing for the wrong cause produces a solution that reduces disruption without eliminating the structural barrier.

| Cause | What it is | What it looks like |
|-------|-----------|-------------------|
| **Learning burden** | The product requires the customer to learn new skills, concepts, or behaviours before receiving value. The learning curve is too steep relative to the perceived gain at the trial stage. | Customers try once, find the product confusing or demanding, and revert to their prior routine. They do not say it is bad — they say it is "not for them." |
| **Routine disruption** | Integrating the product requires changing embedded habits or workflows. The disruption cost exceeds the perceived benefit at the point of activation. | Customers use the product inconsistently — when they remember, or when it is convenient. They do not build it into their routine because doing so requires displacing something that already runs on autopilot. |
| **Dependency gap** | The product works only when other conditions are met — infrastructure, partner behaviour, complementary products — that the customer cannot control or guarantee at the point of trial. | Customers want to use the product but cannot. The barrier is external to their own motivation or capability. They are blocked, not reluctant. |

**Diagnosis discipline:** the Use Block is not the same as the Want Block (R4). A customer who has not yet formed the intention to try has a Want Block — R4 addresses that. R5 only applies after R4 is confirmed. Solving R5 for customers who have not cleared R4 wastes architecture on a problem that does not yet exist.

---

## Why onboarding is not R5

A tutorial, guided setup, or user onboarding flow reduces learning burden — it does not eliminate the Use Block. Any incumbent can add an onboarding flow. R5 requires an architectural change that makes the disruption structurally unnecessary, not a process that guides the customer through it.

The test: could an incumbent operating within the existing BFF adopt the same solution without changing their architecture? If yes, it is not R5.

**Worked contrast — personal finance software:**
- **Not R5:** a guided setup wizard that walks the customer through categorising their transactions.
- **R5:** automatic bank feed integration that categorises transactions without the customer doing anything — eliminating the Learning Burden of the categorisation routine entirely.

The first solution reduces the burden of learning. The second eliminates the need to learn. That is the R5 distinction.

---

## This skill IS a design loop (read first)

Running R5 is not a five-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.**

The four steps map onto this skill's existing structure:
- **Diagnose** — the Required Product Use Routine + the Key Learning Block (the Use Block this challenge isolates).
- **VA-23 at Diagnose (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30) — the bottleneck is the at-scale one.** A launch constraint — no cash, the founder's hours, no cold outreach, a pilot's volume, a phase — is not a bottleneck and does not enter Diagnose, Theorize, Productize or Simulate at any of C1–C10. Test every candidate block: can the workaround be described without a phase, a pilot, a joint venture or a bootstrap? If not, it is a launch-instance item; write it in the carried-items row "carried to pilot-instance design after R10" and nowhere else. Tom's correction, 17 Sep 2026; RD-033.
- **Theorize** — the Adoption Theory of Change (named mechanism; prescriptive, not descriptive).
- **Productize** — the Adoption Strategy + cumulative BFF (C1–C5) + the CTM/AOM update (the architectural decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back. R5 sits in F2 (adoption), but the gate still runs — activation activities add to the cost floor.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure. `[evidence: VA-FID1]`

**Simulate — the gate with teeth (mandatory; do not skip on illustrative data).** A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R5 has not been designed, only described. The Section 8 FIT gate enforces this; the rules below govern it.

1. **Use the correct FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling; Cost_high = the AOM high-point unit cost. **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on? (For R5, the activation / Using-stream cost per unit is usually one of them.)
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL and the specific result that would force a pivot: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* The bar for a sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

**Loop-back and the pivot discipline.**
- **FAIL or BORDERLINE → return to Diagnose** (Section 2 — the Use Block diagnosis), not to a tweak. Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why the challenge will not clear and what decision is needed.
- **Loop counter and the third loop (VA-151, RD-036) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).** Print `loop_backs: n` in the gate verdict block. At the third loop-back the run states whether the next turn is a **pivot** (the theorem or the strategy changes) or a **mutation** (same theorem, a different form), and names the FIT line that decides it. A third loop that names neither is the `FLAG FOR TOM` above.
- **Four loop-gate branches (VA-153, RD-037) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).**
  1. *Later owner, adjacent:* a FAIL whose lever the next requirement owns routes forward with the FAIL inherited and the owner named in the verdict block.
  2. *Later owner, non-adjacent:* routes in sequence, the FAIL inherited through every requirement between, with a VA-85 lock on the owner; no requirement between may claim the repair.
  3. *Repair on a re-derived upstream figure:* the repair is claimed, the re-derived figure is named as the critical assumption, the verdict caps at PROVISIONAL, and the upstream requirement's row is annotated, not overwritten.
  4. *Warning band with no person present (autonomous mode):* accept with conditions and record the decision, or revise once and record the loop-back. Never stall; never choose silently. The choice and its reason go in the verdict block.
- **Close criterion.** Mark R5 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## How this skill runs

Open by showing the user this checklist:

```
R5 sub-requirements — we will step through each in order:

[ ] 1. Required Product Use Routine
[ ] 2. Key Learning Block
[ ] 3. Adoption Theory of Change
[ ] 4. Adoption Strategy
[ ] 5. Business Form Factor (C1–C5)
```

Then work through each sub-requirement one at a time. Show the name and definition, ask the user to answer it, confirm the answer, mark it complete, then move to the next. Do not proceed until the current sub-requirement is confirmed.

---

## Sub-requirement 1: Required Product Use Routine

**Definition:** *The steps involved in using the interim offering and the things the target customer must do in order for it to 'work' — i.e., it generates the targeted reduction in the Key Cost.*

Ask the user to map the full step sequence the customer must follow to use the product correctly. This is not the ideal journey — it is what is actually required for the product to generate value. Number each step. Confirm before proceeding.

**Guidance for the user:**
- Start from the moment the customer decides to use the product on a given occasion
- End at the point where the Key Cost reduction is delivered
- Include every required action — setup, inputs, decisions, behaviours
- Do not optimise the steps yet; map what is actually required

---

## Sub-requirement 2: Key Learning Block

**Definition:** *The main factor that causes customers to implicitly or explicitly question whether they can use the product correctly or doubt the value of investing time and energy mastering its proper usage.*

Once the Required Product Use Routine is confirmed, ask the user: which step in the routine is where the Key Learning Block manifests most acutely? The answer must be tied to a specific step number, not stated generically.

**Guidance — three structural causes to apply:**

| Cause | What it is |
|-------|-----------|
| **Learning burden** | The product requires the customer to learn new skills, concepts, or behaviours before receiving value |
| **Routine disruption** | Integrating the product requires changing embedded habits or workflows |
| **Dependency gap** | The product works only when other conditions — infrastructure, partner behaviour, complementary products — are met |

**Diagnostic questions:**
- Is the customer failing because they cannot learn fast enough (learning burden), because the product collides with an existing habit (routine disruption), or because something outside their control prevents use (dependency gap)?
- What does the customer do when activation fails — do they stop trying, try intermittently, or seek a workaround?
- Which customer cluster from R2 research faces the most acute Use Block?

**State as:** the step number, the structural cause (one of the three), and the specific manifestation at that step.

---

## Sub-requirement 3: Adoption Theory of Change

**Definition:** *The nature of the customer learning challenge (e.g., complex, tacit, risky, disruptive) posed by the Key Learning Block and the theory/ies most effective in explaining how to solve that type of challenge.*

Invoke `/theory-of-change-custom` with the frame "R5 Adoption" to develop this formally if needed.

**Must include:**
- **Nature of the challenge** — a named class: complex, tacit, risky, or disruptive
- **Theory** — a citable theory or model that explains how that type of challenge is solved
- **Context** — the specific situation in which this theory applies to this venture
- **Outcome** — what "completed" looks like: the state in which the customer has cleared the learning block and is using the product consistently

**Guidance:**
- The nature of the challenge must be derived from the Key Learning Block diagnosis, not stated generically
- The theory must be citable — name it precisely (e.g., situated learning, deliberate practice, scaffolding)
- Context grounds the theory in this venture's specific customer and routine — not a general application
- Confirm the full four-part structure before proceeding

---

## Sub-requirement 4: Adoption Strategy

**Definition:** *The best way to operationalize the Adoption TOC for getting around or eliminating entirely the customer's Key Learning Block.*

⚠ **MANDATORY — before writing the Adoption Strategy, complete these three steps in order:**

**Step 4a — Baseline honestly.** State where the current BFF stands on the Key Learning Block / Use Block. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 4b — Generate ≥2 candidate BFF mutations.** Structural changes (not features) that could eliminate the Use Block materially better than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 4c until two real mutations exist on the table.

**Step 4c — Evaluate and decide.** For each candidate: does it eliminate (not reduce) the primary structural cause (learning burden / routine disruption / dependency gap)? Is it designed for mainstream customers, not early adopters? What does it cost in coherence with R1–R4? Record the decision. Adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Adoption Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R5
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

Only after the contract block is emitted, write the Adoption Strategy.

**Architectural test:** does this eliminate (not reduce) the Key Learning Block? If the strategy merely makes the block easier to get through, it is not R5. State as a strategy — a direction of architectural intervention — not a product feature or an onboarding process.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

**Constraints:**
- Must work within the BFF the Workaround Strategy from R1 established
- Cannot require a cost structure that violates the R1 cost floor
- Must be designed for the mainstream customer, not the early adopter

**R8 signal:** does the mechanism that eliminates the Use Block also create stickiness? The deeper the integration required to activate the product, the harder it is for the customer to leave. Flag this explicitly.

**Quality tests:**
- Does the strategy eliminate (not reduce) the primary disruption?
- Is it stated as a strategy, not a feature or onboarding process?
- Does it work within the R1 BFF?
- Could an incumbent adopt it without changing their BFF? (If yes, rethink.)
- Is it designed for mainstream customers, not early adopters?

---

## Productizing R5 — Strategy → BFF

The Adoption Strategy names the mechanism that eliminates the learning disruption. Productizing it means shaping the Working Product so the disruption cannot occur if the product is used as designed — not reducing disruption through better support or onboarding.

**Target product component:** Working Product (Using — activation)

Work through these three questions before writing the cumulative BFF:

**1. Elimination, not reduction.** Does the product form factor make the Key Learning Block structurally impossible — because the design prevents it from occurring — or does it reduce the disruption by adding support? Reduction is staffing. Elimination is architecture. If the Adoption Strategy requires an onboarding team, a help desk, or guided sessions to work, the product form has not been productized. Ask: if the customer used the product for the first time entirely alone, would the block still occur?

**2. Accumulation.** Does the Adoption Strategy work within the BFF shape R1–R4 established? Specifically: does the activation mechanism fit within the delivery form R1 set and the conviction promise R4 made? If a customer arrives expecting the product the Attraction Strategy described and encounters a different activation experience, the R4→R5 transition has an architectural fault. Confirm these are consistent.

**3. R8 pre-load.** Does the activation mechanism begin building a switching cost as a by-product of use — data accumulated, routines established, integrations formed? A strong R5 solution that also pre-loads R8 is more valuable than one that solves activation in isolation. Note any accumulation effects and flag them for R8 design.

**4. At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A BFF that requires founding-team bandwidth, managed-by-exception operations, or pilot-only concessions is a launch-phase design, not an architecture. Name the at-scale volume explicitly. If the mechanism breaks before reaching it, return to Diagnose.

When all three are confirmed, identify the architectural spine before writing anything.

**Step 0 — Find the architectural spine.** The architectural spine is the single mechanism that runs through all prior requirements — the element whose removal would cascade failures across the most of C1 through C[N]. Every BFF has one. Finding it before writing forces the statement to be an architecture, not a list.

Diagnostic question: what would break first if you removed one core element from the design? The mechanism that cascades failures across the most requirements is the spine.

Write the opening sentence of the BFF around it. If the opening sentence could be "A product that does X (C1); does Y (C2); does Z (C3)..." — the spine has not been found. Go back and find it.

Write the cumulative BFF (C1–C5).

⛔ **MANDATORY HANDOFF — BFF C1–C5 CONFIRMED. DO NOT EDIT THE VDR. DO NOT PROCEED TO R6.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "BFF C1–C5 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## Sub-requirement 5: Business Form Factor (C1–C5)

**Definition:** *A cumulative statement of the venture's form factor incorporating all solutions from C1 through C5.*

Ask the user to state the updated BFF — a single coherent description that incorporates the Adoption Strategy alongside the solutions from R1 through R4. The BFF statement should be readable as a description of the venture's architecture, not a list of solutions.

**The test for a BFF statement vs a list:** remove the challenge labels (C1, C2, C3...) and read it cold. Does it describe a product? Or a checklist? If a checklist, the architectural spine has not been found. A properly constructed BFF reads as a description of one coherent product — the challenge labels appear as parenthetical citations, not as the structural joints holding the sentence together.

---

## R5 output format

```
SUMMARY
  Adoption Strategy: [strategy in one sentence — the architectural direction]
  Block eliminated: [key learning block in one phrase]
  Grounded in: [named theory — class of problem]

R5 — LEARNING DISRUPTION (USE BLOCK)
---
REQUIRED PRODUCT USE ROUTINE
  Step 1: [...]
  Step 2: [...]
  [...]

KEY LEARNING BLOCK
  Step where block manifests: [specific step number and description]
  Structural cause: [Learning burden / Routine disruption / Dependency gap]
  Specific manifestation: [what breaks down at that step]

ADOPTION THEORY OF CHANGE
  Nature of the challenge: [complex / tacit / risky / disruptive]
  Theory: [citation]
  Context: [specific to this venture and customer]
  Outcome: [completed state — what consistent use looks like]

ADOPTION STRATEGY
  [one to three sentences — the architectural direction, not the product feature]
  Mechanism: [how this eliminates — not reduces — the block]
  R8 signal: [does this create future stickiness? Yes / No / Partial]

BUSINESS FORM FACTOR (C1–C5)
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

ACTOR BUSINESS CASES (VA-127) — mandatory; one row per behaviour the architecture needs from anyone but the venture; a blank table is a FAIL
  For every actor whose behaviour this requirement's mechanism depends on (customer, counterparty, partner, payer, supplier, regulator):
    Actor: [role, not a name]   Behaviour needed: [the act, as a verb]   How often: [per transaction / once / per period]
    What it gains: [priced, by class — expended / foregone / risk-borne / friction; central with band; source tier]
    What it costs: [priced — time at loaded rate, money, risk taken on; band]
    Best alternative for this actor: [what it does today, or the rival it could use; its deflated surplus]
    Arithmetic (VA-157 — two literal lines; a row without both is blank and FAILS):
      central:      gain £[x] − cost £[y] − alternative's surplus £[z] = surplus £[s]
      pessimistic:  gain £[x] − cost £[y] − alternative's surplus £[z] = surplus £[s]
    Surplus vs alternative: [PASS if pessimistic surplus > 0 · PROVISIONAL if > 0 at central only · FAIL if ≤ 0 at central]
    If FAIL or unpriced: the other force that supplies the behaviour: [a named party's request · a contract · a regulation · a relationship the architect holds — and what it costs that party]
  A behaviour the architecture needs with no positive surplus and no named force is a design defect (VA-89), not a constraint.

VA-102 — actor tracks opened at arrival / dispositions stated / counterparty drivers with acquiring transition: [list or 'no new actor or counterparty this challenge']

BFF DELTA AND UPSTREAM RE-VERIFICATION (VA-103) — mandatory; a blank table is a FAIL
  What changed in the BFF at this requirement: [the structural change, or "no change — held"; at C1 this is the baseline BFF]
  Earlier requirements this same move ALSO serves (VA-106): [requirement numbers, and for each the mechanism by which this one move serves it — or "none: this move serves this requirement only"]
  For every earlier requirement (C1 to C[N-1]), on the BFF as it now stands (at C1: "none — first requirement"):
    C1  named checks: [unchanged / re-verified / FAILED — which check]   FIT: [unchanged / re-verified: FMOS x% / FAILED]
    C2  …one row per earlier requirement, none omitted…
  Any FAILED row: dispose under VA-89; the verdict here is capped by VA-95 and the row's requirement is annotated, not overwritten
  Function-gate re-run (only at C3, C7, C10): [every earlier requirement re-run in full on the cumulative BFF — filename of the consistency audit + verification artefact, or NOT YET]

QUALITY CHECK
  Does the strategy eliminate (not reduce) the primary disruption? [Yes / Partial / No]
  Does it work within the R1 BFF? [Yes / No]
  Could an incumbent do this without changing their BFF? [Yes — rethink / No — good]
  Is it designed for mainstream customers, not early adopters? [Yes / No]
  Confidence: [High / Medium / Low]
  What would increase confidence? [one specific check]
```

---

## Common failure patterns at R5

| Failure | What it looks like | What it means |
|---------|-------------------|---------------|
| User onboarding as R5 | A guided setup or tutorial is proposed as the Adoption Strategy | Tutorials reduce learning burden — they do not eliminate the Use Block. Any incumbent can add a tutorial. R5 requires an architectural change that makes the disruption structurally unnecessary. |
| Solving the Want Block again | The strategy is designed to convince customers the product is worth trying | R4 addresses conviction. If customers are not trying at all, R4 has not been solved. R5 only applies after R4 is confirmed — the populations are different. |
| Dependency gap ignored | The learning burden is addressed but the product requires conditions the customer cannot control | When the primary cause is a dependency gap, solving the learning burden is insufficient. The dependency must be resolved architecturally — usually by the venture taking on the dependency rather than requiring the customer to manage it. |
| Designed for early adopters | The Adoption Strategy assumes high tolerance for disruption, complexity, or new behaviour | Early adopters have disproportionate tolerance. The mainstream customer does not. An architecture that works for the enthusiast fails when the venture reaches scale. |
| Reducing disruption, not eliminating it | The strategy makes activation easier but does not remove the structural barrier | "Reduce" and "eliminate" are not the same. R5 requires a mechanism that makes the Use Block structurally impossible — not one that requires less effort to get through it. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

**Sequence:**
- **R4** (prerequisite) → solves the Want Block; proves customers have formed the intention to try
- **R5** → solves the Use Block; ensures customers who intend to try can actually activate the product
- **R6** → addresses the Buy Block; whether customers who are using the product can sustain payment for it

**R5 vs R4 distinction:** R4 addresses conviction — the gap between awareness and intention to try. R5 addresses activation — the gap between intention to try and consistent use. Customers can clear R4 and still fail at R5. The two structural problems are distinct and require different architectural solutions.

**R5 → R8 link:** the Adoption Strategy that eliminates the Use Block often creates switching cost as a byproduct. The deeper the integration required to activate the product in the customer's routine, the harder it is to leave. Flag this signal during R5 design and develop it fully at R8.

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles the biggest learning disruption (the Use Block). It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on the biggest learning disruption (the Use Block)? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on the biggest learning disruption (the Use Block) than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on the biggest learning disruption (the Use Block) vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
5. **Decide and record** — adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

**VA-4 — show your working.** The candidates considered and rejected are not scratch work. Record them in the "considered / not chosen" block of the output format so the choice is auditable. Where a sub-requirement selects among options, first consider 2–3 — across the relevant customers/partners — then record which won and why the others lost.

**VA-1 — synthesis test.** When the (possibly evolved) BFF is stated, anchor it: "this now looks like [real business], because [shared mechanism]." If no clean analogue exists, flag it — the parts have not yet cohered into one business.

**VA-103 — the juggling question, made mechanical.** Canon reconceives the form factor after every theory of change, asking which BFF best supports all of them so far (Business Architecture Framework, 2023, p.10); a system solved for its functions sequentially is the failure the method names (Core Business Archetype, 2024, p.10). So at every requirement, after the synthesis check: (1) state what changed in the BFF; (2) re-run every earlier requirement's named checks and FIT on the BFF as it now stands, one row each, marked unchanged / re-verified / FAILED — an earlier pass is not evidence once the BFF has moved; (3) at each function gate (C3, C7, C10) re-run every earlier requirement in full on the cumulative BFF and run the consistency audit and venture verification there (extends VA-90's trigger list to after F2). Arrows point inward until nothing moves; only then may the BFF be said to explain the challenges. The closing state at C10 is ten verdicts on one BFF, each re-verified on the same cumulative state — a requirement whose last verification predates the last BFF move is not closed. (Tom, 8 September 2026, on delegation.)

**VA-127 — every actor the architecture needs carries a priced business case, gated against its own alternative.** VA-99 says an enabler carries a business case rather than a KMC; it does not say the case must be priced, and no challenge's output contract asks for the number. So a mechanism can be true (the partner already performs the act) and worthless (routing it through the venture is worth nothing to the partner) and clear every named check. Readback C7, 11 September 2026: the anchor buyer's stated value — its statutory payment-practices report as a by-product — priced at about £1,000 a year against a £1,285 compilation cost, once an OCV was actually computed for the buyer; the small buyer's surplus was £4 at central and negative at the pessimistic corner. The behaviour the whole architecture rested on — confirmation — was allocated to the actor the record had studied least, and the Integration ToC read as answered because it named a theory (North 1990) without pricing the cost the theory says drives adoption. The rule: for each behaviour the architecture depends on, name the actor, price what it gains and what it costs, show the surplus against its best alternative — or name the other force that supplies the behaviour and what that force costs its supplier. Unpriced and unforced is a design defect. (Tom, 11 September 2026: "should always explain why actor carries the product.")

**VA-106 — name the earlier requirements this move also serves, or say it serves none.** The ten requirements are constraints the whole business form factor must satisfy together, so one structural move can close several at once, and a design in which no move ever does is a set of parts rather than one business (VA-1). **State the count and the mechanism at every requirement, in the table above.** "None: this move serves this requirement only" is a legitimate and common answer — the rule asks the question and forbids no answer. **The verification pass scores this from the table you wrote, not from its own reading**, so a requirement that leaves the line blank has not completed its output block. `[evidence: VA-106]`

*(VA-102 insert — Head of R&D, 16 Sep 2026, object-after 18 Sep 12:00; closes canon-sweep finding (i))*

**VA-102 — every actor track opens at arrival, and a named absence names its substitute.** The customer's four fixed states put arrival at the front of the customer's journey. They bind no other actor, so a user track or a partner track can open on an actor already engaged with the venture and nothing objects. Whenever this requirement's move adds or changes an actor track (a user, a partner, a payer, a funder, a supplier) or adds a resource-model driver that scales with a count of counterparties, answer three questions in the output block. **(1) Where does each actor's track open?** At a state in which the actor does not yet know the venture exists — or with a recorded reason for opening later. A non-customer track may compress the customer's four states; it may not skip arrival silently. **(2) Where a transition carries no product by decision, what activity does the work instead?** Name it, and put it in the operating model with a driver. An activity named in prose and performed by a person is in the operating model, or it is not in the venture; assigning it to the principal moves it to a resource nothing sizes. **(3) For every driver that scales with a count of counterparties, which routine is accountable for it and which journey transition acquires them?** The rule asks a question and forbids no answer: "no acquisition activity, by design" passes where the mechanism that replaces it is named and its cost is driven. The abuse test: an actor whose participation the architecture asserts may not be disposed of as not-applicable; if the design fails when that actor declines, the actor arrived somehow, and the model says how. **The score this run will meet:** `validate_model.py` runs `_check_track_arrival` on every user track and partner track, and it is a hard error on any model dated on or after `ARRIVAL_RULE_FROM = 2026-09-07`; regression R-CTM9 checks clause 1 and R-W15 checks clause 3, in both directions. A requirement that adds no actor and no counterparty driver writes "no new actor or counterparty this challenge" on the line, and that answer passes. `[evidence: VA-102]`

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

*The failure this cures:* a cell required a provider property rather than a named receiver; the shortlist was chosen on fit and speed; nobody asked which actor had to be convinced, what that actor reads, or whether the supplier sells the thing. A later challenge then moved the receiver, and the element was carried forward by label to the end of the run. `[evidence: VA-81]`

---

### 8 — Test whether an X exists before designing for one, and admit an internal holder (VA-92)

Every requirement that asks *who is the X* — the gateway partner, the block, the intermediary, the supplier, the constraint — must first test whether an X exists on this venture. Enumerate candidates only after the test.

**Three dispositions, not one.** Each is a legitimate answer:

- **(a) An external holder, activated.** The conventional answer the requirement was written for.
- **(b) An internal holder the architecture has already activated.** A function inside the customer's own organisation, or inside the venture, that is already performing the work without being named as the thing the requirement asks for. Where this is the answer, **the requirement's work is to make its output portable to the next customer, not to recruit it.**
- **(c) A stated absence, on falsifiable tests, with the arithmetic published.** Name the tests, answer each from the record, and publish the numbers that settle them.

**Run the affordability screen before enumerating candidates.** State the maximum the architecture can pay any holder of this role, derived from the venture's own binding gate, before a single candidate is named. **Invert it where the role holder pays the venture rather than being paid by it (added 4 September 2026).** For a customer, a payer or any role that is a source of money, the screen becomes **the minimum the architecture must charge**, derived the same way from the binding gate. Stating a maximum-payable for a role that pays you is meaningless, and a run that follows the wording literally will either skip the screen or produce a number with no referent. `[evidence: VA-92]`

**The failure this cures runs in both directions.** A run following the form literally when no X exists will either manufacture one — the exact failure the "do not manufacture a partner" instruction warns against — or record the requirement as not applicable and lose its whole value. On the venture that produced this rule, two requirements reached the right answer only by working against the skill's framing, and both answers came from the redirect rather than from the enumeration. `[evidence: VA-92]`

**Where the absence is found, redirect rather than close.** State the question that is live instead. A worked redirect from the cash-flow requirement — *what observable event fires payment, and is it the event the financial model assumes?* — carried the whole of that requirement's value. `[evidence: VA-92]`

---

### 9 — Challenges that share the cumulative business form factor do not close in parallel (VA-85)

The dependency matrix already knows which requirements share inputs. Sequence those. Where a run must proceed in parallel on the principal's instruction, it is **forbidden from closing its gate on a shared input** and must declare that slot OPEN in its cumulative statement.

*Failures this cures, both within two days (2–4 September 2026):* four workstreams resolved 22 findings in parallel without reading each other, and the re-run audit scored every original finding closed while returning ten fresh contradictions, all of one kind — a resolution written without reading a resolution of the same date. Then R2 and R3 ran in parallel: R3 declared its C2 slot OPEN, correctly, and the damage was one assembled sentence in the design record rather than a contradiction. The rule is what made the second outcome cheap.

---

### 10 — A long production run writes incrementally (VA-88)

For any step expected to run long: **create the output file with its section headings before reading the sources, and save after each section.** Work on disk survives an interrupted run. Work held in context does not. **The skeleton exists so the file exists; its headings carry no authority (added 4 September 2026).** Headings written before the skills are read will sometimes be wrong — a challenge may define four sub-requirements where the skeleton assumed five. Overwrite them without ceremony. A run that keeps a wrong heading because it wrote it first has inverted the purpose of this rule.

*Failure this cures (3 September 2026):* three runs on one venture stalled with the same signature — a long stretch of reading with no write, then the run ended. The two that had already written files lost nothing. The one that had written nothing lost everything. The next run was told to write the skeleton first and completed cleanly.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-challenge-5-custom/SKILL.md` to modify
- **Skill chain:** `/balm-challenge-4-custom` (R4) → `/balm-challenge-5-custom` (R5) → `/balm-challenge-6-custom` (R6)
- **Related skills:** `/theory-of-change-custom` (ToC tool, invoke with "R5 Adoption" if a formal ToC is required); `/ive-fit-verifier-custom` (FIT Verifier gate runs after F1, not per F2 requirement)
- IVE source — the canon is a body of co-authored work, not one paper:
  - Simanis, E., Samani, S., Burnett, P. & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *Rediscovering Capitalism: How Blue-Chip Builders Created Transformative Impact and Profit.* YNOT Institute Working Paper 1, Queens' College Cambridge
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *The Business Architecture: The Hidden Code of Industry Disruption.* YNOT Institute Working Paper 2, Queens' College Cambridge — the Business Architecture Framework
  - Simanis, E. et al. (2024). *The Core Business Archetype* (Jan); *Engineering New Market Ventures* (Apr); *The Market Creator's Dilemma* (Nov)
  - Simanis, E. (2025). *Built to Hold* — the FMOS gates; Simanis, E. & Donohue, K. (2025). *Deciphering the Market Creator's Dilemma.* MIT Sloan Management Review
  - Attribution rule (WS1 feedback log, 5 and 17 Sep 2026): Tom Manuel is a co-author on the 2023 papers; "co-developer of the method" is not supported. TMTH's own additions are the WS1 standards, the VA register, the circle end-state and the direction rule
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–October 2025
- Customer Transformation Model (CTM) reference: Simanis (2021) — Phase 2 (Consuming) is where the Use Block lives

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** `[evidence: VA-71]`

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R5 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R5 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `acme-ctm-at-C5.html` |
| AOM | `[venture]-aom-at-C[N].html` | `acme-aom-at-C5.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `acme-fin-sim-at-C5.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user:
- "What product component does the Adoption Strategy add or change?"
- Which CTM phase does it affect? **Phase 2 — Consuming (activation)**
- Which 4-D product delivers it? **Working Product**
- What is the specific element? (e.g. "automatic bank feed integration that eliminates the categorisation learning burden at first use")
- What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)

**R5 — update mode:** Add or modify only the affected Phase 2 rows in the existing CTM. The Adoption Strategy adds the activation mechanism in Phase 2 — Consuming. Do not rebuild the whole document.

**Catch-up mode:** If the CTM does not yet exist (because prior challenges were run without this integrated structure), build it retrospectively from all confirmed strategies for R1 through R4, then add R5's activation mechanism.

**Diagram format:** follow `.claude/skills/shared/ctm-diagram-spec.md` exactly — horizontal swimlane flow diagram: sparse white state rectangles, coloured hexagon product nodes sitting *between* states on the transition arrows, decision diamonds where the journey forks, escalation box for formal/default tracks. No THINK/FEEL/DO matrix rows, no product tags inside state boxes. Read the spec before generating.

**File naming:** `[venture]-ctm-at-C[N].html` — label by challenge, not version number (per the naming table above).

**Execution route (mandatory — edit the model, generate the views):** the CTM lives as a model file, `[venture]-ctm-model-at-C[N].yaml`; the HTML record and the layered draw.io view are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed strategy as edits to states / transitions / component IDs (Flow Register format, e.g. `WP-2`). The format authority is `.claude/skills/shared/ctm-diagram-spec.md`. Do not read another venture's model file to learn the format. `[evidence: VA-BS1]`
2. Generate both views:
   `python3 .claude/skills/shared/generators/generate_ctm_html.py <path>/[venture]-ctm-model-at-C[N].yaml`
   `python3 .claude/skills/shared/generators/generate_ctm_drawio.py <same YAML>`
3. The generators self-check and REFUSE to write on an incoherent model (a transition with no component and no flag, an unknown state, a malformed component ID). Fix the YAML — never hand-edit a generated file, never weaken the check.
4. **Catch-up:** if no model file exists yet (venture predates the model-file pattern), build the YAML from the current CTM record first, generate, confirm the output matches the record, then apply this challenge's changes.

Before proceeding to Section 6, confirm the CTM file has been written.

---

### Section 6 — AOM Update *(gate: CTM written)*

Ask the user:
- Which stream? **Using**
- Which level? (LMU / Territory / HQ)
- What role delivers the Adoption mechanism?
- How long does it take per unit?
- What is the volume driver? (per unit / per inquiry at X% conversion / per stage at Y% probability / fixed per LMU)

**Check for common errors before writing:**
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if the delivery role requires supervision or QA?
- Has a new HQ function been added if this solution requires central support?

**LMU sizing check:**
1. Is this LMU large enough to be economically viable? (Enough volume to cover fixed LMU costs?)
2. Is this LMU small enough to replicate fast? (Can we stand up another one in weeks, not months?)
If both YES → PASS. If either NO → FLAG before proceeding.

**R5 — update mode:** Add or modify only the affected Using stream activity rows. Do not rebuild the whole AOM.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R5.

**Diagram format:** follow `.claude/skills/shared/aom-diagram-spec.md` exactly — Ops Map + flow diagram, not a table. Build the Ops Map first; activities are derived from flows, not invented.

**File naming:** `[venture]-aom-at-C[N].html` — label by challenge, not version number.

**Execution route (mandatory — edit the model, generate the views):** the AOM lives as a model file, `[venture]-aom-model-at-C[N].yaml` (actors · organisation with FTE and work drivers · components with allocations and DRIs · product/information/money flows per the IFC three-flow decomposition · spine order · waypoints). The views are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed changes. The format authority is `.claude/skills/shared/aom-diagram-spec.md`. Do not read another venture's model file to learn the format. `[evidence: VA-BS1]`
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
   - **Using stream at LMU level** → drives COGS (direct delivery cost per case/unit — activation onboarding activities)
   - **Using stream at HQ level** → drives fixed overheads
   - **Timing of activities relative to revenue** → drives working capital

2. Update the financial simulation with the new activity costs and timing.
   - If a fin-sim exists: update the relevant cost lines. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM.

---

### Section 8 — FIT Verifier Gate *(gate: fin-sim updated)*

Run the financial margin of safety calculation. Display it in this format:

```
COST FLOOR (Cost_high, from AOM)   £[X] / unit
REQUIRED PRICE (25% FMOS)          £[Y] / unit    ← cost floor × 1.25
PRICE CEILING (KMC from R2 = WTP_low) £[Z] / unit

HEADROOM                           £[W] / unit    ← ceiling minus required price
FMOS                               [X]%           ← (WTP_low − Cost_high) ÷ Cost_high

VERDICT: [PASS / BORDERLINE / FAIL]
```

**The gate verdict block — literal, filled here, not described later (VA-157, RD-038) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).** The three-limb close (Step 5 below) fills this block. Print it beside the FIT result now, in this form, and fill every field; a run file that lacks the literal block is refused (the fix R-W5 asked for). It is the same block as Step 5's and the two must be identical.

```
GATE VERDICT — on the cumulative architecture C1 to C[N]
  logical limb:      [PASS / PROVISIONAL / FAIL]    checks failed: [n]
  operational limb:  [PASS / PROVISIONAL / FAIL]    checks failed: [n]
  financial limb:    [PASS / BORDERLINE / FAIL]     FMOS [X]% · binding gate [name]: [surplus / breach]
  dispositions:      [every failed check, with its kind]
  capacity figure:   [the single figure, and confirmation prose and arithmetic use the same one]   VA-91
  independence:      [shown / NOT shown — are the two financial halves one measure?]              VA-97
  gates driven:      [n gates tested; first to fail: [name], margin [x]]                           VA-84
  verification:      [artefact filename, or NONE — a requirement without one closes PROVISIONAL at most]  VA-90
  inherited:         [worst verdict of any prior challenge this builds on, and which]
  repairs:           [any upstream failed check this closes — name it, show the arithmetic — or "none"]
  loop_backs:        [n this requirement; at 3 — pivot / mutation, stated, with the FIT line that decides]   VA-151
  loop-gate branch:  [for every FAIL — this / adjacent / non-adjacent owner · re-derived cap · autonomous choice, with record]   VA-153
  launch constraints:[none inside SR1–SRn and this block — or the offending line, which fails the logical limb]   VA-23
  spread count:      [the one count used for any fixed-cost spread, why it is the at-scale count; margin at the PCO's other counts]   VA-162
  shared input:      [none — or the input that drives both the margin and the binding gate; then independence reads NOT shown]   VA-160
  VERDICT:           [PASS / PROVISIONAL / FAIL]  — may not exceed `inherited` unless a repair is shown
```

**FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high`, where WTP_low = the R2 KMC / price ceiling and Cost_high = the cost floor (AOM high-point unit cost). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure.

**For R5:** Use the R2 KMC as WTP_low (the price ceiling). The cost floor updates with the new AOM additions from R5 (Using stream activation activities).

**Verdicts (cost-denominator FMOS):**
- **PASS (≥25%):** The financial limb's first half clears. Proceed to the three-limb close below — never straight to Section 9.
- **BORDERLINE (25–59% at full model; treat 15–24% as the early-warning band here):** Surface the conditions. With a person present, ask: accept and proceed, or revise? Without one (autonomous mode — VA-153 branch 4): accept with conditions and record the decision in the gate verdict block, or revise once and record the loop-back; never stall and never choose silently. Either way the conditions are recorded as critical assumptions.
- **FAIL (<25%, early-warning <15%):** Return to Section 2 (Use Block diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Adoption Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)


---

## ⛔ THE CLOSE IS THREE CHECKS, NOT ONE (VA-89, extended by VA-91)

*(VA-89 added 4 September 2026, on the principal's finding that a challenge could return PASS with one of the method's own checks failed. Extended the same day, on his second observation: the close has always been three checks — logical, operational, financial — and only the third carried verdict authority. Applied under his explicit delegation, which is the only authority under which the WS1 autonomy boundary permits an edit to this section. Logged against that boundary.)*

**The margin of safety computed above is one of three limbs. It is not the gate.**

The model stack builds three things — CTM → AOM → ARM → Fin-Sim → FMOS — and each of them can fail on its own terms.

| Limb | Model layer | The question it answers | It fails when |
|---|---|---|---|
| **Logical** | CTM, and the BALM answer behind it | Does the design's own logic hold? | A named check of the method failed and nothing has disposed of it |
| **Operational** | AOM | Can the operating model carry this design at the scale claimed? | The work does not fit the capacity, the roles, or the unit |
| **Financial** | ARM → Fin-Sim → FMOS | Do the economics clear, on the gate that actually binds? | The margin of safety fails, or the venture's own binding gate fails |

Compute all three before stating any verdict. A challenge that clears one limb while another has failed has not solved its requirement.

### Step 1 — logical limb: list every named check this challenge ran, with its result

At minimum, and **each one reports a result — a check not listed is a check not run**:

| Check | Rule |
|---|---|
| property-holder test | VA-71 |
| credibility mechanism — instrument and supplier tests | VA-81 |
| pointing test | — |
| coverage of the elimination conditions | — |
| limit of the analogue in the synthesis check | — |
| completeness contract | VA-73 |
| **no forward references** — nothing named that the architecture has not yet introduced | **VA-80** |
| **binding gate found by driving every gate**, not from one formula | **VA-84** |
| **shared-input declaration** — any slot closed against a parallel run is declared OPEN | **VA-85** |
| **incremental write** — the output file existed before the sources were read | **VA-88** |
| **existence test before enumeration**, with the affordability screen stated first | **VA-92** |
| **independence of the two financial halves** shown before both are reported | **VA-97** |
| **independent verification artefact** exists for this requirement | **VA-90** |
| **no launch constraint inside any sub-requirement or the verdict** — no-cash, founder hours, cold outreach, pilot volume, phase appear only in the carried-items row | **VA-23** |
| **loop-gate branch stated for every FAIL** — owner of the lever (this / adjacent / non-adjacent requirement), re-derived-input cap, autonomous warning-band choice, each with its record | **VA-153** |
| **fixed-cost spread count stated once**, with the reason it is the at-scale count, and the margin printed at the PCO's alternative counts | **VA-162** |

*(Rows without a rule number are the method's own long-standing checks. The seven in bold were added 6 September after an enforcement audit found them stated in prose and enforced nowhere — a rule that produces no friction when broken is never noticed as broken.)*

### Step 2 — operational limb: check the AOM against the design it has to carry

Four checks. Each returns PASS or FAIL, and a FAIL is disposed of at Step 4 like any other.

1. **Capacity.** Take the work this challenge's activities drive, at the volume the design claims, against the hours the operating model has. **State the capacity figure once and derive everything from it.** Where a capacity figure appears in prose and again inside a calculation, the two must be the same number. A headline figure that contradicts the arithmetic beneath it is a FAIL, not a rounding note. `[evidence: VA-91]`
2. **Role support.** Every activity has a role that performs it and, where it needs supervision or quality control, a role that supports it. An activity with no supporting role is a FAIL.
3. **Unit sizing.** The local operating unit is large enough to cover its own fixed costs and small enough to replicate in weeks. Either answer NO is a FAIL.
4. **Component carriage.** Every transition this challenge adds to the CTM is carried by a product component, or is flagged with the reason. The generators refuse to write an incoherent model; this check covers what they cannot see, which is a transition carried by a component that no role in the AOM staffs.

**5. Role review (process flow v6 step 6b, 15 September 2026).** For every operating-model component this challenge added or changed, the role named in its `dri:` field reviews the activities under its seat against that role's craft standard (Head of Sales → `launch-sales-standard.md`; Head of Marketing → `landing-page-standard.md`, `sales-marketing-asset-standard.md`; a role with no standard reviews from general practice and records "standard missing"). One question: can this role run this activity at the cost and volume the fin-sim assumes, and what does it need that the plan does not give it? The reviewer rewards a departure from how the function is conventionally done and fails only what the role cannot execute as specified. Output is findings, disposed at Step 4 — never rewrites. A run that records no role review for a component with a `dri:` fails this check (R-V2).

**Executable checks on this limb (sealed toolchain, 16 September 2026).** From the vault root, run and paste the result lines:

```
python3 .claude/skills/shared/generators/check_model_coverage.py <ctm.yaml> <aom.yaml>
python3 .claude/skills/shared/generators/check_requirement_trace.py <aom.yaml>
```

A `REFUSED` result is a FAIL on this limb, disposed at Step 4. A check that cannot run because a model file is missing is a FAIL on the model, not a pass.

### Step 3 — financial limb: the margin of safety AND the gate that binds

The FMOS calculation above is the first half of this limb. The second half is required:

```
BINDING GATE — [name it, with the challenge that identified it]
  measure:      [the constraint — e.g. annual run-rate capacity, working capital peak]
  threshold:    [the value at which it fails]
  this design:  [the value] — [surplus / breach, as a percentage]
```

A venture's binding gate is rarely the FMOS. Name it at the challenge that first identifies it, and print it at every challenge after that one. **Where the binding gate fails, the financial limb fails, whatever the margin of safety says.** **A verdict block that prints only the margin of safety teaches the reader to watch the wrong number.** `[evidence: VA-91]`

**How to find the binding gate — drive the model across every gate, do not compute one threshold and name it (VA-84).** A gate found from a single formula is a guess about which constraint binds. Build the check cell, run the model against every gate it has, and report the one that fails first with the margin to it. **Where that margin is a small fraction of the assumed value, the margin is the finding and is reported unsoftened.** **Separate cause from consequence before reporting (added 4 September 2026).** Where two gates fail at the same smallest departure, test whether one is a consequence of the other; report the cause as the binding gate and the consequence beneath it. Otherwise one constraint is reported several times and reads as several problems. `[evidence: VA-84]`

Where no binding gate has been identified yet, say so, and say what would identify one. Do not leave the line blank.

**Show the two halves are independent before reporting both (VA-97, added 4 September 2026).** The margin of safety and the binding gate are only two checks if they measure different things. **Where one is an algebraic transform of the other, say so, report them as one check, and state what an independent second check would have to measure.** Test it: express both from the same inputs and see whether one reduces to the other. (Found in use: on one venture the margin of safety equalled the binding-gate ratio minus one, identically, at six data points across three records — they looked independent only because the two were computed at different points of the same assumption band. The 25 per cent margin band was, in effect, a test that the venture reached 62.5 per cent of its own objective, and it could not fail while the gate passed. **That limb had never had a passing independent check.**) A limb that prints two numbers which are one number under a transform is the single-number failure this whole rule was written to stop, wearing the fix's clothes.

**The margin of safety may not be computable, and that does not stop the limb (added 4 September 2026).** Where there is no price ceiling to compute it against — no PCO, no measured willingness to pay — **state that the FMOS is not computable and why, and close the financial limb on the binding gate alone.** Do not return "provisional, pending data": an FMOS-only reading of a venture with no ceiling returns a non-answer, while its binding gate may be failing outright. (Regression run, 4 September 2026: the FMOS was not computable at any of C1, C2 or C3, and the zero-spend gate was breached at the first pound.)

**Executable check on this limb (sealed toolchain, 16 September 2026).** The margin of safety is computed by the script, never by hand:

```
python3 .claude/skills/shared/generators/fit_margin.py <venture>-fit-model-at-C[N]-<band>.yaml
```

Paste its verdict lines. A ceiling or floor below tier 1 must be a band, not a point; a bar that reads its own ceiling is refused; both refusals are FAILs on this limb.

### Step 4 — dispose of every check that did not pass, on any limb

Three dispositions, and only three.

| Disposition | What it means | Effect |
|---|---|---|
| **Design defect** | The design could have been different and was not. The check failed on something inside the designer's control. | **FAIL.** Return to Diagnose. Name which lever is off. |
| **Standing constraint** | The check failed on a condition the principal set before the run and recorded in the PCO or a dated instruction — a regulatory perimeter, a market or a jurisdiction the principal excluded, a counterparty the principal barred. Not a design decision. **Launch constraints — no capital, one person, no spend, no cold outreach, a pilot's volume — are not standing constraints at C1–C10 (VA-23, RD-033): a check that fails on one was run on a launch instance, not on the architecture. Re-run it at scale; the launch form goes to the pilot-instance record after R10.** | Caps the verdict at **PROVISIONAL**. State the consequence, and the condition under which the constraint lifts. |
| **Build item** | The capability does not exist yet, and the design does not claim it does. | Caps at **PROVISIONAL**. Needs an owner, a convergence event, and the threshold at which the design must be re-run. |

| **Structural limit** | The check failed on something no design in this class could remove. Not a property of *this* design. | Caps at **PROVISIONAL**. The residual must be **named**, **bounded**, and paired with **the validation that addresses it**. |

**The test that stops "structural limit" becoming the new "consciously accepted with conditions" (VA-101, added 4 September 2026, renumbered 6 September — VA-96 was already claimed by a principal ruling the same day):** *could any competitor, with any budget, remove it?* **If yes, it is not structural — it is a design defect.** A structural limit must be true of **every venture in the class**, not merely of this one. It must state how much of the venture's value rests on it. And it must name the validation that addresses it, because the un-printable residue **is** the validation target — a structural limit with no validation named is an excuse, not a disposition.

*(Why this exists: the regression run of 4 September 2026 found that VA-89's original three dispositions could not hold the R1 residual — a counterparty's free decision to transact cannot be derived. That is not a design defect, since no design removes it; not a standing constraint, since the principal did not set it; and not a build item, since no capability closes it. Under "a check you cannot classify is a design defect", **every derivation-based venture would fail at C1 for a reason true of all ventures.** The rule was made that morning and misfired the same day.)*

> ⚠ **"Caps at PROVISIONAL" is a ceiling, not a floor (clarified 4 September 2026).** It means the verdict **may not be better than** PROVISIONAL. It does **not** mean the verdict reaches PROVISIONAL. **Step 5 still governs**: if any limb fails, the verdict is FAIL, whatever disposition the failed check carried. A disposition explains *why* a check failed; it never makes the check pass. (Found in use: a run hit a breached binding gate — so the financial limb failed — while the check's disposition was a build item, and Step 4 read as though PROVISIONAL were available. The run ruled Step 5 governs and was right.)

**A check that cannot be classified fails.** If the run cannot place a failed check in one of the three, the disposition is design defect. A standing constraint must be traceable to the PCO or to a recorded instruction from the principal. A constraint invented at the gate to explain a failure is a design defect, and calling it a constraint is the failure mode this rule exists to stop.

### Step 5 — state the verdict as a conjunction of the three limbs

```
GATE VERDICT — on the cumulative architecture C1 to C[N]
  logical limb:      [PASS / PROVISIONAL / FAIL]    checks failed: [n]
  operational limb:  [PASS / PROVISIONAL / FAIL]    checks failed: [n]
  financial limb:    [PASS / BORDERLINE / FAIL]     FMOS [X]% · binding gate [name]: [surplus / breach]
  dispositions:      [every failed check, with its kind]
  capacity figure:   [the single figure, and confirmation prose and arithmetic use the same one]   VA-91
  independence:      [shown / NOT shown — are the two financial halves one measure?]              VA-97
  gates driven:      [n gates tested; first to fail: [name], margin [x]]                           VA-84
  verification:      [artefact filename, or NONE — a requirement without one closes PROVISIONAL at most]  VA-90
  inherited:         [worst verdict of any prior challenge this builds on, and which]
  repairs:           [any upstream failed check this closes — name it, show the arithmetic — or "none"]
  loop_backs:        [n this requirement; at 3 — pivot / mutation, stated, with the FIT line that decides]   VA-151
  loop-gate branch:  [for every FAIL — this / adjacent / non-adjacent owner · re-derived cap · autonomous choice, with record]   VA-153
  launch constraints:[none inside SR1–SRn and this block — or the offending line, which fails the logical limb]   VA-23
  spread count:      [the one count used for any fixed-cost spread, why it is the at-scale count; margin at the PCO's other counts]   VA-162
  shared input:      [none — or the input that drives both the margin and the binding gate; then independence reads NOT shown]   VA-160
  VERDICT:           [PASS / PROVISIONAL / FAIL]  — may not exceed `inherited` unless a repair is shown
```

- **PASS** — all three limbs pass, with no failed check outstanding.
- **PROVISIONAL** — no limb fails, and every failed check is a standing constraint or a build item, each fully specified. The challenge may route to the next requirement. **The architecture may not be called design-complete, and no later requirement may rely on a capability recorded as a build item.**
- **FAIL** — any limb fails.

### Step 5a — the verdict composes forward: you cannot fail one requirement and pass the next (VA-95)

*(Added 4 September 2026, on the principal's finding. VA-89 and VA-91 defined the verdict for a single challenge and said nothing about how verdicts compose. In a cumulative method that omission makes the verdict meaningless: the first independent verification run under those rules returned FAIL on one requirement and PROVISIONAL on the requirement built directly on top of it, and nothing in the method objected.)*

**The business form factor accumulates. C5 contains C4.** A requirement's verdict is therefore **a statement about the cumulative architecture at that point**, not about the requirement's own contribution in isolation. Four requirements verified as four independent objects is a category error.

Four clauses.

1. **A verdict is read on the cumulative state.** State which challenges the verdict covers — C1 to C[N], not R[N] alone.
2. **No requirement carries a verdict better than the worst verdict of any requirement it builds on.** A FAIL at C4 makes C5, C6 and C7 FAIL, unless clause 3 applies.
3. **A downstream requirement may repair an upstream failure.** Where it does it must: name the requirement it repairs and **the specific failed check it closes**; show the arithmetic on the cumulative state; and carry the verdict of the repaired state. **The upstream verdict is annotated, never overwritten** — forward-only (VA-52) preserves what was recorded at the time.
4. **Clause 3 is not an escape route.** A downstream requirement that makes an upstream failure *less visible* has not repaired it. **The test: would the failed check still fail if run against the cumulative state at the downstream point?** If yes, it is not repaired, and clause 2 governs. A repair that cannot be shown in arithmetic is not a repair.

**Only the verdict on the final cumulative state governs a function gate.** A function gate reads the cumulative verdict at its last challenge — not the average of its requirements, and not the verdict of the last requirement taken alone.

**Executable check on composition (sealed toolchain, 16 September 2026).** Before stating the cumulative verdict, run:

```
python3 .claude/skills/shared/generators/check_verdict_order.py <verdict file or run record>
```

A `REFUSED` result means a verdict exceeds the worst verdict it rests on; the cumulative verdict is then the script's, not the prose's. The regression walk of 16 September found eight such lifts in one run — the script exists because reading did not catch them.

### Step 6 — classify every item carried out of the challenge (VA-82)

Three kinds, and only two are legitimate.

| Kind | What it is | Requires | Legitimate |
|---|---|---|---|
| **Forward-referenced** | A later challenge owns the question. | The owning requirement, by number, and nothing about how it is solved (VA-80). | Yes |
| **Unmeasured input** | The design is complete and rests on a figure, a capability or a decision nobody holds yet. | An owner · a convergence event · a falsifiable pivot trigger stated with it. | Yes, and only with the trigger |
| **Unowned design defect** | No later challenge owns it, and continuing will not answer it. | A named closing mechanism, before the function gate opens. | **No.** It blocks. |

An open-items table without kinds lets a failing architecture read as complete. The audit of 2 to 4 September 2026 found ten requirements in a row returned borderline-to-fail and each was recorded as "consciously accepted with conditions"; the same undifferentiated table then appeared in the next venture's own record.

### Step 7 — the challenge does not close until an independent verification artefact exists (VA-90)

The gate above is computed by the run that produced the answer, so it cannot be the only check on it. Run `/ive-fit-verifier-custom` on this requirement and save the artefact to the venture folder. Where the failed check is the role-support check, the closing mechanism VA-87 names is structural separation: a second pass that re-derives from the inputs without reading the first pass's working and reports where it disagrees. State its limit as well — two runs of the same kind of machine over the same material share blind spots, so a published standard sits beside it, not after it. After F1 (R1 to R3), and again after R10, run `/ive-consistency-audit-custom` and `/verify-venture-custom`. **A requirement whose verification artefact does not exist is closed provisionally at most**, whatever this section returned.

**Forward-only (VA-52).** This rule applies to runs from 4 September 2026. It does not reopen a closed gate on any venture. Where a venture has closed challenges but has not yet opened its next requirement, the verification runs before that next requirement opens — that is not reopening a gate, it is running the check that should have preceded it.


### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines)
- Current FMOS and verdict
- Mark **R5 complete** (or fail) on the status board
- Route to **R6** (Circumvent the Cash Flow Constraint)

### WS1 Feedback Capture *(mandatory — the mode depends on who is in the conversation)*

**Two modes. Decide which applies before routing.**

**Autonomous run — nobody is in the conversation.** This covers any run under the principal's "act without me" delegation, any dispatched background run, and any run inside a workflow. **Write the capture. Do not ask.** Answer the four questions from the run you have just completed and append them to `04-Projects/TMTH_Venture_Studio/Forge/WS1/ws1-feedback-log.md`. This is part of closing the challenge. A challenge closed without it is not closed.

**Interactive run — a person is in the conversation.** Ask first:

> "Quick WS1 capture? (y / skip)"

If **y**, ask the four questions in sequence and append the answers. If **skip**, route immediately — no friction.

**The format is the same in both modes:**

```
---
## R[N] · [venture name] · [date]

**1. Genuine mutations?** Did this challenge produce ≥2 genuine BFF mutations, or did it justify the existing design?

**2. Criteria signal:** Which registry criterion was most useful? Which should have fired but didn't?

**3. Correction needed?** Did the output require significant human correction? [yes/no — if yes, what]

**4. One change:** What would improve this challenge skill?
```

**Why the autonomous mode is mandatory (added 4 September 2026).** The WS1 objective is defined on autonomous runs. Under the previous wording the step waited for a y/skip answer that nobody could give, so it dropped with no trace. Four runs across two ventures on 2 and 3 September produced no capture at all, and the entries had to be written from the records two days later. The runs that produce the primary data were the runs producing none.


---

## ⛔ VDR completeness contract (added 28 Aug 2026, Tom's ruling — logged VA-73)

The VDR section this challenge produces must contain **every sub-requirement of this skill, labelled SR by SR**, each either completed in full or explicitly marked **OPEN with an owner**. The reference standard for the field set is this skill's own sub-requirement list, in the order this file states it. `[evidence: VA-73]`

**A compressed section is not a completed challenge.** Diagnosis-plus-strategy prose that "covers the ground implicitly" fails this contract, whatever its quality: the sub-requirements are the method's decomposition, and an output that does not show them cannot be checked against them. The logged failure (28 Aug 2026): a full C4–C10 run delivered one diagnosis, one theory citation, one mutation gate and one strategy per challenge — and skipped every named sub-requirement in between. It read complete and was not.

**Rule:** sub-requirements not specified = the challenge is not done. Run `/verify-balm-custom` before declaring any multi-challenge run complete — completeness per sub-requirement is exactly what it checks.
