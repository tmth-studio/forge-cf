#!/usr/bin/env python3
"""Range reading: read a margin with inputs as ranges, beside the all-worst reading. Information only.

Head of R&D, 5 November 2026, RD-062. It sets no pass mark and replaces no test. Item 30 of the run verification
standard stays as it is. The purpose is to test what the band ends mean and whether they are honest, and to report the
chance of nil margin and the chance of 25%.

This reading is not a test. It moves no item. It does not stand in for a VA-171 pessimistic value. The item 28 scorer
does not see it (Head of Verification, 6 November 2026).

Nil means investors earn the cost of capital only where all four cost layers are populated, because returns sit inside
whole cost (registry line 32). Otherwise the label is "nil on the lines built so far; indicative only".

The script reads the two kinds of saved file that hold a cost and a value: a business case model and a fit model. Any
other saved file prints n/a with a reason and exits 0, so a run can call it at any challenge.

Use, on any fin-sim model file:
    python3 range_reading.py <model.yaml> [--side side.yaml] [--n 4000] [--json out.json]
    python3 range_reading.py --selftest
Use from another script, for a run with its own margin function: build a Case and call read_case(case).

The optional side file holds what the model file cannot say:
    groups:        {shared cause name: [input, input]}     inputs that move together (VA-171)
    same_input:    [[input, input]]                        two fields that are one input
    volume_keys:   [input]                                 inputs that set volume (default: the market inputs)
    volume_tied:   {input: {ref_vol, low_vol, high_at_ref, high_at_low_vol}}
                   an input whose high end was set at another volume. The band's high end becomes the value at ref_vol,
                   and the amount moves with sampled volume, as a + b / volume through the two points.
    bands:         {input: {low, high}}                    an override with a stated reason in the record

What it prints:
    central; all-worst (every input at its worst end, volume included); the definition reading (the same, volume at
    central); the share of the way from central to all-worst the design can bear and still read 25% and nil;
    all-worst with every harmful swing halved; the distribution under two meanings of a band end and three
    dependence cases; the place of the all-worst case in that distribution; whole cost at all-worst against central
    and against the 1-in-10 high; each band against its VA-169 class band; the harmful-end check (VA-183): whether the
    ends stated in the file give the lowest reading, or whether another end does in this reading.

Two meanings of a band end are read because the record does not say which the builder meant:
    limit       the end is the furthest the input can go (triangular on low, central, high)
    one_in_ten  the end is a 1-in-10 value and the input can pass it (split normal, the convention of VA-171)
Three dependence cases: independent; shared (0.3 between groups, 1 inside a group, the VA-171 default); together (one
draw for every input). Mapping of tiers to VA-169 classes is an assumption, stated in CLASS_OF_TIER.
"""
import argparse, importlib.util, json, math, pathlib, re, statistics
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
Z90 = 1.2815515655446004
SHAPES = ("limit", "one_in_ten")
MODES = ("independent", "shared", "together")
RHO_SHARED = 0.3
OVERRUN = 1.62   # Built to Hold p. 7, average cost overrun for complex engineering projects, Flyvbjerg and Gardner 2023
CLASS_BAND = {"E5": (1.0, 0.5), "E4": (0.5, 0.3), "E3": (0.3, 0.2), "E2": (0.2, 0.15), "E1": (0.15, 0.1)}  # VA-169: up, down
CLASS_OF_TIER = {"T1": "E1", "T2": "E2", "T3": "E3", "T4": "E5", "A": "E5"}   # assumption: T4 or A is an assumed figure
SKIP_SOURCE = re.compile(r"by construction|by definition|\bFACT\b", re.I)


