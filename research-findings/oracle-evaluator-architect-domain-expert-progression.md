---
name: "Oracle → Evaluator → Architect — The Domain-Expert Progression Framework"
summary: |-
  Plain English: when you bake domain expertise (clinical, legal, editorial — any judgment
  a customer needs to trust) into an AI product, the domain expert can play one of three
  roles, and which one you need is answerable from two questions, not vibes. Chris
  Lovejoy's framework: an Oracle personally assesses AND improves the AI output end to end
  (works when quality isn't objectively measurable, or the org is small enough for one
  person); an Evaluator instead defines measurable quality and builds a system to capture
  it, handing improvement to engineers (works once quality IS measurable and manual
  engineer-iteration is still fast enough); an Architect designs a system that measures
  AND improves itself with minimal human-in-the-loop (needed once manual iteration can't
  keep pace with the variation the product has to handle). Orgs typically start as Oracle
  and progress along the axis as they hit each mode's limits — not because "sophistication"
  increases, but because the questions "can I measure this?" and "is manual iteration fast
  enough?" change as the product scales. Grounded in three named case studies: Granola
  (meeting notes, Oracle by design — no objectively "best" note), Tandem (medical scribe,
  decentralized Oracle — too many specialty/geography variants for one person), and
  Anterior (prior authorization, progressed Oracle → Evaluator → Architect as the org
  scaled and manual fixes stopped keeping up).
implementation_notes: |-
  Useful as a diagnostic lens wherever the engine or a system it helps design embeds a
  single human reviewer's judgment into an AI-quality loop: ask (1) is quality here
  objectively measurable or does it rest on taste/judgment, (2) if measurable, is
  hand-driven iteration on that metric still fast enough. The answers name which of the
  three modes currently applies and what the next bottleneck will be — not a recipe to
  install, a question to ask before redesigning a review/improvement loop.
category: "Agent Design"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "how-to-leverage-domain-expertise-lovejoy.md"
related_findings:
  - file: "principal-domain-expert-single-ownership.md"
    rel: "extended-by"
  - file: "org-redesign-for-agentic-throughput-high-speed-rail.md"
    rel: "same-problem"
  - file: "five-durable-verticals-ai-cannot-replace.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
---

# Oracle → Evaluator → Architect — The Domain-Expert Progression Framework

## What It Is

A three-mode framework (Chris Lovejoy, Notius Labs) for how a domain expert's judgment gets
embedded into an AI product, plus a decision tree for which mode a given product/org needs:

1. **Oracle** — the domain expert performs both halves of the improve loop personally: they
   assess AI output directly (read traces, use the product) and improve it directly (tweak
   prompts, add documents/tools). No measurement layer, no engineers-in-the-loop; judgment
   goes straight from the expert's head into the product.
2. **Evaluator** — the domain expert stops improving directly and instead *defines*
   quality: sets metrics, builds the system that captures them (user signals, hired
   reviewers, LLM-as-judge), and identifies what's failing. A separate loop (engineers)
   does the actual fixing, driven by what the evaluator's system surfaces.
3. **Architect** — the domain expert designs a system that closes the loop itself:
   measurement and improvement both happen with minimal human-in-the-middle, learning from
   usage. The domain expert's leverage moves from "reviewing individual outputs" to
   "designing the mechanism that reviews and fixes itself."

**The decision tree**, asked in order:
- *Can AI quality here be measured in objective metrics, or is it fundamentally a taste
  call?* If not measurable → **Oracle**. (Sub-question: is one person enough at your
  current scale, or do you need several people each owning a subset — a **decentralized
  oracle**?)
- If measurable: *is manual iteration (a domain expert flags issues, an engineer fixes
  them by hand) still fast enough to keep up with need?* If yes → **Evaluator** is
  sufficient.
- If manual iteration can't keep up (too much variation, too much scale, too many edge
  cases to hand-fix one at a time) → progress to **Architect**.

Progression is typically sequential and driven by necessity, not planned in advance: "a
common starting place is an oracle... but then they can progress... it's necessary if
things are currently breaking at your scale."

**Case studies grounding the framework:**
- **Granola** (AI meeting notes, ~$1B valuation): stayed Oracle even at scale. First
  employee Joe (writer/journalist background) personally reviews outputs and improves
  prompts directly. Justification: no objectively "best" meeting note (taste, not metric),
  and meeting notes are the single core output — amenable to direct human review even as
  usage grows.
