"""AOM — Operational Model Map (HTML view) generator (venture-generic).

Reads <venture>-aom-model-at-C<N>.yaml (the model — single source of truth) and
emits <venture>-aom-at-C<N>-generated.html: the Operational Model Map per
.claude/skills/shared/aom-diagram-spec.md — two poles (HQ left, customer
right), a central spine of numbered hexagon component flows on directional
arrows, partners as pass-through waypoints, money in/out explicit.

The YAML is the model; this file and the SysML file are views of it.
Self-checks run before writing; the file is NOT written on any failure.
"""
import html as H, yaml
import sys, pathlib
if len(sys.argv) != 2:
    print(f"usage: python3 {pathlib.Path(__file__).name} <venture>-aom-model-at-C<N>.yaml"); sys.exit(1)
SRC = pathlib.Path(sys.argv[1]).resolve()
assert "-model-" in SRC.name, "model file must be named [venture]-aom-model-at-C[N].yaml"

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate_model import check_or_die, is_venture, provenance, jurisdiction_line
check_or_die(SRC)
PROV = provenance(__file__, SRC)  # schema gate — a malformed model fails before any rendering

OUT = SRC.parent / (SRC.name.replace("-model-", "-").rsplit(".", 1)[0] + "-generated.html")

m = yaml.safe_load(SRC.read_text())

# ---- spine narrative order and partner waypoints come from the YAML
SPINE = m["spine"]
WAYPOINTS = m.get("waypoints", {})
_CLASS_ICON = {"customer": "🏬", "user": "👤", "anti_customer": "⚖️", "enabler": "🤝"}
def icon_of(aid):
    a = m["actors"][aid]
    return a.get("icon", _CLASS_ICON.get(a["class"], "🔷"))

# ---- derive direction + OMM class per component from its flows
comp_flows = {}
extra_flows = []          # flows not carried by a spine component (boundary)
gap_flows = []            # flagged flows with no carrying component
for cls in ("product", "information", "money"):
    for f in m["flows"][cls]:
        f["_cls"] = cls
        if f.get("via"):
            comp_flows.setdefault(f["via"], []).append(f)
        elif f.get("flag"):
            gap_flows.append(f)
        else:
            extra_flows.append(f)

# Customer side derived from the model, never hardcoded (28 Aug audit, fixed 1 Sep
# 2026): the actors the venture transforms — customer, user, anti_customer.
CUST = {aid for aid, a in m["actors"].items() if a["class"] in ("customer", "user", "anti_customer")}
def direction(cid):
    outs = ins = partner = internal = False
    for f in comp_flows.get(cid, []):
        f_v, t_v = is_venture(f["from"], m), is_venture(f["to"], m)
        if f_v and f["to"] in CUST: outs = True
        elif t_v and f["from"] in CUST: ins = True
        elif f_v and t_v: internal = True
        elif f_v or t_v: partner = True
    if outs and ins: return "round"
    if outs: return "out"
    if ins: return "in"
    if internal: return "internal"
    if partner: return "partner"
    return None

# ---- self-checks
errs = []
for cid in m["components"]:
    if cid not in SPINE: errs.append(f"{cid} missing from spine order")
    if cid not in comp_flows: errs.append(f"{cid} has no flow in the YAML")
for cid in SPINE:
    if cid not in m["components"]: errs.append(f"spine id {cid} not a component")
for cid, wps in WAYPOINTS.items():
    for wp in wps:
        if wp not in m["actors"]: errs.append(f"waypoint {wp} on {cid} not an actor")
if errs:
    print("SELF-CHECK FAILURES — file not written:")
    for e in errs: print("  ✗", e)
    sys.exit(1)

# ---- palette
HEX = {"CP": ("#e8eef8", "#1f4fa8"), "WP": ("#eceafb", "#4c3fa8"),
       "PP": ("#e6f4ec", "#166534"), "Part": ("#f0ebfb", "#5b21b6"), "PartP": ("#f0ebfb", "#5b21b6")}
LINE = {"product": "#b3403f", "information": "#1f4fa8", "money": "#166534"}

def esc(s): return H.escape(str(s))

