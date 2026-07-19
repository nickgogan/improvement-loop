---
name: Five-Point Agent Health Checklist
summary: 'Plain English: five questions to ask periodically about any serious deployed agent —

  a concrete fitness-review instrument for the bidirectional-breakage problem.

  (1) Inputs: what is it eating — are sources current, did the workflow move, did an old

  source become misleading? (2) Reach: what can it touch — does each permission still

  fit the current model''s strength (too broad for a strong model, too narrow for an

  improved one)? (3) Job: has the job drifted silently (a summary agent becoming a de

  facto planning agent) — change the job on purpose or not at all. (4) Proof: is its

  evidence a linkable trail a human can inspect (tickets, quoted language, which

  sources checked and which inaccessible), not self-report? (5) Value: does anyone read

  the output, does it save time after review, should the agent be rebuilt (model

  improved) or retired (business changed)?'
implementation_notes: 'P2: the most directly transplantable artifact of the Jones harness-maintenance leg —

  a natural future ENHANCE delta for /system-health or the model-capability-registry

  refresh procedure (triage gate: no mechanism from one source; revisit on recurrence).

  Feeds the named-deps gap-check next session: the engine has audit skills for

  consistency and drift but no periodic instrument asking reach-fits-model or

  value-still-real about its own agents/skills.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (/system-health, registry refresh, agent reviews)
- General
adopted_in: []
sources:
- dont-build-more-ai-agents-until-you-watch-this.md
related_findings:
- file: bidirectional-agent-breakage-world-drift-model-improvement.md
  rel: extends
- file: agentic-harness-self-assessment-skill.md
  rel: same-problem
- file: receipt-artifact-as-agent-trust-mechanism.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-13'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---

# Five-Point Agent Health Checklist

## What It Is

A periodic review instrument for any serious deployed agent, operationalizing the
two-direction breakage model into checkable questions:

1. **What's it eating?** Are the sources current? Did the workflow move? Did a new
   source become important, or an old one become misleading?
2. **Test its reach.** What can it touch — read only, draft, create tickets, post,
   update records, spend money, publish? A permission harmless for a weaker model may
   be too broad for a strong one; a restriction that made sense for an unreliable model
   may hold back a better one.
3. **Check its job.** Is this still a summary agent — and is that still useful? Is it
   becoming a planning agent because the model now can? "Do not let the job change
   silently. Change the job on purpose if you're going to do it at all."
4. **Check the proof.** Not "customers are frustrated with onboarding" as assertion —
   links to the tickets, quoted customer language with sources, and a statement of
   which sources were checked and which could not be accessed. The proof is a linkable
   trail a human can inspect, not the agent saying so.
5. **Check the value.** Does anyone read the output? Does it change the work? Does it
   save time after review, or create another pile? Is it duplicating a report? Has the
   model improved enough that the agent should be rebuilt — or the business changed
   enough that it should be retired?

## Why It Matters

Checklists are what turn a maintenance philosophy into practice. Points 1 and 3 test
world drift; points 2 and 5 test model-improvement fit; point 4 enforces the
receipt/auditability discipline the KB already holds for gates. Retirement as a
first-class outcome (point 5) is rarely represented in agent-health thinking.

## Why People Are Using It

Distilled from the Vercel production case and Jones's own delegation practice; aligns
with his earlier 12-primitive harness self-assessment skill (already in the KB) but is
lighter — five questions an operator can run without tooling.

## Potential Alternatives

- Jones's harness self-assessment skill (Design/Evaluation modes) — deeper,
  primitive-by-primitive, better for build-time; the checklist is the recurring
  operations-time complement.
- Continuous eval suites — stronger where mechanical checks exist, but blind to
  job-drift and value questions.

## Potential Improvements

- Attach each question to its trigger: 1 and 3 on a time cadence; 2 and 5 on every
  model upgrade; 4 on every gated output.
- Severity-ordered findings and a prioritized fix path, as his skill version does.

## Potential Failure Modes

- Checklist rot — the instrument itself is a harness artifact subject to the same drift
  it checks for.
- Answering from memory instead of evidence (point 4 applies to the reviewer too).
- Skipping point 5 because retirement feels like failure; zombie agents that pass
  points 1-4 while producing unread output.
