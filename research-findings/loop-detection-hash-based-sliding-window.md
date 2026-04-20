---
name: Loop Detection with Hash-Based Sliding Window
summary: 'Sliding window of last 20 tool call hashes per thread for loop detection. Warn at 3 identical consecutive calls (inject system message). Hard-stop at 5 (strip tool_calls, force terminal answer).
  Tool-frequency limit: 50 calls to same tool type per session.'
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: gsd-stall-detection-revision-loop-escalation.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A middleware-based loop detection mechanism using a sliding window of hashed tool calls. The system maintains the last 20 tool call hashes per thread (LRU eviction at 100 threads). When 3 identical consecutive calls are detected, a warning system message is injected ("you are repeating"). At 5 identical calls, all `tool_calls` are stripped from the AI message, forcing a terminal text answer. Additionally, a per-tool-type frequency limit of 50 calls per session prevents runaway single-tool loops.

## Why It Matters

The existing KB covers stall detection via trajectory monitoring (GSD's revision-loop escalation). This pattern uses a different mechanism — content-hash-based rather than trajectory-based — and implements a two-stage response (warn then stop) rather than immediate escalation. The hash approach detects exact repetition efficiently; the sliding window bounds memory usage.

## Why People Are Using It

Observed in [DeerFlow](https://github.com/bytedance/deer-flow) v2.0 — see [[deer-flow-analysis]] for structural details. DeerFlow implements this in `loop_detection_middleware.py` as part of its 12-layer middleware stack. The 50-call per-tool-type limit is a separate safety net for loops that vary slightly (different args, same tool).

## Potential Alternatives

- Trajectory monitoring (GSD's approach — pattern matching on action sequences)
- Timeout-based detection (stop after N minutes of no progress)
- Token budget exhaustion (let the context fill up and stop naturally)

## Potential Improvements

Could combine hash-based detection with semantic similarity — detect not just exact repetition but "doing approximately the same thing" via embedding comparison.

## Potential Failure Modes

- Hash-based detection misses semantically identical but syntactically different loops
- The 50-call limit may be too aggressive for legitimate use cases (e.g., many file reads)
- Warning injection may not change agent behavior if the model ignores system messages
