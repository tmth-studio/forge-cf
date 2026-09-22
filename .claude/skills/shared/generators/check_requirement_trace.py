#!/usr/bin/env python3
"""Check that every requirement claim in a journey model resolves.

Written 16 September 2026 for the Head of R&D, from check C-5 of
`Forge/WS1/scorer-tiers-applied-to-ive-2026-09-10.md`.

THE RULE IT EXECUTES (C-5, as proposed). The method refuses a requirement-to-
component matrix on purpose: the ten BALM requirements are constraints the
whole business form factor satisfies together, and a clean one-to-one map is
the signature of bad synthesis (`ive-detailed-design-custom`). That rules out
one direction, not both. The other direction — each row of the journey's
requirement mapping names the requirement it serves, the phase it serves it in
and the component that does the work — still permits a coverage test, and
this script runs it:

  1. Every requirement from R1 up to the model's challenge state is claimed by
     at least one mapping row. The claim is cumulative: a model at C4 must
     claim R1 to R4, and R5 is not yet expected.
  2. Every requirement written in a row is one of the ten, and where a row
     names a sub-requirement (`R4.2`, or a `sub_requirement:` field with the
     name), that sub-requirement is one the method defines for R4.
  3. Every phase a row names resolves: a phase id or name in the model, a
     numbered phase within the model's count, or a user or partner track.
  4. Every component a row names resolves to the operating model's register,
     or, when no operating model sits beside the journey, to a component some
     transition carries.

WHERE THE CLAIM LIVES. The field is `balm_mapping` in the journey model, one
row per claim, with `req`, `phase`, `component` and `overrides`
(ctm-diagram-spec.md, section 2). No `satisfies:` or `trace:` field exists in
either model format, and this script does not invent one. The sub-requirement
names are the ones `verify-balm-custom` assesses, held in this file because a
script cannot read prose.

WHAT IT DOES NOT BUILD, BY DESIGN. It does not report components that claim
no requirement. That is the reverse direction, the matrix the method refuses,
and its absence here is deliberate, not an oversight. It does report, without
refusing, one component claimed against more than half the requirements in
force, because ten requirements on one component is the pattern the detailed
design skill warns about from the other side (proposal §6.2).

Usage:
    python3 check_requirement_trace.py <venture>-ctm-model-at-C<N>.yaml [--aom <file>]
    python3 check_requirement_trace.py --help

Exit 0 when every claim resolves and every requirement in force is claimed,
2 when any trace dangles or the check could not run. Every run prints what it
verified.
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

COMPONENT_IDS = re.compile(r"\b(?:WP|CP|PP|PartP)-\d+\b")
REQ_TOKEN = re.compile(r"\bR(\d+)(?:\.(\d+))?\b")
PHASE_NUMBER = re.compile(r"\bphase\s*(\d+)\b", re.I)
STATE_RE = re.compile(r"^at-C(\d+)$")

# The named sub-requirements of each requirement, in the order the method
# states them (verify-balm-custom, Step 2). `R4.2` is the second of R4's.
SUB_REQUIREMENTS = {
    1: ["Conventional Operational Model", "Critical Limiting Operation",
        "Workaround Theory of Change", "Workaround Strategy", "Business Form Factor"],
    2: ["High-Import Outcome & KPIs", "Key Monetizable Cost",
        "Efficacy Theory of Change", "Efficacy Strategy", "Business Form Factor"],
    3: ["Critical Limiting Operation II", "Scaling Theory of Change",
        "Scaling Strategy", "Business Form Factor"],
    4: ["Customer's Implicit Efficacy Theory", "Key Efficacy Doubt",
        "Attraction Theory of Change", "Attraction Strategy", "Business Form Factor"],
    5: ["Required Product Use Routine", "Key Learning Block",
        "Adoption Theory of Change", "Adoption Strategy", "Business Form Factor"],
    6: ["Key Customer Segments", "Amortisation Strategy", "Gateway Partner",
        "Business Form Factor"],
    7: ["Key Customer Segments", "Gateway Partner", "Integration Theory of Change",
        "Integration Strategy", "Business Form Factor"],
    8: ["Extended Product Use Routine", "Key Store of Value",
        "Lock-In Theory of Change", "Lock-In Strategy"],
    9: ["Required Core Competency", "Key Resource", "Lock-Out Theory of Change",
        "Lock-Out Strategy"],
    10: ["Interim Value Chain", "Key Input", "Leverage Theory of Change",
         "Leverage Strategy"],
}
TRACK_WORDS = {"user_tracks": ("user track", "user journey", "user + partner", "tracks"),
               "partner_tracks": ("partner track", "partner journey", "user + partner", "tracks")}


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


def load_mapping(path, what):
    if not os.path.exists(path):
        raise Refusal("no such file: %s" % path)
    try:
        m = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as exc:
        raise Refusal("%s does not load: %s" % (what, exc))
    if not isinstance(m, dict):
        raise Refusal("%s does not hold a mapping: %s" % (what, path))
    return m


def sibling_aom(ctm_path):
    d, name = os.path.split(ctm_path)
    direct = os.path.join(d, name.replace("-ctm-model-", "-aom-model-"))
    if os.path.exists(direct):
        return direct
    m = re.match(r"^(.*)-ctm-model-(at-C\d+)", name)
    if m:
        cand = os.path.join(d, "%s-aom-model-%s.yaml" % (m.group(1), m.group(2)))
        if os.path.exists(cand):
            return cand
    return None


def run_existing_checker(path, notes):
    """C-8: call the checker that exists. A model that does not load is not checked here."""
    try:
        import validate_model
    except ImportError:
        raise Refusal("validate_model.py is not beside this script; the model cannot "
                      "be loaded through the shared checker.")
    errs, warns = validate_model.validate(path)
    if errs:
        raise Refusal("%s refused to load through validate_model.py:\n    - %s"
                      % (os.path.basename(path), "\n    - ".join(errs[:12])))
    notes.append("%s loads through validate_model.py (%d warning(s))"
                 % (os.path.basename(path), len(warns)))


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def carried_components(ctm):
    out = set()
    for ph in (ctm.get("phases") or {}).values():
        for t in ph.get("transitions") or []:
            out |= set(str(c) for c in (t.get("components") or []))
    for key in ("user_tracks", "partner_tracks"):
        for tr in (ctm.get(key) or {}).values():
            for t in tr.get("transitions") or []:
                out |= set(str(c) for c in (t.get("components") or []))
    return out


def phase_resolves(text, ctm):
    """A phase id, a phase name, `Phase N` within the count, or a track."""
    t = norm(text)
    if not t:
        return False
    phases = ctm.get("phases") or {}
    for pid, ph in phases.items():
        if norm(pid) and re.search(r"\b%s\b" % re.escape(norm(pid)), t):
            return True
        name = norm((ph or {}).get("name", ""))
        if name and re.search(r"\b%s\b" % re.escape(name), t):
            return True
    for m in PHASE_NUMBER.finditer(str(text)):
        if 1 <= int(m.group(1)) <= len(phases):
            return True
    for key, phrases in TRACK_WORDS.items():
        tracks = ctm.get(key) or {}
        if not tracks:
            continue
        if any(norm(p) in t for p in phrases):
            return True
        for uid, tr in tracks.items():
            if norm(uid) in t or (norm((tr or {}).get("actor", "")) and
                                  norm(tr.get("actor")) in t):
                return True
    return False


def sub_requirement_resolves(n, index, name):
    """index from `R4.2`; name from a `sub_requirement:` field. Either may be absent."""
    subs = SUB_REQUIREMENTS[n]
    if index is not None and not (1 <= index <= len(subs)):
        return False, ("R%d has %d named sub-requirements; `.%d` names none of them"
                       % (n, len(subs), index))
    if name:
        wanted = norm(name)
        if not any(norm(s) == wanted or wanted in norm(s) for s in subs):
            return False, ("R%d has no sub-requirement called `%s`; the method names: %s"
                           % (n, name, "; ".join(subs)))
    return True, None


def check(ctm_path, aom_path):
    notes, verified, dangling = [], [], []
    run_existing_checker(ctm_path, notes)
    ctm = load_mapping(ctm_path, "journey model")

    m = STATE_RE.match(str(ctm.get("state", "")))
    if not m:
        raise Refusal("the journey model's `state` is `%s`; it must read at-C<N> so the "
                      "requirements in force are known" % ctm.get("state"))
    in_force = min(int(m.group(1)), 10)

    if aom_path:
        run_existing_checker(aom_path, notes)
        aom = load_mapping(aom_path, "operating model")
        register = set(str(k) for k in (aom.get("components") or {}))
        register_name = "the register in %s" % os.path.basename(aom_path)
    else:
        register = carried_components(ctm)
        register_name = "the components the journey carries (no operating model found)"
        notes.append("no operating model beside the journey model; components are "
                     "resolved against what the journey carries")

    rows = ctm.get("balm_mapping")
    if not isinstance(rows, list) or not rows:
        raise Refusal("the journey model has no `balm_mapping` rows; there is no claim to check")

    claimed = {}          # requirement number -> rows claiming it
    component_claims = {}  # component id -> set of requirement numbers
    verified.append("requirement ids in %d mapping rows are one of the ten" % len(rows))
    verified.append("sub-requirements named in rows resolve to the method's list")
    verified.append("phases named in rows resolve to a phase or track in the model")
    verified.append("components named in rows resolve to %s" % register_name)
    verified.append("every requirement from R1 to R%d is claimed by a row" % in_force)

    for i, row in enumerate(rows):
        where = "balm_mapping[%d]" % i
        if not isinstance(row, dict):
            dangling.append("%s is not a mapping row" % where)
            continue
        req_text = str(row.get("req", "")).strip()
        tokens = REQ_TOKEN.findall(req_text)
        if not tokens:
            dangling.append("%s names no requirement in `req: %s`. Write the requirement "
                            "as R1 to R10." % (where, req_text))
        for num, idx in tokens:
            n = int(num)
            if not 1 <= n <= 10:
                dangling.append("%s claims R%d, which is not one of the ten requirements"
                                % (where, n))
                continue
            ok, why = sub_requirement_resolves(n, int(idx) if idx else None,
                                               row.get("sub_requirement"))
            if not ok:
                dangling.append("%s: %s" % (where, why))
            claimed.setdefault(n, []).append(where)
            if n > in_force:
                notes.append("%s claims R%d, which is beyond the model's state at-C%d"
                             % (where, n, in_force))

        phase_text = row.get("phase", "")
        if not phase_resolves(phase_text, ctm):
            dangling.append("%s names the phase `%s`, which is not a phase or track in the "
                            "model. Phases: %s." % (where, phase_text,
                                                     ", ".join(ctm.get("phases") or {})))

        comp_text = str(row.get("component", ""))
        ids = COMPONENT_IDS.findall(comp_text)
        if not ids:
            dangling.append("%s names no component id in `component: %s`. Name the "
                            "component as CP-1, WP-2, PP-1 or PartP-1." % (where, comp_text[:60]))
        for cid in ids:
            if cid not in register:
                dangling.append("%s names %s, which is not in %s" % (where, cid, register_name))
            for num, _ in tokens:
                component_claims.setdefault(cid, set()).add(int(num))

    for n in range(1, in_force + 1):
        if n not in claimed:
            dangling.append("R%d is in force at at-C%d and no mapping row claims it. Every "
                            "requirement in force is served by at least one component in "
                            "the journey. Add a row naming the component that serves it."
                            % (n, in_force))

    limit = in_force / 2.0
    for cid, reqs in sorted(component_claims.items()):
        if len(reqs) > limit and len(reqs) >= 2:
            notes.append("%s is claimed against %d of the %d requirements in force (R%s). "
                         "One component serving most requirements is the pattern to read, "
                         "not refuse (proposal §6.2)."
                         % (cid, len(reqs), in_force, ", R".join(str(r) for r in sorted(reqs))))

    return ctm, in_force, len(rows), verified, notes, dangling


def report(ctm_path, aom_path, ctm, in_force, n_rows, verified, notes, dangling):
    print("Requirement trace — computed, not read")
    print("  journey model      : %s" % ctm_path)
    print("  operating model    : %s" % (aom_path or "(none beside the journey model)"))
    print("  venture            : %s" % ctm.get("venture", "(unnamed)"))
    print("  state              : %s   (R1 to R%d in force)" % (ctm.get("state"), in_force))
    print("  mapping rows       : %d" % n_rows)
    print("")
    print("  relations checked  : %d" % len(verified))
    for v in verified:
        print("      - %s" % v)
    if notes:
        print("  notes:")
        for n in notes:
            print("      - %s" % n)
    print("")
    print("  not built, by design: the reverse direction (components that claim no "
          "requirement). The method refuses a requirement-to-component matrix; see "
          "ive-detailed-design-custom.")
    print("")
    if dangling:
        print("  dangling traces    : %d" % len(dangling))
        for d in dangling:
            print("      - %s" % d)
        print("  VERDICT            : DANGLING — %d trace(s) do not resolve" % len(dangling))
        return 2
    print("  VERDICT            : RESOLVED — every claim resolves and every requirement in "
          "force is claimed")
    print("  This is a check that the claims resolve. It is not evidence that any "
          "component satisfies the requirement it claims.")
    return 0


def main(argv):
    if not argv or argv[0] in ("--help", "-h"):
        print(__doc__)
        return 0 if argv else 2
    aom_path, ctm_path = None, None
    i = 0
    while i < len(argv):
        if argv[i] == "--aom":
            if i + 1 >= len(argv):
                print("REFUSED: --aom needs a file after it.")
                return 2
            aom_path = argv[i + 1]
            i += 2
        elif ctm_path is None:
            ctm_path = argv[i]
            i += 1
        else:
            print("REFUSED: one journey model per run; `%s` is a second one." % argv[i])
            return 2
    if ctm_path is None:
        print("REFUSED: name the journey model file.")
        return 2
    try:
        announce_origin(ctm_path)
        if aom_path is None:
            aom_path = sibling_aom(ctm_path)
        ctm, in_force, n_rows, verified, notes, dangling = check(ctm_path, aom_path)
    except Refusal as exc:
        print("REFUSED: %s" % exc)
        print("Nothing was traced. There is no coverage result to quote.")
        return 2
    return report(ctm_path, aom_path, ctm, in_force, n_rows, verified, notes, dangling)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
