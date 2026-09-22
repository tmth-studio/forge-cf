---
name: ive-fin-sim-custom
description: Build bottom-up IVE financial simulations as interactive single-file HTML documents. Interviews the user to gather venture inputs, then generates a live model that calculates required price, FMOS, working capital, and cost drivers — following the IVE/IFC methodology by Erik Simanis (Cornell MCL).
---

# IVE Financial Simulation

## Model routing (mandatory default)

Per `.claude/skills/shared/ive-model-routing.md`: run the interview and all input-confirmation and judgment steps in-session. Dispatch the **production step** (generating the HTML simulation document) to an Agent-tool subagent with `model: "opus"` and a self-contained prompt (all confirmed inputs, output path, format spec by absolute path). Verify the produced file in-session before continuing. Skip the dispatch only if Tom says "run inline" or the output is trivially small.

---

## Architecture discipline — model only from confirmed challenges

**Only include revenue lines, cost lines, and operating assumptions grounded in challenges formally completed (marked ✓) at or before the current point in the IVE sequence.**

Do not include costs for roles or operations that serve mechanisms not yet established, and do not include revenue streams not yet architecturally defined. If a cost or revenue line requires a later challenge, flag it as `[REQUIRES C[N]+]` and exclude it from the model. The simulation is a progressive document: costs must derive from the confirmed operational structure, not from the anticipated full architecture.

---

Builds a bottom-up interactive financial simulation for any IVE venture. Follows the methodology set out in the IFC paper by Erik Simanis (Cornell MCL): start from at-scale activities, build costs upward, derive required price at target FMOS.

The output is a single-file HTML simulation where every assumption is editable and every calculated line is expandable to show the formula driving it.

**Quality bar:** the field list and check-cell structure stated in this skill. Do not read another venture's simulation to learn the layout. `[evidence: VA-BS1]`

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: the IVE canon — Simanis, E. et al. (2021), Cornell SC Johnson College of Business, and the co-authored papers 2023–2025 (Simanis, Manuel et al. 2023; Simanis et al. 2024; Simanis 2025). Full list at the foot of this skill or in `architect-custom`.

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

**→ This skill: IVE Financial Simulation** — runs after R1 and R2 are designed; models the at-scale unit economics to verify the architecture is viable

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design. A cost that seems large at 50 units is often trivial against the same cost at 50,000 units.

---

## Source discipline — apply to every input

Every assumption and data point in the simulation must carry a traceable source. This is not optional — untraced assumptions cannot be audited, and unauditable assumptions are hypotheses dressed as facts.

**Source tiers (apply in this order of preference):**

| Tier | What it is | Label in simulation |
|------|-----------|---------------------|
| **1 — Primary data** | Direct measurement from this venture's own field research, pilot, or live operations | `Source: [activity], [date]` |
| **2 — Published statistics** | Government data, regulatory publications, court statistics, academic studies | `Source: [publication], [date], p.[X]` |
| **3 — Industry benchmark** | Recognised industry standard, comparable venture, expert estimate with named source | `Source: [benchmark/expert], [date]` |
| **4 — Reasoned assumption** | No external source; derived from logic and stated constraints. Must name the logic. | `Assumption: [reasoning]. Needs Tier 1–3 validation.` |

**Rules:**
- Every editable input in the simulation HTML must display its source tier and note on hover or in a visible label below the field
- No input may be labelled "estimate" or "assumption" without stating the reasoning behind it
- When the user provides a number without a source, ask: "What's the source for that?" before including it. If they don't have one, classify it as a Tier 4 assumption and flag it for validation.
- When building from a prior simulation, do not carry forward old numbers without re-sourcing them. Old simulations are a starting point for questions, not a source of truth.

**In the simulation HTML:** each input field must include a `data-source` attribute and display it visibly (e.g. as a small muted line below the input). Tier 4 assumptions are highlighted with a yellow left border to make them visually distinct from sourced inputs.

---

## Figures are TPM records, not point estimates — apply to every load-bearing input

Canonical standard: `04-Projects/TMTH_Venture_Studio/Forge/WS1/tpm-measurement-standard.md` (INCOSE Technical Measurement). Read it; do not restate it here.

Every load-bearing figure (one that moves the FMOS or carries material risk) is expressed as a **TPM record**, not a bare point:

