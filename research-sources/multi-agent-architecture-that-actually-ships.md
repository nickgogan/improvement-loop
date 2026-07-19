---
name: Luke Alvoeiro (Factory) — The Multi-Agent Architecture That Actually Ships
source_type: Video
status: Done
key_takeaways: |-
  Factory's "Missions" system, presented via a five-pattern multi-agent communication
  taxonomy (delegation / creator-verifier / direct-communication / negotiation /
  broadcast) composed into a three-role architecture (orchestrator / workers /
  validators). Core mechanisms: pre-code validation contracts written before
  implementation, checked by dual blind adversarial validators (a scrutiny validator and
  a computer-use-driven user-testing validator, neither of which has seen the
  implementation); a structured handoff schema that lets multi-day missions self-heal
  without relying on agent memory; serial-with-targeted-parallelization (naive N-way
  parallel agents were tried and rejected); "droid whispering" — deliberate, sometimes
  cross-provider, per-role model assignment; and a bitter-lesson-resistant design
  (orchestration logic lives in prompts/skills, not a hardcoded state machine). Production
  numbers: 16-day longest mission (30 believed achievable), ~90% test coverage, team
  economics moving from roughly 10 to roughly 30 concurrent workstreams per 5 engineers.
relevance: High
added_by: Nick
tags:
- multi-agent
- orchestration
- validation
- harness-engineering
- model-selection
- handoff-protocol
url: https://www.youtube.com/watch?v=ow1we5PzK-o
authority:
- luke-alvoeiro.md
- ai-engineer.md
findings:
- five-pattern-multi-agent-communication-taxonomy.md
- missions-three-role-architecture-serial-targeted-parallelization.md
- pre-code-validation-contracts-dual-blind-validators.md
- structured-handoff-schema-self-healing-multi-agent-missions.md
- droid-whispering-per-role-model-assignment.md
date_added: '2026-07-18'
date_processed: '2026-07-18'
date_published: '2026-05-06'
---

Batch-b1 Pass 2 deep extraction (link-intake queue, harness-engineering /
multi-agent-architecture cluster). Transcript:
`app/transcript-fetcher/transcripts/ow1we5PzK-o.md` (AI Engineer conference, 18.5 min,
534 segments). Dense, high-yield short talk — five distinct findings staged, all
Strong/Medium evidence given the production numbers cited (16-day missions, enterprise
customers). Two of the five findings (pre-code-validation-contracts + structured-handoff-
schema) are flagged in MANIFEST.md as cross-video convergent with Ryan Lopopolo's
QA-plan-as-trust-gate finding from `harness-engineering-humans-steer-agents-execute.md` —
related, not merged; see MANIFEST cross-link notes.
