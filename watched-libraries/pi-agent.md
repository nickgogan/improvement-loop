---
name: "Pi Agent Harness"
url: "https://github.com/earendil-works/pi"
stars: "~5k"
spectrum_position: "study"
spectrum_rationale: "Self-modifying agent architecture with runtime extension API, session branching, multi-provider LLM abstraction, and supply-chain hardening. Directly relevant to MetaSystem's skill/extension patterns and context management."
current_version: "latest (commit e007fcd)"
last_checked: "2026-07-18"
tracking_focus:
  - "Extension API: runtime tool registration, event hooks, provider registration"
  - "Session management: branching, compaction, tree navigation"
  - "Skills system: frontmatter-based, model-invocable"
  - "Supply-chain hardening: pinned deps, shrinkwrap, pre-commit lockfile checks"
  - "Community extension packages: pi-agent-sub-agents (specialized sub-agent roles over the extension API)"
tags:
  - "coding-agent"
  - "self-modifying"
  - "extension-api"
  - "session-management"
  - "typescript"
date_added: "2026-05-24"
---

# Pi Agent Harness

Open-source self-extensible coding agent CLI by earendil-works (Mario Zechner). Monorepo with 4 packages: `pi-ai` (unified multi-provider LLM API), `pi-agent-core` (agent runtime), `pi-coding-agent` (interactive CLI), `pi-tui` (terminal UI).

## Why We Watch

Pi is the most extensible open-source coding agent — designed to be modified at runtime by the agent itself. The extension API exposes 30+ lifecycle events, tool registration, command registration, provider registration, UI customization, and session control. This is the "self-modifying agent" archetype the Pragmatic Engineer newsletter highlighted.

## Key Architectural Features

- **Extension system**: TypeScript modules subscribing to lifecycle events (session, agent, tool, model, input). Can register tools, commands, shortcuts, providers, message renderers.
- **Session tree**: Branching, compaction, tree navigation with summaries. Sessions persist as files.
- **Multi-provider**: Unified API across Anthropic, OpenAI, Google with OAuth support and dynamic provider registration.
- **Skills**: Frontmatter-based markdown files (name, description, disable-model-invocation). Loaded from project and global dirs.
- **Supply-chain hardening**: Exact-pinned deps, `min-release-age=2`, shrinkwrap generation, pre-commit lockfile checks, no lifecycle scripts by default.

## Notable Extensions

- **pi-agent-sub-agents** (community package, reportedly the most-downloaded Pi
  package): splits a single bloated agent into specialized sub-agent roles
  (Scout/Oracle/Worker/Reviewer/ContextBuilder/Delegate) so the main session stays
  lean — the demo reports ~9% context usage in the main session after a heavy
  multi-agent research pass. Cross-harness confirmation of the engine's own
  Owner/Researcher/Codifier/Librarian split; also confirms the extension API carries
  real third-party ecosystem weight (same API the "Intercom" cross-terminal comms
  extension exercises). Source: setting-up-pi-subagents video (2026-05-18); no
  package repo URL stated in the transcript.

## Spectrum Notes

Full study — the extension API architecture and session management patterns are directly relevant to MetaSystem's skill system design and context engineering research.
