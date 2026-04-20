---
name: 'Session Atomicity: Single-Issue Scope Produces Quadratic Cost Reduction'
summary: 'Bounding each agent session to exactly one fine-grained issue reduces context consumption quadratically relative to multi-task sessions, while improving decision quality. The mechanism: smaller
  scope means less prior context loaded, fewer intermediate states tracked, and cleaner handoffs.'
implementation_notes: Requires a persistent work queue (e.g., Beads JSONL issues) so agents can pick up single issues without reading a full plan. Session start = load one issue + its direct dependencies.
  Session end = update issue status + file any discovered issues. No plan hierarchy needed in context.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- steve-yegge-beads-coding-agent-memory.md
related_findings:
- file: incremental-one-feature-per-session-pattern.md
  rel: same-problem
- file: issue-based-agent-orchestration-replacing-markdown-plans.md
  rel: enabled-by
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: same-problem
- file: work-disavowal-failure-mode-context-limit-cheating.md
  rel: mitigates
- file: context-rot-attention-budget-depletion.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: classified
consumed_by: []
---

## What It Is

A session scoping principle: each agent session is bounded to exactly one issue. Yegge's claim is that this produces quadratic cost reduction — "each session will be quadratically cheaper" — because context consumption scales super-linearly with task scope. A session handling N tasks requires O(N²) context (each task's intermediate state pollutes every subsequent task's context), while N sessions each handling one task requires O(N) total context.

The mechanism in Beads:
1. Orchestrator assigns one issue per agent via `bd ls --assignee <id>`
2. Agent loads that issue's context only (no plan hierarchy)
3. Agent works, files any discovered sub-issues, updates status
4. Agent exits — orchestrator queries `bd ready` for next wave

The session boundary is also a natural kill point: agents that are approaching context limits or showing disavowal behaviors can be killed at issue completion without losing work, since state is in the issue store, not agent memory.

## Why It Matters

The quadratic cost claim matters because it inverts the intuition that batching tasks is efficient. In agentic systems, batching tasks into long sessions has a compounding overhead: each task adds to the context that subsequent tasks must parse, plan against, and avoid contradicting. The coordination cost dominates the task cost. Fine-grained sessions with a persistent issue store decouple coordination overhead from execution overhead.

Secondary benefit: decision quality improves when the agent has full context budget for one task rather than partitioned budget across many tasks.

## Why People Are Using It

Yegge designed Beads after observing that agents in long sessions accumulated hierarchical context they couldn't maintain — "the dementia problem." Breaking sessions at issue boundaries means each session starts fresh with a well-defined goal and terminates with a verifiable outcome (issue status updated). The 5+ concurrent agent deployment on the Wyvern project validated that fine-grained issues (128 filed from legacy TODOs) produced coherent progress without session-to-session context bleed.

## Potential Improvements

- Dynamic scope adjustment: if an issue turns out to involve N sub-issues, automatically split and assign rather than expanding the current session's scope
- Session cost telemetry: instrument sessions to measure actual context consumption vs. estimated cost from issue size, tuning the fine-graining heuristic
- Issue size estimation: predict session cost from issue description before assignment, enabling cost-aware scheduling

## Potential Failure Modes

- Over-atomization: issues too fine-grained require more coordination overhead than they save in context overhead — the break-even point depends on orchestrator communication cost
- Context re-loading: if each issue requires loading the same large codebase context, the per-session fixed cost dominates and quadratic savings don't materialize
- Issue dependency latency: agent waits for a blocked issue to be resolved by another agent in a separate session — parallel benefit requires sufficient parallelizable work
- Quadratic claim unverified: Yegge's cost model is intuitive but not empirically validated across different task types and context window sizes
