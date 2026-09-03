"""CTM — swimlane HTML view generator (venture-generic) (the model of record).

Reads <venture>-ctm-model-at-C<N>.yaml (the model — single source of truth) and
emits <venture>-ctm-at-C<N>.html in the canonical spec format
(.claude/skills/shared/ctm-diagram-spec.md): swimlanes per phase, sparse
state rectangles, coloured hexagon component nodes between states, decision
diamond with A/B branches, escalation box, BALM table, review findings,
routing panel.

The YAML is the model; this file is a generated view. Self-checks run
before writing; the file is NOT written on any failure.
"""
import sys, pathlib, html as H, yaml

import sys, pathlib
if len(sys.argv) != 2:
    print(f"usage: python3 {pathlib.Path(__file__).name} <venture>-MODEL-model-at-C<N>.yaml"); sys.exit(1)
SRC = pathlib.Path(sys.argv[1]).resolve()
assert "-model-" in SRC.name, "model file must be named [venture]-[model]-model-at-C[N].yaml"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate_model import check_or_die, provenance, jurisdiction_line
check_or_die(SRC)
PROV = provenance(__file__, SRC)  # schema gate — a malformed model fails before any rendering

OUT = SRC.parent / (SRC.name.replace("-model-", "-").rsplit(".", 1)[0] + ".html")

m = yaml.safe_load(SRC.read_text())
import re as _re
def _valid_id(c): return bool(_re.match(r"^(WP|CP|PP|PartP)-\d+$", c))

# ------------------------------------------------------------ self-checks
errs = []
for pid, ph in m["phases"].items():
    if ph.get("undesigned"):
        continue
    sids = {s["id"] for s in ph["states"]}
    dec = ph.get("decision")
    valid = sids | ({"decision"} if dec else set())
    if not ph["states"]:
        errs.append(f"{pid}: no states")
    for t in ph["transitions"]:
        for end in (t["from"], t["to"]):
            if end not in valid:
                errs.append(f"{pid}: transition endpoint '{end}' unknown")
        if t.get("branch"):
            continue
        comps = t.get("components", [])
        if not comps and not t.get("flag"):
            errs.append(f"{pid}: transition {t['from']}→{t['to']} has no components and no flag")
        for c in comps:
            if not _valid_id(c):
                errs.append(f"{pid}: component '{c}' is not a Flow-Register-format ID")
    if dec:
        if dec["branch_a"] not in sids:
            errs.append(f"{pid}: decision branch_a '{dec['branch_a']}' unknown")
        if dec["branch_b"] != "escalation":
            errs.append(f"{pid}: decision branch_b must be 'escalation'")
for _tkey in ("user_tracks", "partner_tracks"):
  for uid, tr in (m.get(_tkey) or {}).items():
    sids = {s["id"] for s in tr.get("states", [])}
    if not tr.get("states"):
        errs.append(f"{_tkey}.{uid}: no states")
    for t in tr.get("transitions", []):
        for end in (t["from"], t["to"]):
            if end not in sids:
                errs.append(f"{_tkey}.{uid}: transition endpoint '{end}' unknown")
        comps = t.get("components", [])
        if not comps and not t.get("flag"):
            errs.append(f"{_tkey}.{uid}: transition {t['from']}→{t['to']} has no components and no flag")
        for c in comps:
            if not _valid_id(c):
                errs.append(f"{_tkey}.{uid}: component '{c}' is not a Flow-Register-format ID")
# BALM row count is governed by validate_model.py (warns below 4 rows)
if errs:
    print("SELF-CHECK FAILURES — file not written:")
    [print("  ✗", e) for e in errs]
    sys.exit(1)

def esc(s): return H.escape(str(s))

def hexnode(comps, label, flag=None):
    if not comps:
        cls = "hex-part"
        head = "⚑ no flow ID"
    else:
        cls = {"W": "hex-wp", "C": "hex-cp", "P": "hex-pp" if comps[0].startswith("PP") else "hex-part"}[comps[0][0]]
        head = " / ".join(comps) if len(comps) <= 2 else f"{comps[0].split('-')[0]}-{'/'.join(c.split('-')[1] for c in comps)}"
    return f'<div class="hex-node {cls}">{esc(head)}<br>{esc(label)}</div>'

