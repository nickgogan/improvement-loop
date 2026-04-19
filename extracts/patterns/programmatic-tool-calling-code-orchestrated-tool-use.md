---
title: "Code-Orchestrated Tool Execution"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "programmatic-tool-calling-code-orchestrated-tool-use"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Multi-tool workflow involves 3+ dependent calls, large intermediate datasets, or filtering/aggregation steps. A sandboxed code execution environment is available."
  invariants: "Only final computed output enters the model context. Intermediate tool results remain within the execution sandbox. Each tool opted in via explicit allowed_callers declaration."
  governance: "Decision to route a workflow through code orchestration vs. sequential inference is recorded as a design rationale. Tools opted into code-calling require review of their failure modes in sandbox context."
  recovery: "If code execution fails, fall back to sequential inference-based tool calling. Log the failure and the generated code for debugging. Do not silently swallow sandbox errors."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Code-Orchestrated Tool Execution

**Source:** [[programmatic-tool-calling-code-orchestrated-tool-use]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Multi-tool agent workflows that require sequential tool calls dump all intermediate results into the model context. When a workflow involves iterating over datasets, filtering results, or aggregating across multiple tool outputs, the intermediate data bloats context (e.g., 200KB of raw records), degrades accuracy through NLP-based parsing of structured data, and adds latency from one full inference pass per tool invocation.

## Forces

- **Context budget vs. data volume.** Large intermediate datasets consume context window that should be reserved for reasoning. But the model needs to orchestrate the workflow.
- **Accuracy vs. inference-based parsing.** Models parsing JSON/tabular data through natural language lose precision. But code execution adds a code-generation step that itself can fail.
- **Latency vs. sequential reasoning.** Each inference pass for tool calling adds latency. But parallel execution requires the model to plan the full workflow upfront.
- **Transparency vs. efficiency.** Keeping all intermediates in context lets the model reason about them. But most workflows only need the final aggregate, not every raw record.

## Solution

Move multi-tool orchestration from inference-time sequential calling to code-time batch execution:

1. **Opt-in tool marking.** Tag tools that can be called from code with an explicit declaration (e.g., `allowed_callers`). Not all tools should be code-callable -- tools requiring per-call reasoning stay inference-bound.
2. **Code generation step.** The model writes orchestration code (Python) that calls multiple tools, processes intermediate results, applies filtering/aggregation, and emits only the final output to stdout.
3. **Sandbox execution.** The generated code runs in a sandboxed environment. Tool calls from within the code execute normally but their results stay in the sandbox scope, never entering the model context.
4. **Context-minimal output.** Only the final stdout from the code execution enters the conversation context. A 200KB intermediate dataset becomes a 1KB summary.

Apply this pattern when:
- The workflow involves 3+ dependent tool calls.
- Intermediate data is large (100+ records, multi-KB payloads).
- The final output is a filtered, aggregated, or computed subset of the intermediates.
- The model does not need to reason about individual intermediate data points.

Do NOT apply when:
- The model needs all intermediates for decision-making (e.g., comparing individual options).
- The workflow is simple (1-2 tool calls with small payloads).
- Code generation reliability is lower than sequential calling reliability for the specific workflow.

## Consequences

**Positive:**
- Dramatic context savings (200KB to 1KB in documented cases).
- Accuracy improvements from code-based data processing vs. NLP parsing (25.6% to 28.5% on internal retrieval, 46.5% to 51.2% on GIA benchmarks).
- Latency reduction from parallel tool execution within a single code block vs. sequential inference passes.
- Enables workflows at scale (50+ endpoints, thousands of records) that would exceed context limits under sequential calling.

**Negative:**
- Adds a code generation step that itself can contain bugs. Generated code failures are harder to debug than sequential tool-calling failures.
- Not beneficial for simple workflows -- the code generation overhead exceeds the savings.
- The model loses visibility into intermediates, which matters when individual data points drive decisions.
- Requires sandbox infrastructure and tool-level opt-in configuration.

## Known Uses

- Anthropic's beta API feature for programmatic tool calling.
- Claude for Excel -- processes spreadsheets with thousands of rows without context overload.
- Internal Anthropic benchmarks demonstrating accuracy and efficiency improvements.

## Contract

### Preconditions
The workflow involves 3+ dependent tool calls, produces large intermediate datasets, or requires filtering/aggregation. A sandboxed code execution environment is available. Tools intended for code-calling are explicitly opted in via `allowed_callers` or equivalent declaration.

### Invariants
Only final computed output enters the model context. Intermediate tool results remain within the execution sandbox and are never surfaced to the conversation. Each tool callable from code has an explicit opt-in declaration -- no implicit code-calling of arbitrary tools.

### Governance
The decision to route a workflow through code orchestration vs. sequential inference must be recorded as a design rationale. Tools opted into code-calling require review of their failure modes in a sandbox context (e.g., can they fail silently? do they produce side effects?).

### Recovery
If code execution fails (syntax error, runtime exception, tool error within sandbox), fall back to sequential inference-based tool calling for the same workflow. Log the failure, the generated code, and the error for post-hoc debugging. Do not silently swallow sandbox errors or return empty results as if the workflow succeeded.
