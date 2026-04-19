---
name: ETHOS.md Philosophical Constitution
summary: 'Philosophical principles injected into every skill: ''Boil the Lake'' (completeness is cheap with AI), ''Search Before Building'' (check 3 layers before creating), ''User Sovereignty'' (AI recommends,
  users decide). Distinct from SOUL.md (identity) and CLAUDE.md (rules).'
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: soul-md-agent-constitution-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# ETHOS.md Philosophical Constitution

## What It Is
gstack's ETHOS.md defines three philosophical principles injected into every skill: "Boil the Lake" (completeness is cheap with AI — do more, not less), "Search Before Building" (check 3 layers of existing knowledge before creating anything new), and "User Sovereignty" (AI recommends, users decide — never take autonomous action). These are not rules or constraints — they are philosophical stances that shape judgment. This is distinct from SOUL.md (who you are — identity and personality) and CLAUDE.md (what the rules are — project constraints).

## Why It Matters
Rules tell agents what to do. Identity tells agents who they are. Philosophy tells agents HOW to think — shaping judgment calls that rules cannot anticipate. "Completeness is cheap" reframes the AI cost equation in a way that changes behavior across all skills: when in doubt, do more rather than less. This is a fundamentally different lever than constraints or identity.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Different from SOUL.md (who you are) and AGENTS.md (what the rules are). ETHOS.md is HOW you think — philosophical principles that guide judgment calls. "Completeness is cheap" reframes the AI cost equation in a way that changes behavior across all skills.

## Potential Alternatives
Embedding philosophy into CLAUDE.md alongside rules. Per-skill behavioral tuning instead of universal principles. No philosophical layer — relying on model defaults and explicit rules only.

## Potential Improvements
Situational philosophy (different principles for different task types). Philosophy versioning as organizational values evolve. Measuring philosophical adherence in eval systems.

## Potential Failure Modes
"Boil the Lake" conflicting with budget constraints (completeness is cheap until it isn't). Philosophical principles being too abstract to influence concrete decisions. Philosophy layer adding token overhead without measurable behavioral improvement. Conflict between ETHOS.md principles and CLAUDE.md rules with no clear precedence.
