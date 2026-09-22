# Forge — instructions for the agent

This repository is a venture design method, not a codebase. The person you are
working with wants to design a venture-scale company. Your job is to run the
method as written, in order, and to stop where it says stop.

## Where the method lives

The skills are in `.claude/skills/<name>/SKILL.md`. Each is a set of
instructions with `name` and `description` at the top, in the Agent Skills
format. `.agents/skills` points at the same folder for tools that read that
path.

A name written as `/something-custom` anywhere in this repository refers to
`.claude/skills/something-custom/SKILL.md`. When a skill routes you to another
skill by that name, open that file and follow it. Do not guess at what it says.

## How to start

Always begin with the front door:

```
.claude/skills/architect-custom/SKILL.md
```

It reads what already exists in the venture folder, works out where the venture
sits in the sequence, and routes to the next step. Do not open a challenge skill
on your own initiative because its description matches the task. The sequence
matters and the front door enforces it.

A venture lives in `ventures/<concept-name>/`. Copy `ventures/_template/` to
start one. The person will say which one they are working on, or name a
business to beat, or describe an idea.

## Where the reference files are

- `04-Projects/TMTH_Venture_Studio/Forge/WS1/` — the gate criteria
  (`criteria-registry.md`), the glossary, the standards and the feedback log
- `04-Projects/Family_High_Performance/context/va-design-discipline.md` — the
  design rules the skills cite by number (VA-nn)
- `.claude/skills/shared/` — diagram and model specifications, and the checking
  scripts in `generators/`

The skills cite these by that exact path. Do not move them.

## If your tool differs from the one the skills assume

The skills were written for an agent that has a terminal, can read and write
files, and can run Python 3.9 or later. Some lines assume more than that. Apply
these rules:

- **A skill says to dispatch a step to a subagent, or to use the Agent tool.**
  If your tool has no such thing, do that step yourself in the same session.
  The routing note (`.claude/skills/shared/ive-model-routing.md`) is a cost
  saving, not a requirement of the method.
- **A skill names a model tier** (Opus, Fable, Haiku). Use the model you have.
- **A skill refers to a slash command.** Read the skill file at the path above.
- **A skill refers to a file that is not in this repository** (a path under
  `/Users/`, `Desktop/` or `Downloads/`). It is a source citation from the
  studio's own machine. Do not stop for it; the method text in the skill is
  complete without it.
- **A skill asks a question and waits.** Ask the person and wait. Do not answer
  on their behalf.

## What you must not do

- Do not edit the checking scripts in `.claude/skills/shared/generators/` or the
  files under `04-Projects/`. The scripts verify their own digests and refuse to
  run if changed. A run must not be able to change the tool that grades it.
- Do not move a venture past a gate it has failed. A fail is a result. Report it
  and stop.
- Do not create the venture's output files by hand. The method makes them.
