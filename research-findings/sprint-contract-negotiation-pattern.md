---
name: Sprint Contract Negotiation Between Generator and Evaluator
summary: Generator and evaluator agents negotiate explicit sprint contracts defining granular success criteria before coding begins. Sprint 3 of a retro game had 27 testable criteria for the level editor
  alone.
implementation_notes: 'Could adapt for GSD plan-phase: have a planning agent and verification agent negotiate acceptance criteria before execution begins.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-harness-design-long-running-apps.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

## What It Is

Before each sprint, the generator proposes implementation scope and success criteria; the evaluator reviews and negotiates until both agree on what "done" looks like. These contracts contain granular, testable criteria. The evaluator then scores against these specific criteria rather than subjective quality judgments.

## Why It Matters

Without pre-agreed success criteria, evaluation becomes subjective and generators can game vague standards. Sprint contracts make evaluation deterministic and reduce wasted iteration cycles by surfacing scope disagreements before coding begins.

## Why People Are Using It

Anthropic's harness design blog documents this as production-tested across multiple application types (retro games, DAWs, museum websites).

## Potential Improvements

Auto-generation of criteria from specifications. Difficulty calibration to prevent over-specifying trivial sprints and under-specifying complex ones.

## Potential Failure Modes

Over-specification (too many criteria per sprint) can make evaluation brittle. Criteria that are testable but not meaningful can create a "teaching to the test" effect.
