---
name: "Injection/Observation Split — Bridge plus Forwarder"
summary: |-
  When wrapping a vendor agent harness you don't control, omnigent fully decouples the two
  directions of integration: a bridge injects turns into the live vendor process (tmux
  keystrokes, JSON-RPC, REST — whatever the vendor exposes), while a separate runner-owned
  forwarder observes output (transcript-file tailing, SSE consumption, hook records) and
  mirrors it into a uniform event stream; the two meet only at a filesystem rendezvous. The
  executor just injects and yields TurnComplete — streaming is entirely the forwarder's job.
  For us this is the reference decomposition for driving any third-party interactive process:
  never make one component both drive and watch.
implementation_notes: null
category: "Agentic Systems"
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

Omnigent integrates eleven vendor harnesses (Claude Code, Codex, Cursor, OpenCode, ...) it does not control, and every integration follows the same role split, readable in the per-harness file families at package root: `X_native_bridge.py` handles **injection** — getting a turn into the resident vendor process by whatever channel exists (Claude: a bridge directory plus tmux send-keys typing into the user's pane; OpenCode: a state file carrying loopback URL, auth secret, and vendor session id) — while `X_native_forwarder.py` handles **observation** — a runner-owned background process mirroring the vendor's transcript into a uniform event stream (Claude: transcript-file tail plus hook records; OpenCode: SSE consumer with stable-id dedupe so web and TUI never double-post). The two halves share no in-process state; they meet at a filesystem rendezvous (`/tmp/omnigent-<uid>/claude-native/`, `~/.omnigent/opencode-native/<hash>/state.json`). The unifying executor (`native_server_harness.py`) is deliberately thin: resolve the session from bridge state, inject the prompt, yield `TurnComplete` — "streaming is the forwarder's job."

## Why It Matters

The naive wrapper couples driving and watching in one component, which then needs to be simultaneously synchronous (to inject) and event-driven (to observe), and every vendor quirk multiplies through both concerns. Splitting them means each half degrades independently — observation keeps mirroring output the user typed directly into the vendor TUI even when no injection happened, and injection still works when observation lags — and each half can use the channel best suited to its direction (keystrokes in, file-tail out). The filesystem rendezvous also survives process restarts on either side, which in-process coupling cannot.

## Why People Are Using It

Observed in [omnigent](https://github.com/omnigent-ai/omnigent) v0.6.0.dev0 (alpha) — see [[omnigent-analysis]] for structural details. The split is applied uniformly across all eleven native-harness families, strong evidence it is a load-bearing decomposition rather than one integration's accident.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| SDK/in-process integration | Use the vendor's programmatic API where one exists | Always, when offered — the split is for harnesses exposing only a TUI/server |
| Single wrapper process | One component drives and parses the PTY | Quick spikes; single-harness tools with no multi-client mirroring needs |
| PTY scraping | Screen-scrape the terminal for both directions | Last resort when neither transcripts nor events exist |

## Potential Improvements

- Formalize the rendezvous contract (what state each side may write) so third parties can author new harness families safely
- Health-check both halves independently and surface which direction is degraded

## Potential Failure Modes

- **Rendezvous corruption:** both halves trust the shared files; a stale or partial state file desynchronizes them
- **Observation lag as phantom failure:** injection succeeds but the forwarder misses output, and the turn looks hung
- **Vendor-format drift:** transcript/SSE formats are unversioned vendor internals; the forwarder breaks silently on upstream changes
