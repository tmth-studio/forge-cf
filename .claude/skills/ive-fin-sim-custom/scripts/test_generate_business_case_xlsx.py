#!/usr/bin/env python3
"""Test the business-case workbook generator.

Builds the workbook from example-model.yaml, then evaluates every formula in it with the
`formulas` package (an independent spreadsheet engine — not Excel, not this script) and
compares the named cells with the Python model. If the two agree, the formulas in the
workbook say what the model says. Also asserts the Check tab reads ALL CHECKS PASS.

    python3 test_generate_business_case_xlsx.py
Prints one line: PASS or FAIL with the first mismatch.
Requires: pyyaml, openpyxl, formulas (pip3 install formulas).
"""

import os
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate_business_case_xlsx as gen  # noqa: E402


def evaluate(xlsx):
    import formulas
    model = formulas.ExcelModel().loads(xlsx).finish()
    sol = model.calculate()
    out = {}
    for k, v in sol.items():
        key = k.upper().replace("'", "")  # "'[file]1 MASTER'!B4" -> "[FILE]1 MASTER!B4"
        key = key.split("]", 1)[1] if "]" in key else key
        val = v.value if hasattr(v, "value") else v
        try:
            val = val[0][0]
        except Exception:
            pass
        out[key] = val
    return out


def cell_key(ref):
    # "'1 Master'!$B$4" -> "1 MASTER!B4"
    return ref.replace("'", "").replace("$", "").upper()


def main():
    with open(os.path.join(HERE, "example-model.yaml")) as f:
        m = yaml.safe_load(f)
    tmp = tempfile.mkdtemp()
    xlsx, cells_md, R = gen.build(m, tmp)
    assert os.path.exists(cells_md)

    # names -> refs, from a fresh Book pass (build() does not return it) — re-read the workbook's defined names
    from openpyxl import load_workbook
    wb = load_workbook(xlsx)
    names = {n: dn.attr_text for n, dn in wb.defined_names.items()}

    vals = evaluate(xlsx)
    expect = {
        "tam": R["tam"], "units": R["units"], "customers_per_unit": R["customers"],
        "transactions_per_unit": R["trans"], "revenue_per_unit": R["revenue"], "cogs_per_unit": R["cogs"],
        "headcount_per_unit": R["headcount"], "hr_cost_per_unit": R["hr_unit"], "ho_staff_cost": R["ho_hr"],
        "capital_per_unit": R["capital_unit"], "depreciation_per_unit": R["dep_unit"],
        "running_per_unit": R["running_unit"], "running_head_office": R["running_ho"],
        "startup_per_unit": R["startup_unit"], "startup_charge_per_unit": R["startup_unit_monthly"],
        "returns_per_unit": R["returns_unit"], "tax_per_unit": R["tax_unit"], "ho_total": R["ho_total"],
        "ho_allocated_per_unit": R["ho_alloc"], "whole_cost_per_unit": R["unit_whole_cost"],
        "cost_per_transaction": R["cost_per_trans"], "margin_of_safety": R["fmos"], "interim_price": R["interim_price"],
        "required_price": R["required_price"], "unit_surplus": R["unit_surplus"],
        "venture_surplus_per_month": R["venture_surplus"],
        "year1_sales": sum(x["sales"] for x in R["months"]),
        "loan_repayment_per_month": R["loan_payment"], "lowest_closing_balance": R["min_closing"],
        "lowest_closing_balance_stress": R["min_closing_stress"],
        "closing_balance_month12": R["months"][-1]["closing"],
        "forecast_revenue_total": sum(y["revenue"] for y in R["forecast"]),
        "forecast_profit_after_tax_total": sum(y["pat"] for y in R["forecast"]),
        "forecast_lowest_closing_cash": min(y["cash"] for y in R["forecast"]),
        "forecast_funding_needed": max(0.0, -min(y["cash"] for y in R["forecast"])),
    }
    for y in R["forecast"]:
        n_ = y["year"]
        expect[f"forecast_revenue_year_{n_}"] = y["revenue"]
        expect[f"forecast_operating_profit_year_{n_}"] = y["op"]
        expect[f"forecast_profit_after_tax_year_{n_}"] = y["pat"]
        expect[f"forecast_closing_cash_year_{n_}"] = y["cash"]
        expect[f"forecast_net_assets_year_{n_}"] = y["net_assets"]
        expect[f"forecast_loan_outstanding_year_{n_}"] = y["bal_close"]
    # the balance sheet must balance and year one of the forecast must land on the twelve-month forecast
    for y in R["forecast"]:
        if abs(y["net_assets"] - (y["share_capital"] + y["retained"])) > 1e-6:
            failures_pre = f"balance sheet does not balance in year {y['year']}"
            print("FAIL — " + failures_pre)
            sys.exit(1)
    if abs(R["forecast"][0]["cash"] - R["months"][-1]["closing"]) > 1e-6:
        print("FAIL — forecast year one does not close at the twelve-month forecast's month-twelve balance")
        sys.exit(1)
    failures = []
    for nm, exp in expect.items():
        got = vals.get(cell_key(names[nm]))
        if got is None or abs(float(got) - float(exp)) > 1e-6 * max(1.0, abs(exp)):
            failures.append(f"{nm}: workbook {got!r} vs model {exp!r}")
    for nm, exp in (("verdict", R["verdict"]), ("all_checks", "ALL CHECKS PASS")):
        got = vals.get(cell_key(names[nm]))
        if got != exp:
            failures.append(f"{nm}: workbook {got!r} vs model {exp!r}")
    # the verdict must follow the registry gates
    v = R["fmos"]
    want = "PASS" if v >= 0.25 else ("BORDERLINE" if v >= 0.15 else "FAIL")
    if R["verdict"] != want:
        failures.append(f"verdict logic: {R['verdict']} for FMOS {v:.3f}")
    # the sensitivity must be sorted worst first and the worst corner no better than any single move
    fm = [s[3] for s in R["sensitivity"]]
    if fm != sorted(fm):
        failures.append("sensitivity not sorted worst first")
    if R["sensitivity"] and R["fmos_worst_corner"] > min(fm) + 1e-9:
        failures.append("worst corner better than a single adverse move")
    if failures:
        print("FAIL — " + failures[0] + (f" (+{len(failures)-1} more)" if len(failures) > 1 else ""))
        for f_ in failures[1:]:
            print("       " + f_)
        sys.exit(1)
    print(f"PASS — {len(expect)+2} named cells agree with the model; Check tab reads ALL CHECKS PASS; forecast balances over {len(R['forecast'])} years; FMOS {R['fmos']:.1%} {R['verdict']}")



