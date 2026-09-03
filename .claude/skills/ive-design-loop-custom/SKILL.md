---
name: ive-design-loop-custom
description: IVE Design Loop — OPTIONAL status-board and router across the ten BALM requirements. As of June 2026 the Diagnose→Theorize→Productize→Simulate loop, the FIT gate, the loop-back, and the pivot discipline are embedded INSIDE each balm-challenge-N-custom skill — so invoking a challenge skill directly already runs the full loop. Use this wrapper only when you want the cross-challenge status board (which Rn are PASS/FAIL) and the routing rules between challenges. It is no longer required to enforce the loop.
---

# IVE Design Loop — optional status board / router

**Read this first.** The design loop now lives inside each challenge skill. As of June 2026, every `balm-challenge-N-custom` skill carries its own "This skill IS a design loop" section — the full Diagnose→Theorize→Productize→Simulate sequence, the FIT gate with teeth (correct cost-denominator FMOS, stress test, explicit pivot trigger), the loop-back on FAIL, and the pivot discipline. **Invoking a challenge skill directly runs the complete loop.** You do not need this wrapper to get the loop.

**What this wrapper is still good for:** the cross-challenge view — the status board (which of the ten are PASS / FAIL / BORDERLINE), the routing rules between requirements, and the whole-architecture convergence reminder (the 60% Phase II outer gate, run once after all ten). It orchestrates; it no longer enforces (the skills enforce themselves).

**Bands — single source of truth:** `method/criteria-registry.md`. Per-requirement: PASS ≥25 / BORDERLINE 15–24 / FAIL <15. Phase II (after all ten): PASS ≥60 / BORDERLINE 25–59 / FAIL <25.

**The rule (now enforced by each skill, surfaced here):** you cannot proceed to the next requirement without a FIT PASS on the current one.

**The sequence for each requirement:**

```
1. DIAGNOSE   — run the BALM challenge skill for R[n]
2. THEORIZE   — run /theory-of-change-custom if a ToC is required
3. PRODUCTIZE — write the Strategy, then update CTM and AOM
4. SIMULATE   — run /ive-fit-verifier-custom
        ↓
   PASS → mark R[n] complete, proceed to R[n+1]
   FAIL → return to step 1 with the diagnosis
```

**The Strategy comes before CTM/AOM updates.** It operationalises the ToC — it is the design decision. CTM and AOM updates then reflect that decision. Do not update the CTM or AOM until the Strategy is written and confirmed.

---

## Requirement map

| # | Requirement | BALM skill | Named output | CTM phase affected | 4-D product | AOM stream |
|---|---|---|---|---|---|---|
| R1 | Workaround | `/balm-challenge-1-custom` | Workaround Strategy + Workaround ToC | Phase 2 — Consuming (core delivery) | Working Product | Making + Using |
| R2 | Efficacy | `/balm-challenge-2-custom` | Key Monetizable Cost + Efficacy ToC | Phase 2 — Consuming (value realisation) | Working Product | Using |
| R3 | Scaling | `/balm-challenge-3-custom` | Scaling Mechanism | Phase 3 — Paying (working capital) | Payment Product | Making (WC structure) |
| R4 | Attraction | `/balm-challenge-4-custom` | Want Block solution | Phase 1 — Becoming (conviction) | Communications Product | Selling + Marketing |
| R5 | Adoption | `/balm-challenge-5-custom` | Use Block solution | Phase 2 — Consuming (activation) | Working Product | Using |
| R6 | Amortization | `/balm-challenge-6-custom` | Buy Block solution | Phase 3 — Paying (payment trigger) | Payment Product | Using |
| R7 | Gateway Partners | `/balm-challenge-7-custom` | Partner activation mechanism | Phase 1 — Becoming (awareness + sign-up) | Partner Product | Selling |
| R8 | Lock-in | `/balm-challenge-8-custom` | Switching cost mechanism | Phase 2 — Consuming (accumulation) + Phase 4 | Working Product | Using |
| R9 | Lock-out | `/balm-challenge-9-custom` | Lock-Out Strategy + Lock-Out Theory of Change | Phase 4 — Repeating (competitive moat) | Working Product | Making |
| R10 | Leverage | `/balm-challenge-10-custom` | Leverage Strategy + Leverage Theory of Change | Phase 4 — Repeating | All products | All streams |

---

## Opening — orient the session

When the user invokes `/ive-design-loop-custom`, first ask:

