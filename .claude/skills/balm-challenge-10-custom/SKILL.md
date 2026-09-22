---
name: balm-challenge-10-custom
description: IVE R10 — Manufacture Replaceability of the Key Supplier Input. Maps the interim value chain, identifies the supplier input with highest cost and volume, and designs a Leverage Strategy that makes that input replaceable so suppliers cannot extract value.
---

# BALM R10 — Manufacture Replaceability of the Key Supplier Input

**Purpose:** Manufacture a state of replaceability for the supplier input or service with the highest cost or volume. C10 makes the key supplier input replaceable so suppliers cannot extract value. This is a defensive positioning move — it does not build a competitive moat against market entrants (that is R9); it removes the leverage that suppliers and partners hold over the venture's cost structure.

**When to run:** After R9 (Manufacture a Resource Moat) is resolved. R10 is the final requirement of Function 3 and the capstone of the full IVE architecture. After R10, run `/ive-consistency-audit-custom` immediately.

**Output:** Interim Value Chain, Key Input, Leverage Strategy, and Leverage Theory of Change. Together these constitute the R10 component of the new Business Form Factor.

**Handoff to:** `/ive-consistency-audit-custom` — mandatory after R10 to check cross-requirement dependencies before finalising the architecture.

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

**→ This skill: R10 — Manufacture Replaceability of the Key Supplier Input** (F3, final requirement; requires R9 and all prior requirements)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. A supplier dependency that is manageable at 500 customers may become existential at 500,000. R10 is designed for the at-scale state.

---

## R10 definition

> Manufacture a state of replaceability for the supplier input or service with the highest cost or volume.

C10 makes the key supplier input replaceable so suppliers cannot extract value.

**R10 vs R9 distinction:** R9 is about making a resource scarce for competitors — building a moat. R10 is about making a supplier input replaceable for the venture — removing leverage. These are opposite moves in opposite directions. Confusing them produces a venture that is designed to defend the wrong frontier.

---

## This skill IS a design loop

Running R10 is not a three-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.** R10 is the final F3 challenge and the capstone; it still runs the Simulate gate. The cost floor updates with the leverage/replaceability activities R10 adds across all streams, so the gate is live — do not skip it because "it's a supplier challenge."

