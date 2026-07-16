---
name: "Harness Non-Portability Across Model Families (Lindy Rewrite Evidence)"
summary: |-
  Switching model families is not replacing a model call — it's replacing a whole work
  system. Lindy (Flo Crivello) publicly documented moving off Claude to a DeepSeek
  architecture: the harness had to be rewritten essentially from scratch — prompts,
  memory handling, tool-call handling, system prompt — no lift-and-shift, because
  center-of-distribution models need differently tuned harnesses than frontier ones.
  Jones: "a model can be an incredible brain in a jar — it just isn't useful to you
  without a harness." This is the strongest practitioner corroboration yet for the KB's
  skill↔model coupling findings: model choice is an architecture-level commitment, and
  the rewrite cost is why cheap-model parity alone doesn't trigger migration.
implementation_notes: |-
  Constrains every engine portability claim: "model-agnostic" substrate (skills, agents,
  the /meta-skill-author port toolchain) is a design goal that requires per-model-family
  validation and a budgeted re-tuning pass — never a free property. When evaluating a
  model switch (e.g., routing engine work to a cheaper family), cost the harness rewrite,
  not just the token delta; migration only cleared ROI for teams like Lindy whose token
  costs are the product's margin. Complements the session-level version of the same
  coupling (no-mid-session-model-switching): pin per session, commit per architecture.
category: "Agentic Systems"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "glm-5-2-is-free-and-beats-claude-on-most-work.md"
related_findings:
  - file: "no-mid-session-model-switching-subagent-handoff.md"
    rel: "extends"
  - file: "model-specific-context-file-sensitivity.md"
    rel: "extends"
  - file: "provider-adaptive-prompt-rendering.md"
    rel: "same-problem"
  - file: "skills-as-open-portable-standard.md"
    rel: "same-problem"
  - file: "center-vs-edge-of-distribution-task-classification.md"
    rel: "same-problem"
  - file: "frontier-model-as-harness-designer.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "synthesized"
consumed_by:
  - "building-agentic-systems.md"
---

## What It Is

The claim that a harness — prompts, memory architecture, tool-call handling, system
prompt, verification wiring — is coupled to a model family, so "switch to the cheaper
model" means rebuilding the work system around the new model. Primary evidence: the
Lindy team's publicly written-up migration from Claude to a DeepSeek architecture, in
which they "could not just take all of their systems for working with Claude, all of
their prompts, all of the way they handle memory, all of their tool calls, and just
automatically lift and shift... These models need their own harnesses." Jones adds
corroborating first-hand entrepreneur anecdotes: those who make the jump deal with a
different system prompt, different tool calling, and a different memory architecture
tuned to center-of-distribution models.

Surrounding vendor dynamics (same source): open-source model makers now ship their own
harnesses (GLM 5.2 released with a Codex-clone harness); OpenAI markets Codex as a
harness usable without any OpenAI model; Anthropic's Claude Tag is a team-level harness
whose passive context acquisition in Slack makes the incumbent model "impossible to rip
out" — companies end up "renting their own context back" no matter how cheap the
alternative model is.

## Why It Matters

This resolves the puzzle of why ~98%-cheaper parity models don't trigger mass migration:
the switching cost lives in the harness, not the model. For the engine it hardens the
skill↔model coupling stance already in the KB — coupling holds at every granularity
(session caches, context files, prompt rendering, and now whole-harness architecture) —
and puts a concrete price on portability ambitions: agent-agnostic/model-agnostic
substrate is precisely the "last mile" Jones calls trillion-dollar-scarce. It also
identifies who *does* migrate: teams whose token cost is their product margin (AI-as-a-
service), a useful ROI screen before any engine model-family move.

## Why People Are Using It

Lindy's migration is production-tested and publicly documented; the harness-shipping
behavior of model vendors (GLM's Codex clone, Codex-as-open-harness, Claude Tag) is
observable market confirmation that harnesses, not models, are the sticky asset.

## Potential Alternatives

- **Model-agnostic harness design up front** (Jones's own "open skills / open brain /
  open engine" direction; cf. skills-as-open-portable-standard): pay the abstraction
  cost early so the rewrite never lands at once — unproven at production scale.
- **Adapter/rendering layers** (provider-adaptive-prompt-rendering): confine the
  model-specific surface to a rendering layer; Letta demonstrates this for prompts, but
  Lindy's evidence says memory and tool-call semantics don't reduce to rendering.

## Potential Improvements

- A harness-coupling inventory: enumerate which engine artifacts are model-family-tuned
  (prompt phrasing, tool-call conventions, memory/context assumptions) so a future
  migration is costable instead of discovered.
- Track whether vendor-shipped harnesses (GLM's Codex clone) mature into credible
  lift-and-shift targets — that would weaken this finding.

## Potential Failure Modes

- **Overweighting one migration story:** Lindy is one team with unusual incentives;
  rewrite scope may vary widely by harness complexity.
- **Excuse for lock-in:** "the harness won't port" can rationalize never re-evaluating
  model choice even when the ROI screen passes.
- **Time decay:** models are converging on tool-calling conventions; the coupling may
  loosen at the interface level even if memory/prompt tuning stays model-specific.
