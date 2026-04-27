---
name: Per-Node Tool Restrictions as Workflow-Level Governance
summary: 'Archon''s workflow YAML nodes can specify allowed_tools or denied_tools arrays, giving fine-grained tool access control per workflow step. The orchestrator''s routing calls use tools: [] to prevent
  any tool use during classification. This is tool-level sandboxing within a workflow — the finest granularity observed across all watched libraries.'
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: same-problem
- file: tiered-permission-system-bash-safety.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
---

## What It Is

Archon's YAML workflow nodes support `allowed_tools` and `denied_tools` arrays, enabling fine-grained tool access control at the individual workflow step level. A research node can be restricted to read-only tools. A classification node can have `tools: []` to prevent any tool use during routing decisions. An implementation node can have full tool access. This is configured in YAML, not code — workflow authors control tool permissions without modifying the execution engine.

The key insight is that different steps in the same workflow have different trust requirements. A node that classifies an issue shouldn't be able to write files. A node that generates code shouldn't be able to send messages. Per-node tool restrictions enforce least-privilege at the workflow step level.

## Why It Matters

Most agent frameworks apply tool permissions at the agent or session level — an agent either has access to a tool or it doesn't. But within a multi-step workflow, different steps have fundamentally different trust profiles. A planning step needs read access but not write. A review step needs code reading but not execution. Per-node restrictions bring the principle of least privilege into workflow design.

This is particularly relevant as workflows become more complex and autonomous. Without per-step tool restrictions, a compromised or misbehaving node in a long workflow has access to every tool available to any node in that workflow.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.3.2 — see [[archon-analysis]] for structural details. Archon ships 21 default workflows where tool restrictions are used strategically: orchestrator routing calls use `tools: []`, review nodes use read-only tool sets, and implementation nodes get full access.

GSD has per-agent tool allowlists but not per-step within a workflow. Superpowers has skill-level tool guidance but not enforceable restrictions. Archon's per-node granularity is the finest in the watched-library registry.

## Potential Alternatives

Session-level tool restrictions (coarser but simpler). Code-level tool filtering in the execution engine (harder to configure). Separate agent sessions per workflow step with different tool sets (heavier weight).

## Potential Improvements

Combining tool restrictions with model restrictions per node — a low-trust step could use a cheaper model with fewer tools. Inheritance patterns where a workflow defines default tool sets that individual nodes can narrow but not widen.

## Potential Failure Modes

Over-restriction causing workflow failures (a node needs a tool it was denied). Under-restriction due to difficulty predicting which tools each step will need. Configuration drift where tool lists don't track tool additions to the platform.
