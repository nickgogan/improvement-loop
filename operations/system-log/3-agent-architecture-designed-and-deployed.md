---
notion_id: null
log_entry: "3-agent architecture designed and deployed — Researcher, Codifier, Librarian"
actor: "Agent: Claude"
area: null
change_type: "Design Decision"
milestone: null
rationale: "Three agents designed using IL's own guide KB (G1, G3, G9, G10). Agent-as-directory structure per fractal pattern (DD-52). Researcher owns stage 1 (11 skills), Codifier owns stages 2-3 (3 skills), Librarian is consumption-layer (read-only, 0 skills). File-mediated handoff protocol using pipeline_status field. Librarian deployed as engine-facing subagent at .claude/agents/librarian.md."
source_dd: "DD-82"
target_system: "improvement-loop"
timestamp: "2026-04-19T00:00:00.000Z"
---

## What Changed

- Designed 3 agent definitions: Researcher, Codifier, Librarian
- Each agent deployed as a directory per fractal pattern (DD-52):
  - `agents/researcher/agent.md` — full constitution, 11-skill inventory, disposition
  - `agents/codifier/agent.md` — full constitution, 3-skill inventory, disposition
  - `agents/librarian/agent.md` — full constitution, dual-mode (Teacher/Builder), read-only
- Created handoff protocol: `agents/handoff-protocol.md`
- Created Librarian engine definition: `.claude/agents/librarian.md` (invocable cross-workspace)
- Formalized as DD-82 (supersedes DD-30)

## Affected Items

- `systems/improvement-loop/agents/` (3 agent directories + handoff protocol)
- `.claude/agents/librarian.md` (engine-facing subagent)
- `systems/improvement-loop/CLAUDE.md` (agent roster, skill ownership, handoff reference)
