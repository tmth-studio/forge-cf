#!/usr/bin/env python3
"""Regression tests for check_model_coverage.py. Both directions on every rule."""
import copy
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "check_model_coverage.py")

# Dated before the narrative, actor-economics and jurisdiction rules so the
# fixture stays small; those rules belong to validate_model.py and have their
# own tests. This file tests the coverage relations only.
CTM = {
    "venture": "Test Venture",
    "state": "at-C4",
    "date": "2026-08-01",
    "customer": "Small business",
    "customer_doc": "the paying actor",
    "timeline": ["week 0", "week 4"],
    "phases": {
        "become": {
            "name": "Become",
            "states": [
                {"id": "unaware", "icon": "a", "label": "Business who is unaware"},
                {"id": "signed", "icon": "b", "label": "Business who has signed", "final": True},
            ],
            "transitions": [
                {"from": "unaware", "to": "signed", "components": ["CP-1", "WP-1"],
                 "label": "Offer and sign"},
            ],
        },
    },
    "partner_tracks": {
        "broker": {
            "actor": "Insurance broker",
            "role_note": "brings the business",
            "states": [
                {"id": "cold", "icon": "c", "label": "Broker who is unaware"},
                {"id": "warm", "icon": "d", "label": "Broker who refers", "final": True},
            ],
            "transitions": [
                {"from": "cold", "to": "warm", "components": ["PartP-1"], "label": "Partner deal"},
            ],
        },
    },
    "balm_mapping": [
        {"req": "R4 — Want Block", "phase": "Become", "component": "CP-1", "overrides": "x"},
    ],
    "review_findings": ["none"],
    "routing": {"gate": "R4", "figures": ["none"]},
}

AOM = {
    "venture": "Test Venture",
    "state": "at-C4",
    "date": "2026-08-01",
    "scale_header": "1 unit",
    "actors": {
        "business": {"name": "Small business", "class": "customer", "doc": "pays"},
        "broker": {"name": "Insurance broker", "class": "enabler", "slot": "Part-1",
                   "species": "gateway", "doc": "refers"},
        "cloud": {"name": "Cloud supplier", "class": "enabler", "slot": "Part-2",
                  "species": "commodity_vendor", "doc": "compute"},
    },
    "organisation": {
        "hq": {"name": "HQ", "op_id": "OP-1", "cost_ref": "arm", "functions": {
            "sales": {"name": "Sales", "driver": "deals", "fte": 1},
            "ops": {"name": "Ops", "driver": "cases", "fte": 1},
        }},
    },
    "components": {
        "CP-1": {"name": "offer", "def": "Offer", "allocated_to": "sales", "dri": "Head of Sales",
                 "doc": "the offer", "build_ref": ["BC-01"]},
        "WP-1": {"name": "service", "def": "Service", "allocated_to": "ops", "dri": "Head of Ops",
                 "doc": "the service"},
        "PartP-1": {"name": "broker_deal", "def": "BrokerDeal", "allocated_to": "sales",
                    "dri": "Head of Sales", "doc": "the partner deal"},
    },
    "build_components": {
        "BC-01": {"name": "offer_page", "def": "OfferPage", "allocated_to": "sales",
                  "dri": "Head of Sales", "doc": "builds the offer"},
    },
    "flows": {
        "product": [{"name": "service_out", "item": "Service", "from": "venture",
                     "to": "business", "via": "WP-1"}],
        "information": [{"name": "offer_out", "item": "Offer", "from": "venture",
                         "to": "business", "via": "CP-1"},
                        {"name": "referral", "item": "Referral", "from": "broker",
                         "to": "venture", "via": "PartP-1"}],
        "money": [{"name": "fee_in", "item": "Fee", "from": "business", "to": "venture",
                   "via": "WP-1"}],
    },
    "spine": ["CP-1", "WP-1", "PartP-1"],
}


