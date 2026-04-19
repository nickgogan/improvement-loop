---
title: "OS-Level Agent Sandboxing -- Filesystem and Network Isolation"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "os-level-agent-sandboxing-filesystem-network-isolation"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A coding agent or tool-using agent executes commands with filesystem and/or network access. The host OS supports process-level sandboxing primitives (Linux bubblewrap, macOS seatbelt, or equivalent). The agent's working directory and required network endpoints are known at session start."
  invariants: "Filesystem writes are restricted to the designated working directory and its descendants. Network traffic is routed through a proxy that enforces domain allowlisting. Credentials never enter the sandbox -- they are held by an external proxy that attaches authentication after validation. Both filesystem and network isolation are enforced simultaneously."
  governance: "Sandbox profiles are reviewed when project requirements change (new directories, new network endpoints). Domain allowlists are maintained per project and audited periodically. Credential proxy configurations are owned by the platform team, not the agent. Sandbox escape attempts are logged and surfaced for review."
  recovery: "If the sandbox blocks a legitimate operation, add the required path or domain to the profile and restart the session. If a sandbox escape is detected, terminate the session, revoke any exposed credentials, audit the escape vector, and patch the sandbox profile before restarting."
tags:
  - "extracted-artifact"
  - "pattern"
---

# OS-Level Agent Sandboxing -- Filesystem and Network Isolation

**Source:** [[os-level-agent-sandboxing-filesystem-network-isolation]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Coding agents execute arbitrary commands with access to the host filesystem and network. Permission-based approval models create approval fatigue (93% approval rate in production data), meaning users rubber-stamp dangerous operations. Even with permission systems, a compromised or prompt-injected agent can exfiltrate sensitive files (SSH keys, credentials) over the network, or escape project boundaries to gain broader system access.

## Forces

- **Safety vs. productivity:** Permission prompts protect against dangerous actions but interrupt flow and train users to approve blindly. The safer the system tries to be through prompts alone, the more fatigued users become.
- **Isolation vs. capability:** Strict sandboxing prevents legitimate operations that require system-wide file access or diverse network endpoints. Overly tight boundaries make the agent unusable for real work.
- **Container overhead vs. coverage:** Container-based isolation (Docker, VMs) provides strong boundaries but adds startup latency, resource overhead, and management complexity. Lighter approaches sacrifice coverage.
- **Filesystem isolation vs. network isolation:** Either dimension alone is insufficient. Without network isolation, a filesystem-confined agent can still exfiltrate data. Without filesystem isolation, a network-confined agent can escape to gain network access through system tools.

## Solution

Enforce two isolation dimensions simultaneously using OS-level primitives rather than containers:

**Filesystem Isolation:**
- Restrict read/write access to the current working directory and its descendants
- Use OS-native sandboxing: Linux bubblewrap (`bwrap`) or macOS seatbelt (`sandbox-exec`)
- Coverage extends to all subprocesses -- scripts, compiled programs, and child processes inherit the sandbox constraints
- Blocks modifications outside the project boundary at the kernel level, not through prompt instructions

**Network Isolation:**
- Route all internet access through a Unix domain socket to an external proxy server
- The proxy enforces a domain allowlist -- only pre-approved domains receive traffic
- New domain requests surface for user confirmation (one-time approval, not per-request)
- Customizable rules for arbitrary outgoing traffic patterns

**Credential Proxy (for cloud/remote sessions):**
- Sensitive credentials (git tokens, signing keys, API keys) remain outside the sandbox
- A dedicated proxy handles authenticated interactions: the sandboxed agent uses scoped, limited credentials; the proxy verifies the interaction (e.g., push only to configured branch) before attaching real authentication tokens
- A compromised sandbox cannot access, read, or exfiltrate real credentials

The OS-primitive approach avoids container management overhead while covering all subprocesses. Both dimensions must be enforced together -- either alone leaves an exploitable gap.

## Consequences

**Positive:**
- Eliminates 84% of permission prompts (Anthropic production data), dramatically reducing approval fatigue
- Provides defense-in-depth beneath permission systems and AI classifiers -- even successful prompt injections remain isolated
- OS-level enforcement covers all subprocesses without per-tool instrumentation
- Lighter than container-based isolation -- no Docker daemon, no VM startup, no image management
- Credential proxy ensures secrets never enter the execution environment

**Negative:**
- Sandbox boundaries may be too restrictive for tasks requiring system-wide file access (e.g., cross-project refactoring, system administration)
- Unix domain socket proxy adds latency to network requests
- macOS seatbelt and Linux bubblewrap have different capability sets -- cross-platform parity may be incomplete
- Sandbox does not protect against logic errors within the allowed boundary (e.g., deleting project files the agent was permitted to access)
- Per-project sandbox profiles require maintenance as project requirements evolve

## Known Uses

- Anthropic production deployment in Claude Code -- open-sourced for external teams
- Claude Code's `/sandbox` command enables filesystem and network isolation on local machines
- Cloud version (claude.com/code) runs each session in an isolated sandbox by default with credential proxy
- The 84% permission prompt reduction is measured from Anthropic's production telemetry (93% baseline approval rate)

## Contract

### Preconditions
A coding agent or tool-using agent executes commands with filesystem and/or network access. The host OS supports process-level sandboxing primitives (Linux bubblewrap, macOS seatbelt, or equivalent). The agent's working directory and required network endpoints are known at session start. Credential management infrastructure exists outside the sandbox boundary.

### Invariants
Filesystem writes are restricted to the designated working directory and its descendants -- no exceptions without profile modification. Network traffic is routed through the proxy; direct internet access from within the sandbox is blocked. Credentials never enter the sandbox environment -- they are held and applied by the external credential proxy. Both filesystem and network isolation are enforced simultaneously; disabling either dimension is a configuration error. All subprocesses inherit sandbox constraints.

### Governance
Sandbox profiles are reviewed when project requirements change (new directories, new network endpoints). Domain allowlists are maintained per project and audited for overly broad entries. Credential proxy configurations are owned by the platform team, not modifiable by the agent. Sandbox escape attempts and blocked-operation logs are reviewed periodically. Profile changes require human approval.

### Recovery
If the sandbox blocks a legitimate operation: identify the blocked resource (path or domain), add it to the sandbox profile, and restart the session. Do not disable the sandbox to work around a restriction. If a sandbox escape is detected: terminate the session immediately, revoke any credentials that may have been exposed, audit the escape vector and affected files, patch the sandbox profile, and document the incident before restarting. If cross-platform parity issues arise, document the platform-specific gap and implement the closest available equivalent.
