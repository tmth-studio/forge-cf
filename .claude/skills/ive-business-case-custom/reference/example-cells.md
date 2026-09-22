# Cell index — Spoke business-case evidence workbook

Workbook: `spoke-business-case-evidence.xlsx` · built from the model data file on 2026-09-22 · currency GBP.

Cite a figure in the business case as its name in this table, for example `margin_of_safety` or `cost_per_transaction`. Every name is also a defined name inside the workbook. Values are at the base scenario; the workbook recomputes them live.

## Results

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `scenario` | '1 Master'!$B$4 | 1 | Scenario switch: 1 base, 2 all-low, 3 all-high |
| `tam` | '2 Customers'!$B$5 | 1,292,000 | Total addressable market, households or customers |
| `units` | '2 Customers'!$B$6 | 34 | Number of operating units at scale |
| `customers_per_unit` | '2 Customers'!$B$9 | 2,280 | Customer base per operating unit at steady state |
| `transactions_per_unit` | '2 Customers'!$B$10 | 456 | Transactions per operating unit per month at steady state |
| `transactions_venture` | '2 Customers'!$B$11 | 15,504 | Transactions across the venture per month at steady state |
| `revenue_per_unit` | '2 Customers'!$E$16 | 26,448 | Revenue per operating unit per month at interim prices |
| `cogs_per_unit` | '2 Customers'!$G$16 | 2,827 | Cost of goods per operating unit per month |
| `headcount_per_unit` | '3 HR'!$D$15 | 4 | Headcount per operating unit |
| `hr_cost_per_unit` | '3 HR'!$F$15 | 12,200 | Staff cost per operating unit per month |
| `ho_staff_cost` | '3 HR'!$D$22 | 14,500 | Head-office staff cost per month |
| `capital_per_unit` | '4 Depreciation'!$F$8 | 35,600 | Capital assets per operating unit |
| `depreciation_per_unit` | '4 Depreciation'!$G$8 | 700 | Depreciation per operating unit per month |
| `capital_head_office` | '4 Depreciation'!$F$12 | 60,000 | Head-office capital assets |
| `depreciation_head_office` | '4 Depreciation'!$G$12 | 1,667 | Head-office depreciation per month |
| `running_per_unit` | '5 Running'!$E$10 | 1,474 | General running cost per operating unit per month |
| `running_head_office` | '5 Running'!$E$18 | 8,700 | Head-office running cost per month |
| `startup_per_unit` | '6 Start-up'!$B$10 | 45,503 | Start-up cost per operating unit (one-time plus working capital) |
| `startup_charge_per_unit` | '6 Start-up'!$B$12 | 758 | Start-up charge per operating unit per month |
| `development_head_office` | '6 Start-up'!$B$17 | 20,000 | Head-office development cost, one-time |
| `development_charge_per_month` | '6 Start-up'!$B$18 | 333 | Head-office development charge per month |
| `returns_per_unit` | '7 Returns'!$B$6 | 811 | Investment return required per operating unit per month |
| `returns_head_office` | '7 Returns'!$B$8 | 800 | Investment return required at head office per month |
| `tax_per_unit` | '8 Tax'!$B$5 | 203 | Tax per operating unit per month |
| `tax_head_office` | '8 Tax'!$B$6 | 200 | Tax at head office per month |
| `unit_own_cost` | '9 Unit costs'!$B$12 | 18,974 | Operating unit's own costs per month, before head office |
| `ho_costs` | '9 Unit costs'!$B$13 | 26,200 | Head-office costs per month |
| `ho_total` | '9 Unit costs'!$B$15 | 28,820 | Head-office costs plus target profit per month |
| `ho_allocated_per_unit` | '9 Unit costs'!$B$16 | 848 | Head office allocated per operating unit per month |
| `whole_cost_per_unit` | '9 Unit costs'!$B$17 | 19,821 | Whole cost per operating unit per month |
| `cost_per_transaction` | '9 Unit costs'!$B$18 | 43.47 | Whole cost per transaction — the cost floor |
| `margin_of_safety` | '10 Pricing'!$B$6 | 33.4% | Margin of safety at the interim price, base scenario |
| `interim_price` | '10 Pricing'!$B$5 | 58.00 | Interim price per transaction |
| `verdict` | '10 Pricing'!$B$8 | PASS | Verdict on the margin of safety: PASS, BORDERLINE or FAIL |
| `required_price` | '10 Pricing'!$B$9 | 54.34 | Required price per transaction at the target margin of safety |
| `price_uplift_to_target` | '10 Pricing'!$B$10 | 93.7% | Price uplift needed to reach the target margin of safety (required ÷ interim) |
| `margin_from_failure` | '10 Pricing'!$B$11 | 18.4% | Margin of safety less the 15% floor, in percentage points |
| `price_fall_to_floor` | '10 Pricing'!$B$12 | 8.01 | Price fall per transaction that takes the margin of safety to the 15% floor |
| `required_price_product_1` | '10 Pricing'!$C$15 | 74.94 | Required price at the target margin of safety — Full service |
| `required_price_product_2` | '10 Pricing'!$C$16 | 23.42 | Required price at the target margin of safety — Safety check |
| `binding_input` | '10 Pricing'!$B$33 | Full service — price | The input whose adverse end lowers the margin of safety most |
| `margin_of_safety_worst_corner` | '10 Pricing'!$B$34 | -43.2% | Margin of safety with every banded input at its adverse end |
| `unit_surplus` | '11 Unit P&L'!$B$17 | 6,627 | Surplus per operating unit per month at the interim price |
| `unit_surplus_at_required` | '11 Unit P&L'!$C$17 | 4,955 | Surplus per operating unit per month at the required price |
| `venture_surplus_per_month` | '12 Venture P&L'!$D$20 | 225,304 | Venture surplus per month at scale, interim price |
| `venture_surplus_per_year` | '12 Venture P&L'!$D$21 | 2,703,643 | Venture surplus per year at scale, interim price |
| `venture_revenue_per_month` | '12 Venture P&L'!$D$5 | 899,232 | Venture revenue per month at scale |
| `year1_sales` | '13 Sales'!$N$16 | 207,617 | Sales in year one, the units open in year one |
| `year1_volume` | '13 Sales'!$N$18 | 3,580 | Transactions in year one |
| `loan_repayment_per_month` | '14 Cash flow'!$B$7 | 483 | Monthly loan repayment |
| `lowest_closing_balance` | '14 Cash flow'!$B$29 | -115,461 | Lowest closing cash balance in year one |
| `lowest_closing_balance_stress` | '14 Cash flow'!$B$30 | -129,675 | Lowest closing cash balance in year one under the revenue stress test |
| `closing_balance_month12` | '14 Cash flow'!$B$31 | -108,913 | Closing cash balance at the end of year one |
| `cash_needed` | '14 Cash flow'!$B$32 | 115,461 | Extra cash needed to keep the balance at or above zero |
| `cash_needed_stress` | '14 Cash flow'!$B$33 | 129,675 | Extra cash needed under the stress test |
| `forecast_revenue_year_1` | '16 Forecast P&L'!$B$5 | 207,617 | Forecast revenue, year 1 |
| `forecast_operating_profit_year_1` | '16 Forecast P&L'!$B$15 | -120,913 | Forecast operating profit, year 1 |
| `forecast_profit_after_tax_year_1` | '16 Forecast P&L'!$B$22 | -122,293 | Forecast profit after tax, year 1 |
| `forecast_revenue_year_2` | '16 Forecast P&L'!$C$5 | 524,993 | Forecast revenue, year 2 |
| `forecast_operating_profit_year_2` | '16 Forecast P&L'!$C$15 | -73,476 | Forecast operating profit, year 2 |
| `forecast_profit_after_tax_year_2` | '16 Forecast P&L'!$C$22 | -74,584 | Forecast profit after tax, year 2 |
| `forecast_revenue_year_3` | '16 Forecast P&L'!$D$5 | 1,257,602 | Forecast revenue, year 3 |
| `forecast_operating_profit_year_3` | '16 Forecast P&L'!$D$15 | -68,666 | Forecast operating profit, year 3 |
| `forecast_profit_after_tax_year_3` | '16 Forecast P&L'!$D$22 | -69,484 | Forecast profit after tax, year 3 |
| `forecast_revenue_year_4` | '16 Forecast P&L'!$E$5 | 2,624,964 | Forecast revenue, year 4 |
| `forecast_operating_profit_year_4` | '16 Forecast P&L'!$E$15 | 269,418 | Forecast operating profit, year 4 |
| `forecast_profit_after_tax_year_4` | '16 Forecast P&L'!$E$22 | 268,271 | Forecast profit after tax, year 4 |
| `forecast_revenue_year_5` | '16 Forecast P&L'!$F$5 | 4,419,461 | Forecast revenue, year 5 |
| `forecast_operating_profit_year_5` | '16 Forecast P&L'!$F$15 | 826,808 | Forecast operating profit, year 5 |
| `forecast_profit_after_tax_year_5` | '16 Forecast P&L'!$F$22 | 619,968 | Forecast profit after tax, year 5 |
| `forecast_revenue_total` | '16 Forecast P&L'!$G$5 | 9,034,637 | Forecast revenue over years one to 5 |
| `forecast_operating_profit_total` | '16 Forecast P&L'!$G$15 | 833,170 | Forecast operating profit over years one to 5 |
| `forecast_profit_after_tax_total` | '16 Forecast P&L'!$G$22 | 621,878 | Forecast profit after tax over years one to 5 |
| `forecast_closing_cash_year_1` | '17 Forecast cash flow'!$B$19 | -108,913 | Forecast closing cash, end of year 1 |
| `forecast_closing_cash_year_2` | '17 Forecast cash flow'!$C$19 | 13,011 | Forecast closing cash, end of year 2 |
| `forecast_closing_cash_year_3` | '17 Forecast cash flow'!$D$19 | 92,145 | Forecast closing cash, end of year 3 |
| `forecast_closing_cash_year_4` | '17 Forecast cash flow'!$E$19 | 214,162 | Forecast closing cash, end of year 4 |
| `forecast_closing_cash_year_5` | '17 Forecast cash flow'!$F$19 | 962,934 | Forecast closing cash, end of year 5 |
| `forecast_lowest_closing_cash` | '17 Forecast cash flow'!$B$21 | -108,913 | Lowest year-end cash balance across the forecast |
| `forecast_funding_needed` | '17 Forecast cash flow'!$B$22 | 108,913 | Extra funding needed to keep year-end cash at or above zero across the forecast |
| `forecast_net_assets_year_1` | '18 Forecast balance sheet'!$B$11 | -62,293 | Forecast net assets, end of year 1 |
| `forecast_loan_outstanding_year_1` | '18 Forecast balance sheet'!$B$8 | 20,580 | Loan outstanding, end of year 1 |
| `forecast_net_assets_year_2` | '18 Forecast balance sheet'!$C$11 | 63,123 | Forecast net assets, end of year 2 |
| `forecast_loan_outstanding_year_2` | '18 Forecast balance sheet'!$C$8 | 15,887 | Loan outstanding, end of year 2 |
| `forecast_net_assets_year_3` | '18 Forecast balance sheet'!$D$11 | 193,639 | Forecast net assets, end of year 3 |
| `forecast_loan_outstanding_year_3` | '18 Forecast balance sheet'!$D$8 | 10,905 | Loan outstanding, end of year 3 |
| `forecast_net_assets_year_4` | '18 Forecast balance sheet'!$E$11 | 461,910 | Forecast net assets, end of year 4 |
| `forecast_loan_outstanding_year_4` | '18 Forecast balance sheet'!$E$8 | 5,616 | Loan outstanding, end of year 4 |
| `forecast_net_assets_year_5` | '18 Forecast balance sheet'!$F$11 | 1,081,878 | Forecast net assets, end of year 5 |
| `forecast_loan_outstanding_year_5` | '18 Forecast balance sheet'!$F$8 | 0 | Loan outstanding, end of year 5 |
| `all_checks` | '19 Check'!$D$17 | ALL CHECKS PASS | ALL CHECKS PASS when every check row passes |

