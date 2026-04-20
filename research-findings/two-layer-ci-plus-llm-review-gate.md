---
name: "Two-Layer CI + LLM Review Gate"
summary: "Separate deterministic CI checks (15 rules: structure, secrets, SQL safety, scope, links) from LLM-judgment checks (security deep scan, mission fit, naming consistency) in a two-layer PR review pipeline. CI blocks PRs on mechanical failures; the LLM admin skill handles judgment that CI can't automate."
implementation_notes: "MetaSystem uses human review gates but has no automated CI layer. This pattern suggests splitting review into: (1) hook-based deterministic checks that block automatically, (2) LLM-based judgment review that produces structured output for human decision."
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "two-stage-sequential-review.md"
    rel: "same-problem"
  - file: "review-pipeline-bottleneck-and-quality-at-source.md"
    rel: "same-problem"
  - file: "hook-based-enforcement-for-agent-outputs.md"
    rel: "enables"
  - file: "skill-security-scanner-fail-closed.md"
    rel: "enables"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is
A PR review architecture with two distinct layers that each handle what they do best:

**Layer 1 — CI (deterministic, automated):** 15 rules that can be checked mechanically: folder structure, required files, metadata.json validation against JSON Schema, secret scanning (API keys, tokens), SQL safety (no DROP/TRUNCATE), scope check (all changes within contribution folder), internal link resolution, remote MCP pattern enforcement, tool audit link presence. This layer blocks PRs — must pass before Layer 2 runs.

**Layer 2 — LLM admin skill (judgment, human-gated):** A Claude Code skill (`review-pr.md`) that handles everything CI can't: security deep scan (base64-encoded secrets, prompt injection patterns, data exfiltration URLs), mission fit assessment, naming consistency between files/metadata/README, PR description quality. Produces structured output: review checklist, verdict, admin summary, Discord announcement draft, post-merge task list.

## Why It Matters
Single-layer review creates a bottleneck: either everything is automated (misses judgment calls) or everything is manual (doesn't scale). Two layers let each handle its strength — CI catches 80% of issues instantly with zero human cost, while the admin skill focuses human attention on the 20% that requires judgment. The structured output from Layer 2 (checklist, summary, Discord draft) further reduces admin friction.

## Why People Are Using It
Observed in [OB1 (Open Brain)](https://github.com/NateBJones-Projects/OB1) — see [[ob1-analysis]] for structural details. The CI workflow (`.github/workflows/ob1-review.yml`) runs on every PR. The admin skill (`.claude/skills/review-pr.md`) is invoked manually by admins. The admin skill explicitly consumes CI results as input ("If CI passed, move on to admin checks").

## Potential Improvements
- Layer 1.5: LLM-based but automated pre-screen (clarity review of documentation, planned for v2 in OB1)
- Feedback loop: admin review findings could automatically generate new CI rules when patterns recur
- Cross-repo: the CI rules and admin skill template could be packaged as a reusable pattern for any community-contribution repo

## Potential Failure Modes
- CI rules create false confidence — passing CI doesn't mean the contribution is good, only that it's structurally correct
- Admin skill's LLM judgment is non-deterministic — same PR may get different verdicts on different runs
- The admin skill checks for prompt injection in submitted skills, but the skill itself could be subject to prompt injection from malicious PR content
