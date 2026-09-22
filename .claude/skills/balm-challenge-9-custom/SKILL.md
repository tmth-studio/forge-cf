---
name: balm-challenge-9-custom
description: IVE R9 — Manufacture a Resource Moat. Identifies the core competency and key resource critical to the value proposition, then designs a Lock-Out Strategy that makes that resource scarce or inimitable so competitors cannot replicate it.
---

# BALM R9 — Manufacture a Resource Moat

**Purpose:** Manufacture a state of scarcity or inimitability for a resource or asset needed for delivering on the customer value proposition. R9 builds a resource moat that makes it hard for competitors to enter. This is an offensive positioning move — it does not merely defend against external leverage (that is R10); it actively makes a critical resource structurally unavailable to competitors.

**When to run:** After R8 (Create a Switching Cost) is solved. R9 is the second requirement of Function 3. It must be resolved before R10 (Manufacture Replaceability of the Key Supplier Input).

**Output:** Required Core Competency, Key Resource, Lock-Out Strategy, and Lock-Out Theory of Change. Together these constitute the R9 component of the new Business Form Factor.

**Handoff to:** R10 — Manufacture Replaceability of the Key Supplier Input.

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

**→ This skill: R9 — Manufacture a Resource Moat** (F3, second requirement; requires R8)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints are sequencing problems, not architecture problems.

---

## R9 definition

> Manufacture a state of scarcity or inimitability for a resource or asset needed for delivering on the customer value proposition.

C9 builds a resource moat that makes it hard for competitors to enter.

**R9 vs R10 distinction:** R9 is about the competitive moat — making a critical resource structurally unavailable to competitors. R10 is about supplier leverage — making the venture's key input replaceable so suppliers cannot extract value. These are distinct architectural moves. Confusing them produces a venture that is defensively designed in the wrong direction.

---

## This skill IS a design loop

Running R9 is not a three-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.** R9 is an F3 challenge; it still runs the Simulate gate. The cost floor updates with the resource-moat activities R9 adds, so the gate is live — do not skip it because "it's a moat challenge."

The four steps map onto this skill's existing structure (note the F3 ordering — resource → theory → strategy):
- **Diagnose** — SR1 Required Core Competency / Key Resource (isolating the scarce asset).
- **VA-23 at Diagnose (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30) — the bottleneck is the at-scale one.** A launch constraint — no cash, the founder's hours, no cold outreach, a pilot's volume, a phase — is not a bottleneck and does not enter Diagnose, Theorize, Productize or Simulate at any of C1–C10. Test every candidate block: can the workaround be described without a phase, a pilot, a joint venture or a bootstrap? If not, it is a launch-instance item; write it in the carried-items row "carried to pilot-instance design after R10" and nowhere else. Tom's correction, 17 Sep 2026; RD-033.
- **Theorize** — the Lock-Out Theory of Change (SR2); named mechanism, prescriptive not descriptive.
- **Productize** — the Lock-Out Strategy (SR3) + the resource layer in the architecture + the CTM/AOM update (the design decision and its operational imprint).
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

A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R9 has not been designed, only described.

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
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why R9 will not clear and what decision is needed.
- **Loop counter and the third loop (VA-151, RD-036) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).** Print `loop_backs: n` in the gate verdict block. At the third loop-back the run states whether the next turn is a **pivot** (the theorem or the strategy changes) or a **mutation** (same theorem, a different form), and names the FIT line that decides it. A third loop that names neither is the `FLAG FOR TOM` above.
- **Four loop-gate branches (VA-153, RD-037) (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30).**
  1. *Later owner, adjacent:* a FAIL whose lever the next requirement owns routes forward with the FAIL inherited and the owner named in the verdict block.
  2. *Later owner, non-adjacent:* routes in sequence, the FAIL inherited through every requirement between, with a VA-85 lock on the owner; no requirement between may claim the repair.
  3. *Repair on a re-derived upstream figure:* the repair is claimed, the re-derived figure is named as the critical assumption, the verdict caps at PROVISIONAL, and the upstream requirement's row is annotated, not overwritten.
  4. *Warning band with no person present (autonomous mode):* accept with conditions and record the decision, or revise once and record the loop-back. Never stall; never choose silently. The choice and its reason go in the verdict block.
