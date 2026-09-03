# Forge — venture architecture method

This folder turns Claude Code into a venture architect. You describe a business
concept; the method takes it through a fixed sequence of design steps, scores it
at each gate, and tells you where it fails.

It is not a brainstorming tool. It is a process with pass and fail marks.

---

## Setup — about two minutes

1. Install Claude Code if you do not have it: https://claude.com/claude-code
2. Open a terminal in this folder and start Claude Code:

```bash
cd ~/forge-cf && claude
```

That is the whole setup. The skills live in `.claude/skills/` and Claude Code
loads them automatically for any session started inside this folder.

Type `/` to see them listed. If they do not appear, you are running Claude Code
from a different folder.

**Python is needed for the diagram and model tools.** Check with `python3 --version`.
Anything from 3.9 up works.

---

## Running a concept

Start here, every time:

```
/architect-custom my-concept-name
```

That skill is the front door. It reads what already exists, works out where the
venture sits in the sequence, and routes you to the right next step. Do not start
with one of the other skills — the sequence matters and the front door enforces it.

Your work is saved under `ventures/<your-concept-name>/`. Create that folder first,
or let the first session create it.

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

Every term the method uses is defined in `method/glossary.md`. Read it when a word
does not land. The referee for every gate is `method/criteria-registry.md`.

---

## What is in here

```
.claude/skills/     the 28 method skills, plus shared diagram and model tools
method/             the process flow, the gate criteria, the glossary, the standards
ventures/           your work goes here, one folder per concept
FEEDBACK.md         where friction gets logged — see below
```

---

## Please log the friction

This is the first time the method has run outside its own workshop. Every point
where a step was unclear, a gate felt arbitrary, or the output needed
interpretation is worth more than a compliment.

Some skills will ask you four questions at the end of a session and write your
answers to `FEEDBACK.md`. Say yes when they ask. Add anything else there yourself.

---

## Terms

This method is unpublished work by Tough Minds, Tender Hearts. It is shared with
you for our joint review of a concept. Please do not redistribute it or use it for
other commercial work without asking first.
