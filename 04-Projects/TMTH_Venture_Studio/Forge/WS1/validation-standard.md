# Validation Standard — how a run decides what it does not know, and who settles it

**Owner:** Head of Product · **Part of:** Forge WS1 (CF development) · **Created:** 16 September 2026, on Tom's instruction ("write to Forge CF a process for thinking about validation, because that's what you keep trying to do")
**Pairs with:** `tpm-measurement-standard.md` (the record a figure carries) · `criteria-registry.md` (the gates) · `architecture-process-flow.html` (where in the flow this runs) · `va-design-discipline.md`
**Grounded in:** INCOSE SE Handbook — verification versus validation, and the V-model (validation is planned at design time and executed at the operational readiness review, never demanded of the customer before the system exists) · Simanis et al. (2023) — the method is theory-first; the design is reasoned to failure on paper and validated in operation · Pawson and Tilley (1997) — a theory of change names its own test

**Review date:** 15 December 2026.

---

## The defect this standard removes

A run reaches something it does not know and reaches for a person to settle it: "three client conversations", "the insider confirms", "ask the consultant", "a live launch will show". On 16 September 2026 one run did this four times in a day, and each time the thing handed over was either (a) a fact a public source held, or (b) the designed output of a challenge the run had already solved. The habit has three sources inside the method:

1. R2's fieldwork clusters, read as a licence to outsource research rather than as a coverage device.
2. The tool's proposition that "the insider carries the fieldwork", read as "the insider does the work".
3. VA-82's carried-item class "unmeasured input — owner: [a person]", which names a person where it should name a source.

The cost: effort shifts to the customer of a tool whose promise is that it does the work; a solved challenge reads as an open gate; and the design's own claims are presented as questions.

---

## The process — five questions, in order, for every unknown

Run this the moment a run writes any of: *unmeasured*, *unvalidated*, *needs confirming*, *the insider will*, *a conversation with*, *only a launch will show*.

**Q1 · Is it a designed output?** Does a challenge in this run *produce* this as its outcome — a customer behaviour that R4's mechanism causes, an acceptance that R5's format causes, a partner's adoption that R7's business case causes?
→ **Yes:** it is a **claim**, not an input. It carries the challenge's theory, the mechanism, and the falsification test already written. Its evidence event is **validation at launch** (demonstration/test in the operational environment), scheduled as a TPM convergence event. It is never a gate that blocks design, never a question for the customer, and never disposed as "unmeasured input". *(16 Sep instance: "will an allocator accept a tournament record" — the output of C3, R4, R5 and R7.)*
→ **No:** go to Q2.

**Q2 · Is it a fact about the world that exists somewhere?** A price, a fee, a headcount, a filing, a regulation, a published finding, a revealed behaviour of a named actor.
→ **Yes:** it is a **desk input**. The desk route runs before anything else, in this order, and the answer is recorded with its tier: company filings and regulator registers (T2) · revealed prices and revealed behaviour of named actors (T2/T3) · the literature (T2) · the web, including the actor's own published material (T2/T3) · email to a named party who would answer a factual question (T3). *(16 Sep instances: the incumbent's AUM — Companies House; the premia-fund reference — AQR's fee schedule; consultant attribution practice — their own publications.)*
→ **No:** go to Q3.

**Q3 · Is it a fact about *this* incumbent that only the incumbent holds?** Its own cost lines, its own client count, its own fee schedule where unpublished.
→ **Yes:** it is a **correction input**. The run states its best desk estimate with the band and the tier, designs on it, and presents it to the person as *"here is what we found — correct it"*. The design does not wait; the person's correction re-runs the frame. Never *"validate this for us"*, never *"we need X from you before we can proceed"*.
→ **No:** go to Q4.

**Q4 · Is it a decision?** A fee, a threshold, a commitment, a choice between materially different designs.
→ **Yes:** it is an **approve-before item** for the principal (or the insider, where it is their business). The run states the options with the checker's numbers at each and a recommendation. It is the only class where a person is genuinely required, and the ask is a decision, not a validation.
→ **No:** go to Q5.