def run_models(ctm, aom, tmp, extra_args=()):
    cpath = os.path.join(tmp, "test-ctm-model-at-C4.yaml")
    apath = os.path.join(tmp, "test-aom-model-at-C4.yaml")
    yaml.safe_dump(ctm, open(cpath, "w"))
    yaml.safe_dump(aom, open(apath, "w"))
    p = subprocess.run([sys.executable, SCRIPT, cpath] + list(extra_args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def case(label, mutate, want_code, want_text=None):
    c, a = copy.deepcopy(CTM), copy.deepcopy(AOM)
    if mutate:
        mutate(c, a)
    with tempfile.TemporaryDirectory() as tmp:
        code, out = run_models(c, a, tmp)
    ok = code == want_code and (want_text is None or want_text.lower() in out.lower())
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", label, code))
    if not ok:
        print("       wanted exit=%d text=%r" % (want_code, want_text))
        print("       got: %s" % out.strip().replace("\n", "\n            ")[:900])
    return ok


def main():
    print("check_model_coverage.py regression set")
    results = []

    # --- the happy path, and it must say what it verified ---
    results.append(case("clean pair is covered", None, 0, "VERDICT            : COVERED"))
    results.append(case("clean pair reports the relations it checked", None, 0, "relations checked  : 7"))
    results.append(case("a commodity vendor is exempt and counted", None, 0, "1 commodity vendor(s) exempt"))

    # --- 1. register component carried, or a stated reason ---
    def orphan_component(c, a):
        a["components"]["PP-1"] = {"name": "billing", "def": "Billing", "allocated_to": "ops",
                                   "dri": "Head of Ops", "doc": "bills"}
        a["spine"].append("PP-1")
    results.append(case("a register component no transition carries is uncovered",
                        orphan_component, 2, "PP-1 (billing) is in the register and no journey"))

    def dispositioned_component(c, a):
        orphan_component(c, a)
        a["components"]["PP-1"]["disposition"] = {"not_designed_until": "C6"}
    results.append(case("an uncarried component with a disposition is accepted and noted",
                        dispositioned_component, 0, "declared not designed until C6"))

    def stale_disposition(c, a):
        a["components"]["WP-1"]["disposition"] = {"not_applicable": "kept for the record"}
    results.append(case("a disposition on a carried component is noted as out of date",
                        stale_disposition, 0, "disposition is out of date"))

    # --- 2. every flow names a carrying component ---
    def flow_no_via(c, a):
        a["flows"]["money"].append({"name": "levy_out", "item": "Levy", "from": "venture",
                                    "to": "business", "doc": "a levy"})
    results.append(case("a flow with no component and no flag is uncovered",
                        flow_no_via, 2, "names no component that carries it"))

    def flow_flagged(c, a):
        a["flows"]["money"].append({"name": "levy_out", "item": "Levy", "from": "venture",
                                    "to": "business", "flag": "absent by decision"})
    results.append(case("a flow with no component and a flag is accepted and noted",
                        flow_flagged, 0, "declares why: absent by decision"))

    # --- 3. flow endpoints resolve (the model checker refuses first; C-8 calls it) ---
    def bad_endpoint(c, a):
        a["flows"]["money"][0]["from"] = "regulator"
    results.append(case("a flow endpoint absent from the roster is refused at load",
                        bad_endpoint, 2, "does not resolve"))

    # --- 4. every roster actor is met by the journey (R-W15, first half) ---
    def unmet_partner(c, a):
        a["actors"]["assessor"] = {"name": "Independent assessor", "class": "enabler",
                                   "slot": "Part-3", "species": "capability", "doc": "assesses"}
    results.append(case("a roster actor no track meets is uncovered",
                        unmet_partner, 2, "actor `assessor`"))

    def partner_met_by_flow(c, a):
        unmet_partner(c, a)
        a["flows"]["information"][1]["to"] = "assessor"   # the carried PartP-1 now reaches it
    results.append(case("a partner reached by a carried partner flow is met",
                        partner_met_by_flow, 0, "actor `assessor` met by flows.information.referral"))

    def bound_by_id(c, a):
        c["partner_tracks"]["broker"]["actor"] = "The intermediary"   # no words in common
        c["partner_tracks"]["broker"]["aom_actor"] = "broker"
    results.append(case("a track bound with aom_actor matches on the id alone",
                        bound_by_id, 0, "actor `broker` met by partner_tracks.broker"))

    def unbound_no_words(c, a):
        c["partner_tracks"]["broker"]["actor"] = "The intermediary"
        a["flows"]["information"][1]["from"] = "business"   # no carried partner flow reaches the broker
    results.append(case("a track whose words do not match leaves the actor unmet",
                        unbound_no_words, 2, "bind an existing track with aom_actor: broker"))

    # --- 5. carried component absent from the register (the model checker refuses) ---
    def carried_unregistered(c, a):
        c["phases"]["become"]["transitions"][0]["components"].append("WP-9")
    results.append(case("a carried component absent from the register is refused at load",
                        carried_unregistered, 2, "absent from the AOM register"))

    # --- 6. carried component allocated to a function ---
    def unallocated(c, a):
        a["components"]["WP-1"]["allocated_to"] = "nobody"
    results.append(case("a carried component allocated to no function is refused at load",
                        unallocated, 2, "is not an org function"))

    # --- 7. build component parentage (R-W15, second half) ---
    def orphan_build(c, a):
        a["build_components"]["FD-09"] = {"name": "partner_acquisition", "def": "PA",
                                          "allocated_to": "sales", "dri": "Head of Sales",
                                          "doc": "finds partners"}
    results.append(case("a build component with no parent is uncovered",
                        orphan_build, 2, "build component FD-09 (partner_acquisition) has no parent"))

    def build_named_as_substitute(c, a):
        orphan_build(c, a)
        c["partner_tracks"]["broker"]["states"][0]["label"] = "Broker who already refers"
        c["partner_tracks"]["broker"]["arrival"] = {
            "deliberate_absence": "no partner marketing product by design, revisited at C7",
            "substitute": "FD-09 partner acquisition, one broker approached per broker signed"}
    results.append(case("a build component named as a VA-102 substitute is accepted and noted",
                        build_named_as_substitute, 0, "FD-09 has no parent component; it is the substitute"))

    # --- the models must load through the existing checker first (C-8) ---
    def broken_model(c, a):
        del a["spine"]
    results.append(case("an operating model the checker refuses is not compared",
                        broken_model, 2, "Nothing was compared"))

    # --- several journey files share one operating model: coverage is the union ---
    def two_journeys():
        c1, a = copy.deepcopy(CTM), copy.deepcopy(AOM)
        a["components"]["PP-1"] = {"name": "billing", "def": "Billing", "allocated_to": "ops",
                                   "dri": "Head of Ops", "doc": "bills"}
        a["spine"].append("PP-1")
        c2 = copy.deepcopy(CTM)
        c2["phases"]["become"]["transitions"][0]["components"] = ["PP-1"]
        with tempfile.TemporaryDirectory() as tmp:
            p1 = os.path.join(tmp, "test-ctm-model-at-C4.yaml")
            p2 = os.path.join(tmp, "test-ctm-model-at-C4-second.yaml")
            pa = os.path.join(tmp, "test-aom-model-at-C4.yaml")
            yaml.safe_dump(c1, open(p1, "w"))
            yaml.safe_dump(c2, open(p2, "w"))
            yaml.safe_dump(a, open(pa, "w"))
            alone = subprocess.run([sys.executable, SCRIPT, p1], capture_output=True, text=True)
            both = subprocess.run([sys.executable, SCRIPT, p1, p2, "--aom", pa],
                                  capture_output=True, text=True)
        ok = alone.returncode == 2 and both.returncode == 0 and "COVERED" in both.stdout
        print("  %-4s %-62s exit=%d,%d" % ("PASS" if ok else "FAIL",
                                           "a second journey file covers what the first does not",
                                           alone.returncode, both.returncode))
        if not ok:
            print("       got: %s" % (alone.stdout + both.stdout)[-900:])
        return ok
    results.append(two_journeys())

    # --- help ---
    p = subprocess.run([sys.executable, SCRIPT, "--help"], capture_output=True, text=True)
    ok = p.returncode == 0 and "R-W15" in p.stdout
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", "--help prints the rule it executes", p.returncode))
    results.append(ok)

    print("")
    print("  %d/%d assertions passing" % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
