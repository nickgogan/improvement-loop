---
notion_id: 32b1e08b-9b34-818b-bf02-cbd135c98d61
name: Stacking PAUL with Carl for Domain-Scoped Project Knowledge
summary: 'PAUL and Carl can be run together: Carl manages dynamic domain-based rule loading within the project while PAUL manages the sequential phase architecture. Projects initialized with PAUL can substitute
  a Carl-managed CLAUDE.md structure in place of a monolithic project file.'
implementation_notes: null
category: Context Engineering
evidence_strength: Weak (theoretical)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- why-your-coding-agent-keeps-getting-dumber.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: multi-client-context-isolation-with-shared-skills.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Stacking PAUL with Carl for Domain-Scoped Project Knowledge

## What It Is
When initializing a PAUL project (/paul init), if no CLAUDE.md exists, the developer can install Carl to create domain-specific knowledge files for the project instead. Carl dynamically loads only the relevant rules (e.g., dev rules vs. content rules) while PAUL maintains phase continuity. The creator of PAUL and Carl is the same person, and a combined all-in-one solution is reportedly in development.

## Why It Matters
Long-running PAUL sessions accumulate context not just from the build itself but from the project's knowledge files. Without Carl, a monolithic project CLAUDE.md eats disproportionate context early in each phase. With Carl, only the domain-relevant rules load per task.

## Why People Are Using It
Power users running complex multi-domain SaaS builds (where the agent needs dev rules for some tasks and content/marketing rules for others) benefit from the combined stack.

## Potential Alternatives
Separate CLAUDE.md files per project phase; hierarchical CLAUDE.md with explicit section markers; manually pruned CLAUDE.md kept under 200 lines.

## Potential Improvements
The promised all-in-one combined plugin would eliminate the manual configuration of stacking two separate tools.

## Potential Failure Modes
Two plugins operating simultaneously on context management can produce conflicts if their rules interact unpredictably. Setup complexity increases for non-technical users.
