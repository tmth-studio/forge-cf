# Sales and Marketing Asset Standard — deriving assets from the architecture

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.2 (scope fields, 21 September 2026). The file carried no version line before today; the 27 August text with the 7 September amendment is v0.1.
**Added:** 27 August 2026, on Tom's instruction.
**Amended:** 7 September 2026 — *the state rule* (Tom: *"architect this document as the at-scale value proposition. Launch phase then decides what of it to use."*). Stated in the parent, repeated here because this is the projection that reaches the market.
**Parent:** `derivation-standard.md` — one architecture, three projections; this file is the *assets* projection.
**Companion to:** `landing-page-standard.md` (that one is the craft — structure, headers, proof. This one is the *content*, and where it comes from.)

**Review date:** 15 December 2026 (90-day cycle; owner re-reads against the regression set and the canon mapping, bumps the date)

**Scope field (MI-072, under VA-23) — added 21 September 2026.** Every check in this standard carries one value: `scope: craft` or `scope: launch`. **Craft** means the check reads the at-scale projection of the architecture (C10) and applies at step 6b of a challenge, at Converge and at first article. **Launch** means the check reads a launch form only. A launch form is the downstream derivation that selects from the at-scale projection what is true on day one. A launch check applies to the pilot-instance record that follows R10, never at a challenge. A role review at the architecture reads the craft rows and skips the launch rows. Launch constraints (no cash, the founder's hours, no cold outreach) never enter a craft row.

---

## The claim

**A sales or marketing asset is a projection of the venture architecture, not a creative act.** Every asset answers the same three questions, and all three are already answered in the venture design record:

1. **What outcome does the customer get?** → the **High-Import Outcome** (C2/R2 SR1)
2. **What loss does it eliminate?** → the **Key Monetizable Cost**, and specifically the component the architecture makes *exclusive* (C2/R2 SR3)
3. **How does it work for them?** → the **product use routine** (C5 SR1)

If the architecture is complete, the asset is a derivation. If writing the asset requires inventing an answer, that is not a copywriting problem — it is a gap in the architecture, and it should be recorded as one.

### Which state you are writing about — added 7 September 2026

This standard gets the *what* right — hero claim from the HIO, features from the cost-carrying steps — and was silent on the **state**. That silence is a defect, and this is the projection where it costs most.

> **Every projection is taken at the at-scale state of the architecture — C10, not the launch cohort.** The launch form is a separate, downstream derivation: it selects from the at-scale projection what is true on day one, and says what is not yet available. **A projection that mixes the two states is a defect, and the tell is a sentence that could only be written about launch sitting beside a figure that could only be true at scale.**

**Why it ranks highest here.** A *product* projection built at the wrong state gets caught by a build. **An asset projection built at the wrong state gets sent to a customer.** On the venture that surfaced this, nine outreach sequences had already shipped on a superseded model before anyone looked.

**The specific trap, because it does not feel like an error at the time.** An at-scale truth will present itself as something you must *refuse* — "that isn't true yet under bootstrap" — and refusing it is correct reasoning for a launch document and wrong for the object you were asked to build. The mechanism that makes the product work is exactly what gets dropped this way. Write the at-scale asset; let the launch derivation decide what to hold back, and let it say so explicitly.

**This is the go-to-market payoff of doing IVE properly.** The work of finding the outcome, isolating the monetizable cost and specifying the routine has already been done, under verification, with evidence grades attached. Marketing that starts from a blank page is re-deriving all of it, badly, without the evidence.

---

## The derivation table

| Asset element | Derives from | Rule | Scope |
|---|---|---|---|
| **Hero claim** | HIO (C2 SR1) + the exclusive KMC component (C2 SR3 / R2) | Lead with the outcome, framed by the loss **only the architecture can remove**. See `landing-page-standard.md` §7.2 — the exclusive component, not the computable one. | craft |
| **Subheader / mechanism** | Product use routine — the **active** steps | How it works, in the customer's actions, in order. Two sentences. | craft |
| **Features** (3–6) | Product use routine — the steps that **carry Key Cost** | One feature per cost-carrying step. Not per product capability. | craft |
| **Objections** | C4 want block · C5 use block · C6 buy block | **F2 is the objection architecture.** The blocks were identified as the reasons a customer does not adopt — that is the objection list, already researched. | craft |
| **Proof** | The evidence register, with grades | Cite the source and the grade. Never quote a central estimate bare. | craft |
| **The ask / CTA** | The **first active step** of the routine | The CTA is not "book a demo". It is the first thing the routine actually asks them to do. | craft |
| **Channel and framing** | C7 gateway partner | Where the asset meets them, and whose voice it arrives in. | craft |
| **Words you may not use** | The operating register | The vocabulary constraints are a lint, applied before the asset ships. | craft |
| **Segment variants** | The segment split (PCO / TAM definition) | One asset per segment where the HIO or the routine differs. Not per persona. | craft |

---

## Three rules that fall out of the routine's own annotations

The product use routine marks every step **active or passive**, and marks some as **precondition** (a step the venture imposes that delivers no Key Cost reduction) or **not in record**. Those annotations are not bookkeeping — they tell you what to write.

### Rule 1 — Sell the passive steps. They are the value. · scope: craft

A step the customer performs *passively* is one where they get the outcome without doing anything. That is the product working. Calmly's routine step 6 reads: *"Disputes arise and resolve entirely outside the site — intake, gate, valuation, resolution, payout — entirely passive for site. Carries Component 1."* That sentence is the feature. It needs almost no rewriting.

**Features should dramatise passive, cost-carrying steps.**

### Rule 2 — Active steps are the price of adoption. Answer them, do not hide them. · scope: craft

Every active step is effort you are asking for, and each is a place the sale dies. Calmly's routine has four: build the business case, supply 12 months of dispute history, embed cover at formation, decommission the in-house function. Each needs an answer in the asset — how long, who does it, what it costs.

**Every active step in the routine gets an objection answered in the asset.** If it is not answered, you have found the hole in your funnel before the customer does.

### Rule 3 — Preconditions are pure ask with no give. Name them or they ambush you. · scope: craft

A step marked **precondition** delivers no cost reduction to the customer at all. Calmly has two: supplying historical dispute outcomes, and a shadow-mode scoring period with no cover in force. The customer does work and waits, and receives nothing yet.

**Preconditions must be visible in the asset, with what they buy.** Concealing them converts a known cost into a surprise, which is where deals die late — the most expensive place. And a venture with many preconditions has an adoption problem the marketing cannot fix; that finding belongs back in C5, not in a brochure.

---

## Worked example — Calmly Resolve, site-side

| Asset element | Derived value | VDR source |
|---|---|---|
| Hero claim | Participants transact more, and at higher values, when a guaranteed exit is visible at commitment | C2 Appendix B, Component 2 — "requires a credible guarantee… exclusive to Calmly's architecture" |
| Mechanism | One snippet embeds cover at contract formation; the fee nets at source; disputes run entirely outside the platform | Routine steps 4, 5, 6 |
| Feature 1 | Cover appears where the deal is made | Step 4 (active, C7) |
| Feature 2 | Disputes resolve without you | Step 6 (passive, carries Component 1) |
| Feature 3 | The dispute cost you carry today comes off | Step 8 (active, one-off) |
| Objection: "is this insurance?" | Answered — nothing indemnifies you; your customer sells a claim they own | Operating register + C4 |
| Preconditions: 12 months of history · scoring with nothing at stake | **Fixed 27 Aug** — own section, "Before you go live", stating what each costs and what each buys. Shadow-mode duration deliberately left unstated because the record has it unset. | Routine steps 2 and 3, both preconditions |
| CTA | "Work out your number" | Step 1, the first active step: build and internally approve the business case |
| Proof | Hui, Saeedi, Shen & Sundaresan (2016), attributed as eBay's result | Appendix B evidence register |

**That table found a defect, and fixing it produced the pattern worth keeping.** The routine's two preconditions — twelve months of dispute outcomes including abandoned, ex-gratia and charged-back disputes, and a period of scoring with no cover in force — appeared nowhere in the marketing. Both are real asks the first site would have met *after* becoming interested.

The fix was not to bury them politely. It was a section titled *Before you go live*, each precondition stating **what it costs you** and **what it buys you** — the history buys your numbers instead of our assumptions; the scoring period buys the answer to the question you should be asking, which is whether the method prices *your* disputes sensibly.

**The general finding: a precondition surfaced honestly often converts into a selling point, because the reason it exists is usually a reason to trust the venture.** We ask for the awkward data because pricing on assumptions would be worse for the customer. Hidden, that reads as friction. Stated, it reads as rigour. The asset gets stronger by including the thing the drafter wanted to leave out.

One discipline held while writing it: the record marks the shadow-mode duration *unset*, so the page says the length is agreed with the customer rather than inventing a number to make the section feel finished.

---

## The traceability test

**Every substantive claim in an asset cites the VDR element it derives from.** Then:

- **Cites cleanly** → it is architecture, and it is defensible in the room.
- **Cannot cite, but is true** → an undocumented architecture element. Record it in the VDR, then use it.
- **Cannot cite, and is not in the architecture** → invention. Delete it.

This makes asset production a **verification instrument for the architecture**. Writing the Calmly page surfaced two architecture-level findings before it surfaced a copy problem: the value case was being led from the non-exclusive component, and a precondition had no customer-facing answer. Both were cheaper to find in a draft than in a meeting.

---

## Checklist before any sales or marketing asset ships

Each line carries its scope. A review at the architecture runs the craft lines; the launch line is run only on a launch form, against the pilot-instance record.

- [ ] `scope: craft` · **State declared: this asset is the at-scale (C10) projection** — the state is written on the asset, never left for the reader to infer
- [ ] `scope: launch` · **A launch form names its at-scale parent and says what it holds back.** It is derived from the at-scale asset, never from the architecture directly. A launch form with no parent is the derivation defect one step earlier
- [ ] `scope: craft` · **No launch-only sentence sits beside an at-scale figure** — the tell for a mixed-state asset
- [ ] `scope: craft` · **The mechanism that makes the product work is present**, even where it is not yet live at launch
- [ ] `scope: craft` · Hero claim traces to the HIO plus the **exclusive** KMC component
- [ ] `scope: craft` · Mechanism is the routine's active steps, in order, in two sentences
- [ ] `scope: craft` · Each feature maps to a cost-carrying routine step — not to a product capability
- [ ] `scope: craft` · Every **passive** cost-carrying step appears as value (rule 1)
- [ ] `scope: craft` · Every **active** step has its objection answered (rule 2)
- [ ] `scope: craft` · Every **precondition** is visible, with what it buys (rule 3)
- [ ] `scope: craft` · Objections drawn from the C4/C5/C6 blocks, not invented
- [ ] `scope: craft` · CTA is the first active step of the routine
- [ ] `scope: craft` · Every claim carries its VDR citation; anything uncitable is deleted or recorded
- [ ] `scope: craft` · Vocabulary lint run against the operating register
- [ ] `scope: craft` · Numbers carry band, source and grade

---

**Version line.** v0.2, 21 September 2026, Head of Product, under Tom's `/autonomous` instruction of the same day. VA-23 rescoping, 21 Sep 2026: a scope field on every check (MI-072) — nine derivation-table rows, three rules and 15 checklist lines, 27 checks in all: 26 `craft`, one `launch`. The one launch check is the former second half of the first checklist line: a launch form naming its at-scale parent. It is split out so a review at the architecture can skip it. No rule changed. Ratifies object-after 23 September 2026 17:00 unless Tom objects.
