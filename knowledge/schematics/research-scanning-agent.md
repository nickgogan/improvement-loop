---
title: "Research-Scanning Agent"
id: "research-scanning-agent"
type: "schematic"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
altitude: "middle"
maturity: "seed"
grounded_in:
  - "autoresearch-loop-autonomous-metric-driven"
  - "karpathy-autoresearch-self-improvement-loop"
  - "bounded-tiered-memory-inference-driven-curation"
  - "context-curation-over-context-stuffing"
  - "agent-self-reporting-unreliability-independent-eval"
composed_of:
  - "systems/improvement-loop/.claude/skills/research-loop"
  - "systems/improvement-loop/.claude/skills/source-triage"
  - "systems/improvement-loop/.claude/skills/identify-artifacts"
  - "systems/improvement-loop/research-findings"
source_dd:
  - "DD-107"
tags:
  - "schematic"
  - "research"
aliases:
  - "Research Scanner"
  - "Periodic Research Agent"
---

# Research-Scanning Agent

> A single persistent agent that scans a moving knowledge frontier on a cadence, curates a
> bounded knowledge base of findings, and hands every result to a human gate before it counts.

This schematic captures the engine's own bottom-altitude operation (the Researcher running
`/research-loop`) as a reusable configuration — the recurring shape of "keep a curated KB current
against a fast-moving external domain."

## Demand

| Axis | Value |
|------|-------|
| **Function** | research |
| **Scope / lifespan** | personal-persistent (a standing capability, not a one-off task) |
| **Non-functionals** | data boundary: local-first KB, public sources only; reliability: tolerant — a missed source is recoverable next scan; autonomy need: medium (runs the scan unattended, gates on output); cost: bounded by scan cadence |

Reach for this when a single owner needs to stay current on a domain that changes faster than
they can read, and wants the knowledge captured as durable structured files rather than as
ephemeral chat — with a human deciding what is actually worth keeping.

## Configuration

### Capability + memory core

Scan a defined frontier (sources, watched libraries, blogs, transcripts, arXiv) across a fixed
**dimension registry**; extract one canonical finding per pattern; link findings to sources and
authorities. **Memory is the KB itself** — `research-findings/`, `research-sources/`,
`research-authorities/` — a *bounded, curated* store, not an ever-growing dump: new sources
update existing findings rather than spawn duplicates, and curation (crosslink, dimension
rebalance, priority reassessment) keeps signal density high. This curated-KB core is the reusable
part; other research schematics can swap the frontier and dimensions but keep this core.

### Coordination / architecture

Single agent (the Researcher persona) owns intake. It may fan out **stateless** parallel
subagents for source triage (each scores one source for finding density), but synthesis back into
the canonical KB is single-threaded to preserve one-finding-per-pattern.

### Autonomy

**collaborator** — the agent runs the scan and drafts findings unattended, but it does not
self-promote: every stage boundary carries a human gate (DD-29). It works *alongside* the owner
(proposes priorities and evidence strength), it does not act *for* them at the promotion line.

### Deployment surface

Claude Code harness (this engine). Skills are invoked in-session; the KB is local markdown in the
Obsidian vault. No external runtime; no provider-API hosting.

## Evaluation & feedback

- **How it's evaluated:** finding quality is judged on two recorded axes — `evidence_strength`
  and `priority` — assigned at extraction, then **independently reviewed by the human gate**. The
  agent never certifies its own output as good (per
  [[agent-self-reporting-unreliability-independent-eval]]); Nick adjudicates at the finding-review
  boundary.
- **Feedback mechanism:** **human + internal.** Human: Nick reprioritizes and flags gaps, which
  steer the next scan. Internal: `/reassess-priorities`, `/finding-crosslink`, and
  `/dimension-rebalance` re-curate the KB as evidence accumulates — the self-improvement loop that
  keeps the store bounded and current rather than letting it rot.

## Grounding & composition

- **`grounded_in`** — the evidence:
  - [[autoresearch-loop-autonomous-metric-driven]] — the hypothesis→measure→keep/discard loop with
    a persistent learning store; the shape of a metric-driven scanning agent.
  - [[karpathy-autoresearch-self-improvement-loop]] — the two-layer (skill + main) autonomous
    improvement loop that motivates the internal re-curation feedback.
  - [[bounded-tiered-memory-inference-driven-curation]] — memory under a hard ceiling with
    inference-driven writes; grounds the "bounded, curated KB" core over an unbounded dump.
  - [[context-curation-over-context-stuffing]] — curation beats accumulation for quality; grounds
    one-finding-per-pattern and the re-curation skills.
  - [[agent-self-reporting-unreliability-independent-eval]] — agents over-report success; grounds
    the independent human gate on finding quality.
- **`composed_of`** — what it's built from:
  - `/research-loop` — the scan + extraction procedure (capability core).
  - `/source-triage` — the parallel stateless triage subagents.
  - `/identify-artifacts` — the downstream classification handoff (where findings exit this schematic).
  - `research-findings/` (+ sources, authorities) — the curated-KB memory.

## Risk & maturity

- **Known risks / failure modes:** (1) duplicate findings if the one-canonical-finding discipline
  slips; (2) KB rot if the internal re-curation feedback isn't run on cadence; (3) a stale
  dimension registry biasing the scan toward yesterday's questions.
- **Maturity:** seed — the configuration is the engine's lived operation, so the *shape* is real,
  but it has not yet been instantiated for a *second* domain, which is the test of the reusable core.
- **Revisit when:** a second research-scanning instance is stood up (validates the core), or any
  `grounded_in` finding moves (re-check the eval/feedback layer).
