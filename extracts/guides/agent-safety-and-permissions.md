---
title: "Agent Safety and Permissions"
type: "guideline"
category: "Sandboxing"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "claude-code-auto-mode-ai-driven-permission-classif"
  - "gstack-four-layer-prompt-injection-defense"
  - "os-level-agent-sandboxing-filesystem-network-isolation"
  - "tiered-permission-system-bash-safety"
  - "independent-eval-and-scoped-authority-commandments"
source_dd:
  - "DD-81"
  - "DD-78"
tags:
  - "guide"
  - "sandboxing"
  - "safety"
  - "permissions"
contract:
  preconditions: "You have an agent system that executes actions with side effects (file writes, shell commands, API calls, network requests). You can classify tools by risk level. You have or can build enforcement mechanisms at the OS or orchestration layer."
  invariants: "Permissions are tiered by risk — not binary allow/deny. Safety-critical constraints are enforced structurally, not via prompt instructions. The agent cannot modify its own permission configuration. Defense is layered — no single mechanism is the sole protection."
  governance: "Permission configurations are governed artifacts. Changes require review. Sandbox boundaries are documented per environment. This guide is owned by Meta-System knowledge layer."
  recovery: "If a safety boundary is violated: halt, log, escalate. Investigate the enforcement mechanism, not just the agent's behavior. If approval fatigue is observed (>90% approval rate): add sandboxing or auto-classification to reduce prompt volume."
---

# Agent Safety and Permissions

How to make your agent system safe — from tiered permission systems through OS-level sandboxing to prompt injection defense. This guide is about structural enforcement, not prompt-based instructions. If a constraint matters, enforce it; if a decision is risky, gate it.

## When to Use This Guide

- You are deploying an agent that executes shell commands, writes files, or makes API calls
- You need to prevent agents from accessing resources outside their scope
- You are designing a permission system for a multi-agent pipeline
- You want to reduce permission prompt fatigue without sacrificing safety
- You are exposing agents to untrusted content (web browsing, user-provided files)

## Key Concepts

**1. Permissions are tiered, not binary.** Three trust tiers — built-in tools (highest trust), plug-in tools (medium), user-defined skills (lowest). Within each tier, commands are classified as safe (read-only), mutating, or destructive. Different classifications get different oversight levels.

**2. Structural enforcement beats prompt compliance.** An agent told "never access files outside the project directory" in a prompt may comply most of the time. An agent sandboxed via OS-level filesystem isolation (bubblewrap/seatbelt) physically cannot access files outside the project. Use both, but trust the structural layer.

**3. Define the negative space first.** Specify what agents explicitly cannot do before expanding what they can do. Start with minimal permissions and expand deliberately. Every permission expansion is a conscious decision, not a default.

**4. Approval fatigue is a real safety risk.** Anthropic data: users approve 93% of permission prompts without close attention. Rubber-stamping is objectively less safe than an AI classifier with a 17% false-negative rate. Sandboxing reduces prompt volume by 84%.

**5. Defense is layered.** No single mechanism — classifier, sandbox, prompt instruction, or content filter — is sufficient alone. Defense-in-depth ensures that bypass of one layer is caught by the next.

---

## Procedure

### Step 1: Classify All Tools by Risk

| Risk Level | Description | Examples | Oversight |
|-----------|-------------|---------|-----------|
| **Safe** | Read-only, no side effects | File reads, grep, glob, git status | Auto-allow |
| **Mutating** | Creates or modifies within project scope | File writes, edits within project directory | Auto-allow with audit trail |
| **Destructive** | Irreversible or out-of-scope effects | rm -rf, drop table, git push --force, production deploys | Require approval or block |

For shell commands, build a safety module that pre-classifies commands before execution. Claude Code uses 18 modules for bash alone, covering pre-approved patterns, destructive command detection, and domain-specific safety checks.

### Step 2: Implement the Permission Architecture

