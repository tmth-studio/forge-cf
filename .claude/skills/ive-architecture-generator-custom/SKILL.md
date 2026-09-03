---
name: ive-architecture-generator-custom
description: Architecture Generator for IVE ventures. Takes the CLO from PCO output, abstracts it to a structural class of problem, searches cross-domain for analogical cases where that class was solved, and returns ranked Workaround Strategy candidates — each with its mechanism of action, theory grounding, and elegance score.
---

# IVE Architecture Generator

Runs after PCO and before R1. Its job is to answer the question R1 asks but cannot answer on its own: **who else has solved this class of problem, and how?**

The practitioner working inside one industry is bounded by what they know. Cross-domain analogy is how IVE's most successful architectures were found — Grameen from rotating savings associations and village governance; Ford from continuous-process manufacturing in meatpacking. Neither leap is obvious from inside one industry. This skill makes the search systematic.

The output is a ranked shortlist of Workaround Strategy candidates. The practitioner takes this into R1 and builds the detailed design from there.

---

## Where this fits in the IVE sequence

```
PCO (defines the CLO and the problem class)
    ↓
★ ARCHITECTURE GENERATOR ★
    ↓
R1 — Workaround design (takes the chosen candidate and builds it out)
```

This skill does not design the architecture. It generates candidates. R1 does the design.

---

## The core method

**Step 1 — Extract the CLO from PCO.**
The Critical Limiting Operation is the specific activity in the conventional BFF that produces the cost-to-value barrier. It is always a thing someone does — a process step, a transaction, an operational activity — not a market condition or a customer behaviour.

**Step 2 — Abstract to structural class.**
Strip away the industry context. What type of cost problem is this, at its root? There are eight structural classes:

| Class | What creates the cost | Canonical example |
|---|---|---|
| **Capital commitment** | Must commit large capital per unit before revenue arrives | Lending, claim purchasing, inventory |
| **Information asymmetry** | One party has information the other doesn't; cost of verification is high | Credit assessment, claims validation, due diligence |
| **Coordination failure** | Multiple parties must act together; the cost of coordination dominates | Supply chains, co-ops, collective savings |
| **Trust deficit** | Counterparty risk drives expensive intermediation or collateral | Unsecured lending, informal markets, new entrants |
| **Access barrier** | Physical or logistical cost of reaching the customer | Last-mile delivery, rural healthcare, low-density markets |
| **Skill scarcity** | The limiting input is a rare human capability | Professional services, specialist manufacturing |
| **Time-intensity** | The unit takes a long time to resolve; carrying cost dominates | Litigation, construction, long-cycle sales |
| **Volume threshold** | The unit economics only work above a scale the customer cannot reach alone** | Small-batch manufacturing, pooled purchasing |

**Step 3 — Search for cross-domain analogues.**
For each structural class, identify domains outside the venture's industry where that class was solved at scale. Look especially for:
- Cases that achieved dramatic cost reduction (10× or more relative to the conventional BFF)
- Cases involving resource-constrained customers (the IVE target)
- Cases grounded in a named theory (social learning, peer governance, process substitution, platform economics)

**Step 4 — Extract the workaround mechanism.**
For each analogue: what specifically did they change at the BFF level? The mechanism is the answer — the design choice that produced the cost reduction.

**Step 5 — Translate and score.**
For each mechanism: can it be applied to this venture's CLO? Score on three dimensions:

- **Cost reduction potential (1–5):** How much of the CLO cost does this mechanism eliminate?
- **Theory grounding (1–5):** Is it backed by a named, tested theory with precedent?
- **Elegance (1–5):** Does the cost reduction happen through the design of the product itself, or does it require the team to execute well? 5 = structurally embedded; 1 = operationally dependent.

**Elegance is the key screen.** An architecture that is cheap only when run by exceptional people is not IVE-grade. The cost reduction must be a property of the BFF.

---

## Step 1: Extract the CLO

