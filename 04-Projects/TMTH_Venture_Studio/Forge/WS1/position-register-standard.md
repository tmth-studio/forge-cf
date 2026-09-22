# Position Register Standard — how the third register of `/venture-engineer-custom` is judged

**Owner:** Head of R&D · **Capability:** Forge WS1 — CF development
**Version:** v0.2 · **Added:** 21 September 2026, on Tom's instruction of the same day. Cause: the position register had presence and traceability gates only (R-W28c). The Head of Method's 3 FTE with no routine behind it passed it. So did print operations' 1,920-hour year (portfolio operator standard, §7). **v0.2 (Head of R&D, 21 September 2026, object-after 23 September 17:00).** Cause: the Head of Verification's review of the same day (`Forge/realisation/register-review-2026-09-21.md` §5). PS-01 drops the capacity figure from the per-seat fields; PS-09 holds it once at the head. §7 is re-read against the record on disk, 13 seats.
**Parent:** `derivation-standard.md` · **Siblings:** `component-register-standard.md` (register 1) · `routine-register-standard.md` (register 2, which this register sums) · the craft standards (one per seat)
**Applies to:** the position register a run of `/venture-engineer-custom` derives at Step 2 — every seat, at the at-scale state, with the launch facts in their own column.
**Used at:** `/venture-engineer-custom` Step 2 before routing; `realisation-standard.md` step 6b and step 9; the financial simulation's headcount line reads this register and nothing else.

**What this is, and is not.** This is a **register standard**: the quality checks for the third register. Tier 1 is mechanical — fields, one seat per routine, the capacity arithmetic, the reconciliation to the financial simulation. Tier 2 grades the grouping of routines into seats and the allocation of decisions against named exemplars' published methods. It is not a craft standard for any seat; each seat has its own. Its output is findings, never rewrites, disposed under VA-89.

**The exemplar rule (Tom, 21 September 2026).** Every exemplar's method has a citable, observable source; a named exemplar with no source is opinion and may not appear. The exemplar is for the craft of designing positions, not for the business. Positions are not tagged conventional or architectural: a seat is a container for routines, and the tag lives on the routine (`routine-register-standard.md` RR-03). A seat whose routines are all architectural is still graded here on how it is composed.

**Review date:** 21 December 2026.

---

## 1 · The frame — the register the payroll is derived from

Five facts fix the shape of this standard.

**1. A position is derived from routines, never asserted.** The skill's rule: group routines by competence and decision rights into seats; state each seat's hours at the C10 volume against the one capacity figure (VA-91). The canon's name for the result is the organisational breakdown structure. Its rule: every element of work has exactly one responsible organisational element (ANSI/EIA-748, control accounts; INCOSE SE Handbook 4th ed., project planning). The Head of Method's 3 FTE (`head-of-method-standard.md` §4) failed this: the number came first and the routines were never summed. The derived figure was 0.93 to 1.55 FTE.

**2. One accountable seat per routine, one seat per decision.** Two seats accountable for a routine is none. The same holds for a decision. The register carries a decision-rights table per seat in four columns: what the seat decides alone · what goes to the venture (the CEO or the board) · what goes to the sponsor or principal · what is never decided by any seat. For each decision, exactly one seat holds the "alone" column or a named escalation does (Rogers and Blenko 2006: one D per decision).

**3. One capacity figure (VA-91).** Every seat's hours are read against one figure for the working year — stated once, with its basis — and against nothing else. The portfolio operator standard found two figures in one venture (1,920 and 1,600 hours). A register that carries two is wrong in one of them, and every FTE it prints is wrong with it.

**4. The register is the headcount line.** The sum of seats at C10 is the at-scale headcount, and the financial simulation must reproduce it seat by seat at the cost of people. A headcount in the simulation that the register does not carry is an unsourced cost; a seat in the register the simulation does not cost is an understated floor. Either is a design defect.

