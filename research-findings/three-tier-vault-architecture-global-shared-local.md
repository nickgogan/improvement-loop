---
notion_id: 32b1e08b-9b34-8142-a4fd-f4808fb7db9f
name: Three-Tier Vault Architecture (Global/Shared/Local)
summary: 'A three-layer file system for Claude Code projects: Tier 1 (Global, ~/.claude/) for identity and universal skills; Tier 2 (Shared, git repo) for project reference files and playbooks; Tier 3 (Local,
  gitignored) for ephemeral state like PROGRESS.md, agent logs, and auth tokens.'
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- four-system-separation-session-research.md
proposals: null
date_discovered: '2026-03-16'
last_updated: '2026-04-19'
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
# Three-Tier Vault Architecture (Global/Shared/Local)

## What It Is
The vault is organized into three tiers with distinct sharing and persistence rules. Tier 1 (Global, `~/.claude/`) holds agent identity, core skills (`/bootstrap`, `/resume`, `/compress`, `/preserve`), and universal behaviors — it follows the developer across all projects. Tier 2 (Shared, git repo) holds project-specific reference files, patterns, and playbooks that any collaborator can clone. Tier 3 (Local, gitignored) holds mutable runtime state: PROGRESS.md, agent-log/, and credentials.

## Why It Matters
Without tiering, agents either over-share sensitive state or under-share reusable knowledge. This architecture gives each category of content the right persistence and visibility: global identity travels everywhere, shared reference libraries are portable, and ephemeral state stays private and local.

## Why People Are Using It
Community consensus across 14 observed videos validates this three-tier approach. The pattern allows a collaborator (e.g., JR) to clone Tier 2 and immediately have the same reference library — no manual onboarding. 38 files were generated across tiers in the S3 implementation.

## Potential Improvements
A Tier 2.5 layer — household-specific but shareable configs that sit between the universal global layer and the project-specific shared layer — could handle configurations relevant to a family or team without polluting the project repo.

## Potential Failure Modes
Tier 2 is vulnerable to bloat if reference files are added but never pruned. Over time, a crowded shared layer slows agent context loading and degrades relevance. Without a clear owner and review cadence, the shared repo accumulates stale playbooks.
