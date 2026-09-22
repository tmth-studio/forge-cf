#!/usr/bin/env python3
"""
Validate a TAM model file.

The TAM model is the single source of truth for a venture's market size and
segmentation. This checker refuses an incoherent model, in the same way the
CTM and AOM generators refuse to write on a broken model.

Usage:
    python3 validate_tam_model.py <path-to-tam-model.yaml>

Exit 0 = clean. Exit 1 = one or more checks failed.

THE RULE THIS ENFORCES ABOVE ALL OTHERS (L2):
    A segment is a set of demand units (e.g. disputes, transactions) that share ONE key monetizable cost.
    If two sub-classes have different KMCs, they are different segments,
    however similar the parties look. R2 states this as one focal cost per
    customer type. A partition by who-sues-whom breaks it silently.

Added 27 August 2026, after the Calmly segment addressability audit found four
non-conformances that all trace back to a non-KMC partition.

L11 (added 21 September 2026, VA-147 / RD-032): the pool at risk is stated per
incumbent R2 names, each reading with a source tier, or its absence is declared
with a reason. Refused on models dated on or after 2026-09-23; warned before.
"""

import sys
import pathlib

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is not installed. Run: pip3 install pyyaml")
    sys.exit(1)


VALID_ADDRESSABILITY = {"addressable", "partly", "not"}
VALID_TIERS = {"T1", "T2", "T3", "T4", "unmeasured", "ESTIMATE"}


class Report:
    def __init__(self):
        self.failures = []
        self.warnings = []
        self.notes = []

    def fail(self, code, msg):
        self.failures.append((code, msg))

    def warn(self, code, msg):
        self.warnings.append((code, msg))

    def note(self, msg):
        self.notes.append(msg)


def check_L1_every_subclass_has_one_known_kmc(m, r):
    """L1 — every sub-class names exactly one KMC, and that KMC is defined."""
    known = {k["id"] for k in m.get("kmc_classes", [])}
    if not known:
        r.fail("L1", "no kmc_classes defined — the model has no partition key")
        return
    for sc in m.get("sub_classes", []):
        kmc = sc.get("kmc")
        if kmc is None:
            r.fail("L1", f"{sc.get('id')} has no kmc — every sub-class must name exactly one")
        elif isinstance(kmc, list):
            r.fail("L1", f"{sc.get('id')} names {len(kmc)} KMCs — a sub-class carries exactly one. Split it.")
        elif kmc not in known:
            r.fail("L1", f"{sc.get('id')} names unknown KMC '{kmc}'")


def check_L2_segment_kmc_purity(m, r):
    """L2 — THE PARTITION RULE. A segment holds exactly one KMC."""
    kmc_by_sc = {sc["id"]: sc.get("kmc") for sc in m.get("sub_classes", [])}

    def audit(block, label, hard):
        for seg in block.get("segments", []):
            ids = seg.get("sub_classes", [])
            kmcs = {kmc_by_sc.get(i) for i in ids if i in kmc_by_sc}
            kmcs.discard(None)
            if len(kmcs) > 1:
                msg = (f"{label} {seg.get('id')} ('{seg.get('name')}') holds {len(kmcs)} "
                       f"different KMCs: {sorted(kmcs)}. A segment carries ONE. Split it.")
                (r.fail if hard else r.warn)("L2", msg)

    proposed = m.get("proposed_segments", {})
    recorded = m.get("recorded_segments", {})

    # The proposed partition is the one that must be clean.
    audit(proposed, "proposed segment", hard=True)
    # The recorded partition is retained for traceability; impurity there is the
    # known defect, so it warns rather than fails — but only if declared.
    if recorded and not recorded.get("defect"):
        r.fail("L2", "recorded_segments has no 'defect' field. If the recorded partition "
                     "is not KMC-based, say so in the model — do not leave it implied.")
    audit(recorded, "recorded segment", hard=False)


def check_L3_shares_sum(m, r):
    """L3 — recorded segment shares must be able to sum to 100%."""
    for block, label in ((m.get("recorded_segments", {}), "recorded"),
                         (m.get("proposed_segments", {}), "proposed")):
        segs = [s for s in block.get("segments", []) if "share_pct" in s]
        if not segs:
            continue
        lo = sum(s["share_pct"][0] for s in segs)
        hi = sum(s["share_pct"][1] for s in segs)
        if not (lo <= 100 <= hi):
            r.fail("L3", f"{label} segment shares cannot sum to 100% "
                         f"(range {lo}–{hi}%). The partition is not exhaustive.")