## Line items (tabs 3 to 6 — the amounts entered for each asset, running cost, start-up and development line)

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `line_ho_role_general_manager` | '3 HR'!$D$19 | 6,500 | Staff cost per month, head office — General manager × 1 |
| `line_ho_role_marketing_lead` | '3 HR'!$D$20 | 4,500 | Staff cost per month, head office — Marketing lead × 1 |
| `line_ho_role_finance_and_admin` | '3 HR'!$D$21 | 3,500 | Staff cost per month, head office — Finance and admin × 1 |
| `line_asset_service_van` | '4 Depreciation'!$B$5 | 28,000 | Asset cost, operating unit — Service van |
| `line_asset_tool_set` | '4 Depreciation'!$B$6 | 1,500 | Asset cost, operating unit — Tool set |
| `line_asset_booking_tablet` | '4 Depreciation'!$B$7 | 400 | Asset cost, operating unit — Booking tablet |
| `line_ho_asset_booking_platform_build` | '4 Depreciation'!$B$11 | 60,000 | Asset cost, head office — Booking platform build |
| `line_running_van_fuel_and_maintenance` | '5 Running'!$C$5 | 550 | Running cost amount, operating unit (per_unit_month) — Van fuel and maintenance |
| `line_running_van_insurance_and_tax` | '5 Running'!$C$6 | 220 | Running cost amount, operating unit (per_unit_month) — Van insurance and tax |
| `line_running_card_payment_fees` | '5 Running'!$C$7 | 0.90 | Running cost amount, operating unit (per_transaction) — Card payment fees |
| `line_running_customer_reminders_and_messaging` | '5 Running'!$C$8 | 0.05 | Running cost amount, operating unit (per_customer_month) — Customer reminders and messaging |
| `line_running_uniform_and_phone_per_head` | '5 Running'!$C$9 | 45 | Running cost amount, operating unit (per_head) — Uniform and phone per head |
| `line_ho_running_office_and_software` | '5 Running'!$C$15 | 1,800 | Running cost per month, head office — Office and software |
| `line_ho_running_marketing_spend` | '5 Running'!$C$16 | 6,000 | Running cost per month, head office — Marketing spend |
| `line_ho_running_professional_fees_and_insurance` | '5 Running'!$C$17 | 900 | Running cost per month, head office — Professional fees and insurance |
| `line_startup_van_fit_out_and_livery` | '6 Start-up'!$B$5 | 4,000 | Start-up cost, operating unit, one-time — Van fit-out and livery |
| `line_startup_recruitment_and_training` | '6 Start-up'!$B$6 | 3,500 | Start-up cost, operating unit, one-time — Recruitment and training |
| `line_startup_launch_marketing_in_the_borough` | '6 Start-up'!$B$7 | 5,000 | Start-up cost, operating unit, one-time — Launch marketing in the borough |
| `line_development_brand_and_website` | '6 Start-up'!$B$15 | 15,000 | Development cost, head office, one-time — Brand and website |
| `line_development_company_set_up_and_legal` | '6 Start-up'!$B$16 | 5,000 | Development cost, head office, one-time — Company set-up and legal |

