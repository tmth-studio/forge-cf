---
name: balm-pco-custom
description: IVE Prime Commercial Opportunity session — the upstream prerequisite to all BALM requirements. Determines the broadest credible use case before any segment or product choice is made. Prevents the beachhead trap. Outputs: PCO statement, investment parameters, use case shortlist, financial directionality verdict.
---

# BALM PCO — Prime Commercial Opportunity

**Purpose:** Isolate the broadest use case that can most credibly generate the at-scale cash flows needed to pay back all required investment capital at a competitive rate of return — before any segment-specific, product-specific, or requirement-level choices are made.

**When to run:** At the very start of BALM design work — before R1, before R2, before any customer research. The PCO is the scope-setter. Every downstream decision is constrained by the PCO verdict. If the PCO is wrong, the requirements will be solved for the wrong opportunity.

**Output:** A PCO statement — who, the condition they face, and why it has the right financial shape — together with investment parameters, use case shortlist, and a directionality verdict on financial viability.

**Handoff to:** R1 (Circumvent At-scale Cost Bottleneck) — the CLO identification and Workaround Strategy are designed for the PCO, not for a beachhead segment.

---

## ⛔ Literal-execution discipline — no silent inference (read first)

This skill is a method, not a brief to be filled in by the runner. Execute it as written. Do not substitute your own judgement for inputs the user has not supplied. The following are hard rules — they override any instinct to "be helpful" by guessing.

- **Every required input is elicited, sourced, or proposed-and-confirmed — never silently invented.** Investment period, required IRR, at-scale geography, relevant industry, penetration rate, candidate breadth, and any threshold must be either stated by the user, taken verbatim from a cited source in this skill, or **proposed by the runner as an explicitly flagged assumption that the user confirms before it is used** (see Step 1). The runner must never silently infer, default, or invent any of them. "Global", "2.5%", "£100M" — none of these may appear as settled values unless the user said so, a cited source carries them, or the user confirmed the runner's flagged proposal.
- **Method defaults are stated and confirmed, never applied silently.** Where the method or its source genuinely carries a default value — for example 2.5% penetration, 8% terminal discount, 10% net margin — the runner states it explicitly as "method default per [source]" and gets the user's explicit confirmation before using it. A default is a proposal, not a fact.
- **No invented screening thresholds.** The runner must not introduce a revenue, enterprise-value, or "Prime" bar of its own. The screen's required-price line is *derived* from the user-confirmed investment parameters via the Step 4 calculation — it is not a number the runner makes up. The only gates that apply are the method's own: the loss-to-price ratio (Step 4) and the market-creation-margin / workaround-plausibility gates. No other threshold may be introduced.
- **The runner does not select the PCO.** It presents the completed Step 4 grid and the user selects in Step 5. The runner may recommend a use case with reasoning, but the selection is the user's. Do not declare "X is the PCO" on the user's behalf.
- **Every estimated or placeholder number is visibly flagged as unvalidated.** House rule: flag invented stats visibly. Mark any figure that is an estimate, assumption, or placeholder — for example with `⚠ UNVALIDATED` or red — so the user can systematically replace it. Never present an assumed number as if it were established.
- **If a required input is missing, propose it and stop for confirmation.** Do not proceed on an *unconfirmed* value. The runner drafts a best proposal with its basis, flags it `⚠ ASSUMED`, and waits. A missing investment parameter or penetration rate is a hard stop on *proceeding* — it is not a hard stop on *proposing*.

This discipline sits alongside — and does not replace — the **Path A / Path B routing** (Step 2) and the **Path B contamination guard** (Step 2). Those remain in force at every step. The contamination guard forbids importing a *solution*; this section forbids inventing an *input* or a *decision*. Both apply.

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

**→ This skill: PCO — Prime Commercial Opportunity** (entry point; runs before R1, R2, R3, and all downstream requirements)

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design. A cost that seems large at 50 units is often trivial against the same cost at 50,000 units.

---

## Why the PCO comes first — the beachhead trap

Most ventures begin with a beachhead market: a segment where the founder has existing contacts or domain familiarity. The logic is pragmatic — faster access, lower cost of early sales.

The problem is structural. Early adopters from a beachhead are rarely representative of the broader market. The venture optimises for them, embeds assumptions built for them, and finds itself unable to cross to the wider market it needs to sustain at-scale economics. This is Moore's chasm — not a distribution failure but an architectural one.

