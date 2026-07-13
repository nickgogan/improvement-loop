---
name: "Guardrails as Hook-Lattice Capabilities, Not a Separate Primitive"
summary: |-
  Plain English: you do not need a dedicated "guardrail" abstraction — one sufficiently
  complete interception lattice (hooks at every lifecycle edge) lets guardrails, cost
  budgets, approvals, and redaction all be ordinary composable units. Pydantic AI
  v2.9.0 exposes 7 hook families (run, node, model-request, tool-validate, tool-execute,
  output-validate, output-process), each with before/after/wrap/on-error variants (~28
  interception points) and typed per-hook Protocol signatures. The documented guardrail
  exemplar (PII redaction) wraps `after_model_request`; approval workflows wrap
  `before_tool_execute`; a third-party ecosystem (pydantic-ai-shields) ships cost
  tracking, tool/input/output guards, and prompt-injection defense as capability
  packages. Positive-space evidence that one hook lattice can carry the whole guardrail
  taxonomy without a second primitive.
implementation_notes: null
category: "Agent Design"
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
  - file: "path-scoped-guardrails-edit-time-prevention.md"
    rel: "same-problem"
  - file: "capability-composition-declared-ordering-constraints.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
tags:
  - "agent-design"
  - "guardrails"
  - "hooks"
---

# Guardrails as Hook-Lattice Capabilities, Not a Separate Primitive

## What It Is

A deliberate framework decision: guardrails are not a distinct abstraction. Instead the
capability base class exposes a complete interception lattice — 7 hook families × 4
phases (before/after/wrap/on-error), each with a typed `Protocol` signature — and every
guardrail-shaped concern is implemented as a capability using those hooks:

- PII redaction → wraps `after_model_request`
- Human approval → wraps `before_tool_execute` (plus per-tool `requires_approval`)
- Cost budgets, input/output guards, prompt-injection defense → third-party capability
  packages (`pydantic-ai-shields`)

Determinism knobs live on the same lattice: hook timeouts with `HookTimeoutError`, args
validators, usage limits. A `Hooks` convenience capability covers function-based
registration without subclassing. (`capabilities/hooks.py`, `docs/capabilities.md`)

## Why It Matters

Agent frameworks keep multiplying primitives — guardrails, middlewares, interceptors,
policies — that are all "code at a lifecycle edge." This is positive-space evidence for
the opposite design: enumerate the lifecycle edges once, completely, and let every
cross-cutting concern be a composition unit on that lattice. Fewer primitives means the
ordering, packaging, and reuse machinery (composition, disclosure, sharing across
agents) is built once and guardrails inherit it for free. For any system deciding
whether "guardrail" deserves its own abstraction, the answer demonstrated here is: only
the interception lattice does.

## Why People Are Using It

Shipped in a top-tier production framework with an emerging third-party guard ecosystem
building on the lattice rather than requesting a new primitive. Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Dedicated guardrail primitive** (many enterprise agent stacks) — clearer intent
  signaling and simpler audits, at the cost of a parallel composition system.
- **External policy layer** (gateway/proxy-level guards) — enforces across
  heterogeneous agents but cannot see intra-run structure (tool args, node boundaries).
- **Edit-time prevention** (path-scoped guardrails) — complements runtime hooks by
  blocking before an action is even proposed.

## Potential Improvements

- An audit view that lists which capabilities intercept which edges — lattice
  completeness makes "what guards this agent?" a query, and frameworks should ship it.
- Severity/veto conventions: hooks that *observe* vs hooks that *block* are currently
  distinguished only by their implementation.

## Potential Failure Modes

- **Lattice gaps** — if a lifecycle edge is missing, guardrail authors work around it
  with fragile hacks; the pattern's strength is exactly proportional to hook coverage.
- **Ordering-sensitive security** — a redaction hook composed inside the logging hook
  leaks; safety now depends on the composition-ordering machinery.
- **Discoverability** — with no named "guardrail" type, security review must trace hook
  implementations to know what protections exist.
