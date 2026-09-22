# Head of Method Standard — the method copy a printed company runs on, as a configuration item

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.1 · **Added:** 21 September 2026, under Tom's `/autonomous` instruction of the same day. Cause: "standard missing" reported at step 6b on Forge R1 (v8), R3, R5, R6 and R7 — the seat that keeps the method current and had no standard. The README has carried "still missing: Head of Method" since 16 September.
**Parent:** `derivation-standard.md` · **Siblings:** `print-operations-standard.md` (the seat that stamps the method into a company) · `portfolio-operator-standard.md` (the seat that decides between the gates) · `customer-success-standard.md` (the sponsor during the term) · `finance-standard.md` (the money) · `company-secretary-standard.md` (the legal person) · `run-record-standard.md` (what a run leaves) · `tpm-measurement-standard.md` (how every figure is written)
**Applies to:** every operating-model component that carries `dri: Head of Method` — on Forge, the "Keep the method current" activity (R1 v8; fixed per month; 3 FTE ⚠), the support lines on the price rule and the print budget (R2 v8, R3 v8), the register-row and launch-announcement rules (R7 v7), the term-budget schedule the run emits (R3, R4), the call calendar and reconciliation routine (R6), the term report format and onboarding pack (R5), and the frame for each desk-work family (R1 v8, R2 v8). Any name for the seat that holds the released method version and puts it into every print counts.
**Used at:** process flow v6 step 6b (the light pass per challenge; the full pass at Converge) and `realisation-standard.md` step 6b.

**What this is, and is not.** This is a **craft standard for an output the CF produces** — the versioned method copy that every printed company runs on, its release, its checking, its change loop and its retirement. It is not a change to the CF method. It does not touch Simanis, the BALM disciplines or the criteria system. It gives the reviewing role its questions. The review's output is findings, never rewrites, disposed under VA-89 as design defect, standing constraint, unmeasured input, build item or structural limit.

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date).

---

## 1 · The frame — the seat that holds the released version

Five facts fix the shape of this standard.

**1. The method is maintained once and printed many times, and this seat holds the copy that is printed.** R1 v8 §16: "the method is maintained once for all families"; a family's routines are architected once per family and then printed. Print operations stamps a copy into each company (PR-46); this seat owns what is stamped. The Head of R&D owns what the method says. This seat owns which version of it is in force, what that version contains, and that a run on it leaves the record WS1 needs.

**2. A method that changes while a company runs on it breaks attribution.** The print is a held-out test of a fixed design (WP-5; `objective-function.md`). If the design moves mid-term, a failure after the move belongs to neither version. PR-39 freezes the live company to its printed version. The freeze only means something if the version is a named, fingerprinted set with a change record behind it. That is a configuration item (ISO/IEC/IEEE 15288 §6.3.5), and this seat is its custodian.

**3. The method copy has already drifted once, and nobody was paged.** `forked-toolchain-recommendation-2026-09-10.md`: a second copy of the method under `.agents/skills/` fell about 200 lines behind each challenge skill in six days, across 104 files, after six hand-syncs. Its model checker ran on 7 September with a warning where the canonical checker refuses. The generators were disarmed on 10 September. The finding was disposed in the tool's product spec and the manual's checklist. Nothing in the operating model yet says who holds the canonical version, or what a release must pass.

**4. Registers have collided six times in eleven days, and each collision cost a renumbering.** VA-141 to VA-146 were used as version-block labels inside Calmly's design record on 16 and 17 September while the register was allocating from VA-133 upward. R-W7 was used twice (VA-84's assertion and the 17 September VA-23 note). RD-024 was taken by two parallel sessions on 16 September. RD-030 appears twice in the register. R-V2 collided on 10 September. RD-014 to RD-020 carried seven rule-and-research collisions, ruled on 10 September: a prefix belongs to one register, renumber forward only, cross-reference. The pattern is one defect: a number was written into a file before it was claimed in the register. At 148 prints a year and several sessions a day the rate rises with volume.

**5. Three FTE is a planning figure with no routine behind it.** R1 v8 gives "Keep the method current" 3 FTE at scale, marked ⚠, driver fixed per month. No routine under the seat has hours. The figure cannot be checked until each routine has a driver and a time and the defect rate has a number. The same defect PR-43 found on print operations (2 FTE asserted) is here at 3 FTE.

**The conformity guard, applied to this seat.** The reviewer carries the trade's conventions by training. A change advisory board that meets weekly. A release manager who signs each version. Semantic version numbers on a tag. A product owner who accepts each change. A long-term-support branch patched in place. A deprecation notice with a sunset date. Each is a convention, not a requirement; the reviewer tests each departure for a derivation before any mark-down.

---

## 2 · Canon — the search order, and what each source gives this standard

Canon-first (Tom, 15 September 2026): the systems engineering canon is searched first, then IVE, then the function's own literature, then general practice. The SE canon fixes where each check sits in the life cycle. The function's canon and general practice supply the content of the check.

