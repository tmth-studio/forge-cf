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

Many people arrive here by pasting a prompt such as "Set up Forge by following
https://github.com/tmth-studio/forge-cf/blob/main/AGENTS.md and help me start
my first venture." Assume they do not use a terminal. Do every routine step
yourself and say in one plain sentence what you are doing. Ask before anything
that installs software on the computer itself. Ask the person for nothing else
except their idea.

1. **Get the files.** If you are already inside this repository, stay here.
   Otherwise put Forge in the person's Documents folder as `Forge`. If
   `Documents/Forge` is already this repository, update it with
   `git pull --ff-only` rather than making a second copy. If it exists and is
   something else, stop and ask where to put Forge. If `git` is missing,
   download the ZIP of the `main` branch and unpack it there.
2. **Check Python.** Run `python3 --version` (on Windows, `py --version`).
   Version 3.9 or later is needed. If it is missing or too old, ask before
   installing it: on a Mac, the installer from python.org, or `brew install
   python@3.12` if Homebrew is already there; on Windows,
   `winget install --id Python.Python.3.12 --exact`. Reopen the terminal
   afterwards so the new Python is found.
3. **Install the three packages into Forge's own environment.** Make a virtual
   environment in `.venv` inside the Forge folder, install `pyyaml openpyxl
   formulas` into it, and use that Python for every script in the run. This
   leaves the rest of the computer untouched and avoids the "externally
   managed environment" refusal.
4. **Windows only.** If `.agents/skills` is a plain file, not a link, replace
   it with a copy of `.claude/skills`.
5. **Check the setup worked.** Do not report success because a command ended
   without an error. All three of these must hold:
   - `.venv` Python can import `yaml`, `openpyxl` and `formulas`
   - `.venv` Python running `.claude/skills/shared/generators/toolchain_guard.py verify`
     prints `VERDICT: PASS`
   - the venture folder from step 6 exists
   If one fails, read the error, fix that one thing and check again. Do not
   work around it.
6. **Make the venture folder.** If the person has already described their
   idea, derive a short lowercase concept name from it (two to four words,
   joined by hyphens) and copy `ventures/_template/` to
   `ventures/<concept-name>/`. If they have not — the standard prompt carries no idea, or they said "hi" or nothing
   about an idea — introduce Forge in two sentences and ask for the idea in one
   question. A sentence is enough, or the name of a business they want to
   beat.
7. **Start the method.** Open the front door below with that concept name and
   the person's own words as the opening description. One line saying setup is
   done is enough; do not summarise it.

Running these steps a second time must be safe. It should repair or resume an
existing setup, never make a second one.

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
