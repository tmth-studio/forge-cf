# Customer Success Standard — how a venture keeps the customers it has won

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.2 (VA-23 rescoping, 21 September 2026) · **Added:** 16 September 2026, under Tom's `/autonomous` instruction of the same day. Cause: "standard missing" reported at step 6b on Forge R5 and R6.
**Parent:** `derivation-standard.md` · **Siblings:** `launch-sales-standard.md` (up to the yes) · `finance-standard.md` (the money) · `landing-page-standard.md`
**Applies to:** every operating-model component that carries `dri: Head of Customer Success`, or any other name for the seat that owns the customer after the sale.
**Used at:** process flow v6 step 6b (the light pass per challenge; the full pass at Converge) and `realisation-standard.md` step 6b and step 9 (first-article inspection).

**What this is, and is not.** This is a **craft standard for an output the CF produces** — the customer-success function of an architected venture. It is not a change to the CF method. It does not touch Simanis, the BALM disciplines or the criteria system. It gives the reviewing role its questions. The review's output is findings, never rewrites, disposed under VA-89 as design defect, standing constraint or build item.

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date).

---

## 1 · The frame — the customer after the yes

Three facts fix the shape of this standard.

**1. The function is derived, not imported.** IVE puts the customer's routine at the centre of R5. The customer-success function exists to keep the customer inside that routine and to carry what the routine cannot. So the function is read off the R5 use routine and the CTM's journey states, per `derivation-standard.md`. It is not copied from how the trade does it.

**2. Routines have two parents** (Tom, 4 September 2026; `context/ceo-forge-memory.md`, "CF rule 2"; written into the shared CTM spec). Product-derived routines make the product work. Complaints, incidents, a regulator's letter, a statutory request, a customer leaving — no component produces them. Their parent is the journey state the customer was meant to reach and did not. A customer-success plan derived from product alone misses them. Forge R5 did: its escalation rule was absent (finding 3).

**3. A cost driver must have an accountable routine** (F2, 4 September 2026). Every customer-success pound in the financial simulation names the routine that spends it and the component that carries it.

