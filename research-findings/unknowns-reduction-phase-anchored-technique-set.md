---
name: "Unknowns-Reduction Phase-Anchored Technique Set"
summary: |-
  Anthropic's field guide to Fable 5 (Thariq Shihipar, 2026-07-06) operationalizes the
  finding-your-unknowns thesis as a technique-per-phase playbook, each with exact
  suggested wording. Before build: blind-spot pass, brainstorm/prototype-to-react
  (HTML mocks in wildly different directions), interview-me (one question at a time,
  architecture-changing questions first), references-as-spec (working source code beats
  screenshots and descriptions), and decision-led implementation plans (lead with the
  decisions the human is most likely to tweak — data models, type interfaces, UX — and
  bury trusted mechanical refactoring). During build: an implementation-notes.md file
  with a Deviations section (hit an edge case → pick the conservative option, log it,
  keep going), then a fresh-context handoff carrying spec + prototype + notes. After
  build: package the artifacts into a pitch/explainer for reviewer buy-in, and a quiz-me
  comprehension gate the human must pass before merging.
implementation_notes: |-
  P2 because several techniques land on live engine surfaces with design work needed:
  decision-led plan ordering and the Deviations log are candidate enrichments for the
  engine's handoff/plan documents (adjacent to war-game-plan-format-for-executor-handoff,
  which adds failure signals/countermoves; the two compose — decision-led ordering for
  the human gate, war-game structure for the executor). The quiz-me gate is a candidate
  for keeping Nick genuinely load-bearing as autonomy increases (DD-108 trajectory). Any
  engine adoption routes through the normal pipeline gates.
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "a-field-guide-to-claude-fable-finding-your-unknowns.md"
related_findings:
  - file: "frontier-model-as-unknown-unknown-elicitor.md"
    rel: "extends"
  - file: "war-game-plan-format-for-executor-handoff.md"
    rel: "same-problem"
  - file: "advanced-elicitation-techniques-library.md"
    rel: "same-problem"
  - file: "throwaway-html-editor-structured-input-surface.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "synthesized"
consumed_by:
  - "writing-agent-specifications.md"
---

# Unknowns-Reduction Phase-Anchored Technique Set

## What It Is

The operational half of Anthropic's field guide to Fable 5: a named technique for each
phase of a build, each mapped to the unknowns quadrant it attacks, each with exact
suggested prompt wording.

**Before build:**
- **Blind-spot pass** (attacks unknown unknowns): use the literal phrases — "Can you do a
  blind spot pass to help me figure out my relevant unknown unknowns and help me prompt
  you better", with context on who you are and what you already know.
- **Brainstorms and prototypes** (attacks unknown knowns — criteria you'd recognize but
  can't articulate): "Make me an HTML page with 4 wildly different design directions so I
  can react to them"; mock the new surface with fake data before touching the real app.
- **Interview-me:** "Interview me one question at a time about anything ambiguous,
  prioritize questions where my answer would change the architecture."
- **References-as-spec:** hand over working source code ("this Rust crate implements the
  exact backoff behavior I want — read it and reimplement the same semantics") — richer
  than screenshots or prose descriptions.
- **Decision-led implementation plans:** "lead with the decisions I'm most likely to
  tweak: data model changes, new type interfaces, and anything user-facing. Bury the
  mechanical refactoring at the bottom, I trust you on that part."

**During build:**
- **Deviations log:** "Keep an implementation-notes.md file. If you hit an edge case that
  forces you to deviate from the plan, pick the conservative option, log it under
  'Deviations', and keep going."
- **Fresh-context handoff:** start the build in a new session seeded with the compiled
  artifacts (spec, prototype, notes) rather than the exploration transcript.

**After build:**
- **Pitch/explainer packaging:** "Package the prototype, the spec, and the implementation
  notes into a single doc I can drop in Slack to get buy-in. Lead with the demo GIF."
- **Quiz-me comprehension gate:** an HTML report on the changes "and a quiz at the bottom
  on the changes that I must pass" — the human proves understanding before merging.

## Why It Matters

This is the vendor's own answer to "what does the human do when the model is capable
enough": a disciplined unknowns-reduction loop, with the guide's instructional-balance
principle (over-specification blocks pivots; under-specification forces assumptions) as
the calibration rule. For the engine it lands on concrete surfaces: how handoff and plan
documents are ordered (decisions first), how deviations are logged mid-execution, and how
a human gate stays genuinely load-bearing (the quiz gate) as autonomy increases.

## Why People Are Using It

First-party guidance from the Claude Code team with copy-pasteable wordings; the
secondhand walkthrough ecosystem (e.g. the rejected pw79ro49CzU video) restates it nearly
verbatim, and the Kashef war-game material independently converges on the same
frontier-as-elicitor premise.

## Potential Alternatives

Structured elicitation libraries (the KB's advanced-elicitation-techniques-library
finding) cover the interview move with more technique variety but without the
phase-anchoring or the after-build gates. Spec-first frameworks (GSD-style) formalize the
same before-build intent through heavier process.

## Potential Improvements

Fold the decision-led ordering and Deviations-log conventions into the engine's
handoff/plan templates; pair the quiz gate with receipt artifacts for a two-sided trust
mechanism (agent proves what it did; human proves they understood it).

## Potential Failure Modes

Technique theater: running every pass on every task inflates cost and delays work the
model could just do — the guide itself anchors technique choice to the unknowns actually
present. The quiz gate degrades if the same model writes both the change and the quiz
(self-preferential bias) — an independent quiz-writer is the conservative variant.
