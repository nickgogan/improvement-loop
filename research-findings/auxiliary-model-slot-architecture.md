---
name: Auxiliary Model Slot Architecture for Per-Task Routing
summary: Expose per-task-type model slots in configuration (main, compression, vision, summarization, approval, router, title, skills), enabling cheap models on non-critical subtasks while preserving quality
  on core reasoning. This is a first-class config schema pattern — not a runtime heuristic or ad-hoc override. Hermes implements this as a YAML config with named slots, each defaulting to the main model
  but overridable.
implementation_notes: 'MetaSystem''s GSD skill system uses model profiles (quality/balanced/budget) but routes at the agent level, not the task level. This finding suggests finer-grained routing: compression
  and title generation on Haiku, main reasoning on Opus, vision tasks on a specialized model. The config schema approach (named slots in YAML) is more maintainable than runtime routing logic.'
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- hermes-agent-nousresearch-analysis.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-24'
related_findings:
- file: model-tier-routing-expensive-orchestrator-cheap-s.md
  rel: extends
- file: multimodel-routing-architecture-specialized.md
  rel: extends
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: same-problem
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "rules/declare-model-slots-in-config.md"
tags:
- agent-design
- model-selection
- configuration
---

# Auxiliary Model Slot Architecture for Per-Task Routing

## What It Is

A configuration schema pattern: named model slots for different task types within an agent system. Hermes defines slots for: `main`, `compression`, `vision`, `summarization`, `approval`, `router`, `title`, `skills`. Each slot defaults to the main model but can be overridden with a cheaper/specialized model. The routing is declarative (YAML config), not programmatic (runtime routing logic).

## Why It Matters

Different agent subtasks have vastly different quality requirements. Compression and title generation tolerate a fast, cheap model. Approval gating and core reasoning require the best available model. Fixed per-task slots eliminate the need for runtime quality estimation — the builder decides upfront which tasks justify premium models.

## How It Could Fail

The slot taxonomy (main, compression, vision, etc.) is specific to Hermes. Different agent architectures may need different slot types. Over-splitting into too many slots creates configuration overhead. Under-splitting misses cost savings.
