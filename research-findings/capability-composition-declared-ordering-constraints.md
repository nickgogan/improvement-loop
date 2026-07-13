---
name: "Middleware-Semantics Capability Composition with Declared Ordering Constraints"
summary: |-
  Plain English: when composable units (capabilities, middleware, hooks) wrap an agent,
  their order matters — so let each unit declare its own ordering constraints and have
  the composer topologically sort them, instead of relying on the order a user happened
  to list them in. Pydantic AI v2.9.0 composes capabilities with middleware semantics
  (first-listed is outermost) and adds `CapabilityOrdering(position, wraps, wrapped_by,
  requires)`: a capability can pin itself outermost, declare what it must wrap or be
  wrapped by, and name hard dependencies. `CombinedCapability` topologically sorts the
  declared constraints, using user list-order only as a tiebreaker — e.g. the deferred
  loader pins `position='outermost', wrapped_by=[Instrumentation]`. Composition order
  becomes a first-class, declarable property rather than a list-position convention.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "capability-as-agent-composition-primitive.md"
    rel: "extends"
  - file: "guardrails-as-hook-lattice-capabilities.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "orchestration"
  - "agent-design"
  - "composition"
---

# Middleware-Semantics Capability Composition with Declared Ordering Constraints

## What It Is

The composition mechanics under Pydantic AI's capability primitive. Each capability
contributes to the agent through seven getter seams (instructions, description, model
settings, toolset, native tools, wrapper toolset, ordering) plus lifecycle hooks.
`CombinedCapability` merges a capability list with middleware semantics — first-listed
is outermost, wrapping everything after it. The addition is `CapabilityOrdering`: a
declaration each capability can return, carrying

- `position` — pin to `outermost`/`innermost`,
- `wraps` / `wrapped_by` — relative constraints against named capability types,
- `requires` — hard dependencies that must be present.

The composer topologically sorts these declarations; the user's list order survives only
as a tiebreaker. (`capabilities/abstract.py`, `capabilities/combined.py`)

## Why It Matters

Every layered agent system has an ordering problem — guardrails must wrap tools,
instrumentation must observe everything, loaders must resolve before consumers — and
most systems solve it with documentation ("list X first") that silently breaks when
users reorder. Moving the constraint into the unit itself makes composition
order-independent for the user and lets the unit's author, who knows its invariants,
encode them once. This is the same move dependency resolvers made for packages, applied
to prompt/tool middleware.

## Why People Are Using It

Shipped as the composition engine of a top-tier production agent framework; first-party
capabilities already rely on it (the deferred-capability loader pins itself outermost
under instrumentation). Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Convention by list position** (most middleware stacks) — simple, but ordering
  knowledge lives in docs and user discipline.
- **Fixed framework-defined phases** (e.g., hooks that always run at named lifecycle
  points) — removes ordering freedom entirely; less composable but more predictable.

## Potential Improvements

- Cycle diagnostics: topological sorts fail opaquely on contradictory constraints;
  surfacing *which* two declarations conflict is the usability difference.
- Constraint visualization — rendering the resolved wrap order for audit.

## Potential Failure Modes

- **Over-constrained graphs** — two third-party capabilities both pinning `outermost`
  cannot compose; declared constraints trade flexibility for safety.
- **Hidden reordering surprise** — users who expect list order to hold may be confused
  when declarations override it.
- **Constraint drift** — a capability's declared ordering can silently outlive the
  invariant that motivated it.
