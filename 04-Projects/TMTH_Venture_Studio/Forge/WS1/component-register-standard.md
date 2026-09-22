# Component Register Standard — how the first register of `/venture-engineer-custom` is judged

**Owner:** Head of R&D · **Capability:** Forge WS1 — CF development
**Version:** v0.2 · **Added:** 21 September 2026, on Tom's instruction of the same day. Cause: the three registers had presence and traceability gates only (R-W28); nothing graded whether a register was a good one. **v0.2 (Head of R&D, 21 September 2026, object-after 23 September 17:00).** Cause: the Head of Verification's review of the same day (`Forge/realisation/register-review-2026-09-21.md` §5). CR-01 gains the acceptance criterion as a sixth field. CR-14 is retired; its test lives in the routine standard as RR-14. §7 is re-read against the record on disk, 84 rows.
**Parent:** `derivation-standard.md` · **Siblings:** `routine-register-standard.md` (register 2) · `position-register-standard.md` (register 3) · `realisation-standard.md` (the nine steps the registers feed)
**Applies to:** the component register a run of `/venture-engineer-custom` derives at Step 2 — every row of it, at the at-scale state.
**Used at:** `/venture-engineer-custom` Step 2 (derive) before the register is read for routing; `realisation-standard.md` step 6b and step 9; the independent inspector reads it before any first-article inspection.

**What this is, and is not.** This is a **register standard**: the quality checks for one of the three registers the engineer derives. Tier 1 is mechanical and is applied by the run. Tier 2 grades the register's craft against a named exemplar's published method. It is not a craft standard for a seat, and it does not change what the architect decides. Its output is findings, never rewrites, disposed under VA-89.

**The exemplar rule (Tom, 21 September 2026).** Three conditions bind every exemplar in §4. (1) The exemplar's method has a citable, observable source; a named exemplar with no source is opinion and may not appear. (2) The exemplar is for the craft, not the business. A register is graded against the best published way of keeping a register, never against another venture's register. (3) A routine tagged architectural is graded against the design record, not against any exemplar. That rule lives in the routine standard. It is stated here because the component register carries the tag's source.

**Review date:** 21 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date).

---

## 1 · The frame — the register that says what the venture necessitates

Four facts fix the shape of this standard.

**1. The register is a requirements traceability matrix, and the canon has kept one for fifty years.** Every requirement the design record answers maps to at least one component; every component maps to at least one requirement. The canon calls this bidirectional traceability (ISO/IEC/IEEE 15288 §6.4.2 to §6.4.4; NASA SE Handbook Rev 2, §6.2 requirements management). The engineer's skill states the same two-way check. This standard makes it gradable.

**2. The register is derived, not invented (derivation standard, 27 August 2026).** A component the run cannot cite to a section of the design record is one of two things. If it is not true, it is invention and is deleted. If it is true, it is an undocumented requirement — recorded upstream as an architecture finding first, then included. The register never carries a row on the strength of its plausibility.

**3. A register that stops at the product is a product register (Forge 1.0, 20 September 2026).** The first Forge register listed 13 rows: products, adapters and controls. It had no legal person, no instrument, no platform row, no validation record. The four enabling-system types are components in the canon's sense — without them the value-delivering components cannot exist, be built or be shown to work (15288 §4, enabling systems; SEBoK, System Realization). The type field exists so that nothing is left off because it did not look like a product.

**4. The register is a configuration item list, and its rows must be stable.** Every row carries an identifier that survives re-derivation, so the routine register and the position register can cite it (15288 §6.3.5 configuration management; MIL-HDBK-61A configuration identification). A register whose identifiers change on every run cannot be traced from.