def check_L4_addressability_verdicts(m, r):
    """L4 — every sub-class carries a verdict, and it is consistent with its KMC."""
    for sc in m.get("sub_classes", []):
        v = sc.get("addressability")
        sid = sc.get("id")
        if v is None:
            r.fail("L4", f"{sid} has no addressability verdict")
            continue
        if v not in VALID_ADDRESSABILITY:
            r.fail("L4", f"{sid} has invalid verdict '{v}' — expected one of {sorted(VALID_ADDRESSABILITY)}")
            continue
        # KMC-0 means a supplied alternative eliminates the cost.
        if sc.get("kmc") == "KMC-0" and v == "addressable":
            r.fail("L4", f"{sid} carries KMC-0 (no monetizable cost) but is marked addressable. "
                         f"Contradiction — either the KMC or the verdict is wrong.")
        if sc.get("kmc") != "KMC-0" and v == "not":
            r.warn("L4", f"{sid} is marked not addressable but carries a live KMC ({sc.get('kmc')}). "
                         f"If a supplied alternative eliminates it, its KMC is KMC-0.")


def check_L5_supplied_alternative_evidence(m, r):
    """L5 — a 'not addressable' verdict needs a named alternative, not an assertion."""
    for sc in m.get("sub_classes", []):
        if sc.get("addressability") not in ("not", "partly"):
            continue
        alt = sc.get("supplied_alternative")
        sid = sc.get("id")
        if not alt or not alt.get("route"):
            r.fail("L5", f"{sid} is screened out with no named supplied alternative. "
                         f"Name the route, or the screen is an assertion.")
            continue
        if sc.get("addressability") == "not" and not alt.get("sources"):
            r.warn("L5", f"{sid} is screened out entirely with no source cited for its alternative")


def check_L6_no_invented_shares(m, r):
    """L6 — a share is either measured with a tier, or explicitly unmeasured. Never guessed."""
    for sc in m.get("sub_classes", []):
        share = sc.get("share_of_segment")
        sid = sc.get("id")
        if share is None:
            r.fail("L6", f"{sid} has no share_of_segment field — use {{value: null, tier: unmeasured}}")
            continue
        tier = share.get("tier")
        if tier not in VALID_TIERS:
            r.fail("L6", f"{sid} share tier '{tier}' invalid — expected one of {sorted(VALID_TIERS)}")
        if share.get("value") is not None and tier == "unmeasured":
            r.fail("L6", f"{sid} carries a share value with tier 'unmeasured'. "
                         f"A number with no measurement is a guess — remove it or tier it.")


def check_L7_volume_basis_declared(m, r):
    """L7 — the volume figure must declare whether it counts incidence or residual."""
    vol = m.get("volume", {})
    basis = vol.get("basis")
    if basis not in ("incidence", "residual"):
        r.fail("L7", "volume.basis must be 'incidence' or 'residual'. Undeclared basis is how "
                     "a segment share ends up divided by the wrong denominator.")
        return
    if basis == "incidence":
        residual_defined = any(
            sc.get("supplied_alternative") for sc in m.get("sub_classes", [])
        )
        if residual_defined:
            r.warn("L7", "volume.basis is 'incidence' while sub-classes are defined against "
                         "supplied alternatives (a residual). These count different populations. "
                         "Any segment share quoted against this volume uses the wrong denominator.")


def check_L8_gates_and_screens(m, r):
    """L8 — if a qualifying gate was not applied at sizing, the model must say so."""
    for g in m.get("definition", {}).get("gates", []):
        if g.get("status") == "NOT_APPLIED_AT_SIZING" and not g.get("note"):
            r.fail("L8", f"gate {g.get('id')} is flagged as not applied at sizing with no note "
                         f"explaining the consequence")


