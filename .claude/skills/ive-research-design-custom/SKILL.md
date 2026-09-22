---
name: ive-research-design-custom
description: Research Design Agent for IVE ventures. Takes the PCO output and the chosen Workaround Strategy (R1), and produces a single unified fieldwork protocol that answers both R2 (Key Monetizable Cost, via ethnographic routine mapping) and F2 (Want Block, Use Block, Buy Block classification) in one research wave — eliminating the structural inefficiency of two separate research rounds.
---

# IVE Research Design Agent

Runs after PCO and the Architecture Generator (or after R1 if the architecture is already chosen), and before fieldwork begins. Its job is to design a single research protocol that covers both R2 and F2 — so the practitioner goes into the field once, not twice.

**The problem it solves:** R2 requires ethnographic observation of customer routines to find the Key Monetizable Cost. F2 requires analysis of those same routines to classify Want Blocks, Use Blocks, and Buy Blocks. The raw material is identical. The questions asked of it differ. A practitioner following the skill sequence in order has no signal to design R2 fieldwork with F2 questions already in scope — so they do two rounds. This skill eliminates that inefficiency.

---

## Where this fits in the IVE sequence

```
PCO → Architecture Generator → R1 (Workaround Strategy chosen)
                                          ↓
                              ★ RESEARCH DESIGN AGENT ★
                              (design the fieldwork protocol)
                                          ↓
                              Fieldwork — one wave, two purposes
                                          ↓
                              R2 analysis (Key Monetizable Cost)
                                    +
                              F2 analysis (R4 Want Block, R5 Use Block, R6 Buy Block)
```

This skill produces the protocol. The practitioner conducts the fieldwork. R2 and F2 analysis follow from the same data.

---

## The two lenses this protocol must serve

### Lens 1 — R2 (Key Monetizable Cost)

R2 asks: what is the customer paying — in money, time, or stress — to achieve the outcome the venture will deliver? The answer is the Key Monetizable Cost: the specific cost item in the customer's current routine that the venture's BFF can eliminate or absorb.

**What fieldwork must capture for R2:**
- The full routine the customer goes through to achieve the relevant outcome (the Attendant Routine)
- Every activity in that routine: what they do (DO), what they buy or use (USE-BUY), what they think (THINK), what they feel (FEEL)
- The time cost of each activity (how long it takes)
- The financial cost of each activity (what they spend)
- The stress cost of each activity (how much effort, uncertainty, or frustration)
- Where in the routine the biggest cost concentrations sit — these are the candidates for the KMC

**The Attendant Routines map format:**

| Step | DO | USE-BUY | THINK | FEEL | Time | £ cost | Stress |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |

### Lens 2 — F2 (Block classification)

F2 asks: what stops a customer from switching to the venture's BFF, even after they understand the value? Three types of block:

**Want Block (R4):** The customer doubts the value claim. They do not believe the venture will deliver the outcome. This is a perception problem, not a product problem. The R4 solution must create convincing proof at the point of encounter — not a better product.

**Use Block (R5):** The customer understands the value but cannot integrate the venture's product into their existing routine. The biggest disruption to their daily life is the learning or behavioural change required. The R5 solution must embed adoption into the routine, not fight it.

**Buy Block (R6):** The customer wants to use the product and knows how, but cannot align their cash flow with the payment structure. The timing, size, or format of payment conflicts with when money is available. The R6 solution must match the customer's cash rhythm, not the venture's preferred billing cycle.

**What fieldwork must capture for F2:**
- Where in the routine does doubt about a new solution arise? (Want Block signal — the moment of hesitation)
- What in the routine would be hardest to change? (Use Block signal — the behavioural anchor)
- When does money arrive and when does it leave? What is the cash rhythm? (Buy Block signal — the payment timing pattern)

---

## Step 1: Confirm the PCO context

Ask the user:

