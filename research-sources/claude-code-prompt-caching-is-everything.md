---
name: "Claude Code team — Lessons from building Claude Code: prompt caching is everything"
source_type: "Article"
status: "Not started"
key_takeaways: |-
  Production playbook for treating prompt-cache PREFIX STABILITY as a first-class harness
  design constraint. Five mechanics novel to the KB beyond the basic stable-context caching
  idea: (1) append system-reminder messages for state updates instead of mutating the prompt;
  (2) never switch models mid-session — hand off to a subagent instead (direct input to
  skill↔model coupling guidance and /design-agent variant B); (3) keep the tool set static
  and implement mode changes as callable tools (plan mode = EnterPlanMode/ExitPlanMode);
  (4) cache-safe compaction: fork with an identical prefix plus a reserved compaction buffer
  so cost scales with the compaction prompt, not conversation length; (5) monitor cache hit
  rate like uptime with SEV-grade alerting. Static-first prompt layering: system prompt/tools
  → CLAUDE.md → session context → messages. Deferred tool loading via lightweight stubs
  cross-corroborates the GPT-5.4 tool-search finding (evidence_strength upgrade candidate at
  extraction). Est. 5 novel findings.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - harness
  - prompt-caching
  - context-engineering
  - claude-code
  - token-economy
url: "https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything"
authority: []
findings: []
date_added: "2026-07-11"
date_processed: null
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage run 2
(`operations/research-reports/2026-07-11-link-intake-triage-run2.md`, link #4).
