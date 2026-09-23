# Fin-sim model data file — specification (v1.2, 22 September 2026)

**v1.2 (22 September 2026, object-after 24 September 2026 17:00 BST):** an optional `book` block for a lending venture. `balance_per_transaction` is the balance one transaction carries (for a line priced per £1,000 of drawn balance a month, £1,000 by definition) and `capital_share_of_balance` is the share of that balance the venture funds with its own capital; the rest is deposit-funded. With the block present, tab 7 adds the book one unit carries and the capital held against it to the capital that earns the cost of capital (so the investment return per transaction is the capital charge on the balance lent); tab 15 carries the units running, the loan book, its yearly increase, the deposits and the capital by year; tab 17 shows the book's growth as investing cash and its deposit and capital funding as financing cash (cash-neutral by construction); tab 18 carries loans to customers as an asset, deposits as a liability and the capital held against the book as equity. Names added: `book_per_unit`, `book_capital_per_unit`, `book_at_scale`, `book_capital_at_scale`, `forecast_loan_book_year_N`, `forecast_deposits_year_N`, `forecast_book_capital_year_N`. Reason: the credit facility run (22 September 2026) prices per £1,000 drawn, and its largest cost is the return on the capital held against the balance — a v1.1 file had nowhere to carry it. A file without the block builds exactly as before; the test proves it.

**v1.1 (22 September 2026, object-after 24 September 2026 13:00 BST):** a head-office role's monthly cost, a running amount (unit or head office), a unit one-time cost and a head-office development cost may each be written as a TPM record, not only as a bare number. A banded line is registered on the Master tab like any other input, so the scenario switch, the one-at-a-time sensitivity and the worst corner move it; a bare number stays a constant on its own tab as in v1. Reason: the Traverse run carried its fixed-team and set-up-cost bands in the record, and a v1 file could not reproduce the record's worst corner. Every v1 file is still valid.

The financial simulation writes one data file per venture. The business-case workbook and the business-case document are both built from it, so the two never disagree. The file is plain text in YAML form, named `{slug}-model.yaml`, saved beside the venture's design record.

Example, complete and tested: `.claude/skills/ive-fin-sim-custom/scripts/example-model.yaml`.
Builder: `.claude/skills/ive-fin-sim-custom/scripts/generate_business_case_xlsx.py <model.yaml> [<out-dir>]`.
Test: `.claude/skills/ive-fin-sim-custom/scripts/test_generate_business_case_xlsx.py`.

## Two rules the file obeys

1. **Every load-bearing input is a TPM record**, not a bare number: `{value, low, high, unit, tier, source, adverse}`. `adverse` names the end of the band that lowers the margin of safety (`low` or `high`). The builder moves each input to its adverse end one at a time, sorts the results and names the binding input. If an "adverse" end turns out to raise the margin, the builder prints a warning: fix the label. Inputs that do not move the margin (tax rate, loan term) may be bare numbers.
2. **Steady state, one operating unit, per month.** Every quantity in `market`, `hr`, `assets`, `running` and `startup` describes one last-mile operating unit running at its designed scale, per month. Head office is described once for the whole venture. The year-one cash flow is derived from the steady state by the ramp — it is not entered separately.

## Blocks

### `venture`
`name` · `slug` (file-safe) · `one_line` · `currency` (ISO code, default GBP) · `date` · `unit_name` (what one operating unit is called) · `unit_description` · `design_record` (path to the venture design record the numbers come from).

### `market` — IFC step 1, bound the unit
| key | meaning |
|---|---|
| `total_reachable_population` | people, households or firms the venture can reach at scale (geographic reach × density) |
| `non_viable_share` | share of the reachable population screened out as not viable |
| `unit_population` | reachable population one operating unit serves. Number of units = reachable ÷ this, rounded up |
| `penetration_steady_state` | share of the unit's viable population that becomes customers |
| `transactions_per_customer_per_month` | frequency |

### `products` — list, up to four (the Start Up Loans sales sheet holds four)
`name` · `share_of_transactions` (shares sum to 1) · `price` (the interim price — the credible price from the value ceiling work, not the required price) · `cost_of_goods` per transaction.

### `hr` — IFC step 2, activities to headcount
- `available_hours_per_person_month` — productive hours, not contracted hours.
- `unit_roles` — map of role → `{monthly_cost}` (fully loaded: salary, on-costs, employer contributions).
- `unit_activities` — list of `{activity, role, minutes, driver, multiplier, note}`. `driver` is one of `per_transaction`, `per_customer_month`, `per_unit_month`. `multiplier` scales the driver quantity: 0.6 when the activity applies to 60% of transactions; 1.3 when there are 1.3 contacts per booking. Hours per month = minutes ÷ 60 × driver quantity × multiplier. Headcount per role = hours ÷ available hours, rounded up to whole people; the workbook shows utilisation so a role at 40% is visible.
- `head_office_roles` — list of `{role, count, monthly_cost}`. `monthly_cost` may be a TPM record (v1.1).