def test_v13_blocks():
    """Spec v1.3: readings (file, literal, live formula with a check) and price cases. Both directions: the ruled
    verdict in B8 follows the reading, not the central margin, and a price case equals the model at that fee."""
    import json
    with open(os.path.join(HERE, "example-model.yaml")) as f:
        m = yaml.safe_load(f)
    tmp = tempfile.mkdtemp()
    with open(os.path.join(tmp, "side.yaml"), "w") as f:
        yaml.safe_dump({"a": {"b": [0.10, -0.40]}}, f)
    cogs = float(m["products"][0]["cost_of_goods"]["value"]) if isinstance(m["products"][0]["cost_of_goods"], dict) else float(m["products"][0]["cost_of_goods"])
    m["_model_dir"] = tmp
    m["readings"] = {"source_files": {"side": "side.yaml"}, "verdict_reading": "ruled",
                     "items": [{"name": "ruled", "from": {"file": "side", "path": "a.b.1"}, "unit": "share", "tier": 4},
                               {"name": "half", "value": 0.5, "unit": "share", "tier": 4},
                               {"name": "cogs_rebuilt", "formula": "{rd:half} * 2 * {in:product.0.cogs}", "unit": "GBP",
                                "check_against": "in:product.0.cogs"}]}
    p2 = round(float(gen.compute(m, {k: v["value"] for k, v in gen.collect_inputs(m).items()})["interim_price"]) * 1.2, 4)
    m["price_cases"] = [{"price": p2, "label": "case at 1.2 times", "status": "red"}]
    xlsx, cells_md, R = gen.build(m, tmp)
    from openpyxl import load_workbook
    names = {n: dn.attr_text for n, dn in load_workbook(xlsx).defined_names.items()}
    vals = evaluate(xlsx)
    fails = []
    g = lambda nm: vals.get(cell_key(names[nm]))  # noqa: E731
    if g("verdict") != "FAIL":
        fails.append(f"B8 should read FAIL on the ruled reading -0.40, got {g('verdict')!r}")
    if g("verdict_central") != R["verdict"]:
        fails.append(f"verdict_central {g('verdict_central')!r} vs {R['verdict']!r}")
    if abs(float(g("rd_cogs_rebuilt")) - cogs) > 1e-9:
        fails.append(f"live formula reading {g('rd_cogs_rebuilt')!r} vs {cogs!r}")
    if g("readings_checks") != "ALL PASS":
        fails.append(f"reading checks {g('readings_checks')!r}")
    vals0 = {k: v["value"] for k, v in gen.collect_inputs(m).items()}
    Rc = gen.price_case_values(m, vals0, p2)
    if abs(Rc["interim_price"] - p2) > 1e-9:
        fails.append("price case does not land on its fee")
    if abs(float(g("pc1_revenue_year_1")) - Rc["forecast"][0]["revenue"]) > 1e-6 * max(1, abs(Rc["forecast"][0]["revenue"])):
        fails.append("price case revenue year 1 differs from the model at that fee")
    if abs(float(g("pc1_margin_of_safety")) - Rc["fmos"]) > 1e-9:
        fails.append("price case margin differs")
    if g("all_checks") != "ALL CHECKS PASS":
        fails.append("Check tab broke with the v1.3 blocks")
    # the other direction: a file whose ruled reading passes reads PASS in B8
    m["readings"]["items"][0]["from"]["path"] = "a.b.0"
    m["readings"]["items"][0].pop("from"); m["readings"]["items"][0]["value"] = 0.30
    xlsx2, _, _ = gen.build(m, tempfile.mkdtemp())
    names2 = {n: dn.attr_text for n, dn in load_workbook(xlsx2).defined_names.items()}
    if evaluate(xlsx2).get(cell_key(names2["verdict"])) != "PASS":
        fails.append("B8 should read PASS on a ruled reading of 0.30")
    try:
        m["readings"]["items"].append({"name": "bad", "formula": "__import__('os')"})
        gen.build(m, tempfile.mkdtemp())
        fails.append("a formula with names other than readings and inputs was accepted")
    except ValueError:
        pass
    if fails:
        print("FAIL — v1.3 blocks: " + "; ".join(fails))
        sys.exit(1)
    print("PASS — v1.3 blocks: ruled verdict both directions, live reading with check, price case equals the model at its fee")


if __name__ == "__main__":
    main()
    test_v13_blocks()
