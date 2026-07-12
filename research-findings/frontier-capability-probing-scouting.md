---
name: "Frontier Capability-Probing — the '$40 Question' Scouting Practice"
summary: |-
  Deliberate frontier-model spend on tasks that exist on no backlog, purely to discover
  where the capability line has moved. Anchor case: Mitchell Hashimoto spent $40 and 2
  hours having Fable 5 optimize gnarly systems code he wrote himself — reaching
  performance he says he couldn't have hit on his own, on a task no PM, sprint, or
  best-practices guide had generated. The scarce input is not prompting skill but
  capability instinct built from hours inside models ("you can't imagine with
  capabilities you haven't touched"), plus permission: Jones's organizational test is
  "who on your team is allowed to pose a $400 question to a model today without asking
  anyone?"
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "you-cant-compete-on-cheap-models-anymore.md"
related_findings:
  - file: "prototype-at-frontier-then-downshift.md"
    rel: "enables"
  - file: "frontier-model-as-harness-designer.md"
    rel: "same-problem"
  - file: "five-persistent-human-skills-agent-era-framework.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A named budget line for frontier models distinct from execution: scouting. As cheap
models commoditize execution (routing to them is "about to be table stakes"), the value
of frontier spend concentrates on questions that change what the execution layer is even
building. The probe task's defining property is that it was never assigned — "it didn't
exist as a task until one person, an expert, suspected something new had become possible
and spent money trying to find out." Requirements per Jones: imagination, deep context,
and permission to ask, in one head — hiring an "AI visionary" fails because they arrive
without your context; the job is putting context-holders in contact with capable models
and giving them permission to make bets.

Supporting anecdote: during the Fable 5 launch-week blackout (shipped Tuesday, gone
Friday, back later), what survived the outage was the scouting output — the questions
posed, the workflows redesigned in the first 72 hours — while carefully optimized model
setups were interchangeable.

## Why It Matters

Directly relevant to how the engine spends its own frontier budget: the research loop
scans what practitioners publish, but capability-probing generates first-party evidence
— and each successful probe is exactly the kind of KB-grounded datapoint the
model-capability registry's intentional refresh is supposed to cite. It also gives a
diagnostic for stagnation: "has your task list changed in the last 12/6/3 months, or are
you doing your old list faster and cheaper and calling that AI transformation?"

## Why People Are Using It

Hashimoto's experiment is public and quantified; Jones reports the pattern across his
timeline post-blackout. The framing ("scouting hours," the $400-question permission
test) is analyst synthesis rather than a measured practice, hence Medium evidence.

## Potential Alternatives

- **Benchmark-watching:** track published evals instead of spending on probes — cheaper,
  but Jones's core claim is that capability instinct doesn't transfer from summaries.
- **Community scanning** (the engine's current research loop): harvest others' probe
  results — lags the capability line and is shared with every competitor.

## Potential Improvements

- Institutionalize as a small recurring frontier-probe allowance tied to registry
  refresh cycles, with each probe written up as a finding (Nick-gated adoption).
- Pair with edge-of-distribution classification: probes should target suspected edge
  tasks, not backlog items.

## Potential Failure Modes

- **Scouting theater:** unbounded frontier spend justified as "imagination" with no
  capture mechanism for what was learned.
- **Survivorship bias:** the $40 story is a hit; the base rate of dud probes is
  unreported.
- **Expert dependency:** probes need domain depth to pose and to judge — a non-expert
  running the same probe can't evaluate whether the result beats their own ceiling.
