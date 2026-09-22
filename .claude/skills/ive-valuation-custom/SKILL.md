---
name: ive-valuation-custom
description: IVE Venture Valuation — values an architected venture for two real users at once. (1) An investor deciding whether to back it and at what price; (2) an owner deciding what to invest going forward — what to spend next to de-risk or build, and what return that unlocks. Runs over the CDR at the end of architecting, or on any venture with at least F1 (R1–R3) economics. Bridges architecture → ranged unit economics → discounted enterprise-value range. Outputs an HTML valuation, never a single point.
---

# IVE Venture Valuation

**Model routing (mandatory default):** per `.claude/skills/shared/ive-model-routing.md` — methodology decisions, range judgments and lens verdicts stay in-session; dispatch the HTML document production to an Agent-tool subagent with `model: "opus"` and a self-contained prompt (confirmed inputs, output path, format spec). Verify the produced numbers in-session before presenting. Skip only if Tom says "run inline".

**Purpose:** Turn an architected venture into a defensible **valuation range** that serves two real decisions — an investor's (back it, at what price?) and an owner's (what is worth investing *next*, and what return does it unlock?). The skill is a clean bridge: **architecture → ranged unit economics → discounted enterprise value**, reported through two lenses, with a forward capital-allocation engine that ranks the next investments by value-of-information.

**When to run:** At the end of the architecting process, over the CDR (Complete Design Record) — once the BALM is consistency-audited and the financial simulation reflects the confirmed architecture. It can run earlier on any venture with at least **F1 economics confirmed (R1 cost floor, R2 value ceiling, R3 working capital)** — but the valuation is then explicitly partial (SC/IC layers and F2/F3 retention are not yet priced), and the output says so.

**Output:** A single-file HTML valuation document — SCQA header with the enterprise-value range as the BLUF; a ranged inputs table; the architecture→economics→valuation bridge; two valuation lenses; the owner-forward value-of-information ranking; a sensitivity/tornado; and an explicit statement of what the number can and cannot support.

**Do not run this to produce a number to defend.** Run it to find where the value is uncertain and what it costs to settle that uncertainty. A valuation that hides its ranges is the failure this skill exists to prevent.

---

## IVE framework — where this skill fits

**Integrated Venture Engine (IVE)** is a structured process for building new Core Business Architectures. Source: the IVE canon — Simanis, E. et al. (2021), Cornell SC Johnson College of Business, and the co-authored papers 2023–2025 (Simanis, Manuel et al. 2023; Simanis et al. 2024; Simanis 2025). Full list at the foot of this skill or in `architect-custom`.

**Three nested levels of commercial architecture:**

| Level | What it is |
|-------|-----------|
| **Core Business Architecture (CBA)** | The logic that sets both the cost curve and value curve for an industry. No single company owns it. |
| **Business Form Factor (BFF)** | The essential shape product and operations take given a CBA. |
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

**→ This skill: IVE Venture Valuation** — runs over the CDR after the architecture is built, verified, and the financial simulation (`/ive-fin-sim-custom`) is current. It consumes the model stack (CTM → AOM → ARM → Fin-Sim) and the verify-venture SOUND score; it produces no architecture of its own. It is a reading of the architecture, priced.

**Design principle — value at-scale, not at launch.** Enterprise value lives in the equilibrium/perpetuity period, not the investment-period ramp (Deevabits finding, Simanis/TIL 2021): the perpetuity generates *all* free cash flows; the investment period rarely recovers on its own. Value the architecture operating at the scale required to pay back all capital at the PCO's required IRR. Launch-phase constraints are sequencing problems, not valuation problems.

---

## Two standards baked in (Forge WS1 backlog — state them every run)

These are not optional. The valuation OUTPUT and every input obey them.

### VA-32 — ranges, not points (HARD)

> Every figure is `[low – high]` plus a credibility note. The valuation output is a range. Reject any bare point estimate.

For each input the credibility note has three parts:
1. **Anchor** — where the midpoint comes from (a model line, a benchmark, a confirmed gate clearance, reasoned logic).
2. **Why these endpoints** — what makes the low the low and the high the high. The band must be *reasoned*, not a ±X% cosmetic spread.
3. **What breaks the band** — the result that would push the figure outside `[low – high]` entirely (this becomes a tornado / break-point candidate).

Compute **FMOS and enterprise value at both ends of the band** — never at the midpoint alone. The headline is the EV range; the midpoint, if shown at all, is shown smaller than the endpoints.

