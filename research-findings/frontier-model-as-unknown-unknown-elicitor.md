---
name: "Frontier Model as Unknown-Unknown Elicitor"
summary: |-
  Plain English: the scarce resource is no longer model intelligence but the orchestrator's
  awareness of what they don't know — so spend frontier tokens surfacing blind spots, not
  drafting plans. Now first-party: Anthropic's "A field guide to Claude Fable 5: Finding
  your unknowns" (Thariq Shihipar, Claude Code team, 2026-07-06) states the thesis
  directly — work quality is bottlenecked by the human's ability to clarify unknowns, not
  by model capability, and reducing unknowns is the learnable skill of agentic coding.
  Use the frontier model to elicit unknown-knowns (tacit knowledge you assume is shared
  but isn't stated) and unknown-unknowns (areas you didn't know were worth asking about)
  before committing to any plan or spec — the guide's literal recommended phrase is a
  "blind spot pass".
implementation_notes: |-
  Primary source ingested 2026-07-12 (session 136), same session the secondhand video
  landed — the guide's operational technique set (phase-anchored, with exact wordings) is
  extracted separately in unknowns-reduction-phase-anchored-technique-set.md.
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "do-this-before-you-lose-access-to-fable-5.md"
  - "a-field-guide-to-claude-fable-finding-your-unknowns.md"
related_findings:
  - file: "unknowns-reduction-phase-anchored-technique-set.md"
    rel: "extended-by"
  - file: "frontier-model-as-harness-designer.md"
    rel: "extends"
  - file: "war-game-plan-format-for-executor-handoff.md"
    rel: "enables"
  - file: "advanced-elicitation-techniques-library.md"
    rel: "same-problem"
  - file: "tacit-knowledge-as-agent-delegation-barrier.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Frontier Model as Unknown-Unknown Elicitor

## What It Is

A division of the Rumsfeld quadrant across the human-model boundary. The orchestrator
handles known-knowns and known-unknowns when starting a project. The frontier model's
distinct value is in the other two quadrants: unknown-knowns — tacit knowledge the
orchestrator assumes is shared but isn't stated — and unknown-unknowns — questions the
orchestrator would never have thought to ask. The practical move is to prompt the frontier
model to pull these questions out ("guide you in areas where you would have never thought
to go") rather than asking it for a plan, which even strong models render as a linear
blue-sky sequence.

## Why It Matters

It relocates the value of frontier spend. "The fix isn't asking for better plans — it's
not asking for plans at all." For an engine whose thesis is that the strongest model
belongs at design time (harness/governance design, execution delegated down), this names
the specific design-time activity with the highest leverage: blind-spot elicitation
upstream of specification. It is the conceptual "why" behind the war-game plan format.

## Why People Are Using It

First-party confirmed (primary ingested 2026-07-12): Thariq Shihipar's field guide frames
the whole map-vs-territory gap — the map is your prompts/skills/context, the territory is
the real codebase and constraints — as unknowns to be surfaced across a four-quadrant
matrix (known knowns / known unknowns / unknown knowns / unknown unknowns), with the
blind-spot pass as the named opening move (use the literal phrases "blind spot pass" and
"unknown unknowns", plus context on who you are and what you know). Reported to have
drawn wide practitioner attention within days; adopted by practitioners rationing scarce
frontier access — elicitation output survives losing the model, plans go stale.

## Potential Improvements

Turn the elicitation into a reusable prompt scaffold (mission brief in, ranked blind-spot
questions out). The guide's instructional-balance principle is the calibration knob:
over-specification blocks pivots, under-specification forces assumptions.

## Potential Failure Modes

Elicited "unknowns" can be generic checklist filler rather than genuinely
situation-specific blind spots — quality depends on giving the model differentiated
context (the guide's own condition). Endless elicitation becomes procrastination; needs a
stop condition.
