---
name: "On-Policy vs Naive Trace Distillation (Style Transfers, Genius Does Not)"
summary: |-
  Plain English: copying a frontier model's transcripts into a small model makes the small
  model worse, not better — the only distillation route with evidence behind it is grading
  the student's own attempts. Community measurements on Fable-5-trace fine-tunes of
  Qwen3-4B: tool-calling score fell 99 -> 96 and bug-fix rate fell 19/30 -> 11/30 versus
  the untouched base — naive off-policy imitation copies the teacher's voice while real
  capability leaks out ("style transfers, genius does not"; a 4B model lacks room for a
  frontier brain). The fix, per the Thinking Machines "On-Policy Distillation" paper: the
  student attempts the task and the teacher grades every token — reported 70% on a hard
  math benchmark at 1/10 the cost of full RL, up to 30x cheaper than naive imitation, and
  7-10x faster to train. Evidence-only for the Model dimension; the engine has no
  fine-tuning surface. Primary-paper verification pending.
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "how-to-distill-claude-fable-5.md"
related_findings:
  - file: "distillator-with-round-trip-validation.md"
    rel: "same-problem"
  - file: "finite-training-generalization-via-error-recovery.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# On-Policy vs Naive Trace Distillation

## What It Is

Two distillation regimes with opposite results. **Off-policy (naive):** capture the
teacher's traces (reasoning + tool calls; community datasets: "Fable Traces" — 4,600 agent
sessions from 60 real Claude Code runs, 81% tool-call rows; a second effort at 2.3M
reasoning traces) and train the student to imitate them line by line. The student only
ever sees the teacher's perfect path, never its own mistakes. **On-policy (Thinking
Machines paper):** the student attempts the task itself and the teacher grades every token
it produces — right move high score, wrong move low score. The student learns from its own
walk, including recovery from its own errors.

Measured outcomes (secondhand, flagged for primary verification): naive Fable-5
distillation onto Qwen3-4B degraded the model below its own base on both a live
tool-calling test (base 99, +Opus reasoning 98, +Fable traces 96) and a 30-bug coding test
(base fixed 19, distilled fixed 11 and gave up on 16). On-policy: 70% on a hard math
benchmark at 1/10 the cost of full RL, up to 30x cheaper than naive imitation, 7-10x
faster to train.

## Why It Matters

This is quantified counter-evidence against a currently viral practice (racing to capture
frontier traces before access ends). The mechanistic lesson generalizes: imitating a
flawless transcript never teaches recovery — only graded practice does. For the KB it is
decision-relevant Model-dimension evidence (e.g., when evaluating community
"local Fable" models or any distillation-based product claim), not an adoption candidate:
the engine has no fine-tuning surface.

## Why People Are Using It

Frontier-access volatility (export-control shutdown narrative, pricing changes) drives
"insurance policy" distillation; Hugging Face datasets and one-line vLLM/Ollama serving
make the naive route nearly free — which is exactly why the counter-evidence matters.

## Potential Improvements

Verify against the primary On-Policy Distillation paper (numbers here are secondhand via a
YouTube digest). Track whether on-policy tooling matures enough that small local
executors become viable for the engine's cheap-executor tiers.

## Potential Failure Modes

Benchmark selection effects — the degradation numbers come from one engineer's
head-to-head, not a systematic eval. "1/10 cost" compares to full RL, not to doing
nothing. Even on-policy distillation transfers a sliver of capability into 4B-class
students — adequate for simple repetitive work only. Legal/ToS status of trace capture is
unexamined in the source.
