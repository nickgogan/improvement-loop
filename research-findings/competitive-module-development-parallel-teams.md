---
name: Competitive Module Development (Parallel Teams)
summary: Instead of one team building a module and reviewers checking it, run multiple small teams (or agents) building the same component independently. Select the best result. Quality through evolution
  and competition rather than inspection. AI makes this economically viable because generation cost is low.
implementation_notes: 'Applicable to agent design: run N sub-agents on the same task with different approaches, evaluate outputs, select the best. This is already partially captured in ''orchestrated competition''
  finding but Pennarun adds the org-design framing and economic argument that AI makes parallel development cheap enough to be the default.'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- every-layer-of-review-makes-you-10x-slower.md
related_findings:
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: extends
- file: orchestrated-competition-n-sub-agents-solve-same.md
  rel: extended-by
- file: agent-teams-shared-communication-channel.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: contradicts
- file: deep-plan-multi-agent-exploration-pattern.md
  rel: same-problem
- file: org-redesign-for-agentic-throughput-high-speed-rail.md
  rel: same-problem
- file: gstack-spec-team-parallel-research-agents.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---
## What It Is

An organizational pattern from Avery Pennarun: rather than having one team build a module and layering review on top, run parallel small teams building the same component differently. "Try it 100 ways and see who comes up with the best one." Quality emerges from competition and selection rather than from inspection.

The AI-era economics: with AI-assisted development, the cost of building multiple versions of a component drops dramatically. The traditional objection ("we can't afford to build it twice") no longer holds when generation is cheap and review is expensive.

Team sizing: "one pizza and some tokens" -- smaller teams than the traditional "two pizza team" because AI handles much of the implementation work.

## Why It Matters

This inverts the traditional quality model. Instead of build-then-review, it's build-multiple-then-select. The review effort shifts from "find flaws in this approach" to "compare approaches and pick the best," which is a fundamentally different (and often easier) cognitive task.

## Why People Are Using It

Pennarun frames this as newly viable due to AI economics. The pattern has precedent in manufacturing (competitive prototyping) and open source (fork-and-select). AI makes it economically viable for routine development work.

## Potential Improvements

Could be combined with automated evaluation to score competing implementations on test pass rate, performance benchmarks, code quality metrics, and readability, reducing the human judgment burden in selection.

## Potential Failure Modes

Only works for well-defined modules with clear interfaces and success criteria. Poorly specified modules will produce N different interpretations that are hard to compare. The selection step still requires human judgment for non-trivial decisions.
