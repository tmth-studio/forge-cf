---
name: theory-of-change-custom
description: Write a rigorous Theory of Change and Strategy for any BALM requirement (R1–R10). Accepts an R-number requirement context and produces a named output — e.g. Workaround ToC + Workaround Strategy for R1, Efficacy ToC + Efficacy Strategy for R2. Stage 1 builds the ToC (class of problem, theory, context, outcome). Stage 2 builds the strategy (design choice, hypothesis, critical assumption). Uses CMO structure (Pawson & Tilley, 1997). Enforces the theory/hypothesis distinction throughout.
model_routing:
  default: balanced
---

# Theory of Change

Guides the user through writing a rigorous Theory of Change (ToC) for a BALM requirement. Enforces the distinction between published theory and design hypothesis. Tests each field against named quality criteria before accepting it. Produces a structured output named for the requirement — ready for insertion into the BALM output or as a standalone artefact.

---

## Purpose and framing

A Theory of Change in the BALM context answers the question: *why is change possible here?* It uses the CMO structure from Realist Evaluation (Pawson & Tilley, 1997): it names the class of problem, cites the established academic theory (the mechanism), describes the conditions under which the mechanism operates on this specific group (context), and states the observable change that results when the mechanism is activated (outcome).

The strategy — how the venture will cause the change — is a separate field. The ToC does not explain what the venture does. It explains why the change is achievable in principle.

This distinction matters. A design hypothesis ("we think that X will cause Y") belongs in strategy. A theory ("Kahneman & Tversky, 1979, demonstrated that reframing losses as gains shifts decision-making") belongs in the ToC. Conflating them produces a ToC that cannot be interrogated or stress-tested, because hypothesis and theory are held to different standards of evidence.

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

**→ This skill: Cross-cutting ToC + Strategy tool** — invoked from R1 (Workaround ToC + Strategy), R2 (Efficacy ToC + Strategy), R3, and any other requirement that needs a named Theory of Change

**Design principle — architect for at-scale, not for launch.** Every requirement is designed for the venture operating at the scale required to pay back all investment capital at a competitive rate of return. Early-stage operational constraints (team size, regulatory budget, portfolio volume) are sequencing problems, not architecture problems. Do not let launch-phase limitations constrain the design. A cost that seems large at 50 units is often trivial against the same cost at 50,000 units.

---

## Step 0 — Context gathering (silent)

Before the first question, read:

1. `System/user-profile.yaml` — communication preferences
2. If the user names a specific requirement (e.g., "R1 Workaround"), read the relevant requirement skill (e.g., `/balm-challenge-1-custom`) to understand what the ToC must accomplish in context — the CLO or Key Monetizable Cost that the ToC should explain change for.

Do not surface these reads. Use them to contextualise your questions and pre-fill any draft content for the user to react to rather than generate from scratch.

---

## Step 1 — Scope the requirement

Ask:

> "Which BALM requirement are we writing a Theory of Change for? Give me the requirement number and name (e.g., R1 Workaround, R2 Efficacy, R3 Scaling), or describe the problem in your own words if you're working outside the BALM structure."

### R-number naming convention

The output of this skill is named according to the requirement type. Use this table:

| Requirement | ToC name | Strategy name |
|---|---|---|
| R1 — At-scale Cost Bottleneck | Workaround Theory of Change | Workaround Strategy |
| R2 — Customers' Value Bottleneck | Efficacy Theory of Change | Efficacy Strategy |
| R3 — Scaling Cost Bottleneck | Scaling Theory of Change | Scaling Strategy |
| R4 — Want Block (Attraction) | Attraction Theory of Change | Attraction Strategy |
| R5 — Use Block (Adoption) | Adoption Theory of Change | Adoption Strategy |
| R6 — Buy Block (Amortization) | Amortization Theory of Change | Amortization Strategy |
| R7 — Gateway Partner | Gateway Partner Theory of Change | Gateway Partner Strategy |
| R8 — Lock-in | Lock-in Theory of Change | Lock-in Strategy |
| R9 — Lock-out | Lock-out Theory of Change | Lock-out Strategy |
| Other / outside BALM | Theory of Change — [descriptive name] | Strategy — [descriptive name] |

