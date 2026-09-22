#!/usr/bin/env python3
"""Compute the financial margin of safety, and refuse inputs it cannot check.

Landed 10 September 2026 on Tom's ruling, from the finding
`Forge/WS1/scorer-tiers-applied-to-ive-2026-09-10.md`.

WHY THIS EXISTS. The margin of safety is the number the capital decision turns
on. Until today it was produced by a language model adding four figures a person
read out, and dividing. The relation was tier 2 and the scorer was tier 4.

WHAT IT DOES NOT DO, STATED FIRST. This script checks that the inputs are
declared, dimensioned, sourced, scale-consistent and arithmetically consistent,
and it does the arithmetic itself. It cannot check that any figure is TRUE of
the world. An empty model of the right shape passes every check here. A PASS
means the gate was computed, not that the venture is viable.

WHERE THE INPUTS COME FROM. That was the open half of the escalation and it is
settled here: from a fit model file, not from the run's own prose. Every figure
in that file states an amount, a unit, a period, a scale state and a source, and
a cost layer states whether it is derived from activities or asserted. A figure
an identity produces may not also be stored (VA-91); where it is, it must
reproduce. The file names the operating model and the customer model it draws
from, and those files must exist.

16 September 2026 — three rule changes landed by the Head of R&D from the
candidates of 14 September 2026:
  (a) A ceiling or floor figure below evidence tier 1 is a band, not a point.
      Every figure (each cost layer and the key cost) may carry
      `tier: T1 | T2 | T3 | T4`. A figure with no `tier` is read at T4, the
      strictest reading, and the message says so. At T2 to T4 the figure must
      be stated as `band: {low: ..., high: ...}`; a single `amount` is refused.
      At T1 a single `amount` is allowed. A band is carried into the
      arithmetic: the floor and the ceiling become bands, the margin is stated
      at the worst corner (ceiling low against floor high) and at the best
      corner, and the verdict is taken at the worst corner. A stored headline
      `amount` on a block whose inputs form a band is refused (VA-91).
      Fixture decision: the regression fixture in test_fit_margin.py carried
      five figures with no tier. There is one fixture, so choice (i) was
      taken: `tier: T1` was added to each of the five with a comment, and no
      grace period was introduced. A model file in the vault that states no
      tier now refuses until its generator writes one.
  (b) RB-V-025 — a bar that reads its own ceiling is an indicator, not a bar.
      An optional top-level `required_price` block states the bar in
      fixed-number form: (operating cost + required profit) ÷ units. It may
      carry `derived_from: [...]` (a list of the keys it is built from) and
      `formula: "..."`. If either names the ceiling — `price_ceiling`,
      `ceiling` or `kmc` — the file is refused. A bar is one number; it does
      not carry a band. The bar is reported and compared with the ceiling;
      it does not change the gate verdict.
  (c) VA-99 grace — the header date must not lag the edit history. The header
      `date` (or `updated` / `last_updated`) is compared with the file's
      modification time on disk. A header date names a whole day, so the 24
      hours are counted from the end of that day. A file modified more than
      24 hours after that produces a WARNING naming both dates. The exit code
      is unchanged; a warning is not a refusal.

Usage:
    python3 fit_margin.py <venture>-fit-model-at-C<N>.yaml
    python3 fit_margin.py --template > my-fit-model.yaml

Exit 0 PASS, 1 BORDERLINE or FAIL, 2 REFUSED (the model could not be checked).
"""
import datetime
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("REFUSED: PyYAML is not installed.")
    sys.exit(2)

