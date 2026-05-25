---
name: Shell-Injection Vector Taxonomy for Agent Bash Security
summary: Claude Code's leaked bashSecurity.ts runs 23 numbered security checks on every bash command; 18 of those checks specifically block Zsh builtins. Beyond pattern allowlisting, the module enumerates and defends against named injection vectors — Zsh equals expansion (`=curl` bypassing a `curl` allowlist), unicode zero-width-space insertion in command names, IFS null-byte injection, and a malformed-token bypass found during a HackerOne bug-bounty review. Teams building bash-access agents need an enumerated injection-vector list, not just an allowlist of known-safe commands.
implementation_notes: MetaSystem's S3 (Claude Code Build) work involves bash access via hooks. Rules in `.claude/rules/` can block dangerous patterns, but the leaked bashSecurity.ts shows the set of vectors that a mature shell guard must cover. This is a direct input to any future "MetaSystem bash-hook hardening" IB item.
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claudefa-st-claude-code-source-leak.md
- dev-to-claude-code-leaked-via-npm-source-maps.md
related_findings:
- file: tiered-permission-system-bash-safety.md
  rel: extends
- file: prompt-injection-risk-from-trusted-vs-untrusted.md
  rel: same-problem
- file: gsd-prompt-injection-scanner-hardening.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: enables
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-23'
pipeline_status: "classified"
consumed_by: []
---

# Shell-Injection Vector Taxonomy for Agent Bash Security

## What It Is

Claude Code's leaked `bashSecurity.ts` module runs every bash command through 23 numbered security checks. The checks divide into two layers:

1. **Builtin-blocker layer (18 checks)** — blocks 18 specific Zsh builtins whose semantics bypass pattern matching (aliases, functions, eval variants, etc.).
2. **Injection-vector layer** — named defenses against specific attack patterns:
   - **Zsh equals expansion** — `=curl` resolves to the full path of `curl`, bypassing an allowlist that only matched literal `curl`
   - **Unicode zero-width-space insertion** — `c\u200Burl` renders as "curl" visually but doesn't match literal `curl`
   - **IFS null-byte injection** — splits a blocked command name across safe-looking tokens
   - **Malformed-token bypass** — a parser edge case found and reported via HackerOne bug-bounty review

The taxonomy matters more than the specific checks: it establishes that a production bash guard needs an *enumerated* vector list, not just a pattern allowlist.

## Why It Matters for Us

Plain English: if you're letting an agent run `bash`, the naive defense is "allow only commands on this list." That's been broken for years by shell injection. Claude Code's leak shows the specific attacks a serious production defense actually has to cover — and the HackerOne-originated fix proves the list isn't static. For MetaSystem, any future bash-hook rule (for S3 work or otherwise) should be audited against this vector list rather than hand-rolled.

## Why People Are Using It

Anthropic ships it in Claude Code's production bash tool; the leak surfaced it publicly. Multiple security researchers (Alex Kim, Ken Huang, Gabriel Anhaia) have independently analyzed the module and corroborated the 23-check structure. HackerOne was the input channel for at least one fix, meaning the module is actively maintained against new vectors.

## Potential Alternatives

- **Pattern allowlist only** — insufficient; defeated by any of the named vectors above
- **Full shell disable** — adequate but severely restricts useful agents
- **Container/sandbox escape** (E2B, Daytona) — complementary, not a substitute; attackers who escape the guard are still contained but the guard is still the first line
- **Structured-tool-only agents** — skip bash entirely; viable for narrow agents

## Potential Improvements

- Publish an IL rule-checklist: for any proposed bash hook, confirm defenses against each named vector
- Cross-link the checklist to MetaSystem's `governance/agent-rules.md` so it surfaces during Owner audits
- Track HackerOne / disclosure channels for new vectors — this module evolves

## Potential Failure Modes

- New injection vectors are invented; the taxonomy is a point-in-time snapshot
- Overly aggressive blocking breaks legitimate workflows (e.g., all `curl` variants)
- Hooks that don't run the module defeat the guarantee; single-point-of-defense is fragile
