---
name: balm-challenge-7-custom
description: IVE R7 — Activate Gateway Partners. Identifies the intermediaries who control access to the target customer at scale and produces a Partner Activation Strategy that brings them into the venture's operating model as active participants.
---

# BALM R7 — Activate Gateway Partners

**Purpose:** Identify the gateway partner and design the Integration Strategy that secures their active commitment to champion the venture's solution. The Integration Strategy is a single architectural decision — how to apply the Integration ToC to this specific venture context. The resulting product architecture (the BFF) is documented in SR5, not SR4. R7 does not design a distribution channel — it determines whether the BFF architecture makes gateway partner activation structurally inevitable.

**When to run:** After R6 (Circumvent the Cash Flow Constraint) is complete. R7 is the final requirement of Function 2. It must be solved before F3 (R8–R10) begins. After all SR1–SR5 are confirmed, run Sections 5–8 (CTM, AOM, Fin-Sim, FIT gate) at the end of this skill session before proceeding to R8.

**Output:** Gateway partner identification, Integration Theory of Change, Integration Strategy (the single architectural decision that applies the ToC to this venture context), and Business Form Factor (C1–C7). Together these constitute the R7 component of the new Business Form Factor.

**Handoff to:** R8 (Create a Switching Cost) — R7 completes Function 2; R8 begins Function 3.

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

**→ This skill: R7 — Activate Gateway Partners** (F2, fourth and final requirement; completes Function 2)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design.

---

## R7 definition

> Identify and activate the intermediaries — gateway partners — who control the customer's awareness, trust, and access at the point where the venture must reach them. Gateway partners are not distribution channels. They are actors who already have the relationship, the trust, and the access that the venture needs to normalise its product in the customer's routine.

R7's impact shows up across F2: a well-activated gateway partner simultaneously advances the customer's Want (R4), reduces the learning disruption (R5), and can absorb or redistribute the cash flow constraint (R6). R7 is a force multiplier on F2 as a whole — not a standalone mechanism.

**Design principle — the elegance test for R7.** A strong Partner Activation Strategy resolves the partner's F2 barriers while simultaneously advancing the customer's F2 journey. The partner product and the customer product are not separate things — they are the same mechanism viewed from two angles. If the partner product solves the partner's barriers without advancing the customer's adoption, it is a partner incentive scheme, not an R7 solution.

---

## Why gateway partners are not distribution channels

Most founding teams conflate gateway partners with distribution. A logistics partner who moves product is not a gateway partner. A white-label reseller is not a gateway partner. The diagnostic question is: does this intermediary change the customer's conviction, activation, or payment behaviour — or do they only change where the product is available?

**The distinction that matters:**

| Distribution channel | Gateway partner |
|---------------------|-----------------|
| Moves product to the customer | Changes the customer's decision to adopt |
| Receives commission for sales | Bears reputational risk for recommendations |
| Relationship with the venture | Pre-existing relationship with the customer |
| Can be replaced by another channel | Cannot be replaced without rebuilding the trust infrastructure |

The Grameen Bank analogy: the peer group in joint liability lending is not a distribution channel for loans. It is a trust infrastructure that changes borrowers' conviction about repayment and creates the social mechanism that makes the product work. Remove the peer group and the product fails — not because distribution fails, but because the adoption mechanism fails.

---

---

## This skill IS a design loop

Running R7 is not a five-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.**

