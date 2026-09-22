#!/usr/bin/env python3
"""Regression tests for VA-147 — the pool at risk and the side of the book.

Two checkers carry the rule. validate_tam_model.py L11 requires the market model
to state the pool per incumbent; validate_model.py requires every stated partner
business case to name the side of the partner's book it sits on, bounds a
loss-side partner by the pool the market model states, and requires a gain-side
gateway chosen over a loss-side candidate to state an admissible reason. Both
directions on every clause: a model that complies passes with no VA-147 line,
and a model that breaks the clause is refused on or after the rule date and
warned before it. Tests import validate() directly; the origin check
(toolchain_guard) has its own tests and is not exercised here.
"""
import copy
import os
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import validate_model as vm  # noqa: E402
import validate_tam_model as vt  # noqa: E402

# Dated on the rule date so every clause refuses. The pre-date direction is one
# explicit case below. One customer, one loss-side gateway, one gain-side
# capability partner, one commodity vendor (exempt).
AOM = {
    "venture": "Test Venture",
    "state": "at-C7",
    "date": vm.POOL_RULE_FROM,
    "scale_header": "1 unit",
    "jurisdiction": {"country": "United Kingdom", "profile": "EW-1", "standard": "v2.0"},
    "actors": {
        "claimant": {"name": "Claimant", "class": "customer", "doc": "pays",
                     "outcome": "I am paid what I am owed",
                     "kmc": {"statement": "cash foregone to an unpaid claim", "type": "money",
                             "sub_type": "foregone", "basis": "current_routine", "tier": "T3",
                             "source": "test"}},
        "conveyancer": {"name": "Conveyancer", "class": "enabler", "slot": "Part-1",
                        "species": "gateway", "doc": "carries the offer",
                        "outcome": "I keep my completions margin",
                        "business_case": {
                            "earns": "a referral fee per case", "costs": "one screen per completion",
                            "beats_next_best": "the next-best use of the desk is nil at completion",
                            "operational_fit": "already at the point of instruction",
                            "timing": "at exchange",
                            "effect_on_book": {"side": "loss_side", "amount": -400000,
                                               "source": "market model pool_at_risk, typical firm",
                                               "tier": "T3", "pool_ref": "conveyancer"}}},
        "insurer": {"name": "Insurer", "class": "enabler", "slot": "Part-2",
                    "species": "capability", "doc": "underwrites",
                    "outcome": "I write profitable premium",
                    "business_case": {
                        "earns": "premium", "costs": "claims", "beats_next_best": "beats the book's average loss ratio",
                        "operational_fit": "existing line", "timing": "per policy",
                        "effect_on_book": {"side": "gain_side", "amount": 120000,
                                           "source": "term sheet draft", "tier": "T3"}}},
        "cloud": {"name": "Cloud supplier", "class": "enabler", "slot": "Part-3",
                  "species": "commodity_vendor", "doc": "compute"},
    },
    "organisation": {
        "hq": {"name": "HQ", "op_id": "OP-1", "cost_ref": "arm", "functions": {
            "ops": {"name": "Ops", "driver": "cases", "fte": 1},
        }},
    },
    "components": {
        "CP-1": {"name": "offer", "def": "Offer", "allocated_to": "ops", "dri": "Head of Sales",
                 "doc": "the offer"},
        "WP-1": {"name": "service", "def": "Service", "allocated_to": "ops", "dri": "Head of Ops",
                 "doc": "the service"},
    },
    "flows": {
        "product": [{"name": "service_out", "item": "Service", "from": "venture",
                     "to": "claimant", "via": "WP-1"}],
        "information": [{"name": "offer_out", "item": "Offer", "from": "venture",
                         "to": "claimant", "via": "CP-1"}],
        "money": [{"name": "fee_in", "item": "Fee", "from": "claimant", "to": "venture",
                   "via": "WP-1"}],
    },
    "spine": ["CP-1", "WP-1"],
}