VERSION = "1.1.0 (16 September 2026)"
CANONICAL_DIR = ".claude/skills/shared/generators"
COST_LAYERS = ["pvc", "rc", "sc", "ic"]
TIERS = ("T1", "T2", "T3", "T4")
MISSING_TIER = "T4"          # (a): no `tier` stated is read at the strictest tier
CEILING_KEYS = ("price_ceiling", "ceiling", "kmc")   # (b): what a bar may not read
HEADER_DATE_KEYS = ("date", "updated", "last_updated")   # (c)
HEADER_GRACE = datetime.timedelta(hours=24)              # (c)
LAYER_NAMES = {
    "pvc": "product variable cost",
    "rc": "running cost",
    "sc": "scaling cost",
    "ic": "infrastructure cost",
}
# Single source of truth for the bands: Forge/WS1/criteria-registry.md.
# Restated here because a script cannot read prose. If these ever disagree with
# the registry, the registry wins and this constant is the defect.
GATES = {
    "per_requirement": [(0.25, "PASS"), (0.15, "BORDERLINE"), (None, "FAIL")],
    "phase_ii": [(0.60, "PASS"), (0.25, "BORDERLINE"), (None, "FAIL")],
}
TOLERANCE = 0.005  # half a per cent, for reproducing a stored figure


class Refusal(Exception):
    pass


