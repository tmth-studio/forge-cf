---
name: ive-conductor-custom
description: IVE Conductor — knows where you are in the INCOSE/IVE V-model, what gate you're approaching, what's blocking it, and what to do next. Run at the start of any IVE session to orient before picking up work.
---

# IVE Conductor

Tells you exactly where a venture sits in the INCOSE/IVE V-model, what is blocking the next gate, and which skill to run next — with the reason why visible at every step.

**The problem it solves:** IVE has many skills. Without a conductor, you get handed tasks without understanding why they're the next thing, what gate they're serving, or what the full horizon looks like. The conductor makes the process visible.

---

## ⛔ The deterministic run — same inputs, same process, same output (overrides everything below)

The conductor is a **state machine, not a thinking partner.** Every run gathers the **same inputs**, executes the **same procedure**, and produces the **same output**. Steps 1–5 below are the *reference detail*; **this section is the operating procedure and it wins** wherever they differ.

If you find yourself reasoning about what the venture *should* do, weighing a strategic option, inventing a gate or decision, or proposing a step out of order — **stop. You have left the process.** The next step is never reasoned to; it is the next incomplete row of the ledger.

### A — Fixed inputs (gather these every run, in this order — nothing else)
1. The venture slug + project folder.
2. `ls` the folder; record which artifacts exist, by challenge state C[N]: `*-vdr*.html`, `*-ctm-at-C[N].html`, `*-aom-at-C[N].html`, `*-arm-at-C[N].html`/`*-fin-sim-at-C[N].html`, `*-consistency-audit-*.html`, latest `conductor-*.html`.
3. Read the latest VDR and latest conductor report — nothing else decides position. **Disk artifacts are the only source of truth; never infer position from how "done" a brief reads.**

### B — The canonical step ledger (the process — never reordered, never added to)

Walk top to bottom. A step is COMPLETE only when its completion artifact exists on disk.

| # | Step | Completion artifact |
|---|------|--------------------|
| P0 | Investment parameters (period, IRR, geography, industry) | VDR PCO entry |
| P1 | Path routing (A / B) | VDR |
| P2 | Architect's lens (Step 2c) | VDR |
| P3 | Use/impact cases generated (≥6) | VDR |
| P4 | Evaluate + select PCO (market-creation margin > 30%) | VDR PCO statement |

Then for **each** challenge R1…R10 the **same** sub-sequence (C[n]):

| # | Sub-step | Completion artifact |
|---|----------|--------------------|
| a | SR1 conventional BFF | VDR |
| b | SR2 CLO (**operation, not resource**) | VDR |
| c | SR3 Workaround ToC (citable) | VDR |
| d | SR4 Workaround strategy | VDR |
| e | SR5 BFF(C[n]) + CLO gate pass | VDR |
| f | CTM-at-C[n] | `*-ctm-at-C[n].html` |
| g | AOM-at-C[n] | `*-aom-at-C[n].html` |
| h | ARM + fin-sim-at-C[n] | `*-fin-sim-at-C[n].html` |
| i | FIT gate (computed FMOS, failable) | fin-sim verdict + VDR FIT entry |

**Challenge R[n] is COMPLETE only when f–i exist. SR1–SR5 prose without f–i = IN PROGRESS, not done.**

**After R10 — the fixed-point pass (VA-161, RD-040 (Head of R&D, 21 Sep 2026, object-after 23 Sep 12:30)).** The loop over the ten requirements does not end at a count. It ends at a **fixed point**: one full C1–C10 pass that changes no answer — no verdict moves, no BFF delta, no row of the challenge input ledger (VA-132) re-versioned. The ledger is the instrument: a pass is "no change" when every consumer's input version equals the current version. Each pass is scoped to the customer of record; the customer-facing challenges (C2, C4, C5, C6, C7, C8) are re-run and the others are re-verified from the ledger. The authority file states `fixed_point: pass [n], [date]`; PDR may not be called before that line exists.

| # | Sub-step | Completion artifact |
|---|----------|--------------------|
| j | Fixed-point pass after R10 — full C1–C10 pass, no answer changed, ledger unchanged | authority file line `fixed_point: pass [n], [date]` |

