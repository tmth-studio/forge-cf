#!/usr/bin/env python3
"""Price at zero net present value: information only, for the simulation page.

Owner: Head of R&D. Source: RD-063 FIT price test, 6 November 2026, section 9, on the
Head of Verification's ruling of the same date. The printed words are that ruling's.

The line on the simulation page has no pass mark and is information. When run with price
low and every cost input at its high end, the result is the required price for the FIT
reading, and item 30 v0.4 reads it. The printed line stays as it is, and it stays off the
Check tab, the workbook and the business case. The builder does not import this file, and
nothing here writes to a workbook, the cells index or a readings block. It reads a model
file through the live builder and prints text.

Form, in our words, from the FIT financial model guide, Valuation section, read on the FIT
site on 6 November 2026. FIT did not produce these figures and does not endorse them.
  terminal value = at-scale annual net cash flow / discount rate, no growth
  net present value = discounted monthly flows + discounted terminal value
  price moves until net present value is zero, all other inputs fixed

Treatments this file fixes, none settled by the guide (RD-063 test, section 3):
  after tax at the model's rate, losses carried forward; working capital paid when a unit
  opens and never recovered; replacement at steady state equal to depreciation; all costs
  held fixed; all money put in earns the rate; debt only through a funding file.

Run:  python3 -B zero_npv_price.py <model.yaml> [--funding funding.yaml] [--unit-word transaction]
Checks: test_zero_npv_price.py
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yaml  # noqa: E402

import generate_business_case_xlsx as G  # noqa: E402

RATES = (0.25, 0.40)
GUIDE_READ = "6 November 2026"
SYMBOLS = {"GBP": "£", "USD": "$", "EUR": "€"}
WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


class FundingRefused(ValueError):
    """A funding file that does not meet the Head of Verification's conditions."""


def read_model(path):
    with open(path, encoding="utf-8") as f:
        m = yaml.safe_load(f)
    inputs = G.collect_inputs(m)
    vals = {k: v["value"] for k, v in inputs.items()}
    return m, G.compute(m, vals), vals, inputs


def plan(m, r, full):
    """Units and head office share by year. Full scale extends in equal steps to year seven."""
    fc = m["forecast"]
    units = [float(x) for x in fc["units_open_by_year"]]
    share = [float(x) for x in fc["head_office_share_by_year"]]
    if full and units[-1] < r["units"] - 1e-9:
        steps = max(7 - len(units), 1)
        u0, s0 = units[-1], share[-1]
        for i in range(1, steps + 1):
            units.append(u0 + (r["units"] - u0) * i / steps)
            share.append(s0 + (max(1.0, s0) - s0) * i / steps)
    return units, share


def asset_lines(m, r):
    unit = []
    for a in m["assets"]["unit"]:
        q = r["headcount"] if a.get("quantity_driver") == "per_head" else a.get("quantity", 1)
        unit.append((a["cost"] * q, a["life_months"]))
    head = [(a["cost"] * a.get("quantity", 1), a["life_months"]) for a in m["assets"]["head_office"]]
    return unit, head


def monthly(m, r, units, share):
    """Monthly transactions and cash lines, plus the steady state read after the last month."""
    ramp = m["cashflow"]["ramp_share_of_steady_state"]
    years = len(units)
    unit_assets, head_assets = asset_lines(m, r)
    opened = [units[0]] + [units[i] - units[i - 1] for i in range(1, years)]
    rows = []
    for t in range(1, 12 * years + 1):
        y, mi = (t - 1) // 12, (t - 1) % 12
        active = sum(opened[:y]) + opened[y] * ramp[mi]
        running = (r["cogs"] * active + r["hr_unit"] * units[y] + r["ho_hr"] * share[y]
                   + r["running_unit_fixed"] * units[y] + r["running_unit_variable"] * active
                   + r["running_ho"] * share[y])
        once = capex = 0.0
        if mi == 0:
            once += r["one_time_unit"] * opened[y]
            capex += (r["capital_unit"] + r["wc_unit"]) * opened[y]
        if t == 1:
            once += r["dev_ho"]
            capex += r["capital_ho"]
        for c in range(y + 1):
            start = 12 * c + 1
            for cost, life in unit_assets:
                if t > start and (t - start) % int(life) == 0:
                    capex += cost * opened[c]
        for cost, life in head_assets:
            if t > 1 and (t - 1) % int(life) == 0:
                capex += cost
        rows.append({"y": y, "trans": r["trans"] * active, "opx": running, "once": once, "capex": capex,
                     "dep": r["dep_unit"] * units[y] + r["dep_ho"]})
    steady = {
        "trans": r["trans"] * units[-1],
        "opx": (r["cogs"] + r["hr_unit"] + r["running_unit"]) * units[-1] + (r["ho_hr"] + r["running_ho"]) * share[-1],
        "dep": r["dep_unit"] * units[-1] + r["dep_ho"],
    }
    return rows, steady


