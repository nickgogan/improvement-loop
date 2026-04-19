---
notion_id: null
log_entry: "IL skills moved to system-scoped directory (DD-49 executed)"
actor: "Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "15 IL skills (11 Researcher + 3 Codifier + 1 deprecated) moved from root .claude/skills/ to systems/improvement-loop/.claude/skills/. First execution of DD-49's mandate that root skills hold only cross-system utilities. 12 cross-system skills remain at root."
source_dd: "DD-49"
target_system: "improvement-loop"
timestamp: "2026-04-19T00:00:00.000Z"
---

## What Changed

- Created `systems/improvement-loop/.claude/skills/` directory
- Moved 15 skill directories from `.claude/skills/` to `systems/improvement-loop/.claude/skills/`:
  - Researcher intake/monitoring (7): research-loop, source-triage, watch-upstream, watch-blogs, transcript-fetcher, perplexity-research, repo-analyzer
  - Researcher KB maintenance (4): promote-findings, linkage-repair, finding-crosslink, dimension-rebalance
  - Codifier (3): identify-artifacts, extract-artifacts, synthesize-guide
  - Deprecated (1): research-proposer
- 12 cross-system skills remain at root: bootstrap, dd, governance-audit, ib, pdf-to-markdown, preflight, prompt-enhancer, prompt-evaluator, session-handoff, simplify-context, sl, track
- Updated IL CLAUDE.md skill path reference and root CLAUDE.md skills description

## Affected Items

- `systems/improvement-loop/.claude/skills/` (15 directories)
- `.claude/skills/` (12 directories remain)
- `systems/improvement-loop/CLAUDE.md` (path reference updated)
- `CLAUDE.md` (skills note updated)
