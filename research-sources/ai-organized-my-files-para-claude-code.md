---
name: "AI Organized My Files. I Checked Every Decision. (Claude Code + PARA)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Tiago Forte (PARA method creator) ran an unedited, checked-every-decision trial: gave
  Claude Code (Opus 4.6, stock $20/mo Pro account, no memory or connectors) his real
  32-file desktop backlog and one instruction — sort it into PARA. Result: 78% accuracy
  (7/32 misfiled), with the taxonomy itself independently verified as correctly
  understood beforehand — errors clustered where a bounded, time-sensitive project
  nested inside a general ongoing area, and where content looked disposable but had
  unstated future value. His response was calibration, not rejection: recommends
  learning PARA manually first, and shipped an official "PARA skill" to raise the
  accuracy rate.
relevance: "Medium"
added_by: "Nick"
tags:
  - "claude-code"
  - "agentic-systems"
  - "second-brain"
  - "evaluation"
url: "https://www.youtube.com/watch?v=HjWESsnoU6g"
authority:
  - "tiago-forte.md"
findings:
  - "agentic-file-classification-reliability-calibration.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-04-07"
---

Session-150 Pass 2 deep extraction (link-intake triage, KB-ONLY verdict, Nick-accepted).
Transcript: `app/transcript-fetcher/transcripts/HjWESsnoU6g.md`.

Triage expected ~1 finding — a measured reliability calibration for agentic
taxonomy-classification, with a named systematic failure mode — and that is exactly
what was extracted. The core value of this source is the number and the failure-mode
name, not a reusable technique: 78% accuracy (7/32 misfiled) on real personal files,
with the agent's comprehension of the PARA taxonomy independently confirmed correct
beforehand, isolating the errors to instance-level context the agent structurally could
not have (a time-bound project nested inside an ongoing area; disposable-looking content
with unstated future value).

Dedup check against the existing KB surfaced two genuinely adjacent (not duplicate)
findings, cross-linked from the new finding rather than merged: `ai-delegated-knowledge-
organization.md` (same underlying problem — AI delegated classification into a
taxonomy — different mechanism: typed knowledge-graph node/edge-typing vs. one-time
PARA folder sorting; staged as an `extends`/`extended-by` pair) and `para-based-file-
memory.md` (PARA-structured agent memory, different substrate again: an agent's own
memory system vs. a user's personal files). Also cross-linked, per the triage brief's
explicit "verify, don't assume duplicate" flag: `flat-root-vault-with-property-based-
organization.md` and `production-memory-architecture-spectrum.md` (the latter already
names PARA-with-decay as one of its five observed memory-architecture levels).