The four steps map onto this skill's existing structure:
- **Diagnose** — SR1 Key Customer Segments & Routines and SR2 Gateway Partner (isolating who controls access).
- **Theorize** — the Integration Theory of Change (SR3); named mechanism, prescriptive not descriptive.
- **Productize** — the Integration Strategy (SR4) + BFF (C1–C7) + the CTM/AOM update (the design decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back. R7 completes F2 — it is not exempt from the gate.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure (a common fidelity failure is omitting a money-flow outflow — e.g. a guarantee payout, a refund, a fee paid to a third party).

### Simulate — the gate with teeth (mandatory; do not skip on illustrative data)

A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R7 has not been designed, only described.

1. **Use the correct FMOS formula — cost denominator.**
   `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7).
   Do **not** use `(Price − Cost) / Price` (gross-margin / price denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling; Cost_high = the AOM high-point unit cost.
   **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on? Name them explicitly — these are the pivot triggers if the gate fails.
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* A sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

### Loop-back and the pivot discipline

- **FAIL or BORDERLINE → return to Diagnose** (not to a tweak). Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why R7 will not clear and what decision is needed.
- **Close criterion.** Mark R7 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## Process — step through each sub-requirement in order

Open by displaying this checklist to the user:

```
R7 sub-requirements
  [ ] 1. Key Customer Segments & Current Routines
  [ ] 2. Gateway Partner
  [ ] 3. Integration Theory of Change
  [ ] 4. Integration Strategy
  [ ] 5. Business Form Factor (C1–C7)
```

Then work through each sub-requirement one at a time:
- Show the sub-requirement **name** and its *definition*
- Ask the user to answer it
- Wait for their response, confirm it, then move to the next
- Do not present multiple sub-requirements at once

---

### Sub-requirement 1: Key Customer Segments & Current Routines

*Groups within the total addressable market of target customers that share common characteristics, along with their unique routines for achieving the High-import Outcome.*

Describe the key segments and their current routines. Stop there. Do not introduce gateway partners, category entry points, or any assessment of intermediaries — those belong in SR2. SR1 only establishes who the customers are and what they currently do.

---

### Sub-requirement 2: Gateway Partner

*An organization or entity common to all customer segment routines that occupies a central location in the ecosystem of information, expertise, and solutions currently consumed by target customers to achieve the High-import Outcome.*

Name the gateway partner and establish that they are already present in the customer's routine — specifically where in the routine they appear and that this is true across all segments. Nothing more. The answer should be short: who they are, and the moment in the routine where they appear.

Do not argue for why the gateway partner is better than alternatives. Do not describe what the venture will do through the partner. Do not explain their two-sided function or their role in the architecture. Those belong in SR3 and SR4. SR2 only establishes structural presence in the existing routine.

---

### Sub-requirement 3: Integration Theory of Change

*The unifying mission across all organizations and entities that comprise the Gateway Partner, and the theory/theories for securing each organization's commitment to champion the venture's solution under that unifying mission.*

This has two parts:

**(a) The unifying mission:** what goal or purpose do all gateway partner organisations share that the venture's product advances? This must be a genuine alignment of interests — not a commercial pitch.

**(b) The theory for securing commitment:** why will the gateway partner champion this product? Name the mechanism — the specific feature of the venture's architecture or the partner's situation that converts passive awareness into active championing. The theory must explain what causes the partner to move, not just describe the outcome of that movement.

Point to `/theory-of-change-custom` (invoke as "R7 Integration") for the formal ToC.

---

### Sub-requirement 4: Integration Strategy

*The best way to operationalize the Integration TOC for securing the commitment of the Gateway Partner to champion the venture's solution.*

⚠ **MANDATORY — before writing SR4, complete these three steps in order:**

**Step 4a — Baseline honestly.** State where the current BFF stands on gateway partner activation. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 4b — Generate ≥2 candidate BFF mutations.** Structural changes (not features) that could do materially better on gateway partner activation than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 4c until two real mutations exist on the table.

**Step 4c — Evaluate and decide.** For each candidate: what does it gain on gateway partner activation? What does it cost in coherence with R1–R6? Record the decision. Adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Integration Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R7
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

Only after the contract block is emitted, write the Integration Strategy.

**What SR4 is:** the single architectural decision that makes the Theory of Change fire in this specific venture context. It is the *how to apply the generic theory to this venture* — one sentence or short paragraph naming the structural move. It is not a description of the resulting product architecture; that belongs in SR5. Think of it as the move the chess player makes, not the resulting position on the board.

**What SR4 is not:** a description of what the BFF will look like, what features the product will have, or what the partner will experience. Those are consequences of the strategy, not the strategy itself. If the answer could be the opening of SR5 (the BFF), it has slipped into the wrong field.

**The architectural decision test:** ask "Is this the decision that causes the outcome, or a description of the outcome?" If it names what will happen rather than the structural move that causes it, the strategy has not been found. Strip back until one decision remains — the one whose removal would make the theory fail to fire.

**The boundary with go-to-market:** how activation differs in practice across partner types is a business model question, not an architecture question. SR4 names one structural decision that works across all partner types. If it requires bespoke activation per category, the architecture has not been solved.

**The value proposition presence test:** if the theory requires participants to know about the product before they need it (North 1990 / Del Duca — enforcement infrastructure changes transaction behaviour), the strategy must reach participants at the point of transaction initiation, not the point of dispute. Ask: does this decision fire at transaction, or downstream of it?

**The componenty test:** the strategy must read as one coherent argument, not a set of labelled components. Write it as prose that builds to the decision. Structural properties should be visible in the logic, not announced as headings.

**The elegance test:** does the strategy simultaneously advance the customer's F2 journey? If partner activation and customer adoption are structurally separate, look harder.

---

### Productizing R7 — Strategy → BFF

The Integration Strategy names how gateway partners are activated. Productizing it means shaping the Partner Product so it is the same BFF viewed from the partner's angle — not a separate product that runs alongside the customer product.

**Target product component:** Partner Product (Selling — access and trust)

Work through these three questions before writing the cumulative BFF:

**1. One architecture, two views.** Does the Partner Product require independent infrastructure, incentive schemes, or operational processes separate from the customer product — or does it emerge from the same BFF? The elegance test for R7 is strict: if the partner's activation mechanism and the customer's F2 journey are structurally separate, the architecture has been split when it should be unified. A partner activation scheme that requires its own budget line has not been productized.

**2. Accumulation.** Does the Partner Product work within the BFF shape R1–R6 established? The partner's role must fit naturally within the delivery mechanism (R1), the value proposition (R2), the payment structure (R6), and the customer's use routine (R5). If activating the partner requires changing any of these, surface the conflict now — do not absorb it into the BFF statement without resolving it.

**3. F2 completeness.** This is the last cumulative BFF before F3. The C1–C7 statement must read as a coherent architecture that could stand alone — not a list of seven separate solutions. Read it back as a whole: does the form factor described make it clear how the venture creates value, exchanges it, and sustains it? If the statement requires prior knowledge of the individual requirements to make sense, it has not been synthesised into a true BFF.

When all three are confirmed, identify the architectural spine before writing anything.

**Step 0 — Find the architectural spine.** The architectural spine is the single mechanism that runs through all prior requirements — the element whose removal would cascade failures across the most of C1 through C[N]. Every BFF has one. Finding it before writing forces the statement to be an architecture, not a list.

Diagnostic question: what would break first if you removed one core element from the design? The mechanism that cascades failures across the most requirements is the spine.

Write the opening sentence of the BFF around it. If the opening sentence could be "A product that does X (C1); does Y (C2); does Z (C3)..." — the spine has not been found. Go back and find it.

Write the cumulative BFF (C1–C7). This is the full F2 form factor — the last statement before F3.

---

### Sub-requirement 5: Business Form Factor (C1–C7)

*A cumulative statement of the venture's form factor incorporating all solutions from C1 through C7. This is the full F2 BFF — the last cumulative statement before F3.*

Draw on everything established across C1–C7. This is not a summary of R7 alone — it is the complete architectural statement of what the product is, how it is made, sold, delivered, and paid for, updated to include the gateway partner activation layer.

**The test for a BFF statement vs a list:** remove the challenge labels (C1, C2, C3...) and read it cold. Does it describe a product? Or a checklist? If a checklist, the architectural spine has not been found. A properly constructed BFF reads as a description of one coherent product — the challenge labels appear as parenthetical citations, not as the structural joints holding the sentence together.

⛔ **MANDATORY HANDOFF — SR5 CONFIRMED. DO NOT EDIT THE VDR. DO NOT PROCEED TO ANY OTHER STEP.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "SR5 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5. This gate exists because skipping to VDR editing after SR5 is a confirmed failure pattern (WS1, 4 June 2026).

---

## R7 output format

```
SUMMARY
  Integration Strategy: [strategy in one sentence — the architectural direction]
  Gateway partner: [who — specific entity type]
  Why they move: [unifying mission + named theory in one phrase]
  Dual effect on customer F2: [Yes / Partial / No]

R7 — GATEWAY PARTNER ACTIVATION
---
KEY CUSTOMER SEGMENTS & CURRENT ROUTINES
  Segment(s): [name + where gateway partner appears in their routine]

GATEWAY PARTNER
  Partner: [who — specific entity type, not generic "an intermediary"]
  Why central: [what role they play in the customer's existing routine]
  Current relationship to venture: [passive / unaware / aware but uncommitted]

INTEGRATION THEORY OF CHANGE
  Unifying mission: [what all gateway partner orgs share that this advances]
  Theory: [citation]
  Context: [...]
  Mechanism: [what causes the partner to move from passive to active]
  Outcome: [...]

INTEGRATION STRATEGY
  [answer]
  Mechanism: [how the partner moves from inactive to active]
  Dual effect: [how partner activation also advances the customer's F2 journey]

BUSINESS FORM FACTOR (C1–C7)
  [cumulative BFF statement — full F2 form factor]

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
  Is the gateway partner already present in the customer's routine (not just convenient)? [Yes / No]
  Does the Integration ToC explain why the partner moves from passive to active? [Yes / Partial / No]
  Does partner activation also advance customer F2? [Yes / No — if No, look harder]
  Could an incumbent deploy this without changing their BFF? [Yes — rethink / No — good]
  Confidence: [High / Medium / Low]
```

---

## Common failure patterns at R7

| Failure | What it looks like | What it means |
|---------|-------------------|---------------|
| Distribution channel as gateway partner | "Our distribution partner moves product to 500 retailers" | A logistics or sales partner who moves product is not a gateway partner. R7 requires an intermediary who changes the customer's conviction, activation, or payment behaviour. |
| Referral schemes as R7 | "We pay partners 15% commission on referred sales" | Commission is a business model decision, not an architecture decision. The architecture question is what the BFF must become so the partner has a structural reason to embed the product — commission is a consequence of that decision, not the decision itself. |
| Partner Product designed after customer product | "We'll figure out the partner offer once the product is launched" | The Partner Product must emerge from the same architecture as the customer product — not retrofitted later. If they require separate design, the architecture has been split when it should be unified. |
| Activation tactics as Integration Strategy | "We'll approach payment providers differently from ecosystem managers — two activation sequences" | Observations about how activation differs across partner types in practice are go-to-market observations, not architecture. SR4 answers one question: what does the BFF need to become for any partner type to embed it automatically? If the architecture requires bespoke activation per partner category, SR4 has not been solved. |
| Referral activation as Integration Strategy | "The strategy is to make it easy for partners to refer customers — low friction, embedded in existing workflow" | Reducing referral friction is an operational property, not a strategy. The strategy must answer: what does the BFF need to become so that the partner embeds it as a feature of their own value proposition? If the theory of change requires participants to know about the product before they need it, the strategy must fire at the point of transaction initiation — not at the point of dispute. Referral activation fires at the wrong moment. |
| Strategy written as labelled components | "Strategic objective / Guiding policy / Crux / Three enabling conditions..." | A strategy written as a set of named components is a parts list, not an argument. The Integration Strategy must read as one coherent logic that flows from diagnosis to championship. Structural properties — guiding policy, crux, enabling conditions — should be visible in the argument, not announced as headings. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

```
R4 (Customer doubt) → R5 (Learning disruption) → R6 (Cash flow) → R7 (Gateway Partners) → R8 (Switching Cost)
```

R7 completes F2. The customer adoption mechanisms established in R4–R6 define what the partner product must deliver — the partner product is the same BFF viewed from the partner's angle, not a separate design. R7 is the last F2 requirement before F3 begins.

**R7 completes the F2 picture.** After R7, the CTM and AOM should reflect the full F2 design — customer journey from Want through Buy, partner activation mechanism, and the interactions between them. This is the prerequisite before R8 begins.

**R7 vs channel strategy:** channel strategy is a Business Model decision — it determines how the venture competes within a shared BFF. R7 is an architecture decision — it determines whether the BFF works at all, given the structural access and trust barriers the venture faces. The same intermediary can appear in both: the architecture decision (R7) answers whether their activation is required for the BFF to function; the business model decision answers how the venture manages that relationship competitively.

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `method/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles gateway partner activation. It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on gateway partner activation? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on gateway partner activation than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on gateway partner activation vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
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
- Edit `.claude/skills/balm-challenge-7-custom/SKILL.md` to modify
- **Skill chain (predecessor):** `/balm-challenge-6-custom` (R6) → `/balm-challenge-7-custom` (R7)
- **Skill chain (successor):** `/balm-challenge-7-custom` (R7) → `/balm-challenge-8-custom` (R8 — F3 begins)
- `/theory-of-change-custom` is the shared ToC tool across all requirements — invoke it with "R7 Partner Activation" when the activation mechanism requires a named behavioural or institutional theory
- CTM, AOM, and Fin-Sim updates run at the end of this skill (Sections 5–8), after all SR1–SR5 are confirmed — not mid-session or between sub-requirements. Format specs: `shared/ctm-diagram-spec.md`, `shared/aom-diagram-spec.md` (the old `/ive-ctm-custom` and `/ive-aom-custom` skills are deprecated — do not invoke)
- IVE source: Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–August 2025
- 4-D product model: Simanis, E. (2021). IVE course materials, Cornell SC Johnson College of Business

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** (Found on Calmly C1: "credible litigation backstop" — credibility is held by the defendant, and no product reached the defendant for three months.)

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


**These sections run after ALL sub-requirements (SR1–SR5) are confirmed and the skill session is otherwise complete.** Do not run CTM, AOM, or Fin-Sim updates mid-session or between sub-requirements. The model updates are the last step of the architecting skill — they translate confirmed architectural decisions into the integrated model. Run SR1 through SR5 first, confirm the BFF, then execute Sections 5–8 in sequence.

These sections make R7 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R7 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention |
|-------|-------------------|
| CTM | `[venture]-ctm-at-C[N].html` |
| AOM | `[venture]-aom-at-C[N].html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing.

### Section 5 — CTM Update *(gate: all SR1–SR5 confirmed, BFF written and confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

**Diagram format:** See `.claude/skills/shared/ctm-diagram-spec.md` for the visual format, design system, and HTML boilerplate. The output is a horizontal swimlane flow diagram — state rectangles connected by coloured hexagon nodes. No THINK/FEEL/DO matrix rows in the diagram. Sparse text only.

**Execution route (mandatory — edit the model, generate the views):** the CTM lives as a model file, `[venture]-ctm-model-at-C[N].yaml`; the HTML record and the layered draw.io view are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed strategy as edits to states / transitions / component IDs (Flow Register format, e.g. `WP-2`). Reference implementation: `ventures/FinTech_Justice/calmly-ctm-model-at-C10.yaml`.
2. Generate both views:
   `python3 .claude/skills/shared/generators/generate_ctm_html.py <path>/[venture]-ctm-model-at-C[N].yaml`
   `python3 .claude/skills/shared/generators/generate_ctm_drawio.py <same YAML>`
3. The generators self-check and REFUSE to write on an incoherent model (a transition with no component and no flag, an unknown state, a malformed component ID). Fix the YAML — never hand-edit a generated file, never weaken the check.
4. **Catch-up:** if no model file exists yet (venture predates the model-file pattern), build the YAML from the current CTM record first, generate, confirm the output matches the record, then apply this challenge's changes.

**File naming:** `[venture]-ctm-at-C7.html` — label by challenge, not version number.

**Update process (5 steps):**

1. **Identify what changed** — which customer state transitions does R7 add or modify? R7 affects how the customer first encounters and adopts the product — typically Phase 1 (gateway partner activation changes the acquisition path). Check whether R7 overrides an existing sub-phase or adds a new one.
2. **Override or new row** — if R7 replaces a prior acquisition path, update the existing sub-phase rather than adding a row. Flag the override in the BALM mapping table.
3. **Update the BALM mapping table** — add the R7 row: challenge, phase affected, product components, what it replaces.
4. **Elegance check** — can all R7 state changes be driven by a single product component? If not, note explicitly which components are required and why they cannot be collapsed.
5. **Save and confirm** — file is `[venture]-ctm-at-C7.html`. Add `<!-- Updated: C7 — [date] -->` comment at top. Confirm before proceeding to Section 6.

**Actor lanes — general principle:**

Include a lane for every actor whose transformation is architecturally required by at least one confirmed challenge. Never add a lane for an actor whose transformation is not load-bearing. If a challenge activates a new actor type (e.g. a capital provider, an insurer, a regulator), add their lane from that challenge forward.

**Catch-up mode:** If the CTM does not yet exist, build it retrospectively from all confirmed strategies for C1 through C6 first, then apply the C7 update.

Before proceeding to Section 6, confirm the CTM file has been written.

---

### Section 6 — AOM Update *(gate: CTM written)*

**Diagram format:** See `.claude/skills/shared/aom-diagram-spec.md` for the visual format, Ops Map rules, HTML structure, and cost layer discipline. The output is an Ops Map + flow diagram — not a table. Build the Ops Map first; activities are derived from flows, not invented.

**Execution route (mandatory — edit the model, generate the views):** the AOM lives as a model file, `[venture]-aom-model-at-C[N].yaml` (actors · organisation with FTE and work drivers · components with allocations and DRIs · product/information/money flows per the IFC three-flow decomposition · spine order · waypoints). The views are GENERATED from it and never hand-written.
1. Copy the prior challenge's model file to the new `at-C[N]` name, then apply this challenge's confirmed changes. Reference implementation: `ventures/FinTech_Justice/calmly-aom-model-at-C10.yaml`.
2. Generate the views:
   `python3 .claude/skills/shared/generators/generate_aom_html.py <path>/[venture]-aom-model-at-C[N].yaml` (the Op Model Map)
   `python3 .claude/skills/shared/generators/generate_aom_drawio.py <same YAML>` (layered draw.io / Lucid view)
   `python3 .claude/skills/shared/generators/generate_aom_sysml.py <same YAML>` (machine-checkable SysML v2 — optional but recommended)
3. The generators self-check and REFUSE to write on an incoherent model (a component with no flow, an allocation to a non-existent function, a flow endpoint that resolves to nothing). Fix the YAML — never hand-edit a generated file, never weaken the check.
4. **Catch-up:** if no model file exists yet, build the YAML from the current AOM record first, generate, confirm equivalence, then apply this challenge's changes.

**File naming:** `[venture]-aom-at-C7.html` — label by challenge, not version number.

**Update process (7 steps):**

1. **Identify what changed** — R7 always adds to the Selling stream (gateway partner activation activities). Check whether it also adds to Making, Using, or Payment streams — it typically does not, but confirm from the confirmed Integration Strategy.
2. **Check for new enabler roles** — does gateway partner activation require a new role (e.g. account management, partnerships lead) not already in the AOM? If yes, add it.
3. **Check for new HQ function** — does the Integration Strategy require a regulatory, compliance, or legal setup activity at HQ level? If yes, flag with `⚑ Open: [confirmation required]` — do not add cost until confirmed.
4. **Add activity rows** — new Selling stream activities with volume drivers (per partner acquired ÷ conversion rate) and cost layers (RC) in the Activity detail table.
5. **LMU sizing check** — (a) LMU large enough to be economically viable at target partner volume? (b) Small enough to replicate fast? If either fails, flag before proceeding.
6. **Update cost stack** — RC per unit increases by new Selling stream activity cost. Recalculate FMOS. SC may increase if setup activities are confirmed. Produce the Group 4 fin-sim feed.
7. **Save and confirm** — file is `[venture]-aom-at-C7.html`. Add `<!-- Updated: C7 — [date] -->` at top. Confirm before proceeding to Section 7.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for C1 through C6 using `shared/aom-diagram-spec.md`, then apply C7 additions.

Before proceeding to Section 7, confirm the AOM file has been written.

---

### Section 7 — Fin-Sim Update *(gate: AOM written)*

**Skill:** `/ive-fin-sim-custom` — this skill stays live (it's a model builder, not a process guide). Point to it for the full simulation.

**File naming:** `[venture]-fin-sim-at-C7.html`

---

**Pricing unit — critical principle (apply to every venture):**

The pricing unit for the fin-sim must match the BFF at this challenge — not carried forward from the prior challenge's unit. R7 may change the BFF in a way that changes the natural unit of value exchange. Before building the fin-sim, ask: "What is one unit of the product the customer buys at C7?" Derive from the confirmed BFF, not from prior challenge conventions.

**Why the pricing unit is a pre-model gate (Simanis, "Running the Right Numbers", IFC/Lighting Global, p.35):**

> *"Before starting to build a bottom-up model, it is necessary to be clear on two things: 1) the basic mix of products to be sold, and 2) the way products will be priced. The reason for this is because the bottom-up modeling approach calculates required prices/margins by allocating whole costs back to products based, in part, on the number of monthly transactions of each."*

The mechanism: pricing unit → transaction count (Step 1: Bound the Operating Unit) → cost allocation across running costs and investment costs (Steps 2–3) → required price per unit (Step 4). A wrong unit produces a wrong transaction count, which misallocates costs and produces a required price that bears no relation to the actual product being sold. This is not a rounding error — it is a structural fault that invalidates the entire model. Do not proceed to the fin-sim until the pricing unit is confirmed from the BFF.

**Price ceiling — critical principle (apply to every venture):**

The ceiling is the incremental value created per unit for the gateway partner — not the gateway partner's current cost of doing the equivalent function in-house (that is a substitution floor, not a value ceiling). The ceiling is what a unit of the product is worth to the partner, measured as the incremental value it enables.

**Update process:**
1. State the pricing unit explicitly — derived from the confirmed BFF, not assumed from prior challenges.
2. State the price ceiling explicitly — incremental value created, not substitution cost. Name it as red if unvalidated.
3. Derive the cost floor from the AOM (Section 6 Group 4 feed + prior challenge cost stack).
4. Name all load-bearing assumptions explicitly. The two most common: (a) the key volume/rate driver that determines cost per unit, (b) the value ceiling input. Both must be stated as red until validated.
5. Run financial simulation → required price per unit.
6. Gate must be able to fail — do not suppress red inputs or use a proxy that cannot fail.

Before proceeding to Section 8, confirm the fin-sim is built on the correct unit for this challenge's BFF.

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

**For R7:** Use the pricing unit confirmed in Section 7. Cost floor from the updated AOM. Price ceiling = incremental value per unit to the gateway partner (not substitution cost — see Section 7 principle). If either the cost floor or the value ceiling is a red (unvalidated) input, the verdict is provisional: *"⚠ Provisional — pending [named input]. Would FAIL if [stated threshold]."* Do not record a clean PASS on red inputs.

**Verdicts:**
- **PASS (≥25%):** Proceed to Section 9.
- **BORDERLINE (15–24%):** Surface the conditions. Ask user: accept and proceed, or revise? If they accept, note the conditions as critical assumptions.
- **FAIL (<15%):** Return to Section 2 (gateway partner diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Integration Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)

---

### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines)
- Current FMOS and verdict
- Mark **R7 complete** (or fail) on the status board
- Route to **R8** (Create a Switching Cost) — F2 is complete. F3 begins.

### WS1 Feedback Capture *(optional — prompted at every close)*

Before routing, ask:

> "Quick WS1 capture? (y / skip)"

If **y**, ask these four questions in sequence and append the responses to `FEEDBACK.md` using this format:

```
---
## R7 · [venture name] · [date]

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
