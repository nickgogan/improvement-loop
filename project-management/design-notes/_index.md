---
title: "IL Design Notes"
id: "il-design-notes-index"
type: "index"
category: "design-notes"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-22"
updated: "2026-04-22"
author: "owner"
source_dd:
  - "DD-52"
  - "DD-82"
  - "DD-86"
tags:
  - "design-notes"
  - "deliberative"
  - "project-management"
  - "moc"
  - "improvement-loop"
aliases:
  - "Design notes catalog"
---

# Improvement Loop — Design Notes

Deliberative specifications for IL pipeline mechanics, substrate architecture, read contracts, and classification rubrics. Not runtime event output (that lives in `operations/`); not ratified governance (that lives in `governance/`); not tracked work items (those live in `implementation-backlog/`). Design notes are the "what we're deciding and why" substrate.

## What belongs here

- **Substrate audits** — how dimensions, patterns, guides, and the Librarian relate.
- **Read contracts** — query-execution protocols for agents.
- **Use-case registries** — canonical enumerations of consumer demand (e.g., Librarian use cases).
- **Classification rubrics** — decision specs (Form Router, artifact acceptance).
- **Lifecycle specs** — artifact-state transition specifications.
- **Pipeline-mechanics proposals** — structural-change proposals (e.g., pipeline collapse).
- **Spot-check reports** — empirical validation of proposed mechanisms.

## What does NOT belong here

- **Runtime event output** (SL entries, handoffs, research-reports, loop-reports, identification reports) → `operations/`.
- **Ratified governance rules** (boundary, pipeline, agent, knowledge rules) → `governance/`.
- **Owner-authored governance-rule proposals** (tracking mechanisms, DD proposals, amendments) → `governance/proposals/`.
- **Tracked work items** → `project-management/implementation-backlog/`.
- **Ratified decisions** → `project-management/design-decisions/`.

## Governance

Owner-governed folder; any agent may author here. Shape governs placement, not author (see DD-89 for the four-zone architecture that frames this rule).

## Current contents

| File | Created | Author | Shape |
|------|---------|--------|-------|
| `2026-04-20-artifact-acceptance-rubric.md` | 2026-04-20 | Codifier (session 46) | Acceptance rubric |
| `2026-04-20-artifact-lifecycle-spec.md` | 2026-04-20 | Codifier (session 46) | Lifecycle spec |
| `2026-04-20-pipeline-collapse-proposal.md` | 2026-04-20 | Codifier (session 47) | Pipeline-mechanics proposal |
| `2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` | 2026-04-20 | Codifier (session 47) | Substrate audit |
| `2026-04-21-contract-section-spotcheck-agent-audit.md` | 2026-04-21 | Codifier (session 48) | Spot-check report |
| `2026-04-21-librarian-read-contract.md` | 2026-04-21 | Codifier (session 49) | Read contract |
| `2026-04-21-librarian-use-case-registry.md` | 2026-04-21 | Codifier (session 49) | Use-case registry |
| `2026-04-21-agent-reflections-to-proposals-architecture.md` | 2026-04-21 | Owner (session 51) | Self-improvement architecture spec |
| `2026-04-21-session-telemetry-harness-requirements.md` | 2026-04-21 | Owner (session 51) | Harness-portable observability spec |
| `2026-04-22-librarian-boundary-case-tracking.md` | 2026-04-22 | Owner (session 50) | Tracking-mechanism spec (awaiting Nick's gate) |

## Provenance

The first seven files were migrated from `operations/design-notes/` on 2026-04-22 during session 50, when the Owner proposed the four-zone architecture (ratified as DD-89). The `operations/design-notes/` folder was deprecated and removed.

The two session-51 files were authored natively in this folder under the new four-zone convention. Both are substrate design notes for cross-system DDs (DD-90 session telemetry; DD-91 reflections architecture).

The 2026-04-22 boundary-case-tracking file was relocated here during session 52 from `governance/proposals/` after DD-89's proposals-folder scope was clarified to agent-initiated output only.

## Cross-References

- Four-zone architecture: DD-89
- Project-management parent: `project-management/_index.md`
- Design Decisions: `project-management/design-decisions/`
- Implementation Backlog: `project-management/implementation-backlog/`
- Governing DDs: DD-52 (fractal pattern), DD-86 (Owner responsibility)