def announce_origin(model_path=None):
    """Refuse to run from a fork, and refuse if the toolchain fails its manifest."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import toolchain_guard
    except ImportError:
        raise Refusal("toolchain_guard.py is not beside this script. A checker "
                      "that cannot verify its own origin does not run.")
    try:
        toolchain_guard.require_canonical(model_path)
    except Exception as exc:
        raise Refusal(str(exc))


def need(block, key, where):
    if not isinstance(block, dict) or key not in block:
        raise Refusal("%s has no `%s`" % (where, key))
    return block[key]


def number(block, key, where):
    v = need(block, key, where)
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise Refusal("%s.%s is `%r`, which is not a number" % (where, key, v))
    return float(v)


def read_tier(fig, where):
    """(a) Return (tier, stated). A missing tier is read at MISSING_TIER."""
    if not isinstance(fig, dict) or "tier" not in fig or fig["tier"] is None:
        return MISSING_TIER, False
    tier = str(fig["tier"]).strip().upper()
    if tier not in TIERS:
        raise Refusal("%s.tier is `%s`; the evidence tiers are %s"
                      % (where, fig["tier"], ", ".join(TIERS)))
    return tier, True


def read_value(fig, where, comparisons, tiered=True, allow_band=True):
    """Return (low, high). A point gives low == high.

    (a) A figure states either `amount` (one number) or `band: {low, high}`.
    Where the figure's evidence tier is below T1, only a band is accepted.
    """
    has_point = isinstance(fig, dict) and "amount" in fig
    has_band = isinstance(fig, dict) and "band" in fig
    if has_point and has_band:
        raise Refusal("%s states both `amount` and `band`. State one." % where)
    if not has_point and not has_band:
        raise Refusal("%s has no `amount` and no `band`" % where)

    if tiered:
        tier, stated = read_tier(fig, where)
        comparisons.append("%s evidence tier vs its form (point or band)" % where)
        if has_point and tier != "T1":
            if stated:
                tier_text = "tier %s" % tier
            else:
                tier_text = ("tier %s (no `tier` is stated, so the strictest "
                             "reading applies)" % tier)
            raise Refusal(
                "%s is a single number (`amount`) at evidence %s. A value below "
                "tier 1 is a band, not a point. State it as `band: {low: ..., "
                "high: ...}`, or raise the evidence to tier 1 and state `tier: T1`."
                % (where, tier_text)
            )

    if has_point:
        v = number(fig, "amount", where)
        return v, v

    if not allow_band:
        raise Refusal("%s is stated as a band. A bar is one number in "
                      "fixed-number form; state `amount`." % where)
    band = fig["band"]
    low = number(band, "low", where + ".band")
    high = number(band, "high", where + ".band")
    comparisons.append("%s band low is not above band high" % where)
    if low > high:
        raise Refusal("%s.band has low %.4f above high %.4f" % (where, low, high))
    return low, high


def check_figure(fig, where, bounding, comparisons, tiered=True, allow_band=True):
    """A figure declares an amount (or a band), a unit, a period, a scale state
    and a source. Returns (low, high); a point gives low == high."""
    low, high = read_value(fig, where, comparisons, tiered, allow_band)

    unit = need(fig, "unit", where)
    expected = "%s per %s" % (bounding["currency"], bounding["unit"])
    comparisons.append("%s unit vs bounding unit" % where)
    if str(unit).strip().lower() != expected.lower():
        raise Refusal(
            "%s carries the unit `%s`. Every per-unit figure in this file must "
            "be `%s`. A multiplication across two different units is the fault "
            "class that put a price ceiling out by about seven times on "
            "7 September 2026." % (where, unit, expected)
        )

    period = need(fig, "period", where)
    comparisons.append("%s period vs bounding period" % where)
    if str(period).strip().lower() != str(bounding["period"]).strip().lower():
        raise Refusal("%s is per `%s`; the file is bounded per `%s`"
                      % (where, period, bounding["period"]))

    scale = need(fig, "scale_state", where)
    comparisons.append("%s scale state vs bounding scale state" % where)
    if str(scale).strip().lower() != str(bounding["scale_state"]).strip().lower():
        raise Refusal(
            "%s is stated at scale state `%s` while the file is bounded at "
            "`%s`. RD-017: a per-unit figure names the scale state of its "
            "numerator and of its denominator, and they are the same state."
            % (where, scale, bounding["scale_state"])
        )

    source = need(fig, "source", where)
    if not str(source).strip():
        raise Refusal("%s has an empty `source`" % where)

    return low, high


def fmt(low, high):
    """Print a point as one number and a band as `low to high`."""
    if abs(high - low) <= 1e-12:
        return "%.4f" % low
    return "%.4f to %.4f" % (low, high)


def check_stored(block, where, low, high, identity, comparisons, notes):
    """VA-91: a stored headline figure must reproduce, and a band cannot be
    stored as a point."""
    stored = block.get("amount")
    if stored is None:
        return
    comparisons.append("%s.amount vs %s" % (where, identity))
    if abs(high - low) > 1e-12:
        raise Refusal(
            "%s.amount is a single number (%.4f) but its inputs form the band "
            "%.4f to %.4f. VA-91: do not store a figure an identity produces, "
            "and a band cannot be stored as one number."
            % (where, float(stored), low, high)
        )
    if abs(float(stored) - low) > max(TOLERANCE * abs(low), 1e-9):
        if where == "cost_floor":
            raise Refusal(
                "cost_floor.amount is %.4f and its layers sum to %.4f. VA-91: "
                "state a figure once and derive everything from it. A headline "
                "figure contradicting the arithmetic beneath it is a FAIL."
                % (float(stored), low)
            )
        raise Refusal(
            "price_ceiling.amount is %.4f but the key cost times the surplus "
            "fraction is %.4f. Do not store a number an identity produces."
            % (float(stored), low)
        )
    notes.append("stored %s.amount reproduces from %s" % (where, identity))


def load_bounding(model, comparisons):
    b = need(model, "bounding", "the model")
    for k in ("currency", "unit", "period", "scale_state"):
        if not str(b.get(k, "")).strip():
            raise Refusal("bounding.%s is missing or empty" % k)
    if str(b["scale_state"]).strip().lower() not in ("launch", "at-scale"):
        raise Refusal("bounding.scale_state must be `launch` or `at-scale`, not `%s`"
                      % b["scale_state"])
    return b


def check_source_models(model, model_path, notes):
    """The fit model names where its figures came from, and those files exist."""
    refs = need(model, "derived_from", "the model")
    for key in ("operating_model", "customer_model"):
        path = refs.get(key)
        if not path or not str(path).strip():
            raise Refusal(
                "derived_from.%s is missing. A margin of safety with no named "
                "source models is the run defining its own inputs, which is the "
                "defect this script exists to remove." % key
            )
        if str(path).strip().lower().startswith("not_applicable"):
            notes.append("derived_from.%s declared not applicable" % key)
            continue
        candidates = [path, os.path.join(os.path.dirname(os.path.abspath(model_path)), path)]
        if not any(os.path.exists(p) for p in candidates):
            raise Refusal("derived_from.%s names `%s`, which does not exist" % (key, path))
        notes.append("derived_from.%s resolves" % key)


def compute_cost_floor(model, bounding, comparisons, notes):
    block = need(model, "cost_floor", "the model")
    layers = need(block, "layers", "cost_floor")
    low_total, high_total = 0.0, 0.0
    included, excluded = [], []
    for key in COST_LAYERS:
        if key not in layers:
            raise Refusal(
                "cost_floor.layers has no `%s` (%s) and no disposition for it. "
                "A margin computed on some layers is always too optimistic and "
                "will clear a gate the full architecture fails."
                % (key, LAYER_NAMES[key])
            )
        fig = layers[key]
        where = "cost_floor.layers.%s" % key
        if isinstance(fig, dict) and ("not_designed_until" in fig or "not_applicable" in fig):
            key_used = "not_applicable" if "not_applicable" in fig else "not_designed_until"
            reason = fig[key_used]
            if reason is None or not str(reason).strip():
                raise Refusal("%s carries a disposition with no reason" % where)
            excluded.append(key)
            notes.append("%s excluded: %s" % (where, reason))
            continue
        low, high = check_figure(fig, where, bounding, comparisons)
        if high > low:
            notes.append("%s is a band %s (tier %s)"
                         % (where, fmt(low, high), read_tier(fig, where)[0]))
        basis = str(fig.get("basis", "")).strip().lower()
        if basis not in ("activity", "asserted"):
            raise Refusal("%s.basis must be `activity` or `asserted`, not `%s`"
                          % (where, fig.get("basis")))
        if basis == "asserted":
            if not str(fig.get("asserted_reason", "")).strip():
                raise Refusal(
                    "%s is asserted with no `asserted_reason`. Every cost traces "
                    "resource to activity to driver to volume; an asserted "
                    "per-unit rate with no activity behind it is a refusal, not "
                    "an opinion." % where
                )
            notes.append("%s is ASSERTED, not derived from activities: %s"
                         % (where, fig["asserted_reason"]))
        low_total += low
        high_total += high
        included.append(key)

    if not included:
        raise Refusal("every cost layer is dispositioned. There is nothing to compute.")

    check_stored(block, "cost_floor", low_total, high_total,
                 "the sum of its layers", comparisons, notes)

    return (low_total, high_total), included, excluded


def compute_price_ceiling(model, bounding, comparisons, notes):
    block = need(model, "price_ceiling", "the model")
    kmc_block = need(block, "kmc", "price_ceiling")
    kmc_low, kmc_high = check_figure(kmc_block, "price_ceiling.kmc", bounding, comparisons)
    if kmc_high > kmc_low:
        notes.append("price_ceiling.kmc is a band %s (tier %s)"
                     % (fmt(kmc_low, kmc_high), read_tier(kmc_block, "price_ceiling.kmc")[0]))
    frac_block = need(block, "customer_surplus_fraction", "price_ceiling")
    frac = number(frac_block, "value", "price_ceiling.customer_surplus_fraction")
    if not str(frac_block.get("source", "")).strip():
        raise Refusal("price_ceiling.customer_surplus_fraction has no `source`")
    comparisons.append("customer surplus fraction is between 0 and 1")
    if not 0.0 < frac < 1.0:
        raise Refusal(
            "price_ceiling.customer_surplus_fraction.value is %r. It is the share "
            "of the customer's key cost the venture may capture, so it lies "
            "strictly between 0 and 1." % frac
        )
    ceiling_low, ceiling_high = kmc_low * frac, kmc_high * frac

    check_stored(block, "price_ceiling", ceiling_low, ceiling_high,
                 "key cost times the fraction", comparisons, notes)

    return (ceiling_low, ceiling_high), (kmc_low, kmc_high), frac


def check_required_price(model, bounding, ceiling, comparisons, notes):
    """(b) RB-V-025. The bar, if stated, is in fixed-number form and does not
    read the ceiling it is tested against. Returns the bar or None."""
    block = model.get("required_price")
    if block is None:
        return None
    where = "required_price"
    if not isinstance(block, dict):
        raise Refusal("required_price is not a mapping")
    mentions = []
    derived = block.get("derived_from") if isinstance(block, dict) else None
    if derived is not None:
        if isinstance(derived, str):
            derived = [derived]
        if not isinstance(derived, list):
            raise Refusal("%s.derived_from must be a list of the keys the bar is "
                          "built from" % where)
        for item in derived:
            text = str(item).strip().lower()
            if any(text == k or text.startswith(k + ".") or text.startswith(k + "/")
                   for k in CEILING_KEYS):
                mentions.append("derived_from names `%s`" % item)
    formula = str(block.get("formula", "") if isinstance(block, dict) else "").lower()
    if formula:
        for k in CEILING_KEYS:
            if k in formula:
                mentions.append("formula mentions `%s`" % k)
                break
    comparisons.append("required_price does not read the price ceiling")
    if mentions:
        raise Refusal(
            "required_price reads the ceiling it is tested against (%s). RB-V-025: "
            "a bar that reads its own ceiling is an indicator, not a bar. State the "
            "bar in fixed-number form: (operating cost + required profit) ÷ units."
            % "; ".join(mentions)
        )
    bar, _ = check_figure(block, where, bounding, comparisons,
                          tiered=False, allow_band=False)
    if derived:
        notes.append("required_price is built from: %s"
                     % ", ".join(str(d) for d in derived))
    else:
        notes.append("required_price states no `derived_from`; its derivation "
                     "is not checked, only its form")
    ceiling_low = ceiling[0]
    if ceiling_low >= bar:
        notes.append("the price ceiling (low end %.4f) clears the stated required "
                     "price bar %.4f" % (ceiling_low, bar))
    else:
        notes.append("the price ceiling (low end %.4f) does not clear the stated "
                     "required price bar %.4f" % (ceiling_low, bar))
    return bar


def parse_header_date(value):
    """Return a date, or None when the value is not a date."""
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    text = str(value).strip()
    for form in ("%Y-%m-%d", "%d %B %Y", "%d %b %Y"):
        try:
            return datetime.datetime.strptime(text, form).date()
        except ValueError:
            continue
    return None


def check_header_date(model, path, notes, warnings):
    """(c) VA-99 grace. The header date must not lag the edit history."""
    key = next((k for k in HEADER_DATE_KEYS if k in model), None)
    if key is None:
        notes.append("no header date (`date`, `updated` or `last_updated`), so "
                     "the header could not be compared with the edit history")
        return
    header = parse_header_date(model[key])
    if header is None:
        warnings.append("the header `%s: %s` is not a date the checker can read "
                        "(use YYYY-MM-DD), so it could not be compared with the "
                        "edit history" % (key, model[key]))
        return
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    end_of_day = datetime.datetime.combine(header, datetime.time()) + datetime.timedelta(days=1)
    lag = modified - end_of_day
    if lag > HEADER_GRACE:
        days = lag.days + (1 if lag.seconds else 0)
        warnings.append(
            "the header says `%s: %s` but the file on disk was last modified "
            "%s, which is more than 24 hours (about %d day%s) after the end of "
            "the dated day. VA-99: the grace cannot be kept by leaving an old "
            "header behind; set the header date to the day of the last edit."
            % (key, header.isoformat(), modified.strftime("%Y-%m-%d %H:%M"),
               days, "" if days == 1 else "s")
        )
    else:
        notes.append("header %s %s is within 24 hours of the last edit on disk"
                     % (key, header.isoformat()))


def verdict_for(margin, gate):
    for threshold, word in GATES[gate]:
        if threshold is None or margin >= threshold:
            return word
    return "FAIL"


def run(path):
    announce_origin(path)
    if not os.path.exists(path):
        raise Refusal("no such file: %s" % path)
    model = yaml.safe_load(open(path, encoding="utf-8"))
    if not isinstance(model, dict):
        raise Refusal("%s does not hold a mapping" % path)

    comparisons, notes, warnings = [], [], []
    bounding = load_bounding(model, comparisons)
    check_source_models(model, path, notes)
    check_header_date(model, path, notes, warnings)

    gate = str(need(model, "gate", "the model")).strip().lower()
    if gate not in GATES:
        raise Refusal("gate must be `per_requirement` or `phase_ii`, not `%s`" % gate)

    (floor_low, floor_high), included, excluded = compute_cost_floor(
        model, bounding, comparisons, notes)
    (ceiling_low, ceiling_high), (kmc_low, kmc_high), frac = compute_price_ceiling(
        model, bounding, comparisons, notes)
    bar = check_required_price(model, bounding, (ceiling_low, ceiling_high),
                               comparisons, notes)

    comparisons.append("cost floor is greater than zero")
    if floor_low <= 0:
        raise Refusal("the cost floor is %.4f. The margin divides by the cost "
                      "floor, so a floor of zero or less has no verdict." % floor_low)

    # (a) The margin is a band when any input is. The verdict is taken at the
    # worst corner: the ceiling's low end against the floor's high end.
    banded = (floor_high > floor_low) or (ceiling_high > ceiling_low)
    margin_worst = (ceiling_low - floor_high) / floor_high
    margin_best = (ceiling_high - floor_low) / floor_low
    margin = margin_worst
    word = verdict_for(margin, gate)

    cur, unit = bounding["currency"], bounding["unit"]
    print("Financial margin of safety — computed, not read   (fit_margin %s)" % VERSION)
    print("  model              : %s" % path)
    print("  venture            : %s" % model.get("venture", "(unnamed)"))
    print("  state              : %s" % model.get("state", "(unstated)"))
    print("  bounded at         : %s per %s, per %s, %s"
          % (cur, unit, bounding["period"], bounding["scale_state"]))
    print("")
    print("  cost floor         : %s %s   (layers %s)"
          % (cur, fmt(floor_low, floor_high), ", ".join(included)))
    if excluded:
        print("  layers excluded    : %s" % ", ".join(excluded))
    print("  key cost           : %s %s" % (cur, fmt(kmc_low, kmc_high)))
    print("  surplus fraction   : %.4f" % frac)
    print("  price ceiling      : %s %s   (key cost x fraction)"
          % (cur, fmt(ceiling_low, ceiling_high)))
    if banded:
        print("  net contribution   : %s %s   (worst corner to best corner)"
              % (cur, fmt(ceiling_low - floor_high, ceiling_high - floor_low)))
        print("  MARGIN OF SAFETY   : %.1f%% at the worst corner (ceiling low against "
              "floor high); %.1f%% at the best corner"
              % (margin_worst * 100, margin_best * 100))
    else:
        print("  net contribution   : %s %.4f" % (cur, ceiling_low - floor_low))
        print("  MARGIN OF SAFETY   : %.1f%%   ((ceiling - floor) / floor)" % (margin * 100))
    print("")
    print("  required price at 60%%: %s %s" % (cur, fmt(floor_low * 1.60, floor_high * 1.60)))
    print("  required price at 25%%: %s %s" % (cur, fmt(floor_low * 1.25, floor_high * 1.25)))
    if bar is not None:
        print("  required price bar : %s %.4f   (stated in fixed-number form)" % (cur, bar))
    print("")
    # VA-105: say what was verified, not only whether it passed.
    print("  checks reaching a verdict : %d" % len(comparisons))
    for c in comparisons:
        print("      - %s" % c)
    if notes:
        print("  notes:")
        for n in notes:
            print("      - %s" % n)
    if warnings:
        print("  warnings (the exit code is not changed by a warning):")
        for w in warnings:
            print("      - WARNING: %s" % w)

    print("")
    print("  gate applied       : %s" % gate)
    if banded:
        print("  VERDICT            : %s at %.1f%% (worst corner; best corner %.1f%%)"
              % (word, margin * 100, margin_best * 100))
    else:
        print("  VERDICT            : %s at %.1f%%" % (word, margin * 100))
    if excluded:
        print("  ** The verdict is INDICATIVE. %d cost layer(s) are excluded, so the "
              "margin is optimistic. **" % len(excluded))
    print("  This verdict is arithmetic on declared inputs. It is not evidence "
          "that any input is true of the world.")
    return 0 if word == "PASS" else 1


TEMPLATE = """\
# Financial margin of safety — input model.
# Every figure states an amount (or a band), a tier, a unit, a period, a scale
# state and a source. Delete nothing. A layer that is not designed yet carries
# a disposition.
#
# tier: the evidence tier of the figure, T1 to T4. A figure with no tier is
#   read at T4. At T2 to T4 the figure is a band, not a point:
#       band: {low: 0.0, high: 0.0}      # instead of `amount:`
#   At T1 a single `amount:` is allowed.
# date: the day of the last edit. A file modified more than 24 hours after
#   the end of that day produces a warning (VA-99).
venture: <name>
state: at-C<N>
date: 2026-09-16

