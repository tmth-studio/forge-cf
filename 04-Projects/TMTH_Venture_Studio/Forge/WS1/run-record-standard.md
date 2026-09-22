# The run record — what every Forge run leaves behind

**Date:** 14 September 2026 · **Version 2:** 21 September 2026
**Written by:** Head of Product, on item (a) of `meta-harness-note-2026-09-14.md`
**Status:** in force from the next run. Version 2 — adds the qualification block (Tom's correction of 21 September 2026: "SOUND WITH GAPS" is a failed qualification, not an end state; a score is diagnostic and never stands in for a completed, verified architecture). Version 1 records are read with both new fields treated as `INCOMPLETE` / `iterative_design_case` until the fields are written.
**Reads with:** `meta-harness-note-2026-09-14.md` · `README.md` (the WS1 loop) · `../product-spec-forge-tool-2026-09-14.md`

Labels. FACT is in a named file or was checked on disk today. INFERENCE follows from named facts. ASSUMPTION was chosen and can be replaced; every assumed figure carries ⚠.

Two terms used throughout. A **fingerprint** is a short code computed from a file's contents: the same contents give the same code, and one changed character gives a different one. A **version mark** is the label the version-control tool gives each saved state of the code.

**Owner:** Head of Product
**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date)

---

## The rule in one paragraph

Every Forge run leaves one folder. The folder holds five files with fixed names. Together they say which version of the method and the code ran, what the run started from, everything that happened, and what it scored. A person can read the files, and so can a program. Nothing about a run lives only in prose any more. The exhaust of a run is the product of WS1 (Tom, 14 September), and this is the shape of the exhaust.

---

## Where the folders live

FACT. Two places, one layout.

| Runs from | Folder | How the record gets there |
|---|---|---|
| The vault — a challenge skill run in a session on this Mac | `04-Projects/TMTH_Venture_Studio/Forge/WS1/runs/` | Written by hand, or by the session, to the layout below |
| The hosted service (`tmth-studio/forge-app`) | The same folder, after export | The service builds the record from its database on request; a small script writes it into the folder. Or set the service's `RUN_RECORDS_DIR` and it writes the folder as the run goes |

INFERENCE. The hosted service keeps runs in a database, not in files (FACT: `lib/db.js` — tables for runs, messages, findings, refused findings, spend, feedback and the close answers). So the record is built from the database and written out; the database stays the store. The hosting machine does not keep its disk between deployments, so writing there as the run goes would lose the files. Export is the route for the live service; writing as the run goes is for a machine that keeps its files.

---

## One folder per run

The folder is named so that folders sort by date and read on their own:

```
<date>_<venture>_<label>
```

