# Business Case Standard — the two files a run hands to someone else's company

**Owner:** Head of Product · **Capability:** Forge WS1 — CF development
**Version:** v0.2 (forecast statements added, same day) · **Added:** 22 September 2026, on Tom's instruction of the same day: *"Want the output to be a business case document, with an excel file for supporting evidence, organised in the way the IFC document advises … That's a format someone can use in their own company"* and *"Use this standard for the business case / plan: https://www.gov.uk/write-business-plan"*.
**Parent:** `derivation-standard.md` · **Siblings:** `finance-standard.md` · `tpm-measurement-standard.md` (how every figure is written) · `run-record-standard.md`
**Applies to:** the final output of every run — what the architect hands over once Verify has closed.
**Used at:** the front door's Verify step (`architect-custom`, output line) · `ive-fin-sim-custom` Stage 2 · `ive-business-case-custom`.

**What this is, and is not.** This is a **format standard for the run's output**. It does not change the method: the ten requirements, the gates, the registry and the grader are untouched. It fixes the shape of the two files a reader in another company receives, so that the case can be read by a manager, checked by a finance colleague and taken into a funding conversation without the method's vocabulary.

**Review date:** 15 December 2026.

---

## 1 · The two files

| file | standard it follows | built from |
|---|---|---|
| `{slug}-business-case.html` — the business case document | GOV.UK *Write a business plan*, which points to the Start Up Loans / British Business Bank template. Its seven sections, in its order, with its questions answered | the venture design record and the cell index |
| `{slug}-business-case-evidence.xlsx` — the evidence workbook | IFC *Running the Right Numbers* (Simanis), Part II: the twelve tabs of the bottom-up financial model; the two sheets the Start Up Loans template asks for; the three forecast financial statements by year, as a lender or an investor expects them; a Check tab | the model data file (`{slug}-model.yaml`, spec: `.claude/skills/shared/finsim-model-spec.md`) |

Both come from one model data file. The document quotes the workbook; it never carries a figure of its own. **Rule: every figure in the document is a named cell in the workbook**, written as the number with its cell name beside it in small type, for example *£43.47 per service (`cost_per_transaction`)*. A reader who doubts a number opens the workbook and finds it. A number with no cell is a defect.

## 2 · The workbook

Tabs 1 to 12 are the IFC model in the IFC order. Tabs 13 and 14 are the Start Up Loans sheets. Tabs 15 to 18 are the forecast financial statements by year. Tab 19 checks.

