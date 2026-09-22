# The Objective Function — what the Forge core functionality is trying to do

**Owner:** Head of Product · **Part of:** Forge WS1 (CF development) · **Created:** 16 September 2026, on Tom's instruction ("we need an objective function for what the Forge CF process is trying to do: drive the NPV of the venture")
**Pairs with:** `architecture-process-flow.html` (the loop this directs) · `criteria-registry.md` (the constraints) · `tpm-measurement-standard.md` (the measures that roll up to it) · `validation-standard.md` · `realisation-standard.md` Step 3b (threads ordered by it)
**Grounded in:** Simanis et al. (2021), the PCO definition — "the at-scale cash flows needed to pay back all required investment capital at a competitive rate of return" · `balm-pco-custom` — "a rigorous PCO reduces the cash-out required and increases the probability of commercial success — both of which improve the venture's expected net present value" · INCOSE SE Handbook — measures of effectiveness (MOE) at the top, technical performance measures (TPM) rolling up to them; trade studies decided against the MOE · Flyvbjerg and Gardner (2023) — the overrun evidence behind the 60 per cent bar

**Review date:** 15 December 2026.

---

## The statement

**The Forge core functionality maximises the expected net present value of the venture, at the required rate of return, over the investment period, subject to the gates.**

Written out:

```
maximise   E[NPV] = Σ_t  E[cash flow_t] / (1 + r)^t      over t = 0 … T
where      r = the required IRR set at the frame (the capital allocator's hurdle)
           T = the investment period set at the frame
           E[·] = the expectation over the TPM bands, each claim weighted by its probability
subject to the gates in the criteria registry (FMOS bands, the binding gate, VA-rules),
           the principal's standing constraints (zero spend, no cold outreach, approve-before items),
           and the regulatory position for the venture's class.
```

Three consequences follow, and each changes how a step of the flow is run.

---

## 1 · Gates are constraints. NPV is the objective. Neither is the other.

The FMOS bars (25 per cent per requirement, 60 per cent at Phase II) exist because of overrun evidence: a venture that cannot absorb a 62 per cent cost overrun is not safe to fund. That is a constraint on the design space, not the thing to maximise. A design at 300 per cent margin and £2m of NPV loses to a design at 65 per cent margin and £20m of NPV, provided both clear the bar. Until today the CF could not say so, because it had no objective to rank them by.

**Rule.** Where two designs both clear every gate, the one with the higher E[NPV] wins. Where a design choice raises E[NPV] and lowers a margin that stays above its bar, take it. Where a choice raises a margin at the cost of E[NPV], it is a defensive move and must say what risk it buys down, in NPV terms.

**The mode targets are proxies, not objectives.** Mode 2's "cut cost by N per cent" and mode 1's "reach group X" are ways of pointing the search; the objective they serve is the NPV. A run that meets the target with a lower NPV than a design that missed it has optimised the proxy. State both.

---

## 2 · Every TPM rolls up to the objective — so every band has a price

A claim's band is a range of NPVs, not a range of percentages. The TPM record gains one field: **the NPV sensitivity** — the change in E[NPV] from the band's low to its high. That number is what ranks:

- **Design attention.** Generate mutations first for the requirement whose bands move E[NPV] most (the flow's "generate for synergy" now has a direction: synergy that moves the largest NPV band).
- **Validation threads** (`realisation-standard.md` Step 3b). Risk burn-down is defined: a thread's value is the E[NPV] it narrows per pound to stand it up — the value of information. The thread with the highest ΔE[NPV] ÷ cost runs first, subject to dependency and the Q4 gates.
- **Verification effort.** The critic weights findings by the NPV that rests on them. A hard contradiction on a figure worth 40 per cent of E[NPV] is not the same defect as one on a figure worth 1 per cent.

*(16 Sep instance, algotrading: the measured-excess band drives 60 per cent of the at-scale floor through the payout pool, and the fee spread decides the margin at every posture — those two bands carry more NPV than the other nine figure classes combined. Thread 2, the paper tournament, narrows the first for nothing. That is why it runs first.)*

---

## 3 · The fin-sim over time is the instrument, and it is not optional

The fit gate computes a margin at one scale state. The objective needs cash flows over the investment period at the required rate: the ramp deficit, the volume path, the payback year, the terminal value. That is the financial simulation (`ive-fin-sim-custom`), built on the AOM's activities and the CTM's volumes, run over the TPM bands so the NPV is a distribution, not a point.

**Rule.** No design closes Phase 3 (Converge) without an E[NPV] from the fin-sim, reported as a band with the binding input named — the same discipline the FMOS already has. A run whose fit gate passes and whose fin-sim does not exist has a constraint satisfied and an objective unmeasured. *(The algotrading record is in that state: fit at-C10 computed, no fin-sim over time, the IRR asserted. It is a build item before the next verification.)*

---

## What this does not change

- **The gates stay hard.** A design that maximises NPV by failing the 60 per cent bar has not maximised anything; it has priced overrun risk at zero.
- **The conformity guard stays.** A design that breaks the conventional form and raises E[NPV] is the point; the objective rewards it.
- **The principal's constraints stay.** Zero spend, approve-before, no cold outreach are constraints on the search, not terms in the objective.
- **The integrity score is not the objective.** It measures the trustworthiness of the record, not the value of the venture. A 95 on a £1m venture is a well-documented small venture.
- **Whose NPV.** The venture's, at the capital allocator's required rate. The principal's other objectives (right livelihood, the family plan) are constraints the principal applies when deciding whether to pursue the venture — they sit at the Q4 decision, not inside the CF.

---

## Landing

- `architecture-process-flow.html` v7: "The governing idea" gains the objective statement; Phase 2 step 4 (Generate) ranks by NPV band moved; Phase 3 requires the fin-sim E[NPV]; the design-decision table gains "gates constrain, NPV ranks".
- `tpm-measurement-standard.md`: the seventh field, NPV sensitivity.
- `realisation-standard.md` Step 3b: risk burn-down defined as ΔE[NPV] ÷ cost.
- `criteria-registry.md`, Phase 3, proposed row (Tom approves as a grader rule): **E[NPV] stated** — the run reports E[NPV] from the fin-sim as a band with the binding input named, and every trade it made states its NPV effect; a run with no E[NPV] has not converged.
- `ive-fin-sim-custom`: the output contract gains E[NPV] over the TPM bands.

The flow, TPM standard and realisation standard changes are delegated and will be taken; the registry row and the fin-sim skill's output contract are proposed for Tom.
