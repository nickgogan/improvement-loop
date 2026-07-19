---
notion_id: 32b1e08b-9b34-8180-b4fe-c63cd1499adf
name: Karpathy Autoresearch Self-Improvement Loop
summary: 'Binary assertions in evals.json drive an autonomous make-one-change → test → keep/revert loop. Two layers: skill description loop and main improvement loop. Designed for overnight autonomous execution.'
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P2
applicability:
- Perplexity Skills
adopted_in:
- Improvement Loop
sources:
- karpathy-autoresearch-video.md
- openai-self-evolving-agents-cookbook.md
proposals: []
date_discovered: '2026-03-15'
last_updated: '2026-07-12'
related_findings:
- file: volume-over-quality-eval-principle.md
  rel: enabled-by
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: enabled-by
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: process-optimizer-agent-loop-improvement.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- eval-driven-improvement-loops.md
---
# Karpathy Autoresearch Self-Improvement Loop

## What It Is
The Karpathy Autoresearch pattern uses binary assertions stored in evals.json as the ground truth for autonomous self-improvement. An agent makes exactly one change to a skill or prompt, runs the eval suite, and keeps the change only if assertions pass — reverting otherwise. Two loops operate in concert: an inner skill description loop and an outer main improvement loop, designed to run unsupervised overnight.

## Why It Matters
Manual prompt tuning is slow and subjective. This pattern creates a tight, machine-verifiable feedback loop where improvement is constrained to provably-passing changes. The revert-on-failure mechanism prevents regressions from accumulating and makes the improvement trajectory monotonically positive within the eval scope.

## Why People Are Using It
The pattern has been applied conceptually to three skills in the vault — notion-operations, build-spec-execution, and ib-spec-writing — and the macro version of this loop is already instantiated as the research-loop -> prompt-evaluator -> prompt-enhancer pipeline. Production testing by Karpathy provides strong evidence of viability at scale.

## Potential Improvements
The evals.json assertions could be run overnight against vault skills autonomously, with a morning report summarizing which changes were accepted and which were reverted. Connecting the loop to the IB system would allow improvement tasks to be issued as IBs and tracked like any other build work.

## Potential Failure Modes
Binary assertions are a blunt instrument — they can miss nuanced quality regressions where a change is technically correct but degrades the skill's usefulness in edge cases. If the eval suite is sparse or poorly calibrated, the loop can converge on a local optimum that passes all assertions while being worse on real-world tasks.