Gates/audits in sequence: after R3 → **AR** (FIT verifier on F1, computed) · after R10 → fixed-point pass (VA-161) → verify-balm → consistency audit = **PDR** · after PDR → detailed design (buildable process definitions + asset specs + interfaces, via `/ive-detailed-design-custom`) = **CDR** · then build pilot (`/ive-build-pilot-custom`) = **TRR** · then MRP = **ORR**.

### C — Determination algorithm (run exactly this, every time)
1. Walk the ledger top to bottom.
2. The **first** step whose completion artifact is absent = the **CURRENT step**.
3. The **NEXT ACTION is to complete exactly that one step** — not the next one, not a related decision, not a strategic question.
4. The CURRENT GATE = the gate that step sits under.
5. Produce the fixed output (Step 3 template, every field filled). Stop.

### D — Anti-variation rules (hard)
- **The next step is always the next incomplete ledger row.** Never invent a step, gate, or decision not in the ledger.
- **A step's only legal inputs are upstream.** Each ledger step consumes ONLY (a) the completion artifacts of *prior* ledger rows, and (b) for a challenge's first sub-step, the PCO. **A step may never require an artifact that a *later* ledger row produces.**
- **Input-legality test — run before asking the user anything, or before treating anything as "needed" to proceed:** *does a later ledger row produce this thing?* If yes → you may NOT require it. Proceed on the current step's own conventional/preliminary base. The "ask the user for a named input" allowance covers ONLY genuine upstream inputs (e.g. the investment parameters at P0) — never a downstream output.
- **R1 is customer-agnostic (the canonical instance of the rule above).** The customer's identity, value bottleneck, attendant routines, KMC, and value ceiling are **produced by R2** — so they are never inputs to R1. R1 builds the CTM from *standard industry practice*, applies the workaround, and uses a *preliminary PCO WTP* for the FIT (refined at R2). **If you are about to ask "who is the customer / what do they pay" to build R1 — stop; that is R2's output.** (This exact error was made twice on 21 June 2026: first as a "decision gate", then re-smuggled in as a "required input for the CTM". Both are the same violation.)
- **Never substitute a strategic decision for a process step.** Route to the next ledger step; do not pause the process to "decide the direction."
- **Never jump levels or reorder.** If a venture is re-leveled (e.g. venture → studio), the ledger restarts at P0 for the new level; do not carry a half-built lower-level stack into a higher-level gate.
- **Same output every time** — only the Step 3 template, every field present, nothing added.

---

## The V-model — IVE mapped to INCOSE

```
LEFT SIDE (decomposition — design)
──────────────────────────────────
Phase 1 — Stakeholder Needs        → IVE: PCO selection                   [Gate: PCOR]
Phase 2 — System Requirements      → IVE: BALM F1 (R1–R3) + FIT Verifier  [Gate: AR]
Phase 3 — Architecture Definition  → IVE: BALM F2+F3 (R4–R10)             [Gate: PDR]
Phase 4 — Design Definition        → IVE: CTM + AOM + ARM + Fin-Sim        [Gate: CDR]
                         ▼ BUILD POINT ▼
RIGHT SIDE (integration — validate)
────────────────────────────────────
Phase 5 — Implementation           → IVE: Build + test individual processes
Phase 6 — Integration              → IVE: Assemble validated processes into LMU
Phase 7 — System Verification      → IVE: Full workflow integration test    [Gate: TRR]
Phase 8 — Validation               → IVE: MRP — unit economics in real conditions [Gate: ORR]
```

### Gate definitions

| Gate | Full name | Governing question |
|------|-----------|-------------------|
| **PCOR** | PCO Review | Is this the right problem, for the right customer, at a scale that can pay back capital? |
| **AR** | Architecture Review | Is there a plausible F1 architecture — workaround, value ceiling, scaling path — with positive FMOS headroom? |
| **PDR** | Preliminary Design Review | Are all 10 BALM requirements designed, FMOS ≥ 60%, and the consistency audit PASS? |
| **CDR** | Critical Design Review | Is every process detailed-designed to buildable depth — a buildable definition per process, an acceptance criterion per asset set by the process that runs it, interfaces specified with an owner on each side — with no open architectural decisions? |
| **TRR** | Test Readiness Review | Are individual processes verified and the workflow integration test ready to run? |
| **ORR** | Operational Readiness Review | Has the MRP validated unit economics, and does NPV exceed the hurdle rate? |

---

## Step 1 — Identify the venture

Ask the user which venture to orient on, or infer from context.

