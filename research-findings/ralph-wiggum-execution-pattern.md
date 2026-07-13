---
notion_id: 32b1e08b-9b34-8106-995b-c0422e4bf83a
name: Ralph Wiggum Execution Pattern
summary: Persistent deep execution on individual complex IB items using a bash loop with plan.md, pass verification, and fresh context per iteration. Best for heavyweight items requiring multiple passes.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
- anthropic-long-running-claude-scientific-computing.md
- anthropic-effective-harnesses-long-running-agents.md
- anthropic-building-c-compiler.md
- gstack-gsd-superpowers-orchestrator-headless.md
proposals: null
date_discovered: '2026-03-15'
last_updated: '2026-07-13'
related_findings:
- file: stop-rules-as-execution-boundaries.md
  rel: enabled-by
- file: ralph-loop-brute-force-security-and-ui-testing.md
  rel: extends
- file: loop-node-anatomy-schema-enforced-ralph-primitive.md
  rel: extended-by
pipeline_status: "extracted"
consumed_by:
  - "skills/ralph-wiggum-execution-pattern.md"
---
# Ralph Wiggum Execution Pattern

## What It Is
Ralph Wiggum is a depth-first execution pattern for complex individual IB items. It runs a bash loop that maintains a plan.md file tracking progress across iterations. Each iteration starts with a fresh context window, executes a single pass, then tests against pass/fail criteria before looping. The loop continues until the item passes verification or a maximum iteration count is hit.

**Updated 2026-03-22:** Additional implementation detail from production testing ("You're Using Ralph Wiggum Loops WRONG"): the correct implementation uses headless Claude (`claude -p`) spawned per task — not the Anthropic-published Ralph Wiggum plugin, which runs within the same session and causes context rot. Each iteration: (1) reads the spec.md and implementation plan thoroughly; (2) picks the highest-leverage unchecked task; (3) implements the task; (4) writes an unbiased unit test and verifies it passes; (5) marks the task complete in the plan. The 'dumb zone' threshold for Opus is ~100k tokens — fresh-context loops stay well below this throughout. Source: [You're Using Ralph Wiggum Loops WRONG](https://www.youtube.com/watch?v=I7azCAgoUHc)

## Why It Matters
Complex IB items — database schema migrations, multi-file refactors, multi-step Notion configurations — often can't be completed in a single agent pass. Ralph Wiggum provides structure for iterative refinement without requiring human intervention between passes, making deep work automatable.

**Updated 2026-03-22:** Traditional vibe coding accumulates context until compaction is forced, causing the model to work increasingly in the 'dumb zone' where intelligence degrades rapidly. Ralph loops sidestep this entirely by externalizing state to the spec/plan file rather than the context window — meaning even very long projects can be implemented at full model intelligence throughout. The core appeal is autonomous, overnight implementation: spin up a loop, go to sleep, wake up to completed features. Source: [You're Using Ralph Wiggum Loops WRONG](https://www.youtube.com/watch?v=I7azCAgoUHc)

## Why People Are Using It
Ralph Wiggum is designed as the depth complement to GSD's breadth: GSD handles many simple items in parallel waves, while Ralph handles one hard item thoroughly. The reference file and bash script already exist in the vault, confirming the pattern has been evaluated and staged for S3 deployment.

## Potential Improvements
Integrating Ralph Wiggum with PROGRESS.md would enable true cross-session deep execution — the loop could be paused, checkpointed, and resumed in a later session without losing state. This would remove the current implicit constraint that complex items must complete within a single session.

## Potential Failure Modes
If pass/fail criteria in plan.md are ambiguous or under-specified, the bash loop can enter an infinite cycle where each iteration makes marginal changes but never reaches a clean pass state. The pattern also assumes the item is genuinely self-contained; items with hidden dependencies on other IB completions will fail silently.

**Updated 2026-03-22:** Additional failure modes confirmed in production: a bad spec cascades errors across all iterations because each loop builds on the previous one's output — a bug introduced early poisons later loops. Tests written by the model may be biased toward passing rather than truly testing correctness. Not token-efficient for parallel runs — cost scales super-linearly. Critically: the Anthropic-published Ralph Wiggum plugin runs within the same session (causing context rot) — avoid it in favor of the bash `claude -p` implementation. Source: [You're Using Ralph Wiggum Loops WRONG](https://www.youtube.com/watch?v=I7azCAgoUHc)

**Updated 2026-04-09 (Anthropic Tier 1 evidence):** Anthropic's "Long-running Claude for scientific computing" blog post confirms the Ralph loop as a key orchestration pattern for multi-day autonomous work. Anthropic describes it as scaffolding to combat "agentic laziness" — the tendency of models to make excuses to pause on complex tasks. The Ralph loop provides capability uplift via minimal prompt engineering, RAG, or context stuffing, and is expected to become less necessary as models improve. The scientific computing workflow used the Ralph loop to drive a cosmological Boltzmann solver reimplementation over multiple days, achieving sub-percent accuracy against a reference implementation. This is the strongest production evidence for the Ralph loop pattern to date — Anthropic themselves deploying it for sustained autonomous execution. Evidence strength upgraded from Medium to Strong.

**Updated 2026-07-13 (Archon v0.5.0 — Ralph as a schema-enforced engine primitive):** Archon promotes the Ralph loop from a bash/prompt idiom to a first-class `loop:` workflow-engine node whose config schema covers the full loop anatomy — signal-string `until` plus deterministic `until_bash` completion checks, a required `max_iterations` budget, `fresh_context: true` per-iteration session reset with `$LOOP_PREV_OUTPUT` bridging the prior iteration's cleaned output, optional per-iteration human gates, and iteration-level events/metrics. The primitive is exercised in production by the shipped `archon-ralph-dag.yaml` default workflow (PRD-driven, one story per fresh-context iteration, then PR). This corroborates the pattern's core moves (fresh context per pass, state externalized to plan/spec artifacts, pass/fail verification per iteration) and hardens them into load-time schema validation. Details in [[loop-node-anatomy-schema-enforced-ralph-primitive]]; structural analysis in [[archon-analysis]].

## Extraction Note — 2026-05-25
Extracted as **skill**: [[ralph-wiggum-execution-pattern]] in `extracts/skills/`
