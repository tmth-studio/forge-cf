#!/usr/bin/env python3
"""Regression tests for fit_margin.py. Both directions on every rule."""
import copy
import datetime
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "fit_margin.py")

# 16 September 2026, rule (a): every figure below evidence tier 1 must be a band.
# This fixture's five figures carried no tier; a missing tier is read at T4 and a
# point at T4 is refused. Choice (i) was taken: `tier: T1` on each, so the fixture
# keeps its meaning (single-number figures at the top tier). No grace period.
BASE = {
    "venture": "Test Venture",
    "state": "at-C10",
    "bounding": {"currency": "GBP", "unit": "covered transaction",
                 "period": "year", "scale_state": "at-scale"},
    "derived_from": {"operating_model": "aom.yaml", "customer_model": "ctm.yaml"},
    "gate": "phase_ii",
    "cost_floor": {"layers": {
        "pvc": {"amount": 1.00, "tier": "T1", "unit": "GBP per covered transaction", "period": "year",
                "scale_state": "at-scale", "basis": "activity", "source": "activity rows 1-4"},
        "rc": {"amount": 0.50, "tier": "T1", "unit": "GBP per covered transaction", "period": "year",
               "scale_state": "at-scale", "basis": "activity", "source": "activity rows 5-9"},
        "sc": {"amount": 0.30, "tier": "T1", "unit": "GBP per covered transaction", "period": "year",
               "scale_state": "at-scale", "basis": "activity", "source": "ramp build"},
        "ic": {"amount": 0.20, "tier": "T1", "unit": "GBP per covered transaction", "period": "year",
               "scale_state": "at-scale", "basis": "activity", "source": "HQ functions"},
    }},
    "price_ceiling": {
        "kmc": {"amount": 6.00, "tier": "T1", "unit": "GBP per covered transaction", "period": "year",
                "scale_state": "at-scale", "source": "published fee schedule"},
        "customer_surplus_fraction": {"value": 0.60, "source": "R2 surplus rule"},
    },
}
# floor 2.00, ceiling 3.60, margin 80% -> PASS at phase_ii


