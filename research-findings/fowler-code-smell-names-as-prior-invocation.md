---
name: "Fowler Code-Smell Names as ~10-Line Prior Invocation"
summary: |-
  Plain English: you don't need to teach the model a review rubric it already knows — you
  need to activate it. Pocock's v1.1 code-review skill lists Martin Fowler's refactoring
  smell names (mysterious name, duplicated code, feature envy, data clumps, primitive
  obsession, repeated switches, divergent change, speculative generality, message chains,
  middle man), each described in one sentence — about 10 lines total. Because Refactoring
  is so old and well-cited, the smells are "deep in the agent's priors"; naming them leads
  the agent to identify and report them by name ("I found some message chains — I need to
  remove them"). Two weeks of production testing: "outrageously useful" for code quality
  at near-zero token cost. The general move: canonical-literature vocabulary is a
  compressed rubric — invoke it, don't restate it.
implementation_notes: null
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "pocock-skills-v1-1-wayfinder-research-implement.md"
related_findings:
  - file: "leading-words-lexical-steering-reasoning-trace-verification.md"
    rel: "extends"
  - file: "two-axis-parallel-code-review-standards-vs-spec.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Fowler Code-Smell Names as ~10-Line Prior Invocation

## What It Is

A special case of leading words applied to review rubrics: instead of writing custom
review criteria, list the named smells from Martin Fowler's *Refactoring* — one sentence
each, roughly 10 lines in total — inside the code-review skill. The smell names (mysterious
name, duplicated code, feature envy, data clumps, primitive obsession, repeated switches,
divergent change, speculative generality, message chains, middle man) are so deeply
represented in training data that a one-line mention activates the full concept; the agent
then reports findings *in that vocabulary* ("Yes, I found some message chains. I need to
remove them"), which is the same reasoning-trace echo that verifies leading words
generally.

## Why It Matters

It reframes rubric authoring as a retrieval problem: for any domain with canonical,
heavily cited literature, the highest-leverage skill content is the literature's *names*,
not restated explanations. Ten lines buy what a bespoke multi-page rubric would cost —
and the bespoke version would generalize worse, since it lacks prior density. The
transferable test for skill authors: before writing criteria, ask whether a canonical
vocabulary already exists in the model's priors and can be invoked by name. (The same
logic underlies why "vertical slice" works as a leading word, and why the engine's own
audit skills can lean on well-known terms rather than re-deriving them.)

## Why People Are Using It

Pocock tested it for two weeks in his production code-review skill before shipping in
v1.1: "outrageously useful... really, really nice at improving the quality of my code and
it's really cheap to add." The smells slot into the review's standards axis alongside
repo-specific coding standards.

## Potential Alternatives

Bespoke rubric prose (expensive, weaker priors). Linters/static analysis for mechanical
smells (deterministic but blind to semantic smells like feature envy). Few-shot examples
of good/bad code (heavy token cost per concept).

## Potential Improvements

Domain catalogs of prior-dense vocabularies (Fowler for refactoring; design-pattern names;
OWASP categories for security review; Nielsen heuristics for UI review). Verifying prior
coverage per model family before relying on a vocabulary.

## Potential Failure Modes

- **Prior drift from the source**: the model's internalized version of a smell may differ
  subtly from Fowler's definition; the one-sentence gloss is the only correction applied.
- **Vocabulary hammer**: the agent force-fits findings into the named smells and
  under-reports issues outside the catalog.
- **Weak or contested canons**: the trick fails where literature is recent, niche, or
  contradictory — prior density is the load-bearing property, and it's unmeasured.
