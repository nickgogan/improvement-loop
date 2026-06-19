---
notion_id: null
log_entry: "DD-60 through DD-64 created — agent team model formalized"
actor: "Nick + Agent: Claude"
area: null
change_type: "Design Decision"
milestone: null
rationale: "Derived 5 new DDs from agent-team-design-brief.md (Nick + Perplexity research). Scanned all 59 existing DDs for overlap before creating. Resolved 2 conflicts: communication model (markdown for non-HOS, Notion only for HOS runtime) and human gate stance (mandatory at milestones, free within)."
source_dd: "DD-60, DD-61, DD-62, DD-63, DD-64"
target_system: "Cross-System"
timestamp: "2026-04-06T00:00:00.000Z"
---

## What Changed

Five new Design Decisions created from the agent-team-design-brief.md:

| DD | Title | Extends |
|----|-------|---------|
| DD-60 | Composable Agent Team Model | DD-53 (agentic layer) |
| DD-61 | Milestone-Gated Development Loop | DD-29 (human gate, IL → cross-system) |
| DD-62 | Phased Quality Tiers (Explore / Harden) | DD-37 (start lean, refine later) |
| DD-63 | Artifact-Chain Communication | DD-35 (IL pipeline → cross-system) |
| DD-64 | Bootstrap Agent Team Instantiation | DD-49 (skill/template placement) |

## Conflicts Resolved

1. **Communication model:** agent-architecture.md described Notion-database-mediated communication. Per Nick: markdown artifact chains for all non-HOS work. Notion only for Household OS runtime. Future migration to real DB (not Notion). Added note to agent-architecture.md.
2. **Human gate:** agent-architecture.md said gates are "available but opt-out-able." Per Nick and DD-29 spirit: mandatory at milestone boundaries. Agents hand off freely within milestones. Human does E2E testing at milestone completion.

## Nick's Expanded Vision (beyond the original brief)

- Tester is a separate agent role (same competencies as engineers, different POV/incentives)
- Domain-specific engineers (backend, frontend, middleware) as separate agents
- Intra-milestone autonomy — agents work and test independently
- Testing hierarchy: agent self-tests → tester agent validates → human E2E at gate

## Affected Items

- `systems/meta-system/project-management/design-decisions/DD-60.md` through `DD-64.md` (new)
- `systems/meta-system/project-management/design-decisions/_index.md` (5 entries added)
- `CLAUDE.md` (DD count 59 → 64, cross-system count 22 → 27)
- `.claude/rules/governance.md` (DD count updated)
- `incubator/claude-build/CLAUDE.md` (DD count updated)
- `incubator/household-os/knowledge/reference/system-governance/agent-architecture.md` (DD-63/DD-61 notes added)
- `PROGRESS.md` (session history, current focus, what still needs work)
- `agent-team-design-brief.md` (archived)