- **Band** `[low, high]` — never a single number. A point estimate is high-resolution / low-fidelity — the Simanis failure mode.
- **V/Val type** — **Verification** (the figure follows from the design meeting its requirement — cost floor, FMOS arithmetic; evidenced by analysis/examination, high confidence now) or **Validation** (a claim about real-world behaviour — WTP, adoption, completion rate; ultimately needs demonstration/test in the operational environment). This tag governs how the figure can be evidenced.
- **Evidence method** — INCOSE's four: examination · analysis · demonstration · test. "Assumed / no method" is a verifiability defect, not a tier. (Maps onto the source tiers above: T4 = assumed/no-method; T3 = examination against a benchmark; T2 = analysis/published; T1 = demonstration/test confirmed.)
- **Threshold / objective** — the must-meet gate (FMOS ≥ 60% Phase-II / ≥ 25% per-requirement) and the design target above it.
- **Convergence** — the event that confirms the band and roughly when. For a validation figure this is a demonstration or operational test; analysis only gives interim evidence.

**FMOS is a propagated band, not a point.** Flow the input bands through to an FMOS band. Then: (1) test whether the whole band clears the threshold; (2) name the binding input (whose low end drives the worst corner); (3) report the margin from failure at the worst corner. The sensitivity surface is native output, not an afterthought.

**The IVE promise is conditional.** A validation-by-analysis band is credible only if the requirement is soundly solved and the IVE mechanism holds for this venture — state it as "predicted-by, conditional on R-n holding," never "proven." Pilot in-band corroborates; out-of-band is diagnostic of a mis-solved requirement.

**Discipline guard:** TPM records are for load-bearing figures only. Derived line items inherit their driver's band. A model where every number is a band signals nothing.

---

## Stage 0: AOM alignment check (run before the interview)

**Before gathering any numbers, check whether an AOM exists for this venture.** If it does, the fin-sim must use the same operating model — otherwise the simulation models a venture that doesn't match the operational design.

Check for an AOM file:

```
04-Projects/{venture-slug}/aom-{date}.html
```

**If no AOM exists yet:** proceed to Stage 1. Note that Group 1 and Group 4 operating inputs (LMU count, cases/LMU, staff structure) are ungrouped assumptions — they must be cross-checked against the AOM when it is built.

**If an AOM exists:** read it and extract the following parameters before starting the interview:

| Parameter | AOM value | Notes |
|---|---|---|
| LMU count at scale | | |
| LMU type (location, legal structure) | | e.g. university law clinic vs county court catchment area |
| Delivery staff role and seniority | | e.g. law student vs litigation associate |
| Cases / LMU / month (at-scale) | | |
| Conversion rate (inquiries → purchased) | | |
| At-scale cases / month (total) | | should equal LMU count × cases/LMU × conversion rate |

Use these as the starting defaults for Group 1 and Group 4. When the user provides a different number, flag the discrepancy: *"The AOM shows [X] — you've given [Y]. Which is correct, and should the AOM be updated to match?"*

**Why this matters:** It is possible for the AOM and the fin-sim to drift apart — typically because the fin-sim was updated to reflect a later design stage while the AOM was not revised. When this happens, neither document is reliable on its own. The check takes two minutes and prevents the GIGO problem the methodology exists to solve.

**A warning that applies to any reference simulation.** A simulation built for one operating model does not transfer to another. Where the reference was built on a delivery model the current venture does not use, its unit counts, volumes and cost lines are not comparable — use it for structure, never for levels. `[evidence: VA-BS1]`

---

## Stage 1 — Interview

Ask the following questions in sequence. Don't ask all at once — work through them conversationally, one group at a time. Confirm answers before moving to the next group.

**Default interview posture — assume and note, audit later.**

Do not block the interview on missing sources. When a number is needed and the user hasn't provided one:
1. Make the most defensible assumption based on available context, comparable ventures, and IVE methodology defaults
2. State the assumption clearly with a one-line rationale ("Assumed X because Y")
3. Tag it Tier 4 in the simulation
4. Move on — do not ask the user to confirm unless the assumption is genuinely high-stakes (e.g. the single number that determines whether FMOS passes or fails)

Source validation is a separate audit step, run after the simulation is built. The goal of the interview is to get to a working model fast, not to achieve perfect sourcing before the first number is entered.

**For every number the user provides:** record the source alongside the number. If they can't give a source, classify it as Tier 4 and note what validation would upgrade it.

### Group 1: The venture and the unit

1. **Venture name and one-line description.** What does it do?

