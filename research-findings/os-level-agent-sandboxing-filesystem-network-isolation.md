---
name: "OS-Level Agent Sandboxing -- Filesystem and Network Isolation"
summary: "Production sandboxing for coding agents using OS primitives (Linux bubblewrap, macOS seatbelt) to enforce filesystem and network isolation. Reduces permission prompts by 84%. Network isolation via Unix domain socket proxy with domain allowlisting. Credential proxy keeps secrets outside sandbox. Open-sourced by Anthropic."
implementation_notes: null
category: "Sandboxing"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "anthropic-claude-code-sandboxing.md"
related_findings:
  - file: "tiered-permission-system-bash-safety.md"
    rel: "extends"
  - file: "claude-code-auto-mode-ai-driven-permission-classif.md"
    rel: "same-problem"
  - file: "tool-gateway-security-boundary.md"
    rel: "enables"
  - file: "explicit-permission-allow-listing-for-agent-resou.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "agent-safety-and-permissions.md"
---

## What It Is
A production sandboxing system for coding agents that uses OS-level primitives rather than containers. Two isolation dimensions enforced simultaneously:

**Filesystem Isolation:**
- Read/write restricted to current working directory
- Blocks modifications outside project boundary
- Built on Linux bubblewrap and macOS seatbelt
- Covers direct interactions, scripts, programs, and subprocesses

**Network Isolation:**
- Internet access routed through Unix domain socket to an external proxy server
- Proxy restricts outgoing traffic to allowed domains
- New domain requests surface for user confirmation
- Customizable for arbitrary outgoing traffic rules

**Credential Proxy (Claude Code on the Web):**
- Sessions run in isolated cloud sandboxes
- Sensitive credentials (git credentials, signing keys) stay outside the sandbox
- Custom proxy handles git interactions: sandbox git client uses scoped credentials, proxy verifies credentials and interaction contents (e.g., pushes only to configured branch), then attaches authentication tokens for GitHub
- Compromised sandbox code cannot access real credentials

Both filesystem and network isolation are essential -- without network isolation, compromised agents could exfiltrate files (SSH keys); without filesystem isolation, agents could escape to gain network access.

## Why It Matters
Permission-based models create approval fatigue (Anthropic data: 93% approval rate, 84% prompt reduction with sandboxing). Sandboxing provides a complementary defense layer beneath permission systems and AI classifiers. Even successful prompt injections remain isolated -- the agent cannot steal SSH keys or contact attacker servers. The OS-primitive approach (bubblewrap/seatbelt) avoids container management overhead while covering all subprocesses.

## Why People Are Using It
Anthropic production deployment in Claude Code. Open-sourced for other teams to use. The `/sandbox` command in Claude Code enables it. Cloud version (claude.com/code) runs each session in an isolated sandbox by default. The 84% permission prompt reduction is a concrete productivity metric.

## Potential Improvements
Per-project sandbox profiles with different filesystem and network boundaries. Integration with auto mode for layered defense (sandbox + classifier). Warm sandbox pools for faster session startup. Sandbox escape detection and alerting.

## Potential Failure Modes
Sandbox boundaries may be too restrictive for tasks requiring system-wide file access or diverse network endpoints. The Unix domain socket proxy adds latency to network requests. macOS seatbelt and Linux bubblewrap have different capability sets -- cross-platform parity may be incomplete. Sandbox does not protect against logic errors within the allowed boundary.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[os-level-agent-sandboxing-filesystem-network-isolation.md]] in `extracts/patterns/`
