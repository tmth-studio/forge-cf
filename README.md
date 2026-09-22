# Forge — venture architecture method

This folder turns Claude Code into a venture architect. You describe a business
concept; the method takes it through a fixed sequence of design steps, scores it
at each gate, and tells you where it fails.

It is not a brainstorming tool. It is a process with pass and fail marks.

**Version 2 — 22 September 2026.** Built from the studio's working copy of the
method on that date. `PROVENANCE.md` lists every file with its digest. Version 1
was a hand-made copy of 3 September 2026; this version is built by a script, so
the next one will be too.

---

## Setup — about two minutes

1. Install Claude Code if you do not have it: https://claude.com/claude-code
2. Install the one Python package the model tools need:

```bash
pip3 install pyyaml
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

### What the sequence does

| Phase | What happens |
|-------|--------------|
| PCO | Sets the widest credible commercial opportunity, before any product or segment choice |
| R1–R3 | Cost floor, customer value ceiling, and whether it scales — the arithmetic gates |
| R4–R7 | Why people would want it, use it, pay for it, and who controls access to them |
| R8–R10 | Switching costs, resource moat, supplier leverage |
| Verify | Cross-checks all ten for contradictions, then scores the whole architecture |

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
.claude/skills/         the 29 method skills, plus shared diagram, model and checking tools
04-Projects/TMTH_Venture_Studio/Forge/WS1/
                        the process flow, the gate criteria, the glossary, the standards,
                        and the feedback log the skills write to
04-Projects/Family_High_Performance/context/va-design-discipline.md
                        the register of design rules the skills cite by number (VA-nn)
ventures/               your work goes here, one folder per concept
PROVENANCE.md           what this copy was built from, file by file
FEEDBACK.md             where to put what you found
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

## Please log the friction

This is the method running outside its own workshop. Every point where a step
was unclear, a gate felt arbitrary, or the output needed interpretation is worth
more than a compliment.

Some skills will ask you four questions at the end of a session and write your
answers to `04-Projects/TMTH_Venture_Studio/Forge/WS1/ws1-feedback-log.md`. Say
yes when they ask. Add anything else there yourself, in the same format. Then
send us the file, or open a pull request with it.

---

## Terms

This method is the work of Tough Minds, Tender Hearts. It is public so that
other people can run it and improve it through their runs. You may use it,
run it and share it. Keep this notice and the attribution below with any copy.
Tough Minds, Tender Hearts keeps ownership of the method.

The method rests on a body of published work led by Erik Simanis at Cornell,
written with co-authors 2021–2025. The skills name the sources they draw on.
