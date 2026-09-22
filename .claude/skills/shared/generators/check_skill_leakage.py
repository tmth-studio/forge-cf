#!/usr/bin/env python3
"""Refuse a design skill that names a studio venture.

RD-002, landed 10 September 2026. A design skill states the rule; the worked
example that produced it lives in the evidence companion, keyed by identifier.
A skill file that names a studio venture hands the next run an answer key.

Usage:
    python3 check_skill_leakage.py                # check every design skill
    python3 check_skill_leakage.py <file> [...]   # check named files

Exit 0 clean, exit 1 on any hit. Reports what it checked, per VA-105.
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.dirname(HERE)
SKILLS = os.path.dirname(SHARED)
VENTURE_LIST = os.path.join(SHARED, "studio-ventures.txt")

# ENFORCED — repaired, and a hit here refuses. Anything a venture run reads to
# DESIGN or to be SCORED must be blind-safe.
ENFORCED_GLOBS = [
    os.path.join(SKILLS, "balm-challenge-*-custom", "SKILL.md"),
    os.path.join(SKILLS, "balm-pco-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-architecture-generator-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-detailed-design-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-fit-verifier-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-fin-sim-custom", "SKILL.md"),
    os.path.join(SKILLS, "verify-balm-custom", "SKILL.md"),
    os.path.join(SKILLS, "verify-venture-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-consistency-audit-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-design-loop-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-aom-custom", "SKILL.md"),
]

# REPORTED — in scope for the rule and NOT YET REPAIRED. Listed every run so the
# residual is visible and dated rather than quietly out of scope. Move a file up
# to ENFORCED on the day it is repaired, and never the other way.
REPORTED_GLOBS = [
    os.path.join(SKILLS, "ive-ctm-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-conductor-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-build-pilot-custom", "SKILL.md"),
    os.path.join(SKILLS, "ive-valuation-custom", "SKILL.md"),
]


def load_ventures(path=VENTURE_LIST):
    """Return (venture names, allowed substrings)."""
    if not os.path.exists(path):
        return [], []
    names, allowed = [], []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("ALLOW:"):
            allowed.append(line[len("ALLOW:"):].strip())
        else:
            names.append(line)
    return names, allowed


def check_file(path, ventures, allowed):
    """Return a list of (line_no, venture, excerpt)."""
    hits = []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as exc:
        return [(0, "?", "cannot read: %s" % exc)]
    for i, line in enumerate(lines, 1):
        # Blank out the allowed substrings first, then look at what is left.
        scan = line
        for a in allowed:
            scan = re.sub(re.escape(a), " ", scan, flags=re.IGNORECASE)
        for v in ventures:
            if re.search(r"\b%s\b" % re.escape(v), scan, re.IGNORECASE):
                hits.append((i, v, line.strip()[:160]))
                break
    return hits


def main(argv):
    sys.path.insert(0, HERE)
    try:
        import toolchain_guard
        toolchain_guard.verify()
    except ImportError:
        print("REFUSED: toolchain_guard.py is not beside this script.")
        return 1
    except Exception as exc:
        print("TOOLCHAIN REFUSED: %s" % exc)
        return 1

    ventures, allowed = load_ventures()
    if not ventures:
        print("REFUSED: no venture list at %s. The check cannot run." % VENTURE_LIST)
        return 1

    pending = []
    if argv:
        files = list(argv)
    else:
        files = []
        for g in ENFORCED_GLOBS:
            files.extend(sorted(glob.glob(g)))
        for g in REPORTED_GLOBS:
            pending.extend(sorted(glob.glob(g)))

    if not files:
        print("REFUSED: no design skill files found to check.")
        return 1

    total_hits = []
    for f in files:
        hits = check_file(f, ventures, allowed)
        total_hits.extend((f, h) for h in hits)

    pending_hits = []
    for f in pending:
        pending_hits.extend((f, h) for h in check_file(f, ventures, allowed))

    comparisons = (len(files) + len(pending)) * len(ventures)
    print("Skill leakage check (RD-002)")
    print("  files enforced     : %d" % len(files))
    print("  files reported only: %d  (in scope, not yet repaired)" % len(pending))
    print("  venture names      : %d  (%s)" % (len(ventures), ", ".join(ventures)))
    print("  allowed substrings : %d  (%s)" % (len(allowed), ", ".join(allowed) or "none"))
    print("  comparisons made   : %d" % comparisons)

    if total_hits:
        print("  VERDICT            : FAIL — %d line(s) name a studio venture" % len(total_hits))
        print("")
        for f, (ln, v, excerpt) in total_hits:
            print("  %s:%d  names %s" % (os.path.relpath(f, SKILLS), ln, v))
            print("      %s" % excerpt)
        print("")
        print("  Repair: state the rule abstractly in the skill; move the worked example to")
        print("  04-Projects/Family_High_Performance/context/va-design-evidence.md and cite")
        print("  its key as `[evidence: KEY]`.")
        return 1

    if pending_hits:
        print("")
        print("  PENDING — %d line(s) in files not yet repaired. These do not refuse yet."
              % len(pending_hits))
        for f, (ln, v, excerpt) in pending_hits:
            print("      %s:%d  names %s" % (os.path.relpath(f, SKILLS), ln, v))
        print("      Repair each, then move its file from REPORTED_GLOBS to ENFORCED_GLOBS.")
    else:
        print("  pending files      : clean — move them to ENFORCED_GLOBS")

    print("  VERDICT            : PASS — %d enforced file(s) checked against %d names, no hit"
          % (len(files), len(ventures)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