class Case:
    """inputs: {name: {low, central, high, adverse, tier, source}}. fn(values) returns {margin, cost} and may add fit."""

    def __init__(self, name, inputs, fn, groups=None, same=None, volume_keys=None, worst_override=None, base=None, note=""):
        self.name, self.inputs, self.fn = name, inputs, fn
        self.groups, self.same = groups or {}, same or []
        self.volume_keys = list(volume_keys or [])
        self.worst_override = worst_override
        self.base = base or {k: b["central"] for k, b in inputs.items()}
        self.note = note

    def harm(self, k):
        b = self.inputs[k]
        return b["high"] if b["adverse"] == "high" else b["low"]

    def other(self, k):
        b = self.inputs[k]
        return b["low"] if b["adverse"] == "high" else b["high"]

    def central(self):
        return dict(self.base)

    def all_worst(self):
        v = dict(self.base)
        for k in self.inputs:
            v[k] = self.harm(k)
        if self.worst_override:
            v.update(self.worst_override)
        return v


def _tri(o, c, h, q):
    """Inverse triangular, q is the chance towards the harmful end h."""
    if h == o:
        return c
    a, b = (o, h) if o < h else (h, o)
    q2 = q if o < h else 1 - q
    cut = (c - a) / (b - a)
    return a + math.sqrt(q2 * (b - a) * (c - a)) if q2 < cut else b - math.sqrt((1 - q2) * (b - a) * (b - c))


def _split(o, c, h, z):
    """Split normal with each end at its 1-in-10 point."""
    return c + z / Z90 * (h - c) if z >= 0 else c + (-z) / Z90 * (o - c)


def _clusters(case):
    """Each cluster is a list of inputs that take one draw whatever the dependence case: the same input."""
    seen, out = set(), []
    for lst in case.same:
        lst = [k for k in lst if k in case.inputs and k not in seen]
        if lst:
            out.append(lst)
            seen.update(lst)
    for k in case.inputs:
        if k not in seen:
            out.append([k])
    return out


def _bounded(case, k, x):
    b = case.inputs[k]
    if min(b["low"], b["central"]) >= 0:
        x = max(x, 0.1 * b["low"])       # a positive input stays positive: a draw cannot pass a tenth of its low end
        if b.get("kind") != "z" and max(b["high"], b["central"]) <= 1:
            x = min(x, 1.0)
    return x


NORMAL = statistics.NormalDist()


def draw_values(case, shape, mode, rng):
    common = rng.standard_normal()
    gz = {g: rng.standard_normal() for g in case.groups}
    member = {k: g for g, lst in case.groups.items() for k in lst}
    v = dict(case.base)
    for cl in _clusters(case):
        e = rng.standard_normal()
        g = next((member[k] for k in cl if k in member), None)
        if mode == "independent":
            z = e
        elif mode == "together":
            z = common
        else:
            own = gz[g] if g else e
            z = math.sqrt(RHO_SHARED) * common + math.sqrt(1 - RHO_SHARED) * own
        for k in cl:
            o, c, h = case.other(k), case.inputs[k]["central"], case.harm(k)
            if shape == "limit":
                v[k] = _tri(o, c, h, min(max(NORMAL.cdf(z), 1e-9), 1 - 1e-9))
            else:
                v[k] = _bounded(case, k, _split(o, c, h, z))
    return v


def _at(case, s):
    """Every input s of the way from central to its harmful end."""
    w, c = case.all_worst(), case.central()
    v = dict(c)
    for k in case.inputs:
        v[k] = c[k] + s * (w[k] - c[k])
    return v


def bearable(case, bar):
    """Share of the way from central to all-worst at which the margin first falls to the bar. None: under it at central."""
    if case.fn(_at(case, 0.0))["margin"] < bar:
        return None
    if case.fn(_at(case, 1.0))["margin"] >= bar:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if case.fn(_at(case, mid))["margin"] >= bar:
            lo = mid
        else:
            hi = mid
    return lo


