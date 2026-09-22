#!/usr/bin/env python3
"""Regression tests for check_requirement_trace.py. Both directions on every rule."""
import copy
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "check_requirement_trace.py")

# Dated before the narrative, actor-economics and jurisdiction rules so the
# fixture stays small; those rules belong to validate_model.py.
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
        "consume": {
            "name": "Consume",
            "states": [
                {"id": "using", "icon": "c", "label": "Business who uses the service"},
                {"id": "served", "icon": "d", "label": "Business who has been served", "final": True},
            ],
            "transitions": [
                {"from": "using", "to": "served", "components": ["WP-1"], "label": "Serve"},
            ],
        },
    },
    "partner_tracks": {
        "broker": {
            "actor": "Insurance broker",
            "role_note": "brings the business",
            "states": [
                {"id": "cold", "icon": "e", "label": "Broker who is unaware"},
                {"id": "warm", "icon": "f", "label": "Broker who refers", "final": True},
            ],
            "transitions": [
                {"from": "cold", "to": "warm", "components": ["PartP-1"], "label": "Partner deal"},
            ],
        },
    },
    "balm_mapping": [
        {"req": "R1 — Workaround", "phase": "Consume", "component": "WP-1 — the service",
         "overrides": "bespoke delivery"},
        {"req": "R2 — Efficacy", "phase": "Phase 2 / Consume", "component": "WP-1",
         "overrides": "partial outcome"},
        {"req": "R3 — Scaling", "phase": "become", "component": "CP-1 / PartP-1",
         "overrides": "field sales"},
        {"req": "R4 — Want Block", "phase": "Partner track", "component": "PartP-1",
         "overrides": "cold outreach"},
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
    },
    "organisation": {
        "hq": {"name": "HQ", "op_id": "OP-1", "cost_ref": "arm", "functions": {
            "sales": {"name": "Sales", "driver": "deals", "fte": 1},
            "ops": {"name": "Ops", "driver": "cases", "fte": 1},
        }},
    },
    "components": {
        "CP-1": {"name": "offer", "def": "Offer", "allocated_to": "sales", "dri": "Head of Sales",
                 "doc": "the offer"},
        "WP-1": {"name": "service", "def": "Service", "allocated_to": "ops", "dri": "Head of Ops",
                 "doc": "the service"},
        "PartP-1": {"name": "broker_deal", "def": "BrokerDeal", "allocated_to": "sales",
                    "dri": "Head of Sales", "doc": "the partner deal"},
    },
    "flows": {
        "product": [{"name": "service_out", "item": "Service", "from": "venture",
                     "to": "business", "via": "WP-1"}],
        "information": [{"name": "offer_out", "item": "Offer", "from": "venture",
                         "to": "business", "via": "CP-1"}],
        "money": [{"name": "fee_in", "item": "Fee", "from": "business", "to": "venture",
                   "via": "WP-1"}],
    },
    "spine": ["CP-1", "WP-1", "PartP-1"],
}