**5. The launch facts live in their own column (VA-23).** Holder today · conversion trigger · funding route at zero cash are launch facts, and the skill requires them on every seat. They are read against the pilot instance, never against the at-scale hours, and never as a reason to size the at-scale seat differently. The tension is named here so the reviewer does not resolve it by dropping either. The at-scale columns describe the seat. The launch column describes who fills it on day one and what number converts it.

**The conformity guard, applied to this register.** The reviewer carries an org chart by training: a head of sales, an account manager, an operations lead, a finance function of a familiar size. These are the trade's positions. The register's seats are derived from the routines the design needs, and a seat that has no conventional name is not a defect. Fail the seat that exists because the trade has it; reward the seat that exists because the routines sum to it.

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): SE canon, then IVE, then the function's own literature, then general practice. Section numbers are the anchors as the handbooks are indexed today; page numbers to be added when each is opened against the check.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — project planning (§6.3.1); human resource management (§6.2.4); decision management (§6.3.3); configuration management (§6.3.5) | Roles and responsibilities are defined and staffed as part of planning; skills are identified and developed; a decision has a defined maker and a recorded outcome; the register is a configuration item re-derived on change |
| SE 2 | INCOSE SE Handbook, 4th ed. — project planning (the organisational breakdown structure and the responsibility assignment); specialty engineering: human systems integration (manpower, personnel, training as design domains) | The seat is designed as the system is designed; headcount, skills and training are outputs of the design, not inputs to it |
| SE 3 | ANSI/EIA-748 (earned value management systems) — the control account: the intersection of one work-breakdown element and one responsible organisational element | Every routine has one accountable seat; every cost line names its seat |
| SE 4 | MIL-HDBK-46855A — human engineering: task analysis, workload analysis | Hours are derived from tasks; workload is compared with capacity before the position is fixed |
| SE 5 | INCOSE technical measurement (Roedler and Jones 2005), through `tpm-measurement-standard.md` | Every hours and FTE figure is a technical performance measure with band, evidence, convergence event and trigger |
| SE 6 | IEEE 15288.2 — technical reviews: the review chair is independent of the item under review | The inspecting seat is not the performing seat |
| IVE | VA-91 (one capacity figure); VA-23 (at-scale only; launch facts in their own column); VA-134 (every critical-path act has an owning component, and so an owning seat); the 4 September rules (run, manage, hold); the DRI rule (Tom, 10 September 2026: a role, never a person); the fin-sim headcount line | Which figure the hours are read against, at which state, and what the sum must reconcile to |
| Function 1 | Jaques, *Requisite Organization* (Cason Hall, 1989; 2nd ed. 1996); Jaques, *A General Theory of Bureaucracy* (Heinemann, 1976) — the time-span of discretion; strata one apart between a seat and its manager | Each seat's longest task is stated; a seat and the seat it reports to sit one stratum apart |
| Function 2 | Rogers and Blenko, "Who Has the D? How Clear Decision Roles Enhance Organizational Performance", *Harvard Business Review*, January 2006 — RAPID: recommend, agree, perform, input, decide; exactly one D | Every decision has exactly one deciding seat; the four-column table is the register's form of it |
| Function 3 | Bryar and Carr, *Working Backwards* (2021) — the single-threaded leader: one seat owns one thing and nothing else | Each value-producing component has a seat that owns it and no competing charge |
| Function 4 | Mintzberg, *The Structuring of Organizations* (Prentice-Hall, 1979), ch. 7 — the bases for grouping positions: knowledge and skill, work process, output, client, place | The register states the basis on which routines were grouped into each seat; the skill's "by competence and decision rights" is two of Mintzberg's five |
| General practice | The functional org chart; the head of sales; the account manager; a finance team of conventional size | Named so the reviewer knows what they carry — and rejects a seat that exists because the trade has it |

Where a check has no SE analogue the anchor column says so; those checks are candidate findings for `se-canon-sources.md` §3.

---

## 3 · The shared rubric for Tier-2 checks