The four steps map onto this skill's existing structure (note the F3 ordering — input → strategy → theory):
- **Diagnose** — SR1 Interim Value Chain / Key Input (isolating the highest-cost/volume supplier dependency).
- **VA-23 at Diagnose (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30) — the bottleneck is the at-scale one.** A launch constraint — no cash, the founder's hours, no cold outreach, a pilot's volume, a phase — is not a bottleneck and does not enter Diagnose, Theorize, Productize or Simulate at any of C1–C10. Test every candidate block: can the workaround be described without a phase, a pilot, a joint venture or a bootstrap? If not, it is a launch-instance item; write it in the carried-items row "carried to pilot-instance design after R10" and nowhere else. Tom's correction, 17 Sep 2026; RD-033.
- **Theorize** — the Leverage Theory of Change (SR3); named mechanism, prescriptive not descriptive.
- **Productize** — the Leverage Strategy (SR2) + replaceability designed into the architecture + the CTM/AOM update (the design decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure. `[evidence: VA-FID1]`

### Simulate — the gate with teeth (mandatory; do not skip on illustrative data)

A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R10 has not been designed, only described.

1. **Use the correct FMOS formula — cost denominator.**
   `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7).
   Do **not** use `(Price − Cost) / Price` (gross-margin / price denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling; Cost_high = the AOM high-point unit cost.
   **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on? `[evidence: CS-7]`
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* A sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

### Loop-back and the pivot discipline

- **FAIL or BORDERLINE → return to Diagnose** (not to a tweak). Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why R10 will not clear and what decision is needed.
- **Loop counter and the third loop (VA-151, RD-036) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).** Print `loop_backs: n` in the gate verdict block. At the third loop-back the run states whether the next turn is a **pivot** (the theorem or the strategy changes) or a **mutation** (same theorem, a different form), and names the FIT line that decides it. A third loop that names neither is the `FLAG FOR TOM` above.
- **Four loop-gate branches (VA-153, RD-037) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).**
  1. *Later owner, adjacent:* a FAIL whose lever the next requirement owns routes forward with the FAIL inherited and the owner named in the verdict block.
  2. *Later owner, non-adjacent:* routes in sequence, the FAIL inherited through every requirement between, with a VA-85 lock on the owner; no requirement between may claim the repair.
  3. *Repair on a re-derived upstream figure:* the repair is claimed, the re-derived figure is named as the critical assumption, the verdict caps at PROVISIONAL, and the upstream requirement's row is annotated, not overwritten.
  4. *Warning band with no person present (autonomous mode):* accept with conditions and record the decision, or revise once and record the loop-back. Never stall; never choose silently. The choice and its reason go in the verdict block.
- **Close criterion.** Mark R10 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## Running this skill — step-through protocol

When this skill is invoked, open by showing the user the full R10 checklist, then work through each sub-requirement one at a time. Do not present all sub-requirements simultaneously. Present one, wait for the answer, confirm it, then move to the next.

**Opening checklist — show this first:**

```
R10 — MANUFACTURE REPLACEABILITY OF THE KEY SUPPLIER INPUT
Sub-requirements to work through:

☐ 1. Interim Value Chain / Key Input
☐ 2. Leverage Theory of Change
☐ 3. Leverage Strategy
☐ 4. BFF (C1–C10)

Let's start with sub-requirement 1.
```

Then proceed sub-requirement by sub-requirement as follows.

---

## Sub-requirement 1 — Interim Value Chain / Key Input

**Name:** Interim Value Chain / Key Input

**Definition:** *The series of activities, suppliers, partners, and inputs involved in sourcing, manufacturing, marketing, selling, and delivering a product or service to a customer / The supplier or partner input that has the highest cost and volume.*

This has two parts:

**(a) Interim Value Chain:** map the full chain of activities, suppliers, partners, and inputs that deliver the product or service to the customer. This does not need to be exhaustive — focus on the supply-side dependencies. The goal is to make visible what the venture depends on that it does not control.

**(b) Key Input:** from that value chain, identify the single input or supplier relationship with the highest cost and/or highest volume. This is the one that creates the most leverage risk — the supplier that, if they chose to exercise power, would cause the most damage to the venture's economics or continuity.

**Diagnostic questions:**
- Who supplies the venture with inputs it cannot easily source elsewhere?
- Which input, if priced up by 30%, would most damage the unit economics?
- Which supplier, if they withdrew, would take the longest to replace operationally?
- As the venture scales, which supplier dependency becomes more concentrated rather than less?
- Are any of the gateway partners from R7 now supply-side dependencies rather than distribution enablers?

**Ask the user:** "Map the key activities, suppliers, and inputs in your value chain — then identify the single input or supplier relationship with the highest cost or volume that creates the most leverage risk."

Wait for the answer. Confirm it. Mark sub-requirement 1 complete. Then move to sub-requirement 2.

---

## Sub-requirement 2 — Leverage Theory of Change

**Name:** Leverage Theory of Change

**Definition:** *The nature of the supplier's or partner's power over the Key Input, and the theory/ies most effective in explaining how to offset and create a position of leverage over that power.*

The Theory of Change grounds and justifies the Leverage Strategy — it precedes the Strategy. The F3 order is: identify the input → explain the nature of the supplier's power and the theory that governs it → name the strategy that fires the theory → state the evolved BFF.

Point the user to `/theory-of-change-custom` and tell it: "R10 Leverage." It will produce the named Leverage Theory of Change using CMO structure in BALM-ready format.

**Ask the user:** "What is the nature of the supplier's power over the Key Input — and what theory explains why your Leverage Strategy will work to offset it? Run `/theory-of-change-custom` and tell it 'R10 Leverage' to get this in BALM format."

Wait for the answer. Confirm it. Mark sub-requirement 2 complete. Then move to sub-requirement 3.

---

## Sub-requirement 3 — Leverage Strategy

**Name:** Leverage Strategy

**Definition:** *The best way to operationalize the Leverage Theory of Change for offsetting the supplier's or partner's power over the Key Input.*

⚠ **MANDATORY — before writing the Leverage Strategy, complete these three steps in order:**

**Step 3a — Baseline honestly.** State where the current BFF stands on supplier replaceability / leverage. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 3b — Generate ≥2 candidate BFF mutations.** Structural changes (not procurement tactics) that could manufacture more genuine replaceability than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 3c until two real mutations exist on the table.

**Step 3c — Evaluate and decide.** For each candidate: does it manufacture genuine replaceability (venture can credibly switch without disruption) or just reduce dependency? What does it cost in coherence with R1–R9? Does it close the loop back to R1's Critical Limiting Operation? Record the decision. Adopt a mutation (restate the evolved architecture) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Leverage Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R10
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

If `justificationModeFlag: true` — stop. Do not write the strategy. Return to Step 3a and genuinely attempt mutations.

Only after the contract block is emitted, write the Leverage Strategy.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

The Leverage Strategy must manufacture replaceability — not just reduce dependency. The venture must be able to credibly threaten to switch suppliers without operational disruption. A strategy that merely diversifies sources without creating genuine replaceability is not a Leverage Strategy — it is portfolio management.

Three approaches, in ascending order of architectural quality:

**1. Substitute development**
Build or cultivate an alternative input source that makes the key input non-scarce for the venture's purposes. The original supplier retains their resource; the venture now has an alternative and can switch credibly. The substitute does not need to be owned by the venture — it needs to exist and be accessible at comparable quality and cost.

**2. Exclusivity capture**
Secure exclusive access to the input before the supplier understands their leverage position — or before a competitor does. This is time-sensitive. The goal is to convert a potential adversary into a locked-in partner before they recognise the asymmetry in their favour. Most effective when the input is currently undervalued or when the supplier is not yet aware of the venture's dependence on them.

**3. Structural bypass**
Redesign the architecture so the high-cost, high-volume input is no longer required — or so it can be produced internally at comparable quality and cost. The highest-quality R10 solution. It is harder to arrive at but produces the cleanest result: a supplier who holds leverage over an input the venture no longer needs has no leverage at all.

**Ask the user:** "What is your Leverage Strategy — how will you manufacture replaceability for the Key Input? Which approach fits best: substitute development, exclusivity capture, or structural bypass?"

Wait for the answer. Confirm it. Mark sub-requirement 3 complete. Then move to sub-requirement 4.

---

## Sub-requirement 4 — BFF (C1–C10)

**Name:** Business Form Factor (C1–C10)

**Definition:** *The evolved or confirmed Business Form Factor incorporating all solutions from C1 through C10 — the complete new Core Business Architecture the venture proposes.*

This is the capstone BFF. It is not a list of ten challenge solutions. It is the single integrated statement of what the venture structurally *is* — how it is made, delivered, paid for, and defended — as a consequence of all ten architectural decisions.

**The evolution test (mandatory):** Does the Leverage Strategy change what the venture structurally is — how it organises its supply side, who its primary customer is, what form its product takes? Or does it protect the existing form without changing it? Both are valid outcomes, but the test cannot be skipped. "Hold" is only legitimate if mutations were genuinely generated and rejected with explicit reasons recorded in the VA-4 section.

**The spine test:** Remove all challenge labels and read the BFF cold. Does it describe one coherent product architecture? Or a checklist? A properly constructed BFF reads as a description of one business — the challenge labels appear as parenthetical citations, not as the structural joints holding the sentence together.

**The synthesis test (VA-1):** Does this now look like a real business? Name the real-world analogue — "this now looks like [business] because [mechanism]." If no clean analogue exists, flag it — the parts have not cohered into one architecture.

Ask: "Here is the final BFF (C1–C10) — [state it, evolved or held]. Does this read as one coherent business? Is there a real-world analogue that confirms the architecture has cohered?"

Wait for confirmation. Then proceed to the handoff.

⛔ **MANDATORY HANDOFF — BFF C1–C10 CONFIRMED. DO NOT EDIT THE VDR. DO NOT ROUTE TO CONSISTENCY AUDIT.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "BFF C1–C10 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## Productizing R10 — Strategy → architecture

The Leverage Strategy names how the venture manufactures replaceability for the Key Input. Productizing it means ensuring replaceability is a structural property of the architecture — the venture can credibly switch suppliers without operational disruption — not a procurement posture.

**Target product component:** All products (supply chain — input independence)

Work through these two questions before finalising the Leverage Strategy:

**1. Genuine replaceability vs reduced dependency.** Does the Leverage Strategy produce a situation where the venture can switch suppliers without operational disruption — because the architecture is designed around substitutable inputs — or does it merely reduce dependency through diversification or dual-sourcing? Reduced dependency is procurement management. Genuine replaceability requires the architecture to be designed around the substitutability from the outset. Ask: if the primary supplier raised prices by 40% tomorrow, what would the venture do — and would doing it require operational disruption?

**2. R1 continuity.** The Critical Limiting Operation from R1 often depends on a specific input. If R1's Workaround Strategy required a novel input source or capability, that source is likely the Key Input R10 must address. The strongest R10 solutions close the loop back to R1 — the architecture that solved the cost floor at R1 is also the architecture that protects the venture from supplier leverage at R10.

**3. BFF evolution — mandatory test at C10.** R10 is the capstone requirement. After the Leverage Strategy is confirmed, the BFF must be tested for evolution: does the replaceability strategy change what the venture structurally *is* — how it organises its supply side, who its primary customer is, what form its product takes — or does it protect the existing form? Both are valid outcomes, but the test is mandatory. "Hold" is only a legitimate answer if mutations were genuinely generated and rejected with explicit reasons. A hold that skips mutation generation is the justification-mode failure pattern (VA-3).

**The question to ask:** "Does the structural move this Leverage Strategy makes — owning the interface, bypassing the input, or locking in the alternative — produce a form factor the venture didn't have before? If so, state the evolved BFF. If not, show the mutations that were considered and explain why each was rejected."

C10 often *does* evolve the BFF, because a genuinely structural bypass or interface ownership move changes what the venture sells, to whom, and on what terms — which is form-factor territory. A replaceability strategy that leaves the BFF entirely unchanged should be examined for whether it is truly structural or merely procurement posture.

**At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A supplier dependency that is manageable at 500 customers may become existential at 500,000. Name the at-scale volume explicitly. If the replaceability mechanism breaks before reaching it, return to Diagnose.

After the productizing questions are confirmed, state the BFF (evolved or held with explicit reasoning) and move to Sub-requirement 4 for formal confirmation.

---

## R10 output format

```
SUMMARY
  Leverage Strategy: [strategy in one sentence — the architectural direction]
  Input made replaceable: [key input + approach: substitute / exclusivity / structural bypass]
  Grounded in: [named theory — nature of the supplier's power]

R10 — SUPPLIER REPLACEABILITY (LEVERAGE)
---
INTERIM VALUE CHAIN / KEY INPUT
  Value chain (summarised): [activities → suppliers → inputs → delivery]
  Key input: [the supplier input with highest cost/volume]
  Leverage risk: [how the supplier could exercise leverage — specific and concrete]

LEVERAGE THEORY OF CHANGE
  Nature of the supplier's power: [...]
  Theory: [citation]
  Context: [...]
  Outcome: [...]

LEVERAGE STRATEGY
  Approach: [Substitute development / Exclusivity capture / Structural bypass]
  [answer]
  Replaceability mechanism: [how this creates a credible alternative]

CONSIDERED / NOT CHOSEN (VA-4 — show your working)
  Baseline on this dimension: [honest current position of the BFF]
  Candidate mutations / options:
    A. [structural change or option] → [why it could do better] → [adopted / rejected because…]
    B. [structural change or option] → [why it could do better] → [adopted / rejected because…]
  Decision: [adopted mutation X / held current BFF; alternatives rejected for reasons above]

BFF (C1–C10) — mandatory evolution test
  Does the Leverage Strategy change what the venture structurally is? [Yes / No]
  If yes — evolved BFF: [restated BFF in one sentence — the new form factor]
  If no — held BFF: [restate the unchanged BFF + list the mutations generated and why each was rejected]
  Note: "hold" without listed rejected mutations is the justification-mode failure. Show the working.

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
  Does the strategy manufacture replaceability (not just reduce risk)? [Yes / No]
  Could an incumbent do this without a new BFF? [Yes — rethink / No — good]
  Did the BFF evolution test run genuinely? [Yes — mutations listed / No — flag]
  Confidence: [High / Medium / Low]

→ All 10 requirements complete. Run /ive-consistency-audit-custom before finalising the architecture.
```

---

## Common failure patterns

| Failure pattern | Why it fails | What to do instead |
|-----------------|-------------|-------------------|
| Confusing R10 with R9 | R10 is about making a supplier input replaceable for the venture. R9 is about making a resource scarce for competitors. Designing a competitive moat as the answer to R10 solves the wrong problem. | R10: what can the venture replace if a supplier turns adversarial? R9: what can competitors not get? |
| Supplier diversification as R10 | Having two suppliers instead of one reduces risk but does not manufacture replaceability. If neither supplier knows the venture can switch, the leverage dynamic is unchanged. | Design the strategy so the venture can credibly and operationally switch without disruption — not just theoretically. |
| Contractual protection as R10 | Long-term supply contracts reduce leverage risk but do not eliminate it. Contracts can be breached, renegotiated under duress, or simply not renewed. | The Leverage Strategy must change the structural relationship — the supplier must face a credible alternative, not just a legal constraint. |
| Leverage map too narrow | Mapping only current suppliers misses partners from R7 who have become supply-side dependencies — and future intermediaries who may emerge as the venture scales. | Map leverage at scale, not at launch. Ask: who will matter at 50,000 customers who does not matter today? |
| Theory of Change stated before Strategy | In F3 challenges, Theory of Change grounds and explains the Strategy — it does not precede it. | Follow the F3 order: input → strategy → theory. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

**Sequence:**
- **R9** (prerequisite) → manufactures a resource moat against competitors; without a resolved R9, the competitive position may be undermined even if supplier leverage is neutralised
- **R10** → manufactures replaceability of the key supplier input; the final architectural move before the consistency audit
- **After R10 → `/ive-consistency-audit-custom`** — mandatory; checks that all ten requirements are internally coherent and do not contradict each other

**R10 and R1:** The Critical Limiting Operation from R1 often depends on a specific input. If R1's Workaround Strategy required a novel input source, that source may now be the Key Input that R10 must address. Strong architectures produce a natural handoff from R1 to R10 — the cost structure and the leverage structure are designed together.

**R10 and R7:** Gateway partners activated in R7 are the most common source of R10 leverage. The same characteristic that made them essential for customer normalisation (they control access to a hard-to-reach customer segment) makes them dangerous if they re-price or withdraw. R10 must explicitly assess every R7 partner for supplier leverage risk.

**Cross-requirement elegance.** The strongest R10 solutions also touch other requirements. A Leverage Strategy that makes an input replaceable may simultaneously reduce a scaling cost (R3), remove a bottleneck that was embedded in R1's cost structure, or free the venture from a dependency that was constraining R9's resource moat. Ask at each design iteration: does this architectural move also advance any other requirement?

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles the replaceability of the key supplier input so suppliers cannot extract value. It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on the replaceability of the key supplier input so suppliers cannot extract value? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on the replaceability of the key supplier input so suppliers cannot extract value than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on the replaceability of the key supplier input so suppliers cannot extract value vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
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

### 6 — Propose, don't evaluate-request

When reviewing previously confirmed content against new context (a correction, an architectural update, a new analogy), the default is: assess the content, state whether it holds or needs changing and why, then ask for approval on that assessment. Never ask the user "does anything need adjusting?" or "does this still hold?" — that transfers the diagnostic burden to the investor. The skill does the diagnosis. The user approves or corrects.

Pattern: **assess → propose → get approval.** Not: present → ask if anything needs adjusting.

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
- Edit `.claude/skills/balm-challenge-10-custom/SKILL.md` to modify
- **Predecessor:** `/balm-challenge-9-custom` (R9 — Manufacture a Resource Moat)
- **Successor:** `/ive-consistency-audit-custom` (mandatory after R10 — all 10 requirements complete)
- **Related skills:** `/theory-of-change-custom` (invoke as "R10 Leverage"), `/ive-fit-verifier-custom` (financial viability — should already be cleared at F1/F2), `/ive-design-loop-custom` (full design process wrapper)
- IVE source — the canon is a body of co-authored work, not one paper:
  - Simanis, E., Samani, S., Burnett, P. & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *Rediscovering Capitalism: How Blue-Chip Builders Created Transformative Impact and Profit.* YNOT Institute Working Paper 1, Queens' College Cambridge
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *The Business Architecture: The Hidden Code of Industry Disruption.* YNOT Institute Working Paper 2, Queens' College Cambridge — the Business Architecture Framework
  - Simanis, E. et al. (2024). *The Core Business Archetype* (Jan); *Engineering New Market Ventures* (Apr); *The Market Creator's Dilemma* (Nov)
  - Simanis, E. (2025). *Built to Hold* — the FMOS gates; Simanis, E. & Donohue, K. (2025). *Deciphering the Market Creator's Dilemma.* MIT Sloan Management Review
  - Attribution rule (WS1 feedback log, 5 and 17 Sep 2026): Tom Manuel is a co-author on the 2023 papers; "co-developer of the method" is not supported. TMTH's own additions are the WS1 standards, the VA register, the circle end-state and the direction rule

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** `[evidence: VA-71]`

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R10 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R10 complete.

**R10 is special — it affects all products and all streams.** In Sections 5 and 6, instruct the user to review all CTM phases and all AOM streams for potential updates, not just one. The Leverage Strategy may affect Making (how inputs are sourced), Selling (partner relationships from R7 that now carry leverage risk), Using (delivery mechanisms that depend on the key input), and Marketing (brand or content dependencies).

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `acme-ctm-at-C10.html` |
| AOM | `[venture]-aom-at-C[N].html` | `acme-aom-at-C10.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `acme-fin-sim-at-C10.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user to review all CTM phases:
- **Phase 1 — Becoming:** does the Leverage Strategy affect how customers discover or are convinced? (e.g. if a gateway partner from R7 is also a supplier at risk of withdrawal)
- **Phase 2 — Consuming:** does the Leverage Strategy affect how the Working Product is delivered? (e.g. if the key input is part of the delivery mechanism)
- **Phase 3 — Paying:** does the Leverage Strategy affect the Payment Product? (e.g. if a payment processor is both partner and high-leverage supplier)
- **Phase 4 — Repeating:** does the Leverage Strategy reinforce or conflict with R9's resource moat?

For each phase where the Leverage Strategy has an effect, ask:
- Which 4-D product delivers it? (All products may be affected — Working Product, Payment Product, Communications Product, Partner Product)
- What is the specific element added or changed?
- What state change does it produce in the customer?

**R10 — update mode:** Add or modify all affected rows across all phases. Do not rebuild the whole document.

**Catch-up mode:** If the CTM does not yet exist, build it retrospectively from all confirmed strategies for R1 through R9, then update for R10.

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

Ask the user to review all AOM streams:
- **Making stream:** does the Leverage Strategy change how inputs are sourced or manufactured? (substitute development, structural bypass of existing supply)
- **Selling stream:** does it change partner relationships that carry leverage risk?
- **Marketing stream:** are there content, brand, or platform dependencies now made replaceable?
- **Using stream:** does the delivery mechanism depend on the key input, and does replaceability change how delivery operates?

For each affected stream, ask:
- Which level? (LMU / Territory / HQ)
- What role manages the replaceability mechanism?
- How long does it take per unit (or per period)?
- What is the volume driver?

**Check for common errors before writing:**
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if replaceability requires specialist sourcing or supplier management?
- Has a new HQ function been added if managing multiple supplier alternatives requires central procurement?

**LMU sizing check:**
1. Is this LMU large enough to be economically viable? (Enough volume to cover fixed LMU costs?)
2. Is this LMU small enough to replicate fast? (Can we stand up another one in weeks, not months?)
If both YES → PASS. If either NO → FLAG before proceeding.

**R10 — update mode:** Add or modify all affected stream activity rows. Do not rebuild the whole AOM.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R10.

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

1. Map those activities to the financial model's cost lines across all streams:
   - **Making stream** → drives COGS changes (cost of substitute sourcing vs existing key input)
   - **Selling stream** → drives CAC changes (partner management for replaceability)
   - **HQ functions** → drives fixed overhead changes (procurement, supplier management infrastructure)
   - **Timing changes** → drives working capital (if switching suppliers introduces timing gaps)

2. Update the financial simulation with the new activity costs and timing across all affected streams.
   - If a fin-sim exists: update all relevant cost lines. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM across all streams.

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

⚠ **FMOS uses the cost denominator: `FMOS = (ceiling − floor) ÷ floor` = `(WTP_low − Cost_high) / Cost_high`** (Simanis, *Built to Hold*, p.7). Do **not** divide by the ceiling/price — `(ceiling − floor) ÷ ceiling` is the gross-margin metric, a different and incompatible figure that understates FMOS. WTP_low = R2 KMC / price ceiling; Cost_high = AOM high-point unit cost.

**For R10:** Use the R2 KMC as the price ceiling. The cost floor updates with all new AOM additions from R10 across all streams. Note whether the Leverage Strategy increases or decreases the cost floor (substitute development may temporarily increase costs; structural bypass may ultimately reduce them).

**Verdicts:**
- **PASS (≥25%):** The financial limb's first half clears. Proceed to the three-limb close below — never straight to Section 9.
- **BORDERLINE (15–24%):** Surface the conditions. With a person present, ask: accept and proceed, or revise? Without one (autonomous mode — VA-153 branch 4): accept with conditions and record the decision in the gate verdict block, or revise once and record the loop-back; never stall and never choose silently. Either way the conditions are recorded as critical assumptions.
- **FAIL (<15%):** Return to Section 2 (key input diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Leverage Strategy? Name the mechanism and the precedent."
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
- What was created or updated: CTM (all affected phases and rows), AOM (all affected streams and levels), fin-sim (all affected cost lines)
- Current FMOS and verdict
- Mark **R10 complete** (or fail) on the status board
- All 10 requirements complete — route immediately to **`/ive-consistency-audit-custom`** (mandatory before the architecture is finalised)

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
