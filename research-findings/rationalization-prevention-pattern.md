---
name: Rationalization Prevention Pattern
summary: Superpowers includes explicit tables of common LLM rationalizations with rebuttals ('I am confident' → 'Confidence != evidence') and Red Flags tables of thoughts that mean STOP — anticipating and
  blocking specific ways LLMs evade constraints. No other analyzed repo addresses rationalization as a governance concern.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Rationalization Prevention Pattern

## What It Is
Every discipline-enforcing skill in Superpowers includes a table of common LLM rationalizations paired with rebuttals. Examples: "I'm confident" → "Confidence is not evidence," "Just this once" → "No exceptions," "It's a simple change" → "Simple changes cause complex bugs." Additionally, each skill includes a "Red Flags" table listing specific thoughts that should trigger an immediate STOP (e.g., "I already know what this code does" → STOP and read it). This is psychological enforcement — anticipating the specific internal reasoning patterns that lead LLMs to bypass constraints, and pre-loading counterarguments.

## Why It Matters
This is a second-order governance innovation. First-order governance defines rules. Second-order governance anticipates how the governed entity will try to circumvent those rules and blocks the circumvention paths. Most agent systems define rules and hope agents follow them. GSD uses structural enforcement (gates, tool allowlists) to make rule-breaking mechanically difficult. Superpowers takes a different approach: it makes rule-breaking psychologically difficult by pre-empting the rationalization narratives that LLMs generate when they are about to violate constraints.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. Cross-repo context from [[cross-repo-comparison]]. Across seven analyzed repos (GSD, BMAD, OpenClaw, Paperclip, gstack, mem0, Superpowers), Superpowers is the only one that addresses LLM rationalization as an explicit governance concern. The approach is grounded in Meincke et al. (2025) persuasion research applied to LLM behavior.

## Potential Alternatives
Structural enforcement via gates and tool allowlists (GSD) — makes rule-breaking mechanically impossible rather than psychologically difficult. Output validation that catches violations after the fact. Constitutional AI training that embeds constraints at the model level. Simple rule repetition (saying the rule multiple times in different places). Human-in-the-loop review as the sole safeguard.

## Potential Improvements
Combining rationalization prevention (psychological) with structural enforcement (mechanical) for defense-in-depth. Dynamic rationalization tables that update based on observed failure patterns in production. Model-specific rationalization profiles — different models may have different characteristic evasion patterns. Logging when rationalization rebuttals are triggered, providing observability into near-misses.

## Potential Failure Modes
The rationalization tables are static and may not cover novel evasion patterns that emerge with model updates. If the model does not engage in explicit chain-of-thought reasoning, the rebuttals may not activate (they target the reasoning process). Overly aggressive red flags could cause false positives — the agent stops when it should proceed. The approach assumes LLMs reason in ways analogous to human rationalization, which may not hold for all model architectures.
