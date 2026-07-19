---
name: 'Invariant Column as Contract Field — Adaptation-Survival Property per Wiring Row'
summary: 'Every wiring row in an installable agent system''s contract carries an `invariant` field: the property that must survive any adaptation, however the target platform satisfies the row. A field-level prior-art survey (A2A, MCPB, MCP server.json, OASF, agents.md, Archon) found no equivalent — capability declarations exist everywhere, but nothing declares what must be preserved under adaptation. The invariant doubles as the acceptance test at install time and as the probe spec for post-install behavioral conformance.'
implementation_notes: 'Queued by CareerBuddy explicitly as a corpus contribution to this engine. Directly serves the restructure program''s portable-governance-kernel: when the engine enumerates its own wiring rows (CLAUDE.md injection, rules, skills, hooks, PROGRESS spine), each row should declare the property that must survive a harness move — e.g. "governance-tier files are never edited without explicit human approval" — independent of mechanism. That gives the kernel machine-checkable acceptance tests plus ready-made probe specs for any future port.'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented, single production system with a research-cited design gate)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-improve-backlog-corpus-contributions.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: machine-readable-system-contract-with-wiring-rows.md
  rel: extends
pipeline_status: synthesized
consumed_by:
- building-agentic-systems.md
- rules/wiring-rows-must-declare-testable-invariant.md
tags:
- system-contract
- invariants
- portability
- acceptance-testing
---
# Invariant Column as Contract Field — Adaptation-Survival Property per Wiring Row

## What It Is

A contract field with no known prior art. In CareerBuddy's `onboarding/system-contract.yaml`,
each of the eight wiring rows (one per harness-integration concern) carries five fields —
tier, capabilities, purpose, degradation, and `invariant`: "the property that must survive
**any** adaptation, however the target platform satisfies the row." CareerBuddy's MV21
Phase R research (four parallel subagents doing a field-level survey of A2A, MCPB, MCP
server.json, OASF, agents.md, and Archon's `requires:` gate) concluded the per-row
invariant column "has no prior art anywhere" — the ecosystem declares *capabilities
required*, never *properties preserved*.

## Why It Matters

Plain English: when you port an agent system to a new harness, the mechanism always
changes — a path-scoped rule becomes a `.mdc` file on Cursor, an `applyTo` glob on
Copilot, or a prose paragraph on a bare host. What must NOT change is the guarantee the
mechanism existed to provide. Without a named invariant, "did the port work?" degenerates
into "did we copy the files?". With one, every row of the install has a testable
acceptance condition that is mechanism-independent — the difference between checking
installation and checking preservation.

## How It Works

- Field semantics: the invariant states the guarantee, not the mechanism. Example rows
  from the shipped contract: always-on entry — "One minimal file reaches every request
  carrying mission + load order + guards; it names the active {user-id} pointer-only and
  never restates user facts"; governance registry — "Governance-tier files are never
  edited without explicit human approval; the registry exists, travels with the
  workspace, and classifies itself."
- Acceptance-test role: the receiving-agent protocol (ADAPTATION.md step 4) requires the
  adaptation plan to state, per row, "how the row's `invariant` is preserved under your
  mechanism. The invariant is the acceptance test — the mechanism may be anything your
  platform offers; the invariant may not bend."
- Probe-spec role: behavioral conformance (ADAPTATION.md step 7) runs "one
  self-administrable binary probe per wiring row — **the row's `invariant` is the probe
  spec**." A failed probe is a mechanism problem: return to planning for that row; the
  invariant never bends.
- Degradation coupling: every `degradation` field names its prose fallback "so the
  worst-case host (prose-only) still preserves the invariant" — degradations weaken
  mechanisms, never invariants.
- Audit enforcement: the workspace doc audit (C15) checks the contract has an invariant
  per row; it is one of five negative-tested violation classes.
- Motivating evidence: the design gate was research-cited (P-8 discipline) against the
  Phase R survey. Capability negotiation in the surveyed ecosystem is declare-and-adapt
  with required/optional tiers (A2A extensions, Archon requires, MCPB user_config), but
  none of those formats can express "whatever you do, this property holds afterward."

## How It Could Fail

Invariants written as mechanisms in disguise ("the file X exists at path Y") reimport the
portability problem they exist to solve. Vague invariants ("the system stays safe") are
unprobeable — the field only earns its keep if each invariant is binary-testable in a
fresh session. And invariants are only checked at install/audit time in this design;
between runs they are declared, not enforced (an absence CareerBuddy's contract itself
declares).

## Extraction Note — 2026-07-19
Extracted as **rule**: [[wiring-rows-must-declare-testable-invariant]] in `extracts/rules/`
