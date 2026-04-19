---
notion_id: 32b1e08b-9b34-81f9-8043-c83e6922045f
name: Four-Layer Agent Evaluation Architecture
summary: 'A defense-in-depth eval architecture for high-stakes agents: (1) progressive autonomy routing; (2) deterministic rule-based validation of reasoning-output consistency; (3) LLM-as-judge flywheel
  with explicit false-positive review; (4) factorial stress testing for hidden bias detection.'
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- General
adopted_in: []
sources:
- chatgpt-health-identified-respiratory-failure-then.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-09'
related_findings:
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: enabled-by
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: success-rate-eval-over-binary-pass-fail.md
  rel: extends
- file: three-tier-grading-hierarchy.md
  rel: enabled-by
- file: volume-over-quality-eval-principle.md
  rel: enabled-by
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Four-Layer Agent Evaluation Architecture

## What It Is
Layer 1 -- Progressive Autonomy: Route high-confidence, low-stakes decisions to fully autonomous agent action. Route edge cases to shadow mode. Layer 2 -- Deterministic Validation: Rules-based checks that verify reasoning-output consistency without relying on the model to self-check. Layer 3 -- LLM-as-Judge Flywheel: Configure eval system to bias toward false positives. Continuously update both the eval rulebook and the scenario library. Layer 4 -- Factorial Stress Testing: Periodic, domain-targeted factorial design tests on high-stakes agents.

## Why It Matters
Each layer addresses a different failure mode. Together they provide defense-in-depth: a failure missed by one layer is caught by another.

## Why People Are Using It
Adoption is currently limited to high-stakes enterprise contexts.

## Potential Alternatives
Single LLM-as-judge evaluation. Human-in-loop for all decisions. Standard benchmark suites.

## Potential Improvements
Productized tooling that implements the four-layer architecture as a reusable framework.

## Potential Failure Modes
Layers 2 and 3 require deep domain expertise. LLM-as-judge in Layer 3 can itself have systematic biases.

---
## April 2026 Update
**Confident AI's March 22, 2026 guide on multi-turn LLM evaluation** formalizes the sliding-window approach as the production standard for Layer 3. Two evaluation modes now required: holistic conversation-level and per-turn with sliding context window (default window_size=5). Four new metrics: Conversation Relevancy, Knowledge Retention, Role Adherence, Task Completion.

**Updated evidence strength:** Strong (was Medium)
**Source:** https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026
