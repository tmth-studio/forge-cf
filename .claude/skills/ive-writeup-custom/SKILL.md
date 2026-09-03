---
name: ive-writeup-custom
description: Produce the venture's public-facing explainer — a write-up of what the venture is and does, in the style of The Economist. Complex architecture made simple and lucid, with ranged quantitative evidence woven into the prose. Runs over the full CDR, or after any single challenge — scoping its depth to whatever architecture exists so far.
---

# IVE Write-up — The Economist Brief

**Model routing (mandatory default):** per `.claude/skills/shared/ive-model-routing.md` — scope and judge in-session; dispatch the drafting/production step to an Agent-tool subagent with `model: "opus"` and a self-contained prompt (architecture sources by absolute path, output path, this skill's craft rules). Verify the draft in-session. Skip only if Tom says "run inline".

**Purpose:** Produce the thing you hand someone to make them *understand the business in five minutes*. Not a pitch deck, not a model, not a requirements list — an essay in the register of The Economist that takes the venture's architecture and renders it as a clear, honest, lightly wry argument: here is the puzzle, here is the insight that solves it, here is how it makes money, here is what is still a bet.

**When to run:** At the END of the architecting process, over the full CDR (R1–R10). But it MUST also be runnable after ANY single challenge — adapting its depth to whatever architecture exists so far. After R1 it explains the cost-floor insight; after R7 it can tell the whole demand-and-access story; after R10 it is the complete venture explainer.

**Output:** A single-file HTML brief in the house design system — headline + italic standfirst + 4–6 short sections of flowing argument, ranged quant woven inline, an understated honest close. Saved to the venture folder, opened in the browser.

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: Simanis, E. et al. (2021), Cornell SC Johnson College of Business.

**Three nested levels of commercial architecture:**

| Level | What it is |
|-------|-----------|
| **Core Business Architecture (CBA)** | The logic that sets both the cost curve and value curve for an industry. No single company owns it. |
| **Business Form Factor (BFF)** | The essential shape product and operations take given a CBA. The default way the product is made, sold, delivered, and paid for. |
| **Business Model** | A company's unique strategy for outcompeting others within a shared BFF. |

**The full sequence:**

```
PCO — Prime Commercial Opportunity (scope-setter; runs before all requirements)
│
├── F1 — Neutralise the Value Barrier
│   ├── R1: Circumvent At-scale Cost Bottleneck       [P&L — sets the cost floor]
│   ├── R2: Eliminate Customers' Value Bottleneck      [value ceiling — what customers pay]
│   └── R3: Circumvent Scaling Cost Bottleneck         [balance sheet — working capital at scale]
│
├── F2 — Normalise the Customer Routine
│   ├── R4: Circumvent Customer Doubt about Value
│   ├── R5: Eliminate the Biggest Learning Disruption
│   ├── R6: Circumvent the Cash Flow Constraint
│   └── R7: Activate Gateway Partners
│
└── F3 — Lock In the Market Position
    ├── R8: Create a Switching Cost
    ├── R9: Manufacture a Resource Moat
    └── R10: Manufacture Replaceability of the Key Supplier Input
```

**→ This skill: IVE Write-up** — runs after the CDR is complete (or after any single challenge), downstream of all design and verification. It does not design anything. It reads the finished (or partial) architecture and explains it. Its sibling is `/ive-valuation-custom` (which prices the same architecture); together they are the two outward-facing artefacts the architecture produces.

**Design principle — explain at the level the reader needs, not the level you built at.** The architecture was built at-scale and in technical IVE language (CLO, FMOS, BFF, ARM). The write-up translates. The reader does not need the vocabulary — they need the *idea*. A good write-up could be read by an intelligent person with no exposure to IVE and leave them able to explain the business to someone else.

---

## The Economist register — reproduce this precisely on every run

The voice is the point of this skill. Any run must reproduce it. The rules:

1. **Lead with a puzzle or tension, not a description.** Open on the thing that makes this venture interesting — usually a paradox, a market that should exist and doesn't, or a cost that should be impossible to remove. Not "X is a company that does Y." Example shape: *"Every founder is told to write a business plan. Almost none can tell whether the plan is any good. That, it turns out, is a market."*

2. **Authoritative, lucid, lightly wry.** Confident but never breathless. The reader should feel they are in the hands of someone who understands the business completely and finds it quietly interesting. No hype words — banned: *revolutionary, game-changing, disruptive, cutting-edge, world-class, unprecedented*. No exclamation marks.

3. **Mechanism through analogy.** Explain how the thing works by comparing it to something the reader already understands. The venture's own real-business analogues are gifts here — if the architecture has a VA-1 synthesis ("this looks like FICO / Zillow / an insurance float / a clearing house"), use it as the spine of the explanation. The analogy carries the mechanism so the prose does not have to grind through it.

4. **Numbers as evidence, inline.** A figure appears mid-sentence to settle a point, never bolted on as a standalone table. One or two well-chosen pull-figures maximum across the whole brief. Per VA-32 below, every figure is a *range* with its reason. Example shape: *"perhaps £10,000–50,000 a head — a tenth of what the consultants charge, a fraction of the exit value at stake."*

5. **Short declarative sentences. Plain words.** "Use" not "utilise". "Help" not "facilitate". Active voice — the subject acts. UK spelling throughout. Alternate sentence length deliberately: short for the truth, longer to unpack it.

6. **Structure is an essay, not a template.** A headline. An italic standfirst — the one-line summary directly under it. Then an argument that flows across 4–6 short sections, each opening with an *assertion* sub-head (a claim, not a label — "The cost was never the lawyers" beats "Cost structure"). It reads as one continuous argument, not a filled-in form.

7. **A restrained, understated ending.** Close on a quiet observation, not a crescendo. The strongest endings note what is still uncertain, or land a single dry line, and stop. No summary paragraph that restates everything. No call to action.

---

## Two standards baked in (from Forge WS1 backlog)

These are non-negotiable. They are what make the brief persuasive *and* honest — it earns belief by clarity, not by overclaiming.

**VA-32 — ranges, not points.** Every quantitative figure in the write-up is a *range* with a one-clause credibility reason: the anchor, why those endpoints, and what would break it. The Economist voice makes this elegant rather than clumsy — a range with its reason reads as authority, not hedging. *"perhaps £10,000–50,000 a head — a tenth of what the consultants charge"* tells the reader the number, its spread, and why it is plausible in nine words. Never a bare false-precision point ("£27,400 per customer"). A point estimate in this kind of brief signals either naivety or salesmanship; a reasoned range signals command of the uncertainty.

**VA-31 — honesty about what's proven.** The write-up must not present assumed behaviour as established fact. Where a number is something the architecture *predicts* rather than has *observed*, the prose signals it honestly — "should", "the model implies", "if the design holds", "on the architecture's own logic" — without collapsing into a hedge-fest. There is a register between false confidence and timidity: state the prediction plainly, mark it as a prediction once, and move on. The reader trusts a writer who tells them which ground is firm and which is still a bet. A brief that overclaims is found out; a brief that is honest about its bets is the more persuasive document, because the reader stops looking for the catch.

The two standards work together: VA-32 keeps the numbers honest about their precision, VA-31 keeps the claims honest about their status. Apply both on every figure and every causal claim.

---

## Field-hardened rules (v1.1 — from first runs on Forge + Calmly, 6 Jun 2026)

Apply these before and during drafting. Each fixed a real stumble on a live venture.

1. **Identify the operative architecture before drafting — write only to it.** A venture often carries superseded lineage: an earlier CDR, a unit change mid-architecture (e.g. per-claim → per-transaction), or a same-week structural decision that supersedes earlier framing. First, name the *operative* model vs the superseded lineage. When figures conflict across files, **the latest gate wins, and the SC-inclusive figure overrides the SC-excluded one.** Write to the operative model; mention lineage only as a footnote if useful.
2. **Name and neutralise flattering artefact figures — do not quote them for effect.** Excluding a cost layer (SC, or a guarantee/loss payout) produces an enormous, false-impressive margin. Surface it *as an artefact and debunk it* (this reads as authority), then quote the honest pair instead. Never let the flattering number travel alone.
3. **Red-flag rendering in long-form prose = colour only, not colour+bold** — a bold red number mid-sentence studs the prose. If a figure is *both* a range and a prediction, colour the whole token (range + units). Add one reader-orientation byline before the first red figure explaining the convention.
4. **Figure budget flexes for margin-driven ventures.** The "one or two pull-figures" rule holds everywhere *except* the single section where the margin spread *is* the thesis — there, use as many inline figures as the artefact-neutralisation (rule 2) requires. Keep the rest of the piece spare.
5. **When a venture has two strong puzzles, lead with the R1 one and use the F3 reframe as the second-act turn.** The "the customer was never who you thought" F3 reframe usually makes a stronger mid-piece pivot than a competing opener.

---

## Workflow — numbered sections

Work through these in order. Sections 1–2 are reading and diagnosis; 3–6 are the draft; 7 renders it.

### Section 1 — Inputs and scope

Read the venture's design record before writing a word.

- Read the **VDR / CDR** (the requirements record) — e.g. `ventures/{venture-slug}/...-cdr-package-{date}.html` or the VDR markdown.
- Read the **fin-sim** if one exists (`...-fin-sim-at-C[N].html`) — this is where the ranged economics come from.
- Read the **CTM / AOM** if present — for how the venture actually delivers and who does what.
- Identify **what architecture exists** — which requirements are solved (✓). This sets the scope of the write-up:
  - **After R1 only:** explain the puzzle and the cost-floor insight (the CLO and its workaround). No moat claims, no demand story.
  - **After F1 (R1–R3):** the full economics story — cost floor, value ceiling, working capital. The brief can now say what it costs, what it earns, and why the margin exists.
  - **After F2 (R4–R7):** add the demand-and-access story — why customers come, how they are reached.
  - **After F3 / full CDR:** add why it defends itself (the moat, the switching cost, the supplier story).

State the scope explicitly to yourself before drafting: *"This brief covers the architecture through R[N]. It can honestly claim X; it must not yet claim Y."*

### Section 2 — Find the puzzle

The brief opens on one tension — the thing that makes this venture interesting. Find it before writing.

The richest source is almost always **R1**: the broken boundary condition, the CLO, the cost that the conventional architecture cannot remove. That is usually a genuine puzzle — *why does this obviously valuable thing not already exist at scale?* The answer ("because the conventional way to do it costs more than anyone will pay") is the tension the whole brief resolves.

Other sources, depending on what's built:
- A market that exists on one side but not the other (a value the customer clearly wants but cannot buy affordably).
- A cost everyone treats as fixed that the workaround makes variable, or removes.
- An analogue from another industry that the reader will recognise as having solved exactly this.

Write the puzzle as a single sentence. If it does not contain a tension — something that *should* be true but isn't, or *shouldn't* be possible but is — keep looking. A description is not a puzzle.

### Section 3 — Draft the standfirst and headline

- **Headline:** short, concrete, slightly oblique. Names the venture's *idea*, not the venture. It can carry the tension.
- **Standfirst:** one italic sentence directly beneath, summarising the argument the brief will make. The reader should be able to read only the headline and standfirst and come away with the thesis. This is the brief's BLUF — it goes in the navy panel treatment if it is the single most important sentence (see Output).

Draft these now, even roughly — they discipline the argument that follows. Refine them last.

### Section 4 — Build the argument

Across 4–6 sections, in roughly this order (drop any the architecture doesn't yet support):

1. **What the venture is.** Resolve the puzzle from Section 2 by naming what the venture actually does — plainly, in one or two sentences, before any mechanism.
2. **The insight that makes it work.** The workaround / BFF — the structural move that removes the bottleneck. Explain it through the analogue (Section 3 register, rule 3). This is the heart of the brief: the reader should finish this section thinking *"oh — that's clever, and obvious in hindsight."*
3. **How it makes money.** The ranged economics, woven in (VA-32). Cost floor, the price the value supports, the margin between them. Inline, never tabled.
4. **Why it defends itself.** Only if F3 exists — the moat (R9), switching cost (R8), supplier replaceability (R10). If F3 isn't built, say nothing about defensibility, or note in one honest line that it is not yet designed.

Each section opens with an assertion sub-head. The sections connect — each picks up where the last left off. No section stands alone as a labelled box.

### Section 5 — Integrate the quant (VA-32)

Pass back over the draft. For every number:
- Is it a **range** with a one-clause reason? If it's a point, convert it.
- Is it **inline**, settling a point mid-sentence — not sitting in a table? If tabled, dissolve it into prose.
- Are there **too many**? Cut to one or two pull-figures. A brief with a number in every sentence reads like a spreadsheet with delusions; the Economist uses figures sparingly, for impact.
- Does each range's reason name the **anchor and what would break it**? (e.g. "anchored to the consultants' day-rate; breaks if the AI can't carry the analysis unsupervised.")

### Section 6 — The honest close (VA-31)

Two moves, in the understated register:
- **What's true:** what the architecture has actually established — the firm ground.
- **What's still a bet:** the load-bearing assumption the venture has not yet observed, stated plainly as a prediction the design *makes* rather than a fact it *has*. Often this is the single number from the fin-sim's pivot trigger, or the behavioural assumption the workaround depends on.

End on a quiet observation. Not a crescendo, not a call to action. The strongest close names the open question and stops — it leaves the reader thinking, which is more persuasive than leaving them cheering.

### Section 7 — Render as HTML

Produce the single-file HTML brief in the house design system (tokens below). Save it, open it, report.

---

## Output

A single-file HTML brief: **headline + italic standfirst + 4–6 sections (assertion sub-heads) + ranged quant inline + honest close.** Long-form Economist prose set in **Lora**; UI, headline, and sub-heads in **DM Sans**.

### House design system — key tokens (apply exactly)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Lora:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f5f4f1; --surface: #ffffff; --text: #0f1923;
      --text-secondary: #4a5568; --text-muted: #718096;
      --border: #dde1e7; --accent: #1f4fa8; --accent-light: #e8eef8;
      --panel-bg: #0f2744; --panel-text: #ffffff;
      --red: #c0392b;
      --font-ui: 'DM Sans', system-ui, sans-serif;
      --font-body: 'Lora', Georgia, serif;
      --width: 960px;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: var(--text); font-family: var(--font-ui); font-size: 17px; line-height: 1.6; }
    .container { max-width: var(--width); margin: 0 auto; padding: 48px 32px 100px; background: var(--surface); }
    .red { color: var(--red); font-weight: 600; }
  </style>
</head>
```

**Layout rules:**
- Container max-width **960px**, base font **17px**, line-height **1.6**.
- No government styling. Custom CSS only. Google Fonts via CDN (DM Sans + Lora).
- **Headline** in DM Sans 600, ~30px. **Standfirst** in Lora italic, ~18px, `--text-secondary`, directly beneath.
- **Body prose** in Lora (this skill is long-form — use Lora for paragraphs, not DM Sans). Sub-heads in DM Sans 600.
- **The single most important sentence** (usually the standfirst's thesis, or the one line that captures the whole business) gets the **navy panel** treatment: `background: var(--panel-bg)`, white text, no border-radius. One panel maximum.
- Sharp corners throughout. No tables for the quant — the numbers live in the prose.
- **Flag any assumed/placeholder figure in red** (`#c0392b`) so it is visibly distinct from grounded numbers — consistent with VA-31. A red number is a number the architecture predicts but has not observed, or a stand-in awaiting real data.

**File location:** save as `{venture-slug}-brief-YYYY-MM-DD.html` in the venture's folder (e.g. `ventures/{venture-slug}/`). Open in the browser after saving.

---

## Quality checks before closing

- **Puzzle test:** does the brief open on a tension, not a description?
- **Five-minute test:** could an intelligent reader with no IVE exposure finish it and explain the business to someone else?
- **VA-32:** is every figure a range with a reason, inline, and are there no more than ~two pull-figures?
- **VA-31:** is every predicted behaviour marked as a prediction once, and is no assumption dressed as a fact?
- **Register:** zero hype words, zero exclamation marks, UK spelling, active voice, short sentences?
- **Close:** does it end quietly on the open question — not a crescendo or a call to action?
- **Scope honesty:** does the brief claim only what the built requirements support? (No moat story if F3 isn't designed.)

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-writeup-custom/SKILL.md` to modify
- Invoke as: `/ive-writeup-custom`
- Related: `/ive-valuation-custom` (prices the same architecture) · `/architect-custom` (the design front door that produces the CDR this reads) · `/verify-venture-custom` (integrity scoring of the architecture)
- Reference for the house HTML system and an example CDR to write up: `ventures/Forge/forge-cdr-package-2026-06-06.html`
- Standards source: Forge WS1 backlog (VA-31, VA-32) — `method/`
- IVE source: Simanis, E. et al. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