| Order | Source | What it supplies here |
|---|---|---|
| SE 1 | ISO/IEC/IEEE 15288 — configuration management (§6.3.5: identification, change management, status accounting, evaluation, release control); information management (§6.3.6); measurement (§6.3.7); verification (§6.4.9); maintenance (§6.4.13); disposal (§6.4.14) | The method is a configuration item with a baseline; a change is evaluated, approved and recorded; a release is controlled; a retired item is disposed of with its record kept |
| SE 2 | MIL-HDBK-61A — configuration identification (a unique identifier assigned before release), change classification (Class I touches the baseline's form, fit or function; Class II does not), configuration status accounting, the engineering change proposal | A number is assigned before the item exists; a change that touches what the grader reads is a different class from one that adds a check; the status of every change is accounted for |
| SE 3 | IEEE 828-2012 — configuration management in systems and software engineering (the plan, identification, control, status accounting, audits, release management) | The release is a managed event with entry criteria and a recorded result; an audit compares the built copy with its record |
| SE 4 | INCOSE SE Handbook, 4th ed., §5.5 configuration management; §5.7 measurement; ch. 10 supportability | A baseline is the reference every change is measured against; a technical performance measure has a threshold and a trigger; a fault in the field must be detectable and traceable to a version |
| SE 5 | NASA SE Handbook (SP-2016-6105 Rev 2) §6.5 configuration management; §6.6 technical data management; §6.7 technical assessment | Configuration identification, change control, status accounting and verification are four separate activities; the change record is what the audit reads |
| SE 6 | ISO/IEC 26550 — software and systems product line engineering (core assets, product-specific assets, variability) | One method for all families is a core asset; a family's frame is a product-specific asset; a fork of the core asset is a defect, a variation point is not |
| SE 7 | ISO/IEC/IEEE 29119-1 and -2 — test processes; regression testing as re-execution of a fixed suite after a change | The regression set is re-walked in full on every candidate version; a rule with no regression item is not released |
| SE 8 | INCOSE technical measurement (Roedler and Jones 2005), applied through `tpm-measurement-standard.md` | The defect rate per run per version is a technical performance measure: band, evidence, convergence event, trigger |
| SE 9 | ANSI/EIA-748 — one responsible manager per control account | Every hours line under this seat names the routine that spends it |
| IVE | R1 v8 §16 (the method maintained once for all families; the per-family frame as a WS1 item); R2 v8 (the reliability target as a frame field; the price rule per family, supported by this seat); R3 v8 (the term-budget schedule the run emits; the four calibration conditions on the print gate); R5 v7 (the term report format, the onboarding pack, the escalation rule); R6 v7 (the call calendar, the reconciliation routine, the 'sponsor default' class); R7 v7 (the register-row rule, the announcement rule); `objective-function.md` (the print as a held-out case; the integrity score as diagnostic) | What the seat owes the operating model, item by item, and which of those are build items today |
| Function 1 | `.claude/skills/head-of-rd-custom/SKILL.md` — Mode A (defect to rule change: the four classes, the writing test, the generality test, the regression check); Mode C (the monthly canon sweep; single-sourcing); Mode D (publication: v0.x object-after 48 hours with HoV countersign; v1.0 Tom's); the boundaries (never the grader, never a venture's answer) | The loop this seat's intake feeds, and the line between the two seats |
| Function 2 | `run-record-standard.md` v2 — `harness.json` (fingerprint, length, vault source per method file; version mark); the qualification block; `runs.py diff` | The evidence a version leaves on disk; the tool that compares two runs |
| Function 3 | `forked-toolchain-recommendation-2026-09-10.md`; `manual-release-checklist.md`; `regression-set.md` (RUN WALK, 16 September, 47 of 82) | Drift measured in lines and days; the checklist form a release borrows; the walk a release must repeat |
| Function 4 | Beyer, Jones, Petoff and Murphy (eds.) 2016, *Site Reliability Engineering*, ch. 8 (release engineering: hermetic builds, a release is reproducible from its record), ch. 15 (blameless postmortems: an action item per finding, owned) | A release that cannot be rebuilt from its record is not a release; a postmortem's rule change enters through the change loop, not by edit |
| Function 5 | Deming 1986, *Out of the Crisis*, ch. 11 (the funnel experiment: adjusting a stable process on each result increases its variation); Shewhart 1931 (special cause against common cause) | A rule changed on every run's defect gets worse, not better; a change follows a pattern, a one-off follows a refusal or a safety event |
| Function 6 | Nosek, Ebersole, DeHaven and Mellor 2018 (pre-registration); Holmström 1979 (the party that reports must not decide) | A test whose design moves while it runs loses attribution; the defect rate is read from run records, never reported by the seat |
| Function 7 | Preston-Werner, Semantic Versioning 2.0.0 | A version scheme in which the number says what kind of change the version carries |
| Law | UK GDPR art. 5(1)(e) (storage limitation) — for what a retired version's record keeps of any personal data in reference sets | A retired version is kept while a run record cites it; personal data inside it follows the retention rule of the record, not of the version |
| General practice | The change advisory board; the release manager's sign-off; the long-term-support branch; the deprecation notice; the product owner's acceptance | Named so the reviewer knows what they carry — and so departures from it are recognised, not marked down |

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

The standard is written against the routines below. Each is read off the Forge v7 and v8 records where the record has it. Where the record has no hours the figure is this standard's estimate, marked ⚠, and is an unmeasured input until a run times it. A venture other than Forge substitutes its own record; the routine list is the same because every printed company runs on a released version.

| # | Routine | Driver | Hours or cost in the record | Class | Where it sits in the AOM |
|---|---|---|---|---|---|
| 1 | **Defect intake** — a finding arrives from a run record, a print record, an incident postmortem (PR-28) or a verification pass; the seat logs it against the version it ran on | per defect received | not stated; 0.5 hours (⚠) | run | absent from the record — see §8 |
| 2 | **Canon-first diagnosis** — the defect classified under the four classes (method silence, rule defect, instance leakage, execution failure); SE canon searched, then IVE, then the literature; the search recorded | per defect accepted | not stated; 2 hours (⚠) | run | absent — the Head of R&D's Mode A names the classes; no seat in the AOM performs the intake |
| 3 | **Rule drafting** — the writing test and the generality test; the rule names its enforcement point and its regression item | per rule change | not stated; 3 hours (⚠) | run | absent |
| 4 | **Regression item added; the set walked in full** — the new item written; the whole set re-walked on the candidate version | per rule change; per release | not stated; 1 hour the item (⚠); 8 hours the walk (⚠, from RUN WALK 16 September) | run | absent |
| 5 | **The object-after clock** — the change dated in, countersigned where the rule needs it, dated out; the change record line written | per rule change | not stated; 0.25 hours (⚠) | manage | absent |
| 6 | **Version release** — the release gates walked (§5 group B), the manifest published, the copy stamps checked with print operations (PR-47), the change record closed | per release; monthly at scale (⚠) | not stated; 4 hours (⚠) | manage | absent |
| 7 | **The per-family frame** — the family's routines architected once; the reliability target field set; the frame versioned against the method version | per family | not stated; 40 hours (⚠) | run | R1 v8 §16, R2 v8 (the frame's field) |
| 8 | **The re-run on a ratified change** — which companies, which version pair, the diff of findings (PR-40) | half-yearly; per live company | not stated; £22 compute a run (⚠, R2 retry cap) plus 0.5 hours the read (⚠) | manage | WP-2 by reference; absent as a routine |
| 9 | **Retirement of a version** — no live company on it, the post-term window closed, the manifest kept, new prints refused | per version retired | not stated; 2 hours (⚠) | hold | absent |
| 10 | **Register stewardship** — a number claimed in the register before any file is written; the monthly collision audit | per claim; monthly | not stated; 1 hour a month (⚠) | hold | absent |
| 11 | **Measurement** — the defect rate per run per version read from the run records; the TPM line updated | monthly | not stated; 2 hours (⚠) | hold | absent |
| 12 | **The hand-off to canon** — a change that reaches what a challenge asks or what the grader reads is packaged with its classification and sent to the Head of R&D | per canon-reaching change | not stated; 0.5 hours (⚠) | manage | absent |
| 13 | **The build items owed** — the term-budget schedule (PR-13), the call calendar and reconciliation routine, the 'sponsor default' class, the term report format, the open-job shape, the onboarding pack, the escalation rule, the register-row rule, the announcement rule, the collection-probability guard | once each | not stated | — | R3, R4, R5, R6, R7 build-item tables |

