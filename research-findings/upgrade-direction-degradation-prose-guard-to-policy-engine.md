---
name: Upgrade-Direction Degradation — Prose Guard Floor, Policy-Engine Ceiling
summary: 'In a portable system contract, most degradation paths describe how a row weakens on a lesser host. One row inverts the direction: its floor is guards carried as prose (in the always-on file and
  skill bodies, with the install report naming which guards are prose-only), and a host WITH native permission gates may replace prose guards with real enforcement — explicitly allowed to exceed the source,
  never the reverse. CareerBuddy''s wiring row 08 is the pattern''s production instance, with a concrete enforcement ladder across Cursor hooks, Codex execpolicy, and Claude Code PreToolUse hooks.'
implementation_notes: 'Queued by CareerBuddy explicitly as a corpus contribution to this engine. The engine runs the same asymmetry today without declaring it: most guards are prose (governance rules, human-gate
  constraints) while a few are enforced (pre-commit hook for frontmatter/line-budget; bypassPermissions removes a whole enforcement layer by ruling). A portable-governance-kernel wiring row for permissioning
  should state the prose floor, name which guards are prose-only on the current harness, and mark the row upgrade-direction so richer hosts harden rather than merely match. Monotonicity rule to keep: upgrades
  allowed, downgrades never.'
category: Governance
evidence_strength: Medium (practitioner-documented, production system; enforcement ladder verified against three platform adapters' live-doc surveys)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-improve-backlog-corpus-contributions.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: machine-readable-system-contract-with-wiring-rows.md
  rel: extends
- file: policy-as-data-machine-readable-constraints.md
  rel: same-problem
- file: runtime-governance-gap-buildtime-to-production.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
tags:
- enforcement
- prose-guards
- policy-engine
- degradation-paths
- permissioning
---
# Upgrade-Direction Degradation — Prose Guard Floor, Policy-Engine Ceiling

## What It Is

A degradation-path pattern for the permissioning row of a portable agent-system
contract. Seven of CareerBuddy's eight wiring rows degrade downward (native mechanism →
documented prose fallback). Row 08 (`operational-quirks`, capability
`native-permission-enforcement`) is "the one row whose degradation runs in the *upgrade*
direction": absent native gates, every guard is carried as prose in the always-on file
and skill bodies and the install report names which guards are prose-only; "a host WITH
native gates may replace prose guards with enforcement (may exceed the source)." The
receiving-agent protocol makes the monotonicity explicit: "you may *upgrade* the guard
to enforcement; record the upgrade. Never the reverse."

## Why It Matters

Plain English: prose guards ("never push without approval") are the weakest enforcement
that exists — they depend on the model reading and honoring them. But they are also the
only universally portable form. This pattern resolves the tension by declaring prose as
the contract's floor, not its spec: a poor host runs honestly (it *says* which guards
are prose-only), and a rich host is invited — contractually — to swap prose for a policy
engine. Without the upgrade direction stated, ports to capable platforms faithfully
reproduce the weakest form of every guard, wasting enforcement the host already offers.

## How It Works

- **The floor (canon 08, "permissioning honesty"):** where the platform lacks native
  enforcement, the equivalent guard is carried as prose in the always-on file and skill
  bodies — "and the install report must say which guards are prose-only on this
  platform." Row 08's invariant bakes that reporting in.
- **The ceiling, per platform (from the staged adapters' live-doc surveys):**
  - *Cursor:* `.cursor/hooks.json` `beforeShellExecution` with a matcher on
    `git push|gh pr create|rm -rf` etc. (allow/deny/ask + `failClosed: true`) "makes the
    side-effect guard *enforced*"; `beforeReadFile` adds PII-file blocking.
  - *Codex:* execpolicy rules (Starlark, testable via `codex execpolicy check`) give
    deterministic command gating — e.g. `forbidden` on `git push`.
  - *Claude Code:* PreToolUse hooks are "the docs' designated enforcement layer —
    rules/CLAUDE.md are context, not enforcement."
  - *VS Code Copilot (the source harness):* skill *invocation* gates are native
    (`disable-model-invocation`), but *tool* gates are absent — the side-effect guard
    stays prose there, which is exactly why the source's declared form is prose.
- **Vocabulary encoding:** the wiring-vocabulary entry for
  `native-permission-enforcement` carries the direction in the controlled vocabulary
  itself ("a policy-engine host can exceed the source's prose guards"), design-gate
  cited to a policy-as-data finding from this engine's corpus.
- **Honesty coupling:** the contract's `trust.declared_absences` opens with "No enforced
  permission system (prose-only guards; see wiring row 08)" and the containment menu
  points hosts at the upgrade — degradation, absence declaration, and hardening path all
  reference the same row.

## How It Could Fail

An upgrade that changes semantics (a deny-matcher narrower than the prose rule it
replaces) silently weakens the guard while claiming to strengthen it — the row's
invariant, not the mechanism, must stay the acceptance test. Recorded upgrades create
platform-drift risk: the enforced form lives in host config (hooks.json, execpolicy)
outside the portable repo, so a re-install that skips the install report re-degrades to
prose without noticing. And the pattern tempts blanket enforcement; the production
instance keeps the enforced set small (push/deploy/delete side effects), leaving
judgment-shaped guards as prose.
