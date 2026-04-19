---
name: 'Think Tool: Dedicated Scratchpad for Mid-Chain Reasoning'
summary: A 'think' tool gives agents a structured scratchpad to reason about tool outputs mid-response without side effects, improving policy compliance and sequential decision accuracy. Distinct from extended
  thinking (pre-response planning) -- think tool processes new information discovered during execution.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
sources:
- anthropic-claude-think-tool.md
related_findings:
- file: thinking-models-mental-framework-commands-for-codi.md
  rel: same-problem
- file: chain-of-thought-reasoning-output-divergence.md
  rel: same-problem
- file: rationalization-prevention-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---
# Think Tool: Dedicated Scratchpad for Mid-Chain Reasoning

## What It Is

A tool with no side effects that gives agents a structured place to reason during multi-step tool chains. The tool definition is minimal: a single `thought` string parameter. The agent calls it between other tool calls to pause, assess what it has learned, check policy compliance, and plan next steps. Unlike extended thinking (which occurs before response generation for deep planning), the think tool activates mid-response to process new information from tool outputs.

Implementation is a standard tool spec with zero external behavior -- it simply appends the thought to the conversation log. The key differentiator is domain-specific prompting: instructing the agent when and how to use the tool with examples relevant to the task domain dramatically improves results.

Anthropic's tau-Bench results (Claude 3.7 Sonnet, airline domain): think tool + optimized prompt achieved 0.584 pass@1 vs 0.332 baseline (+76%). Think tool alone: 0.404. Extended thinking alone: 0.412. On the easier retail domain, think tool alone (no special prompt) achieved 0.812 vs 0.783 baseline. On SWE-Bench, the think tool contributed to a SOTA score of 0.623 with +1.6% improvement (Welch's t-test: t(38.89) = 6.71, p < .001, d = 1.47).

The improvements persist at pass^k (k=5), showing better handling of edge cases and more consistent performance, not just lucky runs.

## Why It Matters

Policy-heavy environments and long tool chains are exactly the scenarios where agents make the most errors -- they lose track of constraints, skip verification steps, and act on incomplete information. The think tool creates an explicit checkpoint pattern: before acting, reason about what you know, what the rules are, and what you still need. This is a zero-cost intervention (no external calls, no latency from real tools) that addresses the reliability problem at the reasoning layer.

The pattern also mitigates CoT/output divergence (existing finding): by forcing reasoning into a visible, structured tool call between actions, the agent's reasoning stays grounded in the specific tool outputs it just received rather than drifting from its chain of thought.

## Why People Are Using It

Anthropic uses it in production for Claude's tool-use scenarios. It contributed to SWE-Bench SOTA. The pattern generalizes to Claude 3.5 Sonnet New as well. Key insight from the post: "minimal downside -- no external behavior change unless used; no interference with other tools."

## Potential Improvements

Domain-specific think tool prompts could be templated per skill/workflow. The think tool description itself could be varied per domain (the SWE-Bench variant emphasizes "brainstorm several unique ways of fixing the bug" while the tau-Bench variant emphasizes policy checking). Could combine with the rationalization prevention pattern: include anti-rationalization triggers in think tool prompting.

## Potential Failure Modes

Without domain-specific prompting, the think tool provides modest gains (0.404 vs 0.332 on airline). Over-use could add latency to simple tasks. The tool is less valuable for non-sequential tool calls or simple instruction-following without complex constraints. Extended thinking has improved since initial release and may be preferred in most non-tool-chain scenarios.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[think-tool-scratchpad-for-mid-chain-reasoning.md]] in `extracts/patterns/`