> "Which requirement are we working on? And do you have the venture's current CTM and AOM files? (If this is R1, we'll create them from scratch. For R2+, we'll update what's already there.)"

Then display the current status board:

```
VENTURE: [name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

F1 — Neutralise the Value Barrier
  R1  Workaround        [ ] / [✓ PASS] / [✗ FAIL]
  R2  Efficacy          [ ] / [✓ PASS] / [✗ FAIL]
  R3  Scaling           [ ] / [✓ PASS] / [✗ FAIL]

F2 — Normalise the Customer Routine
  R4  Attraction        [ ] / [✓ PASS] / [✗ FAIL]
  R5  Adoption          [ ] / [✓ PASS] / [✗ FAIL]
  R6  Amortization      [ ] / [✓ PASS] / [✗ FAIL]
  R7  Gateway Partners  [ ] / [✓ PASS] / [✗ FAIL]

F3 — Lock In the Market Position
  R8  Lock-in           [ ] / [✓ PASS] / [✗ FAIL]
  R9  Lock-out          [ ] / [✓ PASS] / [✗ FAIL]
  R10 Leverage          [ ] / [✓ PASS] / [✗ FAIL]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current: R[n] — [Requirement name]
```

Update this board at the close of every requirement loop.

**Gate rule:** If the user asks to move to R[n+1] and R[n] is not marked ✓ PASS, refuse and return to Step 4 (FIT Verifier). State the reason: "R[n] has not cleared the FIT Verifier. Run the verification before proceeding."

---

## Step 1: DIAGNOSE — run the BALM challenge skill

> "Run `/[balm-skill-for-R[n]]` now. Come back here when you have the requirement solution."

While the user works through the BALM skill, the Design Loop waits. When they return with the solution, confirm:

- What is the core design choice? (The strategy — what the venture will do differently)
- What is the critical assumption? (The condition that must be true for the strategy to work)
- What does this change about the cost structure? (More or fewer activities? More or less capital commitment? Higher or lower working capital?)

For R1 and R2, also confirm:
- Has `/theory-of-change-custom` been run for this requirement? If not, prompt them to run it before continuing — the ToC grounds the strategy in a named mechanism, which is required for the T check in the FIT Verifier.

---

## Step 2: THEORIZE — confirm the Theory of Change

For R1, R2, R3, and any requirement where the strategy involves a novel mechanism (not standard industry practice):

> "What is the theory grounding this strategy? Name the mechanism and the precedent."

If the user has run `/theory-of-change-custom`, this is already done — ask them to confirm the named theory and the critical assumption from the ToC output.

If not run yet: prompt them to run it now. The FIT Verifier's T check requires a named theory.

For requirements where the strategy is standard industry practice (no novel mechanism), the T check defaults to PASS — note this explicitly.

---

## Step 3: PRODUCTIZE — write the Strategy, then update CTM and AOM

This step has three sub-steps in order: Strategy first, then CTM, then AOM. The Strategy is the design decision; the CTM and AOM record its operational implications. Skipping 3a means the CTM and AOM have no confirmed design to reflect.

### 3a — Write the Strategy

The Strategy operationalises the Theory of Change. It is the venture's specific answer to the requirement — what it will do, why it works (grounded in the ToC), and how it changes the cost or value structure.

Ask:

> "What is the R[n] Strategy? Specifically:
> - What does the venture do to circumvent or eliminate the challenge named in DIAGNOSE?
> - Why does this work — which mechanism from the ToC fires, and under what conditions?
> - What does this change about the cost structure, value delivered, or working capital requirement?
> - Does this solution create new value, or does it redistribute an existing cost?"

The last question is a test for R3 in particular: cost-shifting is not architecture (see IVE institutional memory). A genuine Strategy creates new value. Confirm this before proceeding.

When the Strategy is confirmed, write it into the BALM design memo's Strategy cell for R[n].

### 3b — CTM update

Using the requirement map table above, identify which CTM phase and 4-D product component this requirement affects.

Ask:

> "What product component does R[n]'s solution add or change? Specifically:
> - Which phase of the customer journey does it affect? (Becoming / Consuming / Paying / Repeating)
> - Which 4-D product delivers it? (Working / Communications / Payment / Partner)
> - What is the specific element? (e.g. 'a peer group session that substitutes for expert facilitation')
> - What state change does it produce in the customer? (Cognitive / Emotive / Behavioural)"

