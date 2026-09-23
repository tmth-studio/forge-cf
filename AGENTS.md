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

## First run — do the setup for the person

Many people arrive here by pasting a prompt such as "Set up Forge from
https://github.com/tmth-studio/forge-cf and help me start my first venture."
Assume they do not use a terminal. Do every setup step yourself, tell them in
one plain sentence what you are doing, and ask them for nothing except their
idea.

1. **Get the files.** If you are not already inside this repository, clone it
   into a new folder called `forge` and work from there. If `git` is missing,
   download the ZIP of the `main` branch from the same address and unpack it.
2. **Check Python.** Run `python3 --version` (on Windows, `py --version`).
   Version 3.9 or later is needed. If it is missing or too old, tell the
   person in one sentence and give them the one install link for their
   system, then continue once they say it is done.
3. **Install the three packages.** Run `python3 -m pip install --user pyyaml
   openpyxl formulas`. If the system refuses (an "externally managed
   environment" error), make a virtual environment in `.venv` inside the
   repository, install there, and use that Python for every later script.
4. **Windows only.** If `.agents/skills` is a plain file, not a link, replace
   it with a copy of `.claude/skills`.
5. **Make the venture folder.** If the person has already described their
   idea, derive a short lowercase concept name from it (two to four words,
   joined by hyphens) and copy `ventures/_template/` to
   `ventures/<concept-name>/`. If they have not, ask for the idea in one
   question — a sentence is enough, or the name of a business they want to
   beat — then make the folder.
6. **Start the method.** Open the front door below with that concept name and
   the person's own words as the opening description. Do not summarise the
   setup at length; one line saying it is done is enough.

If the person pasted the prompt into a chat that cannot run commands or write
files, say so plainly: Forge needs an agent that works on files, such as
Claude Code, Codex, Cursor or GitHub Copilot in agent mode. Do not try to run
the method inside the chat.

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
