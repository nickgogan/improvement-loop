---
notion_id: null
log_entry: "Cross-repo comparison regenerated: 7→10 repos, 6 new cross-repo findings"
actor: "Nick + Agent: Claude"
area: null
change_type: "Documentation Update"
milestone: null
rationale: "Archon (v0.3.2), n8n (v2.16.0), and LangGraph (v1.1.6) were analyzed in session 16 but the cross-repo comparison still only covered the original 7 repos. Regenerated the full comparison to incorporate all 10, producing 6 new cross-repo findings candidates and updating all comparison matrices."
source_dd: "DD-45, DD-46"
target_system: "improvement-loop"
date: "2026-04-09"
---

## What Changed

Regenerated `watched-libraries/analysis/cross-repo-comparison.md` with all 10 watched libraries (was 7). All comparison matrices expanded to 10 columns. Pattern clusters, heat map, and contradictory approaches updated.

**6 new cross-repo findings candidates (CR-9 through CR-14):**

- **CR-9**: DAG vs BSP — two graph-based orchestration models (Archon YAML DAGs vs LangGraph Pregel BSP)
- **CR-10**: Cross-platform context file strategy (3 repos, 3 different approaches)
- **CR-11**: Specification-as-governance — a fourth enforcement philosophy (LangGraph conformance tests, n8n spec-driven development)
- **CR-12**: Per-node tool restrictions as workflow-level governance (Archon)
- **CR-13**: Immutable sessions as audit architecture (Archon)
- **CR-14**: Monorepo context distribution — three strategies (n8n per-package, Archon path-scoped rules, LangGraph single global)

**Key analytical updates:**
- Three architectural classes (was two) — added "markdown-parity" for Archon/gstack
- Governance philosophies expanded from 3 to 4 (specification-based added)
- Orchestration spectrum now has DAG and BSP as formal poles, not just ad-hoc patterns
- Sandboxing dimension strengthened by Archon's IsolationResolver and n8n's task-runner

## Affected Items

- `systems/improvement-loop/watched-libraries/analysis/cross-repo-comparison.md` — full rewrite
- `systems/improvement-loop/watched-libraries/analysis/_index.md` — updated comparison description