2. **The operating unit (module).** This is the most important input in the model — get it right before anything else.

   The unit is not just the customer transaction. It is the **operating module** — the smallest self-contained operational structure that the venture replicates when it scales. Everything in the simulation is anchored to this module: headcount, fixed costs, volume capacity, and peak working capital.

   **How to identify the right unit:**
   - Ask: "What is the thing we replicate when we grow?" If growth means adding another team, another location, another processing cohort — that is the unit.
   - The unit has a **capacity ceiling**: the maximum number of customer transactions it can process per period before a new unit must be added.
   - Fixed costs (supervision, infrastructure, management overhead) are anchored to the unit, not to individual transactions. They amortise across the transactions the unit processes.
   - Variable costs (direct labour, consumables, working capital) scale with the number of transactions within the unit.

   **The distinction matters because:**
   - If you define the unit as a single transaction, you strip out fixed costs — the model underprices
   - If you define it as the whole business, you lose the replication logic — the model can't tell you when to add capacity
   - The operating module threads both: fixed costs are real, and the module is the thing that gets cloned

   **Example — Grameen Bank:** The unit is a peer group (5 members + their joint liability structure). The bank replicates groups, not loans. Fixed supervision cost amortises across the 5 members. Working capital scales with group count.

   **Worked example:** the unit might be a supervised cohort — several trainees plus one qualified supervisor, processing a stated volume per month. Fixed supervision cost amortises across the cohort. Working capital scales with claims under management.

   Ask: "What is the operating module for this venture — the thing that gets replicated when you scale? And what is its monthly processing capacity?"

2b. **The customer base — one-time or held stock.** *(Method step 1(c), added v1.1. Do not skip. A model that skips this asserts a leaving rate of zero.)*

   Item 2 bounds the **supply** side — the unit that serves customers. This item bounds the **demand** side as a *stock*: what it costs to stop the customer base from falling while you build it.

   **First, list every group the venture must hold on its books to earn revenue.** Usually more than one:
   - End customers
   - **Any intermediary that delivers volume** — referral partner, distribution site, accredited supplier, channel. This is the one that gets missed. If it can leave, and its leaving cuts revenue, it is a stock.

   **Then classify each group with one question: one-time customer, or held stock?**

   | Answer | What it means | What the model does |
   |---|---|---|
   | **One-time** | Buys once, does not return. Each sale is a fresh acquisition. | Acquisition cost moves to **running costs** as a per-unit line. Replacement is then priced automatically on every unit, in ramp and equilibrium alike. No leaving rate needed. **Record the classification explicitly** — otherwise a reader cannot tell a considered answer from a missing one. |
   | **Held stock** | Must be retained to keep earning. | Three numbers are required before the build can proceed: **annual leaving rate**, **cost to win one**, **months to full productivity**. |

   Ask: *"Does a customer buy once and leave, or do you have to keep them? And is there any partner or channel you have to keep, that would take volume with it if it left?"*

   **If the answer is "held stock" and the user has no leaving rate:** do not block, and do not leave it blank. Band it, tag it Tier 4, and name it as the assumption it is. A blank reads as zero, and zero is a claim that nobody ever leaves, forever.

   **Flag concentration.** If one held stock carries a large share of at-scale volume, say what share and say it in the output. A venture with 60% of volume arriving through a partner channel has 60% of revenue sitting on a stock it does not own.

3. **Pricing model.** How does the customer pay? (% of recovered value, flat fee, subscription, contingency, settlement spread, etc.)

4. **Revenue per unit.** What are the variables that determine revenue per transaction? (e.g. average settlement value × take rate, or face value × spread %, or flat £X)

### Group 2: Cost of goods and capital

5. **Cost of goods per unit.** What upfront cash must the venture commit per unit *before* receiving revenue? This goes on the balance sheet as an asset. (e.g. purchasing a claim, manufacturing a product, deploying a service, advancing a loan)
6. **Cost of capital.** What is the annual financing cost on that commitment? (Default: 15%)

### Group 3: Resolution waterfall

7. **How long does each unit take to generate revenue?** Ask for a distribution — the % of units resolving in each time period. Should sum to 100%. Example format:
   - Month 0: X%
   - Month 1: X%
   - Month 2: X%
   - Month 3: X%
   - Month 4: X%
   - Long tail (e.g. court/default): X% — ask how many months this cohort averages

   Explain why this matters: the waterfall determines working capital carrying cost. A unit that resolves in month 0 costs almost nothing to finance. A unit that takes 13 months ties up capital for a year at 15%/yr.

### Group 4: Direct labor activities