## Forecast inputs (tab 15 — units open, head-office share and equity raised, by year)

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `in_forecast_units_open_year_1` | '15 Roll-out'!$B$5 | 1 | Operating units open at the end of year 1 |
| `in_forecast_head_office_share_year_1` | '15 Roll-out'!$B$8 | 30.0% | Share of the at-scale head office staffed and run in year 1 |
| `in_forecast_equity_raised_year_1` | '15 Roll-out'!$B$9 | 60,000 | Equity raised in year 1 |
| `in_forecast_units_open_year_2` | '15 Roll-out'!$C$5 | 2 | Operating units open at the end of year 2 |
| `in_forecast_head_office_share_year_2` | '15 Roll-out'!$C$8 | 60.0% | Share of the at-scale head office staffed and run in year 2 |
| `in_forecast_equity_raised_year_2` | '15 Roll-out'!$C$9 | 200,000 | Equity raised in year 2 |
| `in_forecast_units_open_year_3` | '15 Roll-out'!$D$5 | 5 | Operating units open at the end of year 3 |
| `in_forecast_head_office_share_year_3` | '15 Roll-out'!$D$8 | 100.0% | Share of the at-scale head office staffed and run in year 3 |
| `in_forecast_equity_raised_year_3` | '15 Roll-out'!$D$9 | 200,000 | Equity raised in year 3 |
| `in_forecast_units_open_year_4` | '15 Roll-out'!$E$5 | 10 | Operating units open at the end of year 4 |
| `in_forecast_head_office_share_year_4` | '15 Roll-out'!$E$8 | 100.0% | Share of the at-scale head office staffed and run in year 4 |
| `in_forecast_equity_raised_year_4` | '15 Roll-out'!$E$9 | 0 | Equity raised in year 4 |
| `in_forecast_units_open_year_5` | '15 Roll-out'!$F$5 | 16 | Operating units open at the end of year 5 |
| `in_forecast_head_office_share_year_5` | '15 Roll-out'!$F$8 | 100.0% | Share of the at-scale head office staffed and run in year 5 |
| `in_forecast_equity_raised_year_5` | '15 Roll-out'!$F$9 | 0 | Equity raised in year 5 |