| tab | contents | IFC step |
|---|---|---|
| 1 Master | every variable and assumed value, with its base, low and high, unit, tier and source; a scenario switch (base / all-low / all-high). Inputs are blue. Change numbers here only | — |
| 2 Customers | reachable population → total addressable market → number of operating units → customer base per unit → transactions per month; revenue and cost of goods by product | 1 |
| 3 HR | activities × minutes × driver quantity × multiplier → hours → headcount (rounded up) → cost, with utilisation; head-office roles | 2 |
| 4 Depreciation | assets, cost, life, quantity, monthly depreciation; unit and head office | 2 |
| 5 Running | general running costs by driver; unit and head office; fixed and volume-driven totals | 2 |
| 6 Start-up | one-time costs, working capital, the monthly start-up charge; head-office development | 3 |
| 7 Returns | capital invested × cost of capital ÷ 12 | 3 |
| 8 Tax | return × tax rate | 3 |
| 9 Unit costs | the unit's whole cost per month, line by line, with head office allocated; cost per transaction | 4 |
| 10 Pricing | cost floor, interim price, FMOS, verdict, required price, required price by product, price fall to the floor; the one-at-a-time sensitivity, the binding input and the worst-corner FMOS | 4, 5 |
| 11 Unit P&L | whole-cost profit and loss per unit at the interim price and at the required price; surplus ÷ cost recomputes FMOS | 5 |
| 12 Venture P&L | units × unit lines plus the head-office block; venture surplus per month and year | 5 |
| 13 Sales | the template's sales assumptions: up to four products, twelve months of volume, sales and cost of sales for the units open in year one | template |
| 14 Cash flow | the template's twelve-month forecast: inflows, outflows by line, net, opening and closing; loan repayment; lowest balance; the stress test with revenue reduced by 10%; cash needed | template |
| 15 Roll-out | operating units open by year, new units, unit-months at steady-state volume; head-office share and equity raised by year; the loan split into principal and interest by year; capital spend on new units, replacement of assets at the end of their life, depreciation and net book value | forecast |
| 16 Forecast P&L | revenue to profit after tax by year, with a total: cost of sales, staff, running costs, start-up costs of new units, head-office development, depreciation, interest, tax after losses brought forward | forecast |
| 17 Forecast cash flow | cash from operations, investing and financing by year; opening and closing cash; the lowest year-end balance and the extra funding needed | forecast |
| 18 Forecast balance sheet | fixed assets, cash, loan, tax payable, net assets; share capital and retained profit; a row that must read zero | forecast |
| 19 Check | eleven recomputations (the margin two ways; required price returns the target; venture = units × unit; cash chain; year-one volume; whole cost; the builder's own margin; forecast year one opens the same units and closes at the same cash as tab 14; the balance sheet balances in every year). Every row PASS or the workbook is broken | — |

Rules the workbook keeps:

- **Live formulas everywhere.** The only pasted values are the sensitivity table on tab 10, labelled as computed by the builder from the same inputs. A reader can change any blue cell and watch every tab move.
- **The transport pattern.** Ship the finished workbook, never the script or a recipe for one. The recipient's environment may not run code; a workbook opens anywhere. The Check tab is the built-in proof the file arrived whole.
- **The margin of safety as the registry defines it** (its name there is FMOS): (price − cost) ÷ cost. Gate 25% pass, 15% to 24% borderline, under 15% fail. Required price = cost × (1 + target).
- **Every input the verdict depends on is a band with a source and a tier** (`tpm-measurement-standard.md`). The binding input is named on tab 10 and in the document.
- **Headcount is whole people.** The model rounds up and shows how full each person is, so a role at 40% is visible and the reader can decide whether to share it.
- **The forecast is conventional accounting.** The IFC tabs price the unit with an investment return and its tax inside the cost; the forecast statements show the venture as a lender or an investor reads it — profit after actual interest and actual tax, cash, and a balance sheet that balances. The two views share every input. Their rules are written on the tabs and in the model data file spec.
- **No venture but this one.** The workbook carries nothing from any other venture.

## 3 · The document

The seven sections of the GOV.UK / Start Up Loans template, in its order, under its headings, answering its questions. Each section states where its content comes from in the design record. The reader never sees the method's requirement numbers; the writer uses them to find the material.

| § | template heading and questions | drawn from |
|---|---|---|
| 1 | **Your business and objectives.** What the business does, its products or services. Objectives: short term (this year) and medium term (one to two years), each specific, measurable, achievable, relevant and timed. What the funding will be used for: cost, amount, reason | the commercial opportunity and the business form; the requirement gates and the launch plan as the objectives; the start-up and development lines on tabs 4 and 6 as the funding table; tabs 15 to 18 for the units, revenue, profit and cash by year and the funding the roll-out needs |
| 2 | **Your skills and experience.** Who runs it and what they bring; the gaps and how they are filled | the position register: the seats the design needs, named by role, who holds each today, the conversion trigger for each |
| 3 | **Your target customers.** Who they are; the need or problem addressed; how prices were set | the target customer and the key market characteristic (R2); the want, use and buy blocks (R4 to R6); tab 10 for the pricing — interim price, cost floor, required price, and how the price was set against what customers pay today |
| 4 | **Your market and competition.** Research done; two named competitors with location, prices, strengths and weaknesses; what sets the business apart; strengths, weaknesses, opportunities, threats | the opportunity sizing and what customers pay today (the baseline); the switching cost, resource moat and supplier replaceability (R8 to R10) as what sets it apart; the research methods are the source tiers on tab 1, stated in plain words |
| 5 | **Your sales and marketing plans.** How customers will hear of it, choose it and keep buying; the channels and their cost | the want block and the gateway partners (R4, R7); the sales and marketing assets standard; the marketing lines on tabs 3 and 5 |
| 6 | **Your operational plans.** Key suppliers and relationships with status and terms; staff now and in twelve months with roles; premises; laws and regulations; insurance | the operating model — the last-mile unit and head office (tabs 2 to 5); the partnerships standard for suppliers; the position register for staff; the finance standard for regulation and insurance |
| 7 | **Back-up plan.** How repayments are met if the plan fails, and why that is realistic | tab 10: the margin from failure, the binding input and the worst-corner margin; tab 14: the stress test, the lowest balance and the cash needed; tab 17: the lowest year-end cash and the funding the roll-out needs; the pivot trigger from the design record |

Rules the document keeps:

- **The template's headings, lowercase after the first word, in the template's order.** A reader who knows the GOV.UK page finds what they expect where they expect it.
- **Plain English, house style, no method vocabulary.** No requirement numbers, no BFF, no FMOS in the body — say "margin of safety". The checker runs before the file is shown: `python3 .scripts/check-house-style.py <file>`.
- **A one-page summary first** (a navy panel): what the business is, the price, the cost floor, the margin of safety and its verdict, the cash needed in year one, the binding input. Six numbers, six cell names.
- **Every figure cites its cell** (section 1 above). The cell index (`{slug}-business-case-evidence-cells.md`, written by the builder) is the writer's source; the document's last section reproduces it as an appendix so the reader has the map.
- **Bands, not points, on the figures the verdict depends on.** "£65 to £90, base £80" with the source, not "£80".
- **Both files open together.** The document's header names the workbook file; the workbook's Master tab names the document in its title row.

## 4 · Where this sits in the run

1. The challenges close and Verify passes.
2. `ive-fin-sim-custom` Stage 2 writes `{slug}-model.yaml` from the confirmed inputs, then runs the builder: workbook plus cell index. The interactive single-file simulation the skill also builds remains the studio's working tool; the workbook is what leaves.
3. `ive-business-case-custom` writes the document from the design record and the cell index, runs the house-style checker, and opens both files.
4. The run record lists the three files (model data file, workbook, document) with their digests.

## 5 · What this standard does not settle

- **Office formats.** The document is HTML. A reader in a large company may need `.docx`; the skill notes that a print-to-PDF from the browser is the interim route. Tom's call whether to add a `.docx` build.
- **The interactive simulation.** Whether the single-file HTML simulation continues to be built once the workbook exists, or is retired, is a fin-sim question for the Head of R&D.