- **Close criterion.** Mark R9 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## Running this skill — step-through protocol

When this skill is invoked, open by showing the user the full R9 checklist, then work through each sub-requirement one at a time. Do not present all sub-requirements simultaneously. Present one, wait for the answer, confirm it, then move to the next.

**Opening checklist — show this first:**

```
R9 — MANUFACTURE A RESOURCE MOAT
Sub-requirements to work through:

☐ 1. Required Core Competency / Key Resource
☐ 2. Lock-Out Strategy
☐ 3. Lock-Out Theory of Change

Let's start with sub-requirement 1.
```

Then proceed sub-requirement by sub-requirement as follows.

---

## Sub-requirement 1 — Required Core Competency / Key Resource

**Name:** Required Core Competency / Key Resource

**Definition:** *The capability most critical to delivering on the value proposition / The asset critical to performing the required core competency for which there are few to no alternatives.*

This has two parts:

**(a) Required Core Competency:** what capability is the venture most critical to have — what must it be excellent at in order to deliver on its value proposition?

**(b) Key Resource:** what specific asset enables that competency, for which there are few or no alternatives? This is the resource that, if a competitor wanted to replicate the venture, would be hardest to acquire or develop.

**Diagnostic questions:**
- If a competitor wanted to replicate exactly what this venture does, what single resource would be hardest to acquire or develop?
- Is the resource tacit (embedded in people and processes), intangible (data, IP, relationships), perishable (time-sensitive), or complex (hard to reverse-engineer)?
- Does the resource exist in the world, or does the venture need to manufacture it?
- Is the scarcity natural or manufactured — and if manufactured, what is the mechanism?

**Ask the user:** "What capability is most critical to delivering your value proposition — and what specific asset enables that capability for which there are few or no alternatives?"

Wait for the answer. Confirm it. Mark sub-requirement 1 complete. Then move to sub-requirement 2.

---

## Sub-requirement 2 — Lock-Out Theory of Change

**Name:** Lock-Out Theory of Change

**Definition:** *The nature of the Key Resource to be protected (e.g., tacit, intangible, perishable, complex) and the theory/ies most effective in explaining how to limit its accessibility or imitability.*

**Order note:** R9 follows the same sub-requirement order as C8 and C1–C7: SR1 = resource, SR2 = Theory of Change, SR3 = Strategy. The Theory of Change explains *why* the resource is inimitable; the Lock-Out Strategy explains *what the architecture does* to manufacture that inimitability in this specific venture context. Theory before Strategy — not the reverse.

Point the user to `/theory-of-change-custom` and tell it: "R9 Lock-Out." It will produce the named Lock-Out Theory of Change using CMO structure in BALM-ready format.

**Ask the user:** "What is the nature of the Key Resource — is it tacit, intangible, perishable, complex, or something else — and what theory explains why the resource is inimitable? Run `/theory-of-change-custom` and tell it 'R9 Lock-Out' to get this in BALM format."

Wait for the answer. Confirm it. Mark sub-requirement 2 complete. Then move to sub-requirement 3.

---

## Sub-requirement 3 — Lock-Out Strategy

**Name:** Lock-Out Strategy

**Definition:** *The best way to operationalize the Lock-Out Theory of Change for making the Key Resource scarce or inimitable — stated at BFF level as a single architectural decision, not as a set of implementation choices.*

⚠ **MANDATORY — before writing the Lock-Out Strategy, complete these three steps in order:**

**Step 3a — Baseline honestly.** State where the current BFF stands on resource moat / lock-out. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 3b — Generate ≥2 candidate BFF mutations.** Structural changes (not features) that could make the Key Resource more scarce or inimitable than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 3c until two real mutations exist on the table.

**Step 3c — Evaluate and decide.** For each candidate: does it produce structural scarcity (not just contractual or time-based)? Does it build on what R1 already created rather than introducing an unrelated new asset? What does it cost in coherence with R1–R8? Record the decision. Adopt a mutation (restate the evolved architecture) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Lock-Out Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R9
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

Only after the contract block is emitted, write the Lock-Out Strategy.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

