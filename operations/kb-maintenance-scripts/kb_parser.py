#!/usr/bin/env python3
"""
KB Parser — Shared frontmatter parsing and map building for KB maintenance scripts.

Provides reusable functions for reading YAML frontmatter from research sources,
findings, and authorities. Used by linkage_analyzer, crosslink_pair_generator,
crosslink_coverage, and kb_health.

Usage as module:
    from kb_parser import build_source_map, build_finding_map, SOURCES_DIR, FINDINGS_DIR
"""

import os
import re
from pathlib import Path

import yaml

# Paths relative to MetaSystem root
ROOT = Path(__file__).resolve().parents[4]
SOURCES_DIR = ROOT / "systems/improvement-loop/research-sources"
FINDINGS_DIR = ROOT / "systems/improvement-loop/research-findings"
AUTHORITIES_DIR = ROOT / "systems/improvement-loop/research-authorities"


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file.

    Returns (frontmatter_dict, body_text). If no frontmatter found,
    returns ({}, full_content).
    """
    with open(filepath, "r") as f:
        content = f.read()
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}, content
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, content[m.end() :]


def normalize_list(val):
    """Normalize a frontmatter field to a list of strings.

    Handles: None, [], "string", ["a", "b"], and mixed types.
    """
    if not val:
        return []
    if isinstance(val, str):
        return [val]
    if isinstance(val, list):
        return [str(v) for v in val if v is not None]
    return []


def extract_file_refs(items):
    """Extract .md filename references from a list, filtering out Notion URLs."""
    return [
        f
        for f in normalize_list(items)
        if isinstance(f, str) and f.endswith(".md") and "notion.so" not in f
    ]


def extract_notion_refs(items):
    """Extract Notion URL references from a list."""
    return [
        f for f in normalize_list(items) if isinstance(f, str) and "notion.so" in f
    ]


def extract_related_findings(items):
    """Extract related_findings entries (list of {file, rel} dicts or plain strings)."""
    if not items:
        return []
    result = []
    for item in items:
        if isinstance(item, dict) and "file" in item:
            result.append({"file": item["file"], "rel": item.get("rel", "unknown")})
        elif isinstance(item, str) and item.endswith(".md"):
            result.append({"file": item, "rel": "untyped"})
    return result


def build_source_map(sources_dir=None):
    """Build a map of all research source files.

    Returns: {filename: {name, url, source_type, status, relevance, tags,
              key_takeaways, findings_files, findings_notion, authority}}
    """
    d = sources_dir or SOURCES_DIR
    sources = {}
    for fn in os.listdir(d):
        if fn == "_index.md" or not fn.endswith(".md"):
            continue
        fm, _ = parse_frontmatter(d / fn)
        findings_raw = fm.get("findings", []) or []
        sources[fn] = {
            "name": fm.get("name", "") or "",
            "url": fm.get("url", "") or "",
            "source_type": fm.get("source_type", "") or "",
            "status": fm.get("status", "") or "",
            "relevance": fm.get("relevance", "") or "",
            "tags": normalize_list(fm.get("tags")),
            "key_takeaways": (fm.get("key_takeaways", "") or "")[:300],
            "findings_files": extract_file_refs(findings_raw),
            "findings_notion": extract_notion_refs(findings_raw),
            "authority": normalize_list(fm.get("authority")),
            "notion_id": fm.get("notion_id", "") or "",
        }
    return sources


def build_finding_map(findings_dir=None):
    """Build a map of all research finding files.

    Returns: {filename: {name, category, summary, evidence_strength, adoption_status,
              priority, applicability, sources_files, sources_notion,
              related_findings, date_discovered, last_updated}}
    """
    d = findings_dir or FINDINGS_DIR
    findings = {}
    for fn in os.listdir(d):
        if fn == "_index.md" or not fn.endswith(".md"):
            continue
        fm, _ = parse_frontmatter(d / fn)
        sources_raw = fm.get("sources", []) or []
        findings[fn] = {
            "name": fm.get("name", "") or "",
            "category": fm.get("category", "") or "",
            "summary": (fm.get("summary", "") or "")[:200],
            "evidence_strength": fm.get("evidence_strength", "") or "",
            "adoption_status": fm.get("adoption_status", "") or "",
            "priority": fm.get("priority") or "",
            "applicability": normalize_list(fm.get("applicability")),
            "sources_files": extract_file_refs(sources_raw),
            "sources_notion": extract_notion_refs(sources_raw),
            "related_findings": extract_related_findings(
                fm.get("related_findings", [])
            ),
            "date_discovered": fm.get("date_discovered", "") or "",
            "last_updated": fm.get("last_updated", "") or "",
            "notion_id": fm.get("notion_id", "") or "",
        }
    return findings


def write_frontmatter(filepath, fm, body):
    """Write YAML frontmatter + body back to a markdown file.

    Args:
        filepath: Path to the markdown file.
        fm: Dict of frontmatter fields.
        body: Everything after the closing --- (including leading newline).

    Validates the output parses correctly. Raises ValueError on invalid YAML.
    """
    fm_str = yaml.dump(
        fm,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=200,
    )
    output = f"---\n{fm_str}---{body}"

    # Validate before writing
    round_trip_fm = yaml.safe_load(fm_str)
    if round_trip_fm is None:
        raise ValueError(f"Frontmatter round-trip produced None for {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output)


def file_exists(filename, directory):
    """Check if a referenced .md file actually exists in the given directory."""
    return (Path(directory) / filename).exists()
