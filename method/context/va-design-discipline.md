# VA Design Discipline — the generative spine of the BALM challenges

**Canonical reference for the venture-assistant architecting skills.** Every BALM challenge skill (R1–R10) and the PCO skill carry a "Generative discipline" section that points here. This file is the single source of truth; the per-skill sections are the operative inserts.

Captured from the Forge VDR review, 2 Jun 2026 (Head of Product). Supersedes `va-3-challenge-step-prompt.md` as the canonical version — that file remains as the standalone prompt-text draft.

---

## The disease this cures

A 10-challenge process has two opposite failure modes, plus a root cause that produces both:

- **Parts-bin (VA-1):** ten bolted-on strategies that never cohere into one business.
- **Premature design (VA-2):** detail specified before a challenge earned it — false certainty.
- **Justification mode (VA-3, the root cause):** challenge 1 conceives the Business Form Factor, and every later challenge merely *explains how the already-conceived BFF solves it too*. The BFF is defended, never beaten. Observed live in the Forge VDR.

When challenges defend rather than mutate, you get premature design and false coherence. Fix the root (VA-3) and the other two become checks rather than rescues.

---

## The four principles

### VA-3 — challenges mutate the BFF, they don't justify it (root cause)

The BFF is a **living draft each challenge has standing to rewrite** — not a fixed artifact each challenge must defend. Challenges are mutation pressure, like selection: each round can change the organism, not just describe it. The current BFF is the *baseline to beat* on that challenge's dimension.

**The tell:** if a challenge produces **zero candidate changes to the BFF**, it has defaulted to justification. A genuine challenge always generates alternatives — some of which it then consciously rejects.

**The five-step structure for every challenge:**
1. **Baseline, honestly.** Where does the *current* BFF stand on this challenge's dimension? Not zero, not solved.
2. **Generative target.** "How could we change the BFF to do materially better on this dimension than the baseline?"
3. **Generate ≥2–3 candidate BFF mutations.** Structural changes to the business, not features bolted on. (Zero mutations = the tell above — say so explicitly.)
4. **Evaluate each against the whole.** Gain on this dimension vs cost to coherence (VA-1) and to dimensions earned in earlier challenges. A mutation that maximises one dimension but breaks the synthesis is rejected.
5. **Decide and record.** Adopt a mutation (restate the evolved BFF) or hold the current one with explicit reasons each alternative was rejected — never "it already works."

**Supporting move — under-specify the challenge-1 / PCO BFF.** A fully-formed early BFF anchors everything after it into justification mode. Keep the first cut minimal; license every later challenge to rewrite it. A heavy early BFF is itself premature design (VA-2).

### VA-1 — synthesis test (anchor the BFF to a real business)

Whenever the (possibly evolved) BFF is stated, anchor it to a *real, existing business*: "this now looks like **[real business]**, because **[the mechanism they share]**." If you can name a real business the venture resembles, the parts have cohered. If you *can't*, that's the flag — it's still a parts-bin. Apply at the close of each challenge.

### VA-2 — premature-design audit (traceability)

Every specified detail should trace back to a challenge that *required* it. Anything specified with no such trace is the suspect for premature design. Run via the verification agent (`/verify-venture-custom`, Pass 3) across the whole VDR, and as a light check at each challenge close: "did I just specify something this challenge didn't need?"

### VA-4 — show your working (auditable choices)

The candidates generated and rejected in VA-3 steps 2–4 are not scratch work. Record them in a "considered / not chosen" block so every choice is auditable — a reviewer can see the options weighed, not just the verdict. This is free if VA-3 runs: the generation *is* the working.

---

### VA-80 — no forward references (earn the mechanism)

A challenge is solved with what exists at that challenge: the PCO and the solutions of the challenges before it. A later challenge's actor, mechanism or vocabulary may not close a gap here. A condition that cannot be met yet is a residual carried to the later requirement by number, with nothing said about how it is solved there. A cell that names something the architecture has not yet introduced is not complete; it is borrowing. (Tom, 2 Sep 2026, Calmly C2 re-run.)

### VA-81 — credibility mechanisms: receiver, instrument, supplier

An endorsement, signal, warranty, certification or published record exists to change what a named actor believes. Specify it as that: who must believe what, to decide what; what they rely on today to believe things of that kind; whether the element is that instrument or one they already accept; and which organisation issues it today, from public record, before the element is admitted. Re-derive it whenever a later challenge changes the receiver. Provider properties ("independent", "standing") are never enough on their own. Added 2 Sep 2026 after the Calmly C3 endorser (CEDR) failed the receiver test at C4/C5.

## How they relate

| Principle | The question it asks | When |
|-----------|----------------------|------|
| VA-3 | Did the challenge *try* to redesign the BFF, or just defend it? | During each challenge (the root) |
| VA-1 | Have the parts *cohered* into one business? | At each challenge close |
| VA-2 | Was each specified detail *earned*? | Standalone audit + light check |
| VA-4 | Are the *options behind each choice* visible? | Output of every choice |

VA-2 (every detail traces to a challenge) + VA-4 (every choice shows its options) together make the whole VDR inspectable.

---

## The operative insert (carried by each challenge skill)

> ## Generative discipline — mutate the BFF, don't justify it (VA-1 / VA-3 / VA-4)
>
> Reference: `04-Projects/Family_High_Performance/context/va-design-discipline.md`
>
> This challenge's job is **not** to confirm the current BFF already handles {DIMENSION}. It is to find out whether changing the BFF could handle it **materially better**. Treat the current BFF as the baseline to beat.
>
> **VA-3 — generate before you justify.** Before writing this challenge's Strategy, run the five steps: (1) baseline honestly on {DIMENSION}; (2) set the generative target; (3) generate ≥2–3 candidate BFF mutations — structural, not features; (4) evaluate each against the whole; (5) decide and record. ⚠ If you cannot produce two genuine mutations, say so explicitly — that is the tell you have slipped into justification mode. Do not paper over it by restating the existing BFF.
>
> **VA-4 — show your working.** Record the candidates considered and rejected in the "considered / not chosen" block of the output format, so the choice is auditable.
>
> **VA-80 — no forward references.** Use only the PCO and C1–C[N] to solve this challenge. Name a later requirement only as the number a residual is carried to; never describe its solution or use its actors.
>
> **VA-81 — credibility mechanisms.** For any endorsement, signal, warranty or record: name the receiver and its decision, the proposition, the instrument the receiver uses today, a public-record supplier of it, and re-derive when a later challenge changes the receiver.
>
> **VA-1 — synthesis test.** When the (possibly evolved) BFF is stated, anchor it: "this now looks like [real business], because [shared mechanism]." If no clean analogue exists, flag it — the parts have not yet cohered.

## The output-format insert (added to each challenge's output block)

```
CONSIDERED / NOT CHOSEN (VA-4 — show your working)
  Baseline on this dimension: [honest current position of the BFF]
  Candidate mutations:
    A. [structural change] → [why it would do better] → [adopted / rejected because…]
    B. [structural change] → [why it would do better] → [adopted / rejected because…]
  Decision: [adopted mutation X — evolved BFF restated below / held current BFF; alternatives rejected for the reasons above]

SYNTHESIS CHECK (VA-1)
  Real-business analogue: [the venture now looks like [business], because [mechanism]]
  If none: [flag — parts not yet cohered; what is missing]
```