def run_model(model, tmp):
    for name in ("aom.yaml", "ctm.yaml"):
        open(os.path.join(tmp, name), "w").write("placeholder: true\n")
    path = os.path.join(tmp, "fit.yaml")
    yaml.safe_dump(model, open(path, "w"))
    p = subprocess.run([sys.executable, SCRIPT, path], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def case(label, mutate, want_code, want_text=None, absent_text=None):
    m = copy.deepcopy(BASE)
    if mutate:
        mutate(m)
    with tempfile.TemporaryDirectory() as tmp:
        code, out = run_model(m, tmp)
    ok = (code == want_code
          and (want_text is None or want_text.lower() in out.lower())
          and (absent_text is None or absent_text.lower() not in out.lower()))
    print("  %-4s %-58s exit=%d" % ("PASS" if ok else "FAIL", label, code))
    if not ok:
        print("       wanted exit=%d text=%r absent=%r" % (want_code, want_text, absent_text))
        print("       got: %s" % out.strip().replace("\n", "\n            ")[:600])
    return ok


def main():
    print("fit_margin.py regression set")
    results = []

    # --- the happy path, and it must actually compute ---
    results.append(case("clean model computes and passes", None, 0, "VERDICT            : PASS"))
    results.append(case("clean model reports what it verified", None, 0, "checks reaching a verdict"))

    # --- the gate bands ---
    def borderline(m):
        m["price_ceiling"]["kmc"]["amount"] = 4.50   # ceiling 2.70, margin 35%
    results.append(case("35% at phase_ii is BORDERLINE", borderline, 1, "BORDERLINE"))

    def fail_band(m):
        m["price_ceiling"]["kmc"]["amount"] = 3.50   # ceiling 2.10, margin 5%
    results.append(case("5% at phase_ii is FAIL", fail_band, 1, "VERDICT            : FAIL"))

    def per_req(m):
        m["gate"] = "per_requirement"
        m["price_ceiling"]["kmc"]["amount"] = 4.50   # margin 35% -> PASS per-requirement
    results.append(case("35% at per_requirement is PASS", per_req, 0, "PASS"))

    # --- C-3: units must compose ---
    def wrong_unit(m):
        m["cost_floor"]["layers"]["rc"]["unit"] = "GBP per order"
    results.append(case("a mixed unit is refused", wrong_unit, 2, "must be"))

    # --- RD-017: scale states must agree ---
    def wrong_scale(m):
        m["cost_floor"]["layers"]["ic"]["scale_state"] = "launch"
    results.append(case("a mixed scale state is refused", wrong_scale, 2, "RD-017"))

    # --- period ---
    def wrong_period(m):
        m["price_ceiling"]["kmc"]["period"] = "month"
    results.append(case("a mixed period is refused", wrong_period, 2, "per `month`"))

    # --- VA-91: a stored figure must reproduce ---
    def bad_stored_floor(m):
        m["cost_floor"]["amount"] = 1.75
    results.append(case("a stored cost floor that contradicts is refused", bad_stored_floor, 2, "VA-91"))

    def good_stored_floor(m):
        m["cost_floor"]["amount"] = 2.00
    results.append(case("a stored cost floor that reproduces is accepted", good_stored_floor, 0, "reproduces"))

    def bad_stored_ceiling(m):
        m["price_ceiling"]["amount"] = 5.00
    results.append(case("a stored price ceiling that contradicts is refused", bad_stored_ceiling, 2, "identity produces"))

    # --- C-1: an asserted rate needs a reason ---
    def asserted_no_reason(m):
        m["cost_floor"]["layers"]["rc"]["basis"] = "asserted"
    results.append(case("an asserted rate with no reason is refused", asserted_no_reason, 2, "asserted_reason"))

    def asserted_with_reason(m):
        m["cost_floor"]["layers"]["rc"]["basis"] = "asserted"
        m["cost_floor"]["layers"]["rc"]["asserted_reason"] = "vendor quote, no activity yet"
        m["cost_floor"]["layers"]["rc"]["source"] = "vendor quote of 1 Sep"
    results.append(case("an asserted rate with a reason passes and is flagged", asserted_with_reason, 0, "is ASSERTED"))

    # --- every figure needs a source ---
    def no_source(m):
        m["cost_floor"]["layers"]["pvc"]["source"] = ""
    results.append(case("a figure with no source is refused", no_source, 2, "empty `source`"))

    # --- a missing layer is refused; a dispositioned one is allowed and flagged ---
    def missing_layer(m):
        del m["cost_floor"]["layers"]["sc"]
    results.append(case("a missing cost layer is refused", missing_layer, 2, "no `sc`"))

    def dispositioned_layer(m):
        m["cost_floor"]["layers"]["sc"] = {"not_designed_until": "C3"}
    results.append(case("a dispositioned layer computes and marks the verdict indicative",
                        dispositioned_layer, 0, "INDICATIVE"))

    def disposition_no_reason(m):
        m["cost_floor"]["layers"]["sc"] = {"not_applicable": ""}
    results.append(case("a disposition with no reason is refused", disposition_no_reason, 2, "no reason"))

    # --- the source models must be named and must exist ---
    def missing_source_model(m):
        del m["derived_from"]["customer_model"]
    results.append(case("no named customer model is refused", missing_source_model, 2, "derived_from.customer_model"))

    def bad_source_model(m):
        m["derived_from"]["operating_model"] = "does-not-exist.yaml"
    results.append(case("a source model that does not exist is refused", bad_source_model, 2, "does not exist"))

    # --- the surplus fraction is a fraction ---
    def bad_fraction(m):
        m["price_ceiling"]["customer_surplus_fraction"]["value"] = 1.4
    results.append(case("a surplus fraction above one is refused", bad_fraction, 2, "between 0 and 1"))

    # --- a zero cost floor has no verdict ---
    def zero_floor(m):
        for k in ("pvc", "rc", "sc", "ic"):
            m["cost_floor"]["layers"][k]["amount"] = 0.0
    results.append(case("a cost floor of zero is refused", zero_floor, 2, "has no verdict"))

    # --- a bad gate name is refused ---
    def bad_gate(m):
        m["gate"] = "whatever"
    results.append(case("an unknown gate is refused", bad_gate, 2, "per_requirement"))

    # --- (a) 16 Sep 2026: a figure below tier 1 is a band, not a point ---
    def point_at_t2(m):
        m["price_ceiling"]["kmc"]["tier"] = "T2"
    results.append(case("a single number at tier 2 is refused", point_at_t2, 2,
                        "a value below tier 1 is a band, not a point"))

    def point_no_tier(m):
        del m["cost_floor"]["layers"]["rc"]["tier"]
    results.append(case("a single number with no tier is read at T4 and refused",
                        point_no_tier, 2, "no `tier` is stated"))

    def band_at_t2(m):
        m["price_ceiling"]["kmc"]["tier"] = "T2"
        del m["price_ceiling"]["kmc"]["amount"]
        m["price_ceiling"]["kmc"]["band"] = {"low": 6.00, "high": 7.00}
        # ceiling 3.60 to 4.20, floor 2.00: worst corner 80% -> PASS at phase_ii
    results.append(case("a band at tier 2 is accepted and judged at the worst corner",
                        band_at_t2, 0, "VERDICT            : PASS at 80.0% (worst corner"))

    def band_worst_corner_fails(m):
        m["cost_floor"]["layers"]["pvc"]["tier"] = "T3"
        del m["cost_floor"]["layers"]["pvc"]["amount"]
        m["cost_floor"]["layers"]["pvc"]["band"] = {"low": 1.00, "high": 2.00}
        # floor 2.00 to 3.00, ceiling 3.60: worst corner 20% -> FAIL at phase_ii
    results.append(case("a band whose worst corner fails the gate is FAIL",
                        band_worst_corner_fails, 1, "VERDICT            : FAIL at 20.0%"))

    def point_at_t1(m):
        m["price_ceiling"]["kmc"]["tier"] = "t1"
    results.append(case("a single number at tier 1 is accepted", point_at_t1, 0,
                        "VERDICT            : PASS at 80.0%", absent_text="worst corner"))

    def unknown_tier(m):
        m["price_ceiling"]["kmc"]["tier"] = "T5"
    results.append(case("an unknown tier is refused", unknown_tier, 2, "the evidence tiers are"))

    def band_inverted(m):
        m["price_ceiling"]["kmc"]["tier"] = "T2"
        del m["price_ceiling"]["kmc"]["amount"]
        m["price_ceiling"]["kmc"]["band"] = {"low": 7.00, "high": 6.00}
    results.append(case("a band with low above high is refused", band_inverted, 2, "above high"))

    def stored_point_over_band(m):
        m["price_ceiling"]["kmc"]["tier"] = "T2"
        del m["price_ceiling"]["kmc"]["amount"]
        m["price_ceiling"]["kmc"]["band"] = {"low": 6.00, "high": 7.00}
        m["price_ceiling"]["amount"] = 3.60
    results.append(case("a stored headline number over a band is refused",
                        stored_point_over_band, 2, "cannot be stored as one number"))

    # --- (b) RB-V-025: a bar that reads its own ceiling is an indicator ---
    BAR = {"amount": 3.20, "unit": "GBP per covered transaction", "period": "year",
           "scale_state": "at-scale", "source": "capital bar ruling of 14 Sep 2026"}

    def bar_reads_ceiling(m):
        m["required_price"] = dict(BAR, derived_from=["price_ceiling", "margin_factor"])
    results.append(case("a bar derived from the price ceiling is refused",
                        bar_reads_ceiling, 2, "reads the ceiling it is tested against"))

    def bar_formula_reads_kmc(m):
        m["required_price"] = dict(BAR, formula="kmc x 0.6 x (1 - 0.12)")
    results.append(case("a bar whose formula mentions the key cost is refused",
                        bar_formula_reads_kmc, 2, "RB-V-025"))

    def bar_fixed_number(m):
        m["required_price"] = dict(BAR, derived_from=["cost_floor", "required_profit"])
    results.append(case("a bar in fixed-number form is accepted and reported",
                        bar_fixed_number, 0, "required price bar : GBP 3.2000"))

    def bar_as_band(m):
        m["required_price"] = dict(BAR, derived_from=["cost_floor"])
        del m["required_price"]["amount"]
        m["required_price"]["band"] = {"low": 3.0, "high": 3.4}
    results.append(case("a bar stated as a band is refused", bar_as_band, 2, "a bar is one number"))

    # --- (c) VA-99: the header date must not lag the edit history ---
    def header_today(m):
        m["date"] = datetime.date.today().isoformat()
    results.append(case("a header dated today carries no warning", header_today, 0,
                        "within 24 hours", absent_text="WARNING"))

    def header_stale(m):
        m["date"] = (datetime.date.today() - datetime.timedelta(days=10)).isoformat()
    results.append(case("a header ten days behind the edit warns, exit unchanged",
                        header_stale, 0, "the grace cannot be kept by leaving an old header behind"))

    def header_unreadable(m):
        m["updated"] = "mid September"
    results.append(case("a header date the checker cannot read warns, exit unchanged",
                        header_unreadable, 0, "is not a date the checker can read"))

    print("")
    print("  %d/%d assertions passing" % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
