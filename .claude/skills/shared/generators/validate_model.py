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
- AOM, VA-147: every stated partner business case names the side of the
  partner's book it sits on; a loss-side partner is bounded by the pool the
  sibling market model states; a gain-side gateway over a loss-side candidate
  states an admissible reason with its arithmetic.
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
# Partners need a BUSINESS CASE, not a KMC (Tom's ruling, 1 Sep 2026). A KMC asks
# what loss the actor already carries; a partner is not buying relief from a loss,
# they are deciding whether supplying us beats their next-best use of the same
# capacity. Asking a partner for a KMC is what produced weeks of
# `kmc: unstated, owner: CEO` on Calmly's panel firm, assessor and three funders —
# the field was unanswerable, so it was carried unanswered.
PARTNER_RULE_FROM = "2026-09-01"
BUSINESS_CASE_FIELDS = ["earns", "costs", "beats_next_best", "operational_fit", "timing"]
# Every actor's track opens where the actor is NOT YET in the journey (VA-102,
# 7 Sep 2026). The four fixed Become states put arrival at the front of the
# CUSTOMER's journey and bind no other actor, so a funder track opened on a
# funder already at the table and nothing objected. The cost model then copied
# the journey model faithfully: Calmly costed "sell the layer into a site" and
# "work an opportunity that does not close", and costed nothing at all for
# finding a funder. The check asks where a track opens; it forbids no answer.
# A track may declare `arrival: { not_applicable: "<reason>" }` instead.
ARRIVAL_RULE_FROM = "2026-09-07"
# Words that mark a state as pre-engagement. Deliberately broad: the check is a
# prompt to state a disposition, not a judgement about wording quality.
_ARRIVAL_WORDS = re.compile(
    r"\b(unaware|does not know|has not heard|never heard|not yet know|"
    r"no knowledge|unknown to|has not encountered|does not yet know)\b", re.I)


# --- RD-014 (Head of R&D, 8 Sep 2026) -------------------------------------
# A transition between NON-NEIGHBOURING states is dropped in silence by every
# CTM renderer. generate_ctm_html.py and generate_ctm_drawio.py walk the state
# list in order and look up only (previous state -> this state); a transition
# that skips a state is never looked up, so no hexagon is drawn, no warning is
# raised, and the only visible symptom is a hexagon count that fails to rise.
# Reported by a venture architect on 7 Sep 2026: a component added to the model
# left the roster at 19 and the picture at 13, and the route the model said
# every customer would take was the one route the picture could not draw.
#
# The ruling: the renderer may be imperfect, but it may not be silent. A model
# that carries a transition no renderer can draw is rejected here, at the check,
# rather than discovered later in a diagram nobody can reconcile. Two legal
# answers: reorder the states so the transition is between neighbours, or
# declare it as a branch, which the renderer draws explicitly.
def _check_renderable_transitions(ctx, order, transitions, errs):
    pos = {sid: i for i, sid in enumerate(order)}
    for t in transitions or []:
        if t.get("branch"):
            continue
        a, b = t.get("from"), t.get("to")
        if a not in pos or b not in pos:
            continue          # unknown-endpoint case is already an error elsewhere
        if pos[b] - pos[a] != 1:
            errs.append(
                f"{ctx}: transition {a}->{b} skips {abs(pos[b] - pos[a]) - 1} state(s) in the "
                f"listed order. Every renderer draws only transitions between neighbouring "
                f"states, so this one would be dropped without a warning. Either reorder the "
                f"states so {a} and {b} are adjacent, or declare it with `branch:` so it is "
                f"drawn explicitly. (RD-014)")


