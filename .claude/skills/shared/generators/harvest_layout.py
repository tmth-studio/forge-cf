#!/usr/bin/env python3
"""Harvest hand-arranged node positions from an edited .drawio into its layout file."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from layout_overlay import harvest
if len(sys.argv) != 2:
    print("usage: python3 harvest_layout.py <venture>-(aom|ctm)-at-C<N>.drawio"); sys.exit(1)
lp, n, stale = harvest(sys.argv[1])
print(f"harvested {n} node positions → {lp.name}" + (f" · {len(stale)} stale entries kept" if stale else ""))