8. **4-D Product activities.** For each step in delivering the product, gather:
   - Activity name
   - Which product it belongs to (Communication Product, Working Product, Payment Product, Partner Product)
   - Who does it (role title + estimated hourly rate)
   - How long it takes (minutes per occurrence)
   - Volume driver — what scales this activity? Options:
     - Per unit purchased (happens once per unit)
     - Per inquiry (happens for all inquiries, only a % convert)
     - Per escalation stage (happens only for units reaching that stage — ask for the probability)
     - Fixed per month (amortised across units)

   Work through this iteratively. Start with the main product delivery steps. Prompt: "What happens first when a new customer arrives? Who does it and how long does it take?"

   Keep going until the full delivery chain is covered. Typical IVE venture has 8–15 activities.

### Group 5: Other costs

9. **Consumable resources per unit.** Flat £ estimate for variable non-labor costs (office space, software licences, comms, materials). Ask for a description to label it.
10. **Depreciating assets per unit.** Flat £ estimate for fixed asset depreciation amortised per unit (laptops, platform, equipment). Ask for a description.

### Group 6: Special mechanism (optional)

11. **Is there a design mechanism that changes the cost structure?** (For instance an independent assessment at the point of acquisition — it adds a small cost per unit and reduces the proportion of units falling into the expensive long tail. `[evidence: CS-9]`)
    - If yes: What is it? What cost does it add per unit? What does it change in the waterfall?
    - This becomes the "baseline vs mechanism" comparison in the simulation.

### Group 7: Scale and targets

12. **At-scale volume.** How many units per year at scale? (Can be a range — bear/central/bull)
13. **Target FMOS.** What financial margin of safety are you designing for? Default: 30%.
    - Explain: FMOS = net contribution / revenue per unit. At 30% FMOS, required price = total costs / 0.70.

---

## Stage 2 — Build the simulation

Once all inputs are gathered, build the HTML simulation. Do not ask further questions — generate from the answers.

### File location

Save to: `04-Projects/{venture-slug}/{venture-slug}-fin-sim.html`

Open in browser after saving.

### Design system (apply exactly — no exceptions)

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
      --green-bg: #e6f4ec; --green-text: #166534;
      --yellow-bg: #fef9e6; --yellow-text: #854d0e;
      --red-bg: #fde8e8; --red-text: #991b1b;
      --tag-radius: 3px;
      --font-ui: 'DM Sans', system-ui, sans-serif;
      --font-body: 'Lora', Georgia, serif;
      --width: 1140px;
    }
  </style>