**The conformity guard, applied to this register.** The reviewer carries conventions by training: a product backlog, a feature list, a roadmap, a bill of materials of software modules. None of these is a criterion. A component register lists what the design record necessitates, including absences and interlocks. Reward a register that carries a built absence as a row. Fail only "cannot be traced" or "cannot be cited".

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon is searched first, then IVE, then the literature, then general practice. For this register the SE canon is also the exemplar (§4): the craft of a traceability register is the canon's own craft, and no commercial practitioner has published a method that exceeds it. Section numbers are the anchors as the handbooks are indexed today; page numbers are to be added when each handbook is opened against the check, not asserted from memory.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — stakeholder needs and requirements (§6.4.2); system requirements definition (§6.4.3); architecture definition (§6.4.4); design definition (§6.4.5); configuration management (§6.3.5); information management (§6.3.6) | The requirement-to-element allocation the register records; the identifier discipline; the record's keeping |
| SE 2 | INCOSE SE Handbook, 4th ed. — technical processes (requirements definition, architecture definition, traceability); project planning (the product breakdown structure); tailoring | Every element is allocated to a requirement and every requirement to an element; the breakdown covers the system and its enabling systems |
| SE 3 | INCOSE *Guide for Writing Requirements* (INCOSE-TP-2010-006, v3, 2019) — characteristics of a requirement statement (necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming) and of a requirement set | The Tier-2 craft test: is each row's citation and acceptance criterion written to the characteristics the Guide names |
| SE 4 | NASA SE Handbook (SP-2016-6105 Rev 2) — §4.2 technical requirements definition; §6.2 requirements management (bidirectional traceability); Appendix D, the requirements verification matrix | The shape of a trace matrix; the verification method per row; the rule that a requirement with no verification method is incomplete |
| SE 5 | MIL-HDBK-61A — configuration identification; SAE EIA-649C | A configuration item has one identifier, one baseline and a change record |
| SE 6 | SEBoK — System Realization; Enabling Systems | The four enabling-system types are part of the system-of-interest's realisation, not overhead |
| IVE | R1 to R10 as the requirement set; the CTM (journey states and products); the AOM (components with `dri:`, cost lines and drivers); `derivation-standard.md` (project from C10; the launch form is a later selection); VA-134 (a component owns every act on the critical path); VA-23 | What the requirements are, what a component is, and at which state a row is read |
| Law | None at this register. Statutory components (the legal person, filings, registrations) are rows here and are inspected by `company-secretary-standard.md` and `finance-standard.md` | — |
| General practice | The product backlog; the feature list; the bill of materials; the roadmap | Named so the reviewer knows what they carry — and so a row that is an absence or an interlock is recognised as a component, not marked down |

Where a check has no SE analogue the anchor column says so. Those checks are candidate contributions for the dissertation and the INCOSE working group, per `se-canon-sources.md` §3.

---

## 3 · The shared rubric for Tier-2 checks

Tier-1 checks are mechanical: presence, count, arithmetic, traceability. Tier-2 checks are scored one to five by an independent scorer, never the producer; two scorers must agree; the pass mark is four. Each Tier-2 check names the exemplar whose method sets the anchor.

| Level | Anchor |
|---|---|
| 5 | The row carries every element the exemplar's method names for this check, each as a field in the register, and a second reader lands on the same section of the design record from the citation alone |
| 4 | As 5, but one element is a band or a placeholder with a convergence event named |
| 3 | The elements are present in prose, not as fields; or one element the method names is absent |
| 2 | The row asserts the property in a sentence and carries none of the method's elements |
| 1 | Absent |

**These descriptors are drafted for Tom's ratification and are marked so. The score model is his.** Applying the rubric is permitted; changing it is not (README, autonomy boundaries). Until ratified, a Tier-2 score is reported as diagnostic beside the Tier-1 result, and no register is refused on a Tier-2 score alone.

---

## 4 · Exemplars — who does this craft best, and the check derived from each

Every exemplar is a **candidate for Tom**. Each has a citable, observable source (condition 1) and is an exemplar for the craft of keeping a traceability register, not for any business (condition 3).

