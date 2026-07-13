---
name: "Cheap Reversible Forks Enable Parallel Sampling"
summary: |-
  Once every layer of agent-touched state can be forked cheaply and discarded cheaply
  (copy-on-write filesystem + git + forkable database), a categorically new capability
  appears: run multiple agent attempts on the same task in parallel, keep the attempt
  that works, discard the rest. This exploits agent non-determinism as a resource
  (sample several times, select the best) instead of a defect. The claim from the Replit
  teardown: most AI coding products cannot do parallel sampling not because of model
  limitations but because their state model cannot represent multiple concurrent
  timelines — the snapshot infrastructure had to exist first. Secondhand — verify
  against Replit primary sources.
implementation_notes: |-
  Infrastructure-side complement to the eval-side repeated-sampling literature (solve
  rates scale with attempts, but selection needs a mechanical verifier). Both constraints
  must hold: cheap forks make attempts affordable; a verifier makes selection meaningful.
  Engine analogue today: git worktree isolation for parallel subagent attempts is the
  files-only version of the same precondition.
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "replit-agent-engineering-teardown.md"
related_findings:
  - file: "three-layer-reversible-state-single-undo-surface.md"
    rel: "enabled-by"
  - file: "parallel-independent-workflow-execution-at-scale.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "orchestration"
  - "sandboxing"
  - "infrastructure"
---

# Cheap Reversible Forks Enable Parallel Sampling

## What It Is

Parallel sampling for coding agents: fork the entire working state (files, code history,
database) N times, run N independent agent attempts at the same task, evaluate the
results, keep the winner, discard the losers. The enabling condition is that forks are
near-free to create (copy-on-write shares data until written) and free to destroy — so
attempt count becomes a dial, not an architecture change.

Distinct from `parallel-independent-workflow-execution-at-scale` (many *different* tasks
running concurrently): here it is many attempts at the *same* task, competing.

## Why It Matters

It reorders the usual causality. The instinct is to treat sampling strategy as an
agent-loop concern; this finding says it is a **state-model concern** — products whose
state cannot branch simply cannot offer it, whatever their model quality. For any system
design, the question "could we run three attempts and keep the best?" is answered by the
storage layer, not the prompt. The engine's markdown+git substrate answers yes for
file-shaped work (worktrees/branches are its cheap forks); anything that adds
non-forkable state (a live index, a mutable external store) silently forfeits the
capability.

## Why People Are Using It

Non-determinism is the constant complaint about agents; sampling-and-selection is the
known statistical remedy (repeated-sampling results show solve rates climbing steeply
with attempt count). Replit's snapshot engine is cited as the infrastructure that lets a
consumer product actually exercise it.

## Potential Improvements

- Verifier-coupled sampling: attempt count auto-scales with the availability and
  confidence of a mechanical verifier (tests, type-checks, deploy health), since
  selection quality — not fork cost — is the binding constraint.
- Partial-merge of attempts (cherry-pick the best pieces of losers) rather than
  winner-take-all.

## Potential Failure Modes

- **Selection without a verifier** — N samples with eyeball selection reintroduces the
  human bottleneck N-fold; without a mechanical check the extra attempts are mostly
  spend.
- **Cost multiplication** — every attempt pays full model tokens; parallel sampling is a
  deliberate cost/quality trade, not a free lunch.
- **Shared external side effects** — forks isolate state the snapshot engine owns;
  attempts that call external APIs (emails, payments, deploys) escape the fork boundary
  and must be stubbed or gated.
