---
term: agent
type: concept
variants:
  - prompt-based
  - harness-based
  - autonomous-vs-supervised
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "agent"
  - "variant-carrier"
aliases:
  - "Agent"
  - "AI agent"
  - "agent.md"
---

# Agent

## Short definition

An **agent** is a model-plus-context assembly authored to perform a bounded class of tasks under a stated intent, within a harness. Its authored surface is typically a specification file (`agent.md`, `CLAUDE.md`, a system prompt) that encodes identity, intent, constraints, tools, and recovery behavior.

Three distinct referents appear in our problem space. Variant selection should happen before composition; the three variants compose different guide sets.

## Not to be confused with

| Not agent | What it is instead |
|---|---|
| **Prompt** | The instruction content an agent executes. An agent has a prompt; a prompt alone is not an agent. See `prompt.md` (this directory). |
| **Skill** | A procedural packaging of a bounded operation. An agent may invoke skills; a skill is not an agent. See `skill.md` (this directory). |
| **Harness** | The runtime substrate the agent runs inside — Claude Code, Cursor, a SaaS wrapper, the Anthropic API. An agent has a harness; the harness is not the agent. See `harness.md`. |
| **Agentic system** | A topology of multiple agents + shared state. An agent is a unit; an agentic system is a composition. See `agentic-systems.md` (planned). |

## Variant selection

Quick heuristics. Pick a variant from the consumer's phrasing; ask one disambiguating question if ambiguous.

| Consumer says… | Variant | Why |
|---|---|---|
| "my `agent.md`," "the instructions I wrote for my agent," "my system prompt for the agent" | **prompt-based** | The agent's behavior is carried by an authored spec the harness loads. |
| "my custom Claude Code agent," "my Cursor agent with these hooks," "my MCP-tool-enabled agent" | **harness-based** | The agent's behavior is meaningfully carried by harness configuration (tools, hooks, permissions), not only its prompt. |
| "my background agent," "my long-running agent," "my agent that does things without me watching" | **autonomous-vs-supervised** | The agent's autonomy envelope matters — HITL gating, escalation paths, trust promotion become load-bearing. |

An agent can fit more than one variant simultaneously (an autonomous Claude Code agent is both harness-based and autonomous). When variants overlap, the audit/design composition pulls the union of their guide sets.

## Variants (stubs)

Stubs only. Enough to distinguish referents; deeper per-variant composition iterates in later sessions. A consumer who needs a variant-specific deep dive should ask for it.

### Variant A — Prompt-based

The agent's behavior is primarily carried by an authored prompt or spec file. The harness is generic (base Claude Code, plain Claude app, raw Anthropic API). Audit/design focuses on specification quality and prompt discipline. Canonical artifact: a `.md` spec file.

### Variant B — Harness-based

The agent's behavior is load-bearing on harness configuration — custom tool registry, hooks, permission tiers, MCP servers, session-state mechanisms. The prompt is one input among several. Audit/design must include harness aspects (permissions, tool loading, hooks) alongside the prompt. Canonical artifacts: `agent.md` + `.claude/settings.json` + hook scripts + MCP config.

### Variant C — Autonomous vs supervised

The agent operates over an extended time horizon with variable human supervision. Trust promotion, HITL gating, escalation paths, recovery-on-error, and governance audit cadence become load-bearing. The authoring surface may be the same as Variant A or B; the *operating envelope* is what distinguishes this variant. Audit/design pulls G9 more heavily and adds G7 (session persistence + memory) when the agent spans sessions.

## Composition

Substrate pointers for the core Librarian operations. Variant overlays noted where load-bearing.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Intent / spec | G1 `writing-agent-specifications.md` §Contract, §Key Concepts | — | `anthropic-claude-code/` custom-agent examples |
| Identity / persona | G10 `agent-design-patterns.md` §Contract, §Pitfalls | Patterns on identity-capability coupling | — |
| Context management | G2 `managing-agent-context.md` §Contract, §Pitfalls | `context-rot-attention-budget-depletion`, `proactive-compaction-before-intelligence-degradation` | — |
| Architecture / decomposition | G3 `agent-architecture-decisions.md` §Contract, §Key Concepts | `autonomy-gradient-not-binary-delegation` | — |
| Workflow / execution (Variants B, C) | G3b `agent-workflow-and-execution.md` §Contract, §State, §Termination | Patterns on durable workflow state | — |
| Tool design (Variant B or tool-using agents) | G5 `designing-agent-tools.md` §Contract, §Pitfalls | Patterns on tool registry, deferred loading, MCP ecosystems | Anthropic MCP registry, Claude Code tool source |
| Safety / permissions (Variants B, C) | G6 `agent-safety-and-permissions.md` §Contract | Patterns on defense-in-depth, prompt-injection mitigation | Claude Code permission model |
| Session persistence / memory (Variant C) | G7 `session-persistence-and-memory.md` §Contract, §Handoff | `gsd-global-learnings-store-cross-session-persistence`, Memongo cluster | Anthropic memory-tool docs |
| Governance / trust (Variant C, HITL-gated Variant B) | G9 `agent-governance-and-trust.md` §Contract — **G9.I6 required for destructive-action agents** | Patterns on HITL gating, trust promotion | — |
| Model selection | G3.I4 / G8.I4 (merged invariant: task-based, not provider-based) | — | Anthropic model-comparison docs |

**Variant overlays.** Variant A pulls {G1, G2, G3, G10}; typically skips G3b/G5/G6/G7 unless the prompt embeds tool/workflow/safety directives. Variant B adds {G3b, G5, G6} and often G9. Variant C adds {G7, G9} and elevates G9.I6 on any destructive-action path.

## Librarian read rule

**Default (Tier 1).** Identify the variant from the consumer's phrasing. Pull the Tier-1 subsection kind named by the active operation (e.g., `audit` → `### Contract`; `design` → `### Step N`; `diagnose` → `### Pitfalls`) from the variant's composed guides.

**Escalate to Tier 2 when:**
- Consumer asks about tool-call reliability, context rot symptoms, or memory mechanics (load-bearing findings live below the guide synthesis surface).
- Consumer is weighing design debates (single-agent vs multi-agent; single-store vs triple-storage memory).

**Escalate to Tier 3 when:**
- Consumer is comparing their agent design against a canonical reference (Claude Code custom agents, Memongo's memory surface).
- Consumer needs the exact shape of a harness API (hook signature, permission config format).

**Do not:**
- Treat Variant A as a Variant B or C silently. A prompt-only agent does not need a G5/G6 audit unless it embeds tool/safety directives.
- Skip G9 for any Variant-C agent — the autonomy envelope is exactly what G9 governs.
- Audit an agent from an imagined spec. Ask the consumer for the artifact.

## Provenance surfacing

Tier-1 citations point to `<guide>.md#<anchor>` (heading-match fallback until the section manifest lands, with line-range appendix per Nick's session-49 gate on exact links). Tier-2 citations point to the finding file path plus slug. Tier-3 citations point to `watched-lib/<path>:<line-range>`.

## Cross-references

- Audit composition and procedure: `audit.md` (this directory).
- Related concepts: `harness.md`, `second-brain.md`, `prompt.md` (this directory), `skill.md` (this directory).
- Use-case registry (UC-1.1–1.3, UC-3.1, UC-4.2, UC-5.1, UC-5.4, UC-6.2, UC-9.1, UC-9.2): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
