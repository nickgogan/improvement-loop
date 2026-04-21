---
term: skill
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
  - "skill"
aliases:
  - "Skill"
  - "SKILL.md"
  - "Claude Code skill"
---

# Skill

## Short definition

A **skill** is a procedural packaging of a bounded operation that an agent (or a harness) can invoke. In Claude Code, the canonical shape is `SKILL.md`: a file with frontmatter (`name`, `description`, `allowed-tools`, optional `argument-hint`) and a body describing when to use the skill, what tools to use, the procedure, output shape, and boundary conditions. Skills are reusable units — the same skill runs in many contexts, invoked by the same trigger shape.

Single referent. A skill is not an agent, not a workflow, not a playbook. Those adjacencies are handled in §"Not to be confused with."

## Not to be confused with

| Not skill | What it is instead |
|---|---|
| **Agent** | A model-plus-context assembly. An agent may invoke skills; a skill is not an agent. See `agent.md` (this directory). |
| **Workflow** (as orchestrated multi-step process) | A composition that may call multiple skills. Workflow state and termination concerns live in G3b; a skill is a unit within a workflow. |
| **Playbook** | Prose-form guidance for a human. A skill is executable by an agent; a playbook is read by a human. |
| **Prompt** | Instructional content. A skill contains a prompt but also names tools, a procedure, and an output shape. See `prompt.md` (this directory). |
| **Hook** | A harness mechanism that runs in response to events. A hook may call a skill; a skill does not call a hook (the harness does). |

## Safety-critical classification

Some skills perform **destructive actions** — file deletes, repo pushes, database writes, external API posts, permission changes. Safety-critical skills require G9.I6 enforcement: destructive actions are human-approved, not agent-autonomous.

A skill is safety-critical if **any** of:
- Its `allowed-tools` include Write, Edit, Bash (destructive flags), or any MCP tool that mutates external state.
- Its procedure steps include deployment, publication, cross-system writes, or credential manipulation.
- Its output is consumed by a downstream automated action without human review.

Per session-48 Test 4 refinement: the audit composition for any safety-critical skill **always fires G9.I6** regardless of whether the skill's prompt itself mentions governance.

## Composition

Substrate pointers for the core Librarian operations on skills.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Intent / spec quality | G1 `writing-agent-specifications.md` §Contract | Patterns on skill-spec clarity | — |
| Workflow / execution | G3b `agent-workflow-and-execution.md` §Contract, §State, §Termination | Patterns on durable workflow state, termination conditions | — |
| Tool use | G5 `designing-agent-tools.md` §Contract, §Pitfalls | Patterns on tool registry, deferred loading, intermediate-result handling | Claude Code tool source, MCP ecosystem |
| Safety / permissions | G6 `agent-safety-and-permissions.md` §Contract — **G6 applies to all skills with tool access** | Patterns on defense-in-depth | Claude Code permission model |
| Prompt craft (trigger description, procedure) | G8 `model-resilient-prompt-engineering.md` §Contract, §Pitfalls | Patterns on skill-description quality (triggers the skill reliably) | — |
| **Governance (safety-critical only)** | **G9 `agent-governance-and-trust.md` §Contract — G9.I6 fires on every destructive-action skill** | Patterns on HITL gating for destructive operations | — |

## Librarian read rule

**Default (Tier 1).** Pull the operation's named subsection kind from {G1, G3b, G5, G6, G8}. For safety-critical skills (see classification above), **add G9.I6 unconditionally**.

**Escalate to Tier 2 when:**
- Consumer asks about skill-trigger reliability (why the skill isn't being invoked when it should be) — pull G8 Pitfalls + findings on description quality.
- Consumer's skill has a symptom of unreliable termination or state leakage — G3b patterns apply.

**Escalate to Tier 3 when:**
- Consumer is comparing their skill against a canonical one (Claude Code's built-in skills, MCP reference implementations).

**Do not:**
- Skip the G9.I6 gate on a safety-critical skill. The classification is a non-negotiable trigger.
- Audit a skill from its `name` and `description` alone. The procedure body is where most invariants fire.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding file path + slug. Tier-3 citations: `watched-lib/<path>:<line-range>`. Any G9.I6 fire must quote the invariant text and cite the source so the consumer sees why the destructive-action gate applied.

## Cross-references

- Audit composition and procedure: `audit.md` (this directory) — see Phase 2 §"Build rubric" for how G9.I6 is added for safety-critical skills.
- Contract-section spot check §Test 4 (where the G9.I6 refinement was validated): `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`.
- Related concepts: `agent.md`, `prompt.md` (this directory).
- Use-case registry (UC-3.3, UC-4.5): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
