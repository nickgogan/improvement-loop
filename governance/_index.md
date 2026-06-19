---
title: "IL Governance"
type: "index"
target_system:
  - "improvement-loop"
tags:
  - "governance"
  - "improvement-loop"
---

# IL Governance

System-specific governance documents for the Improvement Loop (the engine). Derived from the charter and workspace operating law, and translated into operational rules by the Owner agent.

## Purpose

This directory holds governance artifacts that are specific to the engine — rules, policies, and constraints that operationalize the charter (`CHARTER.md`) and workspace operating law (`CLAUDE.md`, `.claude/rules/`) for the research-pipeline context.

## What Belongs Here

- System-specific operational rules derived from the constitution
- Drift reports produced by the Owner agent
- Structural proposals awaiting human approval
- System-specific policy documents

## What Does NOT Belong Here

- Vision, values, trajectory signals → `CHARTER.md` (workspace root)
- Design Decisions → `project-management/design-decisions/`
- Implementation Backlog items → `project-management/implementation-backlog/`
- System Log entries → `operations/system-log/`

## Current Contents

### Root — ratified governance rules

| File | Purpose | Source |
|------|---------|--------|
| `boundary-rules.md` | What IL can/cannot modify, cross-system constraints, artifact placement (four-zone) | Constitution, DD-89 |
| `pipeline-rules.md` | How IL work flows through DBDO, human gates, stage boundaries, SL telemetry | Constitution, Principles, DD-90 |
| `agent-rules.md` | Agent boundaries, handoff requirements, agent-as-directory, agent-private reflections, proposal pathways, generator-assessor separation, abstractions-must-earn-their-keep, audit-design symmetry | Constitution, Fractal Pattern, Vocabulary, DD-89, DD-91 |
| `knowledge-rules.md` | KB management, terminology, evidence tracking, structural memory | Constitution, Values, Vocabulary |

### `proposals/` — agent-authored governance-rule proposals (Proposal-First tier)

Per DD-89 (four-zone architecture) and DD-91 (reflections-to-proposals), this subfolder holds **agent-initiated** proposals — output from `/solicit-proposals` rounds (structured) or ad-hoc proposals raised by an individual agent (unstructured). Both pathways land here; both face Nick's review at acceptance time; accepted proposals convert to IB items or become DDs. Owner + Nick collaborative governance work bypasses this path and writes DDs directly — `governance/proposals/` is not the home for Owner's own drafts when he and Nick are co-authoring governance.

## Owner

The Owner agent (`agents/owner/agent.md`) is responsible for creating and maintaining content in this directory. Use `/translate-governance` to refresh translations and detect drift against source governance. Use `/solicit-proposals` to run reflection rounds that seed agent-initiated proposals.