Layer three tiers of enforcement, from bottom (structural) to top (intelligent):

```
┌──────────────────────────────────┐
│ Tier 3: AI Classifier            │ ← Smart filter for ambiguous cases
│   Reasoning-blind transcript     │    (Stage 1: single-token filter,
│   classifier evaluates actions   │     Stage 2: CoT only if flagged)
├──────────────────────────────────┤
│ Tier 2: Project Scope Rules      │ ← Auto-allow within project boundary
│   File ops within project dir    │    Reviewable via version control
│   auto-allowed                   │
├──────────────────────────────────┤
│ Tier 1: OS Sandbox               │ ← Structural enforcement floor
│   Filesystem isolation           │    Cannot be bypassed by the agent
│   Network isolation via proxy    │    Credential proxy for secrets
│   (bubblewrap / seatbelt)        │
└──────────────────────────────────┘
```

**Key design insight for the AI classifier:** Make it reasoning-blind — the classifier sees user messages and tool calls but NOT the agent's reasoning. This prevents the agent from "talking the classifier into" allowing dangerous actions.

**Deny-and-continue pattern:** When an action is blocked, return the denial as a tool result with instructions to find a safer approach. Don't terminate the session. Backstop: stop after 3 consecutive or 20 total denials and escalate to human.

### Step 3: Add Sandbox Isolation

OS-level sandboxing provides the structural floor beneath the permission tiers:

| Isolation Type | What It Enforces | Mechanism |
|---------------|-----------------|-----------|
| **Filesystem** | Read/write restricted to project directory | Linux bubblewrap, macOS seatbelt |
| **Network** | Outbound traffic restricted to allowed domains | Unix domain socket proxy with domain allowlist |
| **Credentials** | Secrets stay outside the sandbox | Credential proxy handles auth; sandbox code never sees real tokens |

Both filesystem AND network isolation are essential. Without network isolation, a compromised agent could exfiltrate files (SSH keys). Without filesystem isolation, an agent could escape to gain network access.

### Step 4: Defend Against Prompt Injection

When agents read untrusted content (web pages, user-provided files, external APIs), apply defense-in-depth:

| Layer | Defense | Purpose |
|-------|---------|---------|
| 1 | **Content envelope** | Bracket untrusted content with explicit markers; inject zero-width spaces to prevent marker spoofing |
| 2 | **Hidden element stripping** | Remove CSS-hidden content and ARIA label injection from web pages |
| 3 | **Datamarking** | Session-scoped watermarks (zero-width chars) for content leakage tracing |
| 4 | **Content filter hooks** | URL blocklist (requestbin, pipedream, webhook.site) + custom filters |

### Step 5: Instrument and Monitor

Build observability from day one — it is expensive to retrofit:

- **Permission grant log:** Every approval, denial, and auto-allow with the action, risk classification, and tier that handled it
- **Sandbox violation log:** Every blocked filesystem or network access attempt
- **Classifier decision log:** What the classifier saw, what it decided, why (Stage 1 vs Stage 2)
- **Approval rate tracking:** If approval rate exceeds 90%, investigate for fatigue

---

## Templates

### Permission Architecture Worksheet

```markdown
## Permission Architecture — {{SYSTEM_NAME}}

### Tool Risk Classification
| Tool / Command | Risk Level | Tier | Oversight |
|---------------|-----------|------|-----------|
| {{TOOL}} | {{safe/mutating/destructive}} | {{1/2/3}} | {{auto/approve/block}} |

### Sandbox Configuration
- Filesystem boundary: {{PATH}}
- Network allowlist: {{DOMAINS}}
- Credential handling: {{PROXY/DIRECT/NONE}}

### Classifier Configuration (if using AI classification)
- Reasoning-blind: {{YES/NO}}
- Block rules: {{LIST}}
- Allow exceptions: {{LIST}}
- Denial backstop: {{N}} consecutive, {{M}} total

### Monitoring
- Approval rate target: < {{PERCENT}}%
- Permission log location: {{PATH}}
- Review frequency: {{SCHEDULE}}
```

