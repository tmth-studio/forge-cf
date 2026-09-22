---
name: architect-custom
description: Architect a venture end-to-end with the IVE process. The single front door for IVE/BALM design and review — orients to where the venture sits, drives the five phases (Frame → CLO/seed → Architect → Converge → Verify), enforces the criteria registry at every gate, and ends with an integrity score. Routes to the phase skills; never short-circuits them.
---

# Architect — the IVE front door

**Purpose:** Orchestrate the IVE design process. Read the current state of the venture's BALM design memo, diagnose where it sits in the sequence, surface the right next skill, and hold institutional memory of design principles developed across sessions.

This is not a design skill itself. It does not generate architecture. It knows the sequence, reads the state, and routes correctly.

**Invoke with:** `/architect-custom [venture name]` — with no argument to get a status + routing recommendation, or with a venture name to focus on a specific project.

**Relationship to `/ive-design-loop-custom`:** This skill reads state and routes. `/ive-design-loop-custom` enforces the Diagnose → Theorize → Productize → Simulate loop within each requirement and gates progression on the FIT Verifier. Use `/architect-custom` to orient; use `/ive-design-loop-custom` to work. When routing to requirement work, always direct to `/ive-design-loop-custom` rather than a BALM skill directly.

---

## How to run this — the v2 process

This skill is the front door. The user invokes it; it conducts. **Load these two specs before routing, and enforce them throughout:**

- **The flow:** `04-Projects/TMTH_Venture_Studio/Forge/WS1/architecture-process-flow.html` — the five phases and what each does, and *why* (CLO-as-spine, synergy-as-objective, the conformity guard).
- **The criteria registry:** `04-Projects/TMTH_Venture_Studio/Forge/WS1/criteria-registry.md` — the objectively-verifiable test (Tier-1 mechanical or Tier-2 anchored-rubric) for **every** mini-output. **This is the referee.**

**The session experience:** the user names a venture. Orient (new → Phase 0; existing → resume at the current phase), then drive phase by phase, routing to the sub-skill for each step. At every mini-output, check its registry criterion. **Do not pass a gate that fails its criterion — return to the step.** The run ends at Phase 4 with `/verify-venture-custom` and an integrity score.

**Enforce the three v2 criteria the older pipeline lacked:**
1. **Synergy** — in every requirement, seek the move that also solves an *earlier* requirement; the finished architecture must contain ≥1 move solving ≥2 requirements (the moat test). A requirement that generates zero synergy candidates has defaulted to local optimisation — flag it.
2. **Conformity guard** — reject only "wrong because incoherent." Never penalise "wrong because it breaks the conventional CBA" — that is the signal the architecture is working (Simanis: the right form factor looks wrong by conventional standards).
3. **Convergence routing** — if Phase 3 finds no real-business analogue or any hard contradiction, route back to generation; do not patch.

**FMOS gates:** the canonical two-gate scheme lives in the criteria registry — per-requirement PASS ≥ 25%, Phase II gate PASS ≥ 60%. Do not use any other bands.

**Two modes:** *interactive* (the user in the loop, confirming each gate — this skill) and *autonomous* (the CF runner fires the same flow, stopping only at the irreducible human points: PCO confirm, objective/gate change, final sign-off).

---

## The IVE sequence — full map

