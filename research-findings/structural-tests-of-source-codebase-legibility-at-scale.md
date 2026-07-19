---
name: 'Structural Tests-of-Source — Codebase Legibility as a Context-Budget Constraint'
summary: |-
  A distinct test category — tests that assert facts about the shape of the source tree
  itself, separate from both syntax lints and behavioral tests. Concrete instances from a
  750-package PNPM workspace (Lopopolo, OpenAI): a hard file-length cap (350 lines,
  motivated explicitly by "if we know context is limited, we can write a test that
  limits [this]"); package-privacy enforcement; dependency-edge rules between
  architectural layers; and duplication checks forcing one canonical implementation of
  shared primitives. Stated cause: agents left alone "optimize for local coherence of a
  package" rather than reusing shared utilities. Design goal stated explicitly: minimize
  the tokens required for a model to predict what's acceptable, by minimizing variance in
  how equivalent things are done across the codebase — "code in the file system is also
  text, which means it's effectively prompts."
implementation_notes: |-
  The engine's own frontmatter schema validation (validate_frontmatter.py, pre-commit) is
  already a structural test in spirit (asserting shape, not behavior); the specific gap
  this finding surfaces is codebase/skill-directory-shape checks (e.g., a skill file
  exceeding a size budget, or duplicated logic across skills) that IL doesn't currently
  enforce mechanically.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- harness-engineering-humans-steer-agents-execute.md
related_findings:
- file: code-as-compiled-artifact-of-a-spec.md
  rel: extends
- file: harness-engineering-third-evolution.md
  rel: extends
- file: lint-test-failures-as-remediation-prompts.md
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

Tests that assert facts about the shape of the source tree, distinct from syntax lints
(which check individual statements) and behavioral tests (which check what code does).
Concrete instances at a 750-package PNPM-workspace scale: a hard cap on file length (350
lines), justified directly by context-budget reasoning rather than readability
conventions; package-privacy enforcement (which APIs are public versus internal to a
package); dependency-edge rules between architectural layers; and duplication checks that
force a single canonical implementation of shared primitives (one bounded-concurrency
helper, one observable/instrumented command wrapper) instead of letting each package
reinvent its own. The stated cause these tests were built to counter: agents left alone
tend to optimize for *local* coherence — solving a problem correctly within the file or
package in front of them, using a slightly different pattern than the rest of the
codebase already uses for the same problem. Structural tests catch that drift
mechanically, rather than relying on a human reviewer to notice cross-package
inconsistency buried in a large diff.

## Why It Matters

The stated design goal is explicit and unusual: minimize the tokens required for a model
to predict what's acceptable, by minimizing variance in how equivalent things are done
across the codebase — "code in the file system is also text, which means it's effectively
prompts... regardless of where in the repository your agent is looking, it develops a ton
of transferable context." This reframes codebase consistency from a maintainability
nice-to-have into a context-engineering lever with a measurable payoff: less exploration
needed per task, fewer tokens spent re-deriving local convention. At 750 packages it's
also a concrete scale data point for how far "one canonical way to do X" can be
mechanically enforced rather than socially maintained through review alone.

## Why People Are Using It

Production account from a team that started with a single flat package and, after
hitting exactly the coherence-drift problem described above, restructured to a heavily
domain-isolated architecture specifically to give the agent "concrete hooks in the file
system to determine which domains were separate from the other ones" — the restructuring
was agent-legibility-motivated, not primarily a human-organizational choice.

## Potential Alternatives

- **Rely on the code-review layer** (garbage-collection-day-persona-review-agents.md) to
  catch structural drift after the fact: cheaper to set up, but reactive and dependent on
  a reviewer noticing a cross-package inconsistency — exactly the kind of low-signal
  pattern-matching humans are worst at over large diffs.
- **One-time architectural audit rather than continuously-enforced tests:** catches drift
  at snapshot points instead of preventing it from landing in the first place.

## Potential Improvements

- A minimum-viable structural-test starter set (file-length cap, one
  canonical-implementation-per-primitive check) rather than requiring the full
  package-privacy/dependency-edge apparatus before getting any benefit.
- Tooling to detect *candidate* structural rules from observed agent drift
  automatically — the same "durable class of failure" identification that garbage
  collection day does manually, applied specifically to structure rather than review
  feedback.

## Potential Failure Modes

- **Artificial splits:** a hard file-length cap can force awkward divisions on genuinely
  cohesive files — the constraint optimizes for context budget at a possible cost to
  human readability if applied without judgment.
- **Retrofit cost:** migrating an existing codebase to satisfy new structural tests is
  itself a large-scale refactor — only cheap in a world already deep into agent-driven
  "large-scale refactoring is free" development, not a good zero-to-one starting move.
- **Over-uniformity:** forcing "one way to do X" everywhere can suppress legitimate local
  variation where a domain genuinely needs a different pattern than the rest of the
  codebase.
