---
title: "Enrich Context Engineering with Memory Isolation/Topology Sub-Dimension"
id: "proposal-2026-04-24-ctx-subdims"
type: "proposal"
category: "taxonomy-evolution"
target_system:
  - "improvement-loop"
stage: "accepted"
created: "2026-04-24"
updated: "2026-04-24"
author: "codifier"
trigger: "agent-initiated"
source_session: 63
source_report: "operations/research-reports/guide-routing-check-2026-04-24.md"
affects:
  - "operations/references/research-dimensions.md"
  - "research-findings/*.md (category field)"
  - "operations/references/guide-routing-table.md"
source_dd:
  - "DD-91"
tags:
  - "proposals"
  - "taxonomy"
  - "research-dimensions"
  - "memory"
---

# Proposal: Enrich Context Engineering with Memory Isolation/Topology Sub-Dimension

## Context

Session 63's guide-routing check surfaced a taxonomy mismatch. Findings `subagent-persistent-memory-directory` and `memory-bank-isolation-per-agent-per-project` carry `category: Memory Architecture`, which is not a top-level research dimension. Routing works because `guide-routing-table.md` admits "Memory Architecture" under G7's Dimensions field, but `research-dimensions.md` has no registered home for these.

Dimension 1 (Context Engineering) has one sub-dimension today: **1.A Memory Decay, Forgetting, and Compaction** (added session 62). Neither #10 nor #15 fits 1.A — they're about memory *isolation and persistence topology*, not decay.

## Problem

Three related taxonomy gaps:

1. **`category: Memory Architecture`** is orphaned — it appears on findings but isn't in `research-dimensions.md`. This is drift between the frontmatter taxonomy and the registered dimension taxonomy.
2. **Memory isolation/topology findings have no sub-dimension home.** Parent Dimension 1 (Context Engineering) accepts them, but the registry provides no query shape or seed-cluster guidance for scans in this area.
3. **A broader sweep may find similar cases.** Memory topology is unlikely to be the only Context Engineering sub-topic with enough external research mass to deserve its own query shape.

## Proposal

### Primary: Add Sub-dimension 1.B (Memory Isolation and Topology)

Add to `research-dimensions.md` under Dimension 1 (Context Engineering), alongside existing Sub-dimension 1.A:

**Sub-dimension 1.B: Memory Isolation and Topology**

- **Why this sub-dimension.** Memory *selectivity* (1.A) and memory *isolation* (1.B) are orthogonal concerns. Decay asks "what gets forgotten?"; isolation asks "whose memory sees what?" Multi-agent, multi-project, and multi-tenant agent systems are independently converging on isolation primitives — bank IDs, per-agent directories, tenant tags, channel-scoped recall — that prevent cross-contamination between contexts that happen to share a memory substrate.
- **What to search for.** Bank-ID and channel-based isolation, per-agent persistent memory directories, per-project memory scopes, multi-tenant memory tagging, session-bounded vs cross-session memory, cross-agent memory sharing protocols, memory access-control patterns, scope-boundary alignment with system boundaries (e.g., IL vs Household OS vs Claude Build).
- **Seed findings** (existing KB entries that seed the cluster): `memory-bank-isolation-per-agent-per-project`, `subagent-persistent-memory-directory`, `hierarchical-container-tag-multi-tenancy`, `multi-client-context-isolation-with-shared-skills`, plus same-problem-linked neighbors.
- **Graduation criteria.** Same threshold as 1.A: ≥10 findings specifically about isolation/topology mechanics (not decay, not storage medium, not retrieval algorithm), plus multiple sibling-dimension references, plus an independent Librarian concept file. Until then, nested under Dimension 1.

### Secondary: Reconcile `category: Memory Architecture`

Once 1.B exists, findings currently tagged `category: Memory Architecture` need a home:

- **Option A.** Reclassify all "Memory Architecture" findings into `category: Context Engineering` (the parent). Sub-dimension membership is tracked by seed-cluster listing in `research-dimensions.md`, not by frontmatter category. Consistent with how 1.A is currently tracked.
- **Option B.** Add "Memory Architecture" as its own top-level Dimension 12. Higher ceremony; only justified if memory findings no longer compose primarily within Context Engineering (per the existing elevation criteria in `research-dimensions.md`).

Recommendation: **A**, for consistency with 1.A's nesting and to preserve the "Researcher-side scan topic" framing. Memory architecture is a facet of Context Engineering at current KB density.

### Tertiary: Queue a KB Re-classification Pass

Nick flagged this: once sub-dimensions change, a research re-run over the KB is expected and desired. The `/dimension-rebalance` skill is designed for exactly this — it reads all findings, evaluates each against the new dimension definition, proposes reclassifications and splits, then executes approved changes.

Suggested sequence if this proposal accepts:
1. Update `research-dimensions.md` with Sub-dimension 1.B.
2. Run `/dimension-rebalance` to propose category reassignments (Memory Architecture → Context Engineering, plus any other drift the pass surfaces).
3. Nick gates the rebalance report; Codifier applies approved changes.
4. Update `guide-routing-table.md` if any Dimension → Guide edges shift.

## Scope and Non-Goals

- **In scope:** Adding 1.B to `research-dimensions.md`, reconciling the orphan category, queuing the rebalance pass.
- **Out of scope:** Creating a new top-level Dimension 12 for Memory Architecture (rejected above). Surfacing additional sub-dimensions beyond 1.B (those should arise from evidence, not speculation).

## Impact

- **Research-dimensions.md.** +1 sub-dimension block (1.B), pattern-matches the structure of 1.A.
- **Findings.** ~10-15 findings likely reclassified category: Memory Architecture → Context Engineering (exact count via `/dimension-rebalance`).
- **Guide-routing-table.md.** G7's Dimensions field can drop "Memory Architecture" since it becomes subsumed under Context Engineering with 1.B membership.
- **No DD required.** This is taxonomy evolution of an operational reference, not a governance change. Session 62 added 1.A the same way — direct edit to `research-dimensions.md`.

## Open Questions for Nick

1. **Accept 1.B as proposed**, or refine the sub-dimension name/scope?
2. **Option A or B** for reconciling `category: Memory Architecture`?
3. **Timing of `/dimension-rebalance`** — this session, next Codifier session, or later?

## Status

- `accepted` — Nick approved in session 63 (2026-04-24). Direction: enrich Context Engineering with Memory Isolation/Topology sub-dimension; Option A for reconciling orphan `category: Memory Architecture`; timing of `/dimension-rebalance` queued for a later Codifier session.
- **Applied this session:** Sub-dimension 1.B added directly to `operations/references/research-dimensions.md`.
- **Queued:** IB-153 tracks the `/dimension-rebalance` run.
