#!/usr/bin/env python3
"""
KB Health Checker — Unified health report for the Improvement Loop knowledge base.

Usage:
    python3 kb_health.py                       # Full markdown report
    python3 kb_health.py --json                # Full JSON report
    python3 kb_health.py --section linkage     # Only linkage integrity
    python3 kb_health.py --section crosslink   # Only crosslink coverage
    python3 kb_health.py --section summary     # Quick summary only

Composes linkage_analyzer and crosslink_coverage into a single report.
Exit code: 0 = healthy, 1 = issues found.
"""

import argparse
import json
import sys
from datetime import date

from crosslink_coverage import analyze as crosslink_analyze
from linkage_analyzer import analyze as linkage_analyze


def grade(linkage, crosslink):
    """Compute overall health grade based on metrics."""
    score = 100

    # Linkage penalties (broken file refs, not legacy Notion URLs)
    if linkage["broken_count"] > 0:
        score -= 5 * min(linkage["broken_count"], 5)  # Cap at -25
    if linkage["asymmetric_count"] > 0:
        score -= 2 * linkage["asymmetric_count"]
    orphan_pct = (
        linkage["orphaned_count"] / linkage["total_findings"] * 100
        if linkage["total_findings"]
        else 0
    )
    if orphan_pct > 10:
        score -= 10
    elif orphan_pct > 5:
        score -= 5

    # Crosslink penalties
    isolated_pct = crosslink["distribution"]["pct_isolated"]
    if isolated_pct > 80:
        score -= 30
    elif isolated_pct > 60:
        score -= 20
    elif isolated_pct > 40:
        score -= 10

    if score >= 90:
        return "A", score
    elif score >= 80:
        return "B+", score
    elif score >= 70:
        return "B", score
    elif score >= 60:
        return "C+", score
    elif score >= 50:
        return "C", score
    else:
        return "D", score


def recommendations(linkage, crosslink):
    """Generate prioritized recommendations."""
    recs = []

    if linkage["broken_count"] > 0:
        recs.append(
            f"FIX: {linkage['broken_count']} broken reference(s) — files referenced that don't exist on disk"
        )
    if linkage["asymmetric_count"] > 0:
        recs.append(
            f"FIX: {linkage['asymmetric_count']} asymmetric link(s) — one-way references that need reciprocal links"
        )

    isolated_pct = crosslink["distribution"]["pct_isolated"]
    if isolated_pct > 60:
        # Find the worst categories
        worst = sorted(
            crosslink["categories"].items(),
            key=lambda x: (-x[1]["total"] if x[1]["pct_zero"] > 80 else 0),
        )
        worst_names = [
            cat for cat, s in worst[:3] if s["pct_zero"] > 80 and s["total"] > 5
        ]
        if worst_names:
            recs.append(
                f"CROSSLINK: {isolated_pct}% of findings have zero crosslinks. "
                f"Run /finding-crosslink on: {', '.join(worst_names)}"
            )

    if linkage["orphaned_count"] > 10:
        recs.append(
            f"REVIEW: {linkage['orphaned_count']} findings have no linked sources — "
            f"consider running /linkage-repair --content-match"
        )

    if crosslink["isolated_in_connected"]:
        count = len(crosslink["isolated_in_connected"])
        recs.append(
            f"CROSSLINK: {count} finding(s) isolated in otherwise-connected categories — quick wins for linking"
        )

    if not recs:
        recs.append("No urgent actions. KB is in good health.")

    return recs


