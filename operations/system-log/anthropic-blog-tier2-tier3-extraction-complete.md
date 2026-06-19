---
notion_id: null
log_entry: "Tier 2 + Tier 3 Anthropic blog extraction complete — 15 posts, 25 new findings, 35 updated"
actor: "Nick + Agent: Claude"
area: null
change_type: "Research Intake"
milestone: null
rationale: "Completed extraction of remaining 15 Anthropic blog posts (11 Tier 2 engineering, 4 Tier 3 research) identified by /watch-blogs triage. Combined with prior Tier 1 session, all 21 EXTRACT posts from both Anthropic blogs are now processed into the KB."
source_dd: null
target_system: "improvement-loop"
timestamp: "2026-04-09T00:00:00.000Z"
---

## What Changed

### Extraction Summary

| Metric | Count |
|--------|-------|
| Posts processed | 15 |
| Source entries created | 15 |
| New findings created | 25 |
| Existing findings updated | 35 |
| Evidence upgrades (Medium → Strong) | 6 |
| Anthropic authority source_count | 8 → 23 |

### Combined Totals (Tier 1 + Tier 2 + Tier 3)

| Metric | Tier 1 | Tier 2+3 | Total |
|--------|--------|----------|-------|
| Posts | 6 | 15 | 21 |
| Sources created | 6 | 15 | 21 |
| New findings | 15 | 25 | 40 |
| Existing updated | 7 | 35 | 42 |

### New P1 Findings (actionable now)

- Think tool scratchpad for mid-chain reasoning (+76% pass@1)
- Eval awareness — autonomous benchmark identification
- Infrastructure noise as eval confound (6-point swings)
- File-based task locking for parallel agents
- Test output design for LLM context windows
- Effort scaling rules embedded in orchestrator
- Teach orchestrator to delegate pattern
- Progressive search: wide then narrow
- Incremental one-feature-per-session execution
- Programmatic tool calling (200KB → 1KB context)
- MCP as code API with progressive tool discovery (98.7% token reduction)
- OS-level agent sandboxing (84% permission prompt reduction)

### Key Themes

1. **Eval integrity under multi-vector attack** — gaming, infra noise, web contamination
2. **Layered defense convergence** — OS sandboxing + AI permission classification + allowlists
3. **Cross-vendor convergence on deferred tool loading** — Anthropic + OpenAI both shipped it
4. **Parallel agent coordination via filesystem** — git + file locks, no orchestrator needed
5. **Self-improving agents** — prompt and tool diagnosis loops closing (40% improvement)
6. **Internal state monitoring as safety frontier** — emotion vectors, model diffing

### Post Logs Updated

- `watched-blogs/anthropic-engineering.md` — 18 posts logged (17 source-created, 1 triaged-skip)
- `watched-blogs/anthropic-research.md` — 6 posts logged (4 source-created, 2 triaged-skip)

## Affected Items

- `research-findings/` — 25 new files, 35 updated
- `research-sources/` — 15 new Anthropic source entries
- `research-authorities/anthropic.md` — source_count 8 → 23, specialties expanded
- `watched-blogs/anthropic-engineering.md` — Post Log populated
- `watched-blogs/anthropic-research.md` — Post Log populated
