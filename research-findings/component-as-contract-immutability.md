---
name: Component-as-Contract Immutability
summary: "Explicit frozen-surface enumeration for public APIs — class names, input names, output names, and defaults are immutable once published. Deprecated components use `legacy=True` + `replacement=[]` fields rather than removal, preserving backward compatibility while signaling the preferred path forward."
implementation_notes: null
category: Governance
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - General
adopted_in: []
sources: []
proposals: []
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
related_findings:
  - file: contract-first-design-for-agent-interfaces.md
    rel: same-problem
pipeline_status: raw
consumed_by: []
---

# Component-as-Contract Immutability

## What It Is

A governance pattern where 15 public component surfaces are documented in a CONTRACTS.md file as frozen — class names, input names, output names, and default values cannot change once published. Deprecation is handled via `legacy=True` + `replacement=[...]` metadata fields rather than deletion. A "before-you-change matrix" maps proposed actions (rename, remove, add) to required compatibility checks. Version mapping tests validate that every component exists at every supported version.

## Why It Matters

In systems with user-composed workflows (visual builders, plugin architectures, or agent tool registries), renaming or removing a public interface silently breaks all downstream compositions referencing it. Explicit frozen-surface enumeration makes the cost of any breaking change visible before it happens and forces the team into additive-only evolution, which is the only safe path for published APIs consumed by autonomous agents.

## Why People Are Using It

Observed in [Langflow](https://github.com/langflow-ai/langflow) v1.9.3 — see [[langflow-analysis]] for structural details. Langflow has 504 component Python files across 109 categories, all composable in a visual graph editor. The frozen contract system prevents user-built flows from breaking silently when components are updated.

## Potential Alternatives

Semantic versioning with major bumps for breaking changes (shifts the cost to consumers who must migrate). Adapter/shim layers that translate old interface names to new implementations. Runtime deprecation warnings that log usage but don't block execution.

## Potential Improvements

Automate contract validation via pre-commit hooks that diff component signatures against the frozen surface list. Generate the contracts file from code annotations rather than maintaining it separately. Add a sunset date field to legacy components so teams can plan removal windows with advance notice.

## Potential Failure Modes

The frozen surface can become a growth ceiling — if the original interface was poorly designed, teams are stuck with it forever. Legacy components accumulate without cleanup, increasing codebase size and confusing new contributors who cannot distinguish current from deprecated. The replacement field requires manual maintenance and can point to components that themselves get deprecated, creating chains.
