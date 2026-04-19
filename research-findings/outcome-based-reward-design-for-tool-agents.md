---
name: Outcome-Based Reward Composition for Tool-Using Agents
summary: 'ARTIST uses a three-component reward signal for RL-trained tool agents: answer correctness (binary), format compliance (structural tags), and tool execution success (fraction of syntactically
  valid calls). This decomposed reward teaches agents not just what to produce but how to invoke tools well.'
implementation_notes: Design tool feedback loops to return structured success/failure signals. Verification steps in our workflows already approximate the answer-correctness component. Adding explicit format
  compliance checks (did the agent use the expected output structure?) and tool execution tracking (did the call parse correctly?) would create a richer self-correction signal.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- artist-agentic-reasoning-and-tool-integration-via.md
related_findings:
- file: rl-trained-autonomous-tool-selection-artist-pattern.md
  rel: enables
- file: emergent-agentic-behaviors-from-outcome-rl.md
  rel: enables
- file: loss-masking-deterministic-tool-outputs.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
# Outcome-Based Reward Composition for Tool-Using Agents

## What It Is
A multi-component reward structure used in ARTIST's RL training for tool-using agents. Rather than a single pass/fail signal, the reward decomposes into three orthogonal components:
- **Answer Reward** (0 or 2): Binary correctness of final output
- **Format Reward** (0.5-1.0): Structural compliance with expected tag ordering (`<think>`, `<tool>`, `<output>`, `<answer>`)
- **Tool Execution Reward** (0-1): Fraction of tool invocations that are syntactically valid and executable

For function-calling domains, rewards shift to state-tracking accuracy (0.5 max) and function-sequence correctness (0.5 max).

## Why It Matters
Single-signal rewards (correct/incorrect) give the model no gradient to improve intermediate steps. Decomposed rewards create learning signal at each stage of the tool-use chain: the model learns to format calls correctly, invoke tools successfully, and produce correct answers -- simultaneously and independently.

## Why People Are Using It
ARTIST's decomposed reward enabled a 7B model to beat GPT-4o on math olympiad benchmarks while doubling performance on multi-turn function calling benchmarks (tau-bench). The tool execution component specifically prevents the common failure mode where models generate plausible-looking but syntactically broken tool calls.

## Potential Improvements
The format reward could be generalized beyond tag ordering to validate arbitrary structured output schemas. The tool execution fraction could weight by call importance rather than treating all calls equally.

## Potential Failure Modes
Reward hacking: models may optimize for format compliance and tool execution scores at the expense of answer correctness. Component weights require careful tuning per domain.
