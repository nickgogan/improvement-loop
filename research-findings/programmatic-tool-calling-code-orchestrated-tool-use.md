---
name: Programmatic Tool Calling -- Code-Orchestrated Tool Use
summary: 'Claude orchestrates multi-tool workflows via code execution (Python) rather than sequential inference passes. Tool results are processed in the code sandbox -- only the final output enters the
  model context. Reduces 200KB intermediate data to 1KB final output. Accuracy gains: internal retrieval 25.6% to 28.5%, GIA 46.5% to 51.2%.'
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-advanced-tool-use.md
related_findings:
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: extends
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
- file: mcp-as-code-api-progressive-tool-discovery.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is
A beta API feature where Claude writes Python code to orchestrate multi-tool workflows inside a sandboxed code execution environment. Tools are marked as callable from code via `allowed_callers: ["code_execution_20250825"]`. The API converts tool definitions to Python functions. Claude generates orchestration code, tool calls execute within the sandbox, and only the final `stdout` output enters the model context.

Key mechanics:
1. **Mark tools callable from code** -- set `allowed_callers` on opt-in tools alongside `code_execution` tool type
2. **Claude writes orchestration code** -- generates `server_tool_use` with Python code input
3. **Execution without context hit** -- tool calls from code include a `caller` field linking back to the code execution block; results stay in the sandbox
4. **Final output to context** -- only `code_execution_tool_result` with `stdout` enters the conversation

Example: "Which team members exceeded Q3 travel budget?" with 3 tools (get_team_members, get_expenses, get_budget_by_level) -- Claude writes a script that loops through members, fetches expenses, compares to budget, and outputs only the 2-3 violators. Raw data: 2,000+ line items (200KB). Context impact: 1KB.

## Why It Matters
Traditional tool calling requires full inference per invocation and dumps all intermediate results into context. For workflows involving 3+ dependent calls, large datasets, or filtering/aggregation, this creates: (1) token bloat from intermediates, (2) inference latency from sequential passes, (3) accuracy degradation from NLP-based result parsing. Code execution eliminates all three by moving orchestration logic out of inference.

## Why People Are Using It
Anthropic beta feature. Internal testing powered Claude for Excel (spreadsheets with thousands of rows without context overload). Measured accuracy improvements on internal benchmarks. Suits messy data, conditionals, parallel operations (e.g., 50 endpoints), and scale.

## Potential Improvements
Could be combined with Tool Search Tool for discovery + execution pipeline. Error handling patterns for code execution failures need documentation. The `allowed_callers` mechanism could extend to other execution environments beyond Python.

## Potential Failure Modes
Extra code generation step adds latency for simple single-tool calls. Claude needs to write correct orchestration code -- bugs in generated code fail silently within the sandbox. Not beneficial when Claude needs all intermediates for reasoning (e.g., decision-making that depends on individual data points rather than aggregates).

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[programmatic-tool-calling-code-orchestrated-tool-use.md]] in `extracts/patterns/`
