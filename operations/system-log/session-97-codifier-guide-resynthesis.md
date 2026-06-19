---
notion_id: null
log_entry: "Session 97: Codifier — 4-guide re-synthesis cycle (G3, G2, G5, G8)"
actor: "Nick + Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "83 newly classified pattern findings from sessions 95-96 triggered staleness threshold across all guide clusters. Prioritized by finding count delta — largest gaps first. 45 new findings absorbed across 4 guides."
source_dd: "DD-81, DD-93, DD-94, DD-98, DD-101"
target_system: "improvement-loop"
date: "2026-05-25"
---

## What Changed

Re-synthesized 4 guides incorporating 45 newly classified pattern findings:

| Guide | Prior | New | Total | Key Additions |
|-------|-------|-----|-------|---------------|
| G3 — Agent Architecture Decisions | 24 | +18 | 42 | Patterns G (Wave-Based Sub-Agent) + H (Review-Triggered Remediation); Step 3b (Execution Topology Selection); Key Concepts 9-11 (four-zone anatomy, sub-agent-as-tool, harness evolution); Pitfalls 12-13 |
| G2 — Managing Agent Context | 48 | +16 | 64 | Step 9 (Output Format Engineering); Anthropic 5-tool decision matrix; agentic RAG + summary-gate retrieval; multi-agent shared memory (Step 8g); Key Concepts 8-10; Pitfalls 18-20 |
| G5 — Designing Agent Tools | 16 | +7 | 23 | Steps 4 (Integration Layer — CLI vs MCP vs headless), 6 (Multi-Tool Composition), 8 (Tool Output Design), 12-13 (Skill Scoping/Portability); Key Concepts 10-12; Pitfalls 13-16 |
| G8 — Model-Resilient Prompt Engineering | 16 | +4 | 20 | Steps 6 (Output Format Controls), 10 (Metaprompting Loop); Output Grounding subsection; Templates 5-6; Pitfalls 10-12 |

Companion artifacts:
- 4 changelog entries written (DD-94)
- 1 split proposal emitted: G3 at 42 findings, 2+ practitioner questions → `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md` (Codifier rec: re-evaluate bifurcation)
- G3 harvest queue: +4 rows (2 rule, 1 template, 1 skill) per DD-101
- Routing table: 4 rows updated with new dates and finding counts
- 45 findings back-annotated: `pipeline_status: "synthesized"`, `consumed_by:` updated

## Affected Items

- `extracts/guides/agent-architecture-decisions.md` — rewritten (42 findings)
- `extracts/guides/managing-agent-context.md` — rewritten (64 findings)
- `extracts/guides/designing-agent-tools.md` — rewritten (23 findings)
- `extracts/guides/model-resilient-prompt-engineering.md` — rewritten (20 findings)
- `extracts/guides/changelog/agent-architecture-decisions.changelog.md` — new entry
- `extracts/guides/changelog/managing-agent-context.changelog.md` — new entry
- `extracts/guides/changelog/designing-agent-tools.changelog.md` — new entry
- `extracts/guides/changelog/model-resilient-prompt-engineering.changelog.md` — new entry
- `extracts/guides/agent-architecture-decisions.harvest-queue.md` — +4 rows
- `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md` — new
- `operations/references/guide-routing-table.md` — 4 rows updated
- 45 finding files in `research-findings/` — `pipeline_status` and `consumed_by` updated
