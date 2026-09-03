---
name: verify-balm-custom
description: Verifies completeness of any venture's BALM across all 10 IVE challenges. Reads the venture's workspace transcription, applies IVE-framework criteria per sub-requirement, and produces a traffic-light report with a prioritised gap list.
---

# Verify BALM

Audits the completeness of any venture's BALM across all ten IVE challenges. Reads the venture's live transcription as ground truth, assesses each named sub-requirement against IVE framework standards, and surfaces what has moved and what still needs design work.

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: Simanis, E. et al. (2021), Cornell SC Johnson College of Business.

**Three nested levels of commercial architecture:**

| Level | What it is |
|-------|-----------|
| **Core Business Architecture (CBA)** | The logic that sets both the cost curve and value curve for an industry. No single company owns it. |
| **Business Form Factor (BFF)** | The essential shape product and operations take given a CBA. The default way the product is made, sold, delivered, and paid for. |
| **Business Model** | A company's unique strategy for outcompeting others within a shared BFF. |

IVE intervenes at the CBA/BFF level. Business model thinking comes after.

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

**→ This skill: Audit tool** — verifies completeness across all requirements; run after design sessions to identify gaps

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design. A cost that seems large at 50 units is often trivial against the same cost at 50,000 units.

---

## Step 0 — Identify venture and load source

Ask the user:
1. **What venture are we auditing?** (One word — used as the slug for file paths and the report title.)
2. **Where is the workspace transcription?** The authoritative record of completed design work. Typical locations:
   - `ventures/{venture-slug}/workspace-transcription.md`
   - `ventures/{venture-slug}/{venture-slug}-workspace.md`
   - Or the user can provide the path directly.

Read the file fresh each run — do not rely on memory or any memo HTML. Note the file's `Last updated:` date at the top and include it in the report header.

If no transcription file exists: ask the user for the design decisions they want to audit. Capture them verbatim as the ground truth before proceeding.

---

## Step 1 — Assess each challenge

Work through all ten challenges in order. For each, assess every named sub-requirement against the completeness criteria below. Assign one of three statuses:

| Status | Symbol | Criteria |
|--------|--------|----------|
| Complete | ✅ | Answer meets IVE standard — specific, named, and internally consistent. No open flags. |
| Partial | ⚠️ | Answer exists but one or more element is directional only, missing a named theory, or explicitly flagged TBD in the workspace. |
| Open | ❌ | No answer, placeholder text only, or answer contradicted by an open flag in the workspace. |

A challenge-level status is the **worst** sub-requirement status within it — one open sub-requirement makes the whole challenge open.

---

## Step 2 — IVE completeness criteria per sub-requirement

Apply these standards when assessing each sub-requirement. A sub-requirement is **Complete** only if it satisfies all criteria listed.

**At-scale check (apply to all requirements):** Was the requirement designed for at-scale economics, or was it constrained by launch-phase limitations? A strategy that only works at 50 units but not at 50,000 is not a valid R-level solution. Flag any answer that appears launch-phase-constrained as Partial (⚠️) rather than Complete (✅).

### F1 — Neutralise the Value Barrier

**C1 — At-scale cost bottleneck**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Conventional Operational Model | A specific named entity or model (not generic "current practice") — describes how the target problem is solved today in the default system |
| Critical Limiting Operation | The single procedure within that model identified as contributing the greatest share of at-scale running costs — not a category, a specific operation |
| Workaround Theory of Change | All four elements present: (1) class of problem named, (2) named theory cited, (3) current state articulated, (4) desired state articulated |
| Workaround Strategy | A specific mechanism that circumvents the CLO without replicating its cost structure — not a restatement of the theory |
| Business Form Factor (C1) | Product form described in one clear sentence that productizes the strategy — not just a category label |

**C2 — Eliminate customer's biggest monetizable cost**

