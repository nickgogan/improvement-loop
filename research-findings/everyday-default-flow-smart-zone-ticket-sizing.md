---
name: "Everyday Default Flow — The Implement-Directly-vs-Spec+Tickets Fork, Sized by the Smart Zone"
summary: |-
  Plain English: Matt Pocock's default per-idea workflow answers one question explicitly,
  out loud, before doing anything else — "will this fit in one agent session, or do I need
  to plan across several?" `grill-with-docs` interviews the idea against the real codebase
  until agent and user share understanding. Then comes an explicit fork: if the remaining
  work comfortably fits in one session's "smart zone," skip straight to `/implement`. If
  it won't, run `to-spec` (compress the grilling discussion into a written spec) then
  `to-tickets` (cut the spec into tickets, each sized to fit one smart zone on its own),
  then implement one ticket at a time, clearing context between tickets. The fork isn't
  guesswork — Pocock treats roughly 140k tokens as the edge of the smart zone, past which
  he expects attention degradation and hallucination, and does the budget arithmetic
  out loud before committing to a path ("we've got 100k of budget here to remove 10
  commands — that seems super easy"). Demonstrated live end-to-end on a real repo (his own
  AI Hero CLI): grilled down to 6 questions, deliberately forked to spec+tickets to show
  the multi-session path, caught and collapsed an over-cut 3-ticket split down to 1 on
  inspection, implemented, and the built-in review (see the two-axis parallel review
  finding) passed and committed.
implementation_notes: |-
  A concrete, numeric answer to a question every session-scoped agent workflow has to
  make implicitly: how do you decide whether an idea needs multi-session planning at all?
  Relevant to how the engine or GSD-style workflows size units of work (IB items, phases,
  ticket-equivalents) — not as a number to copy (140k is Pocock's own felt sense on his
  own model/effort configuration) but as the pattern of doing the token-budget arithmetic
  explicitly at the fork point rather than discovering the budget was wrong mid-session.
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "mattpocock-skills-complete-workflow-end-to-end.md"
related_findings:
  - file: "wayfinder-issue-tracker-decision-map.md"
    rel: "same-problem"
  - file: "leg-work-amplification-hiding-future-steps.md"
    rel: "same-problem"
  - file: "context-degradation-40-50-percent-threshold.md"
    rel: "same-problem"
  - file: "two-axis-parallel-code-review-standards-vs-spec.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
---

# Everyday Default Flow — The Implement-Directly-vs-Spec+Tickets Fork, Sized by the Smart Zone

## What It Is

Matt Pocock's default per-session workflow for "idea to ship" in his `mattpocock/skills`
repo, walked live end-to-end on a real working repo (AI Hero CLI, his own command-line
tool):

1. **`grill-with-docs`** — an interview-driven interrogation of a stated idea against the
   actual codebase. Stateful: records what it learns into `context.md` and ADRs as it
   goes. Runs until the agent and user "reach a shared understanding" — in the
   demonstrated run, this took 6 questions (Pocock notes his usually run closer to 20,
   scaled to the size of the idea).
2. **The fork** — an explicit decision point, not an automatic one: *will the remaining
   work fit inside one agent session's "smart zone," or will it need several?*
   - **Fits in one session** → skip straight to `/implement`. This is what Pocock says he
     would normally do for work this size ("I would just say implement and then I would
     leave it, let it run, and it would finish the work").
   - **Needs multiple sessions** → `to-spec` compresses the grilling discussion into a
     written spec (problem statement, solution, user stories, implementation/testing
     decisions) saved to the repo's configured issue tracker (GitHub, Jira, Linear, or —
     as demonstrated — local markdown). `to-tickets` then turns the spec into tickets,
     each deliberately sized to fit one smart zone on its own: "each one of these tickets
     is supposed to just be the size of a single context window."
