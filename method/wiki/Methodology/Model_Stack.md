# Model Stack — How the IVE Models Relate

The IVE design process produces six interdependent models. Each one answers a different question. Each one is an input to the next. None is optional — skipping one disconnects the financial model from operational reality.

This document maps the models, their dependencies, and the validation layer that runs across them.

---

## The Six Models

| Model | Question it answers | V-Model step |
|-------|---------------------|--------------|
| **BALM** | What are the 10 architectural requirements the CBA must satisfy? | Steps 2–3 |
| **CTM** | What must happen in the customer for the product to work at scale? | Step 3 |
| **AOM** | Who does what, where, at what volume, to make that happen? | Step 4 |
| **ARM** | What does that operation cost, built from first principles? | Step 4 |
| **Financial Simulation** | Does the cost structure produce a viable margin? | Step 4 |
| **FMOS** | Is the margin of safety sufficient to absorb real-world uncertainty? | Gate at Phase I close |

---

## The Dependency Chain

```
PCO
 └─→ BALM R1–R3 (F1: Catalyze Value Surplus)
       └─→ [FIT Verifier gate — mid-BALM]
             └─→ BALM R4–R10 (F2+F3) + CTM develops throughout
                   └─→ AOM (derives from BALM solutions)
                         └─→ ARM ←─────────────────────────────┐
                         │    (takes demand side from CTM)     │
                         │    (takes supply side from AOM)  ───┘
                               └─→ Financial Simulation
                                     └─→ [FMOS ≥ 60% gate — Phase I close]
```

---

## What each model is and is not

### BALM — Business Architecture Logic Model

The design record. Documents each of the 10 architectural requirements and the strategies chosen to satisfy them. The BALM is not a financial model — it records *what* is decided, not what that decision costs.

The BALM is worked through sequentially: R1 → R2 → R3 → [FIT Verifier] → R4 → R5 → R6 → R7 → R8 → R9 → R10. Each requirement is solved before the next is attempted because the solution space for each depends on constraints established by the earlier ones.

**Output used by:** CTM (each BALM solution shapes a stage of the customer journey), AOM (each BALM solution implies operational activities).

**See:** [[BALM]], [[Design_Loop]]

---

### CTM — Customer Transformation Model

The outside-in view of the architecture. Shows the cognitive, emotional, and behavioural state changes a customer must move through for the venture to function at scale — from first encounter through purchase, use, payment, and repeat.

The CTM is built alongside BALM R4–R10 (V-Model Step 3). It does not precede the BALM — it is shaped by it. Each requirement solution from R4–R7 specifies a mechanism (want, use, pay, gateway) that corresponds to a phase in the CTM.

The CTM identifies the 4-D Product (Working / Communications / Payment / Partner) that drives each state change. This 4-D product list is the demand-side input to the ARM.

**Inputs:** BALM solutions (what the product must do at each stage).  
**Output used by:** ARM (Step 1 — list what must be produced at each stage of the journey).

**See:** [[Customer_Transformation_Model]], [[BALM]]

---

### AOM — At-Scale Operational Model

The inside-out view of the architecture. Shows who (LMU / Territory / HQ) does what (Making / Selling / Marketing / Using), at what volume, for the venture to function at scale.

The AOM is built after the BALM is complete (V-Model Step 4). It is the operational counterpart to the CTM: both are derived from the same BALM solutions, from opposite vantage points. The AOM maps the operational system that produces the state changes the CTM requires.

The AOM is built right-to-left — from the last-mile unit back to head office. Design the LMU first; build head office around what the LMU requires.

**Inputs:** BALM solutions (what the product must be), CTM (what state changes must be delivered).  
**Output used by:** ARM (supply side — the roles and activities to be costed).

**See:** [[AOM_Guide]]

---

### ARM — At-Scale Resourcing Model

Translates the AOM and CTM into a cost structure derived from first principles. The ARM is not a financial model — it is the input to one.

The ARM takes two inputs simultaneously:
- **Demand side (from CTM):** what 4-D products must be delivered at each customer journey stage
- **Supply side (from AOM):** what roles and activities are required to deliver them

From these it derives four cost layers:

| Layer | Code | What it covers |
|-------|------|----------------|
| Personnel Variable Cost | PVC | Direct personnel — scales with volume |
| Resource Cost | RC | Non-personnel (assets, tech, consumables) |
| Support Cost | SC | Indirect personnel — semi-fixed overhead |
| Infrastructure Cost | IC | Fixed platform costs (HQ, central tech) |

Costs are built at LMU level first, then aggregated upward to Territory and HQ. If the LMU is not viable standalone, scale amplifies the problem rather than fixing it.

