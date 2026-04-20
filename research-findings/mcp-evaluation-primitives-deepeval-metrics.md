---
name: MCP Evaluation Primitives (DeepEval Metrics)
summary: 'DeepEval provides three purpose-built metrics for evaluating MCP-based agents: MCPUseMetric (single-turn primitive usage and argument correctness), MultiTurnMCPUseMetric (multi-turn MCP interactions),
  and MCPTaskCompletionMetric (end-to-end task achievement through MCP). Test cases capture runtime tool/resource/prompt calls with MCPServer definitions. LLM-as-judge scores alignment between primitives
  used and primitives available.'
implementation_notes: Directly applicable if MetaSystem moves to automated MCP evaluation. Current MCP usage is human-gated. These metrics would enable automated regression testing of MCP tool selection
  accuracy. The MCPServer + MCPToolCall test case structure provides a concrete schema for capturing MCP interaction traces.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- deepeval-mcp-evaluation-quickstart.md
related_findings:
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: enables
- file: three-tier-grading-hierarchy.md
  rel: same-problem
- file: mcp-ecosystem-critical-mass-97m-installs.md
  rel: extends
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

# MCP Evaluation Primitives (DeepEval Metrics)

## What It Is

DeepEval's MCP evaluation framework provides three metrics for testing MCP-based agent applications:

**MCPUseMetric (Single-Turn):** Evaluates how well an MCP-based agent uses available MCP primitives (tools, resources, prompts) in a single interaction. Scores on two dimensions: (1) primitive selection -- did the agent call the right tools/resources/prompts given the task? (2) argument correctness -- were the inputs to those primitives correct and accurate?

**MultiTurnMCPUseMetric:** Same evaluation dimensions as MCPUseMetric but across a multi-turn conversation. Accounts for cumulative tool usage and evolving context across turns. Score = AlignmentScore(Primitives Used, Primitives Available) / Total MCP Interactions.

**MCPTaskCompletionMetric:** End-to-end evaluation of whether the agent accomplished its task through MCP interactions. Evaluates both whether the goal was achieved and whether the plan (sequence of MCP calls) was sound.

**Test case structure:**
- Define `MCPServer` objects with available tools, resources, and prompts
- Capture runtime calls as `MCPToolCall`, `MCPResourceCall`, `MCPPromptCall` objects
- Create `LLMTestCase` (single-turn) or `ConversationalTestCase` (multi-turn) with MCP parameters
- Run metrics via `evaluate()` function

All three metrics use LLM-as-judge with configurable threshold, strict mode, and reasoning output.

## Why It Matters

MCP is becoming the standard protocol for agent-tool interaction, but there has been no standardized way to evaluate whether agents use MCP primitives correctly. These metrics provide the first structured evaluation framework for MCP interactions, enabling regression testing of tool selection accuracy and argument correctness.

## Why People Are Using It

DeepEval is a widely-used open-source LLM evaluation framework. The MCP metrics were added in response to the explosion of MCP-based agent applications. The framework supports multiple judge models (GPT, Claude, Gemini, Ollama) and integrates with the Confident AI platform for test reports.

## Potential Improvements

Deterministic tool selection validation (for cases where the correct tool is known a priori, no LLM judge needed). Latency-aware evaluation (penalizing unnecessary tool calls that slow down the workflow). Cost-aware evaluation (penalizing expensive tool calls when cheaper alternatives exist).

## Potential Failure Modes

LLM-as-judge may not correctly evaluate domain-specific tool selection decisions. Threshold calibration is critical -- too low allows poor tool usage to pass, too high creates false failures. Multi-turn evaluation can be noisy if conversation structure varies significantly across test runs.