Tier-1 checks are mechanical. Tier-2 checks are scored one to five by an independent scorer, never the producer; two scorers must agree; the pass mark is four.

| Level | Anchor |
|---|---|
| 5 | The seat carries every element the exemplar's method names for this check, each as a field in the register, and the reviewer can check each from the record |
| 4 | As 5, but one element is a band or a placeholder with a convergence event named |
| 3 | The elements are present in prose, not as fields; or one element the method names is absent |
| 2 | The seat names the exemplar or the method and carries none of its elements |
| 1 | Absent, or the trade's org chart copied |

**These descriptors are drafted for Tom's ratification and are marked so. The score model is his.** Applying the rubric is permitted; changing it is not. Until ratified, a Tier-2 score is reported as diagnostic beside the Tier-1 result, and no register is refused on a Tier-2 score alone.

---

## 4 · Exemplars — who does this craft best, and the check derived from each

Every exemplar is a **candidate for Tom**. Each has a citable, observable source and is an exemplar for the craft of designing positions, not for any business.

| Exemplar | Source (citable, observable) | The check derived | Status |
|---|---|---|---|
| Jaques — requisite organization | Jaques (1989; 1996): the time-span of discretion measures a seat's level; a seat and its manager sit one stratum apart; a manager must be able to add value to the subordinate's work | PS-17 (time-span stated per seat; reporting seats one stratum apart) | Candidate. Forty years of field measurement, published with the instrument |
| Bain — RAPID | Rogers and Blenko, HBR January 2006: five roles per decision; exactly one D | PS-18 (one deciding seat per decision) | Candidate. The method is stated in full in the article and is checkable against a decision table |
| Amazon — single-threaded owner | Bryar and Carr (2021): a leader who owns one thing and has no competing charge; the org is shaped so that the owner can act without cross-team dependency | PS-19 (one owning seat per value-producing component; no competing charge on that seat) | Candidate. Practitioners' own account; the construct is one sentence and is checkable |
| **Added — Mintzberg, bases for grouping** | Mintzberg (1979), ch. 7: positions are grouped by knowledge and skill, work process, output, client or place; each basis has a stated cost in coordination | PS-20 (the grouping basis is stated per seat, and it is one of the five) | Candidate, **added by this draft**. Why: the skill's rule "group by competence and decision rights" is Mintzberg's construct without the name; naming the basis makes the grouping checkable, and the four candidates above do not grade how routines are grouped into seats at all |

**Considered and not used.** Galbraith's star model (1977; 2002) — the construct overlaps Mintzberg's on grouping and adds nothing checkable at the register level. Hamel and Zanini, *Humanocracy* (2020) — an argument against positions, not a method for designing them.

---

## 5 · The checks

Each check is a question the reviewer puts to the position register or to one of its seats. "Seat" means one row; "routine" means a routine-register row; "simulation" means the financial simulation at the at-scale state.

