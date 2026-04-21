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

System-specific governance documents for the Improvement Loop. Derived from the MetaSystem constitution and translated into operational rules by the Owner agent.

## Purpose

This directory holds governance artifacts that are specific to the IL system — rules, policies, and constraints that operationalize MetaSystem's constitution for the research pipeline context. These are not MetaSystem-level governance (which lives in `systems/meta-system/governance/`), but IL-specific translations.

## What Belongs Here

- System-specific operational rules derived from the constitution
- Drift reports produced by the Owner agent
- Structural proposals awaiting human approval
- System-specific policy documents

## What Does NOT Belong Here

- MetaSystem-level governance (constitution, values, principles) → `systems/meta-system/governance/`
- Design Decisions → `project-management/design-decisions/`
- Implementation Backlog items → `project-management/implementation-backlog/`
- System Log entries → `operations/system-log/`

## Current Contents

### Root — ratified governance rules

| File | Purpose | Source |
|------|---------|--------|
| `boundary-rules.md` | What IL can/cannot modify, cross-system constraints | Constitution |
| `pipeline-rules.md` | How IL work flows through DBDO, human gates, stage boundaries | Constitution, Principles |
| `agent-rules.md` | Agent boundaries, handoff requirements, agent-as-directory | Constitution, Fractal Pattern, Vocabulary |
| `knowledge-rules.md` | KB management, terminology, evidence tracking, structural memory | Constitution, Values, Vocabulary |

### `proposals/` — Owner-authored governance-rule proposals

Proposal-First tier output per the Owner autonomy table. Contains tracking-mechanism proposals, DD proposals, amendment proposals, and drift reports with remediation plans. Each proposal is Owner-written and Nick-gated; ratified proposals migrate upstream into DDs, governance rules, or the implementation backlog. The session-50 four-zone architecture proposal (`proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md`) formalizes this subfolder's role.

## Owner

The Owner agent (`agents/owner/agent.md`) is responsible for creating and maintaining content in this directory. Use `/translate-governance` to refresh translations and detect drift against source governance.
