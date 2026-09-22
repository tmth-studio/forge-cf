#!/usr/bin/env python3
"""Forge run records — list, show, diff.

One directory per run under this folder, five files each, to the standard in
../run-record-standard.md. This tool reads them; it never writes.

  python3 runs.py list [--sort score|date|cost] [--graded]
  python3 runs.py show <run-id>
  python3 runs.py diff <run-id-a> <run-id-b>
  python3 runs.py best [n]           the n highest-scoring graded runs (default 5)
  python3 runs.py qualify            the objective's counter: which records count, and why not

Standard library only. A field a record marks absent is printed as "absent".
A score is diagnostic. Only a record that is held_out_autonomous and
COMPLETE_VERIFIED, with its three supporting facts present, counts toward the
WS1 objective (run-record-standard.md, version 2, 21 September 2026).
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("FORGE_RUN_RECORDS", HERE)
FILES = ["meta.json", "harness.json", "inputs.json", "trace.jsonl", "score.json"]


# ------------------------------------------------------------------ reading

def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return {"_error": f"{os.path.basename(path)}: {e}"}


def load_trace(path):
    events = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    events.append(json.loads(line))
    except FileNotFoundError:
        return None
    return events


def load_run(run_id):
    d = os.path.join(ROOT, run_id)
    if not os.path.isdir(d):
        return None
    return {
        "run_id": run_id,
        "dir": d,
        "meta": load_json(os.path.join(d, "meta.json")),
        "harness": load_json(os.path.join(d, "harness.json")),
        "inputs": load_json(os.path.join(d, "inputs.json")),
        "score": load_json(os.path.join(d, "score.json")),
        "trace": load_trace(os.path.join(d, "trace.jsonl")),
        "missing": [f for f in FILES if not os.path.exists(os.path.join(d, f))],
    }


def all_runs():
    if not os.path.isdir(ROOT):
        return []
    ids = sorted(
        n for n in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, n)) and os.path.exists(os.path.join(ROOT, n, "meta.json"))
    )
    return [load_run(i) for i in ids]


# ------------------------------------------------------------------ fields

def is_absent(v):
    return v is None or (isinstance(v, str) and v.lower().startswith("absent"))


def fmt(v, width=None):
    if is_absent(v):
        s = "absent"
    elif isinstance(v, float):
        s = f"{v:.2f}"
    elif isinstance(v, list):
        s = ",".join(str(x) for x in v)
    elif isinstance(v, dict):
        s = json.dumps(v, ensure_ascii=False)
    else:
        s = str(v)
    if width:
        s = s[:width].ljust(width)
    return s


def get(d, *keys, default=None):
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def norm_score(s):
    """Return the score file in the version-1 shape. One 16 Sep record wrote
    integrity_score / sub_scores / verdict; read it, do not copy it."""
    if not isinstance(s, dict):
        return {}
    if "overall" in s or "integrity_score" not in s:
        return s
    out = dict(s)
    out["overall"] = s.get("integrity_score")
    for k in ["completeness", "consistency", "discipline", "synthesis"]:
        out.setdefault(k, get(s, "sub_scores", k))
    out.setdefault("verdict_band", s.get("verdict"))
    out.setdefault("report_path", s.get("report"))
    out["_shape_deviation"] = "integrity_score/sub_scores — not the standard's field names"
    return out


def score_of(run):
    s = norm_score(run.get("score") or {})
    if not s.get("graded"):
        return None
    return s.get("overall")


# ------------------------------------------------------------------ qualification (standard v2)

THRESHOLD = 85
CLASSES = ("held_out_autonomous", "iterative_design_case")
STATES = ("COMPLETE_VERIFIED", "INCOMPLETE")
INCOMPLETE_WORDS = ("open", "partial", "provisional", "not reached", "blocked", "fail", "borderline")


def labelled_class(run):
    return get(run.get("meta") or {}, "qualification_class")


def labelled_state(run):
    return get(run.get("meta") or {}, "completion_state")


def read_class(run):
    """The class the tool reads the record as, and the reasons where that is
    not the class it was labelled with."""
    m = run.get("meta") or {}
    reasons = []
    lab = labelled_class(run)
    if lab not in CLASSES:
        reasons.append("qualification_class absent or not one of the two values")
    if lab != "held_out_autonomous":
        return "iterative_design_case", reasons
    q = m.get("qualification") or {}
    if not q.get("source_input_fingerprint"):
        reasons.append("no source_input_fingerprint")
    att = q.get("no_edit_attestation") or {}
    if att.get("attested") is not True:
        reasons.append("no_edit_attestation not attested")
    ver = q.get("verifier_identity") or {}
    if ver.get("independent_of_runner") is not True:
        reasons.append("verifier not independent of the runner, or not stated")
    if reasons:
        return "iterative_design_case", reasons
    return "held_out_autonomous", reasons


def read_state(run):
    """The completion state the tool reads, with the reasons INCOMPLETE is forced."""
    m = run.get("meta") or {}
    s = norm_score(run.get("score") or {})
    reasons = []
    lab = labelled_state(run)
    if lab not in STATES:
        reasons.append("completion_state absent or not one of the two values")
    st = m.get("stage_status") or {}
    for stage, status in st.items():
        text = str(status).lower()
        if any(w in text for w in INCOMPLETE_WORDS):
            reasons.append(f"stage {stage}: {status}")
            break
    ev = m.get("evidence") or {}
    fitr = ev.get("fit_record")
    if not isinstance(fitr, dict):
        reasons.append("evidence.fit_record not stated")
    elif not (fitr.get("present") is True and fitr.get("current") is True):
        reasons.append("FIT record absent or stale against the current component set")
    for item in ev.get("required_external") or []:
        if isinstance(item, dict) and item.get("present") is not True:
            reasons.append(f"required evidence absent: {item.get('name')}")
    if not s.get("graded"):
        reasons.append("not graded")
    else:
        band = str(s.get("verdict_band") or "").lower()
        if "gap" in band or "sound" not in band:
            reasons.append(f"verdict band: {s.get('verdict_band')}")
        gates = s.get("gates") or {}
        for g in ("justification_mode", "parts_bin"):
            if gates.get(g) is True:
                reasons.append(f"structural gate active: {g}")
    if reasons:
        return "INCOMPLETE", reasons
    return "COMPLETE_VERIFIED", reasons


def qualifies(run):
    """True only when every clause of the objective holds on this record."""
    c, _ = read_class(run)
    st, _ = read_state(run)
    sc = score_of(run)
    s = norm_score(run.get("score") or {})
    gates = s.get("gates") or {}
    return (
        c == "held_out_autonomous"
        and st == "COMPLETE_VERIFIED"
        and sc is not None and sc >= THRESHOLD
        and gates.get("justification_mode") is False
        and gates.get("parts_bin") is False
    )


def cmd_qualify(args):
    runs = all_runs()
    if not runs:
        print(f"No runs under {ROOT}")
        return 0
    mismatches = 0
    counted = []
    for r in runs:
        lc, creasons = read_class(r)
        ls_, sreasons = read_state(r)
        sc = score_of(r)
        print(f"# {r['run_id']}")
        print(f"  labelled   class {fmt(labelled_class(r))}  state {fmt(labelled_state(r))}")
        print(f"  read as    class {lc}  state {ls_}  score {'—' if sc is None else sc}")
        if labelled_class(r) != lc:
            mismatches += 1
            for x in creasons:
                print(f"    class differs: {x}")
        if labelled_state(r) != ls_:
            mismatches += 1
            for x in sreasons:
                print(f"    state differs: {x}")
        elif ls_ == "INCOMPLETE" and sreasons:
            print(f"    incomplete because: {sreasons[0]}" + (f" (+{len(sreasons)-1} more)" if len(sreasons) > 1 else ""))
        if qualifies(r):
            counted.append(r)
            print("  COUNTS toward the WS1 objective")
        else:
            print("  does not count toward the WS1 objective")
        print()
    print(f"Objective: {len(counted)} of 3 consecutive held-out runs at ≥ {THRESHOLD} with both gates clear, complete and verified.")
    if mismatches:
        print(f"{mismatches} label(s) differ from the tool's reading — a mislabelled record is a failure, not a footnote.")
        return 1
    return 0


def harness_id(run):
    h = run.get("harness") or {}
    c = h.get("commit") or h.get("vault_commit")
    if c:
        tag = str(c)[:8]
        if h.get("vault_commit_inferred"):
            tag += "?"
        return tag
    code = h.get("code_sha256")
    return ("code:" + code[:8]) if code else "absent"


def cost_gbp(run):
    return get(run.get("meta") or {}, "cost", "gbp")


def date_of(run):
    return get(run.get("meta") or {}, "date") or run["run_id"][:10]


def gate_verdicts(run):
    out = []
    for e in run.get("trace") or []:
        if e.get("kind") == "gate":
            v = e.get("verdict")
            if e.get("held"):
                v = "held"
            out.append(f"{e.get('stage')}:{v}")
    return out


# ------------------------------------------------------------------ list

def cmd_list(args):
    sort = "date"
    graded_only = False
    for i, a in enumerate(args):
        if a == "--sort" and i + 1 < len(args):
            sort = args[i + 1]
        if a == "--graded":
            graded_only = True
    runs = all_runs()
    if graded_only:
        runs = [r for r in runs if score_of(r) is not None]
    if sort == "score":
        runs.sort(key=lambda r: (score_of(r) is None, -(score_of(r) or 0)))
    elif sort == "cost":
        runs.sort(key=lambda r: (is_absent(cost_gbp(r)), -(cost_gbp(r) or 0) if not is_absent(cost_gbp(r)) else 0))
    else:
        runs.sort(key=lambda r: date_of(r))
    if not runs:
        print(f"No runs under {ROOT}")
        return 0
    head = f"{'run':44} {'date':10} {'source':7} {'harness':11} {'stages':12} {'class':10} {'state':10} {'score':6} {'£':>7}"
    print(head)
    print("-" * len(head))
    for r in runs:
        m = r["meta"] or {}
        sc = score_of(r)
        print(
            f"{r['run_id'][:44]:44} "
            f"{fmt(date_of(r))[:10]:10} "
            f"{fmt(m.get('source'), 7)} "
            f"{harness_id(r)[:11]:11} "
            f"{fmt(m.get('stages_reached'), 12)} "
            f"{('held-out' if read_class(r)[0] == 'held_out_autonomous' else 'iterative'):10} "
            f"{('complete' if read_state(r)[0] == 'COMPLETE_VERIFIED' else 'INCOMPLETE'):10} "
            f"{('—' if sc is None else str(sc)):6} "
            f"{fmt(cost_gbp(r)):>7}"
        )
        if r["missing"]:
            print(f"{'':44} missing: {', '.join(r['missing'])}")
    print(f"\n{len(runs)} run{'s' if len(runs) != 1 else ''} · a ? after a harness id means the version was inferred, not recorded · score is diagnostic; see `qualify` for what counts")
    return 0


def cmd_best(args):
    n = int(args[0]) if args and args[0].isdigit() else 5
    runs = [r for r in all_runs() if score_of(r) is not None]
    runs.sort(key=lambda r: -score_of(r))
    if not runs:
        print("No graded runs yet. A run is graded when its score.json has graded: true.")
        return 0
    for r in runs[:n]:
        s = norm_score(r["score"])
        tag = "counts" if qualifies(r) else "diagnostic only"
        print(f"{score_of(r):>4}  {r['run_id']}  {fmt(s.get('verdict_band'))}  harness {harness_id(r)}  [{tag}]")
    return 0


# ------------------------------------------------------------------ show

def cmd_show(args):
    if not args:
        print("show needs a run id")
        return 2
    r = load_run(args[0])
    if r is None:
        print(f"No run {args[0]} under {ROOT}")
        return 1
    m, h, s, i = r["meta"] or {}, r["harness"] or {}, norm_score(r["score"] or {}), r["inputs"] or {}
    print(f"# {r['run_id']}")
    if r["missing"]:
        print(f"missing files: {', '.join(r['missing'])}")
    print()
    print("## meta")
    for k in ["source", "venture", "date", "status", "model", "effort", "entry_path", "stages_reached", "stage_status", "turns"]:
        if k in m:
            print(f"  {k:16} {fmt(m[k])}")
    c = m.get("cost") or {}
    if isinstance(c, dict):
        print(f"  {'cost':16} £{fmt(c.get('gbp'))}  (${fmt(c.get('usd'))}, rate {fmt(c.get('gbp_rate'))}{' assumed' if c.get('gbp_rate_assumed') else ''})")
        t = c.get("tokens")
        if isinstance(t, dict):
            print(f"  {'tokens':16} in {t.get('input')} · cache read {t.get('cache_read')} · cache write {t.get('cache_write')} · out {t.get('output')}")
        elif t is not None:
            print(f"  {'tokens':16} {fmt(t)}")
    tr = m.get("trace") or {}
    if isinstance(tr, dict):
        print(f"  {'trace':16} {tr.get('events')} events · complete: {tr.get('complete')}")
        for a in tr.get("absent") or []:
            print(f"  {'':16} absent: {a}")
    print()
    print("## harness")
    print(f"  {'id':16} {harness_id(r)}")
    for k in ["app", "commit", "vault_commit", "code_sha256"]:
        if k in h:
            print(f"  {k:16} {fmt(h[k])}")
    if h.get("vault_commit_inferred"):
        print(f"  {'inferred':16} yes — {fmt(h.get('vault_commit_reasoning'))[:160]}")
    mf = h.get("method_files") or {}
    for name, info in mf.items():
        sha = info.get("sha256") if isinstance(info, dict) else None
        lines = info.get("lines") if isinstance(info, dict) else None
        print(f"  {'method':16} {name}  {fmt(sha)[:12]}  {('%s lines' % lines) if lines else ''}")
    st = h.get("settings") or {}
    if st:
        print(f"  {'settings':16} {fmt(st)}")
    ref = h.get("reference") or {}
    if ref:
        print(f"  {'reference':16} present: {ref.get('present')} · files: {len(ref.get('files') or [])}")
    print()
    print("## inputs")
    if "website" in i:
        print(f"  {'website':16} {fmt(i.get('website'))}")
    if "entries" in i:
        print(f"  {'entries':16} {len(i.get('entries') or [])} written by the person")
    if "files_read" in i:
        for f in i["files_read"]:
            tag = fmt(f.get('sha256'))[:12] if 'sha256' in f else f"({f.get('role')}, see harness)"
            print(f"  {'file':16} {f.get('path')}  {tag}")
    print()
    print("## trace")
    kinds = {}
    for e in r["trace"] or []:
        kinds[e.get("kind")] = kinds.get(e.get("kind"), 0) + 1
    print("  " + " · ".join(f"{k} {v}" for k, v in sorted(kinds.items())) if kinds else "  none")
    gv = gate_verdicts(r)
    if gv:
        print(f"  {'gates':16} {' → '.join(gv)}")
    print()
    print("## score")
    if not s.get("graded"):
        print(f"  not graded — {fmt(s.get('note'))}")
    else:
        for k in ["overall", "completeness", "consistency", "discipline", "synthesis", "verdict_band", "validation_maturity", "graded_at", "report_path"]:
            print(f"  {k:20} {fmt(s.get(k))}")
        print(f"  {'gates':20} {fmt(s.get('gates'))}")
    if s.get("_shape_deviation"):
        print(f"  shape: {s['_shape_deviation']}")
    print()
    print("## qualification")
    lc, cr = read_class(r)
    ls_, sr = read_state(r)
    print(f"  {'class':20} labelled {fmt(labelled_class(r))} · read as {lc}")
    for x in cr:
        print(f"  {'':20} {x}")
    print(f"  {'state':20} labelled {fmt(labelled_state(r))} · read as {ls_}")
    for x in sr[:3]:
        print(f"  {'':20} {x}")
    st_all_closed = all(not any(w in str(v).lower() for w in INCOMPLETE_WORDS) for v in (m.get("stage_status") or {}).values())
    print(f"  {'architecture':20} {'every stage closed' if st_all_closed else 'stages open'} — reported separately from the WS1 state above")
    print(f"  {'counts':20} {'yes' if qualifies(r) else 'no — score is diagnostic only'}")
    extra = os.path.join(r["dir"], "grading", "marking.json")
    if os.path.exists(extra):
        mk = load_json(extra) or {}
        marks = mk.get("marks") or {}
        print(f"  sealed-key marking: " + ", ".join(f"{k} {v.get('result')}" for k, v in marks.items()))
    return 0


# ------------------------------------------------------------------ diff

def cmd_diff(args):
    if len(args) < 2:
        print("diff needs two run ids")
        return 2
    a, b = load_run(args[0]), load_run(args[1])
    for x, name in ((a, args[0]), (b, args[1])):
        if x is None:
            print(f"No run {name} under {ROOT}")
            return 1
    print(f"{'':22} {args[0][:34]:34} {args[1][:34]:34} {'change'}")
    print("-" * 110)

    def row(label, va, vb, numeric=False):
        change = ""
        if is_absent(va) and is_absent(vb):
            change = ""
        elif numeric and isinstance(va, (int, float)) and isinstance(vb, (int, float)):
            d = vb - va
            change = f"{d:+.2f}" if isinstance(d, float) else f"{d:+d}"
        elif va != vb:
            change = "differs"
        print(f"{label:22} {fmt(va, 34)} {fmt(vb, 34)} {change}")

    print("score")
    sa, sb = norm_score(a["score"] or {}), norm_score(b["score"] or {})
    row("  graded", sa.get("graded"), sb.get("graded"))
    for k in ["overall", "completeness", "consistency", "discipline", "synthesis"]:
        row("  " + k, sa.get(k), sb.get(k), numeric=True)
    row("  verdict band", sa.get("verdict_band"), sb.get("verdict_band"))
    row("  justification gate", get(sa, "gates", "justification_mode"), get(sb, "gates", "justification_mode"))
    row("  parts-bin gate", get(sa, "gates", "parts_bin"), get(sb, "gates", "parts_bin"))
    row("  class (read)", read_class(a)[0], read_class(b)[0])
    row("  state (read)", read_state(a)[0], read_state(b)[0])

    print("harness")
    ha, hb = a["harness"] or {}, b["harness"] or {}
    row("  id", harness_id(a), harness_id(b))
    row("  code hash", (ha.get("code_sha256") or "absent")[:12], (hb.get("code_sha256") or "absent")[:12])
    # Method files are keyed by their canonical vault path where the record
    # names one, so a copy in the app lines up with the vault file it copies.
    def by_canonical(files):
        out = {}
        for name, info in (files or {}).items():
            key = (info.get("canonical_path") if isinstance(info, dict) else None) or name
            out[key] = (info or {}).get("sha256") if isinstance(info, dict) else None
        return out
    ma, mb = by_canonical(ha.get("method_files")), by_canonical(hb.get("method_files"))
    for name in sorted(set(ma) | set(mb)):
        short = name.split("/")[-2] + "/" + name.split("/")[-1] if "/" in name else name
        row("  " + short[:20], (ma.get(name) or "absent")[:12], (mb.get(name) or "absent")[:12])
    sta, stb = ha.get("settings") or {}, hb.get("settings") or {}
    for k in sorted(set(sta) | set(stb)):
        if sta.get(k) != stb.get(k):
            row("  setting " + k, sta.get(k), stb.get(k))

    print("run")
    xa, xb = a["meta"] or {}, b["meta"] or {}
    row("  date", xa.get("date"), xb.get("date"))
    row("  model", xa.get("model"), xb.get("model"))
    row("  entry path", xa.get("entry_path"), xb.get("entry_path"))
    row("  stages reached", xa.get("stages_reached"), xb.get("stages_reached"))
    row("  turns", xa.get("turns"), xb.get("turns"), numeric=True)
    row("  cost £", cost_gbp(a), cost_gbp(b), numeric=True)
    row("  gates", gate_verdicts(a), gate_verdicts(b))
    return 0


# ------------------------------------------------------------------ main

def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__.strip())
        return 0
    cmd, args = argv[0], argv[1:]
    if cmd == "list":
        return cmd_list(args)
    if cmd == "show":
        return cmd_show(args)
    if cmd == "diff":
        return cmd_diff(args)
    if cmd == "best":
        return cmd_best(args)
    if cmd == "qualify":
        return cmd_qualify(args)
    print(f"Unknown command {cmd}. Try: list, show, diff, best, qualify.")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
