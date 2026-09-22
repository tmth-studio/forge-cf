---
name: ive-business-case-custom
description: Write the business case document for an architected venture — the GOV.UK / Start Up Loans seven sections, every figure cited to a named cell in the evidence workbook the fin-sim built. The run's final output, in a form someone can use in their own company. Run after Verify has closed and the workbook exists.
---

# Business case document

**Standard:** `04-Projects/TMTH_Venture_Studio/Forge/WS1/business-case-standard.md` — read it first, every time. This skill executes it; it does not restate it.

**What you produce:** `{venture-folder}/{slug}-business-case.html`. One file, house style, seven sections in the template's order, a one-page summary panel first, the cell index as the last section.

**What you need before starting.** Stop and route back if any is missing:

1. The venture design record (the VDR) with Verify closed — `architect-custom` owns that; do not write a case for a design that has not passed.
2. The model data file `{slug}-model.yaml` and the two files the builder wrote from it: `{slug}-business-case-evidence.xlsx` and `{slug}-business-case-evidence-cells.md`. If the workbook is missing, run the builder first:
   ```bash
   python3 .claude/skills/ive-fin-sim-custom/scripts/generate_business_case_xlsx.py {venture-folder}/{slug}-model.yaml {venture-folder}
   ```
   If the model data file is missing, the fin-sim has not run its Stage 2 — go to `ive-fin-sim-custom`.

## Model routing

Per `.claude/skills/shared/ive-model-routing.md`: read and decide in-session; dispatch the writing of the HTML to a background helper run with `model: "opus"` and a self-contained prompt that carries the standard's path, the VDR path, the cell index path and the output path. Verify the file in-session before showing it.

## Step 1 — Read (silent)

1. The standard, section 3 — the seven sections and where each draws from.
2. The cell index — every name, cell and base value. This is the only source of numbers.
3. The VDR — the design, requirement by requirement, and the BFF evolution. Take the prose from here.
4. `WS1/position-register-standard.md` and the venture's position register, if present — for section 2 and the staffing in section 6.

## Step 2 — Write

Follow the standard's table for section 3. For each section: answer the template's questions in the template's order, in plain English, with no method vocabulary. Use the design record's reasoning, not new reasoning. Where the design record is silent on a template question (a second competitor, insurance), say what the design implies and mark the line as an assumption to confirm — do not invent a fact.

**Citing.** Every figure carries its cell name in a `<span class="cite">name</span>` immediately after the number. The name must exist in the cell index. A figure that has no cell must not appear. Bands are written as "£65 to £90, base £80" with the source from tab 1.

**The summary panel** (navy, first thing after the title): what the business is in one sentence; the interim price (`interim_price`); the cost floor (`cost_per_transaction`); the margin of safety and verdict (`margin_of_safety`, `verdict`); the cash needed in year one and under stress (`cash_needed`, `cash_needed_stress`); the binding input (`binding_input`). Nothing else.

**Section 1, objectives and funding**, draws the year-by-year line from tabs 15 to 18: units open, revenue and profit after tax by year (`forecast_revenue_year_N`, `forecast_profit_after_tax_year_N`), the year the venture turns a profit, closing cash and net assets at the end of the forecast, and the equity the roll-out needs by year (`in_forecast_equity_raised_year_N`, `forecast_funding_needed`).

**Section 7, back-up plan**, must give the reader three things from tab 10 and tab 14: how far price can fall before the margin reaches the floor; which input moves the margin most and what is being done to fix it; what cash the year-one plan needs if revenue is 10% lower than forecast, and where it comes from.

**The appendix** reproduces the cell index's Results, Line items, Forecast inputs and Inputs tables as HTML tables under the heading "Where each number lives".

**Worked example:** `reference/example-business-case.html` with its cell index `reference/example-cells.md` — a hypothetical venture (Spoke, mobile bicycle servicing) written to this standard and clean on both checkers. Match its shape; do not copy its prose.

**House style** — the HTML boilerplate and components in `CLAUDE.md` (DM Sans for UI, Lora for prose, the panel, the summary list, the inset block, tags). No developer vocabulary, no metaphor in any sentence the argument depends on.

## Step 3 — Check, then show

1. Cites: `python3 .claude/skills/ive-business-case-custom/scripts/check_business_case_cites.py <html> <cells.md>` — every cited name exists; every paragraph with a money or percentage figure carries a cite. Fix until clean.
2. House style: `python3 .scripts/check-house-style.py <html>` — fix until clean, except quotations and single definitions, which you judge.
3. Open the document and the workbook side by side. The document's header names the workbook; the numbers in the summary panel match the workbook at scenario 1.
4. Add the three files (model data file, workbook, document) to the run record per `WS1/run-record-standard.md`.

## What this skill does not do

- It does not compute. If a number is needed that the workbook lacks, the model data file is changed and the builder re-run; the document is then rewritten. Never patch a number in the document.
- It does not argue for the venture beyond what the design record supports. A failed margin is written as a failed margin.
- It does not produce `.docx`. Print to PDF from the browser is the interim route for readers who need a fixed format; whether to add a Word build is Tom's call (standard, section 5).

---

*Custom skill, protected from Dex updates. Added 22 September 2026 with `business-case-standard.md`. Related: `/ive-fin-sim-custom` (builds the workbook) · `/architect-custom` (the front door, whose Verify step calls this).*