### Group A — Fields and identity

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PS-01 | Does every seat carry the five at-scale fields — seat · routines held (by routine-register identifier) · hours at C10 volume · FTE, computed against the one capacity figure PS-09 holds at the head · craft standard — with none blank? *(v0.2: the capacity figure is no longer a per-seat field. PS-09 is the ruled position — one figure, stated once at the head, everything derived from it (VA-91; VA-135). A per-seat copy is a second statement of the same input, which is what PS-09 fails. Head of R&D, 21 September 2026, object-after 23 September 17:00.)* *(R-W52 as rewritten: two further fields belong to this list and each has its own check, so PS-01 does not test them for blanks — the seat's cost, the market rate at its source (PS-16; summed by PS-13 and PS-23), and the measurement of the hours and FTE figures — band, evidence basis, convergence event, trigger (PS-14). Head of R&D, 21 September 2026, later; object-after 23 September 17:00.)* | 1 | 15288 §6.3.1; Handbook 4th ed. project planning; VA-91 (one capacity figure, stated once); `/venture-engineer-custom`, register 3 | Five at-scale fields on every seat | A blank field → design defect on the seat; a capacity figure repeated on a seat → read under PS-09 |
| PS-02 | Does every seat carry the launch column — holder today · conversion trigger · funding route at zero cash — held separately from the at-scale fields and never used to size them? | 1 | VA-23; the skill's register 3; `calmly-head-of-launch-ops-custom` (every seat names its holder, trigger and route) | Three launch fields on every seat, in their own column | A launch fact absent → design defect; a launch fact used as an at-scale figure → design defect (state mixing) |
| PS-03 | Does every seat carry a decision-rights table in four columns — decides alone · goes to the venture · goes to the sponsor or principal · never decided by any seat — with at least one entry in each column or the line "none — reason"? *(Re-sort: an entry in the second or third column names its route — the seat or body that decides. PS-07 reads every table for one holder per decision; the route on each entry is a form rule here. Head of R&D, 21 September 2026, night; object-after 23 September 17:00.)* | 1 | NASA SE Handbook §6.8 decision analysis; Rogers and Blenko 2006; `portfolio-operator-standard.md` §4 (the four-column form) | Four columns on every seat; a route on every escalation entry | Table absent → design defect; a column empty with no reason → design defect; an escalation entry with no route → design defect |
| PS-04 | Is every seat a role title, never a person's name — and is no seat titled "Founder", "Tom" or "the CEO for now"? | 1 | Tom, 10 September 2026 (a DRI is a role, never a person); 15288 §6.2.4 | Every seat is a role | A person → design defect; "Founder" → design defect (the launch column is where the founder's name goes, as holder today) |
| PS-05 | Does every seat name its craft standard by file, or carry the line "standard missing" with the owner and date by which one is drafted? | 1 | `realisation-standard.md` step 6b; README standards library | A file or a dated "standard missing" on every seat | Neither → design defect |

### Group B — One accountable seat

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PS-06 | Is every routine in the routine register held by exactly one seat — and does the count of routine identifiers across all seats equal the routine register's row count, with no identifier appearing twice? | 1 (traceability, both ways) | ANSI/EIA-748 (one responsible element per control account); `routine-register-standard.md` RR-04 | The counts match; no duplicate | A routine in no seat → design defect (unowned work); a routine in two → design defect (two accountable is none) |
| PS-07 | For every decision named in any seat's table, is there exactly one seat that holds it in the "alone" column, or exactly one named escalation route — never zero and never two? | 1 (count) | Rogers and Blenko 2006 (one D); NASA §6.8 | One holder per decision | Zero → design defect (an undecidable decision); two → design defect |
| PS-08 | Where a routine inspects, watches or verifies another routine's output, are the performing seat and the inspecting seat different seats? | 1 | IEEE 15288.2 (independent review chair); Handbook 4th ed. system safety; "No self-certification" | Different seats on every such pair | The same seat → design defect |

