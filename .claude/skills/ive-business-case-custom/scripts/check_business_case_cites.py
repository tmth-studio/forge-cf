#!/usr/bin/env python3
"""Check that a business case document cites the evidence workbook for every figure.

    python3 check_business_case_cites.py <business-case.html> <evidence-cells.md>

Two checks, per business-case-standard.md section 3:
  1. every <span class="cite">name</span> names a cell that exists in the cell index
  2. every paragraph, list item or table cell that carries a money or percentage figure
     carries at least one cite
Exit 0 when clean. Prints each defect with the text around it.
"""

import html
import re
import sys


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    doc = open(sys.argv[1], encoding="utf-8").read()
    index = open(sys.argv[2], encoding="utf-8").read()
    names = set(re.findall(r"^\| `([a-z0-9_]+)` \|", index, flags=re.M))
    defects = []

    for m in re.finditer(r'<span class="cite">([^<]+)</span>', doc):
        if m.group(1).strip() not in names:
            defects.append(f"unknown cell name: {m.group(1).strip()}")

    # the appendix reproduces the index and is exempt
    body = re.split(r'id="appendix"', doc, maxsplit=1)[0]
    body = re.sub(r"<style.*?</style>|<script.*?</script>", "", body, flags=re.S)
    blocks = re.findall(r"<(p|li|td|dd|h[1-6])\b[^>]*>(.*?)</\1>", body, flags=re.S)
    figure = re.compile(r"(£|\$|€)\s?\d|\d[\d,]*(\.\d+)?\s?%")
    for tag, inner in blocks:
        text = html.unescape(re.sub(r"<[^>]+>", " ", inner))
        if figure.search(text) and 'class="cite"' not in inner:
            snippet = re.sub(r"\s+", " ", text).strip()
            defects.append(f"figure without a cite in <{tag}>: {snippet[:110]}")

    if defects:
        for d in defects:
            print("DEFECT  " + d)
        print(f"{len(defects)} defect(s)")
        sys.exit(1)
    print("clean — every cite resolves; every figure is cited")


if __name__ == "__main__":
    main()
