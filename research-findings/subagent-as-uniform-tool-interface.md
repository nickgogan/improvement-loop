---
name: "Subagent-as-Uniform-Tool-Interface (Composition Principle)"
summary: "Sub-agent dispatch is implemented as a standard tool in the tool registry ('agent tool'), called identically to bash, file-read, or web-search. The orchestrator does not have special-case logic for delegation — spawning a sub-agent follows the same call/result/checkpoint path as any other tool. This interface homogeneity simplifies composition: hooks, logging, and permission checks work on sub-agent calls without modification."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "claude-code-architecture-under-the-hood.md"
related_findings:
  - file: "brain-hands-decoupling-architecture.md"
    rel: "extends"
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "same-problem"
  - file: "claude-code-12-agent-primitives.md"
    rel: "extends"
  - file: "tool-gateway-security-boundary.md"
    rel: "enables"
  - file: "acp-spawn-cross-tool-delegation.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
  - "rules/sub-agent-dispatch-as-uniform-tool-entry.md"
tags:
  - "session-95-reextract"
---

# Subagent-as-Uniform-Tool-Interface (Composition Principle)

## What It Is

A design principle where sub-agent dispatch is implemented as a regular tool entry in the tool registry, not as a special orchestration mechanism. In Claude Code's architecture, the "agent tool" sits alongside bash, file-read, grep, and web-search in the same registry. The orchestrator (main agent loop) calls it through the identical path:

1. Model decides to use `agent_tool` with input parameters
2. Pre-tool hook fires (can inspect, modify, or block)
3. Sub-agent spawns and runs its own loop
4. Result returns as a string (same as any tool output)
5. Post-tool hook fires (can inspect or transform result)
6. Result enters the orchestrator's context

The critical design choice: **no special-case code for delegation**. The orchestrator does not distinguish between "run a bash command" and "spawn a sub-agent to handle code review." Both are tool calls. Both pass through hooks. Both return strings.

## Why It Matters

Interface homogeneity has three composition benefits:

1. **Hooks work for free** — Safety checks, logging, and permission gates that apply to tool calls automatically apply to sub-agent dispatch. No separate "agent permission" system needed.

2. **Tool registry is the single source of capabilities** — The orchestrator's available actions are enumerated in one place. Adding a new sub-agent type means adding a tool entry, not modifying orchestration logic.

3. **Testability** — Sub-agent dispatch can be mocked the same way as any tool call. Integration tests don't need special harness for multi-agent scenarios.

This contrasts with frameworks where sub-agent dispatch is a first-class orchestration concept with its own API surface, lifecycle management, and error handling — adding complexity that the uniform interface avoids.

## Why People Are Using It

The Claude Code architecture analysis describes this as "elegant" — the system "stays consistent all the way through" because the orchestrator calls the agent tool "exactly the same way it calls the bash tool or the file reader." The 24-hour clean room rewrite (TS → Python → Rust) was feasible partly because the uniform interface meant fewer special cases to reimplement.

This pattern also appears in the brain-hands decoupling finding (Anthropic managed agents), where the uniform `execute(name, input) -> string` interface abstracts all tool types including sandbox execution. The consistent design across Claude Code (CLI agent) and managed agents (platform) suggests this is a deliberate Anthropic architectural principle, not an accident.

## Potential Improvements

- Extend the uniform interface to include structured output types (not just strings) for sub-agent results, enabling typed composition without losing interface homogeneity.
- Add a "delegation depth" metadata field to the tool call so hooks can apply different policies to direct tool calls vs. sub-agent dispatches when needed — without breaking the uniform interface.

## Potential Failure Modes

- **Leaky abstraction** — Sub-agents have fundamentally different resource profiles (longer running, higher cost, own context window) than simple tools. Treating them identically may hide resource management concerns that need explicit handling.
- **Error semantics mismatch** — A bash command failing returns an error string. A sub-agent failing might mean partial work was done, state was modified, or resources were consumed. The uniform string return masks these differences.
- **Recursive spawning** — If sub-agents can call the agent tool themselves, unbounded recursion is possible. The uniform interface doesn't inherently prevent this — depth limits must be imposed externally.
