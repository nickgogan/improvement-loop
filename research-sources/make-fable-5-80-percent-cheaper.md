---
name: "Make Fable 5 80% Cheaper (& Other Usage Cheat Codes)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Five cost levers for frontier-model usage, two quantified. (1) Effort-level tuning is the
  first-order lever: on the Deep Sweet long-horizon agentic benchmark, Fable 5 at low effort
  scores 60% for $3.76/task vs 59% for Opus 4.8 at max effort ($13/task) — and vs $22/task
  for Fable 5 at max (>80% intra-model reduction; max adds little over extra-high). Effort
  curve: low 60%, medium 65%, high 69%, extra-high 70%. Anthropic's own accuracy-vs-cost
  chart shows Fable low matching Opus 4.8 max at half the cost. Change via /effort. (2)
  Frontier-as-advisor via the /advisor CLI command: set the executor as the session model,
  then /advisor fable — extends the Opus-advises-Sonnet API pattern to Fable-tier advisors
  in Claude Code. Also: Fable-as-architect plans that explicitly assign executor models per
  phase; delegating research to cheaper models (deep-research spawned 109 subagents — never
  at frontier prices); independent-ish replication of Ponytail token-reduction claims on
  Fable 5 medium (~22% cheaper than baseline; vendor benchmarks were Haiku-4.5-only).
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "orchestration"
  - "evaluation"
url: "https://www.youtube.com/watch?v=p8ypBeNXQ8E"
authority:
  - "chase-ai.md"
findings:
  - "effort-level-tuning-as-first-order-cost-lever.md"
  - "advisor-executor-api-pattern.md"
  - "seven-rung-minimal-code-decision-ladder.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-07-03"
---

# Make Fable 5 80% Cheaper (Chase AI)

Pass 2 extraction completed 2026-07-12 (session 136) from the full transcript
(`app/transcript-fetcher/transcripts/p8ypBeNXQ8E.md`). Effort-level economics numbers are
itemized for the Nick-gated model-capability-registry refresh bundle. The Ponytail
replication here is the one independent-ish corroboration behind the Ponytail
watched-libraries candidacy (Nick-gated).
