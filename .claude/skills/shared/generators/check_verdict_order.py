#!/usr/bin/env python3
"""Refuse a requirement verdict that is better than the worst verdict beneath it.

Written 16 September 2026 for the Head of R&D, from check C-4 of
`Forge/WS1/scorer-tiers-applied-to-ive-2026-09-10.md`. It makes VA-95
executable.

THE RULE IT EXECUTES (VA-95, Tom, 4 September 2026). The business form factor
accumulates, so a verdict is a statement about the cumulative architecture at
that point, not about one requirement alone. "No requirement carries a verdict
better than the worst verdict of any requirement it builds on." A downstream
requirement may repair an upstream failure only by naming the specific failed
check it closes and showing the arithmetic on the cumulative state; the
upstream verdict is annotated, never overwritten. A function gate reads the
cumulative verdict at its last challenge.

THE VERDICT ORDER. PASS is better than PROVISIONAL, which is better than FAIL.
That is the whole vocabulary for a gate verdict (criteria registry, three-limb
close). BORDERLINE is a value of the financial limb, not of the gate, and is
refused here.

WHAT A REQUIREMENT BUILDS ON. The challenge order, cumulative: R[n] builds on
every R[m] with m below n. This is read from the order and never from the
record's own declaration, because a record that declares fewer inherited
requirements gets a better floor (proposal §6.2). The cross-requirement
dependency matrix in `.claude/skills/ive-consistency-audit-custom/SKILL.md`
was read before this choice was made. It is a matrix of compatibility
tensions (nine named pairs), every forward pair of which is already inside
the cumulative order, and its one backward pair (R6 against R2) is a
compatibility check rather than an inheritance. The named pairs are kept in
this file so a report can say which named dependency a violation crosses.
The narrower chain the brief offered as a fallback (R1 to R2 to R3, then R2
to R4 through R8) is not used: it would let R9 ignore R4, which VA-95 forbids.

WHERE THE VERDICTS COME FROM. No machine-readable per-requirement verdict
record existed in the vault on 16 September 2026; the gate verdict block in
each challenge skill is prose. So this script reads a verdict record file,
one per venture, and prints a template with --template. Each requirement
states its verdict, the cumulative span it covers, and any repair it claims.

WHAT IT DOES NOT DO. It cannot apply VA-95 clause 4 — whether the failed check
would still fail against the cumulative state at the downstream point. A
repair claim that is fully stated is accepted for the floor and printed
loudly, and a reader decides whether it holds. A repair that names no check
or no arithmetic is not a repair and is refused.

Usage:
    python3 check_verdict_order.py <venture>-verdict-record.yaml
    python3 check_verdict_order.py --template > my-verdict-record.yaml
    python3 check_verdict_order.py --help

Exit 0 when every verdict respects the order, 2 when any does not or the
record could not be checked. Every run prints what it verified.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("REFUSED: PyYAML is not installed.")
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Better verdicts have a higher number. The gate vocabulary and nothing else.
RANK = {"FAIL": 0, "PROVISIONAL": 1, "PASS": 2}
REQ_ID = re.compile(r"^R(10|[1-9])$")
COVERS_RE = re.compile(r"^\s*C1\s*(?:to|-|–|—)\s*C(\d+)\s*$", re.I)
REQUIREMENT_NAMES = {
    1: "Workaround (at-scale cost bottleneck)",
    2: "Efficacy (customer value bottleneck)",
    3: "Scaling (working capital)",
    4: "Attraction (Want Block)",
    5: "Adoption (Use Block)",
    6: "Amortisation (Buy Block)",
    7: "Gateway partners",
    8: "Lock-in (switching cost)",
    9: "Lock-out (resource moat)",
    10: "Leverage (supplier replaceability)",
}
# The consistency audit's named pairs, forward direction only. Reporting aid;
# the floor is computed from the cumulative order, not from these.
NAMED_PAIRS = {
    (1, 2): "R1 cost structure -> R2 value ceiling",
    (1, 6): "R1 BFF -> R6 Amortisation",
    (3, 8): "R3 Scaling mechanism -> R8 Lock-in",
    (4, 7): "R4 Attraction -> R7 Gateway Partners",
    (5, 8): "R5 Adoption data -> R8 Lock-in",
    (7, 9): "R7 Gateway Partners -> R9 Scarce Resource",
    (8, 10): "R8 Lock-in -> R10 Competitive Moat",
    (9, 10): "R9 Scarce Resource -> R10 Competitive Moat",
}
FUNCTION_GATES = {3: "F1", 7: "F2", 10: "F3"}


class Refusal(Exception):
    pass


def announce_origin(model_path=None):
    """Refuse to run from a fork, and refuse if the toolchain fails its manifest."""
    try:
        import toolchain_guard
    except ImportError:
        raise Refusal("toolchain_guard.py is not beside this script. A checker "
                      "that cannot verify its own origin does not run.")
    try:
        toolchain_guard.require_canonical(model_path)
    except Exception as exc:
        raise Refusal(str(exc))


def req_number(key):
    m = REQ_ID.match(str(key).strip())
    if not m:
        raise Refusal("`%s` is not a requirement id. The ten requirements are R1 to R10."
                      % key)
    return int(m.group(1))


def verdict_of(entry, where):
    if not isinstance(entry, dict) or "verdict" not in entry:
        raise Refusal("%s has no `verdict`" % where)
    v = str(entry["verdict"]).strip().upper()
    if v not in RANK:
        extra = ""
        if v == "BORDERLINE":
            extra = (" BORDERLINE is a value of the financial limb, not of the gate; "
                     "the gate verdict is the conjunction of the three limbs.")
        raise Refusal("%s carries the verdict `%s`. A gate verdict is PASS, PROVISIONAL "
                      "or FAIL.%s" % (where, entry["verdict"], extra))
    return v


def check_covers(n, entry, where, notes):
    """VA-95 clause 1: the verdict names the cumulative span C1 to C[n]."""
    cov = entry.get("covers")
    if cov is None or str(cov).strip() == "":
        notes.append("%s states no `covers` span; VA-95 clause 1 asks for `C1 to C%d`"
                     % (where, n))
        return
    m = COVERS_RE.match(str(cov))
    if not m or int(m.group(1)) != n:
        raise Refusal("%s says it covers `%s`. A verdict is read on the cumulative "
                      "state, so R%d covers `C1 to C%d`." % (where, cov, n, n))


def repairs_of(n, entry, where, present):
    """Fully stated repair claims: (upstream number, check, arithmetic)."""
    raw = entry.get("repairs")
    if raw in (None, "", "none", "None", []):
        return []
    if isinstance(raw, dict):
        raw = [raw]
    if not isinstance(raw, list):
        raise Refusal("%s.repairs must be a list of claims, each naming `requirement`, "
                      "`check` and `arithmetic`" % where)
    out = []
    for i, r in enumerate(raw):
        rwhere = "%s.repairs[%d]" % (where, i)
        if not isinstance(r, dict):
            raise Refusal("%s is not a mapping" % rwhere)
        target = r.get("requirement")
        if target is None:
            raise Refusal("%s names no `requirement` it repairs" % rwhere)
        t = req_number(target)
        if t >= n:
            raise Refusal("%s claims to repair R%d, which R%d does not build on. A repair "
                          "runs downstream to upstream only." % (rwhere, t, n))
        if t not in present:
            raise Refusal("%s claims to repair R%d, which carries no verdict in this record"
                          % (rwhere, t))
        chk = str(r.get("check", "")).strip()
        if not chk:
            raise Refusal("%s names no `check`. A repair names the specific failed check "
                          "it closes, or it is not a repair (VA-95 clause 3)." % rwhere)
        arith = str(r.get("arithmetic", "")).strip()
        if not arith:
            raise Refusal("%s shows no `arithmetic`. A repair that cannot be shown in "
                          "arithmetic is not a repair (VA-95 clause 4)." % rwhere)
        out.append((t, chk, arith))
    return out


def check(path):
    if not os.path.exists(path):
        raise Refusal("no such file: %s" % path)
    try:
        rec = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as exc:
        raise Refusal("the record does not load: %s" % exc)
    if not isinstance(rec, dict):
        raise Refusal("%s does not hold a mapping" % path)
    reqs = rec.get("requirements")
    if not isinstance(reqs, dict) or not reqs:
        raise Refusal("the record has no `requirements` block. Run --template for the shape.")

    verdicts, entries = {}, {}
    for key, entry in reqs.items():
        n = req_number(key)
        if n in verdicts:
            raise Refusal("R%d appears twice in the record" % n)
        verdicts[n] = verdict_of(entry, "requirements.R%d" % n)
        entries[n] = entry

    notes, verified, violations, repair_lines = [], [], [], []
    present = set(verdicts)
    order = sorted(present)
    rows = []

    for n in order:
        where = "requirements.R%d" % n
        entry = entries[n]
        check_covers(n, entry, where, notes)
        upstream = list(range(1, n))
        missing = [m for m in upstream if m not in present]
        if missing:
            raise Refusal("R%d builds on R%s, which carr%s no verdict in this record. "
                          "The worst verdict beneath R%d cannot be known, so its verdict "
                          "cannot be checked. Record every requirement from R1 up."
                          % (n, ", R".join(str(m) for m in missing),
                             "ies" if len(missing) == 1 else "y", n))
        repairs = repairs_of(n, entry, where, present)
        repaired = set()
        for t, chk, arith in repairs:
            if verdicts[t] == "PASS":
                raise Refusal("%s claims to repair R%d, and R%d carries PASS. There is "
                              "nothing to repair." % (where, t, t))
            repaired.add(t)
            repair_lines.append("R%d claims to repair R%d (%s): check `%s`, arithmetic at %s"
                                % (n, t, verdicts[t], chk, arith))

        floor_sources = [m for m in upstream if m not in repaired]
        if floor_sources:
            # The earliest requirement at the worst rank, so the message names where
            # that verdict was first recorded.
            worst = min(floor_sources, key=lambda m: (RANK[verdicts[m]], m))
            floor = verdicts[worst]
        else:
            worst, floor = None, "PASS"
        if n == 1:
            verified.append("R1 (%s) has nothing beneath it" % verdicts[n])
        else:
            tail = (" with R%s repaired" % ", R".join(str(x) for x in sorted(repaired))
                    if repaired else "")
            verified.append("R%d (%s) against the worst verdict of R1 to R%d%s"
                            % (n, verdicts[n], n - 1, tail))

        # The record's own declaration is checked against the order, never used.
        decl = entry.get("inherited")
        if decl not in (None, "", "none", "None"):
            d = str(decl).strip().upper()
            if d in RANK and worst is not None and RANK[d] > RANK[floor]:
                violations.append("R%d declares it inherits `%s`; the order says the worst "
                                  "verdict beneath it is %s at R%d. The order governs, not "
                                  "the declaration." % (n, decl, floor, worst))

        status = "in order"
        if worst is not None and RANK[verdicts[n]] > RANK[floor]:
            named = [NAMED_PAIRS[(m, n)] for m in floor_sources
                     if (m, n) in NAMED_PAIRS and verdicts[m] == floor]
            via = (" This crosses the named dependency %s." % "; ".join(named)) if named else ""
            violations.append(
                "R%d carries %s and builds on R%d, which carries %s. No requirement carries "
                "a verdict better than the worst verdict of any requirement it builds on "
                "(VA-95). Either R%d is %s, or R%d names the failed check it repairs and "
                "shows the arithmetic.%s"
                % (n, verdicts[n], worst, floor, n, floor, n, via))
            status = "EXCEEDS %s at R%d" % (floor, worst)
        rows.append((n, verdicts[n], floor if worst is not None else "-", status))

    return rec, rows, verified, notes, violations, repair_lines


def report(path, rec, rows, verified, notes, violations, repair_lines):
    print("Verdict partial order — computed, not read")
    print("  record             : %s" % path)
    print("  venture            : %s" % rec.get("venture", "(unnamed)"))
    print("  date               : %s" % rec.get("date", "(unstated)"))
    print("  order              : PASS > PROVISIONAL > FAIL; R[n] builds on every R[m] below it")
    print("")
    print("  %-5s %-12s %-14s %s" % ("req", "verdict", "worst beneath", "status"))
    for n, v, floor, status in rows:
        print("  %-5s %-12s %-14s %s" % ("R%d" % n, v, floor, status))
    last = rows[-1][0] if rows else 0
    for n, gate in FUNCTION_GATES.items():
        if n <= last and any(r[0] == n for r in rows):
            v = [r[1] for r in rows if r[0] == n][0]
            print("  function gate %s reads the cumulative verdict at R%d: %s" % (gate, n, v))
    print("")
    print("  checks reaching a verdict : %d" % len(verified))
    for v in verified:
        print("      - %s" % v)
    if repair_lines:
        print("  repairs claimed — a reader applies clause 4 (would the check still fail on "
              "the cumulative state?):")
        for r in repair_lines:
            print("      - %s" % r)
    if notes:
        print("  notes:")
        for n in notes:
            print("      - %s" % n)
    print("")
    if violations:
        print("  out of order       : %d" % len(violations))
        for v in violations:
            print("      - %s" % v)
        print("  VERDICT            : REFUSED — the record breaks the order")
        return 2
    print("  VERDICT            : IN ORDER — every verdict is at most the worst beneath it")
    print("  This is a check on the record's own verdicts. It is not evidence that any "
          "verdict is right.")
    return 0


TEMPLATE = """\
# Verdict record — one per venture. Every requirement from R1 up to the
# current challenge, in order. The checker refuses a gap.
venture: <name>
date: 2026-09-16

