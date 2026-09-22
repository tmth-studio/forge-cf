# Print Operations Standard — how an architecture becomes a running company, and stays one

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.2 (VA-23 rescoping, 21 September 2026) · **Added:** 16 September 2026, under Tom's `/autonomous` instruction of the same day. Cause: "standard missing" reported at step 6b on Forge R1, R2, R3 and R4 — the seat that owns the organising mechanism and had no standard.
**Parent:** `derivation-standard.md` · **Siblings:** `portfolio-operator-standard.md` (the seat that decides between the gates) · `customer-success-standard.md` (the sponsor during the term) · `finance-standard.md` (the money) · `run-record-standard.md` (what a run leaves) · `tpm-measurement-standard.md` (how every figure is written)
**Applies to:** every operating-model component that carries `dri: Head of Print Operations` — on Forge, WP-1 (frame intake), WP-2 (the architecting run and its gate), WP-3 (the print) — and the supervision the seat holds over WP-5, WP-6 and the pod's customer-success function. Any name for the seat that turns a print file into a trading company and keeps it running counts.
**Used at:** process flow v6 step 6b (the light pass per challenge; the full pass at Converge) and `realisation-standard.md` step 6b and step 9 (first-article inspection).

**What this is, and is not.** This is a **craft standard for an output the CF produces** — the production and operation of printed companies. It is not a change to the CF method. It does not touch Simanis, the BALM disciplines or the criteria system. It gives the reviewing role its questions. The review's output is findings, never rewrites, disposed under VA-89 as design defect, standing constraint or build item. Jurisdiction for the statutory checks: England and Wales.

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date).

---

## 1 · The frame — the seat that holds the mechanism

Five facts fix the shape of this standard.

**1. The print is the organising mechanism, and this seat owns it.** R1 §9: remove the print and the design must be carried by people. The check on the design falls back to reputation. The displaced cost falls back to a design fee. The frontier row loses its holder, and the studio's measurement site disappears. Five components make the form: the frame intake, the architecting run, the print, the running company with its record, the director appointment. This seat carries the first three and supervises the fourth. At scale it is two FTE (⚠); at stage 1 it is the founder. Every act the seat performs is therefore an act on the mechanism the whole architecture rests on, so every act must be checkable.

**2. The print is the realisation pipeline applied once per company.** `realisation-standard.md` steps 7 to 9 — Test Product, Realised Product, first-article inspection — run for a product type once. Here they run for every print, because every printed company is a Realised Product built from the same file. In production terms the print file is the product baseline (MIL-HDBK-61A; 15288 §6.3.5): the architecture record, the model files, the agent roster and its routines, stamped with a version. A company printed from an unstamped file cannot be inspected, because there is nothing to inspect it against. First-article inspection is per version of the print file, not per company (AS9102: the first article of each configuration).

**3. Run cost per company-month at required reliability is the top unmeasured input, and it is this seat's to measure.** Inference is 73 per cent of the floor (R3 §14.2). The band is £450 to £4,200 a company-month; the trigger is £4,367 on 148 live, where R3 fails at the gate basis (R3 §17). The telemetry behind the band measures advisory sessions with a person present, not a company being run (11 June note §6). Two levers would pull the figure down: the batch route at half price, and routine turns on a smaller model. Both are unmeasured. The desk classification of 13 June put the combined saving at about 38 per cent, not the 52 per cent the earlier simulations assumed. It found zero smaller-model turns in the whole corpus. "Required reliability" is stated nowhere as a number. The seat's job is to read the figure from a printed company's own meter, at a reliability it has defined, with the levers stated as exercised or not.

**4. Nobody is paged today, and at scale somebody must be.** At 148 live companies and 4.4 operators (the 1,600-hour basis, `portfolio-operator-standard.md` §7 finding 1) the pod absorbs escalations at under four a company-month (R5 §15). That is 592 escalations a month, 135 per operator, about 34 hours of 133 — inside the hours. What the record does not say is what fails, how often, who acts on a failure the watchdog cannot see (a vendor outage, a runaway job, a bank refusal), and what happens between 18:00 and 09:00. Reliability engineering has one rule that applies before any other: a fault must be detectable to be managed (Handbook ch. 10). The site-reliability literature adds the instruments — a service-level objective, an error budget, a bounded on-call load, one commander per incident (Beyer et al. 2016, chapters 3, 4, 11, 14).

**5. The seat holds the levers the design removed from everyone else.** The design took the funding lever from the sponsor (R3), the control lever from the sponsor (R5) and the discretion lever from the operator (`portfolio-operator-standard.md` group A). What remains is held here: the print-file version, the gate's refusal, the halt, the kill command. A seat holding those levers as judgements would re-create the moral-hazard defect the architecture exists to remove (Holmström 1979). So each lever is written as a refusal the run performs or a runbook the seat executes, never as a decision the seat takes. Where the seat finds itself deciding, the rule is missing.

