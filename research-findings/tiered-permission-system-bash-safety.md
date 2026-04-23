---
name: Tiered Permission System with Destructive-Command Safety Architecture
summary: A three-tier trust architecture for agent tools (built-in → plug-in → skills/user-defined) backed by bashSecurity.ts — a bash security layer running 23 numbered checks per command, 18 of which specifically block Zsh builtins. Commands are pre-classified (read-only, mutating, destructive) with pre-approved patterns, domain-specific safety checks, and named injection-vector defenses. The taxonomy of injection vectors is captured as a separate extended finding.
implementation_notes: MetaSystem governance rules require human gate for destructive operations. The tiered model could formalize this into a systematic classification.
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
- anthropic-claude-code-auto-mode.md
- anthropic-claude-code-sandboxing.md
- claudefa-st-claude-code-source-leak.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-23'
related_findings:
- file: claude-code-12-agent-primitives.md
  rel: extended-by
- file: tool-gateway-security-boundary.md
  rel: enables
- file: claude-code-auto-mode-ai-driven-permission-classif.md
  rel: same-problem
- file: shell-injection-vector-taxonomy-agent-bash-security.md
  rel: extended-by
pipeline_status: synthesized
consumed_by:
- agent-safety-and-permissions.md
---
# Tiered Permission System with Destructive-Command Safety Architecture

## What It Is
Three trust tiers: built-in (highest, always available) → plug-in (medium, disableable) → skills (user-defined, lowest trust). The bash tool's `bashSecurity.ts` runs 23 numbered checks per command; 18 of those checks specifically block Zsh builtins (aliases, functions, eval variants, etc.). The remaining checks cover pre-approved patterns, destructive-command detection, domain-specific safety, sandbox termination, and named injection-vector defenses (see [[shell-injection-vector-taxonomy-agent-bash-security]] for the enumerated vectors, including Zsh equals expansion, unicode zero-width-space, IFS null-byte, and a malformed-token bypass surfaced via HackerOne review). Application pattern: pre-classify all tools as read-only / mutating / destructive; log all permission grants.

## Why It Matters
Shell-access agents are the highest-risk surface. The 18-module approach prevents catastrophic actions (rm -rf, drop table) while allowing productive work. Permission audit logging creates accountability.

## Why People Are Using It
Anthropic's production Claude Code system. Nate B Jones: "Tier 1 non-negotiable."

## Potential Alternatives
Simple allowlist/blocklist. Sandboxed execution environments. No-shell agents that operate only through structured tools.

## Potential Improvements
User-customizable pre-approved patterns. Per-project permission profiles. Graduated trust escalation based on agent track record.

### Anthropic Auto Mode Tier Architecture (2026-04-09)
Anthropic's auto mode post confirms and extends this pattern with a concrete 3-tier implementation: Tier 1 (built-in safe-tool allowlist + user settings, drops blanket shell rules on auto mode entry), Tier 2 (in-project file ops auto-allowed), Tier 3 (transcript classifier for shell, web, external tools, subagent spawns). The auto mode entry behavior of stripping overly permissive rules is a key safety innovation -- ensures the classifier always sees high-risk commands.

### OS-Level Sandboxing Layer (2026-04-09)
The sandboxing post adds a complementary OS-level enforcement layer beneath the permission tiers: Linux bubblewrap and macOS seatbelt provide filesystem and network isolation. This reduces permission prompts by 84% while maintaining security. The sandbox is the "floor" beneath the tiered permission "ceiling."

## Potential Failure Modes
Over-restrictive permissions block legitimate work. Under-classification of destructive commands. Permission fatigue from too many approval prompts. Anthropic data: 93% approval rate indicates fatigue is real and systemic.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[tiered-permission-system-bash-safety.md]] in `extracts/patterns/`
