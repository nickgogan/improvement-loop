---
title: 'CLAUDE.md Minimum Viable Rule: Only Add Globally True Lines'
type: extracted-artifact
assigned_form: rule
source_finding: claudemd-minimum-viable-rule-only-add-globally
extraction_date: '2026-04-26'
identification_report: 2026-04-26-identification-report.md
deployed: false
deployed_to: null
context:
  applies_to:
  - agent operators configuring a persistent context file that is loaded into every session (e.g., CLAUDE.md at user or project scope)
  - teams managing shared agent configurations where accumulated rules from multiple contributors have caused context bloat
  - anyone noticing that their agent starts sessions with degraded response quality due to irrelevant context noise
  platform_coupling: specific:claude-code
  autonomy: all
  stage: specify
  reversibility: trivial — removing a line from a text file; no migration cost, no downstream state
  auditability: high — each line in CLAUDE.md is a discrete artifact; the global-truth self-test is a binary check that can be reviewed by any reader; session startup context utilization is an observable
    proxy metric for compliance
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: null
contract:
  preconditions: A CLAUDE.md (or equivalent agent context file) exists or is being created. The operator has write access to the file. The operator can reason about the frequency distribution of their sessions
    — what tasks they actually perform, how often.
  invariants: Every line present in CLAUDE.md passes the global-truth test (applicable in nearly every session). The file does not contain rules whose primary justification is handling a single past failure.
    Per-project or per-session context mechanisms exist as an alternative destination for scoped rules so that removing a line from CLAUDE.md does not mean permanently losing the guidance.
  governance: 'Owner: the individual or team responsible for the agent setup. Any person or agent authorized to modify CLAUDE.md must apply this rule before each addition. Audit trigger: if session startup
    context utilization is unexpectedly high, audit CLAUDE.md for lines that fail the global-truth test. No external governance gate required — enforcement is at the point of authorship.'
  recovery: 'If a line is discovered to fail the global-truth test after being added: remove it from CLAUDE.md immediately; if the rule is genuinely useful in specific contexts, migrate it to a per-project
    CLAUDE.md or a slash command. If bloat has already accumulated: audit every line against the global-truth test in a single pass; remove all non-qualifying lines; verify that session startup context
    utilization returns to baseline.'
tags:
- extracted-artifact
- rule
---

# CLAUDE.md Minimum Viable Rule: Only Add Globally True Lines

**Source:** [[claudemd-minimum-viable-rule-only-add-globally]]
**Form:** rule
**Extraction date:** 2026-04-26

## Condition

An agent operator is editing or extending a CLAUDE.md (or equivalent agent context file) — at the user, project, or workspace level — and is considering whether to add a new line, section, or rule.

This rule fires on every proposed addition to a CLAUDE.md file. It does not apply to initial scaffolding (when the file is empty and baseline identity/preferences are being established for the first time).

## Action

**Required:** Before adding any line, apply the following self-test: "Would I type this line into context manually at the start of nearly every coding session?" If the honest answer is "no" or "sometimes", the line must not be added to CLAUDE.md.

**Forbidden:**
- Adding rules that are only relevant in a minority of sessions (e.g., framework-specific instructions when only some tasks touch that framework)
- Adding rules reactively after a single failed interaction without establishing a recurrence pattern
- Adding content that belongs in a slash command, per-project context file, or inline session instruction

**Permitted alternatives:**
- Per-project CLAUDE.md files for project-scoped rules (loaded only when relevant)
- Slash commands for session-specific context injection
- Inline instructions passed at invocation time for one-off behavioral adjustments

## Boundary

Enforced at the moment of authoring: before any edit to a CLAUDE.md file is finalized. Applies equally to human operators and to any agent authorized to modify CLAUDE.md.

## Enforcement

- **Mechanism:** Apply the global-truth self-test to each candidate line before writing. The test is binary: globally true (nearly every session) or not.
- **Check (deterministic):** For each candidate line L, evaluate: `sessions_where_L_is_relevant / total_sessions ≥ threshold` (threshold: approximately 0.8 or higher). Lines below threshold are excluded.
- **Violation response:**
  - Line fails the self-test → do not add it; route to per-project file or slash command instead.
  - Line was added in error → remove it; check whether the marginal noise it introduced in irrelevant sessions has caused downstream confusion.
- **Cannot be self-certified:** The operator must explicitly reason about session frequency before adding each line. Post-hoc audits ("does this CLAUDE.md line apply to most of my actual sessions?") are the primary enforcement mechanism.
- **Signal for bloat:** If the agent starts a session at significantly higher context utilization than expected before any task context has been loaded, audit CLAUDE.md for lines that fail the global-truth test.

## Rationale

Every token in CLAUDE.md is loaded unconditionally into every session context window. Rules that apply to 20% of sessions consume 100% of their token cost, injecting noise in the 80% of sessions where they are irrelevant. This noise degrades response coherence and wastes context budget before the task even begins — the "starting at 60%" problem.

The discipline to resist adding rules is non-intuitive: every failed interaction produces an impulse to codify a fix. The global-truth test is the counterweight — it forces the operator to ask whether the rule generalizes before it is promoted to universal context.

The corollary: a lean CLAUDE.md (3–5 lines of genuinely universal truth) outperforms a thorough CLAUDE.md (30 lines covering every edge case) on average-session quality, even though the thorough version handles more edge cases when they arise.

## Contract

### Preconditions
A CLAUDE.md (or equivalent agent context file) exists or is being created. The operator has write access to the file. The operator can reason about the frequency distribution of their sessions — what tasks they actually perform, how often.

### Invariants
Every line present in CLAUDE.md passes the global-truth test (applicable in nearly every session). The file does not contain rules whose primary justification is handling a single past failure. Per-project or per-session context mechanisms exist as an alternative destination for scoped rules so that removing a line from CLAUDE.md does not mean permanently losing the guidance.

### Governance
Owner: the individual or team responsible for the agent setup. Any person or agent authorized to modify CLAUDE.md must apply this rule before each addition. Audit trigger: if session startup context utilization is unexpectedly high, audit CLAUDE.md for lines that fail the global-truth test. No external governance gate required — enforcement is at the point of authorship.

### Recovery
If a line is discovered to fail the global-truth test after being added: remove it from CLAUDE.md immediately; if the rule is genuinely useful in specific contexts, migrate it to a per-project CLAUDE.md or a slash command. If bloat has already accumulated: audit every line against the global-truth test in a single pass; remove all non-qualifying lines; verify that session startup context utilization returns to baseline.
