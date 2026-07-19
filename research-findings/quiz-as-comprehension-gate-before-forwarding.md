---
name: "Quiz-as-Comprehension-Gate Before Forwarding Agent Work"
summary: |-
  Plain English: after an agent explains what it changed, answer a short quiz about the
  explanation before doing anything with the result — Geoffrey Litt's (Notion) personal
  rule is he won't send agent-written code for team review until he can pass a
  5-question quiz on what his own agent did. It's built on researcher Andy Matuschak's
  "books don't work" observation — it's easy to read something, feel informed, and be
  wrong about whether you actually understood it, and only a forced-recall check catches
  that gap before someone else does. Litt calls it a "speed regulator": every other
  incentive in agent-assisted work pushes to go faster, and the quiz is the one
  mechanism that gates on demonstrated understanding instead of on task completion. It is
  portable independently of any specific tool — applicable anywhere a human is expected
  to have understood agent output before acting on it.
implementation_notes: |-
  After an agent explains a nontrivial change, have it (or a second, independent
  instance) generate 3-5 medium-difficulty questions over its own explanation, and
  withhold approval or forward-routing until they're answered correctly. Prefer a
  separate pass or model for writing the quiz so quiz quality doesn't silently track
  whatever the explanation glossed over — the same generator/assessor separation
  already standing practice elsewhere in this engine.
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (human review gate before accepting staged/agent-authored output)"
  - "General"
adopted_in: []
sources:
  - "understanding-is-the-new-bottleneck.md"
related_findings:
  - file: "microworlds-ephemeral-interactive-debuggers.md"
    rel: "same-problem"
  - file: "shared-spaces-multiplayer-human-agent-surfaces.md"
    rel: "same-problem"
  - file: "goal-backward-verification.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
---

# Quiz-as-Comprehension-Gate Before Forwarding Agent Work

## What It Is

A "comprehension gate" pattern: an agent-generated explanation ends with a short quiz
— Geoffrey Litt's (Notion) implementation is 5 questions, medium difficulty — over the
material just presented, and the human enforces a personal rule not to forward the
agent's work (e.g., to a teammate for review) until they can pass it. Explicitly modeled
on researcher Andy Matuschak's (with collaborator Michael Nielsen) work embedding
interactive spaced-repetition quizzes in essays, built on the observation "books don't
work" — it's easy to read something and believe you understood it, with nothing forcing
you to notice when you didn't.

Litt frames it as a deliberate "speed regulator": every other incentive in an
agent-assisted workflow pushes toward going faster, and the quiz is the one mechanism
that gates advancement on demonstrated understanding rather than on task completion or
elapsed time. It sits at the end of his broader ExplainDiff skill (background →
intuition → interactive mockup → literate diff → quiz), but the mechanism itself —
forced-recall check before forwarding agent output — does not depend on that specific
skill or output format.

## Why It Matters

Directly names a failure mode any agent-assisted reviewer will recognize: believing you
read and understood a change, and discovering the gap only when someone else asks a
basic question. Litt's own account: "I sent a PR to my coworker that I thought I had
read... I thought I understood, and she asked me the most basic question. And I was
like, 'Oh, no. I don't know.'" Passive review — read the diff, feel informed, approve —
has no mechanism to catch this; producing a correct quiz answer requires actually
holding the model in your head, not just having scrolled past the material.

This is a generically portable human-verification primitive, independent of ExplainDiff
or any specific skill — applicable anywhere an agent produces something a human is
expected to have understood before acting on it: approving a PR, gating a governance
change, greenlighting a deploy. Litt also names the term "cognitive debt" — an analogy to technical debt that he
attributes to a scholar (the source transcript renders the name as "Margaret Stories,"
which reads as a likely transcription artifact of a real name the auto-transcript
mangled; not independently verified here) and notes Simon Willison has also blogged
about the term. The claim: un-understood agent output compounds silently, and — like
technical debt — the cost only surfaces later, when the gap has grown too large to close
cheaply. The quiz is Litt's concrete mechanism for keeping that debt from accumulating
in the first place.

## Why People Are Using It

Litt reports daily personal use plus adoption by coworkers at Notion, describing it as
"shocking the number of times this has caught me." He traces the technique to an
established research lineage in spaced-repetition and testing-effect pedagogy
(Matuschak and Nielsen's interactive essays) rather than inventing the mechanism from
scratch — an evidence base that predates and sits outside AI tooling, newly applied to
agent-output review.

## Potential Alternatives

- **Passive review checklists.** Cheaper, but don't force active recall — exactly the
  gap this pattern targets.
- **Explain-it-out-loud to a person (rubber-ducking with a human).** Similarly effective
  at surfacing gaps, but requires a second person's synchronous time; the quiz is
  asynchronous and generated on demand.
- **Predict-then-check.** Have the reviewer write their own summary before reading the
  agent's explanation, then compare. Not mentioned in the talk, but a natural adjacent
  variant with a similar forced-recall property.

## Potential Improvements

- Difficulty and coverage calibration: a badly-written quiz (too easy, or testing
  trivia instead of load-bearing logic) gives false confidence. The quiz's own quality
  needs a check, which the talk doesn't address.
- Track quiz results over time as a personal or team comprehension-debt signal —
  repeated failures in one topic area indicate a standing gap, not a one-off lapse.
- Combine with the microworld pattern
  (`microworlds-ephemeral-interactive-debuggers.md`): build intuition interactively,
  then gate on the quiz — pairing a "why it's true" tool with a "did it land" check.

## Potential Failure Modes

- **Gameable.** Once someone learns a quiz is coming, they can optimize for passing it
  rather than for genuine understanding — a teaching-to-the-test risk, especially
  pronounced if the same agent that wrote the code also writes the quiz.
- **Self-graded, self-administered.** No external enforcement; the entire mechanism
  depends on the individual's discipline to actually stop and not skip it under deadline
  pressure — the same voluntary-compliance risk as any personal checklist.
- **Verifies understanding, not correctness.** A confidently-wrong explanation of a bug
  could produce a confidently-wrong but internally-consistent quiz that the human
  passes while still being misled about what the code actually does.