**The capacity figures the record states.** "Keep the method current": 3 FTE at scale (⚠; R1 v8 §16), driver fixed per month. Nothing else. At the pilot instance (a launch figure, read only in §11 under VA-23) the founder performs every routine above by hand, inside 172.4 architect-hours a year.

**An illustrative derivation, so the 3 FTE has something to be tested against.** All figures ⚠. Volume: 148 prints a year (R3's trigger); 20 runs a print (C4); 2,960 runs. Defect rate: 5 per cent of runs produce a method-attributable defect — 148 a year. Per defect, routines 1 to 5: 6.75 hours; 999 hours. Twelve releases: 13 hours each; 156 hours. Five new families: 200 hours. The re-run: 74 hours and £3,256 compute. Register, measurement, retirement and hand-offs: 55 hours. Sum: about 1,484 hours, 0.93 FTE on the 1,600-hour basis. At a 10 per cent defect rate the sum is about 2,480 hours, 1.55 FTE. Three FTE needs a defect rate near 25 per cent, or a routine the record does not name. The defect rate is the input the verdict turns on; it has no measurement yet.

**What the seat does alone, what goes elsewhere.** Written here so the checks in groups C, D and E have something to test against.

| The seat does alone, by refusal or runbook | Goes to the venture (CEO Forge) | Goes to canon (Head of R&D) | Never, by any seat |
|---|---|---|---|
| Release a method version that has passed every gate in group B | Which live companies take a safety-stop change, and when (with the operator's halt) | Any change to what a challenge asks, to the wording of a rule in the canon, to a checking script's rule, to the regression set's rule items | Edit the grader, the rubric, the score model, a threshold or a gate |
| Refuse a release that fails a gate | The decision to reprint a live company on a new version outside a safety stop | Any research item — the number is claimed first (Mode B) | Edit a released version in place (PR-38) |
| Change the shape of what the run emits for operations — the schedule, the record fields, the refusal wording within its ratified meaning | A build item's priority against the venture's other items | The monthly canon sweep for forked generators (Mode C) | Answer a venture's challenge or write a venture's record |
| Write and version a family's frame | A trigger firing on the measured defect rate | Publication of a v0.x standard (Mode D) | Waive a release gate — a waiver is Tom's, approve-before |
| Claim numbers in the registers and run the collision audit | — | — | Change a Tier-2 rubric descriptor |
| Retire a version | — | — | Reuse a register number |

---

## 5 · The checks

Each check is a question the reviewer puts to a component carrying this seat's `dri:`, or to the routine the seat performs. Each names its tier, its anchor, what passes, and what the failure is under VA-89. "Component" means the AOM component under review; "record" means the venture design record and its model files; "the method" means the versioned set of files a run executes; "release" means the act of naming a version and publishing its manifest.

### Group A — The method as a configuration item: baseline, version, change record

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-01 | Is the method identified as one configuration item — the challenge skills, the conductor, the shared generators and checking scripts, the reference sets, the standards a run reads — listed by path in a manifest with a version mark and a fingerprint over the whole set? | 1 | 15288 §6.3.5.3 (identify items); MIL-HDBK-61A (configuration identification); IEEE 828 §6 | The manifest exists, lists every file a run reads, and carries version and fingerprint | Absent → design defect (a version with no contents list cannot be released or retired) |
| HM-02 | Is there a named baseline — the last ratified release — and does every run record state which baseline it ran on, in `meta.json` or `harness.json`? | 1 | 15288 §6.3.5 (baseline); NASA §6.5.1.2; `run-record-standard.md` (version mark) | The baseline is named in the manifest; the field is in the run record and populated on the latest run | Absent → design defect |
| HM-03 | Does the version scheme say what kind of change moves which part of the number — a check-adding row, a change to what the run emits, a change to what a challenge asks — so the number alone tells print operations whether a live company is affected? | 1 | Preston-Werner (semantic versioning); MIL-HDBK-61A (change classification) | The scheme is written with one example per part; ⚠ the assumed scheme is: a check-adding row moves the third part; a change to what the run emits moves the second; a change to what a challenge asks or to canon moves the first | Absent → design defect |
| HM-04 | Is there a change record for the current version listing every change since the baseline, each with its origin (the run or print record ID), its class (HM-16), its enforcement point (VA-100), its regression item, its clock dates and who ratified it? | 1 | 15288 §6.3.5.3 (status accounting); MIL-HDBK-61A; NASA §6.5.1.4 | The record exists with those seven fields per row, and no row is blank in a field | Absent → design defect; a row with a blank field → design defect on that change |
| HM-05 | Is each change classified before it is drafted — Class I: touches what the grader reads (never the seat's); Class II-a: changes what the run emits (the seat's, with the venture); Class II-b: adds a check only (object-after 48 hours, HoV countersign)? | 1 | MIL-HDBK-61A (Class I and Class II); Tom's publication rule of 16 September 2026; the Head of R&D's boundaries | The class is a field on the change record row and matches the change's content | A Class I change in the seat's record → design defect, and the release is refused (HM-14) |
| HM-06 | Is the method one version for all families, with a family's differences held in a frame and never in a second copy of the method? | 1 | ISO/IEC 26550 (core asset against product-specific asset); R1 v8 §16 ("maintained once for all families"); the 10 September fork finding | The record states one method, one canonical path; the family content is a frame that names the method version it was written against | A per-family copy → design defect (the drift of 10 September, once per family) |
| HM-07 | Is each family's frame itself versioned and fingerprinted, does it name the method version it was written against, and does it carry the reliability target as a required field? | 1 | ISO/IEC 26550 (product-specific asset under configuration control); R1 v8 (design defect disposed: the reliability target as a frame field); R2 v8 (the frame's field) | The frame has version, fingerprint, method version and the reliability field | A frame without the reliability field → design defect (R1 v8's disposed defect stays open) |

### Group B — Release gates for a method version

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-08 | Before a version is released, is the regression set walked in full on the candidate version, and is the walk's result recorded with the set's item count, the date, and the count passed — in the RUN WALK form? | 1 | ISO/IEC/IEEE 29119-2 (regression testing); `regression-set.md` (RUN WALK 16 September, 47 of 82) | The walk record exists for the candidate version and every item passes or carries a disposed exception | A release with no walk, or with an undisposed fail → design defect; the release is refused |
| HM-09 | Does every checking script in the shared generators — model coverage, requirement trace, verdict order, fit margin, skill leakage, the toolchain guard, the model checks and their tests — run on the reference set with exit code zero before release? | 1 | 15288 §6.4.9 (verification); `manual-release-checklist.md` section C | Each script is named in the release record with its exit code, all zero | A non-zero exit → the release is refused; a script not run → design defect |
| HM-10 | Does the house-style checker pass with exit code zero on every prose file the release changes — the standards, the skills' prose, the README? | 1 | CLAUDE.md house-style rule (run the checker, do not eyeball it); `manual-release-checklist.md` section D | Each changed prose file is listed with a clean result | A flagged file → the release is refused |
| HM-11 | Has a run on the candidate version emitted every run-record v2 field — the five files, the fingerprint, length and source per method file, the version mark, the system-prompt and reference-set fingerprints, the qualification block — and has `runs.py qualify` accepted it? | 1 | `run-record-standard.md` v2; PR-52 | The latest run on the candidate version is on disk with the five files and passes qualification | A missing field → design defect; the release is refused |
| HM-12 | Is every change in the version's change record ratified — the object-after clock run out, the HoV countersign present where the class needs it, Tom's word present where the class is approve-before — before the version is released? | 1 | 15288 §6.3.5.3 (change approval before implementation); Tom's publication rule of 16 September 2026 | Every row shows a ratification date and, where required, a countersign | An unratified change in a release → design defect; the release is refused |
| HM-13 | Does the release publish a manifest (HM-01) and walk a release checklist in the form of `manual-release-checklist.md` — stamps and identity, open items, ratification integrity, structure, record — with the result kept? | 1 | IEEE 828 (release management); Beyer et al. 2016 ch. 8 (a release reproducible from its record); `manual-release-checklist.md` | The checklist record exists for the release with every line answered | Absent → build item (owner: this seat; convergence: the first release under this standard) |
| HM-14 | Does the release refuse when any gate in this group fails, with no waiver available to the seat — a waiver being Tom's and approve-before? | 1 | `derivation-standard.md` (a prohibition is a built absence); PR-48 (a warning is not a refusal) | The refusal is stated and the waiver path names Tom | A waiver the seat can grant → design defect (the cheaper route under gate pressure stays open) |

### Group C — The rule-change loop as routines with hours

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-15 | Does a defect enter the loop only from a record — a run record, a print record (PR-53), an incident postmortem (PR-28) or a verification finding — carrying that record's ID, so that no rule changes on an untraced report? | 1 | 15288 §6.3.5.3 (a change request identifies its source); Beyer et al. 2016 ch. 15 (an action item per finding); `run-record-standard.md` | The intake routine (§4 row 1) states the four sources and the ID field, and the change record shows an ID on every row | A change with no origin ID → design defect |
| HM-16 | Is each defect classified under the four classes — method silence, rule defect, instance leakage, execution failure — after a canon-first search recorded in the order SE canon, IVE, literature, and is the classification reproducible from the search record? | 2 | Head of R&D Mode A (the four classes); `se-canon-sources.md` §4 (the search order); Tom's ruling of 15 September 2026 (canon first) | Scored four or above on the §3 rubric by two independent scorers | Below four → design defect on the diagnosis |
| HM-17 | Before a rule is drafted, do the writing test (can the rule be stated in one sentence that a run can act on) and the generality test (would the rule have caught the defect on a different venture) both pass, with the test recorded? | 2 | Head of R&D Mode A (writing test, generality test); VA-46 (no invented dependency) | Scored four or above by two independent scorers | Below four → design defect; the rule returns to drafting |
| HM-18 | Does every rule the seat drafts name its enforcement point — a checking script, a refusal in the run, a checklist line, a required field — and does that point exist or carry a build item? | 1 | VA-100 (a rule with no enforcement point has not been made); `derivation-standard.md` (interlocks) | The enforcement point is a field on the change record row, and it names a file or a build item | A rule with a blank enforcement point → design defect (the rule has not been made) |
| HM-19 | Is a regression item added for every rule change before the version carrying it is released, and does the set then re-walk in full (HM-08)? | 1 | ISO/IEC/IEEE 29119-2; Head of R&D Mode A (add the regression check) | The item number appears on the change record row and in `regression-set.md` | A rule with no item → design defect; the release is refused |
| HM-20 | Does the object-after clock run by class — a check-adding row 48 hours with HoV countersign; a change to what the run emits object-after with the venture; a Tier-2 descriptor, the grader, a threshold or a gate approve-before — with the start and end dated on the change record row? | 1 | Tom's publication rule of 16 September 2026; the derived-work rule of 1 September 2026 (object-after 48 hours) | Each row shows class, clock start, clock end and, where required, the countersign | A change released inside its clock → design defect |
| HM-21 | Does a ratified change produce a new version, never an edit to a released version in place, and does the change record show the version each change first appears in? | 1 | 15288 §6.3.5 (release control); PR-38 | Every change names the version it entered; no released manifest has been altered after its release date | An in-place edit → design defect |
| HM-22 | Is there a stopping rule — a rule changed three times in 90 days (⚠) stops changing and is reopened as a research item with an RD number claimed; a change follows a pattern of two or more (⚠) runs, except a refusal or safety defect, which may change on one? | 2 | Deming 1986 ch. 11 (tampering with a stable process); Shewhart 1931 (special cause against common cause); Head of R&D Mode B (claim the number first) — partial SE analogue: 15288 §6.3.5 evaluates each change but has no rule against repeated change | Scored four or above: the rule is stated with the two thresholds and the exception, and the change record shows it applied | Absent → design defect (the loop tampers) |
| HM-23 | Does every routine in §4 rows 1 to 12 carry a driver and hours, and is the seat's FTE derived from the sum at the at-scale volume and the measured defect rate — not asserted at 3 FTE (⚠)? | 1 (arithmetic) | ANSI/EIA-748 (one responsible manager per control account); `tpm-measurement-standard.md`; PR-43 (the same defect on print operations) | The sum is shown and the FTE recomputed from it; the defect rate carries its convergence event | 3 FTE with no sum → unmeasured input (owner: this seat; convergence: the first 20 runs' defect count and the first release timed) |

### Group D — Whose rule it is: the seat's, canon's, nobody's

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-24 | Does the record state what the seat may change alone — the shape of what the run emits for operations (the schedule, the record fields, the refusal wording within its ratified meaning), a family's frame, the release checklist, the register-row and announcement rules — as the set of components carrying `dri: Head of Method`? | 1 | 15288 §6.3.5.2 (the change authority is defined per item); ANSI/EIA-748 | The set is listed and matches the `dri:` fields in the AOM | Absent → design defect |
| HM-25 | Is each change routed by its content — to the Head of R&D when it touches what a challenge asks, the canon's wording, a checking script's rule or a regression rule item; kept by the seat when it touches only what the run emits or a frame — with the routing recorded and reproducible from the change's diff? | 2 | Head of R&D boundaries (never edit the grader; the method's content is canon's); MIL-HDBK-61A (Class I and Class II) | Scored four or above by two independent scorers on the routing of the last ten changes | Below four → design defect on the routing |
| HM-26 | Does the seat's change record contain no change to the grader, the rubric, the score model, a threshold, a gate or the IVE canon — and does the release refuse a change record that does (HM-14)? | 1 | Head of R&D boundaries; README autonomy boundaries; `objective-function.md` (the grader is the constraint set) | The change record has no Class I row; the refusal is stated | A Class I row → design defect; the release is refused |
| HM-27 | Does the seat answer no venture's challenge and write no venture's record — the same boundary the Head of R&D carries — with the seat's outputs limited to the method, its frames, its releases and its records? | 1 | Head of R&D boundaries (never answer a venture's challenge) | The seat's output list in the AOM has no venture record in it | A venture record with this seat as author → design defect |
| HM-28 | Does a canon change ratified by the Head of R&D enter the method only through this seat's release (group B), so that canon and the released version cannot differ except between a ratification and the next release? | 1 | 15288 §6.3.5 (release control); IEEE 828 (release management) | The path from ratified canon change to released version is one route, through group B | A second route (a canon edit that a run reads before release) → design defect |
| HM-29 | Where a change to what the run emits also changes what the grader reads — a field the score model consumes — is the change treated as Class I and routed to canon, not kept as the seat's? | 1 | MIL-HDBK-61A (a change that touches the baseline's function is Class I whatever its size); PR-55 (the run does not write its own score) | The change record shows the Class I routing on any row that touches a scored field | Kept as the seat's → design defect |

