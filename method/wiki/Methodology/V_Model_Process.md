# V-Model — The Full IVE Venture Journey

IVE follows systems engineering's V-model structure. The left side designs top-down; the right side builds and validates bottom-up. 85% of a venture's cost structure is locked in at the CBA/Core Operating System stage — before any product is built or customer is acquired.

Source: IVE Venture Training Studio (Half-Solved + Cornell MCL + INCOSE), July–November 2025

---

## The V-Model Overview

```
Phase I (Design & Validate)              Phase II (Build & Validate)
─────────────────────────────────        ──────────────────────────────
Step 1: Define PCO                       Step 5: Build & Test Components
    ↓                                        ↓
Step 2: Design CBA & BFF                 Step 6: Build & Test Workflows
    ↓                                        ↓
Step 3: Design Core Business Outputs     Step 7: Minimum Representative Pilot
    ↓                                        ↓
Step 4: Design Key Workflows ─────────→ Step 8: Launch & Scale (MVV)
         [Gate: FMOS ≥ 60%]                  [Gate: NPV > Hurdle Rate]
```

---

## Phase I: Design & Validate (4–6 months, low capital)

### Step 1: Define the Prime Commercial Opportunity (PCO)

Identify the broad use case that can most credibly generate at-scale revenues to pay back all required investment capital at a competitive rate of return.

**The Venture Design Funnel:**
1. PCO Screen — first-principles filters to eliminate clearly non-viable opportunities
2. Rapid Architecting (Venture Sketches) — lightweight architecture sketches for 2–4 shortlisted PCOs
3. Full Architecting (Venture Blueprints) — complete BALM-based design for selected PCO

Output: One PCO with documented rationale.

**See:** [[PCO_Methodology]]

---

### Step 2: Design CBA & BFF

Solve Function 1 of the BALM — Catalyze Value Surplus (R1, R2, R3).

This step defines:
- The Critical Limiting Operation (at-scale cost bottleneck)
- The Customer's Key Monetizable Cost (value ceiling)
- The Scaling Cost Bottleneck (working capital problem)

**Key principle:** R1 must be productized first. The workaround strategy from R1 gives the first "handhold" — it shapes the product form factor, which then constrains the solution space for R2 and R3.

Gate check: Is there positive "headroom" between cost floor and value ceiling? If not, the CBA cannot generate value surplus.

**See:** [[Venture_Architecture]], [[BALM]]

---

### Step 3: Design Core Business Outputs

Solve Functions 2 and 3 of the BALM — Normalize Customer Routines (R4–R7) and Dictate Competitive Landscape (R8–R10).

**The 4-D Product:**

| Output | What It Solves |
|--------|---------------|
| **Working Product** | The core functionality delivered to the customer |
| **Communications Product** | How the venture sells, attracts, and activates customers |
| **Payment Product** | How the venture gets paid, and how customers pay |
| **Partner Product** | How the venture integrates gateway partners and enablers |

Each Core Business Output has product form and operational form — shaping the product determines the operational requirements that follow.

**See:** [[Customer_Transformation_Model]]

---

### Step 4: Design Key Business Workflows

Map the at-scale operational model and financial simulation.

**At-Scale Operational Model:**
- Operating Units: Head Office → Territory → Last-Mile Unit
- Ops Map: product flow, information flow, money flow
- HR assignment to activities
- At-Scale Resourcing Model: personnel, durables, consumables per activity

**Financial Model (4-step construction):**
1. At-scale unit revenue and cost (from CBA and BFF)
2. Operating unit structure and cost
3. At-scale cash flow timeline
4. Investment required and return on capital

### Gate: FMOS ≥ 60%

The Financial Margin of Safety measures the venture's ability to absorb higher-than-expected costs and lower-than-expected demand.

- **Conservative FMOS** = (Conservative Value Surplus − Required Return) / Required Return
- Target: conservative FMOS ≥ 60%
- If FMOS < 60%: identify which requirements are under-solved and revise

**What good looks like:** Architecture stress-tested against worst-case scenarios. No single requirement failure kills the model. Investment case documentable and defensible.