def npv(price, rows, steady, rate, tax):
    monthly_rate = (1 + rate) ** (1 / 12) - 1
    total = losses = year_profit = 0.0
    for i, x in enumerate(rows):
        t = i + 1
        revenue = price * x["trans"]
        cash = revenue - x["opx"] - x["once"] - x["capex"]
        year_profit += revenue - x["opx"] - x["once"] - x["dep"]
        if t % 12 == 0:
            taxable = max(0.0, year_profit - losses)
            losses = max(0.0, losses - max(0.0, year_profit)) + max(0.0, -year_profit)
            cash -= taxable * tax
            year_profit = 0.0
        total += cash / (1 + monthly_rate) ** t
    profit = 12 * (price * steady["trans"] - steady["opx"] - steady["dep"])
    after_tax = profit - max(0.0, profit) * tax
    return total + (after_tax / rate) / (1 + monthly_rate) ** len(rows)


def solve(rows, steady, rate, tax):
    lo, hi = 0.0, 1.0
    while npv(hi, rows, steady, rate, tax) < 0:
        hi *= 2
        if hi > 1e12:
            raise ValueError("no price reaches zero net present value")
    for _ in range(100):
        mid = (lo + hi) / 2
        if npv(mid, rows, steady, rate, tax) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def read_funding(funding):
    """Apply the conditions in the ruling. Refuse a line, never guess one."""
    funding = funding or {}
    debt = funding.get("debt")
    if debt:
        for key in ("lender", "share", "rate", "rate_source", "share_source"):
            if debt.get(key) in (None, ""):
                raise FundingRefused(f"debt line refused: {key} is missing. A lender's rate needs a share too.")
        if not 0 < float(debt["share"]) < 1:
            raise FundingRefused("debt line refused: share must be above 0 and below 1.")
        for key in ("rate_source", "share_source"):
            if not re.search(r"\b(19|20)\d\d\b", str(debt[key])):
                raise FundingRefused(f"debt line refused: {key} carries no dated source.")
    allocator = funding.get("allocator")
    if allocator and not allocator.get("confidential"):
        for key in ("rate", "set_by", "source"):
            if allocator.get(key) in (None, ""):
                raise FundingRefused(f"allocator line refused: {key} is missing.")
        if not re.search(r"\b(19|20)\d\d\b", str(allocator["source"])):
            raise FundingRefused("allocator line refused: source carries no date.")
    return funding


def say(n):
    """Numbers in prose: one to nine spelled out, numerals from 10."""
    n = round(float(n), 1)
    if n == int(n):
        n = int(n)
        return WORDS.get(n, f"{n:,}")
    return f"{n:,}"


def money(x, cur):
    sym = SYMBOLS.get(cur, cur + " ")
    return f"{sym}{x:,.0f}" if abs(x) >= 100 else f"{sym}{x:,.2f}"


def pct(x):
    return f"{100 * x:g}"


def read(m, r, vals, inputs, funding=None):
    """All figures for the block, as data. No comparison is calculated here, by design."""
    funding = read_funding(funding)
    tax = vals["finance.tax_rate"]
    fu, fs = plan(m, r, True)
    pu, ps = plan(m, r, False)
    frows, fss = monthly(m, r, fu, fs)
    prows, pss = monthly(m, r, pu, ps)
    out = {
        "full": [solve(frows, fss, d, tax) for d in RATES],
        "own": [solve(prows, pss, d, tax) for d in RATES],
        "plan_units": pu[-1], "plan_years": len(pu), "full_years": len(fu), "units": r["units"],
        "price": r["interim_price"], "tax": tax, "own_rate": vals["finance.cost_of_capital"],
        "assumed": sum(1 for v in inputs.values() if str(v.get("tier", "")) in ("4", "T4")),
        "untiered": sum(1 for v in inputs.values() if v.get("tier") in (None, "")),
        "inputs": len(inputs),
    }
    debt = funding.get("debt")
    if debt:
        s, rd = float(debt["share"]), float(debt["rate"])
        out["debt"] = [solve(frows, fss, s * rd + (1 - s) * d, tax) for d in RATES]
    allocator = funding.get("allocator")
    if allocator and not allocator.get("confidential"):
        out["allocator"] = solve(frows, fss, float(allocator["rate"]), tax)
    return out