</head>
```

Sharp corners throughout (no border-radius except tags at 3px). No external JS libraries. All calculations in vanilla JavaScript.

### Section A — Input panel

Two-column layout of editable `<input type="number">` fields. Every input has:
- A label (DM Sans 600, small)
- A unit label (£, %, mins, etc.)
- A one-line description in muted text explaining what it represents
- `oninput="recalculate()"` on every field
- A **source line** in 12px muted text below the description: `Source: [tier label] — [note]`
- Tier 4 assumptions (no external source) display a 3px yellow left border on the input group and the label "⚠ Assumption — needs validation"

Group inputs as: Case Economics / Resolution Waterfall / Labor Rates / Special Mechanism (if applicable) / **Customer Stock** / Scale & Targets.

**Customer Stock group (v1.1)** — one block per held stock identified at interview item 2b, labelled with the group name (e.g. "End customers", "Distribution partners"):
- Annual leaving rate (%)
- Cost to win one (£)
- Months to full productivity
- Read-only derived: gross adds in the final ramp year · equilibrium replacement spend (£/yr) · equilibrium penetration

If a group was classified **one-time**, show the block collapsed with the line: *"One-time customer — acquisition charged per unit in running costs. No leaving rate applies."* Show it; do not omit it. The reader must be able to see the classification was made.

Waterfall inputs must sum to 100% — show a live green tick or red warning.

Read-only derived fields (accent blue): weighted avg months to resolution, blended working capital cost per unit.

### Section B — Activity cost build

Title: "Direct cost per unit — activity breakdown"

A table with one row per activity. Columns:
- ▶ toggle (click to expand formula)
- Product component (CP#1, WP#1, etc.)
- Activity name
- Role
- Driver
- Time (mins)
- £/unit (calculated)

When expanded, a detail row shows:
`Formula: [volume_driver_description] × ([time_mins] mins ÷ 60) × £[hourly_rate]/hr = £[result]`

If a special mechanism adds a new activity, highlight that row with a 3px left border in accent blue and label it "Mechanism cost (C3)" or equivalent.

Subtotals at the bottom:
- Total direct labor per unit
- Consumables per unit
- Asset depreciation per unit

### Section C — Unit economics summary

Side-by-side panels: **Baseline** | **With [Mechanism Name]** (omit second panel if no mechanism).

Each panel is a breakdown table:

| Line | £/unit | Definition |
|---|---|---|
| Revenue per unit | | "What the venture receives per resolved unit" |
| − Cost of goods | | "Upfront cash committed per unit before revenue" |
| − Direct labor | | "Sum of all activity costs" |
| − Consumables | | "[description from interview]" |
| − Asset depreciation | | "[description from interview]" |
| − Working capital cost | | "Financing cost on cost-of-goods held on balance sheet from commitment to resolution: cost_of_goods × (cost_of_capital/12) × months, weighted across waterfall cohorts" |
| − Mechanism cost | | "[description from interview]" |
| **Net contribution** | bold | |
| **FMOS** | coloured tag | "Net contribution ÷ revenue. Target: ≥[target_fmos]%" |
| **Required price** | | "Total costs ÷ (1 − [target_fmos]) — the revenue per unit needed to hit the FMOS target" |

FMOS tag: red if < 20%, yellow if 20–29%, green if ≥ 30%.

Below table: annual cases at scale, annual revenue, annual net contribution.

### Section D — Working capital model

Two prominent number cards:
- **Peak WC — baseline**
- **Peak WC — with mechanism**

Formula shown: `Peak WC = (units/month) × cost_of_goods × weighted_avg_months`

CSS-only bar chart showing waterfall distribution. Each cohort is a labelled bar proportional to its %, coloured from green (short) to red (long). No JS charting library.

### Section E — Sensitivity table

Title: "[Key lever] sensitivity" — the mechanism's primary variable (e.g. court rate, default rate, churn rate).

Vary the key lever from its baseline value down to near zero in 6–8 steps. For each row:
- Key lever value
- Avg months to resolution (changes if lever affects waterfall)
- WC cost per unit
- Mechanism cost per unit
- FMOS (coloured tag)
- Required price at target FMOS
- Saving vs baseline

Highlight the row matching the current mechanism input value.

### Section F — Insight panel

Navy panel (`background: var(--panel-bg)`), white text, Lora body.

Dynamic paragraph, recalculates on every input change:

> "At [X]% [lever description], the [mechanism name] reduces FMOS from [A]% to [B]% — moving required price from £[C] to £[D]. The mechanism costs £[E]/unit in [cost description] against a working capital saving of £[F]/unit — a net improvement of £[G] per unit ([H]% of gross margin)."

---

## Calculation rules (implement exactly)

```javascript
// Working capital cost per unit
function wc_cost_per_unit(cohorts, cost_of_goods, annual_rate) {
  const monthly_rate = annual_rate / 12;
  return cohorts.reduce((sum, c) => {
    return sum + c.pct * cost_of_goods * monthly_rate * c.months;
  }, 0);
  // months for each cohort = midpoint of the month it resolves in
  // e.g. month 0 cohort = 0.5 months, month 1 = 1.5 months, court (13mo) = 13 months
}

// Required price at target FMOS
function required_price(total_costs, target_fmos) {
  return total_costs / (1 - target_fmos);
}

// Peak working capital at scale
function peak_wc(units_per_year, cost_of_goods, cohorts) {
  const units_per_month = units_per_year / 12;
  const avg_months = cohorts.reduce((sum, c) => sum + c.pct * c.months, 0);
  return units_per_month * cost_of_goods * avg_months;
}

// Activity cost per unit
function activity_cost(time_mins, hourly_rate, volume_driver_pct) {
  return (time_mins / 60) * hourly_rate * volume_driver_pct;
}

