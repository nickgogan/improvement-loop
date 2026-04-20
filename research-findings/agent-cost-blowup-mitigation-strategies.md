---
name: Agent Cost Blowup Mitigation Strategies
summary: 'Silent Killer #2 in production multi-agent systems: runaway loops, excessive tool calls, and expensive models used everywhere. Mitigations: per-step budgets plus global budget caps, loop termination
  rules, output caching (retrieval + tool results), model tier routing, and fast-fail on missing evidence.'
implementation_notes: MetaSystem has no cost monitoring or budgeting. Claude Code Max subscription insulates from per-token costs currently, but any move to API-based agents would need these controls. The
  fast-fail pattern (refuse to proceed when evidence is insufficient) is immediately applicable to research and proposal skills.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- multi-agent-orchestration-production-playbook-nick.md
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: task-contract-pattern-schema-first-agent.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: capability-saturation-threshold-45-percent.md
  rel: same-problem
- file: competitive-module-development-parallel-teams.md
  rel: contradicts
- file: gsd-stall-detection-revision-loop-escalation.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: multimodel-routing-architecture-specialized.md
  rel: same-problem
- file: scalpel-local-parse-then-llm-cost-optimization.md
  rel: same-problem
- file: agent-sprawl-anti-pattern-microservices-redux.md
  rel: same-problem
- file: agent-type-system-six-roles.md
  rel: same-problem
- file: autoresearch-loop-autonomous-metric-driven.md
  rel: same-problem
- file: claude-code-loop-in-session-cron-scheduling.md
  rel: enables
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: critic-verifier-loop-with-termination.md
  rel: same-problem
- file: emergent-tool-strategy-optimization.md
  rel: same-problem
- file: model-tier-routing-expensive-orchestrator-cheap-s.md
  rel: extends
- file: token-budget-pre-turn-projection.md
  rel: enabled-by
- file: token-waste-taxonomy-and-two-mode-workflow.md
  rel: same-problem
- file: loop-detection-hash-based-sliding-window.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Agent Cost Blowup Mitigation Strategies

## What It Is
Silent Killer #2 in production multi-agent systems. Five mitigation strategies:

1. **Per-step budgets + global budget:** Each workflow step has a token/cost budget; the total workflow has a global cap. Exceeding either triggers graceful degradation, not unbounded spending.
2. **Loop termination rules:** Every iterative pattern (generate-critique, retry, search) has explicit maximum iterations.
3. **Caching:** Cache retrieval results and tool outputs to avoid redundant expensive calls.
4. **Model tier routing:** Use expensive models for orchestration and cheap models for narrow sub-tasks (see model-tier-routing finding).
5. **Fast-fail on missing evidence:** Agents refuse to proceed ("insufficient evidence") rather than hallucinating to fill gaps, which prevents cascading token waste on bad premises.

## Why It Matters
Without cost controls, agent systems exhibit runaway cost growth. A single infinite loop or poorly-configured retry can consume an entire budget in minutes. Cost blowups are the second most common production failure after context rot.

## Why People Are Using It
Nick Gupta identifies this alongside context rot and undebuggable behavior as the three silent killers. The mitigations are drawn from established patterns in cloud cost management (budgets, quotas) and distributed systems (circuit breakers).

## Potential Improvements
Real-time cost dashboards per workflow and agent. Predictive cost estimation before workflow execution. Automatic model downgrade when budget threshold is reached.

## Potential Failure Modes
Over-aggressive budgets that terminate workflows before completion. Caching stale results when tool outputs change. Fast-fail triggering too often on genuinely novel tasks where evidence is sparse.
