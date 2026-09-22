---
name: ive-build-pilot-custom
description: IVE build phase (CDR→TRR). Takes a CDR-complete detailed design (buildable process definitions + asset specs + interfaces) and drives it to a built, workflow-verified pilot ready to launch. Risk-orders a slice build, builds and tests each process via functional best-practice bounded by its spec, produces the assets those processes run on, integrates into the Last-Mile Unit and proves the synthesis holistically against the FMOS, then produces the Minimum Representative Pilot plan + a failable launch-readiness gate. Does NOT design (that is /ive-detailed-design-custom), run the real-world MRP, or scale.
---

# IVE — Build the Pilot (CDR → TRR)

Takes a **CDR-complete detailed design** and builds it down to a **pilot venture ready to launch** — processes built, verified and runnable by a real operator, integrated into the Last-Mile Unit, the Minimum Representative Pilot designed and ready to run in real conditions.

**The problem it solves:** detailed design (`/ive-detailed-design-custom`) produces buildable process definitions, asset specs, and interfaces — but not a built thing. This skill builds them, verifies the synthesis holistically, and readies the pilot. It does **not** design; if a "how should this work?" question is still open, that is a detailed-design (or architecture) gap — go back, don't decide it here.

**When to run:** after CDR — detailed design is complete. Run it via `/ive-conductor-custom` once the venture sits at the CDR→TRR boundary.

**Output:** a **pilot-readiness package** (HTML, house style) — risk-ordered slice map, process build+test record, LMU integration result, the MRP plan, and a failable TRR gate verdict. Plus VDR build/validation entries.

**Handoff to:** the real-world MRP run (Phase 8 / ORR) — which this skill prepares but does not execute.

---

## Where this fits — the right side of the V

```
Architecting (BALM + models)   → [PDR]   what / who / how-much
   ↓
Detailed design                → [CDR]   process definitions + asset specs + interfaces   (/ive-detailed-design-custom)
   ↓  ▼ BUILD POINT ▼
THIS SKILL: build → integrate → MRP design   → [TRR]   ready to launch
   ↓
Real-world MRP run             → [ORR]   (NOT here)
```

Source: IVE V-Model (`TMTH_IVE_Wiki/wiki/Methodology/V_Model_Process.md`), Phase II Steps 5–7. Exemplar of a good right-side artifact: a venture validation plan (risk-ordered slices, T4 flows, go/no-go gates).

**Founding principle (load-bearing):** *build and test the smallest runnable process before integrating processes into the workflow.* The smallest runnable unit is a process, not an artefact — test it first, then integrate. This front-loads validation and avoids burning capital testing an architecturally-broken product at the workflow level. 85% of cost is locked at the design stage — so the pilot's job is not to *discover* the model, it is to *verify the architecture survives contact with reality.*

---

## ⛔ Precondition gate — do not start without a CDR-complete detailed design

This skill builds what detailed design specifies. If the detailed design is incomplete, it builds the wrong thing — or starts re-designing, which is out of remit. Confirm the **detailed-design package** exists on disk (`{venture}-detailed-design-*.html`) and contains:

- [ ] **A buildable definition for every process** (named function + decision logic + exceptions + handoffs + SOP — an operator in that function could run it cold)
- [ ] **An acceptance criterion for every asset, set by the process that runs it**
- [ ] **Interface specs to buildable depth, with an owner named on each side**
- [ ] **CDR gate PASS** recorded in the VDR — no open architectural decisions. *(A CONDITIONAL CDR qualifies only when every condition is explicitly non-blocking for the build; carry the conditions into the TRR record.)*

If any is missing → **STOP.** Return to `/ive-conductor-custom`; the venture has not cleared CDR — run `/ive-detailed-design-custom` first. A pilot built on an incomplete design is the most expensive mistake on the right side (change after build = ~100× design-stage cost; Sheldon et al. 1990).

---

## Step 1 — Inherit the detailed design & risk-order into slices

Take the detailed-design package as given — process definitions, asset specs, interfaces, org/role map. **Do not redesign.** Then cut the venture into **slices** — coherent bundles of processes + roles — and order them **riskiest-first**: the slice whose failure kills the venture fastest, and is cheapest to test, goes first.

For each slice produce:
- **Slice name + why it's here** (the assumption it kills)
- **Risk tier:** T4 (highest — would break the architecture) · T3 (would dent it) · T2 (refinement)
- **Min-build:** the smallest build that genuinely tests the slice — nothing more
- **The flows it exercises**, with the **T4 (highest-risk) flows named and their FAIL condition stated** — "this slice FAILS if [observable result]"
- **A go/no-go gate** for the slice

