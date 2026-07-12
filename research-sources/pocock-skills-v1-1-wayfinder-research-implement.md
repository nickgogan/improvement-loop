---
name: New Skills! v1.1 brings /wayfinder, /research, /implement, /to-spec, /to-tickets (Matt Pocock)
source_type: Video
status: Done
key_takeaways: 'Applied evidence for the missing-manual techniques plus one new planning topology.

  Wayfinder: for ideas too big for one agent session, chart the plan as a shared map on the

  repo''s issue tracker — typed (research/grilling/prototype/task), session-sized,

  blocking-ordered decision tickets; the map, not the chat, carries state; when all tickets

  close, the map feeds /to-spec. Leading words applied: a facts-vs-decisions split (facts

  the agent finds by exploring; decisions only the user can make) stopped interview skills

  grilling themselves, especially on Fable; Fowler code-smell names (message chains, feature

  envy, data clumps…) invoke a whole review rubric from the model''s priors in ~10 lines —

  tested two weeks, "outrageously useful." Code review runs two parallel subagent axes:

  standards conformance (coding-standards.md, kept outside agents.md, loaded at review

  time) and spec fidelity. TDD skill converted to reference-only shape (red before green,

  one slice at a time; refactoring moved into code review) so AFK agents can consume it

  without interactive step-walking. Renames: to-PRD → to-spec, to-issues → to-tickets.'
relevance: High
added_by: Nick
tags:
- skills
- prompt-engineering
- orchestration
url: https://www.youtube.com/watch?v=A8mokin_YOs
authority:
- matt-pocock.md
findings:
- leading-words-lexical-steering-reasoning-trace-verification.md
- fowler-code-smell-names-as-prior-invocation.md
- leg-work-amplification-hiding-future-steps.md
- wayfinder-issue-tracker-decision-map.md
- two-axis-parallel-code-review-standards-vs-spec.md
- reference-only-skill-shape-for-afk-agents.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-08'
---

Session-136 Pass-2 extraction (link-intake wave 2). Transcript:
`app/transcript-fetcher/transcripts/A8mokin_YOs.md`. Processed as one cluster with
`building-great-agent-skills-the-missing-manual.md` (06-29 talk); this video is newer, so
its applied-evidence framing leads on shared techniques (leading words, leg-work). Roster
question already answered at triage and declined: /wayfinder et al. overlap the GSD suite
and /session-handoff — patterns captured as KB findings only.