### VA-31 — emergent ≠ unknowable; estimate now, confirm later

> WTP and other behavioural inputs are not surveyed and not treated as known facts. They are **estimated by the quality of requirement-solving** — the architecture predicts the range; a pilot later confirms it.

This is the warrant for the WTP and volume ranges. State it explicitly in the output:

- The valuation's confidence is a **direct function of how soundly the requirements were solved.** A venture whose requirements were adversarially verified (high `/verify-venture-custom` SOUND score, both FMOS gates clear, R2 Key Monetizable Cost grounded in a cited theory) earns a **tighter, more credible** WTP range than one resting on assumed inputs.
- Cite the warrant by name. The WTP-range credibility note must read, e.g.: *"Range warranted by: SOUND 87, R2 FMOS gate clear at 25%, KMC grounded in [theory]. Tightened accordingly."* or, where the warrant is weak: *"Range wide: R2 KMC is a Tier-4 assumption, SOUND not yet run. Band cannot be narrowed until verified."*
- An emergent input is therefore **estimated, not unknown.** Do not refuse to value it; do not pretend it is a fact. Estimate the range from the architecture's soundness, and tag it for pilot confirmation.

---

## Honesty discipline (standing instruction — applies to every figure)

- **Flag every assumed / placeholder figure in red** (`--red` token, see Output). A reader must see at a glance which numbers are evidenced and which are hypotheses dressed as facts.
- **Distinguish fact vs inference vs assumption** in the inputs table — a dedicated column, not a footnote. "X is measured" / "X follows from Y" / "X is assumed here" are not interchangeable.
- **Never present a valuation built on unfielded inputs as decision-grade for deploying capital.** State plainly what the number CAN support (a go/no-go on *funding validation* — i.e. should the owner spend to field the load-bearing assumptions) versus what it CANNOT (deploying *growth/build* capital, or quoting a price to an external investor as if settled). This distinction is mandatory in the closing section.

---

## Evidence tiers (T1–T4) — apply to every input

Same tier system as the architecture-assumption audit and the fin-sim. Every input carries a tier; tier drives both the credibility note and the de-risked lens.

| Tier | What it is | Effect on valuation |
|------|-----------|---------------------|
| **T1 — Primary data** | This venture's own field research, pilot, or live operations | No de-risking discount; tightest band |
| **T2 — Published statistics** | Government / regulatory / court / academic data | Light discount; band reflects source variance |
| **T3 — Industry benchmark** | Comparable venture or named expert estimate | Moderate discount; band reflects analogue distance |
| **T4 — Reasoned assumption** | No external source; logic + stated constraints | **Full de-risking discount** in Lens 2; widest band; first in the VoI queue |

**Rule:** the gap between the architecture-conditional lens and the de-risked lens is driven almost entirely by the T4 inputs. That gap is not noise — it *is* the value of validation, and it is what the owner-forward engine monetises.

---

## Field-hardened rules (v1.1 — from first runs on Forge + Calmly, 6 Jun 2026)

Apply throughout. Each fixed a real stumble on a live venture.

1. **Cost-floor specification — state which floor feeds the valuation.** A stack often carries two legitimate floors (a thin "layer/operations-only" floor that excludes a major cost line, and the full floor). **An excluded cost layer makes the EV an UPPER BOUND, not a midpoint — build the range asymmetric** (low case pairs the bad ends; the headline is a ceiling). If the architecture changed units mid-design (per-claim → per-transaction), pick the operative unit and never silently combine the two economics.
2. **Missing discount rate — standard fallback.** If no IRR exists anywhere in the stack (the fin-sim that would set it may be a coverage gap), default to the **IVE pre-revenue rate (30%)**, flag it red, run 25–40% sensitivity, AND add "build the fin-sim to set the real IRR" as a value-of-information line. Do not silently pick a rate.
3. **Absent SOUND score — verification is itself a top VoI move.** If `/verify-venture-custom` has not been run, VA-31's band-tightening has nothing to bite on: state loudly that the whole valuation is structurally *pre-verification* and the band stays wide. Then place running `/verify-venture-custom` **at or near the top of the value-of-information ranking** — it re-rates every band at once, so it is often higher-leverage than fielding any single input.
4. **Terminal value — apply an explicit retention/equilibrium-penetration haircut, not just a flag.** When at-scale retention is unevidenced, multiply TV by an explicit factor (e.g. 0.45–0.85) and show it. Also surface when 100% of value is perpetuity-dependent (investment-period flows ≈ zero/negative) — that is a material risk reading, not a footnote.
5. **Value-of-information: the rank order is the robust output, not the £Z magnitudes.** The £-unlocked figures are themselves estimates; present them as directional and lead with the ranking. The decision the owner makes is *sequence*, which survives even when the magnitudes are soft.

