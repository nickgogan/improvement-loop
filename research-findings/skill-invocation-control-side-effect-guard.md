---
name: Skill Invocation Control — Side-Effect Guard via disable-model-invocation
summary: 'Claude Code skills carry two frontmatter flags that gate who can invoke them. `disable-model-invocation: true` blocks Claude from auto-loading the skill (user must type /skill-name); use for side-effect
  workflows (commit, deploy, send-slack) — and, per Cursor''s shipped thermo-nuclear review skill, for intentionally harsh modes whose intensity the user should opt into even when no side effects exist.
  `user-invocable: false` blocks the skill from the / menu but keeps Claude''s auto-invocation; use for background-knowledge skills that aren''t meaningful as user commands. Default is both-can-invoke.
  Matt Pocock (missing-manual talk, 06-29) adds a third rationale that turns the flag into a fleet-level design triad: every model-invocable skill costs context load (its description on every request, one
  more thing to think about) and buys unpredictability (a context pointer the model may simply not follow — forcing triggering evals); user-invoked skills trade that for cognitive load on the user. His
  repo defaults to user-invoked to delete the triggering-eval problem class entirely.'
implementation_notes: 'Side-effect skills should default to disable-model-invocation: true. Specific cases the docs name: /commit, /deploy, /send-slack-message. Reasoning: ''You don''t want Claude deciding
  to deploy because your code looks ready.'' Background-knowledge case: a ''legacy-system-context'' skill explains an old system — Claude should know it when relevant but /legacy-system-context isn''t a
  user action. Both flags also affect context loading: disable-model-invocation removes the description from Claude''s context entirely; user-invocable: false leaves it in.'
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-claude-code-skills-docs.md
- cursor-team-kit-thermo-nuclear-review-skill.md
- building-great-agent-skills-the-missing-manual.md
related_findings:
- file: claude-code-skill-frontmatter-extensions.md
  rel: extends
- file: skill-md-frontmatter-as-discovery-trigger-primitive.md
  rel: extends
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
- rules/side-effect-skills-require-explicit-invocation.md
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

**Second use case beyond side effects — intentionally harsh modes.** Cursor's shipped `thermo-nuclear-code-quality-review` skill (cursor/plugins, cursor-team-kit) sets `disable-model-invocation: true` on a skill with *no* side effects at all: an extremely strict, blocker-heavy review mode. The rationale generalizes the flag from "Claude must not act without consent" to "Claude must not select an aggressive posture without consent" — a deliberately punishing review triggering on a casual "can you look at my code?" would be a tone/expectation failure, not a safety failure. The flag is the explicit-invocation-only pattern for any mode whose intensity, cost, or register the user should opt into, not just destructive operations.

**Third rationale — predictability and context-load economics (Matt Pocock, missing-manual talk, 06-29).** The invocation-mode choice is a fleet-level cost triad, not a per-skill safety toggle:

- **Context load** — every model-invocable skill puts its description in the agent's context on every request; 100 model-invoked skills = 100 descriptions the agent must pay for and think about.
- **Unpredictability** — a description is a context pointer, and "the model may just choose not to follow it," even when the skill is perfect for the task. Living with model invocation means eval-ing your skills' triggering — "which is really nasty."
- **Cognitive load** — the user-invoked alternative shifts the burden to the pilot, who must know the skill roster deeply to deploy it.

Pocock's repo (contrasted with Superpowers, which is primarily model-invoked) defaults to user-invoked specifically to remove the triggering-unpredictability problem class — accepting higher pilot skill as the price. His framing: neither mode is better; both have real costs, and the trigger decision is checklist item #1 when auditing any skill.

## Potential Alternatives

Permission deny rules at the harness level (works but lives outside the skill — drifts from skill versioning). Manual confirmation prompts inside the skill body (Claude can still invoke it). Naming convention only ("skills starting with `/deploy-*` are user-only" — no enforcement). Skill listing exclusion only (loses the still-invocable-by-name property).

## Potential Improvements

A `requires-confirmation: true` middle option — Claude can invoke but the user must confirm before execution. Skill-level tier classification matching MetaSystem's autonomy tiers (Full Autonomy / Guarded / Proposal-First). Per-tool authorization within a skill (this skill can read but not write). A standard `tags: [destructive]` convention for the user's permission rules to match against.

## Potential Failure Modes

**Side-effect skill without the flag.** Author writes a `/commit` skill, ships without `disable-model-invocation: true`. Claude reads "commit current changes" matches a request like "make sure my work is saved" and runs the skill — possibly committing work the user wasn't ready to commit.

**`user-invocable: false` confusion.** Background skills hidden from the `/` menu look "missing" to users who try to invoke them directly. Documentation must point out the asymmetric visibility.

**Override settings shadow the flag.** `skillOverrides` in settings can flip a skill to `"user-invocable-only"` from outside the skill — the skill author's intent is overridable per user. Trust boundaries blur.

**False sense of security.** `disable-model-invocation` prevents auto-loading but the user can still invoke the skill, and a malicious skill that gets the user to type its name still runs. The flag is a Claude-gating control, not a destructive-action control.

## Extraction Note — 2026-07-19
Extracted as **rule**: [[side-effect-skills-require-explicit-invocation]] in `extracts/rules/`
