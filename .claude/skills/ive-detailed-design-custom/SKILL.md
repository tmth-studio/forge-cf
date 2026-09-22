---
name: ive-detailed-design-custom
description: IVE detailed-design phase (PDR→CDR). Takes the frozen architecture (synthesised BFF + model stack) and closes the gap to buildable — for every process a buildable definition (named function / decision-logic / exceptions / handoffs / SOP / an owner on each side of every interface), for every asset the acceptance criterion its process sets, for every connection an interface spec. Inherits the integrated process set (not a requirement→component map) and allocates it to the org model. Produces a detailed-design package + a failable CDR gate. Does NOT build — hands off to /ive-build-pilot-custom.
---

# IVE — Detailed Design of Processes (PDR → CDR)

Closes the gap between **what the architecture defines** (what / who / how-much) and **what you need to actually build every single part of the pilot venture.** This is the proper systems-engineering meaning of the **CDR** phase: *detailed design complete, ready to build.*

**The problem it solves:** the model stack tells you a process exists, who runs it, and what it costs — but nobody can build or run from that. *"U1 guided submission, intake assessor, 265 min/claim, £108"* is not something you can build or hire into. Detailed design produces the **buildable definition**, the **assets it runs on**, and the **interface** for every part.

**When to run:** after PDR (architecture complete — 10 BALM designed, FMOS ≥ 60%, consistency audit PASS), before `/ive-build-pilot-custom`.

**Output:** a detailed-design package — per process a buildable definition, per asset the acceptance criterion its process sets, per connection an interface spec — and a failable CDR gate.

**Handoff to:** `/ive-build-pilot-custom`, which builds from this. It does not design.

---

## Where this fits

```
Architecting (BALM + CTM/AOM/ARM/fin-sim)   → [PDR]   what / who / how-much
   ↓
DETAILED DESIGN (this skill)                → [CDR]   buildable — ready to build
   ↓
Build → integrate → MRP                     → [TRR / ORR]   built + verified
```

---

## ⛔ Precondition gate — PDR-complete frozen architecture

Detailed design designs *the architecture as frozen*. If it isn't PDR-complete, you'll detail-design the wrong thing. Confirm on disk:
- [ ] **VDR frozen** — all 10 BALM requirements solved
- [ ] **Model stack at C10** — CTM / AOM / ARM / fin-sim — with FMOS ≥ 60% (or a consciously-accepted conditional pass, conditions recorded)
- [ ] **Consistency audit PASS** (PDR cleared)

If any is missing → **STOP.** Back to `/ive-conductor-custom`; the venture hasn't cleared PDR. Detail-designing on an unfrozen architecture is wasted work — the design changes underneath you.

---

## Step 1 — Inherit the integrated process set + its full requirement spec

The processes are **inherited** from the synthesised BFF (AOM activities + the 4-D product they deliver). **Do not re-derive them, and do not build a requirement→component matrix.** Inherit the set, but **re-check every defer/require judgement against the frozen architecture** — deferral rationales go stale faster than the set itself (a register written under a superseded form will defer processes the committed form requires).

**Why no requirement→component traceability — IVE principle, not a detail.** The 10 BALM requirements are *constraints the whole BFF must satisfy together*, not modules solved one-component-each. A well-synthesised BFF is integrated: **one mechanism serves several requirements at once** (Grameen's joint liability solved R1+R2+R3; SDG Solver's per-child-gain metric carried R4/R5/R7/R8). A healthy architecture has **far fewer components than requirements** — so a clean 1:1 map is the *signature of bad synthesis*. If you can draw it cleanly, flag it, don't design it.

For each process, gather **every requirement it carries — from all five models** (direction is always *process → its requirements*, several per process):

| Model | What it specifies for the process |
|-------|-----------------------------------|
| VDR / BALM | which of R1–R10 it carries (usually several) |
| CTM | the customer state-change(s) it must produce |
| AOM | level (LMU/Territory/HQ), performer, volume/throughput |
| ARM | cost target — layer (PVC/RC/SC/IC) and the £/unit it must hold |
| fin-sim | its contribution to the unit FMOS |

Output: a **process definition sheet** — the 4-D class of product it delivers, all five-model requirements, its interfaces with an owner named on each side, and an **acceptance criterion = its contribution to the integrated value surplus** (does it perform its role so the unit hits the modelled FMOS). Any asset the process uses or produces is listed against it and takes its acceptance criterion from that process — an asset is never signed off on its own.

---

## Step 2 — Allocate processes to roles in the venture org model

Read the org from the **AOM** — its performers, levels (LMU / Territory / HQ), Customer / User / Enabler classification. Allocate each process to the **role/position that owns it at scale.**

Keep the many-to-many discipline: **a role owns several components; a multi-purpose component may touch several roles** (name a primary owner). If every component slots cleanly into one role, that's the 1:1 smell — the synthesis was thin. *(Sense note, 4 September 2026: "component" in this statement and in the no-1:1 statement above means the **mechanism from the integrated BFF** — the left-side sense — not a Process or an Asset in the right-side vocabulary this file otherwise uses. Both statements are kept verbatim because the many-to-many claim is about mechanisms serving several requirements, which is exactly what the re-basing must not flatten.)*