---

## The core method — architecture → economics → valuation

Run these six steps in order. Each is a Section in the workflow below.

1. **Assemble ranged unit economics from the architecture.** Cost floor (four layers PVC · RC · SC · IC), value ceiling (WTP = R2 Key Monetizable Cost), at-scale volume, CAC. Every input is a `[low – high]` range + credibility note (VA-32) + evidence tier (T1–T4).
2. **Build to at-scale cash flow.** Revenue (price range × volume range) → contribution → EBITDA / operating cash, computed at both the low case and the high case.
3. **Discount at the PCO's required return.** Use the IRR the PCO set (for Forge: **30%**). Produce an enterprise-value **range** via the two-period framework (investment period + terminal value), never a single point.
4. **Report two valuation lenses** (both, always).
5. **Run the owner-forward value-of-information engine** — rank the next investments by £-value-unlocked per £-spent.
6. **Sensitivity / tornado** — the 3–4 assumptions that move the valuation most, and the break point.

---

## Section 1 — Assemble ranged unit economics

Read the current model stack for the venture (do not re-derive it — read it):

```
04-Projects/{venture-slug}/.../{venture}-fin-sim-at-C[N].html   (or latest fin-sim)
04-Projects/{venture-slug}/.../{venture}-aom-at-C[N].html
04-Projects/{venture-slug}/.../{venture}-ctm-at-C[N].html
04-Projects/{venture-slug}/.../{venture}-cdr-package-*.html      (if CDR exists)
```

Also read the latest `/verify-venture-custom` SOUND score and FMOS gate clearances — these are the **warrant** for the WTP band (VA-31).

Pull these into a ranged inputs table. For **every** line: low, high, midpoint (smaller), evidence tier, fact/inference/assumption, credibility note (anchor / endpoints / break).

| Input | Source in stack | Notes |
|-------|-----------------|-------|
| **Cost floor — PVC** (cost of goods / unit) | Fin-Sim COGS line | Per-unit cash committed before revenue |
| **Cost floor — RC** (running: labour + operating) | AOM activity build × rates | Sum of activity costs/unit + consumables + depreciation |
| **Cost floor — SC** (CapEx + dev + customer acquisition) | Fin-Sim investment costs; CAC | "Acquisition costs are usually significant" — do not footnote |
| **Cost floor — IC** (working-capital financing) | Fin-Sim WC model | `PVC × (rate/12) × weighted_avg_months`; dominant for capital-commitment models |
| **Value ceiling — WTP** | R2 Key Monetizable Cost | Estimated by R2 soundness (VA-31), **not** surveyed |
| **At-scale volume** | AOM × PCO penetration | Per-segment by F3 (see registry TAM note); monolithic only through F1 |
| **CAC** | F2 attraction design / benchmark | Often T3/T4 — flag |
| **Cost of capital / required IRR** | PCO investment parameters | Forge: 30% |

If a layer is not yet designed (e.g. SC before R3, or F2/F3 retention before those challenges), mark it `[REQUIRES R[N]]` in red and **exclude it** — then say in the closing section that the valuation is partial for that reason. Do not invent it.

---

## Section 2 — Build to at-scale cash flow (low case and high case)

Compute the full at-scale annual cash flow at **both** ends of the band:

```
Revenue/unit      = WTP (price)                 [low / high]
− Cost floor      = PVC + RC + SC + IC          [high / low]   ← worst pairing for low case
= Net contribution/unit                          [low / high]
× at-scale volume                                [low / high]
= Annual net operating cash                      [low / high]
```

**FMOS at both ends** — canonical cost-denominator formula, single source of truth `Forge/WS1/criteria-registry.md`:

```
FMOS = (Price Ceiling − Cost Floor) / Cost Floor
```

Do not use `(Price − Cost) / Price` — that is the gross-margin / price-denominator metric and understates the figure. Report the Phase-II band: **PASS ≥ 60% · BORDERLINE 25–59% · FAIL < 25%** (the whole-architecture gate, since this runs over the CDR). If running pre-CDR on F1 only, note the per-requirement band (≥25% PASS) applies instead and the result is indicative.

