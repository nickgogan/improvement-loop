---
name: Six-File Workspace Taxonomy
summary: OpenClaw defines 6 workspace files for agent identity — SOUL.md (personality/values), USER.md (user profile), AGENTS.md (rules), TOOLS.md (environment), HEARTBEAT.md (proactive tasks), MEMORY.md
  (long-term memory). Clean separation of concerns for agent context.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: soul-md-agent-constitution-pattern.md
  rel: extends
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: extends
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

OpenClaw defines six workspace files, each with a distinct purpose in the agent's identity and operational context:

| File | Purpose |
|------|---------|
| **SOUL.md** | Who you are — personality, values, communication style |
| **USER.md** | Who you help — user profile, preferences, needs |
| **AGENTS.md** | Workspace rules and conventions — what to do and not do |
| **TOOLS.md** | Local environment notes — available tools, configurations, paths |
| **HEARTBEAT.md** | Proactive tasks — things to do without being asked |
| **MEMORY.md** | Long-term memory — accumulated knowledge across sessions |

The separation principle is: identity vs. user context vs. rules vs. environment vs. behavior vs. memory. Each file has a clear owner and update lifecycle. SOUL.md is rarely changed (identity is stable). USER.md evolves as the agent learns about the user. AGENTS.md is maintained by the project. TOOLS.md reflects the current environment. HEARTBEAT.md defines background behaviors. MEMORY.md grows across sessions.

## Why It Matters

Most AI-assisted development tools use one or two context files (CLAUDE.md, .cursorrules) that conflate identity, rules, environment, and memory into a single document. As these files grow, they become difficult to maintain because changes to one concern (e.g., adding a tool) risk disrupting another (e.g., personality instructions).

The six-file taxonomy provides clean separation of concerns at the file level. Each file can be loaded selectively — a quick task might only need AGENTS.md and TOOLS.md, while a personal assistant interaction needs SOUL.md and USER.md. This enables context-aware loading rather than all-or-nothing.

## Why People Are Using It

Observed in [OpenClaw](https://github.com/openclaw/openclaw) v2026.4.5 — see [[openclaw-analysis]] for structural details.

The existing KB covers SOUL.md as a standalone pattern and the general taxonomy concept. This finding adds the complete six-file separation and the design principles behind each file's purpose. OpenClaw's taxonomy is the most comprehensive context file separation of concerns among analyzed frameworks.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single CLAUDE.md with sections | All context in one file with clear section headers | Simple projects where maintenance overhead of multiple files is not justified |
| Two-file split (identity + rules) | SOUL.md for identity, CLAUDE.md for everything else | When the full six-file split is overkill but identity separation matters |
| Directory-based context | Context organized by directory (hierarchical CLAUDE.md files) | When context is subsystem-scoped rather than concern-scoped |
| Dynamic context assembly | No static files; context assembled at runtime from a database | When context changes frequently and file-based management becomes a bottleneck |

## Potential Improvements

- Define clear guidelines for what belongs in each file — the boundary between AGENTS.md (rules) and SOUL.md (values) can be blurry
- Explore selective loading strategies — which files are needed for which task types?
- Test whether six files is the right number or if some can be merged without losing the separation benefit (e.g., TOOLS.md into AGENTS.md)

## Potential Failure Modes

- **File proliferation overhead**: Six files per workspace is six files to maintain, keep consistent, and load. For simple projects, this is over-engineering
- **Boundary disputes**: "Is this a rule (AGENTS.md) or a value (SOUL.md)?" leads to inconsistent placement and eventual duplication
- **Load order dependencies**: If files reference each other, the load order matters and may create subtle bugs
- **Staleness divergence**: Different files update at different rates. TOOLS.md may become stale while MEMORY.md stays current, creating inconsistent context
- **Context budget fragmentation**: Six files may collectively exceed the context budget, forcing arbitrary truncation decisions about which files to prioritize
