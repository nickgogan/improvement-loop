---
name: "Microworlds — Agent-Built Ephemeral Interactive Debuggers for Intuition"
summary: |-
  Plain English: instead of asking an agent to explain code in prose, ask it to build
  you a small, disposable, interactive tool whose only job is making one confusing piece
  of runtime behavior visible and clickable — a scrubbable timeline of an interpreter's
  execution, or a step-through "game" of a file migration instead of a script you have
  to trust blind. Geoffrey Litt (Notion) calls these "microworlds," after educator
  Seymour Papert's "Mathland" idea (kids learn math by living inside it, not reading
  about it). The tool gets thrown away once the intuition lands — it isn't a
  deliverable, it's a means of getting a feel for the machine that reading code or an
  agent's prose summary doesn't give you. Generation is now cheap enough (one prompt
  plus iteration) that building custom tooling just to understand one thing has flipped
  from "not worth it" to routine.
implementation_notes: |-
  Prompt pattern: ask the agent for a scrubbable/steppable visualizer of the specific
  internal state that's unclear (timeline + state inspector + a way to leave notes),
  scoped to one confusion at a time, and treat the artifact as throwaway rather than a
  maintained deliverable. Candidate first application: an interactive step-through of DD
  dependency/supersession chains for the parked governance-visualization work (IB-175),
  which the KB already flagged as a strong match for interactive over linear
  explanation.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented, working demo)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (governance-visualization interactive exploration, IB-175)"
  - "General"
adopted_in: []
sources:
  - "understanding-is-the-new-bottleneck.md"
related_findings:
  - file: "interactive-explanations-extend-linear-walkthroughs.md"
    rel: "same-problem"
  - file: "shared-spaces-multiplayer-human-agent-surfaces.md"
    rel: "same-problem"
  - file: "quiz-as-comprehension-gate-before-forwarding.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
---

# Microworlds — Agent-Built Ephemeral Interactive Debuggers for Intuition

## What It Is

"Microworlds" — a term Geoffrey Litt (design engineer, Notion) borrows from educator
Seymour Papert's "Mathland" concept (kids learn math by inhabiting an environment built
for intuitive exploration, not by reading about it, exemplified by Papert's LOGO turtle)
— applied to code understanding. Instead of asking an agent to explain code in prose,
you ask it to *build* a small, throwaway, interactive tool whose entire purpose is
making one specific piece of internal or runtime state visible and manipulable.

Two examples from the talk:

1. **Interpreter step-through debugger.** While implementing a Prolog interpreter for
   his own learning, Litt had Claude build an ephemeral UI purpose-built to visualize
   the interpreter's internals: a scrubbable timeline of every execution step with all
   state visible at each step, plus a commenting feature to leave notes for himself on
   the timeline. He used it to fix real bugs, but the byproduct — "getting a feel for
   the machine" — was the actual goal. His explicit contrast: "if you just have an agent
   go fix the bug, you don't get that peripheral vision. If you live in a microworld, you
   do."
2. **Framework-migration walkthrough.** Migrating his personal website between
   frameworks, Litt first had Claude write a migration script. Reading it left him
   unconvinced ("I just don't have a feel for what it's doing"). So he asked for a
   game-like step-through instead: old site on the left, new site on the right, a "Next"
   button, a live commentary of each command, and a live file tree showing files moving.
   Same underlying migration, but experienced iteratively and verifiably instead of
   trusted as a batch script.

Framing: "agents can write code to help us understand code," where "the point isn't
building software to ship, it's building these little microworlds for us." Ephemeral by
design — built for one understanding task, then discarded, not committed or maintained.

## Why It Matters

Names a third documentation register beyond prose docs and diffs: a disposable,
purpose-built interactive artifact whose only job is building the *builder's* own
intuition about a system's runtime behavior, not communicating a finished result to an
audience. Generation cost has collapsed (agent-authored, one prompt plus iteration),
flipping the old cost/benefit of hand-building custom tooling just to understand one
thing — previously not worth the investment, now cheap enough to be routine mid-task
practice, including while the code is still being debugged rather than only after it
ships.

This is the generation-side, builder-facing complement to the KB's existing
reader-facing pattern (`interactive-explanations-extend-linear-walkthroughs.md`, Simon
Willison): that finding is about an author building an interactive artifact to explain
finished code *to an audience*; this pattern is about a builder generating one *for
themselves*, often mid-task, disposably, as a debugging tool rather than a
documentation deliverable. Both converge on the same underlying claim — prose and
diffs are weak at conveying dynamic, spatial, or temporal behavior, and an interactive
artifact is often the fastest path to an accurate mental model — from opposite ends of
the author/reader relationship.

## Why People Are Using It

Litt demoed both examples from his own daily practice — not a shipped Notion product
feature, but a personal workflow habit nested inside a talk about staying genuinely "in
the loop" on agent-written code. Grounded explicitly in Papert's Mathland pedagogy and
in Alan Kay's 1970s "personal computer for children of all ages" vision; Litt frames the
pattern as executing a 50-year-old idea that's newly cheap: "code is free... we can make
ephemeral UIs, dynamic simulations to understand concepts... it's actually not a new
idea. This was the goal all along."

## Potential Alternatives

- **Static diagrams or prose walkthroughs.** Cheaper to produce, but don't convey
  dynamic or temporal behavior — the same trade-off already documented in
  `interactive-explanations-extend-linear-walkthroughs.md`'s comparison table.
- **Traditional debugger plus breakpoints.** General-purpose and already available, but
  not purpose-built to the specific confusion, and requires the human to already know
  what to inspect.
- **Print statements or logging.** Cheapest option, but linear and non-explorable — no
  scrubbing, no state inspection at arbitrary points.

## Potential Improvements

- A lightweight "build me a microworld for X" prompt template or skill, standardizing
  the ask (scrub timeline, comment-on-state, state inspector) the way
  `interactive-explanations-extend-linear-walkthroughs.md` proposes standardizing
  affordances for reader-facing interactive docs.
- Pairing with the quiz/comprehension-gate mechanic (`quiz-as-comprehension-gate-before-
  forwarding.md`): a microworld builds intuition; a quiz verifies it actually landed.

## Potential Failure Modes

- Throwaway-by-design cuts against verifiability: nothing stops the microworld itself
  from having a bug that produces a false mental model — the same hidden-state-bug risk
  already flagged in `interactive-explanations-extend-linear-walkthroughs.md`. Being
  ephemeral and unreviewed makes that check easy to skip.
- Generation overhead for trivial state doesn't pay for itself — best reserved for
  spatial, temporal, or state-machine complexity that resists prose, the same scoping
  caveat as the sibling interactive-explanations finding.
- Risk of becoming a time sink or toy-building distraction if not scoped tightly to one
  specific confusion at a time.