```
PCO — Prime Commercial Opportunity
│     Skill: /balm-pco-custom
│     Output: target customer, high-import outcome, CLO, PCO statement
│     Gate: PCO confirmed before any architecture work begins
│
├── Architecture Generator                            [before R1]
│   Skill: /ive-architecture-generator-custom
│   Input: CLO from PCO
│   Output: ranked Workaround Strategy candidates with theory + elegance scores
│   Gate: candidate chosen before R1 design begins
│
├── Research Design                                   [after R1, before fieldwork]
│   Skill: /ive-research-design-custom
│   Input: PCO + chosen Workaround Strategy
│   Output: unified fieldwork protocol covering R2 (KMC) + F2 (block classification)
│   Note: run before R2 fieldwork — eliminates two separate research waves
│
├── F1 — Neutralise the Value Barrier
│   │   Wrapper: /ive-design-loop-custom (enforces gate on every requirement)
│   │
│   ├── R1: Circumvent At-scale Cost Bottleneck       [P&L — cost floor]
│   │   Skill: /balm-challenge-1-custom
│   │   Then: /theory-of-change-custom (invoke as "R1 Workaround")
│   │   Then: Write Workaround Strategy (operationalise the ToC)
│   │   Then: CTM create (/ive-ctm-custom) + AOM create (/ive-aom-custom)
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │   Output: CLO, Workaround ToC, Workaround Strategy
│   │
│   ├── R2: Eliminate Customers' Value Bottleneck     [value ceiling]
│   │   Skill: /balm-challenge-2-custom
│   │   Then: /theory-of-change-custom (invoke as "R2 Efficacy")
│   │   Then: Write Efficacy Strategy (operationalise the ToC)
│   │   Then: CTM update + AOM update
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │   Output: KMC, Efficacy ToC, Efficacy Strategy, price ceiling
│   │
│   └── R3: Circumvent Scaling Cost Bottleneck        [balance sheet / working capital]
│       Skill: /balm-challenge-3-custom
│       Then: /theory-of-change-custom (invoke as "R3 Scaling")
│       Then: Write Scaling Strategy (operationalise the ToC)
│       Then: CTM update + AOM update (cost-of-goods structure)
│       Then: /ive-fit-verifier-custom — PASS required to proceed
│       Output: CLO II, Scaling ToC, Scaling Strategy
│
├── F2 — Normalise the Customer Routine
│   │   Wrapper: /ive-design-loop-custom (enforces gate on every requirement)
│   │
│   ├── R4: Circumvent Customer Doubt about Value     [Want Block]
│   │   Skill: /balm-challenge-4-custom
│   │   Then: Write Attraction Strategy (operationalise the ToC)
│   │   Then: CTM update (Phase 1 / Conviction) + AOM update (Selling stream)
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │
│   ├── R5: Eliminate the Biggest Learning Disruption [Use Block]
│   │   Skill: /balm-challenge-5-custom
│   │   Then: Write Adoption Strategy (operationalise the ToC)
│   │   Then: CTM update (Phase 2 / Activation) + AOM update (Using stream)
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │
│   ├── R6: Circumvent the Cash Flow Constraint       [Buy Block]
│   │   Skill: /balm-challenge-6-custom
│   │   Then: Write Amortization Strategy (operationalise the ToC)
│   │   Then: CTM update (Phase 3 / Payment) + AOM update (Using stream)
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │
│   └── R7: Activate Gateway Partners
│       Skill: /balm-challenge-7-custom
│       Then: Write Partner Activation Strategy (operationalise the ToC)
│       Then: CTM update (Phase 1 / Awareness + partner CTM) + AOM update (Selling stream)
│       Then: /ive-fit-verifier-custom — PASS required to proceed
│
├── F3 — Lock In the Market Position
│   │   Wrapper: /ive-design-loop-custom (enforces gate on every requirement)
│   │
│   ├── R8: Create a Switching Cost
│   │   Skill: /balm-challenge-8-custom
│   │   Then: Write Lock-in Strategy (operationalise the ToC)
│   │   Then: CTM update (Phase 2 accumulation + Phase 4) + AOM update
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │
│   ├── R9: Manufacture a Resource Moat
│   │   Skill: /balm-challenge-9-custom
│   │   Then: Write Lock-out Strategy (operationalise the ToC)
│   │   Then: CTM update (Phase 4) + AOM update (Making stream)
│   │   Then: /ive-fit-verifier-custom — PASS required to proceed
│   │
│   └── R10: Manufacture Replaceability of the Key Supplier Input
│       Skill: /balm-challenge-10-custom
│       Then: Write Leverage Strategy (operationalise the ToC)
│       Then: CTM update (Phase 4) + AOM update (all streams)
│       Then: /ive-fit-verifier-custom — PASS required to proceed
│
├── Full financial simulation                         [after all 10 requirements]
│   Skill: /ive-aom-custom (produces Group 4 feed) → /ive-fin-sim-custom
│   Gate: FMOS ≥ 60% (conservative scenario) before Phase II capital committed
│
└── Consistency Audit                                 [final gate]
    Skill: /ive-consistency-audit-custom
    Input: all 10 requirement solutions
    Output: dependency matrix, contradictions diagnosed, routing to resolution
    Gate: PASS before architecture is finalised
```

**Supporting skills:**
- `/ive-design-loop-custom` — **use this for all requirement work** — enforces Diagnose → Theorize → Productize → Simulate and gates every requirement on FIT Verifier
- `/ive-architecture-generator-custom` — cross-domain analogue search, before R1
- `/ive-ctm-custom` — Customer Transformation Model (create at R1, update after each requirement)
- `/ive-aom-custom` — At-Scale Operational Model (create at R1, update after each requirement)
- `/ive-fin-sim-custom` — Financial simulation (updated continuously via AOM feed; full rebuild after all 10)
- `/ive-fit-verifier-custom` — FIT gate after every requirement (25% FMOS each time; 60% final gate)
- `/ive-research-design-custom` — unified fieldwork protocol (run after R1, before R2 fieldwork)
- `/ive-consistency-audit-custom` — cross-requirement dependency check (run after R10)
- `/verify-balm-custom` — BALM completeness audit (checks fields present, not consistency)
- `/theory-of-change-custom` — ToC for any requirement (name it: R1 Workaround / R2 Efficacy / etc.)

---

## Challenge completion protocol

**Sub-requirements being filled is necessary but not sufficient. A challenge is not complete until all five conditions are met:**

1. **Sub-requirements** — every SR in the challenge is filled and confirmed ✓
2. **CTM updated** — the Customer Transformation Model reflects the mechanisms established in this challenge (create at R1; update at every subsequent requirement)
3. **AOM updated** — the At-Scale Operational Model reflects any new operational requirements from this challenge (create at R1; update at every subsequent requirement)
4. **Financial simulation updated** — the sim reflects the new cost floor and/or value ceiling established by this challenge
5. **FIT Verifier PASSED** — `/ive-fit-verifier-custom` has been run against the architecture as it now stands, using the updated cost floor and price ceiling, and returned a PASS or confirmed BORDERLINE verdict