- **Tandem** (medical AI scribe, largest UK clinical-AI adoption): started Oracle (Roy, MD
  → McKinsey, reviewed notes and updated prompts), then scaled to a **decentralized
  oracle** — many doctors, each owning a specialty/country/note-type subset, each able to
  push their own prompt customization live for their slice. Necessary because one person
  couldn't cover the combinatorics of specialties × countries × note types, but the
  underlying quality question (is this medical note good?) still isn't a hard metric.
- **Anterior** (US prior-authorization AI): Lovejoy himself as first technical employee
  started as Oracle (built the product, clinically reviewed outputs, updated
  prompts/code). Didn't scale — progressed to **Evaluator** (defined metrics and failure
  modes, built a review dashboard, hired clinicians to review a sample). That also stopped
  scaling on the fixing side (too much variation in how insurers interpret policy rules
  for engineers to hand-patch), forcing progression to **Architect** (automated,
  self-improving system). Justification for the full progression: output here IS
  measurable (approve / escalate, checkable against medical evidence), which unlocked
  Evaluator; but rule-interpretation variation was too large for manual iteration, which
  forced Architect.

## Why It Matters

Reframes "winning in vertical AI" as an organizational-design problem, not a model
problem: Lovejoy's stated thesis (echoing an earlier well-attended talk of his) is that
"the system for incorporating domain insights is more important than the sophistication of
your models." He grounds this against Gartner's reported ~50% abandonment rate for
generative-AI projects, attributing much of it to building automation without a deep
understanding of the actual workflow being automated — a gap only a domain expert closes.

The framework's value is that it converts "do I need a domain expert, and what kind" from
a values question into two testable questions (measurable? fast-enough-manually?) with a
concrete next-mode answer either way. It also explains *why* teams that hire "a domain
expert" without specifying the mode often stall: an Oracle-shaped hire dropped into a
product that actually needs an Evaluator (or vice versa) has the wrong skill emphasis for
the job.

## Why People Are Using It

Lovejoy reports his original talk on this thesis (at a prior AI Engineer conference) was
seen by roughly 100,000 people across platforms, and the most common follow-up question
was "how do I build my organization to enable this" — this talk is the direct answer,
delivered with three named, verifiable case studies (Granola, Tandem, Anterior) spanning
three different resolutions of the same decision tree.

## Potential Alternatives

Treating "hire a domain expert" as sufficient without specifying a mode (the failure
pattern Lovejoy is explicitly arguing against). Consultant/advisory-only domain expertise —
brought in for opinions but not embedded in the loop (rejected; see the companion
ownership finding). Model-quality-first strategies that assume a better foundation model
substitutes for organizational judgment-capture (the framing Lovejoy opens by rejecting:
"I don't think this is true... winning in vertical AI is an organizational problem").

## Potential Improvements

The framework doesn't name what happens when different parts of the same product sit at
different modes simultaneously (e.g., a core feature at Architect while a new feature
launches at Oracle) — a multi-mode product map would be a natural extension. The
measurability question is treated as binary; many products have partially-measurable
quality (some dimensions scorable, others taste) and would benefit from a hybrid-mode
variant. The decentralized-oracle sub-case (Tandem) is described as a variant of Oracle
rather than a fourth named mode, despite having materially different scaling properties
(more people, not more automation) — naming it explicitly would sharpen the tree.

## Potential Failure Modes

- **Mode misdiagnosis**: building Architect-grade automation before quality is even
  measurable (skipping Evaluator) wastes engineering effort on a system with nothing solid
  to optimize against.
- **Premature Evaluator investment**: formalizing metrics and review dashboards when
  manual iteration was still fast enough is process overhead the org didn't yet need.
- **Progression treated as one-way**: the framework implies "evolve" but doesn't address
  regression — a product whose variation drops (post-consolidation, narrower scope) might
  rationally move back down the ladder, which isn't discussed.
- **The 50% abandonment root cause is asserted, not measured** here — Lovejoy cites
  Gartner's statistic and attributes it to this gap, but the causal link is his
  interpretation, not something the talk demonstrates directly.
