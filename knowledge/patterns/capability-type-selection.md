---
title: "Capability Type Selection"
id: "capability-type-selection"
type: "pattern"
category: "agent-design"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-06"
updated: "2026-04-06"
author: "claude"
source_dd:
  - "DD-34"
  - "DD-49"
  - "DD-52"
  - "DD-53"
  - "DD-60"
  - "DD-63"
  - "DD-65"
tags:
  - "pattern"
  - "agent-design"
  - "skill-design"
  - "decision-framework"
  - "agentic-layer"
aliases:
  - "Agent vs Skill"
  - "When to use agents"
  - "Capability taxonomy"
---

# Capability Type Selection

When building something that an AI agent can do, choose the right capability type. The wrong choice creates either unnecessary complexity (agent when a hook would do) or insufficient structure (skill when an agent team is needed).

## The Four Capability Types

| Type | What It Is | Invocation | Identity | State |
|------|-----------|------------|----------|-------|
| **Agent** | A persona with its own thinking style, scope, and responsibilities | Implicit — always active within its system | Named role with cognitive disposition | Long-lived; maintains context across tasks |
| **Skill** | A reusable procedure with defined inputs, outputs, and access boundaries | Explicit — slash command or trigger phrase | Borrowed from the invoking agent | Stateless; runs and completes |
| **Workflow** | A multi-step artifact chain coordinating work across agents or skills | Orchestrated — triggered by milestone or human | None of its own; agents bring identity | Tracked via artifacts at each stage |
| **Hook** | An event-triggered automation that runs without explicit invocation | Automatic — fires on events (file save, tool use, session start) | None — mechanical, not cognitive | Stateless; fire-and-forget |

## Decision Framework

### Start here: What are you building?

```
Does it need its own thinking style and point of view?
  YES → Agent
  NO  →
    Is it a multi-step procedure that should be invocable on demand?
      YES → Skill
      NO  →
        Does it coordinate work across multiple agents or skills?
          YES → Workflow
          NO  →
            Should it fire automatically in response to an event?
              YES → Hook
              NO  → It's probably just a rule (put it in .claude/rules/)
```

### The key discriminators

**Agent vs Skill** — the most common decision.

| Signal | Agent | Skill |
|--------|-------|-------|
| Has a cognitive disposition ("thinks like a skeptical analyst") | Yes | No — borrows the caller's disposition |
| Has long-lived responsibilities ("owns prompt quality") | Yes | No — runs when invoked, then done |
| Needs to make judgment calls under ambiguity | Yes | Follows a defined procedure |
| Has its own read/write scope boundaries | Yes (DD-53) | Yes (DD-65) — but scope is per-invocation |
| Multiple instances with different configurations | No — one per role | Yes — parameterized |
| Communicates through artifacts to other roles | Yes (DD-63) | No — returns output to the invoker |

Rule of thumb: If you're defining **how something thinks**, make an agent. If you're defining **what something does**, make a skill.

**Skill vs Hook** — automation boundary.

| Signal | Skill | Hook |
|--------|-------|------|
| Requires human to decide when to run | Yes | No — event-driven |
| Produces output the user reviews | Yes | No — silent unless it fails |
| Has complex logic or branching | Yes | No — keep hooks simple |
| Needs access to multiple tools | Yes | Typically one command |

Rule of thumb: If the user says "do this now", it's a skill. If the user says "do this every time X happens", it's a hook.

**Workflow vs Skill** — scope boundary.

| Signal | Workflow | Skill |
|--------|----------|-------|
| Multiple agents contribute to the output | Yes | No — single executor |
| Stages have different owners/dispositions | Yes | No |
| Intermediate artifacts need human review | Yes (gates) | No |
| Can be completed in one invocation | No | Yes |

Rule of thumb: If the work flows through multiple roles with handoffs, it's a workflow. If one agent can complete it end-to-end, it's a skill.

