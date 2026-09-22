# Finance Standard — how the money of an architected venture is modelled, held, taxed and accounted for

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.2 (VA-23 rescoping, 21 September 2026) · **Added:** 16 September 2026, under Tom's `/autonomous` instruction of the same day. Cause: "standard missing" reported at step 6b on Forge R5 and R6.
**Parent:** `derivation-standard.md` · **Siblings:** `customer-success-standard.md` · `launch-sales-standard.md` · `tpm-measurement-standard.md` (how every figure is written)
**Applies to:** every operating-model component that carries `dri: Head of Finance and Compliance`, `dri: CFO` or `dri: Head of Finance`. Any name for the seat that owns the money counts.
**Used at:** process flow v6 step 6b (the light pass per challenge; the full pass at Converge) and `realisation-standard.md` step 6b and step 9 (first-article inspection).

**What this is, and is not.** This is a **craft standard for an output the CF produces** — the finance function of an architected venture and of every company it prints. It is not a change to the CF method. It does not touch Simanis, the BALM disciplines or the criteria system. It gives the reviewing role its questions. The review's output is findings, never rewrites, disposed under VA-89 as design defect, standing constraint or build item. Jurisdiction: England and Wales; UK tax.

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set, the canon mapping and the tax thresholds, bumps the date).

---

## 1 · The frame — the money after the design

Three facts fix the shape of this standard.

**1. The financial simulation is the design's cost model.** In systems engineering terms it is the affordability artefact (INCOSE SE Handbook 4th ed. ch. 10). The finance seat does not review whether the design is right. It reviews whether the money can be held, moved, taxed and reported as the model says, in the hours the AOM gives.

**2. Every pound between pay-in and pay-out has a holder and a cost of carry.** "No working capital" is shown by attribution, one flow at a time. It is never asserted. Forge R3 states the venture holds no carry; R6 shows it, flow by flow, with the sponsor's timing cost priced at eight per cent. That is the form every venture must reach.

**3. Every company the venture prints or runs is a legal person with duties on a calendar.** Records, accounts, the confirmation statement, corporation tax, VAT, PAYE. Each duty is a routine with hours. A duty with no owner is the F2 defect (Tom, 4 September 2026): a cost driver with no accountable routine.

**Launch constraints stay out of the architecture (VA-23; Tom, 17 September 2026).** No cash for Forge at any size (Tom, 2 September 2026) is a constraint on the venture as it exists today, not a property of the design. At the architecture the seat is sized at the cost of people and every balance is held at the cost of capital. The founder-and-checking-script form of the seat is a pilot-instance fact. So is "no bookkeeper, no software subscription, no adviser before revenue". The checks that read them sit in §9 and apply only to a pilot-instance record. At the architecture, a check that could only be met by spending is a cost line. At the pilot instance it is a standing constraint, not a design defect.

