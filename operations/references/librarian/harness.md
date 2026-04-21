---
term: harness
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "harness"
  - "cross-cutting"
aliases:
  - "Harness"
  - "Agent harness"
  - "Runtime harness"
---

# Harness

## Short definition

The **harness** is the runtime + tooling surface an agent operates *inside*: the CLI/IDE/API that loads the agent's prompt, enforces its permissions, invokes its tools, manages its context window, and executes its hooks. The agent is *in* the harness; the harness is not *in* the agent.

Examples: Claude Code (CLI + IDE + hooks + MCP loader), Cursor (IDE + chat harness + model router), GitHub Copilot (editor harness + completion surface), the Anthropic API (stateless harness — provides tool-use, caching, thinking, batch, but no session state).

## Not to be confused with

| Not harness | What it is instead |
|---|---|
| **Prompt / agent spec** | Authored content the harness loads. The harness enforces; the prompt instructs. See `agent.md` (concept, planned) for the agent-spec term. |
| **Model** | The underlying LLM. A harness invokes a model; a model does not imply a harness. See Dimension 2 (research registry). |
| **Skill / workflow / pipeline** | Procedural composition on top of the harness. A skill is content the harness runs; it is not the harness itself. |
| **Agentic system** | A system-level assembly of multiple agents (see `agentic-systems.md`, planned). A harness is the runtime underneath; agentic systems are topologies on top. |
| **Second brain** | The knowledge surface an agent reads *through* the harness. See `second-brain.md`. |

## Why this is a concept, not a dimension

The Researcher scans for aspects of the world (Context, Tools, Prompt, Orchestration, …). The harness is a *consumer lens* that cross-cuts those aspects — any real question about a harness touches tool loading, context caching, prompt composition, permissions, and session mechanics simultaneously. Scan-topic framing would force the Researcher to invent a "Harness" partition that overlaps every other dimension. Consumer-query framing is the right place for it: this concept file points into the aspects that already exist.

## Composition

Where in the KB to look when a consumer asks about the harness. Pointers are to guide sections (Tier 1), patterns and findings (Tier 2), and watched-library repos (Tier 3).

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings, on escalation) | Tier 3 (watched-libraries, on explicit ask) |
|---|---|---|---|
| Tool registry, deferred tool loading, progressive discovery | G5 `designing-agent-tools.md` §"Step N — Tool Registry" and §"Deferred Loading" | Patterns under Tools dimension; findings on Tool Search, MCP server ecosystems | `anthropic-claude-code/` repo §tool/hooks source; MCP server registry implementations |
| Context loading, caching, budget management | G2 `managing-agent-context.md` §"Step — Budget", §"Caching", §"Hidden Context" | Patterns `context-rot-attention-budget-depletion`, `ace-delta-updates`; any finding tagged `prompt-caching` | Claude Code caching implementation; Cursor context-composer source |
| Prompt composition — what the harness prepends, appends, wraps | G8 `model-resilient-prompt-engineering.md` §"Role/Authority/Constraint/Failure Signal" | Patterns on prompt layering, negative constraints | Claude Code system-prompt assembly; Anthropic SDK cookbook prompt-caching examples |
| Hooks, events, session mechanics, checkpoints | G3b `agent-workflow-and-execution.md` §"State", §"Termination"; G7 `session-persistence-and-memory.md` §"Handoff", §"Crash Recovery" | Patterns on durable workflow state, session handoff; `gsd-global-learnings-store-cross-session-persistence` | Claude Code hook source; Temporal/Prefect repos for workflow-engine comparison |
| Permissions, sandboxing, blast radius | G6 `agent-safety-and-permissions.md` §Contract (invariants on tiered permissions, structural enforcement) | Patterns on defense-in-depth, prompt-injection mitigation; findings on container sandboxes | Claude Code settings.json permission model; E2B / Daytona sandbox implementations |
| Observability, traces, cost monitoring | G4 `building-agent-evaluation-suites.md` §Eval harness instrumentation; G2 `managing-agent-context.md` §"Measurement" | Patterns on compounding-reliability, multi-step failure attribution | Claude Code tracing output; OpenTelemetry LLM conventions in tracked repos |

### Cross-guide threads for harness-level queries

When a query is about the harness *as a whole* (e.g., "what should I demand of a production harness?"), the composition stitches together:

1. **Permissions posture** — G6 invariants (tiered, structurally enforced, agent cannot self-modify).
2. **Context mechanics** — G2 invariants (justified elements, caching, hidden context accounted for).
3. **Tool loading discipline** — G5 invariants (only task-relevant tools, intermediate results kept out of context).
4. **Workflow mechanics** — G3b invariants (termination conditions, state tracking, cost controls).
5. **Prompt composition** — G8 invariants (ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL, versioning).
6. **Observability** — G4 invariants (independent eval; harness must expose enough signal to verify).

This list is the default aspect-sweep for harness questions that don't name an aspect.

## Librarian read rule

**Default (Tier 1):** Start with the composition table above. If the consumer's query names one aspect (e.g., "how does the harness handle context caching?"), read only the relevant row's Tier-1 pointers. If the query is aspect-unspecified (e.g., "audit this harness"), read the cross-guide thread above in order.

**Escalate to Tier 2 when:**
- Consumer asks for rationale behind a Tier-1 claim ("why does G2 say intermediate results should stay out of context?").
- Consumer asks about a design debate or contradicting findings (surface `contradicts` typed links).
- Tier-1 confidence is low because the aspect is sparsely covered in the named guide.

**Escalate to Tier 3 when:**
- Consumer explicitly asks for a reference-implementation comparison ("how does Claude Code actually do this?").
- Consumer is auditing *their own* harness design against a canonical example and wants the canonical in view.
- A Tier-1 or Tier-2 answer names a specific mechanism (hook API, permission config format) and the consumer needs the exact shape.

**Do not:**
- Read the full Claude Code source to answer a definitional question ("what is a harness?"). Definition + disambiguation above suffices.
- Cite a Tier-2 pattern file as if it were a Tier-1 guide. Attribute tier explicitly in the response.
- Default to Tier 3 for any harness question — watched-library reads are high-cost and should be gated on clear need.

## Provenance surfacing

Every claim cites its substrate tier: `G<N>.md#<anchor>` for Tier 1 (anchor IDs stabilize post the collapse-proposal section manifest; until then, section-heading references are acceptable), `finding-id` or `pattern-slug` for Tier 2, `watched-lib/path:line-range` for Tier 3.

## Cross-references

- Substrate audit §"The Librarian Reference Layer": `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- `_index.md` in this directory.
- Related concepts (planned): `agent.md`, `mcp.md`, `context-rot.md`.
- Related operation: `audit.md` — composition of harness audit pulls this file's cross-guide thread.
