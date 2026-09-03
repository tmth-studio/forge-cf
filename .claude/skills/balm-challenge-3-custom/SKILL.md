---
name: balm-challenge-3-custom
description: IVE R3 — Circumvent Scaling Cost Bottleneck. Identifies the Critical Limiting Operation II (CLO II) — the working capital constraint that prevents the venture reaching at-scale without running out of cash. Produces a Scaling Strategy that transforms the financing lag into a value-creating mechanism.
---

# BALM R3 — Circumvent Scaling Cost Bottleneck

**Purpose:** Identify the financing gap between the venture's capital outlay per unit and the point at which revenue is received. Produce a Scaling Strategy that transforms this working capital constraint into a value-creating mechanism — not a cost transferred to someone else.

**When to run:** After R2 is complete and productized. R3 completes Function 1. The FIT Verifier gate runs after R3 — F2 (R4–R7) begins only after a PASS verdict.

**Output:** Critical Limiting Operation II (working capital constraint), Scaling Theory of Change, Scaling Strategy, Business Form Factor (C1–C3).

**Handoff to:** FIT Verifier (`/ive-fit-verifier-custom`), then R4 (Circumvent Customer Doubt about Value) — the Scaling Strategy from R3 completes F1; R4 begins F2.

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

**→ This skill: R3 — Circumvent Scaling Cost Bottleneck** (F1, third and final requirement; completes the Value Barrier)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design.

---

## R3 definition

> Circumvent the financing gap between the venture's capital outlay per unit and the point at which revenue is received. R3's impact shows up on the balance sheet — it is a working capital problem, not a P&L problem.

R1 determines the at-scale cost floor. R3 determines whether the venture can survive long enough to reach at-scale. A venture can have a sound R1 (viable unit economics) and still fail at R3 if the scaling architecture requires prohibitive upfront capital before revenue arrives.

**The stakes.** Working capital is expensive for new ventures — 25–40% APR is typical, because lenders price the higher risk. Because interest compounds across the scaling period, the cumulative cost of carrying a financing lag can add 50% or more to the required price. The off-grid rural solar case is the canonical example: the cost of carrying the financing lag between paying the OEM supplier and recouping installment payments from customers inflated the required price for profitability by over 50%. A venture with viable at-scale unit economics destroyed its market creation margin before it got there. R3 is the requirement that closes that trap before launch.

**The three-way distinction:**

| Requirement | Problem type | Shows up on |
|-------------|-------------|-------------|
| R1 | At-scale operating cost — CLO eliminates the conventional cost floor | P&L |
| R2 | Customer value ceiling — what customers will pay, and how many | Revenue line |
| R3 | Working capital during growth — financing the gap between outlay and receipt | Balance sheet |

---

## This skill IS a design loop (read first)

Running R3 is not a four-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.**