Build T4 slices before T2. A pilot that validates the comfortable flows first and the dangerous ones last has learned nothing when it runs out of money.

A slice whose only real test is a counterparty signing is still a slice — build its materials, and make its test the MRP entry gate, stated as such.

---

## Step 2 — Build each slice via functional best-practice, bounded by the spec

For each slice, riskiest first, build its processes using the **best practice of the functional area its primary 4-D class maps to**, and **stand each process up** for the roles detailed design named:

| 4-D class | Functional best-practice playbook |
|-----------|-----------------------------------|
| Working Product | product / engineering / operations |
| Communications Product | marketing + sales |
| Payment Product | finance / payments |
| Partner Product | partnerships / BD |

**Bounded by the acceptance criterion (load-bearing).** Functional best-practice is the *how*; the detailed-design spec is the *what it must do*. A process that is excellent by its discipline's own metric (engagement, delight, conversion) but misses its acceptance criterion is a **FAIL** — the "users like it" trap one level up. An asset has no acceptance criterion of its own: it inherits the one set by the process that runs it, and is never signed off independently. Build multi-purpose processes cross-functionally; the primary discipline leads, the others contribute.

Per process: build the min-version, **test against the acceptance criterion** → PASS / PARTIAL / **FAIL**. A FAIL is an architecture/design problem — back to detailed design or the model stack, not a build tweak. Check a real operator can run each process end to end — this is the first read on whether it actually hits the ARM's assumed rate (it narrows that range toward an actual). Digital/AI processes and the assets they run on: the skill builds/orchestrates directly. Human/partner processes: produce the build+test spec for execution. Run the slice's go/no-go gate before starting the next slice.

**Step 2b — representation audit (every external-facing artifact).** Acceptance criteria test *function*; this audits *representation*. Before any external use, run the audit pair: **truthfulness** (no claim exceeds the canonical record) and **full-BFF expression** (the artifact expresses the whole BFF — pitch = complete expression as mechanism; operational touchpoint = situated and non-contradicting; process doc = one situating paragraph). Register every external artifact as a configuration item in a CM register (baseline version expressed · audit-pair status · propagation on any baseline change — no baseline change is complete until every CI is re-audited or marked unaffected). Standard basis: configuration management (EIA-649 / ISO 10007), PCA-style audit, production-representative test articles.

---

## Step 3 — Holistic integration test (prove the synthesis)

Assemble the validated slices into the full **Last-Mile Unit** and run the whole operating model — attract → adopt → pay → retain, partner integration, position processes live. Verify the **integrated unit hits the modelled FMOS**.

This is where the synthesis is actually proven — **holistically, not requirement-by-requirement** (processes are multi-purpose; they can only be validated together). If integration breaks the FMOS, that is a workflow-level architecture failure — back to the model stack, not a patch.

Standing integration item: the **capacity-vs-load check** — standing operator capacity ÷ expected volume at full attachment. A ratio below 1 converts a staffing preference into a contractual phasing clause; run it before any go-live volume is agreed.

---

## Step 4 — Design the Minimum Representative Pilot

Produce the MRP plan — the real-conditions test that will validate unit economics. A valid MRP meets **three criteria**:
1. **Tests key operations** — exercises all critical (T4) workflows, not just the comfortable ones;
2. **Representative context** — pilot population, geography, and conditions reflect the *at-scale* target, NOT a friendly early-adopter pocket;
3. **Reflects seasonality** — long enough to capture the relevant full cycle.

The MRP plan states: pilot population + geography, duration, the workflows it exercises, the **unit economics / FMOS it will validate**, the **go/no-go gate (NPV > hurdle, or FMOS holds in real conditions)**, and the **FAIL conditions** (the T4 results that would force an architecture revision). It targets the **widest × most-FMOS-sensitive ranges** first — the pilot's job is to narrow those to actuals.

The MRP plan must also carry the pilot's **test logic** — the MRP is an experiment on the architecture, instrumented through standard processes:

1. **The activity→bound→premise attribution map** — for every key AOM activity: its fin-sim bound · the BALM premise that makes hitting it possible · the diagnosis if it fails, routed to its challenge. A by-the-book process that fails is an architecture diagnostic, not an execution failure (a Buy Block in a standard sales process falsifies the C6 answer — it is not fixed by selling harder).
2. **The no-heroics rule** — every activity must succeed by the standard playbook at modelled cost (principal-hours priced). Success bought by founder heroics is out-of-bounds performance masking an architecture failure, and validates nothing. Heroics are detectable: busted hour-bounds and off-library representations.
3. **The two-layer verdict** per activity — performance (hit the bound?) × attribution (by the standard process at modelled cost?). Only PASS/PASS validates the architecture. A FAIL with a clean diagnosis is a *successful pilot outcome*: the architecture answering the question the pilot asked, at pilot cost instead of scale cost.

