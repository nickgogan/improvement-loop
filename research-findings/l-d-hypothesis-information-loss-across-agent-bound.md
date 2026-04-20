---
notion_id: 32c1e08b-9b34-8150-a949-c0e254a86a6e
name: 'L > D Hypothesis: Information Loss Across Agent Boundaries'
summary: Information loss across agent boundaries (L) typically exceeds context degradation from long contexts (D). Multi-agent swarms degrade sequential tasks by 39-70%. Subagents justified only for parallelizable,
  lossy-tolerant tasks. Context windows improve faster than inter-agent communication.
implementation_notes: 'Validates preference for single-agent execution. Formalize a pre-spawn checklist: is the task parallelizable? lossy-tolerant? context-window-limited? Google''s empirical paper (2512.08296)
  confirms: independent agents amplify errors 17.2x, centralized 4.4x.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- agent-orchestrators-are-bad.md
- multi-agent-orchestration-production-playbook-nick.md
proposals: []
date_discovered: '2026-03-23'
last_updated: '2026-04-09'
related_findings:
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: extended-by
- file: specialization-theater-anti-pattern.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
# L > D Hypothesis: Information Loss Across Agent Boundaries

## What It Is
A formalization of when multi-agent systems help vs hurt. Two variables: D (degradation from long context within a single agent) and L (information loss across the boundary between agents). When L > D, subagents make things worse. The hypothesis: for most tasks, L > D, making single-agent execution preferable.

## Why It Matters
Agent orchestrator hype pushes teams toward multi-agent architectures by default. This framework provides a principled decision boundary.

## Why People Are Using It
Backed by Google's empirical analysis across 180 configurations: independent agents amplify errors 17.2x, centralized coordination 4.4x.

## Potential Alternatives
Single-agent with extended context, checkpoint-and-resume patterns, shared memory/scratchpad architectures.

## Potential Improvements
L could potentially be reduced through structured handoff protocols, shared memory stores, or training models specifically for agent-to-agent communication.

## Potential Failure Modes
Overreacting by avoiding all subagent use. The L > D threshold varies by task type. As context windows grow, single-agent approaches may hit different scaling limits.

## April 2026 Update: Convergent Evidence

**Nick Gupta's production playbook** independently confirms the L > D hypothesis through a different lens: context rot (information decay within single agents) is identified as "Silent Killer #1" but is addressable through state machines, contracts, and structured summarization. Information loss across agent boundaries lacks equivalent mitigations -- you cannot "summarize" what was never communicated.

**Capability saturation threshold:** Research shows multi-agent coordination yields diminishing/negative returns once single-agent baselines exceed ~45% performance, providing a concrete decision threshold for the L > D tradeoff.

**Legitimate domains taxonomy:** The "Agent Orchestrators Are Bad" essay identifies four task types where L < D (research, debugging, mechanical operations, review) -- all characterized by parallelizability and tolerance for lossy handoffs.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[single-agent-default-l-greater-than-d.md]] in `extracts/patterns/`
