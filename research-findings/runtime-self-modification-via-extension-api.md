---
name: "Runtime Self-Modification via Extension API"
summary: "Agent harness exposes a typed extension API allowing runtime registration of tools, providers, commands, keyboard shortcuts, and message renderers. Extensions subscribe to 30+ lifecycle events (session, agent, tool, model, input) and can intercept/modify behavior at every stage. The agent can build its own extensions, making it genuinely self-modifying."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "dynamic-tool-pool-assembly-transcript-compaction.md"
    rel: "extends"
  - file: "progressive-skill-loading.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "rules/runtime-extension-governance-policy.md"
---

# Runtime Self-Modification via Extension API

## Pattern

An agent harness exposes a strongly-typed extension API that allows runtime (not just config-time) registration of:
- **Tools** (LLM-callable, with TypeBox parameter schema + execute + render)
- **Providers** (add/override LLM providers including OAuth, custom stream handlers)
- **Commands** (slash commands with argument completion)
- **Keyboard shortcuts**
- **Message renderers** (custom display for custom message types)
- **Event handlers** (30+ lifecycle events covering session, agent loop, tool execution, model selection, and input)

Extensions are TypeScript modules loaded via `jiti` (runtime TS evaluation). They can be created by the agent itself during a session, making the system genuinely self-modifying — the agent can extend its own capabilities.

## Why It Matters

This is the architectural enabler for "self-modifying agents" — the agent doesn't just execute within a fixed tool set, it can reshape its own capabilities based on task requirements. Compared to static config (CLAUDE.md, settings.json), this allows behavioral changes without restarting the session.

## How It Could Fail

- Extension conflicts (two extensions registering the same tool name)
- Security: agent-created extensions bypass human review
- Complexity explosion: too many extensions create unpredictable interaction effects
- Runtime TS eval (jiti) has performance and sandboxing implications

## Evidence

Pi agent harness (earendil-works/pi) — 1500-line `types.ts` defining the full extension API, `loader.ts` with jiti for runtime TypeScript evaluation, `runner.ts` for execution. Production-tested in the pi coding agent CLI.
