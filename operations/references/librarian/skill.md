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

## Construction

Author-time substrate for `/design-skill` and any operation that constructs a new SKILL.md. Audit-time operations consume the same gates (notably the Safety-critical classification in §Decision sequence) but in inspection mode.

### Decision sequence

Ordered steps the author works through before drafting. Each step bounds a downstream authoring choice — skipping a step does not skip the decision, only the deliberation.

1. **Name the single bounded operation.** A skill packages one operation. State it as a verb-phrase ("triage research sources", "lint frontmatter against schema"). If you cannot state it without "and", the scope is two skills or one workflow — return and read §Scoping heuristics.
2. **Identify the trigger shape.** Write the consumer phrasings or upstream conditions that should invoke this skill. The `description` frontmatter is derived from this; G8 governs description quality (a skill that never triggers reliably is dead weight).
3. **Enumerate the tool surface.** List the tools the procedure actually needs — not the tools it *might* want. Each tool added widens the safety envelope (next step) and the deferred-loading cost (G5).
4. **Run the Safety-critical classification.** Destructive actions require G9.I6 enforcement; treat this as a hard gate, not a polish step.

   A skill is **safety-critical** if **any** of:
   - Its `allowed-tools` include Write, Edit, Bash (destructive flags), or any MCP tool that mutates external state.
   - Its procedure steps include deployment, publication, cross-system writes, or credential manipulation.
   - Its output is consumed by a downstream automated action without human review.

   Per session-48 Test 4 refinement: any safety-critical skill **always fires G9.I6** at audit time, regardless of whether the skill's prompt itself mentions governance. At design time, this means the procedure must encode HITL gating for the destructive action (confirm-before-act, dry-run mode, or explicit human-approval step). Authoring a safety-critical skill without HITL gating produces a skill that will fail audit on first inspection.

5. **Specify procedure, state, and termination.** The procedure body is where most invariants fire (G3b §State, §Termination). State explicitly what conditions end the skill — both success and abort paths.
6. **Specify output shape.** Skills produce reports, files, or state changes. Name the shape so the consumer can verify against it.
7. **Cross-check against §Composition.** Confirm the guide set the skill will be audited against matches the surface authored (no embedded context = no G2a/G2b firing; no tools = no G5 firing). Mismatches mean you've either over-scoped or under-specified.

### Template skeleton

The minimum valid SKILL.md shape. Fill in placeholders; do not delete required sections.

````markdown
---
name: <kebab-case-name>
description: <one-line description used for trigger matching — phrase it the way a consumer would ask>
allowed-tools: <minimal list>
argument-hint: <optional — what the user passes after the slash command>
---

# <Skill Display Name>

## When to use

<Concrete trigger conditions. Mirror the description in fuller prose; name the consumer questions that should invoke this skill and the ones that should not.>

## Procedure

1. <Step — name the tool used and what's read/written>
2. <Step>
3. <Step>

## Output shape

<Describe the produced artifact — file path, report structure, conversation message, etc.>

## Boundary conditions

- **Termination:** <When the skill ends. Success criterion. Abort criterion.>
- **Out of scope:** <Adjacent operations this skill does NOT do — point to the skill that does.>
- **Safety-critical?** <Yes / No, per §Construction Decision sequence step 4. If yes, name the HITL gate.>
````

A skill missing any of `When to use`, `Procedure`, `Output shape`, or `Boundary conditions` is not a complete skill — audit will fire G1.I1 (Contract presence) on first read.

### Scoping heuristics

When in doubt, prefer the smaller skill plus explicit composition over the larger one with internal branching.

- **Split when:** the procedure has two distinct end-states that require different follow-ups (e.g., a skill that both *identifies* candidates and *extracts* them — split per DD-80 precedent). A second sign: the `description` needs "and" or two trigger conditions joined by "or".
- **Collapse when:** the "skill" is a single tool call with no decision logic — that's a procedure step inside the calling skill, not its own skill. A SKILL.md whose Procedure section has one step is almost always over-extracted.
- **Stay one skill when:** the operation has multiple branches but the same end-shape (e.g., `/research-query --persist` vs. without — same operation, same output shape, one decision branch).

### Authoring-time anti-patterns

Mistakes made while writing the SKILL.md. Distinct from G8 Pitfalls, which surface at inspection time when the skill is failing to trigger or producing wrong output.

- **Tool over-granting.** Listing every tool the procedure *could* use rather than the minimum it *does* use. Over-grants enlarge the audit surface (G5, G6) and trip Safety-critical classification false positives.
- **Description that won't trigger.** Writing `description` as a feature label ("research helper") rather than as consumer phrasing ("when the user asks to research a topic, investigate a question, or explore an area not in the KB"). Triggers on the latter; ignored on the former.
- **Embedded workflow.** Authoring multi-stage orchestration inside the procedure. If the procedure has explicit phase boundaries with gates between, it's a workflow — extract the phases into separate skills and orchestrate from outside.
- **Skipping Safety-critical classification.** Writing the procedure first and leaving classification "for review". This inverts the safety envelope — the procedure has already been authored before the destructive-action gate ran.
- **Conflating skill with playbook.** Authoring a SKILL.md whose Procedure reads as prose-for-a-human ("then you might want to consider…"). A skill is executable by an agent; if a human is in the loop reading prose, write a playbook in `knowledge/guides/`.
- **Re-stating guide content in the procedure.** Repeating G3b §Termination text inside the skill body. The composition table routes to guides; the procedure should embody invariants, not paraphrase them.

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

**Default (Tier 1).** Pull the operation's named subsection kind from {G1, G3b, G5, G6, G8} — `audit → ### Contract`, `design → ### Step N` (uses §Construction Decision sequence + Template skeleton from this concept doc), `diagnose → ### Pitfalls`. For safety-critical skills (see §Construction Decision sequence step 4), **add G9.I6 unconditionally**.

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
- Contract-section spot check §Test 4 (where the G9.I6 refinement was validated): `archive/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`.
- Related concepts: `agent.md`, `prompt.md` (this directory).
- Use-case registry (UC-3.3, UC-4.5): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
