# IVE Criteria Registry — objectively verifiable criteria per mini-output

**Owner:** Head of Product · **Part of:** Forge WS1 (CF development) · **Created:** 2026-06-03
**Pairs with:** `architecture-process-flow.html` (the v2 flow) · `/verify-venture-custom` (Phase 4 critic) · `va-design-discipline.md`

Every mini-output the CF produces must carry a criterion of a **checkable type** — so "is this good?" becomes a test, not a judgement call. This registry is the spec the independent critic (flow Phase 4) runs, and the bar each gate enforces.

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date)

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
| **Levelling record (Path C)** | Presence | names the line's job as stated · the levelled case · the next-broader case and the delivery difference that excludes it; a company typicality statement; the cost-target mode named (1 reach a group · 2 cut by a number · 3 just show me); in mode 1 the excluded population with count, source and reason; in mode 2 the user's number with the line "a target, not a market claim"; in mode 3 the incumbent's volume as the scale; every ceiling figure labelled by population; where the entry named a company and not a line, the line chosen by the core-business default with the rule that chose it, its source and the other lines declined (RD-026) | pass/fail · **HARD** · **NEW** (RD-023, Tom approved 16 Sep 2026; modes added by RD-024 and the core-business default by RD-026 the same day) |

### Phase 1 — CLO + seed  (`ive-architecture-generator-custom`)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| CLO statement | Format | is a *process step*, not a market condition | pass/fail · **HARD** |
| Structural class | Presence | primary + secondary assigned from the **9-class** table; where the value the conventional form sells depletes with extraction, rivalrous value source is named as primary or the run states why not | pass/fail (amended, RD-030, Tom approved 21 Sep 2026) |
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
| **Synergy (generation) — VA-106** | **Count** | the requirement's output block carries a VA-106 line naming the earlier requirements this move also serves, with the mechanism for each, or stating "none". **A blank line fails this row. "None" passes it.** | pass/fail |
| Loop gate | Threshold | cannot proceed to R[n+1] without FIT PASS **or a fully specified PROVISIONAL** on R[n] (see VA-82) | pass/fail · **HARD** |
| **Three-limb close (VA-89 + VA-91)** | Presence + Traceability | the challenge verdict is a conjunction of a **logical** limb (the method's named checks), an **operational** limb (AOM capacity — one capacity figure, derived consistently — role support, unit sizing, component carriage) and a **financial** limb (FMOS **and** the venture's named binding gate, printed at every challenge after the one that identified it; a failing binding gate fails the limb whatever the FMOS says); every named check that did not pass is disposed as design defect (FAIL) · standing constraint (caps at PROVISIONAL) · build item (caps at PROVISIONAL, needs owner + convergence event + re-run threshold); an unclassifiable failed check is a design defect | pass/fail · **HARD** · **NEW** |
| **Financial halves shown independent (VA-97)** | Traceability | the margin of safety and the binding gate are reported as two checks only where the run shows they measure different things; where one reduces to a transform of the other, it says so, reports one check, and states what an independent second check would have to measure | pass/fail · **HARD** · **NEW** |
| **Enforcement point named (VA-100)** | Presence + Traceability | every ratified rule names where it is enforced — executable (file + check) / contractual (skill output contract or hard gate) / judgement (with reason); a rule with none is drafted, not ratified; a check with no rule behind it fails the same criterion from the other side | pass/fail · **HARD** · **NEW** |
| **Partner business case (VA-99)** | Presence + Format | every enabler actor except a commodity vendor carries an outcome and a `business_case` (earns · costs · beats_next_best · operational_fit · timing); a `kmc` on a partner is a defect; `unstated` needs an owner and a reason | pass/fail · **HARD** from 2026-09-01 · **NEW** |
| **Structural-limit disposition (VA-101)** | Traceability | a failed check that fails on a limit of the world rather than of the design is disposed as **structural limit** — caps at PROVISIONAL, requires the residual named, bounded, and paired with the validation that addresses it; it must be true of every venture in the class, and it is a design defect if any competitor with any budget could remove it | pass/fail · **HARD** · **NEW** |
| **Verdict composes forward (VA-95)** | Threshold + Traceability | every verdict names the cumulative span it covers (C1 to C[N]) and the worst verdict it inherits; no requirement's verdict exceeds the worst verdict of any requirement it builds on, unless it names the specific upstream failed check it repairs and shows the arithmetic on the cumulative state; a function gate reads the cumulative verdict at its last challenge | pass/fail · **HARD** · **NEW** |
| **Upstream re-verified on every BFF move (VA-103)** | Presence + Traceability | every requirement's output carries the VA-103 table: what changed in the BFF, and one row per earlier requirement marking its named checks and FIT unchanged / re-verified / FAILED on the BFF as it now stands; a blank or partial table is a FAIL; at C3, C7 and C10 the table also names the consistency-audit and verification artefacts produced by the full cumulative re-run; a requirement whose last verification predates the last BFF move is not closed | pass/fail · **HARD** · **NEW** |
| **Actor business cases priced and gated (VA-127)** | Presence + Rule | every requirement's output carries the VA-127 table with one row per behaviour the architecture needs from any actor but the venture: gain priced by OCV class with band and tier, cost priced, best alternative and its surplus, surplus verdict; a FAIL row with no named force is a design defect (VA-89); a blank table, or a row that names a theory without a price, is a FAIL | pass/fail · **HARD** from 2026-09-14 · **NEW** |
| **Gateway partner classed and priced against the pool (VA-147)** | Presence + Traceability | R7's SR2 enumeration carries every candidate present in the customer's routine in two classes (loss side · gain side), with the sign of the architecture's effect on each candidate's own book; each loss-side candidate's pool is priced from R2's `POOL AT RISK` block; the selected partner's surplus is stated at launch and at the at-scale count; a gain-side selection with a loss-side candidate present carries a stated reason from the admissible list; a stated absence names its falsifying test. A loss-side candidate priced against the status quo is a FAIL. A selection with no reason is a FAIL. | pass/fail · **HARD** · **NEW** (RD-032, 17 Sep 2026; landed on Tom's approval, 21 September 2026; Head of Verification's four tests pass — presence-only, enforcement point named, terms defined, walkable) |
| **Fixed-cost spread count stated once (VA-162) — every requirement** | Presence | the count used for any fixed-cost spread is stated once with the reason it is the at-scale count; the margin is printed at the PCO's alternative counts | pass/fail · **NEW** (RD-041 row 1; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Residue driver stated with legal basis (VA-149) — R1** | Presence + Traceability | a licensed or statutory residue states its driver (per company / per outcome) and the statute or rule that fixes it; an assumed hours figure fails | pass/fail · **NEW** (RD-035, RD-041 row 2; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Affordability screen complete (VA-164) — R4** | Presence | the screen lists every running-cost line the challenge adds before the headroom is read; a line added after the screen fails | pass/fail · **NEW** (RD-041 row 5; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Loop-gate branches (VA-153) — loop gate, all requirements** | Presence | every FAIL states its branch: owner of the lever (this / adjacent / non-adjacent requirement), re-derived-input cap, autonomous warning-band choice, with the record | pass/fail · **NEW** (RD-037, RD-041 row 7; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Partner's return classified (VA-156) — R7** | Presence | fee-in-the-floor or share-of-surplus, with the unit margin under each reading and the venture's own reading | pass/fail · **NEW** (RD-038, RD-041 row 9; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Count line with G15 (VA-155) — R7** | TPM | the gateway route's count at central against the at-scale count, the PCO screen and the objective; partners active (G15) as a gate with margin | pass/fail · **NEW** (RD-038, RD-041 row 10; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Yes-threshold inside a pre-registered budget (VA-163) — R3** | Presence + Traceability | the yes-threshold is read inside a pre-registered acquisition budget stated in the same file before the count is read; a count an acquisition line could buy is not a kill signal; a threshold with no budget beside it fails | pass/fail · **NEW** (RD-041 row 6, re-submitted 21 September 2026 in the C3 skill's wording; landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it) |
| **Existence test before enumeration (VA-92)** | Presence + Traceability | every requirement asking "who is the X" runs an existence test before naming candidates, states the maximum the architecture can pay any holder (derived from the binding gate), and records one of three dispositions — external holder activated / internal holder already activated, with its output made portable / stated absence on falsifiable tests with the arithmetic published and the live question named instead | pass/fail · **HARD** · **NEW** |
| **Binding gate found by driving the model (VA-84)** | Threshold | the pivot trigger and binding gate are found by running the model against every gate it has and reporting the one that fails first with the margin to it — never from a single formula; a margin that is a small fraction of the assumed value is itself the finding | pass/fail · **HARD** · **NEW** |
| **No parallel close on a shared BFF input (VA-85)** | Format | challenges sharing the cumulative business form factor are sequenced; a parallel run may not close its gate on a shared input and declares that slot OPEN in its cumulative statement | pass/fail · **HARD** · **NEW** |
| **TAM as a validated data file (VA-83)** | Presence | R2 does not close until `[venture]-tam-model.yaml` exists and validates; no file-set or naming instruction overrides this, and prose is never the source of a market figure | pass/fail · **HARD** · **NEW** |
| **Excluded population sized (R2)** | Presence + Traceability | the routines mapped and the KMC isolated belong to the population the conventional form excludes, with count and source; where current buyers' routines are also mapped, both costs are stated and compared; where the excluded population is out of scope, the gate that excluded it is named | pass/fail · **HARD** · **NEW** (RD-023, Tom approved 16 Sep 2026) |
| **Capital bar stated** | Presence + Traceability | the run states every element of the capital test it applies — required return, horizon, terminal assumption, margin — each with a source, and labels the set either as the venture's ruling (dated, by whom) or as a canon rule with its citation; a bar applied without its elements stated is refused; a change to any element is a dated ruling, not an edit | pass/fail · **HARD** · **NEW** (RB-V-026; HoV countersigned 16 Sep 2026; landed 16 Sep on Tom's instruction) |
| **Classified carried items (VA-82)** | Format | every item carried out of a challenge is classified forward-referenced (owning requirement by number) / unmeasured input (owner + convergence event + falsifiable pivot trigger) / unowned design defect (blocks until a closing mechanism is named); an unclassified open-item list is inadmissible | pass/fail · **HARD** · **NEW** |
| **Independent verification artefact (VA-90)** | Presence | a requirement is closed provisionally at most until an `/ive-fit-verifier-custom` artefact for it exists in the venture folder; `/ive-consistency-audit-custom` + `/verify-venture-custom` run after F1 and after R10 | pass/fail · **HARD** · **NEW** |
| **No forward references (VA-80)** | Format | no actor or mechanism introduced at a later requirement appears in this requirement's cells; a residual carries only the later requirement's number, never its solution | pass/fail · **HARD** · **NEW** |
| **Credibility mechanism (VA-81)** | Presence + Traceability | every endorsement, signal, warranty, certification or published-record element names its receiver, the proposition, the instrument that receiver uses today, and a public-record supplier of that instrument; re-derived whenever a later requirement changes the receiver | pass/fail · **HARD** · **NEW** |
| **Conventional cost line named and removed (F2)** | Presence + Traceability | each of R4–R7 names the line of the conventional form's cost structure it replaces, with the figure that line carries in the C1 floor, or in the conventional cost table where the C1 record carries one, and the cost the design removes from it; the cost the design adds is stated on a separate line; a requirement that carries a conventional acquisition, onboarding, financing or channel cost into the new form as a given fails; "no conventional line — [reason]" passes | pass/fail · **HARD** · **NEW** (RD-030, Tom approved 21 Sep 2026; wording adjusted on the Head of Verification's opinion, 21 Sep 2026; substance as Tom approved; object-after 23 Sep 17:00) |
| **Position-holding assumption named (F3)** | Presence + Traceability | each of R8–R10 carries the position-holding table: every model assumption that depends on this requirement holding, the requirement it holds because of, and the value it fails to, as a band. Each named assumption exists in the venture's fit model; the venture's run record names the file the executable check reads. A blank table fails. Where the barrier score (SCIS/FIS/HRS) is below threshold, the fit verifier (`/ive-fit-verifier-custom`) re-tests the margin at the failure value and reports the result in its artefact — the re-test is enforced at the fit verifier, not in R8–R10 | pass/fail · **NEW** (RD-030, Tom approved 21 Sep 2026; wording adjusted on the Head of Verification's opinion, 21 Sep 2026; substance as Tom approved; object-after 23 Sep 17:00) |
| **Mode 2 verdict form (C1)** | Format + Traceability | where the cost target fails at the incumbent's volume and clears above it, the C1 financial limb prints the cut at the incumbent's volume and the clearing volume as two fixed lines; the verdict reads FAIL at the incumbent's volume; the volume gap is classified forward-referenced to R3 with the bound, never as a structural limit; any later verdict above FAIL names the C1 volume gate as the check repaired and shows the arithmetic (VA-95) | pass/fail · **HARD** · **NEW** (RD-030, Tom approved 21 Sep 2026) |

*Function gates (C3, C7, C10):*

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| **Counterfactual costed (F1 gate)** | Presence + Traceability | a `counterfactual.md` exists in the run's outputs at the C3 close gate: for a run that reaches C3 after this row lands, before the C4 state opens; for a record already past C4 when this row lands, at that record's next regeneration, with the propagation dated — the row reads from that date. The counterfactual is the C1–C3 form launched with R4–R10 conventional. The file states: that form costed with the conventional lines the later challenges attack, each as a band; the named real-business instance where one exists, costed from its public record (headcount, capital, volume, years), or a stated absence; every C1–C3 floor line checked against the instance with re-costing or a named design choice where the instance's figure is larger; the corrected floor propagated to C1–C3 under VA-103 before C4, or at the dated regeneration | pass/fail · **HARD** · **NEW** (RD-030, Tom approved 21 Sep 2026; wording adjusted on the Head of Verification's opinion, 21 Sep 2026; substance as Tom approved; object-after 23 Sep 17:00) |

