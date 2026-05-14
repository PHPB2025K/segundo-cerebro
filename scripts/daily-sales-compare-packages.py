#!/usr/bin/env python3
"""Compare two data packages for the same date (e.g., 06:50 vs 09:00).

Usage:
    python3 scripts/daily-sales-compare-packages.py package_a.json package_b.json

Outputs a summary of differences in totals, cancelamentos, and top products.
Does NOT modify any file. Read-only comparison.
"""

import json
import sys
from pathlib import Path


def load_pkg(path_str):
    p = Path(path_str)
    if not p.exists():
        print(f"ERROR: {p} not found", file=sys.stderr)
        sys.exit(1)
    with open(p) as f:
        return json.load(f)


def compare_totals(a, b, label):
    """Compare recipient totals between two packages."""
    recs_a = a.get("recipients", {})
    recs_b = b.get("recipients", {})
    all_keys = sorted(set(list(recs_a.keys()) + list(recs_b.keys())))

    print(f"\n{'='*60}")
    print(f"  {label}: Totals Comparison")
    print(f"{'='*60}")
    print(f"{'Recipient':<12} {'Metric':<16} {'Pkg A':>10} {'Pkg B':>10} {'Diff':>10} {'Diff%':>8}")
    print("-" * 68)

    for rk in all_keys:
        ta = recs_a.get(rk, {}).get("totals", {})
        tb = recs_b.get(rk, {}).get("totals", {})
        for metric in ["orders", "gmv", "ticket_medio", "cancelamentos"]:
            va = ta.get(metric, 0) or 0
            vb = tb.get(metric, 0) or 0
            diff = vb - va
            pct = (diff / va * 100) if va else 0
            flag = " !!!" if abs(pct) > 10 else ""
            print(f"{rk:<12} {metric:<16} {va:>10.2f} {vb:>10.2f} {diff:>+10.2f} {pct:>+7.1f}%{flag}")
        print()


def compare_readiness(a, b):
    """Compare data readiness status."""
    dra = a.get("data_readiness", {})
    drb = b.get("data_readiness", {})
    sa = dra.get("status", "N/A")
    sb = drb.get("status", "N/A")
    match = "MATCH" if sa == sb else "DIVERGE"
    print(f"\nData Readiness: A={sa} | B={sb} → {match}")

    if sa != sb:
        print("  WARNING: Data Readiness diverges between packages!")
        for c in dra.get("checks", []):
            if c.get("status") == "fail":
                print(f"    A FAIL: {c['check']} — {c.get('detail', '')}")
        for c in drb.get("checks", []):
            if c.get("status") == "fail":
                print(f"    B FAIL: {c['check']} — {c.get('detail', '')}")


def compare_top_products(a, b):
    """Compare top products per account."""
    pa = a.get("platforms", a.get("accounts", {}))
    pb = b.get("platforms", b.get("accounts", {}))
    all_slugs = sorted(set(list(pa.keys()) + list(pb.keys())))

    print(f"\n{'='*60}")
    print(f"  Top Products Comparison (top 3 per account)")
    print(f"{'='*60}")

    for slug in all_slugs:
        ma = pa.get(slug, {}).get("metrics", {})
        mb = pb.get(slug, {}).get("metrics", {})
        top_a = ma.get("top_products", [])[:3]
        top_b = mb.get("top_products", [])[:3]

        titles_a = [p.get("title", "?") for p in top_a]
        titles_b = [p.get("title", "?") for p in top_b]

        if titles_a == titles_b:
            status = "MATCH"
        else:
            status = "DIVERGE"

        print(f"\n  {slug} [{status}]")
        if status == "DIVERGE":
            for i, (ta, tb) in enumerate(zip(top_a, top_b)):
                qa = ta.get("quantity", 0)
                qb = tb.get("quantity", 0)
                na = ta.get("title", "?")[:40]
                nb = tb.get("title", "?")[:40]
                if na != nb or qa != qb:
                    print(f"    #{i+1} A: {na} (qty={qa})")
                    print(f"    #{i+1} B: {nb} (qty={qb})")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 daily-sales-compare-packages.py <package_a.json> <package_b.json>")
        sys.exit(1)

    pkg_a = load_pkg(sys.argv[1])
    pkg_b = load_pkg(sys.argv[2])

    date_a = pkg_a.get("date", "?")
    date_b = pkg_b.get("date", "?")
    gen_a = pkg_a.get("generated_at_utc", "?")
    gen_b = pkg_b.get("generated_at_utc", "?")

    print(f"Package A: date={date_a} generated={gen_a}")
    print(f"Package B: date={date_b} generated={gen_b}")

    if date_a != date_b:
        print(f"\nWARNING: Dates differ ({date_a} vs {date_b}). Comparison may not be meaningful.")

    compare_readiness(pkg_a, pkg_b)
    compare_totals(pkg_a, pkg_b, f"Date {date_a}")
    compare_top_products(pkg_a, pkg_b)

    print(f"\n{'='*60}")
    print("  Comparison complete. No files modified.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