| Exemplar | Source (citable, observable) | The check derived | Status |
|---|---|---|---|
| The SE canon's requirements traceability matrix | NASA SE Handbook Rev 2, Appendix D and §6.2; ISO/IEC/IEEE 15288 §6.4.3 and §6.4.4 | CR-06 to CR-08 (two-way trace); CR-16 (allocation completeness) | Candidate. Free; the most readable statement of the construct |
| INCOSE's characteristics of a well-written requirement | INCOSE *Guide for Writing Requirements*, INCOSE-TP-2010-006, v3 (2019), §4 characteristics C1 to C9 and set characteristics C10 to C14 | CR-15 (the citation is unambiguous); CR-17 (the acceptance criterion is singular and verifiable) | Candidate. Members have it; the characteristics are also reproduced in the Handbook |
| Configuration identification | MIL-HDBK-61A (free); SAE EIA-649C | CR-03 (one stable identifier per row); CR-22 (change dated) | Candidate. Free |
| Avionics software trace data | RTCA DO-178C §5.5 (trace data between requirements, design, code and tests, in both directions) | Considered and not used at v0.1: it adds no element the NASA matrix lacks, and it is paid | Not used — reason stated |

**No commercial exemplar is named.** The search was made (condition 1). Commercial traceability practice is tool documentation, not an observable method with a source that can be cited independently of a vendor. The canon is the exemplar for this register. If Tom names a practitioner whose register method is published and observable, it is added here with its check.

---

## 5 · The checks

Each check is a question the reviewer puts to the component register or to one of its rows. Each names its tier, its anchor, what passes, and what the failure is under VA-89. "Row" means one component; "record" means the venture design record and its model files; "the two other registers" means the routine and position registers derived from this one.

