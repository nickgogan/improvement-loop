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

## Construction

Author-time substrate for `/design-agent` and any operation that constructs a new agent specification (`agent.md`, `CLAUDE.md`, a system prompt). One section, variant-aware: the Decision sequence routes via Variant selection (step 1), and the Template skeleton overlays variant additions on a common core.

### Decision sequence

Ordered steps the author works through before drafting. Step 1 gates the rest: subsequent steps' content depends on which variant fired. An agent can fit more than one variant simultaneously (a Variant-B + Variant-C agent is common); apply both overlays where they overlap.

1. **Select the variant.** Variant selection determines which guides compose, which artifact surfaces are load-bearing, and which sections the spec must carry. Pick from authorial intent or consumer phrasing; ask one disambiguating question if ambiguous.

   | Authorial intent / consumer phrasing… | Variant | Why |
   |---|---|---|
   | "my `agent.md`," "the instructions I wrote for my agent," "my system prompt for the agent" | **A — Prompt-based** | The agent's behavior is carried by an authored spec the harness loads. |
   | "my custom Claude Code agent," "my Cursor agent with these hooks," "my MCP-tool-enabled agent" | **B — Harness-based** | The agent's behavior is meaningfully carried by harness configuration (tools, hooks, permissions), not only its prompt. |
   | "my background agent," "my long-running agent," "my agent that does things without me watching" | **C — Autonomous-vs-supervised** | The agent's autonomy envelope matters — HITL gating, escalation paths, trust promotion become load-bearing. |

   When variants overlap (most often B + C), the construction pulls the union — apply each variant's overlay in the steps below. Variant stubs are defined in §"Variants (stubs)".

2. **State identity, intent, and bounded class of tasks.** All variants. Author the Core Truths / Intent statement; this anchors every downstream constraint. (Loads G1 §Contract, G10 §Contract.)

3. **Specify context structure.** All variants. What does the agent need to know at session boot vs. on demand? (Loads G2a §Contract.) For multi-session or long-context agents, also specify defense against context degradation (G2b).

4. **Specify architecture.** All variants. Single agent vs. delegating to sub-agents; if delegating, name the boundary. (Loads G3 §Contract.) See §Scoping heuristics for one-agent-vs-multi-agent decisions.

5. **Enumerate harness surface — Variant B (and B+C).** Tools, hooks, permission tiers, MCP servers, session-state mechanisms. Each item added widens the safety envelope (step 7).

6. **Specify workflow and termination — Variants B, C.** Durable workflow state, termination conditions, recovery on error. (Loads G3b §State, §Termination.)

7. **Size the autonomy envelope — Variant C primarily; HITL-gated Variant B.** Trust-promotion thresholds, HITL gates, escalation paths, governance-audit cadence. Destructive-action paths fire G9.I6 unconditionally (analogous to skill safety-critical classification — treat as a hard gate). The Autonomy Table from the agent's constitution lives here.

8. **Specify session persistence — Variant C, or any agent spanning sessions.** Handoff protocol, memory mechanism, what persists vs. what's re-derived. (Loads G7 §Contract, §Handoff.)

9. **Specify recovery.** All variants. What happens when state is inconsistent, a tool fails, or context is corrupted.

10. **Cross-check against §Composition.** Confirm the variant's composed guide set matches the authored surface (a Variant A agent that embeds tool directives has silently become Variant B; an agent spanning sessions without persistence treatment fails G7).

### Template skeleton

Common-core skeleton with variant overlays. Author the common core for every agent; add overlays per declared variant.

**Common core (all variants):**

````markdown
---
title: "<Agent Name>"
type: "agent"
target_system:
  - "<system>"
created: "<date>"
updated: "<date>"
---

# <Agent Name>

## Constitution

### Core Truths
<3–6 bullets. The agent's anchoring beliefs.>

### Boundaries
<NEVER / MAY rules. Explicit out-of-bounds.>

### Vibe
<How the agent communicates. Concision, tone, action bias.>

### Continuity
<Session boot, memory model, state persistence.>

## Disposition

### When Active
### Cognitive Approach

## Scope

### In Scope
### Out of Scope

## Autonomy Table

| Action | Tier | Notes |
|---|---|---|
| <action> | <Full Autonomy / Guarded / Proposal-First / Human-Required> | <notes> |

## Skill Inventory

<Per-skill row: name, purpose, status.>

## Communication

### Input Artifacts Consumed
### Output Artifacts Produced
### Relationship to Other Agents

## Contract

### Preconditions
### Invariants
### Recovery
### Governance
````

**Variant B overlay (additions):**

- Constitution → add a **Harness surface** subsection: tools, hooks, permission tiers, MCP servers.
- Communication → "Input Artifacts Consumed" must include the tool registry / hook definitions / harness config.
- Contract → Invariants reference G5/G6 invariants explicitly.

**Variant C overlay (additions):**

- Constitution → expand **Continuity** to cover handoff protocol and persistence mechanism in concrete terms (which file, which channel).
- Insert an **Autonomy Envelope** section between Scope and Autonomy Table: HITL gates, escalation thresholds, trust-promotion criteria.
- Contract → Invariants reference G7 + G9 invariants. G9.I6 fires for any destructive-action path.

