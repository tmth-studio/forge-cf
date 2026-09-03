"""Layout overlay — hand-composed positions as a saved, versioned artefact.

Solves "hand-layout is lost on regeneration": content lives in the model YAML,
POSITIONS live in a sibling layout file, and the generators apply the layout
on top of their rule-based defaults. Compositional judgment is spent once per
node, not once per regeneration.

Files: for a view  [venture]-aom-at-C[N].drawio  the layout file is
                   [venture]-aom-layout-at-C[N].yaml
(same rule for -ctm-). Format: {node_id: {x, y[, w, h]}}.

Harvest (run after hand-arranging in draw.io / Lucid and saving the file):
    python3 harvest_layout.py <edited>.drawio
reads every vertex's geometry by its stable id and writes the layout file.
Nodes later removed from the model leave harmless stale entries; new nodes
simply have no entry and fall back to the rule-based default.
"""
import pathlib
import xml.etree.ElementTree as ET
import yaml


def layout_path_for(view_path):
    p = pathlib.Path(view_path)
    name = p.name
    for m in ("-aom-at-C", "-ctm-at-C"):
        if m in name:
            stem = name.replace(m, m.replace("-at-C", "-layout-at-C")).rsplit(".", 1)[0]
            return p.parent / (stem + ".yaml")
    raise ValueError(f"cannot derive layout path from '{name}' — expected -aom-at-C[N] or -ctm-at-C[N]")


def load_overlay(view_path):
    """Returns {node_id: {x, y[, w, h]}} or {} when no layout file exists."""
    lp = layout_path_for(view_path)
    if not lp.exists():
        return {}
    data = yaml.safe_load(lp.read_text()) or {}
    return data.get("nodes", data)  # tolerate bare mapping


def harvest(drawio_path):
    """Read vertex geometries from an edited .drawio into the layout file."""
    drawio_path = pathlib.Path(drawio_path)
    root = ET.fromstring(drawio_path.read_text())
    nodes = {}
    for c in root.iter("mxCell"):
        if c.get("vertex") == "1" and c.get("id"):
            g = c.find("mxGeometry")
            if g is None or g.get("x") is None:
                continue
            nodes[c.get("id")] = {
                "x": round(float(g.get("x")), 1), "y": round(float(g.get("y")), 1),
                "w": round(float(g.get("width", 0)), 1), "h": round(float(g.get("height", 0)), 1),
            }
    lp = layout_path_for(drawio_path)
    existing = {}
    if lp.exists():
        existing = (yaml.safe_load(lp.read_text()) or {}).get("nodes", {})
    stale = sorted(set(existing) - set(nodes))
    merged = {**existing, **nodes}
    lp.write_text(yaml.dump(
        {"_note": f"Hand-composed layout for {drawio_path.name} — harvested positions; applied on regeneration. Delete an entry to return that node to the rule-based default.",
         "nodes": merged}, sort_keys=True, allow_unicode=True))
    return lp, len(nodes), stale


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("usage: python3 harvest_layout.py <venture>-(aom|ctm)-at-C<N>.drawio")
        sys.exit(1)
    lp, n, stale = harvest(sys.argv[1])
    print(f"harvested {n} node positions → {lp.name}" + (f" · {len(stale)} stale entries kept: {stale[:5]}" if stale else ""))
