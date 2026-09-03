# The Realisation Standard — from ratified architecture to realised products

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Added:** 28 August 2026 · **Status: DRAFT v0.1 — awaiting Tom's review.** Written in ASD-STE100 register.
**Parent:** `derivation-standard.md` (one architecture, three projections — this standard runs the product projection to completion).
**Vocabulary:** `glossary.md` is the controlled vocabulary. This file does not redefine terms.

> **⚠ VOCABULARY DEPENDENCY.** The process-primary re-basing (parked 23 Aug 2026) is not decided. This draft uses process verbs where possible. If Tom approves the re-basing, review the nouns in this file before v1.0.

> **⚠ TWO OPEN RULINGS sit inside this standard.** See "Open rulings" at the end. Each is marked **[OPEN — TOM]** where it lands in the text.

---

## The principle

One pipeline takes a product from ratified architecture to a realised product that passed first-article inspection.

The pipeline is stated once. It is the same for all four product types. Type content enters at two points only:

1. **The requirements stack** — the type's Level 1, 2 and 3 statements (`Product_Architecture_Definitions.md`).
2. **The type insert** — the type's U-set, its primary sources, and its type standards (this file, below).

A rule stated in the pipeline is not restated in a type insert. A bound the VDR holds is not restated here. If a caution you want to add is already a bound, it is duplication (VA-67). Two copies of one rule become different the first time one copy changes.

---

## Entry condition

Start the pipeline only when all of these are true:

- The architecture is ratified and behind its gate. Forward-only applies (VA-52).
- The VDR is the design authority. Every downstream question checks the VDR first and cites the section.
- An NCR is the only route back into the architecture. A derivation gap is an architecture finding. Report it upstream. Do not work around it.

### The bridge check — per actor, before Step 1 (added 1 Sep 2026, Tom's ruling)

Ratified architecture is not automatically realisable. Before the pipeline runs for any product, confirm three definitions are **present and current** for every actor that product touches:

1. **Outcome** — the actor's first-person outcome, from the AOM. Current means re-examined since the last architecture change that touched this actor. An outcome written under a superseded payer, mechanism or scope is stale even if its words still read well.
2. **KMC** — the actor's key monetizable cost, stated with its basis. The product's claims, price and copy derive from it; an unstated or under-revision KMC means there is nothing current to derive from.
3. **Journey** — the actor's state track in the CTM at the current challenge state. Asserted-unchanged across an architecture change does not count (the C10 lesson): the track must exist as a drawn, validated model.

**If any of the three is missing, stale, or under revision: realisation for that actor holds at demonstration state, and the gap routes to the owning challenge as work — not to the realisation queue as a blocker note.** The bridge check is cheap (three lookups); skipping it is not.

*Origin: Calmly, 1 Sep 2026. Site-facing products were in realisation while the site's outcome had not been re-examined since payment was de-scoped from C7, its KMC was under revision on two findings, and its journey awaited reconciliation with a C6 re-run. The products had nothing current to derive from, and only a manual hold caught it.*

---

## The pipeline — nine steps

**Step 1 — State the requirements stack for the product type.**
Write the Level-1 sentence: which actor, which routine, which loss, which causal chain.
Write the Level-2 contribution with its fin-sim constraints.
Confirm the Level-2 contribution closes in the fin-sim.
List the Level-3 requirements: the type's U-set plus the venture's 11-field flow specifications.
Check the trace rule: each Level-3 requirement traces to Level 2, each Level-2 contribution to Level 1.
A requirement with no upward trace is scope creep. Remove it or record it upstream.

**Step 2 — Derive the product elements.**
Apply the derivation standard in full:
- Each component cites the challenge requirement it satisfies.
- Each surface maps to one **active** step of the product use routine. A passive step gets no surface.
- Each architectural prohibition becomes a built absence, not a permission.
- Each operating rule that binds at runtime becomes an interlock that can refuse.
An element you cannot cite, and that is not true, is invention. Delete it.
An element you cannot cite, but that is true, is an undocumented requirement. Record it upstream first. Then build it.

**Step 3 — Set the realisation order.**
Order the four products by dependency, then by which components carry the Key Cost:
- The Working Product comes before the Communications Product. The value proposition is the Working Product journey, described. You cannot describe a journey that does not exist.
- The Payment Product trigger is a value event. Specify the value event in the Working Product before you realise the Payment Product.
- Realise a Partner Product before the point where its capacity gates an interlock (example: no intake without committed capacity).
Record the order and its reasons in the realisation queue. Each queue item names the actor it serves.
Order governs the build sequence only. It does not permit realising one product in isolation — see Step 4.

