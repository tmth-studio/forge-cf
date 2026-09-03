"""Schema validator for CTM and AOM model files.

"A view can refuse to render; a model should refuse to load."

Standalone:  python3 validate_model.py <venture>-ctm-model-at-C<N>.yaml
Imported:    from validate_model import validate; errors, warnings = validate(path)

Every generator in this directory calls validate() before rendering and
exits on any error. Warnings print but do not block.

Checks, beyond per-field types:
- CTM: state ids unique and resolvable; every transition carried (components
  in Flow-Register format) or explicitly flagged; decision branches resolve;
  escalation outcomes well-formed; BALM mapping >= 5 rows.
- AOM: exactly one customer actor; enabler slots Part-N; org functions carry
  drivers; component allocations resolve; all three OMM flow classes present;
  flow endpoints resolve; spine covers every component exactly once;
  waypoints resolve both ends.
- Both: a jurisdiction block naming the country and the profile in force.
- Cross-model (when the sibling file exists for the same venture+state):
  every component ID the CTM uses must exist in the AOM's component register.
"""
import re, sys, pathlib
import yaml

FR_ID = re.compile(r"^(WP|CP|PP|PartP)-\d+$")
STATE_RE = re.compile(r"^at-C\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ACTOR_CLASSES = {"customer", "user", "anti_customer", "enabler"}

# --- Actor outcome + KMC rule (added 27 Aug 2026, Tom's ruling) -------------
# Every actor in the AOM carries a defined outcome and ONE key monetizable
# cost, assigned in the architecting phase. Before this rule, outcomes and
# costs were defined for the target customer at C2 and discovered ad hoc for
# everyone else — which is why the Actor Economics Audit had to go looking,
# and found two actors failing and three constraints unevidenced.
#
# Three design points, each from a real past failure:
#  - ONE cost per actor. Two costs means two actors; split them. (Same rule
#    as the TAM partition: a boundary that holds two costs is drawn wrong.)
#  - 'basis' is required and distinguishes a cost the actor bears in their
#    CURRENT routine from one that only exists once the venture does. The
#    25 Aug defendant correction is exactly this error; the field stops it
#    recurring silently. A venture_created cost must never anchor WTP.
#  - 'unstated' is a legitimate DECLARED value with an owner. Silently
#    missing is not. Same pattern as the market model's 'unmeasured'.
#
# Commodity vendors are exempt, per the vendor boundary test: if the
# counterparty's standard offer at standard terms suffices, no Partner
# Product is required and no loss needs eliminating. Claiming the exemption
# is explicit — species: commodity_vendor.
ENABLER_SPECIES = {"gateway", "capability", "commodity_vendor"}
KMC_TYPES = {"money", "fear", "stress"}
KMC_SUB_TYPES = {"expended", "foregone", "risk_borne", "friction"}
KMC_BASIS = {"current_routine", "venture_created"}
ACTOR_RULE_FROM = "2026-08-27"   # models dated before this warn; on/after, error
_ADVERBS = re.compile(r"\b\w+(?:ly)\b(?<!\bonly)(?<!\bfamily)(?<!\bsupply)", re.I)


def _check_actor_economics(aid, a, errs, warns, hard):
    """Outcome + exactly one KMC per actor. hard=False downgrades to warnings."""
    out = (errs if hard else warns)
    ctx = f"actors.{aid}"
    species = a.get("species")
    if a.get("class") == "enabler":
        if species and species not in ENABLER_SPECIES:
            errs.append(f"{ctx}: species '{species}' not in {sorted(ENABLER_SPECIES)}")
        if species == "commodity_vendor":
            if "kmc" in a or "outcome" in a:
                warns.append(f"{ctx}: commodity_vendor carries no Partner Product — "
                             f"outcome/kmc are not required and should be removed")
            return

    # --- outcome ---
    o = a.get("outcome")
    if not o:
        out.append(f"{ctx}: missing 'outcome' — every actor needs the outcome it already pursues")
    elif isinstance(o, str):
        if not o.strip().startswith("I "):
            warns.append(f"{ctx}.outcome: state it first person and clinical ('I ...'), got {o[:48]!r}")
        for m in _ADVERBS.finditer(o):
            warns.append(f"{ctx}.outcome: '{m.group(0)}' is an adverb — it smuggles the value "
                         f"proposition into the outcome. Strip it.")

    # --- kmc ---
    k = a.get("kmc")
    if k is None:
        out.append(f"{ctx}: missing 'kmc' — declare it, or declare it unstated with an owner")
        return
    if isinstance(k, list):
        errs.append(f"{ctx}.kmc: {len(k)} costs on one actor. Two costs means two actors — "
                    f"split the actor. (One focal cost per customer type.)")
        return
    if not isinstance(k, dict):
        errs.append(f"{ctx}.kmc: must be a mapping, got {type(k).__name__}")
        return

    if k.get("status") == "unstated":
        if not k.get("owner"):
            errs.append(f"{ctx}.kmc: unstated needs an 'owner' — who closes it")
        if not k.get("reason"):
            errs.append(f"{ctx}.kmc: unstated needs a 'reason' — why it is not stated")
        warns.append(f"{ctx}.kmc: UNSTATED, owner {k.get('owner')} — {str(k.get('reason'))[:90]}")
        return

    _require(k, ["statement", "type", "basis", "tier"], errs, f"{ctx}.kmc")
    if k.get("type") not in KMC_TYPES:
        errs.append(f"{ctx}.kmc.type '{k.get('type')}' not in {sorted(KMC_TYPES)}")
    subs = k.get("sub_type")
    subs = subs if isinstance(subs, list) else ([subs] if subs else [])
    if k.get("type") == "money" and not subs:
        errs.append(f"{ctx}.kmc: a money cost needs sub_type from {sorted(KMC_SUB_TYPES)}")
    for st in subs:
        if st not in KMC_SUB_TYPES:
            errs.append(f"{ctx}.kmc.sub_type '{st}' not in {sorted(KMC_SUB_TYPES)}")
    if k.get("basis") not in KMC_BASIS:
        errs.append(f"{ctx}.kmc.basis '{k.get('basis')}' not in {sorted(KMC_BASIS)} — "
                    f"say whether the actor bears this cost today or only once the venture exists")
    elif k.get("basis") == "venture_created":
        warns.append(f"{ctx}.kmc: basis is venture_created — this cost does NOT exist in the "
                     f"actor's current routine. It may support a participation-EV case. "
                     f"It must never anchor willingness to pay.")
    if not k.get("source"):
        warns.append(f"{ctx}.kmc: no source cited")


# --- Jurisdiction rule (added 3 Sep 2026) ----------------------------------
# A model file said which venture, which state and which date, and never which
# country. Every CTM and AOM in the Calmly set was built on England and Wales —
# county-court fee objects, Companies House, an English consumer statute — and
# not one file said so. Assessment methodology standard v2.0 makes the country a
# named setting a reader takes from a published profile (§7) instead of an
# assumption the document carries. A model file is a reader of that profile, so
# it names the profile it reads.
#
# There was no existing home for this. 'venture', 'state' and 'date' are scalars
# with fixed meanings, and overloading one of them would hide the country inside
# a field a reader scans past. So the schema gains one block, at the top level,
# alongside the other identity fields.
#
# Date-gated on the same pattern as the actor rule and VA-72: models dated on or
# after the rule warn-then-error, earlier snapshots stay valid as records of
# their time.
JURISDICTION_RULE_FROM = "2026-09-03"
PROFILE_RE = re.compile(r"^[A-Z]{2,4}-\d+$")


def _check_jurisdiction(m, errs, warns):
    hard = str(m.get("date", "")) >= JURISDICTION_RULE_FROM
    out = (errs if hard else warns)
    j = m.get("jurisdiction")
    if j is None:
        out.append("jurisdiction: missing — name the country this model is built on and the "
                   "published profile in force (standard v2.0 §7 rule 2). A model that does not "
                   "say which country it reads is read as every country.")
        return
    if not isinstance(j, dict):
        errs.append(f"jurisdiction: must be a mapping, got {type(j).__name__}")
        return
    _require(j, ["country", "profile"], errs, "jurisdiction")
    prof = str(j.get("profile", ""))
    if prof and not PROFILE_RE.match(prof):
        errs.append(f"jurisdiction.profile '{prof}' is not a profile name — a profile name is a "
                    f"country code and a serial number, for example 'EW-1' (standard §7, Naming)")
    std = j.get("standard")
    if std and not re.match(r"^v\d+\.\d+$", str(std)):
        errs.append(f"jurisdiction.standard '{std}' must be written as 'v2.0'")
    if not std:
        warns.append("jurisdiction: no 'standard' version stated — a report states the pair, "
                     "written 'v2.0 / EW-1'")


def _require(m, keys, errs, ctx="root"):
    for k in keys:
        if k not in m or m[k] in (None, "", []):
            errs.append(f"{ctx}: missing or empty '{k}'")


def _common(m, errs, warns):
    _require(m, ["venture", "state", "date"], errs)
    if "state" in m and not STATE_RE.match(str(m["state"])):
        errs.append(f"state '{m.get('state')}' must match at-C[N]")
    if "date" in m and not DATE_RE.match(str(m["date"])):
        errs.append(f"date '{m.get('date')}' must be YYYY-MM-DD")
    _check_jurisdiction(m, errs, warns)


def validate_ctm(m):
    errs, warns = [], []
    _common(m, errs, warns)
    _require(m, ["customer", "customer_doc", "timeline", "phases",
                 "balm_mapping", "review_findings", "routing"], errs)
    used_components = set()
    needs_escalation = False
    for pid, ph in (m.get("phases") or {}).items():
        ctx = f"phases.{pid}"
        if ph.get("undesigned"):
            _require(ph, ["name", "undesigned"], errs, ctx)
            continue
        _require(ph, ["name", "states", "transitions"], errs, ctx)
        states = ph.get("states") or []
        sids = [s.get("id") for s in states]
        if len(sids) != len(set(sids)):
            errs.append(f"{ctx}: duplicate state ids")
        for s in states:
            _require(s, ["id", "icon", "label"], errs, f"{ctx}.states")
            # Person-state register (28 Aug 2026): a CTM state is a person in a state of
            # belief/understanding/commitment — "[Actor] who ...". A label with no person
            # in it is usually a process step wearing a state's clothes. Heuristic, so warn.
            lbl = str(s.get("label", ""))
            if lbl and str(m.get("date", "")) >= "2026-08-28" and not re.search(
                    r"\bwho\b|\bwhose\b|\bthat (?:has|is|holds|can|believes|knows)\b", lbl, re.I):
                warns.append(f"{ctx}.states.{s.get('id')}: '{lbl[:60]}' reads as a process step, "
                             f"not a person-state — write it as '[Actor] who ...' (exemplar register)")
        valid = set(sids) | ({"decision"} if ph.get("decision") else set())
        finals = [s for s in states if s.get("final")]
        if not finals:
            warns.append(f"{ctx}: no final state marked")
        for t in ph.get("transitions") or []:
            tctx = f"{ctx}.{t.get('from')}→{t.get('to')}"
            for end in (t.get("from"), t.get("to")):
                if end not in valid:
                    errs.append(f"{tctx}: endpoint '{end}' does not resolve")
            if t.get("branch"):
                continue
            comps = t.get("components", [])
            if not comps and not t.get("flag"):
                errs.append(f"{tctx}: no components and no flag — every transition is carried or explicitly flagged")
            if comps and not t.get("label"):
                warns.append(f"{tctx}: carried transition has no label")
            # --- State-change narrative rule (added 28 Aug 2026, Tom's ruling) ---
            # The diagram shows THAT a transition happens; the mechanism lives nowhere.
            # Every carried transition must carry a written narrative: what changes in
            # the customer, which register it lands in, and HOW the 4-D product causes
            # it. "Easy to lose some of that context in the diagrams" — so the model
            # holds it and the generator renders it. Date-gated like the actor rule.
            if comps:
                hard = str(m.get("date", "")) >= "2026-08-28"
                sink = (errs if hard else warns)
                nar = t.get("narrative")
                if not isinstance(nar, dict):
                    sink.append(f"{tctx}: missing 'narrative' — every carried transition needs "
                                f"change_type / state_change / mechanism (rule of 28 Aug 2026)")
                else:
                    if nar.get("change_type") not in ("cognitive", "emotive", "behavioural"):
                        sink.append(f"{tctx}.narrative: change_type must be cognitive / emotive "
                                    f"/ behavioural, got {nar.get('change_type')!r}")
                    if not str(nar.get("state_change", "")).strip():
                        sink.append(f"{tctx}.narrative: missing 'state_change' — what is true of "
                                    f"the customer after this transition that was not true before")
                    mech = str(nar.get("mechanism", "")).strip()
                    if not mech:
                        sink.append(f"{tctx}.narrative: missing 'mechanism' — HOW the 4-D "
                                    f"product causes the change, not that it does")
                    elif len(mech.split()) < 8:
                        warns.append(f"{tctx}.narrative.mechanism: {len(mech.split())} words — "
                                     f"'{mech}' names the product, it does not explain the cause")
            for c in comps:
                if not FR_ID.match(str(c)):
                    errs.append(f"{tctx}: '{c}' is not a Flow-Register-format ID")
                used_components.add(c)
        dec = ph.get("decision")
        if dec:
            _require(dec, ["id", "label", "branch_a", "branch_b"], errs, f"{ctx}.decision")
            if dec.get("branch_a") not in set(sids):
                errs.append(f"{ctx}.decision: branch_a '{dec.get('branch_a')}' does not resolve to a state")
            if dec.get("branch_b") != "escalation":
                errs.append(f"{ctx}.decision: branch_b must be 'escalation'")
            else:
                needs_escalation = True
    # --- User tracks + partner tracks (added 1 Sep 2026, Tom's rulings) ---
    # The CTM's phases carry the CUSTOMER's journey. user_tracks: actors who use
    # the product without being the payer (Calmly: the disputants). partner_tracks:
    # enabler actors the Partner Product transforms — R7's journey, carried by the
    # historic CTM v3 "Track B" and lost in the Aug 2026 YAML migration; this key
    # restores it. Both: same person-state register, same narrative rule, same
    # component discipline — validated identically to a phase.
    for _key in ("user_tracks", "partner_tracks"):
      for uid, tr in (m.get(_key) or {}).items():
        ctx = f"{_key}.{uid}"
        _require(tr, ["actor", "role_note", "states", "transitions"], errs, ctx)
        states = tr.get("states") or []
        sids = [s.get("id") for s in states]
        if len(sids) != len(set(sids)):
            errs.append(f"{ctx}: duplicate state ids")
        for s in states:
            _require(s, ["id", "icon", "label"], errs, f"{ctx}.states")
            lbl = str(s.get("label", ""))
            if lbl and str(m.get("date", "")) >= "2026-08-28" and not re.search(
                    r"\bwho\b|\bwhose\b|\bthat (?:has|is|holds|can|believes|knows)\b", lbl, re.I):
                warns.append(f"{ctx}.states.{s.get('id')}: '{lbl[:60]}' reads as a process step, "
                             f"not a person-state — write it as '[Actor] who ...' (exemplar register)")
        if tr.get("decision"):
            errs.append(f"{ctx}: tracks do not carry decisions — forks belong to the customer phases")
        valid = set(sids)
        finals = [s for s in states if s.get("final")]
        if not finals:
            warns.append(f"{ctx}: no final state marked")
        for t in tr.get("transitions") or []:
            tctx = f"{ctx}.{t.get('from')}→{t.get('to')}"
            for end in (t.get("from"), t.get("to")):
                if end not in valid:
                    errs.append(f"{tctx}: endpoint '{end}' does not resolve")
            comps = t.get("components", [])
            if not comps and not t.get("flag"):
                errs.append(f"{tctx}: no components and no flag — every transition is carried or explicitly flagged")
            if comps and not t.get("label"):
                warns.append(f"{tctx}: carried transition has no label")
            if comps:
                hard = str(m.get("date", "")) >= "2026-08-28"
                sink = (errs if hard else warns)
                nar = t.get("narrative")
                if not isinstance(nar, dict):
                    sink.append(f"{tctx}: missing 'narrative' — every carried transition needs "
                                f"change_type / state_change / mechanism (rule of 28 Aug 2026)")
                else:
                    if nar.get("change_type") not in ("cognitive", "emotive", "behavioural"):
                        sink.append(f"{tctx}.narrative: change_type must be cognitive / emotive "
                                    f"/ behavioural, got {nar.get('change_type')!r}")
                    if not str(nar.get("state_change", "")).strip():
                        sink.append(f"{tctx}.narrative: missing 'state_change'")
                    mech = str(nar.get("mechanism", "")).strip()
                    if not mech:
                        sink.append(f"{tctx}.narrative: missing 'mechanism' — HOW the 4-D "
                                    f"product causes the change, not that it does")
                    elif len(mech.split()) < 8:
                        warns.append(f"{tctx}.narrative.mechanism: {len(mech.split())} words — "
                                     f"'{mech}' names the product, it does not explain the cause")
            for c in comps:
                if not FR_ID.match(str(c)):
                    errs.append(f"{tctx}: '{c}' is not a Flow-Register-format ID")
                used_components.add(c)
    # --- Absent 4-D class disposition (VA-72, 1 Sep 2026) ---
    # The roster's "not present in this journey" flag fired correctly on C1 and
    # sat inert until a human read it. A flag that requires a reader is not a
    # gate: every 4-D class absent from every transition must carry a stated
    # disposition in the model — not_designed_until: C<N> or not_applicable:
    # <reason> — and the model refuses to load without one. Date-gated: hard
    # for models dated on/after 2026-09-01, warn for earlier snapshots.
    _used_types = {str(c).rsplit("-", 1)[0] for c in used_components}
    _absent = [t for t in ("CP", "WP", "PP", "PartP") if t not in _used_types]
    if _absent:
        hard = str(m.get("date", "")) >= "2026-09-01"
        sink = (errs if hard else warns)
        disp = m.get("absent_products") or {}
        for t in _absent:
            d = disp.get(t)
            if not isinstance(d, dict) or not (
                    str(d.get("not_designed_until", "")).strip() or str(d.get("not_applicable", "")).strip()):
                sink.append(f"absent_products.{t}: no {t} component on any transition and no disposition — "
                            f"state not_designed_until: C<N> or not_applicable: <reason> (VA-72: "
                            f"a flag that requires a reader is not a gate)")
        for t, d in disp.items():
            if t not in _absent:
                warns.append(f"absent_products.{t}: disposition stated but {t} components ARE carried — remove the stale entry")
    if needs_escalation or m.get("escalation"):
        e = m.get("escalation") or {}
        _require(e, ["title", "timeline", "note", "outcomes"], errs, "escalation")
        for o in e.get("outcomes") or []:
            if o.get("kind") not in ("win", "lose"):
                errs.append(f"escalation outcome kind '{o.get('kind')}' must be win|lose")
            _require(o, ["label"], errs, "escalation.outcomes")
    if not m.get("balm_mapping"):
        errs.append("balm_mapping: empty")
    elif len(m["balm_mapping"]) < 4:
        warns.append(f"balm_mapping: only {len(m['balm_mapping'])} rows — check cumulative coverage for this challenge state")
    for r in m.get("balm_mapping") or []:
        _require(r, ["req", "phase", "component", "overrides"], errs, "balm_mapping")
    _require(m.get("routing") or {}, ["gate", "figures"], errs, "routing")
    return errs, warns, used_components


SPEC_VERSION = "2026-09-01"  # bumped when the model format or rendering rules change

def provenance(script_file, model_path):
    """Provenance stamp + stale-fork warning (VA-73, 1 Sep 2026).

    Two incidents (VA-64, and the 1 Sep 09:20 fork run) came from copies of shared
    tools drifting from the shared originals. Every generator stamps its resolved
    path and the spec version into its output, and warns loudly when the running
    script is not the one in .claude/skills/shared/generators/.

    The canonical directory is found by walking UP FROM THE MODEL FILE to the vault
    root — never from the running script or this module, because a fork that copies
    both files would carry its own reference point and pass its own check (caught
    live while testing this function, 1 Sep 2026).
    """
    import pathlib as _pl
    script = _pl.Path(script_file).resolve()
    canon = None
    for parent in _pl.Path(model_path).resolve().parents:
        cand = parent / ".claude" / "skills" / "shared" / "generators"
        if cand.is_dir():
            canon = cand.resolve()
            break
    if canon is None:
        return f"generated by {script} · spec {SPEC_VERSION} · canonical toolchain not locatable from model path"
    if script.parent != canon:
        print(f"  ⚠ PROVENANCE: running {script} — NOT the shared toolchain at {canon}. "
              f"A fork does not receive shared fixes (VA-73); output is stamped as fork-generated.")
        return f"generated by FORK {script} · spec {SPEC_VERSION} · shared toolchain at {canon} NOT used"
    return f"generated by {script} · spec {SPEC_VERSION}"



def jurisdiction_line(m):
    """One line naming the country and the profile, for a generated view's header.

    Every view of a model states the country the model reads, in the register that
    view uses. The model holds it as a field; the view says it in words.
    """
    j = m.get("jurisdiction") or {}
    country = j.get("country")
    profile = j.get("profile")
    std = j.get("standard")
    if not country and not profile:
        return "Jurisdiction not stated in the model"
    pair = f"{std} / {profile}" if std and profile else (profile or std or "")
    return f"{country}" + (f" · profile {pair}" if pair else "")


def venture_endpoint_ids(m):
    """The set of flow-endpoint ids that resolve to THE VENTURE itself.

    Single source of truth for venture-endpoint resolution (1 Sep 2026, closing the
    28 Aug audit's headline: VA-64 fixed this set in the validator, while all four
    view generators kept their own hardcoded copy and disagreed with it). Every
    generator imports THIS — never its own literal.
    Accepted: the literal "venture", the legacy "calmly" (so no existing model
    breaks), the slugified venture name, and its first word.
    """
    vname = (m.get("venture") or "").strip().lower()
    vslug = re.sub(r"[^a-z0-9]+", "", vname)
    vfirst = re.split(r"[^a-z0-9]+", vname)[0] if vname else ""
    return {"venture", "calmly"} | {s for s in (vslug, vfirst) if s}


def is_venture(endpoint, m):
    """True if this flow endpoint is the venture rather than an actor."""
    return str(endpoint) in venture_endpoint_ids(m)


def validate_aom(m):
    errs, warns = [], []
    _common(m, errs, warns)
    _require(m, ["scale_header", "actors", "organisation", "components", "flows", "spine"], errs)
    actors = m.get("actors") or {}
    customers = [a for a in actors.values() if a.get("class") == "customer"]
    if len(customers) != 1:
        errs.append(f"actors: exactly one class=customer required, found {len(customers)}")
    # Historical snapshots stay valid as records of their time; work dated on or
    # after the rule's introduction must comply.
    hard = str(m.get("date", "")) >= ACTOR_RULE_FROM
    for aid, a in actors.items():
        _require(a, ["name", "class", "doc"], errs, f"actors.{aid}")
        if a.get("class") not in ACTOR_CLASSES:
            errs.append(f"actors.{aid}: class '{a.get('class')}' not in {sorted(ACTOR_CLASSES)}")
        if a.get("class") == "enabler" and not re.match(r"^Part-\d+$", str(a.get("slot", ""))):
            errs.append(f"actors.{aid}: enabler needs slot 'Part-N', got '{a.get('slot')}'")
        _check_actor_economics(aid, a, errs, warns, hard)
    functions = {}
    for oid, o in (m.get("organisation") or {}).items():
        _require(o, ["name", "op_id", "cost_ref", "functions"], errs, f"organisation.{oid}")
        if not re.match(r"^OP-\d+$", str(o.get("op_id", ""))):
            errs.append(f"organisation.{oid}: op_id must be OP-N")
        for fid, fn in (o.get("functions") or {}).items():
            _require(fn, ["name", "driver"], errs, f"organisation.{oid}.{fid}")
            if "fte" not in fn:
                errs.append(f"organisation.{oid}.{fid}: missing 'fte' (number or null)")
            functions[fid] = fn
    comps = m.get("components") or {}
    names_seen = set()
    for cid, c in comps.items():
        if not FR_ID.match(str(cid)):
            errs.append(f"components: key '{cid}' is not Flow-Register format")
        _require(c, ["name", "def", "allocated_to", "dri", "doc"], errs, f"components.{cid}")
        if c.get("allocated_to") not in functions:
            errs.append(f"components.{cid}: allocated_to '{c.get('allocated_to')}' is not an org function")
        if c.get("name") in names_seen:
            errs.append(f"components.{cid}: duplicate name '{c.get('name')}'")
        names_seen.add(c.get("name"))
    flows = m.get("flows") or {}
    # The venture itself is a valid flow endpoint. Derive it from the model rather than
    # hardcoding one venture's name — the generators are shared across all IVE ventures, and a
    # hardcode here silently blocks every venture except that one (found 27 Aug 2026 building
    # a second venture's AOM; "calmly" was the only accepted venture endpoint).
    # Accepted: the literal "venture", the slugified venture name, and its first word.
    endpoints = set(actors) | venture_endpoint_ids(m)
    fnames = set()
    for cls in ("product", "information", "money"):
        if not flows.get(cls):
            errs.append(f"flows.{cls}: empty — the OMM three-flow decomposition requires all three classes")
            continue
        for f in flows[cls]:
            fctx = f"flows.{cls}.{f.get('name')}"
            _require(f, ["name", "item", "from", "to"], errs, fctx)
            if f.get("name") in fnames:
                errs.append(f"{fctx}: duplicate flow name")
            fnames.add(f.get("name"))
            for end in (f.get("from"), f.get("to")):
                if end not in endpoints:
                    errs.append(f"{fctx}: endpoint '{end}' does not resolve")
            via = f.get("via")
            if via and via not in comps:
                errs.append(f"{fctx}: via '{via}' is not a registered component")
            if not via and not f.get("flag") and not f.get("doc"):
                errs.append(f"{fctx}: uncarried flow needs a flag or doc explaining why")
    spine = m.get("spine") or []
    if sorted(spine) != sorted(comps):
        missing = set(comps) - set(spine)
        extra = set(spine) - set(comps)
        if missing:
            errs.append(f"spine: components missing: {sorted(missing)}")
        if extra:
            errs.append(f"spine: unknown ids: {sorted(extra)}")
        if len(spine) != len(set(spine)):
            errs.append("spine: duplicate entries")
    for cid, wps in (m.get("waypoints") or {}).items():
        if cid not in comps:
            errs.append(f"waypoints: '{cid}' is not a component")
        for w in wps:
            if w not in actors:
                errs.append(f"waypoints.{cid}: '{w}' is not an actor")
    return errs, warns, set(comps)


def validate(path):
    """Returns (errors, warnings). Model type detected from the filename."""
    path = pathlib.Path(path)
    try:
        m = yaml.safe_load(path.read_text())
    except Exception as ex:
        return [f"YAML does not parse: {ex}"], []
    if not isinstance(m, dict):
        return ["model file is not a YAML mapping"], []
    if "-ctm-model-" in path.name:
        errs, warns, used = validate_ctm(m)
        sibling = path.parent / path.name.replace("-ctm-model-", "-aom-model-")
        if sibling.exists():
            try:
                aom = yaml.safe_load(sibling.read_text())
                register = set(aom.get("components") or {})
                orphans = {c for c in used if c not in register}
                if orphans:
                    errs.append(f"cross-model: CTM uses components absent from the AOM register ({sibling.name}): {sorted(orphans)}")
            except Exception as ex:
                warns.append(f"cross-model: could not read {sibling.name}: {ex}")
        else:
            warns.append(f"cross-model: no sibling AOM model found ({sibling.name}) — component IDs unchecked against the register")
    elif "-aom-model-" in path.name:
        errs, warns, _ = validate_aom(m)
    else:
        return [f"cannot detect model type from filename '{path.name}' — expected -ctm-model- or -aom-model-"], []
    return errs, warns


def check_or_die(path):
    errs, warns = validate(path)
    for w in warns:
        print(f"  ⚠ {w}")
    if errs:
        print(f"MODEL INVALID — {pathlib.Path(path).name} refused to load:")
        for e in errs:
            print(f"  ✗ {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 validate_model.py <venture>-(ctm|aom)-model-at-C<N>.yaml")
        sys.exit(1)
    check_or_die(sys.argv[1])
    print(f"MODEL VALID — {pathlib.Path(sys.argv[1]).name}")