3. **`/implement`**, one ticket at a time. Convention: clear context between tickets rather
   than batch them through in one long session ("usually I would say you clear in between
   every single ticket"); only squeeze in an extra ticket if there's budget left in the
   current smart zone.
4. **Built-in code review** runs as part of `/implement`'s own script — type-check, build,
   internal verification, then delegates to the two-axis parallel reviewer (spec-fidelity
   + standards-conformance; see the companion finding) before committing.

**The sizing heuristic driving the fork and the ticket cuts:** Pocock treats roughly
**140k tokens as the edge of the "smart zone"** — his term for the point past which he
expects "attention degradation... it ends up getting stupider, does weird
hallucinations." He does the budget arithmetic explicitly, out loud, before committing to
a path rather than discovering mid-session that the budget was wrong: "I think of having
like, okay, we've got 100k of budget here to remove 10 commands. That seems super easy."
In the demo, he caught his own over-cut spec (3 tickets where 1 would do) by inspecting the
output against this same budget sense and collapsing it before implementing.

**Setup prerequisite:** the flow depends on `set up mattpocock skills` having already
configured the repo — an issue-tracker backend (told to the agent in plain language: "set
it up with Jira," or accept the local-markdown default), triage labels, and a
single-vs-multi-context domain-docs choice (single context is the default recommendation
for all but large monorepos).

## Why It Matters

Gives a concrete, numeric answer to a question every session-scoped agent workflow answers
implicitly: is this small enough to just do, or does it need to be planned across
sessions? Most planning-vs-doing guidance is qualitative ("if it feels big, plan it");
this pattern shows a practitioner doing the arithmetic out loud before choosing a path,
which is falsifiable and teachable in a way "use your judgment" is not.

It also encodes a composability property: the same "does it fit in a smart zone" test
applies at two granularities — once to the whole idea (the fork itself) and again to each
individual ticket (the sizing rule behind `to-tickets`). The fork and the ticket-cutting
aren't two different mechanisms; they're the same budget test applied recursively, which
is why the multi-session path composes cleanly back down to single-session units.

## Why People Are Using It

Demonstrated live end-to-end on a real, working repo — not a toy example. Pocock grilled
a genuine internal-tooling-removal idea (delete 10 of 11 CLI subcommands) down to 6
questions, deliberately took the `to-spec`/`to-tickets` fork even though the work would
have fit in one session (to demonstrate the multi-session path on camera), caught an
over-eager 3-ticket split and collapsed it back to 1 ticket on inspection, implemented,
and the built-in review passed both axes and committed the result. Positioned explicitly
as "the main flow that all of my work runs through" for a skills repo reporting roughly
162k GitHub stars and 7.5M downloads at the time of the video — this is the default path,
not an edge case.

## Potential Alternatives

Always plan multi-session regardless of size — this is what `/wayfinder`'s issue-tracker
decision map does for ideas that are both too big *and* foggy; heavier apparatus, and
explicitly scoped by its own author to that harder case rather than the everyday default.
Always implement directly with no spec/ticket step — simpler, but loses the multi-session
continuity artifact and the final spec-fidelity review anchor that `to-spec` provides.
Fixed task-count heuristics instead of a token budget — e.g. a different practitioner's
"limit plans to 2-3 tasks max" rule, which targets a related but distinct failure mode
(rushed "completion mode" at 40-50% utilization, rather than attention
degradation/hallucination past an absolute token count).

## Potential Improvements

An explicit token-count readout at the grilling checkpoint would make the fork decision
measurable rather than felt — right now it rests on Pocock's own intuition ("I think of
having like, okay..."). The 140k figure is unlikely to transfer as-is across models or
effort levels (Pocock notes he was running Opus on medium effort, but says the skills are
used across different harnesses and models) — a per-model/effort calibration would make
the heuristic portable. The manual ticket-recut Pocock did by eyeballing the spec (3
tickets down to 1) is a candidate for automation: a sizing check that flags
over-partitioned specs before they're handed to `/implement`.

## Potential Failure Modes

- **Single-practitioner heuristic**: 140k is Pocock's felt sense on his own
  model/effort/harness combination, not a measured threshold — likely to mis-calibrate
  elsewhere.
- **Manual budget estimation**: the fork-point arithmetic is eyeballed ("I think of having
  like...100k of budget"), not computed from an actual token counter; misjudgment at the
  spec stage compounds across every ticket cut from it.
- **Fork-point subjectivity**: "will this need multiple sessions" is exactly the kind of
  estimate practitioners get wrong — demonstrated by the video's own over-cut
  3-tickets-to-1 correction, caught only because Pocock happened to inspect the output
  before implementing.
- **Prerequisite setup debt**: the flow assumes `set up mattpocock skills` already wired
  an issue tracker and domain docs; without that setup, the spec/ticket step has nowhere
  durable to write and the multi-session path degrades.
