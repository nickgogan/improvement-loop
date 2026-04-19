---
title: "Advisor-Executor API Pattern"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "advisor-executor-api-pattern"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An API-based application uses Anthropic models. Tasks involve a mix of routine execution steps and occasional hard reasoning decisions. Both a high-capability model (Opus) and a cost-efficient model (Sonnet/Haiku) are available."
  invariants: "The advisor never makes tool calls -- it provides reasoning guidance only. The executor retains full agency over tool use and code generation. Shared context is maintained between advisor and executor throughout the task."
  governance: "The max_uses parameter is set per task type based on measured decision complexity. Advisory consultation logs are retained for cost and quality analysis. Advisor-executor pairings are reviewed when benchmark results shift after model updates."
  recovery: "If the executor exhausts max_uses on a task, it completes remaining decisions independently and flags them for post-hoc review. If advisor context drifts from executor reality in long conversations, reset shared context at a defined checkpoint."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Advisor-Executor API Pattern

**Source:** [[advisor-executor-api-pattern]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Using a single model for all agent steps forces a choice between quality and cost. A high-capability model (Opus) produces excellent results but is expensive for routine steps. A cost-efficient model (Sonnet) handles most steps well but makes poor decisions at critical reasoning junctures. Neither single-model approach optimizes the quality-cost tradeoff.

## Forces

- **Quality vs. cost:** High-capability models are overkill for routine steps but critical for hard decisions. Using them everywhere is wasteful; excluding them entirely degrades output.
- **One-shot planning vs. dynamic consultation:** A plan-then-execute approach generates the plan upfront but cannot adapt when the executor encounters unexpected situations. Dynamic consultation adds latency but improves decision quality.
- **Shared context vs. independence:** The advisor needs full visibility into what the executor is doing, but maintaining synchronized context across two models adds complexity.
- **Consultation budget vs. decision quality:** Too few advisory calls mean the executor makes bad decisions alone; too many waste money on trivial questions.

## Solution

Pair a powerful reasoning model (advisor) with a cheaper execution model (executor) using Anthropic's Advisor Strategy API feature:

1. **Executor handles all tool calls and code generation.** It processes the task step by step, making autonomous decisions for routine operations.

2. **Advisor provides reasoning-only guidance on demand.** When the executor hits a decision point it cannot resolve confidently, it consults the advisor. The advisor has full shared context of the executor's progress but never makes tool calls itself.

3. **max_uses controls consultation budget.** This parameter caps the number of advisory consultations per task, preventing runaway costs while ensuring the advisor is available for genuinely hard decisions.

The relationship is dynamic, not one-shot: unlike plan-then-execute, the executor consults the advisor as situations arise throughout the task. The advisor sees the full conversation including tool results, so its guidance accounts for actual execution state rather than predicted state.

Set `type: 'advisor'` and `max_uses` in the API call. The advisor model is specified separately from the executor model.

## Consequences

**Positive:**
- Better quality at lower cost: SWE-Bench 74.8 (with advisor) vs 72.1 (Sonnet alone); cost $0.96 vs $1.89 per task
- Dynamic consultation adapts to task complexity -- simple tasks use few or no advisory calls; complex tasks use more
- Clean separation of concerns: reasoning and execution are distinct roles with distinct cost profiles
- Strictly dominates single-model Sonnet for API-based applications in benchmarks

**Negative:**
- max_uses requires tuning per task type -- too low and the executor makes avoidable mistakes; too high and costs increase without quality gains
- Advisor context may drift from executor reality in very long conversations
- Adds architectural complexity: two model configurations, shared context management, consultation logging
- Currently an Anthropic-specific API feature -- not portable across providers

## Known Uses

- Anthropic's Advisor Strategy API (production feature, April 2026)
- SWE-Bench and Terminal-Bench evaluations demonstrating quality and cost improvements
- API developers building web applications report it as a cost-quality "no-brainer"
- Conceptually related to Claude Code's plan mode, which uses a similar advisor-executor split but as a one-shot plan rather than dynamic consultation

## Contract

### Preconditions
An API-based application uses Anthropic models. Tasks involve a mix of routine execution steps and occasional hard reasoning decisions. Both a high-capability model (Opus) and a cost-efficient model (Sonnet/Haiku) are available via the API. A reasonable max_uses estimate exists for the task type.

### Invariants
The advisor never makes tool calls -- it provides reasoning guidance only. The executor retains full agency over tool use and code generation. Shared context is maintained between advisor and executor throughout the task. The max_uses cap is enforced per task invocation.

### Governance
The max_uses parameter is set per task type based on measured decision complexity, not guessed. Advisory consultation logs are retained for cost analysis and quality review. Advisor-executor model pairings are reviewed when benchmark results shift after model updates. Cost per task is monitored against the single-model baseline.

### Recovery
If the executor exhausts its max_uses allowance mid-task, it completes remaining decisions independently and flags those decisions for post-hoc human review. If advisor context drifts from executor reality in long conversations, reset shared context at a defined checkpoint. If cost exceeds the single-model baseline for a task type, reduce max_uses or reclassify the task as not needing advisory consultation.
