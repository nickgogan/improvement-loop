---
name: "Pre-Merge Reconciliation Queue for Concurrent Agent Changes"
summary: |-
  Namespace's proposed replacement for the PR-as-unit-of-work model once many agents
  write code concurrently against the same codebase. Near-term shape already in use at
  Namespace and cited customers (Fal, Zed, Ramp): work starts from a written intent/
  plan rather than a diff, an agent harness checks out a well-known commit and
  self-validates against the repo's own build/test assets, and a human check-in
  ("continue" is now the most common human utterance) gates progress before a
  conventional merge queue. The forward-looking extension — "weeks to months, not
  years" out — is the actual reconciliation queue: because so many agent-authored
  changes are in flight at once against the same codebase, they land in a "pre-merge"
  queue instead of going straight to the repository, where a reconciliation process
  resolves them against each other for serializability before the ledger write. Real
  number backing the urgency: Namespace's own team's PR-equivalent volume is already
  "four times as big as before" agent-driven development.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "cicd-is-dead-continuous-compute-and-computers.md"
related_findings:
  - file: "velocity-vs-operational-discipline-risk-pattern.md"
    rel: "same-problem"
  - file: "review-outcome-not-diff-for-agent-changes.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "synthesized"
consumed_by:
  - "autonomous-scheduled-agent-operation.md"
tags:
  - "orchestration"
  - "ci-cd"
  - "tools"
---

## What It Is

Namespace's (Hugo Santos, CEO; co-presented with NEA partner Madison Faulkner) proposed
architecture for software delivery once code generation and self-validation both run
fast and largely autonomously. Today's shape, already running at Namespace and named
customers (Fal, Zed, Ramp): there is no PR as the starting artifact. Work begins from a
written intent/plan — a spec captured wherever ("a linear ticket," Slack, anywhere) — an
agent harness (Amp, Cursor, Factory, and similar are named as examples) checks out a
**well-known commit** (an enforced invariant, not an arbitrary starting point), runs
**internal validation** using the repository's own build/test assets, and checks in
with a human ("does this look good? should I change something?" — "continue" is
described as now the most common human utterance). The change then reaches a
conventional merge queue and lands in the git ledger. This is "fast, but not fast
enough," because external validation still has a human in the loop at every step.

The named forward extension — the reconciliation queue proper — addresses what happens
once code generation and internal validation get fast enough that **many agents are
producing changes concurrently against the same codebase**. Because there are too many
concurrent in-flight changes to merge one at a time, they don't go straight into the
repository. They land in a queue Namespace calls **pre-merge**: "a queue of changes
that are done. They would have been merged if the process of merging was fast enough."
A reconciliation process resolves the queued changes against each other for
serializability — "you actually can guarantee that all the changes go back to back
into your ledger" — before anything reaches the repository. The framing is explicitly
database-shaped: merging becomes a single-ledger serialization problem (lock, commit,
release) rather than a per-PR review workflow. Human-scale merge conflicts were rare
because humans naturally throttled the rate of change; agent-scale concurrent writers
make conflicts the default case, not the exception.

## Why It Matters

The concrete number behind the urgency: Namespace's own team's PR-equivalent volume is
"four times as big as before" agent-driven development — at that volume, "it's
impossible for a human reviewer to look at every single PR." **Coordination is named as
moving out of CI entirely** — CI's traditional role of gating and ordering changes
dissolves into something that runs continuously as part of the agent loop, rather than
existing as a discrete pipeline stage a human or bot triggers after the fact.

## Why People Are Using It

Namespace (a compute-infrastructure vendor purpose-built for agentic dev workflows) and
its cited customers (Fal, Zed, Ramp) are already operating in the "no-PR, intent-first,
human-checks-in" shape described above. Mitchell Hashimoto's (HashiCorp founder) public
writeup on "what he would do to fix GitHub" is cited as independent convergent support
for the broader thesis that GitHub-era CI/CD tooling was not built for inference-scale
change volume.

## Potential Alternatives

- **Traditional per-PR merge queue** (e.g., GitHub's native merge queue) — works at
  human-authored volume; the talk's explicit claim is that it breaks down at
  agent-authored volume, where thousands of short-lived branches pulling the codebase
  in different directions make merging "impossible."
- **Throttling agent commit throughput** to stay within human-scale merge-queue
  capacity — not discussed in the source, but a simpler alternative that trades agent
  throughput for infrastructure simplicity.
- **`velocity-vs-operational-discipline-risk-pattern`** (existing finding) — addresses
  the adjacent risk (configuration drift, security leaks from high shipping velocity)
  via "boring" validation primitives, but does not solve the specific concurrent-write
  conflict problem this pattern targets.

## Potential Improvements

No concrete reconciliation algorithm is given — the talk names serializability as the
goal, not the mechanism. The actual conflict-resolution logic is the load-bearing
unbuilt part of this vision.

## Potential Failure Modes

- **Vision/pitch register** — presented as "where we're headed," not a documented
  production system; the reconciliation mechanism itself (how conflicting agent changes
  actually get resolved before the ledger write) is asserted, not shown or measured.
- **Unspecified semantic grouping** — batching multiple agents' changes into one
  human-reviewable unit is named as necessary but never specified; too-large groupings
  overwhelm the human, too-small groupings reintroduce the original volume problem (see
  the companion `review-outcome-not-diff-for-agent-changes` finding, which depends on
  this grouping working).
- **Attribution loss** — a reconciliation queue that reorders or merges intent across
  multiple agents risks making "whose plan actually shipped" ambiguous once several
  agents' candidate changes have been reconciled together.
