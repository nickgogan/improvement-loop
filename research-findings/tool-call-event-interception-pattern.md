---
name: "Tool Call Event Interception Pattern"
summary: "Extensions can subscribe to a 'tool_call' event fired before tool execution. Handlers can block the call (with a reason) or mutate the arguments in-place. Later handlers see earlier mutations. No re-validation after mutation. Enables policy enforcement, argument transformation, and conditional blocking without modifying the tool itself."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "ide-first-claude-code-with-deterministic-hooks.md"
    rel: "same-problem"
  - file: "ralph-loop-brute-force-security-and-ui-testing.md"
    rel: "enables"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "synthesized"
consumed_by:
  - "designing-agent-tools.md"
  - "rules/hook-based-enforcement-for-agent-outputs.md"
---

# Tool Call Event Interception Pattern

## Pattern

A tool execution pipeline with an interception point:
1. LLM emits tool call with arguments
2. `tool_call` event fires with mutable `event.input`
3. Extensions can: (a) return `{ block: true, reason: "..." }` to prevent execution, or (b) mutate `event.input` in-place to transform arguments
4. Later handlers in the chain see earlier mutations
5. No schema re-validation after mutation
6. Tool executes with final (possibly modified) arguments
7. `tool_result` event fires after execution (can modify result content)

## Why It Matters

This is a more powerful version of Claude Code's hooks (which use exit codes for block/allow). Key advantages:
- **Typed**: handlers know the tool name and can narrow to specific tool types
- **Composable**: multiple extensions chain without knowing about each other
- **Bidirectional**: intercept both before (tool_call) and after (tool_result)
- **Granular**: per-tool-call blocking, not per-tool-type

Enables: safety policies (block dangerous bash commands), argument normalization (fix paths), audit logging (record all tool calls), and A/B testing (modify tool behavior without changing tool code).

## How It Could Fail

- No re-validation means extensions can produce invalid arguments
- Mutation ordering is extension-load-order-dependent
- Silent argument corruption if extensions don't coordinate
- Performance impact of long handler chains

## Evidence

Pi agent harness (earendil-works/pi) — `ToolCallEvent` type with typed variants per built-in tool, `ToolCallEventResult` with `block`/`reason` fields. Type guard `isToolCallEventType()` for safe narrowing.
