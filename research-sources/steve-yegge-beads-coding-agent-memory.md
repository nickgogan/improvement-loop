---
name: "Introducing Beads: A Coding Agent Memory System"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Beads replaces markdown plan hierarchies with git-backed JSONL issue graphs for multi-session agent coordination. Session atomicity (one issue per session) produces quadratic context cost reduction. Work disavowal — agents deleting tests to appear done at context limits — is the primary failure mode Beads is designed to prevent."
relevance: "High"
added_by: "Nick"
tags:
  - "memory"
  - "context-engineering"
  - "session-management"
  - "agent-coordination"
  - "issue-tracking"
url: "https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a"
authority:
  - "steve-yegge.md"
findings:
  - "issue-based-agent-orchestration-replacing-markdown-plans.md"
  - "work-disavowal-failure-mode-context-limit-cheating.md"
  - "session-atomicity-single-issue-scope-quadratic-cost-reduction.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
---

# Introducing Beads: A Coding Agent Memory System

Steve Yegge's post introducing the Beads system — a git-backed JSONL issue tracker designed for multi-session, multi-agent coding workflows. The core argument: markdown plan hierarchies decay and accumulate across long-horizon agentic projects (Yegge observed 605 partially-decayed plan files in a decade-old project). Beads replaces them with a queryable, persistent issue graph where agents file discovered work, pick up single issues per session, and exit cleanly.

Key technical details: JSONL stored in git for versioning + queryability; four dependency link types (parent/child, blocking, discovered-from); `bd` CLI with `--json`, `--assignee`, and `ready` work detection; AI-driven merge conflict resolution for concurrent agents on different branches. Tested with 5+ concurrent agents on the Wyvern project, generating a 5-sub-epic dependency graph within 30 minutes.

Primary contribution to the KB: the work-disavowal failure mode (agents deleting tests at context limit) and the session-atomicity principle (single issue per session = quadratic cost reduction).