def check_L9_surviving_arithmetic(m, r):
    """L9 — the surviving-TAM arithmetic must reproduce from its own inputs."""
    s = m.get("surviving")
    if not s:
        r.note("no surviving-TAM block — the addressability screen has not been run")
        return
    rows = s.get("segment_survival", [])
    if not rows:
        r.fail("L9", "surviving block present with no segment_survival rows")
        return
    wsum = sum(row["weight_pct"] for row in rows)
    if abs(wsum - 100) > 0.5:
        r.fail("L9", f"segment weights sum to {wsum}%, not 100%")
    stated = s.get("weighted_survival_pct", {})
    for key in ("low", "central", "high"):
        calc = sum(row["weight_pct"] * row[f"{key}_pct"] for row in rows) / 100.0
        claim = stated.get(key)
        if claim is None:
            r.fail("L9", f"weighted_survival_pct.{key} missing")
        elif abs(calc - claim) > 1.0:
            r.fail("L9", f"weighted_survival_pct.{key} states {claim}% but the rows compute {calc:.1f}%")
    # cross-check the volume figures
    vol = m.get("volume", {})
    sv = s.get("surviving_volume", {})
    for key in ("low", "central", "high"):
        pct = stated.get(key)
        band = sv.get(key)
        if pct is None or not band:
            continue
        for edge in ("low", "high"):
            expected = vol.get(edge, 0) * pct / 100.0
            got = band.get(edge)
            if got and abs(expected - got) > max(20000, expected * 0.05):
                r.fail("L9", f"surviving_volume.{key}.{edge} states {got:,} "
                             f"but {pct}% of {vol.get(edge):,} is {expected:,.0f}")


def check_L10_consumers_tracked(m, r):
    """L10 — downstream documents that quote a TAM figure must be listed."""
    cons = m.get("consumers")
    if not cons:
        r.warn("L10", "no consumers listed. Every document quoting a TAM figure should appear here, "
                      "or a change to this model cannot be traced downstream.")
        return
    for c in cons:
        if c.get("status") not in ("CURRENT", "STALE", "CHECK"):
            r.fail("L10", f"consumer '{c.get('doc')}' has status '{c.get('status')}' — "
                          f"expected CURRENT, STALE or CHECK")


# Pool at risk per incumbent (VA-147, RD-032, 17 Sep 2026). R2 names the
# incumbents whose pool the architecture takes; a loss-side partner at R7 is
# priced against that pool, so the block must exist here before R7 can read it.
# Models dated on or after the rule date are refused without it; earlier models
# are warned. A pool is stated per incumbent, never only in aggregate.
POOL_RULE_FROM = "2026-09-23"
POOL_STATUSES = {"sized", "none"}
POOL_QUANTITIES = ["revenue_a_year", "reading_s", "reading_d", "pool_a_year"]
POOL_CHANNELLING = {"yes", "partly", "no"}
POOL_AGGREGATE_KEYS = {"total", "aggregate", "pool_total"}


def _pool_band(r, ctx, q):
    """One quantity in the block: {low, high, source, tier}; low <= high; a tier
    of 'unmeasured' carries no numbers (the L6 rule, applied here)."""
    if not isinstance(q, dict):
        r.fail("L11", f"{ctx} must be a mapping {{low, high, source, tier}}, got {type(q).__name__}")
        return
    tier = q.get("tier")
    if tier not in VALID_TIERS:
        r.fail("L11", f"{ctx}.tier '{tier}' invalid — expected one of {sorted(VALID_TIERS)}")
    if not str(q.get("source", "")).strip():
        r.fail("L11", f"{ctx} has no source — every reading carries where it came from")
    lo, hi = q.get("low"), q.get("high")
    if tier == "unmeasured":
        if lo is not None or hi is not None:
            r.fail("L11", f"{ctx} carries numbers with tier 'unmeasured' — remove them or tier them")
        return
    for k, v in (("low", lo), ("high", hi)):
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            r.fail("L11", f"{ctx}.{k} must be a number, got {v!r}")
            return
    if lo > hi:
        r.fail("L11", f"{ctx}: low {lo} exceeds high {hi}")