def _check_track_arrival(key, uid, tr, errs, warns, hard):
    """VA-102 clause 1: a track opens at arrival, or says why not.

    The first state of a user or partner track is the actor before the venture
    acts on them. Where that state shows the actor already engaged, the track
    carries `arrival:` with either `not_applicable: <reason>` or
    `deliberate_absence: <reason>` plus `substitute: <the activity that does the
    work instead>` — clause 2, because an absence removes a product and never
    removes the work.
    """
    out = (errs if hard else warns)
    ctx = f"{key}.{uid}"
    states = tr.get("states") or []
    if not states:
        return
    first = str(states[0].get("label", ""))
    arrival = tr.get("arrival")
    if _ARRIVAL_WORDS.search(first):
        if isinstance(arrival, dict) and arrival.get("not_applicable"):
            warns.append(f"{ctx}.arrival: track opens on an unaware state AND declares "
                         f"not_applicable — one of the two is wrong")
        return
    if not isinstance(arrival, dict):
        out.append(
            f"{ctx}: opens on '{first[:70]}' — an actor already engaged with the venture. "
            f"VA-102: every actor track opens where the actor does not yet know the venture "
            f"exists, or carries `arrival:` with `not_applicable: <reason>`, or "
            f"`deliberate_absence: <reason>` + `substitute: <activity doing the work "
            f"instead>`. An activity named in prose and done by a person is in the "
            f"operating model or it is not in the venture.")
        return
    if arrival.get("not_applicable"):
        return
    if arrival.get("deliberate_absence"):
        sub = str(arrival.get("substitute", "")).strip()
        if not sub:
            out.append(f"{ctx}.arrival: deliberate_absence with no `substitute` — "
                       f"VA-102 clause 2, an absence removes a product, never the work")
        elif len(sub.split()) < 5:
            warns.append(f"{ctx}.arrival.substitute: {len(sub.split())} words — "
                         f"'{sub}' names no activity that a resource model could size")
        return
    out.append(f"{ctx}.arrival: present but declares neither `not_applicable` nor "
               f"`deliberate_absence` + `substitute`")
_ADVERBS = re.compile(r"\b\w+(?:ly)\b(?<!\bonly)(?<!\bfamily)(?<!\bsupply)", re.I)


def _check_partner_economics(aid, a, errs, warns, hard):
    """Partner (enabler) actors: outcome + a business case. NOT a KMC.

    Tom's ruling, 1 September 2026. A partner is not buying relief from a loss it
    already carries; it is deciding whether supplying us beats the next-best use of
    the same capacity. The five fields are the numbers that partner's own committee
    needs in order to say yes.
    """
    out = (errs if hard else warns)
    ctx = f"actors.{aid}"

    if "kmc" in a:
        out.append(f"{ctx}: a partner carries a BUSINESS CASE, not a 'kmc'. "
                   f"A KMC asks what loss they already carry; the question for a partner is "
                   f"whether supplying us beats their next-best use of the same capacity. "
                   f"Replace 'kmc' with 'business_case' ({', '.join(BUSINESS_CASE_FIELDS)}).")

    o = a.get("outcome")
    if not o:
        out.append(f"{ctx}: missing 'outcome' — every actor needs the outcome it already pursues")
    elif isinstance(o, str) and not o.strip().startswith("I "):
        warns.append(f"{ctx}.outcome: state it first person and clinical ('I ...'), got {o[:48]!r}")

    bc = a.get("business_case")
    if bc is None:
        out.append(f"{ctx}: missing 'business_case' — declare it, or declare it unstated "
                   f"with an owner. Fields: {', '.join(BUSINESS_CASE_FIELDS)}")
        return
    if not isinstance(bc, dict):
        errs.append(f"{ctx}.business_case: must be a mapping, got {type(bc).__name__}")
        return

    if bc.get("status") == "unstated":
        if not bc.get("owner"):
            errs.append(f"{ctx}.business_case: unstated needs an 'owner' — who closes it")
        if not bc.get("reason"):
            errs.append(f"{ctx}.business_case: unstated needs a 'reason' — why it is not stated")
        warns.append(f"{ctx}.business_case: UNSTATED, owner {bc.get('owner')} — "
                     f"{str(bc.get('reason'))[:90]}")
        return

    _require(bc, BUSINESS_CASE_FIELDS, errs, f"{ctx}.business_case")
    if isinstance(bc.get("beats_next_best"), str) and len(bc["beats_next_best"].strip()) < 12:
        warns.append(f"{ctx}.business_case.beats_next_best: state what the capacity would "
                     f"otherwise earn, in their numbers — a bare assertion is not a comparison.")


def _check_actor_economics(aid, a, errs, warns, hard, partner_hard=None):
    """Outcome + exactly one KMC per actor. hard=False downgrades to warnings.

    Enabler actors route to _check_partner_economics instead — partners need a
    business case, not a KMC (Tom, 1 September 2026).
    """
    if partner_hard is None:
        partner_hard = hard
    out = (errs if hard else warns)
    ctx = f"actors.{aid}"
    species = a.get("species")
    if a.get("class") == "enabler":
        if species and species not in ENABLER_SPECIES:
            errs.append(f"{ctx}: species '{species}' not in {sorted(ENABLER_SPECIES)}")
        if species == "commodity_vendor":
            if "kmc" in a or "outcome" in a or "business_case" in a:
                warns.append(f"{ctx}: commodity_vendor carries no Partner Product — "
                             f"outcome/kmc/business_case are not required and should be removed")
            return
        # gateway and capability are PARTNERS: business case, not KMC.
        _check_partner_economics(aid, a, errs, warns, partner_hard)
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