For each venture, the conductor needs to find:
- Latest BALM verification report (`04-Projects/{venture}/balm-verification-*.html` or workspace transcription)
- Latest consistency audit report (`04-Projects/{venture}/consistency-audit-*.html`)
- Latest design memo (`04-Projects/{venture}/*.html` — look for "design-memo")
- Workspace transcription (`04-Projects/{venture}/workspace-transcription.md` or similar)
- Fin-sim status (`04-Projects/{venture}/` — look for fin-sim or resourcing model files)
- AOM status (`04-Projects/{venture}/{venture}-aom-*.html` or similar)
- VDR — the running design record (`04-Projects/{venture}/{venture}-VDR*.html` or VDR changelog)
- Model-stack files (`{venture}-ctm-at-C*.html`, `{venture}-aom-at-C*.html`, `{venture}-fin-sim-at-C*.html`) — note which challenge state (C[N]) each reflects. **Their absence means the model stack has not been built — even if design prose / a brief exists.**

For a venture's current gate position, read in this order:
1. Latest conductor report: `04-Projects/{venture}/conductor-{latest-date}.html` — the most recent conductor run is the authoritative process position summary
2. Latest CDR package: `04-Projects/{venture}/{venture}-cdr-package-{date}.html` — gate entry criteria, FMOS results, open items, and CDR verdict
3. V-model methodology reference: `04-Projects/TMTH_Venture_Studio/TMTH_IVE_Wiki/wiki/Methodology/V_Model_Process.md` — canonical IVE V-model phases and gate definitions

Note: `incose-process-2026-05-21.html` was referenced here but was never created. The CDR package and conductor report are the operative evidence sources.

---

## Step 2 — Determine current gate position

Work through the gates in order. A gate is **passed** when its governing question is fully answered with documented, defensible evidence. A gate is **in progress** when some evidence exists but not all exit criteria are met. A gate is **not started** when no design work has begun for that phase.

### What counts as "complete" — the artifact contract (read before judging any gate)

A challenge or phase is **not complete because a design memo, brief, or prose write-up exists.** Diagnostic prose is the *start* of a challenge, not the end of it. For any BALM challenge (R1–R10) to count as complete, the conductor must confirm these artifacts exist **on disk** for that challenge:

- **VDR entry** — the requirement's solution recorded in the venture's Venture Design Record (`{venture}-VDR*.html` / VDR changelog)
- **CTM** at the challenge state — `{venture}-ctm-at-C[N].html`
- **AOM** at the challenge state — `{venture}-aom-at-C[N].html`
- **ARM + fin-sim** at the challenge state — `{venture}-fin-sim-at-C[N].html`, with the four cost layers (PVC / RC / SC / IC)
- **A computed FIT/FMOS** derived from that fin-sim — a number that *could have failed the gate*, with its pivot trigger stated

**A directional, structural, or "illustrative" FMOS written in prose is NOT a FIT pass.** If the only evidence is a brief with a hand-reasoned margin, the challenge is **in progress**, not complete — the model stack and VDR have not been built. The conductor must check disk for the files above and, if absent, report the gate as blocked on "model stack + VDR not built", however finished the prose looks.

This contract exists because of a logged failure (20 June 2026): a full R1–R3 brief was produced with a directional FMOS and *no* CTM/AOM/ARM/fin-sim/VDR — the design looked done, but the process had not run. Catching exactly this is the conductor's job.

### PCOR exit criteria
- [ ] PCO selected — problem, customer segment, and scale defined
- [ ] At-scale market size estimated (TAM or SAM with source)
- [ ] First-principles filter passed (addressable, scalable, viable)

### AR exit criteria
- [ ] R1 (Workaround Strategy) complete — CLO identified, BFF described, ToC named
- [ ] R2 (Efficacy) complete — KMC quantified, price ceiling set, Attendant Routines mapped
- [ ] R3 (Scaling) complete — scaling mechanism designed, working capital solution identified
- [ ] **Model stack built for R1–R3** — CTM, AOM, ARM/fin-sim at each challenge state, plus VDR entries (per the artifact contract above). Prose design alone does **not** satisfy AR.
- [ ] FIT Verifier PASS — FMOS ≥ 60% on F1 architecture, **computed from the fin-sim (not a directional estimate)**, able to fail, with pivot trigger stated

