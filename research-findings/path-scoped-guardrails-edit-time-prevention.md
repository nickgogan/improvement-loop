---
name: 'Path-Scoped Guardrails as Edit-Time Prevention Layer'
summary: 'Conditional instruction files the harness auto-applies only when the agent touches files matching a path pattern, used specifically for guardrails: the rule fires exactly when the risk exists (editing a protected tree), without paying always-on cost. Prevention (rule injected at edit time) complements post-hoc audit scripts. Where the platform lacks path-conditional injection, the documented fallback is folding the rules into the always-on file and recording the weaker guarantee.'
implementation_notes: 'The engine has path-scoped context (.claude/rules/, system-scoped CLAUDE.md) but uses it for orientation, not guardrails. The adoptable delta is the framing: identify the engine''s highest-risk edit-time mistakes (e.g. hand-editing generated files like FOUNDATIONS.md, writing counts into tracked docs, editing governance-tier files casually) and put the preventing rule on the tree where the mistake happens, paired with the existing audit/hook layer as the post-hoc check. Also a candidate criterion for /assess-* and the portable kernel''s wiring rows (optional tier with a prose fallback).'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- path-scoped-rules
- guardrails
- prevention-layer
- context-injection
---
# Path-Scoped Guardrails as Edit-Time Prevention Layer

## What It Is

Instruction files the harness auto-applies only when the agent touches files matching a
path glob — used not for general context distribution but for **guardrails scoped to the
tree they protect**. CareerBuddy runs two standing rule-sets this way: a method-layer
separability rule on the shared KB tree (zero user-specific content — no names, no
target lists; judgment test: "true for every other user and any future adopter?") and
user-evidence guardrails on the per-user tree (traceability to documented sources,
tenant isolation, human gates on profile writes).

## Why It Matters

Plain English: the highest-risk mistakes in a file-based agentic system are edit-time
mistakes in specific trees — leaking private data into a shared layer, mishandling
evidence, hand-editing generated files. Path-scoping puts the rule in front of the agent
at exactly the moment it matters, without taxing every other request the way an
always-on rule would. It is the *prevention* half of a two-layer defense whose other
half is post-hoc audit scripts — cheaper than always-on, earlier than audit.

## How It Works

- **Mechanism (harness-specific):** e.g. VS Code Copilot's
  `.github/instructions/*.instructions.md` with `applyTo:` glob frontmatter (`kb/**`,
  `users/**`); Claude Code analogs are directory-scoped CLAUDE.md files and path-scoped
  rules. The canon requirement is only that both rule-sets *exist and auto-apply* on
  their trees — the mechanism is adapter-delegated.
- **Escalation rule embedded in the guardrail:** if the agent finds a violation already
  present (user content in the shared layer), the instruction is freeze and report —
  not silently fix — because a violation implies the prevention layer failed and the
  blast radius is unknown.
- **Degradation path is part of the pattern:** platforms without path-conditional
  injection fold the rules into the always-on file (short form) or the protected tree's
  AGENTS.md, accepting the weaker guarantee — and *record that weakening* in the
  install report. The invariant that survives any adaptation: both rule-sets are
  presented to the agent before it edits their trees, and the substantive bar itself
  (e.g. separability) is never weakened.
- **Pairing with audit:** a post-hoc audit script checks the same invariants
  (completeness targets like "every root doc classified"), so prevention and detection
  reference one shared rule statement rather than drifting apart.

## How It Could Fail

Path-scoped rules are invisible until triggered, so they escape review — stale guardrails
persist silently. Glob mismatches (files moved, tree renamed) turn protection off with no
error. Overuse for general context (rather than genuine edit-time risk) recreates the
always-on bloat problem one directory at a time.