Once you have the requirement, state back in one sentence what the ToC needs to explain — and confirm the output name — before proceeding.

---

## Step 2 — Class of problem

Ask:

> "What class of problem does this represent? I'm looking for a named category from social science, behavioural economics, institutional economics, or related fields — not a description of symptoms."

### Quality gate — class of problem

Accept only if the answer meets all three criteria:

| Criterion | Pass | Fail |
|-----------|------|------|
| Named category | "Information asymmetry", "present bias", "coordination failure", "moral hazard", "adverse selection" | "People don't have enough information", "defendants don't make rational decisions" |
| Not a symptom description | The name refers to a class of problem, not a consequence of it | "Confusion", "poor decision-making", "lack of trust" |
| Domain-grounded | Traceable to a recognised field or literature | Vague management language without a disciplinary anchor |

If the answer fails, respond with:

> "That reads more like a symptom than a named problem class. [Specific issue]. Here are some candidate classes that might fit this requirement — tell me which resonates, or use them as a starting point:
> [offer 2–3 candidates from the reference library in Step 7 that are plausible given the requirement context]"

If the answer is close but imprecise (e.g., "cognitive bias" rather than "present bias"), ask them to narrow it:

> "That's the right territory. Can you name the specific bias or mechanism? 'Cognitive bias' is a category, not a class — I need the named instance."

Once accepted, confirm: "Class of problem: [name]. Moving to theory."

---

## Step 3 — Theory

Ask:

> "What published, peer-reviewed theory explains how this class of problem can be solved or why the desired change is achievable? I need a named researcher and paper — not a design hypothesis or a general principle."

### The theory/hypothesis distinction — enforce rigorously

A **theory** is:
- Published in peer-reviewed literature or established academic canon
- Attributable to named researchers with a citable date
- Empirically grounded — based on observation, experiment, or formal modelling
- Generalisable beyond this specific product or market

A **hypothesis** is:
- A novel design claim about what the venture will do
- Not yet tested or published
- Specific to this venture's design choices

If the user offers a hypothesis instead of a theory, name it directly:

> "That's a hypothesis — a claim about what the venture will do — not a published theory. Hypotheses belong in strategy. What I need here is the established academic result that gives your hypothesis its theoretical basis. For example: if your hypothesis is 'showing defendants their expected value will shift their settlement decisions', the theoretical grounding is Kahneman & Tversky's (1979) prospect theory, which established how reframing gains and losses changes decision behaviour. What is the established result underneath your claim?"

Common substitution patterns to intercept:

| What the user says | What it actually is | What to ask instead |
|---|---|---|
| "We believe that X will cause Y" | Hypothesis | What published research supports the causal mechanism? |
| "It makes sense that if X then Y" | Intuition | Has this mechanism been empirically demonstrated? Where? |
| "X is well known to cause Y" | Folklore | Who demonstrated it, and when? |
| "Research shows that nudges work" | Undercited generalisation | Which specific nudge mechanism, and from which study? |

### Quality gate — theory

Accept only if:

| Criterion | Pass | Fail |
|-----------|------|------|
| Named researcher | "Kahneman & Tversky (1979)", "Akerlof (1970)", "Deci & Ryan (1985)" | "Psychology research shows...", "Studies have found..." |
| Specific paper or book | At least year and rough topic, ideally full citation | "Some economists think..." |
| Mechanism stated | The theory explains *how* the change is possible, not just that it exists | Citation given but mechanism not linked to the class of problem |
| Applicable to the named class | The theory directly addresses the class of problem from Step 2 | Theory cited from unrelated domain without explanation of applicability |

If the user names the right researcher but cannot name the mechanism:

> "Right researcher, right territory. But I need the mechanism — not just the name. What specifically did [researcher] establish that applies here? What is the causal claim in the paper?"

Once accepted, confirm: "Theory: [name + citation + mechanism in one sentence]. Moving to context."

---

## Step 4 — Context

Ask:

> "Under what conditions does this mechanism operate on this specific group? I'm not asking what is happening in general — I'm asking what is specific about this population's situation that makes them susceptible to this class of problem."