An agent missing the common-core sections is not a complete agent spec — audit will fire G1.I1 (Contract presence) on first read. An agent missing its declared variant's overlay fails that variant's audit gates.

### Scoping heuristics

When in doubt about agent decomposition, prefer one bounded agent over multiple loosely-coupled ones — multi-agent topologies pay coordination cost every session (G3 §State).

- **Split into multiple agents when:** the in-scope task list contains two persistent dispositions that conflict (analytical vs. creative; generator vs. assessor — rule 10). Or: the read/write boundaries are disjoint and one agent's writes would violate another's read-only contract.
- **Stay one agent when:** the apparent "two roles" are actually one disposition with mode switches (Librarian's Teacher/Builder modes are one agent). The cost of a second agent — separate constitution, separate handoff protocol, separate audit — is paid every session.
- **Variant overlap resolution:** if two variants fire (B + C is most common), apply both overlays. Do not pick "the dominant variant" — gates from each are non-substitutable. A harness-based autonomous agent needs *both* the tool/permission gates and the autonomy-envelope gates.
- **One agent + skill vs. two agents:** by default, a new capability is a skill on the existing agent. Promote to a new agent only when the capability requires a different disposition or different read/write boundaries.

### Authoring-time anti-patterns

Mistakes made while writing the agent spec. Distinct from G3/G6/G9 Pitfalls, which surface at inspection time when the agent is misbehaving in production.

- **Variant silently drifting.** Author declares Variant A, then embeds tool/permission directives in the prompt. The spec has become Variant B; audit composition for A misses G5/G6 gates. (See Librarian read rule §"Do not".)
- **Skipping autonomy-envelope sizing on Variant C.** Writing the Skill Inventory and Communication sections before defining HITL gates inverts the safety envelope — by the time autonomy is sized, the spec has already implied operating modes the gates can't constrain.
- **Borrowing identity from the harness.** Writing "I am a Claude Code agent" or "I am Cursor's helper" as identity. The harness is substrate, not identity (per `## Not to be confused with`). Identity is the bounded class of tasks under stated intent; harness is *where it runs*.
- **Composing every guide "just in case".** Pulling all of {G1, G2a, G2b, G3, G3b, G5, G6, G7, G9, G10} for a Variant A prompt-only agent. Composition overlays exist so unused gates don't fire — over-composition is unused audit weight that biases findings toward noise.
- **Multi-agent decomposition without a coordination contract.** Splitting an agent into sub-agents without specifying how they hand off state (which file? which channel? what gate?). Multi-agent without contract is one agent with extra startup cost.
- **Re-stating constitution invariants in every skill.** Writing "follows DD-86, respects rule 11, runs proposal-first" inside every SKILL.md attached to the agent. Constitution is canonical; skills inherit. Re-stating invites drift.

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
| Context structuring | G2a `structuring-agent-context.md` §Contract, §Pitfalls | — | — |
| Context degradation | G2b `defending-agent-context.md` §Contract, §Pitfalls | `context-rot-attention-budget-depletion`, `proactive-compaction-before-intelligence-degradation` | — |
| Architecture / decomposition | G3 `agent-architecture-decisions.md` §Contract, §Key Concepts | `autonomy-gradient-not-binary-delegation` | — |
| Workflow / execution (Variants B, C) | G3b `agent-workflow-and-execution.md` §Contract, §State, §Termination | Patterns on durable workflow state | — |
| Tool design (Variant B or tool-using agents) | G5 `designing-agent-tools.md` §Contract, §Pitfalls | Patterns on tool registry, deferred loading, MCP ecosystems | Anthropic MCP registry, Claude Code tool source |
| Safety / permissions (Variants B, C) | G6 `agent-safety-and-permissions.md` §Contract | Patterns on defense-in-depth, prompt-injection mitigation | Claude Code permission model |
| Session persistence / memory (Variant C) | G7 `session-persistence-and-memory.md` §Contract, §Handoff | `gsd-global-learnings-store-cross-session-persistence`, Memongo cluster | Anthropic memory-tool docs |
| Governance / trust (Variant C, HITL-gated Variant B) | G9 `agent-governance-and-trust.md` §Contract — **G9.I6 required for destructive-action agents** | Patterns on HITL gating, trust promotion | — |
| Model selection | G3.I4 / G8.I4 (merged invariant: task-based, not provider-based) | — | Anthropic model-comparison docs |

**Variant overlays.** Variant A pulls {G1, G2a, G2b, G3, G10}; typically skips G3b/G5/G6/G7 unless the prompt embeds tool/workflow/safety directives. Variant B adds {G3b, G5, G6} and often G9. Variant C adds {G7, G9} and elevates G9.I6 on any destructive-action path.

## Librarian read rule

**Default (Tier 1).** Identify the variant from the consumer's phrasing (or, at design time, from authorial intent). Pull the Tier-1 subsection kind named by the active operation: `audit` → `### Contract` from the variant's composed guides; `design` → §Construction (Decision sequence + Template skeleton) from this concept doc, plus `### Pitfalls` from the variant's composed guides as anti-pattern reference; `diagnose` → `### Pitfalls` from the variant's composed guides.

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
- Use-case registry (UC-1.1–1.3, UC-3.1, UC-4.2, UC-5.1, UC-5.4, UC-6.2, UC-9.1, UC-9.2): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