# --- Pool at risk and the side of the book (VA-147, RD-032, 17 Sep 2026) ----
# A gateway partner sits on one of two sides of the venture's effect. On the
# loss side the architecture takes a pool the partner earns today; on the gain
# side the venture pays it a fee. Tom's observation of 17 Sep 2026: the party
# that stands to LOSE the pool is the one to pitch to carry the product, and
# its price is the pool it loses, never the status quo (this corrects VA-127's
# status-quo comparison for that actor). The preference is not a gate: a
# gain-side selection is admissible on one of five stated reasons, each with
# its arithmetic.
#
# Two objects carry the rule. The market model states the pool per incumbent
# (a `pool_at_risk:` block, checked by validate_tam_model.py L11 — per
# incumbent, never only in aggregate). The partner's business case states which
# side it sits on (`effect_on_book:`), and the amount it carries is bounded by
# the pool the market model states. The AOM check below reads the sibling market
# model for that bound; it does not re-check the block's own shape.
POOL_RULE_FROM = "2026-09-23"
EFFECT_SIDES = ("loss_side", "gain_side")
# The admissible reasons for a gain-side selection with a loss-side candidate
# present (RD-032 §4.2). A reason outside this list is not a reason.
POOL_REASONS = ("absent_from_routine", "fails_operational_fit", "barred",
                "pool_below_cost_of_carrying", "lower_surplus_at_scale")
POOL_TIERS = {"T1", "T2", "T3", "T4"}
# What this check verified, one line per model (VA-105); check_or_die prints it.
POOL_REPORT = []
# The sibling market model, loaded by validate() for the file being checked.
_MARKET = {"model": None, "name": None}


def _load_sibling_market_model(path):
    """Find and load the market (TAM) model beside an AOM file.

    An explicit `market_model:` filename in the AOM wins. Otherwise the venture
    stem (the filename before `-aom-model-`) names `<stem>-tam-model.yaml`, or
    the last of `<stem>-tam-model*.yaml` in sorted order. None when absent.
    """
    _MARKET["model"], _MARKET["name"] = None, None
    POOL_REPORT[:] = []
    path = pathlib.Path(path)
    if "-aom-model-" not in path.name:
        return
    stem = path.name.split("-aom-model-")[0]
    candidates = [path.parent / f"{stem}-tam-model.yaml"]
    candidates += sorted(path.parent.glob(f"{stem}-tam-model*.yaml"))[::-1]
    try:
        m = yaml.safe_load(path.read_text())
        explicit = m.get("market_model") if isinstance(m, dict) else None
        if explicit:
            candidates.insert(0, path.parent / str(explicit))
    except Exception:
        pass
    for c in candidates:
        if c.exists():
            try:
                _MARKET["model"] = yaml.safe_load(c.read_text())
                _MARKET["name"] = c.name
            except Exception:
                _MARKET["model"], _MARKET["name"] = None, c.name
            return


def _pool_rows():
    """Incumbent rows from the sibling market model's pool_at_risk block, by id."""
    mm = _MARKET["model"]
    if not isinstance(mm, dict):
        return None
    block = mm.get("pool_at_risk")
    if not isinstance(block, dict) or block.get("status") == "none":
        return None
    rows = block.get("incumbents") or []
    return {str(row.get("id")): row for row in rows if isinstance(row, dict)}