### PDR exit criteria
- [ ] All 10 BALM requirements designed to IVE standard
- [ ] FMOS ≥ 60% confirmed (ARM-derived cost floor, not estimated)
- [ ] BALM verification audit: all 10 challenges COMPLETE (no Partial or Open)
- [ ] Consistency audit: PASS (or PASS WITH CONDITIONS — all conditions resolved)
- [ ] Fixed point reached (VA-161): one full C1–C10 pass changed no answer; the authority file states the pass number and date

### CDR exit criteria
- [ ] CTM complete — customer state changes mapped across full journey
- [ ] AOM complete — at-scale operating model showing actors, flows, and LMU structure
- [ ] ARM complete — cost structure derived from AOM (PVC / RC / SC / IC layers)
- [ ] Financial simulation complete — unit economics, cash flow timeline, FMOS at LMU level
- [ ] Detailed design complete (run `/ive-detailed-design-custom`) — for **every process** a buildable definition (named function + decision logic + exceptions + handoffs + SOP, an owner on each side of every interface — an operator in that function could run it cold), and for **every asset** the acceptance criterion set by the process that runs it
- [ ] Interfaces specified to buildable depth — the contract each connection needs to be built independently
- [ ] Integrated process set, not a 1:1 requirement→component map (a clean 1:1 signals a badly-integrated BFF, not completeness)
- [ ] No open architectural decisions — a still-open "how should this work?" is a PDR gap, back to the model stack
- [ ] Build sequence agreed — which slice is built first, and why

### TRR exit criteria
- [ ] Each process built and individually tested against its acceptance criterion
- [ ] Integration test plan written — what the end-to-end workflow test will verify

### ORR exit criteria
- [ ] MRP (Minimum Replicable Pilot) run — real customers, real conditions
- [ ] Unit economics validated at actual cost and actual settlement rate
- [ ] NPV exceeds hurdle rate at conservative assumptions

---

## Step 3 — Produce the conductor report

This is the **one fixed output** — every field present, in this order, nothing added or omitted. The NEXT ACTION names exactly one ledger step (the CURRENT step from the determination algorithm), never a strategic choice. Format:

```
VENTURE: [name]
CURRENT POSITION: [gate name] — [description of where in the gate]
GOVERNING QUESTION: "[the gate's governing question]"

WHAT'S DONE
  ✓ [evidence item]
  ✓ [evidence item]
  ...

WHAT'S BLOCKING THE NEXT GATE
  ✗ [specific missing item] — [one sentence on why it matters for the gate]
  ✗ [specific missing item]
  ...

NEXT ACTION
  → [specific action] — [one sentence on why this resolves the blocker]
  Skill: /[skill-name] | Session: [description if no skill exists]

HORIZON (after this gate)
  → CDR: [what that requires]
  → TRR: [what that requires]
  → ORR: [what that requires]
```

---

## Step 4 — Route to the next skill

### Before launching any build or challenge — mandatory pre-launch gate

The conductor must not hand off into a challenge/build without first asking the user this, in plain conversation (**not** a popup):

> **"Full research, or flagged placeholders?"**
> - **Full research (default, recommended):** before/while building the model stack, go gather and validate the real inputs — success rates, costs, willingness-to-pay, volumes — so the FIT runs on data that can be trusted.
> - **Flagged placeholders (stopgap only):** build the stack on clearly-flagged illustrative numbers for a directional FIT now, research deferred.

State plainly that **full research is the default and almost always the right choice** — placeholders produce a FIT that cannot be trusted and has to be redone, so they are only worth it to sanity-check structure before committing research time. Do not assume; wait for the answer, then pass the chosen mode into the challenge skill.

At hand-off, also state the **artifact contract** the challenge must produce (VDR + CTM + AOM + ARM/fin-sim + computed FIT, per Step 2) — so "done" is unambiguous before work starts.

### Routing table

Based on the blocker, name the specific skill or session. Reference the full IVE skill set:

