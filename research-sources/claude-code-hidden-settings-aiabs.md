---
name: "Claude Code Hidden Settings and Flags (AIABS)"
source_type: "Video"
status: "Done"
key_takeaways: "Comprehensive walkthrough of undocumented Claude Code settings. Key items: cleanup_period_days for session retention, path-specific rules for separation of concerns, bash output limit override (30K→150K chars), subagent config (skills/effort/hooks/background/isolation/permitted-agents), read line limit workaround (2000 lines), auto-compact percentage override (95%→70-75%), agent teams vs subagents distinction, Claude CTX profile switching, hook exit code 2 as behavioral enforcement mechanism, RALP loops for iterative quality."
relevance: "Medium"
added_by: "Nick"
tags:
  - "context-engineering"
  - "tool-integration"
  - "claude-code"
url: "https://www.youtube.com/watch?v=pDoBe4qbFPE"
authority: []
findings: []
date_added: "2026-05-24"
date_processed: "2026-05-24"
---

# Claude Code Hidden Settings and Flags (AIABS)

YouTube video covering undocumented Claude Code configuration. Largely corroborates existing KB findings rather than introducing novel patterns.

## Corroborates Existing Findings

- **Context degradation threshold** — video cites 70% as quality degradation point, recommends `auto_compact_percentage_override: 75`. Matches our `context-degradation-40-50-percent-threshold.md` finding.
- **CLAUDE.md context rot** — path-specific rules as solution for instruction overload. Matches our `claudemd-context-rot-from-indiscriminate-rule-accu.md` finding.
- **Agent teams** — distinguishes teams (inter-agent communication) from subagents (isolated). Matches our `agent-teams-shared-communication-channel.md` finding.
- **Hook exit codes** — exit code 2 as behavioral enforcement. Relevant to our existing hooks/RALP findings.

## New Details (not novel patterns)

- `cleanup_period_days` setting for session retention
- Subagent config: `skill`, `effort`, `hooks`, `background`, `isolation`, `permitted_agent_names`
- Claude CTX — open-source profile switching tool
- `attribution` key to control commit co-authoring
- Telemetry opt-out settings (3 separate flags vs CLI `--offline` which also blocks updates)
- Prompt stashing (Ctrl+S)