## Where Each Type Lives (DD-52, DD-49)

Per the fractal unit pattern, each system has:

```
agents/
  {agent-name}/
    skills/        ← Agent-specific skills
    workflows/     ← Multi-step sequences
    hooks/         ← Event triggers
```

Per DD-49, Claude Code skills also live in:

```
.claude/skills/    ← Cross-system or system-specific slash commands
.claude/agents/    ← Engine-facing agent definitions
.claude/rules/     ← Conditional rules (not a capability type)
```

| Scope | Skills placement | Agent placement |
|-------|-----------------|-----------------|
| Cross-system | Root `.claude/skills/` | Root `.claude/agents/` |
| System-specific | `{system}/.claude/skills/` | `{system}/agents/` |
| Project-scoped | `incubator/{project}/.claude/skills/` | `incubator/{project}/agents/` |

## Anatomy of Each Type

### Agent Specification (DD-53, DD-60)

```yaml
# In agents/{name}/README.md or .claude/agents/{name}.md
Role: Product Owner
Intention: Maximize user value while respecting system constraints
Cognitive Disposition: Thinks in outcomes, not features
Directives:
  Must: Validate every requirement against the constitution
  Must Not: Approve scope without architect review
  May: Defer low-priority items to next milestone
Escalation: When requirements conflict with existing DDs
Read Scope: PRDs, DDs, IB items, architecture docs
Write Scope: PRDs, IB items (create only)
Handoff Artifact: PRD → Architect
```

### Skill Specification (DD-34, DD-65)

```yaml
# In .claude/skills/{name}/SKILL.md
---
name: research-loop
description: Periodic research scan...
user-invocable: true
allowed-tools: Read Grep Glob Write Edit WebSearch WebFetch
argument-hint: "<full|context|model|prompt|tools|intent|arxiv>"
---
# Procedure, access model, calibration notes...
```

### Hook Specification

```json
// In .claude/settings.json or settings.local.json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "node hooks/validate-frontmatter.js",
        "timeout": 5
      }]
    }]
  }
}
```

### Workflow (Artifact Chain per DD-63)

```
PO writes PRD
  → Architect reads PRD, writes Architecture Doc
    → TPM reads Architecture, writes Task Plan
      → Engineer reads Plan, writes Code
        → Tester reads Code, writes Test Report
          → TPM verifies completion
```

Each arrow is a handoff. Each role reads upstream artifacts and writes downstream artifacts. No direct cross-modification without escalation.

## Anti-Patterns

| Anti-Pattern | What Goes Wrong | Fix |
|-------------|-----------------|-----|
| **Agent without disposition** | Generic "helpful assistant" that hedges on everything | Define the cognitive disposition first — how does it think? |
| **Skill without access model** | Skill reads/writes things it shouldn't, breaks scope boundaries | Add explicit read/write scope table (DD-65 pattern) |
| **Hook doing skill work** | Complex logic in a hook that should be invoked explicitly | Extract to a skill; hook should only trigger simple actions |
| **Workflow as a single skill** | One skill trying to do what needs multiple roles with handoffs | Split into artifact chain with clear stage owners |
| **Agent for one-off task** | Full persona definition for something that runs once | Use a skill — agents are for long-lived roles |
| **Rule masquerading as skill** | Skill that just says "don't do X" with no procedure | Put it in `.claude/rules/` as a conditional rule |

## When to Revisit

Promote a capability type upward when:
- A **rule** keeps getting invoked manually → make it a **hook**
- A **hook** needs branching logic or user interaction → make it a **skill**
- A **skill** starts needing its own thinking style and judgment → make it an **agent**
- Multiple **skills** need coordinated handoffs → define a **workflow**

Demote when:
- An **agent** has no judgment calls and just follows steps → simplify to a **skill**
- A **skill** always runs on the same trigger → simplify to a **hook**
- A **workflow** has only one real contributor → collapse to a **skill**