Context in the CMO sense (Pawson & Tilley, 1997) is not a description of the current state of the world. It is the set of conditions under which the mechanism is active — the when, where, and for whom that determines whether the theory's predictions hold in this specific case.

### Quality gate — context

Accept only if:

| Criterion | Pass | Fail |
|-----------|------|------|
| Conditions, not situation | Describes the circumstances that activate the mechanism | Describes the current state of affairs without linking to the mechanism |
| Population-specific | Names the specific group and their structural position | Generic description applicable to any market or population |
| Mechanism-linked | Makes clear why these conditions make this group susceptible to the named class of problem | Observations about the group that float free from the mechanism |
| Not editorialised | Neutral, observable conditions | Embedded judgement about the group |

Common failure modes:

- **Current situation substituted for conditions**: "Defendants receive a settlement offer" is a situation. "Defendants in UK small-claims consumer disputes contacted before a court date is set, with no legal representation" describes the conditions under which motivated reasoning operates. The difference is whether it connects to the mechanism.
- **Too broad**: "In markets with information asymmetry" is not specific enough. Name the population, the structural position, the triggering event.
- **Editorialised**: Strip value judgements. Context is the conditions, not the problem.

If it fails:

> "That describes the situation, not the conditions. What is it about this group's specific position — structurally, procedurally, economically — that makes the mechanism [from Step 2] active for them and not for others?"

Once accepted, confirm: "Context: [statement]. Moving to outcome."

---

## Step 5 — Outcome

Ask:

> "What is the observable change that results when the mechanism is activated in this context? Give me something that has happened — a different state — not an activity the venture performs."

### Quality gate — outcome

Accept only if:

| Criterion | Pass | Fail |
|-----------|------|------|
| Observable change | Something that has changed for the person or market | Something the venture does or delivers |
| Observable and testable | You could in principle verify this has occurred | Abstract aspiration with no measurable referent |
| Logically connected | Follows plausibly from the context and mechanism | Non-sequitur or introduces a new problem |
| Does not restate the strategy | Does not describe how change happens, only that it has | Mechanism of the venture's intervention described as the outcome |
| Proportionate | The outcome is what the mechanism can actually produce — not a grand transformation | "Access to justice is restored" when the mechanism only shifts one decision |

The test: if you can substitute "we will do X" for the outcome and it still makes sense, it is an activity. An outcome reads as something that has *happened* — a different state of the world.

Common failure modes:

- **Activity substituted for outcome**: "Customers receive the information package" is an activity. "Customers settle at or near expected value within 30 days of contact" is an outcome.
- **Vague aspiration**: "Customers make better decisions" is not testable. Push to specifics — what decisions, what does better mean, over what timeframe.
- **Strategy creep**: Outcome must not mention the venture's mechanism. If the mechanism appears, strip it out and restate as pure outcome.
- **Overclaiming**: The outcome should be what this mechanism, in this context, can produce — not the venture's long-term vision.

If it fails:

> "That's an activity [or aspiration], not an outcome. What has changed for the customer [or market] when the mechanism has done its work? Imagine it's three years from now and this specific mechanism has operated as the theory predicts — what does someone observe in the world that was not there before?"

Once accepted, confirm: "Outcome: [statement]."

---

## Step 6 — Internal consistency check

Before producing the output, run a silent check across all four fields:

1. **Class of problem → Theory alignment**: Does the cited theory directly address the named class of problem? A prospect theory citation under an adverse selection class is a mismatch — name it.

2. **Context → Mechanism fit**: Do the conditions described in the context field actually make this population susceptible to the named class of problem? If someone in a different context would face the same mechanism, the context is not specific enough.

3. **Theory → Outcome mechanism**: Does the theory's established mechanism provide a credible explanation of why the outcome is achievable in this context? If the theory says "reframing changes decisions" and the outcome says "customers settle at expected value", the connection should be explicit.

4. **Class of problem — second look**: Re-examine the class of problem with all four fields in view. If it now reads as a symptom of the actual problem class, surface this before finalising.

If any inconsistency is found, surface it directly before producing output:

> "Before I finalise this — I want to flag a tension. [Specific inconsistency in plain terms]. Do you want to adjust [field] before I write it up?"

---

## Step 7 — Output

