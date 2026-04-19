---
name: Three Sandbox Architectures for Agent Execution
summary: 'Three distinct sandbox architectures observed: worktree isolation (GSD, Archon), monolithic container (AIO Sandbox), graduated provisioner (DeerFlow). Each trades complexity for isolation differently.'
implementation_notes: null
category: Sandboxing
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: all-in-one-sandbox-architecture.md
  rel: same-problem
- file: three-tier-sandbox-provisioner.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A cross-repo comparison finding: three distinct sandbox architectures serve agent execution with different tradeoffs:

1. **Worktree isolation** (GSD, Archon) — Git worktrees provide filesystem isolation without containers. Lightweight, no Docker dependency. Archon adds a 7-step IsolationResolver with branded types. Limited to file-level isolation; no process or network isolation.

2. **Monolithic container** (AIO Sandbox) — Single Docker container with all services (browser, shell, IDE, MCP). Shared filesystem enables cross-tool workflows. Trade-off: `seccomp:unconfined` required for browser disables syscall filtering. No per-session isolation within the container.

3. **Graduated provisioner** (DeerFlow) — Three-tier provider (local → Docker pool with LRU → Kubernetes) behind a unified `SandboxMiddleware` interface. Configuration-driven isolation level. Most flexible but most complex.

## Why It Matters

As agent autonomy increases, sandboxing becomes critical for safety. These three architectures represent the full tradeoff spectrum: worktrees are simplest and cheapest but least isolated; containers provide OS-level isolation but are heavier; provisioners add flexibility but significant infrastructure complexity. The choice depends on threat model, infrastructure budget, and operational maturity.

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Observed across [GSD](https://github.com/coleam00/gsd), [Archon](https://github.com/coleam00/archon), [AIO Sandbox](https://github.com/agent-infra/sandbox), and [DeerFlow](https://github.com/bytedance/deer-flow).

## Potential Alternatives

- No sandboxing (trust the agent — risky at scale)
- VM-based isolation (Firecracker, gVisor — heaviest)
- Cloud sandbox-as-a-service (E2B, Daytona — external dependency)

## Potential Improvements

A graduated approach that starts with worktrees (cheapest) and escalates to containers/K8s based on task risk classification. DeerFlow's provisioner pattern is closest to this.

## Potential Failure Modes

- Worktrees provide no network or process isolation
- Containers require Docker infrastructure and add startup latency
- K8s provisioners add significant operational complexity