**Inputs:** CTM (4-D product demand list), AOM (role and activity structure).  
**Output used by:** Financial Simulation (PVC, RC, SC, IC as primary cost inputs).

**See:** [[ARM_Guide]]

---

### Financial Simulation

Projects ARM cost outputs across volume, time, and pricing assumptions to produce:
- Unit economics (cost per claim / transaction / customer at LMU level)
- Cash flow timeline (working capital requirements at each scale point)
- FMOS at each stage

The financial simulation is an engineering stress test, not a pitch document. It surfaces the scale point at which the venture becomes viable and reveals which assumptions most threaten that outcome.

**Inputs:** ARM (cost structure), BALM R1–R3 (price ceiling and revenue assumptions).  
**Output used by:** FMOS gate check.

---

### FMOS — Financial Margin of Safety

The output metric of the financial simulation. Measures the distance between the low-point estimate of willingness to pay and the high-point estimate of total unit cost, as a percentage of that cost.

```
FMOS = (Price Ceiling − Cost Floor) / Cost Floor     ← cost in the denominator
       where Price Ceiling = WTP_low
             Cost Floor    = full unit cost = PVC + RC + SC + IC + cost of capital
```

Source: Simanis, *Built to Hold* (Jan 2025, p.7). ⚠ NOT `(Revenue − PVC − RC) / Revenue` — that gross-margin / revenue-denominator form drops SC and IC and is incompatible with the Simanis benchmarks (corrected June 2026; was NCR-001).

**Bands (single source of truth: `Forge/WS1/criteria-registry.md`):** per-requirement PASS ≥25 / BORDERLINE 15–24 / FAIL <15; Phase II (LMU level, after all ten) PASS ≥60 / BORDERLINE 25–59 / FAIL <25.

Below the Phase II gate indicates an architectural problem, not an execution one. Execution optimisation cannot fix a structurally unviable cost structure. Return to the BALM requirement(s) responsible for the cost or value-ceiling problem and redesign.

---

## The Validation Layer

Three tools run across the model stack to check different properties:

| Tool | What it checks | When to run |
|------|---------------|-------------|
| **FIT Verifier** | FMOS at F1/F2 boundary — does the F1 architecture (R1–R3) produce viable unit economics before F2 design begins? | After R3, before R4 |
| **BALM Verification** | Completeness — are all 10 requirements present and to IVE standard? | After all 10 requirements are designed |
| **Consistency Audit** | Logical coherence — do the 10 requirement solutions contradict each other? | After BALM Verification passes |

The FIT Verifier is a mid-design gate. If it fails, R1–R3 must be revised before F2 work begins — F2 cannot be productized on a broken F1 architecture.

BALM Verification and Consistency Audit are Phase I close-out checks. Both must pass before Phase II capital is committed.

---

## Common Errors in Model Construction

| Error | What breaks |
|-------|-------------|
| Building the financial model without an AOM | Cost assumptions are untethered from operational reality — the ARM is skipped |
| Building the ARM before the AOM is complete | Resources are mapped to activities that don't exist or are mis-specified |
| Building the AOM before BALM R4–R10 are solved | AOM embeds the conventional BFF because the architectural solutions haven't constrained it |
| Running the FMOS gate on best-case assumptions | Passes on paper; fails on contact with real cost overruns |
| Treating FMOS < 60% as fixable through execution | FMOS is an architectural signal. It is not fixable through better sales or lower overheads |

---

## Build Sequence (summary)

```
1. PCO — select the venture opportunity
2. BALM R1–R3 — design F1 (cost floor, value ceiling, scaling)
3. FIT Verifier — gate check on F1 architecture
4. BALM R4–R7 — design F2 (adoption mechanics)
5. CTM — build alongside R4–R7, finalise after R7
6. BALM R8–R10 — design F3 (market position)
7. AOM — map the full at-scale operation (all 10 BALM solutions)
8. ARM — derive cost structure from AOM + CTM
9. Financial Simulation — project ARM costs across volume and time
10. BALM Verification — completeness check
11. Consistency Audit — logical coherence check
12. FMOS gate — ≥ 60% at LMU level → Phase II cleared
```

---

## See Also

- [[BALM]] — the 10-requirement framework
- [[Customer_Transformation_Model]] — the CTM in detail
- [[AOM_Guide]] — how to build the AOM
- [[ARM_Guide]] — how to derive costs from the AOM
- [[FIT_Framework]] — FMOS and the evaluative framework
- [[V_Model_Process]] — the full Phase I → Phase II journey
- [[Design_Loop]] — the iterative mechanism within each requirement

---

*Written 21 May 2026. Sources: AOM_Guide.md, ARM_Guide.md, Customer_Transformation_Model.md, V_Model_Process.md, FIT_Framework.md (TMTH IVE Wiki).*