Ask the user to share their PCO output, or answer directly:

> "What is the Critical Limiting Operation — the specific activity in the conventional BFF that creates the cost-to-value barrier for your target customer? Name the activity and describe why it is expensive."

If the user has run `/balm-pco-custom`, the CLO is already defined. Ask them to paste it or point to the file.

Confirm:
- The CLO is a process step, not a market condition
- It is something that happens in the conventional BFF — not something the venture has chosen to do
- It is the primary driver of the cost-to-value barrier (not a secondary cost)

---

## Step 2: Abstract to structural class

Once the CLO is confirmed, classify it. Work through the eight classes:

> "What type of cost problem is this at its root?"

Show your reasoning. Name the primary class and any secondary classes. Example:

> "Your CLO — purchasing distressed consumer debt before the outcome is known — is primarily a **capital commitment** problem: you commit capital per unit before revenue arrives, and the carrying cost of that commitment is what makes the conventional model expensive. There's a secondary **time-intensity** dimension: the longer each unit takes to resolve, the higher the carrying cost. The architecture needs to attack both."

If the user disagrees with the classification, iterate. The class must be right before the analogue search is useful.

---

## Step 3: Cross-domain analogue search

For the identified structural class(es), generate 6–10 cross-domain analogues. For each:

**Format:**

> **[Analogue name]** — [Industry/domain]
> **What they did:** [One sentence describing the BFF design choice]
> **Why it worked:** [The mechanism — what specifically reduced the cost]
> **Theory:** [Named theory or principle]
> **Precedent evidence:** [Scale achieved, outcome measured]

Work through the eight structural classes systematically. Do not limit to the venture's industry. The further the domain, the more likely the analogy is novel.

**Reference analogues by structural class (seed list — extend from context):**

*Capital commitment:*
- Grameen Bank: peer group liability shifts collateral cost from the lender to the social network. No physical collateral required. Theory: social capital as credit substitute (Putnam, 1993).
- Rotating savings and credit associations (ROSCAs): pool small regular contributions to create lump sums for each member in turn. Eliminates the lending institution entirely. Theory: temporal arbitrage within a trust network.
- Invoice factoring: sell the receivable to a specialist who carries the capital cost. Unbundles the capital commitment from the operational delivery.

*Information asymmetry:*
- Ford's assembly line: moved the inspection function upstream (in-process quality checks) rather than end-of-line rejection. Made information about defects available at the point where correction was cheapest.
- Calmly-style C3 assessment: independent third-party assessment at point of acquisition reduces the proportion of units entering the expensive long tail. Converts outcome uncertainty into a scored probability at low unit cost.
- Microfinance loan officers (BRI Indonesia): embedded agents with local knowledge replace central credit assessment. Information cost collapses because the agent already knows the borrower.

*Coordination failure:*
- Ostrom's common-pool resource governance: community-managed rules replace state or market coordination. Works when: group is bounded, members are identifiable, monitoring is mutual. Theory: Ostrom (1990).
- Agricultural co-operatives: pool purchasing power to reach volume thresholds individually unachievable. Coordination cost borne by the co-op structure, not the individual farmer.
- Open-source software: distributed production eliminates the coordination cost of a central R&D function. Contribution is self-selecting; quality is enforced by peer review.

*Trust deficit:*
- Kiva: social proof from lender community replaces institutional due diligence. The crowd validates where the institution cannot.
- M-Pesa: mobile money built trust through a network of physical agents (trust proxies) before the digital transaction was credible on its own.
- Airbnb: mutual review system creates reputational stakes that substitute for contractual guarantees.

*Access barrier:*
- Narayana Hrudayalaya (heart surgery): hub-and-spoke model with telemedicine triage. Complex care concentrated at scale; routine care delivered locally. Access cost falls without quality loss.
- Last-mile logistics (e.g. Jumia Africa): agent networks in dense informal settlements replace centrally-managed delivery. Local agent carries access cost in exchange for commission.

