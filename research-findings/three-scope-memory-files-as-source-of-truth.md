---
name: 'Three-Scope Memory Model with Files as Source of Truth, Memory Tools as Accelerators'
summary: 'Agent memory routes across three scopes — user (machine-personal, cross-workspace), repo (workspace-scoped durable rules), session (current conversation, discarded at end) — with a hard rule that durable memory is file-based: control surfaces, ledgers, git, and in-repo memory files. A harness memory tool is an accelerator, never the source of truth. Repo memories must travel with the workspace as plain files; platform-keyed storage (e.g. workspace-identity hashes) is met structurally by tracking authoritative guardrails in-repo with machine memory holding pointer stubs.'
implementation_notes: 'Directly relevant to IB-172 layered-memory design. The routing rule gives the engine a decision table: machine/environment pitfalls → user scope; workspace conventions and guardrail history → repo scope (in-repo files); in-progress task state → session scope, discarded. The anti-stranding lesson matters for any harness with platform-side memory (Claude Code auto-memory included): authoritative rules live in tracked files, memory holds pointers, and session handoff reconciles the two.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- memory-scopes
- durable-memory
- file-based-memory
- session-handoff
---
# Three-Scope Memory Model with Files as Source of Truth, Memory Tools as Accelerators

## What It Is

A memory architecture for stateless-session agents built on three scopes plus one
authority rule. Scopes: **user** (machine-personal, cross-workspace — preferences and
environment pitfalls), **repo** (workspace-scoped durable rules — mistake patterns,
verified conventions, guardrail history), **session** (in-progress task state, discarded
at conversation end). Authority rule: durable memory is deliberately file-based —
control surfaces (PROGRESS/HISTORY), the profile ledger, git, and in-repo memory files;
a harness memory tool is an accelerator, not the source of truth.

## Why It Matters

Plain English: harness memory tools are convenient and fragile — they store state in
platform-side locations keyed to things like storage-path hashes, so renaming, moving,
or cloning a workspace can silently strand every remembered guardrail with nothing
failing loudly. If the durable rules live in tracked files inside the repo, they survive
any move, any harness swap, and any platform pricing change. The scope model also gives
agents a routing rule instead of a junk drawer: each remembered thing has exactly one
correct home.

## How It Works

- **Routing rule:** personal/machine preferences and environment pitfalls → user scope;
  workspace conventions, guardrail history, verified practices → repo scope; task state
  → session scope, discarded at end. Durable *facts and decisions* go to the ledger and
  control surfaces — not to memory at all.
- **No stolen authority:** memories never carry another surface's authority — they
  point to the registry, ledger, or PROGRESS rather than restating them; user-named
  content stays in the user's scope with at most pointer stubs elsewhere.
- **Travel requirement:** repo memories persist as plain files readable as ordinary
  docs, so the durable-rule topics stay available on any harness. Where the platform's
  repo-scope memory keys to workspace identity rather than the repo (VS Code Copilot's
  memory tool), the requirement is met *structurally, not natively*: authoritative
  guardrails are tracked in-repo (e.g. `.github/memories/repo/`, itself
  registry-classified), machine memory holds pointer stubs, and every rename/clone/
  install step re-seeds the stubs — recorded in the install report.
- **Handoff discipline:** repo memories are reconciled at session end, owned by the
  session-handoff skill — the same closure that reconciles the control surfaces.
- **Degradation path:** a platform with no memory tool at all treats the repo-memory
  folder as ordinary always-loadable docs pointed from the always-on file, dropping or
  emulating user/session scopes and recording the degradation.

## How It Could Fail

Pointer stubs that are never re-seeded after a clone leave the memory tool pointing at
nothing — the stranding failure returns one level up. Without the routing rule enforced
at write time, repo scope becomes an unbounded rule pile (the context-rot failure mode).
Session scope that isn't actually discarded leaks task state across conversations and
masquerades as durable knowledge.
