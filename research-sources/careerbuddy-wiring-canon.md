---
name: CareerBuddy Wiring Canon — onboarding docs 01-08, system contract, wiring manifest
source_type: "Repository"
status: Done
key_takeaways: CareerBuddy documents its harness wiring as eight platform-agnostic canon docs (always-on entry, path-scoped rules, governance registry, memory scopes, skill registry, cold-start chain, invocation context, operational quirks), distilled into a machine-readable system contract shaped as an agent card with per-row tier/capability/degradation/invariant fields, plus a receiving-agent adaptation protocol with graded capability intersection and a layered install-verification stack. The recurring meta-pattern is abstract-then-adapt with pointer discipline and permissioning honesty throughout.
relevance: High
added_by: Nick
tags: [harness-wiring, system-contract, portability, cold-start, governance, memory-scopes, skill-packaging]
url: https://github.com/nickgogan/CareerBuddy (onboarding/)
authority: []
findings:
- machine-readable-system-contract-with-wiring-rows.md
- always-on-context-minimalism-pointer-only-entry.md
- cold-start-chain-and-cold-start-test.md
- path-scoped-guardrails-edit-time-prevention.md
- governance-registry-blast-radius-classification.md
- three-scope-memory-files-as-source-of-truth.md
- operational-quirks-recurrence-to-guard-discipline.md
- skills-generic-users-are-data-invocation-context.md
- harness-adaptation-protocol-graded-capability-intersection.md
- wiring-canon-abstract-then-adapt-doc-structure.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-12'
---

# CareerBuddy Wiring Canon — onboarding docs 01-08, system contract, wiring manifest

The onboarding/ layer of CareerBuddy, Nick's single-agent, harness-wired, cross-platform agentic system, intaken as a primary source for the engine restructure program Phase 1. The corpus comprises eight numbered harness-wiring canon docs (each split into Canon / Adapter-delegated / Harness-specific examples), a canonical system-contract.yaml (agent card with embedded realization manifest: identity, trust, end-user value, skills rollup, composition, and one wiring row per canon doc with tier, capability IDs, degradation, and invariant), a SHA-256 wiring-manifest.json for canon-vs-live drift detection, an ADAPTATION.md protocol for foreign receiving agents (graded provides inventory, intersection semantics, human-gated plan, install report, cold-start echo, trigger evals, invariant probes, behavioral smokes), and an AGENTS.md router with a two-source change model. Ten findings extracted covering harness wiring, contracts, cold-start discipline, memory scopes, path-scoped guardrails, governance registries, quirk discipline, skill decoupling, adaptation protocol, and the abstract-then-adapt doc architecture.