The PCO process is the antidote. It defines the broadest credible market before any segment-specific choices are made.

**The financial rationale:** by eliminating otherwise avoidable pivots, a rigorous PCO reduces the cash-out required and increases the probability of commercial success — both of which improve the venture's expected net present value.

**The discipline:** do not bound both sides of the equation simultaneously. Do not choose the type of problem you are solving and the type of solution you are offering before evaluating whether the combination can generate at-scale returns. The solution space stays open until the commercial logic of the problem space is established.

---

## IVE framework source

Simanis, E., Samani, S., Burnett, P., & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* IVE Programme Materials. Cornell SC Johnson College of Business.

Extended with: The Intrapreneur Lab, "From Social Problem to Market Opportunity," Barclays Intrapreneur Lab, November 2021. IVE Venture Training Studio, Half-Solved + Cornell MCL, July 2025.

**IVE's Design Principle 01:** "Isolate the Prime Commercial Opportunity — reduce venture search space to the broad use case that can most credibly generate at-scale revenues to pay back all required investment capital at a competitive rate of return. Scope before depth."

---

## PCO Definition

> "The broadest possible use case for a core functionality OR the broadest possible impact case for a pervasive societal problem that can most credibly generate the at-scale cash flows needed to pay back all required investment capital at a competitive rate of return."

---

## Choose the biggest PCO possible — breadth is the default

The PCO is a **scope-setter for field research, not a segment commitment.** Its job is to make sure infield research covers the widest credible set of use cases, so the *most likely* one is discovered on evidence rather than assumed up front. Narrowing to a single use case at this stage re-introduces the beachhead trap the PCO exists to prevent.

So the default is **maximum breadth**: select the broadest credible combination of use cases that survives the directionality screen — not the single highest-scoring one. **Combine compatible cases rather than choosing between them.** When in doubt, include.

