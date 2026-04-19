---
notion_id: 32b1e08b-9b34-8171-83ff-d850649fe62d
name: OpenSpec (YCombinator)
summary: Specification engineering framework that treats specs as living documents with 'spec deltas' tracking what requirements change. Brownfield-first — works on existing systems like the Household OS.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- openspec-ycombinator.md
proposals: []
date_discovered: '2026-03-09'
last_updated: '2026-04-19'
related_findings:
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# OpenSpec (YCombinator)

## What It Is
OpenSpec is a lightweight spec-driven planning layer for AI coding agents (works across Claude Code, Cursor, GitHub Copilot, 20+ tools natively). Its core innovation is the "spec delta" — diff-style requirement documents showing what changes, not what the full spec is.

**Spec structure:** Specs live in `openspec/specs/{feature}/spec.md` with Purpose, Requirements (using "SHALL" language), and Scenarios (GIVEN/WHEN/THEN format). Change proposals generate `openspec/changes/{change-id}/` with proposal.md, design.md, tasks.md, and affected spec diffs.

**Brownfield-first:** Designed for existing codebases. "Create specs as you need them" — no upfront comprehensive specification. Incremental spec creation reduces overhead for mature systems.

**Workflow:** `/openspec:proposal` reads existing specs + codebase, generates change proposal with implementation tasks before any code is written. Agent surfaces changes for review before executing.

## Why It Matters
Most AI-assisted build workflows treat specs as write-once inputs, leading to drift between the current system state and the documented spec over time. OpenSpec closes this loop by making requirement changes traceable, so any agent or human can reconstruct the current state of truth from a chain of deltas rather than a single monolithic document.

## Why People Are Using It
Practitioners working on brownfield systems — existing codebases or operating systems like the Household OS — need a way to evolve specs without rewriting them from scratch. The delta pattern maps naturally to how IBs are issued incrementally, and the tree-structured DD approach gives agents a navigable hierarchy rather than a flat document.

## Potential Improvements
Spec deltas could be auto-generated from IB execution logs rather than written by hand, closing the feedback loop fully. Integrating with a diff-aware retrieval system would allow agents to query only the deltas relevant to their current task without loading the full spec.

## Potential Failure Modes
Spec delta overhead can slow down simple IB items where the change is obvious and the bookkeeping cost exceeds the clarity benefit. If delta authoring is inconsistent or skipped under time pressure, the living document degrades into the same static artifact the pattern was meant to replace.