def statenode(s):
    final = " final" if s.get("final") else ""
    return (f'<div class="state-node"><div class="state-icon">{s["icon"]}</div>'
            f'<div class="state-label{final}">{esc(s["label"])}</div></div>')

CONN = '<div class="connector"><div class="connector-line"></div></div>'

lanes = []
for pid, ph in m["phases"].items():
    if ph.get("undesigned"):
        lanes.append(f'<div class="swimlane" style="opacity:.55"><div class="swimlane-label">{esc(ph["name"])}</div>'
                     f'<div style="border:1px dashed var(--border);border-radius:6px;padding:18px 24px;font-size:12px;color:var(--text-muted);flex:1;text-align:center">{esc(ph["undesigned"])}</div></div>')
        continue
    states = {s["id"]: s for s in ph["states"]}
    order = [s["id"] for s in ph["states"]]
    dec = ph.get("decision")
    trans = {(t["from"], t["to"]): t for t in ph["transitions"]}
    parts = [f'<div class="swimlane"><div class="swimlane-label">{esc(ph["name"])}</div>']
    seq = []  # walk states in order, inserting decision before its branch_a target
    for i, sid in enumerate(order):
        if dec and dec["branch_a"] == sid:
            seq.append(("decision", dec))
        seq.append(("state", states[sid]))
    prev_sid = None
    for kind, obj in seq:
        if kind == "state":
            if prev_sid is not None:
                t = trans.get((prev_sid, obj["id"])) or trans.get(("decision", obj["id"]))
                if t and not t.get("branch"):
                    parts.append(CONN + hexnode(t.get("components", []), t.get("label", "")) + CONN)
                elif t and t.get("branch") == "A":
                    parts.append('<span class="branch-marker">A</span>' + CONN)
            parts.append(statenode(obj))
            prev_sid = obj["id"]
        else:
            t = trans.get((prev_sid, "decision"))
            if t:
                parts.append(CONN + hexnode(t.get("components", []), t.get("label", "")) + CONN)
            parts.append(f'<div class="diamond"><div class="diamond-label">{esc(obj["label"])}</div></div>')
            prev_sid = "decision"
    if dec:
        e = m["escalation"]
        outcomes = "".join(f'<div class="outcome-{o["kind"]}">{"✓" if o["kind"]=="win" else "✗"} {esc(o["label"])}</div>'
                           for o in e["outcomes"])
        parts.append(
            f'<span class="branch-marker">B</span><div class="connector"><div class="connector-line dashed"></div></div>'
            f'<div class="escalation-box"><h5>{esc(e["title"])}</h5>'
            f'<div class="escalation-timeline">{esc(e["timeline"])}<br>{esc(e["note"])}</div>{outcomes}</div>')
    parts.append('</div>')
    # flagged transitions render a rowflag under the lane
    for t in ph["transitions"]:
        if t.get("flag"):
            parts.append(f'<div class="rowflag">⚑ {esc(t.get("label", t["from"] + "→" + t["to"]))}: {esc(t["flag"])}</div>')
    lanes.append("".join(parts))

# --- Actor tracks (1 Sep 2026, Tom's rulings): user_tracks — actors who use the
# product without being the payer; partner_tracks — enabler actors the Partner
# Product transforms (R7's journey, restoring the historic CTM "Track B").
def build_track_lane(tr):
    states = {s["id"]: s for s in tr["states"]}
    order = [s["id"] for s in tr["states"]]
    trans = {(t["from"], t["to"]): t for t in tr["transitions"]}
    parts = [f'<div class="swimlane"><div class="swimlane-label">{esc(tr["actor"])}</div>']
    prev_sid = None
    for sid in order:
        if prev_sid is not None:
            t = trans.get((prev_sid, sid))
            if t:
                parts.append(CONN + hexnode(t.get("components", []), t.get("label", "")) + CONN)
        parts.append(statenode(states[sid]))
        prev_sid = sid
    parts.append('</div>')
    parts.append(f'<div class="track-note">{esc(tr["role_note"])}</div>')
    for t in tr["transitions"]:
        if t.get("flag"):
            parts.append(f'<div class="rowflag">⚑ {esc(t.get("label", t["from"] + "→" + t["to"]))}: {esc(t["flag"])}</div>')
    return "".join(parts)

