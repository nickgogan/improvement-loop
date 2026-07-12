---
term: prompt
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
  - "prompt"
aliases:
  - "Prompt"
  - "System prompt"
  - "User prompt"
---

# Prompt

## Short definition

A **prompt** is an authored instruction a model executes — the text the model receives before generating a response. Prompts range from single-turn user messages to multi-thousand-token system prompts that persist across turns. A prompt is the *content*; the agent is the *assembly* that includes the prompt plus model, tools, context, and harness.

Single referent — no variants. Prompts for single-turn tasks, system prompts, agent instruction sets, and spec documents share the same core authoring concerns; size and persistence shift the emphasis, not the discipline.

## Not to be confused with

| Not prompt | What it is instead |
|---|---|
| **Agent** | The full assembly (prompt + model + tools + context + harness). A prompt is one input into the agent. See `agent.md` (this directory). |
| **Spec document** (CLAUDE.md, agent.md, build spec) | A specification document *is* a prompt in function (the model executes against it), but its size and scope pull in Specification Engineering concerns (G1). Treat as a prompt at the document level when auditing. |
| **Skill** | A prompt packaged as a reusable procedural unit. A skill contains a prompt; a prompt alone is not a skill. See `skill.md` (this directory). |
| **Rule** (as artifact class) | A declarative invariant. A rule is an input into a prompt's constraints; it is not the prompt itself. |
| **Role-only directive** | "You are a helpful assistant." Valid as a role, insufficient as a prompt. See G1 Pitfalls. |

## Audit behavior — extension over `/prompt-evaluator`

**The IL audit of a prompt extends `/prompt-evaluator`; it does not replace it.**

`/prompt-evaluator` (workspace root) applies a 4-discipline rubric (Prompt Craft, Context Engineering, Intent Engineering, Specification Engineering — Nate B. Jones + Anthropic guidance) to produce a general-purpose scorecard. That rubric is the primary lens. Most prompts are well-served by it alone.

The IL audit adds only what `/prompt-evaluator` cannot, without duplicating what it already covers. Specifically:

| 4-discipline dimension | IL extension — fires only when applicable |
|---|---|
| Prompt Craft (Disc 1) | No IL addition. G8 Contract at aspect level overlaps; no extension required. |
| Context Engineering (Disc 2) | **G2a/G2b Contract specifics** if prompt embeds context: G2a for structuring/tiering/retrieval; G2b for attention-budget mechanics, caching invariants, hidden-context accounting, degradation defense. Plus Tier-2 findings (`context-rot-attention-budget-depletion`, `proactive-compaction-before-intelligence-degradation`). |
| Intent Engineering (Disc 3) | No IL addition. G1 Contract at aspect level overlaps; no extension required. |
| Specification Engineering (Disc 4) | No IL addition unless the prompt is a spec document — then G1 Spec-level invariants may surface beyond the 4-discipline's self-containment / acceptance-criteria / decomposition / evaluation lens. |
| (Not covered — new category) | **G5 Contract specifics** if prompt embeds tool directives: tool registry discipline, deferred loading, intermediate-result handling. |
| (Not covered — new category) | **Harness-specific IL findings** (Claude-specific model-task mapping, prompt-caching threshold patterns) — Tier-2 surfacing, on ask. |

Precondition gating (audit.md composition rule c) is load-bearing: G2a/G2b fire only if the prompt embeds context directives; G5 fires only if it embeds tool directives. A one-shot prompt that is role + task with no context and no tools fires **no IL extensions** — `/prompt-evaluator` alone is sufficient and the IL audit reports that explicitly.

## Composition

Only IL-extension pointers. For baseline rubric coverage, route to `/prompt-evaluator`.

| IL extension aspect | Tier 1 (guides) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Context management specifics (fires when prompt embeds context) | G2a `structuring-agent-context.md` §Contract (structuring); G2b `defending-agent-context.md` §Contract (degradation) | `context-rot-attention-budget-depletion`, `proactive-compaction-before-intelligence-degradation` | Anthropic caching docs |
| Tool-use specifics (fires when prompt embeds tool directives) | G5 `designing-agent-tools.md` §Contract — gate on G5 Preconditions | Patterns on tool-call reliability, registry discipline | Claude Code tool source |
| Spec-document-scale quality (fires when prompt is a spec document > ~500 lines) | G1 `writing-agent-specifications.md` §Contract | Patterns on spec decomposition | — |
| Harness-specific / Claude-specific tuning (fires on ask or on symptom) | — | Prompt-caching threshold findings; G3.I4=G8.I4 merged invariant (task-based model selection) | Anthropic prompt cookbook |

## Librarian read rule

**Default for audit-prompt:** invoke `/prompt-evaluator` first (or receive its output). Then apply IL extensions only where Preconditions fire. If no IL extension fires, report that explicitly — "IL audit adds no further findings beyond `/prompt-evaluator`'s output; the 4-discipline scorecard is sufficient for this prompt."

**Escalate to Tier 2 when:**
- A 4-discipline dimension scored weakly and the IL has a mechanism-level finding that explains the weakness (e.g., low Context Engineering score + prompt has long stable context → surface `context-rot-attention-budget-depletion`).
- Consumer's prompt exhibits a known symptom (losing constraints mid-turn, drifting tone) — pull pattern substrate on the symptom's mechanism.

**Escalate to Tier 3 when:**
- Consumer is comparing their prompt against a canonical reference (Anthropic cookbook example, a Claude Code system prompt).

**Do not:**
- Duplicate `/prompt-evaluator`'s rubric. If the 4-discipline dimension already covers the concern, do not re-run it under a different name.
- Fire G2a/G2b or G5 on a prompt that doesn't invoke them. Precondition gates exist for a reason.
- Run the IL extension if the consumer only asked for a general prompt review — offer `/prompt-evaluator` alone and ask whether the IL extension is wanted.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding file path + slug. Tier-3 citations: `watched-lib/<path>:<line-range>`.

## Cross-references

- Audit composition and procedure: `audit.md` (this directory).
- Related concepts: `agent.md`, `skill.md` (this directory).
- Coordination target: `.claude/skills/prompt-evaluator/SKILL.md` (workspace root).
- Use-case registry (UC-3.2, UC-2.3): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role).
