---
name: Sandbox Architecture by Threat Model (microVM vs Container)
summary: E2B and Daytona represent two architectural choices that map to distinct threat models — not pricing-tier differences. E2B uses Firecracker microVMs with a dedicated kernel per session (hardware
  isolation, ~150ms cold start, optimized for executing untrusted LLM-generated code). Daytona uses Docker containers with a shared kernel (27–90ms cold start, persistent workspaces, optimized for stateful
  agent workflows where packages/files must survive across interactions). The right choice is determined by "is the code untrusted?" — not by latency or pricing.
implementation_notes: MetaSystem does not currently sandbox agent code execution. If S3 (Claude Build) ever runs LLM-generated code against real repos, the microVM-vs-container choice maps directly onto
  MetaSystem's risk model — code drafted by research agents against repo-cache is untrusted-ish (container plausible); code drafted against production Household OS Notion would be untrusted (microVM required).
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- northflank-daytona-vs-e2b-2026.md
- zenml-e2b-vs-daytona-2026.md
- from-fork-to-fleet-agent-sandbox-cloud.md
related_findings:
- file: three-sandbox-architectures-comparison.md
  rel: extends
- file: all-in-one-sandbox-architecture.md
  rel: same-problem
- file: three-tier-sandbox-provisioner.md
  rel: same-problem
- file: incremental-snapshotting-copy-on-write-block-diffing.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
- agent-safety-and-permissions.md
---

# Sandbox Architecture by Threat Model (microVM vs Container)

## What It Is

Two agent sandboxes — E2B and Daytona — were built with different architectural first principles that map directly onto threat models:

- **E2B (Firecracker microVM)**: Each code execution gets a dedicated Linux kernel with hardware-level isolation. Cold start ~150ms. Per-sandbox resource ceiling: up to 8 vCPU / 8 GiB RAM. Focused on running untrusted LLM-generated code; the isolation boundary is a syscall boundary, not a namespace boundary.
- **Daytona (Docker container)**: Shared-kernel containers with stateful workspaces — package installs and file edits persist across agent reconnects. Cold start 27–90ms (industry-leading). Per-sandbox cap ~4 vCPU / 8 GB RAM, but larger org-wide pools and GPU access. Focused on agents that need to maintain state across many interactions.

Pricing structures reinforce the split: E2B charges a base fee ($150/month for Pro features) plus usage; Daytona is pure usage-based.

Concrete mechanics behind the microVM approach, per OpenAI's talk: the modern generation of microVM hypervisors (VMMs) is Rust-based rather than the older C-based QEMU — CrosVM (built at Google for Linux VMs on Chromebooks) was the first, Firecracker forked CrosVM for AWS Lambda/serverless, and Cloud Hypervisor is a more general, multi-vendor VMM built on the same lineage. Memory safety (Rust) plus per-device jailing (the emulated block device and network device are sandboxed separately, so compromising one does not grant access to the other) are the two safety properties this generation adds over QEMU. "MicroVM" describes the VMM's own footprint — fewer supported devices, less legacy code, faster boot — not anything about what runs inside the guest. Spin-up sequence: the harness forks a VMM binary (e.g., Cloud Hypervisor), which exposes an API over a Unix domain socket; a `create` call supplies rootfs/kernel/CPU/memory, and a `start` call boots the guest through the kernel's `/dev/kvm` interface. The sandboxed guest exposes its own PID-1 API server that the harness talks to over Vsock (or the guest's IP stack) for control operations such as "save your state."

## Why It Matters for Us

Plain English: the question "which sandbox should our agent use?" is not a pricing comparison. It's a safety comparison. If the agent runs code we didn't write — code the model generated on the fly — you want hardware isolation (microVM). If the agent runs code *we* wrote and it just needs to keep its Python env around between turns, a container is cheaper, faster, and adequate. Picking the wrong sandbox for the wrong threat model means paying for isolation you don't need (Daytona-as-E2B) or not getting the isolation you do need (E2B-as-Daytona).

## Why People Are Using It

E2B's Firecracker approach is Anthropic's own choice for Claude Code's code-execution tool and is the standard among teams running adversarial-risk agents. Daytona's persistence-first model matches dev-loop agents (coding copilots, research notebooks) where statelessness would destroy the workflow. Multiple practitioner comparisons (Northflank, ZenML, Superagent, Lifo) converge on this threat-model framing rather than pricing.

A third independent production system corroborates the microVM choice at even larger scale: OpenAI's agent-infrastructure team runs Firecracker-class microVMs (via Cloud Hypervisor) as the sandbox for ChatGPT and Codex Web, reached by walking the same threat-model ladder from first principles — fork/exec (fastest, zero isolation: the forked process can attack the kernel directly, and an unbounded fork loop makes a sandbox a noisy neighbor) → containers (Linux namespaces + cgroups isolate resources, but all containers still share the host kernel; `seccomp` filters reduce the attack surface but create a bad iteration loop for products that want agents to "do crazy things" — unanticipated syscalls get blocked until the filter is manually widened) → gVisor (a user-space kernel — the "Sentry" process implements the Linux API itself, with a separate "Gopher" daemon for filesystem access — turning a direct kernel exploit into a two-step chain, since Sentry and Gopher still run on top of the host kernel and can themselves be chained through) → hardware-virtualized microVMs (the guest kernel genuinely runs in a separate CPU privilege context — VMX non-root vs. the host's VMX root — so the host stays protected even if the guest is fully compromised). The team's own framing: nearly every team that tries cheaper isolation first eventually wants a full microVM anyway ("the seven stages of grief"), and the direct recommendation for anyone starting a new sandbox is to skip the intermediate stages: "just use micro VMs from the start."

## Potential Alternatives

- **Worktree isolation** (GSD, Archon) — file-level only, no process or network containment; cheapest but unsafe for untrusted code
- **Modal** — serverless containers with strong per-function isolation
- **Sprites.dev** — emerging alternative
- **Kubernetes-backed provisioner** (DeerFlow pattern) — most flexible, most complex

## Potential Improvements

A "graduated sandboxing" pattern that defaults to containers and escalates to microVMs when the task classifier flags untrusted code — this is a forward extension of the existing three-tier-sandbox-provisioner finding.

## Potential Failure Modes

- Untrusted-code workload mis-routed to container-based sandbox → container escape is a realistic compromise path
- Stateful workflow forced onto microVM → every session starts from scratch; the persistence premise breaks
- Per-sandbox resource ceilings (both providers) bite large-batch workloads before pricing does
- OpenAI's talk corroborates and sharpens this finding's cost side: guest/host context switches carry real performance overhead; memory reclaim requires a balloon driver and is reactive, not immediate (the guest must be asked to give memory back, it can't be reclaimed on demand); and GPU access is hard inside a microVM — `virtio-GPU` gives only high-level graphics-library access, while `VFIO` gives direct hardware access but can only be held by one sandbox at a time (no multi-tenant sharing)