def _check_pool_at_risk(m, actors, errs, warns):
    """VA-147: every partner business case states the side of the book it sits
    on; a loss-side partner is priced against the pool the market model states;
    a gain-side gateway chosen over a loss-side candidate states why."""
    hard = str(m.get("date", "")) >= POOL_RULE_FROM
    tag = "VA-147" + ("" if hard else " (warning — model dated before the rule)")
    sink = errs if hard else warns
    rows = _pool_rows()
    partners = {}
    for aid, a in actors.items():
        if not isinstance(a, dict) or a.get("class") != "enabler":
            continue
        if a.get("species") == "commodity_vendor":
            continue
        bc = a.get("business_case")
        if not isinstance(bc, dict) or bc.get("status") == "unstated":
            continue
        partners[aid] = a
    if not partners:
        POOL_REPORT.append("VA-147: no stated partner business case — nothing to classify")
        return

    sides = {}
    for aid, a in partners.items():
        ctx = f"actors.{aid}.business_case"
        eob = a["business_case"].get("effect_on_book")
        if not isinstance(eob, dict):
            sink.append(f"{tag} {ctx}: missing 'effect_on_book' — state the side of the "
                        f"partner's own book this venture sits on ({' | '.join(EFFECT_SIDES)}) "
                        f"and the signed amount a year, with source and tier")
            continue
        side = eob.get("side")
        if side not in EFFECT_SIDES:
            sink.append(f"{tag} {ctx}.effect_on_book.side: '{side}' — must be one of "
                        f"{' | '.join(EFFECT_SIDES)}")
            continue
        sides[aid] = side
        amount = eob.get("amount")
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            sink.append(f"{tag} {ctx}.effect_on_book.amount: must be a signed number a year, "
                        f"got {amount!r}")
            amount = None
        elif side == "loss_side" and amount >= 0:
            sink.append(f"{tag} {ctx}.effect_on_book.amount: loss_side carries a negative "
                        f"number (the pool the partner loses), got {amount}")
        elif side == "gain_side" and amount <= 0:
            sink.append(f"{tag} {ctx}.effect_on_book.amount: gain_side carries a positive "
                        f"number (the fee the venture pays), got {amount}")
        if not str(eob.get("source", "")).strip():
            sink.append(f"{tag} {ctx}.effect_on_book: no source cited for the amount")
        if eob.get("tier") not in POOL_TIERS:
            sink.append(f"{tag} {ctx}.effect_on_book.tier: '{eob.get('tier')}' — "
                        f"one of {sorted(POOL_TIERS)}")

        if side == "loss_side":
            # Priced against the pool, never the status quo: the pool row is the bound.
            ref = eob.get("pool_ref")
            if rows is None:
                sink.append(f"{tag} {ctx}: loss_side needs a sized pool_at_risk block in the "
                            f"sibling market model ({_MARKET['name'] or 'none found'}) — "
                            f"a loss-side actor is priced against the pool it loses")
            elif not ref or str(ref) not in rows:
                sink.append(f"{tag} {ctx}.effect_on_book.pool_ref: '{ref}' does not name an "
                            f"incumbent in {_MARKET['name']} pool_at_risk "
                            f"({', '.join(sorted(rows)) or 'no rows'})")
            elif amount is not None:
                band = (rows[str(ref)].get("pool_a_year") or {})
                high = band.get("high")
                if isinstance(high, (int, float)) and not isinstance(high, bool) \
                        and abs(amount) > high:
                    sink.append(f"{tag} {ctx}.effect_on_book.amount: {abs(amount)} exceeds the "
                                f"pool stated for '{ref}' (high {high}) — the pool figure "
                                f"is the bound, not the status quo")

    # A gain-side gateway with a loss-side candidate present states why.
    loss_candidate = bool(rows) or any(s == "loss_side" for s in sides.values())
    for aid, a in partners.items():
        if sides.get(aid) != "gain_side" or a.get("species") != "gateway":
            continue
        ctx = f"actors.{aid}.business_case"
        if rows is None and _MARKET["model"] is None:
            warns.append(f"VA-147 {ctx}: gain_side gateway — no sibling market model found, "
                         f"so whether a loss-side candidate exists is unchecked")
            continue
        if not loss_candidate:
            continue
        reason = a["business_case"].get("reason")
        if not isinstance(reason, dict) or reason.get("code") not in POOL_REASONS:
            sink.append(f"{tag} {ctx}: gain_side gateway with a loss-side candidate present "
                        f"needs reason.code from {' | '.join(POOL_REASONS)}, got "
                        f"{(reason or {}).get('code') if isinstance(reason, dict) else reason!r}")
        elif not str(reason.get("arithmetic", "")).strip():
            sink.append(f"{tag} {ctx}.reason: '{reason['code']}' carries no arithmetic — "
                        f"the reason is the number, not the label")

    n_loss = sum(1 for s in sides.values() if s == "loss_side")
    n_gain = sum(1 for s in sides.values() if s == "gain_side")
    POOL_REPORT.append(
        f"VA-147: {len(partners)} partner case(s) — {n_loss} loss side, {n_gain} gain side, "
        f"{len(partners) - len(sides)} unclassified; pool rows in "
        f"{_MARKET['name'] or 'no market model'}: {len(rows) if rows else 0}"
        + ("" if hard else " (warning only — model dated before the rule)"))


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
        _require(ph, ["name", "states"], errs, ctx)
        # RD-013 (Head of R&D, 8 Sep 2026): a phase may be DESIGNED and legitimately hold no
        # transition — an actor who does nothing in that phase. Calmly's claimant pays nothing:
        # zero at intake, zero on outcome, zero if they decline. That is an architectural
        # invariant, not an omission, and the format previously could not say so. The only
        # workarounds were to invent a self-transition (routing around a working check) or to
        # move a transition between phases (a design act). Distinct from 'undesigned', which
        # means not yet designed. Same shape as absent_products, per VA-72: a flag that
        # requires a reader is not a gate, so the absence must be DECLARED, not left silent.
        _disp = ph.get("disposition")
        _has_disp = isinstance(_disp, dict) and (
            str(_disp.get("not_applicable", "")).strip() or str(_disp.get("not_designed_until", "")).strip())
        if not (ph.get("transitions") or []):
            if _has_disp:
                _na = str(_disp.get("not_applicable", "")).strip()
                if _na and len(_na) < 40:
                    warns.append(f"{ctx}.disposition.not_applicable: too short to explain why the "
                                 f"phase is empty — state the invariant, not a label")
            else:
                errs.append(f"{ctx}: missing or empty 'transitions' — or, if the phase is designed "
                            f"and legitimately empty, declare it: disposition: {{ not_applicable: "
                            f"<reason> }} or {{ not_designed_until: C<N> }} (RD-013)")
        elif _has_disp:
            warns.append(f"{ctx}.disposition: stated but the phase HAS transitions — remove the stale entry")
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
        _check_renderable_transitions(ctx, [s.get("id") for s in (ph.get("states") or [])],
                                      ph.get("transitions"), errs)
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
        # VA-102 (7 Sep 2026) — the track opens at arrival, or says why not.
        _check_renderable_transitions(ctx, [x.get("id") for x in (tr.get("states") or [])],
                                      tr.get("transitions"), errs)
        _check_track_arrival(_key, uid, tr, errs, warns,
                             str(m.get("date", "")) >= ARRIVAL_RULE_FROM)
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
    partner_hard = str(m.get("date", "")) >= PARTNER_RULE_FROM
    for aid, a in actors.items():
        _require(a, ["name", "class", "doc"], errs, f"actors.{aid}")
        if a.get("class") not in ACTOR_CLASSES:
            errs.append(f"actors.{aid}: class '{a.get('class')}' not in {sorted(ACTOR_CLASSES)}")
        if a.get("class") == "enabler" and not re.match(r"^Part-\d+$", str(a.get("slot", ""))):
            errs.append(f"actors.{aid}: enabler needs slot 'Part-N', got '{a.get('slot')}'")
        _check_actor_economics(aid, a, errs, warns, hard, partner_hard)
    _check_pool_at_risk(m, actors, errs, warns)
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
    _load_sibling_market_model(path)
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
    # The origin check is a REFUSAL, not a warning (R-CTM8, closed 10 Sep 2026).
    # This script writes no document, so a forked copy used to announce nothing.
    try:
        sys.path.insert(0, str(pathlib.Path(__file__).parent))
        import toolchain_guard
        toolchain_guard.require_canonical(path)
    except ImportError:
        print("TOOLCHAIN REFUSED: toolchain_guard.py is not beside this script. "
              "A checker that cannot verify its own origin does not run.")
        sys.exit(2)
    except Exception as exc:
        print("TOOLCHAIN REFUSED: %s" % exc)
        print("Nothing was validated. There is no verdict to quote.")
        sys.exit(2)

    errs, warns = validate(path)
    for w in warns:
        print(f"  ⚠ {w}")
    if errs:
        print(f"MODEL INVALID — {pathlib.Path(path).name} refused to load:")
        for e in errs:
            print(f"  ✗ {e}")
        for line in POOL_REPORT:
            print(f"  · {line}")
        sys.exit(1)
    for line in POOL_REPORT:
        print(f"  · {line}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 validate_model.py <venture>-(ctm|aom)-model-at-C<N>.yaml")
        sys.exit(1)
    check_or_die(sys.argv[1])
    print(f"MODEL VALID — {pathlib.Path(sys.argv[1]).name}")
