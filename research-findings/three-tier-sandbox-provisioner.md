---
name: "Three-Tier Sandbox Provisioner"
summary: "Graduated sandbox isolation behind a unified interface: local filesystem (dev) → Docker container pool with LRU eviction (staging) → Kubernetes remote backend (production). Same SandboxMiddleware regardless of provider."
implementation_notes: null
category: "Sandboxing"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - {file: "tiered-permission-system-bash-safety.md", rel: "same-problem"}
proposals: null
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
---

## What It Is

A sandbox provisioner pattern with three graduated tiers behind a unified interface: (1) `LocalSandboxProvider` — files on host filesystem, bash disabled by default, for development/low-risk tasks. (2) `AioSandboxProvider` — Docker container pool with LRU eviction, idle timeout (600s), configurable replica limits, for staging/moderate-risk tasks. (3) Provisioner/Kubernetes — remote backend on port 8002 for K8s-managed sandboxes, for production/high-risk tasks. The `SandboxMiddleware` wraps the entire agent turn — acquires sandbox before execution, releases after — and the agent code is identical regardless of which provider is active.

## Why It Matters

The existing KB covers tiered permissions (bash safety modules) but not tiered execution environments. This pattern separates the concern of "how isolated should this be?" from "what should the agent do?" The provider selection is a configuration decision, not a code change. This enables gradual rollout: start with local, move to Docker when ready, move to K8s for production.

## Why People Are Using It

Observed in [DeerFlow](https://github.com/bytedance/deer-flow) v2.0 — see [[deer-flow-analysis]] for structural details. DeerFlow's `config.yaml` → `sandbox.use` selects the provider. The Docker pool implementation includes LRU eviction, idle timeout, and replica limits — production-grade container lifecycle management.

## Potential Alternatives

- Single-tier sandboxing (always Docker, or always local)
- Cloud sandbox-as-a-service (E2B, Daytona — external dependency)
- VM-based isolation (Firecracker)

## Potential Improvements

Could add a fourth tier for ephemeral cloud sandboxes (serverless functions) for the cheapest/fastest option on trivial tasks.

## Potential Failure Modes

- Behavioral differences between tiers (code works locally but fails in Docker)
- Docker pool management complexity (LRU eviction, resource leaks)
- K8s provisioner adds significant infrastructure requirements