rows = []
for cid in SPINE:
    c = m["components"][cid]
    d = direction(cid)
    cls = comp_flows[cid][0]["_cls"]
    colour = LINE[cls]
    typ = cid.split("-")[0]
    bg, fg = HEX[typ]
    dashed = "dashed" if cid == "PP-2" else "solid"
    wps = "".join(
        f'<span class="waypoint">{icon_of(w)} {esc(m["actors"][w]["name"])} <span class="slot">{esc(m["actors"][w].get("slot",""))}</span></span>'
        for w in WAYPOINTS.get(cid, []))
    flag = f'<div class="rowflag">⚑ {esc(c["flag"].lstrip("⚑ "))}</div>' if c.get("flag") else ""
    left_arr = "◀" if d in ("in", "round") else ""
    right_arr = "▶" if d in ("out", "round") else ""
    if d == "partner": right_arr = "▶"
    if d == "internal": left_arr, right_arr = "⟳", ""
    items = " · ".join(sorted({f["item"] for f in comp_flows[cid]}))
    rows.append(f'''
      <div class="flowrow">
        <div class="fl-line {dashed}" style="--lc:{colour}">
          <span class="arr left">{left_arr}</span>
          <div class="hexwrap">
            <div class="hex" style="background:{bg};color:{fg}">{cid}<br><span class="hexname">{esc(c["doc"].split("—")[0].split("·")[0][:52])}</span></div>
          </div>
          {f'<div class="wps">{wps}</div>' if wps else ''}
          <span class="arr right">{right_arr}</span>
        </div>
        <div class="rowmeta">{esc(items)} · DRI: {esc(c["dri"])}{" · " + esc(c["cost_ref"]) if c.get("cost_ref") else ""}</div>
        {flag}
      </div>''')

gap_rows = "".join(f'''
      <div class="flowrow gap">
        <div class="fl-line dashed" style="--lc:#9ca3af">
          <div class="hexwrap"><div class="hex gaphex">GAP<br><span class="hexname">{esc(f["name"])}</span></div></div>
          <span class="arr right">▶</span>
        </div>
        <div class="rowflag">⚑ {esc(f["flag"].lstrip("⚑ "))}</div>
      </div>''' for f in gap_flows)

def _ep_label(e):
    return m["venture"] if is_venture(e, m) else m["actors"].get(e, {"name": e})["name"]
boundary_rows = "".join(
    f'<tr><td>{esc(f["name"])}</td><td>{esc(_ep_label(f["from"]))} → '
    f'{esc(_ep_label(f["to"]))}</td>'
    f'<td>{esc(f["_cls"])}</td><td>{esc(f.get("doc", ""))}</td></tr>' for f in extra_flows)

org_cards = "".join(
    f'<div class="card"><h4>{H.escape(o["name"])} [{o["op_id"]}]</h4>' +
    " · ".join(H.escape(fn["name"]) for fn in o["functions"].values()) +
    (f'<div class="flag">{H.escape(o["cost_ref"])}</div>' if "⚑" in o.get("cost_ref", "") else f'<div style="color:#718096;font-size:11.5px;margin-top:4px">{H.escape(o["cost_ref"])}</div>') +
    "</div>" for o in m["organisation"].values())

_orgs = list(m["organisation"].items())
other_org_subs = "".join(
    f'<div class="sub">{H.escape(o["name"])} [{o["op_id"]}]: ' +
    ", ".join(H.escape(fn["name"]) for fn in o["functions"].values()) +
    f' · {H.escape(o["cost_ref"])}</div>'
    for oid, o in _orgs if oid != "hq")

cust_actor = next(a for a in m["actors"].values() if a["class"] == "customer")
_ICON2 = {"user": "👤", "anti_customer": "⚖️"}
other_actor_lines = "".join(
    f'<div class="sub">{_ICON2[a["class"]]} <b>{a["class"].replace("_", "-").title()}:</b> {H.escape(a["doc"])}</div>'
    for a in m["actors"].values() if a["class"] in _ICON2)

hq_functions = "".join(
    f'<li>{esc(fn["name"])} <span class="fte">{fn["fte"] if fn["fte"] is not None else "—"} FTE</span></li>'
    for fn in m["organisation"]["hq"]["functions"].values())

partner_band = "".join(f'''
    <div class="partner-card{" flagged" if a.get("flag") else ""}">
      <div class="p-ico">{icon_of(aid)}</div>
      <div class="p-name">{esc(a["name"])}</div>
      <div class="p-slot">{esc(a.get("slot", ""))} · modular slot</div>
      {f'<div class="p-flag">⚑ {esc(a["flag"])}</div>' if a.get("flag") else ""}
    </div>''' for aid, a in m["actors"].items() if a["class"] == "enabler")

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(m["venture"])} Op Model {esc(m["state"])} — generated view</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Lora:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{ --bg:#f5f4f1; --surface:#fff; --text:#0f1923; --muted:#718096; --border:#dde1e7;
  --accent:#1f4fa8; --accent-light:#e8eef8; --panel:#0f2744; --warn-bg:#fff8e6; --warn-bd:#d4820a;
  --ui:'DM Sans',system-ui,sans-serif; --body:'Lora',Georgia,serif; }}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:var(--ui);font-size:16px;line-height:1.55}}
