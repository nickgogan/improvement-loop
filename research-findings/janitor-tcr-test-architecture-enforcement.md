---
name: "Janitor Static Analysis with TCR Workflow"
summary: "n8n's janitor is a custom AST-based static analysis tool for Playwright test architecture enforcement with 7 rules (selector-purity, no-page-in-flow, boundary-protection, etc.). Uses TCR (test-commit-revert): changes commit only if tests pass, revert if they fail. Includes baseline tracking for incremental cleanup."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - {file: "specification-as-governance-fourth-enforcement-philosophy.md", rel: "same-problem"}
  - {file: "two-level-verification-agent-run-plus-harness-inte.md", rel: "same-problem"}
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

n8n has a custom `janitor` tool in `packages/testing/janitor/` that performs AST-based static analysis of Playwright test files. It enforces 7 architectural rules:

1. **Selector purity** — test selectors must follow specific patterns
2. **No-page-in-flow** — flow files cannot access Playwright's page object directly
3. **Boundary protection** — test layers must respect boundaries (Tests → Flows → Page Objects → Components → Playwright API)
4. **Scope lockdown** — tests scoped to their designated areas
5. **Dead code detection** — unused test utilities flagged
6. **Deduplication** — duplicate test logic identified
7. **Duplicate logic** — similar patterns that should be extracted

The janitor uses a **TCR (Test-Commit-Revert)** workflow: changes are automatically committed if tests pass, and automatically reverted if tests fail. This is a strict quality gate — there is no "commit anyway" option. If your change breaks the architectural rules, it's undone.

Baseline tracking enables incremental adoption: existing violations are recorded in a baseline, and the tool only flags new violations. This prevents a "fix everything first" blocking pattern.

## Why It Matters

Test architecture degrades over time as developers take shortcuts — accessing page objects directly from tests, duplicating selectors, bypassing abstraction layers. Traditional code review catches some of these, but architectural rule violations are easy to miss in PR reviews and tedious to enforce manually.

The TCR workflow is particularly interesting: it's a harder gate than CI — instead of blocking a merge, it reverts the local change. This creates immediate feedback and makes architectural violations impossible to commit, not just impossible to merge.

## Why People Are Using It

Observed in [n8n](https://github.com/n8n-io/n8n) v2.16.0 — see [[n8n-analysis]] for structural details. The janitor operates on n8n's substantial Playwright test suite and is integrated into the development workflow via the `packages/testing/playwright/AGENTS.md` context file.

## Potential Alternatives

ESLint rules for architectural patterns (less precise for cross-file rules). Manual code review checklists (slower, less consistent). CI-only enforcement without TCR (catches at merge time, not authoring time).

## Potential Improvements

Extending the pattern beyond test architecture to application code layer boundaries. Auto-fix capabilities for common violations. Integration with AI agents so the janitor can explain why a change was reverted and suggest alternatives.

## Potential Failure Modes

Baseline inflation if violations are added to the baseline instead of fixed. Developer frustration with TCR auto-revert for non-obvious violations. False positives from AST analysis that doesn't understand intent.