| Sub-requirement | Complete when… |
|----------------|----------------|
| High-Import Outcome & KPIs | Outcome named; KPI named; current customer routine described with at least three concrete steps |
| Key Monetizable Cost | Single greatest cost identified (money, fear, or stress); quantified or bounded where possible; not a list of several costs |
| Efficacy Theory of Change | All four elements: key parameter named, named theory cited, current state, desired state |
| Efficacy Strategy | Specific mechanism — not a restatement of the theory |
| Business Form Factor (C1–C2) | Updated product form incorporating C2 answer |

**C3 — Working capital bottleneck**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Critical Limiting Operation II | Specific procedure in the interim model identified as requiring greatest working capital — with a timeframe or magnitude indicator |
| Scaling Theory of Change | Named theory + current state + desired state. Note: two candidate theories are acceptable if neither has been eliminated yet — flag as partial |
| Scaling Strategy | Strategy must not be flagged as operationally problematic by the workspace itself. If the workspace has flagged the current strategy, this sub-requirement is Open until an alternative is provided |
| Business Form Factor (C1–C3) | Complete synthesis of all three F1 answers into a single product form description |

**C4 — Customer doubt**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Customer's Implicit Efficacy Theory | What the customer currently believes about how the problem should be solved — not Calmly's view, the customer's view |
| Key Efficacy Doubt | The single most important factor causing the customer to doubt the product — specific and testable |
| Attraction Theory of Change | Named theory (e.g. Framing Theory, Anchoring) + current state + desired state |
| Attraction Strategy | Specific reframe or mechanism — not a restatement of the theory |
| Business Form Factor (C1–C4) | Product form updated to incorporate C4 answer |

**C5 — Learning difficulty**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Required Product Use Routine | All steps a customer must complete for the product to "work" — numbered, sequential, specific |
| Key Learning Block | The single main barrier to learning the routine — specific and named (not "it's complex") |
| Adoption Theory of Change | Named class of problem (e.g. risky, tacit, disruptive, complex) + named theory + current state + desired state. If class of problem is TBD, this is Partial |
| Adoption Strategy | Specific trust signal or mechanism — not just "sell through law firms" (too generic to be actionable) |
| Business Form Factor (C1–C5) | Updated synthesis |

**C6 — Budget line item**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Key Customer Segments | Named, with their routines described |
| Amortisation Strategy | Specific mechanism for how the customer pays — including timing, trigger, and who bears the float |
| Gateway Partner | Named entity + unifying mission across all gateway organisations articulated. If mission is "?" this is Partial |
| Business Form Factor (C1–C6) | Updated synthesis |

**C7 — Gateway partner**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Key Customer Segments | All segments identified with their distinct routes to the high-import outcome |
| Gateway Partner | Named + clear explanation of why this entity is common to all segment routines |
| Integration Theory of Change | A named theory for why the gateway partner would actively champion (not merely tolerate) Calmly — with current and desired state |
| Integration Strategy | Specific mechanism to embed product in customer routines through the gateway — not just "partner with law firms" |
| Business Form Factor (C1–C7) | Updated synthesis |

**C8 — Lock-in (switching cost)**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Extended Product Use Routine | How the product use extends over time and interfaces with the customer's life or organisational context — not just the initial use |
| Key Store of Value | The specific asset that accretes value over time and would be lost or put at risk on switching — named and concrete |
| Lock-In Theory of Change | Named theory for how this store of value creates a switching cost; current state; desired state |
| Lock-In Strategy | Specific mechanism to manufacture, accrete, and make that store of value subject to loss — not just a direction |

**C9 — Lock-out (resource moat)**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Required Core Competency | The specific capability needed to deliver the value proposition that competitors would need to replicate |
| Key Resource | The specific resource or asset that is or can be made scarce or inimitable — named concretely |
| Lock-Out Theory of Change | Named theory for how scarcity is manufactured; current state; desired state |
| Lock-Out Strategy | Specific mechanism to build and maintain the moat — not just an analogy |

**C10 — Leverage (supplier replaceability)**

| Sub-requirement | Complete when… |
|----------------|----------------|
| Interim Value Chain | Key steps and supplier inputs in the operational model — enough to identify where leverage risk sits |
| Key Input | The specific supplier input with highest cost or volume — named concretely |
| Leverage Theory of Change | Named theory for how replaceability is manufactured; current state; desired state |
| Leverage Strategy | Specific mechanism to make the key input replaceable — including what Calmly controls to achieve this |

