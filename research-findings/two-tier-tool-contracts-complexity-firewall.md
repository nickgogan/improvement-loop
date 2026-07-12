---
name: "Two-Tier Tool Contracts as a Complexity Firewall"
summary: |-
  opencode maintains two deliberately different tool-authoring contracts: an internal one
  (Effect Schema parameters, typed errors whose message getter IS the model-facing repair
  prompt, live progress metadata, output auto-truncation with file spill) and a public one for
  user tools that is minimal on purpose — zod shape in, Promise out. The internal machinery's
  power never leaks into the public contract, so user tools stay writable in five lines while
  first-party tools keep their rich failure semantics. For us the lesson for any skill/tool
  substrate: the contract you ask outsiders to satisfy should be simpler than the one you use
  yourself, and the gap is bridged by the framework, not the author.
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

Two tool contracts with an adapter between them. **Internal** (`packages/opencode/src/tool/tool.ts`): `Tool.define(id, {...})` with Effect Schema parameter validation, a context object carrying `ask()` (permission), `metadata()` (live progress), and abort signals, schema-validation failures raised as `InvalidArgumentsError` whose `message` getter *is the model-facing correction prompt*, and a wrapper that auto-truncates oversized output to a spill file. **Public** (`packages/plugin/src/tool.ts`, used by `.opencode/tool/*.ts`): `tool({ description, args: zodShape, execute })` — a plain zod/Promise contract with none of the above visible. The framework adapts public tools into the internal representation; tool authors never see Effect, typed error channels, or truncation plumbing.

## Why It Matters

Frameworks habitually export their internal tool contract, and the sophistication that makes first-party tools robust (typed errors, effect systems, streaming metadata) becomes the barrier that makes third-party tools rare. Splitting the contract lets each tier optimize for its real audience: the internal tier for correctness under composition, the public tier for a five-minute authoring experience. The firewall runs both directions — internal refactors (opencode is mid-migration on its provider layer) don't break user tools, and user-tool simplicity never pressures the internal design to dumb down. The repair-prompt-as-error-message detail is independently notable: the internal error type is designed so that *throwing it* is what teaches the model to correct its arguments.

## Why People Are Using It

Observed in [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[opencode-analysis]] for structural details. The repo dogfoods the public contract: its own CI agents' tools (`github-triage`, `github-pr-search`) are written against the minimal tier.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| One exported contract | Public tools use the internal API | Internal contract already minimal; no external authors |
| MCP as the only extension path | External tools live behind a protocol server | Cross-process isolation or cross-product reuse wanted |
| Codegen from a spec | Tools declared in a schema, both tiers generated | Very large tool fleets with uniform shapes |

## Potential Improvements

- Document which internal capabilities (progress metadata, custom truncation) are deliberately absent from the public tier, so authors don't reinvent them badly
- Conformance tests that run public-tier tools through the internal wrapper's edge cases (abort, oversized output, invalid args)

## Potential Failure Modes

- **Adapter drift:** the bridge between tiers becomes the least-tested code path while carrying every third-party call
- **Capability envy:** power users hit the public tier's ceiling and fork into internals, recreating the coupling the firewall prevented
- **Two docs to maintain:** the tiers age at different rates; samples for the wrong tier confuse authors
