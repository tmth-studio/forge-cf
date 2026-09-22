# Routine Register Standard — how the second register of `/venture-engineer-custom` is judged

**Owner:** Head of R&D · **Capability:** Forge WS1 — CF development
**Version:** v0.2 · **Added:** 21 September 2026, on Tom's instruction of the same day. Cause: the routine register had presence and traceability gates only (R-W28b); nothing graded whether the register described a good operation. **v0.2 (Head of R&D, 21 September 2026, object-after 23 September 17:00).** Cause: the Head of Verification's review of the same day (`Forge/realisation/register-review-2026-09-21.md` §5). RR-01 is now the single field list, thirteen fields, and every check names the field it tests. RR-07 states when a reason per group passes. RR-19 states what the reviewer does when RR-03 has failed. §7 is re-read against the record on disk, 57 rows.
**Parent:** `derivation-standard.md` · **Siblings:** `component-register-standard.md` (register 1, which this register cites) · `position-register-standard.md` (register 3, which cites this one) · the craft standards (what each seat's routines must do)
**Applies to:** the routine register a run of `/venture-engineer-custom` derives at Step 2 — every row, at the at-scale state.
**Used at:** `/venture-engineer-custom` Step 2 before the register is read for routing; `realisation-standard.md` step 6b and step 9; every seat's craft-standard review reads its own routines from this register.

**What this is, and is not.** This is a **register standard**: the quality checks for the second of the three registers. Tier 1 is mechanical and is applied by the run. Tier 2 grades each routine against either a named exemplar's published method or the design record, and which of the two depends on the routine's tag (§1, fact 2). It is not a craft standard for any seat. Its output is findings, never rewrites, disposed under VA-89.

**The exemplar rule (Tom, 21 September 2026).** (1) Every exemplar's method has a citable, observable source; a named exemplar with no source is opinion and may not appear. (2) Every routine is tagged **conventional** or **architectural**. A conventional routine is graded against the exemplar's method. An architectural routine — one that implements an R1 to R10 move — is graded against the design record, and matching the conventional exemplar there is a **defect**. (3) The exemplar is for the craft of running a routine, not for the business.

**Review date:** 21 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date).

---

## 1 · The frame — the register that says what running the venture costs

Five facts fix the shape of this standard.

**1. The register is the work breakdown over the system and its enabling systems.** Every component in the first register needs three kinds of routine. **Make-work** runs it at the C10 volume. **Fail** fires when it does not. **Manage** monitors, decides and changes it — including who may halt it and who may alter it. The canon calls the list a work breakdown structure and requires it to cover the enabling systems, not only the product (INCOSE SE Handbook 4th ed., project planning; MIL-STD-881; SEBoK System Realization). The fail kind is the canon's failure modes and effects analysis applied to the journey states (IEC 60812). The manage kind is project assessment and control (15288 §6.3.2).

**2. Two classes of routine, two referees (Tom, 21 September 2026).** Most routines are conventional: a complaints routine, a monthly close, a re-run on a ratified change. The trade knows how to do these well, and the best published methods are the referee. Some routines are architectural: they are the R1 to R10 moves themselves — the origination routine R4 designs, the partner activation R7 designs, the payment routine R6 designs. IVE removes the bottleneck the conventional form pays for (F2, Tom, 16 September 2026: R4 to R7 remove the blocks the conventional form solves with spend). Grading an architectural routine against the conventional exemplar reintroduces the cost the design removed: an origination routine graded against a pipeline-sales method books the acquisition cost R4 eliminated. So an architectural routine is graded against the design record, and a match to the conventional exemplar is a design defect, not a pass. **The tag is a Tier-1 field on every row.**

**3. The second source (Head of Verification, Calmly, September 2026).** Routines derived only from components omit origination by construction — nothing fails if a funder is never approached; the journey never starts. The origination routines are derived directly from the requirements: R4 attraction, R7 partner activation, R3 the raise, R10 supplier terms. Each has a seat and an hours figure. A routine register with no routine sourced from a requirement directly is incomplete, and its cost floor is understated by the absent line.

