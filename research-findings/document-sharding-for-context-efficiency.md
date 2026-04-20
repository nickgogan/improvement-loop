---
name: Document Sharding for Context Efficiency
summary: Splitting large documentation artifacts into small, focused shard files (coding-standards.md, tech-stack.md, source-tree.md, individual story files) so each agent loads only what it needs. BMad
  Method uses a /shard command to auto-split PRDs and architecture docs.
implementation_notes: MetaSystem's fractal pattern (DD-52) already produces focused, role-specific files. The explicit /shard command for auto-splitting larger artifacts could be valuable for skill files
  and governance docs.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: progressive-skill-loading.md
  rel: same-problem
- file: progressive-tiered-context-loading-convergence.md
  rel: extended-by
- file: three-tier-progressive-context-loading.md
  rel: same-problem
- file: step-file-micro-architecture.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
# Document Sharding for Context Efficiency

## What It Is
Large docs (PRDs, architecture specs) are broken into focused shards: coding-standards.md, tech-stack.md, source-tree.md, and individual epic/story files. Developer agents load only the files relevant to their current task. BMad Method provides a /shard command for auto-splitting. Brian (BMad) claims 90% token savings from sharding vs loading full documents.

## Why It Matters
Context windows are the critical constraint. Loading a full PRD when the developer only needs coding standards wastes tokens and degrades output quality. Sharding aligns context loading with actual information needs.

## Why People Are Using It
Core pattern in BMad Method v6 (43.7K GitHub stars). Practical token savings demonstrated in the masterclass video.

## Potential Alternatives
- Full document loading with manual extraction.
- RAG-based retrieval of relevant sections.
- Hierarchical document references.

## Potential Improvements
- Dynamic shard loading based on task context.
- Automated shard refresh when source documents change.
- Cross-shard consistency validation.

## Potential Failure Modes
Over-sharding creates too many small files. Cross-shard dependencies missed when loading individual shards. Shard drift when source docs are updated but shards aren't re-generated.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[document-sharding-for-context-efficiency]] in `extracts/patterns/`
