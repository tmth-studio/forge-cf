# Forge CF Glossary — Controlled Vocabulary

**Status:** **v0.4 — RATIFIED 28 Aug 2026 as a REFERENCED CONTROLLED DOCUMENT of the TMTH Manual (v0.5, §2.5 / VA-65).** Not merged into the manual as content: this file holds terms from three provenance classes — IVE canon, systems-engineering practice, and dated principal rulings — and each entry carries its own source line, which a merge would flatten. The manual's front-matter now names this file; role skills and VDRs reference it and never redefine.

> **⚠ ONE OPEN FLAG from the 28 Aug fidelity confirmation (flags 1, 2 and 3 closed 1 Sep 2026) — the seeded definitions were checked against the `simanis-*.html` sources, not blanket-blessed. Do not treat a flagged entry below as settled.**
>
> **1. ✅ CLOSED 1 Sep 2026 — KMC stays "Key Monetizable Cost" (Tom's ruling).** The canon's named Key Construct is the Key Monetizable **Loss**: "the money **expended, foregone, feared, or stress** from managing a poor status quo," with the canonical microfinance example targeting *foregone* income. The CF carries **Cost** throughout. Not cosmetic — "cost" invites the reading *money paid out*, which is the expended class only, and that is almost certainly the root cause of the 27 Aug misclassification ratified as VA-63. Ruled by Tom, 1 Sep 2026: **keep Cost.** A deliberate WS1 divergence from the canon's "Loss", carried openly: the definition below still holds all four canon loss classes (expended · foregone · feared/risk-borne · friction/stress), and the expended-only misreading the flag warned about is guarded mechanically by the VA-63 regression checks (R-R2a–R-R2d), not by the word. No skill or record changes follow.
>
> **2. ✅ CLOSED 1 Sep 2026 — BFF definition drift corrected.** This file defines BFF by the *process* that produces it ("evolved structural design; each challenge mutates it"). Canon defines it by *content*: "the essential shape the product and operations take — shared by all competitors and visible to the customer." The manual's §1.1 table carries the canon form. Corrected on Tom's ruling of 1 Sep 2026: the entry now carries the canon content definition, with the mutation process as a note beneath it. No longer open.
>
> **3. ✅ CLOSED 1 Sep 2026 — BALM ten vs canon thirteen: the thirteen is the SUPERSEDED version.** This file defines BALM as ten requirements (R1–R10) in three functions. The canon's Business Architecture Plan is "six core business functions and their thirteen essential requirements" (R1–R13), clustered R1–R6 viability / R7–R10 diffusability / R11–R13 scalability. Predates this glossary (the manual has carried the ten-challenge framing since v0.1), but ratifying a glossary is what *locks a definition down*. Ruled by Tom, 1 Sep 2026: **the thirteen-requirement BAP is an older version of IVE, superseded; the current canon is the ten requirements (R1–R10).** BALM-10 is not a subset and needs no subset label. Wiki pages that carry the thirteen (the JVI entry, the BAP-as-logic-model entry, `baf-requirements-full.html` and its R11–R13 Phase-II note) are records of the older canon — read them under temporal quarantine, and do not re-open this flag from them.
>
> **4. Unverified against the available canon (recorded as neither confirmed nor contradicted).** **CTM** and **ARM** are sourced to "Simanis, IVE models slides," which is not in the `simanis-*.html` corpus. **FMOS thresholds** (≥25% per requirement, 60% Phase II) are honestly sourced to "IVE gates; venture fin-sims" and are not canon numbers — canon gives 30% for MCM and 50% illustratively for FMOS. Keep them labelled as gate settings, especially as they sit one line from the canon MCM ≥30%.
>
> **Confirmed canon, no change needed:** MCM (formula and the ≥30% rule of thumb), HIO, MRBU, at-scale operational model, the FMOS formula, and the corrected 4-D Product reading (the "form, function, fit, feel" version is fabricated and rightly removed).
>
> **✅ HELD BATCH CLEARED 1 Sep 2026 (Tom's instruction).** The batch was five terms, not seven: `value proposition` and `Communications Product` were listed as held while already present in the Product section below — a stale list, the same defect class as the version stamp maintained in two places and updated in one. All five now enter: **operating unit · MRBU · launch operating unit · launch strategy · sales pilot**.
>
> **The blocking naming decision is made.** The Head of Product recommendation stands: **keep MRBU**, the canon's Minimum Representative Business Unit, and let the two species be MRBU (function: test) and launch operating unit (function: grow). The proposed rename to "MRP (Minimum Representative Pilot)" is **rejected** — it fails two of the three naming tests (not the source discipline's term; collides with Material Requirements Planning). The genus/species distinction it carried is preserved in full; only the label changed.
>
> **⚠ Consequent record sweep NOT done, and must not be bulk-replaced.** "MRP" appears about 190 times across the venture records and skills. Each occurrence needs reading to decide which axis it meant — MRBU (venture configuration) or sales pilot (customer commitment). Tracked as follow-on work, per the 27 Aug instruction.

*Created on Tom's instruction after the 27 Aug terminology rulings.*

**Rules of the glossary:**
1. Every term traces to a source — the source discipline's own materials (Simanis/IVE, SE/INCOSE) or a dated principal ruling. A term with no source does not enter.
2. Every term passes the three-way naming test (WS1 feedback log, 27 Aug 2026): correct in the source discipline · parseable by a commercial reader with no glossary · no collision with a meaning already live in the records.
3. One definition per term. If a record needs a different meaning, it needs a different term.
4. Changes enter by the same route as manual changes — feedback log → Head of Product ratification. This file is the controlled copy; role skills and VDRs reference it, never redefine.

---

## Product and instance terms

**4-D Product** — the venture's four product types, each eliminating a named gap for a named actor: Working, Communications, Payment and Partner Products. The "D" is the four types, NOT "form, function, fit, feel" (a fabricated definition corrected 27 Aug 2026). *Source: Simanis, AOM process slides; Product_Architecture_Definitions.md (11 Aug 2026).*

**Working Product** — eliminates a named loss (the Key Monetizable Cost) in the customer's current routine for an outcome they already pursue. *Source: Product_Architecture_Definitions.md.*

**Communications Product** — makes the actor **aware of** the value proposition, and **able to act on it**. The two verbs are the two sub-types: *aware of* is the retrieval gap (the venture does not come to mind at the moment the need fires — advertising, Ehrenberg-Bass memory structures, measured on mental availability rather than conversion); *able to act on it* is the conviction gap plus the practical route (the actor can check the claim against their own numbers, and a way to transact exists — sales and the purchase or acceptance path). Note "act on", not "buy": at Calmly the claimant pays nothing, so their act is acceptance, not purchase. A definition written around buying mis-handles the actor who pays nothing. *Source: Product_Architecture_Definitions.md; sharpened by principal ruling 27 Aug 2026.*

**Payment Product** — converts a completed, evidenced value event into venture revenue without creating a new loss on either side: no working-capital gap for the venture, no payment friction for the customer. *Source: Product_Architecture_Definitions.md.*

**Partner Product** — eliminates a named loss in a partner's routine such that supplying what the venture needs (but cannot buy at standard market terms) becomes the partner's best way to achieve their own outcome. *Source: Product_Architecture_Definitions.md (v2, vendor boundary test).*

**Value proposition** — a statement with exactly three fields: (1) **the outcome** the actor already pursues, stated first person and clinical; (2) **the key monetizable cost eliminated**; (3) **the journey** by which the actor gets from where they are to that outcome. All three are required. A statement missing any one of them is a slogan, not a value proposition.

Three consequences the definition is worth having for:
- **The value proposition is the Working Product journey, described.** The three fields are its endpoint, the loss it removes, and its path. It is therefore *derived*, never written fresh.
- **It gives a mechanical check.** Compare the value proposition as published against the Working Product journey as built, field by field. A claimed outcome the journey does not reach, a cost the journey does not eliminate, or a path the journey does not have, each means the Communications Product is promising something the architecture does not build. This is the testable form of the rule that an over-promising Comms journey manufactures Working Product failure.
- **One per actor, not one per venture.** Every actor carrying an outcome and a key monetizable cost in the operating model has a value proposition. The Communications Product makes *that* actor aware of *that* proposition.

*Source: principal ruling 27 Aug 2026.*

**Realised Product** — an instance of a 4-D Product built for real use (live claim documents, live integrations). "Realisation" per ISO/INCOSE product-realisation usage. *Source: principal ruling 27 Aug 2026.*

**Test Product** — an instance produced solely to verify or demonstrate the design, never for live use: worked examples, reference claim files, dry-run packs. Id convention TP-NNN (historic SP ids retained, e.g. Calmly SP-007). *Source: principal ruling 27 Aug 2026; supersedes "specimen" and rejects "fabricated product" (collision with fabricated-content vocabulary).*

**First-article inspection** — exhaustive verification of the FIRST Realised Product of each type against its requirements and its Test Product reference; a named verification event at first live operation (Calmly: tranche 1). *Source: SE/manufacturing practice (FAI); adopted 27 Aug 2026.*

## Verification terms

**Verification ladder** — inspection → analysis → demonstration → test; each contact event or design claim is verified at the highest rung available on the ground before any live exposure. Principal inspection is a formal rung. *Source: SE verification methods; verification-first doctrine (26 Aug 2026).*

**Verification vs validation** — verification: does the built thing meet its spec (component test, pre-field)? Validation: does it produce the real-world effect the architecture claims (field)? Verification predicts validation only if every requirement traces up to an architectural causal claim. *Source: Product_Architecture_Definitions.md (three-level requirements structure).*

**NCR (non-conformance report)** — the formal record that a design element does not conform to its requirement or intent, with evidence, disposition (rework/use-as-is/scrap), containment and closure criteria. The ONLY re-entry route into ratified architecture. *Source: SE quality practice; gated-architecture rule (26 Aug 2026).*

**Test Product / Realised Product boundary in verification** — a Test Product proves the design on paper (demonstration-grade); a Realised Product's first article proves the build (test-grade). The two are different verification events and are never conflated. *Source: 27 Aug 2026 ruling.*

**Band-never-bare** — no external document quotes a central estimate without its band and confidence grade. *Source: Calmly operating rule; applies CF-wide.*

## Operating unit and launch terms

*Entered as a batch 1 Sep 2026 on Tom's instruction, with the MRBU naming decision made. One genus (operating unit), two species split by **function** — and representativeness follows the function, never the reverse.*

**Operating unit** — the smallest complete configuration that delivers the value proposition to a real customer and can be repeated. It includes every process, actor, agreement and capital input that must be live at the same time for value to flow. A signed customer is one input to the unit, not the unit. Always say which species is meant. *Source: Simanis/IVE C3 inputs ("launch and grow the first operating unit"); principal ruling 27 Aug 2026.*

**MRBU (Minimum Representative Business Unit)** — an operating unit that is representative of the at-scale configuration. Its **function is to TEST** the venture, and representativeness follows from that function. Canon: "the smallest scale of the business model that allows all the activities most critical to at-scale profitability to be tested in high fidelity, under conditions that capture the market's real variability." Calmly's MRBU is one dispute-cover cell; representative of at-scale means per-unit economics, not volume.

- **Do not call it "the pilot"** in any new document — see *sales pilot*, which sits on a different axis.
- **Do not call it "MRP"**. The proposed rename to Minimum Representative Pilot was **rejected 1 Sep 2026**. It failed two of the three naming tests: it is not the source discipline's own term, and it collides with Material Requirements Planning. That is live vocabulary in the same operations register this method borrows from. The genus and species distinction the proposal carried is preserved in full; only the label was refused.

*Source: Simanis/IVE canon (anchored at VA-58, 26 Aug 2026); principal rulings 27 Aug and 1 Sep 2026.*

**Launch operating unit** — an operating unit that does **not** have to be representative. Its **function is to GROW** the venture, so the representativeness constraints that bind an MRBU do not bind it. Calling both "the first unit" imports the test constraint into the growth job as a silent tax on speed. Owned by the Head of Launch. *Source: principal ruling 27 Aug 2026.*

**Launch strategy** — the staging and timing of the key activities that bring the first launch operating unit into operation. Scope is the whole unit, not the first sale. Equivalent to IVE's Interim Scaling Model (C3, Input 1). *Source: Simanis/IVE C3 inputs; principal ruling 27 Aug 2026.*

**Sales pilot** — a bounded, reversible trial agreed with a customer as part of the sales motion. It describes the **customer's level of commitment**, never the venture's configuration. A sales pilot is served by whichever operating unit the venture is running at the time; during launch that is the launch operating unit, not the MRBU. Preferred over "client pilot", which said only whose side the pilot was on rather than what it was. *Source: principal ruling 27 Aug 2026.*

**Open, not resolved here:** whether Calmly's "tranche 1" and its MRBU are the same object under two names. A venture-record question, not a method one. *Raised 27 Aug 2026.*

## Method and model terms

**BALM** — Business Architecture Logic Model: the ten universal functional requirements (R1–R10) in three functions that dictate a market-creating venture's commercial viability. (Ten is the current canon. The thirteen-requirement BAP is a superseded IVE version — ruled by Tom, 1 Sep 2026, closing flag 3; older wiki pages that carry thirteen are records of that prior version.)

**The term is used two ways, and a record must make clear which:**
- **the BALM structure** — the requirements and sub-requirements themselves, with no venture's answers in them;
- **the answered BALM** — the same structure carrying one venture's written answers, its per-requirement FIT verdicts, its per-requirement synthesis checks, and **the BFF evolution those answers produce**.

**The BFF evolution sits inside the answered BALM, not beside it** (principal ruling, 1 Sep 2026). Each challenge answer is a strategy productized into the business form factor. Canon: "bake the strategies into the product idea itself… like a marble statue being carved." Ten strategies recorded without the shape they produced is a parts-bin, and that is a named failure mode of this method. The cumulative BFF therefore belongs to the answer set by construction, not by preference.

**The answered BALM is not the VDR.** The VDR is the rendered record. It carries the answered BALM, plus the PCO context line (upstream of BALM, and therefore not part of it), plus the rendering conventions of the VDR scope standard — each requirement's canonical definition alongside its answer, the design-working blocks shown closed by default, the related-artefacts footer. The relation is model to view, as already ratified for the CTM and AOM under VA-60: the answered BALM is the content, the VDR is a controlled document that presents it.

**"Logic model" is not a name for any of this.** Canon calls a structure of this kind *a logic model* — "a description of the key chain of causes and effects that explain how a complex system works" — and states explicitly that it is not the programme-evaluation sense (inputs → activities → outputs → outcomes → impact). That is the category BALM belongs to. It is never a name for the answered instance, for one part of the record, or for the VDR.

*Source: Simanis, IVE models slides; `ive-bap-logic-model.html` (IVE Systems / Half-Solved, Apr 2026); principal ruling 1 Sep 2026.*

**BFF (Business Form Factor)** — the essential shape the product and operations take: shared by all competitors in a category, and visible to the customer. Defined by **content**, per canon. *(The previous WS1 wording defined it by the process that produces it — corrected 1 Sep 2026, closing glossary flag 2.)*

*Process note:* each challenge R1–R10 mutates the BFF, with mutations considered and adopted or held with reason. The cumulative record of those mutations is the **BFF evolution**, which sits inside the answered BALM — see BALM.

*Source: Simanis/IVE canon (manual §1.1 table); VDR scope standard (8 Jun 2026); principal ruling 1 Sep 2026.*

**CTM / AOM / ARM** — the three visual models: Customer Transformation Model (mental, emotional and behavioural state changes the 4-D Product must cause), At-scale Operational Model (flow of 4-D Products from head office to customer and back, unitised), At-scale Resourcing Model (direct activities, responsible personnel, assets and resources). *Source: Simanis, IVE models slides.*

**MCM (Market Creation Margin)** — venture robustness measure: (WTP low − unit cost high) ÷ unit cost high (conservative form; best-case uses the opposite ends). Target ≥30% conservative. *Source: Simanis, IVE models slides.*

**HIO (High-Import Outcome)** — the outcome of greatest importance to the target actor, set at a level the venture can meaningfully impact (the level-finding drill: usually one step lower than first instinct). *Source: BALM R2.*

**KMC (Key Monetizable Cost)** — the single biggest monetizable cost in the target actor's current routines for the HIO; P&L line items they no longer pay, cross-department, PLUS the dominant opportunity-cost component where present. Spans all four canon loss classes — expended · foregone · feared/risk-borne · friction/stress — never the expended class alone (VA-63). *Term note: the canon writes "Key Monetizable Loss"; WS1 keeps **Cost** by principal ruling, 1 Sep 2026 — a deliberate, recorded divergence. Source: BALM R2; Calmly two-component extension (VDR Appendix B).*

**OCV (Objective Customer Value)** — the DO / USE-BUY / THINK / FEEL routine map evidencing what the actor does today to achieve the HIO. *Source: BALM R2 / OCV standard (tmth-studio/methods).*

**FIT / FMOS** — FIT: the per-requirement financial integrity test (floor/ceiling closure); FMOS: the margin-of-safety measure gated at ≥25% per requirement (pass), 60% whole-architecture Phase-II. *Source: IVE gates; venture fin-sims.*

**VDR (Venture Design Record)** — the design record and only the design: PCO line, R1–R10 answers with canonical definitions rendered alongside, BFF evolution. Economics, verification status and investment cases live in separate artefacts. The design authority for its venture (VDR-first protocol). *Source: HoP scope standard (8 Jun 2026); VDR-first ruling (27 Aug 2026).*

**EV anchor / ⬇EV tag** — one anchor (segment expected net recovery) governs claimant price, funder price and site-fee justification; any component or asset derived downstream of it carries the ⬇EV tag and re-derives on any EV change. *Source: Calmly VDR Appendix C (proposal, 27 Aug 2026); generalises as single-anchor pricing coupling.*

---

*Maintenance: propose additions via the WS1 feedback log with source attribution. Head of Product ratifies into the manual on the weekly pass.*