**Low case = pessimistic pairing.** The low EV case pairs low WTP × low volume × high cost. Do not average; pair the bad ends together — that is the case the owner must survive.

---

## Section 3 — Discount to an enterprise-value range

Two-period framework (Deevabits / Simanis–TIL 2021). FMOS gates per-unit viability; venture value needs the perpetuity.

```
Investment period:  ramp 0 → at-scale; cash negative early (WC + losses), recovering
Equilibrium period: steady-state at-scale as a perpetuity = terminal value

TV = Equilibrium annual net cash × equilibrium-penetration factor ÷ required IRR
EV = NPV(investment-period flows @ required IRR) + PV(TV)
```

Compute EV at **both** ends of every load-bearing band, then report the **EV range** `[EV_low – EV_high]`. Always show two IRR-style readings for transparency: EV **with** terminal value (the decision number) and EV from the investment period **only** (diagnostic — reveals how perpetuity-dependent the value is). Flag the **equilibrium-penetration** assumption explicitly: using at-scale penetration in the TV when the venture cannot sustain it inflates the perpetuity and overstates EV.

The headline EV range is the BLUF. A single point is a VA-32 violation — reject your own output if it collapses to one.

---

## Section 4 — Two valuation lenses (report both, always)

| Lens | What it answers | How computed |
|------|-----------------|--------------|
| **Lens 1 — Architecture-conditional value** | What the venture is worth **IF the requirements are soundly solved** — i.e. behaviour lands inside the model range. The upside the architecture stands behind (the IVE promise). | EV range from Section 3 with each input at its architecture-predicted band, T-tier untouched |
| **Lens 2 — Risk-adjusted / de-risked value now** | What it is worth **today**, discounting for unfielded assumptions. | Same EV computation, with T4 (and weak-T3) inputs pushed toward their pessimistic end and/or probability-weighted by the chance the assumption fails to confirm |

**The gap between Lens 1 and Lens 2 IS the value of validation.** State the gap in £ explicitly. It is the prize the owner-forward engine (Section 5) allocates against: every £ of validation spend that collapses a T4 band toward T1 moves Lens 2 toward Lens 1.

Frame for both users:
- **Investor:** Lens 2 is the defensible price today; Lens 1 is the upside they are buying optionality on. The spread tells them how much of the price is promise versus proof.
- **Owner:** the spread is the budget rationale — closing it is the return on validation spend.

---

## Section 5 — Owner-forward value-of-information engine (the differentiating feature)

This turns the valuation from a number into a **forward capital-allocation tool**. For each load-bearing assumption (rank candidates via `/architecture-assumption-audit-custom`: sensitivity × evidence gap):

For each assumption Y:

```
Spend £X  to field Y
  → collapses Y's range from [a – b]  to  [c – d]   (expected post-test band)
  → moves risk-adjusted (Lens 2) value by £Z
VoI ratio = £Z / £X     (value unlocked per £ spent)
```

Rank the next investments by the VoI ratio, descending. The top of the list is what the owner should spend on **next** — the cheapest test that moves the most value. Present as a ranked table:

| Rank | Assumption (Y) | Current tier | Field it by (test) | Cost £X | Band before → after | Δ Lens-2 value £Z | VoI = £Z/£X |
|------|----------------|--------------|--------------------|---------|---------------------|-------------------|-------------|

Tie the ranking explicitly to `/architecture-assumption-audit-custom` (which already ranks assumptions by FMOS sensitivity × T-tier gap). This skill adds the **£-value-per-£-spent** layer on top of that ranking. If the audit has been run, read its output; if not, run the sensitivity here (Section 6) and derive the ranking from it.

**This is the owner's answer to "what should I invest in next?"** — not "build the product" but "spend £X fielding assumption Y, because it unlocks £Z of provable value, which is the precondition for deploying build capital safely."

---

## Section 6 — Sensitivity / tornado and the break point

- **Tornado:** the 3–4 assumptions whose bands move EV the most, drawn as a CSS-only horizontal bar chart (longest bar = most sensitive, at top). Each bar spans the EV at the assumption's low end to its high end.
- **Break point:** for each top driver, name the value at which EV goes to zero — or, more usefully, the value at which the venture's **return falls below the required IRR** (the real kill line for an IVE venture, since a positive-but-sub-IRR EV still fails the investment test). State it as: *"EV crosses below the 30% IRR hurdle when [assumption] reaches [value] — that is the break point."*
- The top tornado drivers and the top VoI-ranked assumptions should substantially overlap. If they do not, say why (a highly sensitive input that is cheap to leave unfielded, or an expensive test on a low-sensitivity input).