def distribution(case, shape, mode, n, seed, worst_margin):
    rng = np.random.default_rng(seed)
    ms, cs = [], []
    for _ in range(n):
        r = case.fn(draw_values(case, shape, mode, rng))
        ms.append(float(r["margin"]))
        cs.append(float(r["cost"]))
    ms, cs = np.array(ms), np.array(cs)
    return dict(median=float(np.median(ms)), bad_1_in_5=float(np.percentile(ms, 20)), chance_nil=float((ms >= 0).mean()),
                chance_25=float((ms >= 0.25).mean()), share_at_or_below_all_worst=float((ms <= worst_margin + 1e-12).mean()),
                cost_1_in_10_high=float(np.percentile(cs, 90)), cost_median=float(np.median(cs)))


def class_of(band):
    t = str(band.get("tier") if band.get("tier") is not None else "").strip()
    if t.isdigit():
        t = "T" + t
    m = re.search(r"E[1-5]", t)
    if m:
        return m.group(0)
    m = re.search(r"T[1-4]", t)
    if m:
        return CLASS_OF_TIER[m.group(0)]
    return CLASS_OF_TIER.get(t.strip())


def class_case(case, relevant):
    """Harmful end moved out to the class band wherever the builder's is narrower. Wider bands stay. Returns case, rows."""
    inputs, rows = {}, []
    for k, b in case.inputs.items():
        b2 = dict(b)
        cl, c = class_of(b), b["central"]
        if cl and c and k in relevant and not SKIP_SOURCE.search(str(b.get("source", ""))):
            up, down = CLASS_BAND[cl]
            target = c * (1 + up) if b["adverse"] == "high" else c * (1 - down)
            builder = abs(case.harm(k) - c) / abs(c)
            cls = abs(target - c) / abs(c)
            rows.append(dict(input=k, cls=cl, builder_swing=builder, class_swing=cls, narrower=builder < cls - 1e-9))
            if builder < cls - 1e-9:
                b2["high" if b["adverse"] == "high" else "low"] = target
        inputs[k] = b2
    new = Case(case.name + " at class bands", inputs, case.fn, case.groups, case.same, case.volume_keys, None, case.base)
    return new, rows


def relevant_inputs(case, central_margin):
    out, swing = set(), []
    for k in case.inputs:
        v = case.central()
        v[k] = case.harm(k)
        m = float(case.fn(v)["margin"])
        if abs(m - central_margin) > 1e-9:
            out.add(k)
        swing.append((abs(m - central_margin), k))
    swing.sort(reverse=True)
    return out, [k for _, k in swing[:3]]


def lowest_reading(case, key="margin", limit=14):
    """VA-183: is each declared harmful end the harmful end in this reading? Search the range ends, one-value inputs held together.
    A margin that is one line divided by another, each straight in the input, is lowest at a range end. A step or a ramp can be lowest inside the range, so one input at a time is also tried inside it."""
    fixed = set(case.worst_override or {})
    free = [cl for cl in _clusters(case) if not fixed.intersection(cl)]
    start = case.all_worst()
    read = lambda v: float(case.fn(v)[key])

    def place(v, cl, s):
        """s = 0 is the declared harmful end, s = 1 the other end."""
        for k in cl:
            v[k] = case.harm(k) + s * (case.other(k) - case.harm(k))

    declared, best, flips = read(start), read(start), []
    if len(free) <= limit:
        method = "every combination of range ends"
        for mask in range(1 << len(free)):
            v = dict(start)
            for i, cl in enumerate(free):
                if mask >> i & 1:
                    place(v, cl, 1.0)
            m = read(v)
            if m < best - 1e-12:
                best, flips = m, [cl for i, cl in enumerate(free) if mask >> i & 1]
    else:
        method = f"one input at a time from all-worst, {len(free)} inputs, so a lower combination can be missed"
        moved = True
        while moved:
            moved = False
            for cl in free:
                v = dict(start)
                for fl in flips:
                    place(v, fl, 1.0)
                if cl in flips:
                    place(v, cl, 0.0)
                else:
                    place(v, cl, 1.0)
                m = read(v)
                if m < best - 1e-12:
                    best, moved = m, True
                    flips = [fl for fl in flips if fl != cl] if cl in flips else flips + [cl]
    at = dict(start)
    for fl in flips:
        place(at, fl, 1.0)
    inside = []
    for cl in free:
        for s in (0.25, 0.5, 0.75):
            v = dict(at)
            place(v, cl, s)
            if read(v) < best - 1e-9:
                inside.append(cl[0])
                break
    return dict(declared=declared, lowest=best, method=method, ends_that_differ=[k for cl in flips for k in cl], lower_inside_the_range=inside)


