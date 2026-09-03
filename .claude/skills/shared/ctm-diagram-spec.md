# CTM Diagram Format Specification

> **🗣 STATE LANGUAGE — the person-state register (exemplar set by Tom, 28 Aug 2026).** A CTM state is a PERSON in a state of belief, understanding or commitment — never a process step. Write every designed state in the form **"[Actor] who [believes / understands / has done X]"**. The reference exemplar is the original Calmly claimant/defendant CTM, whose customer track reads: *"Claimant who wants to resolve their issue" → "Claimant who believes Calmly can help them + becomes a customer" → "Claimant who understands why they should sell their claim now" → "Claimant who has given up rights to their claim" → "Claimant who has resolved their issue."* Note what changes rung to rung: first a belief, then an understanding, then a commitment, then a resolution — the person transforms; the product is what transforms them. ❌ "Obligation raised on the shared record" (a process event — nobody transforms) · ✅ "Business whose customer has agreed what is owed" (a person whose position has changed). Where a second actor's state changes are load-bearing — an anti-customer, a counterparty — give that actor its own state track in the same register, with the value posture stated (the exemplar's note: "Defendant is an anti-customer; we're maximizing value for the claimant, which requires reducing value for the defendant in this phase"). Product labels carry their causal action the way the exemplar's CP2 does — "Comms to the defendant that the claim is owned by Calmly and a team is preparing to represent it in court" says what the product *does to the person*, not what it is.

