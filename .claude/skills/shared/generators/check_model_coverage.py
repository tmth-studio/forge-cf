#!/usr/bin/env python3
"""Check the journey model and the operating model against each other, both ways.

Written 16 September 2026 for the Head of R&D, from check C-2 of
`Forge/WS1/scorer-tiers-applied-to-ive-2026-09-10.md`. It makes regression
assertion R-W15 executable: a counterparty with no acquiring transition fails,
and an activity in the build with no component parent fails the same way.

THE RULE IT EXECUTES. Every designed product meets an actor in the journey, and
every state change in the journey is produced by something in the operating
model. Until today one direction existed (the model checker refuses a journey
that uses a component the register does not hold) and the reverse was never
tested. Three faults sat in prose comments in the Calmly operating model, each
found by a person over several days: a designed product no actor meets (CP-4),
a second one (PP-3), and flows whose endpoint was absent from the roster. All
three are set differences a machine finds in under a second.

WHAT IT CHECKS, IN THE DIRECTION OPERATING MODEL -> JOURNEY MODEL.
  1. Every component in the register is carried by at least one journey
     transition (customer phases, user tracks and partner tracks together), or
     carries a stated reason for not being: `disposition: { not_applicable:
     <reason> }` or `{ not_designed_until: C<N> }` on the component, the same
     vocabulary as RD-013 and VA-72.
  2. Every flow names the component that carries it, and that component is in
     the register. A flow with no component carries a `flag` saying why, or it
     is uncovered. A description alone is not a declaration of absence.
  3. Every flow endpoint is an actor in the roster, or the venture itself.
  4. Every actor in the roster is met by the journey: the customer by the
     phases, a user or anti-customer by a user track, a partner by a partner
     track or by a carried partner product flow that reaches them. A commodity
     vendor is exempt (validate_model.py, vendor boundary test). This is the
     first half of R-W15.

WHAT IT CHECKS, IN THE DIRECTION JOURNEY MODEL -> OPERATING MODEL.
  5. Every component a transition carries is in the register. (The model
     checker already refuses this; it is restated so the report is complete.)
  6. Every carried component is allocated to a function in the organisation
     block, so something in the operating model produces it.
  7. Every build component has a parent: a register component names it in
     `build_ref`, or a journey track names it as the `substitute` for a
     deliberate absence under VA-102. This is the second half of R-W15.

HOW ACTORS ARE MATCHED ACROSS THE TWO FILES. The journey model names an actor
in prose (`customer`, or a track's `actor`) and the operating model names it by
id and by `name`. The match is by words in common, either name contained in the
other, or the id written as words. A track may bind exactly with `aom_actor:
<id>`. Where the words do not match, the actor is reported as unmet, and the
fix is the binding field.

WHAT IT DOES NOT DO. It cannot tell whether the transition that carries a
component causes any real change in the actor. That is a reading of the
narrative and it stays with a reader. Section 6.2 of the proposal says this
plainly and so does this header.

Usage:
    python3 check_model_coverage.py <venture>-ctm-model-at-C<N>.yaml [more journey files]
                                    [--aom <venture>-aom-model-at-C<N>.yaml]
    python3 check_model_coverage.py --help

Where several journey files share one operating model (a venture with a
separate journey per actor), name them all; coverage is computed over the
union. Without --aom the operating model is the sibling file with
`-ctm-model-` replaced by `-aom-model-`.

Exit 0 when nothing is uncovered, 2 when anything is uncovered or the check
could not run. Every run prints what it verified, not only whether it passed.
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

COMPONENT_ID = re.compile(r"^(WP|CP|PP|PartP)-\d+$")
BUILD_ID = re.compile(r"\b[A-Z]{2,3}-\d{2,3}\b")
EXEMPT_SPECIES = {"commodity_vendor"}


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
    """The operating model beside a journey model, by the naming convention."""
    d, name = os.path.split(ctm_path)
    direct = os.path.join(d, name.replace("-ctm-model-", "-aom-model-"))
    if os.path.exists(direct):
        return direct
    m = re.match(r"^(.*)-ctm-model-(at-C\d+)", name)
    if m:
        cand = os.path.join(d, "%s-aom-model-%s.yaml" % (m.group(1), m.group(2)))
        if os.path.exists(cand):
            return cand
    return direct


def run_existing_checker(path, notes):
    """C-8: call the checker that exists. A model that does not load is not checked here."""
    try:
        import validate_model
    except ImportError:
        raise Refusal("validate_model.py is not beside this script; the models "
                      "cannot be loaded through the shared checker.")
    errs, warns = validate_model.validate(path)
    if errs:
        raise Refusal("%s refused to load through validate_model.py:\n    - %s"
                      % (os.path.basename(path), "\n    - ".join(errs[:12])))
    notes.append("%s loads through validate_model.py (%d warning(s))"
                 % (os.path.basename(path), len(warns)))
    return validate_model


def words(text):
    return set(w for w in re.split(r"[^a-z0-9]+", str(text).lower()) if len(w) > 2)


def actor_matches(aom_id, aom_actor, ctm_actor_text, bound_id=None):
    """Words in common, containment either way, or an exact binding by id."""
    if bound_id:
        return bound_id == aom_id
    ct = str(ctm_actor_text).lower().strip()
    if not ct:
        return False
    name = str(aom_actor.get("name", "")).lower().strip()
    id_as_words = aom_id.replace("_", " ").lower()
    for cand in (name, id_as_words):
        if cand and (cand in ct or ct in cand):
            return True
    return len(words(name) & words(ct)) >= 2


# --------------------------------------------------------------------------
# Reading the journey model
# --------------------------------------------------------------------------
def journey_carriage(ctm):
    """Components carried by any transition, with the transition that carries them."""
    carried = {}
    for pid, ph in (ctm.get("phases") or {}).items():
        for t in ph.get("transitions") or []:
            for c in t.get("components") or []:
                carried.setdefault(str(c), []).append(
                    "phases.%s %s->%s" % (pid, t.get("from"), t.get("to")))
    for key in ("user_tracks", "partner_tracks"):
        for uid, tr in (ctm.get(key) or {}).items():
            for t in tr.get("transitions") or []:
                for c in t.get("components") or []:
                    carried.setdefault(str(c), []).append(
                        "%s.%s %s->%s" % (key, uid, t.get("from"), t.get("to")))
    return carried


def journey_actors(ctm):
    """(kind, label, actor text, bound id) for the customer and every track."""
    out = [("customer", "customer", str(ctm.get("customer", "")),
            ctm.get("aom_actor"))]
    for key, kind in (("user_tracks", "user"), ("partner_tracks", "partner")):
        for uid, tr in (ctm.get(key) or {}).items():
            out.append((kind, "%s.%s" % (key, uid), str(tr.get("actor", "")),
                        tr.get("aom_actor")))
    return out


def journey_substitutes(ctm):
    """Text of every `arrival.substitute`, which may name a build component (VA-102)."""
    out = []
    for key in ("user_tracks", "partner_tracks"):
        for uid, tr in (ctm.get(key) or {}).items():
            arr = tr.get("arrival")
            if isinstance(arr, dict) and arr.get("substitute"):
                out.append(("%s.%s" % (key, uid), str(arr["substitute"])))
    return out


# --------------------------------------------------------------------------
# The checks
# --------------------------------------------------------------------------
def check(ctm_paths, aom_path):
    notes, verified = [], []
    uncovered = {"operating model -> journey model": [],
                 "journey model -> operating model": []}
    fwd = uncovered["operating model -> journey model"]
    rev = uncovered["journey model -> operating model"]

    vm = None
    for p in ctm_paths:
        vm = run_existing_checker(p, notes)
    vm = run_existing_checker(aom_path, notes)

    ctms = [(p, load_mapping(p, "journey model")) for p in ctm_paths]
    aom = load_mapping(aom_path, "operating model")

    register = aom.get("components") or {}
    actors = aom.get("actors") or {}
    functions = set()
    for o in (aom.get("organisation") or {}).values():
        functions |= set((o.get("functions") or {}).keys())
    endpoints = set(actors) | vm.venture_endpoint_ids(aom)

    carried = {}
    ctm_actor_rows = []
    substitutes = []
    for p, ctm in ctms:
        for c, where in journey_carriage(ctm).items():
            carried.setdefault(c, []).extend(
                "%s: %s" % (os.path.basename(p), w) for w in where)
        ctm_actor_rows.extend(journey_actors(ctm))
        substitutes.extend(journey_substitutes(ctm))

    # 1. Every register component is carried, or says why not.
    verified.append("register components carried by a journey transition (%d checked)"
                    % len(register))
    for cid, comp in register.items():
        disp = comp.get("disposition") if isinstance(comp, dict) else None
        has_disp = isinstance(disp, dict) and (
            str(disp.get("not_applicable", "")).strip()
            or str(disp.get("not_designed_until", "")).strip())
        if cid in carried:
            if has_disp:
                notes.append("%s carries a disposition and IS carried by %s — the "
                             "disposition is out of date, remove it" % (cid, carried[cid][0]))
            continue
        if has_disp:
            notes.append("%s is not carried by any transition; declared %s"
                         % (cid, "not applicable: %s" % disp.get("not_applicable")
                            if disp.get("not_applicable")
                            else "not designed until %s" % disp.get("not_designed_until")))
            continue
        fwd.append("%s (%s) is in the register and no journey transition carries it. "
                   "A designed product is met by no actor. Carry it on a transition, "
                   "or state on the component why it is absent: disposition: "
                   "{ not_applicable: <reason> } or { not_designed_until: C<N> }."
                   % (cid, comp.get("name", "unnamed") if isinstance(comp, dict) else "unnamed"))

    # 2 and 3. Every flow names a carrying component and resolves; endpoints resolve.
    flows = aom.get("flows") or {}
    n_flows = sum(len(v or []) for v in flows.values())
    verified.append("flows carrying a component that resolves to the register (%d checked)"
                    % n_flows)
    verified.append("flow endpoints in the actor roster or the venture (%d checked)"
                    % (2 * n_flows))
    partner_reach = {}   # actor id -> flows carried by a PartP the journey carries
    for cls, fl in flows.items():
        for f in fl or []:
            fname = "flows.%s.%s" % (cls, f.get("name"))
            via = f.get("via")
            if via is None or str(via).strip() == "":
                if f.get("flag"):
                    notes.append("%s has no component and declares why: %s"
                                 % (fname, str(f.get("flag"))[:80]))
                else:
                    fwd.append("%s names no component that carries it and declares no "
                               "reason. Name the component in `via`, or state the absence "
                               "in `flag`." % fname)
            elif str(via) not in register:
                fwd.append("%s is carried by `%s`, which is not in the register."
                           % (fname, via))
            for end in (f.get("from"), f.get("to")):
                if end not in endpoints:
                    fwd.append("%s runs to or from `%s`, which is not in the actor roster "
                               "and is not the venture. Add the actor, or correct the "
                               "endpoint." % (fname, end))
                elif end in actors and via and str(via).startswith("PartP") and str(via) in carried:
                    partner_reach.setdefault(end, []).append(fname)

    # 4. Every roster actor is met by the journey (R-W15, first half).
    checkable = {aid: a for aid, a in actors.items()
                 if isinstance(a, dict) and a.get("species") not in EXEMPT_SPECIES}
    verified.append("roster actors met by a journey track or a carried partner flow "
                    "(%d checked, %d commodity vendor(s) exempt)"
                    % (len(checkable), len(actors) - len(checkable)))
    for aid, a in checkable.items():
        cls = a.get("class")
        met_by = None
        for kind, label, text, bound in ctm_actor_rows:
            if actor_matches(aid, a, text, bound):
                met_by = label
                break
        if met_by is None and cls == "enabler" and aid in partner_reach:
            met_by = partner_reach[aid][0]
        if met_by is None:
            fwd.append("actor `%s` (%s, class %s) is in the roster and the journey never "
                       "meets it: no track names it and no carried partner product "
                       "reaches it. A counterparty with no acquiring transition fails "
                       "(R-W15). Give it a track, or bind an existing track with "
                       "aom_actor: %s." % (aid, a.get("name"), cls, aid))
        else:
            notes.append("actor `%s` met by %s" % (aid, met_by))

    # 5 and 6. Every carried component is registered and produced.
    verified.append("carried components present in the register (%d checked)" % len(carried))
    verified.append("carried components allocated to an organisation function (%d checked)"
                    % len(carried))
    for cid, where in sorted(carried.items()):
        if cid not in register:
            rev.append("%s is carried by %s and is not in the register. The journey "
                       "changes a state with a product the operating model does not "
                       "hold." % (cid, where[0]))
            continue
        comp = register[cid]
        alloc = comp.get("allocated_to") if isinstance(comp, dict) else None
        if alloc not in functions:
            rev.append("%s is carried by %s and is allocated to `%s`, which is not a "
                       "function in the organisation block. Nothing in the operating "
                       "model produces it." % (cid, where[0], alloc))

    # 7. Every build component has a parent (R-W15, second half).
    builds = aom.get("build_components") or {}
    verified.append("build components with a parent component or a journey substitute "
                    "(%d checked)" % len(builds))
    parents = {}
    for cid, comp in register.items():
        if isinstance(comp, dict):
            for b in comp.get("build_ref") or []:
                parents.setdefault(str(b), []).append(cid)
    for bid in builds:
        if bid in parents:
            continue
        named_by = [label for label, text in substitutes
                    if bid in BUILD_ID.findall(text)]
        if named_by:
            notes.append("build component %s has no parent component; it is the substitute "
                         "named by %s under VA-102, which is the permitted route"
                         % (bid, named_by[0]))
            continue
        rev.append("build component %s (%s) has no parent: no register component names it "
                   "in `build_ref` and no journey track names it as a substitute. An "
                   "activity in the build with no component parent fails (R-W15)."
                   % (bid, builds[bid].get("name", "unnamed")
                      if isinstance(builds[bid], dict) else "unnamed"))

    return uncovered, verified, notes


def report(ctm_paths, aom_path, uncovered, verified, notes):
    print("Two-way model coverage — computed, not read")
    for p in ctm_paths:
        print("  journey model      : %s" % p)
    print("  operating model    : %s" % aom_path)
    print("")
    print("  relations checked  : %d" % len(verified))
    for v in verified:
        print("      - %s" % v)
    if notes:
        print("  notes:")
        for n in notes:
            print("      - %s" % n)
    total = 0
    for direction, items in uncovered.items():
        print("")
        print("  %s: %d uncovered" % (direction, len(items)))
        for it in items:
            print("      - %s" % it)
        total += len(items)
    print("")
    print("  not checked, by design: whether the carrying transition causes a real "
          "change in the actor. That is a reading of the narrative (proposal §6.2).")
    if total:
        print("  VERDICT            : UNCOVERED — %d item(s) across both directions" % total)
    else:
        print("  VERDICT            : COVERED — every relation above held")
    return 2 if total else 0


def main(argv):
    if not argv or argv[0] in ("--help", "-h"):
        print(__doc__)
        return 0 if argv else 2
    aom_path = None
    ctm_paths = []
    i = 0
    while i < len(argv):
        if argv[i] == "--aom":
            if i + 1 >= len(argv):
                print("REFUSED: --aom needs a file after it.")
                return 2
            aom_path = argv[i + 1]
            i += 2
        else:
            ctm_paths.append(argv[i])
            i += 1
    if not ctm_paths:
        print("REFUSED: name at least one journey model file.")
        return 2
    try:
        announce_origin(ctm_paths[0])
        if aom_path is None:
            aom_path = sibling_aom(ctm_paths[0])
        uncovered, verified, notes = check(ctm_paths, aom_path)
    except Refusal as exc:
        print("REFUSED: %s" % exc)
        print("Nothing was compared. There is no coverage result to quote.")
        return 2
    return report(ctm_paths, aom_path, uncovered, verified, notes)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
