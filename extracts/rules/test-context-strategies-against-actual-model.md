---
title: "Test Context Strategies Against Your Actual Deployment Model"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "model-specific-context-file-sensitivity"
identification_report: "managing-agent-context.harvest-queue.md::model-specific-context-file-sensitivity::rule::test-context-strategies-against-actual-model"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "context file authoring (CLAUDE.md, AGENTS.md, .cursor/rules, equivalents) for any coding-agent deployment"
    - "teams choosing or migrating between coding-agent platforms (Claude Code, Codex, Cursor, GPT-5.x mini, Qwen Code, etc.)"
    - "context-engineering changes that propose model-agnostic guidance as a default"
    - "skill, agent, and template authors whose artifacts ship as context loaded by an underlying model"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "low — context strategies tuned to the wrong model produce silent quality regressions; reversal requires re-running the eval against the correct deployment model and rewriting affected files"
  auditability: "high — eval-result logs and per-model A/B deltas are mechanically recordable; absence of an eval log before a context-file change is directly observable"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "ETH Zurich March-2026 paper tested four agents (Claude Code Sonnet-4.5, Codex GPT-5.2, GPT-5.1 mini, Qwen Code Qwen3-30b-coder) and found Claude Code uniquely did not benefit from human-written context files — even hurt by LLM-generated ones. Other agents showed divergent sensitivities. No production deployments of model-specific context profiles known at time of extraction."
contract:
  preconditions: "A change to a context file (CLAUDE.md, AGENTS.md, project rules, skills loaded as context, or equivalent) is being proposed or imported from another team/platform. The deployment model (or model class) the agent will run against is identified. A small eval set covering the relevant capability axis is available, or can be constructed."
  invariants: "No context-file change is merged based solely on its effectiveness in another team's setup, in a paper, or against a different deployment model. Every context-file change runs at least one eval against the actual deployment model before merge. Eval results (delta vs. baseline, sample size, model+version tested) are recorded with the change. Cross-platform mirroring (CLAUDE.md ↔ AGENTS.md ↔ .cursor/rules) does not assume identical content — each tier is evaluated against its own deployment model."
  governance: "Owner: any system that ships context files consumed by a coding agent (MetaSystem, Improvement Loop, Household OS, Claude Build, downstream skills). The rule is enforced at the merge / deploy gate for context files. Exemptions (e.g., trivial typo fixes, pure formatting) must be declared on the change. Modification of the rule itself requires a Design Decision."
  recovery: "If a context-file change was merged without per-model eval and a regression is suspected: roll back to the prior version, run the eval, and re-merge only on confirmed delta. If the deployment model changes (version bump, vendor switch): re-run evals against the new model on the live context files; do not assume previous wins carry forward. If no eval set exists for the capability axis: block the change until a minimal eval set (≥10 cases covering the axis) is constructed, rather than merging on faith."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "model-specific"
  - "eval-driven"
  - "managing-agent-context"
---

# Test Context Strategies Against Your Actual Deployment Model