def block(m, x, funding=None, unit_word="transaction"):
    """The printed block, in the words the Head of Verification ruled on 6 November 2026."""
    funding = funding or {}
    cur = m["venture"].get("currency", "GBP")
    a, b = (money(v, cur) for v in x["full"])
    c, d = (money(v, cur) for v in x["own"])
    u = x["untiered"]
    no_tier = f" {say(u).capitalize()} {'carries' if u == 1 else 'carry'} no tier." if u else ""
    lines = [
        "Price at zero net present value: information only",
        f"Per {unit_word}, at 25 to 40 per cent a year. Full scale: {a} to {b}. "
        f"End of the run's own plan ({say(x['plan_units'])} of {say(x['units'])} units): {c} to {d}. "
        f"The run's price: {money(x['price'], cur)}.",
        "This line has no pass mark. It changes no checklist item, margin test or verdict. "
        "It is not the price clearing 25 per cent margin, the capital bar or the full unit cost in any result target.",
        f"Form: our reading of the valuation method in the FIT financial model guide, read {GUIDE_READ}. "
        "FIT did not produce this figure and does not endorse it.",
        f"Inputs: central values from this model, not validated. {say(x['assumed']).capitalize()} of {say(x['inputs'])} inputs "
        f"are assumed (tier 4).{no_tier} It is not read at the worst case.",
        f"Treatment: after tax at {pct(x['tax'])} per cent. Working capital is paid and never recovered. "
        "No growth after scaling. Replacement equals depreciation. All costs are held fixed, including any that could move with price.",
        "Funding: all money put in, early losses included, earns this return. No debt.",
        f"The cost floor already carries a charge for return at this model's own rate, {pct(x['own_rate'])} per cent. "
        "That rate is not the rate on this line.",
    ]
    if x["plan_units"] < x["units"] - 1e-9:
        lines.append(f"The full-scale reading extends the plan in equal steps from {say(x['plan_units'])} units in year "
                     f"{say(x['plan_years'])} to {say(x['units'])} units in year {say(x['full_years'])}. "
                     "The run's plan does not contain that extension.")
    else:
        lines.append("The plan reaches full scale, so the two readings are the same.")
    if funding.get("named_no_rate"):
        lines.append(f"The record names {funding['named_no_rate']} with no sourced rate, so it is not counted here.")
    debt = funding.get("debt")
    if debt:
        e, f = (money(v, cur) for v in x["debt"])
        lines.append(f"With debt: {e} to {f}. Of the money put in, {pct(float(debt['share']))} per cent comes from "
                     f"{debt['lender']} at {pct(float(debt['rate']))} per cent. The rest earns 25 to 40 per cent. "
                     f"Rate source: {debt['rate_source']}. Share source: {debt['share_source']}.")
    allocator = funding.get("allocator")
    if allocator:
        if allocator.get("confidential"):
            lines.append("The capital allocator set a confidential rate for this run. It is not printed.")
        else:
            lines.append(f"At the rate set by the capital allocator: {money(x['allocator'], cur)} at "
                         f"{pct(float(allocator['rate']))} per cent. Set by {allocator['set_by']}, {allocator['source']}.")
    return "\n\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Print the zero net present value block for a simulation page.")
    ap.add_argument("model")
    ap.add_argument("--funding", help="optional file: debt, allocator or named_no_rate")
    ap.add_argument("--unit-word", default="transaction", help="what one price buys; the price is per transaction")
    a = ap.parse_args()
    funding = None
    if a.funding:
        with open(a.funding, encoding="utf-8") as f:
            funding = yaml.safe_load(f)
    m, r, vals, inputs = read_model(a.model)
    print(block(m, read(m, r, vals, inputs, funding), funding, a.unit_word), end="")


if __name__ == "__main__":
    main()
