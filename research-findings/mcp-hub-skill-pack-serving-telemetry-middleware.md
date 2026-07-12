---
name: 'MCP Hub Serving the Skill Pack to Any Agent, with Telemetry Middleware Wrapping Every Tool'
summary: 'The canonical skill pack is exposed through a TypeScript MCP server (stdio + loopback HTTP transports over one service layer), making the same skills, prompts, catalogs, roles, and concept tree available to ANY agent — not just the harness on the author''s laptop. Two serving distinctions: search_* tools do substring/metadata matching ("find a known item") while recommend_* tools do relevance ranking ("rank for a described task"). Every tool is registered through an instrumentedRegisterTool wrapper — never the raw registration call — so every invocation is captured (status, duration, redacted args, console output) to a telemetry log with replay (hub_resync_call) and inspection (hub_get_call_card) tools built on top.'
implementation_notes: 'Watch-tier for the engine today (local-first, single operator), but this is the end-state architecture for the planned asset catalog as a retrieval-reuse surface: once assets live in a canonical generated registry, an MCP layer over that registry is what makes them consumable by agents that don''t share the filesystem — the catalog stops being a directory and becomes a service. Two details are adoptable independently of MCP: (1) the search-vs-recommend split (known-id lookup vs described-need ranking) is a clean contract for any /ask-kb-like surface — the writeup notes picking the wrong one is the top reason queries return nothing useful; (2) the never-raw-registration telemetry rule is the observability analog of the engine''s generator-assessor separation — instrumentation by construction, not by discipline, with the enforcing convention that any tool change must land in service, server, tests, and the tool inventory together. Loopback-only HTTP (127.0.0.1) as an explicit trust boundary matches the engine''s local-first posture.'
category: Tool Integration
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P3 (Watch)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: two-tree-model-authoring-vs-canonical-generated-pack.md
  rel: enabled-by
pipeline_status: raw
consumed_by: []
tags:
- mcp-server
- telemetry-middleware
- asset-serving
- observability
---

# MCP Hub Serving the Skill Pack to Any Agent, with Telemetry Middleware

## What It Is

The runtime half of the context-hub system: a single-package TypeScript MCP server that loads
the generated registries (skills, prompts, six catalogs, roles, concept tree) into an
in-memory cache at start and serves them as a `hub_*` tool family:

```
registry.ts ─► service.ts ─► server.ts ─► index.ts  (stdio)
   (load)       (logic)     (register)  └► http.ts   (loopback HTTP :3939 /mcp + /healthz)
                                  ▲
                            telemetry.ts (wraps every tool)
```

Tool groups mirror the catalogs: skills (`hub_list/get/search/recommend_skills`,
`hub_build_skill_bundle`), prompts (incl. `hub_optimize_prompt`, `hub_save_prompt`),
libraries (MCP servers / repos / shared code / URLs), roles (`hub_role_list/recommend/
resolve_skills`), concept tree (`hub_concept_tree_*`), coding patterns, per-file
analysis state, dependency/staleness reports (`hub_dependency_graph`,
`hub_impact_analysis`, `hub_staleness_scan`), and telemetry/ops.

## Why It Matters

Plain English: file-based skill libraries only help agents that can read the files. The
moment a second operator, a background agent, or a cloud agent needs the same knowledge,
the library has to become a *service*. This shows the shape of that move: same canonical
pack, one service layer, two transports — a teammate clones the repo, runs the server,
points `.mcp.json` at loopback, and has the identical skill pack, prompt library, and
catalogs without copying anyone's home directory. Mid-task, an agent can ask
`hub_recommend_skills "private-endpoint networking"` instead of guessing — the hub acts
as a remote skill index.

The telemetry rule matters on its own: because instrumentation happens at registration
(middleware), coverage is total by construction. There is no such thing as an unlogged
tool call, and debugging a flaky tool is a lookup (`hub_get_call_card`) plus a replay
(`hub_resync_call`), not a code change.

## How It Works

- **Search vs recommend.** `search_*` is substring/metadata matching for a known
  id/term; `recommend_*` is relevance ranking for a described need. The docs call
  choosing wrong "the most common reason a hub query returns nothing useful."
- **Instrumented registration.** Every tool is wrapped by `instrumentedRegisterTool`;
  `server.registerTool` is never called directly. The middleware captures per-call
  status, duration, redacted args, console output, and suggested fixes; persists to
  `file-analysis/telemetry.jsonl`; and exposes in-memory history via
  `hub_get_call_history` / `hub_get_call_card` / `hub_resync_call`.
- **Change discipline.** Any tool change lands in three places together — `service.ts`,
  `server.ts`, `tests/mcp-server.test.ts` — plus `docs/tool-inventory.json`; versions in
  `package.json` and `constants.ts` move in lockstep.
- **Trust boundary.** The HTTP transport binds `127.0.0.1:3939` and is treated as
  trusted loopback; transport changes with security impact require documentation before
  merge.
- **Resources and prompts, not just tools.** Each skill/prompt asset is also registered
  as a dynamic MCP *resource*, and each saved prompt as an MCP *prompt* entry — the pack
  is native MCP surface area, not blobs behind a query tool.

## How It Could Fail

- **In-memory cache staleness.** The registry loads at server start; a sync while the
  server runs serves stale assets until restart.
- **Telemetry redaction gaps.** Logging every call's args is an observability win and a
  data-hygiene liability; redaction has to keep pace with new tool schemas.
- **Loopback assumption erosion.** The trusted-local-client posture breaks silently if
  the port is ever exposed; the design depends on that never happening casually.