### Group C — Capacity and the reconciliation

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PS-09 | Is there exactly one capacity figure for the working year, stated once at the head of the register with its basis — contracted hours, less leave, less the stated non-routine allowance — and is every seat's FTE computed against it and nothing else? | 1 (arithmetic) | VA-91; VA-135; `portfolio-operator-standard.md` §7 (the 1,920 finding; the WS1 convention is 1,600 — stated there from v0.2) | One figure, one basis, every FTE reproduces from it | Two figures → design defect; an FTE that does not reproduce → design defect |
| PS-10 | Does each seat's hours at C10 equal the sum of the hours of the routines it holds — at central, and at the top and bottom of the band — and does the sum reproduce from the routine register's own rows? | 1 (arithmetic) | MIL-HDBK-46855A (workload from task analysis); `routine-register-standard.md` RR-17 | The sums match at all three points | A mismatch → design defect in whichever register is wrong, named |
| PS-11 | Is each seat's hours at the top of the band at or below its capacity, or does the register state how the excess is met — a second seat, an automation row in the component register, or a named routine removed? | 1 (arithmetic) | MIL-HDBK-46855A; Handbook 4th ed. human systems integration | Hours ≤ capacity, or the excess is met by a named row | An unmet excess → design defect (a seat that cannot do its work) |
| PS-12 | Are one-off hours in a year — a print, a raise, a first-article inspection — deducted from that year's routine capacity, with the deduction printed? | 1 (arithmetic) | `portfolio-operator-standard.md` PO-27 (Datum R7: −23 per cent in the print year) | The deduction is printed where a one-off falls | Not deducted → design defect (arithmetic) |
| PS-13 | Does the sum of seats at C10 equal the headcount the financial simulation carries, seat by seat, at the cost of people — and where they differ, does the register say which is wrong and why? | 1 (reconciliation) | VA-91; `derivation-standard.md` (the register is the payroll's source); 15288 §6.3.7 | Every seat appears in both with the same FTE and cost | A seat in one and not the other → design defect in the one that is wrong, named; a silent difference → design defect on the register |
| PS-14 | Is every hours and FTE figure a technical performance measure — band, evidence basis, convergence event, trigger — and does the trigger say what moves when it fires? | 1 | `tpm-measurement-standard.md`; Roedler and Jones 2005 | All fields present | Trigger absent → unmeasured input with no convergence event, which VA-89 does not allow → design defect |
| PS-15 | Is every figure the at-scale reading, with no founder hours, no no-cash rule and no launch volume in the at-scale columns? | 1 | VA-23; `derivation-standard.md` state rule | No launch fact in an at-scale column | A founder reading in an at-scale column → design defect (state mixing) |
| PS-16 | Is each seat's cost the market cost of the person the craft standard requires, with the rate's source named, never the holder today's cost? | 1 | VA-23 (at the cost of people); the no-cash rule applies to launch, not to the at-scale seat | A sourced market rate on every seat | The holder's cost, or no source → design defect |

### Group D — Composition and decision rights, against the named exemplars

| ID | Question to the seat | Tier | Exemplar · source · the element graded | Passes when | If it fails |
|---|---|---|---|---|---|
| PS-17 | Does each seat state the time-span of its longest routine — the longest task the seat completes without review — and does each seat sit one stratum above the seats it manages and one below the seat that manages it? | 2 | Jaques · *Requisite Organization* 1989/1996 · time-span stated; strata one apart | Score ≥ 4 | Score < 4 → design defect on the reporting structure (two strata apart is a manager who cannot add value; the same stratum is no manager) |
| PS-18 | For each decision in the register, are the five RAPID roles assignable from the seats — recommend, agree, perform, input, decide — with the D on exactly one seat and the four-column table consistent with it? | 2 | Bain · Rogers and Blenko, HBR January 2006 · five roles; one D | Score ≥ 4 | Score < 4 → design defect (PS-07 is the mechanical floor; this grades whether the other four roles are assigned) |
| PS-19 | Does each value-producing component in the component register have one seat that owns it with no competing charge — and where a seat owns two such components, does the register state why one owner suffices at C10? | 2 | Amazon · Bryar and Carr 2021 · single-threaded owner; no competing charge | Score ≥ 4 | Score < 4 → design defect (a shared owner at C10 is a queue the design did not draw) |
| PS-20 | Does each seat state the basis on which its routines were grouped — knowledge and skill, work process, output, client or place — and is the coordination cost that basis carries named as a manage routine? | 2 | Mintzberg · *The Structuring of Organizations* 1979, ch. 7 · grouping basis; its coordination cost | Score ≥ 4 | Score < 4 → build item (the basis, with owner); a seat whose routines share no basis → design defect (the seat is an org-chart convention) |

### Group E — The launch column and the record

| ID | Question to the register | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PS-21 | Is each seat's conversion trigger a number tied to a named model driver — a volume, a cash figure, a count — never a phrase such as "when needed"? | 1 | VA-140 (a driver is a resolving reference); `calmly-head-of-launch-ops-custom` | A number and a driver on every seat | A phrase → design defect |
| PS-22 | Where the holder today is one person across several seats, does the launch column sum that person's hours across the seats and compare the sum with one person's capacity? | 1 (arithmetic) | VA-91 applied to the launch column; MIL-HDBK-46855A | The sum is printed and compared | Not summed → design defect (the launch plan assumes a person who cannot exist) |
| PS-23 | Does the register carry a seat count, a total FTE and a total cost at C10, and do they reconcile to the rows? | 1 (arithmetic) | 15288 §6.3.6 | Totals match | A mismatch → design defect |
| PS-24 | Does the register live in `realisation-record.md` with its authority line, and is it re-derived on any ratified change to the routine register, with the change noted? | 1 | 15288 §6.3.5; the 4 September rule (4) | In the record; re-derivation noted | Elsewhere, or stale after a change → design defect |

**Count: 24 checks** — 20 Tier 1, four Tier 2. **Kinds under R-W52 (as rewritten 21 September 2026, later; sorted by first part, and re-sorted the same day, night, on the Head of Verification's second application, A3 and A4):** row-field checks, nine — PS-01, PS-02 (the launch column; second part a content judgement — a launch fact used as an at-scale figure), PS-03, PS-04 (seat), PS-05 (craft standard; second part row-content — the file named is in the standards library), PS-14 (measurement), PS-15 (every at-scale field, for a launch fact; a content judgement on each), PS-16 (cost), PS-21 (conversion trigger, in PS-02's column; second part row-content — the driver against the model). Row-content checks, six — PS-08 (the routines-held field against the routine register, for a seat that performs and inspects the same output), PS-10, PS-11 and PS-12 (the hours field against the routine register and the capacity figure), PS-17 (the longest routine held), PS-20 (the grouping basis). Register checks, nine — PS-06 and PS-07 (coverage, and one holder per decision across every table; the route on each escalation entry is a form rule PS-03 holds), PS-09 (the one capacity figure at the head; second part row-field — each seat's FTE against it, the arithmetic PS-01 routes here), PS-13 (the seats against the simulation; second part row-content — each seat against its line in the simulation), PS-18 and PS-19 (every decision, every value-producing component; PS-18's second part is row-content — each seat's four-column table against the D assignment, the seat that holds the D carrying that decision in its alone column), PS-22 (one holder across seats), PS-23 (totals), PS-24 (location). Nine plus six plus nine is 24. The sentence this line carried when v0.2 was first saved — that every check tests a field PS-01, PS-02, PS-03 or PS-09 names — was false and is withdrawn. *(Head of R&D, 21 September 2026, later; object-after 23 September 17:00.)* *(Re-sort. PS-08 moved from register to row-content: one seat that holds both the performing and the inspecting routine fails it alone, and the check reads that seat's routines-held field against the routine register. PS-07, PS-09 and PS-13 stay register: each first part reads the whole. Their per-row parts are named beside the sort under R-W52's fifth FAIL form. Head of R&D, 21 September 2026, night; object-after 23 September 17:00.)* *(PS-18's second part named beside its sort on the Head of Verification's third application, Addendum 2 B4: consistency is read seat by seat, not against the whole — one seat's table that carries a decision in its alone column while the D sits elsewhere fails it alone. Head of R&D, 21 September 2026, night, later; object-after 23 September 17:00.)*

---

## 6 · What a failed check becomes

| Failure | Class | What the record must carry |
|---|---|---|
| A field, table, seat or figure is absent, or two figures disagree, or the register and the simulation differ | **Design defect** | The check ID and the seat; the register returns to Step 2 |
| A routine has no seat or two seats; a decision has no holder or two | **Design defect** | The check ID, the routine or decision, the seats involved |
| A seat lacks a grouping basis or a RAPID role is unassigned | **Build item** (caps at PROVISIONAL) | Owner, the element, convergence event |
| An hours figure is a band with no measurement | **Unmeasured input** (caps at PROVISIONAL) | Owner, convergence event, trigger, what the trigger moves |
| The failure is a limit of the world, true of every venture in the class | **Structural limit** (VA-101) | The residual, bounded |
| A standing ruling forbids the fix | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect.

---

## 7 · Worked application — Forge realisation record, the position register, 21 September 2026

*(§7 re-read at v0.2 — Head of R&D, 21 September 2026, object-after 23 September 17:00. The v0.1 table graded a ten-seat draft with ST- identifiers that the record no longer carries. This table grades the record on disk: 13 seats, capacity 1,600 stated once in §4, £50 an hour. Results are the Head of Verification's (`register-review-2026-09-21.md` §3), re-counted by this seat.)*

| Check | Result |
|---|---|
| PS-01 | Fails on nine of 13 — hours and FTE unpriced or part-unpriced on seven operating seats; the Principal and Studio Director rows carry "—" |
| PS-02 | Passes in form — holder today, conversion trigger and funding route on every operating seat |
| PS-03 | Fails on all 13 — no seat carries a decision-rights table; rights sit as sentences inside routine rows |
| PS-04 | Fails on two — "Principal (Tom)" is a seat titled with a name; "Studio Director; family CFO" is two roles in one seat |
| PS-05 | Fails on two — the accountable person (SM&CR) and HQ engineering say "standard missing" with no owner and no date |
| PS-06 | Fails on ten routines — RT-14, RT-15, RT-17, RT-18, RT-20 sit in no seat; RT-07, RT-08, RT-12, RT-30, RT-32 sit in two. The record's line "every routine sits in exactly one seat" is false |
| PS-07 | Cannot run — no decision tables; on the routine rows 12 decisions name the principal beside a seat |
| PS-08 | Passes — the Head of Verification (RT-56, RT-57) is separate from every performing seat |
| PS-09 | Passes — 1,600 stated once in §4, by citation to PO-39 and PR-43 rather than computed from contracted hours less leave less allowance. The 1,920 in the operator standard's §7 was the venture record's figure reported as a defect, not the library's convention; the operator standard now says so (DA-12) |
| PS-10 | Cannot run on any seat — the routine register carries no measured hours (RD-045: the operating-model generator writes £ per company-month with no hours). The review adds no estimate |
| PS-11 | Passes on the six priced seats — the operator's 3,328 against 1,600 is met by 2.05 people. Cannot run on the seven unpriced seats |
| PS-12 | Fails — no one-off deduction printed; RT-32 (200 hours per round) and RT-01 (the print) fall in a year and are not taken from it |
| PS-13 | Cannot run — the oversight 2.05 FTE reconciles; HQ overhead £375,000 is not itemised and the unpriced seats sit outside the sum (DA-15) |
| PS-14 | Fails on all 13 — no band, basis, convergence event or trigger |
| PS-15 | Fails on one — the Principal row carries founder hours ("2 per version") in the at-scale hours column |
| PS-16 | Fails on all 13 — one rate, £50 an hour, is applied to every seat; no seat names the market rate its craft standard requires |
| PS-17 to PS-20 | Diagnostic: 1, 2, 2, 2 — no time-span or stratum; the D sits on the principal for 12 decisions; 37 component rows carry more than one owner; no seat states its grouping basis |
| PS-21 | Fails on 11 — conversion triggers are event phrases; only the portfolio operator has a number on a driver |
| PS-22 | Fails — the CEO Forge agent is holder today on four seats and the principal on the exceptions; neither load is summed against a capacity |
| PS-23 | Fails — no total cost; the total FTE is "~9,300 upper bound + unpriced"; the 13-seat count is correct |
| PS-24 | Passes — first derivation, in the record, under the authority line |

**Tier-1 verdict on the 21 September record: FAIL — not derivable.** Twelve checks fail outright; three cannot run (PS-07, PS-10, PS-13) and count as failures. The register is not read for routing.

**Three checks that would have caught earlier findings.** PS-09 is the 1,920-against-1,600 finding (`portfolio-operator-standard.md` §7) made mechanical. PS-10 is the Head of Method's 3 FTE: a seat's hours that do not reproduce from its routines is a failed check, not a discovery two standards later. PS-04 is the DRI rule (Tom, 10 September 2026): 71 Calmly components named "Founder" would have failed on sight.

---

## 8 · What this standard does not cover

- **Whether a seat's routines are the right ones for its craft.** The seat's own craft standard.
- **Which routines exist, and their hours.** `routine-register-standard.md`. This standard sums them; it does not derive them.
- **The design of a seat's decision rights.** The venture's architecture (R1 to R10) and the CEO's rulings fix what a seat may decide. This standard checks that the register states it once, in four columns, with one holder per decision.
- **Compensation design, hiring, contracts, employment law.** The Head of Launch Operations' business at launch; the CFO's at scale.
- **The launch plan.** Who fills each seat on day one, and in what order the seats convert, is `calmly-head-of-launch-ops-custom`'s register. This standard checks that the launch column is present, numeric and separate.
- **Scoring the Tier-2 rubric.** §3 and §4 are drafted for ratification and stay Tom's to change.

---

## 9 · Reviewer checklist — before the register is read for routing

- [ ] The routine register passed its own standard first; every seat lists routine identifiers from it
- [ ] The capacity figure was found at the head of the register, stated once, with its basis (PS-09)
- [ ] Every seat's hours were re-summed from the routine register at central and both ends of the band (PS-10)
- [ ] The two-way routine count was made and written into the review (PS-06)
- [ ] Every decision in every four-column table was listed once and its single holder found (PS-07)
- [ ] The simulation's headcount line was opened and reconciled seat by seat (PS-13)
- [ ] Each Tier-2 check was scored by two people who did not derive the register, and reported as diagnostic until the rubric is ratified
- [ ] Each failed check carries one VA-89 class and the fields that class needs
- [ ] The conformity guard was applied: no seat was added because the trade has it; no derived seat was marked down for lacking a conventional name
- [ ] No launch fact was read against an at-scale column (PS-15)
- [ ] The review cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## Related

- `.claude/skills/venture-engineer-custom/SKILL.md` — register 3; the DRI rule; the launch fields
- `component-register-standard.md` · `routine-register-standard.md` — the registers this one sums and cites
- `portfolio-operator-standard.md` §4 (the four-column decision-rights form) and §7 (the capacity finding)
- `head-of-method-standard.md` §4 — the 3 FTE derived down to 0.93–1.55
- `04-Projects/Family_High_Performance/context/va-design-discipline.md` — VA-23, VA-91, VA-134, VA-140
- `se-canon-sources.md` — the search order; no check in this standard is without an SE analogue
- `regression-set.md` — R-W28 (presence and order); R-W50 (this standard); R-W52 (every check tests a named field)
- `Forge/realisation/realisation-record.md` §7 — the register read in §7 of this standard

**Version line.** v0.2, 21 September 2026, Head of R&D, object-after 23 September 2026 17:00. Changes: PS-01 five fields, the capacity figure held once by PS-09; §7 re-read against the 13-seat record; DA-12 answered in the operator standard. v0.1, 21 September 2026, Head of R&D, on Tom's instruction; 24 checks; canon anchors as stated; no check without an SE analogue. Exemplars: Jaques, Bain RAPID, Amazon single-threaded owner — all candidates — and one added with its reason (Mintzberg 1979, ch. 7); two considered and not used (Galbraith; Hamel and Zanini). Tier 1 ratifies object-after 23 September 2026 17:00 unless Tom objects; Tier 2 (§3, §4, PS-17 to PS-20) is approve-before.