### Group E — Live companies, the version in force, and the re-run

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-30 | Is the version in force for each live company read from that company's own record (PR-02), never from "the current version"? | 1 | MIL-HDBK-61A (status accounting per unit); PR-02 | The seat's version register lists each live company against its printed version, read from the company record | A list read from the current version → design defect |
| HM-31 | Does each release note list the live companies frozen to earlier versions (PR-39), with their term-end dates, so the re-run (HM-32) can be scheduled? | 1 | PR-39; Nosek et al. 2018 (the design fixed while the test runs) | The list is in the release record | Absent → design defect |
| HM-32 | Is the re-run on a ratified change (PR-40) scheduled by this seat — which companies, which version pair, half-yearly — and does it produce a run-record pair with the diff of findings, read with `runs.py diff`? | 1 | PR-40; `run-record-standard.md` (`runs.py diff`) | The schedule exists and the last re-run's pair is on disk | Absent → build item (owner: this seat; convergence: the first ratified change after a live print) |
| HM-33 | Is a safety-stop change — the one exception to the freeze — classified as such on the change record with the defect that made it a safety stop, and does it reach a live company only with the operator's halt and the venture's decision? | 2 | PR-39 (the safety-stop exception); Handbook ch. 10 system safety; PO-25 (the in-term stop) | Scored four or above: the classification is stated, the defect named, the route through halt and decision shown | Below four → design defect |
| HM-34 | Is a defect found on a live company on version n classified and counted against version n (PR-30), not against the current version? | 1 | PR-30; MIL-HDBK-61A (status accounting) | The intake routine records the version from the company record; the rate (HM-48) is computed per version | Counted against the current version → design defect (the rate is wrong for both versions) |