If this is R1 (first requirement): create the CTM from scratch per Section 5 of `/balm-challenge-1-custom` — write `[venture]-ctm-model-at-C1.yaml` and run the generators in `.claude/skills/shared/generators/` (`/ive-ctm-custom` is deprecated — do not invoke; never hand-write the HTML). The CTM starts with standard industry practice; R1's Workaround Strategy is the first override.

If R2+: update mode — add or modify only the affected row(s) in the CTM. Do not rebuild the whole document. Update the relevant phase and sub-phase in the existing CTM file.

Confirm the CTM update is complete before moving to 3c.

### 3c — AOM update

Using the requirement map table, identify which operating unit level and activity stream this requirement affects.

Ask:

> "What activities does R[n]'s product component require? Specifically:
> - Which stream? (Making / Selling / Marketing / Using)
> - Which level? (LMU / Territory / HQ)
> - What role delivers it?
> - How long does it take per unit?
> - What is the volume driver? (per unit / per inquiry at X% conversion / per stage at Y% probability / fixed per LMU)"

If this is R1: create the AOM from scratch per Section 6 of `/balm-challenge-1-custom` — write `[venture]-aom-model-at-C1.yaml` and run the generators in `.claude/skills/shared/generators/` (LMU first; `/ive-aom-custom` is deprecated — do not invoke; never hand-write the HTML).

If R2+: update mode — add or modify only the affected activity rows. Do not rebuild the whole AOM. Confirm the activity cost driver is fully specified (volume driver, time, role, operating level).

Check for the common errors:
- Has a pre-purchase activity been divided by the conversion rate?
- Has a new enabler role been added if the delivery role requires supervision or QA?
- Has a new HQ function been added if R[n]'s solution requires central support (technology, compliance, partner management)?

Confirm the AOM update is complete before moving to Step 4 (SIMULATE).

---

## Step 4: SIMULATE — run the FIT Verifier

With the CTM and AOM updated, the cost structure has changed. Run the verification.

> "Run `/ive-fit-verifier-custom` now. Bring the updated cost floor from the AOM and the price ceiling from R2."

**For R1:** The cost floor is the R1-designed BFF cost structure (from the AOM activities just mapped). The price ceiling is not yet defined — use a preliminary estimate from PCO (what the target customer can pay). Note the FIT Verifier result is indicative until R2 is solved.

**For R2:** The Key Monetizable Cost is now defined. Re-run the FIT Verifier with the R2 price ceiling. This is the first definitive FMOS check.

**For R3–R10:** The cost structure changes with each requirement (new activities, new product components). Re-run the FIT Verifier with the updated AOM cost floor after each one.

**Updating the fin-sim:** If `/ive-fin-sim-custom` has been built for this venture, update the relevant Group 4 activities with the new AOM rows before running the FIT Verifier. The FIT Verifier should pull costs from the fin-sim if it exists, not from rough estimates.

---

## Step 5: Verdict and routing

### PASS

> "R[n] — [Requirement name] — ✓ PASS
> FMOS: [X]%. Architecture clears the financial hurdle with R[n]'s solution incorporated.
>
> Mark R[n] complete. Proceed to R[n+1] — [Requirement name].
> Run `/ive-design-loop-custom` and confirm R[n+1] to continue."

Update the status board. Mark R[n] as ✓ PASS.

Route to the next requirement:
- R1 → R2 (also trigger `/ive-research-design-custom` before fieldwork if not yet run)
- R3 → R4 (also note: R4 begins F2 — check the Research Design Agent output is available for Want Block analysis)
- R10 → `/ive-consistency-audit-custom` (all requirements complete — run the full dependency check)

### BORDERLINE (FMOS 15–24%)

> "R[n] — [Requirement name] — ⚠ BORDERLINE
> FMOS: [X]% — below 25% but not fatal.
>
> Conditions to meet before marking complete:
> [List conditions from FIT Verifier output]
>
> Options:
> 1. Accept the conditions as critical assumptions and proceed — they become test priorities in Phase II fieldwork
> 2. Revise R[n]'s design to improve the cost floor or price ceiling, then re-run the FIT Verifier"

Do not automatically gate on borderline. Ask the user explicitly: "Accept conditions and proceed, or revise R[n]?"

If they accept: mark R[n] as ✓ PASS (conditional) and note the conditions in the status board. Proceed to R[n+1].
If they revise: return to Step 1.

### FAIL