// Fixed cost per unit (module-level costs amortised across transactions)
// fixed_cost_per_module = monthly cost of running one operating module (supervision, infrastructure, overhead)
// transactions_per_module_per_month = capacity of one module
function fixed_cost_per_unit(fixed_cost_per_module, transactions_per_module_per_month) {
  return fixed_cost_per_module / transactions_per_module_per_month;
}
// Note: fixed_cost_per_unit feeds into the unit economics as a separate line — not buried in direct labor.
// It makes visible the relationship between module capacity utilisation and cost floor:
// a module running at 50% capacity has double the fixed cost per unit vs. a module running at 100%.
```

**Module capacity rule:** when building the simulation, always include a module capacity input (transactions per module per month) and a fixed cost per module input. The simulation shows how the fixed cost per unit falls as capacity utilisation rises — this is the primary intrinsic performance curve for module-based ventures.

All displayed numbers:
- £ values: rounded to nearest £1, formatted as £X,XXX
- Percentages: 1 decimal place
- No decimal places on £ values
- Negative values in red

---

---

## IFC Methodology Reference

**Source:** "Running the Right Numbers" — Erik Simanis, Lighting Global / World Bank IFC (2024 manuscript also at Desktop/Temporary/Simanis et al Financial Simulations May 1, 2024.pdf)

### The core insight

Top-down models fail at the base of the pyramid because they start from a market share assumption ("if we capture 5% of 10M customers…"). This embeds a penetration fantasy. Simanis's approach starts from the venture at steady-state operating scale and builds costs from the ground up. Required price is the output, not the input.

### 5-step bottom-up model (Simanis Part II)

**Step 1: Bound the unit and head office**
- Define the customer base (at-scale) and the monthly transaction volume
- Every subsequent cost line is tied back to one of these two anchors — this prevents costs from floating free of volume
- **Step 1(c) — v1.1:** classify each customer and partner group as one-time or held stock, and set a leaving rate, cost to win one, and months to productivity for every held stock. Sizing the unit sizes supply; this sizes demand as a stock. Without it the model prices growth but never prices retention.

**Step 2: Total running costs**
- **Human resources:** For each role, list all activities, their time demands, and whether they scale per transaction or per customer. Sum the total monthly time demands per role. Divide by one staff person's available hours/month (137 hrs in UK, adjusted for NI, pension, benefits). This gives headcount. Multiply headcount × fully-loaded annual cost.
- **Depreciating capital assets:** Amortise fixed assets (equipment, platform) across the useful life and annual transaction volume → cost per unit
- **General running:** Variable non-labor costs (rent, software, comms) per unit

**Step 3: Total investment costs**
- One-time startup costs (licenses, fit-out, working capital seed)
- Expressed as an annual charge by dividing by a payback period, then divided by annual transaction volume → investment cost per unit
- Add required investment return (cost of capital on total invested)
- Add tax provision

**Step 4: Preliminary price / interim margin**
- Preliminary unit price = variable cost per unit + running cost per unit + investment cost per unit
- At this stage: does the price clear the market? If not, the model is telling you the venture doesn't work at this scale — not that the price is wrong.

**Step 5: Whole Cost P&L — finalize via Goal Seek**
- Build a full P&L at the scale defined in Step 1
- Use Goal Seek (or equivalent) to find the price at which net margin hits the target FMOS (≥30%)
- Key formula: `Required price = Total whole costs per unit ÷ (1 − target_FMOS)`
- `FMOS = Net contribution ÷ Revenue per unit`

### Activity driver logic (most-misunderstood element)

Every human activity must have a **volume driver** — the scale parameter that determines how often it happens per unit:

| Driver type | When to use | Example |
|---|---|---|
| Per unit purchased | Happens once for every unit the venture commits to | Generating a contract after purchase |
| Per inquiry (pre-purchase) | Happens for all inquiries; only a % convert to purchased units | Case analysis before buying a claim (2 inquiries processed per purchased claim at 50% conversion) |
| Per stage probability | Only happens when a unit reaches that escalation stage | Settlement negotiation round (probability-weighted) |
| Fixed per month ÷ volume | Happens regardless of volume; amortised | Supervisor training sessions ÷ monthly cases |

**The volume driver math:** If the conversion rate from inquiry to purchase is 50%, then 2 inquiries are processed per purchased unit. An activity that takes 120 mins per inquiry therefore costs 240 mins per purchased unit — a 2× multiplier on labor cost. Failing to account for this is the single most common modelling error.

### How the skill's 7 interview groups map to Simanis's 5 steps

| Skill group | Simanis step | What it captures |
|---|---|---|
| Group 1: Venture & unit | Step 1 | Bounding the unit; revenue per unit |
| Group 2: Cost of goods & capital | Steps 2–3 | Working capital commitment; financing cost |
| Group 3: Resolution waterfall | Step 2 | Time-weighted financing cost per unit |
| Group 4: Direct labor activities | Step 2 (HR) | Activity × time × wage × volume driver |
| Group 5: Other costs | Steps 2–3 | Consumables + asset depreciation |
| Group 6: Special mechanism | Steps 2–3 | Mechanism cost vs. working capital saving |
| Group 7: Scale & targets | Step 1 + FMOS | At-scale volume; required margin |

### Key formulas (implement exactly in the simulation)

```javascript
// Working capital cost per unit
// months = midpoint of the month (month 0 = 0.5, month 1 = 1.5, court = actual months)
wc_cost = cohorts.reduce((sum, c) => sum + c.pct * cost_of_goods * (annual_rate/12) * c.months, 0)

