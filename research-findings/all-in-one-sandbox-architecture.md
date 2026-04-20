---
name: All-in-One Sandbox Architecture
summary: Single Docker container packaging browser (VNC+CDP), shell, file system, IDE (VSCode), notebooks (Jupyter), and MCP servers with a shared filesystem. Eliminates cross-service communication overhead
  at the cost of seccomp:unconfined for browser support.
implementation_notes: null
category: Sandboxing
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: isolation-resolver-worktree-lifecycle-algorithm.md
  rel: same-problem
- file: os-level-agent-sandboxing-filesystem-network-isolation.md
  rel: same-problem
- file: three-tier-sandbox-provisioner.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A sandbox design where a single Docker container hosts all services an agent might need: browser (VNC + Chrome DevTools Protocol), shell (WebSocket terminal), file operations, IDE (VSCode Server), notebooks (Jupyter), and pre-configured MCP servers (browser, file, shell, markitdown). All services share the same filesystem (`/home/gem`), enabling seamless cross-tool workflows (e.g., browser downloads immediately available to shell commands). 15+ internal services orchestrated via port-readiness gating.

## Why It Matters

The alternative — separate containers per service — requires network communication between services, volume mounts for shared state, and complex orchestration. The all-in-one approach trades container isolation for operational simplicity and zero-latency cross-service access. For AI agent sandboxes where the primary threat model is agent-vs-external (not service-vs-service), this trade-off is often acceptable.

## Why People Are Using It

Observed in [AIO Sandbox](https://github.com/agent-infra/sandbox) v1.0.0.150 — see [[sandbox-analysis]] for structural details. 4.3k stars. Multi-SDK support (Python, TypeScript, Go) auto-generated from OpenAPI spec. Used in integration examples with AG2, LangGraph, OpenAI, Browser-Use, and Playwright.

## Potential Alternatives

- Separate containers per service with Docker Compose networking
- VM-based isolation (Firecracker, gVisor)
- Cloud sandbox-as-a-service (E2B, Daytona)

## Potential Improvements

Could add per-session cgroup isolation within the container for multi-agent scenarios where agents shouldn't see each other's processes or files.

## Potential Failure Modes

- `seccomp:unconfined` required for Chrome disables all kernel-level syscall filtering
- No per-session isolation — all agent sessions share the same user and filesystem
- Resource contention between 15+ services in a single container
- Optional authentication (JWT) means default deployment is fully open