The four steps map onto this skill's existing structure:
- **Diagnose** — the Critical Limiting Operation II (the working capital constraint this challenge isolates).
- **Theorize** — the Scaling Theory of Change (named mechanism; prescriptive, not descriptive).
- **Productize** — the Scaling Strategy + cumulative BFF (C1–C3) + the CTM/AOM update (the architectural decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back. R3 completes F1, so this Simulate feeds the F1-outer FIT Verifier.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure (it is how Calmly's first floor omitted the guarantee payout).

**Simulate — the gate with teeth (mandatory; do not skip on illustrative data).** A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R3 has not been designed, only described. The Section 8 FIT gate enforces this; the rules below govern it.

1. **Use the correct FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling; Cost_high = the AOM high-point unit cost. **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on?
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL and the specific result that would force a pivot: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* The bar for a sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

**Loop-back and the pivot discipline.**
- **FAIL or BORDERLINE → return to Diagnose** (Sub-requirement 1 / Section 2 — CLO II), not to a tweak. Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why the challenge will not clear and what decision is needed.
- **Close criterion.** Mark R3 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## Sub-requirements checklist

Work through these four sub-requirements in sequence. Each must be confirmed before moving to the next.

- [ ] **1. Critical Limiting Operation II** — identify the working capital constraint
- [ ] **2. Scaling Theory of Change** — name the class of problem and the theory that solves it
- [ ] **3. Scaling Strategy** — operationalise the ToC to transform (not transfer) the constraint
- [ ] **4. Business Form Factor (C1–C3)** — cumulative BFF incorporating all solutions from C1–C3

---

## Sub-requirement 1: Critical Limiting Operation II

> *The operational procedure that commands the greatest amount of working capital as the venture scales — i.e., commands a significant amount of upfront investment and time before it starts to 'pay for itself.'*

The CLO II is not the same as the CLO from R1.

| Term | What it is |
|------|-----------|
| CLO | The operation in the conventional BFF whose cost makes the model unworkable at-scale. An operating cost problem. |
| CLO II | The financing lag that makes the journey to at-scale unworkable. A working capital problem. |

**Quick and Dirty key activities scan.** Before working through the diagnostic questions, map the key activities and their attendant resources across the four product types. This prevents missing a working capital driver that is obvious in operations but invisible in unit economics.

| | **Get Paid** (Payment Product) | **Make** (Working Product) | **Sell** (Comms Product) | **Deliver** (Partner Product) |
|---|---|---|---|---|
| **Key activities** | | | | |
| **Key resources** | | | | |

Resources fall into three types — identify which type applies to each key resource before estimating costs:
- **Personnel:** people that perform activities to make or move products (recurring labour cost — scales with volume)
- **Durables:** assets that depreciate over a long period (upfront capex — committed before revenue; creates the financing lag)
- **Consumables:** inputs used up at once (per-unit cost — ties to transaction volume directly)

**Durables are the primary CLO II risk:** they require upfront capital before revenue and depreciate over time, creating a multi-period financing lag. Identify every durable in the above table before proceeding to the diagnostic questions.

**Diagnostic questions — work through these:**

- What capital must be committed before a unit can generate revenue? When exactly does it go out?
- When is revenue received per unit? What determines the lag?
- What is the working capital requirement per unit (outlay − receipt × duration)?
- At the volume required for at-scale economics, what is the total working capital requirement?
- What happens to the venture's cash position during a growth ramp? At what growth rate does the venture run out of cash before reaching at-scale?

**State precisely:**
- Capital committed per unit: £ amount and timing
- Revenue received: £ amount and timing
- Financing lag: duration between the two
- Working capital per unit: £
- At-scale working capital requirement: £ at X units/year

Once you have described the CLO II, confirm it before we move to Sub-requirement 2.

---

## Sub-requirement 2: Scaling Theory of Change

> *The class of problem the Critical Limiting Operation II represents/falls into, and the theory/ies most effective in explaining how to solve that class of problem.*

**Run `/theory-of-change-custom` now, invoked as "R3 Scaling".** It will produce the Scaling Theory of Change in CMO format (Pawson & Tilley, 1997), enforce the theory/hypothesis distinction, and output the four fields in BALM-ready format.

**Format (four fields):**
- **Class of problem:** name the mechanism that produces the financing lag (maturity mismatch, information asymmetry between venture and capital market, adverse selection in asset markets, etc.)
- **Theory:** cite the peer-reviewed theory that predicts how addressing this mechanism changes financing behaviour
- **Current state:** how the CLO II currently manifests — specific and observable
- **Desired state:** the outcome state after the CLO II is circumvented — stated as a completed state, not an activity

**Discipline:** the theory section contains only established, citable findings. The design claim belongs in Sub-requirement 3 (Scaling Strategy).

Once the Scaling ToC is confirmed, move to Sub-requirement 3.

---

## Sub-requirement 3: Scaling Strategy

> *The best way to operationalize the Scaling TOC for circumventing or eliminating the Critical Limiting Operation II driving up working capital during the scaling period.*

⚠ **MANDATORY — before writing the Scaling Strategy, complete these three steps in order:**

**Step 3a — Baseline honestly.** State where the current BFF stands on the CLO II / working capital constraint. Not "not yet addressed" and not "already solved" — what does it actually do, and what does it leave unresolved?

**Step 3b — Generate ≥2 candidate BFF mutations.** Structural changes (not features) that could transform the working capital constraint materially better than the baseline. If you cannot produce two genuine mutations, say so explicitly — that is justification mode. Do not paper over it. Do not proceed to Step 3c until two real mutations exist on the table.

**Step 3c — Evaluate and decide.** For each candidate: does it transform (not transfer) the working capital cost? Does it require the venture's specific BFF to function? What does it cost in coherence with R1/R2? Record the decision. Adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected. Never "it already works."

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing the Scaling Strategy. No strategy text is valid without it.**

```
MUTATION GATE — R3
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

Only after the contract block is emitted, write the Scaling Strategy.

**Critical constraint:** the Scaling Strategy must be consistent with the Workaround Strategy from R1 and the Efficacy Strategy from R2. The Scaling Strategy operates within the BFF those strategies established.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

**State as a strategy, not a product feature.** One to three sentences. The next step is productization.

### The cost-shifting test — the most common R3 failure

> "We found someone else to hold the cost" is not R3.

Any incumbent can transfer working capital to an investor, lender, or partner. This creates no new value and builds no architectural advantage. A genuine R3 solution transforms the working capital constraint into a mechanism that creates value for someone.

**Test: does this solution require a new BFF, or could any incumbent do the same thing without changing their architecture?**

- If an incumbent could adopt it without structural change → it is not R3. It is a financing arrangement.
- If the solution requires the venture's specific BFF to function → it may be R3. Now check: does it create new value, or just move existing cost?

**Worked example:**

*Cost-shifting (not R3):* A solar energy leasing company raises equity from impact investors who hold the asset and earn a return. This is standard project finance — any incumbent could do the same. No new BFF required. No new value created by the structure itself.

*Transformation (R3):* The same company designs the leasing portfolio as a standardised, tradeable asset class. Standardisation enables secondary market liquidity. Liquidity drives down the cost of capital below what any bespoke arrangement achieves. The standardisation process is itself a value-creating mechanism — it is the thing that makes the capital cheap. The BFF had to change to make this possible.

**Three quality tests for the Scaling Strategy:**

1. **Cost-shifting test:** does this create new value for someone, or does it just transfer the cost to someone else?
2. **New BFF test:** does this solution require the venture's specific architecture to function?
3. **R1/R2 consistency test:** does this work within the cost floor (R1) and value ceiling (R2) established?

Once the Scaling Strategy is confirmed, move to Sub-requirement 4.

---

## Productizing R3 — Strategy → BFF

The Scaling Strategy names the mechanism that transforms the working capital constraint. Productizing it means shaping the Payment Product so the financing structure is a built-in property of the architecture — not a separate arrangement that lives alongside it.

**Target product component:** Payment Product (Making — working capital structure)

Work through these three questions before writing the cumulative BFF:

**1. Architecture, not finance.** Is the working capital solution embedded in the product's payment architecture, or does it depend on an external financing arrangement (investor capital, grant funding, bank facility)? External arrangements are not architecture — they are working capital management. The cost-shifting test applies directly: if the Scaling Strategy requires a third party to absorb the financing lag without receiving structural value in return, it has not been productized. Ask: what product form factor would make the financing structure self-generating?

**2. Accumulation.** Does the Scaling Strategy work within the BFF shape R1 and R2 established? The payment architecture must be compatible with how the Working Product delivers its efficacy — the payment trigger must sit at the right point in the customer's use routine. If R3's productizing creates a tension with R1's delivery form or R2's value mechanism, surface it now and resolve it before writing the BFF.

**3. Value creation check.** Does the productized form factor create new value through its structure — lower cost of capital, better liquidity, faster cycle times — or does it merely redistribute an existing cost? Only the former passes R3. The latter is an accounting adjustment, not architecture.

**4. At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A BFF that requires founding-team bandwidth, managed-by-exception operations, or pilot-only concessions is a launch-phase design, not an architecture. Name the at-scale volume explicitly. If the mechanism breaks before reaching it, return to Diagnose.

When all three are confirmed, identify the architectural spine before writing anything.

**Step 0 — Find the architectural spine.** The architectural spine is the single mechanism that runs through all prior requirements — the element whose removal would cascade failures across the most of C1 through C[N]. Every BFF has one. Finding it before writing forces the statement to be an architecture, not a list.

Diagnostic question: what would break first if you removed one core element from the design? The mechanism that cascades failures across the most requirements is the spine.

Write the opening sentence of the BFF around it. If the opening sentence could be "A product that does X (C1); does Y (C2); does Z (C3)..." — the spine has not been found. Go back and find it.

Write the cumulative BFF (C1–C3). This statement completes F1 — it is the full cost-and-value architecture that the FIT Verifier will test.

⛔ **MANDATORY HANDOFF — BFF C1–C3 CONFIRMED. DO NOT EDIT THE VDR. DO NOT ROUTE TO FIT VERIFIER OR R4.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "BFF C1–C3 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## Sub-requirement 4: Business Form Factor (C1–C3)

> *A cumulative statement of the venture's form factor incorporating all solutions from C1 through C3.*

This is the cumulative BFF — it incorporates the Workaround Strategy (R1/C1), the Efficacy Strategy (R2/C2), and the Scaling Strategy (R3/C3) into a single integrated statement of how the venture creates, delivers, and sustains value.

**State as a coherent whole**, not a list of three separate answers. The BFF is the essential shape the product and operations take — the default way it is made, sold, delivered, and paid for, at the level of the Core Business Architecture.

**The test for a BFF statement vs a list:** remove the challenge labels (C1, C2, C3...) and read it cold. Does it describe a product? Or a checklist? If a checklist, the architectural spine has not been found. A properly constructed BFF reads as a description of one coherent product — the challenge labels appear as parenthetical citations, not as the structural joints holding the sentence together.

**Check:** does the cumulative BFF hold together as a single architectural logic? If any of the three solutions pull in different directions, the architecture has a fault line. Resolve it before the FIT Verifier gate.

After confirming the BFF (C1–C3), run the FIT Verifier (`/ive-fit-verifier-custom`) against the R1 cost structure and R2 value ceiling. F2 begins only after a PASS verdict.

---

## R3 output format

```
SUMMARY
  Scaling Strategy: [strategy in one sentence — the architectural direction]
  Working capital constraint addressed: [CLO II in one phrase — the financing lag being resolved]
  Grounded in: [named theory]
  Creates new value (not a cost-shift): [Yes / No]

R3 — SCALING COST BOTTLENECK
---
CRITICAL LIMITING OPERATION II
  Capital committed per unit: [£ / timing]
  Revenue received: [£ / timing]
  Financing lag: [duration]
  Working capital per unit: [£]
  At-scale working capital requirement: [£ at X units/year]

SCALING THEORY OF CHANGE
  Class of problem: [Named mechanism]
  Theory: [Citation]
  Context: [How the CLO II currently manifests — specific and observable]
  Mechanism: [How addressing this class of problem changes financing behaviour]
  Outcome: [Desired state — completed state, not an activity]

SCALING STRATEGY
  [One to three sentences — architectural direction, not product feature]
  Cost-shifting test: [Does this create new value, or transfer cost?]
  New BFF test: [Does this require the venture's specific architecture to function?]

BUSINESS FORM FACTOR (C1–C3)
  [Cumulative statement — one integrated description of how the venture creates, delivers, and sustains value across all three solutions]

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
  Does the Scaling Strategy transform (not transfer) the working capital constraint? [Yes / Partial / No]
  Does it require a new BFF? [Yes / No]
  Is Stage 1 economically viable standalone? [Yes / No / Unverified]
  Is the cumulative BFF internally consistent? [Yes / No]
  Confidence: [High / Medium / Low]
```

---

## Common failure patterns at R3

| Failure | What it looks like | What it means |
|---------|-------------------|---------------|
| Equity as R3 | "We'll raise equity to fund working capital" | Equity is a Stage 1 bridge at best. It does not transform the constraint — it transfers it to investors at a high cost of capital. Not R3. |
| Architecture confusion | Single model designed to serve both scaling and at-scale purposes | Two distinct engineering problems conflated into one design. Usually fails at both. Design them separately. |
| Stage 1 only | Proof-of-concept stage with no Stage 2/3 economics | The venture stalls between stages. Institutional capital requires Stage 2 data. Without Stage 2 design, Stage 1 is a dead end. |
| Cost-shifting dressed as transformation | "Investors hold the working capital and earn a return" | Standard debt with extra steps. Not R3 unless the return structure is architecturally different from available alternatives and creates value through the structure itself. |
| R3 designed before R1/R2 | Scaling strategy built without a confirmed cost floor or value ceiling | Working capital requirement cannot be calculated without at-scale unit economics. R3 requires R1 and R2 inputs. |
| Ignoring durables | Treating all resource costs as per-unit consumables | Durables (equipment, infrastructure, vehicles) require upfront capital before revenue and create multi-period financing lags — the primary source of CLO II. The off-grid solar case: OEM system cost paid upfront, revenue collected as installments over 24 months. The carrying cost of this lag raised required price by 50%+ before architecture was changed. |
| Operational description as Strategy | Listing outcomes ("multiple providers compete", "fees fall", "customers persist") instead of naming the architectural decision that produces them. An outcome is evidence the strategy works — it is not the strategy. | Name the single structural move whose removal would make the outcome impossible. That is the architectural decision. Everything else is consequence. |
| Semicolon chain as BFF statement | "A product that does X (C1); does Y (C2); does Z (C3)..." | A semicoloned list of challenge solutions is a checklist, not a BFF. The statement should describe one coherent product architecture. Find the architectural spine — the single mechanism whose removal would cascade failures across the most prior requirements — and write the opening sentence around it. The challenge labels should appear as parenthetical citations, not as the structural joints holding the sentence together. |

---

## Relationship to other BALM requirements

```
PCO → R1 (Workaround Strategy) → R2 (Efficacy Strategy) → R3 (Scaling Strategy) → FIT Verifier → R4
```

R3 completes F1. After R3, the FIT Verifier gate runs against the R1 cost structure and R2 value ceiling. F2 (R4–R7) begins only after a PASS verdict from the FIT Verifier.

**R1 vs R3:** R1 solves the operating cost problem (P&L). R3 solves the working capital problem (balance sheet). They are distinct. A venture with a solved R1 can still fail at R3 if the growth architecture requires capital before revenue arrives.

**Cross-requirement elegance:** the highest-quality R3 solutions also advance other requirements. A standardised, tradeable asset class (R3) may also function as proof of efficacy for R4 (customer conviction) or R2 (value ceiling signal). A stage-gate financing structure may also generate the customer data needed for R5 (activation) or R7 (partner activation). Ask: does this mechanism also touch any other requirement? The best solutions usually do.

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `method/context/va-design-discipline.md`

This challenge's job is **not** to confirm the current BFF already handles scaling cost / working capital. It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat — not the answer to defend.

**VA-3 — generate before you justify.** Before writing this challenge's Strategy:
1. **Baseline, honestly.** Where does the current BFF stand on scaling cost / working capital? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on scaling cost / working capital than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations** — structural changes to the business, not features bolted on.
   ⚠ If you cannot produce two genuine mutations, say so explicitly. That is the tell you have slipped into justification mode — do not paper over it by restating the existing BFF.
4. **Evaluate each against the whole** — gain on scaling cost / working capital vs cost to coherence (VA-1) and to dimensions earned in earlier challenges.
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

## Output language — ASD-STE100 (Tom's standing preference, 17 Aug 2026)

Write every rendered output document this skill produces — the VDR challenge section, HTML records, and any prose deliverable — in **ASD-STE100 Simplified Technical English**:

- One instruction or one statement per sentence. Descriptive sentences ≤ 25 words; procedural sentences ≤ 20 words.
- Active voice. Present tense unless the past is necessary.
- One meaning per word, one word per meaning — add a "Defined terms" table to rendered documents and use those terms consistently.
- No idioms, no gerund-led clauses, no empty hedging, no metaphor in load-bearing statements.
- Prefer approved-word constructions: "make sure" not "ensure"; "use" not "utilise"; "start" not "commence".
- Warnings and open items as commands ("Check X before Y. Do not assume it."), not observations.

This governs the *rendered document*, not the method: sub-requirement definitions quoted from this skill stay verbatim, theory citations keep their original titles, and internal working notes may stay in normal register. Reference example: `ventures/Education/education-venture-design-record-2026-08-17.html`.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-challenge-3-custom/SKILL.md` to modify
- **Predecessor:** `/balm-challenge-2-custom` (R2)
- **Successor:** `/balm-challenge-4-custom` (R4, via FIT Verifier gate at `/ive-fit-verifier-custom`)
- **ToC tool:** invoke `/theory-of-change-custom` as "R3 Scaling" to produce the Scaling Theory of Change in BALM-ready format
- IVE source: Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–October 2025
- Asset standardisation / securitisation theory: Fabozzi, F. J. (2000). *The Handbook of Fixed Income Securities.* McGraw-Hill
- Information asymmetry in capital markets: Akerlof, G. (1970). "The Market for Lemons." *Quarterly Journal of Economics*, 84(3), 488–500

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** (Found on Calmly C1: "credible litigation backstop" — credibility is held by the defendant, and no product reached the defendant for three months.)

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R3 self-contained: it updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R3 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `calmly-ctm-at-C3.html` |
| AOM | `[venture]-aom-at-C[N].html` | `calmly-aom-at-C3.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `calmly-fin-sim-at-C3.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user:
- "What product component does the Scaling Strategy add or change?"
- Which CTM phase does it affect? **Phase 3 — Paying (working capital structure)**
- Which 4-D product delivers it? **Payment Product**
- What is the specific element? (e.g. "a standardised portfolio structure that enables secondary market sale before the venture receives primary revenue")
- What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)

**R3 — update mode:** Add or modify only the affected rows in the existing CTM. The Scaling Strategy modifies how payment is structured in Phase 3 — do not rebuild the whole document.

**Catch-up mode:** If the CTM does not yet exist (because prior challenges were run without this integrated structure), build it retrospectively from all confirmed strategies for R1 and R2, then add R3's payment phase mechanism.

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
- Which stream? **Making (working capital structure)**
- Which level? (LMU / Territory / HQ)
- What role manages the working capital mechanism?
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

**R3 — update mode:** Add or modify only the affected Making stream activity rows. Do not rebuild the whole AOM.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R3.

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
   - **Making stream at LMU level** → drives COGS (direct delivery cost per case/unit)
   - **Making stream at HQ level** → drives fixed overheads
   - **Timing of activities relative to revenue** → drives working capital (cash committed before revenue lands)

2. **For R3 specifically — the working capital calculation is the primary output.** The key question is: which activities happen before revenue lands, how long is the gap, and how much cash is tied up per unit during that gap? Confirm the timing structure is captured in the fin-sim before proceeding.

3. Update the financial simulation with the new activity costs and timing.
   - If a fin-sim exists: update the relevant cost lines. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM including the working capital structure.

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

**FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high`, where WTP_low = the R2 KMC / price ceiling and Cost_high = the cost floor (AOM high-point unit cost). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure.

**For R3:** Use the R2 KMC as WTP_low (the price ceiling). The cost floor updates with the new AOM additions from R3 (working capital structure activities). Note: R3's primary output is the balance sheet (working capital per unit and at-scale), but the FMOS check still runs against the same ceiling and updated floor.

**Verdicts (cost-denominator FMOS):**
- **PASS (≥25%):** Proceed to Section 9.
- **BORDERLINE (25–59% at full model; treat 15–24% as the early-warning band here):** Surface the conditions. Ask user: accept and proceed, or revise? If they accept, note the conditions as critical assumptions.
- **FAIL (<25%, early-warning <15%):** Return to Section 2 (CLO II diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Scaling Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)

---

### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines, working capital structure)
- Current FMOS and verdict
- Mark **R3 complete** (or fail) on the status board
- Route to **R4** (Circumvent Customer Doubt about Value) — via FIT Verifier PASS. F2 begins only after a PASS verdict.

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