---

## Worked Example: MetaSystem Safety Architecture

```
Permission Architecture — MetaSystem

CURRENT STATE:
- CLAUDE.md rules (prompt-layer) ← sole enforcement mechanism
- "Never modify files outside system boundary" ← prompt instruction, not enforced
- "Never commit to main without review" ← prompt instruction
- Human gate (DD-29) ← procedural, not structural
- Pre-commit hooks ← structural enforcement for code quality

GAPS:
- No OS-level sandboxing (filesystem or network)
- No AI classifier for permission decisions
- No prompt injection defense for web content
- Destructive command safety is prompt-based, not structural
- No permission grant logging

RECOMMENDED ARCHITECTURE:
Tier 1: Enable Claude Code /sandbox command
  - Filesystem: restrict to MetaSystem/ directory
  - Network: allowlist github.com, api.anthropic.com, perplexity.ai
  
Tier 2: Project scope auto-allow
  - File writes within current system directory: auto-allow
  - Cross-system file writes: require approval

Tier 3: Already in effect via Claude Code's built-in classifier
  - Covers shell commands, web fetches, external tools
  
Prompt injection: Not currently exposed to untrusted web content
  - Would need Layer 1-4 defense if /watch-blogs fetches raw HTML
```

---

## Pitfalls

### 1. All safety in the prompt layer
"Never access files outside the project" is a prompt instruction that the agent may fail to follow. If the constraint matters, enforce it structurally — filesystem isolation, pre-tool-use hooks, API authentication gates.

### 2. Binary permissions (allow everything or ask everything)
Users rubber-stamp 93% of prompts. Binary permission systems either bottleneck the agent or create dangerous approval fatigue. Tier the permissions by risk.

### 3. Reasoning-visible classifiers
If the classifier can read the agent's reasoning, the agent can craft reasoning that convinces the classifier to allow dangerous actions. Make classifiers reasoning-blind.

### 4. Filesystem isolation without network isolation (or vice versa)
Either isolation alone is insufficient. Without network: agent exfiltrates files. Without filesystem: agent escapes to gain network access. Both are needed.

### 5. Permission expansion by default
Every tool starts with maximum permissions. The safe approach: start with minimum and expand deliberately. Define what the agent cannot do before what it can do.

---

## Related Guides

- **Risk classification → tool registries:** The risk levels in Step 1 map to the metadata-first tool registry in *Designing Agent Tools* (G5), Step 1.
- **Hard constraint enforcement → boundary design:** Hard constraints that need structural enforcement are defined in *Writing Agent Specifications* (G1), Step 3a.
- **Untrusted content → context curation:** When agents read untrusted web content, context curation principles from *Managing Agent Context* (G2) apply alongside the injection defenses in Step 4.

---

## Contract

### Preconditions
- You have an agent system that executes actions with side effects.
- You can classify tools by risk level (safe/mutating/destructive).
- You have or can build enforcement mechanisms at the OS or orchestration layer.

### Invariants
- Permissions are tiered by risk, not binary allow/deny.
- Safety-critical constraints are enforced structurally, not via prompt instructions alone.
- The agent cannot modify its own permission configuration.
- Defense is layered — no single mechanism is the sole protection.

### Governance
- Permission configurations are governed artifacts. Changes require review.
- Sandbox boundaries are documented per environment.
- Approval rates are monitored — rates above 90% trigger investigation.

### Recovery
- If a safety boundary is violated despite structural enforcement: treat as a security incident — halt, log, escalate. Investigate the enforcement mechanism failure, not just the agent's behavior.
- If approval fatigue is observed: add sandboxing or auto-classification to reduce prompt volume rather than telling users to "pay more attention."
- If prompt injection is detected: activate content filter hooks, review the content source, and add the source to blocklists if necessary.
