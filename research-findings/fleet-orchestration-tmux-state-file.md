---
name: "Fleet Orchestration via tmux + Atomic State File"
summary: "Meta-agent supervisor managing N parallel Claude Code instances via tmux with atomic JSON state writes. Implements checkpoint protocol (save-to-file before risky ops), session resume (re-read state after context loss), and convergence verification (dual clean-poll exit). A production-tested pattern for multi-agent coding coordination."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - file: "agent-management-tool-landscape.md"
    rel: extends
  - file: "parallel-subagent-wave-execution.md"
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: raw
consumed_by: []
---

## What It Is

AutoGPT's `/orchestrate` skill implements a meta-agent supervisor that manages N parallel Claude Code instances. The architecture uses tmux windows as agent containers, a shared JSON state file (`~/.claude/orchestrator-state.json`) with atomic writes (`jq + mv`), and a checkpoint protocol where agents output `CHECKPOINT:<step-name>` to signal progress.

**Key mechanisms:**
- **Agent states**: `running | idle | stuck | waiting_approval | complete | done | escalated`
- **Checkpoint protocol**: Agents signal progress via structured output; the orchestrator tracks completions
- **Convergence verification**: `/pr-polish` requires 2 consecutive clean polls 60s apart before accepting completion — accounts for delayed bot responses that create false "done" signals
- **Self-recovery**: Agents auto-recover from context compaction by reading the state file and running `gh pr view`
- **Serial resource management**: Only one `/pr-test` runs at a time due to shared ports/DB; the orchestrator owns the queue

## Why It Matters

Multi-agent coding coordination typically requires custom infrastructure — message queues, orchestration servers, or specialized frameworks. This pattern achieves production-grade fleet management using only tmux (process isolation), JSON files (state persistence), and standard CLI tools (git, gh). The infrastructure cost is zero.

The dual clean-poll exit pattern addresses a real failure mode in automated workflows: systems that declare "done" based on a single check, missing delayed reactions (CI bot comments, linter results arriving after the initial pass). Requiring two consecutive clean states separated by a time gap dramatically reduces false completion signals.

## Why People Are Using It

Observed in [AutoGPT](https://github.com/significant-gravitas/autogpt) v0.5.0 — see [[autogpt-analysis]] for structural details.

The orchestrator manages real development workflows: spawning parallel agents across worktrees, coordinating PR creation and review cycles, and handling the full lifecycle from task assignment to merge-ready verification. The 700+ line SKILL.md definition and multiple supporting scripts indicate production use, not a proof-of-concept.

## Potential Alternatives

- Custom orchestration server with WebSocket coordination: more robust communication but requires infrastructure deployment and maintenance.
- GitHub Actions-based parallelism: use CI runners as agent containers; gains infra management but loses interactive coordination.
- Claude Agent SDK's native multi-agent: framework-level support but less control over process isolation and state management.

## Potential Improvements

- Structured state schema validation to catch corruption from concurrent writes (currently relies on atomic mv but no schema checking).
- Health heartbeats from agents (periodic liveness signals) rather than relying solely on checkpoint outputs which may stop if an agent hangs silently.
- Dynamic agent pool scaling based on task queue depth rather than fixed N at orchestration start.

## Potential Failure Modes

- **tmux session fragility**: If the terminal session dies, all agents lose their parent process; recovery depends on session resume via saved session IDs.
- **State file contention**: Multiple agents writing state simultaneously could corrupt despite atomic mv if write timing collides (unlikely but possible with high parallelism).
- **Context compaction cascades**: If multiple agents compact simultaneously, the orchestrator may be overwhelmed with recovery coordination.
- **Silent agent death**: An agent that crashes without outputting a checkpoint or error signal appears as "running" indefinitely until the orchestrator's stuck-detection threshold fires.
