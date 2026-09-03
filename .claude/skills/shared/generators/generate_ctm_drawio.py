"""CTM — draw.io layered view generator (venture-generic).

Reads <venture>-ctm-model-at-C<N>.yaml (the model — single source of truth) and
emits <venture>-ctm-at-C<N>.drawio with FOUR TOGGLEABLE LAYERS:
  1 · Journey — states & transitions
  2 · Product components (FR-ID hexagons on the transitions)
  3 · Escalation track
  4 · Audit overlay — flags

Open at https://app.diagrams.net or the draw.io desktop app; toggle layers
via Edit > Layers. Lucidchart imports this file directly (Import > draw.io).

The YAML is the model; this file is a generated view. Self-checks run
before writing; the file is NOT written on any failure.
"""
import sys, pathlib, html as H, yaml
import xml.etree.ElementTree as ET

import sys, pathlib
if len(sys.argv) != 2:
    print(f"usage: python3 {pathlib.Path(__file__).name} <venture>-MODEL-model-at-C<N>.yaml"); sys.exit(1)
SRC = pathlib.Path(sys.argv[1]).resolve()
assert "-model-" in SRC.name, "model file must be named [venture]-[model]-model-at-C[N].yaml"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate_model import check_or_die, provenance, jurisdiction_line
check_or_die(SRC)  # schema gate — a malformed model fails before any rendering

OUT = SRC.parent / (SRC.name.replace("-model-", "-").rsplit(".", 1)[0] + ".drawio")

m = yaml.safe_load(SRC.read_text())
from layout_overlay import load_overlay
OVERLAY = load_overlay(OUT)   # hand-composed positions win over rule-based defaults
import re as _re
def _valid_id(c): return bool(_re.match(r"^(WP|CP|PP|PartP)-\d+$", c))

errs = []
for pid, ph in m["phases"].items():
    if ph.get("undesigned"):
        continue
    sids = {s["id"] for s in ph["states"]} | ({"decision"} if ph.get("decision") else set())
    for t in ph["transitions"]:
        for end in (t["from"], t["to"]):
            if end not in sids: errs.append(f"{pid}: endpoint '{end}' unknown")
        if not t.get("branch") and not t.get("components") and not t.get("flag"):
            errs.append(f"{pid}: {t['from']}→{t['to']} uncarried and unflagged")
        for c in t.get("components", []):
            if not _valid_id(c): errs.append(f"{pid}: '{c}' is not a Flow-Register-format ID")
if errs:
    print("SELF-CHECK FAILURES — file not written:")
    [print("  ✗", e) for e in errs]
    sys.exit(1)

STATE_W, STATE_H, STEP, LANE_H, TOP, LEFT = 150, 70, 260, 210, 140, 60
FILLS = {"W": ("#e8eef8", "#1f4fa8"), "C": ("#e8f4f4", "#007d7a"), "P": ("#fef9e6", "#854d0e")}

cells, pos = [], {}
ALL_GEOM = []
def cell(id_, value, style, x, y, w, h, layer):
    ov = OVERLAY.get(id_)
    if ov:
        x, y = ov["x"], ov["y"]
        w, h = ov.get("w") or w, ov.get("h") or h
    ALL_GEOM.append((x, y, w, h))
    cells.append(f'<mxCell id="{id_}" value="{H.escape(value)}" style="{style}" vertex="1" parent="{layer}">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
def edge(id_, style, src, dst, layer, label=""):
    cells.append(f'<mxCell id="{id_}" value="{H.escape(label)}" style="{style}" edge="1" parent="{layer}" '
                 f'source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry"/></mxCell>')

max_cols = 0
for li, (pid, ph) in enumerate(m["phases"].items()):
    y = TOP + li * LANE_H
    if ph.get("undesigned"):
        cell(f"lane_{pid}", ph["name"].upper(),
             "text;html=1;fontSize=11;fontStyle=1;fontColor=#6b7280;horizontal=0;align=center;",
             LEFT - 45, y, 26, STATE_H, "L1")
        cell(f"und_{pid}", ph["undesigned"],
             "rounded=1;whiteSpace=wrap;html=1;dashed=1;fillColor=none;strokeColor=#9ca3af;fontSize=10;fontColor=#6b7280;",
             LEFT, y, STEP * 3, STATE_H, "L1")
        continue
    cell(f"lane_{pid}", ph["name"].upper(),
         "text;html=1;fontSize=11;fontStyle=1;fontColor=#6b7280;horizontal=0;align=center;",
         LEFT - 45, y, 26, STATE_H, "L1")
    col = 0
    order = [s["id"] for s in ph["states"]]
    dec = ph.get("decision")
    seq = []
    for sid in order:
        if dec and dec["branch_a"] == sid:
            seq.append(("decision", dec))
        seq.append(("state", sid))
    for kind, obj in seq:
        x = LEFT + col * STEP
        if kind == "state":
            s = next(st for st in ph["states"] if st["id"] == obj)
            fill = "#d1fae5" if s.get("final") else "#f0f9f9"
            stroke = "#059669" if s.get("final") else "#93c5c4"
            cell(f"st_{pid}_{obj}", f"{s['icon']} {s['label']}",
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};fontSize=10;",
                 x, y, STATE_W, STATE_H, "L1")
            pos[(pid, obj)] = (x, y)
        else:
            cell(f"dec_{pid}", obj["label"],
                 "rhombus;whiteSpace=wrap;html=1;fillColor=#fff8e6;strokeColor=#d4820a;fontSize=9;fontColor=#854d0e;",
                 x + 25, y - 8, STATE_W - 50, STATE_H + 16, "L1")
            pos[(pid, "decision")] = (x, y)
        col += 1
    max_cols = max(max_cols, col)
    # journey edges + component hexagons at midpoints
    for t in ph["transitions"]:
        a, b = t["from"], t["to"]
        sa = f"dec_{pid}" if a == "decision" else f"st_{pid}_{a}"
        sb = f"dec_{pid}" if b == "decision" else f"st_{pid}_{b}"
        lbl = "A" if t.get("branch") == "A" else ""
        edge(f"j_{pid}_{a}_{b}", "strokeColor=#9ca3af;strokeWidth=2;endArrow=block;html=1;fontSize=10;fontStyle=1;", sa, sb, "L1", lbl)
        comps = t.get("components", [])
        if comps or t.get("flag"):
            xa, xb = pos[(pid, a)][0], pos[(pid, b)][0]
            mx = (xa + xb) / 2 + STATE_W / 2 - 45
            head = " / ".join(comps) if comps else "⚑ no flow ID"
            fill, fg = FILLS.get(comps[0][0], ("#f0ebfb", "#5b21b6")) if comps else ("#f0ebfb", "#5b21b6")
            cell(f"hex_{pid}_{a}_{b}", f"{head}&#10;{t.get('label','')}",
                 f"shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={fg};fontSize=8.5;fontColor={fg};",
                 mx, y - 52, 110, 48, "L2")
            if t.get("flag"):
                cell(f"flag_{pid}_{a}_{b}", f"⚑ {t['flag']}",
                     "rounded=0;whiteSpace=wrap;html=1;fillColor=#fff8e6;strokeColor=#d4820a;fontSize=8.5;fontColor=#854d0e;align=left;spacing=4;",
                     mx - 30, y + STATE_H + 8, 190, 54, "L4")