def read_case(case, n=4000, seed=20261105):
    c, w = case.fn(case.central()), case.fn(case.all_worst())
    d = case.all_worst()
    for k in case.volume_keys:
        d[k] = case.central()[k]
    dr = case.fn(d)
    half = case.fn(_at(case, 0.5))
    wm = float(w["margin"])
    rel, top3 = relevant_inputs(case, float(c["margin"]))
    res = dict(name=case.name, note=case.note, nil_label=getattr(case, "nil_label", NIL_PARTIAL), unbuilt=getattr(case, "unbuilt", []),
               not_applicable=getattr(case, "not_applicable", []), inputs_with_a_band=len(case.inputs), inputs_that_move_the_margin=len(rel),
               largest_three_single_swings=top3, central=float(c["margin"]), item30=wm, definition=float(dr["margin"]),
               volume_difference=float(dr["margin"]) - wm, half_swings=float(half["margin"]),
               bearable_25=bearable(case, 0.25), bearable_nil=bearable(case, 0.0),
               cost_central=float(c["cost"]), cost_all_worst=float(w["cost"]),
               cost_ratio=float(w["cost"]) / float(c["cost"]), reference_overrun=OVERRUN)
    if "fit" in c:
        res.update(fit_central=float(c["fit"]), fit_item30=float(w["fit"]), fit_definition=float(dr["fit"]))
    res["harmful_end_check"] = {}
    for key in ("margin", "fit") if "fit" in c else ("margin",):
        try:
            res["harmful_end_check"][key] = lowest_reading(case, key)
        except (ZeroDivisionError, ValueError, KeyError) as e:
            res["harmful_end_check"][key] = f"the search could not read every end ({type(e).__name__}: {e})"
    res["readings"] = {s: {m: distribution(case, s, m, n, seed, wm) for m in MODES} for s in SHAPES}
    for s in SHAPES:
        for m in MODES:
            res["readings"][s][m]["all_worst_cost_over_1_in_10_high"] = float(w["cost"]) / res["readings"][s][m]["cost_1_in_10_high"]
    cc, rows = class_case(case, rel)
    res["class_rows"] = rows
    res["class_compared"] = len(rows)
    res["class_narrower"] = sum(r["narrower"] for r in rows)
    res["class_narrower_inputs"] = [r["input"] for r in rows if r["narrower"]]
    if rows:
        cw = cc.fn(cc.all_worst())
        res["class_all_worst"] = float(cw["margin"])
        res["class_shared_limit"] = distribution(cc, "limit", "shared", n, seed, float(cw["margin"]))
    return res


def _gbx():
    spec = importlib.util.spec_from_file_location("gbx", GBX_PATH)
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def _find_gbx():
    """Beside this script once landed. From the held folder, the live copy in the skill folder."""
    near = HERE / "generate_business_case_xlsx.py"
    if near.exists():
        return near
    for up in HERE.parents:
        c = up / ".claude/skills/ive-fin-sim-custom/scripts/generate_business_case_xlsx.py"
        if c.exists():
            return c
    return near