Output: the **org/role map** — **positions, not persons**: every role is a named position with an **incumbent column** (default incumbent: the principal, who may appoint others, including on success-fee terms subject to spend governance). Never write a person as the role — person-dependencies hide staffing options the same way invented dependencies hide design options.

---

## Step 3 — Detailed-design each process to buildable depth

For each process, design the gap between the architecture line and a **buildable definition** — the level of detail at which a competent operator in the relevant function could run it, and a competent builder could build the assets it needs, **with no further architectural decisions.** The product each process delivers is designed by 4-D class:

| 4-D class | The buildable design produces |
|-----------|-------------------------------|
| Working Product | the product design — flows, screens, data model, logic, content, decision trees |
| Communications Product | the messages, channels, sequences, creative assets |
| Payment Product | the payment/collection mechanism, rails, terms |
| Partner Product | the partner offer, integration spec, agreement terms |

**Carry ranges, not points** for any value still uncertain, tier-tagged (T1–T4). Detailed design narrows the architecture's ranges *by better design*; the build and MRP narrow them *to actuals*. The widest × most-FMOS-sensitive ranges are the ones to flag for the build/MRP to close.

---

## Step 4 — Design how each process runs

For each process, design **how it runs** — the operating detail that makes the ARM's assumed rate **real and repeatable.** It is **not** capacity sizing — throughput (time-per-unit) and spans-of-control are the **ARM's** job. A process definition carries:

- the **decision logic** the role applies — *how* the judgement is actually made (the ARM assumes the activity happens; it never says how)
- **exception / variance handling** — the tail the ARM's *mean* rate hides (escalations, edge cases, QA re-review), and whether the mean holds
- **handoffs** — what package moves to whom, in what form, with an owner named on each side
- the **trainable SOP** — the literal steps a new hire follows

The process is **designed here**; it is **built, run, and validated** (does a real person following it hit the ARM's rate?) in the pilot. A process is the unit of replication — you scale a role by handing a new hire its process definition, not its cost line.

---

## Step 5 — Specify the interfaces to buildable depth

For each connection between processes/roles, design the actual **contract**: API / data format, the handoff protocol, timing, and the failure/exception behaviour. The architecture *names* the interface; detailed design *specifies* it so the two sides can be built independently and still connect.

---

## Step 6 — CDR gate (failable)

Detailed design is complete only when **every part can be built with no further architectural decisions.** Check:

- [ ] Every process has a **buildable definition** (named function + decision logic + exceptions + handoffs + SOP — an operator in that function could run it cold)
- [ ] Every asset carries the **acceptance criterion set by the process that runs it** — no asset is signed off on its own
- [ ] Every interface is **specified to buildable depth, with an owner named on each side**
- [ ] **No open architectural decisions remain** — if a "how should this actually work?" question is still open, that is a *PDR gap*, not a detail to defer → back to the model stack
- [ ] Still-uncertain values carry **tier-tagged ranges**; the widest × most-FMOS-sensitive are flagged for the build/MRP to narrow

**Verdict: CDR PASS** (all clear) · **CONDITIONAL** (ready with named, recorded conditions) · **FAIL** (name the gap, route back). Never round CONDITIONAL up to PASS.

---

## Output — the detailed-design package (artifact contract)

An HTML package (house style: DM Sans + Lora, `#f5f4f1` bg, `#0f2744` navy panel) saved to `04-Projects/{venture-slug}/{venture}-detailed-design-{date}.html`:
1. **CDR verdict panel** — verdict + the one open item
2. **Process definition sheets + org/role map**
3. **Per-process buildable design specs**
4. **Per-process operating detail** — decision logic, exceptions, handoffs, SOP
5. **Interface specs**
6. **CDR checklist** — ticked

Then write the CDR entry into the VDR.

**No prose-only "detailed design done."** A package without buildable process definitions + asset criteria + interfaces is *in progress*, not CDR-complete — the same artifact-contract discipline the conductor enforces elsewhere.

---

## Discipline rules

**Detailed design, not redesign.** You close the gap to buildable; you do not re-open architectural decisions. An open "how should this work?" is a PDR gap — back to the model stack, not a deferred detail.

**Many-to-many holds.** A role owns several components; a component spans roles/functions. A clean 1:1 anywhere is the bad-synthesis smell. *(Same sense note as Step 2 — "component" here is the BFF mechanism, not a Process or Asset.)*

**Process definitions design the operation, not the capacity.** Throughput and spans-of-control are the ARM's. The process makes the ARM's assumed rate *deliverable* — and is what the pilot validates.

**Ranges, not points.** Carry tier-tagged ranges; narrow by design here, by measurement in the pilot.

**The buildable test.** Could a competent operator in the relevant function run this, and a competent builder build the assets it needs, with no further architectural decisions? If no, it is not detail-designed yet.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-detailed-design-custom/SKILL.md` to modify
- **Upstream gate:** PDR (run `/ive-conductor-custom` to confirm) · **Downstream:** `/ive-build-pilot-custom` (build → integrate → MRP → TRR)
- **Registered in** `/ive-conductor-custom` routing table for the PDR→CDR phase
- Workstream: Forge build-tooling (a conductor-routed skill) — NOT WS1 (WS1 refines the architecture-*producing* skills)
