---
notion_id: null
log_entry: "Repo analysis findings promotion batch 2: 15 new findings from Archon, n8n, LangGraph + cross-repo"
actor: "Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "Second promotion batch completing the repo-analysis pipeline. 15 new findings created from remaining candidates (CR-10/12/13/14, 3 Archon, 5 n8n, 3 LangGraph). 12 candidates skipped as duplicates, 1 existing finding (DAG vs BSP) updated with typed channels detail. KB now at ~400 findings."
source_dd: "DD-45"
target_system: "improvement-loop"
date: "2026-04-09"
---

## What Changed

- Promoted 15 new findings from repo-analyzer analysis docs:
  - **Cross-repo (4):** CR-10 cross-platform context, CR-12 per-node tool restrictions, CR-13 immutable sessions, CR-14 monorepo context distribution
  - **Archon (3):** IsolationResolver algorithm, intent meta-routing skill, hook-based enforcement
  - **n8n (5):** plugin namespacing, janitor+TCR, security fix hygiene, PromptBuilder+Mermaid, CRDT-ready state management
  - **LangGraph (3):** interrupt/Command HITL primitives, tool injection via type annotations, auto-generated threat model
- Updated DAG vs BSP finding with typed channels as state primitives detail
- Skipped 12 candidates as duplicates of existing findings or cross-repo promotions
- Updated _index.md with 15 new rows
- Added back-links (→ Promoted to [[...]]) to all 4 analysis docs

## Affected Items

- `systems/improvement-loop/research-findings/` — 15 new files, 1 updated, _index.md updated
- `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` — 4 back-links added
- `systems/improvement-loop/watched-libraries/analysis/archon-analysis.md` — 3 back-links added
- `systems/improvement-loop/watched-libraries/analysis/n8n-analysis.md` — 5 back-links added
- `systems/improvement-loop/watched-libraries/analysis/langgraph-analysis.md` — 3 back-links added