def check_L11_pool_at_risk(m, r):
    """L11 — the pool at risk is stated per incumbent named in R2, with a source
    tier on every reading, or its absence is declared with a reason."""
    hard = str(m.get("date", "")) >= POOL_RULE_FROM
    sink = r.fail if hard else r.warn
    block = m.get("pool_at_risk")
    if block is None:
        sink("L11", "no pool_at_risk block — state the pool per incumbent R2 names "
                    "(status: sized, incumbents: [...]) or declare status: none with a reason"
                    + ("" if hard else " (warning — model dated before the rule)"))
        return
    if not isinstance(block, dict):
        r.fail("L11", f"pool_at_risk must be a mapping, got {type(block).__name__}")
        return
    status = block.get("status")
    if status not in POOL_STATUSES:
        r.fail("L11", f"pool_at_risk.status '{status}' invalid — expected one of {sorted(POOL_STATUSES)}")
        return
    rows = block.get("incumbents") or []
    if status == "none":
        if not str(block.get("reason", "")).strip():
            r.fail("L11", "pool_at_risk.status none needs a reason — why no incumbent pool is taken")
        if rows:
            r.fail("L11", f"pool_at_risk.status none with {len(rows)} incumbent row(s) — one or the other")
        r.note("L11: pool at risk declared none — " + str(block.get("reason", ""))[:90])
        return
    if POOL_AGGREGATE_KEYS & set(block) and not rows:
        r.fail("L11", "pool_at_risk states an aggregate and no incumbent rows — "
                      "a pool is stated per incumbent, never only in aggregate")
        return
    if not isinstance(rows, list) or not rows:
        r.fail("L11", "pool_at_risk.status sized needs at least one row in incumbents")
        return
    seen = set()
    for i, row in enumerate(rows):
        ctx = f"pool_at_risk.incumbents[{i}]"
        if not isinstance(row, dict):
            r.fail("L11", f"{ctx} must be a mapping")
            continue
        rid = row.get("id")
        if not rid:
            r.fail("L11", f"{ctx} has no id — the AOM's loss-side partner refers to it by id")
        elif rid in seen:
            r.fail("L11", f"{ctx} id '{rid}' repeats — one row per incumbent")
        seen.add(rid)
        if not str(row.get("class", "")).strip() and not str(row.get("name", "")).strip():
            r.fail("L11", f"{ctx} ({rid}) names no incumbent — give class (the typical incumbent) or name")
        for q in POOL_QUANTITIES:
            if q not in row:
                r.fail("L11", f"{ctx} ({rid}) missing {q} — the four readings are "
                              f"{', '.join(POOL_QUANTITIES)}")
            else:
                _pool_band(r, f"{ctx}.{q}", row[q])
        ch = row.get("channelling")
        if not isinstance(ch, dict):
            r.fail("L11", f"{ctx} ({rid}) missing channelling {{condition: yes|partly|no, evidence}}")
        else:
            if ch.get("condition") not in POOL_CHANNELLING:
                r.fail("L11", f"{ctx}.channelling.condition '{ch.get('condition')}' — "
                              f"one of {sorted(POOL_CHANNELLING)}")
            if not str(ch.get("evidence", "")).strip():
                r.fail("L11", f"{ctx}.channelling has no evidence")
    r.note(f"L11: pool at risk stated for {len(rows)} incumbent(s): "
           f"{', '.join(str(x) for x in seen if x)}")


CHECKS = [
    check_L1_every_subclass_has_one_known_kmc,
    check_L2_segment_kmc_purity,
    check_L3_shares_sum,
    check_L4_addressability_verdicts,
    check_L5_supplied_alternative_evidence,
    check_L6_no_invented_shares,
    check_L7_volume_basis_declared,
    check_L8_gates_and_screens,
    check_L9_surviving_arithmetic,
    check_L10_consumers_tracked,
    check_L11_pool_at_risk,
]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)

    # Verify this script and its siblings against the integrity manifest before
    # producing any verdict. Added 11 September 2026: this is a checker, and it
    # was the one checker in the set that did not check itself.
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

    model = yaml.safe_load(path.read_text(encoding="utf-8"))
    r = Report()
    for check in CHECKS:
        check(model, r)

    print(f"\n─── {path.name} ───")
    print(f"{model.get('venture')} · TAM model v{model.get('version')} · {model.get('date')}")
    n_sc = len(model.get("sub_classes", []))
    n_kmc = len(model.get("kmc_classes", []))
    print(f"{n_sc} sub-classes · {n_kmc} KMC classes\n")

    if r.failures:
        print(f"FAILURES ({len(r.failures)}) — the model is incoherent, fix before use")
        for code, msg in r.failures:
            print(f"  [{code}] {msg}")
        print()
    if r.warnings:
        print(f"WARNINGS ({len(r.warnings)}) — declared defects and known gaps")
        for code, msg in r.warnings:
            print(f"  [{code}] {msg}")
        print()
    for n in r.notes:
        print(f"  note: {n}")

    if r.failures:
        print("✗ INVALID")
        sys.exit(1)
    print("✅ valid" + (" (with declared warnings)" if r.warnings else ""))
    sys.exit(0)


if __name__ == "__main__":
    main()
