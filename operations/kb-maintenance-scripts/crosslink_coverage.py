#!/usr/bin/env python3
"""
Crosslink Coverage Analyzer — Measure KB interconnection health.

Usage:
    python3 crosslink_coverage.py          # Text report
    python3 crosslink_coverage.py --json   # Structured JSON output

Reports:
  - Coverage distribution (0 / 1-2 / 3-5 / 6+ crosslinks per finding)
  - Per-category breakdown (total, avg links, % zero)
  - Isolated findings in otherwise-connected categories
  - Hub findings (most connected)
  - Relationship type distribution
"""

import argparse
import json
import sys

from kb_parser import build_finding_map


def analyze():
    findings = build_finding_map()

    # Coverage distribution
    buckets = {"zero": [], "low": [], "medium": [], "high": []}
    for fn, f in findings.items():
        count = len(f["related_findings"])
        if count == 0:
            buckets["zero"].append(fn)
        elif count <= 2:
            buckets["low"].append(fn)
        elif count <= 5:
            buckets["medium"].append(fn)
        else:
            buckets["high"].append(fn)

    total = len(findings)
    distribution = {
        "zero_crosslinks": len(buckets["zero"]),
        "one_to_two": len(buckets["low"]),
        "three_to_five": len(buckets["medium"]),
        "six_plus": len(buckets["high"]),
        "total": total,
        "pct_isolated": round(len(buckets["zero"]) / total * 100, 1) if total else 0,
    }

    # Per-category breakdown
    by_cat = {}
    for fn, f in findings.items():
        cat = f["category"] or "Uncategorized"
        if cat not in by_cat:
            by_cat[cat] = {"findings": [], "total_links": 0}
        by_cat[cat]["findings"].append(fn)
        by_cat[cat]["total_links"] += len(f["related_findings"])

    categories = {}
    for cat, data in sorted(by_cat.items()):
        count = len(data["findings"])
        zero = sum(
            1 for fn in data["findings"] if len(findings[fn]["related_findings"]) == 0
        )
        avg = round(data["total_links"] / count, 1) if count else 0
        categories[cat] = {
            "total": count,
            "avg_links": avg,
            "zero_count": zero,
            "pct_zero": round(zero / count * 100, 1) if count else 0,
        }

    # Isolated findings in partially-connected categories
    isolated_in_connected = []
    for cat, stats in categories.items():
        if stats["pct_zero"] < 80 and stats["zero_count"] > 0:
            for fn in by_cat[cat]["findings"]:
                if len(findings[fn]["related_findings"]) == 0:
                    isolated_in_connected.append(
                        {
                            "finding": fn,
                            "name": findings[fn]["name"][:80],
                            "category": cat,
                            "category_avg": stats["avg_links"],
                        }
                    )

    # Hub findings (top 10 by crosslink count)
    ranked = sorted(
        findings.items(), key=lambda x: len(x[1]["related_findings"]), reverse=True
    )
    hubs = []
    for fn, f in ranked[:10]:
        count = len(f["related_findings"])
        if count == 0:
            break
        hubs.append(
            {
                "finding": fn,
                "name": f["name"][:80],
                "category": f["category"],
                "crosslink_count": count,
            }
        )

    # Relationship type distribution
    rel_types = {}
    for fn, f in findings.items():
        for rel in f["related_findings"]:
            t = rel["rel"]
            rel_types[t] = rel_types.get(t, 0) + 1

    total_links = sum(rel_types.values())

    return {
        "distribution": distribution,
        "categories": categories,
        "isolated_in_connected": isolated_in_connected,
        "hubs": hubs,
        "relationship_types": rel_types,
        "total_crosslinks": total_links,
    }


def print_text(result):
    d = result["distribution"]
    print("=== Crosslink Coverage Analysis ===")
    print(f"Total findings: {d['total']}")
    print(f"Isolated (0 links): {d['zero_crosslinks']} ({d['pct_isolated']}%)")
    print(f"Light (1-2 links):  {d['one_to_two']}")
    print(f"Medium (3-5 links): {d['three_to_five']}")
    print(f"Rich (6+ links):    {d['six_plus']}")
    print(f"Total crosslinks:   {result['total_crosslinks']}")

    print(f"\n--- Category Breakdown ---")
    print(f"{'Category':<35} {'Total':>5} {'Avg':>5} {'Zero':>5} {'%Zero':>6}")
    print("-" * 60)
    for cat, stats in sorted(
        result["categories"].items(), key=lambda x: x[1]["total"], reverse=True
    ):
        print(
            f"{cat:<35} {stats['total']:>5} {stats['avg_links']:>5} {stats['zero_count']:>5} {stats['pct_zero']:>5.1f}%"
        )

    if result["hubs"]:
        print(f"\n--- Hub Findings (Top 10) ---")
        for h in result["hubs"]:
            print(f"  [{h['crosslink_count']:>2}] {h['name']} ({h['category']})")

    if result["isolated_in_connected"]:
        print(
            f"\n--- Isolated in Connected Categories ({len(result['isolated_in_connected'])}) ---"
        )
        for i in result["isolated_in_connected"][:15]:
            print(f"  {i['finding'][:60]} ({i['category']}, cat avg {i['category_avg']})")

    if result["relationship_types"]:
        print(f"\n--- Relationship Types ---")
        for t, count in sorted(
            result["relationship_types"].items(), key=lambda x: -x[1]
        ):
            print(f"  {t}: {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crosslink Coverage Analyzer")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = analyze()

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_text(result)