This skill *designs and readies* the MRP. It does not run it — running it is Phase 8 / ORR, in the real world.

---

## Step 5 — Launch-readiness gate (TRR) — failable

The venture is "ready to launch" only when this gate clears. Check every item; a gate that cannot fail is theatre.

- [ ] Every process built and **verified against its acceptance criterion** (no Open, no unresolved FAIL), and every asset it runs on verified against the criterion that process sets
- [ ] Every role's **processes stood up** and runnable by a real operator at pilot volume
- [ ] The integrated LMU workflow verified against the modelled unit economics
- [ ] Each T4 (highest-risk) assumption has a **live kill-test** in the MRP — the pilot can actually disprove it
- [ ] The MRP is designed with **representative (not friendly) context** + seasonality + FAIL conditions + a go/no-go gate
- [ ] Open risks named, with the one most likely to fail the pilot flagged as the #1 watch item

**Verdict:** **READY** (all clear) · **CONDITIONAL** (ready with named, recorded conditions) · **NOT READY** (name the blocker and route back — to the build, the integration, or detailed design). Never round a CONDITIONAL up to READY.

---

## Output — the pilot-readiness package (artifact contract)

Produce an HTML package (house style: DM Sans + Lora, `#f5f4f1` bg, `#0f2744` navy panel) saved to `04-Projects/{venture-slug}/{venture}-pilot-readiness-{date}.html`, containing:
1. **Readiness verdict panel** — navy, prominent: TRR verdict + the one watch item
2. **Risk-ordered slice map** — slices, tiers, min-builds (the slice-map format in `/ive-build-pilot-custom`)
3. **Process build+test record** — each process, its acceptance criterion, PASS/FAIL/PARTIAL, and the assets it produced
4. **Operator run record** — each role's processes run end to end by a real operator, with the first read on the rate vs the ARM
5. **LMU integration result** — integrated unit economics vs the modelled FMOS
6. **The MRP plan** — the three criteria, the go/no-go gate, the FAIL conditions, the ranges it will narrow
7. **Launch-readiness checklist** — the TRR gate, ticked

Then write the build/validation entries into the venture VDR.

**No prose-only "ready."** A readiness package without a verified build record and a failable MRP design is *in progress*, not ready — the same artifact-contract discipline the conductor enforces on the left side.

---

## Discipline rules

**Build, don't design.** Detailed design is done (CDR). If a "how should this work?" question is open, that is a design gap — back to `/ive-detailed-design-custom`, not decided here.

**Build and test the smallest runnable process before integrating into the workflow.** Always. Integrate only validated processes.

**Test against the process definition, not satisfaction.** The acceptance criterion is the process's contribution to the integrated FMOS — "they liked it" is not a pass.

**Functional best-practice serves the architecture, not its own metric.** A process excellent by its discipline (engagement, delight, conversion) but failing its acceptance criterion is a FAIL.

**Riskiest slice first.** Order by what kills the venture fastest and is cheapest to test. Validate T4 before T2.

**Representative, not friendly, pilot context.** A pilot in a comfortable pocket that doesn't reflect at-scale conditions has validated nothing — the single most common right-side failure.

**A process FAIL is an architecture/design problem, not a build tweak.** Return to detailed design / the model stack — do not patch around a failed acceptance criterion.

**Don't pass a gate you didn't clear.** CONDITIONAL ≠ READY. Conditions are blockers to be recorded and resolved.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-build-pilot-custom/SKILL.md` to modify
- **Methodology reference:** `TMTH_IVE_Wiki/wiki/Methodology/V_Model_Process.md` (Phase II, Steps 5–7)
- **Exemplar (what a good right-side artifact looks like):** a venture validation plan — risk-ordered slices, T4 flows with FAIL conditions, go/no-go gates
- **Upstream:** `/ive-detailed-design-custom` (CDR) · **Downstream:** real-world MRP run → ORR
- **Registered in** `/ive-conductor-custom` routing table for the CDR→TRR phase
- Workstream: Forge build-tooling (a conductor-routed skill) — NOT WS1 (WS1 refines the architecture-*producing* skills, scored by `/verify-venture-custom`; this is the build/verify layer)