### Group A — Fields and identity

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-01 | Does every row carry the six fields — component · type · the requirement(s) and design-record section it satisfies · owning seat · the standard that inspects it · the acceptance criterion (one condition, and the method that tests it) — with none blank? *(v0.2: the sixth field added. Reason: CR-17 grades the acceptance criterion and CR-20 reads it, so the field list must name it; NASA App. D — a requirement with no verification method is incomplete. The engineer's register-1 list names five; adding the sixth there is a build item for the skill's owner. Head of R&D, 21 September 2026, object-after 23 September 17:00.)* *(R-W52 as rewritten: three columns the engineer's artefact contract supplies are fields of this list too — the identifier (CR-03), the state (CR-05; its content read by CR-20 and CR-22) and the launch-form column (CR-13). CR-01 does not test them for blanks because each has its own check. Head of R&D, 21 September 2026, later; object-after 23 September 17:00.)* *(Re-sort: two more fields, on an `external gate` row only — the act that closes the gate, and who performs it (CR-11). Head of R&D, 21 September 2026, night; object-after 23 September 17:00.)* | 1 | 15288 §6.4.3; NASA App. D (the matrix columns, verification method per row); `/venture-engineer-custom`, register 1 and completion protocol (2) | Six fields on every row | A blank field → design defect on the row |
| CR-02 | Is every row's type one of the eight the engineer names — Working Product · Communications Product · Payment Product · Partner Product · Instrument or agreement · Legal person and money apparatus · Platform and stack · Validation record? | 1 | SEBoK, Enabling Systems; the engineer's type table | Every type is one of the eight | A type outside the eight → design defect (the type table is incomplete, or the row is not a component) |
| CR-03 | Does every row carry one identifier that is stable across re-derivations — the same component keeps the same identifier when the register is refreshed — and is the identifier the one the two other registers cite? | 1 | MIL-HDBK-61A configuration identification; 15288 §6.3.5 | Identifiers unchanged on refresh for unchanged components; every citation from the other registers resolves | An identifier that changed for an unchanged component → design defect; a citation that does not resolve → design defect |
| CR-04 | Does the register open with a design-authority line naming the highest-numbered ratified design record (R-W28a), and does every row's citation resolve to a section that exists in that version? | 1 | 15288 §6.3.5 (the baseline); `/venture-engineer-custom` Step 1a | Authority line present; every citation resolves | A citation to a superseded version → design defect on the row; no authority line → the register is not read |
| CR-05 | Does every row's state use the engineer's vocabulary and no other — `absent` · `derived` · `specified` · `reviewed` · `test product` · `realised (conditional)` · `realised (inspected)` · `external gate` · `NCR`? | 1 | `/venture-engineer-custom` item completion protocol; 15288 §6.3.5 (status accounting) | Every state is one of the nine | "done", "built", "complete" or any other word → reclassified on sight to the highest state the evidence supports |

### Group B — Two-way traceability

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-06 | Forward: does every requirement R1 to R10, and every sub-requirement the design record answers, map to at least one row? | 1 (count) | NASA §6.2 bidirectional traceability; 15288 §6.4.4 allocation | Zero requirements with no row | A requirement with no row → architecture finding (a gap), then a row |
| CR-07 | Backward: does every row map to at least one requirement, by section? | 1 (count) | Same | Zero rows with no requirement | A row with no requirement → deleted if not true; recorded upstream as an architecture finding then kept, if true (the derivation standard's rule) |
| CR-08 | Is each of the four enabling-system types present — Instrument or agreement · Legal person and money apparatus · Platform and stack · Validation record — with at least one row each, or a stated reason a type has none? | 1 (count) | 15288 §4 enabling systems; SEBoK System Realization; the 20 September finding | Four types present or reasoned absent | A type absent with no reason → design defect (a product register, not a component register) |
| CR-09 | Is every architectural prohibition in the design record a row (a built absence), and every operating rule that binds at runtime a row (an interlock that refuses)? | 1 (traceability) | "Build the absence, not the permission" (Calmly Head of Product, August 2026). **No SE analogue** — the canon allocates functions; it has no construct for allocating a prohibition as a built element | Every prohibition and every runtime rule in the record has a row | A prohibition with no row → design defect |
| CR-10 | Is every act on the critical path owned by a row — including the acts only a principal can perform — so that no step of the journey depends on an unlisted actor (VA-134)? | 1 (traceability) | VA-134; NASA App. D (every requirement has an owner) | Every critical-path act traces to a row | An act with no row → design defect |
| CR-11 | Is every external gate a row — with state `external gate`, the act that closes it, and who performs the act — never a footnote? | 1 | `/venture-engineer-custom` Step 2 ("External gates are rows"); 15288 §6.4.10 transition (acceptance events) | Every external dependency is a row with the three fields | A gate in a footnote or a note column → design defect |
| CR-12 | Does every handoff between rows name the row that owns the next step, so that no interface is left with one side? | 1 (traceability) | NASA §6.3 interface management; 15288 §6.4.4 | Every interface names both rows | A handoff with one owner → architecture finding |

### Group C — The at-scale state

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-13 | Is every row derived at the at-scale state (C10), with what is true on day one held in a separate launch-form column — and does no row mix the two? | 1 | `derivation-standard.md` state rule; VA-23 | Every row at C10; the launch column separate | A launch-only sentence beside a figure true only at scale → design defect (state mixing) |
| CR-14 | *Retired at v0.2 (Head of R&D, 21 September 2026, object-after 23 September 17:00).* The test — every volume driver is a reference to a named quantity in the model, never a sentence — lives in the routine standard as RR-14. Reason: a component does not carry volume; the routines that run it do, and the routine row is where hours are sized from the driver (VA-140 names an activity's driver, and an activity is a routine row). CR-01 names no volume field, so a register that conformed to CR-01 failed CR-14 on every row; a check must test a field the standard names (R-W52). The identifier is kept so earlier reviews still resolve. | — | VA-140; MIL-STD-881 (volume sits on the work package, not the element) | — | — |

### Group D — The quality of the trace (Tier 2, against the named exemplar)

| ID | Question to the row | Tier | Exemplar · source · the element graded | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-15 | Is the citation on each row specific enough that a second reader, given only the citation, lands on the same section and the same sentence of the design record? | 2 | INCOSE *Guide for Writing Requirements* v3 — C3 unambiguous, C9 conforming · the citation's precision | Score ≥ 4 | Score < 4 → design defect (an imprecise citation cannot be verified) |
| CR-16 | Taken together, do the rows allocated to one requirement satisfy the whole requirement as the record states it — every clause, not the first clause? | 2 | NASA SE Handbook Rev 2, §6.2 and App. D — allocation completeness · the set of rows against the requirement's clauses | Score ≥ 4 | Score < 4 → architecture finding (a clause with no row) |
| CR-17 | Is each row's acceptance criterion singular and verifiable — one condition, testable by a named method — and does passing it evidence the Level-1 chain rather than decorate it? | 2 | INCOSE *Guide for Writing Requirements* v3 — C6 singular, C7 verifiable; NASA App. D (verification method per row); `/venture-engineer-custom` completion protocol (2) · the acceptance criterion | Score ≥ 4 | Score < 4 → design defect (a criterion a component can pass while the loss survives) |

### Group E — Ownership and inspection

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-18 | Is every owning seat a role title — never a person, never "Founder" — and does the same title appear in the position register? | 1 | Tom, 10 September 2026 (a DRI is a role); ANSI/EIA-748 (one responsible manager per account); `position-register-standard.md` PS-02 | Every seat is a role and resolves to a position row | A person or "Founder" in the seat field → design defect; a seat with no position row → design defect in the position register |
| CR-19 | Does every row name the standard that inspects it — a file in the standards library — or carry the line "standard missing" with the seat named, logged in the README gap list? | 1 | `realisation-standard.md` step 9; README standards-library rule | Every row names a standard or logs the gap | A row with neither → build item (owner: the venture's product seat, whatever its title — the seat the position register names as owning the component's product; Forge has no seat titled Head of Product) |
| CR-20 | Where a row's state is `realised (conditional)` or `realised (inspected)`, does it cite an inspection record written by a seat that ran no part of the build? | 1 | "No self-certification" (4 and 20 September 2026); AS9102 first-article inspection | Every realised row cites an independent record | No record, or the builder's own → reclassified to `test product` |

### Group F — The record

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CR-21 | Does the register live in `realisation-record.md` under the venture's realisation folder, per the artefact contract, and nowhere else? | 1 | `/venture-engineer-custom` artefact contract; VA-45 (state lives in the record) | One location | A second copy → design defect (two baselines) |
| CR-22 | Is every state change dated, with the record that caused it named — an inspection record, a fabrication brief, an architecture finding? | 1 | 15288 §6.3.5 (status accounting); MIL-HDBK-61A | Every change carries a date and a cause | An undated change → design defect |
| CR-23 | Does the register carry a row count by type and by state, and do the counts reconcile to the rows? | 1 (arithmetic) | 15288 §6.3.6 information management | Counts match | A mismatch → design defect (arithmetic) |

**Count: 22 live checks** — 19 Tier 1, three Tier 2; CR-14 retired at v0.2, identifier kept. *(Head of R&D, 21 September 2026, object-after 23 September 17:00.)*

**Kinds under R-W52 (as rewritten 21 September 2026, later; sorted by first part, and re-sorted the same day, night, on the Head of Verification's second application, A3 and A4):** row-field checks, eight — CR-01, CR-02 (type), CR-03 (identifier; second part row-content — the identifier against the citations in the two other registers), CR-05 (state), CR-07 (the requirement field, on every row), CR-13 (the launch-form column; second part a content judgement — a launch sentence beside an at-scale figure), CR-18 (owning seat; second part row-content — the title against the position register), CR-19 (the standard that inspects; second part row-content — the gap line against the README gap list). Row-content checks, five — CR-04 and CR-15 (the citation against the design record), CR-17 (the acceptance criterion), CR-20 (the state against an inspection record), CR-22 (a state change against the record that caused it). Register checks, nine — CR-06 and CR-08 to CR-12 (coverage, presence, interfaces; CR-11 reads the register against `external-gates.md`, and its second part is row-field — the state, the act that closes the gate and who performs it, three CR-01 fields on each gate row), CR-16 (the rows of one requirement against the whole requirement), CR-21 (location), CR-23 (counts). Eight plus five plus nine is 22. *(Head of R&D, 21 September 2026, later; object-after 23 September 17:00.)* *(Re-sort. CR-07 moved from register to row-field: it reads the requirement field of every row, and one row with no requirement fails it alone. CR-11 stays register: its first part is coverage — every gate a row — read against `external-gates.md`; the two gate fields it reads are now named in CR-01. A check is sorted by its first part, and a second part of another kind is named beside the sort — R-W52's fifth FAIL form. Head of R&D, 21 September 2026, night; object-after 23 September 17:00.)*

---

## 6 · What a failed check becomes

A failed check is disposed under VA-89 and nothing else. The reviewer classifies; the reviewer does not fix.

| Failure | Class | What the record must carry |
|---|---|---|
| A field, identifier, citation, row or count is absent, or two figures disagree | **Design defect** | The check ID and the row; the register returns to Step 2 |
| A requirement, clause or act with no row | **Architecture finding** (VA-89 design defect, routed upstream) | The requirement and the section; sent to `/architect-custom` before a row is added |
| The inspecting standard does not exist | **Build item** (caps at PROVISIONAL) | Owner (Head of Product), the seat, the README gap line |
| The row exists in the design and no independent inspection exists yet | **State reclassified** | The highest state the evidence supports; no VA-89 class needed |
| A standing ruling forbids the fix | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect (VA-89's own residual rule).

---

## 7 · Worked application — the two Forge registers, 20 and 21 September 2026

*(§7 re-read at v0.2 — Head of R&D, 21 September 2026, object-after 23 September 17:00. The v0.1 table graded a 103-row draft with PR- and ST- identifiers that the record no longer carries. This table grades the record on disk: 84 component rows. Types: WP 10 · CP 5 · PP 4 · PtP 3 · IN 11 · LM 10 · PL 24 · VR 17. States: derived 53 · external gate 13 · realised (conditional) 7 · NCR 7 · absent 4. Results are the Head of Verification's (`register-review-2026-09-21.md` §1.1), re-counted by this seat.)*

Two registers exist. The 20 September register (`Forge/forge-1.0-at-scale-component-register-2026-09-20.md`, 13 rows, authority 29 May 2026) and the 21 September realisation record (`Forge/realisation/realisation-record.md`, 84 rows, authority VDR v6.1). Read against the standard:

| Check | 20 September register | 21 September record (84 rows) |
|---|---|---|
| CR-01 | Fails — no owning seat field, no inspecting standard field | Fails — VR-08 carries a blank cell; and at v0.2 the acceptance criterion is not a column, so every row fails until it is added |
| CR-02 | Fails — types are product, platform, operations; no enabling types | Passes — every row is one of the eight types |
| CR-03 | Fails — no identifiers | Passes within the record; whether an identifier survives a refresh is unknown until the second run (the R-W48 instance) |
| CR-04 | Fails — authority is the 29 May package (the R-W28a instance) | Passes — authority line names v6.1; every citation resolves |
| CR-05 | Fails — "Test product built", "To build", "Documentation build" | Passes — the nine states only |
| CR-06 | Not run — no requirement column | Passes — every requirement R1 to R10 has at least one row |
| CR-07 | Not run | Fails — VR-09 cites no requirement and is absent from §5.9 |
| CR-08 | Fails — no instrument, legal person, platform or validation rows | Passes — IN 11, LM 10, PL 24, VR 17 |
| CR-09, CR-10 | Not run | Pass — the prohibitions and the critical-path acts are rows; the acts only a principal can perform (IN-04, IN-10, IN-11) are rows whose owner CR-18 catches |
| CR-11 | Fails — gates in the evidence column | Passes — 13 rows at `external gate`, and `external-gates.md` beside them |
| CR-12 | Not run | Fails — no interface field; no handoff names the row that owns the next step |
| CR-13 | Not run | Passes — the launch form is its own column |
| CR-14 | — | Retired at v0.2; the finding (no volume reference on any row) is read under RR-14 |
| CR-15, CR-16, CR-17 | Not scored | Diagnostic: 3, 3, 1 — no acceptance criterion exists on any row (the CR-17 score is the reason CR-01 now names the field) |
| CR-18 | Fails — no seat field | Fails on 44 rows — seven name a person or a title that is not a seat in the position register (IN-04, IN-10, IN-11, VR-05, VR-07, VR-08, VR-10); 37 name more than one seat |
| CR-19 | Fails — no standard named | Fails on one row — PL-12 names "both standards" |
| CR-20 | Fails — "Test product built" with no inspection record | Fails on seven rows — WP-01, WP-02, WP-06, PP-01, PL-01, VR-12, VR-13 rest on the builder's own statement; reclassified to `test product` |
| CR-21 | — | Passes — one location |
| CR-22 | No dates | Fails — no state change carries a date and a cause |
| CR-23 | No counts | Fails — §10 states 17 · 8 · 8 · 5 where the rows give 13 · 7 · 7 · 4 |

**Tier-1 verdict on the 21 September record: FAIL.** Eight live checks fail: CR-01, CR-07, CR-12, CR-18, CR-19, CR-20, CR-22 and CR-23. CR-14 also failed as it stood at v0.1; it is retired and its test now runs as RR-14. *(Count corrected 21 September 2026, later, on the Head of Verification's v0.2 review §5.2 item 4.)* The register is not read for routing until the record returns from Step 2. Every failure is a design defect on the record, with two exceptions. CR-07 is an architecture finding. The seven CR-18 rows where the design record itself names the principal are an architecture finding (DA-14).

---

## 8 · What this standard does not cover

- **Whether the design is right.** The architect's referee is the criteria registry. This standard reads whether the register traces the design, not whether the design should be built.
- **The routines a component needs, or the seat that runs them.** `routine-register-standard.md` and `position-register-standard.md`.
- **How a component is built well.** The craft standard the row names.
- **The launch form.** Which rows are true on day one is the launch-form column's business and the pilot-instance record's; this standard checks only that the column is separate (CR-13).
- **Scoring the Tier-2 rubric.** The descriptors in §3 are drafted for ratification and stay Tom's to change.

---

## 9 · Reviewer checklist — before the register is read for routing

- [ ] The design-authority line names the highest-numbered ratified design record, and the reviewer opened that file
- [ ] Every row's six fields were read; CR-01 to CR-05 applied row by row *(six from v0.2)*
- [ ] The forward count (CR-06) and the backward count (CR-07) were both made, and the two numbers written into the review
- [ ] The four enabling types were counted (CR-08)
- [ ] Each Tier-2 check was scored by two people who did not derive the register, and reported as diagnostic until the rubric is ratified
- [ ] Each failed check carries one VA-89 class and the fields that class needs
- [ ] The conformity guard was applied: a built absence or an interlock was not marked down for not looking like a product
- [ ] No launch fact was read against any at-scale row (CR-13)
- [ ] The review cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## Related

- `.claude/skills/venture-engineer-custom/SKILL.md` — register 1, Step 2, the completion protocol
- `routine-register-standard.md` · `position-register-standard.md` — the two registers derived from this one
- `derivation-standard.md` — cite or delete; the state rule
- `se-canon-sources.md` — the search order; add CR-09 to §3 as a candidate finding
- `regression-set.md` — R-W28 (presence and order); R-W48 (this standard); R-W52 (every check tests a named field)
- `Forge/forge-1.0-at-scale-component-register-2026-09-20.md` · `Forge/realisation/realisation-record.md` — the two registers read in §7

**Version line.** v0.2, 21 September 2026, Head of R&D, object-after 23 September 2026 17:00. Changes: CR-01 six fields (acceptance criterion added); CR-14 retired to RR-14; §7 re-read against the 84-row record; 22 live checks. v0.1, 21 September 2026, Head of R&D, on Tom's instruction; 23 checks; canon anchors as stated; one check with no SE analogue (CR-09). Exemplars: the SE canon only, with the reason in §4. Tier 1 ratifies object-after 23 September 2026 17:00 unless Tom objects; Tier 2 (§3 descriptors, §4 exemplars, CR-15 to CR-17) is approve-before.
