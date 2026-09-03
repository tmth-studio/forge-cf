---
name: ive-consistency-audit-custom
description: Consistency Audit Agent for IVE ventures. Holds all 10 BALM requirement solutions in context simultaneously, maps the cross-requirement dependency matrix, and surfaces logical contradictions — replacing the completeness check in verify-balm-custom with a logical consistency check. Runs after all 10 requirements are designed.
---

# IVE Consistency Audit Agent

Runs after all 10 BALM requirements are designed. Its job is to catch contradictions that are invisible to a practitioner working through requirements one at a time.

**The problem it solves:** The 10 requirements are interdependent. R6 Amortization must work within the BFF the R1 Workaround Strategy established. R8 Lock-in depends on accumulation data that R5 Adoption must generate. R9 control of a scarce resource may conflict with R7 open access for gateway partners. A sequential design process cannot catch these tensions — no practitioner can hold all 10 strategies in working memory and trace dependencies simultaneously.

`verify-balm-custom` checks completeness: are all fields present? This skill checks consistency: do the solutions contradict each other?

---

## Where this fits in the IVE sequence

```
R1 → R2 → R3 → FIT Verifier → R4 → R5 → R6 → R7 → R8 → R9 → R10
                                                              ↓
                                              ★ CONSISTENCY AUDIT ★
                                              (run after all 10 are designed)
                                                              ↓
                                              PASS → architecture is internally consistent
                                              FAIL → contradictions diagnosed, resolutions proposed
```

Do not run this skill until all 10 requirements have been designed. It requires the full set.

---

## The dependency matrix

These are the known cross-requirement dependencies. Each dependency is a logical claim: if requirement A is designed a certain way, requirement B must be compatible with that design choice.

### F1 dependencies (cost and value architecture)

**R1 BFF → R6 Amortization**
R6 must design a cash flow solution that works within the Business Form Factor R1 established. If R1's BFF requires payment before the customer receives the outcome (e.g. a purchase-and-resolve model), R6 cannot assume the customer pays after resolution. The BFF sets the payment timing constraint; R6 must work within it.

*Contradiction signal:* R6 proposes a payment timing or format that R1's BFF makes structurally impossible.

**R1 cost structure → R2 value ceiling**
Already verified by the FIT Verifier, but worth re-checking at full audit: does the R2 price ceiling still hold against the R1 cost structure as finally designed? Cost assumptions sometimes drift between the FIT gate and the completion of all 10 requirements.

*Contradiction signal:* R1 cost structure has changed since the FIT Verifier ran and now pushes required price above the R2 ceiling.

**R3 Scaling mechanism → R8 Lock-in**
R3 designs the mechanism for reaching scale without a proportional increase in cost. R8 designs a switching cost. If R3's scaling mechanism involves open partner networks or interoperability (to reach scale cheaply), it may compromise R8's lock-in — because open systems are harder to exit-proof.

*Contradiction signal:* R3 opens the system to reach scale; R8 requires closure to create switching cost. Both cannot be true simultaneously.

### F2 dependencies (customer normalisation)

**R5 Adoption data → R8 Lock-in**
R8 requires accumulation of customer-specific data or history to create a switching cost. That accumulation must happen through R5 — the adoption process is what generates the data. If R5's adoption design does not create accumulation (e.g. it uses anonymous transactions, or the data stays with the customer rather than the venture), R8 has no switching cost to build on.

*Contradiction signal:* R5 is designed for fast, frictionless adoption without data capture; R8 requires customer-specific data to be held by the venture.

**R7 Gateway Partners → R9 Scarce Resource**
R7 designs open access for gateway partners — third parties who extend the venture's reach. R9 controls a scarce resource or position to lock out competitors. If the scarce resource is the same channel or relationship that R7 proposes to share with gateway partners, the two strategies contradict: you cannot simultaneously open a position to partners and control it as a competitive moat.

*Contradiction signal:* R9 names a scarce resource (supplier, channel, data, regulation) that R7 has already proposed sharing with partners.

**R4 Attraction → R7 Gateway Partners**
R4 designs how the venture overcomes customer doubt about value at first encounter. R7 designs which gateway partners activate that first encounter. If R4's proof mechanism requires a controlled environment (a demonstration, a trial, a specific setting) that the R7 partner cannot provide, the gateway cannot deliver the attraction.

*Contradiction signal:* R4 requires proof conditions (e.g. a supervised pilot, a specific technology) that the R7 partner network cannot replicate at scale.

**R6 Amortization → R2 Key Monetizable Cost**
R6 designs the payment structure (when, how much, in what format the customer pays). R2 defines the Key Monetizable Cost — the customer's current cost that the venture absorbs. If R6's payment structure requires cash at a time when the customer does not have it (outside their cash rhythm), the KMC is real but the payment solution doesn't work.

*Contradiction signal:* R6 payment timing does not align with the customer's cash rhythm as established in R2 fieldwork.

### F3 dependencies (market position)

**R8 Lock-in → R10 Competitive Moat**
R8 creates a switching cost for existing customers. R10 establishes a structural barrier to new competitors entering the market. If R8 is built on data accumulation that competitors could replicate (generic transaction data, publicly available records), R10 has no durable foundation — a competitor who enters and accumulates their own data will eventually match the switching cost.

