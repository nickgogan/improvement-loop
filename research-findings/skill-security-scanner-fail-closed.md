---
name: "Skill Security Scanner with Fail-Closed Default"
summary: "LLM-based scanner classifies new/modified skills as allow/warn/block. Checks for prompt-injection, privilege escalation, exfiltration. On model failure: block by default. JSONL history log per skill."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - {file: "bmad-module-marketplace-with-vetting.md", rel: "same-problem"}
  - {file: "gsd-prompt-injection-scanner-hardening.md", rel: "extends"}
proposals: null
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
---

## What It Is

A security scanner for agent-created or agent-modified skills. When skill evolution is enabled and an agent writes a new SKILL.md or executable, an LLM call with a security reviewer system prompt classifies the content as `allow` (safe), `warn` (borderline — proceed with notice), or `block` (dangerous — reject). Blocked categories: prompt-injection, system-role override, privilege escalation, exfiltration, unsafe executable code. Critical design decision: if the LLM scanner call itself fails (timeout, error), the default is `block` — fail-closed, not fail-open. A JSONL history log per skill name maintains an audit trail of all scan decisions.

## Why It Matters

The existing KB covers prompt injection scanning (GSD's hardening) and module marketplace vetting (BMAD). This pattern addresses a distinct scenario: when agents can create or modify their own skills (skill evolution), the system needs a gate that prevents malicious or broken skills from being persisted. The fail-closed default is the key insight — in a system where agents write code that agents will execute, the safe default is denial.

## Why People Are Using It

Observed in [DeerFlow](https://github.com/bytedance/deer-flow) v2.0 — see [[deer-flow-analysis]] for structural details. DeerFlow's `skills/security_scanner.py` implements the scanner. The JSONL history enables audit and trend analysis (is a particular skill name repeatedly flagged?).

## Potential Alternatives

- No scanning (trust the agent — risky with skill evolution enabled)
- Static analysis only (regex/AST checks, no LLM involvement)
- Human review gate (all new skills require manual approval)

## Potential Improvements

Could add incremental scanning — only re-scan changed sections of a modified skill rather than the entire file. Could also add a "trust score" that relaxes scanning for skills that have passed N consecutive scans.

## Potential Failure Modes

- LLM scanner may have false positives (blocking legitimate skills)
- LLM scanner may have false negatives (allowing subtle attacks)
- Fail-closed on model failure means transient errors block all skill creation
- The scanner itself is an LLM — it could be prompt-injected via the skill content