---

## Output spec — HTML valuation document

Save to: `04-Projects/{venture-slug}/.../{venture}-valuation-YYYY-MM-DD.html`. Open in browser after saving.

**Structure (Pyramid / SCQA — this is a decision document):**
1. **SCQA header with BLUF** — the enterprise-value range in one line at the top: *"[Venture] is worth £[EV_low] – £[EV_high] if soundly solved (architecture-conditional); £[Lens2_low] – £[Lens2_high] de-risked today. The £[gap] gap is the value of validation."* Situation → Complication → Question → Answer, answer first.
2. **Ranged inputs table** — every input: low / high / midpoint, evidence tier (T1–T4), fact·inference·assumption column, credibility note (anchor / endpoints / break). Assumed figures in red.
3. **Architecture → economics → valuation bridge** — the Section 1–3 chain made visible: cost floor (4 layers) → at-scale cash flow → discounted EV range.
4. **Two valuation lenses** — side-by-side panels; the £ gap called out between them.
5. **Owner-forward VoI ranking** — the ranked table from Section 5.
6. **Sensitivity / tornado** — CSS-only bar chart + break points.
7. **What this number can and cannot support** — the honesty-discipline closing section: go/no-go on funding validation (yes) vs deploying growth capital (not until T4 inputs fielded). State which layers, if any, are `[REQUIRES R[N]]` and excluded.

**House HTML design system (custom CSS — NO government styling). Key tokens:**

```
--bg #f5f4f1   --surface #ffffff   --text #0f1923   --text-muted #718096
--accent #1f4fa8   --border #dde1e7
--panel-bg #0f2744 (navy — use for the headline EV-range BLUF panel, white text)
warning block: left-border 4px #d4820a on #fff8e6 (use for the can/cannot-support caveat)
--red #c0392b   ← every assumed / placeholder figure, in red
```

- Google Fonts via CDN: **DM Sans** (400/500/600) as the **primary** font — UI, headings, tables, numbers (this is a data-heavy document) — and **Lora** (400/600) for any prose passages (the SCQA narrative, the lens explanations).
- Container `max-width: 960px`, centred, `background: var(--surface)`, sharp corners (no border-radius except 3px tags).
- Tables: DM Sans 600 headers, `border-bottom` on the header row. FMOS / VoI tags use the tag colour variants (green ≥ gate, yellow borderline, red fail).
- All charts CSS-only — no JS charting library.
- Copy defaults per house style: plain English, active voice, short sentences, minimal capitalisation, numerals from 10, no exclamation marks, em dashes spaced.

---

## Process discipline

- **Read the model stack; do not re-derive it.** If the fin-sim is stale relative to the CDR, stop and flag it — value a current model or none. A valuation off a stale model is GIGO.
- **No bare points, ever.** If any headline figure collapses to a single number, the run has failed VA-32. Re-open the band.
- **Cite the WTP warrant.** The WTP band's credibility note must name the SOUND score and gate clearances (VA-31). If they do not exist yet, the band stays wide and the output says the valuation is pre-verification.
- **The two users are both real.** Do not write only for the investor (a price) or only for the owner (a to-do list). Every run reports the EV range (investor) *and* the VoI ranking (owner).
- **Distinguish fact / inference / assumption** in the inputs table, and red-flag every assumption. Never let an unfielded input pass as decision-grade for build capital.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-valuation-custom/SKILL.md` to modify
- Invoke as: `/ive-valuation-custom`
- **FMOS formula — single source of truth:** `Forge/WS1/criteria-registry.md` — `FMOS = (Price Ceiling − Cost Floor) / Cost Floor`. Do not redefine locally.
- **Standards:** VA-32 (ranges not points) and VA-31 (emergent ≠ unknowable) — Forge WS1 backlog
- Related: `/ive-writeup-custom` (the narrative CDR write-up) · `/ive-fin-sim-custom` (the model this skill reads) · `/architecture-assumption-audit-custom` (the assumption ranking the VoI engine builds on) · `/architect-custom` (the design front door)
- Two-period / terminal-value framework: Deevabits AECF Debrief (Simanis / TIL, Jan 2021)
- IVE source: Simanis, E. et al. (2021), Cornell SC Johnson College of Business; *Built to Hold* (2025) for the FMOS gates
