---
name: Root Context-File Edit Guard
summary: 'A standing rule written INTO the root router file itself: the agent must ask before

  editing the root CLAUDE.md. Everything else in the structure depends on that one

  file — if it drifts silently (agent "helpfully" appending rules, absorbing detail

  that belongs in pointed-to files), the whole routing system quietly degrades.

  Every change to the front door is approved on purpose, with intention.'
implementation_notes: 'Trivially adoptable, Nick-gated: one guard line in the workspace/engine CLAUDE.md

  ("ask before editing this file"). Complements the existing anti-bloat findings —

  they say the router must stay thin; this is the enforcement mechanism that keeps

  agents from fattening it unattended. Note the engine already gates CLAUDE.md changes

  socially (agent-rules; no agent messages authorize config changes); this makes the

  gate self-describing inside the artifact.'
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- General
- IL (context governance)
adopted_in:
- Improvement Loop
sources:
- the-folder-structure-that-makes-ai-build-better-software.md
related_findings:
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: extends
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
- rules/ask-before-editing-root-context-file.md
---

## What It Is

A one-line governance mechanism against router rot: "make this a standing rule in the
router itself. The number one rule at the top: the AI asks you before it edits the
root claude.md file. That one file is what everything else depends on. It's sacred.
You don't let it drift silently. You approve every change on purpose, with intention."

The threat model is the router's natural growth pressure — "every new rule will feel
like it belongs in the front door. It does not." Agents (and humans) incrementally
promote detail into the root file until it becomes a knowledge dump the AI half-reads,
and the degradation is silent because each individual addition looked reasonable.

## Why It Matters

The root context file is the single highest-leverage artifact in a file-structured
agent setup and the one most edited by the agent itself. A human gate on exactly that
file converts an invisible drift channel into an explicit review point — cheap to
implement (the rule lives in the file it protects, so every session loads it) and
proportionate (only the root is gated; pointed-to files stay freely editable).

## Why People Are Using It

Named by the source as the counter to "the most common way these setups collapse."
Consistent with the KB's instruction-bloat evidence (context files degrade agent
behavior as they fatten) — this is the enforcement half of the thin-router principle.

## Potential Alternatives

VCS-level protection (root file changes require PR review) — stronger but heavier,
and invisible to the agent in-session. Hooks that block writes to the root file
programmatically rather than by instruction.

## Potential Improvements

Extend the guard to a small set of named load-bearing files (root router + settings +
governance rules). Pair with a periodic router audit (is anything in the root that a
pointed-to file should hold?).

## Potential Failure Modes

Instruction-level guards are soft — an agent can fail to honor the rule it was asked
to read, so high-stakes setups still want a mechanical backstop. Over-extension (asking
before editing *any* file) recreates prompt-fatigue and trains reflexive approval.

## Extraction Note — 2026-07-19
Extracted as **rule**: [[ask-before-editing-root-context-file]] in `extracts/rules/`
