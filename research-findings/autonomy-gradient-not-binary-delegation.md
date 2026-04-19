---
name: Autonomy Gradient (Not Binary Delegation)
summary: 'Agent autonomy is not binary (autonomous vs. human-required). Huryn''s Intent Engineering Framework defines four levels: Full autonomy -> Guarded (act then report) -> Proposal-first (propose then
  wait) -> Human-required. Assignment is based on blast radius and reversibility of the decision, not task complexity. This maps to a concrete decision classification system.'
implementation_notes: MetaSystem currently uses a binary human gate (DD-29). This finding suggests refining to a four-level gradient where routine, reversible decisions (e.g., file formatting, index updates)
  get full autonomy while irreversible decisions (e.g., schema changes, DD creation) require human-required gate. The middle tiers (guarded, proposal-first) would reduce bottleneck without sacrificing safety.
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- intent-engineering-framework-for-ai-agents-product.md
- hitl-agentic-ai-strataio-2026-guide.md
- anthropic-trustworthy-agents-in-practice.md
related_findings:
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: stop-rules-as-execution-boundaries.md
  rel: same-problem
- file: intent-engineering-framework-seven-part-agent-inten.md
  rel: same-problem
- file: trust-calibration-progressive-autonomy-ramp.md
  rel: extended-by
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: same-problem
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: enabled-by
- file: health-metrics-vs-hard-constraints-distinction.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: "synthesized"
consumed_by:
  - "writing-agent-specifications.md"
---
## What It Is

A decision classification framework from Pawel Huryn's Intent Engineering Framework. Agent autonomy should be assigned per decision type, not per agent or per task.

**Four autonomy levels:**
1. **Full autonomy**: Agent decides and acts. No notification required. Use for low-blast-radius, easily reversible decisions.
2. **Guarded**: Agent decides and acts, then reports what it did. Use for medium-blast-radius decisions where speed matters but visibility is needed.
3. **Proposal-first**: Agent proposes a decision, waits for approval, then acts. Use for high-blast-radius but time-insensitive decisions.
4. **Human-required**: Agent cannot act. Must escalate to a human. Use for irreversible, high-blast-radius decisions.

**Assignment criteria:**
- **Blast radius**: How many systems, users, or processes are affected by a wrong decision?
- **Reversibility**: Can the decision be undone easily? A renamed variable is fully reversible; a deployed schema migration is not.

This maps to a 2x2 matrix: low blast radius + reversible = full autonomy; high blast radius + irreversible = human-required; the other two quadrants map to guarded and proposal-first.

## Why It Matters

Binary autonomy (do everything vs. ask for everything) creates either unsafe agents or bottlenecked workflows. The gradient allows each decision to be gated at the appropriate level, maximizing agent throughput on safe decisions while preserving human oversight where it matters. Multiple independent sources (Huryn, Carlisia Campos, industrial automation researchers) converge on this four-level model.

## Why People Are Using It

Huryn's framework has been cited across multiple practitioner blogs and a YouTube architecture talk. The pattern maps directly to existing software engineering concepts: feature flags (reversible), database migrations (irreversible), logging (full autonomy), production deployments (human-required). Nate B Jones arrives at the same conclusion independently via production OpenClaw deployments, making "scope authority deliberately" his 5th commandment for agent deployment: define what the agent can and cannot do, guardrail it explicitly, and never give free access to everything. Jones specifically calls out `dangerously-skip-permissions` as a pattern that "may make it faster on day one" but creates real security and reliability failures by day 30.

## Potential Improvements

Could be combined with runtime monitoring: start an agent at a lower autonomy level, then promote it as confidence builds based on track record. An agent that consistently makes good guarded decisions could be promoted to full autonomy for that decision type.

## Potential Failure Modes

Misclassification of blast radius leads to under- or over-gating. Agents may not recognize when a decision's blast radius has changed (e.g., a routine file edit that happens to break a critical dependency). The gradient requires per-decision-type configuration, which is more complex than binary gating.

## Anthropic Implementation (April 2026 — Tier 1)
Anthropic's "Trustworthy agents in practice" confirms this pattern in production across Claude.ai, Claude Desktop, and Claude Code. Their implementation maps directly to the autonomy gradient: users select per-tool permission tiers (always allow / needs approval / block). Example: auto-read calendar but require approval for sending email invites. Claude Code's Plan Mode shifts oversight from individual steps to strategy-level review — the agent shows its full intended plan upfront for review/edit/approval, reducing friction from repeated per-action prompts. This is the "Proposal-first" tier from Huryn's framework, implemented at Anthropic scale. Subagents (parallel Claudes for task parts) introduce coordination complexity that Anthropic is actively exploring for oversight patterns.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[autonomy-gradient-not-binary-delegation]] in `extracts/patterns/`