### Group F — Numbering discipline in the registers

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-35 | Does each register (VA, RD, R-W, R-V, R-T, NCR, HM and the sibling prefixes) have one prefix, one file that allocates, and a rule that the number is claimed in that file before any other file is written — the register is the lock, the file is not? | 1 | MIL-HDBK-61A (a unique identifier assigned before release); 15288 §6.3.5.3; the 10 September ruling (a prefix belongs to one register) | The rule is written at the head of each register and the allocating file is named | Absent → design defect (the six collisions of 10 to 21 September recur with volume) |
| HM-36 | Does a claimed number carry a state — claimed, written, ratified, withdrawn — with the claimant and the date, so two sessions cannot both claim the next number? | 1 | 15288 §6.3.5.3 (status accounting); RD-024 (taken twice, 16 September, two parallel sessions) | The state field exists on every row from the rule's date | Absent → design defect |
| HM-37 | When a collision is found, is the later claimant renumbered forward with a cross-reference, and is the earlier number never edited — renumber forward only? | 1 | The 10 September ruling on RD-014 to RD-020; VA-96 to VA-101, VA-82 to VA-88 to VA-89 and VA-90 (renumbered forward) | The collision rule is written and the last collision's resolution follows it | An earlier number edited → design defect |
| HM-38 | Are labels used inside a design record — version blocks, local section marks — drawn from the record's own local scheme and never from a register's prefix, so a label cannot be mistaken for a claimed number? | 1 | No SE analogue — the canon assigns identifiers to items, not labels to blocks inside a document; evidence: VA-141 to VA-146 used as version-block labels in Calmly's design record, 16 and 17 September 2026 | The rule is written and no record since its date uses a register prefix as a local label | A register prefix as a local label → design defect |
| HM-39 | Is there a duplicate-number check that runs at each release (group B) across every register and every file that cites a register number, and does a duplicate refuse the release? | 1 | IEEE 828 (configuration audit); HM-14 | The check is a script named in the release record with exit code zero | Absent → build item (owner: this seat; convergence: the first release under this standard) |
| HM-40 | Does each register's head state its highest claimed number, and does that figure match the file's rows and the feedback log's last claim? | 1 | 15288 §6.3.5.3 (status accounting) | The head figure matches on the review date (VA-166 at 14:00 on 21 September 2026 — nineteen numbers claimed in five days, six of them today) | A mismatch → design defect |