**Why this matters:** The FIT check is the test of whether the architecture as built can generate value surplus. A challenge whose sub-requirements are filled but which fails the FIT check has not solved the underlying problem — it has produced a design that cannot pay for itself. The challenge must return to redesign, not advance.

**The design memo may mark challenges ✓ based on sub-requirements alone. This is not the definition of complete.** When diagnosing venture state, check all five conditions for each challenge marked ✓. A challenge with filled sub-requirements but no FIT PASS is `~ (pending FIT)`, not complete.

**Implication for routing:** If sub-requirements are filled but the FIT check has not been run or has not passed, the correct next action is not to start the next challenge — it is to run `/ive-fit-verifier-custom` for the current challenge and resolve any fail diagnosis before proceeding.

---

## Step 1 — Read current venture state

When invoked, immediately read the venture's **authoritative** design record (never a stale memo).

- **Calmly:** follow the reading order in `04-Projects/Family_High_Performance/context/ceo-calmly-resolve-memory.md` — canonical VDR is `04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-venture-design-record-v12-2026-09-01.html` (or the highest version number present in that folder). Do not read `calmly-design-memo.html` (flagged stale).
- **Other ventures:** ask for the workspace/design-record path, or look in `04-Projects/{venture}/`.

Scan for:
- Which requirements have ✓ (complete), ~ (partial), or are blank
- For each ✓ requirement: confirm all five completion conditions are met — sub-requirements, CTM updated, AOM updated, fin-sim updated, FIT Verifier PASSED. A ✓ based on sub-requirements alone is incomplete — reclassify as `~ (pending FIT)` if the FIT check is missing or failed
- Any open-note warnings (`⚠ Open`)
- The BFF statement — is it draft or confirmed?
- The FIT Verifier status — has it been run for the *current* challenge? A FIT check from a prior challenge does not cover new challenges added since
- Any design session notes indicating work in progress

Report the status in a compact table before making any recommendation. For each requirement, show: sub-reqs, CTM, AOM, fin-sim, FIT — five columns. This is the only reliable way to see where the venture actually is.

---

## Step 2 — Diagnose and route

Based on the status scan, identify:

1. **Where the venture is in the sequence** — which requirement is next
2. **What is blocking progress** — open questions, missing inputs, unrun skills
3. **What the recommended next action is** — one skill, one step

**FIT check routing rule:** If the current challenge has filled sub-requirements but no FIT PASS, do not route to the next challenge. Route to `/ive-fit-verifier-custom` for the current challenge. The FIT check is not optional and is not a separate audit step — it is part of completing the challenge. The CTM and AOM must be updated *before* the FIT check is run, since the FIT check uses the cost floor and value ceiling derived from those models.

State the recommendation clearly:

> "You are at [position]. The next step is [skill] because [reason]. Before running it, you need [prerequisite if any]."

Do not recommend multiple parallel tracks unless F1 is confirmed complete (all three requirements with FIT PASS). One thing at a time.

---

## Step 3 — Surface relevant context

Before launching any skill, surface the design principles that apply to the next step. Pull from the Institutional Memory section below.

Example: if the next step is R3 design, surface:
- The rocket framing (at-scale architecture vs scaling architecture)
- The R3 elegance test (does this also advance R2?)
- The cost-shifting is not architecture principle

---

## Step 4 — Launch the skill

Ask: "Ready to run [skill]?" and on confirmation, invoke it.

Pass any relevant context as arguments so the skill starts with full awareness of where the venture is.

**Critical discipline — do not skip sub-requirements by producing answers directly.**

The conductor is a router, not a designer. When the next step is a BALM challenge skill (e.g. `/balm-challenge-3-custom`), the conductor must invoke that skill and let it run its structured sub-requirement dialogue. It must NOT:
- Summarise what the answer "probably is" based on prior context
- Fill in sub-requirements itself before launching the skill
- Present a completed challenge design as if the skill had been run

The BALM skills exist precisely because each sub-requirement must be worked through in sequence — each one gates the next, and the user must confirm each before proceeding. A conductor that short-circuits this produces outputs that look complete but have not been interrogated. Those outputs will fail the FIT check.

**The rule:** if the next action is a challenge design skill, invoke it. Do not paraphrase its output in advance. Do not pre-fill its sub-requirements. Launch it and let it run.

This applies equally to `/ive-fit-verifier-custom`, `/ive-ctm-custom`, `/ive-aom-custom`, and `/theory-of-change-custom` — each of these has its own structured process that must be run, not approximated.

---

## Institutional Memory

Design principles and insights developed across sessions. Apply these when routing and when introducing skills.

---

### The rocket framing — at-scale architecture vs scaling architecture

**Established: 16 May 2026, IVE design session (Calmly C3)**

IVE designs two distinct architectures, not one:

