# IVE Criteria Registry — objectively verifiable criteria per mini-output

**Owner:** Head of Product · **Part of:** Forge WS1 (CF development) · **Created:** 2026-06-03
**Pairs with:** `architecture-process-flow.html` (the v2 flow) · `/verify-venture-custom` (Phase 4 critic) · `va-design-discipline.md`

Every mini-output the CF produces must carry a criterion of a **checkable type** — so "is this good?" becomes a test, not a judgement call. This registry is the spec the independent critic (flow Phase 4) runs, and the bar each gate enforces.

---

## The verification standard — two tiers

**Tier 1 — Mechanical (automatable, pass/fail, no judgement).** Five check types, all already present in the BALM toolkit:

| Type | What it checks | Example (existing) |
|------|----------------|--------------------|
| **Presence** | a required element is stated | theory citation present (ToC) |
| **Format / pattern** | text matches/avoids a pattern | no "% of revenue" (AOM) |
| **Count** | a number meets a band | ≥6 use cases (PCO) |
| **Threshold** | a metric clears a number | FMOS ≥ 25% |
| **Traceability** | element X links to required element Y | every AOM activity ↔ a flow |

**Tier 2 — Anchored rubric (for the irreducibly qualitative — elegance, coherence, theory-fit).** 1–5 with *concrete level anchors*, scored by an **independent** critic (never the producer), pass threshold + **≥2 scorers must agree**. Not objective like a number, but *verifiable*: reproducible and inter-rater checkable.

**Rule:** convert every soft criterion to Tier 1 where possible; only genuinely qualitative judgements go Tier 2. A mini-output with no Tier-1 or Tier-2 criterion is not done.

---

## Canonical FMOS gates — single source of truth

`FMOS = (Price Ceiling − Cost Floor) / Cost Floor` — cost in the denominator (Simanis, *Built to Hold*, Jan 2025, p.7). Precondition: all four cost layers (PVC · RC · SC · IC) populated, else the verdict is indicative only.

**There are TWO gates. They were being conflated — this is the reconciliation:**

| Gate | When | PASS | BORDERLINE | FAIL |
|------|------|------|------------|------|
| **Per-requirement** (early warning, run each Rn + at F1→F2) | inside the design loop | **≥ 25%** | 15–24% (proceed only with the gap logged as a Phase II assumption) | **< 15%** |
| **Phase II capital** (go/no-go after all 10 requirements) | before Phase II spend | **≥ 60%** | 25–59% (tighten or carry as critical assumption) | **< 25%** |

*Interpretive call made in reconciling (flag for ratification): the ≥60% band is the **Phase II** gate, not the F1→F2 transition. fit-verifier's text was internally split between line 49 (≥60 at F1→F2) and line 280-equivalent (60 = full Phase I gate); design-loop and AOM both put 25% at every requirement and 60% only at the full Phase I → Phase II gate. Reconciled to the latter. If Simanis canon puts 60% at F1→F2, this one cell flips.*

**Threshold evolution — note for the dissertation:**
The FMOS threshold has evolved across Simanis' published work. The 2023 manuscript (*Financial Simulations to Innovate Disruptive Business Models*) uses **15–20%** ("the credible price must be at least 15–20% greater than the required price"), grounded in the systems-engineering principle that 85% of costs are fixed once the core design is specified — so the margin must absorb unanticipated cost shocks. *Built to Hold* (2025) raises the per-requirement gate to **25%** and sets a **60%** Phase II gate, grounded in Flyvbjerg & Gardner (2023): average cost overruns on complex projects run at 62%, so a 60% FMOS means the venture remains profitable even if unit costs rise by the average overrun. The 2023 threshold is the origin of the reasoning; the 2025 threshold is the canonical operational bar for v2. Both cite the same underlying principle — the margin exists to absorb the "punch in the mouth" (Blank) — but the 2025 version is calibrated to empirical overrun data.

---

## TPM record standard — how every load-bearing figure is expressed

Canonical: `tpm-measurement-standard.md` (INCOSE Technical Measurement). Every figure that moves the FMOS or carries material risk is a **TPM record**, not a bare point estimate. A point estimate is a verifiability defect — high resolution, low fidelity.

A TPM record carries: **band** `[low, high]` · **V/Val type** (verification = built-it-right, evidenced by analysis/examination now; validation = built-the-right-thing, ultimately needs demonstration/test in the operational environment) · **evidence method** (examination/analysis/demonstration/test — "no method" = defect) · **threshold + objective** · **convergence event**. FMOS is a propagated band: test the whole band against the gate, name the binding input, report the margin from failure.

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| **Load-bearing figure as TPM record** | Format / Presence | every FMOS-moving figure carries band + V/Val type + evidence method + threshold/objective + convergence; no bare point estimates | pass/fail · **HARD** · **NEW** |
| **V/Val tag present** | Presence | each load-bearing figure tagged verification or validation; validation figures name a demonstration/test convergence event, not analysis-only | pass/fail · **NEW** |
| **FMOS as band** | Format | FMOS reported as a propagated band with binding input named and worst-corner margin stated, not a single % | pass/fail · **NEW** |
| **No assumed-without-method** | Format | no load-bearing figure is "assumed / no method" without being flagged a defect to close | pass/fail · **HARD** · **NEW** |