### Phase 3 — Converge  (`ive-consistency-audit-custom` + VA-1)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Cross-requirement consistency | Traceability | dependency matrix built; zero hard contradictions | pass/fail |
| **Architecture synergy (the moat test) — VA-106** | **Count** | across the ten VA-106 lines, at least one names two or more other requirements | threshold |
| Real-business analogue (VA-1) | Presence | a named existing business the architecture resembles, with the shared mechanism | pass/fail |
| Convergence routing | Rule | if not cohered (no analogue / contradictions) → route back to generation, do not patch | rule · **NEW** |

### Phase 4 — Verify  (`/verify-venture-custom`)

| Mini-output | Check type | Objective test | Bar |
|-------------|-----------|----------------|-----|
| Completeness sub-score | Count | (complete + 0.5·partial) / total | scored |
| Consistency sub-score | Threshold | 100 − 15·hard − 5·soft contradictions | scored |
| Discipline sub-score | Traceability + gate | traceability % of specified detail; capped at 50 if justification-mode | scored + gate |
| **Verdict caps (VA-107)** | Rule | each cap is a band boundary, not a free number: justification mode caps at 59 (ceiling of NOT YET SOUND), parts-bin caps at 60 (floor of SOUND WITH GAPS). A cap that does not trace to a band is a defect | rule |
| **Registry coverage (added 10 Sep 2026)** | Count | the report states how many rows of this registry were applied, how many were not applicable and why, and how many could not be applied because the record lacks the element | pass/fail · **HARD** |
| Synthesis sub-score | Rubric | analogue + a declared VA-106 synergy → 100 / analogue alone → 70 / parts-bin → 30. **Scored from the VA-106 lines the run wrote, never from the critic's own reading.** For a run predating 10 Sep 2026 the synergy half is not applicable | scored |
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
- **Landed on Tom's approval, 21 September 2026 (RD-032 row "Gateway partner classed and priced against the pool (VA-147)", Phase 2 table).** Head of Verification's four tests pass, so the countersignature also stands: (a) presence-only — adds a check, changes no score model, threshold or existing row; (b) enforcement point named — the grader (this registry), with the contractual half in the R7 and R2 output contracts and regression R-C7b, R-C7c, R-R2o; (c) every term is defined in the R7 skill (SR2 two-class table, admissible reasons, stated absence, surplus at launch and at scale, the status-quo comparator) or the R2 output contract (`POOL AT RISK — R2`); (d) walked mechanically against Forge R7 v7 (mutation D, line 262: the status-quo signature) and Calmly site-scoped R7 (SR2: eight rows, no class column, no surplus at scale) — both FAIL today, as RD-032 §8 states. One observation for the row's owner, not a failure: the R7 skill's SR2 table and named-check row list three classes (loss · neutral · gain); the row, VA-147, the output contract and R-C7b say two. A neutral candidate still passes the row, because "neutral" is a stated sign.
- **Landed on Tom's approval, 21 September 2026 (RD-030 grader rows, five).** Rows (d) the ninth structural class (Phase 1, amended) and (e) the mode 2 verdict form (Phase 2 table) as RD-030 drafts them. Rows (a) the conventional cost line named and removed, (b) the position-holding assumption named and (c) the counterfactual costed at the F1 gate (Phase 2, function-gate table) with the wording changes the Head of Verification's opinion of 21 September gives (`R_and_D/hov-opinion-rd-030-2026-09-21.md`): (a) names the C1 floor as the object the figure comes from; (b) puts the SCIS/FIS/HRS failure-value re-test at the fit verifier; (c) replaces "before C4 starts" with the C3 close gate for new runs and the next dated regeneration for records already past C4, and defines the counterfactual in the row. Substance as Tom approved; the wording is object-after 23 September 2026 17:00. Reference text: `R_and_D/rd-030-f2-f3-counterfactual-rows-2026-09-16.md` §§ per row.
- **Landed on Head of Verification countersignature, 21 September 2026; object-after 23 September 2026 17:00; Tom may strike it (RD-041 §9 check-only rows 1, 2, 5, 7, 9, 10 — Phase 2 table, beneath VA-147).** Each passes the four tests: (a) presence-only — adds a check, changes no score model, threshold or gate; (b) enforcement point named — row 1 the `spread count:` verdict field and named-check row in all ten challenge skills, R-W44; row 2 the C1 SR2 block (VA-149) and the fit verifier's residue corner, R-W31; row 5 the C4 affordability-screen paragraph (VA-164), R-W46; row 7 the loop-back block, BORDERLINE line, `loop-gate branch:` verdict field and named-check row in all ten skills (VA-153), R-W35; row 9 the C7 §7 partner-return block (VA-156), R-W38; row 10 the C7 §7 count-line field (VA-155), R-W37; (c) every term is defined in the skill each cites as it stands today; (d) walked against Forge R1 v8 (rows 1, 2, 7), R2 v8 (row 7), R4 v8 (rows 5, 7), R7 v8 (rows 7, 9, 10) and Cairn Path C (row 1). Walk results, for the record: rows 1, 2, 5 and 7 FAIL on exact wording against the 17 September Forge records (margin not printed at the alternative counts; BC-3 held on an assumed hours figure; the screen computed with the marketing seat off; no `loop-gate branch:` field), row 10 PASSES (R7 v8 G15 gate block, margin zero) and row 9 is one field short of PASS (R7 v8 states share-of-surplus and the venture's own reading). No existing score moves — the critic's never-handed rule holds. Observations for the rows' owner, not failures: C1's close table carries no VA-149 named-check row and C7's carries none for VA-155 or VA-156, so the contractual half of rows 2, 9 and 10 rests on the block text alone; "the PCO's alternative counts" in row 1 resolves to the counts the PCO levelling record states, which the C7 skill does not name in those words.
- **Not landed — RD-041 §9 row 6, "Yes-threshold inside a pre-registered budget" (R3, VA-163).** Fails test (c), terms defined: the row reads "PP-1's yes-threshold", and "PP-1" is a Forge print-file component label that appears in no challenge skill; the C3 skill's own words (VA-163) are "the yes-threshold" read "inside a pre-registered acquisition budget". It also fails the 16 September generality test: Cairn Path C carries no PP-1, so the row cannot be walked against a second venture. Tests (a), (b) — C3 SR3 block, R-W45 — and (d) on Forge R3 v8 pass. The Head of R&D owns the wording; the Head of Verification does not redraft. A row that reads "the yes-threshold" in place of "PP-1's yes-threshold" would pass all four.
- **Landed on Head of Verification countersignature, 21 September 2026 (evening); object-after 23 September 2026 17:00; Tom may strike it (RD-041 §9 row 6, re-submitted as msg-20260921-1302-01 — Phase 2 table, beneath VA-155).** The re-submitted row carries the C3 skill's own words (line 258, VA-163): "the yes-threshold is read inside a pre-registered acquisition budget". The four tests: (a) presence-only — adds a check, changes no score model, threshold or gate; (b) enforcement point named — the C3 VA-163 paragraph ("two things are stated in the same file before any count is read"), read by the grader in the R3 record's scaling-strategy section, regression R-W45; (c) every term — yes-threshold, pre-registered acquisition budget, acquisition line, count, kill signal — is in that paragraph as the skill stands today, and "PP-1" is gone; (d) walked against three records. Forge R3 v8 (17 September): the budget block names "the acquisition spend R4 and R7 set" but the gate basis declares acquisition at £0 and the count is read against no budget — FAIL on exact wording, which R4 v8 §9.5 itself calls "a C3 check repaired". Forge R4 v8 §9.5: the budget line is filled per family and the count is read inside it (a legal trial's window spends £34,875 against a budget of £886 and closes; accounts and lettings spend inside theirs) — PASS. Cairn Path C, C3 stage table: stage 1 must prove "25 companies fit the template" and "the stake option is taken by ≥ 30%" before stage 2, with no acquisition budget stated beside either count — FAIL on exact wording, so the row binds a second venture. No existing score moves. Observations for the row's owner, not failures: the C3 close table (named checks) carries no VA-163 row and the verdict block no field, so the contractual half rests on the paragraph alone; the skill defines the yes-threshold by its reading rule and not in one clause (Forge R3 v8's glossary has the clause — "a yes-threshold in paying buyers at the published price by month three"); on a venture that buys companies, "acquisition" collides with the venture's own word, and the walk read it as the C3 skill does — the spend that brings the counted party in.


---

## Change log — 10 September 2026

**Three rows repaired, all in the same defect class: a criterion scored on something no design skill asked for.**

- **The synergy rows now name VA-106**, which was added to the ten challenge skills the same day. Until then the criterion was enforced at three points, one of them non-softenable, on a word that appeared in none of the eleven design skills. **No run could satisfy it, so every score carrying it was wrong rather than merely biased.** The rows now test a line the design skills require a run to write, and "none" is a passing answer.
- **The two verdict caps are now band boundaries** under VA-107, not the bare numbers 50 and 60 that appeared in no rule.
- **Registry coverage is now itself a row.** The critic is nominated in this file's opening line and did not read it. It now must, and must say how many rows it applied.

---

## Change log — 21 September 2026

**Five grader rows from RD-030 landed on Tom's approval ("approve for me", 21 September 2026).** One Phase 1 row amended (structural class: nine classes, rivalrous value source), three rows added to the Phase 2 per-requirement table (conventional cost line named and removed · position-holding assumption named · mode 2 verdict form), and the registry's first function-gate row (counterfactual costed at the F1 gate) under a new *Function gates* table in Phase 2 — the section RD-030's hygiene note said was missing. Rows (a), (b) and (c) carry the Head of Verification's wording changes; the substance is as approved. No existing score moves: the critic's never-handed rule holds, and the effect is on re-runs under the landed skill text.

**Six check-only rows from RD-041 §9 landed on the Head of Verification's countersignature under the 16 September registry-row rule** (rows 1, 2, 5, 7, 9, 10 — spread count · residue driver with legal basis · affordability screen complete · loop-gate branches · partner's return classified · count line with G15), object-after 23 September 2026 17:00, Tom may strike any of them. Row 6 (yes-threshold inside a pre-registered budget) not landed: "PP-1" is defined in no skill. Rows 3, 4 and 8 (kill band per print kind · band form refuses opposite-direction drivers · KMC admissibility, HARD) stay approve-before with Tom; the Head of Verification's opinion is in `R_and_D/hov-opinion-rd-030-2026-09-21.md`. No existing score moves.