**The conformity guard, applied to this seat.** The reviewer carries the trade's conventions by training: a quarterly business review held as a meeting, a health score per account, a named account manager, a satisfaction survey, a renewal playbook. None of these is a criterion. Reward a departure that is derived from the record. Forge's term report replaces the meeting because the sponsor's routine is an investor's, and that is right. Fail only "cannot be executed by this role as specified".

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon is searched first, then IVE, then the function's own literature, then general practice. The SE canon fixes where each check sits in the life cycle. The function's canon and general practice supply the content of the check.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — transition (§6.4.10), operation (§6.4.12), maintenance (§6.4.13), disposal (§6.4.14); information management (§6.3.6); measurement (§6.3.7); configuration management (§6.3.5) | The life-cycle processes this seat performs: hand the system over, run it, keep it running, take it out of service, keep the records and the numbers |
| SE 2 | INCOSE SE Handbook, 4th ed., ch. 10 — logistics engineering (supportability); usability analysis and human systems integration; training needs analysis; reliability, availability and maintainability; system safety; affordability and life-cycle cost | Support resources are sized from the operating concept; the human's task load is designed; training is a need to be analysed; a fault must be detectable; a monitor is independent of what it monitors; disposal is inside life-cycle cost |
| SE 3 | INCOSE technical measurement (Roedler and Jones 2005), applied through `tpm-measurement-standard.md` | Every hours figure is a technical performance measure: band, evidence, convergence event, trigger |
| SE 4 | IEC 60812 — failure modes and effects analysis | The second parent: for each state the customer should reach, the failure mode and its routine |
| SE 5 | NASA SE Handbook (SP-2016-6105 Rev 2) — technical performance reporting; anomaly reporting | What a periodic report to a decision maker carries; what reaches them between reports |
| SE 6 | Wright (1936), the learning curve, as used in cost estimating (ch. 10 affordability) | The first customers cost more hours than the hundredth; state both readings |
| Function 1 | ISO 10002:2018 — complaints handling in organisations | The guiding principles (visibility, accessibility, responsiveness, objectivity, no charge, confidentiality, accountability) and the process: receipt, tracking, acknowledgement, initial assessment, investigation, response, communicating the decision, closing; analysis and evaluation of complaints |
| Function 2 | ISO 10004 — monitoring and measuring customer satisfaction | The outcome is measured, and the measure is named |
| Function 3 | Mehta, Steinman and Murphy, *Customer Success* (Wiley, 2016) | Churn is the default; time to value is the first objective; health is monitored, not asked; success is driven through hard metrics; renewal is a designed event. Murphy's definition: desired outcome = required outcome + appropriate experience |
| Function 4 | ITIL v3, Service Transition — early-life support; service retirement; knowledge transfer | The first weeks after hand-over are a supported state; a retired service has a routine; what the receiving side needs to run alone |
| Law | UK GDPR art. 15 (access request, one month); Companies Act 2006 s.116 (inspection of the register of members) and s.431 (a member's right to copies of the accounts); s.388 (accounting records kept three years) | The obligations an outside party can trigger that no component produces |
| General practice | The quarterly business review; the no-surprises rule; the escalation matrix; offboarding; gross and net revenue retention | Named so the reviewer knows what they carry — and so departures from it are recognised, not marked down |

Where a check has no SE analogue the anchor column says so. Those checks are candidate contributions for the dissertation and the INCOSE working group, per `se-canon-sources.md` §3.

---

## 3 · The shared rubric for Tier-2 checks

Tier-1 checks are mechanical: presence, count, arithmetic, traceability. Tier-2 checks are scored one to five by an independent scorer, never the producer; two scorers must agree; the pass mark is four.

| Level | Anchor |
|---|---|
| 5 | Stated in the component's definition, note or cost line, with a number, an owner and a driver, and the reviewer can reproduce it from the record |
| 4 | As 5, but one figure is a band with no convergence event |
| 3 | Stated, with one of number, owner or driver missing |
| 2 | Asserted in a sentence, with no field behind it |
| 1 | Absent |

These descriptors are drafted for ratification. The rubric is Tom's to ratify; applying it is permitted, changing it is not (README, autonomy boundaries).

---

## 4 · The checks

Each check is a question the reviewer puts to a component carrying this seat's `dri:`. Each names its tier, its anchor, what passes, and what the failure is under VA-89. "Component" means the AOM component under review; "record" means the venture design record and its model files.

### Group A — Onboarding: the first value

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-01 | Is the customer's first-value event named as a state in the CTM, and does the component say the day or the count at which the customer reaches it? | 1 | Mehta 2016 (time to value); ITIL early-life support; 15288 §6.4.10 | A state identifier and a figure with a band | "Onboarding" with no end state → design defect |
| CS-02 | Is the onboarding routine listed activity by activity, each with a performer, a driver and hours, and does each hours figure carry a TPM band? | 1 | Ch. 10 logistics engineering; `tpm-measurement-standard.md` | Every activity has all four fields | Activity absent → design defect; band absent → unmeasured input |
| CS-03 | Are the onboarding pack's contents derived from the customer's own receiving routine — what their side must do next — with each item citing the CTM step it serves? | 2 | `derivation-standard.md`; ch. 10 human systems integration | Score ≥ 4 on the shared rubric | Score < 4 → design defect (an item with no step is invention) |
| CS-04 | Is there a reading or training item for the customer's people, with their hours priced on the customer's side in the VA-127 actor business case? | 1 | Ch. 10 training needs analysis; VA-127 | The item exists and the VA-127 row carries its hours | Missing → design defect on the VA-127 row |
| CS-05 | Does the hours figure state the first-N-customers reading and the at-scale reading separately, with N and the premium? | 1 | Wright 1936 learning curve, as used in ch. 10 affordability estimating | Both readings printed; N named | One reading only → unmeasured input, with N as the convergence event |

### Group B — The periodic instrument (the term report, or its equivalent)

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-06 | Is the instrument's cadence equal to the customer's decision cadence stated in the CTM, and is the reason written beside it? | 1 | 15288 §6.3.7 measurement (report at the decision maker's cadence); Mehta (customer metrics) | Cadence and reason both present | Cadence with no reason → design defect |
| CS-07 | Does the instrument carry all six contents: (a) the outcome against the promised outcome, in the customer's metric; (b) spend against budget, with money received; (c) exceptions with their attribution class; (d) open jobs; (e) what the customer must decide, and by when; (f) what changed since the last instrument? | 1 | NASA SE Handbook technical performance reporting; 15288 §6.3.7; ISO 10004 | All six present | Any absent → design defect |
| CS-08 | Is the person who signs the instrument named, with hours per instance and a driver? | 1 | Ch. 10 human systems integration | Performer, hours and driver present | Missing → design defect (an unowned activity) |
| CS-09 | Where the instrument replaces a meeting, does the record show that the customer's routine is to read, not to meet, and name the events at which a meeting is held? | 2 | IVE R5 use routine. **No SE analogue** — this is the departure the conformity guard rewards | Score ≥ 4 | Score < 4 → design defect (a departure with no derivation) |
| CS-10 | Does the instrument say what the customer can do with it inside the period, and where the answer is "nothing by design", say so? | 1 | Ch. 10 human systems integration — a display that supports no action is not a task | The sentence is present | Absent → build item (owner: the seat) |

### Group C — Failure and obligation routines: the second parent

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-11 | Does the routines register hold both arcs — for each CTM journey state, the routine when the state is reached and the routine when it is not? | 1 (count) | IEC 60812 failure modes and effects, applied to journey states; the 4 September rule (1); ch. 10 reliability — fault management | Every state has a failure routine or the line "no failure mode — reason" | A state with neither → design defect |
| CS-12 | Are the routines classified run, manage or hold, and is there at least one manage routine (review the numbers, set the level) and one hold routine (check nothing was traded away)? | 1 (count) | The 4 September rule (2); 15288 §6.3.2 assessment and control | All three classes present | Run only → design defect |
| CS-13 | Is there a complaints routine with the ISO 10002 steps — receipt, acknowledgement within a stated time, initial assessment, investigation, response, communicating the decision, closing — each with a performer and hours, and no charge to the complainant? | 1 | ISO 10002 clause 4 (principles) and clause 7 (the process) | All seven steps, each with performer and hours | Any step absent → build item (owner named); routine absent → design defect |
| CS-14 | Are complaints recorded in one place with the fields ISO 10002 names — complainant, product, the failure, the remedy sought, dates, outcome — and does a manage routine review them at a stated cadence? | 1 | ISO 10002 clause 7 (tracking) and clause 8 (analysis and evaluation) | Record fields and review cadence present | Missing → build item |
| CS-15 | Does the register carry the obligations an outside party can trigger, each with its time limit, an owner and hours: an access request (UK GDPR art. 15, one month); a regulator's request; a member's rights where the customer holds shares (CA 2006 s.116 inspection; s.431 copies of the accounts); a counterparty's dispute? | 1 | The statutes named; ISO 10002; 15288 §6.3.6 information management | Each obligation that applies has all three fields | Missing → design defect (a statutory duty with no owner) |
| CS-16 | Does each routine with no product parent name the journey state it hangs from? | 1 (traceability) | The 4 September rule (1). **No SE analogue** beyond the FMEA form | Every such routine cites a state | A routine with neither parent → design defect (invention) |

### Group D — Escalation and the no-surprises rule

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-17 | Is there an escalation rule naming the exception classes that reach the customer inside the period, the time limit for each, and who tells them? | 1 | ISO 10002 responsiveness; NASA anomaly reporting; general practice (no-surprises rule) | Classes, limits and teller present | Absent → build item with owner and convergence event (Forge R5 finding 3) |
| CS-18 | Does the rule cover money — a missed payment, a call notice, a price change — so the customer's operating contact hears it before their finance function's own instrument fires? | 1 | General practice; Forge R6 customer-success finding 2 | The money classes are in the rule | Absent → build item |
| CS-19 | Do escalations land in named hours — whose, how many a period — with a trigger count above which the hours figure moves? | 1 | `tpm-measurement-standard.md`; ch. 10 logistics (support resources sized) | Hours and trigger present | Hours absent → design defect; trigger absent → unmeasured input |

### Group E — The open-job record and watchdog routines

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-20 | Does every operating unit emit its open jobs in one shape carrying at least: job, opened, last moved, owner, the customer it serves? | 1 | 15288 §6.3.6 information management; ITIL incident and problem records | Shape defined with the five fields | Missing → build item (Forge: NCR-C21) |
| CS-21 | Is "stalled" defined as a number of days or moves, per job class? | 1 | Ch. 10 reliability — a fault must be detectable to be managed | A threshold per class | Absent → design defect (the watchdog has nothing to read) |
| CS-22 | Is the watcher separate from the watched — a routine or service above the unit reads the record, and the unit cannot mark its own stalled job as moving? | 1 | Ch. 10 system safety — the independent monitor; independent verification. Tailored: the studio invariant "one company cannot catch the case it itself drops" | Separation stated in the component | Same actor watches itself → design defect |
| CS-23 | Does the watchdog's re-own step land in named hours and priced compute, with the false-alarm rate as a TPM? | 1 | Ch. 10 reliability (false-alarm rate); `tpm-measurement-standard.md` | Hours, compute and rate present | Rate absent → unmeasured input; hours absent → design defect |
| CS-24 | Does the watchdog's output reach the customer through the periodic instrument, and above a threshold through the escalation rule? | 2 | ISO 10002 responsiveness; general practice | Score ≥ 4 | Score < 4 → build item |

### Group F — Wind-down and hand-over

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-25 | For each end state — hold, extend, wind-down, kill, customer default — is there a routine saying what happens to the unit's in-flight customers (completed, transferred or refunded), with a time limit and an owner? | 1 | 15288 §6.4.14 disposal; ITIL service retirement; ch. 10 logistics (disposal support) | Every end state has the routine | An end state with none → design defect |
| CS-26 | Does the wind-down routine list the obligations that outlive the unit — contracts to end or transfer, refunds, data kept and deleted (UK GDPR art. 5(1)(e); CA 2006 s.388 records for three years), complaints still open — each with an owner? | 1 | 15288 §6.4.14; the statutes named | Each obligation has an owner | Missing → design defect |
| CS-27 | On a hand-over, does the pack carry what the receiving side needs to run without the venture, including the tacit part — who to ask, what was tried and failed? | 2 | 15288 §6.4.10 transition; ITIL knowledge transfer; Polanyi (tacit knowledge, cited in the Forge record) | Score ≥ 4 | Score < 4 → build item |
| CS-28 | Is the wind-down cost in the floor at the wind-down share, and the hand-over cost at the hold share? | 1 | Ch. 10 affordability — life-cycle cost includes disposal | Both costs present at their shares | Absent → design defect on the fin-sim line |
| CS-29 | Is the end-state rule — the term, the kill rule — told to the customer before purchase in the CTM and the sales assets, so a wind-down is never a surprise? | 1 | ISO 10002 visibility; `sales-marketing-asset-standard.md` | The rule appears before the yes | Absent → design defect on the asset |

### Group G — Hours per company-year against the AOM

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-30 | Does the sum over every activity under this seat of (driver volume × hours) equal the customer-success figure in the AOM's capacity statement — at central and at both ends of the band? | 1 (arithmetic) | Ch. 10 logistics (support resources sized from the operating concept); VA-89 operational limb | The sum matches at all three points | Mismatch → design defect (arithmetic) |
| CS-31 | Is the figure a TPM — band, evidence basis, convergence event, trigger — and does the trigger say what moves when it fires (cap, count, FTE)? | 1 | `tpm-measurement-standard.md` | All fields present | Trigger absent → unmeasured input without a convergence event, which VA-89 does not allow → design defect |
| CS-32 | Does the at-scale reading of customer-success hours per company-year appear for every routine under this seat, sized at the cost of people, and is the AOM capacity figure read from it — with no launch-instance reading (the founder's) substituted anywhere in the architecture? *Founder form moved to pilot instance (VA-23) — §9, CS-32-P.* | 1 | VA-23; `derivation-standard.md` state rule; TPM | At-scale reading present; the capacity figure uses it | Reading absent → design defect; a founder reading inside the architecture → design defect (VA-23) |
| CS-33 | Does every customer-success cost driver in the financial simulation name its accountable routine and component? | 1 (traceability) | ANSI/EIA-748 — every control account has a responsible manager; the 4 September rule (3), F2 | Every driver traces | An unowned driver → design defect |

### Group H — Measurement and renewal

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-34 | Is the customer's outcome measured by a named metric read from the record — not asked in a survey — with the routine that reads it? | 1 | ISO 10004; Mehta (hard metrics; health monitored, not asked) | Metric and reading routine present | Absent → design defect |
| CS-35 | Is the renewal or extension routine named, or forward-referenced to the requirement that owns it (R8), with its hours marked pending? | 1 | Mehta (renewal as a designed event); IVE R8 | Named or referenced | Neither → design defect |
| CS-36 | Is there a routine that re-runs the operating model on any ratified architecture change, and half-yearly regardless? | 1 | The 4 September rule (4); 15288 §6.3.5 configuration management | The routine exists with an owner | Absent → design defect |

**Count: 36 checks** — 32 Tier 1, four Tier 2. The pilot-instance form in §9 (CS-32-P) is outside this count: it is a launch check, not an architecture check.

---

## 5 · What a failed check becomes

A failed check is disposed under VA-89 and nothing else. The reviewer classifies; the reviewer does not fix.

| Failure | Class | What the record must carry |
|---|---|---|
| A routine, state, owner or figure is absent, or two figures disagree | **Design defect** | The check ID and the component; the challenge that must reopen |
| A figure exists as a band with no measurement yet | **Unmeasured input** (caps at PROVISIONAL) | Owner, convergence event, trigger and what the trigger moves |
| The thing exists in the design and is not yet built | **Build item** (caps at PROVISIONAL) | Owner, convergence event, re-run threshold |
| The failure is a limit of the world, true of every venture in the class | **Structural limit** (VA-101) | The residual, bounded, and the validation that addresses it |
| A standing ruling forbids the fix | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect (VA-89's own residual rule).

---

## 6 · Worked application — Forge R5 and R6, 16 September 2026

The two runs reviewed this seat from general practice. Read against the standard, their findings map as follows.

| Run finding | Check | Result under the standard |
|---|---|---|
| R5 (1): the report replaces the review; the sponsor reads, does not meet | CS-09 | Pass, rewarded — derived from the R5 use routine |
| R5 (2): six hours a company-year is thin for the first sponsor, right at scale | CS-05, CS-31 | Unmeasured input; N = 3; the trigger (12 hours) and what it moves (the stage-1 cap to 2.8) were already stated |
| R5 (3): the plan does not say which exceptions reach the sponsor inside the quarter | CS-17 | Build item — as the run disposed it |
| R5 (4): no health score; the record is the health | CS-34 | Pass — the metric is the record |
| R5 (5): renewal not designed here | CS-35 | Pass — forward-referenced to R8 |
| R6 (2): a missed call is the first bad news the sponsor hears | CS-18 | Build item — as the run disposed it |
| R5 Portfolio Operator: escalations per company-month | CS-19, CS-23 | Unmeasured input with trigger — as disposed |
| NCR-C21: the open-job shape | CS-20 | Build item, open since 2 September |

**Three checks the runs did not put, which the standard now does.** These are findings for the CEO of Forge to dispose at the next challenge, not facts about the model.

1. **CS-11 and CS-16.** The Forge register at C6 carries no failure arc for a printed company's own customers — the people the printed company sells to. A complaint from one of them has no routine and no owner in the record read for this standard.
2. **CS-25 and CS-26.** On a sponsor default the record says the company "runs out the month it holds, winds down". It does not say what happens to that company's in-flight customers and their open jobs.
3. **CS-15.** The sponsor is a member of the printed company from allotment. Its rights to inspect the register and to demand the accounts exist whatever the class rights say, and no routine carries them.

---

## 7 · What this standard does not cover

- **Sales up to the yes.** `launch-sales-standard.md`.
- **Pricing and the payment shape.** `finance-standard.md`; the R6 skill.
- **The design of the use routine itself.** That is the R5 skill's job. This standard reviews whether the design can be executed by this seat, not whether it is the right design.
- **Consumer-facing regulation** beyond the complaints steps — a venture selling to consumers adds its regulator's rules (the Consumer Rights Act 2015; the FCA's rules where they apply) at step 6b as a standing constraint.
- **Support tooling.** At the architecture, tooling is a cost line at the cost of software and people. The launch rule of no tool before 30 customers (`launch-sales-standard.md` §1; the no-cash rule) is a pilot-instance fact. It stays out of the architecture (VA-23; §9).
- **Scoring the Tier-2 rubric.** The descriptors in §3 are drafted for ratification and stay Tom's to change.
- **Jurisdictions other than England and Wales** for the statutory obligations in CS-15 and CS-26.

---

## 8 · Reviewer checklist — before the 6b table is written

- [ ] Every component carrying this seat's `dri:` has been read, with its definition, note and cost line
- [ ] The routines register was read for both arcs, and each of CS-11 to CS-16 put to it
- [ ] The AOM capacity statement and the fin-sim rows were read together for CS-30 to CS-33
- [ ] Each Tier-2 check was scored by two people who did not produce the component
- [ ] Each failed check carries one VA-89 class and the fields that class needs
- [ ] The conformity guard was applied: every departure from the trade's convention was tested for a derivation before any mark-down
- [ ] No launch constraint (the no-cash rule, the founder's hours, no cold outreach) was read against any hours figure or verdict at the architecture (CS-32)
- [ ] The pilot-instance form in §9 was applied only to a pilot-instance record
- [ ] The 6b table cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## 9 · Pilot instance (launch form — outside VA-23 scope)

**Where this applies.** To the pilot-instance record that follows R10. That record is the design that stands the fixed architecture up from zero (PCO v8 §9; Tom's ruling of 17 September 2026, `ws1-feedback-log.md`). Never at step 6b of a challenge, never at Converge, never in a FIT verdict. A challenge record that answers it has the VA-23 design defect.

**Where the record lives.** Forge's v8 pilot-instance record does not yet exist; it is written after R10. The pattern for it is Calmly's launch-form register (`04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-launch-form-register-2026-09-06.html`). See `finance-standard.md` §9 for the same note in full.

| ID | Question to the pilot-instance record | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| CS-32-P | Do the pilot-instance reading (the founder) and the at-scale reading both appear, with the at-scale reading as the parent, and is the pilot-instance reading the one inside the founder-hours cap? | 1 | `derivation-standard.md` state rule (the launch form derived from the at-scale projection); TPM | Both present; the pilot-instance cap uses the founder reading; the at-scale reading is cited as parent | One reading only → design defect (state mixing); a pilot-instance reading with no at-scale parent → design defect |

---

## Related

- `se-canon-sources.md` — the search order and the mapping table; add this standard's "no SE analogue" lines (CS-09, CS-16) to §3 as candidate findings
- `tpm-measurement-standard.md` — how every hours figure is written
- `derivation-standard.md` — why the function is derived; the state rule for CS-32 (the at-scale side; the pilot-instance form is §9)
- `forge-cf-development-backlog.md` — the VA-23 entry; `ws1-feedback-log.md`, 17 September 2026 — Tom's correction and the rule restated
- `realisation-standard.md` — step 6b and step 9, where this standard is applied again at first article
- `context/ceo-forge-memory.md`, 4 September 2026 blocks — the two-parents rule, the three kinds, F2
- `.claude/skills/shared/ctm-diagram-spec.md` — the routines ruling that binds every venture
- Forge R5 and R6 records — `../forge-r5-v7-2026-09-16.md` §17; `../forge-r6-v7-2026-09-16.md` §17

**Version line.** v0.1, 16 September 2026, Head of Product, drafted autonomously; 36 checks; canon anchors as stated; two checks anchored only in IVE (CS-09, CS-16). Ratifies object-after 18 September 2026 unless Tom objects, on the WS1 standards rule; the Tier-2 descriptors stay approve-before.

v0.2, 21 September 2026, Head of Product, under Tom's `/autonomous` instruction of the same day. VA-23 rescoping, 21 Sep 2026: CS-32 rewritten as an at-scale check. Its founder-instance form moved to §9 as CS-32-P, applied only to a pilot-instance record. The §7 support-tooling line rescoped the same way. Two checklist lines added. Check numbers unchanged; the count stays 36. Ratifies object-after 23 September 2026 17:00 unless Tom objects.