### Group G — Method-copy integrity, and retirement of a version

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-41 | Does each release publish a manifest — the file list, a fingerprint and length per file, the version mark, the baseline it succeeds — as the record every copy is compared against? | 1 | IEEE 828 (release management); Beyer et al. 2016 ch. 8 (a hermetic release); HM-01 | The manifest is on disk for the current version and every retired one | Absent → design defect |
| HM-42 | Can a stamped copy in any print file (PR-46) be compared with its release manifest, file by file, and the difference listed — the comparison being a script, not a reading? | 1 | IEEE 828 (physical configuration audit); MIL-STD-1521B (PCA); `run-record-standard.md` (`harness.json` fingerprints) | The comparison script exists and the last release's comparison result is recorded | Absent → build item (owner: this seat; the check at release is print operations' PR-47) |
| HM-43 | Does a copy whose fingerprints differ from its stamped version refuse to run, rather than warn — the refusal built into the method, the check at release built into print operations (PR-47, PR-48)? | 1 | PR-48; the 7 September event (a warning where the canonical checker refuses); `derivation-standard.md` (a built absence) | The refusal is in the method and tested on a deliberately altered copy | A warning → design defect |
| HM-44 | Do print copies come only from the canonical path, with no second generator or fork in the method's own files — the monthly sweep for forks being the Head of R&D's Mode C, and this seat's check being the source field on every stamped copy? | 1 | ISO/IEC 26550 (one core asset); the 10 September finding (`.agents/skills/` fork, 104 files); Head of R&D Mode C | Every `harness.json` source field names the canonical path; none is `null` for a method file | A non-canonical source → design defect |
| HM-45 | Is a version retired only when no live company runs on it and the post-term window (⚠ the term plus the market-answer window WP-5 reads) has closed, and is the retirement a change-record line, dated, with the reason? | 1 | 15288 §6.4.14 (disposal); MIL-HDBK-61A (retention of the record) | The retirement rule is stated and each retired version has its line | Absent → design defect |
| HM-46 | Is a retired version kept readable, with its manifest, for as long as any run record or print record cites it — never deleted — and does a retired version refuse to be stamped into a new print? | 1 | 15288 §6.3.6 (information management); UK GDPR art. 5(1)(e) for any personal data inside reference sets; HM-14 | The retention rule names the citing records as its clock; the refusal is stated | Deletion, or a new print on a retired version → design defect |
| HM-47 | Does the change record for every version — current and retired — list the rule changes it carries, their defects of origin, their regression items, their class, their ratification dates and their ratifiers (HM-04), so that any finding on any run can be traced to the change that caused or missed it? | 1 | 15288 §6.3.5.3 (status accounting); NASA §6.5.1.4 | Every version's change record is complete on those fields | A gap → design defect on that version |

### Group H — Measurement: the defect rate, the family frame, and hours against capacity

| ID | Question to the component | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-48 | Is the defect rate per run per version defined — numerator: findings classified rule defect or method silence and attributed to the version (HM-16, HM-34); denominator: runs completed on the version; window: the last 20 runs (⚠) — with the run record as the only source? | 1 | 15288 §6.3.7 (measurement); Roedler and Jones 2005; `tpm-measurement-standard.md` | The definition is stated with the three parts and the source | Absent → design defect (3 FTE and every release decision rest on it) |
| HM-49 | Does the rate carry the TPM fields — band, evidence, convergence event, threshold, trigger, owner — with ⚠ assumed figures until measured: threshold 5 per cent of runs; trigger 10 per cent over the window; convergence the first 20 held-out runs on a version? | 1 | `tpm-measurement-standard.md`; NASA §6.7 (a TPM has a threshold and a trigger) | The line exists with every field and the ⚠ marks | A field missing → unmeasured input (owner: this seat) |
| HM-50 | Is there a refusal band — a version whose rate is above the trigger over the window refuses to print new companies, and the next release is blocked until a version is below the threshold — built as an absence and tested? | 1 | No SE analogue — the canon triggers a review on a breached TPM (NASA §6.7); it does not make the configuration item refuse its own use; `derivation-standard.md` (a built absence); PR-48 | The refusal is stated, its test recorded, and the block on the next release stated | A review without a refusal → design defect |
| HM-51 | Is the rate treated as diagnostic — it can refuse a version, it cannot make one succeed — with the objective remaining the printed companies' expected net present value, and no release decision made on the rate alone? | 2 | `objective-function.md` (the integrity score is diagnostic; gates are constraints) | Scored four or above: the record states the rate's role and the last release decision shows the objective read beside it | Below four → design defect |
| HM-52 | Is the rate read from the run records by a script, never reported by the seat, and is the party that releases a version not the party that scores its runs? | 1 | Holmström 1979; PR-55 (the run does not write its own score); `run-record-standard.md` (`runs.py list`) | The script is named and the two parties are different seats | Self-reported → design defect |
| HM-53 | Does each family's frame carry the reliability target (HM-07), and are the four calibration conditions on the print gate (R3 v8) — 30 confirmed outcomes in the family, five families, 60 per cent of outcomes within twelve months, 15 points above base rate on a held-out set — read per family before the gate opens for that family? | 1 | R3 v8 (the four conditions); R1 v8 and R2 v8 (the reliability field); NASA §6.7 | Each family's record shows the target and the four conditions with their current values | Absent → unmeasured input (owner: this seat with the venture; convergence: the 30th outcome in the first family) |
| HM-54 | Is the seat's hours-per-month sum recomputed with every routine in §4 at the at-scale volume, against the FTE stated, with the defect rate carried as the input the sum turns on (§4 derivation)? | 1 (arithmetic) | Handbook ch. 10 affordability; PR-41 and PR-43 (the same sums on print operations) | The sum is shown and the FTE matches it within the defect-rate band | 3 FTE with no sum → unmeasured input (as HM-23) |
| HM-55 | Does the latest run on disk emit what §6 lists for this seat — the version and baseline, the findings tagged with check ID and class, the regression walk reference, the checking-script exits — and is the print record (PR-53) reading the same fields? | 1 | No SE analogue for the seat's record inside a run — the canon audits the item, not the record its use leaves; `run-record-standard.md`; PR-53 | The fields are present on the latest run | Absent → build item (owner: this seat via the Head of R&D's skill change — the open item in `run-record-standard.md`) |

**Count: 55 checks** — 49 Tier 1, 6 Tier 2 (HM-16, HM-17, HM-22, HM-25, HM-33, HM-51).

---

## 6 · What a WS1 run must emit for this seat

`run-record-standard.md` v2 fixes five files and the fields in them. This section lists what this seat reads from those files and what is not yet in them. Nothing here changes the five-file layout; a new field is a skill change through the Head of R&D (the open item at the foot of `run-record-standard.md`).

