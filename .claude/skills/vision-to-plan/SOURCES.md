# Sources

Names the upstream methods [SKILL.md](SKILL.md) distills and what was taken from each.
The body carries no `[finding-name]` bracket citations; its debts are method-level, so
this file maps methods rather than findings. Neither upstream is bundled — the URLs are
what an external consumer verifies against.

| Upstream | What this skill took | URL |
|---|---|---|
| BMAD-METHOD | The planning arc (product brief → PRD → architecture → epics) and the YAML-template pattern of embedding per-section elicitation instructions inside document templates (the `references/` templates follow it) | https://github.com/bmad-code-org/BMAD-METHOD |
| Superpowers | Execution discipline: chunked design approval (one section at a time, human gate between), and context-free executable plans (every epic/milestone actionable by an agent with no access to the planning conversation) | https://github.com/obra/superpowers |

The epic → milestone handoff vocabulary (Vision → Milestone → Scope, hill status,
definition-of-done) is owned by the sibling `ops-session-handoff` package — see its
SOURCES.md for those conventions' upstreams.