**Step 4 — Hold the journeys across the four products.**
The actor does not experience four products. The actor experiences one journey, and the four products are its stages: become aware → act → reach the outcome → make the payment. A partner runs its own journey to its own outcome.
The four products are realised in conjunction, with awareness of each other. The connective tissue between them is the easiest thing to lose, because no single product owns it.
Rules:
- Map each actor's journey end to end, across all four products, before any one product's specification closes.
- The product use routine is the single source for the journey. All four products project from the same routine. Two products that read different routines will not join.
- Specify each handoff between products as an interface: name the state the actor is in, what carries over (data, expectations, commitments), and which product owns the next step.
- A handoff with no owner, or with nothing carried over, is a gap. Log it as an architecture finding.
- Verify by walking the journey as the actor. Every step lands in exactly one product. No step is orphaned between two products.
The mechanical check in the Communications insert is one instance of this rule: the published proposition and the built journey are two projections of the same routine, compared field by field. The same comparison applies at every product boundary.

**Step 5 — Mine analogues for each journey.**
Before you specify, find companies whose customers already run a comparable journey. Take whatever transfers.
The working assumption, stated as one: mass-market UX patterns carry very large accumulated research and optimisation investment — hundreds of thousands of hours. Adopt a proven pattern and you inherit that investment. Invent a new pattern and you pay for it yourself, in field failures.
Rules:
- Match on journey shape, not on industry. The analogue is the company whose actor makes the same kind of step: accept an offer, complete a checkout, sign a mandate, track a case, onboard as a supplier.
- Mine at two grains: the whole journey (how the stages sequence, where trust is built, where friction is placed deliberately) and the single step (the form, the confirmation, the handoff screen).
- Take the pattern, not the content. The derivation standard still governs: the pattern is the form; every element's content still cites the architecture.
- Depart from a proven pattern only with a named reason. A departure is a bet against the analogue's optimisation, and the burden of proof sits with the departure.
- Record the analogue per journey stage in the specification, with a source line. An unrecorded borrowing cannot be re-checked when the analogue's pattern moves on.
This is the VA-1 move one level down: the synthesis check finds the business analogue for the architecture; this step finds the journey analogues for the realisation.

**Step 6 — Write the buildable specification.**
Close the design to buildable per the detailed-design discipline (PDR→CDR): a specification per component, a routine per activity, an interface specification per connection.
Each acceptance criterion, if passed, must evidence the Level-1 chain. A criterion that a component can pass while the loss survives is decorative. Rewrite it.

**Step 7 — Build the Test Product first.**
A Test Product verifies or demonstrates the design. It is never for live use.
Give it a TP-NNN identity and a banner that states what is not yet true.
A Test Product proves the design on paper. It does not prove the build.

**Step 8 — Build the Realised Product.**
A Realised Product is built for real use, within the bounds the VDR sets.
For the first instance, shrink the instance. Never remove components. State the evidential cost of anything absent.
Do not restate the VDR's bounds in the product definition. The bounds bind through Step 2's interlocks and absences.

**Step 9 — Run first-article inspection at first live operation.**
Inspect the FIRST Realised Product of each type. The check is two questions:
1. Did the actor do the thing?
2. Did anything fall outside the VDR's bounds?
The bounds register is the VDR itself. Maintain no separate list.
At tranche 1, also walk each actor's full journey across the four products, as the actor. The per-type inspections do not test the handoffs; the walk does.
**[OPEN — TOM]** A second axis is proposed: each product also meets a named external design standard for its kind. Candidates and the selection rule are in the verification register. Do not apply this axis until Tom selects the standards.
A failed first article raises an NCR. The NCR route decides rework, use-as-is, or scrap.

---

## Type inserts

Each insert gives only what is specific to the type. The pipeline above applies to all four.

### Working Product

- **Level-1 sentence:** eliminates a named loss (the Key Monetizable Cost) in the customer's current routine, for an outcome the customer already pursues.
- **Primary sources:** the product use routine with active/passive markings; the component register (each component cites its requirement).
- **U-set:** WP-U, plus U0 ownership.
- **Type rule:** the Working Product creates the value surplus. The other three products distribute, capture, or spend that surplus. Its per-unit cost stays at or under the ARM allocation.
- **Downstream duty:** its journey is the source for the value proposition. Its value events are the source for the Payment Product triggers. Keep both explicit and citable.

### Communications Product

