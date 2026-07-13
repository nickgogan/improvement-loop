---
name: "1.6M agents registered for OpenClaw and did NOTHING"
source_type: "Video"
status: "Done"
key_takeaways: |-
  The routing question ("is this a chat task, a single-agent task, a multi-agent task,
  or not an AI task at all?") answered with measured grounding: Stanford 2024
  repeated-sampling law (15.9% -> 56% solve rate at 250 attempts; ~95% coverage at 10k
  attempts, but selection without a mechanical verifier stalls at ~100 attempts) plus
  Anthropic production data (token spend explains 80% of run-quality variance;
  multi-agent beat single-agent by 90.2%). Distilled into a one-minute four-estimate
  agent test (size / independence / separation-of-concerns / checkability) and a
  two-constraint decomposition theory (split for memory vs split for eval; "fresh eyes
  on demand"). Demonstrated on camera across three tasks, including a ~10x Fable 5 cost
  reduction via plan/judge-expensive + work-cheap model split (Ringer harness).
relevance: "High"
added_by: "Nick"
tags:
  - "multi-agent"
  - "orchestration"
  - "evaluation"
url: "https://www.youtube.com/watch?v=PRqiGS6fnIM"
authority:
  - "nate-b-jones.md"
findings:
  - "repeated-sampling-scaling-law-and-verifier-ceiling.md"
  - "four-estimate-agent-routing-test.md"
  - "two-constraint-decomposition-memory-vs-eval.md"
  - "model-tier-routing-expensive-orchestrator-cheap-s.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-07-10"
---

# 1.6M agents registered for OpenClaw and did NOTHING

Nate B Jones (AI News & Strategy Daily), 28:04, uploaded 2026-07-10. Pass 2 deep
extraction completed 2026-07-13 from the full local transcript
(`app/transcript-fetcher/transcripts/PRqiGS6fnIM.md`).

Part of the three-source "Nate B Jones" leg of the pending named-deps gap-check
(harness fitness reviews, delegation contracts, eval ceilings). This source anchors the
**eval-ceiling** side: evals are the binding constraint on multi-agent scale.

Three new findings extracted; one existing finding
(`model-tier-routing-expensive-orchestrator-cheap-s.md`) extended with the Ringer
plan/judge-expensive + work-cheap production datapoint rather than duplicated.
