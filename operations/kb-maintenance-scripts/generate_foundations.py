#!/usr/bin/env python3
"""
Generate FOUNDATIONS.md — the spine map of foundational Design Decisions (DD-115).

Scans all DD files for `foundational: true` and renders a terse, navigable map
(DD id + title + category + path). The DD files remain canonical; this file is a
DERIVED VIEW, regenerated from frontmatter — never hand-edited.

Usage:
    python3 generate_foundations.py            # (re)write FOUNDATIONS.md
    python3 generate_foundations.py --check     # exit 1 if FOUNDATIONS.md is stale

Exit code (--check): 0 = up to date; 1 = stale (re-run without --check).
"""
import sys
from pathlib import Path

from kb_parser import ROOT, parse_frontmatter

OUT = ROOT / "systems/improvement-loop/governance/FOUNDATIONS.md"
DD_GLOB = "systems/*/project-management/design-decisions/DD-*.md"

HEADER = """\
# FOUNDATIONS — the engine's spine

> **GENERATED — do not edit by hand.** This file is a derived view, rebuilt from DD
> frontmatter by `operations/kb-maintenance-scripts/generate_foundations.py`. To change
> what appears here, set `foundational: true` (or remove it) on the DD itself, then
> regenerate. A pre-commit check fails if this file drifts from the DD flags.
>
> **The DD files are canonical.** If this map and a DD ever disagree, the DD wins.

The load-bearing decisions that define what this system *is* and how it works — read
these first to orient, out of the full DD corpus. Each row links to the canonical DD.
To see the complete set, filter DD frontmatter (`rg -l 'foundational: true'`).

## What earns a `foundational: true` flag (DD-115)

**Litmus test:** if someone had *not* read this DD, would they get the system's
identity, architecture, governance, or core operating model wrong — or just make a
*local, procedural* mistake? Foundational = the former. Orientation, not importance.

**Include** if it fills one role (and shows ≥2 corroborating signals — cited in
CHARTER/CLAUDE/rules, high inbound DD-reference count, scope ∈ Principle/Structure/
Infrastructure/Governance):
- **C1 Identity & architecture** — what the system is / its top-level shape.
- **C2 Non-negotiable governance constraint** — a rule binding every session.
- **C3 Primary actors & interaction model** — who/what does the work.
- **C4 Core value flow** — the pipeline the system exists to run.
- **C5 Load-bearing substrate / ownership boundary** — infra everything sits on; who owns what.

**Exclude** even if Binding + important:
- **X1** procedural "how one part works" (needed only when touching that part)
- **X2** data-integrity / format rule (hit when *writing data*, not *understanding the system*)
- **X3** narrow component/feature addition (one dimension/skill/field/pathway)
- **X4** tuning / threshold change
- **X5** superseded (auto-dropped by the `status == Binding` filter)

**Meta-guard:** the spine's value is being small. Cap ~15–20. A new flag must clear the
bar cleanly **or displace the weakest current member** — it is not additive-by-default.
Past ~20, the test has gone loose; re-tighten rather than expand.

"""


def dd_num(decision_id):
    digits = "".join(c for c in str(decision_id) if c.isdigit())
    return int(digits) if digits else 0


def collect():
    rows = []
    for p in sorted(ROOT.glob(DD_GLOB)):
        fm, _ = parse_frontmatter(p)
        if not fm.get("foundational"):
            continue
        if str(fm.get("status", "")).strip().lower() != "binding":
            continue  # superseded DDs drop out of the spine automatically
        rows.append({
            "id": str(fm.get("decision_id") or p.stem),
            "title": str(fm.get("title") or "").strip(),
            "category": str(fm.get("scope_category") or "").strip(),
            "path": str(p.relative_to(ROOT)),
        })
    rows.sort(key=lambda r: dd_num(r["id"]))
    return rows


def render(rows):
    lines = [HEADER, "| DD | Title | Category | Canonical file |",
             "|----|-------|----------|----------------|"]
    for r in rows:
        title = r["title"].replace("|", "\\|")
        lines.append(f"| {r['id']} | {title} | {r['category']} | `{r['path']}` |")
    lines.append("")
    lines.append(f"_Spine: {len(rows)} foundational DDs._")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    rows = collect()
    content = render(rows)
    if "--check" in argv[1:]:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != content:
            sys.stderr.write(
                "FOUNDATIONS.md is stale relative to DD `foundational` flags.\n"
                "Run: python3 operations/kb-maintenance-scripts/generate_foundations.py\n"
            )
            return 1
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(rows)} foundational DDs).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
