---
title: "Tiered Permission System with Destructive-Command Safety"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "tiered-permission-system-bash-safety"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent has access to shell or filesystem tools capable of destructive operations. A tool inventory exists that can be classified by risk level. An OS-level sandboxing mechanism (bubblewrap, seatbelt) is available or planned for defense-in-depth."
  invariants: "Destructive commands never execute without explicit human approval, regardless of trust tier. Every permission grant is logged with timestamp, command, and approval source. The tiered classification is enforced at the tool gateway -- agents cannot bypass tiers by rephrasing commands. OS-level sandbox provides the floor beneath application-level permission tiers."
  governance: "Owned by Meta-System knowledge layer. Tier classifications and pre-approved patterns are reviewed when new tools are added. Modifications require a Design Decision. MetaSystem constitution already mandates human gate for destructive operations -- this pattern formalizes the mechanism."
  recovery: "If a destructive command bypasses the permission tier (classification gap), halt execution immediately, log the incident, and add the command pattern to the destructive tier. If permission fatigue causes rubber-stamping, audit approval rates and expand the pre-approved safe patterns to reduce prompt volume. If sandbox termination kills a legitimate long-running process, add it to the safe process allowlist."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Tiered Permission System with Destructive-Command Safety

**Source:** [[tiered-permission-system-bash-safety]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agents with shell access represent the highest-risk surface in any agentic system. A single `rm -rf /`, `DROP TABLE`, or `git push --force` can cause irreversible damage. Blanket permission approaches fail in both directions: blocking all shell access cripples productivity, while allowing all shell access invites catastrophe. Binary allow/deny models also produce permission fatigue -- users approve 93% of prompts reflexively, defeating the safety mechanism entirely.

## Forces

- **Productivity vs. safety.** Agents need shell access to be useful (file operations, git, package management), but every shell command is a potential destructive action.
- **Granularity vs. usability.** Fine-grained per-command approval is safe but exhausting. Coarse-grained blanket approval is usable but dangerous.
- **Trust escalation vs. static classification.** Some agents earn trust through track record, but static classification is simpler to audit and harder to exploit.
- **Application-level vs. OS-level enforcement.** Application-level permission tiers can be bypassed by crafty command construction. OS-level sandboxing is harder to bypass but blunter in what it blocks.
- **Permission fatigue vs. security discipline.** Too many approval prompts cause users to rubber-stamp everything (93% approval rate in Anthropic's data), which is functionally equivalent to no security.

## Solution

Implement a **three-tier trust architecture** for agent tools, backed by a **multi-module bash security layer** and an **OS-level sandbox floor**.

**Tier 1 -- Built-in tools (highest trust).** Always available, no approval needed. Read-only operations, safe tool calls, and pre-approved command patterns. When entering auto mode, overly permissive blanket shell rules are stripped to ensure the classifier always sees high-risk commands.

**Tier 2 -- Plug-in tools (medium trust).** In-project file operations auto-allowed. External calls require classification. Disableable per session or project.

**Tier 3 -- Skills and user-defined tools (lowest trust).** Transcript classifier evaluates shell commands, web access, external tool calls, and subagent spawns. Commands are pre-classified as:
- **Read-only:** `ls`, `cat`, `git status`, `grep` -- auto-approved.
- **Mutating:** `git commit`, file writes, package installs -- logged, may require approval based on context.
- **Destructive:** `rm -rf`, `DROP TABLE`, `git push --force`, `truncate` -- always require explicit human approval.

The bash security layer implements this classification through modules: pre-approved patterns (known-safe commands), destructive command detection (regex and semantic matching), domain-specific safety checks (git-specific, database-specific), and sandbox termination (kill processes that escape classification).

**OS-level sandbox floor.** Beneath the application-level tiers, Linux bubblewrap or macOS seatbelt provides filesystem and network isolation. This reduces permission prompts by 84% while maintaining security -- the sandbox catches what the classifier misses.

## Consequences

**Positive:**
- Prevents catastrophic actions (data loss, repository corruption, system damage) through defense-in-depth.
- Permission audit logging creates accountability and enables post-incident analysis.
- Pre-approved patterns for common safe operations reduce permission prompt volume, addressing fatigue.
- OS-level sandbox provides a safety floor that does not depend on correct application-level classification.
- 84% reduction in permission prompts from sandbox layer alone.

**Negative:**
- Over-restrictive classification blocks legitimate work and frustrates users into disabling safety mechanisms.
- Under-classification of destructive commands creates false confidence in the safety system.
- Permission fatigue remains a real risk despite mitigation -- 93% approval rate indicates users do not meaningfully review prompts.
- Maintaining command classification across evolving tool sets requires ongoing effort.
- Sandbox restrictions may block legitimate operations (network access, cross-project file reads) that require per-project exceptions.

## Known Uses

- **Anthropic Claude Code production system.** Three-tier architecture with 18 bash security modules. Used across Anthropic's $2.5B production deployment. Nate B Jones identifies it as "Tier 1 non-negotiable."
- **Anthropic auto mode.** Tier 1 entry behavior strips overly permissive rules, ensuring the classifier always evaluates high-risk commands. Concrete implementation of the principle that safety defaults should be restrictive.
- **Anthropic sandboxing layer.** Linux bubblewrap and macOS seatbelt provide OS-level enforcement beneath the permission tiers. Reports 84% reduction in permission prompts.
- **MetaSystem governance rules.** Constitution and CLAUDE.md already mandate human gate for destructive operations (`rm -rf`, `drop table`, `truncate`). This pattern formalizes the mechanism behind the mandate.

## Contract

### Preconditions

- Agent has access to shell or filesystem tools capable of destructive operations.
- A tool inventory exists that can be classified by risk level (read-only, mutating, destructive).
- An OS-level sandboxing mechanism (bubblewrap, seatbelt, or equivalent) is available or planned for defense-in-depth.

### Invariants

- Destructive commands never execute without explicit human approval, regardless of trust tier.
- Every permission grant is logged with timestamp, command, and approval source.
- The tiered classification is enforced at the tool gateway -- agents cannot bypass tiers by rephrasing commands or chaining safe commands into destructive sequences.
- OS-level sandbox provides the floor beneath application-level permission tiers.

### Governance

- Owned by Meta-System knowledge layer.
- Tier classifications and pre-approved patterns are reviewed when new tools or command types are added.
- Modifications require a Design Decision.
- MetaSystem constitution already mandates human gate for destructive operations -- this pattern formalizes and systematizes that mandate.

### Recovery

- If a destructive command bypasses the permission tier (classification gap), halt execution immediately, log the incident, and add the command pattern to the destructive classification.
- If permission fatigue causes rubber-stamping (approval rates exceeding 90%), audit the approval log and expand pre-approved safe patterns to reduce prompt volume.
- If sandbox termination kills a legitimate long-running process, add the process signature to the safe process allowlist after human review.
- If tier classification conflicts with OS-level sandbox restrictions, the sandbox restriction wins -- it is the safety floor.
