---
title: "Single-Agent Default — Information Loss Exceeds Context Degradation"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "l-d-hypothesis-information-loss-across-agent-bound"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A pre-spawn checklist exists and is evaluated before any subagent invocation. The task's parallelizability, loss tolerance, and context-window requirements are assessed explicitly, not assumed."
  invariants: "Single-agent execution is the default for all tasks. Subagent spawning requires passing the pre-spawn checklist — no spawn without explicit justification. Sequential reasoning tasks are never split across agent boundaries."
  governance: "Owned by Meta-System knowledge layer. The pre-spawn checklist criteria require a Design Decision to modify. Adding new legitimate multi-agent domains requires empirical evidence, not theoretical argument."
  recovery: "If a multi-agent execution produces degraded results (error amplification, context loss), fall back to single-agent re-execution of the full task. If the pre-spawn checklist is bypassed, flag the invocation for post-hoc review."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Single-Agent Default — Information Loss Exceeds Context Degradation

**Source:** [[l-d-hypothesis-information-loss-across-agent-bound]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams default to multi-agent architectures because the industry narrative frames them as inherently superior — more agents implies more capability. In practice, splitting a task across agent boundaries introduces information loss (L) at every handoff: context that was available to agent A is summarized, truncated, or simply not communicated to agent B. This boundary loss typically exceeds the degradation (D) that a single agent experiences from longer context windows. The result is that multi-agent systems perform worse than single agents on sequential tasks, with empirical measurements showing 39-70% degradation and 17.2x error amplification for independent agents.

## Forces

- **Capability scaling vs. boundary cost.** Adding agents appears to add capability (more work in parallel), but each agent boundary introduces information loss that compounds across the pipeline. The net effect can be negative.
- **Context window limits vs. handoff fidelity.** Single agents hit context window ceilings on large tasks, seemingly justifying split-and-delegate. But the information lost across agent boundaries is harder to recover than the degradation from a long context — you cannot summarize what was never communicated.
- **Parallelism vs. sequential dependency.** Some tasks genuinely benefit from parallel execution (research across many sources). Others have step dependencies where each decision constrains the next. The same architectural pattern cannot serve both.
- **Industry hype vs. empirical evidence.** Multi-agent frameworks are heavily marketed. Empirical evidence (Google's 180-configuration study, production playbooks) consistently shows that orchestration overhead dominates for most task types.

## Solution

Default to **single-agent execution** for all tasks, and spawn subagents only when a task passes a pre-spawn checklist that validates the conditions under which L < D.

The pattern has three components:

1. **Single-agent default.** Every task begins as a single-agent execution. No multi-agent architecture is adopted "by default" or because it seems architecturally elegant. The burden of proof is on the multi-agent proposal.

2. **Pre-spawn checklist.** Before spawning any subagent, evaluate three criteria:
   - **Is the task parallelizable?** Can subtasks execute independently without sequential dependencies? If step B depends on the output of step A, splitting across agents loses the dependency context.
   - **Is the task loss-tolerant?** Can the overall result survive lossy handoffs between agents? Research (selecting from abundance) tolerates loss; implementation (where every decision constrains the next) does not.
   - **Is the task context-window-limited?** Does the single-agent approach actually hit context window constraints? If the task fits comfortably in one context, there is no D to avoid, making any L strictly worse.

3. **Capability saturation threshold.** Multi-agent coordination yields diminishing or negative returns once a single-agent baseline exceeds approximately 45% performance on the task. Below 45%, the task may be hard enough that parallel hypothesis-testing adds value. Above 45%, the single agent is already effective and coordination overhead dominates.

The pre-spawn checklist operationalizes the L > D hypothesis into a mechanical decision gate rather than leaving it to architectural intuition.

## Consequences

**Positive:**
- Eliminates the 39-70% degradation observed in sequential tasks split across agent boundaries.
- Reduces error amplification from 17.2x (independent agents) or 4.4x (centralized coordination) to baseline single-agent error rates.
- Simplifies system architecture — fewer moving parts, fewer failure modes, easier debugging.
- Context rot within a single agent (D) is addressable through state machines, contracts, and structured summarization. Information loss across boundaries (L) lacks equivalent mitigations.

**Negative:**
- Single agents hit context window ceilings on genuinely large tasks, requiring either checkpoint-and-resume or selective context loading rather than parallelization.
- Foregoes the genuine benefits of multi-agent execution for the four legitimate domains (research, debugging, mechanical operations, review).
- The pre-spawn checklist adds a decision step before every potential parallelization, which may feel like overhead for experienced practitioners.
- As context windows grow and inter-agent communication protocols improve, the L > D relationship may shift — the pattern needs periodic reassessment.

## Known Uses

- **Google empirical study (paper 2512.08296).** 180 configurations tested. Independent agents amplify errors 17.2x, centralized coordination 4.4x. Sequential task degradation 39-70%.
- **Nick Gupta's production playbook.** Independently confirms the L > D hypothesis: context rot within single agents is addressable through structured mitigations, but information loss across agent boundaries lacks equivalent solutions.
- **MetaSystem's own architecture.** Build spec execution (sequential, context-dependent) runs single-agent. Research-loop extraction (parallel source processing) uses subagents — consistent with the legitimate-domain taxonomy.
- **"Agent Orchestrators Are Bad" synthesis.** Combines Google research with production experience to identify the four task types where L < D (research, debugging, mechanical operations, review).

## Contract

### Preconditions

- A pre-spawn checklist exists and is documented in the system's agent governance.
- The checklist's three criteria (parallelizability, loss tolerance, context-window limitation) are evaluated explicitly before any subagent invocation.
- The capability saturation threshold (~45%) is calibrated for the system's task domain.

### Invariants

- Single-agent execution is the default for all tasks. No exceptions without passing the pre-spawn checklist.
- Sequential reasoning tasks (implementation, planning, integration) are never split across agent boundaries.
- Subagent spawning requires explicit justification recorded in the task's execution log.

### Governance

- Owned by Meta-System knowledge layer.
- The pre-spawn checklist criteria require a Design Decision to modify.
- Adding new legitimate multi-agent domains requires empirical evidence (production measurements, not theoretical arguments).
- The capability saturation threshold is reviewed annually or when foundational model capabilities change significantly.

### Recovery

- If a multi-agent execution produces degraded results (error amplification, lost context, inconsistent outputs), fall back to single-agent re-execution of the full task.
- If the pre-spawn checklist is bypassed (emergency or oversight), flag the invocation for post-hoc review and document the outcome.
- If the L > D relationship inverts for a task type due to improved inter-agent protocols, update the checklist criteria via Design Decision rather than ad-hoc exception.