# The sibling market model. Only the pool block is exercised here; the rest of
# the TAM checks have their own fixture below.
BAND = {"low": 300000, "high": 500000, "source": "SRA firm data 2025", "tier": "T2"}
TAM = {
    "venture": "Test Venture", "version": "1", "date": vm.POOL_RULE_FROM,
    "pool_at_risk": {
        "status": "sized",
        "incumbents": [
            {"id": "conveyancer", "class": "high-street conveyancing firm",
             "revenue_a_year": dict(BAND), "reading_s": dict(BAND), "reading_d": dict(BAND),
             "pool_a_year": dict(BAND),
             "channelling": {"condition": "yes", "evidence": "instructs at exchange"}},
        ],
    },
}


def run(aom, tam=TAM, tam_name="test-tam-model.yaml"):
    with tempfile.TemporaryDirectory() as tmp:
        apath = os.path.join(tmp, "test-aom-model-at-C7.yaml")
        yaml.safe_dump(aom, open(apath, "w"), allow_unicode=True)
        if tam is not None:
            yaml.safe_dump(tam, open(os.path.join(tmp, tam_name), "w"), allow_unicode=True)
        errs, warns = vm.validate(apath)
        return errs, warns, list(vm.POOL_REPORT)


def va(lines):
    return [x for x in lines if "VA-147" in x]


RESULTS = []


def case(label, mutate=None, want="pass", text=None, tam=TAM, tam_name="test-tam-model.yaml"):
    """want: 'pass' (no VA-147 error or warning), 'refuse' (a VA-147 error, no other
    errors introduced), 'warn' (a VA-147 warning and no VA-147 error)."""
    a = copy.deepcopy(AOM)
    if mutate:
        mutate(a)
    errs, warns, report = run(a, copy.deepcopy(tam) if tam is not None else None, tam_name)
    ve, vw = va(errs), va(warns)
    other = [e for e in errs if "VA-147" not in e]
    if want == "pass":
        ok = not ve and not vw and not other
    elif want == "refuse":
        ok = bool(ve) and not other and (text is None or any(text.lower() in e.lower() for e in ve))
    else:
        ok = bool(vw) and not ve and not other and (text is None or any(text.lower() in w.lower() for w in vw))
    print("  %-4s %-70s errs=%d warns=%d" % ("PASS" if ok else "FAIL", label, len(ve), len(vw)))
    if not ok:
        for line in (errs + warns)[:6]:
            print("       ", line[:200])
    RESULTS.append(ok)
    return errs, warns, report


def tam_case(label, mutate=None, want="pass", text=None):
    """L11 on the market model directly. want: 'pass' (no L11 failure or warning),
    'refuse' (an L11 failure), 'warn' (an L11 warning and no L11 failure)."""
    t = copy.deepcopy(TAM)
    if mutate:
        mutate(t)
    r = vt.Report()
    vt.check_L11_pool_at_risk(t, r)
    fails = [m for c, m in r.failures if c == "L11"]
    warns = [m for c, m in r.warnings if c == "L11"]
    if want == "pass":
        ok = not fails and not warns
    elif want == "refuse":
        ok = bool(fails) and (text is None or any(text.lower() in m.lower() for m in fails))
    else:
        ok = bool(warns) and not fails and (text is None or any(text.lower() in m.lower() for m in warns))
    print("  %-4s %-70s fails=%d warns=%d" % ("PASS" if ok else "FAIL", label, len(fails), len(warns)))
    if not ok:
        for line in (fails + warns)[:6]:
            print("       ", line[:200])
    RESULTS.append(ok)
    return r


