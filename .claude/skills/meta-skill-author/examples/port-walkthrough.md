# Worked Example — Port Mode

> End-to-end demonstration of §4 Port Mode: one canonical skill → five
> platform-adapted versions, built from the portable layer + thin per-platform
> wrappers. Read `references/platform-matrix.md` and the `adapters/` files alongside.

Illustrative, not authoritative. If this conflicts with `SKILL.md`,
`references/platform-matrix.md`, or the `adapters/`, those win.

---

## The canonical skill

We port the `incident-pir-drafter` skill from the Design walkthrough. The
**canonical instruction source** is harness-agnostic prose; each platform gets a
thin wrapper that carries only frontmatter and packaging metadata
`[shared-instructions-multi-harness-plugin-wrappers]`. We never fork the body —
the prose lives once, and drift between platform copies is the failure mode this
architecture prevents.

Because we target 5 platforms, the correct strategy is template-generated
artifacts from one canonical source, not hand-maintained copies
`[cross-platform-context-file-strategy]` `[multi-ide-portability-via-installer-templates]`.

---

## The portable layer (identical across all 5)

Open-standard fields only `[skills-as-open-portable-standard]`:

```yaml
name: incident-pir-drafter
description: >
  Drafts a structured post-incident review from an incident channel transcript...
license: MIT
```

The full SKILL.md body is unchanged across platforms. Everything platform-specific
lives in the wrapper, never in the body.

---

## Per-platform adaptations (side by side)

| Concern | Claude Code | Cursor | GitHub Copilot | OpenAI Codex | Perplexity |
|---------|-------------|--------|----------------|--------------|------------|
| File / location | `~/.claude/skills/incident-pir-drafter/SKILL.md` | `.cursor/rules/incident-pir-drafter.mdc` | `.github/copilot-instructions.md` or `AGENTS.md` | `AGENTS.md` | uploaded skill (folder + zip) |
| Auto-load trigger | description-based | `alwaysApply` / glob in MDC frontmatter | workspace auto-load | workspace auto-load | description-based |
| Invocation control | `disable-model-invocation: true` for the PR-comment side effect | n/a (no equivalent) | n/a | n/a | `confirm_action` as HITL primitive |
| Extension fields used | `when_to_use`, `paths` | MDC `globs`, `alwaysApply` | none (tool-agnostic) | none | none |
| HITL primitive | `disable-model-invocation` guard | manual review | manual review | manual review | `confirm_action` |

Each cell maps to its `adapters/<platform>.md` file. The wrapper for each platform
is **< 40 lines** — frontmatter and packaging only `[shared-instructions-multi-harness-plugin-wrappers]`.

---

## The one mandatory cross-platform audit: reasoning-model anti-patterns

Before porting to *any* new platform, audit the body for prescribed-reasoning
patterns — explicit chain-of-thought, few-shot examples inside the body,
self-consistency, least-to-most decomposition, skeleton-of-thought. These degrade
performance on GPT-5.4, Claude 4.6, and Gemini 3.1
`[reasoning-model-anti-pattern-prescribed-reasoning]`. Since the target platforms
route to these model families, a body that "worked" on an older model can regress
silently after porting. Our canonical body already passed this audit in Design,
so no rewrite is needed here — but the audit is run again at port time as a gate.

---

## Context-file taxonomy note

The Codex and Copilot adapters both land in `AGENTS.md`, the tool-agnostic
conventions file `[context-file-taxonomy-claudemd-soulmd-agentsmd]`. Where two
platforms load identical context, prefer a symlink (`AGENTS.md → CLAUDE.md`) over
a duplicated file `[cross-platform-context-file-strategy]`. ETH Zurich found
manually written, concise context files outperform auto-generated ones, so the
wrappers stay thin and hand-checked `[model-specific-context-file-sensitivity]`.

---

## Cross-surface compatibility declaration

Custom skills do **not** sync across surfaces; each deployment is independent
`[skill-cross-surface-portability-with-constraints]`. We declare a `compatibility`
field on any wrapper that uses non-portable extension fields, so a consumer on a
different surface knows what is required before installing.

---

## What this example demonstrates

- One canonical body; five thin wrappers; zero forked prose.
- 3+ platforms → template generation, not hand-copies.
- The reasoning-model anti-pattern audit is a hard gate at port time.
- `AGENTS.md` is shared across Copilot and Codex; symlink over duplicate.
- Non-portable fields are always declared via `compatibility`.
