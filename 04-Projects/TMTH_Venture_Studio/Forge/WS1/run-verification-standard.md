# Run verification standard — v0.5 draft

**Date:** 6 November 2026 (v0.4 and v0.3: 6 November 2026; v0.2: 5 November 2026; v0.1: 2 November 2026) · **Owner:** Head of Verification (studio) · **Asked by:** Tom ("we need to build a verification checklist for these runs … for the whole IVE / FIT start-up process. Need to have a logic model completed too") · **Status:** draft. Item 25 amended 6 November 2026 (rulings on RD-069 below). v0.5 returns item 30 to the IVE test. Tom, 6 November 2026: "lets stick to ours"; on the plan that FIT Startup "isn't used for verdicts": "Nice - go for it"; and "Yes, IVE pass". Tom may object to any other change in the change record, and the change then comes out.

**Why it exists (fact):** the design check (`verify-venture-custom`) tests completeness, consistency, discipline and synthesis. The margin check tests units, periods and band order, and says of itself: "This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world." Nothing tested the inputs, and nothing required the logic model as one output. One studio run passed every check with a cost of goods of £350 that had no breakdown.

**How to use it:** run after the consistency audit and before the integrity score. Record every item as PASS, FAIL or NOT APPLICABLE, with the file and line it refers to. Items marked ★ stop a run being called "verified" if they fail.

## Stage 0 — Intake

1. The entry is stated: named business (enters at C1, sub-requirement 1) or founder idea (starts from the opportunity statement).
2. The customer, the outcome they need and how they get it today are each named with a source.
3. Investment limits are stated, each marked as given or assumed.

## Stage 1 — Opportunity and starting design

4. The broadest credible use case is tested before narrowing.
   - Founder idea: the use-case shortlist (`balm-pco-custom`).
   - Named business, or any other Path C entry: the levelled form only (`balm-pco-custom` Step 2d, `architect-custom` Step 0). No shortlist, and no question to the user.
   - The levelled record states the line taken, the job in the buyer's terms and the levelled case. It also states the next-broader case and the delivery difference that excludes it.
   - Where a whole company is named, the line is the largest by revenue, or the record gives the reason for departing from that default.
   - A record with no next-broader case fails. A later pass that narrows further carries the record forward and states the narrowing.
5. The conventional business it competes with is described with its real costs.
6. At least two alternative designs were generated and ranked before C1, with the reason for the choice.
7. A research plan names the fieldwork that would confirm the key cost and the key value input. A desk-only run states what that fieldwork would be, who it is with and what it costs.

## Stage 2 — Each challenge, C1 to C10

8. The block is identified with evidence, not asserted.
9. A named theory (author, year) says why the fix works: how, for whom, under what conditions.
10. The strategy follows from the theory — not chosen first and justified after.
11. The design choice is the smallest one that solves the block.
12. The customer model and operating model are updated, and the change is visible.
13. The cost or value line the challenge removes or adds is named, with its amount in £.
14. The margin test is re-run on the updated models, reporting central and worst case.
15. The challenge names which earlier challenges its move also serves, and how.
16. ★ Every cost added is built from the bottom up: item, driver, volume, unit price. One figure for several items fails. Every item named in a description has its own price. Both ends of every band have a basis: a published source or, where a recorded search finds none, a labelled assumption that states how the figure was reached. Such a line stays at the lowest evidence grade and shows red. If the scorer finds a published price with a short search, the item fails.
17. The deciding input for this challenge is named, with its evidence grade.

## Stage 3 — The logic model (required output)

18. ★ One table, ten rows, one per challenge. Columns: block → theory → strategy → design choice → effect on cost or value (£ per unit) → margin after → deciding input and evidence grade → links to other challenges. Saved as `outputs/logic-model.md`.
19. Read top to bottom, the cost and value columns add up to the final cost floor and price ceiling. Any gap is named and sized.
20. Every claim in the business case traces to a row.
21. The assumptions that would break the chain are listed separately, each with the test that would settle it.

## Stage 4 — The whole design

