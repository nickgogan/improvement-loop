---
name: linkage-repair
description: >-
  Audit and repair bidirectional links between research sources and findings in the
  Improvement Loop KB. Detects unlinked findings, orphaned sources, and broken references.
  Use after bulk extraction, backfill sessions, or when the source quality audit flags
  linkage gaps. Produces a repair report and optionally executes fixes.
user-invocable: true
allowed-tools: Read Grep Glob Edit
argument-hint: "[--dry-run] [--sources-only] [--findings-only]"
---

# Linkage Repair

Audit and repair bidirectional links between research sources and research findings in the Improvement Loop knowledge base.

## When to Use This Skill

- After a bulk extraction or backfill session that created many findings
- When the source quality audit flags linkage gaps
- After migrating data from Notion or other systems
- Periodically as KB maintenance (e.g., monthly)
- When a source shows 0 findings but you suspect findings exist for it

## The Problem

The KB has two link directions that should be consistent:

1. **Source → Findings:** Each source file has a `findings:` array listing finding filenames
2. **Finding → Sources:** Each finding file has a `sources:` array listing source filenames

These get out of sync when:
- Findings are created without updating the source's `findings:` array
- Sources are created without linking to existing findings
- Findings reference sources by Notion URL instead of filename
- Bulk operations skip the linkage step

## Procedure

### Step 0: Parse Arguments

- `--dry-run`: Report gaps but don't fix anything. Default behavior if no flag specified.
- `--sources-only`: Only check source → finding links (faster, narrower scope)
- `--findings-only`: Only check finding → source links
- No flag: Check both directions and execute repairs after confirmation

### Pre-step: Script-Based Analysis (Recommended)

Run the KB maintenance scripts to get structured gap data, replacing 300+ individual file reads:

```bash
python3 systems/improvement-loop/operations/kb-maintenance-scripts/linkage_analyzer.py --json
```

This outputs a JSON object with `orphaned_findings`, `unlinked_sources`, `asymmetric_links`, `broken_references`, and `notion_authority_refs`. Parse this output and skip Steps 1-3 below — jump directly to Step 4 (Content Matching) or Step 5 (Report).

For a quick text summary first: run without `--json`.

If the scripts are unavailable, fall back to the manual procedure below.

### Step 1: Build the Source Map

1. Use `Glob` to list all `.md` files in `systems/improvement-loop/research-sources/` (excluding `_index.md`).
2. For each source file, use `Grep` or `Read` to extract:
   - `name:` field
   - `findings:` array (list of finding filenames)
   - `url:` field (needed for reverse matching)
   - `key_takeaways:` field (needed for content matching)
3. Build a lookup: `{ source_filename → { name, url, linked_findings[] } }`

### Step 2: Build the Findings Map

1. Use `Glob` to list all `.md` files in `systems/improvement-loop/research-findings/` (excluding `_index.md`).
2. For each finding file, use `Grep` or `Read` to extract:
   - `name:` field
   - `sources:` array (list of source filenames)
   - Body text (first ~20 lines after frontmatter for content matching)
3. Build a lookup: `{ finding_filename → { name, linked_sources[] } }`

### Step 3: Detect Gaps

Run three checks:

**Check A — Orphaned findings (finding has no sources linked):**
- Finding has `sources: []` or `sources:` is missing/empty
- These findings exist in the KB but aren't traceable to any source
- For each orphan, attempt content matching:
  - Search the finding's body for source names, URLs, or distinctive phrases
  - Search source `key_takeaways` for terms matching the finding's `name` or `summary`
  - If a likely match is found, flag it as a repair candidate

**Check B — Unlinked sources (source has findings but doesn't list them):**
- Source has `findings: []` but findings in the KB reference it in their `sources:` array
- Or: source has `findings: []` but content matching suggests findings exist for it

**Check C — Asymmetric links (one direction exists, other doesn't):**
- Source lists finding X in `findings:`, but finding X doesn't list source in `sources:`
- Finding lists source Y in `sources:`, but source Y doesn't list finding in `findings:`

### Step 4: Content Matching for Orphans

For findings with `sources: []`, attempt to match them to sources using these heuristics (in priority order):

1. **Name matching:** Does the finding's name contain keywords from a source's name?
   - Example: finding `tool-shaped-object-evaluation-lens.md` → source `tool-shaped-objects.md`
2. **URL matching:** Does the finding's body mention a URL that matches a source's `url:` field?
3. **Topic matching:** Does the finding's `summary` overlap significantly with a source's `key_takeaways`?
4. **Tag matching:** Does the finding's `category` align with a source's `tags`?

Assign confidence levels:
- **High:** Name substring match + topic overlap
- **Medium:** Topic overlap only, or tag match + partial name
- **Low:** Tag match only, or weak topic similarity

### Step 5: Report

Produce a structured report:

```markdown
## Linkage Repair Report — [Date]

### Summary
| Metric | Count |
|--------|-------|
| Total sources | X |
| Total findings | X |
| Orphaned findings (no sources) | X |
| Unlinked sources (no findings) | X |
| Asymmetric links | X |
| Repair candidates (high confidence) | X |
| Repair candidates (medium confidence) | X |

### High-Confidence Repairs (auto-fixable)
| Finding | Matched Source | Match Type | Confidence |
|---------|--------------|------------|------------|

### Medium-Confidence Repairs (review needed)
| Finding | Candidate Source | Match Type | Confidence | Notes |
|---------|-----------------|------------|------------|-------|

### Remaining Orphans (no match found)
| Finding | Category | Summary (truncated) |
|---------|----------|---------------------|

### Asymmetric Links
| Entity | Has Link To | Missing Reverse Link From |
|--------|-----------|--------------------------|
```

**Stop here if `--dry-run` was specified.**

### Step 6: Human Gate

Present the report. Wait for approval before executing repairs. The user may:
- Approve all high-confidence repairs
- Approve selectively
- Review medium-confidence matches before approving
- Reject all

### Step 7: Execute Repairs

For each approved repair:

**Adding finding to source's `findings:` array:**
1. Use `Read` to get current source file content
2. Use `Edit` to add the finding filename to the `findings:` array
3. Maintain alphabetical order in the array

**Adding source to finding's `sources:` array:**
1. Use `Read` to get current finding file content
2. Use `Edit` to add the source filename to the `sources:` array
3. Update `last_updated` to today

**Fixing asymmetric links:**
1. Identify which direction is missing
2. Add the missing reference using `Edit`

### Step 8: Summary

Report:
- Number of repairs executed
- Number of remaining orphans
- Number of remaining unlinked sources
- Suggestions for manual review

## Calibration Notes

- **Don't force matches.** If a finding genuinely came from a source not in the KB (e.g., a Perplexity search, a conversation, or background knowledge), it's OK for `sources: []` to remain empty. Not every finding traces to a file in `research-sources/`.
- **Prefer precision over recall.** A wrong link is worse than a missing link. Only auto-fix high-confidence matches.
- **Notion IDs are not filenames.** If a finding's `sources:` contains a Notion URL or ID instead of a filename, flag it for manual review rather than auto-fixing — the Notion reference may point to a different version of the source.
- **Index updates are optional.** This skill focuses on the source and finding files themselves. `_index.md` updates can be deferred to session end.
- **Batch efficiently.** Use `Grep` to scan many files at once rather than reading each file individually. The source and finding maps can be built with targeted greps for frontmatter fields.