**Source:** [[model-specific-context-file-sensitivity]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A change is being proposed to a context file consumed by a coding agent — CLAUDE.md, AGENTS.md, `.cursor/rules`, project-scoped rule files, skills loaded as context, or the cross-platform mirror layer. The change may originate from:

- a pattern that worked for another team or platform,
- a paper or blog post recommending a context-engineering technique,
- a model-agnostic best-practice list,
- an LLM-authored or LLM-rewritten context file,
- or a vendor's reference template.

The agent that will consume this context runs on a specific deployment model (or model class) — Claude Code on Sonnet-4.x, Codex on GPT-5.x, GPT-5.x mini, Qwen Code on Qwen3-30b-coder, etc.

## Action

**Required:** Before merging the context-file change, run at least one eval against the **actual deployment model** the agent will use. Record the eval delta versus the prior version (or the no-context-file baseline, where appropriate), the sample size, and the model+version under test. Merge only if the delta is positive or neutral on the capability axis the change targets.

**Forbidden:**
- Merging context-file changes based solely on a paper, blog post, another team's report, or another model's results.
- Assuming a context strategy that helped one model (e.g., Codex) will help a different model (e.g., Claude Code) — the ETH Zurich data shows opposite-sign effects between agents on identical files.
- Treating cross-platform mirror layers (CLAUDE.md ↔ AGENTS.md ↔ `.cursor/rules`) as content-identical without per-model verification.
- Promoting LLM-rewritten context files into production without eval — LLM-generated files have measurably hurt at least one tested agent.
- Skipping the eval on the grounds that "the change is small" without an explicit declared exemption.

**Permitted alternatives:** When a full eval is infeasible, a documented spot-check (≥10 cases on the affected capability axis, run against the deployment model) plus a follow-up scheduled full eval is permitted. The spot-check result and the follow-up commitment must be recorded with the change.

## Boundary

Enforced at the merge / deploy gate for any context-file change that affects what the deployment model loads at session start, on tool invocation, or via skill activation. The rule fires from the moment a change is proposed (PR, commit, manual edit on a live file) until either:

- per-model eval evidence is recorded with the change, *or*
- a declared exemption (typo, pure formatting, comment-only) is attached.

Out of scope: ephemeral session notes, scratch files, and content not loaded as agent context. Also out of scope: governance-document edits (constitution, DDs) whose audience is humans, not the agent's context window.

## Enforcement

- **Mechanism:** A merge-gate check (PR template field, pre-merge hook, or human-review checklist) requires an eval-result entry for context-file changes. The entry names the model+version tested, the eval set, the delta, and the sample size. Cross-platform mirror updates require one entry per deployment model in the mirror.
- **Check (deterministic):** `(change_touches_context_file == true) AND ((eval_record_present == true) OR (declared_exemption == true))`. Any branch false → violation.
- **Violation response:**
  - *Eval missing on a non-exempt change:* block the merge; require either an eval run or an explicit exemption declaration before re-review.
  - *Eval run against the wrong model:* treat as missing; the model must match the deployment model (or model class) the agent will use.
  - *Exemption declared but the change is non-trivial (touches behavior-shaping rules, not just formatting):* reject the exemption; require a real eval.
  - *Cross-platform mirror updated without per-tier evidence:* block the mirror update on the un-evaluated tier; allow on tiers with evidence.
- **Cannot be self-certified:** "I read the file and it looks fine" is not eval evidence. The eval must produce a quantitative delta against the deployment model.

## Rationale

Most context-file guidance circulating in 2026 — including peer-reviewed research and platform-vendor documentation — implicitly assumes model-agnostic effectiveness. The ETH Zurich March-2026 study tested four coding agents with identical context files and found:

- **Claude Code (Sonnet-4.5)** was the only agent where developer-written context files produced no improvement; LLM-generated files actively hurt. Claude Code's built-in context management (sub-agent delegation, internal file discovery) appears to make external context files redundant or counterproductive.
- **Codex (GPT-5.2)** benefited from human-written context (+4% on AGENTbench) and was hurt by LLM-generated (-3%).
- **GPT-5.1 mini** exhibited a unique pathology: redundant re-reading of context files that were already in its context window, only when context files were present.
- **Qwen Code (Qwen3-30b-coder)** showed different sensitivity again, driven by its 60% chat-compression threshold and 2,000-token shell-output cap.

Effects were not just different in magnitude — they were opposite in sign across agents. A "best practice" tuned on Codex can degrade Claude Code performance, and vice versa. Cross-platform mirror layers (Archon-style) that maintain CLAUDE.md, AGENTS.md, `.cursor/rules` as content-identical inherit this risk silently — the mirror enforces text equality, not behavioral equivalence.

The positive invariant: every context-file change runs an eval against the actual deployment model, and the delta is recorded. This subsumes a long enumeration of negative anti-patterns (don't blindly copy from papers, don't trust LLM rewrites, don't mirror without verification) into one auditable check.

## Failure Modes

- **Model version drift.** A context strategy validated against Claude Sonnet 4.5 may behave differently on Sonnet 4.6 or 5.0. Mitigation: re-run evals on every deployment-model version bump; treat the validation as scoped to the tested version.
- **Eval set covers the wrong axis.** If the eval doesn't probe the capability the context change is meant to improve, a positive delta proves nothing. Mitigation: scope the eval set to the capability axis named in the change rationale.
- **Sample size too small.** A delta on 3 cases is noise. Mitigation: minimum eval-set size (e.g., 10 cases) for non-exempt changes; record sample size with every result.
- **LLM-rewritten context files slip through as "trivial formatting."** Brevity bias in LLM rewrites silently drops domain-specific details — measurable as a quality regression, not a typo. Mitigation: any whole-document rewrite (LLM-authored or otherwise) is non-exempt by definition; the exemption category is reserved for true typos and formatting.
- **Cross-platform mirroring assumes equivalence.** Teams maintaining CLAUDE.md, AGENTS.md, `.cursor/rules` as a single source of truth (Archon strategy) bypass per-model verification. Mitigation: each mirror tier is its own eval target.
- **Rule expires faster than the model lands.** Frontier models update on quarterly cadence; eval results from 6 months ago may be obsolete. Mitigation: eval results carry a model+version stamp; evidence older than the current deployment-model version triggers a re-run.

## Contract

### Preconditions

A change to a context file (CLAUDE.md, AGENTS.md, project rules, skills loaded as context, or equivalent) is being proposed or imported from another team/platform. The deployment model (or model class) the agent will run against is identified. A small eval set covering the relevant capability axis is available, or can be constructed.

### Invariants

No context-file change is merged based solely on its effectiveness in another team's setup, in a paper, or against a different deployment model. Every context-file change runs at least one eval against the actual deployment model before merge. Eval results (delta vs. baseline, sample size, model+version tested) are recorded with the change. Cross-platform mirroring (CLAUDE.md ↔ AGENTS.md ↔ `.cursor/rules`) does not assume identical content — each tier is evaluated against its own deployment model.

### Governance

Owner: any system that ships context files consumed by a coding agent (MetaSystem, Improvement Loop, Household OS, Claude Build, downstream skills). The rule is enforced at the merge / deploy gate for context files. Exemptions (e.g., trivial typo fixes, pure formatting) must be declared on the change. Modification of the rule itself requires a Design Decision.

### Recovery

If a context-file change was merged without per-model eval and a regression is suspected: roll back to the prior version, run the eval, and re-merge only on confirmed delta. If the deployment model changes (version bump, vendor switch): re-run evals against the new model on the live context files; do not assume previous wins carry forward. If no eval set exists for the capability axis: block the change until a minimal eval set (≥10 cases covering the axis) is constructed, rather than merging on faith.
