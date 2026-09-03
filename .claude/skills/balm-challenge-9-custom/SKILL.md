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

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure (it is how Calmly's first floor omitted the guarantee payout).

### Simulate — the gate with teeth (mandatory; do not skip on illustrative data)

A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R9 has not been designed, only described.

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
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why R9 will not clear and what decision is needed.
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

Reference: `method/context/va-design-discipline.md`

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

*Failure this cures (Calmly C3, Aug 2026):* the cell required "an independent body with sufficient standing"; the shortlist chose CEDR by fit and speed; nobody asked which actor had to be convinced, what that actor reads, or whether CEDR sells the thing. C4 then moved the receiver from the defendant to the funder and the element was carried by label through C4–C10.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-challenge-9-custom/SKILL.md` to modify
- **Predecessor:** `/balm-challenge-8-custom` (R8 — Create a Switching Cost)
- **Successor:** `/balm-challenge-10-custom` (R10 — Manufacture Replaceability of the Key Supplier Input)
- **Related skills:** `/theory-of-change-custom` (invoke as "R9 Lock-Out"), `/ive-consistency-audit-custom` (run after R10)
- IVE source: Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** (Found on Calmly C1: "credible litigation backstop" — credibility is held by the defendant, and no product reached the defendant for three months.)

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R9 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R9 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `calmly-ctm-at-C9.html` |
| AOM | `[venture]-aom-at-C[N].html` | `calmly-aom-at-C9.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `calmly-fin-sim-at-C9.html` |

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

⚠ **FMOS uses the cost denominator: `FMOS = (ceiling − floor) ÷ floor` = `(WTP_low − Cost_high) / Cost_high`** (Simanis, *Built to Hold*, p.7). Do **not** divide by the ceiling/price — `(ceiling − floor) ÷ ceiling` is the gross-margin metric, a different and incompatible figure that understates FMOS. WTP_low = R2 KMC / price ceiling; Cost_high = AOM high-point unit cost.

**For R9:** Use the R2 KMC as the price ceiling. The cost floor updates with the new AOM additions from R9 (Making stream resource moat activities).

**Verdicts:**
- **PASS (≥25%):** Proceed to Section 9.
- **BORDERLINE (15–24%):** Surface the conditions. Ask user: accept and proceed, or revise? If they accept, note the conditions as critical assumptions.
- **FAIL (<15%):** Return to Section 2 (resource diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Lock-Out Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)

---

### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines)
- Current FMOS and verdict
- Mark **R9 complete** (or fail) on the status board
- Route to **R10** (Manufacture Replaceability of the Key Supplier Input)

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