### `assets` — IFC step 2, depreciation
`unit` and `head_office` lists of `{name, cost, life_months, quantity}` or `{name, cost, life_months, quantity_driver: per_head}` (one per head of unit staff). Depreciation per month = cost × quantity ÷ life.

### `running` — IFC step 2, general running costs
`unit` list of `{name, driver, amount}` with `driver` one of `per_unit_month`, `per_transaction`, `per_customer_month`, `per_head`. `head_office` list of `{name, amount}` per month. `amount` may be a TPM record (v1.1).

### `startup` — IFC step 3, investment costs
`unit_one_time` list of `{name, cost}` (`cost` may be a TPM record, v1.1) · `working_capital_months` (working capital = months × (cost of goods + staff + running) per month) · `head_office_development` list of `{name, cost}` (`cost` may be a TPM record, v1.1) · `investment_period_months` (start-up and development are spread over this period as a monthly charge).

### `finance`
`cost_of_capital_annual` · `tax_rate` (applied to the investment return) · `head_office_target_ebit_margin` (head-office target profit = head-office cost × this) · `target_margin` (0.25 — the registry's per-requirement gate).

### `book` — optional, a lending venture (v1.2)
`balance_per_transaction` (the balance outstanding that one transaction carries; a TPM record) · `capital_share_of_balance` (the share of that balance funded by the venture's own capital, a TPM record; the remainder is funded by deposits or another liability). Present only when the venture lends: the capital held against the book earns the cost of capital on tab 7, and the book, its deposits and its capital appear on tabs 15, 17 and 18. The book at any year end = balance per transaction × transactions per unit × units running (units open at the start of the year at steady state, the year's new cohort at its month-twelve share).

### `cashflow` — the Start Up Loans twelve-month forecast
`year1_units` (operating units open in year one) · `year1_head_office_share` (the share of the at-scale head-office staff and running cost carried in year one — the launch head office; default 1.0) · `ramp_share_of_steady_state` (twelve numbers, each month's volume as a share of steady state) · `opening_balance` · `loan_amount` · `loan_rate_annual` · `loan_term_months` (repayment is a level monthly instalment) · `other_equity` (month one) · `stress_revenue_reduction` (0.10 — the template's test).

Year-one unit staff are costed in full from month one (a unit opens with its team). Head-office staff and running costs are charged at `year1_head_office_share`; head-office development and capital are paid in month one in full. Running costs with `per_unit_month` and `per_head` drivers are charged in full; those with `per_transaction` and `per_customer_month` drivers follow the ramp. Start-up costs, capital assets and head-office development are paid in month one.

### `forecast` — the three forecast financial statements, by year (tabs 15 to 18)
`years` (default 5) · `units_open_by_year` (operating units open at each year end; the first value must equal `cashflow.year1_units`) · `head_office_share_by_year` (the first value must equal `cashflow.year1_head_office_share`) · `equity_raised_by_year` (the first value must equal `cashflow.other_equity`). If the block is absent the builder forecasts five years with year one repeated and no further equity.

Rules the forecast keeps, stated on the tabs: a cohort of units opens at the start of its year and follows the year-one ramp; units already open run at steady state; start-up costs and head-office development are charged to profit when paid; an asset is replaced in the year that holds the month after its life ends, and depreciation is capped at what remains to be written off; the loan is the level monthly instalment on tab 14, split into principal and interest by year; tax is charged on profit after losses brought forward and paid the year after it is charged; a cash business — no debtors, creditors or stock; later funding is equity. Year one of the forecast closes at the same cash balance as month twelve on tab 14, and the Check tab proves it.

## What the builder computes (so the file need not)

Number of units · customer base · transactions · revenue and cost of goods by product · hours, headcount and cost by role · depreciation · running cost · working capital · start-up charge · investment return · tax · head-office total and its allocation per unit · whole cost per unit and per transaction · interim price · margin of safety = (price − cost) ÷ cost · verdict against the registry gates (25% pass, 15% borderline) · required price = cost × (1 + target) · required price by product (same uplift) · one-at-a-time sensitivity and the binding input · worst-corner margin · unit and venture profit and loss · year-one sales, cash flow and the stress test · the roll-out, the loan schedule and asset replacement by year · the forecast profit and loss, cash flow and balance sheet by year · the Check tab.

## Where the numbers come from

| block | source in the design record |
|---|---|
| `market` | PCO and R2 (the key market characteristic and the target customer); R3 (the operating unit and its population) |
| `products.price` | R2 value ceiling; R6 (what people pay for) |
| `products.cost_of_goods`, `hr`, `assets`, `running` | R1 cost floor — the activity-based cost build |
| `startup` | R3 (the scaling architecture) and the launch plan |
| `finance` | the finance standard; cost of capital from the funding route |
| `cashflow` | the launch plan's ramp; the funding route |
| `forecast` | the scaling architecture (R3) for units by year; the funding route for equity by year |
