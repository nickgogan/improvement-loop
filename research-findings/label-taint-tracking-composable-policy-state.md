---
name: "Label Taint-Tracking as Composable Policy State"
summary: |-
  Omnigent conversations carry schema-declared labels (initial value + allowed values) that
  policies may write only through a per-policy whitelist and that other policies gate on via
  condition selectors — enabling taint-style flows where one policy marks a session (e.g.
  "touched untrusted content") and unrelated policies later tighten behavior because of the
  mark. A key invariant: label writes accumulated on an ASK path apply only if the human
  approves. For us this is the cleanest observed mechanism for policies that need memory
  without policies talking to each other directly.
implementation_notes: null
category: "Governance"
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

A composable state channel between otherwise-independent policies. Omnigent sessions carry **labels** declared with a schema (`LabelDef`: an `initial` value plus the set of allowed `values`). Policies can write labels, but only the keys enumerated in their own `set_labels` whitelist; any policy can declare a `condition:` selector so it is dispatched only when the session's labels match. The demonstration fixture is a taint flow: `taint_on_banana` sets `tainted=1` when trigger content appears, and `ask_when_tainted` (`condition: {tainted: "1"}`) then fires an ASK on every subsequent request. A hard invariant completes the design: label writes and state updates accumulated on an ASK path are applied **only on approval** — a denied ASK leaves no side effects (`omnigent/runtime/policies/approval.py`, POLICIES.md §7.2).

## Why It Matters

Policies frequently need memory — "this session touched untrusted input," "spend crossed a checkpoint," "risk is accumulating" — and the naive designs are either global mutable state (any policy can clobber anything) or policy-to-policy coupling (evaluation order becomes load-bearing). Schema'd labels with write-whitelists and declarative gate conditions give the composition a typed, auditable interface: who may write a fact, what values it may take, and who reacts to it are all declared, not emergent. The no-side-effects-on-denied-ASK invariant prevents a subtle corruption class where a refused action still mutates the state that future policies gate on.

## Why People Are Using It

Observed in [omnigent](https://github.com/omnigent-ai/omnigent) v0.6.0.dev0 (alpha) — see [[omnigent-analysis]] for structural details (`omnigent/spec/types.py` `LabelDef`/`PolicySpec.condition`, taint fixture `e2e-label-ask-gate`). Omnigent's own `risk_score_policy` builds on the same state channel to accrue per-session risk and escalate.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Session-state counters | Untyped key-value state each policy reads/writes | Single-policy state (e.g. a call counter) with no cross-policy consumers |
| Policy chaining | One composite policy encoding the whole flow | When the flow is genuinely one policy's logic, not a composition |
| External risk service | Out-of-band system scoring the session | Fleet-level signals spanning many sessions |

## Potential Improvements

- Label provenance (which policy set this value, when) for audit trails
- Time-decaying labels for taint that should expire rather than persist for the session's life

## Potential Failure Modes

- **Label-schema sprawl:** every new interaction between policies mints a label; the namespace becomes its own governance problem
- **Silent gating:** a policy skipped by `condition:` looks identical to a policy that evaluated ALLOW — debugging needs engine-level traces
- **Taint without untaint:** one-way flows can ratchet a long session into permanent friction unless a release path is designed in
