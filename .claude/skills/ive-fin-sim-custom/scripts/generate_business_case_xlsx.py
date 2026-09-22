#!/usr/bin/env python3
"""Build the business-case evidence workbook from a fin-sim model data file.

Usage:
    python3 generate_business_case_xlsx.py <model.yaml> [<out-dir>]

Reads the model data file (spec: .claude/skills/shared/finsim-model-spec.md) and writes:

    <out-dir>/<slug>-business-case-evidence.xlsx        the workbook, live formulas throughout
    <out-dir>/<slug>-business-case-evidence-cells.md    the cell index the document cites from

The workbook follows the IFC bottom-up method (Simanis, "Running the Right Numbers",
Part II) — twelve tabs from Master Control to the venture whole-cost P&L — then the two
sheets the GOV.UK / Start Up Loans business-plan template asks for (sales assumptions and a
twelve-month cash-flow forecast with a revenue stress test), then the three forecast financial
statements by year (profit and loss, cash flow, balance sheet, driven by a roll-out tab), then a
Check tab whose cells recompute the headline figures a second way and reconcile the forecast to
the twelve-month cash flow. Standard: WS1/business-case-standard.md.

Every input sits on tab 1 with its band, tier and source. Every other number is a formula.
Nothing is pasted as a value except the one-at-a-time sensitivity table on the Pricing tab,
which this script computes from the same inputs and labels as such.

Requires: pyyaml, openpyxl.
"""

import math
import os
import sys

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName


def line_name(prefix, text):
    """A defined name for a line item: letters, digits and underscores only."""
    import re as _re
    return prefix + "_" + _re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")

FMOS_PASS, FMOS_BORDER = 0.25, 0.15

INPUT = Font(color="1F4FA8")            # inputs in blue, the modelling convention
BOLD = Font(bold=True)
HEAD = Font(bold=True, color="FFFFFF")
HEADFILL = PatternFill("solid", fgColor="0F2744")
NOTE = Font(italic=True, color="718096")
MONEY = '#,##0;[Red]-#,##0'
MONEY2 = '#,##0.00;[Red]-#,##0.00'
PCT = '0.0%'
NUM = '#,##0'


# ----------------------------------------------------------------------------------------------
# the model, computed in Python — used for the sensitivity table, the cell index and the tests
# ----------------------------------------------------------------------------------------------

def band(x):
    """Normalise an input to {value, low, high, tier, source, adverse}."""
    if isinstance(x, dict):
        v = float(x["value"])
        return {"value": v, "low": float(x.get("low", v)), "high": float(x.get("high", v)),
                "unit": x.get("unit", ""), "tier": x.get("tier", ""), "source": x.get("source", ""),
                "adverse": x.get("adverse", "")}
    v = float(x)
    return {"value": v, "low": v, "high": v, "unit": "", "tier": "", "source": "", "adverse": ""}


def collect_inputs(m):
    """Every banded scalar in the model, keyed by path, in Master Control order."""
    inp = {}
    for k, v in m["market"].items():
        inp[f"market.{k}"] = band(v)
    for i, p in enumerate(m["products"]):
        inp[f"product.{i}.share"] = band(p["share_of_transactions"])
        inp[f"product.{i}.price"] = band(p["price"])
        inp[f"product.{i}.cogs"] = band(p["cost_of_goods"])
    inp["hr.available_hours"] = band(m["hr"]["available_hours_per_person_month"])
    for r, d in m["hr"]["unit_roles"].items():
        inp[f"role.{r}.monthly_cost"] = band(d["monthly_cost"])
    inp["startup.working_capital_months"] = band(m["startup"]["working_capital_months"])
    inp["startup.investment_period_months"] = band(m["startup"]["investment_period_months"])
    f = m["finance"]
    inp["finance.cost_of_capital"] = band(f["cost_of_capital_annual"])
    inp["finance.tax_rate"] = band(f["tax_rate"])
    inp["finance.ho_target_ebit"] = band(f["head_office_target_ebit_margin"])
    inp["finance.target_margin"] = band(f["target_margin"])
    c = m["cashflow"]
    for k in ("year1_units", "year1_head_office_share", "opening_balance", "loan_amount", "loan_rate_annual",
              "loan_term_months", "other_equity", "stress_revenue_reduction"):
        inp[f"cashflow.{k}"] = band(c.get(k, 1.0 if k == "year1_head_office_share" else c[k]))
    for k in ("finance.tax_rate", "finance.ho_target_ebit", "finance.target_margin", "cashflow.year1_head_office_share",
              "cashflow.loan_rate_annual", "cashflow.stress_revenue_reduction"):
        inp[k]["unit"] = inp[k]["unit"] or "share"
    return inp


LABELS = {
    "market.total_reachable_population": "Reachable population (whole venture)",
    "market.non_viable_share": "Share of reachable population that is not viable",
    "market.unit_population": "Reachable population one operating unit serves",
    "market.penetration_steady_state": "Steady-state penetration of the unit's viable population",
    "market.transactions_per_customer_per_month": "Transactions per customer per month",
    "hr.available_hours": "Available hours per person per month",
    "startup.working_capital_months": "Start-up working capital (months of unit running cost)",
    "startup.investment_period_months": "Investment recovery period (months)",
    "finance.cost_of_capital": "Cost of capital (annual)",
    "finance.tax_rate": "Tax rate on investment returns",
    "finance.ho_target_ebit": "Head-office target profit (share of head-office cost)",
    "finance.target_margin": "Target margin of safety",
    "cashflow.year1_units": "Operating units open in year one",
    "cashflow.year1_head_office_share": "Share of the at-scale head office staffed and run in year one",
    "cashflow.opening_balance": "Opening cash balance",
    "cashflow.loan_amount": "Loan amount",
    "cashflow.loan_rate_annual": "Loan interest rate (annual)",
    "cashflow.loan_term_months": "Loan term (months)",
    "cashflow.other_equity": "Other equity or grants in month one",
    "cashflow.stress_revenue_reduction": "Stress test: reduction in revenue",
}


def label_for(key, m):
    if key in LABELS:
        return LABELS[key]
    parts = key.split(".")
    if parts[0] == "product":
        name = m["products"][int(parts[1])]["name"]
        return {"share": f"{name} — share of transactions", "price": f"{name} — price",
                "cogs": f"{name} — cost of goods per transaction"}[parts[2]]
    if parts[0] == "role":
        return f"{parts[1]} — monthly cost per person"
    return key


def compute(m, values):
    """Steady-state monthly model for one operating unit and the venture, from a value map."""
    g = lambda k: values[k]  # noqa: E731
    r = {}
    r["tam"] = g("market.total_reachable_population") * (1 - g("market.non_viable_share"))
    r["units"] = math.ceil(g("market.total_reachable_population") / g("market.unit_population") - 1e-9)
    r["unit_tam"] = g("market.unit_population") * (1 - g("market.non_viable_share"))
    r["customers"] = r["unit_tam"] * g("market.penetration_steady_state")
    r["trans"] = r["customers"] * g("market.transactions_per_customer_per_month")
    r["revenue"] = r["cogs"] = 0.0
    r["products"] = []
    for i, p in enumerate(m["products"]):
        t = r["trans"] * g(f"product.{i}.share")
        rev, cg = t * g(f"product.{i}.price"), t * g(f"product.{i}.cogs")
        r["products"].append({"name": p["name"], "trans": t, "revenue": rev, "cogs": cg})
        r["revenue"] += rev
        r["cogs"] += cg
    qty = {"per_transaction": r["trans"], "per_customer_month": r["customers"], "per_unit_month": 1.0}
    hours = {}
    for a in m["hr"]["unit_activities"]:
        hours[a["role"]] = hours.get(a["role"], 0.0) + a["minutes"] / 60 * qty[a["driver"]] * a.get("multiplier", 1)
    r["roles"] = {}
    r["hr_unit"] = 0.0
    r["headcount"] = 0
    for role in m["hr"]["unit_roles"]:
        h = hours.get(role, 0.0)
        n = math.ceil(h / g("hr.available_hours") - 1e-9)
        cost = n * g(f"role.{role}.monthly_cost")
        r["roles"][role] = {"hours": h, "headcount": n, "cost": cost}
        r["hr_unit"] += cost
        r["headcount"] += n
    r["ho_hr"] = sum(x["count"] * x["monthly_cost"] for x in m["hr"]["head_office_roles"])
    r["dep_unit"] = r["capital_unit"] = 0.0
    for a in m["assets"]["unit"]:
        q = r["headcount"] if a.get("quantity_driver") == "per_head" else a.get("quantity", 1)
        r["dep_unit"] += a["cost"] * q / a["life_months"]
        r["capital_unit"] += a["cost"] * q
    r["dep_ho"] = sum(a["cost"] * a.get("quantity", 1) / a["life_months"] for a in m["assets"]["head_office"])
    r["capital_ho"] = sum(a["cost"] * a.get("quantity", 1) for a in m["assets"]["head_office"])
    rq = {"per_unit_month": 1.0, "per_transaction": r["trans"], "per_customer_month": r["customers"],
          "per_head": float(r["headcount"])}
    r["running_unit"] = sum(x["amount"] * rq[x["driver"]] for x in m["running"]["unit"])
    r["running_unit_fixed"] = sum(x["amount"] * rq[x["driver"]] for x in m["running"]["unit"]
                                  if x["driver"] in ("per_unit_month", "per_head"))
    r["running_unit_variable"] = r["running_unit"] - r["running_unit_fixed"]
    r["running_ho"] = sum(x["amount"] for x in m["running"]["head_office"])
    r["one_time_unit"] = sum(x["cost"] for x in m["startup"]["unit_one_time"])
    r["wc_unit"] = g("startup.working_capital_months") * (r["cogs"] + r["hr_unit"] + r["running_unit"])
    r["startup_unit"] = r["one_time_unit"] + r["wc_unit"]
    r["startup_unit_monthly"] = r["startup_unit"] / g("startup.investment_period_months")
    r["dev_ho"] = sum(x["cost"] for x in m["startup"]["head_office_development"])
    r["dev_ho_monthly"] = r["dev_ho"] / g("startup.investment_period_months")
    r["returns_unit"] = (r["startup_unit"] + r["capital_unit"]) * g("finance.cost_of_capital") / 12
    r["returns_ho"] = (r["dev_ho"] + r["capital_ho"]) * g("finance.cost_of_capital") / 12
    r["tax_unit"] = r["returns_unit"] * g("finance.tax_rate")
    r["tax_ho"] = r["returns_ho"] * g("finance.tax_rate")
    r["ho_costs"] = r["ho_hr"] + r["running_ho"] + r["dep_ho"] + r["dev_ho_monthly"] + r["returns_ho"] + r["tax_ho"]
    r["ho_profit"] = r["ho_costs"] * g("finance.ho_target_ebit")
    r["ho_total"] = r["ho_costs"] + r["ho_profit"]
    r["ho_alloc"] = r["ho_total"] / r["units"]
    r["unit_own_cost"] = (r["cogs"] + r["hr_unit"] + r["dep_unit"] + r["running_unit"]
                          + r["startup_unit_monthly"] + r["returns_unit"] + r["tax_unit"])
    r["unit_whole_cost"] = r["unit_own_cost"] + r["ho_alloc"]
    r["cost_per_trans"] = r["unit_whole_cost"] / r["trans"]
    r["interim_price"] = r["revenue"] / r["trans"]
    r["fmos"] = (r["interim_price"] - r["cost_per_trans"]) / r["cost_per_trans"]
    r["required_price"] = r["cost_per_trans"] * (1 + g("finance.target_margin"))
    r["uplift"] = r["required_price"] / r["interim_price"]
    r["unit_surplus"] = r["revenue"] - r["unit_whole_cost"]
    r["venture_surplus"] = r["units"] * (r["revenue"] - r["unit_own_cost"]) - r["ho_total"]
    r["verdict"] = "PASS" if r["fmos"] >= FMOS_PASS else ("BORDERLINE" if r["fmos"] >= FMOS_BORDER else "FAIL")
    # year one
    ramp = m["cashflow"]["ramp_share_of_steady_state"]
    u1 = g("cashflow.year1_units")
    L, rate, n = g("cashflow.loan_amount"), g("cashflow.loan_rate_annual") / 12, g("cashflow.loan_term_months")
    r["loan_payment"] = L * rate / (1 - (1 + rate) ** (-n)) if rate > 0 else L / n
    bal, bal_s = g("cashflow.opening_balance"), g("cashflow.opening_balance")
    r["months"] = []
    for i, s in enumerate(ramp):
        sales = u1 * r["revenue"] * s
        cos = u1 * r["cogs"] * s
        hs_ = g("cashflow.year1_head_office_share")
        out = (cos + u1 * r["hr_unit"] + hs_ * r["ho_hr"] + u1 * (r["running_unit_fixed"] + r["running_unit_variable"] * s)
               + hs_ * r["running_ho"] + r["loan_payment"])
        inflow = sales + (L + g("cashflow.other_equity") if i == 0 else 0)
        if i == 0:
            out += u1 * (r["one_time_unit"] + r["capital_unit"]) + r["dev_ho"] + r["capital_ho"]
        net = inflow - out
        bal += net
        bal_s += net - sales * g("cashflow.stress_revenue_reduction")
        r["months"].append({"sales": sales, "in": inflow, "out": out, "net": net, "closing": bal, "closing_stress": bal_s})
    r["min_closing"] = min(x["closing"] for x in r["months"])
    r["min_closing_stress"] = min(x["closing_stress"] for x in r["months"])
    r["forecast"] = forecast_years(m, r, g, ramp, L, rate, n)
    return r


