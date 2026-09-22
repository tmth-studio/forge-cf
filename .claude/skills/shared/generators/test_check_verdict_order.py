#!/usr/bin/env python3
"""Regression tests for check_verdict_order.py. Both directions on every rule."""
import copy
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "check_verdict_order.py")

BASE = {
    "venture": "Test Venture",
    "date": "2026-09-16",
    "requirements": {
        "R1": {"verdict": "PASS", "covers": "C1 to C1"},
        "R2": {"verdict": "PROVISIONAL", "covers": "C1 to C2"},
        "R3": {"verdict": "PROVISIONAL", "covers": "C1 to C3"},
        "R4": {"verdict": "FAIL", "covers": "C1 to C4"},
        "R5": {"verdict": "FAIL", "covers": "C1 to C5"},
    },
}
# R1 PASS, R2 and R3 PROVISIONAL, R4 and R5 FAIL: every verdict is at most the worst beneath it.


def run_record(rec, tmp):
    path = os.path.join(tmp, "test-verdict-record.yaml")
    yaml.safe_dump(rec, open(path, "w"))
    p = subprocess.run([sys.executable, SCRIPT, path], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def case(label, mutate, want_code, want_text=None):
    r = copy.deepcopy(BASE)
    if mutate:
        mutate(r)
    with tempfile.TemporaryDirectory() as tmp:
        code, out = run_record(r, tmp)
    ok = code == want_code and (want_text is None or want_text.lower() in out.lower())
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", label, code))
    if not ok:
        print("       wanted exit=%d text=%r" % (want_code, want_text))
        print("       got: %s" % out.strip().replace("\n", "\n            ")[:700])
    return ok


def main():
    print("check_verdict_order.py regression set")
    results = []
    R = lambda r: r["requirements"]

    # --- the happy path, and it must say what it verified ---
    results.append(case("a record in order passes", None, 0, "VERDICT            : IN ORDER"))
    results.append(case("a record in order reports the checks it made", None, 0, "checks reaching a verdict : 5"))
    results.append(case("a function gate reads the cumulative verdict at its last challenge",
                        None, 0, "function gate F1 reads the cumulative verdict at R3: PROVISIONAL"))

    # --- VA-95 clause 2: no verdict better than the worst beneath ---
    def pass_over_fail(r):
        R(r)["R5"]["verdict"] = "PASS"
    results.append(case("PASS above a FAIL is refused", pass_over_fail, 2,
                        "R5 carries PASS and builds on R4, which carries FAIL"))

    def provisional_over_fail(r):
        R(r)["R5"]["verdict"] = "PROVISIONAL"
    results.append(case("PROVISIONAL above a FAIL is refused", provisional_over_fail, 2, "VA-95"))

    def pass_over_provisional(r):
        R(r)["R3"]["verdict"] = "PASS"
    results.append(case("PASS above a PROVISIONAL is refused", pass_over_provisional, 2,
                        "R3 carries PASS and builds on R2, which carries PROVISIONAL"))

    def equal_is_fine(r):
        R(r)["R4"]["verdict"] = "PROVISIONAL"
        R(r)["R5"]["verdict"] = "PROVISIONAL"
    results.append(case("a verdict equal to the worst beneath is in order", equal_is_fine, 0, "IN ORDER"))

    def far_upstream(r):
        R(r)["R2"]["verdict"] = "FAIL"
        R(r)["R3"]["verdict"] = "FAIL"
        R(r)["R4"]["verdict"] = "FAIL"
        R(r)["R5"]["verdict"] = "PROVISIONAL"
    results.append(case("the floor reaches back to the first FAIL, not the nearest requirement",
                        far_upstream, 2, "builds on R2, which carries FAIL"))

    def named_pair(r):
        R(r)["R4"]["verdict"] = "PROVISIONAL"
        R(r)["R5"]["verdict"] = "PROVISIONAL"
        R(r)["R6"] = {"verdict": "PROVISIONAL", "covers": "C1 to C6"}
        R(r)["R7"] = {"verdict": "PASS", "covers": "C1 to C7"}
    results.append(case("a violation across a named dependency names the pair", named_pair, 2,
                        "R4 Attraction -> R7 Gateway Partners"))

    # --- VA-95 clause 3: a fully stated repair lifts the floor for that requirement ---
    def full_repair(r):
        R(r)["R5"]["verdict"] = "PROVISIONAL"
        R(r)["R5"]["repairs"] = [{"requirement": "R4",
                                  "check": "want block named and testable",
                                  "arithmetic": "test-r5-verification.md section 3"}]
    results.append(case("a repair naming the check and the arithmetic is accepted and printed",
                        full_repair, 0, "R5 claims to repair R4 (FAIL)"))

    def repair_no_check(r):
        full_repair(r)
        del R(r)["R5"]["repairs"][0]["check"]
    results.append(case("a repair naming no check is refused", repair_no_check, 2, "names no `check`"))

    def repair_no_arithmetic(r):
        full_repair(r)
        R(r)["R5"]["repairs"][0]["arithmetic"] = ""
    results.append(case("a repair showing no arithmetic is refused", repair_no_arithmetic, 2, "shows no `arithmetic`"))

    def repair_does_not_reach(r):
        # R5 repairs R4 and claims PASS, but R2 and R3 are PROVISIONAL and unrepaired
        full_repair(r)
        R(r)["R5"]["verdict"] = "PASS"
    results.append(case("a repair of one requirement does not lift another's floor",
                        repair_does_not_reach, 2, "R5 carries PASS and builds on R2"))

    def repair_of_pass(r):
        R(r)["R2"]["repairs"] = [{"requirement": "R1", "check": "x", "arithmetic": "y"}]
    results.append(case("a repair of a requirement that carries PASS is refused",
                        repair_of_pass, 2, "nothing to repair"))

    def repair_downstream(r):
        R(r)["R2"]["repairs"] = [{"requirement": "R4", "check": "x", "arithmetic": "y"}]
    results.append(case("a repair pointing downstream is refused", repair_downstream, 2,
                        "does not build on"))

    # --- proposal §6.2: inheritance is read from the order, not the declaration ---
    def missing_upstream(r):
        del R(r)["R3"]
    results.append(case("a gap below a requirement is refused", missing_upstream, 2,
                        "R4 builds on R3, which carries no verdict"))

    def declared_better(r):
        R(r)["R5"]["inherited"] = "PROVISIONAL"
    results.append(case("a declared inheritance better than the order says is refused",
                        declared_better, 2, "The order governs, not the declaration"))

    def declared_right(r):
        R(r)["R5"]["inherited"] = "FAIL"
    results.append(case("a declared inheritance that agrees with the order is accepted",
                        declared_right, 0, "IN ORDER"))

    # --- the vocabulary ---
    def borderline(r):
        R(r)["R3"]["verdict"] = "BORDERLINE"
    results.append(case("BORDERLINE is refused as a gate verdict", borderline, 2, "financial limb"))

    def unknown_word(r):
        R(r)["R3"]["verdict"] = "MOSTLY"
    results.append(case("an unknown verdict word is refused", unknown_word, 2, "PASS, PROVISIONAL or FAIL"))

    def bad_id(r):
        R(r)["R11"] = {"verdict": "PASS", "covers": "C1 to C11"}
    results.append(case("a requirement outside R1 to R10 is refused", bad_id, 2, "not a requirement id"))

    # --- VA-95 clause 1: the span is cumulative ---
    def wrong_span(r):
        R(r)["R3"]["covers"] = "C3"
    results.append(case("a verdict read on one challenge alone is refused", wrong_span, 2,
                        "read on the cumulative state"))

    def no_span(r):
        del R(r)["R3"]["covers"]
    results.append(case("a missing span is noted, not refused", no_span, 0, "states no `covers` span"))

    # --- template and help ---
    with tempfile.TemporaryDirectory() as tmp:
        t = subprocess.run([sys.executable, SCRIPT, "--template"], capture_output=True, text=True)
        path = os.path.join(tmp, "t.yaml")
        open(path, "w").write(t.stdout)
        p = subprocess.run([sys.executable, SCRIPT, path], capture_output=True, text=True)
    ok = t.returncode == 0 and p.returncode == 0 and "IN ORDER" in p.stdout
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", "the template checks in order", p.returncode))
    results.append(ok)

    h = subprocess.run([sys.executable, SCRIPT, "--help"], capture_output=True, text=True)
    ok = h.returncode == 0 and "VA-95" in h.stdout
    print("  %-4s %-62s exit=%d" % ("PASS" if ok else "FAIL", "--help prints the rule it executes", h.returncode))
    results.append(ok)

    print("")
    print("  %d/%d assertions passing" % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
