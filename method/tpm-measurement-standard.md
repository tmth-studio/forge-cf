# TPM Measurement Standard — how every load-bearing figure is expressed

**Owner:** Head of Product · **Part of:** Forge WS1 (CF development) · **Created:** 2026-06-06
**Pairs with:** `criteria-registry.md` · `va-design-discipline.md` · the model-stack skills (`ive-ctm-custom`, `ive-aom-custom`, `ive-fin-sim-custom`) · `ive-assumption-audit-custom` · `/verify-venture-custom`
**Grounded in:** INCOSE Technical Measurement (Roedler & Jones, INCOSE-TP-2003-020-01, 2005) · INCOSE verification/validation canon (SEBoK) · Simanis et al. (2023) "fidelity over resolution".

This is the single source of truth for how a number appears in any IVE model. It replaces the bare point estimate (optionally red-flagged `[assumed]`) with a **Technical Performance Measure (TPM) record**. Every other skill references this file; none restates it.

---

## Why a point estimate is a defect, not a simplification

A single number implies a measurement that does not exist. `WTP = £10,000` looks more rigorous than `£8k–15k` — and is the opposite. It is **high resolution, low fidelity**: precise-looking, disconnected from the commercial logic that warrants it (Simanis 2023). It also hides the warrant — the number is a *prediction warranted by a requirement*, not a fact — and it mis-frames validation, inviting "go measure the true value" when the right question is "is the requirement solved well enough that reality lands in the band?"

INCOSE's answer is the TPM: carry the critical parameters as bands with a threshold, an objective, an evidence basis, and a convergence plan — and track them over the lifecycle as uncertainty narrows. A figure with no evidence method is a **verifiability defect** (INCOSE's four requirement criteria: verifiable, feasible, necessary, sufficient).

---

## The TPM record — every load-bearing figure carries six fields

| Field | What it states |
|-------|----------------|
| **Band** | `[low, high]` (or low / central / high). Never a bare point. |
| **V/Val type** | **Verification** (does the design meet the requirement — "built it right") or **Validation** (does it meet the real need in the operational environment, with the intended users — "built the right thing"). This is the load-bearing tag. See below. |
| **Evidence method** | One of INCOSE's four: **examination · analysis · demonstration · test.** "Assumed / no method" is not a fifth tier — it is a flagged defect to close. |
| **Threshold** | The must-meet value the band is read against (e.g. FMOS ≥ 60% Phase-II gate). |
| **Objective** | The want-to-meet value (the design target above threshold). |
| **Convergence** | The event that will confirm the band, and roughly when — i.e. *how this figure stops being a band and becomes evidence.* For a validation figure this is usually a demonstration or operational test; for a verification figure, an analysis or inspection. |

Plus a one-or-two-sentence **credibility note**: why this band, and what would push the true value outside it.

---

## The one distinction that governs everything — verification vs validation

INCOSE is strict, and IVE inherits it:

- **Verification** = built it right. The figure follows from the design meeting its requirement. Examples: cost floor, derived FMOS arithmetic, the per-layer cost build. Evidenced by **analysis** or **examination**. High confidence is achievable *now*, pre-operationally.
- **Validation** = built the right thing. The figure is a claim about the real world — what customers will pay, adopt, complete — in the operational environment, with the intended users. Examples: WTP, adoption rate, outcome-check-in completion rate. Ultimately requires **demonstration or test in the operational environment**. Analysis gives legitimate *interim* evidence with stated confidence; it cannot substitute for the operational test.

**This resolves the WTP question.** "Requirement-resolution predicts the band" is **validation-by-analysis** — real, legitimate interim evidence (the IVE promise: solve the requirement well and behaviour lands in the band). The pilot is **validation-by-test** — the confirming event. Both are valid validation evidence at different maturity. The band is not a guess pending fieldwork, nor a survey answer — it is a falsifiable prediction with a planned confirmation event.

**Elicitable vs emergent (VA-31) is this distinction in other words.** An *elicitable* parameter exists independent of the system (can be examined/benchmarked now). An *emergent* parameter only comes into being once the system works (a validation parameter confirmable only by demonstration/test). The valid convergence action for an emergent figure is "build the minimum system where the property can be observed" — never "survey."

---

## The IVE promise is conditional — state it as such

A validation-by-analysis band is only as credible as (a) the requirement actually being soundly solved (the grader's job to check) and (b) the IVE mechanism holding for this venture. So the credibility note says **"predicted-by, conditional on R-n holding,"** never "proven." That is what keeps the model falsifiable: pilot lands in-band → corroborates the requirement and the promise; out-of-band → diagnostic that one of them failed. The band is the test, not a hope.

---

## FMOS is a propagated band, not a point

Input bands flow through to an **FMOS band**. The gate then:
1. tests whether the **whole band** clears the threshold (≥60% Phase-II / ≥25% per-requirement),
2. names the **binding input** (the figure whose low end drives the worst corner),
3. reports **how far the worst corner sits from failure** (the margin).

This makes the sensitivity surface native to the model, not an afterthought. (On Forge this was done by hand: the 85% worst corner, the WTP-£5k negative corner. Now it is the standard output.)

---

## Discipline guard — range only the critical few

INCOSE tracks only the parameters that drive operational success and risk (KPPs), not every number. **Apply the TPM record only to load-bearing figures** — those that move the FMOS or carry material risk. Derived line items that follow mechanically from a TPM inherit its band and need no separate record. This prevents range-theatre (a model where everything is a band signals nothing).

---

## Worked example — WTP on Forge

> **WTP_low** — Band: `£8,000–15,000`. V/Val: **Validation**. Method: **analysis** (interim) → **demonstration** (Phase 0 retroactive-corpus) → **test** (first paid engagements). Threshold: keeps FMOS denominator < £6,250 to clear the 60% gate. Objective: ≥ £10,000. Convergence: confirmed by first cohort of paid engagements; interim-validated by the Phase-0 corpus demonstrating score-tracks-outcome. **Credibility note:** band is bracketed below by observed consultant fees (£50–150k, examination) and predicted by how well R2 solves the value-gap display (validation-by-analysis, conditional on R2 holding). Falls outside the band if the credence-good reference class fails to convince — the emergent risk only demonstration resolves.

Contrast the old form: `WTP = £10,000 [assumed]`. Same number, no warrant, no convergence path, no V/Val type — a hypothesis dressed as a figure.

---

## What references this file

- **`criteria-registry.md`** — the TPM-record criterion is registered as a HARD check; the grader runs it.
- **Model-stack skills** (`ive-ctm-custom`, `ive-aom-custom`, `ive-fin-sim-custom`) — every load-bearing figure output as a TPM record; FMOS propagated as a band.
- **`ive-assumption-audit-custom`** — tags each assumption V/Val + method + elicitable/emergent, and prescribes the convergence action by type.
- **`/verify-venture-custom`** — scores verification-soundness separately from validation-maturity; does not penalise a sound design for unfielded validation parameters at a pre-operational gate. *(Grader change — pending Tom's sign-off; see `verify-venture-tpm-change-proposal.md`.)*
