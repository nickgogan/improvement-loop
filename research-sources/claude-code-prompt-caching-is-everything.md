---
name: "Claude Code team — Lessons from building Claude Code: prompt caching is everything"
source_type: "Article"
status: "Done"
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
authority:
  - "anthropic.md"
findings:
  - "append-only-context-updates-system-reminder-injection.md"
  - "no-mid-session-model-switching-subagent-handoff.md"
  - "static-tool-set-mode-changes-as-callable-tools.md"
  - "cache-safe-compaction-forked-prefix-buffer.md"
  - "cache-hit-rate-as-slo.md"
  - "gpt-54-tool-search-deferred-tool-loading.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage run 2
(`operations/research-reports/2026-07-11-link-intake-triage-run2.md`, link #4).

Processed 2026-07-11 (Pass 1). Author: Thariq Shihipar, technical staff, Claude Code team;
published 2026-04-30. Five new findings extracted; static-first prompt layering folded into
the append-only finding's body (it corroborates the existing
`layered-prompt-assembly-stable-segment-caching.md` rather than warranting a new finding).
Deferred tool loading (`defer_loading` stubs) recorded as production corroboration on the
existing `gpt-54-tool-search-deferred-tool-loading.md` (already at Strong evidence — no
upgrade needed).
