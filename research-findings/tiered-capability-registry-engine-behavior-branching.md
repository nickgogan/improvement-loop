---
name: Tiered Provider-Capability Registry Driving Engine Behavior
summary: 'Plain English: when one engine has to drive many AI backends, declare each backend''s

  capabilities as graded values — not booleans — and make the engine branch on the

  grade, so every backend gets the same feature at the best fidelity it can support.

  Archon v0.5.0''s provider registry declares capabilities as discriminated values

  (`structuredOutput: ''enforced'' | ''best-effort'' | false`; `nativeTools`;

  `sessionResume`) and the engine selects behavior per grade: grammar-constrained

  output for ''enforced'' providers, a validate-and-reask loop (max 3 attempts) for

  ''best-effort'', refusal for unsupported; run management delivered as a native

  in-process tool where `nativeTools` is true and as a generated prompt-section

  teaching CLI-over-bash where it is false. One protocol, capability-gated delivery —

  no scattered per-provider if-branches.'
implementation_notes: 'Directly informs the engine''s model-capability registry

  (operations/references/): capability claims should be tiered discriminated values

  with per-tier consumer behavior spelled out (enforce / verify-and-retry /

  refuse-or-degrade), not booleans. Pairs with the Omnigent bench-verification

  finding — Archon supplies the tiered declaration shape, Omnigent supplies the

  falsifiability discipline.'
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources: []
related_findings:
- file: bench-verified-harness-capability-flags.md
  rel: extends
- file: harness-adaptation-protocol-graded-capability-intersection.md
  rel: same-problem
- file: receiver-relative-tier-semantics.md
  rel: same-problem
- file: model-tiers-aliases-cross-provider-indirection.md
  rel: same-problem
- file: vendor-neutral-skill-vocabulary-per-harness-tool-maps.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-13'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
tags:
- tool-integration
- capability-registry
- multi-provider
- archon
---

# Tiered Provider-Capability Registry Driving Engine Behavior

## What It Is

Archon v0.5.0 extracts all AI-backend integration into a `packages/providers` registry where each provider (core: Claude, Codex; community: Pi with ~20 LLM backends, OpenCode, GitHub Copilot) registers a typed `ProviderRegistration` record declaring its capabilities as **discriminated values, not booleans**:

- `structuredOutput: 'enforced' | 'best-effort' | false` — the engine branches: schema-grammar-constrained output for `enforced`; a validate-and-reask loop with up to 3 attempts for `best-effort`; and a node that declares `output_format` on an unsupported provider fails rather than silently degrading.
- `nativeTools` — run management reaches the chat agent as an in-process native `manage_run` tool where true (Claude, Pi), and as a generated system-prompt section teaching CLI-over-bash where false (Codex, OpenCode, Copilot). Same protocol, two delivery mechanisms, selected by declared capability.
- `sessionResume` — gates whether cross-run session persistence is offered.

Workflow and orchestrator code branch on the capability grade, never on provider identity. Files: `packages/providers/src/registry.ts`, `types.ts`; gating in `packages/core/src/orchestrator/`.

## Why It Matters

Boolean capability flags force a lie at the margins: a provider that *mostly* supports structured output is neither `true` nor `false`, and the engine either over-trusts it or wastes it. Tiered declarations let the engine encode a graceful-degradation ladder — enforce where possible, verify-and-retry where plausible, fail closed where impossible — as data rather than scattered conditionals. The capability-gated delivery pattern (native tool vs prompt-section fallback for the same protocol) is the generalizable move: features are written once against the capability contract, and every backend gets the strongest delivery it can support.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. The registry is the seam that let Archon absorb community providers (Pi's ~20 backends, OpenCode's embedded runtime, Copilot) without forking engine behavior per provider; structured-output validation is applied uniformly across all of them.

## Potential Alternatives

Boolean capability flags with bench verification (Omnigent's approach — stronger epistemics, weaker expressiveness). Per-provider adapter subclasses overriding behavior (capability knowledge hidden in code rather than declared as data). Lowest-common-denominator design (only use features every backend supports).

## Potential Improvements

Bench-verify the tiered claims the way Omnigent verifies boolean ones — a declared `'enforced'` that quietly regresses to best-effort behavior is drift the registry can't see. Version the capability declarations against provider releases.

## Potential Failure Modes

Declared tiers drift from actual provider behavior (declaration without verification). Tier vocabulary ossifies — a new provider capability that doesn't fit the enum forces either a lossy mapping or a breaking schema change. The validate-and-reask ladder can triple token cost on best-effort providers before failing anyway.