## Inputs (tab 1, Master Control)

| Name | Cell | Base | Low | High | Tier | Source |
|---|---|---|---|---|---|---|
| `in_market_total_reachable_population` | '1 Master'!$B$7 | 3,400,000 | 3,200,000 | 3,600,000 | 2 | ONS household estimates, Greater London 2024 |
| `in_market_non_viable_share` | '1 Master'!$B$8 | 62.0% | 55.0% | 68.0% | 3 | Active Lives survey 2024 — households with no adult who cycles |
| `in_market_unit_population` | '1 Master'!$B$9 | 100,000 | 90,000 | 110,000 | 4 | assumed — one borough per team |
| `in_market_penetration_steady_state` | '1 Master'!$B$10 | 6.0% | 4.5% | 7.5% | 4 | assumed — direct-to-household service penetration after 24 months |
| `in_market_transactions_per_customer_per_month` | '1 Master'!$B$11 | 0.2 | 0.15 | 0.25 | 3 | two to three services a year per active customer, bicycle trade norm |
| `in_product_0_share` | '1 Master'!$B$12 | 0.6 | 0.6 | 0.6 |  |  |
| `in_product_0_price` | '1 Master'!$B$13 | 80 | 65 | 90 | 3 | Halfords and independent price lists, London 2026 |
| `in_product_0_cogs` | '1 Master'!$B$14 | 9 | 7 | 12 | 3 | parts and consumables per service, trade supplier list |
| `in_product_1_share` | '1 Master'!$B$15 | 0.4 | 0.4 | 0.4 |  |  |
| `in_product_1_price` | '1 Master'!$B$16 | 25 | 20 | 30 | 3 | competitor price lists |
| `in_product_1_cogs` | '1 Master'!$B$17 | 2 | 1 | 3 | 4 | assumed — lubricants and small parts |
| `in_hr_available_hours` | '1 Master'!$B$18 | 140 | 140 | 140 |  |  |
| `in_role_mechanic_monthly_cost` | '1 Master'!$B$19 | 3,200 | 3,000 | 3,600 | 2 | ONS ASHE 2025, vehicle technicians, London, plus 20% on-costs |
| `in_role_booking_coordinator_monthly_cost` | '1 Master'!$B$20 | 2,600 | 2,400 | 2,900 | 2 | ONS ASHE 2025, customer service, London, plus on-costs |
| `in_startup_working_capital_months` | '1 Master'!$B$21 | 2 | 2 | 2 |  |  |
| `in_startup_investment_period_months` | '1 Master'!$B$22 | 60 | 60 | 60 |  |  |
| `in_finance_cost_of_capital` | '1 Master'!$B$23 | 12.0% | 10.0% | 15.0% | 3 | British Business Bank Start Up Loans 6% plus equity return, blended |
| `in_finance_tax_rate` | '1 Master'!$B$24 | 25.0% | 25.0% | 25.0% |  |  |
| `in_finance_ho_target_ebit` | '1 Master'!$B$25 | 10.0% | 10.0% | 10.0% |  |  |
| `in_finance_target_margin` | '1 Master'!$B$26 | 25.0% | 25.0% | 25.0% |  |  |
| `in_cashflow_year1_units` | '1 Master'!$B$27 | 1 | 1 | 1 |  |  |
| `in_cashflow_year1_head_office_share` | '1 Master'!$B$28 | 30.0% | 30.0% | 30.0% |  |  |
| `in_cashflow_opening_balance` | '1 Master'!$B$29 | 0 | 0 | 0 |  |  |
| `in_cashflow_loan_amount` | '1 Master'!$B$30 | 25,000 | 25,000 | 25,000 |  |  |
| `in_cashflow_loan_rate_annual` | '1 Master'!$B$31 | 6.0% | 6.0% | 6.0% |  |  |
| `in_cashflow_loan_term_months` | '1 Master'!$B$32 | 60 | 60 | 60 |  |  |
| `in_cashflow_other_equity` | '1 Master'!$B$33 | 60,000 | 60,000 | 60,000 |  |  |
| `in_cashflow_stress_revenue_reduction` | '1 Master'!$B$34 | 10.0% | 10.0% | 10.0% |  |  |

## Sensitivity (one input at a time to its adverse end, worst first)

| Input | End | Margin of safety | Change |
|---|---|---|---|
| Full service — price | low | 12.7% | -20.7% |
| Share of reachable population that is not viable | high | 15.6% | -17.8% |
| Reachable population one operating unit serves | low | 22.8% | -10.6% |
| Mechanic — monthly cost per person | high | 25.4% | -8.0% |
| Full service — cost of goods per transaction | high | 27.8% | -5.6% |
| Transactions per customer per month | low | 28.4% | -5.0% |
| Steady-state penetration of the unit's viable population | low | 28.7% | -4.8% |
| Safety check — price | low | 28.8% | -4.6% |
| Booking coordinator — monthly cost per person | high | 31.3% | -2.1% |
| Cost of capital (annual) | high | 31.7% | -1.7% |
| Safety check — cost of goods per transaction | high | 32.1% | -1.3% |
| Reachable population (whole venture) | low | 33.1% | -0.4% |

Binding input: **Full service — price**. Margin of safety at the worst corner (every input adverse): **-43.2%**. Verdict at base: **PASS** (33.4% against a 25% gate).
