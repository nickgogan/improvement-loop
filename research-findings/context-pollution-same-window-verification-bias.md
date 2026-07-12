---
name: 'Context Pollution: Same-Window Verification Bias'
summary: When an agent verifies its own work within the same conversation context, it inherits all prior reasoning, assumptions, and mistakes — producing systematically biased verification. The verification
  agent sees the same context that led to the error, making it likely to rationalize rather than detect the problem.
implementation_notes: Argues for spawning verification in a separate context (sub-agent or fresh session). Relevant to MetaSystem's evaluation patterns.
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
- anthropic-effective-context-engineering.md
related_findings:
- file: verification-agent-seven-prompt-patterns.md
  rel: extends
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
- file: cross-vendor-adversarial-build-attack-loop.md
  rel: same-problem
- file: no-mistakes-post-implementation-validation-pipeline.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

Same-window verification is when an agent checks its own output within the same conversation context that produced it. The verifier inherits all prior reasoning, assumptions, and errors from the generation phase. This creates a systematic bias where the agent rationalizes existing conclusions rather than independently evaluating them.

## Why It Matters

Verification is only useful if it can catch errors the original process missed. When the verifier shares the same context window, it has access to the exact reasoning chain that led to the mistake, making it predisposed to agree with flawed conclusions. This undermines the entire purpose of having a verification step in agent workflows.

## Why People Are Using It

Most agent frameworks default to same-window verification because it is the simplest implementation — just add another prompt turn. Users may not realize the verification is systematically biased because it appears to work (the agent confidently confirms its own output). The bias is invisible without controlled comparison against independent verification.

## Potential Improvements

Spawn verification in an isolated context: a sub-agent, a fresh session, or a separate tool invocation that receives only the output and acceptance criteria. The /re command and fork-subagent primitive already provide infrastructure for this pattern within Claude Code.

## Potential Failure Modes

Isolated verification loses access to legitimate context that explains design decisions, leading to false negatives. The overhead of spawning separate contexts for every verification step could make workflows impractically slow or expensive. There is a risk of over-engineering verification for tasks where same-window checking is adequate.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[context-isolated-verification]] in `extracts/patterns/`
