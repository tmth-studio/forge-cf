"""AOM — draw.io MESH view generator (venture-generic).

Mesh style per the design rules in shared/aom-diagram-spec.md ("Mesh view
design rules (IFC-derived)") — structure from Simanis, "Running the Right
Numbers" (book-ended map, three vertical thirds, receiver-end arrows,
dashed=digital); shape/colour semantics from the 2023 Lucid house style:
  · PLACES (the venture, customer premises) — lavender rounded nodes
  · PEOPLE (users, anti-customers, enabler partners) — yellow hexagons
  · FLOW ITEMS (each flow's artifact, labelled with its carrying component) — blue rectangles
  · MONEY ITEMS — green trapezoids
  · ACTIVITIES (org functions) — pink rectangles
  · flows thread FROM actor THROUGH the item node (and any partner waypoints) TO actor,
    as dashed orthogonal lines coloured by OMM class (product red · information blue · money green)

SIX TOGGLEABLE LAYERS:
  1 · Places & people   2 · Product flow   3 · Information flow
  4 · Money flow        5 · Org & allocations   6 · Audit overlay

Open at https://app.diagrams.net or the draw.io desktop app (Edit > Layers).
Lucidchart imports this file directly (Import > draw.io).

The YAML is the model; this file is a generated view. validate_model.py runs
first; render self-checks refuse to write on any failure.
"""
import html as H, yaml
import sys, pathlib
if len(sys.argv) != 2:
    print(f"usage: python3 {pathlib.Path(__file__).name} <venture>-aom-model-at-C<N>.yaml"); sys.exit(1)
SRC = pathlib.Path(sys.argv[1]).resolve()
assert "-model-" in SRC.name, "model file must be named [venture]-aom-model-at-C[N].yaml"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate_model import check_or_die, venture_endpoint_ids, provenance, jurisdiction_line
check_or_die(SRC)  # schema gate — a malformed model fails before any rendering

OUT = SRC.parent / (SRC.name.replace("-model-", "-").rsplit(".", 1)[0] + ".drawio")
m = yaml.safe_load(SRC.read_text())
from layout_overlay import load_overlay
OVERLAY = load_overlay(OUT)   # hand-composed positions win over rule-based defaults

WAYPOINTS = m.get("waypoints", {})
SPINE = m["spine"]

# ---- flatten flows, keep OMM class
flows = []
for cls in ("product", "information", "money"):
    for f in m["flows"][cls]:
        flows.append({**f, "_cls": cls})

# ---- render self-checks
errs = []
# Endpoint set shared with the validator — never a local literal (VA-64 class, fixed 1 Sep 2026).
VENTURE_IDS = venture_endpoint_ids(m)
node_ids = set(m["actors"]) | VENTURE_IDS
for f in flows:
    for end in (f["from"], f["to"]):
        if end not in node_ids: errs.append(f"flow {f['name']}: endpoint '{end}' unknown")
    if f.get("via") and f["via"] not in m["components"]:
        errs.append(f"flow {f['name']}: via '{f['via']}' not a component")
if errs:
    print("SELF-CHECK FAILURES — file not written:")
    [print("  ✗", e) for e in errs]; sys.exit(1)

# ---- styles (the 2023 visual language)
S_PLACE = "rounded=1;arcSize=40;whiteSpace=wrap;html=1;fillColor=#e6d9f2;strokeColor=#8e6bb8;fontSize=10;fontColor=#4a2d6e;"
S_PERSON = "shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=9;fontColor=#7a5c00;"
S_ITEM = "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=9;fontColor=#1f3a63;"
S_MONEY = "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=9;fontColor=#1e4620;"
S_ACT = "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=9;fontColor=#6e1a14;"
S_FLAG = "rounded=0;whiteSpace=wrap;html=1;fillColor=#fff8e6;strokeColor=#d4820a;fontSize=8.5;fontColor=#854d0e;align=left;spacing=4;"
EDGE_C = {"product": "#b3403f", "information": "#1f4fa8", "money": "#166534"}
LAYER_OF = {"product": "L2", "information": "L3", "money": "L4"}

