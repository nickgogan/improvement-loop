---
name: "Declared-Then-Bench-Verified Harness Capability Flags"
summary: |-
  Omnigent replaces scattered "if harness == 'x'" branches with a frozen nine-axis capability
  dataclass per harness (integration mode, elicitation, resume, streaming, subagents, ...) —
  and, critically, treats the boolean claims as falsifiable: live bench probes flag drift when
  a harness stops honoring a declared capability, and flags are flipped only on bench evidence,
  with the epistemics recorded in code comments ("LIVE-VERIFIED: a bench run observed 0 text
  deltas"). For us this is the pattern behind our own model-capability registry: capability
  claims are data with provenance, verified against behavior, never inferred from docs alone.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings:
- file: tiered-capability-registry-engine-behavior-branching.md
  rel: extended-by
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-13"
---

## What It Is

A capability model for heterogeneous agent harnesses. `omnigent/harness_capabilities.py` defines a frozen `HarnessCapabilities` dataclass with nine axes — `integration_mode` (sdk-in-process / cli-subprocess / acp-subprocess / native-tui / native-server), `elicitation` (none / hook / jsonrpc / approval-mirror / sse-permission), `resume` (warm-reattach / cold-only), `effort` vocabulary family, `model_family`, `auth`, plus booleans `subagents`, `interrupt`, `streaming`. The table (`_BUILTIN_CAPABILITIES`) covers 20+ harness ids. Two disciplines make it more than a config table: **declared claims are live-verified** by harness-bench probes that "flag drift when a harness does not honor it," and **epistemics are recorded at the claim site** — a comment notes that `streaming=False` was set only after "a bench run observed 0 text deltas," and that an earlier static grep-based flip had been wrong. Derivable axes are asserted against source in tests.

## Why It Matters

Any system that spans multiple harnesses, models, or providers accumulates capability knowledge, and the default failure mode is twofold: the knowledge scatters into conditionals (`if harness == "x"`), and the claims decay silently as upstreams change. Centralizing the claims into one typed registry solves the first; treating each claim as a falsifiable statement with bench verification and recorded provenance solves the second. The pattern converts "we believe harness X streams" from tribal memory into data with an evidence trail and a drift alarm.

## Why People Are Using It

Observed in [omnigent](https://github.com/omnigent-ai/omnigent) v0.6.0.dev0 (alpha) — see [[omnigent-analysis]] for structural details. The dataclass docstring explicitly frames it as replacing "scattered `if harness == 'x'` branches and presence/absence of companion modules." The engine's own model-capability registry (`operations/references/model-capability-registry.md`, KB-grounded claims with periodic intentional refresh) is a manual variant of the same stance — hence Partially Adopted; the bench-verification loop is the part we lack.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Docs-derived capability table | Trust vendor documentation | Low-stakes selection where a wrong claim costs little |
| Feature detection at runtime | Probe capabilities on every session start | Few capabilities, cheap probes, no registry to maintain |
| Scattered conditionals | Encode knowledge where it is used | Two harnesses, one maintainer, short-lived code |

## Potential Improvements

- Attach a verification date per claim so staleness is queryable, not just drift-alarmed
- Publish the registry through an API so downstream consumers stop re-deriving capabilities

## Potential Failure Modes

- **Bench coverage gaps:** axes without probes silently revert to docs-trust while borrowing the registry's credibility
- **Frozen-table lag:** a capability the vendor ships today is absent until someone re-benches
- **Probe brittleness:** bench flakiness can flip claims on transient failures unless verification requires stable evidence