Produce two outputs: a structured markdown block ready for BALM insertion, and a brief commentary on the analytical quality of the ToC.

### Output A — Structured ToC (BALM-ready)

Use the named ToC title from the R-number naming table in Step 1.

```markdown
## [Named ToC — e.g. Workaround Theory of Change]

**Class of problem**
[Named category, one sentence maximum]

**Theory**
[Named researcher(s), year, paper/book title where known. One to two sentences
stating the specific mechanism that applies here.]

**Context**
[The conditions under which the mechanism operates on this specific group.
One to two sentences, specific, mechanism-linked, no editorialisation.]

**Outcome**
[Observable change that results when the mechanism is activated. One to two
sentences, testable, not an activity, does not describe the venture's method.]
```

### Output B — Quality commentary

Three to five sentences assessing the ToC's analytical strength. Cover:
- How tightly the class of problem and theory are aligned
- Whether the context is specific enough to be mechanism-linked (not just descriptive)
- Whether the outcome is testable and proportionate to what the mechanism can actually produce
- Any remaining risks (e.g., theory widely applicable but mechanism link to this context thin; outcome specific but may be hard to attribute to the product vs. other factors)

Do not inflate quality assessments. A good ToC with one thin link is better described as "strong with one area to watch" than as excellent.

---

## Step 8 — Offer to proceed

After output:

> "Want me to add the strategy field now — how the venture causes this change — or does the ToC need revision first?"

If the user wants revision: return to the relevant step. If the user wants strategy: proceed to Stage 2.

---

# Stage 2 — Strategy

The strategy field answers: how does the venture's specific design activate the mechanism established in the ToC, in this specific context?

The structure of a well-formed strategy is:

> The ToC establishes that mechanism **M** produces outcome **O** under conditions **C**.  
> The strategy claims that design choice **D** creates conditions **C** in this context, thereby activating **M**.

The strategy is a bridge sentence. It connects the generic theory to the specific design. It does not re-explain the theory. It does not describe tactics. It names the mechanism, names the design choice, and states the hypothesis.

**What makes a strategy elegant:** a single structural move that activates the mechanism and resolves the problem — without introducing new dependencies or requiring the venture to perform something fragile. The Grameen Bank example: one design choice (joint liability peer groups) simultaneously eliminated individual credit assessment costs, improved repayment rates beyond what individual assessment achieved, and created a self-organising delivery mechanism — three effects from one structural move. The elegance is that no separate mechanism is needed for each.

---

## Step 9 — Extract the design choice

Ask:

> "What does the venture specifically do — one design choice — that creates the conditions the theory says are needed for change to happen?"

Push for a single design choice. If the user offers multiple, say:

> "That's [number] separate moves. A good strategy is one structural choice that does the work. Which of these is load-bearing — the one that, if you removed it, the mechanism wouldn't activate?"

### Quality gate — design choice

| Criterion | Pass | Fail |
|---|---|---|
| Single structural move | One design choice, clearly named | A list of activities |
| Operationally specific | Someone could implement this | "We will communicate clearly" |
| Mechanism-linked | Names or implies the mechanism from the ToC | Design choice described without connection to theory |
| Venture-specific | Only this venture does this, or does it in a distinctive way | Generic activity any competitor could replicate identically |

If the design choice is a list of tactics:

> "Those are tactics — the execution details of a strategy. What is the single design principle underneath them? If you had to describe what the venture is doing in one sentence, without naming any of those tactics, what would it be?"

---

## Step 10 — Name the hypothesis

Ask:

> "State the hypothesis: if the venture does [design choice], the mechanism from the ToC will activate and produce [desired state]. What assumption must hold for that to be true?"

This forces two things: (1) an explicit connection between design choice and mechanism, and (2) the surfacing of the critical assumption — the condition that, if false, would invalidate the strategy.

### Quality gate — hypothesis

| Criterion | Pass | Fail |
|---|---|---|
| Falsifiable | Names the condition under which it would be wrong | "We believe this will work" |
| Mechanism-explicit | States which mechanism from the ToC is being activated | Desired outcome asserted without mechanism |
| Assumption named | At least one assumption explicitly stated | No assumption surfaced |
| Testable assumption | The assumption could in principle be checked | "People will engage with the product" — too vague |