The Lock-Out Strategy must make the resource structurally scarce — not just harder to access. Three approaches, in ascending order of architectural quality:

**1. Substitute development**
Build an alternative that makes the scarce resource non-scarce for the venture's purposes. The original resource retains its value to others; the venture is no longer dependent — and competitors cannot use dependence on that resource as a lever to replicate the venture's position.

**2. Exclusivity capture**
Secure exclusive access to the resource before a competitor does — or before the resource is recognised as scarce. This is time-sensitive: the exclusivity window closes once others understand the resource's value. Exclusivity capture is most powerful when the venture moves before incumbents have mapped the resource landscape.

**3. Structural bypass**
Redesign the architecture so the resource is manufactured internally or made inimitable by structural means — rather than acquired or locked up. The highest-quality Lock-Out Strategy. It is harder to arrive at but produces the cleanest result: a resource that competitors cannot replicate because its scarcity is built into the venture's structure, not just its contracts or market position.

**BFF-level discipline — critical:** The Lock-Out Strategy must be stated as the single architectural design that manufactures scarcity as a structural consequence. It is not a list of implementation decisions (partner agreements, reporting formats, data governance policies, interface designs). Those belong in the operating model and business model layers. The test: does the strategy describe the *shape* of the product/architecture — how it is made, delivered, and operated — or does it describe *how this company specifically runs it*? Only the former is BFF. When applying a Theory of Change with multiple named properties (e.g. Dierickx & Cool's four asset stock properties), the Lock-Out Strategy should name the single architectural decision from which all those properties follow as consequences — not one implementation decision per property.

**Ask the user:** "What is your Lock-Out Strategy — the single architectural design that manufactures scarcity in this venture's context? Which approach fits best: substitute development, exclusivity capture, or structural bypass?"

Wait for the answer. Confirm it. Mark sub-requirement 3 complete. Then produce the R9 output block.

---

## Productizing R9 — Strategy → architecture

The Lock-Out Strategy names how the Key Resource is made scarce or inimitable. Productizing it means ensuring the scarcity is structural to the venture's architecture — not dependent on external arrangements that a well-resourced competitor could replicate or break.

**Target product component:** Working Product (Making — resource layer)

Work through these two questions before finalising the Lock-Out Strategy:

**1. Structural vs contractual scarcity.** Is the Key Resource scarce because of how the architecture is built — the resource becomes inimitable as a consequence of how the venture operates — or because of a contract, exclusivity deal, or first-mover position that could be replicated with enough money? Structural scarcity is R9. Contractual scarcity is a temporary position that needs an architectural answer. Ask: if a well-funded incumbent decided to replicate this resource in three years, what would stop them? If the honest answer is "not much," the architecture is not complete.

**2. R1 continuity.** The Workaround Strategy from R1 often reveals the competency that is most critical to the architecture. If R1 required developing a novel capability, that capability is likely the resource R9 should protect. Confirm the Lock-Out Strategy builds on what R1 already created — it should not introduce an unrelated new asset.

**3. At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A BFF that requires founding-team bandwidth, managed-by-exception operations, or pilot-only concessions is a launch-phase design, not an architecture. Name the at-scale volume explicitly. If the mechanism breaks before reaching it, return to Diagnose.

F3 requirements do not produce cumulative BFF statements. The productizing step is complete when the scarcity mechanism is confirmed as structural.

⛔ **MANDATORY HANDOFF — LOCK-OUT STRATEGY CONFIRMED. DO NOT EDIT THE VDR. DO NOT PROCEED TO R10.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "Lock-Out Strategy confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## R9 output format

The output block is the **VDR challenge summary panel** — a structured key-value block rendered at the top of the C9 challenge div, above the sub-requirement table. It replaces the prose paragraph summary. Its purpose is scannability: a reader should be able to read every challenge summary panel in sequence and understand the full architecture without opening any sub-requirement.

**Render as a `<dl>` grid in the VDR** (four rows: Lock-Out Strategy / Resource made scarce / Grounded in / Quality check). See C9 in the VDR for the HTML pattern.

```
SUMMARY PANEL — C9 (render as structured key-value block in VDR)

Lock-Out Strategy:    [one sentence — the single architectural decision]
Resource made scarce: [key resource + approach: substitute / exclusivity / structural bypass]
Grounded in:          [named theory — one line, properties cited if multiple]
Quality check:        [Structurally scarce ✓/✗ · Incumbent cannot replicate without new BFF ✓/✗ · Confidence: High/Medium/Low]
```

**Confirmation block** (internal, for session use — not written to VDR):

```
R9 — RESOURCE MOAT (LOCK-OUT)
---
REQUIRED CORE COMPETENCY / KEY RESOURCE
  Core competency: [what capability is most critical to the value proposition]
  Key resource: [the specific asset that enables this competency]
  Why scarce: [what makes it hard for a competitor to acquire or develop]

LOCK-OUT THEORY OF CHANGE
  Nature of the resource: [tacit / intangible / perishable / complex / other]
  Theory: [citation]
  Context: [...]
  Outcome: [...]

LOCK-OUT STRATEGY
  Approach: [Substitute development / Exclusivity capture / Structural bypass]
  [answer — BFF-level architectural statement, not implementation decisions]
  Mechanism: [how this makes the resource scarce or inimitable]

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
  Does the strategy make the resource structurally scarce (not just harder to access)? [Yes / No]
  Could an incumbent replicate this without a new BFF? [Yes — rethink / No — good]
  Confidence: [High / Medium / Low]
```

---

## Common failure patterns

| Failure pattern | Why it fails | What to do instead |
|-----------------|-------------|-------------------|
| Confusing R9 with R10 | R9 is about making a resource scarce for competitors. R10 is about making a supplier input replaceable for the venture. These are opposite moves. A venture that designs supplier replaceability as its resource moat has solved the wrong problem. | R9: what can competitors not get? R10: what can the venture replace if a supplier turns adversarial? |
| Contractual exclusivity as the full answer | A contract is not a moat. Contracts can be challenged, renegotiated, or simply expired. | The Lock-Out Strategy must produce structural scarcity — the resource becomes harder to access because of how the architecture is built, not because of what a contract says. |
| Resource that isn't actually scarce | Naming a resource that a well-resourced competitor could acquire in 12–18 months by spending money. | Test the scarcity: what prevents a competitor from buying, building, or hiring around this resource in 18 months? If the answer is "nothing," the resource is not a moat — it is a lead time. |
| Lock-Out Strategy identical to existing market practice | An approach that incumbents already use is not a moat — it is standard operating procedure. | The Lock-Out Strategy must be something the current BFF cannot accommodate. That is the definition of a new BFF contribution. |
| Theory of Change stated before Strategy | This was the previous guidance and is now corrected. R9 follows the same order as C8 and C1–C7: resource → Theory of Change → Strategy. The ToC explains why the resource is inimitable; the Strategy names the architectural decision that manufactures that inimitability. | Follow the correct order: resource → Theory of Change → Strategy. |
| BFF/business model conflation in the Lock-Out Strategy | The strategy lists implementation decisions — partner agreements, reporting formats, data governance policies, interface designs — rather than the single architectural design that manufactures scarcity. Implementation decisions belong in the operating model and business model layers. A strategy that reads as a list of operational choices is not a BFF-level answer. | State the Lock-Out Strategy as one architectural decision from which the inimitability properties follow as structural consequences. When using a theory with multiple named properties (e.g. D&C's four properties), the strategy names the single design that manufactures all of them — not one implementation decision per property. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

**Sequence:**
- **R8** (prerequisite) → creates switching costs that retain customers; the accumulated customer data and relationships may themselves become the Key Resource that R9 protects
- **R9** → manufactures structural scarcity for a critical resource; clears the way for R10 to address supplier-side leverage
- **R10** → the supplier-side complement to R9's competitive moat; R9 protects against competitors, R10 protects against suppliers

**R9 and R1:** The Workaround Strategy from R1 often reveals the competency that is most critical to the architecture. If R1's workaround required developing a novel capability, that capability may be the exact resource that R9 should protect. The strongest R9 solutions build on what R1 already created — they do not introduce an unrelated new asset.

**Cross-requirement elegance.** The strongest R9 solutions also touch other requirements. A Lock-Out Strategy that makes a resource scarce may simultaneously reduce a scaling cost (R3), deepen a switching cost (R8), or set up the supplier leverage position in R10. Ask at each design iteration: does this architectural move also advance any other requirement?

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles resource moat / lock-out. It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on resource moat / lock-out? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on resource moat / lock-out than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on resource moat / lock-out vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
5. **Decide and record** — adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

**VA-4 — show your working.** The candidates considered and rejected are not scratch work. Record them in the "considered / not chosen" block of the output format so the choice is auditable. Where a sub-requirement selects among options (e.g. the key store of value, the gateway partner), first consider 2–3 — across the relevant customers/partners — then record which won and why the others lost.

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
- Edit `.claude/skills/balm-challenge-9-custom/SKILL.md` to modify
- **Predecessor:** `/balm-challenge-8-custom` (R8 — Create a Switching Cost)
- **Successor:** `/balm-challenge-10-custom` (R10 — Manufacture Replaceability of the Key Supplier Input)
- **Related skills:** `/theory-of-change-custom` (invoke as "R9 Lock-Out"), `/ive-consistency-audit-custom` (run after R10)
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


These sections run after the BALM diagnostic work above is confirmed. They make R9 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R9 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `acme-ctm-at-C9.html` |
| AOM | `[venture]-aom-at-C[N].html` | `acme-aom-at-C9.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `acme-fin-sim-at-C9.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user:
- "What product component does the Lock-Out Strategy add or change?"
- Which CTM phase does it affect? **Phase 4 — Repeating (competitive moat)**
- Which 4-D product delivers it? **Working Product**
- What is the specific element? (e.g. "a proprietary data pipeline that ingests transaction data and becomes inimitable through volume accumulation over time")
- What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)

**R9 — update mode:** Add or modify only the affected Phase 4 rows in the existing CTM. The Lock-Out Strategy modifies how the venture's competitive position is protected through the Repeating phase. Do not rebuild the whole document.

**Catch-up mode:** If the CTM does not yet exist (because prior challenges were run without this integrated structure), build it retrospectively from all confirmed strategies for R1 through R8, then add R9's moat mechanism.

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
- Which stream? **Making**
- Which level? (LMU / Territory / HQ)
- What role maintains or builds the scarce/inimitable resource?
- How long does it take per unit (or per period, if this is a fixed infrastructure activity)?
- What is the volume driver? (per unit / per period / fixed per LMU)

**Check for common errors before writing:**
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if resource cultivation requires supervision or specialist input?
- Has a new HQ function been added if the resource moat requires central infrastructure (e.g. data science, IP management)?

**LMU sizing check:**
1. Is this LMU large enough to be economically viable? (Enough volume to cover fixed LMU costs?)
2. Is this LMU small enough to replicate fast? (Can we stand up another one in weeks, not months?)
If both YES → PASS. If either NO → FLAG before proceeding.

**R9 — update mode:** Add or modify only the affected Making stream activity rows. Do not rebuild the whole AOM.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R9.

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
   - **Making stream at LMU level** → drives COGS (resource cultivation activities per unit)
   - **Making stream at HQ level** → drives fixed overheads (IP, data infrastructure, exclusivity maintenance)
   - **Timing of activities relative to revenue** → drives working capital

2. Update the financial simulation with the new activity costs and timing.
   - If a fin-sim exists: update the relevant cost lines. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM.

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

**For R9:** Use the R2 KMC as the price ceiling. The cost floor updates with the new AOM additions from R9 (Making stream resource moat activities).

**Verdicts:**
- **PASS (≥25%):** The financial limb's first half clears. Proceed to the three-limb close below — never straight to Section 9.
- **BORDERLINE (15–24%):** Surface the conditions. With a person present, ask: accept and proceed, or revise? Without one (autonomous mode — VA-153 branch 4): accept with conditions and record the decision in the gate verdict block, or revise once and record the loop-back; never stall and never choose silently. Either way the conditions are recorded as critical assumptions.
- **FAIL (<15%):** Return to Section 2 (resource diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Lock-Out Strategy? Name the mechanism and the precedent."
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
- Mark **R9 complete** (or fail) on the status board
- Route to **R10** (Manufacture Replaceability of the Key Supplier Input)

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
