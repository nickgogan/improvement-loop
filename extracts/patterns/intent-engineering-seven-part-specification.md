---
title: "Intent Engineering Seven-Part Specification"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "intent-engineering-framework-seven-part-agent-inten"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An AI agent is being designed or configured for a task where instructions alone are insufficient — the agent will encounter situations not covered by explicit instructions and must make judgment calls. The operator can articulate the objective, desired outcomes, and constraints before deployment."
  invariants: "All seven components are specified before the agent is deployed. Health metrics steer behavior without hard-blocking — they are advisory, not enforcement gates. The distinction between steering constraints (prompt layer) and hard constraints (orchestration layer) is maintained architecturally, not just textually."
  governance: "Nick owns the intent specification for each agent. Autonomy scope (component 6) changes require a Design Decision. Stop rules (component 7) cannot be overridden by the agent — they are enforced at the orchestration layer."
  recovery: "If the agent encounters a situation not covered by any of the seven components, it must stop and escalate rather than improvise. If health metrics degrade beyond a defined threshold, the agent logs the degradation and alerts the operator but does not halt autonomously unless a stop rule is also triggered. If a stop rule fires, execution halts immediately and cannot resume without human authorization."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Intent Engineering Seven-Part Specification

**Source:** [[intent-engineering-framework-seven-part-agent-inten]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

AI agents receive task lists and prompts but lack encoded intent — the understanding of *why* a task matters and *how* to behave when instructions run out. Without intent, agents make arbitrary decisions in ambiguous situations, optimize for the wrong outcomes, and fail to stop when conditions change. "Context without intent is noise."

## Forces

- **Specificity vs. adaptability.** Over-specifying intent produces rigid agents that cannot handle novel situations. Under-specifying intent produces agents that improvise dangerously.
- **Steering vs. enforcement.** Some constraints should guide behavior (health metrics) while others must hard-block it (stop rules). Conflating the two produces either brittle agents (everything is hard-blocked) or unsafe agents (everything is advisory).
- **Autonomy vs. escalation.** Agents need clear boundaries on which decisions they may make independently and which require escalation. Without this, every ambiguous situation becomes either an autonomous guess or a bottleneck.
- **Measurability vs. completeness.** Desired outcomes and health metrics must be quantifiable to be enforceable, but not everything that matters is easily measured.
- **Prompt-layer vs. orchestration-layer enforcement.** Constraints expressed only in the prompt can be ignored or misinterpreted by the model. Constraints enforced at the orchestration layer are reliable but require engineering infrastructure.

## Solution

Encode agent intent using a seven-component specification framework. Every agent receives all seven components before deployment. The framework distinguishes between what the agent should *achieve*, what it should *protect*, and when it should *stop*.

**Seven Components:**

1. **Objective** — The problem the agent is solving and why it matters. Not a task list — a statement of purpose that guides behavior when specific instructions are absent.

2. **Desired Outcomes** (2-4 maximum) — Measurable results that define success. Keep the count low to prevent goal dilution. Each outcome should be independently verifiable.

3. **Health Metrics** — Qualities that must not degrade during execution. These steer behavior but do not hard-block: if a health metric degrades, the agent adjusts its approach but does not halt. Examples: response latency, data quality scores, user satisfaction proxies.

4. **Strategic Context** — The broader system the agent operates within. What other agents, processes, or humans depend on this agent's output? What upstream assumptions does the agent rely on? This prevents local optimization that harms the global system.

5. **Constraints** (two types):
   - *Steering constraints* (prompt layer): Preferences and guidelines that shape behavior. Expressed in the agent's prompt/instructions. The model may weigh these against other factors.
   - *Hard constraints* (orchestration layer): Absolute boundaries enforced by the runtime, not the model. File permission restrictions, API rate limits, approval gates. These cannot be overridden by the agent regardless of reasoning.

6. **Decision Types / Autonomy** — An explicit enumeration of which decisions the agent may make independently and which must be escalated to a human. This is the autonomy gradient — not a binary "autonomous or not" but a per-decision classification.

7. **Stop Rules** — Explicit conditions under which the agent must halt execution. Not "slow down" or "be careful" — full stop. Enforced at the orchestration layer, not the prompt layer. Examples: budget exceeded, error rate above threshold, human operator unreachable.

**The key design insight** is the distinction between health metrics (component 3) and hard constraints (component 5b). Health metrics are advisory signals that steer behavior. Hard constraints are enforcement mechanisms that block behavior. Conflating these two — treating everything as either advisory or mandatory — is the most common intent specification failure.

## Consequences

**Positive:**
- Agents behave predictably in novel situations because intent provides decision-making guidance beyond specific instructions.
- The health metrics vs. hard constraints distinction prevents both brittleness (over-blocking) and unsafety (under-blocking).
- Explicit autonomy scope (component 6) eliminates the ambiguity that causes agents to either over-escalate or under-escalate.
- Stop rules (component 7) provide a reliable last line of defense enforced outside the model's reasoning.
- The framework is agent-agnostic — it applies to any agent architecture, not just LLM-based agents.

**Negative:**
- All seven components must be specified upfront, which is a significant design effort per agent.
- Health metrics require quantification, which may not be straightforward for all quality dimensions.
- The two-type constraint distinction (steering vs. hard) requires architectural separation — prompt-layer constraints live in different infrastructure than orchestration-layer constraints.
- Autonomy scope creep: the decision type enumeration (component 6) must be actively maintained as the agent's responsibilities evolve.
- Stop rules that are too conservative halt the agent unnecessarily; stop rules that are too permissive fail to catch real problems.

## Known Uses

- **Product Compass framework** (Jan 2026): Original publication of the seven-part specification by Pawel Huryn, with production examples from agent deployments.
- **MetaSystem CLAUDE.md files:** Partially implement components 1 (objective via system identity), 5 (constraints via hard constraints section), and 7 (stop rules via human gate requirements). Components 2-4 and 6 are not yet formalized.
- **Multiple independent sources** converge on intent engineering as the 2026 breakthrough discipline in AI agent design.

## Contract

### Preconditions

- An AI agent is being designed or configured for a task where instructions alone are insufficient — the agent will face situations not covered by explicit instructions.
- The operator can articulate the objective, desired outcomes, and constraints before deployment.
- The runtime environment supports both prompt-layer configuration (for steering constraints) and orchestration-layer enforcement (for hard constraints and stop rules).

### Invariants

- All seven components are specified before the agent is deployed. Missing components are not acceptable — "not applicable" must be explicitly stated with justification.
- Health metrics steer behavior without hard-blocking — they are advisory, not enforcement gates.
- The distinction between steering constraints (prompt layer) and hard constraints (orchestration layer) is maintained architecturally, not just textually.
- Stop rules are enforced at the orchestration layer and cannot be overridden by the agent's reasoning.

### Governance

- Nick owns the intent specification for each agent.
- Autonomy scope (component 6) changes require a Design Decision or equivalent governance record.
- Stop rules (component 7) cannot be overridden by the agent — they are enforced outside the model's control.
- Health metric thresholds are reviewed periodically and updated based on operational data.

### Recovery

- If the agent encounters a situation not covered by any of the seven components, it must stop and escalate rather than improvise.
- If health metrics degrade beyond a defined threshold, the agent logs the degradation and alerts the operator but does not halt unless a stop rule is also triggered.
- If a stop rule fires, execution halts immediately and cannot resume without human authorization.
- If the intent specification is found to be incomplete or misaligned after deployment, pause the agent, update the specification, and redeploy — do not patch intent at runtime.
