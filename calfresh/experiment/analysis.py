#!/usr/bin/env python3
"""Preregistered analysis of the CalFresh guide experiment (dollars vs. groceries).

Usage:
  python3 analysis.py                       # analyze results.csv, print numbers + summary
  python3 analysis.py --write-md            # same, and write results.md
  python3 analysis.py --from-export FILE    # rebuild results.csv from a GoatCounter CSV export first

Only the Python standard library is used. The plan this follows is PREREGISTRATION.md.
"""
import argparse
import csv
import math
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from statistics import NormalDist
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results.csv")
RESULTS_MD = os.path.join(HERE, "results.md")
FIELDS = ["date", "version", "visitors", "apply_clicks", "help_clicks", "any_click", "ref"]

PACIFIC = ZoneInfo("America/Los_Angeles")
WINDOW_START = date(2026, 10, 2)
WINDOW_END = date(2026, 11, 8)
ALPHA = 0.05
Z975 = NormalDist().inv_cdf(0.975)
KIND_TO_FIELD = {"view": "visitors", "apply": "apply_clicks", "help": "help_clicks", "any": "any_click"}


# ---------------------------------------------------------------- GoatCounter export -> results.csv
def from_export(path):
    """Count exp/<A|B>/<kind>/<ref> events per Pacific date, version, and ref.

    Each event already fires at most once per browser, so a count of events is a count of visitors.
    Rows flagged as bots and rows outside the data window are dropped.
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        # GoatCounter prefixes the first column with its export format version (for example "2Path").
        cols = {h.lstrip("0123456789").strip().lower(): i for i, h in enumerate(header)}
        for need in ("path", "date"):
            if need not in cols:
                sys.exit(f"Export is missing a '{need}' column; header was: {header}")
        counts = defaultdict(lambda: {k: 0 for k in KIND_TO_FIELD.values()})
        dropped_bots = dropped_window = 0
        for row in reader:
            p = row[cols["path"]].strip().lstrip("/")
            parts = p.split("/")
            if len(parts) != 4 or parts[0] != "exp" or parts[1] not in ("A", "B") or parts[2] not in KIND_TO_FIELD:
                continue
            if "bot" in cols and row[cols["bot"]].strip() not in ("", "0", "false", "False"):
                dropped_bots += 1
                continue
            ts = datetime.fromisoformat(row[cols["date"]].strip().replace("Z", "+00:00"))
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            d = ts.astimezone(PACIFIC).date()
            if not (WINDOW_START <= d <= WINDOW_END):
                dropped_window += 1
                continue
            counts[(d.isoformat(), parts[1], parts[3])][KIND_TO_FIELD[parts[2]]] += 1
    with open(RESULTS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for (d, v, ref), c in sorted(counts.items()):
            w.writerow({"date": d, "version": v, "ref": ref, **c})
    print(f"Wrote {RESULTS}: {len(counts)} rows ({dropped_bots} bot events and "
          f"{dropped_window} out-of-window events dropped).\n")


# ---------------------------------------------------------------- statistics
def load():
    tot = {v: defaultdict(int) for v in "AB"}
    by_ref = defaultdict(lambda: {v: defaultdict(int) for v in "AB"})
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d = date.fromisoformat(r["date"])
            if not (WINDOW_START <= d <= WINDOW_END) or r["version"] not in tot:
                continue
            for k in ("visitors", "apply_clicks", "help_clicks", "any_click"):
                n = int(r[k] or 0)
                tot[r["version"]][k] += n
                by_ref[r["ref"] or "direct"][r["version"]][k] += n
    return tot, by_ref


def fisher_two_sided(a, b, c, d):
    """Fisher's exact test for [[a, b], [c, d]]: sum of tables no more likely than the observed one."""
    r1, c1, n = a + b, a + c, a + b + c + d
    lo, hi = max(0, c1 - (n - r1)), min(r1, c1)

    def logp(x):
        return (math.lgamma(r1 + 1) - math.lgamma(x + 1) - math.lgamma(r1 - x + 1)
                + math.lgamma(n - r1 + 1) - math.lgamma(c1 - x + 1) - math.lgamma(n - r1 - c1 + x + 1)
                - math.lgamma(n + 1) + math.lgamma(c1 + 1) + math.lgamma(n - c1 + 1))

    obs = logp(a)
    return min(1.0, sum(math.exp(logp(x)) for x in range(lo, hi + 1) if logp(x) <= obs + 1e-7))


def compare(xa, na, xb, nb):
    """Preregistered comparison of B vs A. Returns a dict, or None if a version has no visitors."""
    if na == 0 or nb == 0:
        return None
    pa, pb = xa / na, xb / nb
    pooled = (xa + xb) / (na + nb)
    se0 = math.sqrt(pooled * (1 - pooled) * (1 / na + 1 / nb))
    z = (pb - pa) / se0 if se0 > 0 else 0.0
    p_z = 2 * (1 - NormalDist().cdf(abs(z))) if se0 > 0 else 1.0
    p_f = fisher_two_sided(xb, nb - xb, xa, na - xa)
    small = min(xa, na - xa, xb, nb - xb) < 10
    se1 = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    diff = pb - pa
    out = dict(pa=pa, pb=pb, xa=xa, na=na, xb=xb, nb=nb, z=z, p_z=p_z, p_fisher=p_f, small=small,
               test="Fisher's exact" if small else "two-proportion z", p=p_f if small else p_z,
               diff=diff, diff_lo=diff - Z975 * se1, diff_hi=diff + Z975 * se1,
               lift=None, lift_lo=None, lift_hi=None)
    if xa > 0 and xb > 0:
        rr = pb / pa
        se_log = math.sqrt(1 / xb - 1 / nb + 1 / xa - 1 / na)
        out.update(lift=rr - 1, lift_lo=math.exp(math.log(rr) - Z975 * se_log) - 1,
                   lift_hi=math.exp(math.log(rr) + Z975 * se_log) - 1)
    return out