user_lanes = [build_track_lane(tr) for tr in (m.get("user_tracks") or {}).values()]
user_section = ""
if user_lanes:
    user_section = ('<div class="section-divider">User journeys — actors transformed by the product '
                    'who are not the payer</div>' + "".join(user_lanes))
partner_lanes = [build_track_lane(tr) for tr in (m.get("partner_tracks") or {}).values()]
partner_section = ""
if partner_lanes:
    partner_section = ('<div class="section-divider">Partner journeys — partners the Partner Product '
                       'transforms into active participants (R7)</div>' + "".join(partner_lanes))

markers = "".join(f'<div class="timeline-marker" style="left: {40 + i * 370}px;">{esc(t)}</div>'
                  for i, t in enumerate(m["timeline"]))
annos = "".join(f'<div class="annotation"><strong>{esc(a["title"])}.</strong> ' +
                "".join(f'<span style="color:#fca5a5">{esc(r)}</span>; ' if False else "" for r in a.get("red_figures", [])) +
                esc(a["text"]) + "</div>" for a in m["annotations"])
balm = "".join(f'<tr><td>{esc(r["req"])}</td><td>{esc(r["phase"])}</td><td>{esc(r["component"])}</td>'
               f'<td>{esc(r["overrides"])}</td></tr>' for r in m["balm_mapping"])
findings = "".join(f'<li>{esc(f)}</li>' for f in m["review_findings"])

def _state_label(ph, sid):
    for s in ph.get("states", []):
        if s.get("id") == sid:
            return s.get("label", sid)
    return sid

_nar_rows = []
def _nar_row(actor, ph, t):
    n = t.get("narrative") or {}
    return (
        f'<tr><td>{esc(actor)}</td><td><strong>{esc(_state_label(ph, t["from"]))}</strong> → '
        f'<strong>{esc(_state_label(ph, t["to"]))}</strong></td>'
        f'<td>{esc(", ".join(t.get("components", [])))}</td>'
        f'<td>{esc(n.get("change_type", "—"))}</td>'
        f'<td>{esc(n.get("state_change", "— (model predates the 28 Aug 2026 rule)"))}</td>'
        f'<td>{esc(n.get("mechanism", "—"))}</td></tr>')
for _pid, _ph in m["phases"].items():
    for _t in _ph.get("transitions") or []:
        if _t.get("branch") or not _t.get("components"):
            continue
        _nar_rows.append(_nar_row(m["customer"], _ph, _t))
for _tkey in ("user_tracks", "partner_tracks"):
    for _uid, _tr in (m.get(_tkey) or {}).items():
        for _t in _tr.get("transitions") or []:
            if not _t.get("components"):
                continue
            _nar_rows.append(_nar_row(_tr["actor"], _tr, _t))
narratives = "".join(_nar_rows)

# --- 4-D products roster (1 Sep 2026, Tom's ruling): every product component the
# journey requires, across the customer phases AND the user tracks, enriched from
# the sibling AOM register where one exists. Derived — never hand-listed.
_TYPE_NAMES = {"CP": "Communications", "WP": "Working", "PP": "Payment", "PartP": "Partner"}
_roster = {}  # comp_id -> list of "actor: from → to" driver strings
def _roster_add(actor, ph, t):
    for c in t.get("components", []):
        _roster.setdefault(c, []).append(
            f'{actor}: {_state_label(ph, t["from"])} → {_state_label(ph, t["to"])}')
for _pid, _ph in m["phases"].items():
    for _t in _ph.get("transitions") or []:
        if not _t.get("branch"):
            _roster_add(m["customer"], _ph, _t)
for _tkey in ("user_tracks", "partner_tracks"):
    for _uid, _tr in (m.get(_tkey) or {}).items():
        for _t in _tr.get("transitions") or []:
            _roster_add(_tr["actor"], _tr, _t)
_aom_register = {}
_aom_path = SRC.parent / SRC.name.replace("-ctm-model-", "-aom-model-")
if _aom_path.exists():
    try:
        _aom_register = yaml.safe_load(_aom_path.read_text()).get("components") or {}
    except Exception:
        _aom_register = {}
def _comp_sort(c):
    typ, num = c.rsplit("-", 1)
    return (["CP", "WP", "PP", "PartP"].index(typ), int(num))