If the hypothesis is not falsifiable:

> "What would have to be true for this strategy to fail? Name the specific condition. If you can't, the hypothesis can't guide design — because nothing the venture learns in the market could ever challenge it."

---

## Step 11 — Test for elegance

After the hypothesis is accepted, run a silent check against the elegance standard:

1. **Does the design choice activate the mechanism directly, or does it depend on a chain of prior conditions that need to be independently managed?** If the latter, the strategy has hidden dependencies — name them.

2. **Does the strategy create value for any actor other than the one it's primarily targeting?** If yes, this is a sign of non-zero-sum design — flag it as a strength.

3. **Does removing any part of the design choice break the mechanism, or is there a simpler version that does the same work?** If simpler is possible, surface it.

4. **Is the design choice fragile — does it depend on a specific behaviour from a third party who has no incentive to cooperate?** If yes, name the dependency and ask how it is managed.

Surface findings directly:

> "Before I write this up — [finding]. Is that something to address now, or are you aware of it and comfortable with it as a known risk?"

---

## Step 12 — Output

Produce the strategy field in BALM-ready format. Use the named strategy title from the R-number naming table in Step 1.

```markdown
## [Named Strategy — e.g. Workaround Strategy]

**Design choice**
[Single structural move. One sentence. Specific enough to implement.]

**Hypothesis**
[If [the venture] does [design choice], [mechanism from ToC] will activate and produce
[desired state]. This hypothesis would be wrong if [falsification condition].]

**Critical assumption**
[The one assumption that, if false, invalidates the strategy. Named explicitly.]
```

Then offer:

> "Want me to insert both the ToC and Strategy into the BALM output now, or review first?"

---

## Common strategy failure modes — name them on sight

1. **Theory restatement** — strategy explains why the mechanism works rather than how the venture activates it. The theory section already did this. Cut it.

2. **Tactic list** — strategy is a list of things the venture will do rather than a single structural design choice. Ask for the principle underneath the list.

3. **Mechanism orphan** — design choice described without naming the mechanism it activates. The connection to the ToC is implicit, not explicit. Make it explicit.

4. **Fragile third-party dependency** — strategy requires a specific actor to behave in a way they have no independent incentive to do. Common in platform strategies. Name it as a risk.

5. **Unfalsifiable hypothesis** — "we believe customers will respond positively." No condition under which it would be wrong. Push for the falsification condition.

6. **Complexity as sophistication** — multiple interlocking design choices presented as a strategy. Usually a sign that the single load-bearing move has not been identified. Push for the one structural choice.

---

## The Rumelt kernel — use as a cross-check

Richard Rumelt's kernel of strategy (Rumelt, *Good Strategy Bad Strategy*, 2011):
- **Diagnosis** — what is the nature of the challenge? (This is your ToC)
- **Guiding policy** — the approach for dealing with the challenge (This is your strategy)
- **Coherent actions** — the specific steps that execute the guiding policy (These are tactics — not in scope here)

A strategy that cannot be stated as a guiding policy — one sentence, prescriptive, without listing specific actions — is not yet a strategy. Test every output against this.

---

## Reference library — named theories by domain

Use this when offering candidates in Step 2 or prompting in Step 3. Not exhaustive — covers the classes most commonly relevant to BALM requirements.

### Behavioural economics and decision science

| Class of problem | Named theory | Key citation |
|---|---|---|
| Loss aversion / framing effects | Prospect theory | Kahneman & Tversky, *Econometrica*, 1979 |
| Present bias / hyperbolic discounting | Hyperbolic discounting | Laibson, *Quarterly Journal of Economics*, 1997; Ainslie, *Picoeconomics*, 1992 |
| Overconfidence / planning fallacy | Inside view bias | Kahneman & Lovallo, *Management Science*, 1993 |
| Default persistence / status quo bias | Status quo bias | Samuelson & Zeckhauser, *Journal of Risk and Uncertainty*, 1988 |
| Inaction despite intent | Intention-action gap | Sheeran & Webb (review), *Motivation Science*, 2016 |
| Choice under complexity | Choice overload | Iyengar & Lepper, *Journal of Personality and Social Psychology*, 2000 |
| Preference for effort-matched reward | Effort justification | Aronson & Mills, *Journal of Abnormal and Social Psychology*, 1959 |
| Reference point dependence | Anchoring | Tversky & Kahneman, *Science*, 1974 |
| Social norm conformity | Descriptive norm influence | Cialdini et al., *Journal of Personality and Social Psychology*, 1990 |
| Commitment and consistency | Commitment devices | Ariely & Wertenbroch, *Psychological Science*, 2002 |
| Choice architecture / defaults | Nudge theory | Thaler & Sunstein, *Nudge*, 2008 |
| Optimism bias in risk assessment | Unrealistic optimism | Weinstein, *Journal of Personality and Social Psychology*, 1980 |