def run_models(ctm, aom, tmp, with_aom=True):
    cpath = os.path.join(tmp, "test-ctm-model-at-C4.yaml")
    yaml.safe_dump(ctm, open(cpath, "w"))
    if with_aom:
        yaml.safe_dump(aom, open(os.path.join(tmp, "test-aom-model-at-C4.yaml"), "w"))
    p = subprocess.run([sys.executable, SCRIPT, cpath], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def case(label, mutate, want_code, want_text=None, with_aom=True):
    c, a = copy.deepcopy(CTM), copy.deepcopy(AOM)
    if mutate:
        mutate(c, a)
    with tempfile.TemporaryDirectory() as tmp:
        code, out = run_models(c, a, tmp, with_aom)
    ok = code == want_code and (want_text is None or want_text.lower() in out.lower())
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", label, code))
    if not ok:
        print("       wanted exit=%d text=%r" % (want_code, want_text))
        print("       got: %s" % out.strip().replace("\n", "\n            ")[:900])
    return ok


def main():
    print("check_requirement_trace.py regression set")
    results = []
    rows = lambda c: c["balm_mapping"]

    # --- the happy path, and it must say what it verified ---
    results.append(case("clean mapping resolves", None, 0, "VERDICT            : RESOLVED"))
    results.append(case("clean mapping reports the relations it checked", None, 0, "relations checked  : 5"))
    results.append(case("the reverse matrix is declared absent by design", None, 0, "not built, by design"))

    # --- 1. every requirement in force is claimed (cumulative to the state) ---
    def drop_r2(c, a):
        del rows(c)[1]
    results.append(case("a requirement in force with no row dangles", drop_r2, 2,
                        "R2 is in force at at-C4 and no mapping row claims it"))

    def later_state_more_in_force(c, a):
        c["state"] = "at-C5"
        a["state"] = "at-C5"
    results.append(case("advancing the state brings the next requirement into force",
                        later_state_more_in_force, 2, "R5 is in force at at-C5"))

    def claim_ahead(c, a):
        rows(c).append({"req": "R7 — Gateway", "phase": "Become", "component": "PartP-1",
                        "overrides": "x"})
    results.append(case("a claim beyond the state is noted, not refused", claim_ahead, 0,
                        "claims R7, which is beyond the model's state"))

    # --- 2. requirement ids and sub-requirements resolve ---
    def bad_req(c, a):
        rows(c)[0]["req"] = "R12 — nothing"
    results.append(case("a requirement outside the ten dangles", bad_req, 2,
                        "R12, which is not one of the ten"))

    def no_req(c, a):
        rows(c)[0]["req"] = "Workaround"
    results.append(case("a row naming no requirement dangles", no_req, 2, "names no requirement"))

    def sub_by_index(c, a):
        rows(c)[3]["req"] = "R4.4 — Attraction Strategy"
    results.append(case("a numbered sub-requirement within the list resolves", sub_by_index, 0, "RESOLVED"))

    def sub_index_out(c, a):
        rows(c)[3]["req"] = "R4.9 — nothing"
    results.append(case("a numbered sub-requirement beyond the list dangles", sub_index_out, 2,
                        "`.9` names none of them"))

    def sub_by_name(c, a):
        rows(c)[3]["sub_requirement"] = "Key Efficacy Doubt"
    results.append(case("a named sub-requirement the method defines resolves", sub_by_name, 0, "RESOLVED"))

    def sub_name_wrong(c, a):
        rows(c)[3]["sub_requirement"] = "Pricing Strategy"
    results.append(case("a named sub-requirement the method does not define dangles",
                        sub_name_wrong, 2, "no sub-requirement called `Pricing Strategy`"))

    # --- 3. phases resolve ---
    def bad_phase(c, a):
        rows(c)[0]["phase"] = "Phase 9 / Renewal"
    results.append(case("a phase outside the model dangles", bad_phase, 2,
                        "names the phase `Phase 9 / Renewal`"))

    def phase_by_number(c, a):
        rows(c)[0]["phase"] = "Phase 1"
    results.append(case("a numbered phase within the count resolves", phase_by_number, 0, "RESOLVED"))

    def phase_by_track_actor(c, a):
        rows(c)[3]["phase"] = "Insurance broker journey"
    results.append(case("a track named by its actor resolves", phase_by_track_actor, 0, "RESOLVED"))

    def track_absent(c, a):
        del c["partner_tracks"]
        c["phases"]["become"]["transitions"][0]["components"].append("PartP-1")
    results.append(case("a track reference when the model has no tracks dangles",
                        track_absent, 2, "names the phase `Partner track`"))

    # --- 4. components resolve to the register ---
    def unknown_component(c, a):
        rows(c)[0]["component"] = "WP-7 — a product nobody registered"
    results.append(case("a component absent from the register dangles", unknown_component, 2,
                        "names WP-7, which is not in the register"))

    def no_component_id(c, a):
        rows(c)[0]["component"] = "the service"
    results.append(case("a row with no component id dangles", no_component_id, 2,
                        "names no component id"))

    results.append(case("with no operating model, components resolve against the journey",
                        None, 0, "resolved against what the journey carries", with_aom=False))

    def unknown_without_aom(c, a):
        rows(c)[0]["component"] = "WP-7"
    results.append(case("with no operating model, an uncarried component dangles",
                        unknown_without_aom, 2, "not in the components the journey carries",
                        with_aom=False))

    # --- the pattern to read, not refuse (proposal §6.2) ---
    def one_component_everywhere(c, a):
        for r in rows(c):
            r["component"] = "WP-1"
    results.append(case("one component claimed for most requirements is noted, not refused",
                        one_component_everywhere, 0, "WP-1 is claimed against 4 of the 4"))

    # --- the model must load through the existing checker first (C-8) ---
    def broken(c, a):
        del c["routing"]
    results.append(case("a journey model the checker refuses is not traced", broken, 2,
                        "Nothing was traced"))

    def no_rows(c, a):
        c["balm_mapping"] = [{"req": "", "phase": "", "component": "", "overrides": ""}]
    results.append(case("empty rows are refused at load", no_rows, 2, "Nothing was traced"))

    # --- help ---
    h = subprocess.run([sys.executable, SCRIPT, "--help"], capture_output=True, text=True)
    ok = h.returncode == 0 and "C-5" in h.stdout
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", "--help prints the rule it executes", h.returncode))
    results.append(ok)

    print("")
    print("  %d/%d assertions passing" % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