*Contradiction signal:* R8 switching cost is based on an asset that competitors can accumulate independently; R10 moat depends on R8 being proprietary.

**R9 Scarce Resource → R10 Competitive Moat**
R9 controls a scarce resource; R10 establishes the competitive moat. If R9's scarce resource is regulatory (a licence, an exclusive relationship), R10 must account for the risk that the resource becomes available to competitors. If R9's resource can be replicated or substituted, R10 is only as durable as R9's exclusivity.

*Contradiction signal:* R9 names a scarce resource but does not account for how it remains scarce as the venture grows and attracts imitators.

---

## Step 1: Collect all 10 requirement solutions

Ask the user to provide the key outputs for each requirement. For each, the minimum needed is:

| Requirement | What to collect |
|---|---|
| R1 — Workaround | BFF description + cost structure + Workaround Theory of Change |
| R2 — Efficacy | Key Monetizable Cost + price ceiling + Attendant Routine summary |
| R3 — Scaling | Scaling mechanism + working capital solution |
| R4 — Attraction | Want Block identified + proof mechanism at point of encounter |
| R5 — Adoption | Use Block identified + adoption pathway + what data is captured |
| R6 — Amortization | Buy Block identified + payment structure (timing, format, amount) |
| R7 — Gateway Partners | Partner type + what the venture shares with them + what the partner provides |
| R8 — Lock-in | Switching cost mechanism + what accumulates + who holds it |
| R9 — Lock-out | Scarce resource or position + how it is controlled + durability case |
| R10 — Leverage | Competitive moat claim + what makes it structural |

If the user has a BALM document or transcript, ask them to paste it or point to the file. Read it and extract the relevant outputs.

If any requirement is incomplete, note it — but proceed with the audit for the requirements that are present. Flag the gap separately.

---

## Step 2: Run the dependency checks

Work through each dependency pair systematically. For each:

1. State what R[A] requires of R[B]
2. State what R[B] actually says
3. Assess: consistent / borderline / contradictory

**Consistent:** R[B]'s design is compatible with R[A]'s constraint. No action required.
**Borderline:** R[B]'s design is compatible with R[A] under certain conditions — name them explicitly. Flag as a critical assumption to test.
**Contradictory:** R[B]'s design directly conflicts with R[A]'s constraint. Name the specific clash. Propose a resolution.

---

## Step 3: Surface additional tensions

Beyond the known dependency pairs, look for any of these structural patterns that indicate hidden contradictions:

**The openness paradox:** Any requirement that proposes sharing something (partners, data, access) may conflict with any requirement that proposes controlling something. Check every R7 sharing design against every R8/R9 control design.