_roster_rows = []
for _c in sorted(_roster, key=_comp_sort):
    _typ = _c.rsplit("-", 1)[0]
    _reg = _aom_register.get(_c) or {}
    _doc = _reg.get("doc", "— (not in the AOM register)" if _aom_register else "— (no sibling AOM model)")
    _drivers = "<br>".join(esc(d) for d in _roster[_c])
    _roster_rows.append(
        f'<tr><td><strong>{esc(_c)}</strong></td><td>{esc(_TYPE_NAMES[_typ])}</td>'
        f'<td>{esc(_doc)}</td><td>{_drivers}</td></tr>')
products_roster = "".join(_roster_rows)
_types_present = {c.rsplit("-", 1)[0] for c in _roster}
_types_absent = [_TYPE_NAMES[t] for t in ["CP", "WP", "PP", "PartP"] if t not in _types_present]
roster_gap_note = ""
if _types_absent:
    # VA-72: where the model states a disposition, print it; only an undispositioned
    # absence renders as a flag (and on models dated >= 2026-09-01 the validator
    # refuses to load those, so the flag survives only on historical snapshots).
    _disp = m.get("absent_products") or {}
    _lines = []
    _inv_names = {v: k for k, v in _TYPE_NAMES.items()}
    for _tn in _types_absent:
        _tk = _inv_names[_tn]
        _d = _disp.get(_tk) or {}
        if str(_d.get("not_designed_until", "")).strip():
            _lines.append(f'<strong>{esc(_tn)} Product:</strong> not designed until {esc(_d["not_designed_until"])}')
        elif str(_d.get("not_applicable", "")).strip():
            _lines.append(f'<strong>{esc(_tn)} Product:</strong> not applicable — {esc(_d["not_applicable"])}')
        else:
            _lines.append(f'<strong>⚑ {esc(_tn)} Product:</strong> absent with no stated disposition (VA-72)')
    roster_gap_note = (f'<p style="color:#854d0e;background:#fff8e6;border-left:3px solid #d4820a;'
                       f'padding:8px 12px;font-size:13px">' + "<br>".join(_lines) + '</p>')
