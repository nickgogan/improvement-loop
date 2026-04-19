---
title: "Reasoning-Blind Permission Classifier"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-auto-mode-ai-driven-permission-classif"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent system has a tool execution layer where actions can be intercepted before execution. A secondary model is available for classification. Actions are classifiable into risk tiers."
  invariants: "The classifier never has access to the primary agent's reasoning trace. Every action passes through at least one classification layer before execution. Denial escalation thresholds are enforced."
  governance: "Classifier policy rules are reviewed and updated as new action types are introduced. False-negative rates are tracked and reported. Escalation thresholds are tunable per deployment context."
  recovery: "If the classifier is unavailable, fall back to manual approval for all Tier 3 actions. If false-negative rate exceeds acceptable threshold, tighten Tier 2 boundaries to route more actions through the classifier."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Reasoning-Blind Permission Classifier

**Source:** [[claude-code-auto-mode-ai-driven-permission-classif]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agentic systems face a fundamental autonomy-safety tension. Manual approval of every action creates approval fatigue -- users rubber-stamp 93% of prompts without close attention, making the approval gate security theater. Skipping permissions entirely (`--dangerously-skip-permissions`) removes the safety net. Neither extreme is acceptable: one is slow and unreliable, the other is fast and dangerous.

## Forces

- **Approval fatigue degrades safety.** The more often users are asked to approve safe actions, the less attention they pay to any individual approval. High approval rates (93%) indicate the gate is mostly noise.
- **Agent persuasion risk.** If the safety classifier can see the agent's reasoning, the agent can construct arguments that manipulate the classifier into approving dangerous actions.
- **Latency cost of classification.** Every action that passes through a classifier adds inference latency. Classifying everything is expensive; classifying nothing is dangerous.
- **Heterogeneous risk profiles.** Some actions (reading a file in the project directory) are categorically safe. Others (executing shell commands, pushing to production) require genuine scrutiny. A uniform policy wastes resources or misses threats.

## Solution

**Implement a multi-tier permission system with a reasoning-blind AI classifier as the safety layer for high-risk actions.**

Three tiers of filtering, in order:

1. **Tier 1 -- Safe allowlist.** Non-modifying tools and user-configured safe actions auto-allowed with zero classifier overhead. File reads, project-scoped queries, and standard tool invocations pass through immediately.

2. **Tier 2 -- In-scope mutations.** File writes and edits within the project directory auto-allowed because they are reviewable via version control. No classifier latency cost for the most common write operations.

3. **Tier 3 -- Classifier gate.** Shell commands, web fetches, external tool invocations, subagent spawns, and out-of-scope filesystem operations pass through an AI classifier. The classifier uses a two-stage architecture:
   - **Stage 1:** Fast single-token filter (allow/flag). Most actions pass here.
   - **Stage 2:** Chain-of-thought reasoning only for flagged actions. Adds cost only when needed.

**The critical security property:** The classifier is reasoning-blind. It sees user messages and tool calls only -- never the primary agent's internal reasoning. This means the agent cannot construct persuasive arguments to bypass the classifier. The classifier evaluates what the agent is doing, not why the agent claims it should be allowed.

**Deny-and-Continue:** Blocked actions return as tool results with instructions to find safer paths, not to bypass. Backstop: escalate to human after 3 consecutive or 20 total denials.

**Multi-agent coverage:** The classifier runs at both ends of subagent delegation -- outbound (catching unintended delegations) and inbound (vetting results).

## Consequences

**Positive:**
- Eliminates approval fatigue by auto-allowing the 93% of actions that are genuinely safe.
- Prevents agent self-persuasion through the reasoning-blind design -- a novel security property not achievable with single-model self-review.
- Tiered filtering minimizes latency cost -- most actions never reach the classifier.
- Deny-and-Continue with escalation thresholds prevents both infinite loops and silent failures.

**Negative:**
- 17% false-negative rate on overeager actions (Anthropic-published). Some actions that should be flagged are not.
- Reasoning-blind design means the classifier cannot consider prior user approvals as context. One approval does not generalize to similar actions with larger blast radius.
- Requires a secondary model for classification, adding infrastructure and cost.
- Stage 2 CoT adds meaningful cost when triggered frequently on borderline actions.
- Tier definitions (what counts as "in-scope" vs. "external") require ongoing maintenance as the project and toolset evolve.

## Known Uses

- Anthropic's Claude Code Auto Mode (March 2026 Research Preview, rolling to Team/Enterprise/API plans).
- Three-tier classifier with Sonnet 4.6 as the classification model, serving Claude Code's production user base.
- 460 Reddit upvotes on day-of announcement, indicating strong demand for the middle path between full manual and full autonomous.

## Contract

### Preconditions
The agent system has a tool execution layer where actions can be intercepted before execution. A secondary model is available for classification (need not be the same model as the primary agent). Actions are classifiable into risk tiers based on observable properties (tool name, arguments, target paths) without requiring access to the agent's reasoning.

### Invariants
The classifier never has access to the primary agent's reasoning trace -- only user messages and tool calls. Every action passes through at least one classification layer (tier assignment) before execution. Denial escalation thresholds (consecutive and total) are enforced and not bypassable by the agent.

### Governance
Classifier policy rules (block rules, mandatory allow exceptions) are reviewed and updated as new action types and tools are introduced. False-negative rates are tracked and reported. Escalation thresholds are tunable per deployment context (interactive vs. headless). Tier boundary definitions are documented and versioned.

### Recovery
If the classifier model is unavailable, fall back to manual approval for all Tier 3 actions (never fail-open to auto-allow). If the measured false-negative rate exceeds the acceptable threshold, tighten Tier 2 boundaries to route more actions through the classifier until the rate is corrected. Log all classifier denials and escalations for post-hoc audit.