cells = []
node_geom = {}
def cell(id_, value, style, x, y, w, h, layer):
    ov = OVERLAY.get(id_)
    if ov:
        x, y = ov["x"], ov["y"]
        w, h = ov.get("w") or w, ov.get("h") or h
    node_geom[id_] = (x, y, w, h)
    cells.append(f'<mxCell id="{id_}" value="{H.escape(value)}" style="{style}" vertex="1" parent="{layer}">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
pending_edges = []
def edge(id_, src, dst, cls, layer, dashed=True, arrow=True, label=""):
    pending_edges.append({"id": id_, "src": src, "dst": dst, "cls": cls,
                          "layer": layer, "dashed": dashed, "arrow": arrow, "label": label})

# ---- layout per IFC thirds (design rules 1-2): marketing info · core product ·
# support/production info · money base. Items numbered by spine (rule 7).
TOP = 130
ITEM_X, ITEM_W, ITEM_H = 520, 210, 56
ACT_X = 40
PARTNER_X = 280
def spine_pos(f):
    return SPINE.index(f["via"]) if f.get("via") in SPINE else 99

def strip_of(f):
    if f["_cls"] == "money": return 3
    if f["_cls"] == "product": return 1
    return 0 if (f.get("via") or "").startswith("CP") else 2

STRIP_NAMES = ["MARKETING INFORMATION (upper third)", "CORE PRODUCT (middle third)",
               "SUPPORT / PRODUCTION INFORMATION (lower third)", "MONEY (base)"]
flows_seq = sorted(flows, key=spine_pos)
seq_no = {f["name"]: i + 1 for i, f in enumerate(flows_seq)}
flows_sorted = sorted(flows, key=lambda f: (strip_of(f), spine_pos(f)))

item_pos, y = {}, TOP
prev_strip = None
for f in flows_sorted:
    s = strip_of(f)
    if s != prev_strip:
        cell(f"strip_{s}", STRIP_NAMES[s], "text;html=1;fontSize=10;fontStyle=1;fontColor=#6b7280;",
             ITEM_X, y, ITEM_W, 20, LAYER_OF[f["_cls"]])
        y += 30; prev_strip = s
    via = f.get("via")
    label = f"{seq_no[f['name']]}. {f['item']}" + (f"  [{via}]" if via else "  [⚑ uncarried]")
    style = S_MONEY if f["_cls"] == "money" else S_ITEM
    nid = f"item_{f['name']}"
    cell(nid, label, style, ITEM_X, y, ITEM_W, ITEM_H, LAYER_OF[f["_cls"]])
    item_pos[f["name"]] = (nid, y)
    if f.get("flag"):
        cell(f"flag_{f['name']}", f"⚑ {f['flag']}", S_FLAG, ITEM_X + ITEM_W + 16, y, 190, ITEM_H, "L6")
    y += ITEM_H + 26
map_bottom = y

# venture place node (left, tall)
cell("venture_node", f"🏛 {m['venture'].upper()}&#10;(the venture)", S_PLACE, ACT_X, TOP, 170, 90, "L1")

# org functions (pink activities) under the venture, allocations dotted to items
ay = TOP + 120
func_node = {}
for oid, o in m["organisation"].items():
    cell(f"org_{oid}", f"{o['name']} [{o['op_id']}]", "text;html=1;fontSize=9;fontStyle=1;fontColor=#6e1a14;",
         ACT_X, ay, 190, 18, "L5"); ay += 22
    for fid, fn in o["functions"].items():
        func_node[fid] = f"act_{fid}"
        fte = f" · {fn['fte']} FTE" if fn.get("fte") is not None else ""
        cell(f"act_{fid}", f"{fn['name']}{fte}", S_ACT, ACT_X, ay, 190, 34, "L5")
        ay += 42
    ay += 10

# actors: customer/user/anti right column · enablers bottom row
AX, ayr = 950, TOP
# every accepted venture-endpoint spelling routes to the one venture node
actor_node = {vid: "venture_node" for vid in VENTURE_IDS}
for aid, a in m["actors"].items():
    if a["class"] == "enabler": continue
    kind = a.get("kind", "place" if a["class"] == "customer" else "person")
    st = S_PLACE if kind == "place" else S_PERSON
    h = 84 if a["class"] == "customer" else 64
    cell(f"actor_{aid}", f"{a['name']}&#10;[{a['class'].replace('_','-')}]", st, AX, ayr, 180, h, "L1")
    actor_node[aid] = f"actor_{aid}"
    ayr += h + 30
py = TOP + 40
for aid, a in m["actors"].items():
    if a["class"] != "enabler": continue
    label = f"{a['name']}&#10;[{a.get('slot','')} · modular slot]"
    cell(f"actor_{aid}", label, S_PERSON, PARTNER_X, py, 180, 64, "L1")
    actor_node[aid] = f"actor_{aid}"
    if a.get("flag"):
        cell(f"flag_a_{aid}", f"⚑ {a['flag']}", S_FLAG, PARTNER_X, py + 68, 180, 60, "L6")
        py += 66
    py += 96
ex = AX + 220

# ---- flows thread from → item → (waypoints) → to
for f in flows_sorted:
    nid, _ = item_pos[f["name"]]
    lay = LAYER_OF[f["_cls"]]
    src, dst = actor_node[f["from"]], actor_node[f["to"]]
    dashed = f.get("medium", "digital") != "physical"   # rule 4: dashed digital, solid physical
    edge(f"e_{f['name']}_in", src, nid, f["_cls"], lay, dashed=dashed, arrow=False)
    chain = [actor_node[w] for w in WAYPOINTS.get(f.get("via"), []) if w in actor_node and actor_node[w] != dst]
    prev = nid
    for i, wnode in enumerate(chain):
        edge(f"e_{f['name']}_w{i}", prev, wnode, f["_cls"], lay, dashed=dashed, arrow=False)
        prev = wnode
    edge(f"e_{f['name']}_out", prev, dst, f["_cls"], lay, dashed=dashed, label=f.get("label", ""))

# allocations: function --performs--> item (thin grey dotted)
for f in flows_sorted:
    via = f.get("via")
    if via:
        alloc = m["components"][via]["allocated_to"]
        if alloc in func_node:
            edge(f"al_{f['name']}", func_node[alloc], item_pos[f["name"]][0], "_", "L5", label="")

# component flags → audit layer, near their first item
for cid, c in m["components"].items():
    if c.get("flag"):
        first = next((f for f in flows_sorted if f.get("via") == cid), None)
        if first:
            _, iy = item_pos[first["name"]]
            cell(f"flag_c_{cid}", f"⚑ {cid}: {c['flag'].lstrip('⚑ ')}", S_FLAG, ITEM_X + ITEM_W + 16, iy + ITEM_H - 8, 190, 56, "L6")

# ---- anchor distribution: one lane per flow on shared nodes (design rule 6)
def center(nid):
    x, yy, w, h = node_geom[nid]
    return (x + w / 2, yy + h / 2)

def side_of(nid, other):
    (cx, cy), (ox, oy) = center(nid), center(other)
    if abs(ox - cx) > abs(oy - cy):
        return "right" if ox > cx else "left"
    return "bottom" if oy > cy else "top"

incident = {}
for i, e in enumerate(pending_edges):
    for role in ("src", "dst"):
        nid, other = e[role], e["dst" if role == "src" else "src"]
        if nid not in node_geom or other not in node_geom: continue
        s = side_of(nid, other)
        okey = center(other)[1] if s in ("left", "right") else center(other)[0]
        incident.setdefault((nid, s), []).append((okey, i, role))

anchors = {}
for (nid, s), lst in incident.items():
    lst.sort()
    n = len(lst)
    for k, (_, i, role) in enumerate(lst):
        fr = (k + 1) / (n + 1)
        anchors[(i, role)] = {"right": (1, fr), "left": (0, fr), "top": (fr, 0), "bottom": (fr, 1)}[s]

for i, e in enumerate(pending_edges):
    st = (f"edgeStyle=orthogonalEdgeStyle;rounded=1;jettySize=auto;html=1;strokeColor={EDGE_C.get(e['cls'], '#9ca3af')};"
          f"strokeWidth=1.5;{'dashed=1;' if e['dashed'] else ''}endArrow={'block' if e['arrow'] else 'none'};fontSize=8;")
    if (i, "src") in anchors:
        ax, ay = anchors[(i, "src")]
        st += f"exitX={ax:.3f};exitY={ay:.3f};exitDx=0;exitDy=0;"
    if (i, "dst") in anchors:
        ax, ay = anchors[(i, "dst")]
        st += f"entryX={ax:.3f};entryY={ay:.3f};entryDx=0;entryDy=0;"
    cells.append(f'<mxCell id="{e["id"]}" value="{H.escape(e["label"])}" style="{st}" edge="1" parent="{e["layer"]}" '
                 f'source="{e["src"]}" target="{e["dst"]}"><mxGeometry relative="1" as="geometry"/></mxCell>')

# title + legend — page bounds follow actual geometry (overlay may move nodes)
_gx = max(x + w for x, y, w, h in node_geom.values())
_gy = max(y + h for x, y, w, h in node_geom.values())
width = max(AX + 220, ex + 40, _gx + 40)
map_bottom = max(map_bottom, _gy - 200)
cell("title", f"OP MODEL MESH {m['state'].replace('at-','AFTER ').upper()} — JURISDICTION: {jurisdiction_line(m)} · {m['scale_header']} · GENERATED from {SRC.name} — edit the YAML, not this diagram",
     "text;html=1;fontSize=11;fontStyle=1;align=left;verticalAlign=middle;fillColor=#1a1a2e;fontColor=#ffffff;spacing=10;whiteSpace=wrap;",
     ACT_X, 24, width - ACT_X - 40, 66, "L1")
cell("legend", "LEGEND — lavender rounded: place · yellow hexagon: person/partner · blue rectangle: flow item [carrying component] · green trapezoid: money item · pink: org activity · line colour: red product / blue information / green money (dashed = digital, solid = physical) · arrows point at the receiver · items numbered in transaction-cycle order · vertical thirds per the IFC guide",
     "text;html=1;fontSize=9;align=left;whiteSpace=wrap;fontColor=#4a5568;",
     ACT_X, map_bottom + 190, 900, 40, "L1")

layers = "".join(f'<mxCell id="{lid}" value="{H.escape(nm)}" parent="0"/>' for lid, nm in [
    ("L1", "1 · Places & people"), ("L2", "2 · Product flow"), ("L3", "3 · Information flow"),
    ("L4", "4 · Money flow"), ("L5", "5 · Org & allocations"), ("L6", "6 · Audit overlay")])

xml = (f'<mxfile host="dex" modified="{m["date"]}" agent="{provenance(__file__, SRC)}" version="21.0.0">'
       f'<diagram name="Op Model mesh {H.escape(m["state"])}" id="aom_mesh"><mxGraphModel dx="1400" dy="900" '
       f'grid="0" page="1" pageWidth="{width}" pageHeight="{max(map_bottom + 260, _gy + 60)}">'
       f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{layers}{"".join(cells)}</root>'
       f'</mxGraphModel></diagram></mxfile>')

import xml.etree.ElementTree as ET
ET.fromstring(xml)  # refuse to write malformed XML
OUT.write_text(xml)
n_money = sum(1 for f in flows if f["_cls"] == "money")
print(f"self-checks PASS · XML valid · wrote {OUT.name} (MESH): 6 layers · "
      f"{len(flows)} flow items ({n_money} money trapezoids) · {len(m['actors'])} actors · "
      f"{len(func_node)} activities · allocations wired")