> **📝 STATE-CHANGE NARRATIVE (mandatory since 28 Aug 2026, Tom's ruling):** the diagram shows *that* each transition happens; the written narrative holds *why*. Every carried transition in the model file carries a `narrative` block with three fields — `change_type` (cognitive / emotive / behavioural), `state_change` (what is true of the customer after the transition that was not true before), and `mechanism` (**how** the 4-D product causes the change — the causal account, not a restatement that the product is present). The validator refuses a model dated on or after 28 Aug 2026 without them, and warns on a mechanism too short to explain anything. The generator renders the narratives as a table below the diagram, so the context that is easy to lose in the diagram is never lost from the record.

> **👥 USER TRACKS (added 1 Sep 2026, Tom's ruling):** the phases carry the CUSTOMER's journey; actors who use the product without being the payer (Calmly: the disputants) get their own modelled state track. Model key: top-level `user_tracks:` — each entry carries `actor`, `role_note` (who they are relative to the payer, and the value posture), `states` and `transitions`, in the same person-state register and under the same narrative rule as the phases. The validator applies identical checks; user tracks carry no decision diamonds (forks belong to the customer phases). The generator renders each track as its own swimlane under a "User journeys" divider, includes its transitions in the narrative table (which now carries an Actor column), and counts its components in the products roster.

> **🤝 PARTNER TRACKS (added 1 Sep 2026, Tom's ruling):** partners belong in the CTM two ways, and both are the method's own practice, not an extension. (1) As PartP hexagons on customer transitions, where the partner's contribution causes the customer's state change — the purple hexagon colour has always been reserved for this. (2) As their own state track: the partner is themselves transformed (R7 — supplying the venture becomes their best route to their own outcome), and the historic Calmly CTM v3 carried exactly this as "Track B — the ITP Journey" before the Aug 2026 YAML migration dropped it. Model key: top-level `partner_tracks:` — identical schema and validation to `user_tracks` (actor / role_note / states / transitions, person-state register, narrative rule, no decisions), for `enabler`-class actors. Rendered under a "Partner journeys" divider; transitions join the narrative table and the products roster. An AOM waypoint says who a flow passes through; it is not a substitute for the partner's transformation journey — a load-bearing partner with no track and no PartP component is a finding.

> **🧩 4-D PRODUCTS ROSTER (added 1 Sep 2026, Tom's ruling):** the generated page ends its diagram supplementary with "4-D products required in the journey" — every product component carried on any transition — customer phases, user tracks and partner tracks together, grouped and sorted by type (CP · WP · PP · PartP). Derived from the transitions, never hand-listed. Descriptions are pulled from the sibling AOM model's component register where one exists. A 4-D type absent from every transition is flagged on the page (⚑) — it is either not yet designed into the journey or not yet carried on a transition, and the record must say which.

> **⚙️ GENERATION ROUTE (mandatory since 25 Aug 2026):** this spec defines the visual format, but the file is never hand-written. The model lives in `[venture]-ctm-model-at-C[N].yaml`; the HTML record and layered draw.io view are generated by the scripts in `.claude/skills/shared/generators/` (see each challenge skill's Section 5 for the run commands). Hand-edits to generated files are lost on regeneration.


Shared reference for all challenge skills. The CTM output is a horizontal swimlane flow diagram — not a table. This spec defines the visual format, design system, and structural rules. Challenge skills point here for format; they define their own process and venture-specific content.

**Reference visual:** `.claude/skills/ive-ctm-custom/reference/calmly-demo-workspace.pdf` — the Calmly CTM page is the canonical visual. Read it before generating. The spec below matches it.

---

## Format rules

- **State nodes** — white rectangles, a few words each, sparse. The cognitive/emotive/behavioural decomposition is the *thinking behind* each node — never rendered in the diagram. No quotes, no THINK/FEEL/DO rows, no FROM→TO bands. Terseness is the spec.
- **Product components** — coloured hexagon nodes sitting *between* two state rectangles on the transition arrow (state → hexagon → state). The hexagon IS the point: it shows which numbered product component (CP #1, WP #1, PP #1, PartP #1) drives the transformation. A few words inside.
- **Colour by 4-D product:** blue = Communications Product · blue/indigo = Working Product · amber = Payment Product · purple = Partner Product
- **Decision points** — diamond shape `◇` where the journey forks. Branch A (main): solid arrow. Branch B (escalation): dashed arrow. Letter in a circle on each branch line.
- **Escalation box** — dark border, light grey background, top-right. Used for court/default tracks.
- **Annotation boxes** — dark background, white text, for important contextual notes.
- **Swimlane labels** — vertical, uppercase, small, left edge of each lane.
- **No BALM requirement badges on the diagram itself** — those belong in the supplementary BALM mapping table below the diagram.

---

## Design system

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #ffffff;
      --text: #1a1a2e;
      --text-muted: #6b7280;
      --border: #d1d5db;
      --node-border: #93c5c4;
      --node-bg: #f0f9f9;
      --label-cp: #e8f4f4;
      --label-wp: #e8eef8;
      --label-pp: #fef9e6;
      --label-part: #f0ebfb;
      --label-cp-text: #007d7a;
      --label-wp-text: #1f4fa8;
      --label-pp-text: #854d0e;
      --label-part-text: #5b21b6;
      --escalation-bg: #f8f9fa;
      --escalation-border: #374151;
      --win-bg: #d1fae5;
      --win-border: #059669;
      --lose-bg: #fee2e2;
      --lose-border: #dc2626;
      --note-bg: #1a1a2e;
      --note-text: #ffffff;
      --arrow: #9ca3af;
      --font: 'DM Sans', system-ui, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); font-family: var(--font); color: var(--text); }

    .diagram-wrapper { width: 100%; overflow-x: auto; padding: 32px 40px 48px; }
    .diagram { min-width: 1400px; position: relative; }

    .timeline { display: flex; align-items: flex-start; margin-bottom: 32px; padding-bottom: 12px; border-bottom: 1px solid var(--border); position: relative; }
    .timeline-marker { position: absolute; top: 0; display: flex; flex-direction: column; align-items: center; font-size: 12px; font-weight: 500; color: var(--text-muted); }
    .timeline-marker::after { content: ''; width: 1px; height: 20px; background: var(--border); margin-top: 4px; }

    .swimlane { display: flex; align-items: center; gap: 0; margin-bottom: 40px; position: relative; min-height: 120px; }
    .swimlane-label { font-size: 11px; font-weight: 600; color: var(--text-muted); writing-mode: vertical-lr; transform: rotate(180deg); margin-right: 16px; text-transform: uppercase; letter-spacing: 0.08em; }

    .state-node { position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; width: 110px; flex-shrink: 0; }
    .state-icon { font-size: 32px; margin-bottom: 6px; }
    .state-label { font-size: 11px; line-height: 1.35; color: var(--text); background: var(--node-bg); border: 1px solid var(--node-border); border-radius: 6px; padding: 6px 8px; width: 100%; }

    /* Hexagon product node */
    .hex-node { display: flex; align-items: center; justify-content: center; width: 72px; height: 72px; flex-shrink: 0; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); font-size: 10px; font-weight: 600; text-align: center; line-height: 1.25; padding: 8px; }
    .hex-cp { background: var(--label-cp); color: var(--label-cp-text); }
    .hex-wp { background: var(--label-wp); color: var(--label-wp-text); }
    .hex-pp { background: var(--label-pp); color: var(--label-pp-text); }
    .hex-part { background: var(--label-part); color: var(--label-part-text); }

    .connector { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; min-width: 24px; }
    .connector-line { width: 100%; height: 2px; background: var(--arrow); position: relative; }
    .connector-line::after { content: '▶'; position: absolute; right: -8px; top: -8px; font-size: 10px; color: var(--arrow); }
    .connector-line.dashed { background: repeating-linear-gradient(90deg, var(--arrow) 0px, var(--arrow) 6px, transparent 6px, transparent 12px); }

    .diamond { width: 80px; height: 80px; background: #fff8e6; border: 2px solid #d4820a; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .diamond-label { transform: rotate(-45deg); font-size: 10px; font-weight: 600; color: #854d0e; text-align: center; line-height: 1.2; }

    .branch-marker { width: 18px; height: 18px; border-radius: 50%; background: #374151; color: white; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin: 0 4px; }

    .escalation-box { border: 2px solid var(--escalation-border); background: var(--escalation-bg); padding: 16px 20px; border-radius: 4px; min-width: 240px; }
    .escalation-timeline { font-size: 11px; color: var(--text-muted); line-height: 1.8; margin-bottom: 16px; }
    .outcome-win { border: 2px solid var(--win-border); background: var(--win-bg); border-radius: 6px; padding: 8px 12px; font-size: 11px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .outcome-lose { border: 2px solid var(--lose-border); background: var(--lose-bg); border-radius: 6px; padding: 8px 12px; font-size: 11px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }

    .annotation { background: var(--note-bg); color: var(--note-text); font-size: 11px; line-height: 1.5; padding: 10px 14px; border-radius: 4px; max-width: 280px; }

    .supplementary { max-width: 960px; margin: 48px auto; padding: 0 40px 80px; }
    h2 { font-size: 18px; font-weight: 600; color: #007d7a; margin: 32px 0 12px; border-bottom: 2px solid #007d7a; padding-bottom: 6px; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 12px 0 24px; }
    thead tr { background: #007d7a; color: #fff; }
    thead th { padding: 9px 12px; text-align: left; font-weight: 600; }
    tbody td { padding: 8px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
    tbody tr:nth-child(even) { background: #f9fafa; }
    .footer { font-size: 12px; color: var(--text-muted); text-align: center; margin-top: 48px; }
  </style>
</head>
<body>
  <div class="diagram-wrapper">
    <div class="diagram">
      <!-- Timeline header -->
      <!-- Swimlane rows: state-node → connector → hex-node → connector → state-node -->
      <!-- Decision diamonds -->
      <!-- Escalation box (if applicable) -->
      <!-- Annotation boxes -->
    </div>
  </div>
  <div class="supplementary">
    <!-- BALM mapping table -->
    <!-- Review findings -->
    <!-- Routing panel -->
    <!-- Footer -->
  </div>
</body>
```

---

## Document structure

**Section 1 — Flow diagram** (the main visual)

**Section 2 — BALM mapping table**

| BALM requirement | CTM phase | Product component | What it overrides |
|---|---|---|---|
| R4 — Want Block | Phase 1 / Conviction | CP #n — element | standard practice |
| R5 — Use Block | Phase 2 / Activation | WP #n — element | standard practice |
| R6 — Buy Block | Phase 3 | PP #n — element | standard practice |
| R7 — Gateway | Phase 1 / Awareness | PartP #n — element | standard practice |
| R8 — Lock-in | Phase 2 + Phase 4 | WP #n — accumulation | what accumulates |

**Section 3 — Review findings** (brief)
- Logical viability risks
- Realistic progression concerns
- Elegance opportunities (state changes that could be collapsed)
- Sub-phases still on standard practice (deliberate or to revisit)

**Section 4 — Routing panel** (dark, full-width)

**Section 5 — Footer:** `Generated [date] · Dex`

---

## File naming convention

Label by challenge, not by version: `[venture]-ctm-at-C[n].html` (Calmly example: `calmly-ctm-at-C10.html`)

Example: `calmly-ctm-at-C7.html`

Do not use version numbers (v6, v7). The challenge label is the version.
