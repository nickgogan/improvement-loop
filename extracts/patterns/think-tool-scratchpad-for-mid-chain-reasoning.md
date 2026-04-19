---
title: "Think Tool Scratchpad for Mid-Chain Reasoning"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "think-tool-scratchpad-for-mid-chain-reasoning"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent operates in a multi-step tool-calling workflow where intermediate results require interpretation before the next action. The tool-calling framework supports no-op tools (tools with no side effects). Domain-specific policy constraints or sequential decision rules exist that the agent must check mid-chain."
  invariants: "The think tool has zero side effects -- it never modifies external state, calls APIs, or writes files. Think tool invocations are logged in the conversation trace for auditability. The think tool does not replace extended thinking (pre-response planning) -- it supplements it for mid-execution reasoning."
  governance: "Owned by Meta-System knowledge layer. Think tool prompt templates are domain-specific and reviewed when new skill domains are added. Modifications require a Design Decision."
  recovery: "If the think tool is overused (adding latency to simple tasks), reduce or remove domain-specific prompting that triggers it. If reasoning quality degrades without the think tool, re-enable it with more targeted prompting. If the think tool produces visible output to users, fix the tool definition -- it must remain internal-only."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Think Tool Scratchpad for Mid-Chain Reasoning

**Source:** [[think-tool-scratchpad-for-mid-chain-reasoning]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agents executing multi-step tool chains lose track of constraints, skip verification steps, and act on incomplete information as the chain lengthens. The agent's reasoning drifts from its chain of thought because there is no structured place to pause and reassess between tool calls. Policy-heavy environments are especially vulnerable: the agent forgets rules discovered early in the chain by the time it reaches later actions. This produces compliance failures, incorrect sequential decisions, and inconsistent behavior across runs.

## Forces

- **Speed vs. deliberation.** Adding reasoning checkpoints between tool calls increases latency, but skipping them causes errors that require more expensive rework.
- **Structured reasoning vs. natural flow.** Forcing reasoning into a tool call creates an explicit checkpoint, but over-structured reasoning can feel artificial and add overhead to simple tasks.
- **Pre-response planning vs. mid-execution reasoning.** Extended thinking (pre-response) handles deep upfront planning well, but cannot process new information discovered during tool execution. The two complement each other but serve different cognitive moments.
- **Generic vs. domain-specific prompting.** A generic think tool provides modest gains; domain-specific prompting for when and how to use it dramatically improves results but requires per-domain maintenance.

## Solution

Add a **think tool** -- a zero-side-effect tool with a single `thought` string parameter -- to the agent's tool set. The agent calls it between other tool calls to pause, assess what it has learned from previous tool outputs, check policy compliance, and plan next steps.

The pattern has three components:

1. **Minimal tool definition.** The tool takes one parameter (`thought`: string) and does nothing except append the thought to the conversation log. No external calls, no state changes, no latency from real tools. Implementation is trivial in any tool-calling framework.

2. **Domain-specific prompting.** The tool description and system prompt instruct the agent when and how to use the think tool with examples relevant to the task domain. For code debugging: "brainstorm several unique ways of fixing the bug before choosing one." For policy compliance: "before taking any action, use the think tool to verify the request against the policy rules." The prompting is the high-leverage component -- the tool definition alone provides modest gains.

3. **Checkpoint placement.** The think tool is most valuable at specific decision points: after receiving tool output that requires interpretation, before taking a mutating action, when multiple valid paths exist, and when policy rules constrain the action space. Over-use on simple tasks adds unnecessary latency.

## Consequences

**Positive:**
- Significant accuracy improvements in policy-heavy domains: +76% pass@1 on Anthropic's tau-Bench airline domain (think tool + optimized prompt: 0.584 vs. 0.332 baseline).
- Zero-cost intervention when not invoked -- no interference with other tools, no external behavior change.
- Mitigates chain-of-thought/output divergence by grounding reasoning in specific tool outputs received mid-execution.
- Improvements persist at pass^k (k=5), indicating better edge-case handling and more consistent performance rather than lucky runs.
- Contributed to SWE-Bench SOTA (0.623) with statistically significant improvement (p < .001, d = 1.47).

**Negative:**
- Without domain-specific prompting, gains are modest (0.404 vs. 0.332 on airline -- a 22% improvement rather than 76%).
- Adds latency to simple tasks where deliberation is unnecessary.
- Domain-specific prompt templates require maintenance as task domains evolve.
- Less valuable for non-sequential tool calls or simple instruction-following without complex constraints.
- Extended thinking capabilities continue to improve and may subsume some think-tool use cases for non-tool-chain scenarios.

## Known Uses

- **Anthropic production tool-use system.** Used across Claude's tool-calling scenarios. The think tool contributed to SWE-Bench SOTA (0.623, Claude 3.5 Sonnet).
- **Anthropic tau-Bench evaluation.** Tested on airline and retail customer service domains. Airline domain showed the largest gains due to complex policy rules; retail domain showed more modest improvement (0.812 vs. 0.783 baseline) due to simpler constraints.
- **Claude 3.5 Sonnet and 3.7 Sonnet.** Pattern generalizes across model versions, confirming it is a workflow-level intervention rather than model-specific.

## Contract

### Preconditions

- Agent operates in a multi-step tool-calling workflow where intermediate results require interpretation before the next action.
- The tool-calling framework supports no-op tools (tools with no side effects that still appear in the conversation log).
- Domain-specific policy constraints or sequential decision rules exist that the agent must check mid-chain.

### Invariants

- The think tool has zero side effects -- it never modifies external state, calls APIs, or writes files.
- Think tool invocations are logged in the conversation trace for auditability.
- The think tool does not replace extended thinking (pre-response planning) -- it supplements it for mid-execution reasoning about new information.

### Governance

- Owned by Meta-System knowledge layer.
- Think tool prompt templates are domain-specific and reviewed when new skill domains are added.
- Modifications to the pattern require a Design Decision.

### Recovery

- If the think tool is overused and adds unacceptable latency to simple tasks, reduce or remove domain-specific prompting that triggers frequent invocation.
- If reasoning quality degrades after removing the think tool, re-enable it with more targeted prompting focused on high-stakes decision points.
- If the think tool produces visible output to users (violating the zero-side-effect invariant), fix the tool definition -- it must remain conversation-internal only.