def main():
    print("VA-147 regression set — the pool at risk and the side of the book")
    print("")
    print("validate_tam_model.py L11 — the market model states the pool per incumbent")

    tam_case("a sized block with one complete incumbent row passes")

    def t_missing(t):
        del t["pool_at_risk"]
    tam_case("no block on the rule date is refused", t_missing, "refuse", "no pool_at_risk block")

    def t_missing_predate(t):
        del t["pool_at_risk"]
        t["date"] = "2026-09-17"
    tam_case("no block before the rule date warns", t_missing_predate, "warn", "dated before the rule")

    def t_none(t):
        t["pool_at_risk"] = {"status": "none", "reason": "the architecture takes no incumbent pool"}
    r = tam_case("status none with a reason passes", t_none, "pass")
    ok = any("declared none" in n for n in r.notes)
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "status none reports the declared absence (VA-105)"))
    RESULTS.append(ok)

    def t_none_no_reason(t):
        t["pool_at_risk"] = {"status": "none"}
    tam_case("status none without a reason is refused", t_none_no_reason, "refuse", "needs a reason")

    def t_none_with_rows(t):
        t["pool_at_risk"]["status"] = "none"
        t["pool_at_risk"]["reason"] = "none taken"
    tam_case("status none carrying incumbent rows is refused", t_none_with_rows, "refuse", "one or the other")

    def t_bad_status(t):
        t["pool_at_risk"]["status"] = "estimated"
    tam_case("a status outside sized | none is refused", t_bad_status, "refuse", "status")

    def t_aggregate_only(t):
        t["pool_at_risk"] = {"status": "sized", "total": dict(BAND)}
    tam_case("an aggregate with no incumbent rows is refused", t_aggregate_only, "refuse", "never only in aggregate")

    def t_no_rows(t):
        t["pool_at_risk"]["incumbents"] = []
    tam_case("sized with no rows is refused", t_no_rows, "refuse", "at least one row")

    def t_two_rows(t):
        second = copy.deepcopy(t["pool_at_risk"]["incumbents"][0])
        second["id"] = "broker"
        t["pool_at_risk"]["incumbents"].append(second)
    r = tam_case("two incumbents each with a full row pass", t_two_rows, "pass")
    ok = any("2 incumbent" in n for n in r.notes)
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "the report counts the rows verified (VA-105)"))
    RESULTS.append(ok)

    def t_dup_id(t):
        t["pool_at_risk"]["incumbents"].append(copy.deepcopy(t["pool_at_risk"]["incumbents"][0]))
    tam_case("a repeated incumbent id is refused", t_dup_id, "refuse", "repeats")

    def t_no_id(t):
        del t["pool_at_risk"]["incumbents"][0]["id"]
    tam_case("a row with no id is refused", t_no_id, "refuse", "no id")

    def t_no_class(t):
        del t["pool_at_risk"]["incumbents"][0]["class"]
    tam_case("a row naming no incumbent is refused", t_no_class, "refuse", "names no incumbent")

    for q in vt.POOL_QUANTITIES:
        def t_missing_q(t, q=q):
            del t["pool_at_risk"]["incumbents"][0][q]
        tam_case(f"a row missing {q} is refused", t_missing_q, "refuse", f"missing {q}")

    def t_no_tier(t):
        del t["pool_at_risk"]["incumbents"][0]["reading_s"]["tier"]
    tam_case("a reading with no tier is refused", t_no_tier, "refuse", "tier")

    def t_bad_tier(t):
        t["pool_at_risk"]["incumbents"][0]["reading_d"]["tier"] = "T9"
    tam_case("a reading with a tier outside the list is refused", t_bad_tier, "refuse", "tier 'T9'")

    def t_no_source(t):
        t["pool_at_risk"]["incumbents"][0]["pool_a_year"]["source"] = ""
    tam_case("a reading with no source is refused", t_no_source, "refuse", "no source")

    def t_low_gt_high(t):
        t["pool_at_risk"]["incumbents"][0]["pool_a_year"]["low"] = 600000
    tam_case("a band whose low exceeds its high is refused", t_low_gt_high, "refuse", "exceeds high")

    def t_not_number(t):
        t["pool_at_risk"]["incumbents"][0]["revenue_a_year"]["high"] = "about half a million"
    tam_case("a band bound that is not a number is refused", t_not_number, "refuse", "must be a number")

    def t_unmeasured_ok(t):
        t["pool_at_risk"]["incumbents"][0]["reading_d"] = {"low": None, "high": None,
                                                          "source": "no attacker precedent found",
                                                          "tier": "unmeasured"}
    tam_case("an unmeasured reading with no numbers passes", t_unmeasured_ok, "pass")

    def t_unmeasured_with_numbers(t):
        t["pool_at_risk"]["incumbents"][0]["reading_d"]["tier"] = "unmeasured"
    tam_case("an unmeasured reading carrying numbers is refused", t_unmeasured_with_numbers, "refuse", "unmeasured")

    def t_no_channelling(t):
        del t["pool_at_risk"]["incumbents"][0]["channelling"]
    tam_case("a row with no channelling condition is refused", t_no_channelling, "refuse", "channelling")

    def t_bad_channelling(t):
        t["pool_at_risk"]["incumbents"][0]["channelling"]["condition"] = "maybe"
    tam_case("a channelling condition outside yes | partly | no is refused", t_bad_channelling, "refuse", "condition")

    def t_no_evidence(t):
        t["pool_at_risk"]["incumbents"][0]["channelling"]["evidence"] = ""
    tam_case("a channelling condition with no evidence is refused", t_no_evidence, "refuse", "no evidence")

    ok = vt.check_L11_pool_at_risk in vt.CHECKS
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "L11 is in the CHECKS list the script runs"))
    RESULTS.append(ok)

    print("")
    print("validate_model.py — every partner case names its side; the pool is the bound")

    _, _, report = case("a loss-side gateway and a gain-side capability partner pass")
    ok = bool(report) and "1 loss side, 1 gain side, 0 unclassified" in report[0] and "1" in report[0].split("pool rows")[-1]
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "the report classifies both partners and names the pool rows read (VA-105)"))
    RESULTS.append(ok)

    # --- (a) effect_on_book: side and signed amount ---
    def no_effect(a):
        del a["actors"]["insurer"]["business_case"]["effect_on_book"]
    case("(a) a partner case with no effect_on_book is refused", no_effect, "refuse", "missing 'effect_on_book'")

    def bad_side(a):
        a["actors"]["insurer"]["business_case"]["effect_on_book"]["side"] = "neutral"
    case("(a) a side outside loss_side | gain_side is refused", bad_side, "refuse", "must be one of")

    def amount_text(a):
        a["actors"]["insurer"]["business_case"]["effect_on_book"]["amount"] = "material"
    case("(a) an amount that is not a number is refused", amount_text, "refuse", "signed number")

    def loss_positive(a):
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["amount"] = 400000
    case("(a) a loss-side amount that is not negative is refused", loss_positive, "refuse", "negative")

    def gain_negative(a):
        a["actors"]["insurer"]["business_case"]["effect_on_book"]["amount"] = -120000
    case("(a) a gain-side amount that is not positive is refused", gain_negative, "refuse", "positive")

    def no_source(a):
        a["actors"]["insurer"]["business_case"]["effect_on_book"]["source"] = ""
    case("(a) an amount with no source is refused", no_source, "refuse", "no source")

    def bad_tier(a):
        a["actors"]["insurer"]["business_case"]["effect_on_book"]["tier"] = "ESTIMATE"
    case("(a) a tier outside T1–T4 is refused", bad_tier, "refuse", "tier")

    def unstated_exempt(a):
        a["actors"]["insurer"]["business_case"] = {"status": "unstated", "owner": "CEO",
                                                   "reason": "term sheet not yet drafted"}
    case("(a) an unstated business case is not classified", unstated_exempt, "pass")

    def vendor_exempt(a):
        a["actors"]["cloud"]["business_case"] = {"earns": "fees", "costs": "compute",
                                                 "beats_next_best": "list price is list price",
                                                 "operational_fit": "yes", "timing": "monthly"}
    case("(a) a commodity vendor is exempt", vendor_exempt, "pass")

    # --- (b) a loss-side partner is bounded by the pool the market model states ---
    def no_pool_ref(a):
        del a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["pool_ref"]
    case("(b) a loss-side partner with no pool_ref is refused", no_pool_ref, "refuse", "does not name an incumbent")

    def wrong_pool_ref(a):
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["pool_ref"] = "broker"
    case("(b) a pool_ref naming no incumbent row is refused", wrong_pool_ref, "refuse", "'broker' does not name")

    def over_pool(a):
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["amount"] = -500001
    case("(b) an amount above the pool's high is refused", over_pool, "refuse", "the pool figure is the bound")

    def at_pool(a):
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["amount"] = -500000
    case("(b) an amount at the pool's high passes", at_pool, "pass")

    def pool_none(t):
        t["pool_at_risk"] = {"status": "none", "reason": "none taken"}
    tam_none = copy.deepcopy(TAM); pool_none(tam_none)
    case("(b) a loss-side partner against a market model declaring no pool is refused",
         None, "refuse", "needs a sized pool_at_risk block", tam=tam_none)

    case("(b) a loss-side partner with no sibling market model is refused",
         None, "refuse", "none found", tam=None)

    tam_noblock = copy.deepcopy(TAM); del tam_noblock["pool_at_risk"]
    case("(b) a loss-side partner against a market model with no block is refused",
         None, "refuse", "needs a sized pool_at_risk block", tam=tam_noblock)

    def explicit_market(a):
        a["market_model"] = "named-market.yaml"
    case("(b) an explicit market_model filename is read", explicit_market, "pass", tam_name="named-market.yaml")

    case("(b) a dated market model filename is found by the venture stem", None, "pass",
         tam_name="test-tam-model-2026-09-21.yaml")

    # --- (c) a gain-side gateway chosen over a loss-side candidate states why ---
    def gain_gateway_no_reason(a):
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"] = {
            "side": "gain_side", "amount": 90000, "source": "draft fee schedule", "tier": "T3"}
    case("(c) a gain-side gateway with a pool row present and no reason is refused",
         gain_gateway_no_reason, "refuse", "needs reason.code")

    def gain_gateway_bad_code(a):
        gain_gateway_no_reason(a)
        a["actors"]["conveyancer"]["business_case"]["reason"] = {"code": "they said yes first",
                                                                 "arithmetic": "n/a"}
    case("(c) a reason code outside the admissible list is refused", gain_gateway_bad_code, "refuse", "needs reason.code")

    def gain_gateway_no_arith(a):
        gain_gateway_no_reason(a)
        a["actors"]["conveyancer"]["business_case"]["reason"] = {"code": "pool_below_cost_of_carrying"}
    case("(c) an admissible code with no arithmetic is refused", gain_gateway_no_arith, "refuse", "no arithmetic")

    def gain_gateway_ok(a):
        gain_gateway_no_reason(a)
        a["actors"]["conveyancer"]["business_case"]["reason"] = {
            "code": "pool_below_cost_of_carrying",
            "arithmetic": "pool £300k–£500k a year against £620k a year to carry at scale"}
    case("(c) an admissible code with its arithmetic passes", gain_gateway_ok, "pass")

    def gain_gateway_loss_partner_elsewhere(a):
        # the loss-side candidate is another partner in the model, not a pool row
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"] = {
            "side": "gain_side", "amount": 90000, "source": "draft fee schedule", "tier": "T3"}
        a["actors"]["insurer"]["business_case"]["effect_on_book"] = {
            "side": "loss_side", "amount": -100000, "source": "market model", "tier": "T3",
            "pool_ref": "conveyancer"}
    case("(c) a loss-side partner elsewhere in the model is a candidate too",
         gain_gateway_loss_partner_elsewhere, "refuse", "needs reason.code")

    case("(c) a gain-side gateway with the pool declared none needs no reason",
         gain_gateway_no_reason, "pass", tam=tam_none)

    def gain_capability_no_reason(a):
        # insurer is gain side with no reason in the fixture — a capability partner, not a gateway
        pass
    case("(c) a gain-side capability partner needs no reason", gain_capability_no_reason, "pass")

    case("(c) a gain-side gateway with no sibling market model warns",
         gain_gateway_no_reason, "warn", "no sibling market model", tam=None)

    # --- the date gate: before the rule, the clauses warn and nothing refuses ---
    def predate(a):
        a["date"] = "2026-09-17"
        del a["actors"]["insurer"]["business_case"]["effect_on_book"]
        a["actors"]["conveyancer"]["business_case"]["effect_on_book"]["amount"] = -900000
    _, warns, report = case("a model dated before the rule warns on every clause and is not refused",
                            predate, "warn", "dated before the rule")
    ok = len(va(warns)) == 2 and "warning only" in report[0]
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "pre-date model: two warnings, report says warning only"))
    RESULTS.append(ok)

    # --- a model with no partner case at all still gets a report ---
    def no_partners(a):
        for k in ("conveyancer", "insurer"):
            del a["actors"][k]
    _, _, report = case("a model with no stated partner case passes and reports nothing to classify", no_partners, "pass")
    ok = bool(report) and "nothing to classify" in report[0]
    print("  %-4s %-70s" % ("PASS" if ok else "FAIL", "empty report line present (VA-105)"))
    RESULTS.append(ok)

    print("")
    print("  %d/%d assertions passing" % (sum(RESULTS), len(RESULTS)))
    return 0 if all(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
