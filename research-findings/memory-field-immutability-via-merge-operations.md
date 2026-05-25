---
name: Memory Field Immutability via Merge Operations
summary: 'Schema-level merge_op field on memory templates controls how fields are updated: immutable (never overwrite), upsert (update in place), append (add to list). Prevents identity drift while allowing
  mutable fields to evolve.'
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: governance-memory-append-only-audit-layer.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: "classified"
---

## What It Is

A schema-level mechanism where each field in a memory template declares its merge operation: `immutable` (once written, cannot be overwritten — identity fields like `tool_name`, `case_name`), `upsert` (update in place — mutable fields like descriptions, preferences), or `append` (add to list — accumulative fields like evidence, examples). This is enforced at the storage layer, not via prompts. The result: identity-critical data is protected from drift while operational data can evolve freely.

## Why It Matters

The existing KB covers append-only audit layers for governance data. This pattern extends that concept to agent memory with field-level granularity. The problem it solves: agents that update their own memory can gradually drift their identity or overwrite critical context. Field-level immutability prevents this without making the entire memory read-only.

## Why People Are Using It

Observed in [OpenViking](https://github.com/volcengine/OpenViking) — see [[openviking-analysis]] for structural details. OpenViking's memory YAML schemas (`memory/tools.yaml`, `memory/identity.yaml`, etc.) define `merge_op` per field. The storage layer enforces these operations during `session.commit()` memory extraction.

## Potential Alternatives

- Full immutability (all memory is append-only)
- No enforcement (trust the LLM to respect field semantics)
- Version control on memory (keep all versions, allow rollback)

## Potential Improvements

Could add a `merge_op: supersede` option that archives the old value before overwriting — preserving history while allowing evolution. Maps to MetaSystem's DD-44 supersession pattern.

## Potential Failure Modes

- Schema complexity grows with many field types
- Immutable fields that need correction require manual intervention
- Merge operations must be defined at schema design time — hard to change later