**At-scale architecture** — the satellite. The venture operating permanently at the scale required to pay back all investment capital at a competitive rate of return. This is what every IVE requirement is designed for. It assumes the scaling mechanisms are already in place and operational (securitisation running, modules at capacity, full partner network active). This is the primary design — the destination.

**Scaling architecture** — the rocket stages. The temporary structures designed to get the venture to orbit without running out of capital on the way. Each stage has different economics. Each stage falls away once it has served its purpose. The scaling architecture is not a compromise version of the at-scale architecture — it is a separate engineering problem.

R3 is the rocket problem. R3 asks: how does the venture reach at-scale without the working capital requirement killing it during the journey? The at-scale architecture assumes the R3 solution is already operational. The scaling architecture designs the sequence of stages that make that transition possible.

**Applied to Calmly** *(illustrative, superseded lineage — operative model is the 6 June Lloyd's / network-operator per-transaction B2B fee model; see the SUPERSEDED LINEAGE banner under "Calmly — current design state" below):*
- At-scale architecture: exchange model (pool operators bear litigation risk, Calmly earns platform fee), LMU specialists at scale, 18,000+ claims/year — FMOS 63.6% (four-layer, 19 May 2026)
- Scaling architecture: Stage 1 (litigation funder capital 25-30%, 1 cohort, 40 claims/month), Stage 2 (specialist debt 15-18%, 5+ cohorts, portfolio history building), Stage 3 (securitisation operational, transition to at-scale complete — booster falls away)

**Implication for the simulation:** two clearly separated models. At-scale architecture is the primary model. Scaling architecture is a stage-gate model asking: what does the venture need to survive at each stage before the next mechanism fires?

---

### Each challenge must be applied in full — prior outputs are inputs, not substitutes

**Established: 19 May 2026**

Every challenge framework must be applied maximally and independently, regardless of how much earlier challenges appear to have addressed the current requirement. The intent of each challenge is maximisation: given the current BFF, how do we use this requirement's framework to extract the most value and remove the most cost? A previous challenge's output that happens to help with the current challenge is an architectural bonus — not a reason to abbreviate the diagnostic work.

**The error to avoid:** treating cross-requirement elegance as a shortcut. If C3's independent assessment org addresses part of the R4 Want Block, that is good architecture — but R4's full diagnostic still runs. R4 may surface additional conviction mechanisms C3 didn't cover. The elegance is in the overlap, not in the omission of R4.

**Rule:** run every challenge's sub-requirements in full, in sequence, using prior challenge outputs as starting context. Never skip or abbreviate a challenge because an earlier mechanism appears sufficient. The framework exists to find what you haven't found yet.

---

### Cross-requirement elegance — a general IVE design quality

**Established: 16 May 2026**

The highest-quality architectural moves serve multiple requirements simultaneously. When designing any requirement, ask: does this mechanism also touch any other requirement?

The Grameen analogy: joint liability solved R1 (eliminated credit assessment cost), advanced R2 (higher repayment rates), and helped R3 (no capital reserve needed for default provision). One mechanism, three functions.

For Calmly: the pre-trial bundle does triple duty. R2 (disrupts defendant motivated reasoning → early settlement), R3 (investor-grade EV assessment → securitisable portfolio), adverse selection (defendant's own engagement independently verifies Calmly's valuation). One mechanism, three functions.

**Diagnostic question at every requirement:** does this mechanism also touch any other requirement? If not, look harder — the best solutions usually do. But note: discovering that a prior mechanism also touches the current requirement is not the end of the diagnostic — it is the start. The full challenge framework still runs.

---

### The operating module — unit vs module distinction

**Established: 16 May 2026**

The unit of transaction (one claim resolved) is not the same as the operating module (the structure that gets replicated when the venture scales). Every IVE financial simulation must anchor to the operating module, not just the transaction.

The module has a capacity ceiling. Fixed costs are module-level costs amortised across transactions. The primary intrinsic performance curve for module-based ventures is: fixed cost per unit falls as capacity utilisation rises.

For Calmly: one module = 6 law students + 1 supervising solicitor, capacity ~40 claims/month. At-scale = ~38 modules. Fixed module cost at capacity: £45/claim. At 50% utilisation: £90/claim.

**Implication:** F2 customer acquisition design must be sized to fill modules, not just grow claim volume.

---

### Source discipline — assume and note, audit later

**Established: 16 May 2026**

Every assumption and data point in the simulation carries a traceable source (Tier 1–4). Do not block design work on missing sources. Make the most defensible assumption, state the rationale, tag it Tier 4, and move on. Source validation is a separate audit step.

**Source tiers:**
- Tier 1: Primary data from this venture's own field research or operations
- Tier 2: Published statistics (government data, regulatory publications, academic studies)
- Tier 3: Industry benchmark (named expert, comparable venture)
- Tier 4: Reasoned assumption (no external source — must state the logic)

**Key Tier 4 assumptions in Calmly simulation (16 May 2026):**
- Average disputed amount: £3,000 (Ipsos Mori 2016 research task spawned)
- Purchase price: 40% of face value (FIT Verifier determination — needs field validation)
- Module capacity: 40 claims/month (law clinic research task spawned)
- Securitised cost of capital: 8% (cost of capital research task spawned)
- Waterfall cohort splits: all Tier 4 except court win rate (Tier 3 — SCS Law partner)

---

### CMO framing — Theory of Change structure

**Established: 15 May 2026**

All Theories of Change in IVE use the CMO structure (Pawson & Tilley, 1997):
- **Context:** the conditions that enable the mechanism to fire — not a description of the current situation, but the specific conditions that make this group susceptible to this mechanism
- **Mechanism:** how participants reason and react when they encounter the resource — not the intervention itself, but the generative causal process
- **Outcome:** the proportionate, observable change that results when the mechanism fires — not the aspiration, but the specific pattern of change this mechanism produces

Theory and hypothesis are separate. Theory = peer-reviewed, citable. Hypothesis = the design claim about why this specific approach will work. They belong in different fields.

Reference: `/theory-of-change-custom` and `06-Resources/Methodology/pawson-tilley/dossier.md`

---

### AOM/fin-sim reconciliation — exchange model cost principle

**Established: 19 May 2026 (Calmly v2.0 FIT Verifier C3 gate)**

The AOM v1 cost floor (£480/claim) and the fin-sim v3 cost floor (£315/claim) used the **same law clinic module architecture** (solicitors + students) but different methodologies (bottom-up hourly rates vs top-down annual budget). The discrepancy was methodology, not architecture.

The AOM v2 (exchange model) correctly excludes solicitor and student costs from Calmly's P&L — those belong to the pool operators who bear litigation risk. Replacing the solicitor+student module with lower-cost LMU specialist roles reduces the cost floor to ~£236/claim (FMOS 63.6%). The fin-sim v3 still uses the old module model and needs to be rebuilt to the AOM v2 cost structure.

**Rule:** any cost model for the v2 exchange model must exclude solicitor salaries, law student supervision, court filing fees, and working capital for claims in litigation. These are pool operator costs. Including them inflates Calmly's cost floor by ~£71/claim and produces a false BORDERLINE verdict.

**Applied to Calmly fin-sim:** the rebuild should use AOM v2 activity table (265.5 min/confirmed claim at blended LMU specialist rates) rather than module annual budget ÷ capacity.

---

### Cost-shifting is not architecture — R3 design principle

**Established: 15 May 2026**

An R3 solution must create new value, not just redistribute an existing cost. Transferring the working capital burden to investors, lenders, or partners reduces exposure but creates no new value — any incumbent could do the same. A genuine R3 solution transforms the working capital constraint into a mechanism that creates value for someone.

**The test:** "We found someone else to hold the cost" is not R3. "We created a new financial instrument that converts the cost into yield" is R3.

---

### Don't specify unless required — architectural precision principle

**Established: 18 May 2026 (Calmly v2.0 design session)**

At the architectural level, do not lock in implementation details that are not load-bearing. An element is required only if removing it changes the mechanism. If it can be removed and the mechanism still works, it is over-specification — and over-specification at R1 propagates constraints through every subsequent requirement.

**Test:** "If I remove this specification, does the mechanism change?" If no: remove it.

**Applied to Calmly C1:** "Investor-held portfolios" was in the original Workaround Strategy. The mechanism is pooling (EV/risk distribution across a claim portfolio). Who holds the pool is not a C1 architectural decision — it is an implementation choice that will be resolved by R3. Removed.

---

### EV/risk-pooling is the mechanism — not economies of scale

**Established: 18 May 2026 (Calmly v2.0 design session)**

The mechanism that makes claims pooling work is EV/risk-pooling (law of large numbers), not cost reduction per unit. These are different arguments and the distinction matters for theory grounding.

**Individual claim:** binary outcome. Win or lose. Expected value may be positive, but the full downside falls on one person. Pursuit is often irrational even when EV is positive — because the variance is unbearable at the individual level.

**Portfolio of claims:** individual binary outcomes average out. The pool operator makes an EV decision across the portfolio. The variance that made individual pursuit irrational disappears at portfolio scale. Pursuit becomes the rational committed strategy — not because it is cheaper per unit, but because the pool operator is no longer taking a single bet.

**What does not change:** the cost per claim. Economies of scale would imply the cost per claim falls as volume increases. That is not the claim. The cost per claim may be similar. What changes is who bears the variance — and therefore whether pursuit is rational at all.

Do not frame C1 as "cheaper at scale." Frame it as: "rational at scale — because individual binary outcomes average to a predictable expected value across a portfolio."

---

### Platform model — Calmly v2.0 architecture

**Established: 18 May 2026 (Calmly v2.0 design session)**

Calmly is a platform, not a claims buyer or claims manager. The pool operator holds claims and bears litigation risk. Calmly operates the platform infrastructure — claim origination, pool matching, settlement facilitation, independent EV assessment.

**Consequence for the P&L:** solicitor costs, litigation filing costs, and working capital for claims in dispute are pool operator costs. They do not appear on Calmly's P&L. Calmly earns platform fees from both parties (claimant and defendant) for each claim resolved.

**Consequence for R3:** v1.0 R3 was securitisation of Calmly-owned claims (13-month financing lag). This is architecturally incompatible with the v2.0 platform model — Calmly owns no claims and therefore has no financing lag on a claims portfolio. v2.0 R3 must address platform scaling constraints: exchange liquidity (enough claims on both sides to make pooling viable), platform infrastructure cost structure, and NTP (Network Tipping Point) activation cost.

**Consequence for modelling:** CTM, AOM, fin-sim, and FIT check must only include Calmly's platform costs. Any model that includes pool operator costs (solicitors, litigation filing, claims working capital) is modelling the wrong entity.

---

### Both parties as paying customers — mediation model

**Established: 18 May 2026 (Calmly v2.0 design session)**

Claimants AND defendants are paying customers. Both receive value. Both pay.

- **Claimant value:** independent assessment of what they are owed (factual basis for settlement)
- **Defendant value:** credible signal of what they legitimately owe (resolves open-ended liability uncertainty)
- **Revenue:** platform fees from both sides per claim resolved

The HIO is shared: "We reach a settlement that reflects the merits of the case." Claimant perspective: I receive what I am owed. Defendant perspective: I pay what I legitimately owe — no more.

**Consequence for C2:** two-customer model required. The C2 KMC identifies the maximum WTP for each party (claimant: £1,233; defendant: £1,400). This is the value ceiling — not the price. Who pays, how much, and when is determined at C6 (Amortization Strategy). Do not conflate KMC with actual fee at the F1 stage.

---

### Fee structure is C6 territory — do not define at C1–C3

**Established: 19 May 2026**

Fee structure — who pays, how much, and when — is determined by the **Amortization Strategy (C6)**. C6 is the correct place to design payment structure because it explicitly asks: how does the customer pay for the product without the cash flow constraint preventing adoption?

**During F1 (C1–C3), only two numbers matter:**
- C1 cost floor: the minimum viable unit cost at scale
- C2 value ceiling: the KMC — the maximum any customer will pay before the product stops creating value surplus

**Do not specify fee amounts, fee recipients, or payment timing during F1.** The only valid F1 statement about revenue is: "the platform generates fees from its customers." Who pays, how much, and when is entirely C6's design. Assumptions introduced before C6 propagate through all downstream modelling and constrain the fee design before the customer adoption and cash flow problems have been properly diagnosed.

**Why this matters:** specifying fee structure at the F1 stage produces a false precision that makes the model look either healthier or weaker than it is — before the actual payment architecture has been designed.

---

## Calmly — current design state (as of 19 May 2026, v2.0)

> ⚠ **SUPERSEDED LINEAGE — do not anchor a valuation on this section.** The 19 May "v2.0 exchange / platform-fee" architecture below (and the "exchange model — pool operators bear litigation risk, Calmly earns a platform fee from both parties" framing in the preceding `Applied to Calmly`, `AOM/fin-sim reconciliation`, `Platform model`, and `Both parties as paying customers` notes) is **earlier lineage**. It is retained as an audit trail of how the design evolved — not as the operative model.
>
> **The operative Calmly architecture is the 6 June Lloyd's / network-operator, per-transaction B2B fee model.** Calmly earns a per-transaction fee from B2B partners (transaction sites / financial platforms) and does **NOT** participate in recovery economics. Capital stays off Calmly's balance sheet. Operative figures: per-transaction cost floor ~£0.14, price ceiling ~£0.50; **FMOS ~196% refined / ~107% conservative**; ~**£21m/yr at-scale EBITDA midpoint** (PV £12–25m). Do **not** use the per-claim £221 cost floor / FMOS 66% / "~20% platform fee" numbers below for any new valuation work.
>
> **Operative sources of truth (anchor here):**
> - Valuation: `04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-valuation-memo-2026-06-05.html`
> - VDR + latest gate: `04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-VDR-changelog.html` and the C8 snapshot `calmlyresolve-venture-design-record-v12-2026-09-01.html`
> - Per-transaction FIT exhibit: `04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-exhibit-C10-fit-per-transaction-2026-06-03.html`
>
> When a new `/architect-custom` or valuation session opens, read the operative sources first. Treat everything below this banner as historical.

**Status columns:** SR = sub-requirements filled | CTM | AOM | Fin-sim | FIT = FIT Verifier PASSED

| Requirement | SR | CTM | AOM | Fin-sim | FIT | Notes |
|---|---|---|---|---|---|---|
| PCO | ✓ | — | — | — | — | Claimants AND defendants in England & Wales with unresolved small claims. Both parties are paying customers. HIO: reach a settlement that reflects the merits of the case. |
| C1 — At-scale cost bottleneck | ✓ | ✓ | ✓ | ~ | ✓ | CLO: credible litigation threat at individual claim level. Workaround: claims pooling (EV/risk distribution). BFF (C1): dispute resolution exchange pooling consumer claims. CTM/AOM updated to C1+C2+C3 scope (platform-only economics, pool operator costs excluded). Fin-sim v3 C3 inputs added but model still uses old solicitor+student module — needs rebuild to AOM v2 LMU specialist structure. FIT PASS 63.6% (19 May, four-layer FMOS). |
| C2 — Value bottleneck | ✓ | ✓ | ✓ | ~ | ✓ | Two-customer: C2a claimant KMC (delay as loss accrual, Prospect Theory), C2b defendant KMC (cost of not knowing fair settlement, Spence 1973). BFF (C1+C2): pooled claims exchange + bilateral independent EV settlement report. BORDERLINE from 18 May resolved: AOM/fin-sim discrepancy explained (exchange model removes solicitor cost from Calmly P&L; both costs measured same architecture, different methodology). FIT PASS 63.6% (19 May, covers C1+C2+C3). |
| C3 — Scaling bottleneck | ✓ | ✓ | ✓ | ~ | ✓ | CLO II: paying assessment org before revenues arrive (£16.28/claim, weighted avg recovery 4.65 months). Scaling Strategy: independent assessment org (university law students, no financial stake) generates every EV report — eliminates defendant credibility objection, shortens recovery cycle. Class of problem: recovery timing (maturity mismatch). Theory: Spence (1973) applied to speed dimension. BFF (C1+C2+C3): pooled claims exchange + bilateral independent EV assessment + dispute resolution platform. CTM: calmly-ctm-v2-2026-05-18.html. AOM: calmly-aom-v2-2026-05-18.html. Fin-sim: calmly-fin-sim-v3-2026-05-19.html (C3 inputs; model rebuild pending). FIT: calmly-fit-verifier-c3-2026-05-19.html — PASS 63.6%. |
| **F1 — complete** | **✓** | **✓** | **✓** | **~** | **✓** | **All three requirements closed. FIT Verifier PASS 63.6% (19 May 2026). Fin-sim rebuild to v2 LMU cost model pending (not a blocker).** |
| R4 — Customer doubt about value | ✓ | ✓ | ✓ | ✓ | ✓ | Attraction Strategy: free independent EV assessment (48hr, university law dept) as conviction mechanism. Same assessment org resolves claimant credibility doubt + investor credibility (C3) — one mechanism, two audiences. CAC: organic SEO + word of mouth. New cost: £38/claim CAC. Cost floor £237. FIT: calmly-fit-verifier-r4-2026-05-19.html — PASS 63.5%. Unit economics: calmly-unit-economics-r4-2026-05-19.html. |
| R5 — Biggest learning disruption | ✓ | ✓ | ✓ | ✓ | ✓ | Adoption Strategy: guided claim submission flow with progressive disclosure and live completeness indicator. Consumer sees exactly what evidence is needed; auto-save prevents abandonment. Theory: Bandura (1986) self-efficacy + Thaler & Sunstein (2008) choice architecture. No new per-unit cost (UX in SC). Cost floor £237. FIT: calmly-fit-verifier-r5-2026-05-19.html — PASS 63.5%. |
| R6 — Cash flow constraint | ✓ | ✓ | ✓ | ✓ | ✓ | Amortization Strategy: EV assessment frame resets consumer reference point from face value to expected value before offer is made. "Y% of independently-assessed EV" vs "Y% of what you're owed." Same assessment mechanism — three functions: C3 investor, R4 conviction, R6 reference frame. Theory: Kahneman & Tversky (1979) Prospect Theory + Thaler (1980) mental accounting. No new cost. Cost floor £237. FIT: calmly-fit-verifier-r6-2026-05-19.html — PASS 63.5%. |
| **F2 — complete** | **✓** | **✓** | **✓** | **✓** | **✓** | **R4–R7 closed. Final F2 FMOS 66% after R7 NTP. Ready for F3.** |
| R7 — Gateway partners | ✓ | ✓ | ✓ | ✓ | ✓ | Partner Activation Strategy: Resolver (agile, data-driven) as first gateway partner; Citizens Advice and Which? follow on Resolver outcome data. API integration + per-claim referral fee (NTP). NTP £25/claim. Replaces part of organic CAC → blended acquisition cost £22/claim (£16 saving vs R4). Cost floor £221. FIT: calmly-fit-verifier-r7-2026-05-19.html — PASS 66%. |
| R8 — Switching cost | ✓ | ✓ | ✓ | ✓ | ✓ | Lock-in Strategy: claim history as fast-track asset. Returning claimants (tenants, small businesses) benefit from established evidence patterns and assessment org familiarity. Switching cost = loss of accumulated claim history. Primary switching cost for one-time consumers: advocacy identity ("someone who beat a company through Calmly"). No new cost. Cost floor £221. FIT: calmly-fit-verifier-r8-2026-05-19.html — PASS 66%. |
| R9 — Supplier/partner leverage | ✓ | ✓ | ✓ | ✓ | ✓ | Lock-out Strategy: Calmly owns assessment methodology + quality standards, not the assessment orgs. Multiple university law departments onboarded under same playbook — competition among assessment orgs prevents hold-up. Pool operators compete for claim pools; no single gateway partner >30% of inflow. Assessment org fee upside: multi-org competition could reduce £16/claim → £10/claim at scale. Cost floor £221 (£215 upside). FIT: calmly-fit-verifier-r9-2026-05-19.html — PASS 66%. |
| R10 — Competitive moat | ✓ | ✓ | ✓ | ✓ | ✓ | Leverage Strategy: compound accuracy advantage data flywheel. More volume → better EV accuracy → tighter pool operator pricing → better claimant offers → more volume. Secondary moats: assessment org network depth (universities invested in training); pool operator calibration (pricing models built on Calmly data). Theory: Metcalfe (1980) network effects + Arrow (1962) learning-by-doing + Teece (1986) complementary assets. No new cost. Final cost floor £221. FIT: calmly-fit-verifier-r10-2026-05-19.html — PASS 66%. |
| **F3 — complete** | **✓** | **✓** | **✓** | **✓** | **✓** | **R8–R10 closed. Full architecture confirmed.** |
| CTM | ✓ | — | — | — | — | calmly-ctm-v2-2026-05-18.html — updated through R10. Exchange model, both-party customer model, independent assessment org, gateway partner journeys, switching cost accumulation. |
| AOM | ✓ | — | — | — | — | calmly-aom-v2-2026-05-18.html — updated through R10. LMU specialist roles, Selling stream (CAC/NTP), methodology ownership function. |
| Fin-sim | ~ | — | — | — | — | calmly-fin-sim-v3-2026-05-19.html — C3 inputs only. **Full rebuild required** to AOM v2 LMU + complete R4–R10 cost structure (CAC £38 → £22 blended, NTP £25). Cost floor should be £221/claim at-scale. Priority task before capital commitment. |
| Consistency audit | ✓ | — | — | — | — | calmly-consistency-audit-2026-05-19.html — CONSISTENT. 6 cross-requirement dependencies verified. Key flags: (1) fin-sim rebuild needed, (2) CLV upside for repeat claimants unmodelled, (3) data flywheel accuracy curve not in model, (4) switching cost stronger for B2C repeat users than one-time consumers. |
| Unit economics | ✓ | — | — | — | — | calmly-unit-economics-r10-2026-05-19.html — final state. Cost floor £221 at-scale. FMOS 66% at price ceiling £650. |

**COST PROGRESSION ACROSS ALL GATES:**
| Gate | Cost added | Cost floor | FMOS |
|---|---|---|---|
| C3 | Base architecture | £199 | 69% |
| R4 | CAC £38 (organic SEO) | £237 | 64% |
| R5 | £0 | £237 | 64% |
| R6 | £0 | £237 | 64% |
| R7 | NTP £25, CAC net £18 → blended £22 (saves £16 vs R4) | £221 | 66% |
| R8–R10 | £0 | £221 | 66% |

**Architecture status: ALL 10 REQUIREMENTS COMPLETE. Consistency audit: PASS.**

**Recommended next actions:**
1. Review R4–R10 outputs (design memo + 14 HTML files + consistency audit)
2. Full fin-sim rebuild to AOM v2 + complete cost structure (£221 cost floor target)
3. Validate 5 conditions from C3 FIT Verifier before capital commitment
4. Run `/ive-research-design-custom` to design F2 fieldwork protocol before pilot

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/architect-custom/SKILL.md` to modify
- **Invoke as:** `/architect-custom`
- **Skill chain this orchestrates:** `/balm-pco-custom` → `/balm-challenge-1-custom` → `/balm-challenge-2-custom` → `/theory-of-change-custom` → `/ive-fin-sim-custom` → `/ive-fit-verifier-custom` → F2 skills → F3 skills
- **Supporting skills:** `/ive-ctm-custom`, `/ive-aom-custom`, `/ive-consistency-audit-custom`, `/ive-research-design-custom`, `/verify-balm-custom`
- IVE source — the canon is a body of co-authored work, not one paper:
  - Simanis, E., Samani, S., Burnett, P. & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *Rediscovering Capitalism: How Blue-Chip Builders Created Transformative Impact and Profit.* YNOT Institute Working Paper 1, Queens' College Cambridge
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *The Business Architecture: The Hidden Code of Industry Disruption.* YNOT Institute Working Paper 2, Queens' College Cambridge — the Business Architecture Framework
  - Simanis, E. et al. (2024). *The Core Business Archetype* (Jan); *Engineering New Market Ventures* (Apr); *The Market Creator's Dilemma* (Nov)
  - Simanis, E. (2025). *Built to Hold* — the FMOS gates; Simanis, E. & Donohue, K. (2025). *Deciphering the Market Creator's Dilemma.* MIT Sloan Management Review
  - Attribution rule (WS1 feedback log, 5 and 17 Sep 2026): Tom Manuel is a co-author on the 2023 papers; "co-developer of the method" is not supported. TMTH's own additions are the WS1 standards, the VA register, the circle end-state and the direction rule
- Pawson & Tilley dossier: `06-Resources/Methodology/pawson-tilley/dossier.md`
