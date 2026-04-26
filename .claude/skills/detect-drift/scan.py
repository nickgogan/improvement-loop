#!/usr/bin/env python3
"""
detect-drift enumeration helper.

Codifies Steps 1-2 of /detect-drift (enumeration + frontmatter parse + source resolution
+ strict-greater-than date compare). The LLM-driven steps (recommendation per hit, report
construction) remain in the skill body.

Read-only: never modifies any artifact, finding, or other file outside the output JSON.

Reads from cwd-relative paths:
  - extracts/{rules,skills,templates,agents}/*.md
  - research-findings/*.md

Invocation (from systems/improvement-loop/):

    python3 .claude/skills/detect-drift/scan.py \
        [--include rules,skills,...] [--exclude ...] \
        --context "<invocation_context>" \
        [--out /tmp/drift-scan-<date>.json]

Prints the output JSON path on stdout. JSON shape — see the `scan` function below.
"""

import argparse
import json
import os
import re
import sys
from datetime import date

VALID_FORMS = {"rules", "skills", "templates", "agents"}
ALL_FORMS = ["rules", "skills", "templates", "agents"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def strip_quotes(v: str) -> str:
    v = v.strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


def parse_frontmatter(path: str) -> dict:
    """Minimal YAML frontmatter parser sufficient for the flat scalars + simple lists
    used by IL findings and extracts. Handles single+double quote styles. Not a general
    YAML parser — does not handle nested mappings, anchors, multiline strings, etc."""
    try:
        with open(path) as f:
            content = f.read()
    except OSError:
        return {}
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = content[4:end]
    out: dict = {}
    current_key = None
    for line in fm.split("\n"):
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if m:
            k, v = m.group(1), strip_quotes(m.group(2))
            out[k] = v
            current_key = k
        elif line.startswith("  - ") and current_key:
            v = strip_quotes(line[4:])
            if not isinstance(out.get(current_key), list):
                out[current_key] = []
            out[current_key].append(v)
    return out


def scan(forms: list, invocation_context: str) -> dict:
    records = []
    enumeration_gaps = []
    unresolvable_sources = []
    quote_styles = {"double": 0, "single": 0, "unquoted": 0}

    for form in forms:
        form_dir = os.path.join("extracts", form)
        if not os.path.isdir(form_dir):
            continue
        for fname in sorted(os.listdir(form_dir)):
            if not fname.endswith(".md") or fname == "_index.md":
                continue
            artifact_path = os.path.join(form_dir, fname)
            artifact_stem = fname[:-3]
            fm = parse_frontmatter(artifact_path)

            with open(artifact_path) as f:
                raw_head = f.read(2000)
            m = re.search(r"^extraction_date:\s*(.*)$", raw_head, re.MULTILINE)
            if m:
                v = m.group(1).strip()
                if v.startswith('"'):
                    quote_styles["double"] += 1
                elif v.startswith("'"):
                    quote_styles["single"] += 1
                else:
                    quote_styles["unquoted"] += 1

            sf = fm.get("source_finding")
            ed = fm.get("extraction_date")
            af = fm.get("assigned_form")
            has_lifecycle_ptr = any(k.startswith("last_change_") for k in fm.keys())
            has_deployed = "deployed" in fm

            if not sf:
                enumeration_gaps.append({"path": artifact_path, "stem": artifact_stem, "reason": "missing source_finding"})
                continue
            if not ed:
                enumeration_gaps.append({"path": artifact_path, "stem": artifact_stem, "reason": "missing extraction_date"})
                continue
            if not DATE_RE.match(ed):
                enumeration_gaps.append({"path": artifact_path, "stem": artifact_stem, "reason": f"malformed extraction_date: {ed!r}"})
                continue
            records.append({
                "path": artifact_path,
                "stem": artifact_stem,
                "form": form,
                "source_finding": sf,
                "extraction_date": ed,
                "assigned_form": af,
                "has_lifecycle_ptr": has_lifecycle_ptr,
                "has_deployed": has_deployed,
            })

    drift_hits = []
    clean_count = 0
    findings_with_legacy_updated = []

    for rec in records:
        sf_path = os.path.join("research-findings", rec["source_finding"] + ".md")
        if not os.path.isfile(sf_path):
            unresolvable_sources.append({
                "path": rec["path"], "stem": rec["stem"],
                "source": rec["source_finding"], "reason": "finding-file-not-found",
            })
            continue
        sf_fm = parse_frontmatter(sf_path)
        last_updated = sf_fm.get("last_updated")
        has_legacy_updated = "updated" in sf_fm
        if has_legacy_updated:
            findings_with_legacy_updated.append({
                "finding": rec["source_finding"], "legacy_updated": sf_fm.get("updated"),
            })
        if not last_updated:
            unresolvable_sources.append({
                "path": rec["path"], "stem": rec["stem"], "source": rec["source_finding"],
                "reason": f"missing-last-updated (legacy 'updated' present: {has_legacy_updated})",
            })
            continue
        if not DATE_RE.match(last_updated):
            unresolvable_sources.append({
                "path": rec["path"], "stem": rec["stem"], "source": rec["source_finding"],
                "reason": f"malformed last_updated: {last_updated!r}",
            })
            continue
        rec["source_last_updated"] = last_updated
        if last_updated > rec["extraction_date"]:
            drift_hits.append(rec)
        else:
            clean_count += 1

    per_form = {}
    for form in forms:
        form_recs = [r for r in records if r["form"] == form]
        form_hits = [r for r in drift_hits if r["form"] == form]
        per_form[form] = {"scanned": len(form_recs), "drift_hits": len(form_hits)}

    mismatches = []
    for r in records:
        expected = r["form"][:-1]
        if r.get("assigned_form") and r["assigned_form"] != expected:
            mismatches.append({
                "path": r["path"], "assigned_form": r["assigned_form"], "expected": expected,
            })

    return {
        "scan_date": date.today().isoformat(),
        "invocation_context": invocation_context,
        "forms_scanned": forms,
        "total_scanned": len(records),
        "drift_hits": drift_hits,
        "clean_count": clean_count,
        "enumeration_gaps": enumeration_gaps,
        "unresolvable_sources": unresolvable_sources,
        "per_form": per_form,
        "smoke_test_signals": {
            "lifecycle_ptr_present": sum(1 for r in records if r.get("has_lifecycle_ptr")),
            "lifecycle_ptr_total": len(records),
            "deployed_marker_present": sum(1 for r in records if r.get("has_deployed")),
            "findings_with_legacy_updated": findings_with_legacy_updated,
            "form_dir_mismatches": mismatches,
            "extraction_date_quote_styles": quote_styles,
        },
    }


def main() -> int:
    p = argparse.ArgumentParser(description="detect-drift enumeration helper.")
    p.add_argument("--include", help="Comma-separated forms to include (rules,skills,templates,agents).")
    p.add_argument("--exclude", help="Comma-separated forms to exclude. Cannot combine with --include.")
    p.add_argument("--context", default="manual scan", help="Invocation-context tag for the report.")
    p.add_argument("--out", help="Output JSON path. Default: /tmp/drift-scan-<date>.json")
    args = p.parse_args()

    if args.include and args.exclude:
        p.error("--include and --exclude cannot both be passed.")

    if args.include:
        forms = [f.strip() for f in args.include.split(",") if f.strip()]
    elif args.exclude:
        excl = {f.strip() for f in args.exclude.split(",") if f.strip()}
        forms = [f for f in ALL_FORMS if f not in excl]
    else:
        forms = list(ALL_FORMS)

    bad = [f for f in forms if f not in VALID_FORMS]
    if bad:
        p.error(f"invalid form value(s): {bad}. valid: {sorted(VALID_FORMS)}")

    out_path = args.out or f"/tmp/drift-scan-{date.today().isoformat()}.json"

    result = scan(forms, args.context)

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