requirements:
  R1:
    verdict: PASS                # PASS | PROVISIONAL | FAIL
    covers: C1 to C1             # the cumulative span the verdict was read on
    artefact: <the independent verification artefact, VA-90>
  R2:
    verdict: FAIL
    covers: C1 to C2
    artefact: <...>
  R3:
    verdict: FAIL                # may not be better than R2 without a repair
    covers: C1 to C3
    artefact: <...>
    repairs: none
  # A repair, when claimed, names the requirement, the specific failed check it
  # closes, and where the arithmetic on the cumulative state is shown:
  # R4:
  #   verdict: PROVISIONAL
  #   covers: C1 to C4
  #   repairs:
  #     - requirement: R2
  #       check: <the named check that failed at R2>
  #       arithmetic: <file and section showing it now holds on the cumulative state>
"""


def main(argv):
    if not argv or argv[0] in ("--help", "-h"):
        print(__doc__)
        return 0 if argv else 2
    if argv[0] == "--template":
        sys.stdout.write(TEMPLATE)
        return 0
    path = argv[0]
    try:
        announce_origin(path)
        rec, rows, verified, notes, violations, repair_lines = check(path)
    except Refusal as exc:
        print("REFUSED: %s" % exc)
        print("Nothing was ordered. There is no result to quote.")
        return 2
    return report(path, rec, rows, verified, notes, violations, repair_lines)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