**Why breadth here is not speculative — the KMC backstop.** Breadth at PCO does not commit the venture to serving everyone. R2 (Eliminate Customers' Value Bottleneck) isolates the **Key Monetizable Cost (KMC)** — and in doing so selects only the customers who actually carry a monetizable cost large enough to pay for. The real customer-qualification happens at R2, downstream and on evidence. A broad PCO simply guarantees R2 has the full population to qualify *from*; it pre-commits to none of them.

The directionality screen (Step 4) therefore does **one job only**: exclude the *obviously* unviable — a loss too small to ever carry any price, or no workaround conceivable even in principle. Everything that clears that low bar stays in the PCO. Do not use the screen to rank-and-pick a winner; use it to drop the dead and keep the rest.

A use case is excluded from the PCO **only if it fails on its own terms** (no monetizable loss, or no conceivable workaround) — never because another case looks bigger, cleaner, or better-fitted to the architect's channel. Channel fit and relative attractiveness are R2-and-later judgements, made on evidence; they are not PCO-stage exclusions.

---

## Step-by-step process

### Step 1 — Define investment parameters

Before evaluating any use case, set the financial parameters that define what "credibly generates at-scale cash flows" means for this venture. These parameters bound the search.

**Propose-and-confirm is the standing mode (Tom's instruction, 27 Aug 2026).** The runner does **not** ask for these four cold. It drafts all four as explicit proposals — each with its basis and each flagged `⚠ ASSUMED` — and presents them as one confirm-or-override block. The user confirms, edits, or replaces. Only confirmed values may be used in the Step 4 screen.

**Why the mode changed:** the failure this rule guards against is a runner *silently* inventing parameters, so the required-price line rests on numbers the user never saw. Proposal-with-confirmation removes that risk while removing the friction of a cold interrogation. It is the same pattern the method already applies to the 2.5% penetration default: a default is a proposal, not a fact.

Draft and present all four:

- **Investment period:** start date to target scale date (the window in which the venture must demonstrate viability) — runner proposes from the venture's context, user confirms
- **Required IRR:** the rate of return the venture must clear. **It is a requirement imposed by whoever allocates the capital — the CFO, the CEO, the investment committee, or the fund's LPs — not a target the venture sets for itself.** The runner proposes a figure; the authoritative number comes from the capital allocator. Record who set it, or record that the figure is the runner's proposal standing in for them. Runner proposes with the **basis named** — see the note below — and the user confirms.

  **Naming the basis is mandatory, because the two common bases differ by roughly a factor of two and neither is the default.**
  - *Venture-fund basis (often 25–40%).* This is **portfolio-loss-adjusted**, not a judgement about the risk of the venture in front of you. A fund returning ~20–25% net to LPs, where most investments return close to nothing and fees plus carry drag gross to net by a third or more, must underwrite each deal at a rate that carries the failures beside it. Applying this to a single corporate project double-counts a loss rate that is not present.
  - *Corporate-parent basis (often lower).* One project does not have to pay for nine dead ones. The capital is cheaper at source — retained earnings, no illiquidity premium, no carry layer. And part of the risk the fund basis prices is already retired: existing distribution, brand, customer base and permissions.

  **⚠ Do not conclude from the above that the corporate rate is low. Capital rationing usually pushes it back up, and often to venture-fund levels.** The cheap-capital argument holds only where capital is freely deployable. Where capital is **scarce** — a regulated balance sheet, a fixed investment envelope, a competing project queue — the correct hurdle is not the cost of capital but the **return on the marginal displaced alternative**. Three forms of it, in rising order of bite:
  - *The core business.* Capital into the venture is capital not deployed into an existing book that already earns a known return at materially lower risk. The venture must beat it **plus** a premium for the risk difference.
  - *Distribution to shareholders.* Dividends and buybacks are always available at near-zero execution risk.
  - *Buyback below book (the sharpest case).* Where the parent trades below tangible book value, a buyback retires book value for less than its worth and is immediately accretive — an alternative with a very high implied return and almost no delivery risk. A venture must clear that. Record this as a mechanism; do not assert any specific company's trading multiple without a source.

  **The two bases therefore often converge on similar numbers for opposite reasons** — the fund's rate pricing portfolio failure, the constrained corporate's rate pricing scarce capital. **Treat "corporate therefore lower" as a defect, not a default.** The runner's obligation is to name which force dominates for *this* allocator — cheap capital and retired risk pulling down, capital rationing and foregone alternatives pushing up — and to say which way the balance falls and why.

  **Always carry a sensitivity.** Where the plausible range spans materially different rates, run the screen at the base rate and at least one higher rate, and report **which verdicts move**. A single rate presented as settled is a FAIL. Where the capital allocator's actual internal hurdle is known but confidential, do not record it — note that a confidential figure governs and run the screen on the proposed rate.
- **At-scale geography:** the market where at-scale operations are defined — not the pilot geography, the full scale. Runner proposes from the venture's context; it must never reach for "Global" as a reflex — user confirms
- **Relevant industry:** the industry classification this venture lands in (determines comparables and cost structure analogies) — runner proposes, user confirms

These are not aspirational — they are the screening criteria against which use cases are evaluated in Step 4.

**How to present the proposals (required form):**

| # | Parameter | Proposed value | Basis for the proposal | Status |
|---|---|---|---|---|
| 1 | Investment period | [value] `⚠ ASSUMED` | [why this, in one line] | confirm / override |
| 2 | Required IRR | [value] `⚠ ASSUMED` | [which hurdle basis, named — venture-fund or corporate-parent; state the counter-argument] | confirm / override · **who sets it:** [CFO / CEO / IC / LPs / runner proposal standing in] |
| 3 | At-scale geography | [value] `⚠ ASSUMED` | [why this scope] | confirm / override |
| 4 | Relevant industry | [value] `⚠ ASSUMED` | [why this classification] | confirm / override |

State plainly which of the four most changes the Step 4 verdict, so the user knows where to spend their attention. A user reply of "confirmed" or "yes" against the block confirms all four as drafted.

**Quality gate:** All four parameters must be **confirmed by the user** before the Step 4 screen runs. Proposing is not confirming. If the user has not responded to the proposal block, stop — do not run the screen on unconfirmed values, and never present a computed required-price line derived from them as if it were settled.

---

### Step 2 — Path routing (critical)

**Before proceeding, determine which path applies:**

| Path | Starting point | Sequence |
|------|---------------|----------|
| **Path A — Technology venture** | A novel technology or capability to commercialise | 2a (core functionality) → 2b (optional) → 2c (architect's lens) → 3 (use cases) → 4 (evaluate) → PCO → R1 |
| **Path B — Social problem venture** | A societal problem or SDG with no existing commercial solution | 2b (right-size problem) → 2c (architect's lens) → 3 (impact cases) → 4 (evaluate) → PCO → **conventional model mapping → CLO identification → then** 2a (core functionality) |

**Why the paths differ:**

For Path A, the core functionality is the known starting point. Use cases are applications of it. Core functionality is described first because it is what you have.

For Path B, the core functionality does not yet exist — it will be *derived* from the workaround that circumvents the CLO. Describing it before the CLO is identified is the contamination error: it imports a known solution from somewhere else (another venture, an existing industry) and retrofits it onto the problem. The core functionality for a Path B venture can only be stated after you know what Critical Limiting Operation you are working around.

**Path B contamination guard — enforce at every step until CLO is identified:**

> At no point before the CLO is identified should you describe, name, or reference:
> — what the venture's product will do
> — how the venture will solve the problem
> — any analogy to an existing venture (including Calmly, Grameen, Airbnb, or any other known CBA)
> — any technology or mechanism you have in mind
>
> Analogues are permitted — and encouraged — during workaround design in R1. They are not permitted at PCO stage. A CLO identified by analogy ("it's like Calmly's due diligence problem") rather than by first-principles analysis of the conventional model is a contaminated CLO.

If you notice yourself describing a solution at PCO stage during a Path B session: stop, discard the solution framing, and return to the problem.

---

### Step 2a — Abstract the core functionality (Path A only — or Path B after CLO is identified)

**For Path A ventures:** complete this step now, before Step 2b and Step 3.

**For Path B ventures:** skip this step entirely until after the PCO is selected, the conventional model is mapped, and the CLO is identified. Return here at that point and state the core functionality as a description of what the workaround does at the most abstract level — derived from the CLO analysis, not imported from elsewhere.

Describe what the venture's technology or capability does and how it does it at the most abstract level — stripped of any specific application or customer context.

**Format:** What it does (output) + How it does it (mechanism), at the most basic level.

**Examples:**

| Venture | Core Functionality | Path |
|---------|-------------------|------|
| Grameen Bank | Growth capital through debt — via peer-group accountability rather than individual credit assessment | B — derived from CLO workaround |
| Kite Mill | Generates consistent energy — by capturing high-altitude wind currents with an airborne kite | A — technology first |
| Calmly | Structured resolution of civil disputes — without requiring per-case expert legal facilitation | B — derived from CLO workaround |
| Ford Model T | Personal mechanical transport — via assembly-line manufacture at mass-market cost | A — technology first |

**Quality gate:** The core functionality description must be usable without knowing anything about the customer. If it contains words like "for landlord disputes" or "for SMEs," it has already been constrained. Strip all customer context — the functionality stands alone.

---

### Step 2b — Right-size the pervasive societal problem

Identify the persistent negative social or environmental condition that the venture could plausibly address. Then deliberately broaden it.

**Format:** Conditions → Effect

**The right-sizing move:** most founders start with a narrowly defined problem ("landlord disputes in England"). The PCO exercise requires deliberately broadening the category of person and/or problem to increase the scope of the opportunity — before evaluating which sub-problem has the right commercial shape.

**Examples of right-sizing:**

| Starting point (too narrow) | Right-sized version |
|-----------------------------|---------------------|
| "People in landlord deposit disputes" | "People facing civil disputes where the cost of resolution exceeds the value of the problem" |
| "Farmers who can't afford fertilizer" | "Agricultural producers unable to convert productive capacity into revenue due to financing constraints" |
| "Unbanked people who need small loans" | "People in informal economies who lack access to formal financial instruments" |

**Why this matters:** the right-sized problem is the correct starting point for use case generation. Use cases that only fit the narrow version will produce a venture optimised for the beachhead. Use cases generated from the broader problem may reveal higher-value entry points that the narrow definition would have excluded.

**Quality gate:** the right-sized problem must still be specific enough to generate observable market conditions — not "inequality" or "poverty." If it cannot be used to generate concrete use cases in Step 3, broaden or refocus.

---

### Step 2c — Establish the architect's lens (industry / expertise) — REQUIRED INPUT

The **industry-relevant causes and consequences** in Step 3 cannot be generated generically — they are generated through the lens of *who is doing the architecting*. This is a Simanis requirement: the industry-relevant impact cases come from the **intersection of the societal problem (2b) and the architect's industry or expertise**. Without this lens, Step 3's industry-related rows are guesswork.

Capture the lens according to who is architecting (**required — elicit from the user, do not infer**):

- **If a business is architecting** → the nature of the business: its industry/sector, core capabilities, assets, distribution, and where it already operates. The industry-relevant causes/consequences are generated from *this industry's* model.
- **If an individual entrepreneur is architecting** → their **knowledge, interests, and "genius"**: the domains they understand deeply, where their unfair advantage / zone of genius lies, and what they are drawn to. The industry-relevant cases are generated from *this person's* expertise.

**Why it matters:** two architects facing the same societal problem will (correctly) surface different viable impact cases, because their industry/expertise makes different causes and consequences tractable. The PCO is not the best impact case in the abstract — it is the best one *this architect can credibly create a market for*.

**Quality gate:** the lens must be specific enough to generate industry-relevant causes/consequences in Step 3. "I want to help people" is not a lens; "20 years in mobile-payments infrastructure" or "deep expertise in early-childhood pedagogy" is.

**Propose-and-confirm applies here too (27 Aug 2026), for the same reason as Step 1.** Where the architect is a known business or a person the runner has context on, the runner **drafts the lens** — assets, capabilities, distribution, permissions, and the credibility constraints that come with them — flags it `⚠ ASSUMED`, and presents it for confirmation alongside the Step 1 block. Do not interrogate the user for a lens the runner can already draft. But do not generate industry-relevant cases on an unconfirmed lens either: a wrong lens produces a wrong shortlist, and the error is invisible downstream because the cases will look plausible. Draft it, flag it, get the nod, then generate. Path A's core functionality already encodes a lens, so this step is lighter there; it is most load-bearing for Path B. Capture it on both paths.

---

### Step 3 — Define and research use cases

Use cases are broad applications of the core functionality (from 2a), or industry-relevant causes/consequences of the societal problem (from 2b, **lensed through the architect's industry/expertise from 2c**), common to a group of people or organisations.

**Critical distinction:** use cases are not customer segments. Two people in the same demographic segment may have different use cases; two people in different segments may share one. Use case thinking keeps the analysis at the level of the job to be done, not the identity of the customer.

**Each use case provides:** either different core value for the user, or different enabling context (institutional, geographic, regulatory) that affects viability.

Generate use cases from both 2a and 2b:

**From Core Functionality (2a) — Use Cases:**

| Question | Format |
|----------|--------|
| Who else needs this functionality? | Group + their version of the job |
| What contexts make this functionality most valuable? | Context + why it amplifies value |
| What enabling conditions (regulation, infrastructure, institutions) create a window? | Condition + opportunity it creates |

**From Societal Problem (2b) — Impact Opportunities:**

| Type | What to generate |
|------|-----------------|
| Societal causes | Conditions directly producing the issue |
| Societal consequences | Harm that results from the issue not being resolved |
| Industry-related causes | Features of **the architect's industry/expertise (2c)** whose model produces or intersects the issue |
| Industry-related consequences | Market failures in **the architect's industry/expertise (2c)** that result — the impact cases *this* architect can credibly address |

Generate at least six use cases / impact opportunities. More is better at this stage. Selection comes next.

---

### Step 4 — Estimate and evaluate

Convert the investment parameters from Step 1 into a financial screen. Test each use case against it.

**The required-price line is computed from the Step 1 parameters — it is not a number the runner invents, and there is no separate "Prime" or revenue/EV bar.** The only screening gates are the method's own: the loss-to-price ratio and the workaround-plausibility / market-creation-margin gates below. Do not introduce any threshold beyond these.

**The conversion:**

1. Required capital → cash flow needed to deliver required IRR at end of investment period
2. Required cash flow → required at-scale annual revenue
3. Required revenue → required price per customer (at a penetration rate that is either **user-supplied** or a clearly-labelled, **user-confirmed method default** — e.g. "method default per IVE: 2.5%". Never apply a penetration rate silently)
4. Required price → compare against the monetizable size of customer loss in each use case

**Every ratio or figure used here is either user-supplied, taken verbatim from a cited source, or flagged as unvalidated.** Penetration rate, importance multiplier, group size, customer loss — if any is an estimate, mark it `⚠ UNVALIDATED` so the user can replace it. If a needed input is missing, propose it flagged `⚠ ASSUMED` and stop for confirmation rather than proceed on it unconfirmed.

**This is a directionality test, not a precision exercise.** The question is: does this use case have the right shape? Is the customer loss large enough that the required price fits within it? The answer is directional — it screens out use cases that are obviously too small and identifies those worth detailed design work. It does **not** select the winner — that is the user's call in Step 5.

**Value Potential formula (from IVE):**

`Value Potential = Group Size × Penetration Rate × Importance Multiplier`

Where Importance Multiplier answers: how mission-critical is this to the customer? A problem that, if unsolved, has severe consequences scores high. A problem that produces mild inconvenience scores low.

Penetration Rate here follows the same rule as in the conversion above — user-supplied or a clearly-labelled, user-confirmed method default. Group Size and Importance Multiplier are estimates: flag them `⚠ UNVALIDATED` unless drawn from a cited source.

**Evaluate each use case against three questions:**

1. **Is the group large enough?** At the required price and penetration rate, can this use case generate the revenue needed to deliver the required IRR?
2. **Is the loss large enough?** Is the customer loss (money, fear, stress) big enough that the required price is rational for them to pay?
3. **Is a credible workaround possible?** Does a solution exist — in principle — that could eliminate the key cost without reproducing the conventional BFF's cost structure?

**Output per use case:**

```
Use Case: [Name]
Group: [Who]
Group size estimate: [Number + source — mark ⚠ UNVALIDATED if estimated]
Customer loss magnitude: [£/time/stress at scale — mark ⚠ UNVALIDATED if estimated]
Required price (computed from Step 1 parameters): [£ — show the calculation; not an invented figure]
Penetration rate used: [user-supplied | method default per [source], user-confirmed]
Loss-to-price ratio: [>2x is viable direction; <1x is not]
Workaround plausibility: [High / Medium / Low — one sentence]
Verdict: [In-PCO (default) / Out of scope — directional screen only. Under the breadth default, every case that clears the screen is In-PCO; "Out of scope" applies ONLY to cases that fail on their own terms (no monetizable loss, or no conceivable workaround). A case is never marked Out of scope merely for being smaller or worse-fitted than another. Use the optional priority note to flag which In-PCO case to research first. The user selects the PCO in Step 5.]
```

---

### Step 5 — State the Prime Commercial Opportunity

**The user selects the PCO from the completed Step 4 grid. The runner does not decide.** Present the grid with all use-case verdicts, then ask the user to select. The runner's recommendation **defaults to the broadest credible combination** of all surviving use cases — not the single highest-scoring one (see "Choose the biggest PCO possible"). Recommend the widest set that clears the directionality screen, and say plainly that narrowing is R2's job via the KMC. The runner frames this as a recommendation, not a declaration, and waits for the user's choice. Do not write "X is the PCO" until the user has chosen it.

Once the user has selected, state the chosen PCO as a single sentence. Where the PCO spans several use cases, the sentence names the broad population and condition they share — not one case — and notes that R2 will isolate the KMC-bearing customers within it.

**Format:** who + the condition they face + why it has the right financial shape.

**Example:**
> *Tenants in England and Wales who are legally owed a deposit return by a landlord who refuses to pay — approximately 1.3m disputes per year — bear a loss they have no cost-effective mechanism to recover, with an average claim value of £1,200 and a monetizable loss that materially exceeds any viable price point.*

**Quality gate:** The PCO statement must:
- Name a specific, observable condition (not a segment description)
- State or imply the size of the group
- Reference the scale of the customer loss
- Imply the financial shape is viable (loss-to-price ratio passes the directionality test)

---

## Output format

After all steps — and after the user has selected the PCO in Step 5 — produce a structured PCO brief. Every figure that is an estimate, assumption, or placeholder is flagged `⚠ UNVALIDATED`; every method default is labelled with its source and noted as user-confirmed.

```
PCO BRIEF
---
Investment parameters (runner-proposed, user-confirmed — record any the user overrode):
  Period: [Start → Scale date]
  Required IRR: [%] — basis: [venture-fund | corporate-parent] — set by: [CFO / CEO / IC / LPs / runner proposal]
    Sensitivity carried: [higher rate tested, and which verdicts moved]
  Geography: [Market]
  Industry: [Classification]

Core Functionality: [One sentence — what + how, no customer context]

Societal Problem (right-sized): [Condition → Effect]

Use cases evaluated:
  1. [Name] — [Verdict] — [One-line rationale]
  2. [Name] — [Verdict] — [One-line rationale]
  3. [Name] — [Verdict] — [One-line rationale]
  [Continue for all evaluated]

Prime Commercial Opportunity (selected by user): [One sentence — who, condition, financial shape]

Directionality verdict: [Viable / Marginal / Unviable — with key reasoning]

Confidence assessment:
  Biggest assumption in the PCO: [Name it]
  What would most change the verdict: [One sentence]
```

---

## Common failure patterns at the PCO stage

| Failure | What it looks like | What it means |
|---------|-------------------|---------------|
| Beachhead anchoring | "Our target is early-adopter SMEs in London" | PCO not defined — the venture is optimised for a beachhead before the broader opportunity is evaluated |
| Both sides bounded | "We're solving deposit disputes with an AI negotiation tool" | Solution space closed before problem space is sized — architecture may be right but for wrong market |
| Use case = segment | "People aged 25–45 in private rental" | Demographic segment, not a use case. What is the specific condition? What job are they trying to do? |
| Loss too small | Required price is £200; average customer loss is £150 | Directionality test fails — no viable price point exists within the customer's loss |
| Workaround implausible | The conventional BFF cost structure is irreducible | R1 may not be solvable for this PCO — needs redesign before proceeding |
| Premature narrowing | "We picked the landlord case over the others" | A single case chosen at PCO when several cleared the screen — re-introduces the beachhead trap. Carry all surviving cases into the PCO; let R2's KMC qualify customers on evidence |

---

## Relationship to BALM requirements

```
PCO → R1 (Circumvent At-scale Cost Bottleneck)
    → R2 (Eliminate Customers' Value Bottleneck)
    → R3 (Circumvent Scaling Cost Bottleneck)
    → R4–R7 (Function 2: Normalize Customer Routines)
    → R8–R10 (Function 3: Dictate Competitive Landscape)
```

The PCO sets the scope for all requirements. R1's CLO identification and Workaround Strategy are designed for the PCO, not for a narrower beachhead. R2's customer research is conducted within the PCO's customer population. Solving requirements for the wrong PCO is the most common and least visible cause of architectural drift.

---

## Generative discipline — keep the PCO open (VA-3 / VA-2)

Reference: `method/context/va-design-discipline.md`

The PCO sets scope, not design. Specify only what the PCO genuinely requires — the broadest credible use case and the investment parameters. Do **not** pin down product features, segments, pricing, mechanisms, or a Business Form Factor here. Those are earned by the BALM challenges (R1–R10), and a PCO that pre-specifies them anchors every later challenge into justification mode — defending an early design instead of generating a better one. Anything specified here that a later challenge will earn is premature design (VA-2): hold it open as a question, not a decision. The test before recording any detail: "does the PCO itself require this, or am I designing the venture early?"

---

## Output language — ASD-STE100 (Tom's standing preference, 17 Aug 2026)

Write every rendered output document this skill produces — the PCO brief, the VDR PCO section, HTML records, and any prose deliverable — in **ASD-STE100 Simplified Technical English**:

- One instruction or one statement per sentence. Descriptive sentences ≤ 25 words; procedural sentences ≤ 20 words.
- Active voice. Present tense unless the past is necessary.
- One meaning per word, one word per meaning — add a "Defined terms" table to rendered documents and use those terms consistently.
- No idioms, no gerund-led clauses, no empty hedging, no metaphor in load-bearing statements.
- Prefer approved-word constructions: "make sure" not "ensure"; "use" not "utilise"; "start" not "commence".
- Warnings and open items as commands ("Check X before Y. Do not assume it."), not observations.

This governs the *rendered document*, not the method: step definitions quoted from this skill stay verbatim, and the `⚠ UNVALIDATED` flagging discipline is unchanged. Reference example: `ventures/Education/education-venture-design-record-2026-08-17.html`.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/balm-pco-custom/SKILL.md` to modify
- Related skills: `/balm-challenge-1-custom` (R1 — Workaround), `/balm-challenge-2-custom` (R2 — Efficacy)
- IVE source: Simanis et al. (2021); VTS Pilot materials, Half-Solved + Cornell MCL (2025)
- Design Principle 01: scope before depth — the PCO is the scope-setting step
