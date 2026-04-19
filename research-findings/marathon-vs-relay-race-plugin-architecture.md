---
notion_id: 32b1e08b-9b34-814d-9ac0-c0b595718b96
name: Marathon vs. Relay-Race Plugin Architecture
summary: PAUL operates as a single, persistent sequential worker (marathon) versus GSD's relay-race model of spinning up fresh context windows per phase. This architectural choice determines context continuity,
  token cost, and error accumulation across a project build.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
- anthropic-effective-harnesses-long-running-agents.md
proposals: null
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: agent-management-tool-landscape-2026.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Marathon vs. Relay-Race Plugin Architecture

## What It Is
PAUL is a Claude Code plugin that maintains a single continuous conversation/worker across all project phases. GSD (Get Shit Done) spins up new context windows per phase in a relay-race pattern. PAUL's approach means human interruptions, corrections, or feedback do not cause the active worker to vanish — the agent stays informed and continues from where it left off.

## Why It Matters
With GSD's relay model, resuming a project triggers a full context reload, losing roughly 70% of accumulated project context per phase transition. Any human input into GSD causes an implicit restart. PAUL avoids this by treating the build as a marathon — it costs more per token but never loses state, which is critical for client-delivery quality.

## Why People Are Using It
Agencies and developers delivering production-grade SaaS applications prefer PAUL because it trades raw build speed for verifiable correctness. The author notes he uses PAUL for all client deliveries specifically because the cost of a broken app exceeds any token savings.

## Potential Alternatives
GSD for independent, unconnected feature branches or large-scale parallelizable work; manual multi-session handoff documents; Claude's built-in /compact command between sessions.

## Potential Improvements
A hybrid mode that uses PAUL's sequential fidelity for integration-heavy phases and GSD's parallelism for truly independent file operations would combine both strengths.

## Potential Failure Modes
PAUL is slower — for projects with strict time constraints or many independent modules, the sequential lock becomes a bottleneck. If the single worker accumulates context rot deep into a session, quality can still degrade without a forced context reset.

---

## April 2026 Update

**Skills 2.0 Benchmark mode** provides objective measurement infrastructure for deciding which architecture a skill should use:
- Relay-race (handoff between discrete skills) now has measurable Pass Rate, Time, and Token metrics vs. marathon (single-session continuous agent)
- The Benchmark mode comparison answers the previously subjective "which is better for this task?" with objective data
- Use Benchmark mode to run the same workflow as both marathon and relay-race, then compare metrics across all three dimensions

**MCP Apps adds a new architectural option:** Skills that return interactive UIs rather than text outputs. A skill that previously needed a marathon agent to collect user feedback mid-run can now return an MCP App form and resume after user interaction — a hybrid pattern not previously possible.

**Practical implication:** The relay-race model is now more capable (Skills 2.0 orchestrates context hand-off cleanly) and the marathon model is now measurable (Benchmark mode shows token cost vs. quality gain). The choice is now data-driven, not architectural preference.

**Source:** https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026
