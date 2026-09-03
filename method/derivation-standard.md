# The Derivation Standard — one architecture, three projections

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Added:** 27 August 2026 (Tom: *"Product should be a derivation too right?"*).
**Children:** `sales-marketing-asset-standard.md` (what to say) · `landing-page-standard.md` (how to lay it out).

---

## The principle

**Everything downstream of the architecture is a projection of it.** Not inspired by it, not consistent with it — *derived* from it, field by field, with a citation.

The venture design record already holds the answers. What varies is the projection function: the product asks *what must exist*, the assets ask *what to say*, the org asks *who runs it*. Same source, three readings.

|  | Asks | Reads from |
|---|---|---|
| **Product** | What must exist — and what must not | Challenge requirements · product use routine · operating rules · invariants |
| **Assets** | What to say | HIO · exclusive KMC component · use routine · C4/C5/C6 blocks |
| **Org and process** | Who runs it, on what cadence | AOM activities · routines · interfaces |

**The test is the same for all three:** every element cites the architecture element it serves. Cannot cite but true → an undocumented requirement; record it upstream, then build it. Cannot cite and not true → invention; delete it.

Which makes every projection a **verification instrument on the architecture**. A thing you cannot derive is a gap you had not noticed, found at the cost of a draft rather than a meeting.

---

## The product projection

Already practised, not newly invented: the Calmly build spec gives every one of its 29 components a *requirement it serves* and a *rules* field. This codifies what that discipline is doing.

| Product element | Derives from | Rule |
|---|---|---|
| **Components** | The challenge requirement it satisfies | A component with no requirement does not get built. The build spec's existing four-field record is the instrument. |
| **Surfaces / screens** | The **active** steps of the product use routine | One surface per step where the customer acts. **A passive step needs no surface** — building one is waste, and usually a sign the routine was not consulted. |
| **Absences** | The invariants and the operating register | The architecture specifies what must *not* exist as firmly as what must. These are load-bearing and must be built as absence, not as permission. |
| **Runtime gates** | Operating rules that bind during operation | A rule that can be breached at runtime becomes an interlock in the product, not a line in a policy document. |
| **Build sequence** | Dependency order, then which components carry Key Cost | Invariant-carrying components first: building the control late means operating without it. |
| **What ships in tranche 1** | The minimum representative instance | Shrink the instance, never remove components. |

### Negative derivation — the part that gets missed

Most product thinking derives features. The architecture also specifies **absences**, and they are harder to hold because nothing reminds you of them.

Calmly's C9 two-layer rule says publish the aggregate, keep the granular. The correct product expression is that **no per-claim view exists anywhere in the site-facing application** — not hidden behind a permission, not admin-only. Absent. A permission can be granted by a support engineer at 5pm on a Friday; an absence cannot.

**Rule: where the architecture forbids something, build the absence, not the permission.** Then the constraint survives contact with a hurried human, which is the only test that matters.

### Runtime gates — rules that must be able to refuse

Calmly's OR-08 says no claim intake without committed capacity. Expressed as a document, it is a rule someone must remember. Expressed as a product element, it is a conformance check that **fails and blocks go-live** — including in the demo, where it would have been easy and dishonest to let it pass.

**Rule: an operating rule that can be breached during operation becomes an interlock. If it only exists in prose, it will be breached.**

---

## Why this matters more than it sounds

Three consequences, in ascending order of value.

**It removes the blank page.** Product specs and marketing copy are both usually written from scratch by someone re-deriving the strategy badly. Here they are readings of a document that already exists, made under verification, with evidence grades attached.

**It makes drift detectable.** If the product and the assets are both projections of the same source, a divergence between them is a defect with a location — one of them stopped tracking the record. Today's evidence: the studio home page still described a DBA-funded no-win-no-fee platform four months after that architecture was replaced. Nobody noticed, because nothing checked the projection against the source.

**It turns downstream work into upstream verification.** Building the Calmly product surfaced an inconsistency between Appendix B's cost build-up and the venture's own dispute rate. Writing the page surfaced that the value case was being led from the non-exclusive component. Neither was found by reading the architecture — both were found by trying to project it.

**That is the real argument for the discipline: the projection is a test of the source, and it is the cheapest test available.**

---

## Checklist — any downstream artefact

- [ ] Every element cites the architecture element it serves
- [ ] Anything uncitable is deleted, or recorded upstream first and then built
- [ ] Surfaces map to active routine steps; no surface built for a passive step
- [ ] Architectural absences are built as absence, not as permission
- [ ] Operating rules that bind at runtime exist as interlocks that can refuse
- [ ] Anything that could not be derived is logged as an architecture gap, not worked around