22. The consistency audit passes; every soft finding is resolved or carried as an open item with an owner.
23. The financial simulation is rebuilt after C10, and its figures match the challenge files.
24. ★ Deciding inputs: the three inputs that move the margin most (one at a time) are listed. Each has a published source, or the run names the measurement that would replace the assumption, who would do it and what it costs. An assumed input that sets both price and ceiling is flagged.
25. The worst case is a real scenario: every input at its worst end in one table; for each pair, whether they move together, apart or are unrelated; where unrelated, a likely-bad case is reported beside the all-worst case; the single input that comes closest to fixing it is named. The worst end of each input is found for this reading (form, basis, test) by search, with one-fact and computed inputs held together, and is not carried from another form or basis. The search states its method and what it can miss. Where the ends differ by test, the one table has a column of ends for each test.
26. Sources fit their use: each is checked for what it measures and for whom ("source OF what, current FOR what"), dated, graded, and every assumed figure shows in red in the business case.
27. Phase II: the margin at the conservative case is 60 per cent or more. If not, the run states which input would have to move, and by how much.

## Stage 5 — Independence and output

28. ★ Scoring and this checklist are run by a different helper from the builder, without its notes. It re-computes the central and worst-case margins from the inputs, without reading the run's results.
29. The business case passes `python3 .scripts/check-house-style.py`; invented figures are red; every number traces to the model (no new numbers in the write-up).
30. The verdict wording matches the result. The Head of Verification gives the verdict. The run's record states one verdict and claims nothing better than this wording. There are three wordings:
   - "Not verified": a ★ item fails. A read of a record that has not reached R10 prints "unfinished" beside the word and names the last requirement reached, for example "not verified · unfinished, R1".
   - "Provisional": every ★ item passes and a margin test below fails.
   - "Verified": every ★ item passes and both margin tests pass, or Tom accepts the failed margin test in writing. The word always carries the validation reading beside it, for example "verified · validation-maturity: pre-operational". It also prints the count of forms tried, from the run's ledger, failed and set aside included. Where the ledger holds more than one form, the word is not given until a helper who has not seen the search sources again the inputs item 24 lists and the input that comes closest to turning a margin test to a fail. A source outside the band widens the band, and item 30 is read again.

   Read the two margin tests at the all-worst case in item 25's table. Every input, volume included, sits at its worst end:
   - (a) fit margin at each challenge (price ceiling ÷ cost floor − 1) is 25 per cent or more
   - (b) business margin of the whole design (price ÷ whole cost − 1) is 25 per cent or more

   A borderline is a fail. A likely-bad case does not replace these tests. Absent fieldwork alone holds no run back.

   The zero net present value price on a simulation page is not a test. It moves no item.

   **An IVE pass is "verified" (my reading, inference).** Tom, 6 November 2026, asked whether "FIT pass" now means an IVE pass: "Yes, IVE pass." Item 30 is the only test in this method that reads the whole design and gives a word, so that word is the pass.

   **Tom's further test, note only.** Tom, 6 November 2026, on what "much less than the price a customer would rationally pay" means: "1.6 sounds better than 1.25 I guess!" He holds it lightly. So customer value ÷ required price is printed against 1.60, at all-worst and also as stated. That reading of his words is the Chief of Staff's. It sits beside item 30, does not replace it, and moves no word.

   **Pay-on-success contracts, note only (my reading, inference).** Where a job that misses earns nothing and bears the cost, the cost floor in test (a) carries the failed jobs. So the fit margin reads value ÷ cost of a paid job − 1. Ruling: a studio run record.

## The marks a design reads against under IVE

Margin form, for every line: (price or ceiling − cost) ÷ cost, low-point price against high-point cost with all four cost layers filled (`criteria-registry.md` line 32; `balm-challenge-2-custom`). Whole cost carries the return on capital, tax and head-office profit (`generate_business_case_xlsx.py` lines 325 to 339, read in RD-062).

| Mark | Reads | Source that IVE uses it | Book source |
|---|---|---|---|
| At least 25 pass, 15 to 24 borderline, under 15 fail | Each requirement's gate reading | `criteria-registry.md` lines 38 and 112, as committed | **None read.** Built to Hold p. 7 gives no 25 (RD-062). With the Chief of Staff as a question for Tom |
| At least 25, a borderline a fail, all-worst, volume included | Item 30, both margins | Change record, 5 November 2026; `finsim-model-spec.md` `target_margin` | The same 25 |
| At least 60, 25 to 59 tighten or carry, under 25 fail | Phase II capital only, item 27 | `criteria-registry.md` lines 39 and 41 | Registry line 44 credits Built to Hold, and RD-062 did not find it there. Flyvbjerg and Gardner's 62 per cent overrun is the reason given. With the Chief of Staff as a question for Tom |
| Capital bar: required return, horizon, terminal assumption and margin, each stated | Each venture | Registry row "Capital bar stated" (RB-V-026, 16 September 2026) | Set per venture or by a cited rule. No fixed figure |

