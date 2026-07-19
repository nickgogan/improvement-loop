---
name: "AI Jason — I Was Building Loops Wrong..."
source_type: "Video"
status: "Done"
key_takeaways: |-
  Production loop architecture from Super Divine (source's company), run for months
  across engineering, CRM, docs, and support-triage automations. Two mechanisms
  extracted: (1) a loop-contract file — goal + boundaries + SOP as the "contract," a
  small durable "state," and an append-only "log," all in one markdown file per
  automation — plus a per-automation "evolve session" cadence (every 5-10 runs) that
  revises the loop's own contract/state/trigger using its past run history; (2) a
  four-type trigger taxonomy (continuous / cron / event-webhook / poll-then-wake
  combo), with the combo trigger as the standout cost optimization and an explicit
  platform gap: neither Claude Code nor Codex natively support event/webhook
  triggers, requiring a self-hosted daemon. Source appears to originate or closely
  precede the "Loop Engineering" framing already in the KB via a secondhand
  explainer (loop-engineering-explained-by-claude-code-creators.md) — see the
  authority note.
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "orchestration"
  - "loop-engineering"
  - "agentic-systems"
url: "https://www.youtube.com/watch?v=JQ_We_ztxrI"
authority:
  - "ai-jason.md"
findings:
  - "loop-contract-anatomy-and-evolve-session-cadence.md"
  - "loop-trigger-taxonomy-poll-then-wake-combo.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-07-13"
---

Session-151 Pass 2 deep extraction (link-intake batch-c, loops cluster). Transcript:
`app/transcript-fetcher/transcripts/JQ_We_ztxrI.md`. The verifier-setup (Playwright CLI
+ sandbox) material and the orchestrator/executor/verifier three-role split overlap
existing KB findings and were not re-extracted; the react-doctor CLI tool mentioned as
an example is color for the loop-contract finding, not independently extracted.
