---
notion_id: null
log_entry: "Session 127: frontmatter/YAML hygiene sweep — 40 parse failures fixed, 4 pipeline_status backfilled"
actor: "Agent: Claude"
area: null
change_type: "Data Integrity"
milestone: null
rationale: "Session 127 closed its two assigned residuals, then Nick asked to run the session-128 frontmatter/YAML hygiene sweep in-round. The IB-157 parse failure surfaced during the DD-113 migration was the seed; a full-corpus scan (1973 files, PyYAML) found 40 frontmatter parse failures in three defect classes: (A) unquoted prose scalars containing ': ' parsed as nested mappings (summary/key_takeaways/log_entry/rationale/notes), (B) mixed-indentation/duplicate simple lists (consumed_by), (C) multi-line unquoted scalars whose continuation held a colon. A field-aware fixer (closed-key-set tokenizer over each corpus's legit keys) rewrote ONLY the offending field per file — prose -> literal block scalar (|-), simple lists -> normalized deduped 2-space quoted lists — leaving every other field byte-identical. All 40 validated; 0 parse failures remain corpus-wide. Schema-conformance pass was clean except 4 research-findings missing the required pipeline_status; backfilled to 'raw' (evidence: zero downstream signals — no consumed_by/proposals/adopted_in — matches the raw definition). The one-off fixer script was removed (Rule 11)."
source_dd: "DD-92"
target_system: "improvement-loop"
date: "2026-06-21"
---

## What Changed

- **40 frontmatter parse failures fixed** across system-log (5), implementation-backlog (1, IB-157), research-findings (33), research-sources (1). Each fix rewrote only the broken field; content preserved verbatim (prose → block scalar; soft-wrapped multi-line prose joined; duplicate list items deduped).
- **4 research-findings backfilled** `pipeline_status: "raw"` (were missing the required field; no downstream pipeline signals).
- Corpus-wide re-scan: **0 parse failures** remaining; schema-conformance otherwise clean (source_dd uniform per DD-113, no stray ib_items, DD status CV valid, required fields present).

## Defect classes (for upstream prevention)

The recurring root cause is extraction-time emission of **unquoted prose scalars** that contain colons/quotes, and **mixed-indent lists**. Positive-space fix for the future: the extraction/codification path (e.g. kb_parser write_frontmatter, /extract-artifacts) should emit prose fields as literal block scalars and lists with uniform indentation, so valid YAML is produced at write time rather than patched downstream. Not mechanized this round (first concentrated occurrence; Rule 11).