GBX_PATH = _find_gbx()
NIL_FULL = "investors earn the cost of capital"
NIL_PARTIAL = "nil on the lines built so far; indicative only"
SELLING = re.compile(r"sell|sales|market|acqui|commission|partner|channel|distribut", re.I)
COST_LAYERS = ("pvc", "rc", "sc", "ic")


def _names_in(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("name", "role") and isinstance(v, str):
                yield v
            else:
                yield from _names_in(v)
    elif isinstance(x, list):
        for v in x:
            yield from _names_in(v)


def business_layers_missing(m, r):
    """Which layers a business case model does not show. A name search for selling, so a miss gives the weaker label."""
    missing = []
    if not any(SELLING.search(n) for n in _names_in([m.get("hr"), m.get("running")])):
        missing.append("sc (no selling line found by name)")
    if r["returns_unit"] + r["returns_ho"] <= 0:
        missing.append("ic (no capital line)")
    return missing


def case_from_fit(m, name="model"):
    """A Case from a fit model, using the same arithmetic as the fit check: ceiling = kmc x share; floor = sum of layers.
    The file holds band ends and no central, so central is the mid point of each band, an assumption stated in the note."""
    pc, layers = m["price_ceiling"], m["cost_floor"]["layers"]
    points, inputs, unbuilt, not_applicable = {}, {}, [], []
    for key in COST_LAYERS:
        d = layers.get(key)
        if not isinstance(d, dict) or "not_designed_until" in d:
            unbuilt.append(key)
        elif "not_applicable" in d:
            not_applicable.append(key)
        elif "amount" in d:
            points[key] = float(d["amount"])
        else:
            lo, hi = float(d["band"]["low"]), float(d["band"]["high"])
            if lo == hi:
                points[key] = lo
            else:
                inputs[key] = dict(low=lo, central=(lo + hi) / 2, high=hi, adverse="high", tier=d.get("tier", ""), source=d.get("source", ""))
    kmc = pc["kmc"]
    if "band" in kmc:
        lo, hi = float(kmc["band"]["low"]), float(kmc["band"]["high"])
        inputs["kmc"] = dict(low=lo, central=(lo + hi) / 2, high=hi, adverse="low", tier=kmc.get("tier", ""), source=kmc.get("source", ""))
    else:
        points["kmc"] = float(kmc["amount"])
    share = pc.get("customer_surplus_fraction", m.get("customer_surplus_fraction"))
    points["share"] = float(share["value"] if isinstance(share, dict) else share)

    def fn(v):
        vals = dict(points)
        vals.update(v)
        cost = sum(vals[k] for k in COST_LAYERS if k in vals)
        return dict(margin=vals["kmc"] * vals["share"] / cost - 1, cost=cost)

    case = Case(name, inputs, fn, note="fit model; central is the mid point of each band (assumption); volume is the file's own, so the all-worst figure on this file is not volume included")
    case.nil_label = NIL_PARTIAL if unbuilt else NIL_FULL
    case.unbuilt = unbuilt
    case.not_applicable = not_applicable
    return case


def case_from_model(m, side=None, name="model"):
    """A Case from any fin-sim model. Margin is the business margin, price against whole cost."""
    side, gbx = side or {}, _gbx()
    raw = gbx.collect_inputs(m)
    base = {k: b["value"] for k, b in raw.items()}
    inputs = {}
    for k, b in raw.items():
        if b.get("adverse") in ("high", "low") and b["low"] != b["high"]:
            inputs[k] = dict(low=min(b["low"], b["value"]), central=b["value"], high=max(b["high"], b["value"]),
                             adverse=b["adverse"], tier=b.get("tier", ""), source=b.get("source", ""))
    for k in inputs:                 # price is set by the design: it can fall short of the set figure, it cannot be drawn above it
        if re.fullmatch(r"product\.\d+\.price", k):
            inputs[k]["high"] = inputs[k]["central"]
    for k, o in (side.get("bands") or {}).items():
        inputs[k].update(o)
    curve = {}
    for k, t in (side.get("volume_tied") or {}).items():
        inputs[k]["high"] = max(t["high_at_ref"], inputs[k]["central"])
        hr, hl = inputs[k]["high"], t["high_at_low_vol"]
        bb = (hl - hr) / (1 / t["low_vol"] - 1 / t["ref_vol"])
        curve[k] = (hr - bb / t["ref_vol"], bb, hr)

    def fn(values):
        vals = dict(base)
        vals.update(values)
        r = gbx.compute(m, vals)
        vol = r["trans"] * r["units"] * 12
        if curve:
            for k, (a, b, hr) in curve.items():
                vals[k] = vals[k] * max(a + b / vol, 0.05 * hr) / hr
            r = gbx.compute(m, vals)
        return dict(margin=r["fmos"], cost=r["cost_per_trans"], volume=vol)

    same = list(side.get("same_input") or [])
    mk = [k for k in inputs if k.startswith("market.")]
    for i, a in enumerate(mk):       # two market fields whose bands stay in one ratio at all three points are one input
        for b in mk[i + 1:]:
            A, B = inputs[a], inputs[b]
            if B["central"] and B["low"] and B["high"] and A["low"]:
                r = [A["central"] / B["central"], A["low"] / B["low"], A["high"] / B["high"]]
                if max(r) - min(r) < 0.01 * r[0]:
                    same.append([a, b])
    volume_keys = side.get("volume_keys") or [k for k in mk if not k.endswith("transactions_per_customer_per_month")]
    case = Case(name, inputs, fn, side.get("groups"), same, volume_keys, base=base)
    vals = dict(base)
    missing = [] if side.get("all_four_layers") else business_layers_missing(m, gbx.compute(m, vals))
    case.nil_label = NIL_PARTIAL if missing else NIL_FULL
    case.unbuilt = missing
    case.not_applicable = []
    return case


def scan_volume_tied(m):
    """Names band sources that say a figure was set at a stated volume. A prompt to look, not a finding."""
    gbx, out = _gbx(), []
    for k, b in gbx.collect_inputs(m).items():
        if re.search(r"\b(at|over)\s+[\d,]+\s+(functions?|sites?|members?|jobs?|customers?|units?)\b", str(b.get("source", ""))):
            out.append(k)
    return out


def selftest():
    """Checks on a toy margin with a known answer."""
    inputs = {"a": dict(low=8.0, central=10.0, high=14.0, adverse="high"), "b": dict(low=4.0, central=5.0, high=9.0, adverse="high"),
              "p": dict(low=20.0, central=30.0, high=40.0, adverse="low")}
    fn = lambda v: dict(margin=v["p"] / (v["a"] + v["b"]) - 1, cost=v["a"] + v["b"])
    case = Case("toy", inputs, fn, volume_keys=["a"])
    r = read_case(case, n=4000)
    r2 = read_case(case, n=4000)
    assert abs(r["central"] - 1.0) < 1e-12, "central must reproduce"
    assert abs(r["item30"] - (20 / 23 - 1)) < 1e-12, "all-worst must reproduce"
    assert abs(r["definition"] - (20 / 19 - 1)) < 1e-12, "definition holds the volume input at central"
    assert r == r2, "the same seed must give the same reading"
    rng = np.random.default_rng(1)
    t = [_tri(8.0, 10.0, 14.0, q) for q in rng.random(100000)]
    assert abs(sum(t) / len(t) - 32 / 3) < 0.03, "triangular mean"
    assert r["readings"]["limit"]["together"]["share_at_or_below_all_worst"] < 0.001, "together, limit: all-worst is the far end"
    z = [_split(8.0, 10.0, 14.0, x) for x in rng.standard_normal(100000)]
    assert abs(sum(x >= 14.0 for x in z) / len(z) - 0.1) < 0.005, "one-in-ten end is passed one time in ten"
    fit = dict(cost_floor=dict(layers=dict(pvc=dict(band=dict(low=10.0, high=20.0)), rc=dict(amount=5.0), sc=dict(not_designed_until="C3"), ic=dict(not_applicable="none"))),
               price_ceiling=dict(kmc=dict(band=dict(low=60.0, high=100.0)), customer_surplus_fraction=dict(value=0.5)))
    fc = case_from_fit(fit, "fit toy")
    fr = read_case(fc, n=500)
    assert abs(fr["item30"] - (60 * 0.5 / 25 - 1)) < 1e-12, "fit reading: low value x share over high cost"
    assert fr["nil_label"] == NIL_PARTIAL and fr["unbuilt"] == ["sc"], "an unbuilt layer gives the weaker label"
    fit["cost_floor"]["layers"]["sc"] = dict(amount=1.0)
    assert read_case(case_from_fit(fit, "fit toy"), n=200)["nil_label"] == NIL_FULL, "a not applicable layer counts as populated"
    # VA-183. Reading = (W + u Q) / (R + p Q). Q is the volume input; W is the rest's money.
    pct = lambda W, u: (lambda v: dict(margin=(v.get("W", W) + u * v["q"]) / (1000.0 + 100.0 * v["q"]), cost=1.0))
    vol = lambda a: {"q": dict(low=1.0, central=10.0, high=20.0, adverse=a)}
    h = lowest_reading(Case("unit earns money, under the rest", vol("low"), pct(400.0, 10.0)))
    assert h["ends_that_differ"] == ["q"] and abs(h["lowest"] - (400 + 200) / 3000) < 1e-12, "unit earns 10 per cent, rest 40: high volume is harmful"
    assert lowest_reading(Case("same, stated right", vol("high"), pct(400.0, 10.0)))["ends_that_differ"] == [], "a right end is not flagged"
    h = lowest_reading(Case("unit loses money, rest loses more", vol("high"), pct(-500.0, -5.0)))
    assert h["ends_that_differ"] == ["q"], "unit loses money, rest loses 50 per cent: low volume is harmful"
    h = lowest_reading(Case("pass-through, rest loses", vol("high"), pct(-100.0, 0.0)))
    assert h["ends_that_differ"] == ["q"], "pass-through, rest loses 10 per cent: low volume is harmful"
    two = dict(vol("low"), W=dict(low=-500.0, central=100.0, high=400.0, adverse="low"))
    assert abs(lowest_reading(Case("one flips with another", two, pct(0.0, 10.0)))["lowest"] - (-500 + 10) / 1100) < 1e-12, "the harmful end of one input moves with another"
    held = {"a": dict(low=1.0, central=2.0, high=3.0, adverse="high"), "b": dict(low=1.0, central=2.0, high=3.0, adverse="high")}
    held_fn = lambda v: dict(margin=v["b"] - v["a"], cost=1.0)
    assert lowest_reading(Case("one fact", held, held_fn, same=[["a", "b"]]))["lowest"] == 0.0, "one value for one fact stays held"
    assert lowest_reading(Case("two facts", held, held_fn))["lowest"] == -2.0, "unheld, the search finds the split"
    step = lambda v: dict(margin=(100.0 * v["q"] - 60.0 * v["q"] - (300.0 if v["q"] > 10 else 0.0)) / (100.0 * v["q"]), cost=1.0)
    assert lowest_reading(Case("step cost", vol("low"), step))["lower_inside_the_range"] == ["q"], "a step cost can be lowest inside the range"
    many = {f"i{n}": dict(low=1.0, central=2.0, high=3.0, adverse="high") for n in range(16)}
    many_fn = lambda v: dict(margin=-sum(v.values()), cost=1.0)
    assert "one input at a time" in lowest_reading(Case("many", many, many_fn))["method"], "many inputs: the print says the search is not every combination"
    print("selftest: all checks pass")


def print_case(r):
    pc = lambda x: "n.a." if x is None else f"{x * 100:+.1f}%"
    print(f"== {r['name']}")
    print("information only: not a test; moves no item; does not stand in for a VA-171 pessimistic value; the item 28 scorer does not see it")
    print(f"nil reads: {r.get('nil_label', NIL_PARTIAL)}")
    if r.get("unbuilt"):
        print(f"lines not built or not found: {r['unbuilt']}")
    if r.get("not_applicable"):
        print(f"layers marked not applicable: {r['not_applicable']}")
    if r.get("note"):
        print(f"note: {r['note']}")
    print(f"central {pc(r['central'])}  all-worst {pc(r['item30'])}  definition (volume at central) {pc(r['definition'])}  half swings {pc(r['half_swings'])}")
    print(f"share of the way to all-worst it can bear: to 25% {pc(r['bearable_25'])}  to nil {pc(r['bearable_nil'])}")
    print(f"whole cost all-worst / central {r['cost_ratio']:.2f} (reference average overrun {OVERRUN})  largest single swings {r['largest_three_single_swings']}")
    for key, h in r.get("harmful_end_check", {}).items():
        if isinstance(h, str):
            print(f"harmful ends ({key}): n/a: {h}")
            continue
        print(f"harmful ends ({key}, VA-183): stated ends read {pc(h['declared'])}; lowest found {pc(h['lowest'])}, by {h['method']}")
        if h["ends_that_differ"]:
            print(f"  check each, the lowest found is not yet a reading: the stated end is wrong in this reading, or the input is tied to another and the two must be held together (side file, same_input): {h['ends_that_differ']}")
        if h["lower_inside_the_range"]:
            print(f"  lower still inside the range, so range ends are not enough for: {h['lower_inside_the_range']}")
    for s in SHAPES:
        for m in MODES:
            d = r["readings"][s][m]
            print(f"  {s:<10} {m:<11} median {pc(d['median'])}  bad 1-in-5 {pc(d['bad_1_in_5'])}  chance nil {d['chance_nil']:.0%}  chance 25% {d['chance_25']:.0%}"
                  f"  draws at or below all-worst {d['share_at_or_below_all_worst']:.2%}  all-worst cost / 1-in-10 high {d['all_worst_cost_over_1_in_10_high']:.2f}")
    if r["class_compared"]:
        print(f"class bands: {r['class_narrower']} of {r['class_compared']} compared are narrower than the VA-169 default; all-worst there {pc(r['class_all_worst'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model", nargs="?")
    ap.add_argument("--side")
    ap.add_argument("--n", type=int, default=4000)
    ap.add_argument("--json")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.model:
        ap.error("name a model file, or use --selftest")
    import yaml
    stem = pathlib.Path(a.model).stem
    try:
        m = yaml.safe_load(open(a.model))
        side = yaml.safe_load(open(a.side)) if a.side else {}
        if not isinstance(m, dict):
            raise ValueError("the file holds no model")
        if "cost_floor" in m and "price_ceiling" in m:
            case, tied = case_from_fit(m, name=stem), []
        elif "market" in m and "hr" in m:
            case = case_from_model(m, side, name=stem)
            tied = scan_volume_tied(m)
        else:
            print(f"range reading: n/a for {stem}: this file holds no cost and value bands (it is not a fit model or a business case model). Read it on the fit model at this challenge.")
            return
        if not case.inputs:
            print(f"range reading: n/a for {stem}: no input in this file has a band.")
            return
        r = read_case(case, n=a.n)
    except Exception as e:
        print(f"range reading: n/a for {stem}: the file could not be read as a model ({type(e).__name__}: {e}).")
        return
    r["bands_set_at_a_stated_volume_look_at_these"] = tied
    print_case(r)
    print("band sources naming a volume, check each:", tied)
    if a.json:
        json.dump(r, open(a.json, "w"), indent=1)


if __name__ == "__main__":
    main()
