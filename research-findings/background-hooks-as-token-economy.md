---
name: Background Hooks as Token Economy for Memory Bookkeeping
summary: 'Move all memory-bookkeeping work (filing, indexing, timestamping, diary entries) out of the chat window into background harness hooks (Stop, PreCompact). Observable change: the founder measured
  ~$1.13 per session in retransmitted diary blocks when bookkeeping ran in-band; moving it to hooks drops that to $0 because the content never enters the chat. Hooks can also coerce the model into a save
  turn via `{"decision": "block", "reason": "..."}` with a `stop_hook_active` infinite-loop guard.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: null
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: claude-code-hooks-for-automatic-session-memory.md
  rel: extends
- file: typed-edge-knowledge-graph-token-reduction.md
  rel: same-problem
- file: bounded-tiered-memory-inference-driven-curation.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-05-24'
pipeline_status: raw
consumed_by: []
---

## What It Is

Two coordinated patterns for running memory work outside the chat window:

1. **Hook-driven auto-ingest.** On `Stop` or `PreCompact`, a hook script parses the session's JSONL transcript, extracts tool output and conversation turns, and writes them to the memory store directly — without the model authoring anything in-window. This captures raw tool output (bash results, search findings, build errors) regardless of whether the model would have summarized them away.
2. **Block-reason coercion with loop guard.** When the hook fires, it returns a JSON decision: `{"decision": "block", "reason": "save tool output verbatim to the palace before stopping"}`. The harness refuses the stop, passes the reason to the model, and the model writes its save turn. Once the model tries to stop a second time, the hook sees `stop_hook_active = true` and returns `{}` — letting the stop proceed. Without the flag check, the hook would loop forever.

Combined: the hook captures what tool output happened mechanically, and the block-reason coerces the model to add its own interpretation. Two layers, guaranteed capture, zero tokens in the chat window for the mechanical part.

Quantified: MemPalace's founder note reports the change from $1.13 per session (when the model wrote diary blocks in-chat, which then got retransmitted on every subsequent turn) to $0 after moving the work to background hooks.

## Why It Matters

Anywhere a system adds "automatic" work that helps the agent be better — governance logging, cross-references, audits, capture of tool output, session summaries — the default is to have the model do it in-window. That work accumulates token cost on every subsequent turn because the harness retransmits the chat history. Moving it to hooks is a one-time cost change that scales with session length.

For MetaSystem: the `/session-handoff` and `/governance-audit` skills both do post-session work that could run as hooks. The IL's delta reports, the Owner's drift detection, and Session Log entries are candidates. The pattern reinforces the standing `feedback_token_economy.md` rule (no content that requires per-session maintenance in the chat window).

Extends [[claude-code-hooks-for-automatic-session-memory]] — the existing finding covers the three-hook pattern (session_start, pre_compact, session_end) for memory capture; this finding adds the *cost-quantification framing* and the *block-reason coercion mechanism* as distinct load-bearing patterns.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. The two hooks are `.claude-plugin/hooks/mempal-stop-hook.sh` (or the repo-root authoritative versions in `hooks/mempal_save_hook.sh`) and `mempal-precompact-hook.sh`, wired via `hooks.json`. The `hooks/README.md` documents the two-layer capture pattern explicitly: "Hooks auto-mine the JSONL transcript directly into the palace (capturing raw tool output — Bash results, search findings, build errors). They also block the AI with a reason message telling it to save verbatim tool output and key context. Belt and suspenders — tool output gets stored even if the AI summarizes instead of quoting." The `stop_hook_active` flag is explicitly documented as the infinite-loop prevention mechanism. The MISSION.md (by co-founder Milla Jovovich) tells the origin story: the model was writing the same diary block repeatedly in-window, which triggered the architectural move.

## Potential Alternatives

- **In-band model writes** — the model saves to memory in the chat, which the harness then retransmits on every turn. Observable cost ~$1.13/session per MemPalace's measurement.
- **Manual CLI invocation** — user runs `/save` at session end. Works if the user remembers; silently loses data when they don't.
- **Separate daemon** — an always-on process tails the transcript file. Works but adds a process-lifetime dependency.
- **Model-initiated tool calls** — the model decides when to save. Suffers the same retransmission cost as in-band writes and is vulnerable to the model forgetting to save.

## Potential Improvements

- **Threshold tuning** — MemPalace's Stop hook triggers every 15 human messages. Too frequent adds latency to normal stops; too infrequent loses data. Dynamic threshold based on content volume (token count, tool-output bytes) could be more robust.
- **Parallel hook exec** — long-running hooks block the stop. Async execution with a progress file would reduce user-facing latency.
- **Hook-to-hook handoff** — a Stop hook that starts async work and hands off to a subsequent harness event (e.g., SessionEnd) would decouple capture latency from stop latency.

## Potential Failure Modes

- **Hook install requires session restart.** Claude Code loads hooks at session start only. Mid-session installs don't fire until restart. Surprises users who think the hook is live.
- **PATH issues on GUI-launched harnesses.** When Claude Code or Codex CLI is launched via Spotlight, dock, or `open -a` on macOS, the environment PATH is the minimal `/usr/bin:/bin:/usr/sbin:/sbin` from launchd, not the user's shell PATH. Hooks that invoke `python3` or other tools can fail mysteriously. MemPalace documents a `MEMPAL_PYTHON` env override as the mitigation.
- **Silent hook failure.** If the hook script crashes, data is lost and the user doesn't know. Logging to a known location (MemPalace uses `~/.mempalace/hook_state/hook.log`) is the minimum; alerting is harder.
- **Coercion abuse.** The `{"decision":"block","reason":"..."}` pattern gives the hook author power to override user intent. If misused, it forces the model into unwanted turns. Short, specific reasons and the loop-guard flag are the discipline; abuse looks like repeated blocks for low-value reasons.