---

## Step 3 — Build the report as HTML

Generate a single-file HTML document using the standard design system below. Save it to:

```
ventures/{venture-slug}/balm-verification-{YYYY-MM-DD}.html
```

Then open it in the browser.

### HTML boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Venture name} BALM — Verification Report</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Lora:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f5f4f1; --surface: #ffffff; --text: #0f1923;
      --text-secondary: #4a5568; --text-muted: #718096;
      --border: #dde1e7; --accent: #1f4fa8; --accent-light: #e8eef8;
      --panel-bg: #0f2744; --panel-text: #ffffff;
      --warning-bg: #fff8e6; --warning-border: #d4820a;
      --green-bg: #e6f4ec; --green-text: #166534;
      --red-bg: #fde8e8; --red-text: #991b1b;
      --yellow-bg: #fef9e6; --yellow-text: #854d0e;
      --tag-radius: 3px;
      --font-ui: 'DM Sans', system-ui, sans-serif;
      --font-body: 'Lora', Georgia, serif;
      --width: 960px;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: var(--text); font-family: var(--font-ui); font-size: 16px; line-height: 1.6; }
    .container { max-width: var(--width); margin: 0 auto; padding: 48px 32px 100px; background: var(--surface); }
    .doc-header { border-bottom: 2px solid var(--text); padding-bottom: 20px; margin-bottom: 36px; }
    .doc-header .label { font-size: 12px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 8px; }
    .doc-header h1 { font-size: 26px; font-weight: 600; margin-bottom: 6px; }
    .meta-row { display: flex; gap: 24px; font-size: 13px; color: var(--text-muted); margin-top: 12px; }
    .scorecard { display: flex; gap: 16px; margin: 28px 0; }
    .score-box { flex: 1; padding: 20px; text-align: center; border: 1px solid var(--border); }
    .score-box .score-num { font-size: 36px; font-weight: 600; line-height: 1; margin-bottom: 6px; }
    .score-box .score-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }
    .score-complete .score-num { color: var(--green-text); }
    .score-partial .score-num { color: var(--yellow-text); }
    .score-open .score-num { color: var(--red-text); }
    .tag { display: inline-block; font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: var(--tag-radius); border: 1px solid; white-space: nowrap; }
    .tag-green { background: var(--green-bg); color: var(--green-text); border-color: #a7d4b8; }
    .tag-yellow { background: var(--yellow-bg); color: var(--yellow-text); border-color: #f0d98a; }
    .tag-red { background: var(--red-bg); color: var(--red-text); border-color: #f0b4b4; }
    h2.section-h2 { font-size: 18px; font-weight: 600; margin: 40px 0 14px; border-top: 1px solid var(--border); padding-top: 28px; }
    .summary-table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
    .summary-table th { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); background: #f7f7f6; padding: 9px 14px; text-align: left; border-bottom: 2px solid var(--border); }
    .summary-table td { padding: 11px 14px; border-bottom: 1px solid var(--border); font-size: 14px; vertical-align: top; }
    .summary-table tr:last-child td { border-bottom: none; }
    .fn-label { font-size: 10px; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; color: var(--accent); }
    .challenge-block { border: 1px solid var(--border); margin-bottom: 20px; }
    .challenge-block-header { display: flex; align-items: center; gap: 12px; padding: 14px 20px; background: #fafaf9; border-bottom: 1px solid var(--border); }
    .c-num { width: 28px; height: 28px; min-width: 28px; background: var(--accent); color: white; font-weight: 600; font-size: 12px; display: flex; align-items: center; justify-content: center; border-radius: 50%; }
    .c-title { flex: 1; font-size: 15px; font-weight: 600; }
    .subreqs { width: 100%; border-collapse: collapse; }
    .subreqs td { padding: 11px 20px; border-bottom: 1px solid var(--border); font-size: 14px; vertical-align: top; }
    .subreqs tr:last-child td { border-bottom: none; }
    .subreqs td.r-name { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-secondary); width: 200px; min-width: 160px; }
    .subreqs td.r-note { font-family: var(--font-body); font-size: 13px; line-height: 1.6; color: var(--text-secondary); }
    .subreqs td.r-status { width: 70px; text-align: center; }
    .gap-item { border-left: 3px solid var(--warning-border); background: var(--warning-bg); padding: 14px 18px; margin-bottom: 14px; }
    .gap-item .gap-header { font-size: 14px; font-weight: 600; margin-bottom: 6px; }
    .gap-item .gap-missing { font-family: var(--font-body); font-size: 13px; color: var(--text-secondary); margin-bottom: 8px; line-height: 1.6; }
    .gap-item .gap-q { font-size: 13px; font-style: italic; color: #7a4a00; line-height: 1.6; }
    .gap-item .gap-q::before { content: "Q: "; font-weight: 600; font-style: normal; }
    .verdict { background: var(--accent-light); border-left: 4px solid var(--accent); padding: 16px 20px; margin-top: 32px; }
    .verdict p { font-family: var(--font-body); font-size: 14px; line-height: 1.7; }
    .verdict strong { font-family: var(--font-ui); }
    .complete-note { color: var(--text-muted); font-size: 13px; font-style: italic; padding: 12px 20px; }
    .gap-num { display: inline-block; width: 22px; height: 22px; background: var(--warning-border); color: white; border-radius: 50%; font-size: 11px; font-weight: 600; text-align: center; line-height: 22px; margin-right: 8px; flex-shrink: 0; }
  </style>
</head>
<body>
<div class="container">
  <!-- content built by the skill -->
</div>
</body>
</html>
```

### Section A — Header and scorecard

Build the header block with:
- Label: "{Venture name} BALM — Verification Report"
- H1: "Design completeness audit — {venture name}"
- Meta row: run date (today's date), source file last-updated date extracted from the transcription, link text "Source: calmly-demo-workspace-transcription.md"

Below the header, render a three-box scorecard:
- Box 1 (green): number of Complete challenges
- Box 2 (amber): number of Partial challenges
- Box 3 (red): number of Open challenges

Below the scorecard, one sentence: "X of 10 challenges complete. Y partial. Z open."

### Section B — Traffic-light summary table

Heading: "Challenge status at a glance"

Table columns: `#` | `Function` | `Challenge` | `Status` | `Bottleneck`

- Status column: render as colour-coded tag (tag-green / tag-yellow / tag-red)
- Bottleneck column: for Complete challenges, em dash. For Partial/Open, one short phrase naming the blocking sub-requirement.

### Section C — Per-challenge detail

Heading: "Challenge breakdown"

Only render detail blocks for Partial or Open challenges. For each:

- Challenge header bar with number circle, title, and status tag
- Sub-requirement table with columns: `Sub-requirement` | `Status` | `Note`
- Note column: one short sentence explaining why the sub-requirement has that status

For Complete challenges, render a single collapsed row: "All sub-requirements complete — no action needed."

### Section D — Prioritised gap list

Heading: "What to work on next"

Intro sentence: "Ordered by structural impact — gaps that block downstream challenges appear first."

For each open or partial sub-requirement, render a gap card with:
- Numbered badge + challenge number + sub-requirement name + status tag
- "What is missing:" one sentence
- "Q:" one specific diagnostic question to resolve it

Priority order:
1. Structural blockers — gaps that prevent downstream challenges from being completed
2. F1 before F2 before F3
3. Within the same function, earlier challenges first

### Section E — Recommended next session

Heading: "Recommended next session"

One paragraph stating which gap to tackle first and why. Note any gaps that share a root cause and should be worked on together. Keep it direct — this is a working note, not a summary.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/verify-balm-custom/SKILL.md` to modify
- Ground truth source: venture workspace transcription — ask user for path, or look in `ventures/{venture-slug}/`
- Design memo: `ventures/{venture-slug}/{venture-slug}-design-memo.html` (if it exists)
- IVE methodology reference: `06-Resources/Methodology/baf-requirements-full.md`
- Related skill: `/pyramid-doc` (for building memos from completed BALM sections)
