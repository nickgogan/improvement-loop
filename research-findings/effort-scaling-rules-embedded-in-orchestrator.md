---
name: "Effort Scaling Rules Embedded in Orchestrator"
summary: "Embed explicit resource allocation rules in the lead agent prompt: 1 subagent/3-10 calls for factual queries, 2-4 subagents/10-15 calls for comparisons, 10+ subagents with divided roles for complex research. Prevents overinvestment in simple queries and underinvestment in complex ones."
implementation_notes: "Directly applicable to MetaSystem's research-loop and any orchestrator skill. Add explicit scaling rules to orchestrator prompts."
category: "Orchestration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-multi-agent-research-system.md"
related_findings:
  - file: "sub-agent-context-isolation-for-parallel-complex.md"
    rel: "extends"
  - file: "orchestrated-execution-one-task-per-sub-agent-wit.md"
    rel: "extends"
  - file: "agent-cost-blowup-mitigation-strategies.md"
    rel: "same-problem"
  - file: "task-complexity-tiering-quick-campaign-deep-build.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

Explicit rules embedded in the lead agent's prompt that govern resource allocation based on query complexity. Anthropic's multi-agent research system uses three tiers: (1) Simple factual queries: 1 subagent, 3-10 tool calls. (2) Comparison queries: 2-4 subagents, 10-15 tool calls. (3) Complex multi-source research: 10+ subagents with explicitly divided roles. Without these rules, early versions of the system would spawn 50 subagents for a simple factual question, wasting tokens and time.

## Why It Matters

Token usage explains 80% of the performance variance in multi-agent systems (per Anthropic's analysis). Effort scaling rules are the primary mechanism for controlling token budget. They transform the lead agent from a naive "spawn as many subagents as possible" strategy to an intelligent resource allocator that matches investment to task complexity.

## Why People Are Using It

Anthropic's production multi-agent research system. The pattern directly addresses the cost blowup problem (identified as "Silent Killer #2" in production multi-agent systems) by making resource allocation explicit and deterministic rather than leaving it to model judgment.

## Potential Improvements

Dynamic scaling based on intermediate results (start small, expand if initial results are insufficient). Historical cost tracking per query type to calibrate scaling rules empirically.

## Potential Failure Modes

Static rules may under-allocate for unusually complex instances of "simple" query types. Over-rigid rules prevent the system from adapting when a seemingly simple query requires deep investigation. Rules need periodic recalibration as model capabilities and costs change.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[effort-scaling-rules-embedded-in-orchestrator]] in `extracts/patterns/`
