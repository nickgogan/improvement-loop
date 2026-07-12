---
name: "Stateful Tools: Long-Lived MCP Subprocess Beats Per-Call CLI Shell-Out"
summary: |-
  A boundary condition on the KB's CLI-first rule: when the tool holds state (an open
  database, a warm engine), a long-lived local MCP stdio subprocess beats shelling out
  to the tool's CLI per call. Each CLI invocation pays full process startup plus
  database open/close, forces the model to compose flags and scrape stdout instead of
  using typed tool schemas, and adds one shell-approval surface per command. The MCP
  subprocess is one process holding the DB open, exposing typed tools, dying with the
  session. Demonstrated with Gbrain: CLI shell-out "works, but is worse as a process"
  — the MCP path was visibly faster.
implementation_notes: |-
  Nuances (does not overturn) the P1 finding cli-first-tool-integration-less-overhead-
  than-mcp and its extracted rule prefer-cli-over-mcp-when-both-exist: that evidence
  came from stateless tools where the CLI shares the terminal environment natively.
  The decision input is statefulness: stateless tool → CLI-first still holds; stateful
  local service (open DB, long-lived engine) → local stdio MCP subprocess. Candidate
  refinement for the extracted rule's applicability clause — flag to the Codifier.
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "IL (tool integration guidance)"
adopted_in: []
sources:
  - "give-your-ai-agent-a-second-brain-gbrain-hermes.md"
related_findings:
  - file: "cli-first-tool-integration-less-overhead-than-mcp.md"
    rel: "extends"
  - file: "markdown-git-system-of-record-derived-disposable-db.md"
    rel: "enabled-by"
  - file: "mcp-n-plus-m-integration-economics.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A statefulness-based decision rule for how an agent should talk to a local tool.
Gbrain exposes ~47 engine operations two ways, and the source demonstrates both:

- **CLI shell-out (per call):** the model composes CLI flags, runs the command through
  the terminal tool, and scrapes stdout. Every call pays full process startup and
  opens/closes the PG lite database. Every command is another shell-approval surface.
  It works, "but it is worse as a process."
- **Local MCP stdio subprocess (long-lived):** the agent spawns `gbrain serve` once as
  a subprocess — no HTTP server, no tunnel, no token. The engine operations are exposed
  as 30+ typed MCP tools with structured inputs/outputs; the one process holds the
  database open for the session and dies with it. Observed result: noticeably faster
  responses and no per-command approval friction.

The generalization: the CLI-vs-MCP choice is not about protocol preference but about
where state lives. Stateless tools amortize nothing across calls, so CLI's zero
protocol overhead wins. Stateful tools amortize startup + connection + schema across
the session, so the long-lived typed server wins.

## Why It Matters

The KB holds a Strong-evidence P1 finding (and an extracted rule) that CLI beats MCP
for Claude Code — built on stateless cases like Playwright. Applied blindly to a
stateful knowledge engine, that rule produces the demonstrably worse integration. This
finding supplies the boundary: same trade, opposite winner, and the discriminator is
whether the tool holds session state worth keeping open.

## Why People Are Using It

Gbrain's own docs steer users to the MCP path; the source verifies the difference
live in Hermes Agent (side-by-side: CLI shell-out per query vs MCP tools after
registration). The stdio-subprocess shape — local, tokenless, session-scoped — also
avoids the security and lifecycle costs that the KB's MCP-skeptical findings attach to
hosted MCP servers.

## Potential Alternatives

Keeping a CLI but running it against a daemonized service (tool-side state, agent
still shells out) — recovers amortization but keeps flag-composition and
stdout-scraping costs. Code-execution-over-MCP patterns that batch many operations
into one call.

## Potential Improvements

A written discriminator checklist for tool-integration reviews: does the tool open a
connection/database/index per call? Is there a session-scoped serve mode? Count the
shell-approval surfaces the CLI path adds.

## Potential Failure Modes

Long-lived subprocesses can hold stale state after the underlying markdown/DB changes
externally (needs reload semantics — the source had to reload the MCP server to pick
up new tools). Tool-count bloat: Gbrain registered 100+ MCP tools after setup, which
is its own context-window tax on tool schemas.