**The conformity guard, applied to this seat.** The reviewer carries the trade's conventions by training. A platform team with a change board. A release manager who signs each deployment. An operations centre with a 24-hour rota. A managed-service agreement with credits for downtime. Reserved capacity bought at a discount to hold the cost line. A golden image of the organisation, patched in place. None of these is a criterion. Reward a departure that is derived from the record. No human team carries the design. A company is a file plus a registration. The company stops when its cash stops. No compute is reserved. Fail only "cannot be executed by this role as specified".

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon is searched first, then IVE, then the function's own literature, then general practice. The SE canon fixes where each check sits in the life cycle. The function's canon and general practice supply the content of the check.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — implementation (§6.4.7); integration (§6.4.8); verification (§6.4.9); transition (§6.4.10); validation (§6.4.11); operation (§6.4.12); maintenance (§6.4.13); disposal (§6.4.14); configuration management (§6.3.5); information management (§6.3.6); measurement (§6.3.7); risk management (§6.3.4) | The processes this seat performs: build the unit from the baseline, integrate its parts, verify it against the file, hand it into operation, run it, keep it current, take it out of service; keep the baseline and the records |
| SE 2 | MIL-HDBK-61A — configuration management; the functional, allocated and product baselines | The print file is the product baseline; a change to it is a new version under control; a live unit names the version it runs |
| SE 3 | MIL-STD-1521B; IEEE 15288.2-2014 — the functional configuration audit (FCA), the physical configuration audit (PCA), the production readiness review (PRR) | First-article inspection has two halves: does each routine perform as designed (functional), and does the built organisation match the file item for item (physical); production readiness is a review with entry and exit criteria |
| SE 4 | AS9102 — first-article inspection | Inspect the first article of each configuration; a change to the configuration requires a new first article |
| SE 5 | INCOSE SE Handbook, 4th ed., ch. 10 — producibility, supportability and logistics, reliability, availability and maintainability, system safety, human systems integration, affordability | The unit is designed to be produced and supported at volume; a fault must be detectable; the human's task load is designed, not assumed; disposal is inside life-cycle cost |
| SE 6 | IEC 60812 — failure modes and effects analysis; MIL-HDBK-338B — reliability design | Enumerate what fails, its effect, its detection and its owner, before the first unit runs |
| SE 7 | NASA SE Handbook (SP-2016-6105 Rev 2) §6.5 product implementation; §6.6 verification and validation; §6.7 technical assessment | The implementation process consumes a baseline and produces a verified product; a technical performance measure has a threshold and a trigger |
| SE 8 | INCOSE technical measurement (Roedler and Jones 2005), applied through `tpm-measurement-standard.md` | Every cost and hours figure is a technical performance measure: band, evidence, convergence event, trigger |
| SE 9 | ANSI/EIA-748 — one responsible manager per control account | Every cost line under this seat names the routine that spends it |
| IVE | R1 §9 and §14 (the five components; the print as the mechanism; the print step as a build item with a 40-hour threshold); R2 (the open gate as a refusal in the run; the close gate and attribution at write time); R3 §6.1 and §17 (the durables check; the term enforced by cash; the kill band; inference at required reliability; the term-budget schedule); R4 (the free first stage; £26 a run; reading the findings; 50 founder-hours a print); R5 (the watchdog; the open-job record; the term report); R6 (the 'sponsor default' class; the bank account); `run-record-standard.md`; `realisation-standard.md` steps 7 to 9; `derivation-standard.md` state rule; `objective-function.md` | What the seat builds, what it refuses, what it measures, what it leaves behind, and at which state each figure is read |
| Function 1 | `../forge-run-cost-telemetry-2026-06-11.md`; `../forge-lever-desk-classification-2026-06-13.md` | The cost shape (cache reads 92.5 per cent of tokens), the right tail (one session at 481 million tokens, about £240), the two levers and why neither is a flat discount, the two unknowns only a trial reads |
| Function 2 | Beyer, Jones, Petoff and Murphy (eds.) 2016, *Site Reliability Engineering*, ch. 3 (error budgets), ch. 4 (service-level objectives), ch. 8 (release engineering), ch. 11 (on-call), ch. 14 (managing incidents), ch. 15 (blameless postmortems); Beyer et al. 2018, *The Site Reliability Workbook*, ch. 2 and 5 (SLO and error-budget policy) | Reliability is a number the customer can read; a release stops while the error budget is spent; on-call load is bounded; one incident commander, one communications lead, one record; every incident writes what changes |
| Function 3 | FEMA, Incident Command System (the source of SRE's incident model) | Roles by function, not by rank; a single command for an event that touches more than one unit |
| Function 4 | `../WS1/forked-toolchain-recommendation-2026-09-10.md`; `../product-spec-forge-tool-2026-09-14.md` risk 2; `manual-release-checklist.md` | A copy of the method drifts about 200 lines in six days; a copy under gate pressure is a cheaper route than designing well; the mitigation is a version stamp checked at each release |
| Function 5 | Nosek, Ebersole, DeHaven and Mellor 2018 (pre-registration); Holmström 1979 | A test whose design is fixed before it runs cannot be changed while it runs without losing attribution; the party that reports must not be the party that decides |
| Law | Companies Act 2006 s.384 (ineligible companies for the small-group exemption); s.388 (records kept three years); ss.1003, 1004, 1006, 1012 (strike-off and its timing); UK GDPR art. 5(1)(e) (storage limitation) | The refusal the gate carries; what the record keeps after the company; the wind-down sequence this seat executes |
| General practice | The platform team's release train and change board; the operations centre's rota and runbooks; the managed-service SLA; reserved-capacity purchasing; print production's first-piece approval; the franchise operations manual | Named so the reviewer knows what they carry — and so departures from it are recognised, not marked down |

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

These descriptors are the same as the sibling standards' and are drafted for ratification. The rubric is Tom's to ratify; applying it is permitted, changing it is not (README, autonomy boundaries).

---

## 4 · The routines the seat runs, and the hours each takes

The standard is written against the routines below. Each is read off the Forge v7 record; the hours are the record's, with the state at which each is read. A venture other than Forge substitutes its own record; the routine list is the same because every printed company passes through the same states.

| # | Routine | Driver | Hours or cost in the record | Class | Where it sits in the AOM |
|---|---|---|---|---|---|
| 1 | **The frame intake** — the run researches the line; the insider corrects the findings | per run | compute, inside the run cost; the insider's three hours on the sponsor's side (⚠) | run | WP-1; `printer_ops` |
| 2 | **The architecting run** — the ten-requirement method on the corrected frame; the gate inside it | per run started; 20 runs a sponsor print at central conversion (C4) | £22 compute at the retry cap (⚠; £26 with the frame research; band 22 to 40) | run | WP-2; CP-2 before the money |
| 3 | **The open-gate review** — the seat reads the frame's count, price and value and the scripts' output before a print | "per run" (R2); 2 hours (⚠); 0.19 FTE "at 148 runs" | 2 hours (⚠) — see §7 finding 1 on the driver | manage | WP-2; `printer_ops` |
| 4 | **Reading the findings by hand** — each completed run's findings, before the conversation | per completed run; 10 a sponsor print | 0.5 hours (⚠); £250 a print in the acquisition line | run | CP-2 (R4 §16.1) |
| 5 | **The print step** — the print file to a running organisation; incorporation; the bank account; the director presented | per printed company | incorporation £50; the account and the appointment via PartP-1; **hours not stated**; build item with a 40-hour stand-up threshold (R1) | run | WP-3 |
| 6 | **First-article inspection** — of the first company printed from each print-file version, and the tranche-1 journey walk | per print-file version | not stated | hold | `realisation-standard.md` step 9 — absent from the AOM |
| 7 | **Supervision** — of the term decision (WP-5), the term report and open-job record (WP-6), the customer-success function, the watchdog | per company-month | not stated; the word "supervised" carries no hours | manage | WP-5, WP-6 doc lines |
| 8 | **Run-cost measurement** — inference per company-month read from the printed company's own meter, at the defined reliability, levers stated | per company-month; convergence the first ten company-months | not stated as a routine; the figure it converges is 73 per cent of the floor | hold | WP-4 cost line; R3 §17 |
| 9 | **Incident response** — a failure the watchdog cannot see: vendor outage, runaway spend, a record that stops writing, a bank or registrar refusal | per incident; rate unmeasured | not stated | run | absent from the record — see §7 |
| 10 | **Kill and wind-down execution** — the halt command to the agents, the record frozen, the sequence handed to finance and the secretariat | per wind-down, at the kill band (⚠ 0.667 to 0.875 of frontier terms) and the sponsor wind-down share | the recommendation is the operator's (PO-31); the seat's own act is not stated | run | WP-5, PP-1, PartP-1 |
| 11 | **Print-file release** — a new version on a ratified change; the version-stamp check against the canonical method; which live companies take it | per ratified change | not stated | manage | absent from the record — see §7 |
| 12 | **The record for WS1** — the run record for each run; the print record for each company | per run; per company | the run record is built (`run-record-standard.md`); the print record is not | hold | absent from the record — see §7 |
| 13 | **One-off, stage 0** — the print step built, the model articles, the decision record, the studio's first article | once | about 400 founder-hours (⚠), priced £192,308 non-cash | — | R3 §14.2 |

**The capacity figures the record states.** Print operations 2 FTE at scale (⚠, inside the £375,000 overhead). The gate review 0.19 FTE at 148 runs. At the pilot instance (a launch figure, read only in §10 under VA-23), the founder's 172.4 architect-hours a year; this seat's part of the 56.5 hours a print is the 2-hour gate review. The print-operations hire is the first hire, at 8 sponsor prints a year (R3 §14.2 stage 2).

**What the seat does alone, what goes elsewhere.** Written here so the checks in groups B, F and G have something to test against.

| The seat does alone, by refusal or runbook | Goes to the venture (CEO Forge) | Goes to the method (WS1, Head of Method) | Never, by any seat |
|---|---|---|---|
| Stamp and release a print-file version | The decision to reprint a live company on a new version outside a safety stop | A change to what the run emits (the schedule, the shape of the record, the refusal rule) | Admit a frame the gate refused |
| Run first-article inspection and raise an NCR on a fail | The kill decision after an in-term stop (PO-25) | A rule change arising from an incident postmortem | Fund a company past its term (PO-06) |
| Execute the halt on a stop-class event and the kill runbook on a ruled kill | A failure attributed to the design — the challenge reopens | — | Change a live company's printed version mid-term, except a safety stop |
| Read the run-cost meter and re-enter the measured figure | Any trigger firing on a measured input — run cost, session time, the refusal rate | — | Buy reserved or committed compute (group J) |
| Declare an incident and take command of it | — | — | Classify an exception from scratch at the term (PO-28) |

---

## 5 · The checks

Each check is a question the reviewer puts to a component carrying this seat's `dri:`, or to the supervision the seat holds. Each names its tier, its anchor, what passes, and what the failure is under VA-89. "Component" means the AOM component under review; "record" means the venture design record and its model files; "print file" means the versioned set the company is printed from.

### Group A — The print file as a baseline, and first-article inspection

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-01 | Is the print file defined as one versioned set — the architecture record, the model files at the ratified state, the agent roster with each agent's routine and skills, the constitution, the schedule the run emits — with a version mark and a fingerprint over the whole set? | 1 | MIL-HDBK-61A (product baseline); 15288 §6.3.5; `run-record-standard.md` (fingerprint, version mark) | The set is listed and the version and fingerprint fields exist | Absent → design defect (a company with no baseline cannot be inspected or attributed) |
| PR-02 | Does every printed company carry the version and fingerprint of the print file it was printed from, in its own record, written at the print and never edited? | 1 | MIL-HDBK-61A (configuration status accounting); 15288 §6.3.6 | The field is in the company's record shape and is write-once | Absent → design defect |
| PR-03 | Is the print step a routine with a performer, a driver and hours — the file read, the agents instantiated, the company incorporated, the account opened, the director presented — and does the stand-up time carry the 40-hour re-run threshold as a TPM? | 1 | 15288 §6.4.7 implementation; §6.4.8 integration; R1 §16 (the build item and its threshold); `tpm-measurement-standard.md` | Performer, driver and hours present; the threshold has a convergence event (the first print, timed) | Hours absent → design defect on WP-3's cost line; the build item carries as R1 disposed it |
| PR-04 | Is first-article inspection defined per print-file version, in two halves: functional — each routine in the file performs as designed on the first company — and physical — the printed organisation matches the file item for item; plus the two questions of `realisation-standard.md` step 9 and the tranche-1 journey walk? | 1 (count) | MIL-STD-1521B (FCA, PCA); AS9102; `realisation-standard.md` step 9 | Both halves, both questions and the walk are stated, with a performer and hours | Absent → design defect (a print with no first article is a Test Product in live use) |
| PR-05 | Does a failed first article raise an NCR and stop further prints from that version until the NCR is disposed — rework, use-as-is with the divergence recorded, or scrap? | 1 | AS9100 nonconformance; `realisation-standard.md` step 9 (the NCR route) | The stop and the three dispositions are stated | Prints continue on a failed version → design defect |
| PR-06 | Is the first article's convergence event the one R1 set — one printed company trading for one sponsor — and is the studio's own stage-0 print counted as the first article of the print step, not of the sponsor form? | 1 | R1 §16; R3 §14.2 stage 0; R4 (the class proof rests on it) | Both stated; the two first articles are distinguished | Conflated → design defect (the sponsor form's first article never runs) |
| PR-07 | Does the print step include a kill drill at first article — the halt command issued, the agents cease new jobs, the record freezes with a final version, the state verified — before the company takes a customer? | 1 | MIL-STD-1521B PRR (production readiness includes the stop); Handbook ch. 10 system safety | The drill is in the first-article procedure with a pass condition | Absent → build item (owner: this seat); the first kill is then the drill, on a live company |

### Group B — The open gate and the close gate as refusals

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-08 | Is the open gate a refusal the run performs — the run stops at challenge two and emits no print file when the excluded population's own key cost cannot carry the print's floor at the margin — and is the gate figure a field read from the record (£3,766 a company-month for a sponsor print at C3; £4,093 for a frontier print), re-read on every floor change? | 1 | NASA §6.8.1.2 (a must-have criterion eliminates, it does not rank); R2 §11.5 (the gate inside WP-2); `derivation-standard.md` (a prohibition is a built absence) | The refusal is a state the run can enter; the figure is a field with a source | Reported, not refused → build item (R2's, as disposed); no field → design defect |
| PR-09 | Does the gate also refuse a frame whose line is an ineligible type — a traded company, an authorised insurer, a bank, an e-money issuer, a MiFID investment firm, a UCITS manager — as a list the run reads, not a note the seat remembers? | 1 | CA 2006 s.384; R5 (the C5 refusal in WP-2) | The list is a field in the run's gate | Absent → design defect (one such print costs every company the group-accounts line) |
| PR-10 | Does the gate-review routine state what the seat does that the refusal does not — confirm the count, price and value the frame carries and the scripts' output — and does it state that the seat holds no admit lever over a refused frame? | 1 | Holmström 1979 (the reviewer cannot be the party that admits); NASA §6.8.2.2 (the selection rule fixed before measurement) | Both stated | An admit lever → design defect (the gate becomes a judgement) |
| PR-11 | Is the gate review's driver one thing — per run started, or per frame that passes the gate, or per subscribed print — and does the FTE figure follow from that driver and the C4 volumes (20 runs a print; 148 prints a year)? | 1 (arithmetic) | EIA-748; VA-91 (one capacity figure, derived consistently) | The driver is named and the FTE recomputes from it | Driver ambiguous or FTE not recomputable → design defect (arithmetic; §7 finding 1) |
| PR-12 | Is the refusal rate a TPM — the share of frames the gate refuses, with R2's trigger (fewer than half of frontier frames refused → the gate figure is re-derived) — read from the run records? | 1 | `tpm-measurement-standard.md`; R2 step 6b | Band, convergence and trigger present, source the run records | Absent → unmeasured input without a convergence event → design defect |
| PR-13 | Is the term-budget schedule the run emits derived from the print file's own cost lines — inference, infrastructure, the director, accountable persons, incorporation — and does a check cell show the subscription sum equals the schedule's sum plus the print fee, with a negative test? | 1 (arithmetic) | NASA-STD-7009A (a model figure is verified by a second route); `finance-standard.md` FN-01, FN-02; R3 §15 (the schedule build item) | The derivation and the check cell exist; the negative test reports a mismatch | Quoted, not derived → design defect; no check cell → build item (owner: Head of Method) |
| PR-14 | Is the close gate enforced by the company's own cash — the last call funds the last month and nothing follows — and does this seat, as supervisor of the term decision, hold no funding lever and no lever to extend the schedule? | 1 | R3 (the term enforced by cash) — **no SE analogue**; the finding is recorded once at `portfolio-operator-standard.md` PO-06 and not counted again here | The mechanism is in the articles; the seat's supervision is stated as read-and-escalate, with no lever | A lever → design defect |

### Group C — Run cost per company-month at required reliability

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-15 | Is "required reliability" defined as a number the printed company's customer can read — a service-level objective per job class (the job completes; the record writes; a customer's request is answered) with a target and a measurement window — before the cost figure is read against it? | 1 | Beyer et al. 2016 ch. 4 (SLOs); Handbook ch. 10 reliability, availability and maintainability | An SLO per job class with target and window | Absent → design defect (the top unmeasured input has no unit of measure; §7 finding 5) |
| PR-16 | Is inference per company-month a TPM — band £450 to £4,200, the evidence basis named as advisory-session telemetry with the transfer to a run company marked as assumed, convergence the first printed company's first ten company-months, trigger £4,367 on 148 live (£4,123 on 92) → R3 fails at the gate basis? | 1 | `tpm-measurement-standard.md`; R3 §17; the 11 June telemetry note §6 | All fields present; the evidence basis carries its own limit | A field absent → design defect; the transfer stated as measured → design defect (the source is stretched past its claim) |
| PR-17 | Is the figure read from the printed company's own meter — the billed token counts per job, attributed to the company and the month, in the shape `run-record-standard.md` gives a run's `usage` events — and never from a session count or a rate card? | 1 | 15288 §6.3.7 measurement; `run-record-standard.md` (`usage` kind; cost fields) | The meter is a component of the print and its shape is stated | Absent → build item (owner: this seat; convergence the first company-month metered) |
| PR-18 | Does the record state, for each lever, whether it is exercised or not on the printed company — the batch route on non-interactive job classes; routine job classes on a smaller model — with the share of tokens each lever touches as a measured field, and is no lever saving entered in the floor before it is measured? | 1 | The 13 June desk classification §6 (about 38 per cent combined, not 52; both shares red-flagged); `tpm-measurement-standard.md` | Each lever has exercised/not, a measured share and a source; the floor uses the no-lever figure until convergence | A lever saving in the floor unmeasured → design defect |
| PR-19 | Does every agent job carry a token budget as a design control, with a breach recorded as an exception in its own class and the job stopped — given one observed session at 481 million tokens, about £240? | 1 | The 11 June telemetry note §6 item 2; Handbook ch. 10 system safety (a bound on the hazardous state); MIL-STD-882E (design out before warn) | The cap is a field per job class and the breach is an exception class | Absent → design defect (a month's term budget can be spent in a day; §7 finding 7) |
| PR-20 | Is the cost of a retry — a job that fails on the smaller model and re-runs on the larger — inside the measured figure, and is the retry rate per job class its own TPM with a trigger at which the routing lever is withdrawn? | 1 | The 13 June desk classification §4 (escalation cost inversion); Beyer et al. 2016 ch. 4 (error rate as an SLI) | Retry cost inside the figure; the rate has a trigger | Retries outside the figure → design defect (the lever saving is overstated) |
| PR-21 | Is the model vendor's outage and price change a named risk with a degraded mode — which job classes pause, which continue, what the customer is told — given that no reserved contract exists to guarantee availability (group J)? | 1 | 15288 §6.3.4 risk management; Beyer et al. 2016 ch. 3 (the dependency's SLO bounds your own) | The degraded mode is stated per job class | Absent → design defect |

### Group D — Reliability at scale: what fails, how often, who is paged

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-22 | Is there a failure-mode table for the printed organisation — at minimum: a job stalls; a job runs away on spend; the record stops writing; the vendor is down; the bank or the registrar refuses; the director is unreachable; the watchdog itself stalls — each with its effect, its detection, its class (design, execution, external) and the seat that acts? Score its completeness on the shared rubric | 2 | IEC 60812 (FMEA); MIL-HDBK-338B; Handbook ch. 10 reliability | Score ≥ 4 | Score < 4 → design defect |
| PR-23 | Does every failure mode in PR-22 have a detector that is not the failing unit — the open-job record and the watchdog for stalls (CS-20 to CS-22); a spend alarm for runaway jobs; a heartbeat for the record; the vendor's published status for outages — and is the false-alarm rate a TPM? | 1 | Handbook ch. 10 reliability (a fault must be detectable) and system safety (the independent monitor); R5 verifier finding 5 | Each mode names its detector; the rate has a field | A mode with no detector → design defect |
| PR-24 | Is on-call defined — who is paged for each failure class, inside which hours, on what rota across the operators — and is the paging load per operator a number inside the operator's hours (at 148 live: under four escalations a company-month, 135 per operator, about 34 hours of 133 at 15 minutes each)? | 1 (arithmetic) | Beyer et al. 2016 ch. 11 (on-call load bounded); Handbook ch. 10 human systems integration | The rota, the classes and the load are stated and the load recomputes | Absent → design defect (§7 finding 6) |
| PR-25 | Does the record say what happens out of hours — a printed company trades while nobody is on shift — either a paged rota with its cost in the floor, or a stated pause of the affected job classes with the customer told in the CTM before purchase? | 1 | Beyer et al. 2016 ch. 4 (the SLO states its window); `customer-success-standard.md` CS-29 (the end-state rule told before purchase) | One of the two, stated, with the cost or the pause | Neither → design defect |
| PR-26 | Is there an error-budget policy — the share of the SLO the company may miss in a window before releases of new print-file versions stop and the failure is worked first — with the budget read from the meter? | 1 | Beyer et al. 2016 ch. 3; Beyer et al. 2018 ch. 2 and 5 | The policy names the budget, the window and the release stop | Absent → build item (owner: this seat; convergence the first window read) |
| PR-27 | For an incident that touches more than one printed company — a vendor outage, a defect in a print-file version — is there an incident-command routine: one commander named by function, one communications role, one record, the halt authority (PO-25) available to the commander, and hours priced at an assumed incident rate with a trigger? | 1 | Beyer et al. 2016 ch. 14; FEMA ICS; Handbook ch. 10 system safety | Roles, record, authority and priced hours present | Absent → design defect |
| PR-28 | Does every incident close with a written postmortem in one shape — timeline, detection, the attribution class, the rule change proposed to WS1 or the print-file change proposed to this seat — and is the postmortem blameless by rule, since the actors are agents and the finding is about the file or the design? | 1 | Beyer et al. 2016 ch. 15; 15288 §6.4.13 maintenance; the WS1 rule-change loop | The shape and the two routes are stated | Absent → design defect (an incident that changes nothing recurs) |

### Group E — The attribution record on every failure

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-29 | Is the attribution rule written and testable — a product built as designed and refused by the customer is a design failure; a product that diverged from the print file is an execution failure; a test the sponsor stopped funding is a sponsor default; an event outside both is external — with the diff between the running organisation and the print file as the evidence of "as designed"? | 1 | R2 §11.5; R6 §19 (the 'sponsor default' class build item, owner this seat with the Head of Method); IEC 60812 (failure classes); Nosek et al. 2018 (pre-registration) | The four classes and the diff test are stated | Absent → build item (R6's, as disposed); no diff test → design defect (attribution has no evidence) |
| PR-30 | Do the agents classify at write time, against the print file's own model files, and does the record show the classifier reads the file version the company runs (PR-02), not the current canonical version? | 1 | R2 WP-5; MIL-HDBK-61A (status accounting against the baseline in force) | Both stated | Classifies against the current version → design defect (a change to canon reclassifies old failures) |
| PR-31 | Is the printed company's record machine-written in one shape — every job, exception with class, spend, call notice, term-report line — with `trace.complete` and `trace.absent` stated as `run-record-standard.md` requires, so an absence is declared and never read as a zero? | 1 | 15288 §6.3.6; `run-record-standard.md` (the absent list) | The shape and the two fields exist | Absent → design defect |
| PR-32 | Does each attribution class name its route — design: an NCR to the owning challenge, the challenge reopens (VA-89); execution: a defect against the print-file version, a new version released (group G); sponsor default: the censored class (PO-30); external: the incident record (PR-28) — with an owner for each? | 1 (count) | 15288 quality management (nonconformance and corrective action); R2; VA-89 | Four routes, four owners | A class with no route → design defect |

### Group F — Kill and wind-down execution as a runbook

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-33 | Is the kill a runbook — each step with a performer (agent or human), the command that starts it, the state it leaves, and the check that it ran: halt new jobs; complete, transfer or refund in-flight customers (CS-25); freeze the record with a final version; the lawful return of capital (FN-40); the record to the venture (R9); the three-month wait (s.1004); the copy to members and creditors within seven days (s.1006); the strike-off (s.1003)? Score the runbook on the shared rubric: would two operators execute it the same way? | 2 | 15288 §6.4.14 disposal; Beyer et al. 2016 (runbooks); CA 2006 ss.1003, 1004, 1006 | Score ≥ 4 | Score < 4 → design defect |
| PR-34 | Is the halt a mechanical act in the print — the agents cease taking new jobs on the command and cannot resume without a new print — rather than an instruction the agents interpret, and was it exercised at first article (PR-07)? | 1 | `derivation-standard.md` (a runtime rule is an interlock that can refuse); MIL-STD-882E (design out before procedure) | The interlock is a component and the drill result is recorded | An instruction → design defect |
| PR-35 | Is the kill's own cost priced at its rate — the kill band on frontier terms (⚠ 0.667 to 0.875), the wind-down share on sponsor prints, the default rate (⚠ 0.02) — with this seat's hours per kill stated beside finance's two, the secretariat's one and the director's one, and the kill run as a scheduled, batchable job? | 1 (arithmetic) | Handbook ch. 10 affordability (disposal inside life-cycle cost); the 13 June desk classification §3 (kill execution is batchable); R6 §15 | The seat's hours are a line and the sum matches the default-handling figure | The seat's hours absent → design defect on the wind-down line |
| PR-36 | Does the runbook say what the company leaves and where — the record kept for the venture (R9); accounting records for three years (s.388); personal data deleted or kept under a stated basis (art. 5(1)(e)); the domain, mailbox and account closed or transferred; the compute account closed — with an owner per item? | 1 (count) | CA 2006 s.388; UK GDPR art. 5(1)(e); `customer-success-standard.md` CS-26; 15288 §6.4.14 | Each item has an owner and a disposition | An item with none → design defect |
| PR-37 | Does the same runbook execute on an in-term stop (PO-25, PO-34) from the halt step, with the attribution written as design, execution or external and never as sponsor default? | 1 | R3 (the class right); R2 (attribution); PO-34 | Stated | Absent → design defect |

### Group G — The re-run on any ratified change, and the live companies

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-38 | Does a ratified architecture change (an NCR disposed) produce a new print-file version by rule — the version bumped, the fingerprint changed, first article required (PR-04) before the version prints — and never an edit to a version in force? | 1 | MIL-HDBK-61A (change control after baseline); VA-52 (forward-only); AS9102 (a changed configuration needs a new first article) | The rule is stated and the version history is a field | Edits in place → design defect |
| PR-39 | Is there a rule for live companies when a new version is released — a company runs the version it was printed from to its term, because a change inside the term contaminates attribution; the only exception is a safety stop, recorded as an incident — and is the sponsor told this before purchase? | 1 | Nosek et al. 2018 (pre-registration) — **partial**: SE configuration management would apply the change under control; the rule that a live unit refuses the change for the sake of attribution is IVE's | The rule and the exception are stated; the CTM carries the disclosure | Absent → design defect (§7 finding 8) |
| PR-40 | Is there a routine that re-runs the operating model and the print file's cost schedule on any ratified change, and half-yearly regardless, and does this seat run the schedule's part or name who does? | 1 | The 4 September rule (4); 15288 §6.3.5; FN-47, PO-45 (the same routine, owned once) | Routine with owner and cadence; the schedule's re-derivation named | Absent → design defect (Forge: FN-47, already routed; not counted twice) |

### Group H — Hours per print against capacity

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-41 | Is every routine this seat performs per print — the gate review, reading the findings per completed run, the print step's stand-up, the first-article inspection — inside the hours-per-print figure, and does the seat's capacity (prints a year at the at-scale staffing) recompute from the sum? *Founder form moved to pilot instance (VA-23) — §10, PR-41-P.* | 1 (arithmetic) | VA-23; VA-91; R4 §15, R6 §15 (the 56.5 decomposition) | Every routine the seat performs is in the sum and the capacity recomputes at the at-scale staffing | A routine outside the sum → design defect (arithmetic; §7 finding 2); a founder cap inside the architecture → design defect (VA-23) |
| PR-42 | Are the one-off hours — the print step built, the articles, the decision record, the studio's first article — carried as a one-off cost line at the cost of people in the year they fall, deducted from this seat's capacity in that year, and not only priced non-cash at the hurdle rate? *Founder form moved to pilot instance (VA-23) — §10, PR-42-P.* | 1 (arithmetic) | Datum R7 verification (4 September 2026); Handbook ch. 10 affordability (the learning cost is in the first units); VA-23 | The one-off line is shown, the deduction from the seat's capacity is shown, and the floor is re-read on it | Priced and not deducted → design defect (the Datum R7 disposition; §7 finding 3); deducted from the founder's year inside the architecture → design defect (VA-23) |
| PR-43 | Is the print-operations FTE at scale derived from hours — (hours per run × runs + hours per print × prints + hours per first article × versions + supervision hours × company-months + incident hours × incidents) ÷ hours a year — at central and both ends of the band, on the 1,600-hour basis the staff business case uses? | 1 (arithmetic) | Handbook ch. 10 logistics engineering (support sized from the operating concept); EIA-748; PO-39 (the 1,600 basis) | The sum matches the FTE at three points | Asserted → design defect (§7 finding 4) |
| PR-44 | Does the at-scale reading — the FTE derived under PR-43 — appear for every routine in §4, is the AOM capacity figure read from it, and is no launch-instance reading (the founder; the agents print) used anywhere in the architecture? *Founder form moved to pilot instance (VA-23) — §10, PR-44-P.* | 1 | VA-23; `derivation-standard.md` state rule; R3 step 6b | At-scale reading present for every routine; the capacity figure uses it | Reading absent → design defect; a founder reading inside the architecture → design defect (VA-23) |
| PR-45 | After each convergence event — the first ten runs timed, the first print timed, the first ten company-months metered — is the figure re-entered as measured with the assumed figure kept beside it, and the floor and the cap re-read? | 1 | `tpm-measurement-standard.md`; 15288 §6.3.7 | The routine exists | Absent → the TPM never closes → design defect |

### Group I — The method copies, and the version-stamp check at each release

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-46 | Does every copy of the method the print uses — the run's method files, each agent's skills in the printed organisation — carry a version stamp and a fingerprint against its canonical file, recorded in the print file (PR-01) and in the run record's `harness.json`? | 1 | `run-record-standard.md` (`harness.json`: fingerprint, length, vault source); MIL-HDBK-61A | Every copy has stamp, fingerprint and source; a copy with no source says `null` | A copy with none → design defect |
| PR-47 | At each print-file release, does a checklist line run the stamp check — every copy compared with its canonical file, the result recorded, a copy behind canon either brought current or the release refused — the way `manual-release-checklist.md` binds the manual? | 1 | `manual-release-checklist.md` (a recurring defect recorded and not mechanised is the defect); the 10 September finding (about 200 lines behind in six days); `product-spec-forge-tool-2026-09-14.md` risk 2 | The line exists and the last release's result is recorded | Absent → build item (owner: this seat; convergence the first release walked) |
| PR-48 | Is there one canonical path the run and the print read from, and does a copy that is not canonical refuse to run rather than warn — given that a forked checker ran silently on 7 September and would have passed a model the canonical checker refuses? | 1 | The 10 September finding ("a warning, not a refusal"); R-CTM8; `derivation-standard.md` (a prohibition is a built absence) | The refusal is stated and tested | A warning → design defect (the cheaper route under gate pressure stays open) |

### Group J — No reserved compute: the durables check

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-49 | Is every compute line in the print file usage-priced — no reserved capacity, no committed-use contract with a term, no dedicated instance — and does the record state that a reserved contract would re-create a durable the form has none of, whatever it saves on the cost trigger? | 1 | R3 §6.1 (the durables check: personnel, consumables, durables — the printed company owns no durable); the R10 watch item (no reserved-capacity contracts). **No SE analogue** — producibility and supportability (Handbook ch. 10) size the asset base; the canon has no rule that refuses an asset because it re-creates the cost driver the design removed | Every line is usage-priced and the constraint is written as a standing constraint on the seat | A reserved line → design defect; the constraint unwritten → build item (the R10 item, owner CEO Forge) |
| PR-50 | Does the printed company hold no durable of any kind — no equipment, no licence or subscription with a term beyond the company's own, the domain, mailbox and account treated as consumables closed or transferred at wind-down (PR-36)? | 1 | R3 §6.1; Handbook ch. 10 supportability | Stated, with the wind-down disposition per item | A durable → design defect |
| PR-51 | Where a lever in PR-18 is exercised through a vendor mechanism — the batch route, a smaller model — is the mechanism confirmed usage-priced with no term, so the lever does not become a durable by another name? | 1 | The 13 June desk classification (the batch route is a published usage price); R3 §6.1 | Confirmed per lever | A lever with a term → design defect |

### Group K — The record every printed company leaves for WS1

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-52 | Does every architecting run leave the five-file run record — `meta.json`, `harness.json`, `inputs.json`, `trace.jsonl`, `score.json` — in the layout `run-record-standard.md` fixes, with `score.json` present and `graded: false` until the grader writes it? | 1 (count) | `run-record-standard.md`; 15288 §6.3.6 | Five files, fixed names, the score file untouched by the run | Absent → build item (owner: this seat with the Head of Method; the hosted service's export or `RUN_RECORDS_DIR`) |
| PR-53 | Does every printed company leave a print record in one shape — the print-file version (PR-02), the first-article result, every exception with its class, the term decision, the outcome the market gave, the measured run cost, the kill or hold — as the held-out case the objective function reads (`objective-function.md`)? | 1 | `objective-function.md`; `run-record-standard.md` (the exhaust of a run is the product of WS1). **No SE analogue** — the canon keeps operational records for the unit's own support; it has no construct for a unit's record as a held-out validation case for the method that designed it | The shape is stated with a fixed name and location | Absent → build item (owner: this seat with the Head of Method; §7 finding 9) |
| PR-54 | Is the insider attached to the case — the operator's corrections to the frame in `inputs.json` as inputs the run did not start with; the data statement governing what WS1 may read; the record never reaching another user — so the held-out case carries the fieldwork the desk cannot supply? | 1 | `run-record-standard.md` (`inputs.json`: every entry the person wrote); R1 §8.4 (the insider supplies the fieldwork); the data statement (CP-2) | The corrections are in the inputs and the data statement is cited | Absent → design defect (the case is desk research with no insider) |
| PR-55 | Is the market's answer written to the record by the trading and read by the grader as validation — never written by the run as its own score — and does the print record state what the trace lacks, as `trace.absent`? | 1 | `run-record-standard.md` (`score.json` is the grader's; `trace.absent` must be present); Holmström 1979 | Both stated | The run scores itself → design defect |

**Count: 55 checks** — 53 Tier 1, two Tier 2. The three pilot-instance forms in §10 (PR-41-P, PR-42-P, PR-44-P) are outside this count: they are launch checks, not architecture checks.

---

## 6 · What a failed check becomes

A failed check is disposed under VA-89 and nothing else. The reviewer classifies; the reviewer does not fix.

| Failure | Class | What the record must carry |
|---|---|---|
| A rule, routine, threshold, owner or figure is absent, or two figures disagree | **Design defect** | The check ID and the component; the challenge that must reopen |
| A figure exists as a band with no measurement yet | **Unmeasured input** (caps at PROVISIONAL) | Owner, convergence event, trigger and what the trigger moves |
| The thing exists in the design and is not yet built | **Build item** (caps at PROVISIONAL) | Owner, convergence event, re-run threshold |
| The failure is a limit of the world, true of every venture in the class | **Structural limit** (VA-101) | The residual, bounded, and the validation that addresses it |
| A standing ruling forbids the fix | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect (VA-89's own residual rule).

---

## 7 · Worked application — Forge R1 to R6, 16 September 2026

Four runs reviewed this seat from general practice. Read against the standard, their findings map as follows. Findings 2 and 3 below were put at the founder form of PR-41 and PR-42. VA-23 moved that form to §10 on 21 September 2026. The findings stand on the v7 record, which the 17 September entry in `ws1-feedback-log.md` annotates as breaching VA-23. At the architecture the same two checks now read the seat's hours at the at-scale staffing.

| Run finding | Check | Result under the standard |
|---|---|---|
| R1: the print of an operating organisation for a third-party line is not built; Calmly's was hand-assembled; 40-hour stand-up threshold | PR-03, PR-06 | Build item with threshold — as disposed; PR-03 adds the hours line WP-3 lacks |
| R2: the gate as a refusal is not built; the run reports challenge two, it does not refuse; trigger fewer than half of frontier frames refused | PR-08, PR-12 | Build item — as disposed; PR-12 makes the refusal rate a TPM read from the run records |
| R3: the term-budget schedule the run must emit, so the sum is derived, not quoted | PR-13 | Build item (Head of Method) — as disposed; PR-13 adds the check cell |
| R3 §17: the kill band, owner this seat; inference at required reliability, owner this seat | PR-35, PR-16 | Unmeasured inputs — as disposed; PR-15 adds the reliability number both need |
| R4: session time a run (trigger four hours); 69 runs a year inside existing compute; reading ten findings a print; the first article as the class proof | PR-17, PR-41, PR-06 | Unmeasured input and build item — as disposed; PR-41 finds the reading hours outside the founder figure |
| R5 verifier finding 5: the watchdog had no function row | PR-23 | Resolved in the pod; PR-23 asks what detects the failures the watchdog cannot |
| R6: the bank account inside the print step, named; the 'sponsor default' class rule not written | PR-03, PR-29 | Build items — as disposed |

**Eleven checks the runs did not put, which the standard now does.** These are findings for the CEO of Forge to dispose at the next challenge, not facts about the model. The arithmetic ones come first.

1. **PR-11 — the gate review's driver is two things at once.** R2 prices the review at two hours "per run", 0.19 FTE "at 148 runs" — one run per print. C4 made the run the free first stage: 20 runs started per sponsor print, 2,960 a year at 148 prints. At two hours per run started that is 5,920 hours: 3.7 FTE on the 1,600 basis, £296,000 a year, £2,000 a print. R4 priced £250 a print for reading ten completed runs' findings at half an hour. If the review is per subscribed print, "per run" is the wrong driver and the 0.19 FTE holds. The record must say which. Nothing flips on the per-print reading; the per-run reading adds about £2,000 a print to the floor. Design defect (definition, then arithmetic).
2. **PR-41 — reading the findings is outside the founder's hours.** R4 gives this seat 0.5 hours per completed run, ten a print; at stage 1 this seat is the founder. Those five hours are not in the 56.5 hours a print (2 gate + 8 term + 12 exceptions + 20 conversations + 8 close + 6 customer success + 0.5 mandate). At 61.5 the year-1 cap falls from 3.05 to 2.80 prints; year-1 fees from £157,400 to about £144,500, 58 per cent of the objective. The first-article hours (PR-04) and the print step's own stand-up hours (PR-03) are not in the figure either and are unstated. Design defect (arithmetic).
3. **PR-42 — stage 0's 400 hours are priced and never deducted.** R3 §14.2 stage 0 is "about 400 founder-hours ⚠", priced £192,308 non-cash. The founder's capacity is 172.4 architect-hours a year. Four hundred hours is 2.3 years of that capacity; if stage 0 and stage 1 share a year, the stage-1 cap in that year is zero, not 3.05. The record charges the hours as money and does not deduct them from the year — the Datum R7 pattern (4 September), in this seat. The fix needs no principal: state how many of the 400 are the founder's and how many the agents', and deduct the founder's from the year they fall. Design defect (arithmetic).
4. **PR-43 — print operations at two FTE is asserted, not derived.** WP-3's cost line is "incorporation £50; director appointment via PartP-1" — no hours. The `printer_ops` function names the frame, the run, the gate review and the print, and states 2 FTE. Only the gate review has hours (finding 1). The print step, first article, supervision and incident response have none, so the FTE cannot be recomputed. Design defect (an unowned line under EIA-748).
5. **PR-15 — "required reliability" has no number.** The top unmeasured input is stated as a cost "at required reliability" in R1, R3 and the AOM. Nowhere does the record say what reliability is required — no job class, no target, no window. The £4,367 trigger cannot be read against a figure whose unit of measure is undefined; a company that misses every job is cheap. Design defect.
6. **PR-22 to PR-25 — no failure-mode table, no rota, no out-of-hours rule.** The record has the watchdog for stalled jobs and nothing for a vendor outage, a runaway job, a record that stops writing, or a refusal by the bank or the registrar. It does not say who is paged, on what rota, or what a printed company does between 18:00 and 09:00 when its customers are awake and its operators are not. The pod's four hours absorb escalations under four a company-month, which is inside the hours (135 per operator a month, about 34 hours), but only for failures the watchdog can see. Design defect; the rota's cost, if any, enters the floor.
7. **PR-19 — no token budget per job.** The 11 June telemetry note recorded one session at 481 million tokens, about £240, and said the R1 model "should carry a per-session token budget as a design control". No run adopted it. A printed company's monthly call is £2,357; one runaway job can spend it in a day, and the sponsor's next call funds a month already gone. Design defect (a control the record's own evidence asked for).
8. **PR-39 — no rule for live companies on a new print-file version.** Attribution (WP-5) depends on the design being fixed while the test runs. The record says nothing about whether a live company takes a ratified change mid-term. If it does, a failure after the change is attributable to neither the printed design nor its execution. The rule — run the printed version to term, safety stops excepted — costs nothing and must be told to the sponsor before purchase. Design defect.
9. **PR-53 — the printed company leaves no record for WS1.** `run-record-standard.md` covers the architecting run. Nothing covers what a printed company leaves: its version, its first-article result, its exceptions with classes, its term decision, the market's answer, its measured cost. That record is the held-out case the objective function is defined on, and no component emits it. Build item; owner this seat with the Head of Method.
10. **PR-46 to PR-48 — the print's method copies carry no stamp.** The drift finding (about 200 lines in six days) and its mitigation (a version stamp checked at release) live in the tool's product spec and the manual's checklist. The print file — which will carry a copy of the method into every printed company — has no stamp, no fingerprint and no release checklist. Design defect on PR-46; build item on PR-47.
11. **PR-49 — the durables constraint is a watch item, not a rule.** R3's durables check found no durable in the form and forward-referenced "no reserved-capacity contracts" to R10. This seat holds the purchasing act, and a committed-use discount is the cheapest way to pass the £4,367 trigger. Until the constraint is written on the seat, the trigger invites the durable back. Build item (the R10 item, owner CEO Forge; this standard supplies the check).

---

## 8 · What this standard does not cover

- **The decision between the gates** — the monthly read, the term decision, the exception classes, the in-term stop's decision. `portfolio-operator-standard.md`. This standard covers the seat's supervision of those routines and the mechanical halt; it does not review the decision.
- **The sponsor during the term** — the term report, the questions, the escalation rule. `customer-success-standard.md`.
- **The money** — the calls, the ring-fence, the return of capital, VAT, the close. `finance-standard.md`. PR-13 and PR-35 read finance's figures; they do not review them.
- **The content of the method the run executes** — what the ten challenges ask, the refusal rule's wording, the shape of the record the run emits. That is the Head of Method's (WS1). This standard checks that the print carries a stamped copy and that the run emits what the record needs, not what the method says.
- **The grader** — `/verify-venture-custom` and the integrity score are untouched; PR-55 checks only that the run does not write its own score.
- **The hosted tool's product design** — the free run's price, the retry cap, the console. `../product-spec-forge-tool-2026-09-14.md`.
- **The reference-set leak check** — `R_and_D/rd-002-instance-leakage-sweep-2026-09-10.md`; the Head of R&D's.
- **The professional director's conduct and the company secretariat's filings** — ss.171 to 177 are the director's; the filings are `finance-standard.md` FN-33 and `company-secretary-standard.md` (groups B to G).
- **Scoring the Tier-2 rubric.** The descriptors in §3 are drafted for ratification and stay Tom's to change.
- **Jurisdictions other than England and Wales** for the statutory checks.

---

## 9 · Reviewer checklist — before the 6b table is written

- [ ] Every component carrying this seat's `dri:` and every supervision line naming the seat has been read, with its definition, note and cost line
- [ ] The print file was looked for as a versioned set with a fingerprint (PR-01), not as a description
- [ ] The gate review's driver was resolved to one thing and the FTE recomputed from it (PR-11)
- [ ] "Required reliability" was looked for as a number with a window (PR-15) before any cost figure was read
- [ ] The failure-mode table was scored by two people who did not produce the component (PR-22)
- [ ] The hours-per-print sum was recomputed with every routine the seat performs at the at-scale staffing (PR-41)
- [ ] The one-off hours were carried as a line in the year they fall and deducted from the seat's capacity (PR-42)
- [ ] No launch constraint (the no-cash rule, the founder's hours, no cold outreach) was read against any figure or verdict at the architecture (PR-44)
- [ ] The pilot-instance forms in §10 were applied only to a pilot-instance record
- [ ] Every compute line was checked for a term or a reservation (PR-49 to PR-51)
- [ ] The run-record layout was checked on disk for the latest run, and the print record looked for (PR-52, PR-53)
- [ ] Each failed check carries one VA-89 class and the fields that class needs
- [ ] The conformity guard was applied: every departure from the trade's convention was tested for a derivation before any mark-down
- [ ] The 6b table cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## 10 · Pilot instance (launch form — outside VA-23 scope)

**Where these apply.** To the pilot-instance record that follows R10. That record is the design that stands the fixed architecture up from zero (PCO v8 §9; Tom's ruling of 17 September 2026, `ws1-feedback-log.md`). Never at step 6b of a challenge, never at Converge, never in a FIT verdict. A challenge record that answers one of these has the VA-23 design defect.

**Where the record lives.** Forge's v8 pilot-instance record does not yet exist; it is written after R10. The pattern for it is Calmly's launch-form register (`04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-launch-form-register-2026-09-06.html`). See `finance-standard.md` §9 for the same note in full. The figures these three checks read on Forge today are the v7 record's: 172.4 architect-hours a year, 56.5 hours a print, 400 one-off hours. They are cited here as the worked instance, not as the rule.

| ID | Question to the pilot-instance record | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| PR-41-P | Is every one of this seat's pilot-instance routines inside the founder-hours figure a print — the gate review (2), reading the findings (0.5 × 10 completed runs), the print step's stand-up, the first-article inspection — and does the cap recompute from the sum (the founder's hours a year ÷ hours a print; 172.4 on Forge v7)? | 1 (arithmetic) | `derivation-standard.md` state rule (the launch form derived from the at-scale projection); VA-91; R4 §15, R6 §15 | Every routine the founder performs at the pilot instance is in the sum and the cap recomputes | A routine outside the sum → design defect (arithmetic) |
| PR-42-P | Are the one-off hours the founder performs — on Forge v7, the print step built, the articles, the decision record, the studio's first article (⚠ 400) — deducted from the founder's year in the year they fall, and not only priced non-cash at the hurdle rate? | 1 (arithmetic) | Datum R7 verification (4 September 2026); Handbook ch. 10 affordability | The deduction is shown and the pilot-instance cap re-read on it | Priced and not deducted → design defect (the Datum R7 disposition) |
| PR-44-P | Do the pilot-instance reading (the founder; the agents print) and the at-scale reading (the FTE under PR-43) both appear for every routine in §4, with the at-scale reading as the parent, is the pilot-instance reading the one inside the founder-hours cap, and is neither used where the other applies? | 1 | `derivation-standard.md` state rule; R3 step 6b | Both present; the pilot-instance cap uses the founder reading; the at-scale reading is cited as parent | One reading, or mixed → design defect; a pilot-instance reading with no at-scale parent → design defect |

---

## Related

- `se-canon-sources.md` — the search order and the mapping table; this standard's "no SE analogue" lines (PR-49, PR-53) and its partial line (PR-39) are added to §3; PR-14 restates PO-06 and is not added again
- `run-record-standard.md` — the five files, the fingerprint and the version mark this standard reuses
- `realisation-standard.md` — steps 7 to 9, applied once per print
- `tpm-measurement-standard.md` — how every hours and cost figure is written
- `derivation-standard.md` — the state rule for PR-44 (the at-scale side; the pilot-instance forms are §10); interlocks and built absences for PR-34 and PR-48
- `forge-cf-development-backlog.md` — the VA-23 entry; `ws1-feedback-log.md`, 17 September 2026 — Tom's correction and the rule restated
- `portfolio-operator-standard.md` — PO-06, PO-25, PO-28, PO-30, PO-31, PO-34, PO-39, PO-45
- `customer-success-standard.md` — CS-20 to CS-22 (the watchdog), CS-25, CS-26, CS-29
- `finance-standard.md` — FN-01, FN-02, FN-40, FN-47
- `manual-release-checklist.md` — the form PR-47 borrows
- `../forge-run-cost-telemetry-2026-06-11.md`; `../forge-lever-desk-classification-2026-06-13.md` — the evidence behind group C
- `forked-toolchain-recommendation-2026-09-10.md`; `../product-spec-forge-tool-2026-09-14.md` — the evidence behind group I
- `Datum/datum-verification-r4-r7-2026-09-04.md` — the one-off hours defect behind PR-42 and PR-42-P
- Forge v7 records — `../forge-r1-v7-2026-09-16.md` §9, §14, §16, §18; `../forge-r2-v7-2026-09-16.md` §11.5, §16, §18; `../forge-r3-v7-2026-09-16.md` §6.1, §8, §13, §14.2, §15, §17; `../forge-r4-v7-2026-09-16.md` §15, §16.1, §17, §19; `../forge-r5-v7-2026-09-16.md` §15, §17, §19; `../forge-r6-v7-2026-09-16.md` §15, §17, §19; `../forge-aom-model-at-C6.yaml`

**Version line.** v0.1, 16 September 2026, Head of Product, drafted autonomously; 55 checks; canon anchors as stated; two checks anchored only in IVE (PR-49, PR-53), one partial (PR-39), and one restating a sibling's IVE-only check (PR-14, PO-06). Ratifies object-after 18 September 2026 unless Tom objects, on the WS1 standards rule; the Tier-2 descriptors stay approve-before.

v0.2, 21 September 2026, Head of Product, under Tom's `/autonomous` instruction of the same day. VA-23 rescoping, 21 Sep 2026: PR-41, PR-42 and PR-44 rewritten as at-scale checks. Their founder-instance forms moved to §10 as PR-41-P, PR-42-P and PR-44-P, applied only to a pilot-instance record. Group H retitled "Hours per print against capacity". A note at the head of §7 on findings 2 and 3. The §9 checklist line on PR-41 and PR-42 split into four. Check numbers unchanged; the count stays 55. Ratifies object-after 23 September 2026 17:00 unless Tom objects.
