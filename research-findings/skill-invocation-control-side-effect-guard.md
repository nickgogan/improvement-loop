---
name: Skill Invocation Control — Side-Effect Guard via disable-model-invocation
summary: |-
  Claude Code skills carry two frontmatter flags that gate who can invoke them. `disable-model-invocation: true` blocks Claude from auto-loading the skill (user must type /skill-name); use for side-effect workflows (commit, deploy, send-slack). `user-invocable: false` blocks the skill from the / menu but keeps Claude's auto-invocation; use for background-knowledge skills that aren't meaningful as user commands. Default is both-can-invoke.
implementation_notes: "Side-effect skills should default to disable-model-invocation: true. Specific cases the docs name: /commit, /deploy, /send-slack-message. Reasoning: 'You don't want Claude deciding to deploy because your code looks ready.' Background-knowledge case: a 'legacy-system-context' skill explains an old system — Claude should know it when relevant but /legacy-system-context isn't a user action. Both flags also affect context loading: disable-model-invocation removes the description from Claude's context entirely; user-invocable: false leaves it in."
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "extends"
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Invocation Control — Side-Effect Guard via disable-model-invocation

## What It Is

Two Claude Code frontmatter fields control which actor can invoke a skill:

| Frontmatter | You can invoke | Claude can invoke | When loaded into context |
|---|---|---|---|
| (default) | Yes | Yes | Description always in context; full skill loads when invoked |
| `disable-model-invocation: true` | Yes | No | **Description not in context**; full skill loads when you invoke |
| `user-invocable: false` | No | Yes | Description always in context; full skill loads when Claude invokes |

The two flags are independent:
- **`disable-model-invocation: true`** — protects against Claude triggering on a description match. Intended for workflows with side effects where timing matters (commits, deploys, outbound messages).
- **`user-invocable: false`** — hides a skill from the `/` menu while keeping it available for Claude's automatic loading. Intended for background-knowledge skills that don't make sense as user commands.

## Why It Matters

This is the harness-level expression of an authority boundary: "Claude can do X" vs. "the user gates X." Without explicit control, skills with side effects are vulnerable to triggering on description match alone — Claude reads "deploy to production" matches a vague request and invokes the skill before the human meant to authorize.

The named example in the docs is `/deploy` — "you don't want Claude deciding to deploy because your code looks ready." This is the same delegation-tier problem MetaSystem's autonomy tiers solve at a different layer: which operations require explicit human consent vs. which Claude can perform autonomously.

The flag also affects context budget. `disable-model-invocation: true` removes the description from Claude's context entirely, freeing the skill-listing budget for skills Claude can actually invoke.

## Why People Are Using It

Built into Claude Code's skill system from the unified skills+commands release. Named examples in the canonical docs: `/commit`, `/deploy`, `/send-slack-message`. The Skill permissions system (`Skill(name)` / `Skill(name *)` deny rules) is a parallel control point at a different layer — `disable-model-invocation` lives in the skill, deny rules live in the user's permissions.

## Potential Alternatives

Permission deny rules at the harness level (works but lives outside the skill — drifts from skill versioning). Manual confirmation prompts inside the skill body (Claude can still invoke it). Naming convention only ("skills starting with `/deploy-*` are user-only" — no enforcement). Skill listing exclusion only (loses the still-invocable-by-name property).

## Potential Improvements

A `requires-confirmation: true` middle option — Claude can invoke but the user must confirm before execution. Skill-level tier classification matching MetaSystem's autonomy tiers (Full Autonomy / Guarded / Proposal-First). Per-tool authorization within a skill (this skill can read but not write). A standard `tags: [destructive]` convention for the user's permission rules to match against.

## Potential Failure Modes

**Side-effect skill without the flag.** Author writes a `/commit` skill, ships without `disable-model-invocation: true`. Claude reads "commit current changes" matches a request like "make sure my work is saved" and runs the skill — possibly committing work the user wasn't ready to commit.

**`user-invocable: false` confusion.** Background skills hidden from the `/` menu look "missing" to users who try to invoke them directly. Documentation must point out the asymmetric visibility.

**Override settings shadow the flag.** `skillOverrides` in settings can flip a skill to `"user-invocable-only"` from outside the skill — the skill author's intent is overridable per user. Trust boundaries blur.

**False sense of security.** `disable-model-invocation` prevents auto-loading but the user can still invoke the skill, and a malicious skill that gets the user to type its name still runs. The flag is a Claude-gating control, not a destructive-action control.