def print_markdown(linkage, crosslink):
    today = date.today().isoformat()
    letter, score = grade(linkage, crosslink)
    recs = recommendations(linkage, crosslink)

    print(f"# KB Health Report — {today}\n")

    # Summary
    print("## Summary\n")
    print("| Metric | Value | Status |")
    print("|--------|-------|--------|")
    print(f"| Overall Grade | **{letter}** ({score}/100) | |")
    print(f"| Total Sources | {linkage['total_sources']} | |")
    print(f"| Total Findings | {linkage['total_findings']} | |")

    link_status = "CLEAN" if not linkage["has_issues"] else "ISSUES"
    notion_note = f", {linkage['notion_authority_count']} legacy Notion refs" if linkage["notion_authority_count"] else ""
    print(
        f"| Linkage Integrity | {linkage['asymmetric_count']} asymmetric, {linkage['broken_count']} broken{notion_note} | {link_status} |"
    )

    iso = crosslink["distribution"]["pct_isolated"]
    cross_status = "CRITICAL" if iso > 70 else ("WARN" if iso > 40 else "OK")
    print(f"| Crosslink Coverage | {iso}% isolated | {cross_status} |")
    print()

    # Linkage Integrity
    print("## Linkage Integrity\n")
    print(f"- Orphaned findings (no sources): **{linkage['orphaned_count']}**")
    print(f"- Unlinked sources (no findings): **{linkage['unlinked_count']}**")
    print(f"- Asymmetric links: **{linkage['asymmetric_count']}**")
    print(f"- Broken references: **{linkage['broken_count']}**")

    if linkage["broken_references"]:
        print("\n### Broken References\n")
        print("| File | References | Missing |")
        print("|------|------------|---------|")
        for b in linkage["broken_references"]:
            src = b.get("source", b.get("finding", "?"))
            print(f"| {src} | {b['type']} | `{b['ref']}` |")

    if linkage["asymmetric_links"]:
        print("\n### Asymmetric Links\n")
        print("| Direction | From | To |")
        print("|-----------|------|----|")
        for a in linkage["asymmetric_links"][:20]:
            if a["direction"] == "finding_refs_source":
                print(f"| finding→source | {a['finding']} | {a['source']} |")
            else:
                print(f"| source→finding | {a['source']} | {a['finding']} |")
    print()

    # Crosslink Coverage
    d = crosslink["distribution"]
    print("## Crosslink Coverage\n")
    print("| Crosslinks | Findings | % |")
    print("|------------|----------|---|")
    print(
        f"| 0 (isolated) | {d['zero_crosslinks']} | {d['pct_isolated']}% |"
    )
    t = d["total"]
    for label, key in [("1-2", "one_to_two"), ("3-5", "three_to_five"), ("6+", "six_plus")]:
        val = d[key]
        pct = round(val / t * 100, 1) if t else 0
        print(f"| {label} | {val} | {pct}% |")

    print(f"\nTotal crosslinks in KB: **{crosslink['total_crosslinks']}**")

    # Category breakdown
    print("\n### By Category\n")
    print(f"| Category | Findings | Avg Links | % Isolated |")
    print(f"|----------|----------|-----------|------------|")
    for cat, s in sorted(
        crosslink["categories"].items(), key=lambda x: -x[1]["total"]
    ):
        print(f"| {cat} | {s['total']} | {s['avg_links']} | {s['pct_zero']}% |")

    # Hubs
    if crosslink["hubs"]:
        print("\n### Hub Findings\n")
        print("| Finding | Category | Links |")
        print("|---------|----------|-------|")
        for h in crosslink["hubs"]:
            print(f"| {h['name']} | {h['category']} | {h['crosslink_count']} |")

    # Recommendations
    print("\n## Recommendations\n")
    for i, r in enumerate(recs, 1):
        print(f"{i}. {r}")
    print()


def print_json(linkage, crosslink):
    letter, score = grade(linkage, crosslink)
    recs = recommendations(linkage, crosslink)
    output = {
        "date": date.today().isoformat(),
        "grade": letter,
        "score": score,
        "linkage": linkage,
        "crosslink": crosslink,
        "recommendations": recs,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KB Health Checker")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--section",
        choices=["linkage", "crosslink", "summary"],
        default=None,
        help="Report only a specific section",
    )
    args = parser.parse_args()

    run_linkage = args.section in (None, "linkage", "summary")
    run_crosslink = args.section in (None, "crosslink", "summary")

    linkage = linkage_analyze() if run_linkage else None
    crosslink = crosslink_analyze() if run_crosslink else None

    # For section-only modes with JSON
    if args.json:
        if args.section == "linkage":
            print(json.dumps(linkage, indent=2))
        elif args.section == "crosslink":
            print(json.dumps(crosslink, indent=2))
        else:
            print_json(linkage, crosslink)
    else:
        if args.section == "linkage":
            from linkage_analyzer import print_text
            print_text(linkage)
        elif args.section == "crosslink":
            from crosslink_coverage import print_text
            print_text(crosslink)
        else:
            print_markdown(linkage, crosslink)

    # Exit code
    has_issues = False
    if linkage and linkage.get("has_issues"):
        has_issues = True
    if crosslink and crosslink["distribution"]["pct_isolated"] > 70:
        has_issues = True
    sys.exit(1 if has_issues else 0)