# escalation (branch B off a decision — only when one exists)
dec_pid = next((pid for pid, ph in m["phases"].items() if ph.get("decision")), None)
e = m.get("escalation")
if dec_pid and e:
    ey = TOP + list(m["phases"]).index(dec_pid) * LANE_H - 10
    ex = LEFT + max_cols * STEP + 40
    outcomes = "&#10;".join(("✓ " if o["kind"] == "win" else "✗ ") + o["label"] for o in e["outcomes"])
    cell("esc", f"{e['title'].upper()}&#10;&#10;{e['timeline']}&#10;{e['note']}&#10;&#10;{outcomes}",
         "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#374151;strokeWidth=2;fontSize=9;align=left;spacing=8;verticalAlign=top;",
         ex, ey, 250, 170, "L3")
    edge("esc_edge", "strokeColor=#374151;strokeWidth=2;dashed=1;endArrow=block;html=1;fontSize=10;fontStyle=1;",
         f"dec_{dec_pid}", "esc", "L3", "B")
else:
    ex = LEFT + max_cols * STEP + 40

# title + governance annotation
width = ex + 290
cell("title", f"CTM {m['state'].upper()} — {m['customer'].upper()} JOURNEY · JURISDICTION: {jurisdiction_line(m)} · {m['customer_doc']} · GENERATED from {SRC.name} — edit the YAML, not this diagram",
     "text;html=1;fontSize=11;fontStyle=1;align=left;verticalAlign=middle;fillColor=#1a1a2e;fontColor=#ffffff;spacing=10;whiteSpace=wrap;",
     LEFT - 45, 30, width - LEFT, 70, "L1")
for i, a in enumerate(m["annotations"]):
    cell(f"anno_{i}", f"{a['title']}: {a['text']}",
         "rounded=0;whiteSpace=wrap;html=1;fillColor=#1a1a2e;fontColor=#ffffff;fontSize=8.5;align=left;spacing=6;",
         LEFT - 45 + i * 480, TOP + len(m["phases"]) * LANE_H, 460, 70, "L4")

layers = "".join(f'<mxCell id="{lid}" value="{H.escape(nm)}" parent="0"/>' for lid, nm in [
    ("L1", "1 · Journey — states & transitions"), ("L2", "2 · Product components (FR IDs)"),
    ("L3", "3 · Escalation track"), ("L4", "4 · Audit overlay — flags")])

xml = (f'<mxfile host="dex" modified="{m["date"]}" agent="{provenance(__file__, SRC)}" version="21.0.0">'
       f'<diagram name="CTM {H.escape(m["state"])}" id="ctm_c10"><mxGraphModel dx="1400" dy="900" grid="0" '
       f'page="1" pageWidth="{max(width, int(max(g[0] + g[2] for g in ALL_GEOM)) + 40)}" pageHeight="{max(TOP + len(m["phases"]) * LANE_H + 130, int(max(g[1] + g[3] for g in ALL_GEOM)) + 60)}">'
       f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{layers}{"".join(cells)}</root>'
       f'</mxGraphModel></diagram></mxfile>')

ET.fromstring(xml)  # refuse to write malformed XML
OUT.write_text(xml)
n_states = sum(len(p.get("states", [])) for p in m["phases"].values())
print(f"self-checks PASS · XML valid · wrote {OUT.name}: 4 layers · {n_states} states · "
      f"{sum(1 for c in cells if 'hex_' in c and 'vertex' in c)} component hexagons · escalation + flags")
