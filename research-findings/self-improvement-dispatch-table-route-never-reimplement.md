---
name: Self-Improvement Dispatch Table — Classify by Owning Surface, Route, Never Re-Implement
summary: 'The self-improvement skill is an umbrella dispatcher: it owns only the observation loop (capture, retro, promotion of internal lessons) and routes every other finding class to the skill that owns
  it via an explicit dispatch table. Classification keys on owning surface, not topic. Unknown classes become internal lessons with the operator flagged — the agent never invents a new route. Recommending
  a route is autonomous; invoking the routed skill asks first.'
implementation_notes: How this could apply to the MetaSystem engine — Phase 2 of its restructure program will size a second-brain-for-operations against this store model; IB-172 (layered memory architecture)
  is the related backlog item. The engine already routes retired-SL learnings three ways (DD / knowledge / IB); this pattern is that rule generalized into a maintained table with per-class signals and a
  named residual owner, letting one intake surface feed many specialized loops without scope creep.
category: Orchestration
evidence_strength: Medium (practitioner-documented, single production system with live store evidence)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-self-improve.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: synthesized
consumed_by:
- production-agent-execution.md
tags:
- dispatch-table
- routing
- skill-boundaries
- self-improvement
---

# Self-Improvement Dispatch Table — Classify, Route, Never Re-Implement

## Why It Matters

A retro over real sessions surfaces findings of many kinds — doc drift, stale platform claims, eval material, genuine operational lessons. If the self-improvement loop tries to fix all of them, it duplicates every other maintenance skill and its scope grows without bound. CareerBuddy's answer is a dispatch table: the loop keeps only what it owns and routes the rest, "never re-implemented locally — not even 'just this once, partially.'" This is how one observation surface feeds many specialized loops without becoming a monolith.

## What It Is

A reference table in the skill package with one row per finding class. Each row carries three things: **signals** (how to recognize the class), **route** (which skill owns the work), and — the subtle part — **what this skill still does** (its residual duty even when routing). CareerBuddy's seven classes: corpus drift, platform-doc drift, doc-surface drift, eval material at threshold, session-state drift, large skill rewrite, and the residual — internal operational lesson, which the loop owns end-to-end.

## How It Works

- **Owning surface decides, not topic.** A lesson *about* the meta-skill's guidance that came from an internal run is an internal lesson (owning surface: that skill's file, promoted through the normal gate); "corpus drift" applies only when the external corpus itself changed. Classification asks "which file, if edited, prevents recurrence?" — not "what is this about?"
- **When two classes fit, route the drift and keep the lesson.** A stale platform claim that also wasted session tokens splits: staleness routes to the refresher; "cache this fact" lands as an internal lesson. One observation, two dispositions.
- **Unknown class → internal lesson with the operator flagged.** "Never invent a new route; the table is amended by editing this file through the normal promotion gate" — the routing topology itself is governance, changed only via the human-gated pipeline.
- **Routing is two-tier autonomous.** *Recommending* a route (a manifest row in the retro report) is autonomous; *invoking* the routed skill "starts a new unit of work — ask first."
- **Residual duties survive routing.** Even for routed classes the loop records the manifest row and, for eval material, owns the raw harvest ("owns the material, never the method") — routing sheds the fix, not the record.
- **Large-fix escape hatch.** A promoted lesson demanding restructuring becomes the proposal "dispatch an improve-mode run" rather than a direct edit — the table bounds even the loop's own fixes to minimal-edit size.
- **Live evidence:** the retro manifest (`retro-latest.md`) shows the table in use — 10 findings in one run classified across internal lessons (landed L-12, L-13), eval material (harvested), store hygiene, and operator-awareness items (surfaced, not actioned), each row carrying an evidence trace; "a manifest row with an empty Evidence cell is invalid."

## How It Could Fail

- The table is only as good as its class boundaries — CareerBuddy's own eval loop found trigger-surface confusion born exactly at skill-boundary edits (its L-16), and dispatch tables inherit the same seam risk.
- Residual-duty rows quietly grow: "what this skill still does" is where scope creep hides if not audited.
- A stale table routes to retired skills; because amendments go through the promotion gate, the table lags roster changes by at least one gated cycle.
