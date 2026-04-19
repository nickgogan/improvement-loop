---
name: Tool Injection via Type Annotations
summary: 'LangGraph tools declare what they need via type annotations: InjectedState for graph state access, InjectedStore for persistent store access, ToolRuntime for runtime context. The framework injects
  these at call time. This is declarative permission boundaries for tools — a tool can only access what it explicitly requests.'
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- General
adopted_in: []
sources: []
related_findings:
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: same-problem
- file: per-node-tool-restrictions-workflow-governance.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---

## What It Is

LangGraph provides a type-annotation-based dependency injection system for tools. Instead of tools having implicit access to everything, they declare exactly what they need via Python type annotations:

- **`InjectedState`** — access to the current graph state (e.g., conversation history, accumulated results)
- **`InjectedStore`** — access to persistent key-value/vector store (cross-thread memory)
- **`ToolRuntime`** — access to runtime context (configuration, user info)

Example:
```python
def search_tool(query: str, state: Annotated[dict, InjectedState]) -> str:
    # state is injected by the framework, not passed by the LLM
    ...
```

The framework strips injected parameters from the tool's schema before presenting it to the LLM (the LLM doesn't see or fill `state`), then injects the actual values at call time. This creates an opt-in permission model — tools get exactly what they declare, nothing more.

## Why It Matters

Tools are a major attack surface in agent systems. A tool with access to the full graph state can read sensitive data it doesn't need. A tool with store access can write to persistent memory. Most frameworks give tools implicit access to everything, relying on the tool author to self-restrict.

LangGraph's annotation-based injection flips this: tools are sandboxed by default and must explicitly request elevated access. This makes tool permissions visible in the code — a reviewer can see at a glance what a tool can access by reading its type signature.

The pattern is also useful for testing: injected dependencies can be mocked without modifying the tool code.

## Why People Are Using It

Observed in [LangGraph](https://github.com/langchain-ai/langgraph) v1.1.6 — see [[langgraph-analysis]] for structural details. The injection system is used in `ToolNode` (the standard tool executor) and `create_react_agent` (the pre-built ReAct agent). Production usage at Klarna, Replit, and Elastic.

## Potential Alternatives

Tool-level middleware that filters accessible state (runtime enforcement). Tool manifest files declaring permissions (static analysis). No tool sandboxing — trust tool authors (common but risky).

## Potential Improvements

Granular state access — instead of injecting the full state dict, inject specific state keys. Read-only vs. read-write annotations for store access. Audit logging for injected resource access.

## Potential Failure Modes

Tools requesting more access than needed (over-injection). Framework overhead from injection mechanism on hot paths. Python-specific pattern that doesn't translate to non-typed languages.
