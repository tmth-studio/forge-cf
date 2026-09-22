---
name: architecture-assumption-audit-custom
description: Architecture Assumption Audit — extracts all assumptions from the model stack (VDR, CTM, AOM, ARM, fin-sim), ranks them by FMOS sensitivity, rates evidence quality on the T1–T4 tier system, and produces a prioritised validation action list. Venture-agnostic. Run after the ARM is built.
---

# IVE Assumption Audit

**Purpose:** Every IVE model rests on assumptions. The assumptions that matter most are those that (a) can fail, and (b) would materially move FMOS if they did. This skill finds those assumptions, ranks them by their impact on the financial margin of safety, rates the current evidence quality for each, and prescribes the minimum validation step needed to reduce the risk.

**When to run:** After the ARM is built. The ARM's sensitivity analysis is the primary input — it tells you which cost and revenue inputs move FMOS most. The audit extends this across all model layers (VDR, CTM, AOM, ARM, fin-sim) to surface assumptions that the ARM may not have reached.

**Output:** A ranked assumption register (HTML) with:
- Every material assumption extracted from each model layer
- Sensitivity rating: how much FMOS moves if the assumption is wrong
- Evidence tier: T1 (validated) → T4 (assumed, no data)
- Priority score: sensitivity × evidence gap
- Validation action: the minimum step to move the assumption one tier

**Venture-agnostic.** This skill works on any IVE architecture. Point it at the relevant VDR, ARM, AOM, CTM, and fin-sim files.

---

## The T1–T4 evidence tier system

Every assumption in an IVE model should carry a tier rating. This is the single source of truth for evidence quality:

| Tier | Label | Meaning | Display |
|------|-------|---------|---------|
| **T4** | Assumed | No supporting data. The number was chosen to make the model work or was a reasonable guess. The model passes on this assumption but has no basis for it. | 🔴 Red |
| **T3** | Proxy / comparable | Evidence from a comparable context — a different market, a different geography, a similar product. The assumption is grounded but not specific to this venture's context. | 🟠 Orange |
| **T2** | Published / industry | Published data from a relevant industry, market, or regulator. Specific enough to be meaningful but not yet validated against the venture's own operators or customers. | 🟡 Yellow |
| **T1** | Validated | Confirmed by operator data, customer research, or primary source specific to this venture's context. The assumption is no longer an assumption — it is a measured input. | 🟢 Green |

**The fidelity guardrail (hard):** any FMOS computed on T4 inputs is indicative only. The verdict is "⚠ Provisional PASS — pending [T4 assumption]." A clean PASS requires T2 or better on all load-bearing assumptions (the top 3–5 by sensitivity). T1 on all load-bearing assumptions closes the loop.

---

## The sensitivity rating system

Sensitivity measures how much FMOS moves if the assumption is wrong by a realistic amount. The ARM's sensitivity table is the primary source; where no sensitivity table exists, derive it from first principles.

| Rating | Definition | FMOS movement |
|--------|-----------|---------------|
| **Critical** | If this assumption is wrong by 2× in the pessimistic direction, the gate fails | >50pp FMOS drop |
| **High** | If wrong by 2× pessimistic, FMOS drops materially but the gate still holds | 20–50pp FMOS drop |
| **Medium** | If wrong by 2× pessimistic, FMOS compresses but stays well above the gate | 5–20pp FMOS drop |
| **Low** | Materially wrong values do not move FMOS significantly | <5pp FMOS drop |

**Priority score = Sensitivity × Evidence gap:**

| | T4 (no data) | T3 (proxy) | T2 (industry) | T1 (validated) |
|---|---|---|---|---|
| Critical | **P1** | **P1** | P2 | — |
| High | **P1** | P2 | P3 | — |
| Medium | P2 | P3 | P4 | — |
| Low | P3 | P4 | — | — |

P1 = validate immediately. P2 = validate before Stage 1 gate. P3 = validate before Stage 2 gate. P4 = monitor.

---

## Process

### Step 0 — Load the model stack

Ask the user to specify which files to read, or read the standard set for this venture:

1. **VDR** — the venture design record (per-requirement assumptions, FIT gate inputs)
2. **ARM** — the at-scale resourcing model (the most assumption-dense document; all cost inputs)
3. **AOM** — the activity and operations model (volume drivers, money flows)
4. **CTM** — the customer transformation model (state change assumptions, willingness to pay)
5. **Fin-sim** — the financial simulation (volume ramp assumptions, cost of capital, discount rate)
6. **Research notes** — any standalone research documents that provide evidence for specific assumptions

If any model is missing, note it — its assumptions cannot be audited and must be surfaced as a gap.

### Step 1 — Extract assumptions

Work through each model layer in order. For each assumption found:

1. **Name it** — one sentence, specific enough to be testable
2. **Locate it** — which model, which section, which line
3. **Current value** — the number or claim the model uses
4. **Current tier** — T1/T2/T3/T4 (read from the document if tagged; infer if not)
5. **Source** — what justifies the current tier rating