.container{{max-width:1200px;margin:0 auto;padding:36px 28px 70px;background:var(--surface)}}
.meta{{font-size:12px;letter-spacing:.05em;color:var(--muted);text-transform:uppercase;margin-bottom:4px}}
h1{{font-size:26px;font-weight:600;margin-bottom:6px}}
.scale-header{{background:var(--panel);color:#fff;padding:12px 18px;font-size:14px;margin:16px 0 26px}}
.scale-header strong{{color:#f0d98a}}
.map{{display:grid;grid-template-columns:200px 1fr 200px;gap:0 18px;margin-bottom:8px}}
.pole{{border:2px solid var(--accent);background:var(--accent-light);padding:16px 14px;grid-row:1;align-self:stretch}}
.pole.hq{{grid-column:1}} .pole.cust{{grid-column:3}}
.pole .ico{{font-size:34px;text-align:center;display:block}}
.pole h3{{font-size:14px;text-align:center;margin:6px 0 10px}}
.pole ul{{list-style:none;font-size:11.5px;color:#334}}
.pole li{{padding:3px 0;border-bottom:1px solid #cdd8ec;display:flex;justify-content:space-between;gap:6px}}
.fte{{color:var(--muted);white-space:nowrap}}
.pole .sub{{font-size:11px;color:var(--muted);margin-top:8px;line-height:1.4}}
.spine{{display:flex;flex-direction:column;gap:14px;padding:4px 0;grid-column:2;grid-row:1}}
.flowrow{{position:relative}}
.fl-line{{display:flex;align-items:center;gap:8px;position:relative;min-height:56px}}
.fl-line::before{{content:'';position:absolute;left:18px;right:18px;top:50%;height:2px;background:var(--lc)}}
.fl-line.dashed::before{{background:repeating-linear-gradient(90deg,var(--lc) 0 7px,transparent 7px 14px)}}
.arr{{font-size:15px;color:var(--lc);z-index:1;width:18px;text-align:center}}
.arr.left{{margin-right:auto}}
.arr.right{{margin-left:auto}}
.hexwrap{{position:absolute;left:50%;transform:translateX(-50%);z-index:2}}
.hex{{width:150px;min-height:62px;clip-path:polygon(12% 0,88% 0,100% 50%,88% 100%,12% 100%,0 50%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  font-size:12px;font-weight:600;padding:8px 20px;line-height:1.25}}
.hexname{{font-weight:500;font-size:10.5px}}
.gaphex{{background:#f1f3f5;color:#4a5568;border:1px dashed #9ca3af}}
.wps{{position:absolute;left:63%;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:3px;z-index:2}}
.waypoint{{background:#f0ebfb;color:#5b21b6;font-size:10px;font-weight:600;
  padding:2px 7px;border:1px solid #c4aff0;white-space:nowrap}}
.waypoint .slot{{font-weight:400;color:#7a5bd6}}
.rowmeta{{font-size:11px;color:var(--muted);text-align:center;margin-top:2px}}
.rowflag{{font-size:11px;color:#854d0e;background:var(--warn-bg);border-left:3px solid var(--warn-bd);
  padding:4px 8px;margin:4px auto 0;max-width:640px;text-align:center}}
.legend{{display:flex;flex-wrap:wrap;gap:18px;font-size:12px;background:var(--accent-light);
  border-left:4px solid var(--accent);padding:12px 16px;margin:22px 0}}
.legend b{{font-weight:600}}
.chip{{display:inline-block;width:11px;height:11px;margin-right:4px;vertical-align:-1px}}
h2{{font-size:19px;font-weight:600;margin:34px 0 12px}}
.partner-band{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:14px 0}}
.partner-card{{border:1px solid var(--border);padding:12px;font-size:12px}}
.partner-card.flagged{{border-color:var(--warn-bd);background:var(--warn-bg)}}
.p-ico{{font-size:22px}} .p-name{{font-weight:600;margin:4px 0 2px}} .p-slot{{color:#5b21b6;font-size:11px}}
.p-flag{{color:#854d0e;font-size:10.5px;margin-top:6px;line-height:1.35}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin:10px 0 24px}}
thead th{{text-align:left;font-weight:600;padding:8px 10px;border-bottom:2px solid #b0b8c4}}
tbody td{{padding:7px 10px;border-bottom:1px solid var(--border);vertical-align:top}}
.cards{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin:14px 0}}
.card{{border:1px solid var(--border);padding:14px;font-size:13px}}
.card h4{{font-size:13px;margin-bottom:6px}}
.card .flag{{color:#854d0e;font-size:11.5px}}
.routing{{background:var(--panel);color:#cbd5e0;padding:18px 22px;font-size:13px;margin-top:30px}}
.routing h3{{color:#f0d98a;font-size:13px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px}}
.footer{{font-size:12px;color:var(--muted);text-align:center;margin-top:36px;border-top:1px solid var(--border);padding-top:12px}}
</style>
</head>
<body>
<div class="container">
  <div class="meta">{esc(m["venture"])} · Operational Model Map · {esc(m["state"])} · GENERATED from {SRC.name} — edit the YAML, not this file</div>
  <h1>Op Model {esc(m["state"].replace("at-", "after "))}</h1>
  <div class="meta" style="margin-top:-2px">Jurisdiction: {esc(jurisdiction_line(m))}</div>
  <div class="scale-header"><strong>LAST-MILE OPERATING UNIT:</strong> {esc(m["scale_header"])}</div>

  <div class="map">
    <div class="pole hq">
      <span class="ico">🏢</span>
      <h3>HQ — {esc(m["venture"])} layer [OP-2]</h3>
      <ul>{hq_functions}</ul>
      {other_org_subs}
    </div>
    <div class="spine">{"".join(rows)}{gap_rows}</div>
    <div class="pole cust">
      <span class="ico">🏬</span>
      <h3>Customer — {esc(cust_actor["name"])}</h3>
      <div class="sub" style="margin-top:0">{esc(cust_actor["doc"])}</div>
      {other_actor_lines}
    </div>
  </div>

  <div class="legend">
    <span><b>Flow class:</b></span>
    <span><span class="chip" style="background:#b3403f"></span>product</span>
    <span><span class="chip" style="background:#1f4fa8"></span>information</span>
    <span><span class="chip" style="background:#166534"></span>money</span>
    <span style="margin-left:14px"><b>Component type:</b></span>
    <span><span class="chip" style="background:#e8eef8;border:1px solid #1f4fa8"></span>CP communications</span>
    <span><span class="chip" style="background:#eceafb;border:1px solid #4c3fa8"></span>WP working</span>
    <span><span class="chip" style="background:#e6f4ec;border:1px solid #166534"></span>PP payment</span>
    <span><b>Direction:</b> ▶ outbound · ◀ inbound · ◀▶ round-trip · ⟳ internal · dashed = excluded / gap</span>
  </div>

  <h2>Partner band — modular slots (pass-through waypoints, never poles)</h2>
  <div class="partner-band">{partner_band}</div>

  <h2>Money &amp; boundary flows not on the customer axis</h2>
  <table>
    <thead><tr><th>Flow</th><th>Path</th><th>Class</th><th>Note</th></tr></thead>
    <tbody>{boundary_rows}
      <tr><td colspan="4" style="color:#718096;font-size:12px">{esc(m.get("boundary_note", "Boundary actors per the completeness check — Shareholders, Employees, Suppliers & vendors, tax — carried in the fidelity boundary."))}</td></tr>
    </tbody>
  </table>

  <h2>Operating unit summary</h2>
  <div class="cards">
    <div class="card"><h4>LMU</h4>{esc(m.get("lmu_note", ""))}</div>
    {org_cards}
  </div>

  <div class="routing">
    <h3>Routing</h3>
    Generated view of {esc(SRC.name)} — the model file is the single source of truth; the SysML and draw.io views are generated from the same file. {esc(m.get("routing_note", ""))}
  </div>
  <div class="footer">Generated {esc(m["date"])} · Dex · Op Model Map per aom-diagram-spec · demo of the model→views pattern<br>{esc(PROV)}</div>
</div>
</body>
</html>
'''

OUT.write_text(page)
print(f"self-checks PASS · wrote {OUT.name}: {len(SPINE)} spine flows · {len(gap_flows)} gap rows · {len(extra_flows)} boundary flows · {len([a for a in m['actors'].values() if a['class']=='enabler'])} partner slots")