### Information asymmetry and market design

| Class of problem | Named theory | Key citation |
|---|---|---|
| Pre-contractual information asymmetry (quality unknown) | Adverse selection / market for lemons | Akerlof, *Quarterly Journal of Economics*, 1970 |
| Signalling to resolve information gaps | Signalling theory | Spence, *Quarterly Journal of Economics*, 1973 |
| Screening by uninformed party | Screening / self-selection | Stiglitz & Weiss, *American Economic Review*, 1981 |
| Post-contractual hidden action | Moral hazard / hidden action | Arrow, *Essays in the Theory of Risk-Bearing*, 1971 |
| Misaligned incentives between principal and agent | Principal-agent problem | Jensen & Meckling, *Journal of Financial Economics*, 1976 |
| Strategic information withholding | Cheap talk / credibility | Crawford & Sobel, *Econometrica*, 1982 |
| Credence goods (quality unverifiable after purchase) | Credence goods | Darby & Karni, *Journal of Law and Economics*, 1973 |

### Institutional economics and coordination

| Class of problem | Named theory | Key citation |
|---|---|---|
| Coordination failure (multiple equilibria) | Coordination games / focal points | Schelling, *The Strategy of Conflict*, 1960 |
| Collective action / free rider problem | Collective action problem | Olson, *The Logic of Collective Action*, 1965 |
| Institutional lock-in / path dependency | Path dependence | David, *American Economic Review*, 1985; Arthur, *Economic Journal*, 1989 |
| Transaction cost barrier to exchange | Transaction cost economics | Coase, *Economica*, 1937; Williamson, *Markets and Hierarchies*, 1975 |
| Network effects and tipping points | Network externalities | Katz & Shapiro, *American Economic Review*, 1985 |
| Trust deficit in new markets | Institutional trust theory | North, *Institutions, Institutional Change and Economic Performance*, 1990 |
| Common pool resource overuse | Commons governance | Ostrom, *Governing the Commons*, 1990 |

### Social psychology and behaviour change

| Class of problem | Named theory | Key citation |
|---|---|---|
| Peer pressure and mutual accountability altering behaviour | Social learning theory | Bandura, *Social Learning Theory*, 1977 |
| Collective self-governance of shared resources | Collective action and self-governance | Ostrom, *Governing the Commons*, 1990 |
| Extrinsic incentives undermining intrinsic motivation | Cognitive evaluation theory / SDT | Deci & Ryan, *Intrinsic Motivation and Self-Determination in Human Behaviour*, 1985 |
| Behaviour driven by unmet autonomy, competence, or relatedness | Self-determination theory | Ryan & Deci, *American Psychologist*, 2000 |
| Attitude-behaviour gap | Theory of planned behaviour | Ajzen, *Organizational Behavior and Human Decision Processes*, 1991 |
| Cognitive dissonance as change lever | Cognitive dissonance theory | Festinger, *A Theory of Cognitive Dissonance*, 1957 |
| Social proof in adoption decisions | Social proof / informational social influence | Deutsch & Gerard, *Journal of Abnormal and Social Psychology*, 1955 |
| Authority and trust transfer | Elaboration likelihood model | Petty & Cacioppo, *Advances in Experimental Social Psychology*, 1986 |
| Reciprocity as commitment trigger | Reciprocity norm | Gouldner, *American Sociological Review*, 1960; Cialdini, *Influence*, 1984 |
| Self-concept consistency | Identity-based motivation | Oyserman, *Psychological Review*, 2009 |