**The conformity guard, applied to this seat.** The reviewer carries the trade's conventions by training. Invoice and chase. The payee controls collection. A bookkeeper closes the month and an auditor signs the year. A cash reserve. Equity or debt funds the build. None of these is a criterion. Reward a departure that is derived from the record. Forge's customer funds the company to its term; a forfeiture replaces a claim in debt; the report is written from the record, not from management accounts. Fail only "cannot be executed as specified". Two things can never be executed as specified: a distribution with no distributable profits, and a strike-off with cash still in the company.

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon first, then IVE, then the function's own canon, then general practice. The SE canon fixes where each check sits; the function's canon supplies the content.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — project assessment and control (§6.3.2); risk management (§6.3.4); configuration management (§6.3.5); information management (§6.3.6); measurement (§6.3.7); verification (§6.4.9); disposal (§6.4.14); the agreement processes (§6.1) | The month is assessed against plan; a stopped payment is a risk with a response; the model file is the baseline; the records are kept; the model is verified; the end state has a process; the subscription agreement is an agreement process |
| SE 2 | INCOSE SE Handbook, 4th ed., ch. 10 — affordability, cost-effectiveness and life-cycle cost analysis; system safety | Cost categories over the life cycle, disposal included; the design order of precedence — a device before a procedure |
| SE 3 | NASA-STD-7009A — models and simulations | A model is verified (does it compute what it claims), validated and carries its uncertainty; a check that cannot fail is not a check |
| SE 4 | NASA SE Handbook (SP-2016-6105 Rev 2) — margins; technical data management | Both readings at every gate; the worst corner named |
| SE 5 | INCOSE technical measurement (Roedler and Jones 2005), through `tpm-measurement-standard.md` | Every figure is a band with a convergence event and a trigger |
| SE 6 | ANSI/EIA-748 — earned value management | Every control account has one responsible manager; variance is read monthly |
| SE 7 | MIL-STD-882E — the design order of precedence | Design it out; then a device; then a warning; then a procedure. A ring-fence is a device, a policy line is a procedure |
| Finance 1 | Richards and Laughlin (1980), the cash conversion cycle | Days between pay-out and pay-in, and who holds the balance |
| Law 1 | Companies Act 2006 — ss.386 to 388 (accounting records); s.394, s.414, ss.441 to 442 (accounts prepared, approved, filed within nine months); ss.382 to 384 (small companies, small groups, excluded companies); s.399 (group accounts); s.477 and s.479A (audit exemption); s.853A (confirmation statement); s.555 (return of allotment within one month); s.113 (register of members); s.790M (PSC register); s.586 (partly paid shares — public companies only); ss.641 to 644 (reduction of capital by solvency statement); s.658 and s.659(2)(c) (a company may not acquire its own shares, except by forfeiture under the articles); s.662 (cancellation of forfeited shares within three years — **public companies only**, s.662(1); a private company cancels by reduction under ss.641 to 644); s.830 (distributions only from profits available); s.1003 (voluntary strike-off); s.1012 (property of a dissolved company passes to the Crown); s.155 (a natural-person director); ss.1159 and 1162 (subsidiary) | The duties, the routes and the prohibitions every printed company lives under |
| Law 2 | Companies (Model Articles) Regulations 2008 — private model article 21 (shares fully paid); public model articles 52 to 62 (calls, liens, forfeiture) | The source text for a call and forfeiture routine |
| FRC 1 | FRS 102 section 1A (small entities) and section 3 (going concern, paragraphs 3.8 to 3.9); FRS 105 (micro-entities); FRC, *Guidance on the Going Concern Basis of Accounting* (2016) | The framework a printed company reports under; the basis of preparation for a company designed to end |
| ICAEW | TECH 02/17BL, *Guidance on realised and distributable profits* | A return of cash to a member is a distribution unless it is a lawful return of capital |
| HMRC 1 | VATA 1994 — s.4 (scope), s.43 and s.43A (VAT groups; bodies corporate under common control; joint and several liability), Schedule 1 (registration threshold, £90,000 from 1 April 2024), Schedules 8 and 9 (zero-rated, exempt); VAT Notice 700/2 (group registration); VAT Notice 706 (partial exemption); Making Tax Digital for VAT (all registered businesses since April 2022); *Kretztechnik* (C-465/03) — an issue of shares is not a supply | The VAT position of every flow, and the group route |
| HMRC 2 | ITEPA 2003 s.5 (office holders taxed as employees); Income Tax (PAYE) Regulations 2003 (real-time information: a full payment submission on or before each payment); SSCBA 1992 (employer NIC — 15 per cent above a £5,000 secondary threshold, 2025 to 2026); NICA 2014 s.2(4A) (no Employment Allowance where the only paid person is a director); ITEPA 2003 Part 2 Chapters 8 and 10 (off-payroll working; a small client leaves the decision with the intermediary); Pensions Act 2008 (auto-enrolment; a director with no contract is not a worker) | Every natural person paid, classified and costed |
| HMRC 3 | FA 2004 s.55 (notify chargeability within three months of trading); CTA 2009 and 2010 (accounting periods; the return within twelve months; payment nine months and one day; the small profits rate, 19 per cent) | The corporation tax calendar |
| Companies House | Fee schedule from 1 May 2024 — incorporation £50, confirmation statement £34, strike-off £33, online; late-filing penalties for a private company £150, £375, £750, £1,500 by lateness; Economic Crime and Corporate Transparency Act 2023 — identity verification; software-only accounts filing and profit-and-loss filing for small companies from 1 April 2027 | The fixed costs, and the cost of the negative case |
| General practice | The month-end close (bank to ledger, accruals, variance to budget); separate accounts for share capital, client money and trading receipts; a statutory calendar with a named reader | Named so the reviewer knows what they carry |