*Skill scarcity:*
- Task decomposition (Taylor / scientific management): break complex work into simple repeatable steps. Each step requires less skill than the whole. Replaces scarce experts with trained generalists.
- Algorithm-assisted diagnosis (e.g. IDx-DR): moves skill from a specialist to an algorithm. The algorithm is expensive to build, cheap to run.

*Time-intensity:*
- Continuous-process manufacturing (meatpacking → Ford): eliminate waiting time between steps by reorganising the sequence. The unit never stops; carrying cost approaches zero.
- Structured negotiation protocols: define the decision tree upfront, compress the resolution timeline. Reduces the number of months each unit spends in the expensive tail.

*Volume threshold:*
- Shared services centres: aggregate low-volume functions across organisations to reach the scale at which unit cost falls. Individual firms can't reach it; the shared structure can.
- Group purchasing organisations (GPOs): pool buying power across members. Reach manufacturer minimums that no individual member could meet.

---

## Step 4: Filter and translate

Apply three filters to reduce 6–10 analogues to 3–4 viable candidates:

**Filter 1 — Mechanism transferability.** Can the mechanism be applied to this venture's CLO without requiring conditions the venture cannot create? (e.g. a peer-group accountability mechanism requires that the customer has pre-existing social ties — if the customer segment is atomised, this fails.)

**Filter 2 — Elegance screen.** Does the cost reduction happen through product design, or through operational excellence? Keep only mechanisms where the cost reduction is structural.

**Filter 3 — Theory grounding.** Is there a named, tested theory explaining why this mechanism works? Discard mechanisms where the reasoning is "it worked over there" without a causal account.

For each surviving candidate, state explicitly:
- What changes at the BFF level
- What stays the same
- What the critical assumption is (the condition that must be true for the mechanism to work in this context)

---

## Step 5: Score and rank

Score each candidate on the three dimensions:

| Candidate | Cost reduction potential | Theory grounding | Elegance | Total |
|---|---|---|---|---|
| [Name] | /5 | /5 | /5 | /15 |

Present in rank order. Recommend the top candidate with a one-sentence rationale.

**Ranking rule:** If two candidates score similarly, prefer the one with higher elegance. An architecture that costs little to run well is worth more than one that saves more money but requires exceptional execution.

---

## Step 6: Output

Produce a summary document as an HTML file.

Save to: `ventures/{venture-slug}/architecture-candidates-{date}.html`

Use the standard design system (DM Sans + Lora, #f5f4f1 background, #0f2744 navy panel).

The document contains:

1. **CLO statement** — the confirmed Critical Limiting Operation
2. **Structural class** — primary and secondary, with one-line reasoning
3. **Candidate architectures** — one card per candidate:
   - Analogue name and domain
   - Mechanism of action
   - Theory grounding
   - Critical assumption
   - Score (cost reduction / theory / elegance / total)
4. **Recommended candidate** in a navy panel — name, mechanism, and one-sentence rationale
5. **Routing instruction:** "Take the recommended candidate into `/balm-challenge-1-custom` (R1) to design the full Workaround Strategy."

Open in browser after saving.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-architecture-generator-custom/SKILL.md` to modify
- **Runs after:** `/balm-pco-custom` (PCO defines the CLO)
- **Feeds into:** `/balm-challenge-1-custom` (R1 — the practitioner takes the chosen candidate and designs the full Workaround Strategy from it)
- **On FIT Verifier FAIL:** this skill is the re-entry point. The FIT Verifier diagnosis tells you which class of problem the current architecture is failing on — use that to search for a candidate that attacks the cost differently
- **Key references:** Grameen/Yunus (1983); Ostrom (1990); Simanis et al. (2021) Cornell IVE; Ford/Taylor on process substitution
- **Related skills:** `/balm-pco-custom`, `/balm-challenge-1-custom`, `/theory-of-change-custom`, `/ive-fit-verifier-custom`
