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
- claude-code-creator-4-loops-10x-ai-output.md
related_findings:
- file: generator-assessor-separation-in-skill-iteration.md
  rel: extends
- file: multi-perspective-review-council.md
  rel: same-problem
- file: declarative-goal-driven-agent-prompting.md
  rel: same-problem
- file: closed-loop-floor-open-exploration.md
  rel: extends
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
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

## Cartridge Variant — Composable Numeric Scoring as an Autonomous Stop Condition (2026-07-12)

A second, independent source (Dream Labs AI, covering Boris Cherny's "four loops"
framing) instantiates the same rehearsal-before-submission idea as a **numeric,
composable goal condition** rather than qualitative feedback — closing the loop fully
autonomously rather than routing back to a human reader. A "cartridge" is a named,
reusable scoring function built from a corpus (public content, historical performance
data, or a style spec) that grades one piece of content 0-10 on one dimension. Three
worked examples, all applied to marketing email:

- **Humanify cartridge** — an anti-AI-slop-filter scoring voice, variety, and
  predictability to detect AI-sounding copy; bar is >=9/10.
- **Hormozi AI cartridge** — a persona-clone-style scorer built from a named public
  figure's (Alex Hormozi) tweets, emails, and YouTube content, grading marketing
  quality against his style; bar is >=9/10. This one *is* a persona clone in the
  sense already documented above — cartridges are the broader category, of which
  persona-clone is one species. Humanify and the open-rate cartridge below are not
  persona clones at all; they are statistical/style scorers with no simulated person
  behind them.
- **Open-rate cartridge** — trained on the user's own historical email data (past
  opens, audience behavior, subject-line patterns) to predict the open rate of a new
  draft; a 9/10 score is calibrated to "predicted to be opened by over 40% of
  recipients."

The composable move: multiple cartridges sum into **one weighted numeric threshold** —
e.g., "score at least 27/30 across the humanify, Hormozi AI, and open-rate cartridges"
— that becomes the literal stop condition of a `/goal`-based autonomous loop. Below the
bar, the loop takes each failing cartridge's specific feedback and rewrites the content,
then rescores, with no described human step in that revision cycle. The source's own
framing: this composability is why the practitioner (echoing Boris Cherny) says he no
longer prompts Claude directly — he has "dozens of these loops going until the work is
perfected."

This is the same "writing a verifier is writing a reward function" move the KB already
holds for code loops (`closed-loop-floor-open-exploration.md`), applied to non-code
content via composed numeric scorers instead of test assertions — and it goes one step
further than the persona-clone-board pattern above: the clones here don't just advise,
their combined score *is* the loop's exit condition. That is a materially more
autonomous claim than "rehearsal, never a replacement of the human gate" — flagged as a
tension between the two sources, not silently folded in. See the added Potential Failure
Modes bullet below.

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
- **Autonomy creep past the rehearsal framing.** The cartridge variant's own worked
  example has the loop auto-send once a combined score clears the bar — "if the
  email... gets a nine out of ten from that cartridge, then the loop can end and it
  can send it to our list" — with no described human step at that point. That is a
  materially different claim than this finding's core framing ("a rehearsal
  mechanism, never a replacement" of the human gate). Flagged as a genuine tension
  between sources, not resolved here: any adoption of the cartridge-composition
  mechanic for engine use must keep the human gate terminal by design, not assume the
  source's own practice does.