def forecast_inputs(m, u1, hs_, equity1):
    """The three per-year rows of the forecast block, defaulted from the year-one cash flow when absent."""
    fc = m.get("forecast") or {}
    years = int(fc.get("years", 5))
    units = [float(x) for x in fc.get("units_open_by_year", [u1] * years)]
    share = [float(x) for x in fc.get("head_office_share_by_year", [hs_] * years)]
    equity = [float(x) for x in fc.get("equity_raised_by_year", [equity1] + [0.0] * (years - 1))]
    for nm, row in (("units_open_by_year", units), ("head_office_share_by_year", share), ("equity_raised_by_year", equity)):
        if len(row) != years:
            raise ValueError(f"forecast.{nm} must list {years} values, one per year")
    if abs(units[0] - u1) > 1e-9:
        raise ValueError("forecast.units_open_by_year[0] must equal cashflow.year1_units")
    if abs(share[0] - hs_) > 1e-9:
        raise ValueError("forecast.head_office_share_by_year[0] must equal cashflow.year1_head_office_share")
    if abs(equity[0] - equity1) > 1e-9:
        raise ValueError("forecast.equity_raised_by_year[0] must equal cashflow.other_equity")
    return years, units, share, equity


def replacements_in_year(life, years_since_open):
    """How many times an asset bought at the start of its cohort's first year is replaced in a later year.
    Bought in month 1; expires at the end of month `life`; the replacement is paid in the year that
    holds month life + 1. Year k after opening covers months 12k + 1 to 12k + 12."""
    k = years_since_open
    if k <= 0:
        return 0
    return (12 * (k + 1) - 1) // life - (12 * k - 1) // life


def forecast_years(m, r, g, ramp, L, rate, n):
    """Annual profit and loss, cash flow and balance sheet, mirrored by tabs 15 to 18.
    Rules: a cohort of units opens at the start of its year and ramps on the year-one profile; existing
    units run at steady state; start-up costs and head-office development are expensed when paid; tax
    is charged on profit after losses brought forward and paid the year after it is charged; no
    debtors, creditors or stock (a cash business); later funding is equity."""
    u1, hs_ = g("cashflow.year1_units"), g("cashflow.year1_head_office_share")
    years, units, share, equity = forecast_inputs(m, u1, hs_, g("cashflow.other_equity"))
    P, ramp_sum, tax_rate = r["loan_payment"], sum(ramp), g("finance.tax_rate")

    def loan_balance(k):
        if k >= n:
            return 0.0
        if rate == 0:
            return max(0.0, L - P * k)
        return max(0.0, L * (1 + rate) ** k - P * ((1 + rate) ** k - 1) / rate)

    out, new_by_year = [], []
    prev_units = nbv = losses = prev_tax = cum_equity = retained = 0.0
    cash = g("cashflow.opening_balance")
    for y in range(1, years + 1):
        U = units[y - 1]
        N = U - prev_units
        new_by_year.append(N)
        V = 12 * prev_units + N * ramp_sum
        sh = share[y - 1]
        revenue, cos = r["revenue"] * V, r["cogs"] * V
        staff_units, staff_ho = r["hr_unit"] * 12 * U, r["ho_hr"] * 12 * sh
        run_units = r["running_unit_fixed"] * 12 * U + r["running_unit_variable"] * V
        run_ho = r["running_ho"] * 12 * sh
        startup = r["one_time_unit"] * N
        dev = r["dev_ho"] if y == 1 else 0.0
        capex_new = r["capital_unit"] * N + (r["capital_ho"] if y == 1 else 0.0)
        rep_unit = 0.0
        for c in range(1, y):
            per_unit = 0.0
            for a in m["assets"]["unit"]:
                q = r["headcount"] if a.get("quantity_driver") == "per_head" else a.get("quantity", 1)
                per_unit += a["cost"] * q * replacements_in_year(a["life_months"], y - c)
            rep_unit += per_unit * new_by_year[c - 1]
        rep_ho = sum(a["cost"] * a.get("quantity", 1) * replacements_in_year(a["life_months"], y - 1)
                     for a in m["assets"]["head_office"])
        dep = min((r["dep_unit"] * U + r["dep_ho"]) * 12, nbv + capex_new + rep_unit + rep_ho)
        nbv_open = nbv
        nbv = nbv + capex_new + rep_unit + rep_ho - dep
        op = revenue - cos - staff_units - staff_ho - run_units - run_ho - startup - dev - dep
        k0 = 12 * (y - 1)
        bal_open, bal_close = loan_balance(k0), loan_balance(12 * y)
        payments = P * min(12, max(0, n - k0))
        principal = bal_open - bal_close
        interest = payments - principal
        pbt = op - interest
        losses_bf = losses
        taxable = max(0.0, pbt - losses_bf)
        tax = taxable * tax_rate
        losses = max(0.0, losses_bf - max(0.0, pbt)) + max(0.0, -pbt)
        pat = pbt - tax
        tax_paid = prev_tax
        cash_ops = op + dep - interest - tax_paid
        loan_in = L if y == 1 else 0.0
        eq = equity[y - 1]
        net = cash_ops - capex_new - rep_unit - rep_ho + loan_in - principal + eq
        cash_open = cash
        cash += net
        cum_equity += eq
        retained += pat
        out.append(dict(year=y, units=U, new_units=N, unit_months=V, share=sh, equity=eq, revenue=revenue, cos=cos,
                        staff_units=staff_units, staff_ho=staff_ho, run_units=run_units, run_ho=run_ho, startup=startup,
                        dev=dev, dep=dep, op=op, interest=interest, pbt=pbt, losses_bf=losses_bf, taxable=taxable, tax=tax,
                        losses_cf=losses, pat=pat, tax_paid=tax_paid, cash_ops=cash_ops, capex_new=capex_new,
                        rep_unit=rep_unit, rep_ho=rep_ho, loan_in=loan_in, bal_open=bal_open, bal_close=bal_close,
                        payments=payments, principal=principal, net=net, cash_open=cash_open, cash=cash, nbv_open=nbv_open,
                        nbv=nbv, tax_payable=tax, net_assets=nbv + cash - bal_close - tax, share_capital=cum_equity,
                        retained=retained))
        prev_units, prev_tax = U, tax
    return out


def sensitivity(m, inputs):
    """One-at-a-time: each banded input moved to its adverse end; FMOS re-read. Sorted worst first."""
    base = {k: v["value"] for k, v in inputs.items()}
    fmos0 = compute(m, base)["fmos"]
    rows = []
    for k, v in inputs.items():
        if not v["adverse"] or v["low"] == v["high"]:
            continue
        alt = dict(base)
        alt[k] = v[v["adverse"]]
        f = compute(m, alt)["fmos"]
        rows.append((k, v["adverse"], alt[k], f, f - fmos0))
        if f > fmos0 + 1e-9:
            print(f"warning: '{k}' is labelled adverse={v['adverse']} but that end raises FMOS "
                  f"({fmos0:.1%} -> {f:.1%}); fix the label in the model file", file=sys.stderr)
    rows.sort(key=lambda x: x[3])
    worst = dict(base)
    for k, v in inputs.items():
        if v["adverse"]:
            worst[k] = v[v["adverse"]]
    return fmos0, rows, compute(m, worst)["fmos"]


# ----------------------------------------------------------------------------------------------
# workbook
# ----------------------------------------------------------------------------------------------

class Book:
    def __init__(self, m):
        self.m = m
        self.wb = Workbook()
        self.wb.remove(self.wb.active)
        self.names = {}          # defined name -> (ref, description)
        self.ref = {}            # input key -> absolute ref on Master

    def sheet(self, title, widths):
        ws = self.wb.create_sheet(title)
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        return ws

    def header(self, ws, row, cols):
        for i, c in enumerate(cols, 1):
            cell = ws.cell(row=row, column=i, value=c)
            cell.font, cell.fill = HEAD, HEADFILL
            cell.alignment = Alignment(wrap_text=True, vertical="top")

    def title(self, ws, text, sub=None):
        ws["A1"] = text
        ws["A1"].font = Font(bold=True, size=14)
        if sub:
            ws["A2"] = sub
            ws["A2"].font = NOTE

    def name(self, nm, ws, cell, desc):
        ref = self._abs(ws, cell)
        self.names[nm] = (ref, desc)
        self.wb.defined_names[nm] = DefinedName(nm, attr_text=ref)
        return ref

    @staticmethod
    def _abs(ws, cell):
        col = "".join(ch for ch in cell if ch.isalpha())
        row = "".join(ch for ch in cell if ch.isdigit())
        return f"'{ws.title}'!${col}${row}"

    def a(self, ws, cell):
        return self._abs(ws, cell)


