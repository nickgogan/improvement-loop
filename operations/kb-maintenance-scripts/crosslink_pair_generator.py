#!/usr/bin/env python3
"""
Crosslink Pair Generator — Build candidate pair lists for /finding-crosslink skill.

Usage:
    python3 crosslink_pair_generator.py                          # All pairs
    python3 crosslink_pair_generator.py --category Orchestration # Single category
    python3 crosslink_pair_generator.py --new-only               # Only pairs involving newest findings
    python3 crosslink_pair_generator.py --max-pairs 500          # Limit output

Generates pairs using three tiers:
  Tier 1: Same-category pairs (within-category relationships)
  Tier 2: Shared-source pairs (cross-category, co-occurrence signal)
  Tier 3: Keyword overlap (cross-category, filtered by 2+ non-trivial keywords)

Outputs JSON to stdout with pair data including summaries for subagent dispatch.
"""

import argparse
import json
import sys
from itertools import combinations

from kb_parser import build_finding_map

STOP_WORDS = {
    "agent", "agents", "code", "claude", "pattern", "system", "tool", "model",
    "framework", "architecture", "production", "based", "using", "context",
    "findings", "engineering", "design", "approach", "multiple", "specific",
}


def keywords(text):
    """Extract meaningful keywords from text, filtering stop words."""
    import re
    words = set(re.findall(r"[a-z]{4,}", text.lower()))
    return words - STOP_WORDS


def build_pairs(new_only=False, category=None, max_pairs=800):
    findings = build_finding_map()

    # Determine which findings are "new" (most recent date)
    dates = [f["date_discovered"] for f in findings.values() if f["date_discovered"]]
    today = max(dates) if dates else ""
    new_findings = (
        {fn for fn, f in findings.items() if f["date_discovered"] == today}
        if new_only
        else set(findings.keys())
    )

    if category:
        scope = {fn for fn, f in findings.items() if f["category"] == category}
        new_findings = new_findings & scope

    # Track already-linked pairs to skip
    already_linked = set()
    for fn, f in findings.items():
        for rel in f["related_findings"]:
            pair = (min(fn, rel["file"]), max(fn, rel["file"]))
            already_linked.add(pair)

    pairs = set()

    # Tier 1: Same-category
    by_cat = {}
    for fn in new_findings:
        by_cat.setdefault(findings[fn]["category"], []).append(fn)
    for cat, fns in by_cat.items():
        all_in_cat = [fn for fn, f in findings.items() if f["category"] == cat]
        for n in fns:
            for o in all_in_cat:
                if n != o:
                    pair = (min(n, o), max(n, o))
                    if pair not in already_linked:
                        pairs.add(pair)

    # Tier 2: Shared-source cross-category
    by_source = {}
    for fn, f in findings.items():
        for src in f["sources_files"]:
            by_source.setdefault(src, []).append(fn)
    for src, fns in by_source.items():
        if len(fns) < 2:
            continue
        for a, b in combinations(fns, 2):
            if findings[a]["category"] != findings[b]["category"]:
                if a in new_findings or b in new_findings:
                    pair = (min(a, b), max(a, b))
                    if pair not in already_linked:
                        pairs.add(pair)

    # Tier 3: Keyword overlap (cross-category only)
    if not category:
        new_list = list(new_findings)
        all_list = list(findings.keys())
        kw_cache = {
            fn: keywords(f["name"] + " " + f["summary"]) for fn, f in findings.items()
        }
        for n in new_list:
            for o in all_list:
                if n >= o:
                    continue
                if findings[n]["category"] == findings[o]["category"]:
                    continue
                pair = (n, o)
                if pair in pairs or pair in already_linked:
                    continue
                overlap = kw_cache[n] & kw_cache[o]
                if len(overlap) >= 2:
                    pairs.add(pair)

    # Limit and format
    pair_list = sorted(pairs)[:max_pairs]
    output = []
    for a, b in pair_list:
        output.append(
            {
                "a": a,
                "a_name": findings[a]["name"][:80],
                "a_cat": findings[a]["category"],
                "a_sum": findings[a]["summary"],
                "b": b,
                "b_name": findings[b]["name"][:80],
                "b_cat": findings[b]["category"],
                "b_sum": findings[b]["summary"],
            }
        )

    return output, len(findings), len(already_linked)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crosslink Pair Generator")
    parser.add_argument("--new-only", action="store_true")
    parser.add_argument("--category", type=str, default=None)
    parser.add_argument("--max-pairs", type=int, default=800)
    args = parser.parse_args()

    pairs, total, existing = build_pairs(
        new_only=args.new_only, category=args.category, max_pairs=args.max_pairs
    )
    print(json.dumps(pairs, indent=2))
    print(
        f"\n# {len(pairs)} pairs generated from {total} findings ({existing} existing links)",
        file=sys.stderr,
    )
