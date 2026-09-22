# Forge — design a venture-scale company, free

Describe a business idea, or name a company you want to beat. Forge designs the
venture that could reach scale, scores the design at ten gates, and hands you a
business case document and a live financial workbook you can take into your own
company or a funding conversation.

It runs inside Claude Code on your own machine. The method is free and stays
free. You pay only for your own Claude usage.

**What "venture-scale" means here.** A company whose cost to serve sits below
what customers will pay, at the volume the opportunity supports, with a way to
reach that volume without running out of cash. Those three conditions are the
first three gates. A design that fails one of them is stopped there and told why.

**Why this and not a pitch deck.** A deck states a plan. A spreadsheet with an
assumed growth rate states a hope. Forge builds the design requirement by
requirement, refuses to move on when a requirement fails its gate, and every
figure in the final document traces to a named cell in the workbook. You finish
with a design that has been tested, or a clear account of where it broke.

**Where it comes from.** This is the studio's own working method, built from its
files by script on 22 September 2026 (`PROVENANCE.md` lists every file with its
digest). It rests on a body of published work led by Erik Simanis at Cornell,
written with co-authors 2021–2025. The skills name the sources they draw on.

---

## What you get

At the end of a run, two files:

- **A business case document** in the seven sections of the GOV.UK *Write a
  business plan* template. Every figure in it is a named cell in the workbook.
- **An Excel evidence workbook** laid out the way the IFC bottom-up method
  (Simanis, *Running the Right Numbers*) prescribes. Twelve tabs: the sales and
  twelve-month cash-flow sheets of the same template, with a 10 per cent revenue
  stress test; the three forecast financial statements by year (profit and loss,
  cash flow, balance sheet, five years by default); and a Check tab that proves
  the workbook arrived whole. The workbook is live formulas. Change a blue cell
  and everything moves.

And behind them, the design itself: ten requirements, each with its diagnosis,
its strategy, its simulation and its pass or fail, plus a cross-check of all ten
for contradictions and a score for the whole.

A worked example is in `.claude/skills/ive-business-case-custom/reference/`.

---

## Setup — about two minutes

1. Install Claude Code if you do not have it: https://claude.com/claude-code
2. Install the three Python packages the model tools need:

```bash
pip3 install pyyaml openpyxl formulas
```

3. Open a terminal in this folder and start Claude Code:

```bash
cd ~/forge-cf && claude
```

That is the whole setup. The skills live in `.claude/skills/` and Claude Code
loads them automatically for any session started inside this folder.

Type `/` to see them listed. If they do not appear, you are running Claude Code
from a different folder.

Python 3.9 or later is needed for the diagram, model and checking tools. Check
with `python3 --version`.

---

## Running a concept

Copy `ventures/_template/` to `ventures/<your-concept-name>/`, then start here,
every time:

```
/architect-custom my-concept-name
```

That skill is the front door. It reads what already exists, works out where the
venture sits in the sequence, and routes you to the right next step. Do not start
with one of the other skills — the sequence matters and the front door enforces it.

**Starting from an idea.** Describe it in your first message. The run opens by
finding the widest commercial opportunity the idea could serve, before any
product or segment choice, and works forward from there.

**Starting from a business you want to beat.** Say so in your first message: "I
want to disrupt [business]". The run takes that business as the conventional form
at challenge one and researches the rest itself — the line, the job it does, who
buys it and at what price. Name one line of one company where you can; if you
name a whole company, the run takes its largest line and tells you.

### What the sequence does

| Phase | What happens |
|-------|--------------|
| PCO | Sets the widest credible commercial opportunity, before any product or segment choice |
| R1–R3 | Cost floor, customer value ceiling, and whether it scales — the arithmetic gates |
| R4–R7 | Why people would want it, use it, pay for it, and who controls access to them |
| R8–R10 | Switching costs, resource moat, supplier leverage |
| Verify | Cross-checks all ten for contradictions, then scores the whole architecture |
| Business case | Writes the business case document and builds the evidence workbook from one model data file |

Each of the ten requirements runs the same loop: diagnose, theorise, productise,
simulate. A requirement is finished only when it passes its gate. The method will
refuse to move you forward on a fail, and that refusal is the point.

### Vocabulary

Every term the method uses is defined in
`04-Projects/TMTH_Venture_Studio/Forge/WS1/glossary.md`. Read it when a word does
not land. The referee for every gate is `criteria-registry.md` in the same folder.

---

## What is in here

```
.claude/skills/         the 30 method skills, plus shared diagram, model and checking tools
04-Projects/TMTH_Venture_Studio/Forge/WS1/
                        the process flow, the gate criteria, the glossary, the standards,
                        and the feedback log the skills write to
04-Projects/Family_High_Performance/context/va-design-discipline.md
                        the register of design rules the skills cite by number (VA-nn)
ventures/               your work goes here, one folder per concept
PROVENANCE.md           what this copy was built from, file by file
FEEDBACK.md             where to put what you found, if you want to
```

The long folder path is deliberate. The skills cite the method files by that path,
and the checking tools read their integrity manifest from it. Do not move it.

### The checking tools

`.claude/skills/shared/generators/` holds the scripts that check a model file,
compute the margin of safety and confirm the verdicts are in order. Each one
verifies itself and its siblings against a manifest of digests before it runs,
and refuses if any script has been edited. This is intended: a run should not be
able to change the tool that grades it. If you need to change a script, tell us
what and why, and we will issue a new version.

---

## If something did not work

You do not owe us anything for using this. If you want to help, the most useful
thing is a note of where a step was unclear, a gate felt arbitrary, or the output
needed interpretation.

Some skills ask four questions at the end of a session and write your answers to
`04-Projects/TMTH_Venture_Studio/Forge/WS1/ws1-feedback-log.md`. Say yes if you
are willing. Add anything else there in the same format, then send us the file or
open a pull request with it.

---

## Terms

This method is the work of Tough Minds, Tender Hearts. It is public so that
other people can run it and improve it through their runs. You may use it,
run it and share it. Keep this notice and the attribution below with any copy.
Tough Minds, Tender Hearts keeps ownership of the method.

The method rests on a body of published work led by Erik Simanis at Cornell,
written with co-authors 2021–2025. The skills name the sources they draw on.