| Field | File | Exists in v2 | Why the seat needs it |
|---|---|---|---|
| Fingerprint, length and vault source per method file; the version mark | `harness.json` | Yes | HM-02, HM-42, HM-44 — the copy compared with its manifest; the source checked as canonical |
| System-prompt and reference-set fingerprints | `harness.json` | Yes | HM-41 — the manifest covers the reference sets, so a leak sweep can name the set version |
| Qualification block — class, completion state, the three facts, the evidence | `meta.json` | Yes | HM-48 — only a COMPLETE_VERIFIED held-out run enters the rate's denominator |
| The baseline the run ran on, named | `meta.json` | No — the version mark is present; the baseline name is not | HM-02 — a run must say which ratified release it stands on |
| Each finding tagged with the check ID that put it and its VA-89 class | `score.json` | No — findings are free text | HM-15, HM-48 — a defect enters the loop with an ID; the rate counts by class |
| Each finding's Mode A class, once diagnosed — method silence, rule defect, instance leakage, execution failure | `score.json`, written back by the seat after diagnosis, never by the run | No | HM-16, HM-34, HM-48 — the numerator of the rate |
| The regression walk the version passed — set date, item count, count passed | `harness.json` | No | HM-08 — a run on an unwalked version is visible from its own record |
| The checking scripts' exit codes at release | `harness.json` | No | HM-09 |
| The register numbers the run claimed, with their state | `trace.jsonl` | No | HM-35, HM-36 — a claim inside a run is visible to the collision audit |

The four fields the seat writes back — the Mode A class and the three release references — go into the record after the run, with the seat's own timestamp, so the run never writes its own diagnosis (HM-52).

---

## 7 · What a failed check becomes

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

## 8 · Worked application — Forge R1 to R7, 16 to 17 September 2026

Five runs named this seat and reviewed it from general practice with no standard. Read against the standard, their findings map as follows.

| Run finding | Check | Result under the standard |
|---|---|---|
| R1 v8: "Keep the method current", 3 FTE ⚠, fixed per month; "standard missing — logged" | HM-23, HM-54 | Unmeasured input — the FTE has no routine sum; §4 gives the illustrative derivation (0.93 to 1.55 FTE ⚠) |
| R1 v8: the reliability target per family as a required frame field — design defect, disposed to R2 and this seat | HM-07, HM-53 | Design defect stands until the field is in the frame; HM-53 adds the four calibration conditions per family |
| R3: the term-budget schedule the run emits, so the sum is derived (PR-13) | HM-24, HM-55 | Build item, owner this seat — as disposed; a change to what the run emits, Class II-a |
| R3 v8: the seat supports the print budget and the price rule per family from the cost model | HM-07, HM-24 | The support line exists; it is a per-family frame item, in scope |
| R5: term report format, open-job shape, onboarding pack, escalation rule | HM-24 | Build items — as disposed; all Class II-a (what the run emits) |
| R6: call calendar, notice and reconciliation routine, 'sponsor default' class in the WP-5 rule | HM-24, HM-29 | Build items — as disposed; the 'sponsor default' class touches what the term decision reads, so HM-29 routes it to canon before release |
| R7: the register-row rule and the launch-announcement rule in the print file | HM-24 | Build items — as disposed |
| R7 v7 §20a: the stamp and fingerprint in the print file and the release checklist (PR-46 to PR-48) | HM-41 to HM-44 | Build item shared: the refusal is in the method (this seat); the check at release is print operations' |

**Twelve checks the runs did not put, which the standard now does.** These are findings for the CEO of Forge to dispose at the next challenge, not facts about the model. The arithmetic ones come first.

1. **HM-23 and HM-54 — three FTE is asserted, not derived.** No routine under the seat has hours. The illustrative sum in §4 lands at 0.93 FTE at a 5 per cent defect rate and 1.55 FTE at 10 per cent, all ⚠. Three FTE needs a defect rate near 25 per cent or a routine the record does not name. The defect rate is the input the verdict turns on and it has no measurement.
2. **HM-48 and HM-49 — the defect rate has no definition.** Nothing in the record says what counts as a method defect, over how many runs, or from which file it is read. Until it does, the FTE, the release decision and the refusal band all rest on nothing.
3. **HM-01 and HM-02 — the method is not identified as one item.** The run reads a set of files; no manifest lists them; no run record names the ratified release it ran on. The version mark in `harness.json` is a start, not a baseline.
4. **HM-04 and HM-47 — there is no change record.** The feedback log holds the history as prose. A finding on a run cannot be traced to the change that caused or missed it without reading the log end to end.
5. **HM-05, HM-25 and HM-26 — changes are not classified before drafting.** The Head of R&D's boundary says what is never touched. Nothing says, per change, which class it is and who may ratify it. The publication rule of 16 September supplies the clocks; the classification that selects a clock is missing.
6. **HM-08 to HM-14 — a release has no gates.** The regression set was last walked in full on 16 September (47 of 82). The checking scripts are run when someone remembers. No rule says a version cannot be released without them, and no refusal exists.
7. **HM-22 — there is no stopping rule.** A rule can be changed on every run's defect. Deming's funnel says that makes it worse. The three-in-90-days figure is ⚠ and is the seat's to converge.
8. **HM-35 to HM-40 — the registers have no lock.** Six collisions in eleven days, each resolved by hand. No register states that the number is claimed before the file is written; no state field; no duplicate check at release. The VA-141 to VA-146 case shows a second failure: a register prefix used as a local label.
9. **HM-31 and HM-32 — the re-run is a rule with no schedule.** PR-40 says half-yearly. Nobody holds the list of frozen companies and their term ends, so nobody can schedule it.
10. **HM-45 and HM-46 — a version has no end.** Nothing says when a version is retired, what is kept, or that a retired version refuses a new print.
11. **HM-50 — a breached rate triggers a review, not a refusal.** The canon's TPM practice reviews; the studio's rule (PR-48, VA-100) is that a rule with no enforcement point has not been made. A version above the trigger must refuse to print.
12. **HM-55 — the run does not emit what the seat needs.** Findings are free text; no check ID, no class, no regression reference. The open item in `run-record-standard.md` — a vault run does not write its own record — carries this too, and is a skill change through the Head of R&D.

---

## 9 · What this standard does not cover

- **The content of the method** — what the ten challenges ask, the wording of a rule in the canon, the regression set's rule items, a checking script's rule, the research pipeline. That is the Head of R&D's (`/head-of-rd-custom`, Modes A to D). This standard covers the released version those contents are stamped into, and the intake that feeds Mode A from printed companies.
- **The grader** — `/verify-venture-custom`, the rubric, the score model, the thresholds and the gates are untouched; HM-26 checks only that the seat's change record contains no change to them.
- **The stamp check at each print-file release and the print step** — PR-46 to PR-48 and PR-01 to PR-07 are print operations'. This standard supplies the manifest they compare against (HM-41) and the refusal in the method (HM-43).
- **The live company between the gates** — PR-30, PR-38 to PR-40 are print operations' and the operator's; this standard reads them by number (group E) and does not restate them.
- **The record a printed company leaves** — PR-53 is print operations' with this seat; §6 states only what the run emits for this seat.
- **The reference-set leak check** — `R_and_D/rd-002-instance-leakage-sweep-2026-09-10.md`; the Head of R&D's.
- **Publication of a standard** — Mode D; the v0.x clock and the HoV countersign are the Head of R&D's to run, and Tom's to sign at v1.0.
- **The hosted tool's product design** — `../product-spec-forge-tool-2026-09-14.md`.
- **Scoring the Tier-2 rubric.** The descriptors in §3 are drafted for ratification and stay Tom's to change.

