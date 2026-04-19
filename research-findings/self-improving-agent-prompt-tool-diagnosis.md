---
name: "Self-Improving Agent: Prompt and Tool Diagnosis"
summary: "Give the agent its own prompt and failure traces, ask it to diagnose and suggest improvements. Separately, a tool-testing agent uses flawed MCP tools, identifies failure modes, and rewrites tool descriptions. The tool-testing approach yielded 40% decrease in task completion time."
implementation_notes: "Directly applicable to MetaSystem's skill development workflow. After a skill fails, feed the failure trace back to Claude to diagnose the prompt/tool issue."
category: "Agent Design"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-multi-agent-research-system.md"
related_findings:
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
  - file: "eval-driven-development-autonomous-quality.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
---

## What It Is

Two complementary self-improvement patterns. (1) **Prompt self-diagnosis**: Give a Claude 4 model its own prompt plus failure traces and ask it to diagnose the issue and suggest improvements. The model identifies root causes like "the prompt doesn't tell me to stop searching after finding sufficient results" that humans miss. (2) **Tool-testing agent**: A dedicated agent uses a flawed MCP tool dozens of times, catalogs failure modes, and rewrites the tool description to prevent misuse. This approach yielded a 40% decrease in task completion time by eliminating tool-description-induced mistakes.

## Why It Matters

Prompt and tool description quality are the highest-ROI investments in agent systems, but diagnosing issues requires observing agent behavior at scale. Self-improvement closes this loop: the agent becomes both the user and the debugger of its own instructions. The tool-testing pattern is especially valuable because MCP tool descriptions are the primary interface between agents and tools -- a bad description causes systematic failures across every invocation.

## Why People Are Using It

Anthropic's production multi-agent research system. The 40% improvement from tool description optimization alone demonstrates that tool interface quality is often the bottleneck, not model capability.

## Potential Improvements

Automated regression testing of prompt/tool changes. A/B testing of alternative descriptions across agent populations. Confidence scoring for self-diagnosed improvements.

## Potential Failure Modes

Self-diagnosis may rationalize rather than truly diagnose (confirmation bias). Prompt changes that fix one failure mode may introduce others. Tool description rewrites may lose important constraints that prevent different failure modes.