---

## Phase II: Build & Validate (12–18 months, high capital)

### Principle: Build Components Before Workflows

Test the smallest testable unit first, then integrate. This front-loads validation and avoids burning capital testing architecturally broken products at the workflow level.

Build sequence:
1. Individual components (e.g., a sales message, a payment mechanism, a partner agreement)
2. Integrated workflows (full customer acquisition → delivery → payment cycle)
3. Minimum Representative Pilot (complete integration test)

---

### Step 5: Build and Test Components

**For each component:**
- Define the testable hypothesis
- Identify the minimum version needed to test it
- Measure against BALM requirement (not just user satisfaction)

**Common traps:**
- Testing whether customers "like" the product rather than whether it eliminates the Key Monetizable Cost
- Building full workflow integrations before components are validated
- Confusing positive user feedback with architectural validation

---

### Step 6: Build and Test Workflows

Assemble validated components into full Operating Unit workflows. Test whether the operational model functions as modelled — not just whether individual components work.

**Key workflow tests:**
- Full customer journey (attract → adopt → pay → retain)
- Partner integration (onboarding, delivery, data)
- Unit economics at small scale

---

### Step 7: Minimum Representative Pilot (MRP)

**Three criteria for a valid MRP:**
1. **Tests key operations** — exercises all critical workflows, not just the comfortable ones
2. **Representative context** — pilot population, geography, and conditions reflect at-scale target
3. **Reflects seasonality** — long enough to capture the full cycle of relevant seasonal variation

Output: Validated unit economics. Updated financial model. Decision: launch at scale or revise architecture.

### Gate: NPV > Hurdle Rate

---

### Step 8: Launch & Scale — Maximum Viable Venture

**Maximum Viable Venture:** The at-scale configuration, where FMOS has been validated through the MRP and the investment case is proven.

**Scaling principle:** Scaling is Operating Unit replication, not product iteration. The architecture is fixed; what changes is geography, volume, and headcount.

---

## Time and Capital Benchmarks

| Phase | Duration | Capital Intensity |
|-------|----------|-------------------|
| Phase I (Design) | 4–6 months | Low — design and simulation only |
| Phase II (Build) | 12–18 months | High — build, pilot, and launch costs |
| Total | 16–24 months | Concentrated in Phase II |

**Why this matters:** Phase I is cheap relative to Phase II. Spending 4–6 months and modest capital on Phase I before committing Phase II capital is the highest-leverage risk mitigation available to a founder.

---

## Mapping to Conventional Frameworks

| Conventional Stage | IVE Equivalent | Key Difference |
|--------------------|---------------|----------------|
| Ideation | PCO Screen + Venture Sketches | IVE selects PCO on FMOS criteria, not market size alone |
| MVP | Design CBA + Core Outputs (Phase I) | IVE "MVP" is an architectural design, not a built product |
| Acceleration | Build & Validate (Phase II) | IVE validates architecture before scaling, not during |

---

## Diagnostic Warning Signals

| Stage | Warning Signal |
|-------|---------------|
| PCO | Selected on passion or market size rather than FMOS criteria |
| CBA | R1 "solved" by efficiency improvement, not architectural workaround |
| Core Outputs | Product designed before R1 workaround strategy is defined |
| Financial Model | FMOS calculated on best-case scenario only |
| Build phase | Testing workflows before components are validated |
| MRP | Pilot is in a "friendly" context that doesn't reflect at-scale conditions |
| All | Moving to next phase without passing the relevant gate |

---

## See Also
- [[PCO_Methodology]] — Step 1 in detail
- [[Venture_Architecture]] — Step 2 (CBA & BFF)
- [[BALM]] — the 10 requirements underlying Steps 2–4
- [[Design_Loop]] — the iterative mechanism within each step
- [[FIT_Framework]] — the evaluative framework across all phases
- [[Diagnostic_Criteria]] — evidence standards for each phase

---
*Sources: ive-founder-journey.md, ive-foundations.md (surrendered-entrepreneurship vault, Apr 2026)*