---

## 10 · Reviewer checklist — before the 6b table is written

- [ ] Every component carrying this seat's `dri:` and every support line naming the seat has been read, with its definition, note and cost line
- [ ] The method was looked for as a manifest with a version and a fingerprint (HM-01), not as a description of files
- [ ] The latest run record was opened and the baseline field looked for (HM-02)
- [ ] The change record was looked for as a table with seven fields per row (HM-04), not as the feedback log
- [ ] Each of the last ten changes was classified by two scorers who did not make it (HM-25)
- [ ] The regression walk and the checking-script exits were looked for on the candidate version, not on an earlier one (HM-08, HM-09)
- [ ] The hours-per-month sum was recomputed with every routine in §4 at the at-scale volume and the defect rate stated (HM-23, HM-54)
- [ ] The defect rate was looked for as a definition with numerator, denominator, window and source (HM-48) before any FTE figure was read
- [ ] The registers were read for a claim rule, a state field and the highest number (HM-35, HM-36, HM-40)
- [ ] The design records since 16 September were searched for a register prefix used as a local label (HM-38)
- [ ] The refusal on a breached rate and the refusal on an altered copy were looked for as built absences, not as reviews (HM-43, HM-50)
- [ ] No launch constraint (the no-cash rule, the founder's hours, no cold outreach) was read against any figure or verdict at the architecture
- [ ] The pilot-instance forms in §11 were applied only to a pilot-instance record
- [ ] Each failed check carries one VA-89 class and the fields that class needs
- [ ] The conformity guard was applied: every departure from the trade's convention was tested for a derivation before any mark-down
- [ ] The 6b table cites the check IDs, so the next run can diff against this one
- [ ] House-style checker run on the review record: `python3 .scripts/check-house-style.py <file>`

---

## 11 · Pilot instance (launch form — outside VA-23 scope)

**Where these apply.** To the pilot-instance record that follows R10. That record is the design that stands the fixed architecture up from zero (PCO v8 §9; Tom's ruling of 17 September 2026, `ws1-feedback-log.md`). Never at step 6b of a challenge, never at Converge, never in a FIT verdict. A challenge record that answers one of these has the VA-23 design defect.

**Where the record lives.** Forge's v8 pilot-instance record does not yet exist; it is written after R10. The pattern for it is Calmly's launch-form register. See `finance-standard.md` §9 for the same note in full. At the pilot instance this seat is the founder, and the Head of R&D is the same person; the two seats' records stay separate even where the hands are the same.

| ID | Question to the pilot-instance record | Tier | Anchor | Passes when | If it fails |
|---|---|---|---|---|---|
| HM-23-P | Is every routine in §4 the founder performs — intake, diagnosis, drafting, the walk, the release, the frame — inside the founder-hours figure a year, and does the cap on releases and families recompute from the sum (172.4 architect-hours on Forge v7, shared with every other seat the founder holds)? | 1 (arithmetic) | `derivation-standard.md` state rule; PR-41-P (the same sum on print operations) | The sum is shown and the release and family caps recomputed from it | Unmeasured input (owner: this seat; convergence: the first release timed) |
| HM-08-P | Is the regression walk at the pilot instance performed by hand, timed, and is that time the convergence event for routine 4's 8 hours (⚠) at scale? | 1 | `tpm-measurement-standard.md` (convergence event); RUN WALK 16 September | The walk is timed on the pilot-instance record and the figure entered against routine 4 | Unmeasured input |

---

## Related

- `se-canon-sources.md` — the search order and the mapping table; this standard's "no SE analogue" lines (HM-38, HM-50, HM-55) and its partial line (HM-22) are added to §3
- `.claude/skills/head-of-rd-custom/SKILL.md` — Modes A to D and the boundaries; the loop this seat's intake feeds
- `run-record-standard.md` — the five files, the fingerprint and the version mark; the open item on a vault run writing its own record, which §6 extends
- `print-operations-standard.md` — PR-01, PR-02, PR-13, PR-19, PR-28, PR-30, PR-38, PR-39, PR-40, PR-46 to PR-48, PR-52, PR-53, PR-55 — read by number, never restated
- `portfolio-operator-standard.md` — PO-25 (the in-term stop, for HM-33)
- `regression-set.md` — RUN WALK; the item every rule change adds
- `manual-release-checklist.md` — the form HM-13 borrows
- `objective-function.md` — the rate as diagnostic (HM-51)
- `tpm-measurement-standard.md` — how every hours and rate figure is written
- `derivation-standard.md` — built absences (HM-14, HM-43, HM-50); the state rule for §11
- `forked-toolchain-recommendation-2026-09-10.md` — the evidence behind group G
- `../R_and_D/README.md` — the collision ruling of 10 September and the register states; the evidence behind group F
- `forge-cf-development-backlog.md` — VA-23, VA-46, VA-89, VA-100, VA-101; `ws1-feedback-log.md` — the collisions of 10 to 21 September (R-V2, RD-014 to RD-020, RD-024, RD-030, R-W7, VA-141 to VA-146)
- Forge records — `../forge-r1-v8-2026-09-17.md` §16; `../forge-r2-v8-2026-09-17.md` (the frame's field; the price rule); `../forge-r3-v8-2026-09-17.md` (the four calibration conditions; the print budget line); `../forge-r5-v7-2026-09-16.md`, `../forge-r6-v7-2026-09-16.md`, `../forge-r7-v7-2026-09-16.md` (the build items owed)

---

**Version line.** v0.1, 21 September 2026, Head of Product, drafted autonomously under Tom's `/autonomous` instruction; 55 checks, 49 Tier 1 and 6 Tier 2; canon anchors as stated; three checks with no SE analogue (HM-38, HM-50, HM-55), one partial (HM-22), each added to `se-canon-sources.md` §3. Boundary with the Head of R&D drawn in §4 and group D: canon content, research, grader proposals and publication are the Head of R&D's; the released version, its gates, its intake from printed companies, its registers, its frames and its retirement are this seat's; the grader, the score model, the thresholds and the IVE canon are nobody's to change but Tom's. Ratifies object-after 23 September 2026 17:00 unless Tom objects, on the WS1 standards rule; the Tier-2 descriptors stay approve-before.