**The scale-lock tension:** Designs that achieve scale by reducing friction (lowering barriers, removing friction, opening access) often undermine lock-in designs that require friction to work (switching costs depend on investment, habituation, or data accumulation that frictionless products don't generate). Check R3 against R8.

**The payment-adoption conflict:** If R5 is designed to maximise adoption speed (get to the outcome fast), it may not generate the usage data R6 needs to offer flexible payment. Fast adoption without data = no proof of value = no basis for deferred payment.

**The proof-at-scale problem:** R4 proof mechanisms that work in a controlled pilot (supervised demonstration, curated trial) may not be replicable by the R7 partner network at scale. Check that R4's proof mechanism can be delivered by R7's partners without the venture being present.

---

## Step 3b: Distinguish conditions from component design requirements

Before classifying any item as 🟡 Borderline, apply this test:

**Is this a gap in the BFF that cannot be resolved through component design alone?**

- **Yes → genuine condition:** something the architecture depends on that isn't yet specified, requires action outside the venture's direct control, and would cause an architectural failure if omitted at the BFF level. Classify as 🟡 Borderline and surface as a condition.

- **No → component design requirement:** an implementation requirement that follows naturally from the architecture, is within the venture's direct control to specify and build, and gets resolved when that component is designed in Phase 5. Classify as 📋 Phase 5 component note.

**The key diagnostic questions:**
- Can this be resolved through a product feature, a contract, a legal agreement, or an operational process that the venture designs and controls?
- Does resolving it require changing the BFF, or only specifying how a component is built?
- Is this already implied by the architecture, just not yet written into a spec?

If the answer to any of these is "yes, it's a component" — it is not an audit condition. It is a Phase 5 design note. Include it in the output as a component note, not a condition. It does not affect the PASS / FAIL verdict.

**Examples:**
- "The sign-up flow must disclose pool insurance before membership confirmation" → component design requirement for the sign-up flow. Not a condition.
- "Assessment org engagement agreements must include NDA and non-solicitation provisions" → component design requirement for the supplier engagement agreement. Not a condition.
- "R6's payment structure requires the customer to have cash at a time the architecture doesn't guarantee" → genuine condition — changes the BFF or requires a new mechanism.

---

## Step 4: Verdict

### PASS — no material contradictions

> **Verdict: PASS**
>
> The 10 requirement solutions are internally consistent. No material contradictions found across the dependency matrix.
>
> [List any borderline items as critical assumptions that fieldwork or pilots should test.]
>
> Proceed to implementation sequencing.

### PASS WITH CONDITIONS — borderline items present

> **Verdict: PASS WITH CONDITIONS**
>
> The architecture is broadly consistent, with [N] conditions that must be managed:
>
> [For each borderline item:]
> - **[Dependency pair]:** Compatible only if [specific condition]. This is a critical assumption — test it before committing to this design.

**Before finalising conditions:** apply the Step 3b test to every 🟡 item. Any item that can be resolved through component design is a Phase 5 note, not a condition. Remove it from the conditions list and add it to a "Phase 5 component notes" section in the report. A clean architecture with only component-level implementation requirements should return a PASS verdict, not PASS WITH CONDITIONS.

### FAIL — contradictions present

> **Verdict: FAIL — [N] contradictions require resolution**
>
> [For each contradiction:]
>
> **Contradiction [N]: [Requirement A] vs [Requirement B]**
> - R[A] requires: [what it needs from R[B]]
> - R[B] says: [what it actually does]
> - The clash: [one sentence naming the specific logical conflict]
> - Resolution options:
>   1. Change R[B] to: [specific design change — always the later requirement]
>   2. Add a bridging mechanism: [description]
>
> Resolve each contradiction and re-run the audit before finalising the architecture.

**Directionality rule — never revise an earlier requirement to satisfy a later one.**

The IVE sequence is intentionally ordered. R[A] was designed, FIT-verified, and confirmed before R[B] was attempted. R[B] was designed knowing R[A]'s constraints. If a contradiction exists between R[A] and R[B], it means R[B] failed to be consistent with R[A] — not that R[A] needs to change.

Resolutions always move forward:
- Change R[B] so it is consistent with R[A]
- Add a bridging mechanism that resolves the tension without altering either

The only exception: if R[A] is found to rest on a factual error (a wrong assumption about the market, a miscalculation in the FIT Verifier) — that is a data problem, not a design problem, and must be flagged separately as a validation gap, not resolved by redesigning R[B].

---

## Step 5: Output

Produce a consistency audit report as an HTML file.

Save to: `ventures/{venture-slug}/consistency-audit-{date}.html`

Use the standard design system (DM Sans + Lora, #f5f4f1 background, #0f2744 navy panel).

The document contains:

1. **Audit summary** — overall verdict (PASS / PASS WITH CONDITIONS / FAIL), date, venture name
2. **Dependency matrix** — a table showing all dependency pairs checked, with traffic-light status:
   - 🟢 Consistent
   - 🟡 Borderline (condition named)
   - 🔴 Contradictory

| Dependency | R[A] requires | R[B] says | Status |
|---|---|---|---|
| R1 BFF → R6 Amortization | | | 🟢 / 🟡 / 🔴 |
| R5 Adoption → R8 Lock-in | | | |
| R7 Gateway → R9 Scarce Resource | | | |
| … | | | |

3. **Contradiction details** — one section per 🔴 item, with the clash named precisely and resolution options
4. **Borderline conditions** — one section per 🟡 item, with the condition named as a critical assumption
5. **Phase 5 component notes** — items that are not architectural conditions but are implementation requirements that follow from the architecture. These belong in Phase 5 component specs. Listed here so they are not lost.
6. **Routing instruction:**
   - PASS: "Architecture is internally consistent. Proceed to implementation sequencing."
   - FAIL: "Resolve contradictions in requirements [list] and re-run `/ive-consistency-audit-custom`."

Open in browser after saving.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-consistency-audit-custom/SKILL.md` to modify
- **Runs after:** all 10 BALM requirements are designed — this is the final gate before implementation
- **Complements, does not replace:** `verify-balm-custom` checks completeness (fields present); this skill checks consistency (fields don't contradict). Run both.
- **On FAIL:** the resolution is always a change to one of the requirement solutions. Identify which requirement to return to, make the design change, and re-run the audit.
- **Known dependency pairs:** R1→R6, R1 cost→R2 ceiling, R3→R8, R5→R8, R7→R9, R4→R7, R6→R2, R8→R10, R9→R10 — always check all of these, plus any additional tensions surfaced in Step 3
- **Model stack reference:** Before running this audit, read `method/wiki/Methodology/Model_Stack.md`. It documents the full dependency chain (BALM → CTM → AOM → ARM → Fin-Sim → FMOS) and the build sequence. The consistency audit checks BALM-level coherence; the model stack explains how BALM solutions propagate into the downstream models — which is why BALM contradictions matter beyond the design document itself.
- **Related skills:** `/verify-balm-custom` (completeness), `/ive-fit-verifier-custom` (financial gate at F1/F2 boundary), `/balm-challenge-1-custom` through all requirement skills
- **Condition vs component discipline:** Before marking any item as a condition, apply the Step 3b test. Many apparent "borderline" findings are Phase 5 component design requirements — they don't affect the PASS verdict and don't require BFF revision. The discipline is: conditions change the architecture; component notes specify how the architecture is built.