**Extraction rules:**
- Any figure marked in red in the document is T4 by convention — extract it
- Any figure described as "illustrative," "placeholder," or "assumed" is T4 — extract it
- Any figure citing a published source is T2 minimum — check the source quality
- Any figure from operator conversations is T1 — verify the conversation is documented
- Do not extract accounting identities (e.g. FMOS = (ceiling − floor) ÷ floor) — those are calculations, not assumptions
- Do extract the inputs to those identities (e.g. the price ceiling, the cost floor components)

**Assumption categories to watch for in each layer:**

*VDR:*
- Price ceiling (the customer's WTP / KMC)
- TAM size and composition
- Penetration rate by segment
- Claim/dispute rate
- Recovery rates
- Claimant behaviour assumptions

*ARM:*
- Labour rates and productivity (time per activity)
- Dispute/claim rate (converts per-claim to per-transaction)
- Expected payout / loss rate
- Recovery rate
- Platform technology costs
- Scale assumptions (sites, transactions, volume ramp)

*AOM:*
- Volume drivers (transactions per site, claims per transaction)
- Money flow magnitudes (referral fees, platform fees, insurer premiums)
- Activity time/cost assumptions

*CTM:*
- State change assumptions (what % of customers actually make the transition)
- Value created per state change
- Customer behaviour assumptions

*Fin-sim:*
- Volume ramp (how fast scale is achieved)
- Cost of capital / discount rate
- Payback period assumptions
- Churn rate

### Step 2 — Rate sensitivity

For each extracted assumption, derive the sensitivity rating. The ARM's sensitivity table (if it exists) is the primary source. For assumptions not covered by the ARM:

1. Identify which FMOS inputs the assumption affects (cost floor, price ceiling, or both)
2. Stress-test: if the assumption is 2× worse in the pessimistic direction, what happens to FMOS?
3. Assign the sensitivity rating (Critical / High / Medium / Low)

**Critical shortcut:** any assumption that directly determines the cost floor or the price ceiling is at least High sensitivity. Any assumption that scales linearly with transaction volume at the layer level (e.g. dispute rate, payout rate) is Critical — because it affects both the loss cost and the revenue model simultaneously.

### Step 3 — Assign priority scores

Cross-reference sensitivity × evidence tier to produce the P1–P4 priority score for each assumption.

### Step 3b — Tag each assumption: V/Val type and elicitable vs emergent

Canonical: `04-Projects/TMTH_Venture_Studio/Forge/WS1/tpm-measurement-standard.md`. Before prescribing a validation action, tag each load-bearing assumption on two axes — because the axes determine which validation actions are even *valid*:

- **V/Val type (INCOSE):** **Verification** (the figure follows from the design meeting its requirement — cost floor, FMOS arithmetic; confirmable now by analysis/examination) or **Validation** (a claim about real-world behaviour in the operational environment — WTP, adoption, completion rate; ultimately needs demonstration/test).
- **Elicitable vs emergent:** **Elicitable** — exists independent of the system; can be examined/benchmarked now (e.g. observed consultant fees). **Emergent** — only comes into being once the system works; cannot be surveyed, only revealed by operating the system (e.g. WTP for a credence good, network-effect adoption).

**The error this prevents (VA-31):** prescribing "interview customers about WTP" for an emergent assumption is a category error — stated preference about a system that doesn't yet work is noise. An emergent + validation assumption's only valid action is *build the minimum system where the property can be observed*, never *ask*.

### Step 4 — Prescribe validation actions

For each P1 and P2 assumption, write a specific validation action — the minimum step to move it one tier. **Branch by the Step 3b tags:**

**Elicitable assumptions** (examination/analysis available now):
- **T4 → T3:** find a published comparable (name the source, search query, or organisation that holds the data)
- **T3 → T2:** find a published primary source for this specific industry/context (name the regulator, trade body, or database)
- **T2 → T1:** operator conversation or primary research (state what to ask, who, and what a T1 answer looks like)

**Emergent assumptions** (no survey can validate — but emergent ≠ unknowable-until-built; VA-31): the assumption is *endogenised into the requirements*, so the estimate comes from requirement quality, not fieldwork. The validation action is **NOT "survey" and NOT merely "build"** — it is, in order:
- **Identify the internalising requirement(s)** — which requirement is supposed to produce this behaviour, and what observable real-world quantity anchors it (e.g. WTP → R2's KMC anchor + the R4–R7 forces that would drag behaviour below the ceiling).
- **Adversarially verify those requirement(s) and harden the anchor** — the estimate is only as good as (a) the internalising requirement being soundly, adversarially-verified solved (not justification-mode) and (b) its anchor grounded in observable fact. Hardening the anchor (benchmark the foregone/observed cost) is where desk research still earns its keep. State the band as "predicted-by, conditional on R-n holding," never "proven."
- **Build only to confirm** — name the minimum operating system that lets the property manifest and what in-band vs out-of-band would show (for a corpus/credence-good venture: the seed/bootstrap). The pilot confirms the estimate; it does not originate it. Never prescribe a survey.

Validation actions must be actionable. "Get more data" is not a validation action. "Request historical dispute rate data from [named operator type], segmented by transaction value band, covering at least 12 months" is. For emergent assumptions: "run the [named] bootstrap so the [property] can be observed against [in-band threshold]" is — "ask customers if they'd pay" is not.

### Step 5 — Produce the assumption register

Output a single HTML document using the standard design system (DM Sans + Lora, `#f5f4f1` background, `#0f2744` navy panel, same CSS variables as the VDR).

**Document structure:**
1. **Governing thought panel** (navy): the single most important finding — the P1 assumption that dominates all others
2. **Summary table**: count of P1/P2/P3/P4 assumptions by model layer; FMOS status at current evidence tier vs. FMOS at T1 (validated)
3. **P1 assumptions** — full detail: name, location, current value (as a band), tier, sensitivity, **V/Val type**, **elicitable/emergent**, validation action (branched per Step 4)
4. **P2 assumptions** — same format
5. **P3/P4 assumptions** — condensed table (name, tier, sensitivity, action)
6. **Model coverage gaps** — which model layers were not available to audit; what assumptions they would surface if built
7. **Validation sequencing** — proposed order of validation actions given resource constraints (which P1 actions can be run in parallel, which are prerequisites for others)

**Output file naming:** `[venture-slug]-assumption-audit-[YYYY-MM-DD].html`
Example: `calmlyresolve-assumption-audit-2026-06-05.html`

---

## Output quality checks

Before finalising the register, run these checks:

1. **Coverage:** is there at least one assumption extracted from each model layer that was available? If a layer produced no assumptions, it was either not read or not assumption-dense — investigate.
2. **No double-counting:** the same assumption may appear in multiple models (e.g. dispute rate appears in ARM, AOM, and fin-sim). Consolidate to one entry; note all locations.
3. **No accounting identities:** verify no pure calculations were extracted as assumptions.
4. **P1 completeness:** every assumption rated Critical + T4 must be P1. Every assumption rated Critical + T3 must be P1. Check this.
5. **Actionability:** every P1 and P2 action must be specific enough to execute. If it reads as vague, rewrite it.

---

## Integration with the IVE model stack

This skill fits between the ARM and the financial simulation in the model stack:

```
CTM → AOM → ARM → [Assumption Audit] → Financial Simulation → required price → FMOS
```

The audit is not a gate — it does not block the financial simulation. It produces the ranked validation agenda that runs in parallel with (and informs) the financial simulation. A P1 assumption that fails validation triggers a loop back to the ARM (same loop-back discipline as the design loop).

**The audit also feeds the FIT verifier.** Any assumption rated T4 that is Critical or High sensitivity means the FIT gate verdict must be "⚠ Provisional PASS — pending [assumption]." The audit makes this explicit and systematic.

---

## Worked example structure (Calmly Resolve, 5 June 2026)

The top P1 assumptions at C8 would include:

1. **Dispute rate (0.05%)** — Critical / T3 — ARM sensitivity shows FMOS drops from 107% to 36% at 0.10%. Validation action: obtain historical dispute rate data from marketplace operators (Checkatrade, Rated People), segmented by transaction value band. A T1-quality answer: >12 months data from ≥2 operators, dispute/claim rate expressed per completed transaction with value band breakdown.

2. **Transaction site in-house dispute-risk cost (£0.50/txn)** — Critical / T3 — ARM sensitivity shows gate fails if ceiling is below £0.28/txn at 0.05% dispute rate. Validation action: request trust & safety cost disclosure from operator during ITP outreach conversations. A T1-quality answer: operations & support headcount + budget / annual transaction volume, from ≥1 primary operator.

3. **Expected payout per claim (£252 net)** — High / T4 — ARM sensitivity: if payout doubles, full floor rises to £0.367/txn, FMOS 36%. Validation action: obtain BTE insurance loss ratio data from DAS, ARAG, or DWF Claims. T1-quality: actual loss ratio (claims paid / premiums earned) for comparable legal expense products.

These are illustrative — the audit extracts and ranks all assumptions systematically rather than selecting manually.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-assumption-audit-custom/SKILL.md` to modify
- Invoke as: `/ive-assumption-audit-custom`
- Related: `/ive-fit-verifier-custom` (the gate this feeds) · `/ive-fin-sim-custom` (downstream) · `/head-of-verification-calmly-custom` (the role that runs this for Calmly)
- Source: Calmly BTE ARM (5 June 2026) — the dispute rate sensitivity table was the immediate trigger for building this as a repeatable skill
