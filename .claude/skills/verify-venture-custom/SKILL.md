---
name: verify-venture-custom
description: The single verification agent for any IVE/BALM venture. One command, four passes — completeness, consistency, discipline (premature design + justification-mode tell), and synthesis (coherence + real-business analogue) — producing one combined design-integrity report. Replaces running verify-balm, the consistency audit, and the premature-design audit separately.
---

# Verify Venture

The one command for checking whether a venture's design record (VDR) holds up. Runs four passes over the venture's design work and produces a single design-integrity report with one top-line verdict and a prioritised action list.

This skill is the front door. It absorbs three checks that used to be run separately:

| Pass | Question | Was |
|------|----------|-----|
| 1 — Completeness | Are all 10 challenges solved to IVE standard? | `/verify-balm-custom` |
| 2 — Consistency | Do the 10 solutions contradict each other? | `/ive-consistency-audit-custom` |
| 3 — Discipline | Was each detail *earned* (no premature design), and did challenges *mutate* the BFF rather than justify it? | `/premature-design-audit-custom` (now folded in here) |
| 4 — Synthesis | Have the parts cohered into one business (real-business analogue), or is it a parts-bin? | (new — VA-1) |

Passes 1 and 2 reuse the criteria in `verify-balm-custom` and `ive-consistency-audit-custom` as engines — read those files for the detailed per-sub-requirement standards and the dependency-matrix method. Passes 3 and 4 are owned in full here.

