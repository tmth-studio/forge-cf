# IVE Model Routing — Execution Economics Standard

**Status:** Operative default for all IVE/BALM skill runs. Set by Studio Director on Tom's instruction, 1 September 2026.
**Class:** Toolchain execution standard — NOT a change to the CF method. The strict folding rule does not bite (same class as `landing-page-standard.md`: governs how the CF is *run*, not what it *does*).

---

## Why this exists (measured, 1 Sep 2026)

A full fresh architecting run (PCO → R1–R10 → audits/FIT → model stack → write-up) costs **~25–35M tokens**, measured from 94 real session transcripts (input + cache-write + output). Against a weekly frontier-model (Fable) allowance of ~25M, that is 100–140% — one venture consumes the whole week's frontier budget. Continuing to CDR ≈ ~60M ≈ 2.5 weeks.

The token spend is not uniform in judgment content. Adversarial and gate work needs the strongest model; document and model *production* does not. Routing production to a cheaper tier cuts the frontier-model share of an architecting run to roughly 10–15M (~half a week).

---

## The routing table

| Tier | What runs there | Skills / stages |
|---|---|---|
| **Session default (strongest model — Fable or whatever Tom is running)** | Contested reasoning, adversarial verification, gate verdicts, generative synthesis | `balm-pco-custom`, `balm-challenge-1..10-custom`, `ive-consistency-audit-custom`, `ive-fit-verifier-custom`, `ive-design-loop-custom`, `ive-architecture-generator-custom`, `ive-detailed-design-custom` gate decisions, `verify-venture-custom`, `head-of-verification-calmly-custom` |
| **Opus subagent (production tier)** | Bulk document/model production once inputs are settled | Production stages of `ive-fin-sim-custom`, `ive-writeup-custom`, `ive-valuation-custom`, `ive-wiki-entry-custom`; mechanical sweeps inside any skill (HTML rendering, diagram generation, formatting passes, file assembly) |

No stage routes to Haiku by default — the quality floor there is unverified for IVE material. Candidate for later: wiki-entry rendering, only after a clean side-by-side check.

---

## The dispatch pattern

The split is **within** a skill, not between skills:

1. **In-session (default model):** everything that gathers or judges — the interview steps, input confirmation, methodology decisions, verdicts on what the numbers mean.
2. **Dispatched (opus):** the production step — generating the HTML model, the write-up prose, the valuation document. Dispatch via the Agent tool with `model: "opus"` and a **self-contained prompt**: all confirmed inputs, the output file path, and the relevant design/format spec pasted or referenced by absolute path. The subagent must not need the session's conversation history.
3. **Back in-session:** verify the produced artefact (read it, check the numbers that carry the argument), then continue.

**Override:** if Tom says "run inline" (or the production step is trivially small, under ~2k words of output), skip the dispatch and produce in-session.

**Do not** use skill frontmatter `model:` fields for this — support is unverified in this harness and a silent no-op would defeat the routing. Instruction-level dispatch via the Agent tool is the mechanism.

---

## Record

Measurement and rationale: Studio Director memory, session log 2026-09-01. Forge-relevance (execution cost per architecture feeds Forge's own unit economics / R1 at-scale cost): noted in `04-Projects/TMTH_Venture_Studio/Forge/WS1/forge-cf-development-backlog.md`.
