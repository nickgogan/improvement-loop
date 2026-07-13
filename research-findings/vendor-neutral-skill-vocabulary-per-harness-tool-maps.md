---
name: "Vendor-Neutral Skill Vocabulary with Per-Harness Tool Maps"
summary: |-
  Plain English: write skill bodies in harness-neutral action language — "dispatch a
  subagent," "your instructions file," "your agent" — and quarantine every
  harness-specific detail into per-harness tool-map reference files, deleting any map
  file with nothing harness-specific left. Superpowers v6.0.0/v6.1.0 rewrote its skill
  suite out of Claude Code's dialect ("use the Task tool" → "dispatch a subagent";
  "Claude Search Optimization" → "Skill Discovery Optimization"); per-harness
  references under `using-superpowers/references/` map actions to concrete tools
  (e.g., Codex `spawn_agent`/`wait_agent`), with environment detection and sandbox
  caveats. The layer is what let one skill set add Kimi Code, Pi, and Antigravity and
  drop Gemini (Google EOL) without touching a single skill body. Behavior evals moved
  to a separate repo that drives real sessions on multiple harnesses.
implementation_notes: |-
  Directly relevant to DD-92's universal-vocabulary requirement and /meta-skill-author's
  porting concern — the engine already mandates universal vocabulary in ContextSpecs;
  this finding supplies the complementary mechanic (per-harness tool maps as the ONLY
  home for harness dialect, with a delete-when-empty rule that keeps the maps honest).
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "shared-instructions-multi-harness-plugin-wrappers.md"
    rel: "same-problem"
  - file: "skills-portability-across-sdk-and-framework-boundaries.md"
    rel: "extends"
  - file: "harness-adaptation-protocol-graded-capability-intersection.md"
    rel: "same-problem"
  - file: "cross-platform-context-file-strategy.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "tool-integration"
  - "portability"
  - "vendor-neutrality"
---

# Vendor-Neutral Skill Vocabulary with Per-Harness Tool Maps

## What It Is

A two-layer portability architecture for behavioral content:

1. **Neutral vocabulary in skill bodies.** Skills speak in actions, not tool names:
   "dispatch a subagent" (not "use the Task tool"), "your instructions file" (not
   "CLAUDE.md"), "your agent" (not "Claude"). Even the meta-skill's discovery
   technique was renamed from "Claude Search Optimization" to "Skill Discovery
   Optimization."
2. **Per-harness tool maps as the dialect quarantine.** Reference files (one per
   harness) map each abstract action to the harness's concrete tool, with environment
   detection and sandbox caveats. Two hygiene rules keep the layer honest: a map file
   whose harness-specific content evaporates is deleted outright (v6.1.0 pruned the
   claude-code/copilot/gemini maps), and harness bootstrap mechanisms (hook / native
   trigger / extension) stay outside skill bodies entirely.

Demonstrated payoff: three harnesses added (Kimi Code, Pi, Antigravity) and one
removed (Gemini, vendor EOL) with zero edits to skill bodies. Behavior verification
moved with it — a separate evals repo drives real sessions per harness.

## Why It Matters

Skill suites rot into their birth harness one tool-name at a time; each mention is a
porting landmine. Separating *what to do* (portable, in the skill) from *how this
harness does it* (per-harness map) is the same interface/implementation split code
solved decades ago, applied to instruction prose — and the harness add/remove evidence
shows it working under real churn, including a vendor dying. For any system exporting
skills beyond one harness, the delete-when-empty rule is the subtle keeper: it
prevents the maps from becoming a second, stale copy of general guidance.

## Why People Are Using It

Applied suite-wide in Superpowers v6.0.0/v6.1.0 across seven harness integrations;
motivated by real multi-harness distribution rather than speculative portability.
Source: Observed in [superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] for structural details.

## Potential Alternatives

- **Thin per-harness wrappers around shared instructions** (MemPalace) — delegation at
  the packaging layer; complementary, but skill *bodies* can still carry dialect.
- **Per-harness skill forks** — full control per platform, N-way maintenance.
- **Graded capability-intersection install protocols** — the heavier machinery for
  when harness *capabilities*, not just tool names, differ.

## Potential Improvements

- Dialect linting: scan skill bodies for known harness-specific tokens (tool names,
  file names) as a CI gate.
- A shared cross-project action vocabulary, so tool maps compose across skill suites
  rather than per-suite.

## Potential Failure Modes

- **Abstraction mismatch** — some actions don't exist on some harnesses; neutral
  vocabulary can paper over a capability gap the tool map then has to refuse.
- **Map staleness** — harness tool APIs churn faster than skill bodies; the maps
  concentrate the maintenance but don't remove it.
- **Vocabulary bloat** — action language invented ad hoc per skill defeats the layer;
  the vocabulary itself needs curation.