def build(m, out_dir):
    inputs = collect_inputs(m)
    base_vals = {k: v["value"] for k, v in inputs.items()}
    R = compute(m, base_vals)
    b = Book(m)
    slug = m["venture"]["slug"]
    cur = m["venture"].get("currency", "GBP")

    # ---- 1 Master Control ------------------------------------------------------------------
    ws = b.sheet("1 Master", [46, 14, 14, 14, 14, 12, 6, 60, 10, 30])
    b.title(ws, f"{m['venture']['name']} — Master Control of variables and assumed values",
            "Blue cells are inputs. Change them here only; every other tab is formulas. Scenario 1 = base, 2 = low end of every band, 3 = high end.")
    ws["A4"] = "Scenario (1 base · 2 low · 3 high)"
    ws["A4"].font = BOLD
    ws["B4"] = 1
    ws["B4"].font = INPUT
    b.name("scenario", ws, "B4", "Scenario switch: 1 base, 2 all-low, 3 all-high")
    scen = b.a(ws, "B4")
    b.header(ws, 6, ["Variable", "Active value", "Base", "Low", "High", "Unit", "Tier", "Source", "Adverse end", "Key"])
    row = 7
    for k, v in inputs.items():
        ws.cell(row=row, column=1, value=label_for(k, m))
        ws.cell(row=row, column=2, value=f"=CHOOSE({scen},C{row},D{row},E{row})")
        for col, key in ((3, "value"), (4, "low"), (5, "high")):
            c = ws.cell(row=row, column=col, value=v[key])
            c.font = INPUT
            c.number_format = PCT if v["unit"] == "share" else (MONEY2 if v["unit"] == cur and v["value"] < 100 else '#,##0.####')
        ws.cell(row=row, column=2).number_format = ws.cell(row=row, column=3).number_format
        ws.cell(row=row, column=6, value=v["unit"])
        ws.cell(row=row, column=7, value=v["tier"])
        ws.cell(row=row, column=8, value=v["source"]).alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=row, column=9, value=v["adverse"])
        ws.cell(row=row, column=10, value=k).font = NOTE
        b.ref[k] = b.a(ws, f"B{row}")
        b.names["in_" + k.replace(".", "_").replace(" ", "_").lower()] = (b.ref[k], label_for(k, m))
        row += 1
    ws.freeze_panes = "B7"
    I = b.ref  # noqa: E741

    # ---- 2 Customers -----------------------------------------------------------------------
    ws = b.sheet("2 Customers", [52, 18, 60])
    b.title(ws, "Customer base and monthly transactions — one operating unit, then the venture",
            f"Operating unit: {m['venture']['unit_name']} — {m['venture'].get('unit_description', '')}")
    lines = [
        ("Reachable population (whole venture)", f"={I['market.total_reachable_population']}", NUM, "Master"),
        ("Total addressable market = reachable × (1 − non-viable share)", f"=B4*(1-{I['market.non_viable_share']})", NUM, "IFC step 1"),
        ("Number of operating units = reachable ÷ population per unit, rounded up", f"=ROUNDUP(B4/{I['market.unit_population']},0)", NUM, "IFC step 1"),
        ("Reachable population per unit", f"={I['market.unit_population']}", NUM, "Master"),
        ("Viable population per unit = reachable per unit × (1 − non-viable share)", f"=B7*(1-{I['market.non_viable_share']})", NUM, ""),
        ("Customer base per unit = viable population × penetration", f"=B8*{I['market.penetration_steady_state']}", NUM, "IFC step 1"),
        ("Transactions per unit per month = customers × frequency", f"=B9*{I['market.transactions_per_customer_per_month']}", NUM, "IFC step 1"),
        ("Transactions across the venture per month = units × per unit", "=B6*B10", NUM, ""),
    ]
    for i, (lab, f, fmt, note) in enumerate(lines):
        r_ = 4 + i
        ws.cell(row=r_, column=1, value=lab)
        c = ws.cell(row=r_, column=2, value=f)
        c.number_format = fmt
        ws.cell(row=r_, column=3, value=note).font = NOTE
    b.name("tam", ws, "B5", "Total addressable market, households or customers")
    b.name("units", ws, "B6", "Number of operating units at scale")
    b.name("customers_per_unit", ws, "B9", "Customer base per operating unit at steady state")
    b.name("transactions_per_unit", ws, "B10", "Transactions per operating unit per month at steady state")
    b.name("transactions_venture", ws, "B11", "Transactions across the venture per month at steady state")
    TRANS, CUST, UNITS = b.a(ws, "B10"), b.a(ws, "B9"), b.a(ws, "B6")
    b.header(ws, 13, ["Product", "Share of transactions", "Transactions per unit per month", "Price", "Revenue per unit per month", "Cost of goods per transaction", "Cost of goods per unit per month"])
    for i, p in enumerate(m["products"]):
        r_ = 14 + i
        ws.cell(row=r_, column=1, value=p["name"])
        ws.cell(row=r_, column=2, value=f"={I[f'product.{i}.share']}").number_format = PCT
        ws.cell(row=r_, column=3, value=f"={TRANS}*B{r_}").number_format = NUM
        ws.cell(row=r_, column=4, value=f"={I[f'product.{i}.price']}").number_format = MONEY2
        ws.cell(row=r_, column=5, value=f"=C{r_}*D{r_}").number_format = MONEY
        ws.cell(row=r_, column=6, value=f"={I[f'product.{i}.cogs']}").number_format = MONEY2
        ws.cell(row=r_, column=7, value=f"=C{r_}*F{r_}").number_format = MONEY
    tr = 14 + len(m["products"])
    ws.cell(row=tr, column=1, value="Total").font = BOLD
    ws.cell(row=tr, column=2, value=f"=SUM(B14:B{tr-1})").number_format = PCT
    ws.cell(row=tr, column=3, value=f"=SUM(C14:C{tr-1})").number_format = NUM
    ws.cell(row=tr, column=5, value=f"=SUM(E14:E{tr-1})").number_format = MONEY
    ws.cell(row=tr, column=7, value=f"=SUM(G14:G{tr-1})").number_format = MONEY
    for col in "CEG":
        ws[f"{col}{tr}"].font = BOLD
    REV = b.name("revenue_per_unit", ws, f"E{tr}", "Revenue per operating unit per month at interim prices")
    COGS = b.name("cogs_per_unit", ws, f"G{tr}", "Cost of goods per operating unit per month")
    ws.column_dimensions["D"].width = 12
    for col in "EFG":
        ws.column_dimensions[col].width = 18
    prod_rows = list(range(14, tr))

    # ---- 3 HR ------------------------------------------------------------------------------
    ws = b.sheet("3 HR", [34, 22, 12, 20, 12, 16, 16, 40])
    b.title(ws, "Human resource costs — activities, time, drivers, headcount",
            "Hours = minutes ÷ 60 × driver quantity × multiplier. Headcount = hours ÷ available hours, rounded up to whole people. IFC step 2.")
    AVAIL = I["hr.available_hours"]
    b.header(ws, 4, ["Activity", "Role", "Minutes", "Driver", "Multiplier", "Driver quantity per month", "Hours per month", "Note"])
    qty_ref = {"per_transaction": TRANS, "per_customer_month": CUST, "per_unit_month": "1"}
    acts = m["hr"]["unit_activities"]
    for i, a in enumerate(acts):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=a["activity"])
        ws.cell(row=r_, column=2, value=a["role"])
        ws.cell(row=r_, column=3, value=a["minutes"]).font = INPUT
        ws.cell(row=r_, column=4, value=a["driver"])
        ws.cell(row=r_, column=5, value=a.get("multiplier", 1)).font = INPUT
        ws.cell(row=r_, column=6, value=f"={qty_ref[a['driver']]}").number_format = NUM
        ws.cell(row=r_, column=7, value=f"=C{r_}/60*F{r_}*E{r_}").number_format = '#,##0.0'
        ws.cell(row=r_, column=8, value=a.get("note", "")).font = NOTE
    a_end = 4 + len(acts)
    rr = a_end + 2
    b.header(ws, rr, ["Role", "Hours per month", "Available hours per person", "Headcount (rounded up)", "Monthly cost per person", "Role cost per month", "Utilisation", ""])
    role_rows = {}
    for i, role in enumerate(m["hr"]["unit_roles"]):
        r_ = rr + 1 + i
        role_rows[role] = r_
        ws.cell(row=r_, column=1, value=role)
        ws.cell(row=r_, column=2, value=f'=SUMIF($B$5:$B${a_end},A{r_},$G$5:$G${a_end})').number_format = '#,##0.0'
        ws.cell(row=r_, column=3, value=f"={AVAIL}").number_format = NUM
        ws.cell(row=r_, column=4, value=f"=ROUNDUP(B{r_}/C{r_},0)").number_format = NUM
        ws.cell(row=r_, column=5, value=f"={I[f'role.{role}.monthly_cost']}").number_format = MONEY
        ws.cell(row=r_, column=6, value=f"=D{r_}*E{r_}").number_format = MONEY
        ws.cell(row=r_, column=7, value=f"=IF(D{r_}=0,0,B{r_}/(C{r_}*D{r_}))").number_format = PCT
    r_end = rr + len(m["hr"]["unit_roles"])
    tr = r_end + 1
    ws.cell(row=tr, column=1, value="Unit total").font = BOLD
    ws.cell(row=tr, column=4, value=f"=SUM(D{rr+1}:D{r_end})").number_format = NUM
    ws.cell(row=tr, column=6, value=f"=SUM(F{rr+1}:F{r_end})").number_format = MONEY
    ws[f"D{tr}"].font = ws[f"F{tr}"].font = BOLD
    HEADCOUNT = b.name("headcount_per_unit", ws, f"D{tr}", "Headcount per operating unit")
    HR_UNIT = b.name("hr_cost_per_unit", ws, f"F{tr}", "Staff cost per operating unit per month")
    hr_ = tr + 2
    ws.cell(row=hr_, column=1, value="Head office").font = BOLD
    b.header(ws, hr_ + 1, ["Role", "Count", "Monthly cost per person", "Cost per month", "", "", "", ""])
    for i, x in enumerate(m["hr"]["head_office_roles"]):
        r_ = hr_ + 2 + i
        ws.cell(row=r_, column=1, value=x["role"])
        ws.cell(row=r_, column=2, value=x["count"]).font = INPUT
        c = ws.cell(row=r_, column=3, value=x["monthly_cost"])
        c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_ho_role", x["role"]), ws, f"D{r_}", f"Staff cost per month, head office — {x['role']} × {x['count']}")
        LINE_VALUES[line_name("line_ho_role", x["role"])] = x["count"] * x["monthly_cost"]
        ws.cell(row=r_, column=4, value=f"=B{r_}*C{r_}").number_format = MONEY
    he = hr_ + 1 + len(m["hr"]["head_office_roles"])
    ws.cell(row=he + 1, column=1, value="Head office staff total").font = BOLD
    ws.cell(row=he + 1, column=4, value=f"=SUM(D{hr_+2}:D{he})").number_format = MONEY
    ws[f"D{he+1}"].font = BOLD
    HO_HR = b.name("ho_staff_cost", ws, f"D{he+1}", "Head-office staff cost per month")

    # ---- 4 Depreciation --------------------------------------------------------------------
    ws = b.sheet("4 Depreciation", [34, 14, 12, 16, 12, 16, 16])
    b.title(ws, "Capital assets — cost, life, quantity, monthly depreciation", "Depreciation per month = cost × quantity ÷ life in months. IFC step 2.")
    b.header(ws, 4, ["Asset (operating unit)", "Cost", "Life (months)", "Quantity driver", "Quantity", "Capital cost", "Depreciation per month"])
    ua = m["assets"]["unit"]
    for i, a in enumerate(ua):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=a["name"])
        c = ws.cell(row=r_, column=2, value=a["cost"]); c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_asset", a["name"]), ws, f"B{r_}", f"Asset cost, operating unit — {a['name']}")
        LINE_VALUES[line_name("line_asset", a["name"])] = a["cost"]
        ws.cell(row=r_, column=3, value=a["life_months"]).font = INPUT
        drv = a.get("quantity_driver", "fixed")
        ws.cell(row=r_, column=4, value=drv)
        if drv == "per_head":
            ws.cell(row=r_, column=5, value=f"={HEADCOUNT}")
        else:
            ws.cell(row=r_, column=5, value=a.get("quantity", 1)).font = INPUT
        ws.cell(row=r_, column=6, value=f"=B{r_}*E{r_}").number_format = MONEY
        ws.cell(row=r_, column=7, value=f"=F{r_}/C{r_}").number_format = MONEY
    ue = 4 + len(ua)
    UNIT_ASSET_ROWS = list(range(5, ue + 1))
    ws.cell(row=ue + 1, column=1, value="Unit total").font = BOLD
    ws.cell(row=ue + 1, column=6, value=f"=SUM(F5:F{ue})").number_format = MONEY
    ws.cell(row=ue + 1, column=7, value=f"=SUM(G5:G{ue})").number_format = MONEY
    CAP_UNIT = b.name("capital_per_unit", ws, f"F{ue+1}", "Capital assets per operating unit")
    DEP_UNIT = b.name("depreciation_per_unit", ws, f"G{ue+1}", "Depreciation per operating unit per month")
    hs = ue + 3
    b.header(ws, hs, ["Asset (head office)", "Cost", "Life (months)", "", "Quantity", "Capital cost", "Depreciation per month"])
    ha = m["assets"]["head_office"]
    for i, a in enumerate(ha):
        r_ = hs + 1 + i
        ws.cell(row=r_, column=1, value=a["name"])
        c = ws.cell(row=r_, column=2, value=a["cost"]); c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_ho_asset", a["name"]), ws, f"B{r_}", f"Asset cost, head office — {a['name']}")
        LINE_VALUES[line_name("line_ho_asset", a["name"])] = a["cost"]
        ws.cell(row=r_, column=3, value=a["life_months"]).font = INPUT
        ws.cell(row=r_, column=5, value=a.get("quantity", 1)).font = INPUT
        ws.cell(row=r_, column=6, value=f"=B{r_}*E{r_}").number_format = MONEY
        ws.cell(row=r_, column=7, value=f"=F{r_}/C{r_}").number_format = MONEY
    hend = hs + len(ha)
    HO_ASSET_ROWS = list(range(hs + 1, hend + 1))
    ws.cell(row=hend + 1, column=1, value="Head office total").font = BOLD
    ws.cell(row=hend + 1, column=6, value=f"=SUM(F{hs+1}:F{hend})").number_format = MONEY
    ws.cell(row=hend + 1, column=7, value=f"=SUM(G{hs+1}:G{hend})").number_format = MONEY
    CAP_HO = b.name("capital_head_office", ws, f"F{hend+1}", "Head-office capital assets")
    DEP_HO = b.name("depreciation_head_office", ws, f"G{hend+1}", "Head-office depreciation per month")

    # ---- 5 Running -------------------------------------------------------------------------
    ws = b.sheet("5 Running", [38, 20, 14, 18, 16])
    b.title(ws, "General running costs — driver-linked", "Cost per month = amount × driver quantity. IFC step 2.")
    b.header(ws, 4, ["Item (operating unit)", "Driver", "Amount", "Driver quantity", "Cost per month"])
    rq_ref = {"per_unit_month": "1", "per_transaction": TRANS, "per_customer_month": CUST, "per_head": HEADCOUNT}
    ru = m["running"]["unit"]
    for i, x in enumerate(ru):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=x["name"])
        ws.cell(row=r_, column=2, value=x["driver"])
        c = ws.cell(row=r_, column=3, value=x["amount"]); c.font, c.number_format = INPUT, MONEY2
        b.name(line_name("line_running", x["name"]), ws, f"C{r_}", f"Running cost amount, operating unit ({x['driver']}) — {x['name']}")
        LINE_VALUES[line_name("line_running", x["name"])] = x["amount"]
        ws.cell(row=r_, column=4, value=f"={rq_ref[x['driver']]}").number_format = NUM
        ws.cell(row=r_, column=5, value=f"=C{r_}*D{r_}").number_format = MONEY
    re_ = 4 + len(ru)
    ws.cell(row=re_ + 1, column=1, value="Unit total").font = BOLD
    ws.cell(row=re_ + 1, column=5, value=f"=SUM(E5:E{re_})").number_format = MONEY
    ws.cell(row=re_ + 2, column=1, value="of which fixed per month (per unit and per head drivers)")
    ws.cell(row=re_ + 2, column=5, value=f'=SUMIF(B5:B{re_},"per_unit_month",E5:E{re_})+SUMIF(B5:B{re_},"per_head",E5:E{re_})').number_format = MONEY
    ws.cell(row=re_ + 3, column=1, value="of which varies with volume")
    ws.cell(row=re_ + 3, column=5, value=f"=E{re_+1}-E{re_+2}").number_format = MONEY
    RUN_UNIT = b.name("running_per_unit", ws, f"E{re_+1}", "General running cost per operating unit per month")
    RUN_FIX = b.a(ws, f"E{re_+2}")
    RUN_VAR = b.a(ws, f"E{re_+3}")
    hs = re_ + 5
    b.header(ws, hs, ["Item (head office)", "", "Amount per month", "", "Cost per month"])
    rh = m["running"]["head_office"]
    for i, x in enumerate(rh):
        r_ = hs + 1 + i
        ws.cell(row=r_, column=1, value=x["name"])
        c = ws.cell(row=r_, column=3, value=x["amount"]); c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_ho_running", x["name"]), ws, f"C{r_}", f"Running cost per month, head office — {x['name']}")
        LINE_VALUES[line_name("line_ho_running", x["name"])] = x["amount"]
        ws.cell(row=r_, column=5, value=f"=C{r_}").number_format = MONEY
    hend = hs + len(rh)
    ws.cell(row=hend + 1, column=1, value="Head office total").font = BOLD
    ws.cell(row=hend + 1, column=5, value=f"=SUM(E{hs+1}:E{hend})").number_format = MONEY
    RUN_HO = b.name("running_head_office", ws, f"E{hend+1}", "Head-office running cost per month")

    # ---- 6 Start-up ------------------------------------------------------------------------
    ws = b.sheet("6 Start-up", [52, 16, 50])
    b.title(ws, "Start-up working capital and development costs", "One-time costs plus working capital, spread over the investment recovery period. IFC step 3.")
    b.header(ws, 4, ["Item (operating unit, one-time)", "Cost", "Note"])
    so = m["startup"]["unit_one_time"]
    for i, x in enumerate(so):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=x["name"])
        c = ws.cell(row=r_, column=2, value=x["cost"]); c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_startup", x["name"]), ws, f"B{r_}", f"Start-up cost, operating unit, one-time — {x['name']}")
        LINE_VALUES[line_name("line_startup", x["name"])] = x["cost"]
    se = 4 + len(so)
    rows6 = [
        ("One-time start-up costs per unit", f"=SUM(B5:B{se})", ""),
        ("Working capital = months × (cost of goods + staff + running) per month", f"={I['startup.working_capital_months']}*({COGS}+{HR_UNIT}+{RUN_UNIT})", "cash the unit needs before revenue covers running cost"),
        ("Start-up total per unit", f"=B{se+1}+B{se+2}", ""),
        ("Investment recovery period (months)", f"={I['startup.investment_period_months']}", ""),
        ("Start-up charge per unit per month = total ÷ period", f"=B{se+3}/B{se+4}", "IFC step 3"),
    ]
    for i, (lab, f, note) in enumerate(rows6):
        r_ = se + 1 + i
        ws.cell(row=r_, column=1, value=lab)
        ws.cell(row=r_, column=2, value=f).number_format = MONEY
        ws.cell(row=r_, column=3, value=note).font = NOTE
    STARTUP_UNIT = b.name("startup_per_unit", ws, f"B{se+3}", "Start-up cost per operating unit (one-time plus working capital)")
    STARTUP_M = b.name("startup_charge_per_unit", ws, f"B{se+5}", "Start-up charge per operating unit per month")
    ONE_TIME = b.a(ws, f"B{se+1}")
    hs = se + 7
    b.header(ws, hs, ["Item (head office development, one-time)", "Cost", "Note"])
    sd = m["startup"]["head_office_development"]
    for i, x in enumerate(sd):
        r_ = hs + 1 + i
        ws.cell(row=r_, column=1, value=x["name"])
        c = ws.cell(row=r_, column=2, value=x["cost"]); c.font, c.number_format = INPUT, MONEY
        b.name(line_name("line_development", x["name"]), ws, f"B{r_}", f"Development cost, head office, one-time — {x['name']}")
        LINE_VALUES[line_name("line_development", x["name"])] = x["cost"]
    de = hs + len(sd)
    ws.cell(row=de + 1, column=1, value="Development total")
    ws.cell(row=de + 1, column=2, value=f"=SUM(B{hs+1}:B{de})").number_format = MONEY
    ws.cell(row=de + 2, column=1, value="Development charge per month = total ÷ period")
    ws.cell(row=de + 2, column=2, value=f"=B{de+1}/{I['startup.investment_period_months']}").number_format = MONEY
    DEV_HO = b.name("development_head_office", ws, f"B{de+1}", "Head-office development cost, one-time")
    DEV_M = b.name("development_charge_per_month", ws, f"B{de+2}", "Head-office development charge per month")

    # ---- 7 Returns / 8 Tax -----------------------------------------------------------------
    ws = b.sheet("7 Returns", [56, 16, 40])
    b.title(ws, "Investment returns", "Return per month = (start-up + capital assets) × cost of capital ÷ 12. IFC step 3.")
    rows7 = [
        ("Operating unit: capital invested = start-up + capital assets", f"={STARTUP_UNIT}+{CAP_UNIT}"),
        ("Cost of capital (annual)", f"={I['finance.cost_of_capital']}"),
        ("Return required per unit per month", "=B4*B5/12"),
        ("Head office: capital invested = development + capital assets", f"={DEV_HO}+{CAP_HO}"),
        ("Return required at head office per month", "=B7*B5/12"),
    ]
    for i, (lab, f) in enumerate(rows7):
        ws.cell(row=4 + i, column=1, value=lab)
        ws.cell(row=4 + i, column=2, value=f).number_format = PCT if i == 1 else MONEY
    RET_UNIT = b.name("returns_per_unit", ws, "B6", "Investment return required per operating unit per month")
    RET_HO = b.name("returns_head_office", ws, "B8", "Investment return required at head office per month")
    ws = b.sheet("8 Tax", [56, 16])
    b.title(ws, "Tax on investment returns", "Tax per month = return per month × tax rate. IFC step 3.")
    ws["A4"], ws["B4"] = "Tax rate", f"={I['finance.tax_rate']}"
    ws["B4"].number_format = PCT
    ws["A5"], ws["B5"] = "Tax per unit per month", f"={RET_UNIT}*B4"
    ws["A6"], ws["B6"] = "Tax at head office per month", f"={RET_HO}*B4"
    ws["B5"].number_format = ws["B6"].number_format = MONEY
    TAX_UNIT = b.name("tax_per_unit", ws, "B5", "Tax per operating unit per month")
    TAX_HO = b.name("tax_head_office", ws, "B6", "Tax at head office per month")

    # ---- 9 Unit costs (summary) -------------------------------------------------------------
    ws = b.sheet("9 Unit costs", [56, 16, 14, 30])
    b.title(ws, "Operating unit — whole cost structure per month", "Every cost the unit carries, including its share of head office. IFC step 4 input.")
    b.header(ws, 4, ["Line", "Per month", "Share", "From"])
    rows9 = [
        ("Cost of goods", f"={COGS}", "2 Customers"),
        ("Staff", f"={HR_UNIT}", "3 HR"),
        ("Depreciation", f"={DEP_UNIT}", "4 Depreciation"),
        ("General running", f"={RUN_UNIT}", "5 Running"),
        ("Start-up charge", f"={STARTUP_M}", "6 Start-up"),
        ("Investment return", f"={RET_UNIT}", "7 Returns"),
        ("Tax", f"={TAX_UNIT}", "8 Tax"),
    ]
    for i, (lab, f, src) in enumerate(rows9):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=lab)
        ws.cell(row=r_, column=2, value=f).number_format = MONEY
        ws.cell(row=r_, column=4, value=src).font = NOTE
    ws["A12"], ws["B12"] = "Unit's own costs", "=SUM(B5:B11)"
    ws["A13"] = "Head office costs per month"
    ws["B13"] = f"={HO_HR}+{RUN_HO}+{DEP_HO}+{DEV_M}+{RET_HO}+{TAX_HO}"
    ws["A14"] = "Head office target profit = head office costs × target margin"
    ws["B14"] = f"=B13*{I['finance.ho_target_ebit']}"
    ws["A15"] = "Head office total per month"
    ws["B15"] = "=B13+B14"
    ws["A16"] = "Head office allocated per unit = total ÷ number of units"
    ws["B16"] = f"=B15/{UNITS}"
    ws["A17"] = "Whole cost per unit per month"
    ws["B17"] = "=B12+B16"
    ws["A18"] = "Whole cost per transaction = whole cost ÷ transactions"
    ws["B18"] = f"=B17/{TRANS}"
    for r_ in range(12, 19):
        ws[f"B{r_}"].number_format = MONEY2 if r_ == 18 else MONEY
    for r_ in (12, 15, 17, 18):
        ws[f"A{r_}"].font = ws[f"B{r_}"].font = BOLD
    for r_ in list(range(5, 12)) + [16]:
        ws.cell(row=r_, column=3, value=f"=B{r_}/$B$17").number_format = PCT
    UNIT_OWN = b.name("unit_own_cost", ws, "B12", "Operating unit's own costs per month, before head office")
    HO_COSTS = b.name("ho_costs", ws, "B13", "Head-office costs per month")
    HO_TOTAL = b.name("ho_total", ws, "B15", "Head-office costs plus target profit per month")
    HO_ALLOC = b.name("ho_allocated_per_unit", ws, "B16", "Head office allocated per operating unit per month")
    WHOLE = b.name("whole_cost_per_unit", ws, "B17", "Whole cost per operating unit per month")
    CPT = b.name("cost_per_transaction", ws, "B18", "Whole cost per transaction — the cost floor")

    # ---- 10 Pricing ------------------------------------------------------------------------
    ws = b.sheet("10 Pricing", [58, 16, 16, 16, 16])
    b.title(ws, "Pricing — cost floor, interim price, margin of safety, required price",
            "Margin of safety = (price − cost) ÷ cost. Gate: 25% or more passes; 15% to 24% borderline; under 15% fails. Required price = cost × (1 + target margin). IFC steps 4 and 5.")
    rows10 = [
        ("Whole cost per transaction (cost floor)", f"={CPT}", MONEY2),
        ("Interim price per transaction (revenue ÷ transactions, at the prices on tab 1)", f"={REV}/{TRANS}", MONEY2),
        ("Margin of safety = (price − cost) ÷ cost", "=(B5-B4)/B4", PCT),
        ("Target margin of safety", f"={I['finance.target_margin']}", PCT),
        ("Verdict", f'=IF(B6>={FMOS_PASS},"PASS",IF(B6>={FMOS_BORDER},"BORDERLINE","FAIL"))', None),
        ("Required price per transaction = cost × (1 + target)", "=B4*(1+B7)", MONEY2),
        ("Price uplift needed to reach target (required ÷ interim)", "=B9/B5", PCT),
        ("Margin from failure: margin of safety less the 15% floor (percentage points)", f"=B6-{FMOS_BORDER}", PCT),
        ("Price fall that takes the margin of safety to the 15% floor", f"=B5-B4*(1+{FMOS_BORDER})", MONEY2),
    ]
    for i, (lab, f, fmt) in enumerate(rows10):
        r_ = 4 + i
        ws.cell(row=r_, column=1, value=lab)
        c = ws.cell(row=r_, column=2, value=f)
        if fmt:
            c.number_format = fmt
    for r_ in (6, 8, 9):
        ws[f"A{r_}"].font = ws[f"B{r_}"].font = BOLD
    FMOS = b.name("margin_of_safety", ws, "B6", "Margin of safety at the interim price, base scenario")
    b.name("interim_price", ws, "B5", "Interim price per transaction")
    b.name("verdict", ws, "B8", "Verdict on the margin of safety: PASS, BORDERLINE or FAIL")
    REQ = b.name("required_price", ws, "B9", "Required price per transaction at the target margin of safety")
    UPLIFT = b.name("price_uplift_to_target", ws, "B10", "Price uplift needed to reach the target margin of safety (required ÷ interim)")
    b.name("margin_from_failure", ws, "B11", "Margin of safety less the 15% floor, in percentage points")
    b.name("price_fall_to_floor", ws, "B12", "Price fall per transaction that takes the margin of safety to the 15% floor")
    b.header(ws, 14, ["Product", "Interim price", "Required price at target", "Share of transactions", ""])
    for i, p in enumerate(m["products"]):
        r_ = 15 + i
        ws.cell(row=r_, column=1, value=p["name"])
        ws.cell(row=r_, column=2, value=f"={I[f'product.{i}.price']}").number_format = MONEY2
        ws.cell(row=r_, column=3, value=f"=B{r_}*{UPLIFT}").number_format = MONEY2
        ws.cell(row=r_, column=4, value=f"={I[f'product.{i}.share']}").number_format = PCT
        b.name(f"required_price_product_{i+1}", ws, f"C{r_}", f"Required price at the target margin of safety — {p['name']}")
    # sensitivity — values computed here, labelled
    fmos0, sens, worst = sensitivity(m, inputs)
    sr = 15 + len(m["products"]) + 2
    ws.cell(row=sr, column=1, value="Sensitivity — one input at a time moved to its adverse end (values computed by the generator from the same inputs; not live — change the scenario on tab 1 to see every band at once)").font = NOTE
    b.header(ws, sr + 1, ["Input", "Adverse end", "Value used", "Margin of safety", "Change from base"])
    for i, (k, end, val, f, d) in enumerate(sens):
        r_ = sr + 2 + i
        ws.cell(row=r_, column=1, value=label_for(k, m))
        ws.cell(row=r_, column=2, value=end)
        ws.cell(row=r_, column=3, value=val).number_format = '#,##0.####'
        ws.cell(row=r_, column=4, value=f).number_format = PCT
        ws.cell(row=r_, column=5, value=d).number_format = PCT
    er = sr + 2 + len(sens)
    ws.cell(row=er, column=1, value="Binding input (largest fall in the margin of safety)").font = BOLD
    ws.cell(row=er, column=2, value=label_for(sens[0][0], m) if sens else "none banded")
    ws.cell(row=er + 1, column=1, value="Margin of safety with every input at its adverse end (worst corner)").font = BOLD
    ws.cell(row=er + 1, column=2, value=worst).number_format = PCT
    ws.cell(row=er + 2, column=1, value="Margin of safety at base, as computed by the builder (must equal B6)")
    ws.cell(row=er + 2, column=2, value=fmos0).number_format = PCT
    b.name("binding_input", ws, f"B{er}", "The input whose adverse end lowers the margin of safety most")
    b.name("margin_of_safety_worst_corner", ws, f"B{er+1}", "Margin of safety with every banded input at its adverse end")
    FMOS_GEN = b.a(ws, f"B{er+2}")
    R["binding_input"] = label_for(sens[0][0], m) if sens else "none banded"
    R["fmos_worst_corner"] = worst
    R["sensitivity"] = sens

    # ---- 11 Unit P&L -----------------------------------------------------------------------
    ws = b.sheet("11 Unit P&L", [52, 16, 16, 30])
    b.title(ws, "Synthesis — whole-cost profit and loss, one operating unit per month",
            "At the interim price and at the required price. Surplus ÷ whole cost recomputes the margin of safety. IFC step 5.")
    b.header(ws, 4, ["Line", "At interim price", "At required price", "Note"])
    rows11 = [
        ("Transactions per month", f"={TRANS}", f"={TRANS}", NUM),
        ("Price per transaction", f"={REV}/{TRANS}", f"={REQ}", MONEY2),
        ("Revenue", "=B5*B6", "=C5*C6", MONEY),
        ("Cost of goods", f"=-{COGS}", f"=-{COGS}", MONEY),
        ("Staff", f"=-{HR_UNIT}", f"=-{HR_UNIT}", MONEY),
        ("Depreciation", f"=-{DEP_UNIT}", f"=-{DEP_UNIT}", MONEY),
        ("General running", f"=-{RUN_UNIT}", f"=-{RUN_UNIT}", MONEY),
        ("Start-up charge", f"=-{STARTUP_M}", f"=-{STARTUP_M}", MONEY),
        ("Investment return", f"=-{RET_UNIT}", f"=-{RET_UNIT}", MONEY),
        ("Tax", f"=-{TAX_UNIT}", f"=-{TAX_UNIT}", MONEY),
        ("Head office allocation", f"=-{HO_ALLOC}", f"=-{HO_ALLOC}", MONEY),
        ("Whole cost", "=SUM(B8:B15)", "=SUM(C8:C15)", MONEY),
        ("Surplus = revenue + whole cost", "=B7+B16", "=C7+C16", MONEY),
        ("Surplus ÷ whole cost (recomputed margin of safety)", "=B17/-B16", "=C17/-C16", PCT),
    ]
    for i, (lab, f1, f2, fmt) in enumerate(rows11):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=lab)
        ws.cell(row=r_, column=2, value=f1).number_format = fmt
        ws.cell(row=r_, column=3, value=f2).number_format = fmt
    for r_ in (16, 17, 18):
        for col in "ABC":
            ws[f"{col}{r_}"].font = BOLD
    UNIT_SURPLUS = b.name("unit_surplus", ws, "B17", "Surplus per operating unit per month at the interim price")
    b.name("unit_surplus_at_required", ws, "C17", "Surplus per operating unit per month at the required price")
    FMOS_RE = b.a(ws, "B18")
    FMOS_REQ_RE = b.a(ws, "C18")

    # ---- 12 Venture P&L --------------------------------------------------------------------
    ws = b.sheet("12 Venture P&L", [52, 16, 16, 16])
    b.title(ws, "Synthesis — whole-cost profit and loss, the venture at scale, per month",
            "Every operating unit plus head office. Venture surplus must equal units × unit surplus. IFC step 5.")
    b.header(ws, 4, ["Line", "Per unit", "Units", "Venture per month"])
    rows12 = [
        ("Revenue", f"={REV}", f"={UNITS}", "=B5*C5"),
        ("Cost of goods", f"=-{COGS}", f"={UNITS}", "=B6*C6"),
        ("Staff (units)", f"=-{HR_UNIT}", f"={UNITS}", "=B7*C7"),
        ("Depreciation (units)", f"=-{DEP_UNIT}", f"={UNITS}", "=B8*C8"),
        ("General running (units)", f"=-{RUN_UNIT}", f"={UNITS}", "=B9*C9"),
        ("Start-up charge (units)", f"=-{STARTUP_M}", f"={UNITS}", "=B10*C10"),
        ("Investment return (units)", f"=-{RET_UNIT}", f"={UNITS}", "=B11*C11"),
        ("Tax (units)", f"=-{TAX_UNIT}", f"={UNITS}", "=B12*C12"),
        ("Head office staff", None, None, f"=-{HO_HR}"),
        ("Head office running", None, None, f"=-{RUN_HO}"),
        ("Head office depreciation", None, None, f"=-{DEP_HO}"),
        ("Head office development charge", None, None, f"=-{DEV_M}"),
        ("Head office investment return", None, None, f"=-{RET_HO}"),
        ("Head office tax", None, None, f"=-{TAX_HO}"),
        ("Head office target profit", None, None, f"=-({HO_TOTAL}-{HO_COSTS})"),
        ("Venture surplus per month", None, None, "=SUM(D5:D19)"),
        ("Venture surplus per year", None, None, "=D20*12"),
        ("Units × unit surplus (must equal venture surplus)", None, None, f"={UNITS}*{UNIT_SURPLUS}"),
    ]
    for i, (lab, f1, f2, f3) in enumerate(rows12):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=lab)
        if f1:
            ws.cell(row=r_, column=2, value=f1).number_format = MONEY
            ws.cell(row=r_, column=3, value=f2).number_format = NUM
        ws.cell(row=r_, column=4, value=f3).number_format = MONEY
    for r_ in (20, 21):
        ws[f"A{r_}"].font = ws[f"D{r_}"].font = BOLD
    VENTURE_SURPLUS = b.name("venture_surplus_per_month", ws, "D20", "Venture surplus per month at scale, interim price")
    b.name("venture_surplus_per_year", ws, "D21", "Venture surplus per year at scale, interim price")
    b.name("venture_revenue_per_month", ws, "D5", "Venture revenue per month at scale")
    VS_CHECK = b.a(ws, "D22")

    # ---- 13 Sales (Start Up Loans sales assumptions) ---------------------------------------
    ws = b.sheet("13 Sales", [34] + [11] * 14)
    b.title(ws, "Sales assumptions — year one, the operating units open in year one",
            "The Start Up Loans template sheet. Volumes = units open × steady-state transactions × the month's share of steady state.")
    ramp = m["cashflow"]["ramp_share_of_steady_state"]
    U1 = I["cashflow.year1_units"]
    ws["A4"] = "Operating units open in year one"
    ws["B4"] = f"={U1}"
    ws["A5"] = "Share of steady-state volume, by month"
    for j in range(12):
        c = ws.cell(row=5, column=2 + j, value=ramp[j]); c.font, c.number_format = INPUT, PCT
    b.header(ws, 7, ["Product / month"] + [f"M{j+1}" for j in range(12)] + ["Year"])
    rows_vol, rows_sales, rows_cos = {}, {}, {}
    r_ = 8
    for i, p in enumerate(m["products"]):
        ws.cell(row=r_, column=1, value=f"{p['name']} — volume").font = BOLD
        for j in range(12):
            col = get_column_letter(2 + j)
            ws.cell(row=r_, column=2 + j, value=f"=$B$4*'2 Customers'!$C${prod_rows[i]}*{col}$5").number_format = NUM
        ws.cell(row=r_, column=14, value=f"=SUM(B{r_}:M{r_})").number_format = NUM
        rows_vol[i] = r_
        ws.cell(row=r_ + 1, column=1, value=f"{p['name']} — sales")
        for j in range(12):
            col = get_column_letter(2 + j)
            ws.cell(row=r_ + 1, column=2 + j, value=f"={col}{r_}*'2 Customers'!$D${prod_rows[i]}").number_format = MONEY
        ws.cell(row=r_ + 1, column=14, value=f"=SUM(B{r_+1}:M{r_+1})").number_format = MONEY
        rows_sales[i] = r_ + 1
        ws.cell(row=r_ + 2, column=1, value=f"{p['name']} — cost of sales")
        for j in range(12):
            col = get_column_letter(2 + j)
            ws.cell(row=r_ + 2, column=2 + j, value=f"={col}{r_}*'2 Customers'!$F${prod_rows[i]}").number_format = MONEY
        ws.cell(row=r_ + 2, column=14, value=f"=SUM(B{r_+2}:M{r_+2})").number_format = MONEY
        rows_cos[i] = r_ + 2
        r_ += 4
    ws.cell(row=r_, column=1, value="Total sales").font = BOLD
    ws.cell(row=r_ + 1, column=1, value="Total cost of sales").font = BOLD
    ws.cell(row=r_ + 2, column=1, value="Total volume").font = BOLD
    for j in range(13):
        col = get_column_letter(2 + j)
        ws.cell(row=r_, column=2 + j, value="=" + "+".join(f"{col}{rows_sales[i]}" for i in rows_sales)).number_format = MONEY
        ws.cell(row=r_ + 1, column=2 + j, value="=" + "+".join(f"{col}{rows_cos[i]}" for i in rows_cos)).number_format = MONEY
        ws.cell(row=r_ + 2, column=2 + j, value="=" + "+".join(f"{col}{rows_vol[i]}" for i in rows_vol)).number_format = NUM
    SALES_ROW, COS_ROW, VOL_ROW = r_, r_ + 1, r_ + 2
    b.name("year1_sales", ws, f"N{SALES_ROW}", "Sales in year one, the units open in year one")
    b.name("year1_volume", ws, f"N{VOL_ROW}", "Transactions in year one")
    ws.freeze_panes = "B8"

    # ---- 14 Cash flow (Start Up Loans twelve-month forecast) --------------------------------
    ws = b.sheet("14 Cash flow", [44] + [11] * 13)
    b.title(ws, "Twelve-month cash-flow forecast — year one", "The Start Up Loans template sheet, with its stress test: revenue down by the rate on tab 1.")
    ws["A4"], ws["B4"] = "Loan amount", f"={I['cashflow.loan_amount']}"
    ws["A5"], ws["B5"] = "Loan interest rate (annual)", f"={I['cashflow.loan_rate_annual']}"
    ws["A6"], ws["B6"] = "Loan term (months)", f"={I['cashflow.loan_term_months']}"
    ws["A7"], ws["B7"] = "Monthly repayment = L × r ÷ (1 − (1 + r)^−n)", "=IF(B5=0,B4/B6,B4*(B5/12)/(1-(1+B5/12)^(-B6)))"
    ws["B4"].number_format = ws["B7"].number_format = MONEY
    ws["B5"].number_format = PCT
    b.name("loan_repayment_per_month", ws, "B7", "Monthly loan repayment")
    b.header(ws, 9, ["Line / month"] + [f"M{j+1}" for j in range(12)] + ["Year"])
    S = "'13 Sales'"
    lines14 = [
        ("IN: sales", lambda col, j: f"={S}!{col}{SALES_ROW}"),
        ("IN: loan", lambda col, j: f"={I['cashflow.loan_amount']}" if j == 0 else "=0"),
        ("IN: other equity or grants", lambda col, j: f"={I['cashflow.other_equity']}" if j == 0 else "=0"),
        ("Total in", None),
        ("OUT: cost of sales", lambda col, j: f"={S}!{col}{COS_ROW}"),
        ("OUT: staff (operating units, full from month one)", lambda col, j: f"={U1}*{HR_UNIT}"),
        ("OUT: staff (head office, year-one share)", lambda col, j: f"={I['cashflow.year1_head_office_share']}*{HO_HR}"),
        ("OUT: running costs, fixed (units)", lambda col, j: f"={U1}*{RUN_FIX}"),
        ("OUT: running costs, varying with volume (units)", lambda col, j: f"={U1}*{RUN_VAR}*{S}!{col}$5"),
        ("OUT: running costs (head office, year-one share)", lambda col, j: f"={I['cashflow.year1_head_office_share']}*{RUN_HO}"),
        ("OUT: start-up costs and capital assets (units)", lambda col, j: f"={U1}*({ONE_TIME}+{CAP_UNIT})" if j == 0 else "=0"),
        ("OUT: development and capital assets (head office)", lambda col, j: f"={DEV_HO}+{CAP_HO}" if j == 0 else "=0"),
        ("OUT: loan repayment", lambda col, j: "=$B$7"),
        ("Total out", None),
        ("Net cash flow", None),
        ("Opening balance", None),
        ("Closing balance", None),
        ("Stress: closing balance with revenue reduced", None),
    ]
    rowmap = {}
    for i, (lab, fn) in enumerate(lines14):
        rowmap[lab] = 10 + i
        ws.cell(row=10 + i, column=1, value=lab)
    for j in range(12):
        col = get_column_letter(2 + j)
        for lab, fn in lines14:
            r_ = rowmap[lab]
            if fn:
                ws.cell(row=r_, column=2 + j, value=fn(col, j)).number_format = MONEY
        ti, to = rowmap["Total in"], rowmap["Total out"]
        ws.cell(row=ti, column=2 + j, value=f"=SUM({col}10:{col}12)").number_format = MONEY
        ws.cell(row=to, column=2 + j, value=f"=SUM({col}14:{col}22)").number_format = MONEY
        net, op, cl, st = rowmap["Net cash flow"], rowmap["Opening balance"], rowmap["Closing balance"], rowmap["Stress: closing balance with revenue reduced"]
        ws.cell(row=net, column=2 + j, value=f"={col}{ti}-{col}{to}").number_format = MONEY
        prev = get_column_letter(1 + j)
        ws.cell(row=op, column=2 + j, value=f"={I['cashflow.opening_balance']}" if j == 0 else f"={prev}{cl}").number_format = MONEY
        ws.cell(row=cl, column=2 + j, value=f"={col}{op}+{col}{net}").number_format = MONEY
        base_prev = f"{I['cashflow.opening_balance']}" if j == 0 else f"{prev}{st}"
        ws.cell(row=st, column=2 + j, value=f"={base_prev}+{col}{net}-{col}10*{I['cashflow.stress_revenue_reduction']}").number_format = MONEY
    for lab in ("IN: sales", "Total in", "Total out", "Net cash flow"):
        r_ = rowmap[lab]
        ws.cell(row=r_, column=14, value=f"=SUM(B{r_}:M{r_})").number_format = MONEY
    for lab in ("Total in", "Total out", "Net cash flow", "Closing balance", "Stress: closing balance with revenue reduced"):
        ws[f"A{rowmap[lab]}"].font = BOLD
    lr = rowmap["Stress: closing balance with revenue reduced"] + 2
    cl, st = rowmap["Closing balance"], rowmap["Stress: closing balance with revenue reduced"]
    ws.cell(row=lr, column=1, value="Lowest closing balance in the year").font = BOLD
    ws.cell(row=lr, column=2, value=f"=MIN(B{cl}:M{cl})").number_format = MONEY
    ws.cell(row=lr + 1, column=1, value="Lowest closing balance under stress").font = BOLD
    ws.cell(row=lr + 1, column=2, value=f"=MIN(B{st}:M{st})").number_format = MONEY
    ws.cell(row=lr + 2, column=1, value="Closing balance, month twelve")
    ws.cell(row=lr + 2, column=2, value=f"=M{cl}").number_format = MONEY
    ws.cell(row=lr + 3, column=1, value="Cash needed = −(lowest closing balance) if negative, else zero")
    ws.cell(row=lr + 3, column=2, value=f"=MAX(0,-B{lr})").number_format = MONEY
    ws.cell(row=lr + 4, column=1, value="Cash needed under stress")
    ws.cell(row=lr + 4, column=2, value=f"=MAX(0,-B{lr+1})").number_format = MONEY
    b.name("lowest_closing_balance", ws, f"B{lr}", "Lowest closing cash balance in year one")
    b.name("lowest_closing_balance_stress", ws, f"B{lr+1}", "Lowest closing cash balance in year one under the revenue stress test")
    b.name("closing_balance_month12", ws, f"B{lr+2}", "Closing cash balance at the end of year one")
    b.name("cash_needed", ws, f"B{lr+3}", "Extra cash needed to keep the balance at or above zero")
    b.name("cash_needed_stress", ws, f"B{lr+4}", "Extra cash needed under the stress test")
    CASH_CHAIN = (f"M{cl}", f"B{rowmap['Opening balance']}", f"B{rowmap['Net cash flow']}", f"M{rowmap['Net cash flow']}")
    ws.freeze_panes = "B10"

    # ---- 15 Roll-out (the forecast's drivers: units by year, loan schedule, capital spend) ---
    FC = R["forecast"]
    NY = len(FC)
    ycols = [get_column_letter(2 + j) for j in range(NY)]          # B.. one column per year
    D4 = "'4 Depreciation'"
    ws = b.sheet("15 Roll-out", [56] + [14] * NY)
    b.title(ws, "Roll-out — operating units by year, the loan schedule and capital spend",
            "Drives tabs 16 to 18. A cohort of units opens at the start of its year and follows the year-one volume profile on tab 13; "
            "units already open run at steady state. Blue cells are inputs.")
    ws["A4"] = "Year"
    ws["A4"].font = BOLD
    for j, col in enumerate(ycols):
        ws[f"{col}4"] = j + 1
        ws[f"{col}4"].font = BOLD
    ro = {}  # label -> row
    lines15 = [
        ("Operating units open at the year end", "units"),
        ("New units opened in the year", "new"),
        ("Unit-months at steady-state volume = 12 × units open last year + new units × sum of the ramp", "um"),
        ("Head-office share staffed and run", "share"),
        ("Equity raised in the year", "equity"),
        ("", None),
        ("Loan drawn", "loan_in"),
        ("Loan balance at the start of the year", "bal_open"),
        ("Loan balance at the end of the year", "bal_close"),
        ("Loan payments in the year", "payments"),
        ("Loan principal repaid = start balance − end balance", "principal"),
        ("Loan interest = payments − principal", "interest"),
        ("", None),
        ("Capital spend on new units and, in year one, head office", "capex_new"),
        ("Replacement of unit assets at the end of their life", "rep_unit"),
        ("Replacement of head-office assets at the end of their life", "rep_ho"),
        ("Fixed assets, net book value at the start of the year", "nbv_open"),
        ("Depreciation charge = 12 × (per-unit depreciation × units + head-office depreciation), capped at what is left to write off", "dep"),
        ("Fixed assets, net book value at the end of the year", "nbv"),
    ]
    for i, (lab, key) in enumerate(lines15):
        ro[key] = 5 + i
        ws.cell(row=5 + i, column=1, value=lab)
    MROW = 5 + len(lines15) + 1          # the cohort matrix header row
    L_, RATE_, N_ = I["cashflow.loan_amount"], I["cashflow.loan_rate_annual"], I["cashflow.loan_term_months"]
    P_ = "'14 Cash flow'!$B$7"
    RAMP_SUM = "SUM('13 Sales'!$B$5:$M$5)"
    for j, col in enumerate(ycols):
        y = f"{col}$4"
        prev = ycols[j - 1] if j else None
        fy = FC[j]
        c = ws.cell(row=ro["units"], column=2 + j, value=fy["units"]); c.font, c.number_format = INPUT, NUM
        nm = f"in_forecast_units_open_year_{j+1}"
        b.name(nm, ws, f"{col}{ro['units']}", f"Operating units open at the end of year {j+1}")
        LINE_VALUES[nm] = fy["units"]
        ws.cell(row=ro["new"], column=2 + j, value=f"={col}{ro['units']}" if j == 0 else f"={col}{ro['units']}-{prev}{ro['units']}").number_format = NUM
        ws.cell(row=ro["um"], column=2 + j, value=(f"={col}{ro['new']}*{RAMP_SUM}" if j == 0 else
                                                     f"=12*{prev}{ro['units']}+{col}{ro['new']}*{RAMP_SUM}")).number_format = '#,##0.0'
        c = ws.cell(row=ro["share"], column=2 + j, value=fy["share"]); c.font, c.number_format = INPUT, PCT
        nm = f"in_forecast_head_office_share_year_{j+1}"
        b.name(nm, ws, f"{col}{ro['share']}", f"Share of the at-scale head office staffed and run in year {j+1}")
        LINE_VALUES[nm] = fy["share"]
        c = ws.cell(row=ro["equity"], column=2 + j, value=fy["equity"]); c.font, c.number_format = INPUT, MONEY
        nm = f"in_forecast_equity_raised_year_{j+1}"
        b.name(nm, ws, f"{col}{ro['equity']}", f"Equity raised in year {j+1}")
        LINE_VALUES[nm] = fy["equity"]
        ws.cell(row=ro["loan_in"], column=2 + j, value=f"={L_}" if j == 0 else "=0").number_format = MONEY
        ws.cell(row=ro["bal_open"], column=2 + j, value=f"={L_}" if j == 0 else f"={prev}{ro['bal_close']}").number_format = MONEY
        k1 = f"(12*{y})"
        ws.cell(row=ro["bal_close"], column=2 + j,
                value=f"=IF({k1}>={N_},0,IF({RATE_}=0,MAX(0,{L_}-{P_}*{k1}),"
                      f"MAX(0,{L_}*(1+{RATE_}/12)^{k1}-{P_}*((1+{RATE_}/12)^{k1}-1)/({RATE_}/12))))").number_format = MONEY
        ws.cell(row=ro["payments"], column=2 + j, value=f"={P_}*MIN(12,MAX(0,{N_}-12*({y}-1)))").number_format = MONEY
        ws.cell(row=ro["principal"], column=2 + j, value=f"={col}{ro['bal_open']}-{col}{ro['bal_close']}").number_format = MONEY
        ws.cell(row=ro["interest"], column=2 + j, value=f"={col}{ro['payments']}-{col}{ro['principal']}").number_format = MONEY
        ws.cell(row=ro["capex_new"], column=2 + j,
                value=f"={CAP_UNIT}*{col}{ro['new']}" + (f"+{CAP_HO}" if j == 0 else "")).number_format = MONEY
        mcol = get_column_letter(3 + j)   # the matrix's year columns start at C
        ws.cell(row=ro["rep_unit"], column=2 + j,
                value=f"=SUMPRODUCT($B${MROW+1}:$B${MROW+NY},{mcol}{MROW+1}:{mcol}{MROW+NY})").number_format = MONEY
        terms = []
        for r4 in HO_ASSET_ROWS:
            life = f"{D4}!$C${r4}"
            terms.append(f"(INT((12*{y}-1)/{life})-INT((12*({y}-1)-1)/{life}))*{D4}!$B${r4}*{D4}!$E${r4}")
        ws.cell(row=ro["rep_ho"], column=2 + j, value=f"=IF({y}>1,{'+'.join(terms) if terms else '0'},0)").number_format = MONEY
        ws.cell(row=ro["nbv_open"], column=2 + j, value="=0" if j == 0 else f"={prev}{ro['nbv']}").number_format = MONEY
        spend = f"{col}{ro['nbv_open']}+{col}{ro['capex_new']}+{col}{ro['rep_unit']}+{col}{ro['rep_ho']}"
        ws.cell(row=ro["dep"], column=2 + j, value=f"=MIN(12*({DEP_UNIT}*{col}{ro['units']}+{DEP_HO}),{spend})").number_format = MONEY
        ws.cell(row=ro["nbv"], column=2 + j, value=f"={spend}-{col}{ro['dep']}").number_format = MONEY
    for key in ("units", "bal_close", "nbv"):
        ws[f"A{ro[key]}"].font = BOLD
    # the cohort matrix: replacement cost per unit, by cohort and year
    b.header(ws, MROW, ["Cohort (year the units opened)", "Units in the cohort"] + [f"Year {j+1}" for j in range(NY)])
    ws.cell(row=MROW - 1, column=1, value="Replacement cost per unit of each cohort, by year — an asset bought in month one of the cohort's "
            "first year is replaced in the year that holds the month after its life ends").font = NOTE
    for c_ in range(1, NY + 1):
        r_ = MROW + c_
        ws.cell(row=r_, column=1, value=c_)
        ws.cell(row=r_, column=2, value=f"={ycols[c_-1]}${ro['new']}").number_format = NUM
        for j, col in enumerate(ycols):
            mcol = get_column_letter(3 + j)
            y = f"{col}$4"
            terms = []
            for r4 in UNIT_ASSET_ROWS:
                life = f"{D4}!$C${r4}"
                terms.append(f"(INT((12*({y}-$A{r_}+1)-1)/{life})-INT((12*({y}-$A{r_})-1)/{life}))*{D4}!$B${r4}*{D4}!$E${r4}")
            ws.cell(row=r_, column=3 + j, value=f"=IF({y}>$A{r_},{'+'.join(terms) if terms else '0'},0)").number_format = MONEY
    ws.freeze_panes = "B5"
    RO = "'15 Roll-out'"

    # ---- 16 Forecast P&L ---------------------------------------------------------------------
    ws = b.sheet("16 Forecast P&L", [58] + [14] * (NY + 1))
    b.title(ws, f"Forecast profit and loss — years one to {NY}",
            "Conventional accounting: start-up costs and head-office development are charged when paid; tax is charged on profit after "
            "losses brought forward. Costs are negative.")
    b.header(ws, 4, ["Line"] + [f"Year {j+1}" for j in range(NY)] + ["Total"])
    pl = {}
    lines16 = [
        ("Revenue", "revenue", lambda col, j: f"={REV}*{RO}!{col}{ro['um']}"),
        ("Cost of sales", "cos", lambda col, j: f"=-{COGS}*{RO}!{col}{ro['um']}"),
        ("Gross profit", "gp", lambda col, j: f"={col}{pl['revenue']}+{col}{pl['cos']}"),
        ("Staff — operating units", "staff_units", lambda col, j: f"=-{HR_UNIT}*12*{RO}!{col}{ro['units']}"),
        ("Staff — head office", "staff_ho", lambda col, j: f"=-{HO_HR}*12*{RO}!{col}{ro['share']}"),
        ("Running costs — operating units", "run_units", lambda col, j: f"=-({RUN_FIX}*12*{RO}!{col}{ro['units']}+{RUN_VAR}*{RO}!{col}{ro['um']})"),
        ("Running costs — head office", "run_ho", lambda col, j: f"=-{RUN_HO}*12*{RO}!{col}{ro['share']}"),
        ("Start-up costs of new units", "startup", lambda col, j: f"=-{ONE_TIME}*{RO}!{col}{ro['new']}"),
        ("Head-office development", "dev", lambda col, j: f"=-{DEV_HO}" if j == 0 else "=0"),
        ("Depreciation", "dep", lambda col, j: f"=-{RO}!{col}{ro['dep']}"),
        ("Operating profit", "op", lambda col, j: f"={col}{pl['gp']}+SUM({col}{pl['staff_units']}:{col}{pl['dep']})"),
        ("Loan interest", "interest", lambda col, j: f"=-{RO}!{col}{ro['interest']}"),
        ("Profit before tax", "pbt", lambda col, j: f"={col}{pl['op']}+{col}{pl['interest']}"),
        ("Losses brought forward", "losses_bf", lambda col, j: "=0" if j == 0 else f"={ycols[j-1]}{pl['losses_cf']}"),
        ("Taxable profit = profit before tax less losses brought forward, not below zero", "taxable", lambda col, j: f"=MAX(0,{col}{pl['pbt']}-{col}{pl['losses_bf']})"),
        ("Tax", "tax", lambda col, j: f"=-{col}{pl['taxable']}*{I['finance.tax_rate']}"),
        ("Losses carried forward", "losses_cf", lambda col, j: f"=MAX(0,{col}{pl['losses_bf']}-MAX(0,{col}{pl['pbt']}))+MAX(0,-{col}{pl['pbt']})"),
        ("Profit after tax", "pat", lambda col, j: f"={col}{pl['pbt']}+{col}{pl['tax']}"),
    ]
    for i, (lab, key, fn) in enumerate(lines16):
        pl[key] = 5 + i
        ws.cell(row=5 + i, column=1, value=lab)
    tot_col = get_column_letter(2 + NY)
    for i, (lab, key, fn) in enumerate(lines16):
        r_ = pl[key]
        for j, col in enumerate(ycols):
            ws.cell(row=r_, column=2 + j, value=fn(col, j)).number_format = MONEY
        if key not in ("losses_bf", "losses_cf", "taxable"):
            ws.cell(row=r_, column=2 + NY, value=f"=SUM(B{r_}:{ycols[-1]}{r_})").number_format = MONEY
    for key in ("gp", "op", "pbt", "pat"):
        ws[f"A{pl[key]}"].font = BOLD
        for j in range(NY + 1):
            ws.cell(row=pl[key], column=2 + j).font = BOLD
    for j, col in enumerate(ycols):
        b.name(f"forecast_revenue_year_{j+1}", ws, f"{col}{pl['revenue']}", f"Forecast revenue, year {j+1}")
        b.name(f"forecast_operating_profit_year_{j+1}", ws, f"{col}{pl['op']}", f"Forecast operating profit, year {j+1}")
        b.name(f"forecast_profit_after_tax_year_{j+1}", ws, f"{col}{pl['pat']}", f"Forecast profit after tax, year {j+1}")
    b.name("forecast_revenue_total", ws, f"{tot_col}{pl['revenue']}", f"Forecast revenue over years one to {NY}")
    b.name("forecast_operating_profit_total", ws, f"{tot_col}{pl['op']}", f"Forecast operating profit over years one to {NY}")
    b.name("forecast_profit_after_tax_total", ws, f"{tot_col}{pl['pat']}", f"Forecast profit after tax over years one to {NY}")
    ws.freeze_panes = "B5"
    PL = "'16 Forecast P&L'"

    # ---- 17 Forecast cash flow ---------------------------------------------------------------
    ws = b.sheet("17 Forecast cash flow", [58] + [14] * (NY + 1))
    b.title(ws, f"Forecast cash flow — years one to {NY}",
            "Tax is paid the year after it is charged. Year one closes at the same balance as tab 14. Outflows are negative.")
    b.header(ws, 4, ["Line"] + [f"Year {j+1}" for j in range(NY)] + ["Total"])
    cfr = {}
    lines17 = [
        ("Operating profit", "op", lambda col, j: f"={PL}!{col}{pl['op']}"),
        ("Add back depreciation", "dep", lambda col, j: f"=-{PL}!{col}{pl['dep']}"),
        ("Loan interest paid", "interest", lambda col, j: f"={PL}!{col}{pl['interest']}"),
        ("Tax paid (the previous year's charge)", "tax_paid", lambda col, j: "=0" if j == 0 else f"={PL}!{ycols[j-1]}{pl['tax']}"),
        ("Cash from operations", "ops", lambda col, j: f"=SUM({col}{cfr['op']}:{col}{cfr['tax_paid']})"),
        ("Capital spend on new units and head office", "capex_new", lambda col, j: f"=-{RO}!{col}{ro['capex_new']}"),
        ("Replacement of assets", "rep", lambda col, j: f"=-({RO}!{col}{ro['rep_unit']}+{RO}!{col}{ro['rep_ho']})"),
        ("Cash used in investing", "inv", lambda col, j: f"={col}{cfr['capex_new']}+{col}{cfr['rep']}"),
        ("Loan drawn", "loan_in", lambda col, j: f"={RO}!{col}{ro['loan_in']}"),
        ("Loan principal repaid", "principal", lambda col, j: f"=-{RO}!{col}{ro['principal']}"),
        ("Equity raised", "equity", lambda col, j: f"={RO}!{col}{ro['equity']}"),
        ("Cash from financing", "fin", lambda col, j: f"=SUM({col}{cfr['loan_in']}:{col}{cfr['equity']})"),
        ("Net cash flow", "net", lambda col, j: f"={col}{cfr['ops']}+{col}{cfr['inv']}+{col}{cfr['fin']}"),
        ("Opening cash", "open", lambda col, j: f"={I['cashflow.opening_balance']}" if j == 0 else f"={ycols[j-1]}{cfr['close']}"),
        ("Closing cash", "close", lambda col, j: f"={col}{cfr['open']}+{col}{cfr['net']}"),
    ]
    for i, (lab, key, fn) in enumerate(lines17):
        cfr[key] = 5 + i
        ws.cell(row=5 + i, column=1, value=lab)
    for i, (lab, key, fn) in enumerate(lines17):
        r_ = cfr[key]
        for j, col in enumerate(ycols):
            ws.cell(row=r_, column=2 + j, value=fn(col, j)).number_format = MONEY
        if key not in ("open", "close"):
            ws.cell(row=r_, column=2 + NY, value=f"=SUM(B{r_}:{ycols[-1]}{r_})").number_format = MONEY
    for key in ("ops", "inv", "fin", "net", "close"):
        ws[f"A{cfr[key]}"].font = BOLD
    lc = cfr["close"] + 2
    ws.cell(row=lc, column=1, value="Lowest closing cash across the forecast").font = BOLD
    ws.cell(row=lc, column=2, value=f"=MIN(B{cfr['close']}:{ycols[-1]}{cfr['close']})").number_format = MONEY
    ws.cell(row=lc + 1, column=1, value="Extra funding needed over the forecast = −(lowest closing cash) if negative, else zero").font = BOLD
    ws.cell(row=lc + 1, column=2, value=f"=MAX(0,-B{lc})").number_format = MONEY
    for j, col in enumerate(ycols):
        b.name(f"forecast_closing_cash_year_{j+1}", ws, f"{col}{cfr['close']}", f"Forecast closing cash, end of year {j+1}")
    b.name("forecast_lowest_closing_cash", ws, f"B{lc}", "Lowest year-end cash balance across the forecast")
    b.name("forecast_funding_needed", ws, f"B{lc+1}", "Extra funding needed to keep year-end cash at or above zero across the forecast")
    ws.freeze_panes = "B5"
    CFT = "'17 Forecast cash flow'"

    # ---- 18 Forecast balance sheet ------------------------------------------------------------
    ws = b.sheet("18 Forecast balance sheet", [58] + [14] * NY)
    b.title(ws, f"Forecast balance sheet — at the end of years one to {NY}",
            "A cash business: no debtors, creditors or stock. Net assets must equal total equity in every year (last row reads zero).")
    b.header(ws, 4, ["Line"] + [f"Year {j+1}" for j in range(NY)])
    bs = {}
    lines18 = [
        ("Fixed assets, net book value", "nbv", lambda col, j: f"={RO}!{col}{ro['nbv']}"),
        ("Cash", "cash", lambda col, j: f"={CFT}!{col}{cfr['close']}"),
        ("Total assets", "assets", lambda col, j: f"={col}{bs['nbv']}+{col}{bs['cash']}"),
        ("Loan outstanding", "loan", lambda col, j: f"={RO}!{col}{ro['bal_close']}"),
        ("Tax payable", "tax", lambda col, j: f"=-{PL}!{col}{pl['tax']}"),
        ("Total liabilities", "liab", lambda col, j: f"={col}{bs['loan']}+{col}{bs['tax']}"),
        ("Net assets", "net", lambda col, j: f"={col}{bs['assets']}-{col}{bs['liab']}"),
        ("", None, None),
        ("Share capital — equity raised to date", "capital", lambda col, j: f"=SUM({RO}!$B${ro['equity']}:{col}{ro['equity']})"),
        ("Retained profit — profit after tax to date", "retained", lambda col, j: f"=SUM({PL}!$B${pl['pat']}:{col}{pl['pat']})"),
        ("Total equity", "equity", lambda col, j: f"={col}{bs['capital']}+{col}{bs['retained']}"),
        ("Net assets less total equity (must be zero)", "diff", lambda col, j: f"={col}{bs['net']}-{col}{bs['equity']}"),
    ]
    for i, (lab, key, fn) in enumerate(lines18):
        if key:
            bs[key] = 5 + i
        ws.cell(row=5 + i, column=1, value=lab)
    for i, (lab, key, fn) in enumerate(lines18):
        if not key:
            continue
        for j, col in enumerate(ycols):
            ws.cell(row=bs[key], column=2 + j, value=fn(col, j)).number_format = MONEY
    for key in ("assets", "liab", "net", "equity"):
        ws[f"A{bs[key]}"].font = BOLD
    for j, col in enumerate(ycols):
        b.name(f"forecast_net_assets_year_{j+1}", ws, f"{col}{bs['net']}", f"Forecast net assets, end of year {j+1}")
        b.name(f"forecast_loan_outstanding_year_{j+1}", ws, f"{col}{bs['loan']}", f"Loan outstanding, end of year {j+1}")
    ws.freeze_panes = "B5"
    BS_DIFF = (f"'18 Forecast balance sheet'!B{bs['diff']}", f"'18 Forecast balance sheet'!{ycols[-1]}{bs['diff']}")
    FC_Y1_CLOSE = f"{CFT}!B{cfr['close']}"
    FC_Y1_UNITS = f"{RO}!B{ro['units']}"

    # ---- 19 Check --------------------------------------------------------------------------
    ws = b.sheet("19 Check", [70, 18, 18, 12])
    b.title(ws, "Check — the headline figures recomputed a second way, and the forecast reconciled", "Every row must read PASS. If one reads FAIL the workbook has been edited in a way that broke it.")
    b.header(ws, 4, ["Check", "First value", "Second value", "Result"])
    cf = "'14 Cash flow'"
    checks = [
        ("Margin of safety on the pricing tab equals surplus ÷ whole cost on the unit P&L", f"={FMOS}", f"={FMOS_RE}"),
        ("At the required price, surplus ÷ whole cost equals the target margin of safety", f"={I['finance.target_margin']}", f"={FMOS_REQ_RE}"),
        ("Venture surplus equals units × unit surplus", f"={VENTURE_SURPLUS}", f"={VS_CHECK}"),
        ("Cash chain: closing month twelve = opening month one + sum of net cash flows", f"={cf}!{CASH_CHAIN[0]}", f"={cf}!{CASH_CHAIN[1]}+SUM({cf}!{CASH_CHAIN[2]}:{CASH_CHAIN[3]})"),
        ("Year-one volume equals units open × steady-state transactions × sum of the ramp", f"='13 Sales'!N{VOL_ROW}", f"={U1}*{TRANS}*SUM('13 Sales'!B5:M5)"),
        ("Whole cost per unit equals unit's own costs + head office allocation", f"={WHOLE}", f"={UNIT_OWN}+{HO_ALLOC}"),
        ("Margin of safety on the pricing tab equals the builder's own computation (base scenario only)", f"={FMOS}", f"={FMOS_GEN}"),
        ("Forecast year one opens the same number of units as the twelve-month forecast", f"={FC_Y1_UNITS}", f"={U1}"),
        ("Forecast year-one closing cash equals month twelve on the twelve-month forecast", f"={FC_Y1_CLOSE}", f"={cf}!{CASH_CHAIN[0]}"),
        ("Balance sheet balances in every forecast year — largest difference is zero", f"=MAX({BS_DIFF[0]}:{BS_DIFF[1].split('!')[1]})", "=0"),
        ("Balance sheet balances in every forecast year — smallest difference is zero", f"=MIN({BS_DIFF[0]}:{BS_DIFF[1].split('!')[1]})", "=0"),
    ]
    for i, (lab, f1, f2) in enumerate(checks):
        r_ = 5 + i
        ws.cell(row=r_, column=1, value=lab)
        ws.cell(row=r_, column=2, value=f1).number_format = '#,##0.0000'
        ws.cell(row=r_, column=3, value=f2).number_format = '#,##0.0000'
        if i == 6:
            ws.cell(row=r_, column=4, value=f'=IF({scen}<>1,"n/a",IF(ABS(B{r_}-C{r_})<0.00001,"PASS","FAIL"))')
        else:
            ws.cell(row=r_, column=4, value=f'=IF(ABS(B{r_}-C{r_})<0.00001,"PASS","FAIL")')
    ce = 4 + len(checks)
    ws.cell(row=ce + 2, column=1, value="All checks").font = BOLD
    ws.cell(row=ce + 2, column=4, value=f'=IF(COUNTIF(D5:D{ce},"FAIL")=0,"ALL CHECKS PASS","CHECK FAILED")').font = BOLD
    ws.cell(row=ce + 3, column=1, value="Scenario in force on tab 1 (1 = base)")
    ws.cell(row=ce + 3, column=4, value=f"={scen}")
    b.name("all_checks", ws, f"D{ce+2}", "ALL CHECKS PASS when every check row passes")

    # ---- write -----------------------------------------------------------------------------
    os.makedirs(out_dir, exist_ok=True)
    xlsx = os.path.join(out_dir, f"{slug}-business-case-evidence.xlsx")
    b.wb.save(xlsx)
    cells_md = os.path.join(out_dir, f"{slug}-business-case-evidence-cells.md")
    write_cell_index(b, m, R, xlsx, cells_md)
    return xlsx, cells_md, R


