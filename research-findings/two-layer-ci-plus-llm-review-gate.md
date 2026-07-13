---
name: "Two-Layer CI + LLM Review Gate"
summary: "Separate deterministic checks from LLM-judgment checks in a two-layer review pipeline. Layer 1 is a scripted battery that blocks on mechanical failures (structure, secrets, links, indexes); Layer 2 is LLM judgment for what scripts can't see (mission fit, superseded claims, naming consistency). Corroborated in two production systems: OB1's PR review (15 CI rules + review-pr admin skill) and CareerBuddy's ops-doc-sync (C1-C16 audit script + fidelity sweep), which adds the sequencing constraints: audit-before-edit, fidelity-not-delta, and re-run-to-exit-0 after fixes."
implementation_notes: "The engine now has the seed of Layer 1: a pre-commit hook enforcing frontmatter validity, FOUNDATIONS sync, and the PROGRESS line budget. Phase 2's planned ops-doc-sync pattern-lift is the direct adoption path: deterministic battery first (script is ground truth, never propose fixes from memory), then an LLM fidelity sweep scoped to what scripts can't see, then one human-gated fix batch, then re-run the script (must exit 0) before the single commit."
category: "Governance"
evidence_strength: "Medium (practitioner-documented, two production systems)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "careerbuddy-ops-doc-sync-audit-battery.md"
related_findings:
  - file: "deterministic-doc-audit-battery.md"
    rel: "same-problem"
  - file: "two-stage-sequential-review.md"
    rel: "same-problem"
  - file: "review-pipeline-bottleneck-and-quality-at-source.md"
    rel: "same-problem"
  - file: "hook-based-enforcement-for-agent-outputs.md"
    rel: "enables"
  - file: "skill-security-scanner-fail-closed.md"
    rel: "enables"
  - file: "externalized-real-session-behavior-evals.md"
    rel: "same-problem"
date_discovered: "2026-04-20"
last_updated: "2026-07-13"
pipeline_status: "classified"
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

**Corroborated in CareerBuddy's `ops-doc-sync` skill (2026-07)** — the same split applied to documentation governance rather than PR review, with three sequencing constraints the OB1 evidence lacked:
- **Audit before edit.** Layer 1 (the C1-C16 deterministic script, see [[deterministic-doc-audit-battery]]) always runs first; the skill forbids proposing fixes "from memory of what the docs should say." The script's report — file + check ID per finding — is the LLM layer's input, not its output.
- **Fidelity, not delta.** Layer 2 (the LLM judgment sweep) is explicitly defined as completeness against what the system is now, never just recent-change drift — "delta-hunting is structurally blind to what was always missing." It hunts what scripts can't see: framings contradicting the vision doc, status claims superseded by shipped milestones, references to retired files, manual entries missing a skill's defining behaviors.
- **Close the loop deterministically.** After the human approves the fix batch and edits are applied, the script re-runs and must exit 0 before the single commit. The deterministic layer both opens and closes the pass; the LLM layer never self-certifies.

CareerBuddy also tiers autonomy by layer: running the script is full-autonomy (read-only), working-file fixes are autonomous, governance-file fixes are proposal-first (one batch approval), and vision-doc content changes are human-required via a separate amendment flow.

## Potential Improvements
- Layer 1.5: LLM-based but automated pre-screen (clarity review of documentation, planned for v2 in OB1)
- Feedback loop: admin review findings could automatically generate new CI rules when patterns recur
- Cross-repo: the CI rules and admin skill template could be packaged as a reusable pattern for any community-contribution repo

## Potential Failure Modes
- CI rules create false confidence — passing CI doesn't mean the contribution is good, only that it's structurally correct
- Admin skill's LLM judgment is non-deterministic — same PR may get different verdicts on different runs
- The admin skill checks for prompt injection in submitted skills, but the skill itself could be subject to prompt injection from malicious PR content