1. **Who is the target customer?** (The segment defined in PCO — be specific: not "low-income consumers" but "sole traders in informal markets with monthly cash flow under £X")
2. **What outcome are they trying to achieve?** (The job-to-be-done the venture addresses)
3. **What is the conventional routine for achieving it?** (How do they do it today — the baseline BFF the venture is designed to replace or bypass)
4. **What is the chosen Workaround Strategy?** (The R1 candidate — what will the venture do differently)

If the user has run `/balm-pco-custom` and `/balm-challenge-1-custom`, these are already defined. Ask them to paste the key outputs or point to the files.

---

## Step 2: Map the Attendant Routine

Before designing the protocol, map the customer's current routine from existing knowledge.

Work through the routine step by step with the user:

> "Walk me through what a customer currently does, from the moment the job-to-be-done arises to the moment it is resolved. For each step: what do they do? What do they use or buy? What are they thinking? What are they feeling?"

Build a draft Attendant Routines map. Note where:
- Costs concentrate (time, money, stress) — these are the R2 candidate KMC sites
- Doubt would naturally arise about a new solution — these are the R4 Want Block signals
- Behavioural anchors exist (habits, dependencies, routines that are hard to break) — these are the R5 Use Block sites
- Cash flow constraints appear (when money comes in, when it goes out) — these are the R6 Buy Block signals

This draft map is the basis for the observation and interview guides.

---

## Step 3: Design the observation guide

The primary method is ethnographic observation — watching the customer execute the routine in their natural environment, not asking them to describe it.

**Produce an observation guide with:**

### 3a — Site and session specification

- **Where to observe:** The specific locations where the routine happens (name them from the draft routine map)
- **When to observe:** The time of day/week/month when the routine is most likely to occur (cash rhythms are seasonal and weekly — specify)
- **Session length:** Long enough to observe a full routine cycle, including waiting and transitions
- **Number of sessions:** Minimum to reach saturation (typically 8–12 for a new customer segment)
- **Observer role:** Participant observer (joining the routine) vs. fly-on-the-wall (watching) — specify which and why

### 3b — Observation focus areas

For each step in the draft Attendant Routine map, specify what to watch for:

**R2 focus (cost sites):**
- Note exact time spent at each step (use a timer, not estimation)
- Record every cash transaction, even small informal ones
- Watch for effort signals: sighing, repeating steps, asking others for help, abandoning and returning
- Note what the customer uses or buys that they would not need if the outcome were delivered differently

**F2 focus (block signals):**
- Note any moment where the customer hesitates, checks, asks someone, or expresses uncertainty about whether something will work — these are Want Block signals
- Note the steps that are most automatic — the ones the customer does without thinking — these are the Use Block anchors (hardest to change)
- Note when cash is present vs. absent: when do they pay others? When do they receive money? What happens when a payment is due and cash is short?

### 3c — Observer notes template

A simple one-page template the observer completes during each session:

```
Date / time:
Customer ID (anonymised):
Location:

ROUTINE STEPS OBSERVED:
Step | Duration | Cost (£) | Effort level (1-5) | Notes

KEY MOMENTS:
- Hesitation/doubt observed at: [step] because: [description]
- Behavioural anchor observed at: [step] — [what they did automatically]
- Cash constraint signal at: [step] — [what happened]

SURPRISES (things not in the draft map):
```

---

## Step 4: Design the interview guide

Follow-up interviews deepen what observation surfaces. They do not replace observation. The interview happens after the observed routine, while the session is still live in the customer's memory.

**Interview structure — three parts:**

### Part 1 — Routine reconstruction (R2)
Prompt the customer to narrate the routine just observed. Do not lead. Ask:
- "Walk me through what you just did, from the start."
- "That step where you [specific observed action] — why do you do it that way?"
- "What would happen if you skipped [costly step]?"
- "What does doing this [whole routine] cost you? In time? In money? In effort?"

**Listen for:** The cost items they name without prompting. The steps they describe as unavoidable. The outcomes they say they'd sacrifice to reduce the cost.

