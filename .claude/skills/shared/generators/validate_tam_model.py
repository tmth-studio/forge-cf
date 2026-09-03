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
]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)

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
