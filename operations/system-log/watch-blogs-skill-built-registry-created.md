---
notion_id: null
log_entry: "/watch-blogs skill built, watched-blogs registry created"
actor: "Nick + Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "Extended IL upstream monitoring from GitHub repos (/watch-upstream) to blogs and content sources. New skill mirrors watch-upstream's 7-step procedure but adapts for blog-specific concerns: RSS/Perplexity fetch, post-level tracking, relevance filters anchored to 10 research dimensions."
source_dd: null
target_system: "improvement-loop"
timestamp: "2026-04-09T00:00:00.000Z"
---

## What Changed

- Created `/watch-blogs` skill in `.claude/skills/watch-blogs/SKILL.md` — 7-step procedure: scope → load → fetch → triage report → create sources → update entries → summary
- Created `systems/improvement-loop/watched-blogs/` directory with `_index.md` catalog
- Registered `watched-blogs/` in `systems/improvement-loop/CLAUDE.md` "What Lives Here" table
- Skill uses parallel subagents (batches of 3-4) with RSS-first, Perplexity fallback, WebFetch last resort
- Supports `--all`, `--dry-run`, and explicit blog name arguments

## Affected Items

- `.claude/skills/watch-blogs/SKILL.md` — new skill
- `systems/improvement-loop/watched-blogs/_index.md` — new catalog
- `systems/improvement-loop/CLAUDE.md` — updated
