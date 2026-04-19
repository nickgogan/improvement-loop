---
name: Artifact-as-Contract Pattern
summary: In GSD, templates define artifact schemas (PLAN.md, SUMMARY.md, VERIFICATION.md) that serve as inter-phase communication contracts — each artifact is both the output of one phase and the input
  contract for the next, eliminating the need for inter-agent messaging infrastructure.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: spec-as-source-of-truth-for-agent-construction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Artifact-as-Contract Pattern

## What It Is
GSD defines templates that specify the schema for each phase artifact: CONTEXT.md, RESEARCH.md, PLAN.md, SUMMARY.md, and VERIFICATION.md. Agents in each phase produce artifacts matching these templates. Downstream agents validate their inputs against the expected schema before proceeding. The artifact IS the communication protocol — no message passing, no shared memory, no event bus needed. The file system becomes the message bus. The chain flows: CONTEXT.md → RESEARCH.md → PLAN.md → SUMMARY.md → VERIFICATION.md.

## Why It Matters
Inter-agent communication is one of the hardest problems in multi-agent systems. Message-passing requires protocol design, serialization, error handling, and state management. The artifact-as-contract pattern sidesteps all of this by making the output of each phase a well-defined file that the next phase reads. The contract is the file schema itself. If the file exists and matches the template, the handoff succeeded.

## Why People Are Using It
Observed in [GSD](https://github.com/gsd-build/get-shit-done) v1.33.0 — see [[gsd-analysis]] for structural details. GSD's entire multi-phase workflow (discuss → research → plan → execute → verify) communicates exclusively through these artifact files. Each agent reads the previous phase's artifact and writes its own. No shared state, no conversation threading between agents, no coordination infrastructure beyond the file system.

## Potential Alternatives
Shared memory / blackboard architectures where agents read and write to a common state store. Message-passing protocols (agent-to-agent direct communication). Database-backed state management with structured queries. Conversation threading where agents share a single conversation context.

## Potential Improvements
Schema validation tooling that automatically checks artifact completeness before the next phase starts. Artifact versioning so rollback is possible when a phase produces a malformed artifact. Partial artifact support for incremental progress within long phases. Metadata headers tracking which agent produced the artifact and when.

## Potential Failure Modes
Schema drift — if templates and agents evolve independently, artifacts may not match what downstream agents expect. Single point of failure — a corrupted or incomplete artifact blocks the entire pipeline. No partial progress visibility — either the artifact exists (phase done) or it does not (phase in progress), with no intermediate state.
