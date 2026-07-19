---
name: Code as a Compiled Artifact of a Spec (LLM-as-Fuzzy-Compiler Framing)
summary: |-
  A named mental model (Lopopolo, OpenAI) for why harness-engineering's constraint-writing
  (docs, lints, review-agent rules, structural tests) is the real engineering work, and
  the literal code is disposable: "code is a disposable build artifact... we can publish
  a library that's actually a super well-defined spec that the code is a compiled
  artifact of." Explicit analogy to LLVM/Rust: harness constraints are the equivalent of
  static-analysis and optimization passes determining which programs are acceptable to
  emit; the model is the swappable code-generation backend (like choosing LLVM vs.
  Cranelift); different models emit different literal code from the same spec, and that's
  expected — the constraint system, not the generated code, is what should be held stable
  and reviewed with care.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- harness-engineering-humans-steer-agents-execute.md
related_findings:
- file: harness-engineering-third-evolution.md
  rel: extends
- file: structural-tests-of-source-codebase-legibility-at-scale.md
  rel: enables
- file: template-generated-skills-multi-host.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: raw
consumed_by: []
---

## What It Is

A named mental model for what deserves careful review and version control versus what
should be treated as freely regeneratable. The claim, offered directly in response to an
audience question ("is code a disposable build artifact?" — "Yes."): a well-defined spec
— captured across docs, lints, review-agent rules, and structural tests — is the durable
artifact; the code a model emits from that spec is a compiled output, analogous to the
machine instructions a compiler backend emits from source. The explicit analogy is
LLVM/Rust: harness constraints (lints, docs, tests, structural rules) play the role of
static-analysis and optimization passes that determine which programs are acceptable to
produce in the first place; the model is the swappable code-generation backend (changing
models is "like changing your code generation backend from LLVM to Cranelift in the Rust
compiler"); different models will emit different literal code ("different x86
instructions") from the same spec, and that variance is expected and acceptable as long
as the constraint system — not the specific generated code — is what's held stable and
reviewed.

## Why It Matters

This reframes what should be protected-and-reviewed versus what should be treated as
regeneratable. If code is the "x86 instructions" and harness constraints are the
"source," then a model upgrade or provider swap is expected to change the literal code
while behavior-under-spec stays constant — a very different posture than reviewing every
diff as if it were hand-authored and precious. It's the philosophical frame that makes
structural-tests-of-source-codebase-legibility-at-scale.md's practice ("large-scale
refactoring is free, fire off 15 agents to finish a stalled migration") read as a
principled default rather than a risky one-off: if the constraint system genuinely
determines acceptability, regenerating the code under it is safe by construction.

## Why People Are Using It

Offered as Lopopolo's own answer to a direct audience question rather than a documented
team process — a stated mental model more than a measured practice, which is why this is
rated Medium evidence despite sitting inside an otherwise strong-evidence production
account.

## Potential Alternatives

- **Code as the primary artifact, spec/docs as secondary support** (the conventional
  posture): matches how most teams already work, and doesn't require the harness-
  constraint apparatus this framing presupposes in order to be worth much.
- **Spec-as-tests** (behavior pinned by an executable test suite rather than by "what a
  good job looks like" documentation): a narrower, more mechanically-checkable version of
  the same instinct, with less room for the fuzzy/interpretive constraints (ADRs,
  personas) this framing explicitly includes.

## Potential Improvements

- Concretely defining, for a given codebase, which artifacts are "spec" (protected,
  carefully reviewed) versus "compiled" (freely regeneratable) — the framing is evocative
  but doesn't itself supply the boundary.
- A worked example of an actual model-swap regenerating a component from spec, with
  before/after diffs, to test whether the analogy holds under a real provider change
  rather than remaining a rhetorical device.

## Potential Failure Modes

- **Under-review risk:** the analogy can be used to justify under-reviewing generated
  code ("it's just compiler output") in codebases where the harness constraints aren't
  actually tight enough to guarantee equivalent behavior across model swaps — LLVM's
  optimization passes are formally verified in ways prompt-based constraints are not.
- **Fuzziness in both directions:** treating documentation/lints as the sole spec risks
  the spec itself becoming under-specified prose that different models interpret
  differently — "fuzzy compiler" cuts both ways; the fuzziness lives in the spec-reading
  step too, not only the code-generation step.
