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

**The session experience:** the user names a venture. Orient (new → Phase 0; existing → resume at the current phase), then drive phase by phase, routing to the sub-skill for each step. At every mini-output, check its registry criterion. **Do not pass a gate that fails its criterion — return to the step.** The run ends at Phase 4 with `/verify-venture-custom` and an integrity score. **What the run hands over** once Verify has closed: the business case document and its evidence workbook — `/ive-business-case-custom`, built to `04-Projects/TMTH_Venture_Studio/Forge/WS1/business-case-standard.md` from the model data file the fin-sim wrote. A run that ends with a score and no business case has not finished.

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

## Step 0 — Named-business entry ("I want to disrupt X")

When the opening request names a business to disrupt — a company ("disrupt Halfords"), one line of a company ("disrupt Tesco's grocery delivery") or a named kind of business ("disrupt high-street bicycle shops") — the run does **not** open with a PCO conversation. **The named business is challenge one, sub-requirement 1.** The conventional business form factor is how that business makes, sells, delivers and gets paid for the thing today. Route straight to `/ive-design-loop-custom` → `/balm-challenge-1-custom` with the named business as the SR1 input. (Tom, 22 September 2026.)

The run fills the frame itself, from public sources, before SR1 — it does not ask the user for any of it:

- **the line** — if a whole company is named, take its largest line by revenue from its published accounts and state it in one sentence; the user can redirect
- **the job** the line does for its buyers, in the buyer's terms, levelled per PCO Step 2d — stop where the next-broader case is delivered a different way today
- **current buyers** — count, price paid, volume, with source. PCO Step 4 on Path C is answered by existence: the line is paid for at scale
- **the mode** (RD-024) — 3, "just show me", unless the user gives a target group (mode 1) or a number (mode 2). In mode 3 add the incumbent's roadmap form (VA-159) with source, red until sourced

These go into the VDR's PCO block, headed "derived from the named business", each figure red until sourced. That block is the confirmed PCO for the run; challenge one's hard stop 1 is met by it. Do not ask the user to confirm a PCO, to name a core functionality or to name an excluded population — in mode 3 none is required.

One business → one line → one conventional form → one CLO. If the named business has several lines, the run lists the ones it found, takes the largest and says so; it does not stop to ask. The research firewall holds from the first line: the incumbent is the baseline, never an analogue — "a cheaper, digital or automated X" is not a design.

---

## Step 1 — Read current venture state

When invoked, immediately read the venture's **authoritative** design record (never a stale memo).

- **A venture with its own architect skill or memory file:** follow that file's reading order to the canonical design record. Never read a memo flagged stale.
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

Design principles established across runs. Apply them when routing and when introducing a skill. The worked examples that produced them are venture records, not method, and live with the venture.

---

### At-scale architecture and scaling architecture are two designs

IVE designs two distinct architectures. The **at-scale architecture** is the venture operating permanently at the scale that pays back all investment capital at a competitive return; every requirement is designed for it, and it assumes the scaling mechanisms are already running. The **scaling architecture** is the sequence of temporary structures that get the venture there without running out of capital; each stage has its own economics and falls away once it has served. R3 is where the second design is done. The simulation keeps the two apart: a primary at-scale model and a stage-gate model that asks what the venture must survive at each stage before the next mechanism fires.

### Each challenge runs in full — prior outputs are inputs, not substitutes

Every challenge is applied maximally and independently, however much earlier challenges appear to have covered the requirement. A prior mechanism that happens to serve the current requirement is an architectural bonus, not a reason to abbreviate the diagnostic. Run every sub-requirement in sequence with prior outputs as starting context. The framework exists to find what has not been found yet.

### Cross-requirement elegance

The best architectural moves serve several requirements at once — Grameen's joint liability removed credit-assessment cost (R1), raised repayment (R2) and removed the default reserve (R3). At every requirement ask whether the mechanism also touches another. Finding that it does is the start of the diagnostic, not the end.

### The operating module is not the unit of transaction

The unit of transaction is one sale or one case; the operating module is the structure that gets replicated at scale. Every simulation anchors to the module. The module has a capacity ceiling, fixed costs are module costs spread across transactions, and the primary intrinsic performance curve for module ventures is fixed cost per unit falling as utilisation rises. F2 acquisition design is sized to fill modules, not only to grow volume.

### Source discipline — assume and note, audit later

Every input carries a source tier. Tier 1: the venture's own field data or operations. Tier 2: published statistics. Tier 3: a named expert or comparable venture. Tier 4: a reasoned assumption with its logic stated. Do not block design on a missing source: make the most defensible assumption, tag it Tier 4, move on. Source validation is a separate audit step.

### CMO framing for every theory of change

Context (the conditions that let the mechanism fire), Mechanism (how participants reason and react to the resource), Outcome (the proportionate observable change). Theory is peer-reviewed and citable; the hypothesis is the design claim. They are separate fields. See `/theory-of-change-custom` and the Pawson and Tilley dossier.

### Cost models must model the right entity

When a design moves an activity to another party, that party's costs leave the venture's P&L. A cost model that keeps them produces a false cost floor and a false verdict. Two models of the same architecture that disagree usually differ in method (bottom-up activity rates against a top-down budget), not in architecture — reconcile the method before touching the design.

### Cost-shifting is not architecture

An R3 solution creates new value; it does not move an existing cost to an investor, lender or partner, which any incumbent could do. "We found someone else to hold the cost" is not R3. "We converted the cost into a yield" is.

### Do not specify what is not load-bearing

An element is required only if removing it changes the mechanism. Over-specification at R1 constrains every later requirement. Test each specification by removing it.

### Pooling is a variance mechanism, not economies of scale

Where a design pools binary outcomes, the mechanism is the law of large numbers: pursuit becomes rational because the variance that made a single bet unbearable disappears across a portfolio. Cost per unit may not fall at all. Frame it as rational at scale, not cheaper at scale.

### Fee structure is C6 territory

Who pays, how much and when is designed at the amortisation strategy (C6). During F1 only two numbers exist: the C1 cost floor and the C2 value ceiling (the KMC). Fee assumptions introduced earlier propagate false precision through every later model.

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
