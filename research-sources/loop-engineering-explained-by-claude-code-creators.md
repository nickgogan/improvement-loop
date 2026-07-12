---
name: Cloud Codes — Loop Engineering Explained by Claude Code Creators
source_type: Video
status: Done
key_takeaways: 'Synthesis of the June-2026 "loop engineering" framing: stop prompting agents, design the

  loop that prompts them (discover → plan → execute → verify → repeat until a set

  condition). Loop anatomy: five pieces (automations, worktrees, skills, connectors,

  sub-agents) plus external memory. Core thesis: a loop is a generator wired to a

  verifier, and the verifier is the bottleneck — writing a verifier is writing a reward

  function; never let the agent grade its own work (the goal command hands the stop

  decision to a separate smaller model). Two design rules survive dedup: closed-loop floor

  + one open exploration instruction (the rescue for non-deterministic loops), and the

  legible/executable/verifiable agent-readiness triad for codebases. Also: pick the least

  autonomous tool that does the job. Provenance caveat: the "I do not prompt Claude

  anymore… my job is to write loops" quote is attributed secondhand to Anthropic''s Claude

  Code lead via a June-2026 field guide — unverified; treat as secondhand.'
relevance: Medium
added_by: Nick
tags:
- claude-code
- orchestration
- evaluation
- context-engineering
url: https://www.youtube.com/watch?v=DQq-z4wROTc
authority:
- cloud-codes.md
findings:
- closed-loop-floor-open-exploration.md
- legible-executable-verifiable-agent-readiness-triad.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-26'
---

Session-136 Pass 2 deep extraction (link-intake wave 2, loops/self-improvement cluster).
Transcript: `app/transcript-fetcher/transcripts/DQq-z4wROTc.md`. Much of the loop anatomy
(sub-agent writer/checker split, external memory files, goal command) is already in the
KB from sessions 130–133 — only the two novel design rules were extracted. The Anthropic
attribution is secondhand and recorded as such wherever this source is cited.