### Innovation and technology adoption

| Class of problem | Named theory | Key citation |
|---|---|---|
| Slow adoption of superior technology | Diffusion of innovations | Rogers, *Diffusion of Innovations*, 1962 (5th ed. 2003) |
| Incumbent advantage despite inferior product | Sustaining vs disruptive innovation | Christensen, *The Innovator's Dilemma*, 1997 |
| Adoption blocked by switching costs | Switching cost lock-in | Klemperer, *Quarterly Journal of Economics*, 1987 |
| New product trust deficit | Technology acceptance model | Davis, *MIS Quarterly*, 1989 |
| Chasm between early adopters and early majority | Technology adoption lifecycle | Moore, *Crossing the Chasm*, 1991 |

---

## Design principles underlying the quality gates

These commitments reflect the academic literature on what separates a robust ToC from a weak one (Mayne, 2019; Connell & Kubisch, 1998; Weiss, 1995).

**Plausibility**: the causal chain from current state to desired state, via the theory's mechanism, must be logically coherent. Each step must follow from the last. A plausibility failure is when the theory cited does not actually explain why the desired state is achievable.

**Specificity**: a ToC is only as useful as it is testable. Vague current and desired states cannot be evaluated — you cannot know if you are making progress or if you have arrived. Specificity is not about length; it is about precision.

**Separability**: the ToC must be separable from the strategy. If removing the strategy collapses the ToC, the two have been conflated. A good ToC stands alone — it explains why change is possible regardless of whether this venture is the one to cause it.

**Grounding**: the theory must be attributable to published research, not to intuition or design hypothesis dressed in academic language. The standard is: could this theory be cited in a peer-reviewed evaluation of the venture's impact? If not, it is not yet a theory for this field.

**Testability**: the desired state must be observable in principle. If there is no conceivable way to measure or verify it, it is an aspiration, not a desired state. The test does not need to be cheap or easy — it needs to be possible.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/theory-of-change-custom/SKILL.md` to modify
- **CMO reference:** `06-Resources/Methodology/pawson-tilley/dossier.md` — read before running this skill for full grounding in the context/mechanism/outcome framework
- **Related skills (BALM chain):**
  - `/balm-pco-custom` — PCO (prerequisite to all requirements)
  - `/balm-challenge-1-custom` — R1 (At-scale Cost Bottleneck; uses Workaround ToC + Workaround Strategy)
  - `/balm-challenge-2-custom` — R2 (Customers' Value Bottleneck; uses Efficacy ToC + Efficacy Strategy)
  - `/verify-balm-custom` — audits ToC completeness across all BALM requirements
  - `/pyramid-doc` — for building memos from completed BALM sections
- The theory/hypothesis distinction is the single most important quality gate. Do not soften it. Hypotheses belong in strategy, always.
- IVE source — the canon is a body of co-authored work, not one paper:
  - Simanis, E., Samani, S., Burnett, P. & Stuart, J. (2021). *Introduction to the Integrated Venture Engine.* Cornell SC Johnson College of Business
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *Rediscovering Capitalism: How Blue-Chip Builders Created Transformative Impact and Profit.* YNOT Institute Working Paper 1, Queens' College Cambridge
  - Simanis, E., Manuel, T., Khater, M., Palmer, E. & Bergmann, J. (2023). *The Business Architecture: The Hidden Code of Industry Disruption.* YNOT Institute Working Paper 2, Queens' College Cambridge — the Business Architecture Framework
  - Simanis, E. et al. (2024). *The Core Business Archetype* (Jan); *Engineering New Market Ventures* (Apr); *The Market Creator's Dilemma* (Nov)
  - Simanis, E. (2025). *Built to Hold* — the FMOS gates; Simanis, E. & Donohue, K. (2025). *Deciphering the Market Creator's Dilemma.* MIT Sloan Management Review
  - Attribution rule (WS1 feedback log, 5 and 17 Sep 2026): Tom Manuel is a co-author on the 2023 papers; "co-developer of the method" is not supported. TMTH's own additions are the WS1 standards, the VA register, the circle end-state and the direction rule
- VTS source: IVE Venture Training Studio, Half-Solved + Cornell MCL, July–October 2025