> "R[n] — [Requirement name] — ✗ FAIL
> FMOS: [X]%.
>
> [Diagnosis from FIT Verifier — which lever is off: cost floor too high or price ceiling too low]
>
> R[n] cannot be closed. Return to Step 1 and redesign before proceeding.
>
> Do not move to R[n+1]."

Mark R[n] as ✗ FAIL on the status board. Return to Step 1 with the FIT Verifier diagnosis as the new brief for the BALM challenge skill.

---

## Special routing rules

**R1 → Architecture Generator:** Before running `/balm-challenge-1-custom`, check whether `/ive-architecture-generator-custom` has been run. If not, prompt:
> "Have you run the Architecture Generator to identify Workaround Strategy candidates? If not, run `/ive-architecture-generator-custom` first — it produces the candidate the R1 skill designs from."

**R2 → Research Design:** After R2 is complete and PASS, prompt:
> "R2 is the last F1 requirement. Before beginning R4 (F2 starts here), run `/ive-research-design-custom` to design a unified fieldwork protocol that covers both R2 analysis and F2 block classification in one wave."

**R3 → FIT Verifier context note:** R3 solves the scaling cost bottleneck (working capital). Its primary impact is on the AOM's cost-of-goods and working capital structure, not on direct labor. Remind the user: "R3's solution should change the working capital cost per unit in the fin-sim (Groups 2–3). Update those inputs before running the FIT Verifier."

**R10 → Consistency Audit:** After R10 is marked complete, automatically prompt:
> "All 10 requirements complete. Run `/ive-consistency-audit-custom` before finalising the architecture — it checks cross-requirement dependencies that the sequential design process cannot detect."

---

## Resuming a session

If the user invokes `/ive-design-loop-custom` mid-project, ask:
> "Where are you in the requirement sequence? I'll show the status board and pick up from the last completed requirement."

Reconstruct the status board from whatever the user shares about completed requirements. Do not require them to re-run completed requirements — only the current incomplete one.

---

## Core discipline — prior outputs are inputs, not substitutes

Every requirement's diagnostic framework must be applied in full, regardless of how much earlier challenges appear to have addressed the current requirement. The intent of each challenge is maximisation: given the current BFF, how do we use this requirement's framework to extract the most value and remove the most cost?

**The rule:** a previous challenge's mechanism that happens to touch the current requirement is a bonus — it is not a reason to abbreviate the diagnostic. Discovering the overlap is the start of the work, not the end. The full sub-requirement sequence still runs.

**Applied:** if C3's independent assessment org addresses part of the R4 Want Block, that is good architecture. R4 still runs all five sub-requirements. R4 may surface additional conviction mechanisms C3 didn't cover. The framework exists to find what hasn't been found yet.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-design-loop-custom/SKILL.md` to modify
- **BALM skills R3–R10:** skills beyond `/balm-challenge-2-custom` may not yet exist in the vault. If a skill is missing, run the Design Loop steps manually: Diagnose (work through the requirement directly), Theorize (name the theory), Productize (update CTM/AOM), Simulate (FIT Verifier). The gate logic is the same.
- **FIT Verifier threshold:** 25% FMOS at each requirement gate. The full Phase I gate (after all 10 requirements) is 60% FMOS — a higher bar that accounts for the full operational model. The 25% check at each requirement is the early warning; the 60% check is the go/no-go for Phase II capital. Per-requirement bands: PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%. **Canonical FMOS gates (single source of truth):** `method/criteria-registry.md` — do not redefine bands locally.
- **CTM and AOM update mode:** see Section 5 (CTM) and Section 6 (AOM) inside each `balm-challenge-N-custom` skill — update mode is now venture-specific and lives in the challenge skill, not in the deprecated generic skills. Diagram format specs: `.claude/skills/shared/ctm-diagram-spec.md` and `.claude/skills/shared/aom-diagram-spec.md`.
- **Fin-sim:** if `/ive-fin-sim-custom` has been built, update Group 4 activities after each requirement before running the FIT Verifier. The fin-sim is the source of truth for the cost floor.
- **Related skills:** `/ive-architecture-generator-custom`, `/balm-challenge-1-custom` through `/balm-challenge-10-custom`, `/theory-of-change-custom`, `/ive-fin-sim-custom`, `/ive-fit-verifier-custom`, `/ive-research-design-custom`, `/ive-consistency-audit-custom`. Note: `/ive-ctm-custom` and `/ive-aom-custom` are deprecated — their guidance now lives inside the challenge skills.