**Not IVE marks, and not read for a verdict (inference from Tom's plan):** margin 50; customer return 50 or 300; the product ratios 2.25 and 6; the band by money at risk; a price solved at a 25 or 40 per cent target return; reading at stated at-scale volume. They came in with FIT and appear in records of 6 November 2026 as dated figures.

**Customer return has no pass mark here.** I found no IVE source for one. It stays information, as RD-065 first said: it moves no item. I do not fill the gap.

### Rulings on RD-068 section 7 (6 November 2026)

These set no new figure. Item 30's text does not change.

1. **"Item 30's test" means item 30's IVE test.** Tom: "Yes, IVE pass." The Chief of Staff confirmed that this answered whether a FIT pass now means an IVE pass. So the test is the two margins above. R&D's change of 35 lines to "Item 30's test" is right.

2. **Item 30 and the challenge gate both hold, because they read different things.** At each challenge, the gate reading and its band (25, 15 to 24, under 15) decide whether design continues. All-worst prints there and decides nothing. On the finished design, item 30 reads all-worst and gives the verdict word. **The cost, named:** a design can run to C10 on the band and fail item 30 at the end. The printed all-worst line is the early warning. Bringing back a stop at each challenge would be a new decision (RD-068 section 1).

3. **VA-182: the 50 and the 300 go. A price still may not exceed value.** Those two figures are FIT Startup's, and IVE has no customer-return mark. I ruled them in after "Yes, FIT replaces it", and that ruling has now been replaced, so I withdraw them.
   - WTP_low is the low end of the price the customer would pay, from research or a sourced comparison, and never above value
   - value is the R2 Key Monetizable Cost
   - where no research or comparison exists, the ceiling is that value, marked "upper limit: no customer return taken off"
   - customer return prints as information (VA-181). It decides nothing
   - RD-059's deflators stay unruled and are not used

   **The cost, named:** readings rise, so a design could pass that does not pass today. This is an easing, so Tom hears it and may object. **Tension, not resolved:** at exactly 25 on this ceiling, cost is 80 per cent of value, and a price at the ceiling leaves the customer no return (arithmetic: 1 ÷ 1.25). Tom's test is "much less", and it may ask for more than item 30 does. That figure is his.

4. **The free-route guard: "has" means available.** `balm-challenge-2-custom` line 422 gives its own test: "does the other route remove the problem itself?" That test reads the route, not the customer's use of it. So a customer with a free route that removes the problem comes out of the market, used or not. "Coping is not solving" still applies: a route that does not remove the problem, or that this customer cannot reach, takes nobody out. **Falsifier:** an IVE source that counts non-use as a carried cost, or evidence that the route fails for that group. FIT Startup's Book may measure value from current routines, but it is a reference only and does not decide this. R&D may tidy "still carries it".

5. **60 is the Phase II capital gate only.** The registry says so at its Phase II row, and the R2 skill says "the registry wins" (line 97). Item 27 has no star, so "verified" does not need 60 (inference). The registry's note says the cell flips if Simanis puts 60 earlier, but his method is now a reference, so that no longer applies. R&D should align the skills: after R1 and at the architecture review exit they read the 25 band, and at PDR 60 is named as the capital gate, not a design stop. This matches the registry and moves no figure.

6. **The reading table needs fresh readings.** Its percentages rest on a required price and do not read against 25. Fresh rows read both item 30 margins at all-worst, on the ceiling in ruling 3.

7. **`Forge/WS1/financial-gate-standard.md` and the registry's "FIT Startup is the binding financial gate" do not operate.** The standard was written at 15:25 on 6 November 2026, after "Yes, IVE pass". Neither is committed and no R&D record cites them. Asked about them, Tom said: "Hmm - may have done by accident...". The result stands on his "lets stick to ours" and "Yes, IVE pass". Reading an accident as not a ruling is the Chief of Staff's inference. R&D is tracing the author.

### Rulings on RD-070 section 7 (7 November 2026)

Tom, 7 November 2026, as the Chief of Staff relays it: the run keeps working until something is verified. These three rulings keep that word worth having. All three are accepted, and they are written into item 30. No mark moves and no star changes. The version stays v0.5. Two of them tighten "verified", so Tom may object, and if he objects the change comes out.

1. **"Verified" prints the count of forms tried.** A run that tries many forms and stops at the first pass is more likely to stop on a form whose inputs read too well (inference; no measure of this size exists here). The reader needs the count to weigh that. A new run for the same aim carries the count on, so a restart cannot reset it.

2. **After a search, a helper who has not seen the search sources the deciding inputs again.** Item 28 re-computes from the inputs, so it does not test the inputs. The helper may be the item 28 helper. If its source falls outside a band, the band widens and item 30 is read again. It never narrows a band. A run with one form in its ledger does not need this, because no search selected that form (inference).

3. **A read of an unfinished record prints "unfinished" beside "not verified".** The ledger can then tell a form that stopped from a finished design that failed. Item 18 fails on an R1 record for that reason alone, as on form C, where it is not the architect's fault. "Unfinished" states how far the record got. It does not say the form would pass. The ledger still records any margin that fails. Item 30's three words do not change. Rulings already issued keep their text.

**Effect on each scored run: none.** Rulings 1 and 2 act only on "verified", and no scored run holds it (fact, table below). Ruling 3 adds a print and moves no word. **The cost, named:** a passing form needs one more helper, and it can drop back to "provisional" or "not verified" on the wider band. This asks more of the run; it does not stop it. VA-184 sends it to the next form.

### Rulings on RD-069 section 6 (6 November 2026)

R&D proposed these and did not edit the standard. They are this seat's decisions. They tighten the standard, so Tom may object, and if he objects the change comes out. No gate figure moves and no item loses its star. The version stays v0.5, because the marks do not change and 13 skill and R&D files cite that number.

1. **Item 25 takes R&D's sentence and one more.** The added sentence requires the search to state its method and what it can miss. Without that, a reader cannot tell a full count from a partial one. Two methods support a pass: every combination of range ends, or a formula that fixes the direction of some inputs and every combination of the rest. Form C used the second, and it gave the architect's three figures (`hov-ruling-2026-11-06.md`). One studio product shows why computed inputs are held: two fees set from price raised a false flag until they were held with price (RD-069 section 3).

2. **Each test's own lowest binds for item 30. "One table" stays as the format.** Item 30 asks for each margin at 25 or more. A pass at one corner does not show that the other margin holds at its own lowest, so a single-corner table could pass a design that fails elsewhere (inference). The one table has a column of ends for each test. Each column holds one value per input, so VA-171 holds inside each test. In form C one corner holds all three lowest figures (fact, by exact count). RD-069 section 6 states that one studio form's lowest figures can use different ends.

3. **Item 30 reads the lowest found, once every flag is answered.** A flag has two answers under VA-183: the stated end is wrong in this reading, or two inputs are tied and must be held. Stated ends are not read where a lower answered reading exists. Item 30's words do not change, because it reads "the all-worst case in item 25's table", and ruling 1 sets what that table holds.
   - an open flag stops a pass; it does not make a fail by itself
   - a fail stands even if the search was partial, because a missed combination can only lower the figure (inference)
   - a pass cannot rest on moving one input at a time over 14 inputs; the item 28 re-computation counts every combination of the inputs whose direction is open
   - a figure found inside a range, from a step or a ramp, is read the same way

   This replaces VA-183's "moves no mark" for item 30 only. The print stays information at each challenge gate, under ruling 2 on RD-068.

4. **VA-183 is countersigned, with three notes.** I checked the derivation by hand: the slope in Q has the sign of uR − pW (fact, arithmetic). The exact count on form C agrees with the architect's search (fact).
   - R-W80 stays unproven until a run with a volume or pass-through input uses it, as RD-069 says
   - R&D should change "Information only: it moves no mark" to match ruling 3
   - "every combination" cannot be run over 14 inputs by the script as it stands, so a run there uses the second method in ruling 1 or says that it has not supported a pass

5. **Not ruled: whether bases may be mixed in one reading.** RD-069 section 7 leaves this with this seat. No word depends on it today: the block form fails on one basis and on two. I rule when a form's word depends on it. My reading in the block ruling stays labelled as inference.

**Effect on each scored run: none.** The lowest found is never above the figure at the stated ends. Every run in the table below fails a star, and so do two later studio forms. So no fail turns into a pass, and no verdict changes (inference). **The cost, named:** a later design can pass at its stated ends and fail at the lowest found, and a run does more search before a pass.