This composes with the T1–T4 source tiers (T4 = assumed/no-method; T1 = demonstration/test confirmed) and the assumption audit's sensitivity ranking. **Discipline guard:** applies to load-bearing figures only — derived line items inherit their driver's band. A model where everything is a band signals nothing.

---

## The registry — by flow phase

Legend: **NEW** = a criterion that did not exist and is being added · **HARD** = non-softenable gate.

### Phase 0 — Frame  (`balm-pco-custom`)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Investment parameters | Presence | all 4 named: period, target IRR, geography, industry | pass/fail |
| Core functionality statement | Format | contains zero customer/segment tokens (usable without knowing the customer) | pass/fail |
| Right-sized problem | Count (downstream) | specific enough to yield ≥3 concrete use cases — verified by producing them | pass/fail |
| Use cases | Count | ≥ 6 generated | pass/fail |
| Loss-to-price ratio (per case) | Threshold | > 2× viable · 1–2× marginal · < 1× kill | banded |
| PCO statement | Presence | names all 4: observable condition · group size · loss scale · viable ratio | pass/fail |
| **Research firewall** | Format | no solution/form-factor/analogue language anywhere before the CLO | pass/fail · **HARD** |

### Phase 1 — CLO + seed  (`ive-architecture-generator-custom`)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| CLO statement | Format | is a *process step*, not a market condition | pass/fail · **HARD** |
| Structural class | Presence | primary + secondary assigned from the 8-class table | pass/fail |
| Cross-domain analogues | Count | 6–10 generated | pass/fail |
| Filtered candidates | Count | reduced to 3–4 | pass/fail |
| Candidate score | Threshold + Rubric | cost-reduction /5 + theory-grounding /5 + elegance /5; elegance anchored (5 = structurally embedded, 1 = operationally dependent) | elegance ≥ 4 |
| Workaround seed | Rubric | highest total; elegance breaks ties | derived |

### Phase 2 — Architect around the spine  (`ive-design-loop` + `balm-challenge-N` + `theory-of-change` + `ive-ctm` + `ive-aom` + `ive-fit-verifier`)