**4. A routine is realised as four things (the engineer's rule).** The written procedure, the tool or interlock it runs on, the record it leaves, and the seat trained on it. A routine with only the procedure written is `specified`, not `realised`. The four-things test is the realised test in this standard. It is the same test the best-sourced exemplars apply: Amazon's mechanism is tool plus adoption plus inspection; Google's on-call is a playbook plus a trained rota plus a postmortem record.

**5. Hours are the output (VA-91, VA-140).** Every row states hours per cycle at the C10 volume, a frequency, and the counted thing the frequency scales with, as a reference to a named quantity in the model. The sum per seat is what the position register carries; the sum over all seats is what the financial simulation must reproduce. A row with no hours is a cost line missing from the floor.

**The conformity guard, applied to this register.** The reviewer carries conventions by training: a sales pipeline with stages, an onboarding programme, a quarterly business review, an account manager, a collections routine. For a conventional routine these are the exemplar's raw material and the method applies. For an architectural routine they are the thing the design removed. Reward the architectural routine that departs from the trade. Fail the architectural routine that matches it.

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon is searched first, then IVE, then the function's own literature, then general practice. The SE canon fixes the construct each check implements. The exemplars in §4 supply the content of the Tier-2 checks. Section numbers are the anchors as the handbooks are indexed today; page numbers are to be added when each is opened against the check.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — project planning (§6.3.1); project assessment and control (§6.3.2); configuration management (§6.3.5); information management (§6.3.6); measurement (§6.3.7); operation (§6.4.12); maintenance (§6.4.13) | The manage kind; the record each routine leaves; the hours as a measure; the run and the repair of the system in service |
| SE 2 | INCOSE SE Handbook, 4th ed. — project planning (the work breakdown structure); specialty engineering: human systems integration (task load), training needs analysis, reliability (a fault must be detectable), system safety (the independent monitor) | The breakdown over the system and its enabling systems; the human's task is designed and trained; the fail routine needs a detectable fault; the watcher is separate from the watched |
| SE 3 | MIL-STD-881 (work breakdown structures for defense materiel items) | A work breakdown is product-oriented and complete: every element of the system, including enabling elements, has work under it |
| SE 4 | IEC 60812 — failure modes and effects analysis | The fail kind: for each state a component should reach, the failure mode and the routine that fires |
| SE 5 | INCOSE technical measurement (Roedler and Jones 2005), applied through `tpm-measurement-standard.md` | Every hours figure is a technical performance measure: band, evidence, convergence event, trigger |
| SE 6 | NASA SE Handbook (SP-2016-6105 Rev 2) — §6.1 technical planning; §6.7 technical assessment; §6.8 decision analysis | The routine's decision rights are fixed before it runs; a decision is recorded with its maker |
| SE 7 | ANSI/EIA-748 — one responsible manager per control account | Every routine has one accountable seat; every cost line names its routine |
| IVE | R1 to R10 as the moves the architectural routines implement; F2 and F3 (Tom, 16 September 2026); the CTM journey states (the fail routines' parent); the AOM activities and drivers; VA-140; VA-23; the 4 September rules (two parents; run, manage, hold; F2; the re-run routine) | Which routines are architectural, what each must implement, and at which state each figure is read |
| Function 1 | Bryar and Carr, *Working Backwards* (St Martin's Press, 2021) — the mechanism: a complete process with a tool, adoption and inspection | The conventional routine is a mechanism, not an intention: tool, adoption, inspection |
| Function 2 | Beyer, Jones, Petoff and Murphy (eds.), *Site Reliability Engineering* (O'Reilly, 2016; free at sre.google) — ch. 5 eliminating toil; ch. 11 being on-call; ch. 14 managing incidents; ch. 15 postmortem culture. *The Site Reliability Workbook* (2018) | The fail routine: a playbook the on-call seat can run without the author; a response target; a blameless postmortem that writes back into the procedure. The make-work routine: its manual share is measured and automated as it scales |
| Function 3 | Ohno, *Toyota Production System* (Productivity Press, 1988); Liker, *The Toyota Way* (McGraw-Hill, 2004), principle 6 — standardised work | The make-work routine states the sequence, the time per cycle and the standard in-process stock, and is the current best-known way with a route for the performer to improve it |
| Function 4 | Gawande, *The Checklist Manifesto* (Metropolitan Books, 2009) — pause points; killer items; five to nine items; read-do against do-confirm; tested in use | The routine with a costly omission carries a checklist of that form |
| Function 5 | FAA Advisory Circular 120-71B, *Standard Operating Procedures and Pilot Monitoring Duties* (2017; public) | The written procedure's form: who does each step, when it is triggered, the action, the expected result, the confirmation |
| General practice | The sales pipeline; the onboarding programme; the quarterly business review; the account manager; the collections routine | Named so the reviewer knows what they carry — and so an architectural routine that departs from them is rewarded, not marked down |

Where a check has no SE analogue the anchor column says so. Those checks are candidate contributions for the dissertation and the INCOSE working group, per `se-canon-sources.md` §3.

---

## 3 · The shared rubric for Tier-2 checks

Tier-1 checks are mechanical: presence, count, arithmetic, traceability. Tier-2 checks are scored one to five by an independent scorer, never the producer; two scorers must agree; the pass mark is four. There are two rubrics, selected by the row's tag.

**Rubric A — a conventional routine, against the exemplar's method**

| Level | Anchor |
|---|---|
| 5 | The routine carries every element the exemplar's method names for this check, each as a field or a named artefact in the register, and the reviewer can check each from the record |
| 4 | As 5, but one element is a band or a placeholder with a convergence event named |
| 3 | The elements are present in prose, not as fields; or one element the method names is absent |
| 2 | The routine names the exemplar or the method and carries none of its elements |
| 1 | Absent, or the trade's convention copied without the exemplar's elements |

**Rubric B — an architectural routine, against the design record**

| Level | Anchor |
|---|---|
| 5 | The routine implements the requirement's move as the design record states it; the conventional routine it replaces is named with the cost line removed; no removed cost line reappears; the reviewer can reproduce the routine from the cited section |
| 4 | As 5, but one figure is a band with no convergence event |
| 3 | Implements the move, and carries one element of the conventional routine the record removed — a stage, a cost line, an intermediary |
| 2 | The conventional exemplar's routine with the requirement's name on it |
| 1 | Absent |

**A score of 3 or below under rubric B is a design defect, never a build item** — the design removed the element and the routine put it back. Under rubric A a score below four is disposed by the check's own column.

**These descriptors are drafted for Tom's ratification and are marked so. The score model is his.** Applying either rubric is permitted; changing one is not (README, autonomy boundaries). Until ratified, a Tier-2 score is reported as diagnostic beside the Tier-1 result, and no register is refused on a Tier-2 score alone.

---

## 4 · Exemplars — who does this craft best, and the check derived from each

Every exemplar is a **candidate for Tom**. Each has a citable, observable source (condition 1) and is an exemplar for the craft of running a routine, not for any business (condition 3). Applies to conventional routines only (condition 2).

| Exemplar | Source (citable, observable) | The check derived | Status |
|---|---|---|---|
| Amazon — the mechanism | Bryar and Carr, *Working Backwards* (2021): a mechanism is a complete process — a tool, adoption, inspection — as against a good intention. Chapter to be confirmed when the book is opened | RR-21 (tool, adoption, inspection on every conventional routine) | Candidate. Practitioners' own account; the construct is stated in one sentence and is checkable |
| Google — site reliability engineering | Beyer et al. (eds.), *Site Reliability Engineering* (2016), ch. 5, 11, 14, 15; free online | RR-22 (the fail routine: playbook, on-call, postmortem); RR-23 (the make-work routine: toil measured and automated) | Candidate. Free; the most complete published account of fail routines at scale |
| Toyota — standardised work | Ohno (1988); Liker (2004), principle 6: work sequence, time per cycle, standard in-process stock; the standard is the current best way and is improved by the performer | RR-24 (sequence, cycle time, in-process stock, improvement route) | Candidate. Two independent published accounts of the same method |
| Gawande — the checklist | Gawande (2009): pause points, killer items, five to nine items, read-do against do-confirm, field-tested | RR-25 (the checklist at a costly pause point) | Candidate. The method is described with its derivation from aviation and its test in eight hospitals |
| **Added — FAA standard operating procedures** | FAA AC 120-71B (2017), public regulatory guidance on the design of a written procedure and the monitoring duty | RR-06 (the procedure's form — who, when, action, expected result, confirmation) | Candidate, **added by this draft**. Why: it is a regulator's published standard for the form of a procedure, audited in the field, free, and it is the source Gawande's method draws on. It grades the written procedure itself, which none of the four above does directly |

**The architectural class has no exemplar.** Its referee is the design record and the requirement's own section (rubric B). This is by rule (Tom, 21 September 2026), not by omission.

---

## 5 · The checks

Each check is a question the reviewer puts to the routine register or to one of its rows. Each names its tier, its anchor, what passes, and what the failure is under VA-89. "Row" means one routine; "component" means the component-register row it cites; "record" means the venture design record and its model files.

### Group A — Fields, the tag, and the realised test

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-01 | Does every row carry the thirteen fields, with none blank? **This list is the single source. Every row-field check in this standard reads one of these fields and names it; row-content and register checks are sorted at the count line (R-W52 as rewritten 21 September 2026, later).** (1) routine · (2) component, or requirement for origination · (3) kind · (4) class tag, with the requirement citation on an architectural row or the exemplar name on a conventional row · (5) accountable seat · (6) trigger · (7) frequency, its driver a reference to a named model quantity · (8) hours per cycle at C10 volume · (9) hours per year, printed as the product · (10) the hours' measurement — band · evidence basis · convergence event · trigger · (11) decision rights — the four columns on a manage row · (12) state, with the four pointers when `realised` · (13) the record it leaves. An architectural row also carries the conventional routine it replaces and the cost line removed (RR-18). The launch form is a separate column and never an at-scale field (RR-16). *(v0.2: eight fields became thirteen. Reason: RR-03, RR-05, RR-13, RR-15 and RR-26 tested fields the eight did not name, so a register could pass RR-01 and fail them on absence. The engineer's register-2 list names eight; adding the rest there is a build item for the skill's owner. Head of R&D, 21 September 2026, object-after 23 September 17:00.)* | 1 | 15288 §6.3.6 information management (one defined shape for the record); MIL-STD-881 (the work-breakdown dictionary defines every element's fields once); `/venture-engineer-custom`, register 2 | Thirteen fields on every row | A blank field → design defect on the row |
| RR-02 | Is every row's kind one of three — make-work · fail · manage? | 1 | The engineer's three kinds; IEC 60812 (fail); 15288 §6.3.2 (manage) | Every kind is one of the three | Another word → design defect |
| RR-03 | Does every row carry the tag `class: conventional` or `class: architectural` — and does an architectural row cite the requirement (R1 to R10) and section whose move it implements, while a conventional row names the exemplar method from §4 it is graded against? | 1 | RR-01 field 4 *(v0.2)*; Tom, 21 September 2026 (condition 2); F2. **No SE analogue** — the canon has no class of work package that must differ from the trade's form | Tag on every row; the citation or the exemplar name beside it | Tag absent → design defect; an architectural row with no requirement → reclassified conventional and re-graded; a conventional row with no exemplar → design defect |
| RR-04 | Does every row name exactly one accountable seat — a role title, never a person — and does that seat exist in the position register? | 1 | RR-01 field 5 *(v0.2)*; ANSI/EIA-748 (one responsible manager); Tom, 10 September 2026 (a DRI is a role); `position-register-standard.md` PS-05 | One seat per row; every seat resolves | Two seats, none, or a person → design defect |
| RR-05 | Does the row's state read `realised` only when all four things exist with a pointer to each — the written procedure · the tool or interlock it runs on · the record it leaves · the seat trained on it — and `specified` when only the procedure exists? | 1 | RR-01 field 12 *(v0.2)*; the engineer's four-things rule; Handbook 4th ed. training needs analysis; Bryar and Carr (tool, adoption, inspection) | Four pointers on every realised row | `realised` with fewer than four → reclassified to `specified`; the missing thing → build item with owner |
| RR-06 | Does the written procedure state, for each step, who performs it, what triggers it, the action, the expected result and the confirmation that it happened? | 1 | RR-01 field 12, the written procedure the state points to *(v0.2, later)*; FAA AC 120-71B (the form of a standard operating procedure); Handbook 4th ed. human systems integration | Five elements per step | A step with no performer or no confirmation → build item (owner: the seat) |

### Group B — Coverage and the two sources

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-07 | Does every component in the component register have all three kinds of routine, or a stated reason per kind it lacks? **A reason given for a group of components passes only when the group lists every member by identifier and the reason is true of each member.** A reason for a type or a class by name ("all platform rows") is not a reason for any component in it. *(v0.2 position. Canon: IEC 60812 lists failure modes per item and excludes an item only by name; MIL-STD-881's dictionary carries an entry per element. Head of R&D, 21 September 2026, object-after 23 September 17:00.)* | 1 (count) | MIL-STD-881 (every element has work under it); IEC 60812; `/venture-engineer-custom` Step 2 ("Check the kinds") | Three kinds or a reason, per component; a group reason lists its members | A component with a kind absent and no reason → design defect (the derivation is incomplete); a group reason that names no members → design defect on every component the group could contain |
| RR-08 | Does every row cite either a component-register row, or — for origination — a requirement and section directly, and never neither? | 1 (traceability) | NASA §6.2 traceability; the second source | Every row traces to one or the other | A row with neither → design defect (invention) |
| RR-09 | **Origination.** Is there at least one row sourced from a requirement directly — R4 attraction, R7 partner activation, R3 the raise, R10 supplier terms — and does each such row carry a seat and an hours figure? | 1 (count) | Head of Verification, Calmly, September 2026 ("origination is omitted by construction"); R-W28b. **No SE analogue** — the canon's work breakdown starts from the product and has no rule that some work has no product parent | At least one origination row per applicable requirement, each with seat and hours | No origination row → design defect (the floor is understated); an origination row with no hours → design defect |
| RR-10 | For each journey state in the CTM, is there a fail routine for the case where the state is not reached, or the line "no failure mode — reason"? | 1 (count) | IEC 60812; the 4 September rule (two parents); `customer-success-standard.md` CS-11 | Every state has a fail routine or a reasoned absence | A state with neither → design defect |
| RR-11 | Does every built absence and every interlock in the component register have a manage routine naming who may halt it and who may alter it? | 1 (traceability) | 15288 §6.3.5 (change authority per item); "Build the absence, not the permission" | Every absence and interlock has a manage row with both names | Missing → design defect (an interlock nobody may alter is unmaintainable; one anybody may alter is not an interlock) |
| RR-12 | Is there a routine that re-derives the three registers on any ratified change to the architecture, and half-yearly regardless, with an owner? | 1 | 15288 §6.3.5 configuration management; the 4 September rule (4) | The routine exists with an owner | Absent → design defect |

### Group C — Hours and capacity arithmetic

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-13 | Does every row print hours per year = hours per cycle × cycles per year at the C10 volume, and is the multiplication reproducible from the row's own fields? | 1 (arithmetic) | RR-01 fields 8 and 9 *(v0.2)*; Handbook 4th ed. human systems integration (task load designed); `tpm-measurement-standard.md` | Every row prints the product and it reproduces | A missing or wrong product → design defect (arithmetic) |
| RR-14 | Is every frequency's driver a reference to a named quantity in the model — the counted thing the routine scales with — never a sentence? *(v0.2: this check also carries the test the component standard's CR-14 held until it was retired — volume sits on the routine, not the component.)* | 1 | RR-01 field 7 *(v0.2)*; VA-140 | A resolving reference on every row | A sentence → design defect |
| RR-15 | Is every hours figure a technical performance measure — band, evidence basis, convergence event, trigger — and does the trigger say what moves when it fires? | 1 | RR-01 field 10 *(v0.2)*; `tpm-measurement-standard.md`; Roedler and Jones 2005 | All fields present | Trigger absent → unmeasured input without a convergence event, which VA-89 does not allow → design defect |
| RR-16 | Is every figure the at-scale reading, sized at the cost of people, with no founder reading, no no-cash rule and no launch volume in the register? | 1 | VA-23; `derivation-standard.md` state rule | No launch fact in any row | A founder reading inside the register → design defect (state mixing); the launch reading belongs in the pilot-instance record |
| RR-17 | Does the sum of hours per seat across this register equal the figure the position register carries for that seat — at central and at both ends of the band? | 1 (arithmetic) | VA-91 (one capacity figure); `position-register-standard.md` PS-09 | The sums match at all three points | A mismatch → design defect in whichever register is wrong, named |

### Group D — The architectural class, against the design record (rubric B)

| ID | Question to the row | Tier | Exemplar · source · the element graded | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-18 | Does the architectural row name the conventional routine it replaces and the cost line the requirement's move removes — the acquisition spend at R4, the onboarding spend at R5, the financing cost at R6, the intermediary's fee at R7? | 1 | RR-01, the architectural-row addition *(v0.2)*; F2 (Tom, 16 September 2026); `feedback_f2_f3` rule ("name the conventional cost line the challenge attacks and state the cost the design removes"). **No SE analogue** | Both named on every architectural row | Either absent → design defect (RR-19 cannot be graded without them) |
| RR-19 | Does the routine implement the requirement's move as the design record states it, with no element of the conventional routine reappearing — no stage, cost line or intermediary the move removed? **When RR-03 has failed** (no tag on the rows), the reviewer sorts the rows by hand, records the sorting under RR-03 in the review with one reason per row, and scores rubric B against that sorting. The scores are diagnostic only; Tier 1 still fails on RR-03; the hand sorting is a finding and does not enter the register as a tag. *(v0.2 rule. Canon: IEEE 15288.2 — a review whose entry criterion is unmet records the shortfall and proceeds as a diagnostic, never as the pass. Head of R&D, 21 September 2026, object-after 23 September 17:00.)* | 2 (rubric B) | The design record — the requirement's section and its evolution line · the routine against the move | Score ≥ 4 | Score ≤ 3 → **design defect** (the conventional form reimported: a booked acquisition cost is a failed R4) |
| RR-20 | For an architectural row under R8, R9 or R10, does it state which at-scale price or cost assumption in the financial simulation depends on the position holding, and what that assumption fails to if the routine does not run? | 2 (rubric B) | F3 (Tom, 16 September 2026) · the routine against the fin-sim assumption it holds | Score ≥ 4 | Score ≤ 3 → design defect (an at-scale number with no routine holding it) |

### Group E — The conventional class, against the named exemplar (rubric A)

| ID | Question to the row | Tier | Exemplar · source · the element graded | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-21 | Is the routine a mechanism and not an intention — does it run on a tool or interlock that makes the procedure the easiest path, name how the seat adopts it, and name the inspection routine (a manage row) that checks it ran? | 2 (rubric A) | Amazon · Bryar and Carr 2021 · tool, adoption, inspection | Score ≥ 4 | Score < 4 → build item (the missing element, with owner) |
| RR-22 | For a fail routine: is there a playbook the on-call seat can run without its author, an on-call assignment with a response-time target, and a blameless postmortem routine whose findings write back into the procedure? | 2 (rubric A) | Google SRE · Beyer et al. 2016, ch. 11, 14, 15 · playbook, on-call, postmortem | Score ≥ 4 | Score < 4 → build item; a fail routine with no playbook at all → design defect |
| RR-23 | For a make-work routine: is its manual share stated, and where the manual share scales with volume, is the automation that removes it at C10 named as a component-register row? | 2 (rubric A) | Google SRE · Beyer et al. 2016, ch. 5 (toil) · manual share measured; automation named | Score ≥ 4 | Score < 4 → unmeasured input (the manual share) with a convergence event; a linear manual routine with no automation row → design defect on the AOM automation depth |
| RR-24 | For a make-work routine: does the procedure state the work sequence, the time per cycle, and the standard in-process stock (the queue allowed between steps), and does it name the route by which the performer changes the standard? | 2 (rubric A) | Toyota · Ohno 1988; Liker 2004, principle 6 · sequence, cycle time, in-process stock, improvement route | Score ≥ 4 | Score < 4 → build item (owner: the seat); a cycle time that disagrees with the row's hours figure → design defect (arithmetic) |
| RR-25 | For a routine with a pause point where an omission is costly — a print, a close, a kill, a hand-over — is there a checklist of Gawande's form: the pause point named, five to nine killer items, read-do or do-confirm stated, tested in use? | 2 (rubric A) | Gawande 2009 · pause point, killer items, count, form, field test | Score ≥ 4 | Score < 4 → build item; a kill or close with no checklist → design defect |

### Group F — Decision rights and the record

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| RR-26 | Does every manage row state its decision rights in the four columns the position standard uses — what the seat decides alone · what goes to the venture · what goes to the sponsor or principal · what is never decided by any seat — and do they match the seat's row in the position register? | 1 | RR-01 field 11 *(v0.2)*; NASA §6.8 decision analysis (the decision rule is fixed before the decision); `position-register-standard.md` PS-03 | Four columns present and matching | Missing → design defect; a mismatch → design defect in whichever register is wrong, named |
| RR-27 | Does the record each row leaves have a defined shape — the fields, where it is kept, who reads it and at what cadence? | 1 | RR-01 field 13, the record it leaves *(v0.2, later)*; 15288 §6.3.6 information management; `customer-success-standard.md` CS-20 | Shape defined on every row | Missing → build item (owner: the seat) |
| RR-28 | Where a routine watches another — a watchdog, a QA sample, an inspection — is the watching seat separate from the watched seat? | 1 | Handbook 4th ed. system safety (the independent monitor); "No self-certification" | Separation stated | The same seat watches itself → design defect |
| RR-29 | Does the register carry a row count by kind, by class and by state, and do the counts reconcile to the rows? | 1 (arithmetic) | 15288 §6.3.6 | Counts match | A mismatch → design defect (arithmetic) |

**Count: 29 checks** — 22 Tier 1, seven Tier 2 (two under rubric B, five under rubric A). **Kinds under R-W52 (as rewritten 21 September 2026, later; sorted by first part, and re-sorted the same day, night, on the Head of Verification's second application, A3 and A4):** row-field checks, twelve — RR-01, RR-02 (field 3), RR-03 (field 4), RR-04 (field 5; second part row-content — the seat against the position register), RR-05 (field 12), RR-08 (field 2), RR-13 (fields 8 and 9), RR-14 (field 7; second part row-content — the reference against the model), RR-15 (field 10), RR-16 (every at-scale field, for a launch fact; a content judgement on each), RR-18 (the two architectural-row fields RR-01 names), RR-26 (field 11; second part row-content — the four columns against the position register). Row-content checks, nine — RR-06 (the procedure field 12 points to), RR-19 and RR-20 (the architectural row against the design record and the simulation), RR-21 to RR-25 (the row against its exemplar), RR-27 (the record field 13 names). Register checks, eight — RR-07, RR-09, RR-10, RR-11, RR-12 (coverage; RR-09's second part is row-field — fields 5 and 8 on each origination row; RR-11's second part is row-field — the two names in field 11 on each manage row; RR-12's second part is row-field — field 5 on the re-derivation row), RR-17 (the sum against the position register), RR-28 (two seats), RR-29 (counts). Twelve plus nine plus eight is 29. The sentence this line carried when v0.2 was first saved — that every check names an RR-01 field — was false and is withdrawn. *(Head of R&D, 21 September 2026, later; object-after 23 September 17:00.)* *(Re-sort. RR-18 moved from row-content to row-field: RR-01 names both fields it reads, and it reads them for presence. RR-09 and RR-11 stay register: each first part is coverage, and no one row can fail it alone. Their per-row parts are named beside the sort under R-W52's fifth FAIL form. Head of R&D, 21 September 2026, night; object-after 23 September 17:00.)* *(RR-12's second part named beside its sort on the Head of Verification's third application, Addendum 2 B4. Head of R&D, 21 September 2026, night, later; object-after 23 September 17:00.)*

---

## 6 · What a failed check becomes

A failed check is disposed under VA-89 and nothing else. The reviewer classifies; the reviewer does not fix.

| Failure | Class | What the record must carry |
|---|---|---|
| A field, tag, kind, seat, figure or count is absent, or two figures disagree | **Design defect** | The check ID and the row; the register returns to Step 2 |
| An architectural routine scores 3 or below under rubric B | **Design defect** — always | The check ID, the row, the conventional element that reappeared, the requirement that must reopen |
| A conventional routine lacks one of the exemplar's elements | **Build item** (caps at PROVISIONAL) | Owner (the seat), the element, convergence event |
| An hours figure is a band with no measurement | **Unmeasured input** (caps at PROVISIONAL) | Owner, convergence event, trigger, what the trigger moves |
| The failure is a limit of the world, true of every venture in the class | **Structural limit** (VA-101) | The residual, bounded |
| A standing ruling forbids the fix | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect (VA-89's own residual rule).

---

## 7 · Worked application — Forge realisation record, the routine register, 21 September 2026

*(§7 re-read at v0.2 — Head of R&D, 21 September 2026, object-after 23 September 17:00. The v0.1 table graded a 19-row draft with PR- identifiers that the record no longer carries. This table grades the record on disk: 57 routines, RT-01 to RT-57. Kinds: make-work 29 · manage 16 · fail 12. Hours: 0 measured · 1 priced by authority (RT-10) · 6 zero-human · 30 estimated · 16 not stated · 4 inside another routine. Results are the Head of Verification's (`register-review-2026-09-21.md` §2), re-counted by this seat.)*

| Check | Result |
|---|---|
| RR-01 | Fails — at v0.1's eight fields, one row (RT-55). At v0.2's thirteen, every row: no class, no hours per year, no measurement fields, no state |
| RR-02 | Passes — every kind is one of the three |
| RR-03 | Fails on all 57 — no tag. Sorted by hand (the RR-19 rule): 13 architectural — RT-04, RT-05, RT-16, RT-17, RT-19, RT-24, RT-32, RT-33, RT-34, RT-35, RT-38, RT-46, RT-51; 44 conventional |
| RR-04 | Fails on 12 — the principal is named as the accountable party (RT-07, 08, 09, 12, 28, 30, 31, 32, 33, 35, 43, 49); most manage rows name two or more seats |
| RR-05 | Fails — no state field on any row |
| RR-06 | Not run — no written procedure exists yet |
| RR-07 | Fails — §6.10 covers all 84 components in form but places ten routines under the wrong kind; reasons for absent kinds are given per group. Under the v0.2 position the groups pass on form (each lists its members) and fail on content (the kind is wrong) |
| RR-08 | Passes — every row cites a component or a requirement |
| RR-09 | Passes in form — origination rows exist for R4 (RT-17), R3 (RT-32), R7 (RT-34, RT-35), R9 (RT-04), R10 (RT-33). Fails on hours — none is measured |
| RR-10, RR-11, RR-12 | Fail — no fail routine per journey state; no manage row per built absence naming who halts and who alters; no re-derivation routine |
| RR-13 | Fails on all 57 — no row prints hours per year; 16 rows state no hours, four say "inside another routine" |
| RR-14 | Fails on 23 — frequency written as a sentence ("per version", "rare", "per incident", "continuous"); the CR-14 finding of the component standard is read here from v0.2 |
| RR-15 | Fails on all 57 — no band, basis, convergence event or trigger on any hours figure |
| RR-16 | Passes — the launch form is a separate column |
| RR-17 | Cannot run — the position register carries no routine sums |
| RR-18 | Fails on the 13 architectural rows — none names the routine replaced or the cost line removed |
| RR-19 | Diagnostic only (RR-03 failed; hand sorting recorded). On the 13: five at 5 or 4 the move as stated (RT-17, RT-24, RT-05; RT-34, RT-04, RT-33, RT-38, RT-46, RT-19 at 4); RT-51 and RT-16 at 3; RT-32 at 3 and RT-35 at 2 — both the conventional form reimported, design defects |
| RR-20 to RR-25 | Diagnostic: 2, 3, 1, 3, 1, 2 — no playbook, on-call or postmortem on any fail row; cycle time on one row (RT-10); a step list on the kill with no pause point |
| RR-26 | Fails on all 16 manage rows — no four-column decision rights |
| RR-27 | Fails on all 57 — no record shape defined |
| RR-28 | Passes — the watchdog seat is separate from the seat it watches |
| RR-29 | Fails — §10 states 30 · 14 · 13 where the rows give 29 · 12 · 16 |

**Tier-1 verdict on the 21 September record: FAIL.** The register is not read for routing until the record returns from Step 2. RR-17 is the reason the position register cannot yet be derived from this one.

**Three checks that would have caught earlier findings.** RR-09 is the Head of Verification's origination finding, made mechanical. RR-13 and RR-17 are two earlier findings made mechanical: the Head of Method's 3 FTE had no routine behind it (`head-of-method-standard.md` §4), and print operations' 0.19 FTE used the wrong driver (PR-43). An FTE figure with no routine sum is now a failed check, not a discovery. RR-19 is the F2 correction of 16 September made into a check: a booked acquisition cost at an architectural row is a design defect on sight.

---

## 8 · What this standard does not cover

- **Whether a seat's routines are the right routines for that craft.** The seat's craft standard — customer success, finance, portfolio operator, print operations, company secretary, partnerships, head of method — asks that. This standard asks whether the register describes each routine well enough to be run, sized and inspected.
- **Which components exist.** `component-register-standard.md`.
- **How routines are grouped into seats, and whether the seats fit their capacity.** `position-register-standard.md`.
- **The design of an architectural routine.** That is the requirement's own skill. Rubric B grades whether the register's routine matches the design, not whether the design is right.
- **The launch form.** What the founder does by hand on day one is the pilot-instance record's business (VA-23).
- **Scoring the Tier-2 rubrics.** The descriptors in §3 and the exemplars in §4 are drafted for ratification and stay Tom's to change.

---

## 9 · Reviewer checklist — before the register is read for routing

- [ ] The component register passed its own standard first; this register cites its identifiers
- [ ] Every row's thirteen fields were read; RR-01 to RR-06 applied row by row *(thirteen from v0.2)*
- [ ] Every row's tag was read, and for each architectural row the requirement's section was opened before grading
- [ ] The three-kinds count (RR-07) and the origination count (RR-09) were both made and written into the review
- [ ] Rubric B was applied to architectural rows and rubric A to conventional rows — never the other way
- [ ] Each Tier-2 check was scored by two people who did not derive the register, and reported as diagnostic until the rubrics are ratified
- [ ] The per-seat hours sums (RR-17) were computed and compared with the position register
- [ ] Each failed check carries one VA-89 class and the fields that class needs; every rubric-B score of 3 or below is a design defect
- [ ] The conformity guard was applied: an architectural routine was not marked down for departing from the trade
- [ ] No launch fact was read against any at-scale row (RR-16)
- [ ] The review cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## Related

- `.claude/skills/venture-engineer-custom/SKILL.md` — register 2, the second source, the four-things rule
- `component-register-standard.md` · `position-register-standard.md` — the registers either side of this one
- `04-Projects/Family_High_Performance/context/va-design-discipline.md` — VA-23, VA-91, VA-140; the F2 and F3 rule (Tom, 16 September 2026)
- `customer-success-standard.md` CS-11 to CS-16 — the two-parents rule at one seat, which RR-10 generalises
- `se-canon-sources.md` — the search order; add RR-03, RR-09 and RR-18 to §3 as candidate findings
- `regression-set.md` — R-W28 (presence and order); R-W49 (this standard); R-W52 (every check tests a named field)
- `Forge/realisation/realisation-record.md` §6 — the register read in §7

**Version line.** v0.2, 21 September 2026, Head of R&D, object-after 23 September 2026 17:00. Changes: RR-01 thirteen fields as the single source, checks reconciled to it. RR-07 group-reason position. RR-19 rule when RR-03 has failed. RR-14 carries the retired CR-14. §7 re-read against the 57-row record. v0.1, 21 September 2026, Head of R&D, on Tom's instruction; 29 checks; canon anchors as stated; three checks with no SE analogue (RR-03, RR-09, RR-18). Exemplars: Amazon mechanisms, Google SRE, Toyota standardised work, Gawande's checklist — all candidates — and one added with its reason (FAA AC 120-71B). Tier 1 ratifies object-after 23 September 2026 17:00 unless Tom objects; Tier 2 (§3 both rubrics, §4 exemplars, RR-19 to RR-25) is approve-before.
