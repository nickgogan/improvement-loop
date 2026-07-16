---
name: Persona-Clone Review Board as Verifier for Test-Less Outputs
summary: 'For outputs with no test suite (emails, reports, decks, strategy docs), build the

  verifier out of simulated stakeholders — "AI time travel": get the feedback before the

  final version is ever submitted. Three tiers: ask-the-board (clone 4-5 public thought

  leaders in your vertical from their scraped public content) for strategic work; an

  internal focus group (clone of the end user/customer, built by having Claude interview

  you about them) for anything customer-facing; and clone-your-manager (an Anthropic

  growth marketer cloned his manager from her blog posts, Slack messages, and emails to

  get her feedback before submitting to her) for day-to-day work. Extends verification —

  Anthropic''s self-reported highest single quality lever — into domains with no

  executable checks.'
implementation_notes: 'Fills a real gap: the KB''s verifier findings are code-centric, but most engine outputs

  (findings, guides, reports, handoffs) have no executable verifier. A persona-based

  reviewer is one design option — e.g., a reviewer primed on Nick''s documented standing

  feedback (plain-English-first, no hardcoded counts, minimum viable abstraction) that

  pre-screens reports before the real gate. Design required; the clone is a rehearsal for

  the human gate, never a replacement of it.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (non-code output verification)
- General
adopted_in: []
sources:
- youre-the-problem-not-claude-6-fixes.md
related_findings:
- file: generator-assessor-separation-in-skill-iteration.md
  rel: extends
- file: multi-perspective-review-council.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

A verification mechanism for work that has no tests: simulate the people who will judge
the output, and run their judgment *before* submission. Marchese's three concrete
skills:

1. **Ask the board** — pick 4-5 thought leaders in your vertical with public content
   (e.g., Hormozi, Cuban, Karpathy), scrape it, and build persona clones that critique
   high-level strategic work.
2. **Internal focus group** — have Claude interview you to construct a clone of the end
   user of whatever you're producing; customer-facing work is reviewed by that clone.
3. **Clone your manager** — the sharpest instance: an Anthropic growth employee cloned
   his manager from her blog posts, Slack messages, and emails, and now gets her
   feedback before actually submitting anything to her.

The framing is "AI time travel": the feedback that would have arrived after delivery
arrives before it, so the delivered version has already absorbed a review cycle. The same
video quotes Anthropic that verification "has had the most measurable impact on Claude's
output quality internally — their highest single quality lever," and positions persona
boards as the verification channel for non-technical work (alongside CLAUDE.md
verification language and MCP connections for real-world data).

## Why It Matters for Us

The engine's verifier patterns (tests-first goal loops, headless verification runs,
rubric scorers) all assume checkable outputs. Its actual products — findings, guides,
audit reports — are judged by a human with documented taste. A persona reviewer built
from that documented taste is a way to move some review cost ahead of the gate: the
generator-assessor separation holds (fresh context, different instructions), and the
human gate stays terminal. It is a rehearsal mechanism, not an approval mechanism.

## Why People Are Using It

Practitioner-documented (Marchese, 2026-07-07) with a named production anecdote inside
Anthropic (manager clone) and his own claim of using the board pattern at a startup that
raised $20M+. The KB's review-council and role-voting findings converge on
multi-perspective simulated judgment from independent sources.

## Potential Alternatives

- **Multi-perspective critic council** (existing finding): decomposes review by dimension
  (facts, safety, style) rather than by simulated person — better when the judging
  criteria are objective, worse at predicting a specific stakeholder's reaction.
- **Rubric-based scoring**: explicit criteria instead of persona inference; more
  auditable, less able to capture unstated taste.

## Potential Improvements

- Grounding clones in accumulated real feedback (past review decisions) rather than
  public content alone, and re-syncing them as the person's standards evolve.
- Calibration checks: periodically compare the clone's verdicts with the real person's
  to measure fidelity drift.

## Potential Failure Modes

- Fidelity illusion: the clone captures the person's public style, not their private
  judgment; confident wrong feedback is worse than none.
- Goodhart on the clone: optimizing to please the simulated reviewer diverges from
  pleasing the real one.
- Consent/privacy: cloning a real colleague from internal communications has obvious
  interpersonal and data-handling sensitivities.
- Staleness: people's standards change; an un-refreshed clone reviews for last year's
  taste.