// Required price at target FMOS
required_price = total_costs / (1 - target_fmos)

// FMOS
fmos = net_contribution / revenue_per_unit

// Peak working capital at scale
peak_wc = (units_per_year / 12) * cost_of_goods * weighted_avg_months

// Activity cost per unit (with volume driver)
activity_cost = (time_mins / 60) * hourly_rate * volume_driver_multiplier
// volume_driver_multiplier: 1.0 for per-unit, 1/purchase_rate for pre-purchase inquiries
```

### Key distinctions from top-down modelling

1. **Start from scale, not from penetration.** Define "at-scale" first, then build the cost structure for that scale. Never ask "what % of the market will we take?" — that question invites fantasy.
2. **Whole cost, not variable cost.** Running costs and investment costs per unit are as real as direct labor. A model that omits them systematically underprices.
3. **Volume drivers prevent the penetration trap.** If you skip volume drivers, activities that happen pre-purchase (case analysis, customer onboarding) appear cheaper than they are — because you're not accounting for the funnel above the purchase event.
4. **Working capital is a cost line, not a note.** The financing cost of holding inventory or claims from commitment to resolution must appear in the unit economics, not in a separate capital model.

---

### The two-period framework — IRR requires a terminal value

**Source: Deevabits AECF Debrief (Simanis / TIL, Jan 2021)**

FMOS (unit economics) is the first gate — it tests per-unit viability. But venture-level return (IRR) requires a second calculation that FMOS alone cannot provide.

**Two free cash flow periods:**

| Period | What it is | Cash flow profile |
|---|---|---|
| **Investment period** | Ramp from 0 to at-scale customer base | Negative in early years (WC losses), recovering as volume grows. **v1.1:** the base loses members every period as well as gaining them — charge acquisition on gross adds, not net |
| **Equilibrium period** | Steady-state at-scale customer base as a perpetuity | Stable positive cash flow = terminal value, **net of standing replacement spend (v1.1)** |

**The critical finding (Deevabits case):** "The greatest source of cost is financing the large cumulative shortfall of operating cash caused by customer financing. The equilibrium period (translated into a terminal value) generates *all* free cash flows for the venture."

This means: a financial model without a terminal value will always understate IRR — and make early-year losses look unrecoverable. The investment period rarely recovers on its own. The perpetuity is where the venture's economics become visible.

**Terminal value formula:**

```
TV = Equilibrium monthly CF × 12 ÷ perpetuity discount rate
```

Where:
- **Equilibrium monthly CF** = net cash flow at at-scale penetration × equilibrium penetration factor (usually 100% of at-scale, but can be less if sustained penetration is below design penetration)
- **Perpetuity discount rate** = required IRR (or WACC if known)
- **TV is added to the last month of the investment period** in the IRR cash flow array

**IRR cash flow array:**

```javascript
const irrFlows = [
  -totalEquity,                                  // t=0: total capital in
  ...netCash.slice(0, M - 1),                    // t=1 to M-1: investment period CFs
  netCash[M - 1] + terminalValue                 // t=M: last period CF + TV
];
const monthlyIRR = calcIRR(irrFlows);            // Newton-Raphson
const annualIRR  = Math.pow(1 + monthlyIRR, 12) - 1;
```

**Always show two IRR figures:**
- IRR including terminal value (the correct P2P number — use for FIT gate)
- IRR without terminal value (investment period only — diagnostic, shows how dependent the return is on the perpetuity)

**At-scale vs equilibrium penetration:**

| | What it is | Where it's used |
|---|---|---|
| **At-scale penetration** | The design assumption — the customer base the architecture is built for | Investment period cash flows, cost floor |
| **Equilibrium penetration** | The sustained rate after the investment period ends — may be the same or lower than at-scale | Terminal value calculation |

Do not use at-scale penetration in the terminal value if the venture cannot sustain it. Using at-scale in the TV compresses IRR by inflating the perpetuity.

**v1.1 — two corrections to how equilibrium is treated.**

**(a) Equilibrium scaling cost is not zero by default.** The source method sets it to zero on the grounds that "natural churn is offset by natural replenishment." That sentence is withdrawn. Holding a customer base still is a standing cost:

```javascript
equilibrium_replacement_spend = leaving_rate_annual * at_scale_base * cost_to_win_one
```

Run this for every held stock from interview item 2b — customers and partners. Deduct it from equilibrium cash flow **before** computing TV. It may be set to zero, but only on named evidence: organic inbound, a genuine one-time-customer architecture, or a base that demonstrably renews at no cost. "The method says so" is not evidence.

This is the single highest-leverage line in the whole model. The Deevabits finding is that the equilibrium period generates *all* the free cash flow. So an unpriced replacement cost is not a P&L rounding error — it is a permanent overstatement of the number the entire valuation rests on.

**(b) Derive the equilibrium base — do not type it in.** Equilibrium penetration should fall out of the leaving rate and the replacement spend the venture will actually fund:

```javascript
// If the venture funds full replacement, the base holds at design scale.
// If it funds less, the base settles where the maintained spend supports it.
sustained_base = maintained_replacement_spend / (leaving_rate_annual * cost_to_win_one)
equilibrium_penetration = Math.min(1, sustained_base / at_scale_base)
```

Setting it to 100% by hand is a guess. Setting it to a prudent-feeling haircut is also a guess. Both are guesses dressed as inputs. Derive it, show the derivation, and let the leaving rate do the work.

**Two types of working capital:**

| Type | What it is | Cost layer |
|---|---|---|
| **WC to fill losses** | Cash needed to fund the cumulative operating shortfall during the investment period ramp | IC — equity requirement |
| **WC for customer financing** | Cash committed per unit from purchase to settlement; `PVC × (rate/12) × weighted_avg_months` | IC — dominant cost driver for capital-commitment models |

Both are IC. Model them separately. For ventures that purchase assets upfront (claims, loans, inventory), WC for customer financing is typically the largest single cost line — larger than all RC combined.

**SC is usually significant:**

SC (Startup & Scaling Cost) = CapEx + Development & launch costs + customer acquisition costs. The Simanis training material explicitly notes: "customer acquisition costs are usually significant." Do not model SC as a footnote.

**v1.1 — charge acquisition on gross adds, and do not flatten it with the shortcut formula.**

The shortcut `SC per unit = total SC ÷ investment period months ÷ monthly volume at scale` divides by volume **at full size**. But acquisition spend happens early, when volume is low. The shortcut therefore spreads early spend across a large late base and makes the ramp years look cheaper than they are. Worse, it prices the acquisition of **net** growth only — it never asks what it costs to replace the customers who left.

For every held stock identified at interview item 2b, run the acquisition cost period by period:

```javascript
// Period-by-period customer stock — both flows, not just the inflow
leavers(t)    = leaving_rate_monthly * opening_base(t)
gross_adds(t) = net_adds(t) + leavers(t)          // what you must actually win
acq_cost(t)   = gross_adds(t) * cost_to_win_one
closing_base(t) = opening_base(t) + gross_adds(t) - leavers(t)
```

Rules:
1. **Charge `acq_cost(t)` in the period it occurs.** Do not amortise it across the investment period. It is real cash in a real month, and it lands in the cash grid alongside staged HQ burn.
2. **Apply months-to-productivity.** A partner won in month 30 does not deliver a full year of volume in year 3. Ramp its contribution; do not switch it on at full rate.
3. **Run it on partner stocks too**, not only end customers. Where a channel delivers a share of volume, model the channel base as its own stock with its own leaving rate.
4. **Keep the shortcut only for CapEx and one-time build costs** — platform, legal setup, fit-out. Those genuinely are one-off and genuinely do amortise.

**One-time-customer ventures are the exception, and the exemption must be earned.** If item 2b classified the base as one-time, acquisition is a per-unit running cost and this whole block does not apply — replacement is priced on every transaction by construction. State that in the model output so the reader knows it was decided, not forgotten.

**GIGO warning:** The P2P tools tell you *what* a company is doing, not *why*. A deeply-flawed business model can unwittingly be made to look good in the financial model. The AOM/CTM activities must be grounded in the confirmed operational structure — not constructed to justify a number.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-fin-sim-custom/SKILL.md` to modify
- Structure reference: the field list and check-cell layout stated in this skill. Do not read another venture's simulation for levels — a simulation built on a different operating model carries that model's unit counts and volumes. `[evidence: VA-BS1]`
- IFC paper: `/Users/tommanuel/Downloads/IFC Path to Profitability At Scale Financial Modelling instructions.pdf`
- Simanis manuscript (2024): `Desktop/Temporary/Simanis et al Financial Simulations May 1, 2024.pdf`
- Framework: Integrative Venture Engineering (Simanis / Cornell MCL)
- Related skills: `/verify-balm-custom` (BALM completeness check), `/theory-of-change-custom` (TOC design)