FACT, examples on disk today: `2026-09-04_datum_blind-c1-c3` (a vault run) and, from the service, `2026-09-14_acmecover-example_forge-run-1` (date, the website the person gave, the service's run number).

Inside, five files with these names and no others in the top level:

| File | What it holds |
|---|---|
| `meta.json` | The small facts: date, model, entry path, stages reached, turns, cost, and what the trace lacks |
| `harness.json` | Which code and which method files ran, each with a fingerprint |
| `inputs.json` | What the run started from: the website and its text, or the files read; every entry the person wrote |
| `trace.jsonl` | Everything that happened, one event per line, in order |
| `score.json` | The grader's output, or "not graded" |

Two optional sub-folders: `outputs/` for the stage outputs or the output document, `grading/` for anything a marker used that is not the integrity score (a sealed key, its marking). A short `notes.md` for provenance is allowed. Nothing else.

The files are plain structured text. A program reads them without guessing; a person reads them in any text editor.

---

## What each file must contain

### `meta.json`

| Field | Meaning | If unknown |
|---|---|---|
| `record_version` | 1 | — |
| `run_id` | the folder name | — |
| `source` | `forge-app` or `vault` | — |
| `venture` | the working name | — |
| `date` | when the run began | date only, with `time_known: false` |
| `status` | `active` or `finished` | — |
| `model`, `effort` | the model and effort setting | `absent — not recorded` |
| `entry_path` | `incumbent`, `concept`, or a sentence for a vault run | — |
| `stages_in_order`, `stages_reached`, `stage_status` | the stage list, which were reached, and each one's state: `closed`, `blocked`, `open`, `not reached` | — |
| `turns` | model turns in room one | `absent` |
| `cost` | dollars as measured, pounds as converted, the rate and whether it is assumed, tokens in four parts, web searches, model calls | `absent` |
| `person` | who ran it (the service keeps email, name and invite code) | a sentence |
| `harness` | the version mark and the code fingerprint, repeated from `harness.json` for quick reading | — |
| `trace.complete` and `trace.absent` | whether the trace holds everything, and a list of what it lacks | must be present |
| `qualification_class` | `held_out_autonomous` or `iterative_design_case` — see the block below | must be present; absent reads as `iterative_design_case` |
| `completion_state` | `COMPLETE_VERIFIED` or `INCOMPLETE` — see the block below | must be present; absent reads as `INCOMPLETE` |
| `qualification` | the three supporting facts: the input fingerprint, the no-edit attestation, the verifier's identity | must be present when the class is `held_out_autonomous` |
| `evidence` | `fit_record` (present, current against the component set, path) and `required_external` (each named validation event with `present: true/false`) — the two clauses of `completion_state` the stage list cannot show | must be present; an absent FIT record or any `present: false` forces `INCOMPLETE` |
| `exported_at` | when the files were written | — |

### The qualification block (version 2 — Tom's ruling, 21 September 2026)

Every record labels itself before its score is read. Two fields, both mandatory, and a block of three supporting facts.

**`qualification_class`.** One of two values.

| Value | Meaning | Counts toward the WS1 objective |
|---|---|---|
| `held_out_autonomous` | The venture was not used to build or fix the method; the method ran end to end with no person editing the architecture between start and output; the score was written by a grader that did not run the challenges | Yes, when `completion_state` is `COMPLETE_VERIFIED` and the three supporting facts are present |
| `iterative_design_case` | Anything else: a run with a person directing it, a run on a venture the method was tuned on, a run re-entered on a correction, a record built up across sessions | Never. It may improve the method; it cannot advance the three-run count |

A run with a tester or an insider in the conversation is `iterative_design_case`, whatever the venture. The Forge application supplies inputs; the scored run is a separate clean run on those inputs (README, 4 September). A run that cannot say which it is, is `iterative_design_case`.

**`completion_state`.** One of two values. The tool reads it from four places — `stage_status`, `score.json`, `evidence.fit_record` and `evidence.required_external` — and a record that is complete as an architecture but has a named validation event outstanding is `INCOMPLETE` for WS1 while its architecture is reported complete: the two states render separately (Tom, 21 September, §9). `INCOMPLETE` is compulsory whenever any one of these holds:

- any challenge C1–C10 is OPEN, PARTIAL or PROVISIONAL, or was not reached;
- no independent FIT record exists against the current component set, or the one that exists is stale (VA-74, VA-90);
- a structural gate is active in `score.json` (justification mode or parts-bin);
- a required external evidence record is absent — a validation event named in the record has not happened;
- the grader's verdict band is anything other than SOUND with no gap listed.

`COMPLETE_VERIFIED` means every C1–C10 requirement is independently verified against the current component set with no exception of any of the five kinds. "SOUND WITH GAPS" is `INCOMPLETE`, whatever the number beside it.

**An integrity score is diagnostic only.** It says where a record is weak. It never says a record is done. The objective's count is over records that are `held_out_autonomous` and `COMPLETE_VERIFIED`; the score threshold (≥ 85, both gates clear) is applied only inside that set.

**`qualification`, the supporting facts.** A `held_out_autonomous` record that lacks any of these is read as `iterative_design_case` by the tool.

| Field | What it holds |
|---|---|
| `source_input_fingerprint` | A fingerprint over `inputs.json` as it stood before the run began, so a reader can tell the inputs were fixed first and not written to fit the output |
| `no_edit_attestation` | `{ "attested": true/false, "by": who, "statement": one sentence }` — the person or seat that watched the run states that no person edited the architecture between start and output. `false` or absent forces `iterative_design_case` |
| `verifier_identity` | `{ "seat": which seat ran the grader, "independent_of_runner": true/false, "report_path": the grader's report }`. The seat that ran the challenges may not be the seat that graded them. `false` or absent forces `iterative_design_case` |

The tool (`runs.py qualify`) applies these rules mechanically and prints, for every record, the class it was labelled with, the class the tool reads it as, and the reason where they differ. A record cannot count toward the objective by labelling alone.

**Why this exists.** On 21 September 2026 an independent verifier returned "SOUND WITH GAPS, 60/100" on the SDG institution record, and a corrected pass the same day returned "SOUND, 100/100". Neither is a WS1 result: the record was built with a person directing it over several sessions. Without a field that says so, a future table would list the 100 beside the objective's threshold and read it as progress. Tom's correction: the WS1 done condition is a complete architecture, independently verified, with no structural-gate or evidence-gap exception — and the case is recorded as unresolved until its C2, C3, current-FIT and WQ blockers are closed. This block is the enforcement point for that ruling (VA-100: a rule with no enforcement point is a wish).

**The cost in pounds.** FACT: the service measures cost in US dollars, from the model's own token counts and the price table in `lib/anthropic.js`. ASSUMPTION ⚠: the pounds figure uses a rate of **0.79 pounds per dollar**, the figure the operating notes already use ("190 USD is about 150 GBP"). The record prints the rate and marks it assumed, so nobody reads the pounds as measured.

### `harness.json`

The harness is the code that decides what the model stores, retrieves and sees. Two things identify a version:

1. **The version mark.** FACT: the hosting service publishes the version it deployed as `RAILWAY_GIT_COMMIT_SHA`; a machine with the source asks the version control tool. A vault run names the vault's version mark for the skill files instead.
2. **A fingerprint of the code.** One fingerprint over the server and every module, so two copies with the same mark have the same fingerprint and a local edit changes it. This is what identifies a version when no mark exists.

Then, for every method file the run used: its fingerprint, its length in lines, and the vault file it copies. Where it copies nothing the entry says `null`; `frame.md` was written for the service and has no vault source yet. FACT: the service already hashes its copies against the vault in `scripts/check-method-copies.mjs`; the record carries the same fingerprints.

Three more things. A fingerprint of each stage's full system prompt (the preamble plus the method file), so a change in the preamble shows even when the method file did not move. The reference set as a list of file names and fingerprints, never its text. And the settings that shape a run: model, effort, entry path, attempt cap, turn budget, web search on or off, offline mode.

**Where a version is inferred, say so.** The Datum record names vault version `c0fbdc1b` for its three skill files with `vault_commit_inferred: true` and the reasoning written beside it. A reader must be able to tell a recorded version from a reconstructed one.

### `inputs.json`

The starting inputs, and nothing the assistant wrote. On the service: the website, the text read from it, and every entry the person typed, with its stage and time — the same set the console's "held-out inputs" download already produces. For a vault run: the files read, each with its fingerprint; the files the run was forbidden; the starting figures as the run recorded them. Any instruction given mid-run goes here too. A mid-run instruction is an input the run did not start with.

### `trace.jsonl`

One event per line, numbered in order. Each event has `seq`, `at`, `kind`, and usually `stage` and `room`. The kinds:

| Kind | What it is |
|---|---|
| `state` | a stage entered, the run finished, a function gate read |
| `system` | the system prompt for a stage: its fingerprint and length, not its text |
| `prompt` | a message into room one: the opener, an entry the person wrote |
| `reply` | room one's reply, with flags for a stage it closed or blocked |
| `usage` | one model call's tokens and cost, with the room it served |
| `gate` | room two's verdict: pass, provisional, fail, or held; the flaws with their rule numbers; the alternatives |
| `refused` | a finding the checker refused, with its reasons and the refused text |
| `finding_shown` | the finding as the person read it |
| `close` | the message that closed a stage at the attempt cap |
| `feedback`, `interest` | what the person said at the stage close and the run close, including the build answer |
| `intervention` | for vault runs: an instruction given while the run was in flight |

**What the trace does not hold today, stated in every record.** FACT, from the service's tables: room two's prompt and its raw reply are not stored — only the parsed finding and any refused version. Web searches inside a model call are counted per call, not listed. The text of the room-one system prompt is reproducible from the method files, so it is fingerprinted rather than copied. Each record lists these under `trace.absent` so a reader is not misled. INFERENCE: closing the first gap means storing room two's raw exchange. That is a change to what the service keeps, not to this standard. It is left for a later decision because the raw reply can carry reference text.

### `score.json`

The grader's output, and only the grader writes it. FACT: `/verify-venture-custom` produces an overall score, four sub-scores (completeness, consistency, discipline, synthesis), two structural gates (justification mode, parts-bin), a verdict band and a validation-maturity readout. The file carries each of those by name, plus `graded_at` and the path of the grader's report.

Before grading, the file is present with `graded: false` and every field `null`. A null is not a zero. An export never overwrites a `score.json` that already exists, because the grader owns it.

A vault run marked some other way — the Datum run was marked against a sealed answer key — keeps that marking in `grading/marking.json`, and `score.json` still says `graded: false`. A sealed-key marking is a finding about the rules; it is not an integrity score, and the two must not be confused in a table.

---

## The small tool

FACT, on disk: `WS1/runs/runs.py`. Standard library only. Five commands:

```
python3 runs.py list [--sort score|date|cost] [--graded]
python3 runs.py show <run-id>
python3 runs.py diff <run-id-a> <run-id-b>
python3 runs.py best [n]
python3 runs.py qualify
```

`list` prints one row per run: date, source, harness id, stages reached, class, state, score, cost in pounds. A `?` after a harness id means the version was inferred. `diff` puts two runs side by side: every score field with its change, the version marks, each method file's fingerprint lined up by the vault file it copies, every setting that differs, and the run facts. `best` lists the highest-scoring graded runs and marks each as diagnostic. `qualify` is the objective's counter: it reads every record, applies the qualification block's rules, prints the class each record is labelled with and the class it is read as, and counts only the records that are `held_out_autonomous`, `COMPLETE_VERIFIED`, graded at or above the threshold with both gates clear, and carry all three supporting facts. It exits non-zero when any record's label and reading differ, so a mislabelled record is a failure, not a footnote. A field a record marks absent prints as `absent` and is never counted as zero.

The tool reads the version-1 `score.json` shape (`overall`, `completeness`, …) and the shape one 16 September record used (`integrity_score`, `sub_scores`). The second is a deviation from this standard, tolerated in reading and not to be repeated in writing.

---

## What was built today and where

| Item | Where | Checked |
|---|---|---|
| The record writer in the service | `~/dev/forge-app`, branch `run-records`, `lib/record.js` | 131 of 131 offline checks pass; 39 of them are new and cover the record |
| The console route that returns a record | `/api/admin/runs/<id>/record`, and `/api/admin/harness` | in the check suite |
| The export script | `scripts/export-run-record.mjs` | run against a local offline service; the exported folder matched the one written as the run went, apart from the export time |
| Writing as the run goes | `RUN_RECORDS_DIR` | in the check suite: written after every turn, gate, advance, feedback and close answer; an existing `score.json` kept |
| The Datum blind re-run as a record | `WS1/runs/2026-09-04_datum_blind-c1-c3/` | listed and shown by the tool |
| The tool | `WS1/runs/runs.py` | list, show, diff and best exercised on two records |
| Version 2 (21 Sep 2026): the qualification block, the `evidence` block, `runs.py qualify`, class and state columns in `list`, the "counts / diagnostic only" tag in `best` | `WS1/runs/runs.py`, the three version-1 records relabelled, the SDG case converted as `runs/2026-09-21_sdg-institution_iterative-c2-c10` | `qualify` walked on four records (all four labels match the reading; objective 0 of 3); a relabelled copy of the SDG record fails with two label differences; regression check R-W27 |

The branch is not pushed, not merged and not deployed. The working copy was found on `main`, clean, at `c31a329`, and is left on `run-records` at `321d070`.

---

## What the Datum record shows about converting old runs

FACT. The 4 September blind re-run left one output document, one sealed key, and a marking in the feedback log. It did not leave a transcript, a model name, a token count or a cost. The converted record says `absent` in each of those places rather than filling them. Its trace has eight events — three gate verdicts, three state changes, the mid-run instruction and the function-gate reading — each with the line of the output document it comes from.

INFERENCE. This is the cheapest conversion there is, and it still took the version of the rules file the run read out of reach: that file is not under version control and has changed since. Old runs can be converted to the layout; they cannot be given what was never kept. The standard exists so the next run keeps it.

---

## Open, and whose

- Storing room two's raw exchange, so the trace is complete — a change to what the service keeps. Head of Product to propose; the leak check on that text is the reason to pause.
- **The three supporting facts are only as good as the moment they are taken.** A fingerprint over `inputs.json` computed after the run (as the four converted records carry today, each saying so) shows the inputs as they stand, not that they were fixed first. The next held-out run takes the fingerprint before the first challenge opens and writes the time beside it. The run-zero prompt (Mode D) must say so.
- A run in the vault does not write its own record yet. The challenge skills would need a closing step that writes the five files. That is a skill change, so it goes through the Head of R&D. Until then a vault run is converted by hand, as Datum was.
- The exchange rate ⚠ 0.79. Replace with a measured rate when the first paid invoice gives one.