Where a check has no SE analogue the anchor column says so.

---

## 3 · The shared rubric for Tier-2 checks

Tier-1 checks are mechanical: presence, count, arithmetic, traceability. Tier-2 checks are scored one to five by an independent scorer, never the producer; two scorers must agree; the pass mark is four.

| Level | Anchor |
|---|---|
| 5 | Stated in the component's definition, note or cost line, with a number, an owner and the section of law or the source relied on, and the reviewer can reproduce it from the record |
| 4 | As 5, but one figure is a band with no convergence event |
| 3 | Stated, with one of number, owner or source missing |
| 2 | Asserted in a sentence, with no field behind it |
| 1 | Absent |

Drafted for ratification; the rubric is Tom's to change.

---

## 4 · The checks

Each check is a question the reviewer puts to a component carrying this seat's `dri:`. "Component" means the AOM component under review; "record" means the venture design record, the model files and the financial simulation; "floor" means the cost per unit-year the simulation prints.

### Group A — The cash model: check cells and negative tests

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-01 | Does every floor and every gate figure have a second-route recomputation — a check cell — and does the record show it reports MATCH? | 1 | NASA-STD-7009A verification; 15288 §6.4.9 | Every printed figure has a check cell at MATCH | Absent → design defect; MISMATCH → design defect |
| FN-02 | Does every check cell have a negative test — one input fed ten per cent wrong — and does the record show the test reported a mismatch? | 1 | NASA-STD-7009A (a check that cannot fail is not a check); the fin-sim skill's own convention | Every check cell has a negative test that fired | "Negative test did not fire" → design defect |
| FN-03 | Is every input editable, sourced and written as a TPM — band, evidence basis, convergence event, trigger? | 1 | `tpm-measurement-standard.md` | Every input has the fields | A bare point → design defect; band with no convergence → unmeasured input |
| FN-04 | Is every line classified — per-unit cost, running cost, one-off cost, capital held — with the reason for the class beside it? | 1 | Ch. 10 life-cycle cost categories | Every line classified with a reason | Unclassified → design defect |
| FN-05 | Are both readings printed at every gate — the count of record and the adverse count — and is the worst corner named with its verdict? | 1 | NASA SE Handbook margins; VA-89 financial limb | Both readings and the worst corner present | Missing → design defect |
| FN-06 | Do the checking script's own outputs — the model file and its corner files — match the figures printed in the record, to the pound? | 1 | 15288 §6.3.5 configuration management | Every printed figure traces to a file | A figure with no file → design defect |
| FN-07 | Is the at-scale state modelled with cash and hours as separate lines — cash at the cost of capital, hours at the cost of people — and is the record free of any launch constraint (the no-cash rule, the founder's hours, no cold outreach) inside a figure, a gate or a verdict? *Founder form moved to pilot instance (VA-23) — §9, FN-07-P.* | 1 | VA-23; `derivation-standard.md` state rule; PCO v8 §9 | Separate lines; no launch constraint inside a figure or verdict | State mixing → design defect; a launch constraint read against a figure or verdict → design defect (VA-23) |

### Group B — Working capital and carry attribution

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-08 | For every money flow in the AOM, is the day the money leaves the payer and the day the payee can spend it stated, and the holder of the balance in between named? | 1 | Richards and Laughlin 1980 | Every flow has both days and a holder | A flow with no holder → design defect |
| FN-09 | Is the cost of carry priced for whoever bears it, at a named rate, even when that party sits outside the floor — the customer's own timing cost, for example? | 1 | Richards and Laughlin; VA-127 actor business case | Rate and cost present for each holder | Absent → unmeasured input on the VA-127 row |
| FN-10 | Is the venture's own carry a number — peak drawdown across the period — and not a sentence? "The venture holds no carry" passes only with the arithmetic beside it. | 1 | The R3 required-capital definition; Richards and Laughlin | A figure with its derivation | Sentence only → design defect |
| FN-11 | For any balance one party holds for another, is the money classified — share capital, client money, a trading receipt, a loan — and the account it sits in named? | 1 | CA 2006 s.386 (records of money received and spent); the FCA client-money boundary (rules apply to firms holding others' money) | Class and account present | Unclassified → design defect |
| FN-12 | Is every ring-fence enforced by a device — the account structure and the articles — and not by a policy line? | 1 | MIL-STD-882E design order of precedence; `derivation-standard.md` runtime gates | The device is named | Policy only → design defect |
| FN-13 | Does the model show what happens when a payment stops: who holds cash, for how long, and which routine fires on which day? | 2 | 15288 §6.3.4 risk management; Forge R6 finding 3 | Score ≥ 4 | Score < 4 → design defect |

### Group C — Calls and forfeiture on partly paid shares

Apply only where the design allots shares partly paid. Otherwise write "not applicable" against the group.

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-14 | Do the articles displace private model article 21 and carry call, lien and forfeiture provisions, drafted from public model articles 52 to 62, as a build item with an owner? | 1 | Model Articles 2008; CA 2006 s.586 (the bar on partly paid shares binds public companies only) | Build item present with owner | Absent → design defect |
| FN-15 | Does the call routine state the notice's contents — the sum, the due date, the account, the consequence — who issues it, from which record, and the hours or compute per call? | 1 | Public model article 54 (a call notice); 15288 §6.3.6 | All fields present | Missing → build item |
| FN-16 | Is the amount unpaid recorded at allotment (the return of allotment, s.555, within one month) and in each statement of capital on the confirmation statement, with the filing fee and hours? | 1 | CA 2006 s.555, s.853A | Both filings and their cost present | Absent → design defect |
| FN-17 | Does the forfeiture routine name the exemption it relies on (s.659(2)(c)), what becomes of the forfeited shares — s.662 applies to public companies only (s.662(1), read at source 16 September 2026), so in a private company the shares are cancelled by the reduction the wind-down already runs (ss.641 to 644, FN-40) or held or re-allotted under the article — the register entry (s.113) and the director's recording hour? | 1 | CA 2006 s.658, s.659(2)(c), s.662(1), ss.641 to 644; `company-secretary-standard.md` SEC-27 | All four present; a lawful disposal named | Disposal absent, or s.662 relied on → design defect (a statutory duty with no owner, or the wrong section) |
| FN-18 | Is the default rate a TPM with a trigger, read separately for each payer instrument — a standing order, which the payer can cancel unseen; a Direct Debit, which the payee collects under the scheme's indemnity? | 1 | `tpm-measurement-standard.md`; Bacs Direct Debit scheme rules; Forge R6 finding 2 | Rate per instrument, with trigger | One rate for both → unmeasured input |
| FN-19 | Does the routine say what a cure does and does not do to the schedule and to the class? | 1 | Public model articles 56 to 59 (payment after a call notice) | Stated | Absent → build item |

### Group D — VAT: the position of fees and groups

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-20 | Does every fee or charge flow carry a VAT position — standard-rated, reduced, zero-rated, exempt, outside scope, or disregarded inside a group — with the section relied on? | 1 | VATA 1994 s.4, Schedules 8 and 9, s.43 | Every flow has a position and a section | A flow with none → design defect (Forge R6 finding 5) |
| FN-21 | Is a share subscription treated as outside scope — an issue of shares is not a supply — and stated so? | 1 | *Kretztechnik* (C-465/03) | Stated | Absent → design defect |
| FN-22 | For each company, is taxable turnover compared with the registration threshold (£90,000), the decision stated — compulsory, voluntary, none — and the input-tax consequence priced? | 1 | VATA 1994 Schedule 1 | Comparison, decision and consequence present | Absent → design defect |
| FN-23 | Where a group registration is relied on: is the control test named (s.43A, bodies corporate under common control), the representative member named, joint and several liability priced as a risk, and the joining and leaving steps written as routines with owner and hours? | 1 | VATA 1994 ss.43 to 43A; VAT Notice 700/2 | All four present | Steps absent → build item; liability unpriced → unmeasured input |
| FN-24 | If any line makes exempt supplies, is partial exemption addressed — the method, the de minimis limit — and the irrecoverable input tax entered in that line's budget? | 1 | VAT Notice 706 | Addressed and priced | Absent → design defect |
| FN-25 | Are the return cadence (quarterly; due one month and seven days after the period), the digital-record requirement and the hours per return inside the finance hours? | 1 | Making Tax Digital for VAT; VAT Regulations 1995 | Cadence and hours present | Absent → design defect (an unowned driver) |
| FN-26 | Does the record print the corner in which the VAT position fails — the fee bears irrecoverable VAT — with its margin and verdict? | 1 | VA-89 financial limb; NASA margins; Forge R6 verifier finding 3 | The corner is printed | Absent → design defect |

### Group E — PAYE and statutory-director costs

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-27 | Is every natural person paid classified — office holder (a director's fee is employment income, ITEPA 2003 s.5), employee, contractor, or a person supplied through their own company (off-payroll; a small client leaves the status decision with the intermediary) — with the on-cost priced? | 1 | ITEPA 2003 s.5; Part 2 Chapters 8 and 10 | Every person classified and costed | Unclassified → design defect |
| FN-28 | Is employer registration before the first payday, and a full payment submission on or before each payment, a routine with an owner and hours? | 1 | Income Tax (PAYE) Regulations 2003 | Routine present | Absent → design defect |
| FN-29 | Is employer NIC priced (15 per cent above £5,000 a year, 2025 to 2026), and is the Employment Allowance excluded where the only paid person is a director? | 1 | SSCBA 1992; NICA 2014 s.2(4A) | Priced; allowance treated correctly | Allowance claimed for a director-only company → design defect |
| FN-30 | Is the auto-enrolment position stated — a director with no contract of employment is not a worker; a company with no workers declares that? | 1 | Pensions Act 2008 | Stated | Absent → build item |
| FN-31 | Are the director's statutory costs in the floor as a list — fee and on-cost, identity verification, the registered office, the recording hours at each event (allotment, forfeiture, wind-down)? | 1 | CA 2006 s.155; ECCTA 2023 | The list is in the floor | Any item absent → design defect |

### Group F — The monthly close and the accounts duties of each printed company

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-32 | Is there a monthly close routine — bank reconciled to the record, accruals, spend against budget, money received against the schedule — with an owner, hours, and the output it hands to the periodic instrument? | 1 | CA 2006 s.386(2)(b) (records must show the position at any time); 15288 §6.3.2; EIA-748 monthly variance | Routine with all fields | Absent → design defect |
| FN-33 | Does each company carry its statutory calendar as routines, each with a date rule, an owner, hours and any fee: accounts prepared (s.394), approved (s.414) and filed within nine months (ss.441 to 442); the confirmation statement (s.853A, £34); corporation tax — notify within three months of trading (FA 2004 s.55), the return within twelve months, payment at nine months and one day; VAT returns; real-time PAYE; the PSC register (s.790M); the register of members (s.113)? | 1 (count) | The sections named | Every duty that applies has the four fields | A duty with no owner → design defect |
| FN-34 | Is the accounting framework chosen and stated — FRS 105 micro-entity or FRS 102 section 1A small — with the audit exemption position (s.477; s.479A for a subsidiary under a parent guarantee)? | 1 | FRS 102, FRS 105; CA 2006 ss.477, 479A | Framework and exemption stated | Absent → design defect |
| FN-35 | Is the group-accounts test run — small group (s.383), excluded companies (s.384) — with the thresholds, the reading at each count, and the trigger at which the group-accounts cost enters the floor? | 1 | CA 2006 ss.383, 384, 399 | Test, readings and trigger present | Absent → unmeasured input (Forge R5 finding 1) |
| FN-36 | For a company designed to end at a term, does the record state the basis on which its accounts are prepared — going concern or not — and the disclosure the directors will make? | 2 | FRS 102 paragraphs 3.8 to 3.9; FRC going-concern guidance (2016) | Score ≥ 4 | Score < 4 → design defect |
| FN-37 | Is the late-filing penalty (£150 to £1,500 for a private company) named as the cost of the negative case, and is the routine that stops it — a calendar with a named reader — inside the hours? | 1 | Companies House penalty schedule | Both present | Absent → build item |
| FN-38 | Does the record carry the dated Companies House changes as assumptions to re-read at the review date — identity verification; software-only filing and profit-and-loss filing for small companies from 1 April 2027? | 1 | ECCTA 2023 | The dated lines are present | Absent → build item |

### Group G — Settlement at the end state

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-39 | For each end state — hold, extend, wind-down, default — is the cash route named: what is paid to whom, on which day, under which statutory mechanism? | 1 | 15288 §6.4.14 disposal; CA 2006 | Every end state has a route | An end state with none → design defect |
| FN-40 | Where cash returns to a shareholder, is the route lawful — a reduction of capital by solvency statement (ss.641 to 644) or a members' voluntary liquidation — and never a distribution without profits available (s.830)? | 1 | CA 2006 ss.641 to 644, s.830; ICAEW TECH 02/17BL | A lawful route is named | Unnamed or unlawful → design defect |
| FN-41 | Is the strike-off (s.1003, £33) sequenced after the cash has left the company, since property of a dissolved company passes to the Crown (s.1012)? | 1 | CA 2006 ss.1003, 1012 | The sequence is stated | Absent → design defect |
| FN-42 | Is the settlement's cost in the floor at the share of each end state — the hold share, the kill band, the default rate? | 1 | Ch. 10 life-cycle cost | Costs at their shares | Absent → design defect |

### Group H — Finance hours per company-year against the AOM

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-43 | Does the sum over every activity under this seat of (driver volume × hours) — the statutory calendar, the close, the calls, the settlement, VAT, PAYE — equal the finance figure in the AOM's capacity statement, at central and at both ends of the band? | 1 (arithmetic) | Ch. 10 affordability; VA-89 operational limb | The sum matches at all three points | Mismatch → design defect |
| FN-44 | Are head-office fixed costs (the finance seats) and per-company costs separated, with the fixed cost divided over live companies at each count? | 1 | Ch. 10 affordability; EIA-748 | Separated and divided | Merged → design defect |
| FN-45 | Does the at-scale reading of finance hours per company-year appear for every routine under this seat, sized at the cost of people, and is the AOM capacity figure read from it — with no launch-instance reading (the founder's) substituted anywhere in the architecture? *Founder form moved to pilot instance (VA-23) — §9, FN-45-P.* | 1 | VA-23; `derivation-standard.md` state rule | At-scale reading present; the capacity figure uses it | Reading absent → design defect; a founder reading inside the architecture → design defect (VA-23) |
| FN-46 | Does every finance cost driver name its accountable routine and component, and is every finance routine classified run, manage or hold — with at least one manage routine (the close) and one hold routine (the ring-fence check)? | 1 (traceability, count) | EIA-748 (one responsible manager per control account); the 4 September rule (2) and (3), F2 | Every driver traces; three classes present | An unowned driver → design defect |
| FN-47 | Is there a routine that re-runs the financial simulation and the operating model on any ratified architecture change, and half-yearly regardless? | 1 | The 4 September rule (4); 15288 §6.3.5 | Routine with owner | Absent → design defect |

**Count: 47 checks** — 45 Tier 1, two Tier 2. Group C applies only where shares are partly paid. The two pilot-instance forms in §9 (FN-07-P, FN-45-P) are outside this count: they are launch checks, not architecture checks.

---

## 5 · What a failed check becomes

A failed check is disposed under VA-89 and nothing else. The reviewer classifies; the reviewer does not fix.

| Failure | Class | What the record must carry |
|---|---|---|
| A routine, route, owner or figure is absent, or two figures disagree | **Design defect** | The check ID and the component; the challenge that must reopen |
| A figure exists as a band with no measurement yet | **Unmeasured input** (caps at PROVISIONAL) | Owner, convergence event, trigger and what the trigger moves |
| The thing exists in the design and is not yet built | **Build item** (caps at PROVISIONAL) | Owner, convergence event, re-run threshold |
| The failure is a limit of the world, true of every venture in the class | **Structural limit** (VA-101) | The residual, bounded, and the validation that addresses it |
| A standing ruling forbids the fix — the no-cash rule most often | **Standing constraint** | The ruling cited |

An unclassifiable failed check is a design defect (VA-89's own residual rule). A tax position is a desk position: adopt it from the statute and name what only a ruling would settle (Tom, 14 September 2026). It is never left "for an adviser".

---

## 6 · Worked application — Forge R5 and R6, 16 September 2026

The two runs reviewed this seat from general practice. Read against the standard, their findings map as follows.

| Run finding | Check | Result under the standard |
|---|---|---|
| R6 (1): partly paid shares need bespoke articles | FN-14 | Build item — as disposed |
| R6 (2): standing order is the payer's instrument, Direct Debit the payee's | FN-18 | Unmeasured input, rate per instrument — as disposed |
| R6 (3): two months ahead against a 30-day notice | FN-13 | Pass — the record shows the balance and the day |
| R6 (4): the float is share capital, not client money | FN-11 | Pass — classified, with the account named |
| R6 (5): VAT on the print fee not asked | FN-20, FN-23, FN-26 | Design defect at the run, cured by the group position; the joining and leaving steps a build item — as disposed |
| R6 (6): the sponsor's uncalled liability | FN-09 | Pass — the sponsor's timing cost priced at eight per cent |
| R5 (1): consolidation and the small-group thresholds | FN-35 | Unmeasured input with trigger — as disposed |
| R5 (3): a subsidiary's losses and the intra-group fee | FN-33, FN-34 | Carried — a desk position due before the first year end |
| Company Secretary R6 (1): the amount unpaid on the statement of capital | FN-16 | Pass |

**Five checks the runs did not put, which the standard now does.** These are findings for the CEO of Forge to dispose at the next challenge, not facts about the model.

1. **FN-40 and FN-41.** The record says unspent budget "returns to the sponsor by class right" and the company "is struck off". A printed company that has spent its subscribed capital has no profits available, so the return is a return of capital. The route — a reduction by solvency statement, or a members' voluntary liquidation — is not named, and the strike-off must follow it, not precede it.
2. **FN-17.** The forfeiture routine does not say what becomes of the forfeited shares or who performs the act. Corrected 16 September 2026: this standard first cited the s.662 cancellation duty, which applies to public companies only (s.662(1)); for a private company the route is the reduction under ss.641 to 644 that FN-40 already requires, or holding or re-allotting under the article. The correction came from `company-secretary-standard.md` SEC-27.
3. **FN-36.** Every printed company is designed to end at its term. The basis of preparation for its accounts is not stated.
4. **FN-33.** The statutory calendar of a printed company — the confirmation statement, the corporation tax notice and return, the register duties — is not listed as routines with hours. The term budget names "accountable persons" and incorporation; it does not show these lines.
5. **FN-47.** No half-yearly re-run routine is in the Forge record.

---

## 7 · What this standard does not cover

- **Price and the payment shape as design choices.** The R2 and R6 skills own them. This standard reviews whether the chosen shape can be executed, taxed and accounted for.
- **Valuation and investor returns.** `ive-valuation-custom`; the Studio Director.
- **The family's own finances.** The CFO role in `Family_High_Performance` is a different seat with a different brief.
- **Tax planning beyond the positions named.** Reliefs, elections and structures are outside a craft standard; where one is relied on, the record names it and the section, and FN-20 to FN-31 apply to it.
- **Regulated activities.** A venture that holds client money, lends, insures or issues e-money is regulated. It adds its regulator's capital and conduct rules at step 6b as a standing constraint (the FCA; the PRA). FN-11 only checks that the boundary is stated.
- **Jurisdictions other than England and Wales**, and tax systems other than the UK's.
- **Scoring the Tier-2 rubric.** The descriptors in §3 are drafted for ratification and stay Tom's to change.
- **Thresholds and rates after the review date.** Every figure in §2 carries the year it was read; the owner re-reads them at each review.

---

## 8 · Reviewer checklist — before the 6b table is written

- [ ] Every component carrying this seat's `dri:` has been read, with its definition, note and cost line
- [ ] The financial simulation was opened and every check cell and negative test read, not the record's summary of them
- [ ] Every money flow in the AOM was walked for FN-08 to FN-12, with a holder named for each balance
- [ ] Each company in the design was given its statutory calendar (FN-33) and its VAT position (FN-20 to FN-25)
- [ ] Each end state was given its cash route (FN-39 to FN-41)
- [ ] The AOM capacity statement and the fin-sim rows were read together for FN-43 to FN-46
- [ ] Each Tier-2 check was scored by two people who did not produce the component
- [ ] Each failed check carries one VA-89 class and the fields that class needs; a tax question is a desk position, never "ask an adviser"
- [ ] The conformity guard was applied: every departure from the trade's convention was tested for a derivation before any mark-down
- [ ] No launch constraint (the no-cash rule, the founder's hours, no cold outreach) was read against any figure, gate or verdict at the architecture (FN-07)
- [ ] The pilot-instance forms in §9 were applied only to a pilot-instance record
- [ ] The 6b table cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## 9 · Pilot instance (launch form — outside VA-23 scope)

**Where these apply.** To the pilot-instance record that follows R10. That record is the "shrink the cell, never remove components" design. It stands the fixed architecture up from zero (PCO v8 §9; Tom's ruling of 17 September 2026, `ws1-feedback-log.md`). Never at step 6b of a challenge, never at Converge, never in a FIT verdict. A challenge record that answers one of these has the VA-23 design defect.

**Where the record lives.** Forge's v8 pilot-instance record does not yet exist; it is written after R10. Until it does, these two checks have nothing to read. The pattern for that record is Calmly's launch-form register (`04-Projects/TMTH_Venture_Studio/FinTech_Justice/calmlyresolve-launch-form-register-2026-09-06.html`), which carries each divergence between the designed form and the launch form as a line. The Forge 1.0 first-article derivation of 20 September (`../forge-1.0-first-article-derivation-2026-09-20.md`) is not this record. It is a test-product register on the May 2026 lineage and carries no founder-form checks.

| ID | Question to the pilot-instance record | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| FN-07-P | Is the pilot instance modelled separately from the at-scale state, with cash and the founder's hours as separate lines, and is the pilot-instance cash at zero under the no-cash rule (Tom, 2 September 2026)? | 1 | The no-cash rule; `derivation-standard.md` state rule (the launch form derived from the at-scale projection) | Separate lines; pilot-instance cash £0 | Pilot form mixed into the architecture → design defect (VA-23); pilot-instance cash above £0 → standing constraint |
| FN-45-P | Do the pilot-instance reading (the founder) and the at-scale reading both appear, with the at-scale reading as the parent, and is the pilot-instance reading inside the founder-hours cap? | 1 | `derivation-standard.md` state rule; VA-91 (the capacity figure at the state in force) | Both present; the pilot-instance cap uses the founder reading; the at-scale reading is cited as parent | One reading → design defect; a pilot-instance reading with no at-scale parent → design defect |

---

## Related

- `se-canon-sources.md` — the search order and the mapping table. This standard adds no "no SE analogue" line. Every check found an anchor in the SE canon, in law or in the finance literature
- `tpm-measurement-standard.md` — how every figure is written
- `derivation-standard.md` — the state rule for FN-07 and FN-45 (the at-scale side; the pilot-instance forms are §9); runtime gates for FN-12
- `forge-cf-development-backlog.md` — the VA-23 entry (architecture solves for at-scale, not for getting started); `ws1-feedback-log.md`, 17 September 2026 — Tom's correction and the rule restated
- `validation-standard.md` — a fact in the world takes the desk route first; the rule behind §5's last line
- `realisation-standard.md` — step 6b and step 9, where this standard is applied again at first article
- `context/ceo-forge-memory.md`, 4 September 2026 blocks — F2, the three kinds of routine, the half-yearly re-run
- Forge R3, R5 and R6 records — `../forge-r3-v7-2026-09-16.md` (the carry rule); `../forge-r5-v7-2026-09-16.md` §17; `../forge-r6-v7-2026-09-16.md` §16 to §17

**Version line.** v0.1, 16 September 2026, Head of Product, drafted autonomously; FN-17 and the Law 1 row corrected the same day on s.662 (public companies only), from `company-secretary-standard.md` SEC-27; 47 checks; canon anchors as stated; every check anchored outside IVE. Ratifies object-after 18 September 2026 unless Tom objects, on the WS1 standards rule; the Tier-2 descriptors stay approve-before.

v0.2, 21 September 2026, Head of Product, under Tom's `/autonomous` instruction of the same day. VA-23 rescoping, 21 Sep 2026: FN-07 and FN-45 rewritten as at-scale checks. Their founder-instance forms moved to §9 as FN-07-P and FN-45-P, applied only to a pilot-instance record. The §1 standing-constraint paragraph rescoped the same way. Two checklist lines added. Check numbers unchanged; the count stays 47. Ratifies object-after 23 September 2026 17:00 unless Tom objects.
