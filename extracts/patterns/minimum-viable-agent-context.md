---
title: "Minimum Viable Agent Context"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "agent-context-kiss-commandments-minimum-viable"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent architecture must support per-agent context configuration. A mechanism for measuring per-call token consumption must exist or be implementable. Stable context (system prompts, tool definitions) must be identifiable and separable from dynamic context."
  invariants: "No agent receives context outside its task scope. Stable context is always cached. Token cost per agent call is measured, not estimated. Reference material arrives pre-processed for consumption, not raw."
  governance: "Owned by Meta-System knowledge layer. Per-agent context scoping decisions require review by the system that owns the agent. Changes to caching strategy require cost-impact analysis."
  recovery: "If an agent produces incorrect output due to insufficient context, widen scope for that agent type and document the minimum context boundary. If token measurement breaks, halt optimization until measurement is restored -- do not optimize blind."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Minimum Viable Agent Context

**Source:** [[agent-context-kiss-commandments-minimum-viable]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems burn tokens at scale -- hundreds of thousands to millions per project. Unlike human chat sessions where waste scales linearly (sessions per day), agent token waste scales multiplicatively (thousands of calls per day). The five most common architectural mistakes are: dumping full documents instead of relevant chunks, passing raw unprocessed reference material, failing to cache stable context, giving every agent the entire knowledge base, and never measuring what is consumed. These mistakes compound: a 10x increase in model cost (e.g., from Opus to a future Mythos-class model) turns sloppy practices from expensive into unviable.

## Forces

- **Sufficiency vs. efficiency.** Agents need enough context to produce correct output, but every excess token degrades performance (models perform worse in irrelevant context) and increases cost.
- **Convenience vs. discipline.** Passing everything to every agent is easy to implement. Scoping context per agent requires upfront architectural work.
- **Quality vs. cost.** Over-indexing on token cost can push teams toward cheaper models where quality models are genuinely needed. The optimization target is efficiency at the required quality level, not minimum cost.
- **Observability vs. overhead.** Instrumenting every agent call adds engineering complexity, but without measurement, optimization is guesswork.

## Solution

Apply five rules to every agent in a multi-agent system:

1. **Index references, don't dump documents.** Retrieval should scope what the model sees to what it needs for the current task. If an agent receives a raw document set instead of relevant chunks, the architecture has failed. Use index files, search, or pre-filtered retrieval -- not bulk injection.

2. **Pre-process context for consumption.** Reference material should arrive ready to be used, not ready to be read. Pre-summarize, pre-chunk, and pre-format before injection. If the model's first several thousand reasoning tokens are spent parsing raw input, that is wasted compute.

3. **Cache all stable context.** System prompts, tool definitions, persona instructions, and stable reference material should use prompt caching. Cached tokens cost 90% less (e.g., $0.50/M vs $5/M on Opus). This is the lowest-effort, highest-impact optimization.

4. **Scope each agent to minimum needed context.** A planning agent does not need the full codebase. An editing agent does not need the project roadmap. Define what each agent type needs and enforce that boundary. If agents need dynamic context, give them a searchable, pre-processed repository -- not the entire knowledge base.

5. **Measure what you burn.** Instrument every agent call: input tokens, output tokens, model used, cost. Track these metrics over time. Most teams optimize for semantic correctness and ignore cost because it is not yet prohibitive -- but costs will increase as models improve.

## Consequences

**Positive:**
- 8-10x token reduction is achievable from clean practices alone, per production reports.
- Models produce better output with scoped, relevant context vs. being drowned in irrelevant material.
- Caching provides immediate cost reduction (90% on stable context) with minimal engineering effort.
- Measurement creates a feedback loop that enables continuous optimization.

**Negative:**
- Aggressive context scoping (rule 4) can starve agents of context they actually need, producing incorrect outputs. The boundary between "minimum viable" and "insufficient" requires per-task-type calibration.
- Pre-processing context (rule 2) adds a build step and maintenance burden. Pre-summaries can themselves lose important details.
- Instrumentation (rule 5) adds engineering complexity and may require infrastructure (logging, dashboards, alerting).
- Over-optimizing for cost can lead to choosing cheaper models where quality is the binding constraint.

## Known Uses

- **Production agent deployments** documented by Nate B Jones, operating at hundreds of millions of tokens per deployment. The five rules are described as hard-won lessons from agent systems at scale.
- **Prompt caching on Anthropic API.** Cache hits on Claude Opus cost $0.50/M vs $5/M standard input, providing the 90% discount referenced in rule 3.
- **MetaSystem's existing index-file pattern** partially implements rule 1 (index references). The pointers-over-copies finding extends this with reference indirection.

## Contract

### Preconditions

- Agent architecture must support per-agent context configuration (not a single shared context for all agents).
- A mechanism for measuring per-call token consumption must exist or be implementable.
- Stable context (system prompts, tool definitions, persona instructions) must be identifiable and separable from dynamic context.

### Invariants

- No agent receives context outside its defined task scope.
- Stable context is always cached when the platform supports it.
- Token cost per agent call is measured, not estimated.
- Reference material arrives pre-processed for consumption, not in raw form.

### Governance

- Owned by Meta-System knowledge layer.
- Per-agent context scoping decisions require review by the system that owns the agent.
- Changes to caching strategy require cost-impact analysis before deployment.

### Recovery

- If an agent produces incorrect output traceable to insufficient context, widen scope for that agent type and document the revised minimum context boundary. Never silently add "just in case" context -- document why it is needed.
- If token measurement infrastructure breaks, halt optimization efforts until measurement is restored. Do not optimize what you cannot measure.
- If caching produces stale results (stable context has changed but cache has not been invalidated), invalidate and rebuild the cache. Document the staleness window.