> ⛔ **LOAD THESE BEFORE PASS 1 — MANDATORY (added 10 September 2026, Tom's ruling).**
>
> 1. `04-Projects/Family_High_Performance/context/va-design-discipline.md` — the discipline register.
> 2. `04-Projects/TMTH_Venture_Studio/Forge/WS1/criteria-registry.md` — **the specification this skill runs.** Its own opening line names this skill as the critic that runs it. Until today this file was never read here, and about twenty rows marked hard were invisible from the grader's side.
>
> **Do not load** `va-design-evidence.md`. It names ventures, figures and outcomes, and handing it to a verification run gives it the answer key.
>
> **The report must state, in the verdict panel: how many registry rows were applied, how many were not applicable to this venture and why, and how many could not be applied because the record does not carry the element they test.** A count of zero for the third is the claim to check hardest.
>
> **A rule the run was never handed may not dock it.** Where a registry row or a register rule appears in no design skill, score it, then list it separately under "scored on rules the run was never told" — that list is a defect in the method, not in the venture, and it routes to the Head of R&D.

Canonical discipline reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`.

---

## Step 0 — Identify venture and load source

Ask the user (or take from context):
1. **What venture are we verifying?** (one word — the slug for file paths and the report title)
2. **Where is the design record?** The authoritative record of completed design work. Typical locations:
   - `04-Projects/{slug}/workspace-transcription.md`
   - `04-Projects/{slug}/{slug}-workspace.md`
   - or a path the user provides.

Read the file fresh each run — never from memory or a memo HTML. Note its `Last updated:` date for the report header. If no record exists, ask the user for the design decisions to verify and capture them verbatim as ground truth.

Run all four passes, then build one report. Do not stop between passes unless Pass 1 finds the record essentially empty (then say so and stop — there is nothing to verify yet).

---

## Pass 1 — Completeness

**Question:** is every challenge (R1–R10) solved to IVE standard?

Apply the per-sub-requirement criteria in `verify-balm-custom` (Step 2). For each sub-requirement assign:

| Status | Symbol | Criteria |
|--------|--------|----------|
| Complete | ✅ | Meets IVE standard — specific, named, internally consistent. No open flags. |
| Partial | ⚠️ | Exists but directional only, missing a named theory, or flagged TBD. |
| Open | ❌ | No answer, placeholder, or contradicted by an open flag. |

A challenge's status is its **worst** sub-requirement status. Apply the at-scale check: a strategy that only works at launch volume, not at-scale, is Partial at best.

**FIT-staleness check (VA-74, Tom's ruling 1 Sep 2026 — mechanical, run per challenge):** compare the challenge's current component set (the CTM roster — derived from the model's transitions, including user and partner tracks) against the component set its FIT verdict records as computed on. **If they differ, the FIT is stale and the challenge cannot be Complete** — cap it at Partial ⚠️ with the finding "FIT-stale: component set changed since FMOS computation", whatever the prose says. A FIT block that records no component set at all is the same defect (unverifiable staleness) and takes the same cap. The check is always the FMOS of the product — the whole cost structure against the value ceiling — so a component added without an FMOS recompute means the verdict is measuring a stack that no longer exists.

Output of this pass: per-challenge status + the count complete / partial / open + any FIT-stale findings.

---

## Pass 2 — Consistency

**Question:** do the solutions contradict each other across challenges?

Hold all solved requirements in view at once and apply the cross-requirement method in `ive-consistency-audit-custom`: map the dependency matrix (which requirement's solution depends on or constrains which other's) and surface logical contradictions — a mechanism claimed in R5 that R8 assumes away, a cost stripped in R1 that R3 silently restores, a partner activated in R7 that R10 makes replaceable, and so on.

Output of this pass: a list of contradictions (or "none found"), each naming the two requirements in tension and the nature of the conflict.

---

## Pass 3 — Discipline (premature design + justification-mode tell)

**Question:** was each specified detail *earned*, and did the challenges *mutate* the BFF rather than *justify* it?

This pass has two parts.

### 3a — Premature-design audit (VA-2, traceability)

Every specified detail should trace back to a challenge that *required* it. Inventory every *specified* element (decisions, not open questions): product features and mechanisms, pricing/packaging/segments, customer/partner specifics, operating-model detail (AOM activities, roles, infrastructure), and each BFF statement. For each, assign:

| Verdict | Meaning | Recommendation |
|---------|---------|----------------|
| 🟢 Earned | Traces to a challenge that required it | Keep |
| 🟡 Premature | No challenge required it yet; specified ahead of evidence | Hold open — re-derive when the relevant challenge runs |
| 🔴 Unjustified | Specified for the appearance of completeness; anchors or constrains later challenges | Strip back to the open question it is hiding |

Premature ≠ wrong. Judge whether it was *earned*, not whether it happens to be right. Pair every 🔴/🟡 with the specific open question it is hiding — a flag without the underlying question is not actionable.

**Prime suspects:** a fully-formed BFF at R1/PCO that later challenges only describe; pricing or segment specificity before R2; features no challenge's Strategy required; AOM detail for activities no Strategy introduced.

### 3b — Justification-mode tell (VA-3, the root cause)

The defining check: **does the BFF actually change across the challenges, or is it fixed from R1 and only re-described?**

- Compare the BFF as stated at R1 against the BFF at the last solved challenge. If they are materially identical and the later challenges only add commentary, the VDR is in **justification mode** — challenges defended the BFF instead of trying to beat it. Flag loudly.
- For each challenge, check the "considered / not chosen" working (VA-4): did it generate candidate BFF mutations, or jump straight to "the existing BFF already handles this"? Zero mutations recorded = justification mode for that challenge.

Output of this pass: the traceability verdict counts (🟢/🟡/🔴 with the load-bearing items named) **and** the justification-mode verdict (did the BFF evolve? which challenges defended rather than mutated?).

---

## Pass 4 — Synthesis

**Question:** have the parts cohered into one business, or is it a parts-bin? (VA-1)

Take the latest BFF and run the synthesis test: can you name a *real, existing business* the venture now resembles — "this looks like [real business], because [the mechanism they share]"?

- **Clean analogue exists** → the parts have fused into a coherent whole. Name it.
- **No clean analogue** → flag it. The BFF is likely a semicoloned list of challenge solutions, not one architecture. Identify the missing architectural spine — the single mechanism whose removal would cascade failures across the most requirements.

**The synergy signal, read from the record rather than from your own eye (changed 10 September 2026).** Every requirement's output block carries a VA-106 line naming the earlier requirements its structural move also serves, and the mechanism for each. **Count the requirements whose VA-106 line names at least one other requirement.** Genuine synthesis usually shows several; total absence is a parts-bin tell.

**Where the VA-106 line is missing or blank, that is a Completeness defect on that requirement, not a Synthesis penalty.** Until 10 September 2026 this criterion was scored on a word that appeared in none of the design skills, so no run could satisfy it and every score carrying it was wrong. A run that predates the change cannot be docked on Synthesis for the absence — record it as "criterion not applicable: the run predates VA-106" and score Synthesis on the analogue alone.

Output of this pass: cohered / parts-bin verdict, the real-business analogue (or the flag + the missing spine).

---

## Scoring — the design-verification integrity score (0–100)

A verdict is not trendable; a number is. Emit one **design-verification integrity score** so WS1 can track whether the CF is improving run over run. This score measures *verification* — "did the design get built right against its requirements" — **not** validation ("is it proven in the world"). The two are separate (INCOSE); see the validation-maturity readout below. Compute four sub-scores, then combine — with gates, because two failures are structural, not incremental.

**Sub-scores (each 0–100):**
- **Completeness** = `(complete + 0.5 × partial) / total sub-requirements × 100`.
- **Consistency** = `100 − (15 × hard contradictions) − (5 × soft contradictions)`, floored at 0.
- **Discipline** = traceability `(🟢 + 0.5 × 🟡) / total specified details × 100`, **capped at 50 if justification-mode is detected** (Pass 3b). **A bare point estimate, a missing V/Val tag, or a missing convergence event on any load-bearing figure counts as a 🔴 unjustified detail** — it is a verifiability defect (the figure is not expressed to the TPM standard, `tpm-measurement-standard.md`), regardless of lifecycle stage. This is distinct from a validation parameter merely being unfielded — see the rule below.
- **Synthesis** = clean analogue + at least one requirement whose VA-106 line names another → 100; analogue but no declared synergy anywhere → 70; no analogue (parts-bin) → 30. **Score the VA-106 lines the run wrote.** For a run predating 10 September 2026 the synergy half is not applicable: score 100 for a clean analogue, 30 for a parts-bin, and say which rule you suspended.

**Overall = weighted average (25% each), then apply gates:**
- Justification-mode detected (VA-3) → overall **capped at 59** — the ceiling of NOT YET SOUND.
- Parts-bin, no real-business analogue (VA-1) → overall **capped at 60** — the floor of SOUND WITH GAPS.

> **VA-107 — a verdict cap is a band boundary, not a free number (added 10 September 2026, Tom's ruling).** Both caps used to be bare numbers, 50 and 60, appearing in no rule and ratified by nobody. **Each is now derived from the verdict bands beneath, and from the rule it enforces.** A design built by defending a fixed form factor may not read as sound at all, so its cap is the ceiling of the band below SOUND WITH GAPS. A design whose parts have not fused may not read better than its gaps, so its cap is the floor of SOUND WITH GAPS. **If a band boundary moves, both caps move with it.** A cap stated as a number that does not trace to a band is a defect. The change from 50 to 59 alters no verdict — both sit inside NOT YET SOUND — and it removes an unratified constant from the one number the capital decision reads. `[evidence: VA-107]`

The gates encode the headline rule: a "complete, consistent" VDR built by defending a fixed BFF is still not sound. Always show the four sub-scores alongside the overall — the shape of the failure matters more than the single number.

**The validation/verification rule (do not conflate):** unfielded *validation* parameters (WTP, adoption, completion rate — claims about real-world behaviour, confirmable only by demonstration/test) do **NOT** reduce any sub-score at a pre-operational gate. A CDR is a verification milestone; lacking operational evidence it cannot yet have is the correct gate state, not a defect. Track these instead in the validation-maturity readout. What *is* dockable (under Discipline) is a figure not expressed to the TPM standard — that is a verification failure (how the figure is stated), not a validation gap (whether the world has confirmed it).

**Validation-maturity readout (reported alongside the integrity score, never folded into it):** list every load-bearing validation parameter with its evidence method (examination/analysis/demonstration/test), elicitable/emergent tag, and convergence event. Summarise as one of: **pre-operational** (no operational evidence yet — expected at CDR) · **partial** (some demonstration evidence) · **confirmed** (operational test in-band).

**Score → verdict band:** ≥85 SOUND · 60–84 SOUND WITH GAPS · <60 NOT YET SOUND — each qualified by validation-maturity, e.g. "SOUND (verification) · validation-maturity: pre-operational." A sound, correctly-staged pre-operational design reads exactly that way — not penalised for being pre-pilot.

Report the overall score, all four sub-scores, **and** the validation-maturity readout in the verdict panel and the scorecard.

---

## The combined report

Generate one single-file HTML document. Save to:

```
04-Projects/{slug}/venture-verification-{YYYY-MM-DD}.html
```

Then open it.

### Structure

1. **Header** — "Design-integrity verification — {venture}", run date, source file + its last-updated date.
2. **Top-line verdict panel** (navy panel, white text) — one of:
   - **SOUND** — complete, consistent, disciplined, cohered.
   - **SOUND WITH GAPS** — broadly holds; named gaps to close.
   - **NOT YET SOUND** — a structural failure in one or more passes; not ready for a FIT gate or investor review.
   One sentence stating why.
3. **Four-pass scorecard** — one row per pass with a status tag (green/amber/red) and a one-line finding:
   - Completeness — X/10 complete
   - Consistency — N contradictions
   - Discipline — premature-design count + justification-mode verdict + TPM-record defects (bare points / missing V/Val tags)
   - Synthesis — cohered / parts-bin
3b. **Validation-maturity readout** — a separate panel (not a sub-score): the load-bearing validation parameters, each with evidence method + elicitable/emergent tag + convergence event, and the overall maturity (pre-operational / partial / confirmed). State explicitly that pre-operational maturity at a CDR is expected and does not reduce the integrity score.
4. **Per-pass detail** — one section per pass, rendering only what needs attention (mirror verify-balm: collapse clean areas to a single line).
5. **Prioritised actions** — ordered by structural impact. Ranking rule:
   1. Justification-mode (Pass 3b) first if present — it is the root cause; fixing it changes everything downstream.
   2. Then 🔴 unjustified detail (Pass 3a) and hard contradictions (Pass 2).
   3. Then completeness gaps (Pass 1), F1 before F2 before F3.
   4. Then 🟡 premature detail and synthesis flags.
6. **Recommended next session** — one paragraph: what to fix first and why; which items share a root cause.

### HTML boilerplate

Use the standard design system (DM Sans UI, Lora body, warm off-white bg, navy panel for the verdict). Reuse the CSS in `verify-balm-custom` (Step 3 boilerplate) plus tag colours — green `#e6f4ec`/`#166534`, amber `#fef9e6`/`#854d0e`, red `#fde8e8`/`#991b1b`. Verdict panel: `background:#0f2744; color:#fff`.

---

## Principles

- One run, one report. Do not send the user to three separate skills.
- The report reads top-down: verdict → scorecard → detail → actions. A reader who stops after the panel still knows whether the venture is sound.
- Verification reads and reports; it does not rewrite the VDR.
- A clean result over an early-stage VDR is itself suspect (premature closure to look complete) — say so.
- If Pass 3b finds justification mode, that is the headline regardless of the other passes — a "complete, consistent" VDR built by defending a fixed R1 BFF is complete and consistent and wrong.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/verify-venture-custom/SKILL.md` to modify
- Engines (read for detailed method): `verify-balm-custom` (completeness criteria), `ive-consistency-audit-custom` (dependency matrix)
- Canonical discipline reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`
- Replaces the standalone `premature-design-audit-custom` (folded into Pass 3)
- IVE source — the canon is a body of co-authored work, not one paper:
  - Simanis, E., Samani, S., Burnett, P. & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *Rediscovering Capitalism: How Blue-Chip Builders Created Transformative Impact and Profit.* YNOT Institute Working Paper 1, Queens' College Cambridge
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *The Business Architecture: The Hidden Code of Industry Disruption.* YNOT Institute Working Paper 2, Queens' College Cambridge — the Business Architecture Framework
  - Simanis, E. et al. (2024). *The Core Business Archetype* (Jan); *Engineering New Market Ventures* (Apr); *The Market Creator's Dilemma* (Nov)
  - Simanis, E. (2025). *Built to Hold* — the FMOS gates; Simanis, E. & Donohue, K. (2025). *Deciphering the Market Creator's Dilemma.* MIT Sloan Management Review
  - Attribution rule (WS1 feedback log, 5 and 17 Sep 2026): Tom Manuel is a co-author on the 2023 papers; "co-developer of the method" is not supported. TMTH's own additions are the WS1 standards, the VA register, the circle end-state and the direction rule
