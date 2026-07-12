---
name: "Plugins Are SDK Clients"
summary: |-
  opencode plugins receive, as their construction input, the same generated HTTP client the
  TUI, desktop app, web app, and Slack bot use — a plugin is just another peer on the one
  client/server protocol seam, plus hook registrations. There is no separate "plugin API" to
  design, document, version, or let lag behind the product surface: anything the first-party
  clients can do, a plugin can do, automatically and forever. For us this is the
  minimum-abstraction answer to extensibility — reuse the existing protocol seam instead of
  inventing a second, narrower one.
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

opencode's plugin contract (`packages/plugin/src/index.ts`): a plugin is a function `(input) => Promise<Hooks>` whose `input` includes `client` — an instance of the same generated, typed SDK the TUI, desktop, web app, and Slack bot use against the local server — along with `serverUrl`, a Bun shell, and project/worktree handles. Extension-specific behavior comes from the returned hooks (permission overrides, tool wrapping, prompt transforms, auth flows), but all *capability* — reading sessions, sending messages, querying config, driving the agent — flows through the one HTTP protocol seam that `packages/protocol` defines and codegen keeps typed.

## Why It Matters

The default extensibility design is a bespoke plugin API: a hand-curated subset of product capability, separately documented and versioned, perpetually behind the product's real surface. Handing plugins the first-party client dissolves that entire layer. Capability parity is structural (a new server route is instantly available to plugins because the client is regenerated, not because someone extended the plugin API), the seam is already exercised by every first-party client, and plugin authors learn one API instead of two. It is the extensibility variant of reuse-before-invention: the protocol seam already existed; plugins just became another consumer of it.

## Why People Are Using It

Observed in [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[opencode-analysis]] for structural details. The repo's whole client fleet — TUI, Electron desktop, web app, Slack bot, enterprise surface, *and plugins* — are peers on the single `HttpApi` seam with websocket event streaming.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Curated plugin API | Hand-designed capability subset | When plugins are untrusted and capability must be scoped per-plugin |
| In-process extension points | Hooks only, no client | Extensions that only transform, never initiate |
| Scripting interface | Embedded language with bindings | End-user automation rather than developer extension |

## Potential Improvements

- Per-plugin capability scoping (the flat client grants everything — see failure modes)
- Version-skew contract: state which client versions a plugin binary may assume

## Potential Failure Modes

- **No privilege boundary:** every plugin gets the full first-party surface; a malicious or buggy plugin can do anything the TUI can — this pattern trades sandboxing for parity
- **Protocol churn hits plugins first:** first-party clients are regenerated in-repo on seam changes; out-of-tree plugins discover breaks at runtime
- **Local-server assumption:** the design presumes a reachable local server; plugins inherit that topology constraint
