---
name: Lint and Test Failure Messages Written as Remediation Prompts
summary: |-
  Treat every lint rule and test-failure message as a prompt-injection surface, not a
  diagnostic string. Worked example (Lopopolo, OpenAI): a generic failure ("unknown type
  at this depth") tells the model nothing actionable; a remediation-shaped failure ("you
  shouldn't have an unknown here at all — we parse, don't validate, at the edge, and this
  value has a derived type from zod") states the convention, the reason, and the fix in
  the same breath the failure fires. Generalized: "prompts powers, prompts rules files,
  prompts skills, prompts these lint error messages, prompts review agents" — every layer
  of the harness that can carry text to the model is a place to inject the standard.
  Extensions: shell out to the agent to write the remediation prompts themselves when
  that becomes its own time sink; embed an agent SDK call directly inside a test for
  checks too fuzzy for a regex/AST rule, so the "test" is itself an LLM judgment call.
implementation_notes: |-
  Directly actionable on the engine's own tooling: operations/kb-maintenance-scripts/
  validate_frontmatter.py is exactly this class of gate (a pre-commit hook enforcing
  YAML/frontmatter conventions). Auditing whether its failure messages are
  remediation-shaped (cite the actual rule, the fix, the schema section) versus terse is
  a concrete near-term improvement.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- harness-engineering-humans-steer-agents-execute.md
related_findings:
- file: harness-engineering-third-evolution.md
  rel: extends
- file: ai-shepherding-anti-pattern-manual-workflow-sequencing.md
  rel: same-problem
- file: structural-tests-of-source-codebase-legibility-at-scale.md
  rel: same-problem
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
  - agent-workflow-and-execution.md
---

## What It Is

A collapse of the usual distinction between "prompts" (deliberately authored context:
CLAUDE.md, skill files) and "lint/test output" (assumed to be terse, machine-directed
diagnostic text). The practice: write every failure message as if it were a prompt,
because from the model's perspective, at the moment it's reading a failed CI run, it is
one. The worked example: a bare failure naming the symptom ("unknown type at this depth,"
"why is the model writing a function called `isRecord`") doesn't change repeat behavior;
a failure that states the codebase's convention, the reason for it, and the specific fix
("you shouldn't have an `unknown` here — we parse, don't validate, at the edge") does,
because it's legible as an instruction rather than a symptom report. Two extensions
described alongside the core pattern: (1) when authoring good remediation prompts becomes
its own time sink, shell out to the agent — pointing a coding agent at an internal
prompting-cookbook and having it synthesize a reusable skill for writing prompts, then
using that skill to write the lint-remediation text itself; (2) for checks too
judgment-shaped for a regex or AST rule, embed an agent SDK call directly inside a test,
so the "test" is an LLM call assessing the code's acceptability rather than a fixed
assertion.

## Why It Matters

Most teams treat lint/test output as machine-to-human diagnostic text and prompts as a
separate, deliberately-authored artifact. Collapsing that distinction turns the
highest-frequency touchpoint an agent has with "did I do this right" — the CI failure —
into a teaching moment instead of a bare pass/fail signal, at zero marginal authorship
cost per future occurrence (write the remediation text once; it fires on every future
violation for free). It's also the mechanism-level detail underneath
garbage-collection-day-persona-review-agents.md's "convert PR feedback into a failing
test" step — this finding specifies what makes that failing test's message actually
load-bearing for a model reading it cold, with no memory of the PR comment that
originally prompted the fix.

## Why People Are Using It

Direct production account: described as the team's default authoring pattern for every
custom ESLint rule and structural test across a 750-package workspace, motivated by the
observation that terse failure messages simply didn't change model behavior on repeat
offenses — the model needed the "why" and the "what instead," not just the "no."

## Potential Alternatives

- **Terse machine-readable errors + a separate troubleshooting doc:** lower authoring
  cost per rule, but relies on the model choosing to go look, which a bare failure
  message doesn't force.
- **Auto-fix tooling** (the linter rewrites the code directly instead of explaining):
  works for mechanical fixes, but has no answer for judgment-shaped violations
  (architecture, taste) that need explanation in order to generalize to the next
  unforeseen case.

## Potential Improvements

- A style guide for remediation-prompt authorship itself (how much "why," how much "what
  instead," how to reference other conventions without bloating every message) —
  currently ad hoc per rule in the source.
- Track which remediation prompts actually reduce repeat violations versus which get
  silently reworked around, to prioritize rewrite effort toward the ones that aren't
  working.

## Potential Failure Modes

- **Convention drift:** a remediation prompt can keep citing a rule or pattern that's
  since changed, the same way any embedded documentation drifts from current reality.
- **Token cost compounding at the worst moment:** verbose remediation text in every
  failure adds cost exactly when a CI run may be re-triggered several times in a row.
- **Nondeterminism creep:** embedding an agent SDK call inside a test introduces a
  costed, nondeterministic network call into what's conventionally a fast deterministic
  gate — needs explicit scoping to checks that genuinely can't be expressed as a
  mechanical rule, or it erodes the reliability the rest of the harness depends on.
