---
name: balm-challenge-1-custom
description: IVE R1 — Circumvent At-scale Cost Bottleneck. Identifies the Critical Limiting Operation (CLO) in the conventional Business Form Factor and produces a Workaround Strategy that eliminates it. The first of three Function 1 mathematical axioms. Uses VTS framework from Half-Solved + Cornell MCL (2025).
---

# BALM R1 — Circumvent At-scale Cost Bottleneck

**Purpose:** Identify and eliminate the Critical Limiting Operation (CLO) — the operation in the conventional Business Form Factor whose cost structure makes the default model unworkable at the required price point. Produce a Workaround Strategy that replaces the CLO at the architectural level.

**When to run:** After the Prime Commercial Opportunity (PCO) has been confirmed — see the **Entry gate** below for what "confirmed" means and the two valid paths into it. R1 is the first requirement of Function 1. It must be solved — and productized — before starting R2.

**Output:** Four structured inputs: Conventional BFF, CLO, Workaround Theory of Change, Workaround Strategy. Together these constitute the R1 component of the new Business Form Factor.

**Handoff to:** R2 (Eliminate Customers' Value Bottleneck) — the Workaround Strategy from R1 gives the initial form factor that R2 works with.

---

## ⛔ Entry gate — what R1 needs before Sub-requirement 1 (read first)

R1 runs on a **confirmed PCO**, expressed as a **single use case (Path A) or single impact case (Path B)**. It does **not** require a "Core Functionality" to begin.

**This gate exists because of a logged failure (June 2026):** the skill-runner demanded a "single core functionality" before R1 — which is Path-A-only language — and stalled an impact venture that had no CF and never needed one. Do not repeat it.

**Two valid entry paths** (Simanis, PCO Methodology, Step 2 — `TMTH_IVE_Wiki/wiki/Methodology/PCO_Methodology.md`):

| Path | Venture type | What you start from | Core Functionality required? |
|------|-------------|--------------------|------------------------------|
| **A** | technology / product | a **Core Functionality** — what it does and how, at its most basic level | yes — it is the starting object |
| **B** | social / impact | a **Pervasive Societal Problem**, levelled to one **impact case** — the industry-specific consequence a paying customer group experiences as a concrete cost | **no** — the core functionality is an *output* of the design loop, not a precondition |

The UN SDGs are an explicitly valid Path-B starting set. Simanis' own Calmly example is Path B: it starts from a problem ("small claims disputes reaching settlement out of court"), not a CF — the CF (risk-pooling + digital disintermediation) is what the loop *produces*.

**The gating object is the same on both paths: ONE confirmed PCO.** Not a CF. Not a mission. Not a category.

**Two hard stops before Sub-requirement 1:**

1. **No confirmed PCO → do not start R1.** "Never start R1 without a confirmed PCO. Attempting R1 on an undefined or un-chosen PCO produces a generic analysis that cannot be productized" (PCO→R1 bridge). If no PCO exists, stop and run `/balm-pco-custom` first. Do not improvise one inline without saying so explicitly.

2. **Scope is a category, not a single case → do not start R1.** "All the SDGs", "all of poverty", "every X" has no Conventional BFF, no single CLO, and no single FMOS — the entire R1 machinery is computed per case. A *mission* can stay broad; the *PCO R1 runs on* must be one levelled case. If the scope is a category, the next step is PCO Path B convergence (level the problem → name one impact case → screen it through the >30% market-creation-margin gate), **not** R1.

**What is NOT a reason to block:** the absence of a Core Functionality on an impact venture. That is normal and correct for Path B. Do not ask the user to "name the one core functionality" — ask for the **confirmed PCO / impact case**. If they have one, proceed to Sub-requirement 1. If they don't, route to `/balm-pco-custom`.

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

**→ This skill: R1 — Circumvent At-scale Cost Bottleneck** (F1, first requirement; prerequisite for R2)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design. A cost that seems large at 50 units is often trivial against the same cost at 50,000 units.

---

## Why R1 comes first — the architecture hierarchy

IVE distinguishes three nested levels of commercial architecture. Most founding teams operate at the wrong level.

| Level | What it is | Who shares it |
|-------|-----------|---------------|
| **Core Business Architecture (CBA)** | The deep strategy that sets both the cost curve and value curve for an industry. The highest-leverage intervention available to a founder. | No single company — it is the logic that makes the industry work |
| **Business Form Factor (BFF)** | The essential shape that product and operations take given a CBA. The "default way" the product is made, sold, delivered, and paid for. A new CBA manifests as a new BFF. | All companies in a market |
| **Business Model** | A company's unique strategy for outcompeting others within a shared BFF. Where differentiation lives. | Individual company |

**The founding trap:** most founders jump directly to business model thinking ("how do we compete?") before diagnosing whether the default BFF is viable for their context. If the BFF cannot produce value surplus at the target price point, competitive differentiation is irrelevant. Solve the BFF problem first.

R1 is an intervention at the CBA/BFF level — not a business model decision.

---

## The core problem R1 solves — the Cost-to-Value Barrier

> "The current/default core business architecture cannot make, sell, deliver, and get paid for a core functionality or solve the social problem at a unit cost that is lower than the value the customer gets."

This is the structural reason new markets do not form. Not product quality. Not marketing. The default BFF has set a cost floor that exceeds the price ceiling the target customer can pay. The solution is not to find better customers or charge more — it is to shift the cost curve down by innovating a new CBA that manifests as a new BFF.

**R1 definition:**
> Replace or bypass the operation in the default BFF that contributes the greatest share of costs once the venture is operating at-scale. Its impact shows up on the P&L — it is an operating cost problem, not a capital problem. "We'll be more efficient than the incumbent" is not a solution to R1.

**Value surplus:** the monetizable value left in the customer's pocket above and beyond the price they must pay for the product — where that price covers full unit costs including a competitive return on capital. R1 sets the floor of the cost curve. R2 sets the ceiling of the value curve. The gap between them is the value surplus.

---

## This skill IS a design loop (read first)

Running R1 is not a five-section form filled once. It is one turn of the IVE design loop — **Diagnose → Theorize → Productize → Simulate** — and the loop only closes when Simulate clears. The point of the loop is *learning by reasoning*: to reason this design to failure on paper and pivot **here, in simulation — not after launch, in market.**

The four steps map onto this skill's existing structure:
- **Diagnose** — Conventional BFF + Critical Limiting Operation (the at-scale cost bottleneck this challenge isolates).
- **Theorize** — the Workaround Theory of Change (named mechanism; prescriptive, not descriptive).
- **Productize** — the Workaround Strategy + BFF (C1) + the CTM/AOM update (the architectural decision and its operational imprint).
- **Simulate** — run the Model Stack (CTM→AOM→ARM→Financial Simulation→required cost per unit→FMOS); a real gate that can fail and loop you back.

### Simulate = run the Model Stack — not "estimate a floor"

Simulate is the IVE Model Stack carried through to a number. It is **not** a guessed cost floor or a top-down `£X ÷ volume`. That shortcut is the "high resolution, low fidelity" failure Simanis (2023, *Financial Simulations*) warns against — detailed numbers disconnected from the commercial logic (the solar-fridge team modelled a cheaper sales channel the product couldn't actually use). The chain:

**CTM → AOM → ARM → Financial Simulation → required cost per unit → FMOS.**
- **CTM** (demand side): the 4-D product components each customer state change requires.
- **AOM** (supply side): who does what, where, at what volume, to deliver them (Ops Map of product/information/money flows; LMU first).
- **ARM** (At-Scale Resourcing Model): the cost structure built **from first principles via resource drivers** — the step that makes this a simulation, not a spreadsheet. Three driver types combine to size every resource: **customer transaction drivers** (reachable market, penetration, share, product life, churn — tie cost to unit sales), **work drivers** (the activities each resource supports), **activity drivers** (time/quantity per granular activity). Output: the four cost layers **PVC · RC · SC · IC**, LMU-first.
- **Financial Simulation**: project the ARM across the volume ramp + the scaling/investment period, **discount for cost of capital**, reduce to the **required cost (and price) per unit**.

**Fidelity guardrail (hard):** every cost must trace to a resource the architecture requires → to a work/activity driver → to a customer-transaction driver tied to unit sales. A cost that can't be traced that way is low-fidelity and does not go in the model. Conversely, every money-flow *outflow* on the Ops Map (e.g. a guarantee payout, a refund, a fee) MUST appear — leaving one out is the most common fidelity failure (it is how Calmly's first floor omitted the guarantee payout).

**Simulate — the gate with teeth (mandatory; do not skip on illustrative data).** A gate that cannot fail is theatre. Even with placeholder figures, the Simulate step must be able to fail — or the loop never fires and R1 has not been designed, only described. The Section 8 FIT gate enforces this; the rules below govern it.

1. **Use the correct FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the R2 Key Monetizable Cost / price ceiling (at R1, a preliminary PCO estimate); Cost_high = the AOM high-point unit cost. **Bands — single source of truth is `Forge/WS1/criteria-registry.md`; do not redefine locally.** Two gate levels, do not conflate: *This challenge's Simulate gate (per-requirement early warning):* **PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%** — the band this skill's FIT section uses. *The whole-architecture / Phase II gate (not this skill — runs once, after all ten):* **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (60% survives the 62% average engineering cost overrun, Flyvbjerg & Gardner 2023). Use the per-requirement band here; the 60% bar is the final convergence criterion checked by the whole-architecture pass. If these ever disagree with the registry, the registry wins.
2. **Name the load-bearing assumptions.** Which 2–3 inputs does the FMOS most depend on?
3. **Run the stress test.** "What is FMOS if the three biggest cost/value assumptions all resolve badly at once?" (Flyvbjerg: complex projects average a 62% cost overrun — a passing design survives it.)
4. **State the pivot trigger explicitly.** Write the threshold at which the gate flips to FAIL and the specific result that would force a pivot: *"Would FAIL if [assumption] crosses [value] — that is the pivot trigger."* The bar for a sound design is exactly this sentence existing.
5. **Illustrative pass ≠ convergence.** If figures are placeholders (red), the verdict is **"⚠ Provisional pass — pending [the data that would settle it]; would FAIL if [trigger]."** Never a clean PASS on unvalidated inputs. The loop converges only when Simulate clears on inputs that *could have failed it*.

**Loop-back and the pivot discipline.**
- **FAIL or BORDERLINE → return to Diagnose** (Section 2 — CLO), not to a tweak. Re-run the loop with the FIT diagnosis as the new brief: which lever is off — cost floor too high, or value ceiling too low — and what changes.
- **A pivot changes the theorem or the strategy, not the tactics.** If the core mechanism is unchanged, it is optimisation, not a pivot.
  - *Pivot when:* FMOS is negative/below-gate and cannot be fixed within the current design; a key assumption is disconfirmed and the theorem no longer holds.
  - *Do not pivot when:* results are ambiguous, or the strategy wasn't actually tested (flawed execution of the reasoning).
- **Iteration cap.** If three loop-backs do not converge, stop and flag — do not spin. Write a `FLAG FOR TOM` block stating why the challenge will not clear and what decision is needed.
- **Close criterion.** Mark R1 complete only when Simulate clears (real PASS) or a BORDERLINE is consciously accepted with its conditions recorded as critical assumptions. An unvalidated provisional pass closes the *design* but leaves the loop open pending data — record it that way.

---

## Process — step through each sub-requirement in order

Open by displaying this checklist to the user:

```
R1 sub-requirements
  [ ] 1. Conventional Business Form Factor
  [ ] 2. Critical Limiting Operation (CLO)
  [ ] 3. Workaround Theory of Change
  [ ] 4. Workaround Strategy
  [ ] 5. Business Form Factor (C1)
```

Then work through each sub-requirement one at a time:
- Show the sub-requirement **name** and its *definition*
- Ask the user to answer it
- Wait for their response, confirm it, then move to the next
- Do not present multiple sub-requirements at once

---

## Sub-requirements

R1 is built from five sub-requirements, worked through in order. Each sub-requirement's output is a required input to the next.

---

### Sub-requirement 1: Conventional Business Form Factor

> *The 'gold standard' way the core functionality or commercial solution would typically be productised — made, sold, delivered, and paid for.*

**What it is:** The way the PCO's solution is conventionally productized — made, sold, delivered, and paid for. The gold-standard method. The default. Read it by path:
- **Path A (product/tech):** how the **core functionality** is conventionally delivered.
- **Path B (social/impact):** how the **impact case** is *addressed today* — the existing operational model a paying customer group already pays for to deal with that consequence. For Calmly that is solicitor-led litigation — that is the conventional BFF, not a "core functionality".

**First check — is the input a single case?** Before describing the conventional BFF, confirm the PCO is one levelled use/impact case, not a category. Test: if the answer to "what is the conventional way *this* is addressed?" is "it depends which sub-problem", the scope has not converged — stop and return to the **Entry gate** / `/balm-pco-custom`. On a Path-B venture, do **not** ask the user to name a "core functionality"; ask for the conventional way the impact case is handled today.

**Why it matters:** The conventional BFF is not a failure — it is the baseline. Without it, there is no CLO to identify and no R1 to solve. Early venture ideas naturally re-purpose existing BFFs. This is the correct starting point for diagnosis.

**Diagnostic questions:**
- What industry / sector currently addresses this case, even imperfectly?
- How is this solution typically packaged and sold today — or, on Path B, what does the customer currently pay someone to do about this consequence?
- What is the gold-standard way this would be solved if money were no object?
- Who are the established players operating in this BFF?
- What does the default customer journey look like from initial contact to post-delivery?

**State as a brief description:** how the solution is conventionally made, sold, delivered, and paid for — four activities, one sentence each.

---

### Sub-requirement 2: Critical Limiting Operation (CLO)

> *A key operation in the conventional business operating system that disproportionately drives up cost and creates a cost threshold that exceeds target customers' ability or willingness to pay.*

**What it is:** An essential operation in the conventional BFF that disproportionately drives up cost and creates a cost threshold that exceeds target customers' ability or willingness to pay.

**Key distinctions:**
- The CLO sits at the **architectural level** — it is a workflow or workstream made of multiple activities, not a single task
- It is **tightly coupled** to the BFF: if you can eliminate or change it without affecting adjacent operations, it is not the CLO
- It is **essential** — the conventional BFF cannot function without it. This is what makes it so hard to optimise away

**⛔ Probe for the operation, not the resource (read before naming the CLO).**

A CLO is an **operation** — a process or workflow the business *performs*. State it as a **verb**: "manufacturing each venture by trial-and-error", "assessing credit per borrower by hand", "facilitating each dispute with an expert". It is **not** a **resource, input, or cost line** — a **noun you buy**: "expensive operators", "teacher labour", "the LLM", "inventory".

**The trap:** the most visible thing is usually the expensive *resource*, so it gets named as the CLO. But the resource is the **symptom**; the **operation that requires it** is the CLO. Always ask: *"this cost is high — what operation incurs it? What process is the business running that forces this resource to be spent?"* Name that process.

**Why it matters:** the Workaround Strategy attacks whatever you name here. Name the **resource** and you will design to make the resource cheaper — optimisation within the existing BFF, which is **not R1**. Name the **operation** and you can replace the *process itself* with a new one — a new BFF, which is **true R1**.

*Worked example (logged 21 Jun 2026):* a venture studio's costly "founder-grade operators" are a **resource**. The CLO is the **venture-manufacturing process (lean startup / trial-and-error)** that requires them — and the workaround replaces that process (with IVE architecting), which dissolves the resource cost as a consequence, rather than just hiring cheaper operators.

**Test:** can you state the CLO as "the operation of [verb-ing]…"? If your candidate is a noun (a thing), it is probably a resource — convert it by asking *what the business does* that makes that thing necessary, and name that.

**Where cost concentrates — four zones:**

| Zone | What it covers | Example CLO |
|------|----------------|-------------|
| Making the product | Manufacturing, sourcing, inventory | Designer gown rental — large, rapidly depreciating inventory must be owned upfront |
| Selling the product | Customer acquisition, conversion, education | Fortified snack foods — high cost of changing customer evaluation and consumption patterns |
| Delivering the product | Logistics, last-mile, fulfilment | Meal subscription boxes — overnight cold-chain delivery forces a unit cost floor incompatible with mass-market pricing |
| Getting paid | Payment infrastructure, collections, credit risk | Installment finance in markets without credit bureau data |

**Diagnostic questions:**
- What is different about the *nature* of this problem compared to the default case? What boundary conditions are violated?
- Map the operational model: where is cost concentrated in Making, Selling, Delivering, or Getting Paid?
- Which single operation, if removed, would most change the cost structure?
- Why does this operation exist in the first place? Can that reason be dissolved?
- Is this operation tightly coupled to everything else (true CLO) or could it be removed without restructuring the whole?

**State precisely:**
- **State the CLO as an operation — a verb/process the business performs, not a resource it buys** (see the probe above)
- Which zone does it sit in?
- What makes the cost inherent to this operation?
- What specific cost threshold does it create relative to the target customer's ability to pay?

---

### Sub-requirement 3: Workaround Theory of Change (ToC)

> *The class of problem the Critical Limiting Operation represents, and the theory/ies most effective in explaining how to solve that class of problem.*

**What it is:** The class of problem the CLO represents, and the theory most effective in explaining how to solve that class of problem.

**Why it matters:** abstracting the nature of the problem from its specific manifestation is essential. Anchoring in a theory base supplies the logical criteria needed to evaluate solutions, not just generate them. A solution without a ToC is an untested assumption. A solution grounded in a ToC has a falsifiable logic chain.

This step prevents solving the surface symptom instead of the underlying structural problem.

**Format (four fields):**
- **Class of problem:** name the mechanism that produces the CLO (information asymmetry, transaction cost, adverse selection, principal-agent problem, behavioural lock-in, etc.)
- **Theory:** cite the peer-reviewed theory that predicts how eliminating this class of problem changes behaviour. The theory must be citable — if you cannot cite it, it is a hypothesis, not a theory
- **Current state:** how the CLO currently manifests — specific, observable, not general
- **Desired state:** the outcome state after the CLO is eliminated — stated as a completed state, not an activity

**Discipline:** theory and hypothesis are separate. The theory section contains only established, citable findings. The venture's design claim — why *this* specific approach will work — belongs in the Workaround Strategy (Sub-requirement 4).

**Diagnostic questions:**
- Why does this CLO exist? What does it solve for in the current BFF?
- Why is it so costly? What makes the cost inherent to this operation?
- Who else deals with similar structural problems in other industries? How have they managed it?
- What academic or practice literature addresses this class of problem?
- What is the minimal sufficient intervention — not a feature, but a change in the logic of the operation?

**Use `/theory-of-change-custom` for the full guided process.** When scoping, tell it: "R1 Workaround." It will produce a named **Workaround Theory of Change** using the CMO structure (Pawson & Tilley, 1997), enforce the theory/hypothesis distinction at each step, and output the four fields in BALM-ready format.

---

### Sub-requirement 4: Workaround Strategy

> *The best way to operationalize the Workaround Theory of Change to neutralise or eliminate the need for the Critical Limiting Operation.*

**What it is:** The best way to operationalise the Workaround ToC to neutralise or eliminate the need for the CLO.

**Critical framing:** state this as a *strategy*, not a product feature. The Workaround Strategy gives the logic of the intervention — the next step is to productize it. Jumping to a product feature at this stage conflates architecture with implementation.

**The architectural decision test:** a Strategy answer names the single structural decision that makes the Theory of Change fire in this specific venture context — not a description of what will happen as a result. Operational consequences (what will happen if the strategy works) are evidence the strategy is correct; they are not the strategy itself. Ask: "Is this an architectural decision, or a description of outcomes?" If the answer lists what will happen rather than naming the structural move that causes it, the strategy has not been found.

The Workaround Strategy becomes the R1 component of the new BFF. It is the architectural-level decision — everything else follows from it.

**The elegance test:** a strong Workaround Strategy does more than one thing simultaneously. Grameen's joint liability mechanism eliminated the CLO (individual credit assessment), improved repayment rates beyond what individual assessment achieved, and created a self-organising delivery mechanism — three effects from one structural move.

**Quality checks:**
- Does the strategy genuinely bypass or eliminate the CLO, or does it just reduce its cost incrementally?
- Is it stated as a strategy (a direction of intervention) rather than a product feature?
- Does it follow logically from the Workaround ToC?
- Could it plausibly shift the cost floor enough to create value surplus at the target price point?
- Does it require a new BFF — or could an incumbent adopt it without changing their architecture? (If the incumbent could do it too, it is not an R1 solution.)

**Use `/theory-of-change-custom` for the full guided Strategy process.** It produces the **Workaround Strategy** in the standard format: design choice + hypothesis + critical assumption. The elegance test in Steps 11 runs automatically.

---

### Sub-requirement 5: Business Form Factor (C1)

⛔ **REQUIRED OUTPUT CONTRACT — emit this block before writing BFF (C1). No BFF text is valid without it.**

```
CLO GATE — R1
cloZone: [Making / Selling / Delivering / Getting Paid]
cloName: [one-phrase name for the critical limiting operation]
cloIsOperationNotResource: true/false  ← false = you have named a resource/input/cost line (a noun you buy), not an operation (a process the business performs); go back and name the operation that requires it
cloStatedAsVerb: [the operation as a verb/process — e.g. "manufacturing each venture by trial-and-error"]
cloIsEssential: true/false  ← false = it is not tightly coupled to the BFF; go back and find the real CLO
cloEliminatesNotReduces: true/false  ← false = the workaround strategy only reduces cost; it does not restructure the BFF
workaroundStrategy: [one sentence — the architectural direction, not a product feature]
theoryGrounded: [citation] or "ungrounded — stop and find a citable theory before proceeding"
newBFFRequired: true/false  ← false = an incumbent could adopt this; it is not R1
cloAuditFlag: true/false  ← set true if cloIsOperationNotResource=false OR cloIsEssential=false OR cloEliminatesNotReduces=false OR newBFFRequired=false
```

If `cloAuditFlag: true` — stop. Do not write BFF (C1). Return to Sub-requirement 2 (CLO) and re-diagnose.

*The initial product form factor that productizes the Workaround Strategy — the minimum form that delivers the workaround as a self-executing mechanism embedded in the product, not as an operational function sitting alongside it.*

The Workaround Strategy names the intervention. Productizing it means shaping the product form factor so the mechanism is self-executing.

**Target product component:** Working Product (Making + Using)

Work through these three questions before writing the BFF:

**1. Architecture, not operations.** Is the workaround mechanism embedded in the product form factor, or does it require a separate operational function to execute? If a human activity delivers the mechanism, ask: what product design would make that activity unnecessary? Operational delivery is a cost that will appear in the AOM and compound at scale.

**2. Three-function check.** R1 sets the cost floor — but the form factor must support all three business functions: cost creation, exchange (sell, deliver, collect payment), and margin retention (the cost structure holds at scale). A BFF that solves R1 but creates downstream exchange or retention problems will surface in R2, R3, or the FIT Verifier.

**3. Simplicity test.** What is the minimum form factor that delivers the workaround? Complexity added at R1 propagates through all subsequent requirements. Eliminate anything that is not load-bearing.

**4. At-scale test.** Is this mechanism designed for the venture operating at capital-payback scale — the volume at which all required investment is paid back at the required IRR — or is it designed for the first cohort? A BFF that requires founding-team bandwidth, managed-by-exception operations, or pilot-only concessions is a launch-phase design, not an architecture. Name the at-scale volume explicitly. If the mechanism breaks before reaching it, return to Diagnose.

When all three are confirmed, identify the architectural spine before writing anything.

**Step 0 — Find the architectural spine.** The architectural spine is the single mechanism that runs through all prior requirements — the element whose removal would cascade failures across the most of C1 through C[N]. Every BFF has one. Finding it before writing forces the statement to be an architecture, not a list.

Diagnostic question: what would break first if you removed one core element from the design? The mechanism that cascades failures across the most requirements is the spine.

Write the opening sentence of the BFF around it. If the opening sentence could be "A product that does X (C1); does Y (C2); does Z (C3)..." — the spine has not been found. Go back and find it.

State the BFF (C1) — the initial form factor shape that R2 works with.

⛔ **MANDATORY HANDOFF — SR5 CONFIRMED. DO NOT EDIT THE VDR. DO NOT PROCEED TO R2.** The next and only permitted action is Section 5 (CTM Update). Announce explicitly: "SR5 confirmed. Running Sections 5–8 now before any VDR editing." Then proceed directly to Section 5.

---

## The R1 failure test

**"We'll be more efficient than the incumbent"** means you have not identified the CLO.

You are optimising within the existing BFF, not replacing it. Efficiency gains within a broken BFF produce incremental improvement, not value surplus. The test: does your solution require a *new* BFF, or could an incumbent adopt it without changing their architecture?

Blue Apron scaled the cold-chain delivery CLO rather than eliminating it. The P&L was structurally unworkable at any scale they reached. The venture raised $300m and never achieved profitability. WebVan spent $800m on the same bet with the same result.

Grameen eliminated the individual credit assessment CLO entirely — replacing it with a group-based social collateral mechanism. The BFF became unrecognisable relative to conventional banking. That is R1.

---

## Worked case — Lending to informal businesses

| Input | Content |
|-------|---------|
| **Conventional BFF** | Branch visit, agent evaluates creditworthiness via FICO score and tax returns, loan priced to reflect default risk, monthly repayments |
| **CLO** | Evaluating credit risk without FICO scores or tax returns dramatically increases due-diligence time and cost — and smaller loan sizes required by informal businesses make this cost structure entirely unworkable. Two compounding problems: assessment cost too high, loan size too low. Sits in: Making the product (risk assessment as part of underwriting) |
| **Class of problem** | Information asymmetry and individual-level risk. The lender cannot assess individual creditworthiness at a cost compatible with small loan economics |
| **Workaround ToC** | Behaviour change theory: peer pressure and peer support alter repayment behaviour (Bandura, 1977 — social learning; Ostrom, 1990 — collective action and self-governance). The group, not the bank, provides enforcement and social collateral |
| **Workaround Strategy** | Harness peer pressure and peer support to get borrowers to practise good repayment behaviour. Shift credit risk management from the lender to the peer group |
| **Productized R1** | Joint liability peer group loan: borrowers form groups and take on shared liability for individual loans. Social pressure within the group replaces individual credit assessment by the lender |

---

## Worked case — Automotive (Henry Ford)

Automotive technology was being sold before Ford — but only to the wealthy, at approximately £1,500 (equivalent). The conventional BFF (hand-crafted manufacture) created a cost floor that excluded the mass market entirely. Ford did not improve the existing BFF — he invented a new one: assembly-line manufacturing. This shifted the cost floor from £1,500 to approximately £300 while multiplying production volume simultaneously. That is the R1 intervention — not "more efficient craftwork," but a new architecture that makes the old cost floor irrelevant.

---

## R1 output format

```
SUMMARY
  Workaround Strategy: [strategy in one sentence — the architectural direction]
  Bottleneck eliminated: [CLO in one phrase]
  Grounded in: [named theory]
  BFF change required: [Yes / No]

R1 — AT-SCALE COST BOTTLENECK
---
CONVENTIONAL BUSINESS FORM FACTOR
  Making the product: [How]
  Selling the product: [How]
  Delivering the product: [How]
  Getting paid: [How]

CRITICAL LIMITING OPERATION
  Zone: [Making / Selling / Delivering / Getting Paid]
  Description: [What the operation is and why it is essential to the conventional BFF]
  Cost mechanism: [Why the cost is inherent to this operation]
  Cost threshold: [What it costs relative to target customer's ability to pay]

WORKAROUND THEORY OF CHANGE
  Class of problem: [Named mechanism]
  Theory: [Citation — peer-reviewed, citable]
  Current state: [Specific and observable]
  Desired state: [Completed state after CLO is eliminated]

WORKAROUND STRATEGY
  [One to three sentences — the architectural direction, not the product feature]

CONSIDERED / NOT CHOSEN (VA-4 — show your working)
  Workaround Strategies considered:
    A. [strategy] → [why it could work] → [adopted / rejected because…]
    B. [strategy] → [why it could work] → [adopted / rejected because…]
  Decision: [why the chosen strategy won]

BUSINESS FORM FACTOR (C1) — FIRST CUT
  [minimal form factor — the architectural spine in one sentence]
  Note: first cut — R2–R10 may rewrite this, including fundamentally.

SYNTHESIS CHECK (VA-1)
  Real-business analogue: [looks like [business], because [mechanism] — or "synthesis not yet earned"]

R1 QUALITY CHECK
  Does the strategy eliminate (not reduce) the CLO? [Yes / Partial / No]
  Does it require a new BFF? [Yes / No — if No, it is not R1]
  Does it pass the elegance test? [Yes / No — does it do more than one thing?]
  Confidence: [High / Medium / Low]
  What would increase confidence? [One specific check]
```

---

## Relationship to other BALM requirements

**Sequence:**
- **PCO** (prerequisite) → defines the opportunity R1 is solving for
- **R1** → sets the cost floor via the Workaround Strategy
- **R2** → sets the value ceiling; must start from a productized R1
- **R3** → addresses the balance sheet (working capital) problem during scaling; distinct from R1's P&L focus

**R1 vs R3 distinction:** R1 addresses at-scale operating costs — what the business costs to run at steady state, reflected on the P&L. R3 addresses working capital — the cash required to bridge the gap between expenditure and revenue during the growth phase, reflected on the balance sheet. A business can have a sound R1 and still fail at R3 if the scaling architecture requires prohibitive upfront capital before revenue arrives.

**R3 design principle — cost-shifting is not architecture.** The same standard that applies to R1 applies to R3: the solution must require a new BFF, not just redistribute an existing cost. Transferring the working capital burden to investors, lenders, or partners reduces exposure but creates no new value — any incumbent could do the same. A genuine R3 solution transforms the working capital constraint into a mechanism that creates value for someone. The Grameen analogy: peer liability didn't just reduce the cost of credit assessment — it created a new mechanism that also improved repayment rates. New value from a new architecture. If the proposed R3 strategy could be described as "we found someone else to hold the cost," it is not yet R3.

**All R requirements are architected for at-scale, not for launch.** The question is never "how do we solve this in year one?" — it is "what is the architecture that works when the venture is operating at the scale required to pay back all required investment capital at a competitive rate of return?" Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the R3 design. A regulatory cost that seems large at 50 claims is trivial against the working capital requirement at 10,000 claims. Architect for the scale that makes the economics work; sequence the build accordingly.

**Cross-requirement elegance — a general IVE design quality.** A strong solution to any requirement does more than solve that requirement. The highest-quality architectural moves serve multiple requirements simultaneously — the same structural change that addresses R3 (balance sheet) also advances R2 (value ceiling); the same move that solves R1 (cost floor) also helps R4 (customer doubt). This is not accidental: requirements often share a common underlying bottleneck (a credible value signal, a trusted relationship, a standardised process). When a single mechanism resolves more than one requirement, it is both harder to copy and more powerful in aggregate than a requirement-specific fix. The Grameen analogy again: joint liability solved R1 (eliminated credit assessment cost), improved R2 efficacy (higher repayment rates), and helped R3 (no capital reserve needed for default provision). Ask at each requirement: does this mechanism also touch any other requirement? If not, look harder — the best solutions usually do.

---

## Optimisation intent

The gate is a floor, not a ceiling. Given everything built so far, use this requirement's framework to create the most efficacy for the target customer outcome and remove the most cost — i.e. increase the financial margin of safety. The goal is the most architecturally efficient solution: the highest ratio of customer value and FMOS improvement to complexity added. A passing answer leaves value on the table.

After arriving at any answer, ask: is there a simpler version of this mechanism that does the same work with less architectural complexity? Reduce to the minimum load-bearing form before closing the requirement.

---

## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)

Reference: `method/context/va-design-discipline.md`

R1 originates the Business Form Factor — so the discipline here is mostly **under-specification**, to keep the BFF open for the nine challenges that follow.

**VA-3 — keep the C1 BFF minimal.** The BFF (C1) is a *first cut*, not a finished design. State the smallest form factor that productizes the Workaround Strategy and nothing more. Do not specify features, segments, pricing, or mechanisms that a later challenge will earn. A heavy, fully-formed BFF at R1 is premature design (VA-2) and forces every later challenge into justification mode — defending the R1 BFF instead of beating it. End the BFF (C1) with the explicit line: "first cut — R2–R10 may rewrite this, including fundamentally."

**VA-1 — synthesis test.** When the BFF (C1) is stated, anchor it: "this now looks like [real business], because [shared mechanism]." A first cut may have no clean analogue yet — that is fine; flag it as "synthesis not yet earned" rather than forcing one.

**VA-4 — show your working.** If more than one Workaround Strategy was considered, record the alternatives and why this one was chosen in the "considered / not chosen" block — even at R1.

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

This governs the *rendered document*, not the method: sub-requirement definitions quoted from this skill stay verbatim, theory citations keep their original titles, and the internal working notes may stay in normal register. Reference example: `ventures/Education/education-venture-design-record-2026-08-17.html`.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-challenge-1-custom/SKILL.md` to modify
- **Skill chain:** `/balm-pco-custom` (PCO) → `/balm-challenge-1-custom` (R1) → `/theory-of-change-custom` (Workaround ToC + Workaround Strategy, invoked as R1) → `/balm-challenge-2-custom` (R2)
- `/theory-of-change-custom` is the shared ToC tool across all requirements — invoke it with "R1 Workaround" to produce correctly named output
- IVE source: Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–August 2025
- Grameen cases: Yunus, M. (1999). *Banker to the Poor.* Public Affairs
- Collective action theory: Ostrom, E. (1990). *Governing the Commons.* Cambridge University Press

---

## Integrated Model Build & FIT Gate

> **🧍 PROPERTY-HOLDER TEST (VA-71, mandatory before the CTM update — added 1 Sep 2026).** Read the workaround (or this challenge's strategy) and the requirement back, and name every property they assert — watch for: *credible · trusted · willing · convinced · perceives · believes · finds it rational · treats it as*. Each names a state inside a person. For each property, name the actor who holds it. If that actor is not the customer, they get a `user_tracks` (or `partner_tracks`) entry in the CTM, and every transition on it is carried by a product component or explicitly flagged with the reason. **A property asserted and not carried to its holder is a relocated bottleneck, not an eliminated one.** (Found on Calmly C1: "credible litigation backstop" — credibility is held by the defendant, and no product reached the defendant for three months.)

> **🧮 FIT-STALENESS RULE (VA-74, Tom's ruling 1 Sep 2026: "the check is always the FMOS of the product").** The FIT gate's check is measured against the venture's whole cost structure and value ceiling — the FMOS — never against a narrower stack. The FIT block must record the **component set it was computed on** (the CTM roster at computation time). If this challenge's component set changes on any later run — a component added, removed or re-carried — the FIT verdict is **stale by definition**, the challenge's Complete status is suspended, and the FMOS is recomputed against the new set before Complete can be restored. Adding a component and leaving the FIT verdict untouched is the recorded failure this rule exists to stop.


These sections run after the BALM diagnostic work above is confirmed. They make R1 self-contained: it builds/updates the CTM and AOM, updates the financial model, and runs the FIT gate before marking R1 complete.

**Model file naming convention — challenge-labeled, not version-numbered.**

Every model file is named by the challenge it reflects, not by an incrementing version number. The format is:

| Model | Filename convention | Example |
|-------|-------------------|---------|
| CTM | `[venture]-ctm-at-C[N].html` | `calmly-ctm-at-C1.html` |
| AOM | `[venture]-aom-at-C[N].html` | `calmly-aom-at-C1.html` |
| Fin-Sim | `[venture]-fin-sim-at-C[N].html` | `calmly-fin-sim-at-C1.html` |

When updating a model for challenge N: copy the prior challenge file (`at-C[N-1]`) to a new `at-C[N]` file, apply the targeted edits, and save. The prior version is preserved unchanged. Do not use version numbers (v1, v2, v6) — they convey no information about which architectural state the model reflects.

If a prior file uses version-number naming, rename it to challenge-labeled naming before editing. The canonical naming is `at-C[N]`.

### Section 5 — CTM Update *(gate: strategy confirmed)*

⛔ **HARD GATE — do not update the VDR until Sections 5–8 are complete.** Confirm CTM, AOM, Fin-Sim, and FIT gate are done before editing any VDR content. This gate exists because skipping Sections 5–8 and going straight to VDR editing is a known failure pattern (logged WS1, 4 June 2026).

Ask the user:
- "What product component does the Workaround Strategy add or change?"
- Which CTM phase does it affect? **Phase 2 — Consuming (core delivery)**
- Which 4-D product delivers it? **Working Product**
- What is the specific element? (e.g. "a joint liability peer group that substitutes for individual credit assessment")
- What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)

**R1 only — create the CTM from scratch** by writing the first `[venture]-ctm-model-at-C1.yaml` and generating the views (Execution route below; do NOT invoke `/ive-ctm-custom` — deprecated). The CTM starts with standard industry practice; R1's Workaround Strategy is the first override. The CLO row is replaced by the Workaround mechanism in Phase 2.

**Catch-up mode:** If the user indicates the CTM does not yet exist (because prior challenges were run without this integrated structure), build it now from the confirmed R1 strategy before proceeding. If R2 or beyond is already solved, build the CTM retrospectively from all confirmed strategies for completed challenges, then update for the current one.

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
- Which stream? **Making + Using**
- Which level? (LMU / Territory / HQ)
- What role delivers the Workaround mechanism?
- How long does it take per unit?
- What is the volume driver? (per unit / per inquiry at X% conversion / per stage at Y% probability / fixed per LMU)

**Check for common errors before writing:**
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if the delivery role requires supervision or QA?
- Has a new HQ function been added if the workaround requires central support?

**LMU sizing check:**
1. Is this LMU large enough to be economically viable? (Enough volume to cover fixed LMU costs?)
2. Is this LMU small enough to replicate fast? (Can we stand up another one in weeks, not months?)
If both YES → PASS. If either NO → FLAG before proceeding.

**R1 only — create the AOM from scratch** (LMU level first). The AOM starts blank; R1's Making + Using activities are the first entries.

**Catch-up mode:** If the AOM does not yet exist, build it retrospectively from all confirmed strategies for completed challenges before updating for R1.

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
   - **Making/Using streams at HQ level** → drives fixed overheads
   - **Timing of activities relative to revenue** → drives working capital (cash committed before revenue lands)

2. Update the financial simulation with the new activity costs and timing.
   - If a fin-sim exists for this venture: update the relevant cost lines. Do not rebuild the whole model.
   - If no fin-sim exists: flag it — prompt the user to run `/ive-fin-sim-custom` before continuing.

Before proceeding to Section 8, confirm the fin-sim reflects the updated AOM.

---

### Section 8 — FIT Verifier Gate *(gate: fin-sim updated)*

Run the financial margin of safety calculation across all four cost layers. FMOS calculated on fewer than four layers is always too optimistic. Display it in this format:

```
COST FLOOR — four-layer breakdown        £/unit

  PVC  (cost of goods per unit)          £[X]
  RC   (labor + operating costs)         £[X]
  SC   (CapEx + dev + acquisition)       [REQUIRES R3]   ← not yet designed; flag as gap
  IC   (WC for customer financing        £[X]
        = PVC × (rate/12) × avg months)
  ─────────────────────────────────────────────
  COST FLOOR (PVC + RC + IC only)        £[X]   ← SC excluded until R3

REQUIRED PRICE (25% FMOS)               £[Y]   ← cost floor × 1.25
PRICE CEILING (preliminary = WTP_low)   £[Z]   ← PCO estimate; definitive at R2

HEADROOM                                £[W]   ← ceiling minus required price
FMOS                                    [X]%   ← (WTP_low − Cost_high) ÷ Cost_high

⚠ SC layer not included — FMOS is indicative only until R3 is solved.

VERDICT: [PASS / BORDERLINE / FAIL]
```

1. **Use the correct FMOS formula — cost denominator.** `FMOS = (WTP_low − Cost_high) / Cost_high` (Simanis, *Built to Hold*, p.7). Do **not** use `(Price − Cost) / Price` (gross-margin / price-denominator) — it is a different, incompatible metric and understates the figure. WTP_low = the price ceiling (R2 KMC; preliminary PCO estimate at R1); Cost_high = the cost floor (AOM high-point unit cost).

**For R1:** Price ceiling is not yet defined — use a preliminary estimate from PCO (what the target customer can pay) as WTP_low. Note the result is indicative until R2 defines the KMC, and again until R3 adds the SC layer.

**Verdicts (cost-denominator FMOS):**
- **PASS (≥25%):** Proceed to Section 9.
- **BORDERLINE (25–59% at full model; treat 15–24% as the early-warning band here):** Surface the conditions. Ask user: accept and proceed, or revise? If they accept, note the conditions as critical assumptions.
- **FAIL (<25%, early-warning <15%):** Return to Section 2 (CLO diagnosis). State which lever is off: cost floor too high, or price ceiling too low.

**Theory robustness check (embedded in FIT):**
Ask: "What is the named theory grounding the Workaround Strategy? Name the mechanism and the precedent."
- If named + replication precedent exists → T: PASS
- If named but replication uncertain → T: FLAG (replication risk)
- If no named precedent → T: FLAG (untested)
- If no theory at all → T: FAIL (return to Section 4)

---

### Section 9 — Status Output

State clearly:
- What was created or updated: CTM (which rows), AOM (which activities, which level), fin-sim (which cost lines)
- Current FMOS and verdict
- Mark **R1 complete** (or fail) on the status board
- Route to **R2** (Eliminate Customers' Value Bottleneck)

### WS1 Feedback Capture *(optional — prompted at every close)*

Before routing, ask:

> "Quick WS1 capture? (y / skip)"

If **y**, ask these four questions in sequence and append the responses to `FEEDBACK.md` using this format:

```
---
## R1 · [venture name] · [date]

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