**Q5 · Is it a limit of the world no design in the class removes?** *(VA-101's test: could any competitor, with any budget, remove it?)*
→ **Yes:** it is a **structural limit**: named, bounded, paired with the validation event that addresses it, and its share of the venture's value stated.
→ **No:** the run has not understood the unknown. Return to the challenge that produced it; it is a design defect (VA-89).

**The rule in one line:** *a person is asked to decide, or to correct — never to validate, and never to research.*

---

## What each class carries in the record

| Class | Where it lives | Evidence method | Event | Owner named as |
|---|---|---|---|---|
| Claim (designed output) | the challenge's ToC and falsification test; a TPM record tagged **Val** | demonstration / test | launch, first cohort, first allocations — the ORR | the venture's role that runs the activity (a role, never a person) |
| Desk input | the frame or the challenge that consumes it; TPM tagged **V** | examination (filings, prices, literature) | now — closed in the run | a source, with tier |
| Correction input | the frame, flagged ⚠ | examination now; the insider's correction later | the frame re-run on correction | the insider, for correction only |
| Decision | the close of the challenge that needs it | — | the principal's ruling | the principal / insider |
| Structural limit | the challenge's dispositions (VA-101) | the paired validation | as paired | the role that runs the validation |

**Carried items (VA-82) are reclassified accordingly.** "Unmeasured input — owner: the insider" is admissible only for a Q3 correction input. A Q1 claim carried as "unmeasured" is a defect; a Q2 fact carried as "unmeasured" is a desk route not run.

---

## What this changes in the flow

- **Phase 0 (Frame):** the frame states, for every ⚠ figure, which class it is (desk / correction) and, for desk inputs, that the desk route ran. A frame that hands a Q2 fact to the insider has not run.
- **Phase 2 (per requirement):** every challenge's close lists its Q1 claims with their validation events, separately from its Q2/Q3 inputs. The binding gate (VA-84) may name a Q1 claim only as *"the design's claim, validated at [event]"* — never as "unmeasured".
- **Phase 4 (Verify):** the critic checks the classification: a claim scored as an open gate, or a desk fact handed to a person, is a discipline defect.
- **Phase 5 (Sign-off):** the human confirms the PCO, rules decisions, and corrects Q3 inputs. Nothing else is put to a human.

---

## Validation by launch — the sales front is the instrument (Tom, 16 September 2026)

When launch is cheap — and with agents it is days and no spend — a Q1 claim's validation event is not a study, a survey or a conversation. It is **the F2 architecture as designed, stood up and put in front of the customer it was designed for.** The conviction mechanism (R4), the adoption format (R5), the payment form (R6) and the gateway product (R7) are built as the minimum sellable front, and the claims are read from what happens: who signs up, who adopts, who pays. This is the operational readiness review at near-zero cost, not a new step.

**Why the weight of validation is a function of the cost of being wrong.** Heavy pre-launch validation exists where producing or fixing the thing is expensive — a factory, a drug, a network of branches — so an error found after launch costs more than the study that would have found it before. Where producing and fixing is cheap, the same study costs more than the error it prevents: the fastest and cheapest test of the claim is the claim in operation, corrected on what it shows. The method's own economics (Simanis: reason to failure on paper, *then* validate in operation) assumed the second half was expensive. With agents it is not. So the standard's default is: reason on paper to the point the design is coherent and its claims are named, then launch the minimum front and let the world correct it — and reserve pre-launch validation for the components whose failure would be expensive or irreversible (regulatory exposure, a commitment of capital, a promise to a named counterparty).

**What the run produces for it:** a "minimum front" section at the F2 close — the smallest set of built products that lets every Q1 claim be observed, with the observation each yields and the cost to stand it up. Products designed at C3 so that nothing needs the fund, the factory or the capital to exist first (the pre-capital record) are what make the front cheap; where the design does not have that property, the front's cost is a finding against R3.

**Two gates before any front goes live, both Q4 decisions:** whose venture it is (the principal's ruling — a demo run on an incumbent's line is not a venture until someone owns it), and the regulatory position for the communication and the product (a desk question answered from statute — for an investment front in the UK, s21 FSMA and the FPO exemptions — never left to a solicitor). Every external send under the principal's name stays approve-before.

*(16 Sep instance: the benchmark page (R7), the shadow-statement sign-up (R4) and the tournament in paper mode (C3/R9) observe every Q1 claim of the algotrading design at near-zero cost; both gates open.)*

---

## Registry rows proposed (Tom approves as grader rules)

| Mini-output | Check type | Objective test | Bar |
|---|---|---|---|
| **Unknowns classified** | Presence + Format | every item a run marks unmeasured, unvalidated or needing confirmation carries one of the five classes; a Q1 claim carries its theory, falsification test and validation event; a Q2 fact carries the desk route run and its tier; a Q3 input is phrased as a correction; no item asks a person to validate or to research | pass/fail · **HARD** |
| **Desk route before ask** | Traceability | for every input handed to a person, the record shows the desk route was run first and what it returned | pass/fail · **HARD** |

Both pass the writing test (they name what the run must state) and the generality test (they bind any venture on any path).

---

## Worked instance — 16 September 2026, algotrading

| The run wrote | Class on this standard | What should have happened |
|---|---|---|
| "C2 needs three client conversations to map the routines" | Q1 for the KMC's magnitude (the literature measures it) · Q2 for revealed prices · Q3 for this firm's clients | Literature and HFR close the KMC; the insider corrects the firm's own figures |
| "Binding gate: allocator acceptance of the tournament record — unmeasured" | **Q1 claim** — the output of C3, R4, R5, R7 | Stated as the design's claim with its validation at launch; public revealed behaviour (Numerai, JPMorgan) cited as evidence |
| "R7 hypothesis: two consultants adopt within 18 months — one consultant conversation" | Q1 claim (R7's business case) · Q2 for their current practice | Their published attribution methods desk-checked; adoption validated at launch |
| "Your AUM — the one figure that decides the verdict" | **Q2** — Companies House, FCA register, fee-revenue arithmetic | Desk route; then "correct it" |
| "The fee schedule — approve-before" | **Q4** — correct | Unchanged |

---

## Notes

- This standard does not lower the bar. Every claim keeps its falsification test and its validation event. It moves *who does what*: the run researches and designs; the person decides and corrects; the world validates, at launch.
- Where a desk route genuinely returns nothing — no filing, no price, no behaviour — the run says so, states the assumption with its tier, and proceeds. Absence of a source is a Q3 or a Q5 finding, not a reason to ask.