footnotes = " ".join(f'<span class="fn"><b>{i+1}</b> {esc(f)}</span>' for i, f in enumerate(m.get("footnotes", [])))

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(m["venture"])} — CTM {esc(m["state"])}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #ffffff; --text: #1a1a2e; --text-muted: #6b7280; --border: #d1d5db;
      --node-border: #93c5c4; --node-bg: #f0f9f9;
      --label-cp: #e8f4f4; --label-wp: #e8eef8; --label-pp: #fef9e6; --label-part: #f0ebfb;
      --label-cp-text: #007d7a; --label-wp-text: #1f4fa8; --label-pp-text: #854d0e; --label-part-text: #5b21b6;
      --escalation-bg: #f8f9fa; --escalation-border: #374151;
      --win-bg: #d1fae5; --win-border: #059669; --lose-bg: #fee2e2; --lose-border: #dc2626;
      --note-bg: #1a1a2e; --note-text: #ffffff; --arrow: #9ca3af; --assumed: #dc2626;
      --font: 'DM Sans', system-ui, sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); font-family: var(--font); color: var(--text); }}
    .doc-head {{ padding: 32px 40px 0; }}
    .doc-head .meta {{ font-size: 12px; color: var(--text-muted); letter-spacing: 0.04em; margin-bottom: 4px; }}
    .doc-head h1 {{ font-size: 24px; font-weight: 600; margin-bottom: 6px; }}
    .doc-head .sub {{ font-size: 13px; color: var(--text-muted); max-width: 860px; line-height: 1.5; }}
    .assumed {{ color: var(--assumed); font-weight: 600; }}
    .diagram-wrapper {{ width: 100%; overflow-x: auto; padding: 32px 40px 48px; }}
    .diagram {{ min-width: 1480px; position: relative; }}
    .timeline {{ display: flex; align-items: flex-start; margin-bottom: 40px; padding-bottom: 12px; border-bottom: 1px solid var(--border); position: relative; height: 40px; }}
    .timeline-marker {{ position: absolute; top: 0; display: flex; flex-direction: column; align-items: center; font-size: 12px; font-weight: 500; color: var(--text-muted); }}
    .timeline-marker::after {{ content: ''; width: 1px; height: 20px; background: var(--border); margin-top: 4px; }}
    .swimlane {{ display: flex; align-items: center; gap: 0; margin-bottom: 48px; position: relative; min-height: 120px; }}
    .swimlane-label {{ font-size: 11px; font-weight: 600; color: var(--text-muted); writing-mode: vertical-lr; transform: rotate(180deg); margin-right: 16px; text-transform: uppercase; letter-spacing: 0.08em; flex-shrink: 0; }}
    .state-node {{ position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; width: 110px; flex-shrink: 0; }}
    .state-icon {{ font-size: 32px; margin-bottom: 6px; }}
    .state-label {{ font-size: 11px; line-height: 1.35; color: var(--text); background: var(--node-bg); border: 1px solid var(--node-border); border-radius: 6px; padding: 6px 8px; width: 100%; }}
    .state-label.final {{ background: #d1fae5; border-color: #059669; }}
    .hex-node {{ display: flex; align-items: center; justify-content: center; width: 78px; height: 78px; flex-shrink: 0; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); font-size: 10px; font-weight: 600; text-align: center; line-height: 1.25; padding: 10px; flex-direction: column; }}
    .hex-cp {{ background: var(--label-cp); color: var(--label-cp-text); }}
    .hex-wp {{ background: var(--label-wp); color: var(--label-wp-text); }}
    .hex-pp {{ background: var(--label-pp); color: var(--label-pp-text); }}
    .hex-part {{ background: var(--label-part); color: var(--label-part-text); }}
    .connector {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; min-width: 24px; }}
    .connector-line {{ width: 100%; height: 2px; background: var(--arrow); position: relative; }}
    .connector-line::after {{ content: '▶'; position: absolute; right: -8px; top: -8px; font-size: 10px; color: var(--arrow); }}
    .connector-line.dashed {{ background: repeating-linear-gradient(90deg, var(--arrow) 0px, var(--arrow) 6px, transparent 6px, transparent 12px); }}
    .diamond {{ width: 80px; height: 80px; background: #fff8e6; border: 2px solid #d4820a; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin: 0 14px; }}
    .diamond-label {{ transform: rotate(-45deg); font-size: 10px; font-weight: 600; color: #854d0e; text-align: center; line-height: 1.2; }}
    .branch-marker {{ width: 18px; height: 18px; border-radius: 50%; background: #374151; color: white; font-size: 10px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin: 0 4px; flex-shrink: 0; }}
    .escalation-box {{ border: 2px solid var(--escalation-border); background: var(--escalation-bg); padding: 16px 20px; border-radius: 4px; min-width: 240px; max-width: 280px; flex-shrink: 0; }}
    .escalation-box h5 {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--escalation-border); margin-bottom: 10px; }}
    .escalation-timeline {{ font-size: 11px; color: var(--text-muted); line-height: 1.8; margin-bottom: 16px; }}
    .outcome-win {{ border: 2px solid var(--win-border); background: var(--win-bg); border-radius: 6px; padding: 8px 12px; font-size: 11px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }}
    .outcome-lose {{ border: 2px solid var(--lose-border); background: var(--lose-bg); border-radius: 6px; padding: 8px 12px; font-size: 11px; display: flex; align-items: center; gap: 8px; }}
    .annotation {{ background: var(--note-bg); color: var(--note-text); font-size: 11px; line-height: 1.5; padding: 10px 14px; border-radius: 4px; max-width: 300px; }}
    .annotation strong {{ color: #f0d98a; }}
    .annotation-row {{ display: flex; gap: 16px; padding: 0 0 32px 32px; flex-wrap: wrap; }}
    .rowflag {{ font-size: 11px; color: #854d0e; background: #fff8e6; border-left: 3px solid #d4820a; padding: 4px 8px; margin: -32px auto 40px; max-width: 640px; text-align: center; }}
    .supplementary {{ max-width: 960px; margin: 24px auto; padding: 0 40px 80px; }}
    h2 {{ font-size: 18px; font-weight: 600; color: #007d7a; margin: 32px 0 12px; border-bottom: 2px solid #007d7a; padding-bottom: 6px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; margin: 12px 0 24px; }}
    thead tr {{ background: #007d7a; color: #fff; }}
    thead th {{ padding: 9px 12px; text-align: left; font-weight: 600; }}
    tbody td {{ padding: 8px 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }}
    tbody tr:nth-child(even) {{ background: #f9fafa; }}
    .supplementary ul {{ margin: 8px 0 16px 22px; font-size: 13.5px; }}
    .supplementary li {{ margin-bottom: 7px; line-height: 1.5; }}
    .routing-panel {{ background: var(--note-bg); color: var(--note-text); padding: 22px 26px; border-radius: 4px; font-size: 13px; line-height: 1.65; margin: 24px 0; }}
    .routing-panel h3 {{ color: #f0d98a; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 10px; }}
    .routing-panel p {{ color: #cbd5e0; margin-bottom: 8px; }}
    .section-divider {{ font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em; border-top: 2px solid var(--border); padding: 20px 0 24px; margin-top: 8px; }}
    .track-note {{ font-size: 11px; color: var(--text-muted); margin: -36px 0 40px 32px; max-width: 720px; font-style: italic; }}
    .fn {{ display: block; font-size: 12px; color: var(--text-muted); margin-bottom: 5px; }}
    .footer {{ font-size: 12px; color: var(--text-muted); text-align: center; margin-top: 48px; }}
  </style>
</head>
<body>
  <div class="doc-head">
    <div class="meta">{esc(m["venture"].upper())} · CUSTOMER TRANSFORMATION MODEL · IVE V-MODEL STEP 3 · GENERATED FROM {esc(SRC.name.upper())} — EDIT THE YAML, NOT THIS FILE</div>
    <h1>CTM {esc(m["state"])} — {esc(m["customer"])} journey</h1>
    <div class="meta" style="margin-top:6px">JURISDICTION: {esc(jurisdiction_line(m).upper())}</div>
    <p class="sub">{esc(m["customer_doc"])} Hexagons carry the Flow Register v0.3 component IDs (G3 workbook, tab 6) driving each state change. {esc(m.get("governing_note", "Figures marked assumed are planning inputs pending operator data."))}</p>
  </div>
  <div class="diagram-wrapper">
    <div class="diagram">
      <div class="timeline">{markers}</div>
      {"".join(lanes)}
      {user_section}
      {partner_section}
      <div class="annotation-row">{annos}</div>
    </div>
  </div>
  <div class="supplementary">
    <h2>State-change narrative</h2>
    <p style="color:#666;font-size:14px">The diagram shows that each transition happens. This table holds why: what
    changes in the customer, and how the 4-D product causes it. (Required since 28 Aug 2026.)</p>
    <table><thead><tr><th>Actor</th><th>Transition</th><th>Product</th><th>Register</th><th>What changes in the actor</th><th>How the product causes it</th></tr></thead>
    <tbody>{narratives}</tbody></table>
    <h2>4-D products required in the journey</h2>
    <p style="color:#666;font-size:14px">Every product component the journey requires, across the customer phases and
    the user and partner tracks — derived from the transitions above, never hand-listed. Descriptions come from the sibling AOM
    component register.</p>
    {roster_gap_note}
    <table><thead><tr><th>Component</th><th>4-D type</th><th>What it is</th><th>Drives</th></tr></thead>
    <tbody>{products_roster}</tbody></table>
    <h2>BALM mapping</h2>
    <table><thead><tr><th>BALM requirement</th><th>CTM phase</th><th>Product component</th><th>What it overrides</th></tr></thead>
    <tbody>{balm}</tbody></table>
    <h2>Review findings</h2>
    <ul>{findings}</ul>
    <div class="routing-panel"><h3>Routing</h3>
      <p><strong>Gate position:</strong> {esc(m["routing"]["gate"])}</p>
      <p><strong>Figure discipline:</strong> {esc(m["routing"]["figures"])}</p>
    </div>
    <h2>Footnotes</h2>
    {footnotes}
    <div class="footer">Generated {esc(m["date"])} · Dex · view of {esc(SRC.name)}<br>{esc(PROV)}</div>
  </div>
</body>
</html>
'''

OUT.write_text(page)
n_states = sum(len(p.get("states", [])) for p in m["phases"].values())
n_hex = sum(1 for p in m["phases"].values() for t in p.get("transitions", []) if not t.get("branch"))
n_utracks = len(m.get("user_tracks") or {})
n_ptracks = len(m.get("partner_tracks") or {})
print(f"self-checks PASS · wrote {OUT.name}: {len(m['phases'])} lanes · {n_utracks} user tracks · {n_ptracks} partner tracks · {n_states} states · {n_hex} hexagons · {len(_roster)} components in roster")
