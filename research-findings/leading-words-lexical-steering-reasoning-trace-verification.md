---
name: "Leading Words — Lexical Steering Verified in Reasoning Traces"
summary: |-
  Plain English: when a skill isn't obeyed, the fix is usually not more rules — it's picking
  one high-prior-density phrase ("vertical slice", "facts vs decisions") and repeating it
  consistently, then confirming it worked by watching the agent echo the phrase in its own
  thinking traces. Matt Pocock names this "leading words": short phrases that pack an entire
  behavior into the model's existing priors. The verification loop is the novel part — the
  phrase appearing in reasoning traces is the observable signal that the steering landed.
  Applied in production (skills v1.1): a facts-vs-decisions leading-word split (facts the
  agent finds by exploring the codebase; decisions only the user can make) fixed interview
  skills that were "grilling themselves" — especially on Fable — with just a couple of
  sentences changed.
implementation_notes: |-
  Rubric-relevant for /assess-skill and /design-skill (steering criteria): a checkable test
  is "does the skill's key behavioral demand exist as a consistent, named phrase — or as
  diffuse prohibitions?" and the acceptance signal is trace echo, not output inspection.
  Pocock's guidance: if the agent isn't complying, make leading words more consistent and
  more powerful before adding rules; agents are good at proposing leading-word candidates.
  Nick-gated restructure Phase 2 decides whether this enters the assess/design substrate.
category: "Prompt Craft"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (assess-skill/design-skill substrate)"
  - "General"
adopted_in: []
sources:
  - "pocock-skills-v1-1-wayfinder-research-implement.md"
  - "building-great-agent-skills-the-missing-manual.md"
related_findings:
  - file: "fowler-code-smell-names-as-prior-invocation.md"
    rel: "extended-by"
  - file: "skill-authoring-explain-the-why-not-musts.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Leading Words — Lexical Steering Verified in Reasoning Traces

## What It Is

A steering technique for skills and prompts: instead of prohibitions ("don't code layer by
layer"), choose a **leading word** — a short phrase with high prior density in the model's
training ("vertical slice") — and repeat it consistently throughout the skill. The agent
repeats the leading word back in its thinking tokens and output, and that self-re-emphasis
changes behavior. The technique comes with a built-in verification protocol: **watch the
reasoning traces**. If the agent starts saying "we'll do this as a thin vertical slice" in
its thinking, the steering landed; if the phrase never appears, the leading word needs to be
more consistent or more powerful.

Production application (skills v1.1, 07-08): Pocock's grilling skills occasionally
interviewed themselves — exploring the codebase and answering their own questions,
especially on Fable. The fix was a leading-word split between **facts** (things the agent
finds itself by exploring the codebase) and **decisions** (things only the user can make).
"Just a couple of sentences, a couple of things changed around" made the behavior
consistent — complaint volume dropped.

## Why It Matters

This is compression with a feedback loop. "English is a pretty wide API" — a well-chosen
phrase invokes a whole behavior from priors at near-zero token cost, which is exactly the
economics the engine's small-skill discipline wants. The verification half is what elevates
it above folk prompting: most steering advice is unfalsifiable; trace echo gives a binary,
observable acceptance test for whether a phrase is doing work. For `/assess-skill`, this
suggests a steering check (is the core demand a named, repeated phrase?); for
`/design-skill`, a construction step (choose leading words before writing procedure prose).

## Why People Are Using It

Pocock (tier-1 skills authority; ~160K stars, 7M downloads on skills.sh) teaches it as the
single main technique of his missing-manual talk and demonstrates deployed fixes built on
it in v1.1. He notes practitioners recognize it immediately ("I've been doing that for a
while") — the contribution is doing it *consistently* and verifying via traces.

## Potential Alternatives

Explicit rule lists and ALL-CAPS imperatives (brittle; see the explain-the-why finding).
Hooks/deterministic enforcement (works for hard constraints, not for shaping approach).
Few-shot examples (heavier token cost for the same prior-invocation effect).

## Potential Improvements

A leading-word lexicon per domain (candidate phrases with known prior density). Automated
trace scanning: grep reasoning traces for the skill's declared leading words as a CI-style
steering regression test. Model-specific calibration — the facts/decisions failure was
model-skewed (Fable), so leading-word strength may vary by model family.

## Potential Failure Modes

- **Weak-prior phrases**: a phrase that means something only to the author ("do it the
  Acme way") has no prior density and steers nothing.
- **Inconsistent usage**: the same behavior referred to by three different phrases dilutes
  the echo effect — the technique demands lexical discipline across the whole skill.
- **Echo without compliance**: the agent can parrot the phrase in traces while still
  deviating in action; trace echo is necessary evidence, not sufficient.
- **Prior mismatch**: a term whose community meaning differs from the author's intent
  steers toward the community meaning.