| What's needed | Skill |
|--------------|-------|
| PCO selection | `/balm-pco-custom` |
| Any BALM requirement (R1–R10) | `/balm-challenge-{N}-custom` |
| FIT Verifier (mid-BALM gate) | `/ive-fit-verifier-custom` |
| BALM completeness check | `/verify-balm-custom` |
| BALM consistency check | `/ive-consistency-audit-custom` |
| Customer Transformation Model | `/ive-ctm-custom` |
| At-Scale Operational Model | `/ive-aom-custom` |
| Financial simulation | `/ive-fin-sim-custom` |
| Research design (for any requirement) | `/ive-research-design-custom` |
| Design loop (for any requirement) | `/ive-design-loop-custom` |
| Architecture generator (overview) | `/ive-architecture-generator-custom` |
| Theory of Change (for any requirement) | `/theory-of-change-custom` |
| **Detailed design — processes to buildable depth (PDR→CDR)** | `/ive-detailed-design-custom` |
| **Build the pilot — build → integrate → MRP (CDR→TRR)** | `/ive-build-pilot-custom` |

The CDR-layer detailed design (process definitions, asset specs, interfaces) is now a skill — route to `/ive-detailed-design-custom`, not a bespoke session. If a blocker genuinely has no skill (e.g. a one-off build-sequence decision), name it as a "Session" and describe what it should produce.

---

## Step 5 — Save the conductor report

Produce an HTML conductor report and save to:
`04-Projects/{venture-slug}/conductor-{date}.html`

Use the standard design system (DM Sans + Lora, #f5f4f1 background, #0f2744 navy panel).

The report contains:
1. **Current position panel** — navy, prominent, gate name + governing question
2. **Progress tracker** — all six gates in a row, colour-coded (✓ passed / → current / · not started)
3. **Done / Blocking / Next action** — the three-section status block
4. **Horizon table** — the remaining gates, what each requires, estimated sessions

Open in browser after saving.

---

## Conductor discipline rules

**Never assign work without showing the gate it serves.** Every task the conductor names must be traceable to a specific gate exit criterion. If you cannot trace a task to a gate, it does not belong in the next action.

**PDR before CDR, always.** The conductor does not route to CTM, AOM, ARM, or fin-sim work until all PDR exit criteria are met. Operational design on an incomplete or unaudited architecture produces the wrong system. The gate sequence is load-bearing.

**Conditions must be resolved, not carried forward.** A PASS WITH CONDITIONS from the consistency audit is not a PDR pass. The conditions are blockers. Name them explicitly and route to their resolution before proceeding.

**The conductor is a read-only observer.** It diagnoses and routes. It does not make design decisions, modify requirement solutions, or run other skills directly. Its output is always a report and a routing instruction — not a design session.

**A directional FMOS is not a FIT pass.** Prose with a hand-reasoned margin does not complete a challenge. The model stack (CTM → AOM → ARM → fin-sim) must exist on disk and the FIT must be computed from it — a number that could have failed. When judging a gate, check the files; if they are missing, the challenge is *in progress*, not done. See the artifact contract in Step 2.

**Never route into a challenge without the pre-launch gate.** Always ask "full research or flagged placeholders?" (default: full research) and state the artifact contract before hand-off. See Step 4.

**Determinism is the master rule.** Same inputs, same process, same output, every run — per "The deterministic run" section at the top, which overrides any improvisation here. The next step is the next incomplete ledger row; it is never reasoned to, chosen strategically, or pulled forward from a later step.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-conductor-custom/SKILL.md` to modify
- **Process reference (primary):** `04-Projects/TMTH_Venture_Studio/FinTech_Justice/conductor-{latest-date}.html` — most recent conductor report is the authoritative position summary
- **Process reference (CDR evidence):** the venture's latest CDR package — gate criteria, FMOS, open items
- **Process reference (TRR preparation):** the venture's validation plan — slice-ordered validation plan; which slices to build and test first, T4 flows per slice, exit gates, and what is explicitly deferred until each gate clears
- **Process reference (methodology):** `04-Projects/TMTH_Venture_Studio/TMTH_IVE_Wiki/wiki/Methodology/V_Model_Process.md` — canonical V-model phases and gates
- **Model stack reference:** `04-Projects/TMTH_Venture_Studio/TMTH_IVE_Wiki/wiki/Methodology/Model_Stack.md` — the six IVE models and their dependency chain
- **Run at the start of every IVE session** to orient before picking up work
- **Related skills:** all `/balm-challenge-*`, `/verify-balm-custom`, `/ive-consistency-audit-custom`, `/ive-fit-verifier-custom`, `/ive-ctm-custom`, `/ive-aom-custom`, `/ive-fin-sim-custom`
