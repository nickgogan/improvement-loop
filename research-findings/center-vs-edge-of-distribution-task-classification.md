---
name: "Center vs Edge of Distribution — Task Classification as the Model-Routing Input"
summary: |-
  Model routing should start from classifying the task load, not from benchmark tables:
  center-of-distribution tasks (familiar shapes, millions of prior examples, outputs a
  human can inspect quickly) are where models have converged — cheap/open models are at
  parity or better. Edge-of-distribution tasks are where models still separate and
  frontier spend pays. Quantified anchor (Mitchell Hashimoto, Fable 5 launch): on
  ordinary "implement this feature" work, GLM 5.2 (<$1, minutes), GPT 5.5 (~$1.50), and
  Fable 5 ($9, 40 min) produced equally acceptable output — 9x cost for parity; on an
  edge task, only the frontier model could touch it. Jones: "almost no one has asked
  what is your distribution of tasks properly yet" — the classification, not the model
  choice, is the unsolved input.
implementation_notes: |-
  The KB's routing findings (task-specific-model-routing-table, model-tier-routing) name
  "task classification requires its own rules" as an open failure mode — this supplies
  the axis. The model-capability registry refresh and any /design-* model recommendation
  should carry a center/edge classification step before consulting per-model rows:
  center-of-distribution work routes to the cheap tier by default; frontier is reserved
  for edge tasks. Convergence-at-center also explains why cheap-ties-frontier results
  (Hashimoto's first half) are facts about the task, not the models.
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "glm-5-2-is-free-and-beats-claude-on-most-work.md"
  - "you-cant-compete-on-cheap-models-anymore.md"
related_findings:
  - file: "task-specific-model-routing-table-march-2026-bench.md"
    rel: "enables"
  - file: "model-tier-routing-expensive-orchestrator-cheap-s.md"
    rel: "same-problem"
  - file: "claude-5-family-retiers-claude-line.md"
    rel: "same-problem"
  - file: "harness-non-portability-across-model-families.md"
    rel: "same-problem"
  - file: "prototype-at-frontier-then-downshift.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A classification axis for model routing (Nate B Jones, June–July 2026, two-video
framework). **Center-of-distribution** tasks are the fat middle of everyday AI work:
brochure sites, standard decks, first-pass copy, routine synthesis, familiar coding
problem types — "what someone has tried with models millions of times before, where the
answer pattern is pretty normal and the output is pretty easy to inspect." **Edge-of-
distribution** tasks are novel in shape, hard to inspect, or beyond prior example
density. The claim: models have converged exactly on the work everyone already knows how
to ask for, so at the center a ~98%-cheaper open model (GLM 5.2 is Jones's exemplar —
framed as "the best model in the world" at center tasks, especially where front-end
taste matters) ties or beats frontier models; at the edge, frontier models remain alone.

Quantified evidence — Hashimoto's three-tier experiment at Fable 5 launch:

| Model | Cost | Time | Result on ordinary feature work |
|---|---|---|---|
| GLM 5.2 | under $1 | minutes | equally acceptable |
| GPT 5.5 | ~$1.50 | — | equally acceptable |
| Fable 5 | $9 | 40 min | equally acceptable (9x cost, no quality premium) |

Second half: an edge task (optimizing gnarly systems code Hashimoto wrote himself) —
$40, 2 hours on Fable 5, reaching performance he says he couldn't have hit himself;
cheap models "couldn't touch it at all."

## Why It Matters

Every routing table in the KB assumes the task's difficulty class is known; this finding
says the classification itself is the scarce input — "individuals aren't used to
measuring their work that way, teams aren't." A company's (or engine's) model strategy
reduces to: what fraction of the task load is center vs edge? If center-weighted, open
models capture most value; if edge-weighted, frontier contracts are justified. It also
reframes cheap-ties-frontier benchmark results as task facts, not model facts —
guarding against over-generalizing parity findings into "frontier is a rip-off."

## Why People Are Using It

Jones reports the classification question as the live struggle among companies
attempting cheapest-model routing; Lindy's DeepSeek migration (see
harness-non-portability-across-model-families) is the documented case of a team that
measured its distribution and acted. Hashimoto's experiment is the quantified public
demonstration of both halves of the axis.

## Potential Alternatives

- **Per-task benchmark routing tables** (task-specific-model-routing-table): route by
  task *type* against benchmark rows — works when the type is known; this finding
  supplies the coarser prior when it isn't.
- **Dynamic runtime routing:** an orchestrator classifies difficulty on the fly —
  Jones flags on-the-fly frontier-vs-cheap recognition as a major 2026–2027 investment
  theme, i.e., not commodity yet.

## Potential Improvements

- An operational rubric for the classification (example density, output inspectability,
  shape familiarity) rather than vibes — none of the sources supply one.
- Instrumenting actual task logs to measure a team's center/edge weighting empirically.

## Potential Failure Modes

- **The line moves:** every model generation converts some edge tasks to center tasks;
  a static classification goes stale (see prototype-at-frontier-then-downshift).
- **Misclassification at the center:** tasks that look familiar but carry hidden
  edge-of-distribution complexity fail silently on cheap models.
- **Parity claims are analyst-tier for breadth:** the quantified anchor is one
  engineer's experiment; "best in the world at center tasks" is opinion, not benchmark.