def inputs_value(m, key):
    return collect_inputs(m)[key]["value"]


def fmt_val(name, v):
    if isinstance(v, str):
        return v
    if any(t in name for t in ("fmos", "share", "rate", "penetration", "reduction", "margin", "uplift")):
        if isinstance(v, float) and abs(v) < 5:
            return f"{v:.1%}"
    if isinstance(v, float) and abs(v) < 100 and not float(v).is_integer():
        return f"{v:,.2f}"
    return f"{v:,.0f}"


LINE_VALUES = {}  # line-item defined names -> base value, filled while building


def write_cell_index(b, m, R, xlsx, path):
    """The cell index: every named cell, where it is, its base value. The document cites from this."""
    val_by_name = {
        "tam": R["tam"], "units": R["units"], "customers_per_unit": R["customers"],
        "transactions_per_unit": R["trans"], "transactions_venture": R["trans"] * R["units"],
        "revenue_per_unit": R["revenue"], "cogs_per_unit": R["cogs"], "headcount_per_unit": R["headcount"],
        "hr_cost_per_unit": R["hr_unit"], "ho_staff_cost": R["ho_hr"], "capital_per_unit": R["capital_unit"],
        "depreciation_per_unit": R["dep_unit"], "capital_head_office": R["capital_ho"],
        "depreciation_head_office": R["dep_ho"], "running_per_unit": R["running_unit"],
        "running_head_office": R["running_ho"], "startup_per_unit": R["startup_unit"],
        "startup_charge_per_unit": R["startup_unit_monthly"], "development_head_office": R["dev_ho"],
        "development_charge_per_month": R["dev_ho_monthly"], "returns_per_unit": R["returns_unit"],
        "returns_head_office": R["returns_ho"], "tax_per_unit": R["tax_unit"], "tax_head_office": R["tax_ho"],
        "unit_own_cost": R["unit_own_cost"], "ho_costs": R["ho_costs"], "ho_total": R["ho_total"],
        "ho_allocated_per_unit": R["ho_alloc"], "whole_cost_per_unit": R["unit_whole_cost"],
        "cost_per_transaction": R["cost_per_trans"], "margin_of_safety": R["fmos"], "interim_price": R["interim_price"],
        "verdict": R["verdict"], "required_price": R["required_price"], "binding_input": R["binding_input"],
        "margin_of_safety_worst_corner": R["fmos_worst_corner"], "unit_surplus": R["unit_surplus"],
        "unit_surplus_at_required": R["required_price"] * R["trans"] - R["unit_whole_cost"],
        "venture_surplus_per_month": R["venture_surplus"], "venture_surplus_per_year": R["venture_surplus"] * 12,
        "venture_revenue_per_month": R["revenue"] * R["units"],
        "year1_sales": sum(x["sales"] for x in R["months"]),
        "year1_volume": sum(m["cashflow"]["ramp_share_of_steady_state"]) * R["trans"] * float(m["cashflow"]["year1_units"]),
        "loan_repayment_per_month": R["loan_payment"], "lowest_closing_balance": R["min_closing"],
        "lowest_closing_balance_stress": R["min_closing_stress"], "closing_balance_month12": R["months"][-1]["closing"],
        "cash_needed": max(0.0, -R["min_closing"]), "cash_needed_stress": max(0.0, -R["min_closing_stress"]),
        "all_checks": "ALL CHECKS PASS", "scenario": 1,
        "price_uplift_to_target": R["uplift"], "margin_from_failure": R["fmos"] - FMOS_BORDER,
        "price_fall_to_floor": R["interim_price"] - R["cost_per_trans"] * (1 + FMOS_BORDER),
        "forecast_revenue_total": sum(y["revenue"] for y in R["forecast"]),
        "forecast_operating_profit_total": sum(y["op"] for y in R["forecast"]),
        "forecast_profit_after_tax_total": sum(y["pat"] for y in R["forecast"]),
        "forecast_lowest_closing_cash": min(y["cash"] for y in R["forecast"]),
        "forecast_funding_needed": max(0.0, -min(y["cash"] for y in R["forecast"])),
    }
    for y in R["forecast"]:
        n_ = y["year"]
        val_by_name[f"forecast_revenue_year_{n_}"] = y["revenue"]
        val_by_name[f"forecast_operating_profit_year_{n_}"] = y["op"]
        val_by_name[f"forecast_profit_after_tax_year_{n_}"] = y["pat"]
        val_by_name[f"forecast_closing_cash_year_{n_}"] = y["cash"]
        val_by_name[f"forecast_net_assets_year_{n_}"] = y["net_assets"]
        val_by_name[f"forecast_loan_outstanding_year_{n_}"] = y["bal_close"]
    for i, p in enumerate(m["products"]):
        val_by_name[f"required_price_product_{i+1}"] = inputs_value(m, f"product.{i}.price") * R["uplift"]
    inputs = collect_inputs(m)
    cur = m["venture"].get("currency", "GBP")
    with open(path, "w") as f:
        f.write(f"# Cell index — {m['venture']['name']} business-case evidence workbook\n\n")
        f.write(f"Workbook: `{os.path.basename(xlsx)}` · built from the model data file on {m['venture'].get('date', '')} · currency {cur}.\n\n")
        f.write("Cite a figure in the business case as its name in this table, for example `margin_of_safety` or `cost_per_transaction`. "
                "Every name is also a defined name inside the workbook. Values are at the base scenario; the workbook recomputes them live.\n\n")
        f.write("## Results\n\n| Name | Cell | Base value | Meaning |\n|---|---|---|---|\n")
        for nm, (ref, desc) in b.names.items():
            if nm.startswith("in_") or nm.startswith("line_"):
                continue
            v = val_by_name.get(nm, "")
            f.write(f"| `{nm}` | {ref} | {fmt_val(nm, v)} | {desc} |\n")
        f.write("\n## Line items (tabs 3 to 6 — the amounts entered for each asset, running cost, start-up and development line)\n\n| Name | Cell | Base value | Meaning |\n|---|---|---|---|\n")
        for nm, (ref, desc) in b.names.items():
            if nm.startswith("line_"):
                f.write(f"| `{nm}` | {ref} | {fmt_val(nm, LINE_VALUES.get(nm, ''))} | {desc} |\n")
        f.write("\n## Forecast inputs (tab 15 — units open, head-office share and equity raised, by year)\n\n| Name | Cell | Base value | Meaning |\n|---|---|---|---|\n")
        for nm, (ref, desc) in b.names.items():
            if nm.startswith("in_forecast_"):
                f.write(f"| `{nm}` | {ref} | {fmt_val(nm, LINE_VALUES.get(nm, ''))} | {desc} |\n")
        f.write("\n## Inputs (tab 1, Master Control)\n\n| Name | Cell | Base | Low | High | Tier | Source |\n|---|---|---|---|---|---|---|\n")
        for k, v in inputs.items():
            nm = "in_" + k.replace(".", "_").replace(" ", "_").lower()
            ref = b.names[nm][0]
            fv = (lambda x: f"{x:.1%}" if v["unit"] == "share" else f"{x:,.10g}")
            f.write(f"| `{nm}` | {ref} | {fv(v['value'])} | {fv(v['low'])} | {fv(v['high'])} | {v['tier']} | {v['source']} |\n")
        f.write("\n## Sensitivity (one input at a time to its adverse end, worst first)\n\n| Input | End | Margin of safety | Change |\n|---|---|---|---|\n")
        for k, end, val, fm, d in R["sensitivity"]:
            f.write(f"| {label_for(k, m)} | {end} | {fm:.1%} | {d:+.1%} |\n")
        f.write(f"\nBinding input: **{R['binding_input']}**. Margin of safety at the worst corner (every input adverse): **{R['fmos_worst_corner']:.1%}**. "
                f"Verdict at base: **{R['verdict']}** ({R['fmos']:.1%} against a 25% gate).\n")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    with open(sys.argv[1]) as f:
        m = yaml.safe_load(f)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(sys.argv[1]))
    xlsx, cells, R = build(m, out_dir)
    print(f"workbook:   {xlsx}")
    print(f"cell index: {cells}")
    print(f"units {R['units']} · transactions/unit/month {R['trans']:,.0f} · cost per transaction {R['cost_per_trans']:,.2f} · "
          f"interim price {R['interim_price']:,.2f} · margin of safety {R['fmos']:.1%} {R['verdict']} · required price {R['required_price']:,.2f} · "
          f"binding input: {R['binding_input']} · worst corner {R['fmos_worst_corner']:.1%}")


if __name__ == "__main__":
    main()
