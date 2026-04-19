---
name: Critic/Verifier Loop with Termination Conditions
summary: Generate -> Critique -> Patch cycle with explicit termination (iteration limit or confidence threshold). Critic has stricter instructions and retrieval access than generator. Critic can 'fail closed'
  if insufficient evidence. Prevents hallucinations in compliance, finance, medical, and legal contexts.
implementation_notes: 'MetaSystem''s iterative-refinement-loop-with-quality-gate is a simpler version. This pattern adds: explicit termination conditions (preventing infinite loops), critic with separate
  retrieval access, and fail-closed behavior. Apply to research-proposer and prompt-evaluator where verification matters.'
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- multi-agent-orchestration-production-playbook-nick.md
related_findings:
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: extends
- file: review-pipeline-bottleneck-and-quality-at-source.md
  rel: contradicts
- file: verification-agent-seven-prompt-patterns.md
  rel: enabled-by
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- agent-design-patterns.md
---

# Critic/Verifier Loop with Termination Conditions

## What It Is
A structured generate-critique-patch cycle where: (1) a generator agent produces output, (2) a critic agent with stricter instructions and independent retrieval access evaluates the output, (3) patches are applied based on critique, (4) the loop terminates at either an iteration limit or confidence threshold. The critic operates with different (usually stricter) constraints than the generator and can "fail closed" -- refusing to approve output when evidence is insufficient rather than defaulting to approval.

## Why It Matters
Unbounded generate-critique loops are a common production failure -- they consume tokens indefinitely without converging. Explicit termination conditions prevent this. The fail-closed behavior is critical for high-stakes domains where a false positive (approving bad output) is worse than a false negative (rejecting good output).

## Why People Are Using It
Nick Gupta identifies this as a core multi-agent orchestration pattern. The parallel debate + judge variant uses multiple generators with a separate judge agent that selects or synthesizes, logging disagreements as evaluation signals for training data.

## Potential Improvements
Adaptive iteration limits based on task complexity. Confidence calibration from historical critique accuracy. Automatic escalation to human review when confidence is below threshold but iteration limit is reached.

## Potential Failure Modes
Critic and generator converging on shared blind spots (both miss the same error). Termination conditions set too aggressively (stopping before quality is sufficient) or too loosely (wasting tokens). Critic that always finds something to critique, preventing convergence.
