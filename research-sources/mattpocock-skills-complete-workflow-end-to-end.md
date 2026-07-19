---
name: "mattpocock/skills: A Complete AI Coding Workflow, End-to-End (Matt Pocock)"
source_type: Video
status: Done
key_takeaways: |-
  Pocock's first proper tutorial for his skills repo, walking the everyday default flow
  end-to-end on a real repo: grill-with-docs interviews the idea against the codebase,
  then an explicit fork — implement directly if it fits one session's "smart zone"
  (~140k tokens, past which he expects attention degradation/hallucination), or
  to-spec + to-tickets (each ticket sized to one smart zone) if it won't. Demonstrated
  live: 6-question grilling session, deliberate fork to spec+tickets, an over-cut 3-ticket
  split caught and collapsed to 1, implementation, and a passing two-axis code review that
  committed. Also newly explains why the code-review skill dispatches to subagents at all
  (agents reviewing their own just-written code self-anchor; fresh context avoids it) —
  a delta on the already-KB'd two-axis parallel review pattern from an earlier Pocock
  video.
relevance: High
added_by: Nick
tags:
  - claude-code
  - orchestration
  - skills
  - session-management
  - code-review
url: "https://www.youtube.com/watch?v=M6mYodf0dJM"
authority:
  - "matt-pocock.md"
findings:
  - "everyday-default-flow-smart-zone-ticket-sizing.md"
  - "UPDATE--two-axis-parallel-code-review-standards-vs-spec.md"
date_added: "2026-07-18"
date_processed: "2026-07-18"
date_published: "2026-07-16"
---

Pass 2 extraction (link-intake batch A, follows session 150). Transcript:
`app/transcript-fetcher/transcripts/M6mYodf0dJM.md`. Triage-accepted KB-ONLY
(`operations/research-reports/2026-07-18-link-intake-triage.md`): "Everyday-flow fork rule
+ ~140k-token 'smart zone' ticket sizing; repo already watched at the version shown — no
re-analysis needed" (`watched-libraries/mattpocock-skills.md`, last evaluated v1.1.0,
unchanged by this video). Judged at triage as distinct from the existing
`wayfinder-issue-tracker-decision-map.md` finding (that's the too-big-and-foggy path; this
is the everyday default) — confirmed on full-transcript read; staged as a new finding plus
a surgical update to the existing two-axis code-review finding for the fresh-context
rationale delta.
