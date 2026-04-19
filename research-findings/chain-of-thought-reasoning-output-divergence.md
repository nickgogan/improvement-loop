---
notion_id: 32b1e08b-9b34-81c2-96a7-c6bf65cc6260
name: Chain-of-Thought Reasoning/Output Divergence
summary: LLM reasoning traces and final outputs frequently operate as semi-independent processes — the chain of thought is not a reliable explanation of or predictor for the model's output, especially at
  the end of long reasoning chains.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- General
adopted_in: []
sources:
- chatgpt-health-identified-respiratory-failure-then.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-07'
pipeline_status: raw
consumed_by: []
---
# Chain-of-Thought Reasoning/Output Divergence

## What It Is
Mount Sinai found that ChatGPT Health's reasoning chain correctly identified dangerous clinical findings, but the output recommendation contradicted those findings. Research on chain-of-thought faithfulness confirms this is structural: the reasoning trace and the final answer are semi-independent generation processes. Studies show models can produce correct answers even when researchers insert incorrect reasoning chains — the link between stated reasoning and output is weaker than it appears. Models also fail to update answers in response to logically significant changes in their reasoning more than 50% of the time. Oxford's AI governance initiative describes CoT as 'fundamentally unreliable as an explanation of a model's decision process.' The output may reflect an earlier state of the reasoning chain rather than its conclusion.

## Why It Matters
Practitioners who assume that a correct-looking reasoning trace guarantees a correct output are missing a critical reliability gap. Compliance, customer service, and coding agents may produce plausible-sounding reasoning and still take the wrong action. Chain of thought cannot be used as a proxy for output quality without independent validation.

## Why People Are Using It
Chain of thought is observable, free, and feels explanatory. The temptation to use it as a quality signal is high even when the research shows it is unreliable.

## Potential Alternatives
External validation layers (deterministic rules, test suites) that verify output independently of reasoning. Shadow mode testing where the output is compared against ground truth regardless of reasoning quality.

## Potential Improvements
Architectural separation of reasoning and action: use the reasoning chain as input to a separate action-selection module with its own validation. Regular comparison of reasoning traces against ground truth outputs as a diagnostic.

## Potential Failure Modes
Overreliance on reasoning trace review as a substitute for output validation. Reasoning traces can provide false assurance that masks systematic output errors.