### Part 2 — New solution response (F2 — Want Block)
Describe the venture's workaround in plain language. Do not show materials yet — just describe the mechanism of action. Ask:
- "Does that make sense to you?"
- "Do you believe it would work?"
- "What would you need to see before you'd trust it?"
- "Who else in your life has tried something like this?"

**Listen for:** The specific doubt. Is it about the venture's capability? About their own eligibility? About what happens if it goes wrong? The exact nature of the doubt is R4 design material.

### Part 3 — Adoption and payment (F2 — Use Block + Buy Block)
- "If you were going to use this, what would you have to change about how you do things now?"
- "What would be hardest to change?"
- "When does money come in for you? When do you have cash available?"
- "When would it be easiest to pay for something like this? Hardest?"

**Listen for:** The specific behavioural anchor (the step in the current routine that the venture's product would replace or disrupt). The cash rhythm — when money arrives, when it's already committed, when flexibility exists.

---

## Step 5: Specify the analysis protocol

The same data serves two analyses. Specify how to code the fieldwork notes for each.

### R2 analysis — Key Monetizable Cost

After fieldwork, build the full Attendant Routines map with data from observation and interview. Then:

1. **Total the costs** at each step (time × estimated hourly value + cash spend + stress weight)
2. **Rank steps by total cost** — the highest-cost step is the primary KMC candidate
3. **Test KMC transferability:** can the venture's BFF eliminate or absorb this cost? If yes: confirmed KMC. If no: move to the next highest-cost step.
4. **Calculate the price ceiling:** what share of the KMC can the venture claim while leaving enough surplus that the customer is better off?

### F2 analysis — Block classification

From the same fieldwork data:

1. **Want Block:** which step in the routine — or which feature of the new BFF — generated the most doubt in Part 2 interviews? This is the R4 design target.
2. **Use Block:** which step in the current routine is the biggest behavioural anchor? This is the R5 design target — the venture's product must fit around this anchor, not fight it.
3. **Buy Block:** what is the customer's cash rhythm? What payment format — size, timing, frequency — would align with it? This is the R6 design target.

---

## Step 6: Output

Produce the research protocol as an HTML file.

Save to: `04-Projects/{venture-slug}/research-protocol-{date}.html`

Use the standard design system (DM Sans + Lora, #f5f4f1 background, #0f2744 navy panel).

The document contains:

1. **Research purpose** — one paragraph: this protocol serves R2 (Key Monetizable Cost) and F2 (Want Block, Use Block, Buy Block) in a single fieldwork wave
2. **Target customer** — the segment specification from PCO
3. **Draft Attendant Routine map** — the pre-fieldwork hypothesis (table format)
4. **Observation guide** — site/session specification + focus areas + observer notes template
5. **Interview guide** — three-part structure with verbatim questions
6. **Analysis protocol** — R2 coding instructions + F2 block classification instructions
7. **Routing instructions:**
   - R2 analysis feeds into `/balm-challenge-2-custom` (R2 — Key Monetizable Cost design)
   - F2 block classification feeds into R4 (`/balm-challenge-4-custom`), R5, and R6 when those skills are run

Open in browser after saving.

---

## Notes

- This is a custom skill, protected from Dex updates
- Edit `.claude/skills/ive-research-design-custom/SKILL.md` to modify
- **Runs after:** `/balm-pco-custom` (PCO) and `/balm-challenge-1-custom` (R1 — Workaround Strategy chosen)
- **Before fieldwork:** not before R1. The Workaround Strategy must be known before designing the fieldwork — R2 and F2 field questions both depend on knowing what the venture will do differently
- **Feeds into:** `/balm-challenge-2-custom` (R2 analysis), and R4/R5/R6 in F2 (block classification analysis)
- **Method:** ethnographic observation first, interview second — do not invert. Observation catches what customers do; interview catches what they say. Both are needed.
- **Attendant Routines map:** the primary IVE tool for R2 — DO / USE-BUY / THINK / FEEL matrix across the routine steps
- **Related skills:** `/balm-pco-custom`, `/balm-challenge-1-custom`, `/balm-challenge-2-custom`, `/ive-fit-verifier-custom`