def pct(x, nd=1):
    return "undefined" if x is None else f"{x * 100:.{nd}f}%"


def pts(x):
    return f"{x * 100:+.1f} points"


def report(name, r):
    lines = [f"{name}"]
    if r is None:
        return lines + ["  No data yet."]
    lines += [
        f"  Version A (dollars):   {r['xa']} of {r['na']} visitors = {pct(r['pa'])}",
        f"  Version B (groceries): {r['xb']} of {r['nb']} visitors = {pct(r['pb'])}",
        f"  Difference (B - A):    {pts(r['diff'])}  (95% CI {pts(r['diff_lo'])} to {pts(r['diff_hi'])})",
        f"  Relative lift (B/A-1): {pct(r['lift'])}  (95% CI {pct(r['lift_lo'])} to {pct(r['lift_hi'])})",
        f"  z = {r['z']:.2f}, p (z-test) = {r['p_z']:.3f}; p (Fisher's exact) = {r['p_fisher']:.3f}",
        f"  Preregistered test used: {r['test']}"
        + (" (a cell is under 10)" if r['small'] else "") + f", p = {r['p']:.3f}",
    ]
    return lines


def summary(r, final):
    if r is None:
        return (f"No visitors have been recorded yet. Data are being collected until "
                f"{WINDOW_END:%B} {WINDOW_END.day}, {WINDOW_END.year}.")
    sig = r["p"] < ALPHA
    direction = "more" if r["diff"] > 0 else "fewer" if r["diff"] < 0 else "the same share of"
    lift = "" if r["lift"] is None or r["diff"] == 0 else f" ({pct(abs(r['lift']), 0)} {direction})"
    status = ("This is the final, preregistered result" if final
              else f"These are interim numbers; the window closes {WINDOW_END:%B} {WINDOW_END.day}, and no test is "
                   "interpreted before then")
    return (
        f"{r['na'] + r['nb']} visitors were randomly shown one of two versions of the CalFresh guide. "
        f"{pct(r['pa'])} of those who saw the aid as dollars ({r['xa']} of {r['na']}) clicked to apply or get help, "
        f"compared with {pct(r['pb'])} of those who saw it as groceries ({r['xb']} of {r['nb']}): a difference of "
        f"{pts(r['diff'])}{lift}. The 95% confidence interval for the difference runs from {pts(r['diff_lo'])} to "
        f"{pts(r['diff_hi'])}, and the preregistered {r['test']} test gives p = {r['p']:.3f}, so the difference "
        + ("is statistically significant at the 0.05 level. " if sig else
           "is not statistically significant at the 0.05 level; the data cannot rule out no difference. ")
        + f"{status}. With this sample, only large effects were detectable, so the study is reported as a pilot."
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from-export", metavar="FILE", help="GoatCounter CSV export to rebuild results.csv from")
    ap.add_argument("--write-md", action="store_true", help="also write results.md")
    args = ap.parse_args()
    if args.from_export:
        from_export(args.from_export)

    tot, by_ref = load()
    final = datetime.now(PACIFIC).date() > WINDOW_END
    primary = compare(tot["A"]["any_click"], tot["A"]["visitors"], tot["B"]["any_click"], tot["B"]["visitors"])
    apply_ = compare(tot["A"]["apply_clicks"], tot["A"]["visitors"], tot["B"]["apply_clicks"], tot["B"]["visitors"])

    out = [f"CalFresh guide experiment: {'FINAL' if final else 'INTERIM'} "
           f"(window {WINDOW_START} to {WINDOW_END}, Pacific)", ""]
    out += report("PRIMARY: clicked apply or help at least once", primary) + [""]
    out += report("SECONDARY: clicked apply at least once", apply_) + [""]
    out.append("SECONDARY: by referrer (descriptive, no tests)")
    out.append(f"  {'ref':<22}{'A visitors':>11}{'A any':>8}{'A rate':>9}{'B visitors':>12}{'B any':>8}{'B rate':>9}")
    for ref, v in sorted(by_ref.items(), key=lambda kv: -(kv[1]['A']['visitors'] + kv[1]['B']['visitors'])):
        row = f"  {ref:<22}"
        for k in "AB":
            n, x = v[k]["visitors"], v[k]["any_click"]
            width = 11 if k == "A" else 12
            row += f"{n:>{width}}{x:>8}{(pct(x / n) if n else '-'):>9}"
        out.append(row)
    if not by_ref:
        out.append("  No data yet.")
    para = summary(primary, final)
    out += ["", "Plain-English summary", para]
    print("\n".join(out))

    if args.write_md:
        with open(RESULTS_MD, "w", encoding="utf-8") as f:
            f.write("# Results: Dollars vs. Groceries on the FLC CalFresh Guide\n\n")
            f.write(f"Preregistration: [PREREGISTRATION.md](PREREGISTRATION.md). "
                    f"Status: **{'final' if final else f'collecting data until {WINDOW_END:%B} {WINDOW_END.day}, {WINDOW_END.year}'}**. "
                    f"Generated by `analysis.py` from `results.csv` on {datetime.now(PACIFIC):%Y-%m-%d}.\n\n")
            f.write(para + "\n\n```\n" + "\n".join(out[:-3]) + "\n```\n")
        print(f"\nWrote {RESULTS_MD}")


if __name__ == "__main__":
    main()