*Per requirement:*

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Diagnosis (bottleneck/block) | Format | names a single operation/block, not a category | rubric |
| ToC — class of problem | Presence | a named category (not a symptom description) | pass/fail |
| ToC — theory | Presence | named researcher + year + paper | pass/fail · **HARD** |
| ToC — context | Rubric | conditions (not situation) · population-specific · mechanism-linked | anchored, ≥2 agree |
| ToC — outcome | Format | substitution test fails: "we will do X" does NOT fit (it's a state, not an activity) | pass/fail |
| Strategy — design choice | Count + Format | exactly one structural move; operationally specific; venture-specific | pass/fail |
| Strategy — hypothesis | Presence | falsification condition stated + ≥1 named assumption | pass/fail |
| CTM update | Traceability | every state change ↔ a BALM requirement; every component ↔ a state change; ungrounded = `[REQUIRES C[N]+]` | pass/fail |
| AOM — Ops Map | Traceability | every activity ↔ a flow on the map | pass/fail · **HARD** |
| AOM — volume drivers | Presence | every activity row has an explicit volume driver | pass/fail · **HARD** |
| AOM — no ratios | Format | no "% of revenue" / "1 per Y%" pattern | pass/fail · **HARD** |
| AOM — role support | Presence | every performer role has a named supervisor + trainer + QA | pass/fail |
| AOM — LMU sizing | Threshold + Rubric | Q1: one LMU contribution margin > 0 (objective); Q2: replicable fast (rubric) | mixed |
| FIT — FMOS (per-requirement) | Threshold | ≥ 25% PASS · 15–24% BORDERLINE · < 15% FAIL (canonical) | banded |
| FIT — I check | Rubric | strategy removes a cost driver at the *design* level, not via operational efficiency | anchored |
| FIT — T check | Presence + Format | T-chain: an explicit logical chain present; T-robustness: theory NOT on the named fragile-findings list (ego depletion, power posing, social priming, money priming, IAT→behaviour, growth-mindset-at-scale) | pass/fail |
| **Synergy (generation)** | **Count** | ≥ 1 move in this requirement also solves ≥ 1 *earlier* requirement | pass/fail · **NEW** |
| Loop gate | Threshold | cannot proceed to R[n+1] without FIT PASS on R[n] | pass/fail · **HARD** |
| **No forward references (VA-80)** | Format | no actor or mechanism introduced at a later requirement appears in this requirement's cells; a residual carries only the later requirement's number, never its solution | pass/fail · **HARD** · **NEW** |
| **Credibility mechanism (VA-81)** | Presence + Traceability | every endorsement, signal, warranty, certification or published-record element names its receiver, the proposition, the instrument that receiver uses today, and a public-record supplier of that instrument; re-derived whenever a later requirement changes the receiver | pass/fail · **HARD** · **NEW** |

### Phase 3 — Converge  (`ive-consistency-audit-custom` + VA-1)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Cross-requirement consistency | Traceability | dependency matrix built; zero hard contradictions | pass/fail |
| **Architecture synergy (the moat test)** | **Count** | ≥ 1 single design move solves ≥ 2 requirements | threshold · **NEW** |
| Real-business analogue (VA-1) | Presence | a named existing business the architecture resembles, with the shared mechanism | pass/fail |
| Convergence routing | Rule | if not cohered (no analogue / contradictions) → route back to generation, do not patch | rule · **NEW** |

### Phase 4 — Verify  (`/verify-venture-custom`)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Completeness sub-score | Count | (complete + 0.5·partial) / total | scored |
| Consistency sub-score | Threshold | 100 − 15·hard − 5·soft contradictions | scored |
| Discipline sub-score | Traceability + gate | traceability % of specified detail; capped at 50 if justification-mode | scored + gate |
| Synthesis sub-score | Rubric | analogue + synergy → 100 / 70 / 30 | scored |
| F3 barrier scores | Threshold | SCIS / FIS / HRS each ≥ 5 pass; ≤ 3 = NCR | banded |
| Integrity score | Threshold | ≥ 85 SOUND, both gates clear | banded |
| **Conformity guard** | Rule | reject only "wrong because incoherent"; never penalise "wrong because it breaks the conventional CBA" | rule · **NEW** |

### Phase 5 — Sign-off

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| PCO confirmation | Gate | human confirms the PCO | human |
| Expert sign-off | Presence | ≥ 1 IVE expert independently confirms SOUND | pass/fail |

---

## What this changes

- **Three new objectively-verifiable criteria** that did not exist: the **synergy count** (Phase 2 generation + Phase 3 architecture — makes Simanis' "synergy is the moat" a *number* for the first time), the **convergence routing rule**, and the **conformity guard**.
- **The conformity guard is enforced by the registry itself:** if "good" is defined *only* by these criteria, the critic cannot regress toward conventional design — conventional-wrongness is penalised by no criterion here; only incoherence, broken traceability, and failed FMOS are.
- **Soft criteria hardened:** "specific not generic" → token/pattern checks; elegance/coherence/theory-fit → anchored rubrics with ≥2-scorer agreement.
- **FMOS reconciled** to one two-gate canonical (above) — the three conflicting schemes resolved.

---

## Methodology note — TAM segmentation through F2/F3

**Source:** Calmly BTE fin-sim (4 June 2026) — qualifying claim rate by Transaction Site type revealed that a single TAM penetration rate collapses real variance across segments into a number that is wrong for all of them.

**The principle:** the BFF sharpening process through F2 and F3 IS the segmentation process.

As the architect works through F2 (normalising the customer routine) and F3 (locking in market position), the design choices generate architecture-derived criteria that distinguish which customers in the TAM can actually be served profitably at-scale. These criteria are not assumptions layered on top of the architecture — they are outputs of it.

**The implication for financial simulation:** by F3 at the latest, the architect should be working with segment-level penetration rates derived from the architecture's own design criteria — not carrying a monolithic TAM penetration assumption through to C10. A single penetration rate applied to a heterogeneous TAM will be wrong for every segment: too optimistic for some, too pessimistic for others, and unable to surface the architectural decision of which segments to prioritise.

**How to apply:**
- **C1–C4 (F1):** a single TAM penetration rate is appropriate — the architecture has not yet generated differentiating criteria.
- **C5–C7 (F2):** as routines, activation mechanisms, and payment structures are designed, segment-level criteria begin to emerge. The architect should note when sub-groups of the TAM diverge materially.
- **C8–C10 (F3):** segment-level penetration rates should replace the monolithic rate. The fin-sim should be structured with a segment table, not a single penetration assumption. If a segment is retained in the TAM at low penetration (e.g. because the architecture supports it at lower priority), that is a design decision to make explicitly — not a gap.

**Criterion (Tier 1 — added to F3 fin-sim check):**

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| F3 financial simulation | Format / pattern | penetration rate input is per-segment, not monolithic | pass/fail |

---

## Open / to ratify

- The one interpretive FMOS call (60% = Phase II gate, not F1→F2) — flagged above.
- Tier-2 anchored rubrics (ToC context, I-check, elegance, LMU-Q2) still need their 1–5 level descriptors written out. Next build.