- **Level-1 sentence:** eliminates the adoption gap — makes the actor aware of the value proposition (mental availability), and able to act on it (physical availability). "Act on", not "buy": an actor who pays nothing acts by acceptance. *(Principal ruling, 28 Aug 2026 — the two verbs map to the two Ehrenberg-Bass availabilities.)*
- **Two sub-types, two work packages:** easy to recall (advertising; memory structures linked to category entry points; builds mental availability) and easy to buy (how easy it is to find and to buy — the route to transact or accept exists, and the customer journey has no friction; builds physical availability). There is no conviction gap (principal ruling, 28 Aug 2026).
- **Derivation:** derive the value proposition from the Working Product journey. Three required fields: the outcome, the key monetizable cost eliminated, the journey. One value proposition per actor, not one per venture.
- **Mechanical check:** compare the published proposition against the Working Product journey as built, field by field. A claimed outcome the journey does not reach is a defect. A claimed cost the journey does not eliminate is a defect.
- **U-set:** CP-U, plus Brand component requirements.
- **Type standards:** `sales-marketing-asset-standard.md` (what to say) · `landing-page-standard.md` (layout).
- **Type rules:** where an operating register governs wording, copy comes from the approved set only. Every number carries its band, source and grade (band-never-bare).

### Payment Product

- **Level-1 sentence:** converts a completed, evidenced value event into venture revenue, with no new loss on either side. **[OPEN — TOM]** This is the only Level-1 definition written as a venture benefit, not as a loss eliminated in an actor's routine. Tom to rule whether Level 1 changes to restore the symmetry, or stays.
- **Realised form (ruled 27 Aug 2026):** a realised Payment Product helps the customer make the payment, within the bounds the VDR sets. That is the whole requirement.
- **Bounds (cited, not restated):** trigger = value event (PP-U1) · terms from the Working Product design · the venture's invariants · floor from the fin-sim.
- **U-set:** PP-U.
- **Type rule:** no working capital beyond the billing cycle, unless the model explicitly prices that capital.

### Partner Product

- **Gate first — the vendor boundary test.** Does participation require the counterparty to change its routine, absorb venture-specific risk, or make venture-specific investments?
  - **No** → commodity vendor. Stop. No Partner Product. Apply procurement discipline only (Part-U2 modularity, Part-U3 SLA).
  - **Yes** → partner. Continue the pipeline.
- **Level-1 sentence:** eliminates a named loss in the partner's current routine, such that supplying what the venture needs — but cannot buy at standard terms — becomes the partner's best way to achieve their own outcome.
- **Two species, one definition:** gateway partners (what flows back is customer access) and capability partners (what flows back is an input the venture cannot own or buy off the shelf). Species are dynamic. Re-test the boundary when a partner's market changes.
- **U-set:** Part-U in full.
- **Type rules:** the partner's own committee must approve it (Part-U1). Partner-side economics stay positive. Validation is the partner adopting through its own governance and renewing on its own P&L, without subsidy.
- **Required step — define the partner proposition before realising the product (added 1 Sep 2026, Tom's ruling).** For each partner actor, ratify a Partner Proposition statement before any Partner Product hardens past demonstration state. Simpler than the value proposition — partners need a business case, not a KMC derivation (Tom's refinement, 1 Sep): the partner's **outcome** (first-person), their **business case** — what supplying us earns them, what it costs them, and why it beats their next-best use of the same capacity, in the numbers their own committee needs to say yes (Part-U1) — **how supplying us fits their operation**, and **what they earn and when**. The Partner Product — terms, onboarding, interfaces, the file we hand them — derives from this statement the way site-facing products derive from the site's value proposition. A partner with no ratified proposition gets no realised product; the gap routes to the owning challenge (usually C7 or C10) as work. This is the bridge check (VA-76) applied to enabler actors, with the proposition as the artefact that satisfies it.

---

## Open rulings

| # | Ruling needed | Where it lands | Owner |
|---|---|---|---|
| 1 | Payment Product Level-1 symmetry — change the definition to a loss eliminated in an actor's routine, or keep the venture-benefit form | Payment insert, Level-1 sentence | Tom |
| 2 | External design standards — select the named standard per product type (second axis of first-article inspection) | Step 9 | Tom |
| 3 | Process-primary re-basing — decides the nouns this file uses at v1.0 | Whole file | Tom |

---

## Checklist — any realisation run

- [ ] Entry condition confirmed: architecture gated; VDR cited; NCR is the only route back
- [ ] Level 1–3 stack stated and traced; Level 2 closes in the fin-sim
- [ ] Every element cites its architecture element; absences built as absence; runtime rules built as interlocks
- [ ] Realisation order recorded with reasons; Working before Communications; value events before Payment
- [ ] Each actor's journey mapped end to end across all four products, from the one product use routine
- [ ] Every handoff between products specified: actor state, what carries over, which product owns the next step
- [ ] Journey walked as the actor; no step orphaned between two products
- [ ] Analogues mined per journey and per step; each borrowing recorded with a source line; each departure carries a named reason
- [ ] Buildable specification complete; every acceptance criterion evidences the Level-1 chain
- [ ] Test Product built first, bannered, TP-NNN
- [ ] Realised Product instance shrunk, no component removed, absences priced
- [ ] First article: the two questions, against the VDR only
- [ ] Anything underivable logged as an architecture finding, not worked around