# Every per-unit figure in this file is in <currency> per <unit>, per <period>,
# at one scale state. The checker refuses a figure that differs on any of these.
bounding:
  currency: GBP
  unit: <the unit the venture sells, e.g. covered transaction>
  period: year
  scale_state: at-scale        # launch | at-scale

# Where these figures came from. Both files must exist.
derived_from:
  operating_model: <venture>-aom-model-at-C<N>.yaml
  customer_model: <venture>-ctm-model-at-C<N>.yaml

gate: phase_ii                 # per_requirement | phase_ii

cost_floor:
  # amount:  optional. If stated it must equal the sum of the layers, and it
  #          may not be stated when any layer is a band.
  layers:
    pvc:
      amount: 0.0
      tier: T1                 # T1 | T2 | T3 | T4 — below T1, use `band:`
      unit: GBP per <unit>
      period: year
      scale_state: at-scale
      basis: activity          # activity | asserted
      source: <the activity rows and drivers this is built from>
    rc:
      band: {low: 0.0, high: 0.0}
      tier: T2
      unit: GBP per <unit>
      period: year
      scale_state: at-scale
      basis: activity
      source: <...>
    sc:
      not_designed_until: C3
      # or a full figure once R3 is complete
    ic:
      amount: 0.0
      tier: T1
      unit: GBP per <unit>
      period: year
      scale_state: at-scale
      basis: activity
      source: <...>

price_ceiling:
  # amount:  optional. If stated it must equal kmc x customer_surplus_fraction,
  #          and it may not be stated when kmc is a band.
  kmc:
    amount: 0.0
    tier: T1
    unit: GBP per <unit>
    period: year
    scale_state: at-scale
    source: <the customer cost this eliminates, and where the figure comes from>
  customer_surplus_fraction:
    value: 0.6
    source: <why this share is left with the customer>

# Optional. The required-price bar in fixed-number form:
# (operating cost + required profit) ÷ units. RB-V-025: a bar built from the
# price ceiling is refused; `derived_from` may not name price_ceiling or kmc.
# required_price:
#   amount: 0.0
#   unit: GBP per <unit>
#   period: year
#   scale_state: at-scale
#   derived_from: [cost_floor, required_profit]
#   source: <the capital bar ruling this applies, dated>
"""


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--template":
        sys.stdout.write(TEMPLATE)
        return 0
    try:
        return run(argv[0])
    except Refusal as exc:
        print("REFUSED: %s" % exc)
        print("Nothing was computed. There is no margin of safety to quote.")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
