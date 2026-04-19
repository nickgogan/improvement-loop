#!/usr/bin/env python3
"""
KB Linkage Analyzer — Audit source-finding bidirectional links and broken references.

Usage:
    python3 linkage_analyzer.py              # Report gaps (dry run, text output)
    python3 linkage_analyzer.py --json       # Structured JSON output for skill consumption
    python3 linkage_analyzer.py --fix        # Execute repairs (not yet implemented)

Exit codes:
    0 = No issues found
    1 = Issues detected (orphans, asymmetries, or broken refs)

Used by /linkage-repair skill as a pre-step to replace 300+ individual file reads.
"""

import argparse
import json
import sys
from pathlib import Path

from kb_parser import (
    FINDINGS_DIR,
    SOURCES_DIR,
    build_finding_map,
    build_source_map,
    file_exists,
)


def analyze():
    sources = build_source_map()
    findings = build_finding_map()

    # Orphaned findings (no sources linked)
    orphans = [
        fn
        for fn, f in findings.items()
        if not f["sources_files"] and not f["sources_notion"]
    ]

    # Unlinked sources (no findings listed)
    unlinked = [
        fn
        for fn, s in sources.items()
        if not s["findings_files"] and not s["findings_notion"]
    ]

    # Asymmetric links: finding→source exists but source→finding missing, and vice versa
    asymmetric = []
    for ffn, f in findings.items():
        for sfn in f["sources_files"]:
            if sfn in sources and ffn not in sources[sfn]["findings_files"]:
                asymmetric.append(
                    {"direction": "finding_refs_source", "finding": ffn, "source": sfn}
                )
    for sfn, s in sources.items():
        for ffn in s["findings_files"]:
            if ffn in findings and sfn not in findings[ffn]["sources_files"]:
                asymmetric.append(
                    {"direction": "source_refs_finding", "source": sfn, "finding": ffn}
                )

    # Broken references: filenames that don't exist on disk
    broken = []
    notion_authority_refs = []  # Legacy Notion URLs in authority fields (migration artifact)
    for sfn, s in sources.items():
        for ffn in s["findings_files"]:
            if not file_exists(ffn, FINDINGS_DIR):
                broken.append(
                    {"type": "source_refs_missing_finding", "source": sfn, "ref": ffn}
                )
        for afn in s["authority"]:
            if "notion.so" in afn:
                notion_authority_refs.append({"source": sfn, "ref": afn})
            else:
                auth_dir = SOURCES_DIR.parent / "research-authorities"
                if not file_exists(afn, auth_dir):
                    broken.append(
                        {
                            "type": "source_refs_missing_authority",
                            "source": sfn,
                            "ref": afn,
                        }
                    )
    for ffn, f in findings.items():
        for sfn in f["sources_files"]:
            if not file_exists(sfn, SOURCES_DIR):
                broken.append(
                    {"type": "finding_refs_missing_source", "finding": ffn, "ref": sfn}
                )
        for rel in f["related_findings"]:
            if not file_exists(rel["file"], FINDINGS_DIR):
                broken.append(
                    {
                        "type": "finding_refs_missing_finding",
                        "finding": ffn,
                        "ref": rel["file"],
                    }
                )

    has_issues = bool(orphans or unlinked or asymmetric or broken)

    return {
        "total_sources": len(sources),
        "total_findings": len(findings),
        "orphaned_findings": sorted(orphans),
        "orphaned_count": len(orphans),
        "unlinked_sources": sorted(unlinked),
        "unlinked_count": len(unlinked),
        "asymmetric_links": asymmetric,
        "asymmetric_count": len(asymmetric),
        "broken_references": broken,
        "broken_count": len(broken),
        "notion_authority_refs": notion_authority_refs,
        "notion_authority_count": len(notion_authority_refs),
        "has_issues": has_issues,
    }


def print_text(result):
    print("=== KB Linkage Analysis ===")
    print(f"Total sources:     {result['total_sources']}")
    print(f"Total findings:    {result['total_findings']}")
    print(f"Orphaned findings: {result['orphaned_count']}")
    print(f"Unlinked sources:  {result['unlinked_count']}")
    print(f"Asymmetric links:  {result['asymmetric_count']}")
    print(f"Broken references: {result['broken_count']}")
    print(f"Notion authority refs (legacy): {result['notion_authority_count']}")

    if result["orphaned_findings"]:
        print(f"\nOrphaned findings (no sources):")
        for fn in result["orphaned_findings"]:
            print(f"  {fn}")

    if result["unlinked_sources"]:
        print(f"\nUnlinked sources (no findings):")
        for fn in result["unlinked_sources"]:
            print(f"  {fn}")

    if result["asymmetric_links"]:
        print(f"\nAsymmetric links:")
        for a in result["asymmetric_links"]:
            if a["direction"] == "finding_refs_source":
                print(f"  Finding {a['finding']} -> Source {a['source']} (no reverse)")
            else:
                print(f"  Source {a['source']} -> Finding {a['finding']} (no reverse)")

    if result["broken_references"]:
        print(f"\nBroken references:")
        for b in result["broken_references"]:
            if "source" in b:
                print(f"  {b['source']} refs non-existent: {b['ref']}")
            else:
                print(f"  {b['finding']} refs non-existent: {b['ref']}")

    status = "CLEAN" if not result["has_issues"] else "ISSUES FOUND"
    print(f"\nStatus: {status}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KB Linkage Analyzer")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = analyze()

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_text(result)

    sys.exit(1 if result["has_issues"] else 0)
