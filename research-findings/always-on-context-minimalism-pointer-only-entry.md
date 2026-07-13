---
name: 'Always-On Context Minimalism — Minimal Entry File, Pointer-Only State'
summary: 'The one instruction file the harness injects into every request carries only the irreducible minimum — mission, load order, standing guards, skill pointers — because it is paid for on every request. Volatile state (active user, targets, status) appears pointer-only, never restated. A wake-up idiom lets a bare control-file mention ("PROGRESS", "continue") resolve directly to the recorded next unit of work without recital.'
implementation_notes: 'The engine already practices pieces of this (wake-up idiom, no-hardcoded-counts rule, lean CLAUDE.md); the CareerBuddy formulation adds the explicit economy rule as a design law — "always-on = minimal; everything else loads on demand" — plus the discipline that the entry file names active state pointer-only. Adoptable as an audit criterion for /assess-agent and /simplify-context: does the always-on surface restate anything that lives elsewhere?'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
related_findings:
- file: rules-layer-collapse-monolithic-context-counter-signal.md
  rel: contradicts
pipeline_status: raw
consumed_by: []
tags:
- always-on-instructions
- context-economy
- pointer-discipline
- wake-up-idiom
---
# Always-On Context Minimalism — Minimal Entry File, Pointer-Only State

## What It Is

A design law for the one instruction file a harness injects unconditionally into every
agent request (CLAUDE.md, copilot-instructions.md, AGENTS.md — whatever the platform's
guaranteed entry point is): it carries the irreducible minimum and nothing else, because
its token cost is paid on every single request. Canon contents: mission statement, layer
split, active-state designation *as a pointer*, cold-start load order, side-effect guard,
maintenance guard, and skill pointers — never skill bodies, never restated facts.

## Why It Matters

Plain English: the always-on file is the most expensive real estate in an agentic system
— every word in it taxes every request forever. Systems drift toward stuffing it with
facts that then go stale and leak. The rule "always-on = minimal; everything else loads
on demand" plus "pointers, never copies" bounds both the token cost and the staleness
risk at the same time. It is the entry-file counterpart of a single-source-of-truth rule.

## How It Works

- **Economy rule as canon:** anything not wired into the entry file may simply never
  load, so the file carries the minimum that guarantees everything else *can* load —
  mission, load order, standing guards — and delegates the rest to on-demand surfaces.
- **Pointer-only active state:** the file names the active `{user-id}` and routes to
  that user's scope; it never restates user facts, targets, or status — "those go stale
  and leak." Volatile facts live in exactly one surface and are pointed to everywhere
  else (pointer-discipline is a first-class process constraint in the system contract).
- **Wake-up idiom as harness behavior, not a skill trigger:** a bare control-file
  mention ("PROGRESS", "continue") means read the named control file (default: the root
  PROGRESS.md session bridge) and check the recorded next unit of work. Clear and
  unambiguous → proceed directly, no status recital or prompting; ambiguous or multiple
  candidates → surface and let the human decide. Proceeding never bypasses standing
  gates.
- **Standing guards carried inline:** a side-effect guard (local reversible actions
  free; lasting external effects human-approved; governance edits deliberate) and a
  maintenance guard (no volatile metrics — counts, sizes — in tracked docs; durable
  rules only).
- **Skill pointers only:** the file names the central mission skill(s) and the skills
  index; skill bodies never get pasted in.
- Platform quirk guards may live here too, but only when they can fire on any request
  and only on platforms where enforcement is prose (see the operational-quirks
  discipline).

## How It Could Fail

The minimalism rule requires an enforcement mechanism (audit or review gate) or the file
regrows — every incident tempts a new always-on paragraph. Pointer-only state assumes the
pointed-to surface is reliably loadable; a broken pointer is worse than a stale copy
because nothing visibly fails. The wake-up idiom needs the "ambiguous → ask" branch, or
it becomes an autonomy bypass.
