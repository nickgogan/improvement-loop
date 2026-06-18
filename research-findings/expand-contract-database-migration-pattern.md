---
name: Expand-Contract Database Migration Pattern
summary: "Pre-commit hook enforces Phase annotation (EXPAND/MIGRATE/CONTRACT) on all database migration files. Each phase has specific rules: EXPAND only adds, MIGRATE moves data, CONTRACT only removes. Prevents mixing additive and destructive changes in a single migration, enabling safe rollback at any phase boundary."
implementation_notes: null
category: Governance
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - General
adopted_in: []
sources: []
proposals: []
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
related_findings: []
pipeline_status: raw
consumed_by: []
---

# Expand-Contract Database Migration Pattern

## What It Is

A database migration governance pattern enforced by pre-commit hooks that requires every migration file to declare its phase: EXPAND (only additive changes — new tables, columns, indexes), MIGRATE (data movement between old and new structures), or CONTRACT (only destructive changes — drop columns, remove tables). The hook validates that the migration's SQL operations match its declared phase. This ensures that rollback is safe at any phase boundary — you can always revert a CONTRACT without losing data because the MIGRATE already copied it.

## Why It Matters

Mixed migrations that simultaneously add columns, move data, and drop old columns are the leading cause of irreversible database failures. When a single migration does all three and fails mid-way, the database is left in an inconsistent state with no safe rollback point. Phase separation guarantees that at every boundary, the database is in a valid, rollback-safe state.

## Why People Are Using It

Observed in [Langflow](https://github.com/langflow-ai/langflow) v1.9.3 — see [[langflow-analysis]] for structural details. Langflow enforces this pattern via its pre-commit configuration and a dedicated `migration-validation.yml` CI workflow, ensuring no mixed-phase migration can reach the main branch.

## Potential Alternatives

Manual review with a "migration safety" label on PRs. Online schema change tools (gh-ost, pt-online-schema-change) that handle expansion and contraction atomically at the engine level. Feature flags on schema columns that allow gradual migration without a hard cutover.

## Potential Improvements

Add a state machine that tracks which phase was last completed per migration sequence, preventing out-of-order execution (e.g., running CONTRACT before MIGRATE). Generate phase annotations automatically by static-analyzing the migration SQL for additive vs. destructive statements. Include a CI check that verifies the full expand-migrate-contract cycle passes against a test database snapshot.

## Potential Failure Modes

Teams may split what should be an atomic change into three PRs for compliance, introducing windows where the schema is in an expanded-but-not-migrated state longer than necessary. The pattern adds overhead for trivial migrations (adding a nullable column needs no contract phase, but the hook may still demand phase annotation). Phase misclassification by developers — declaring EXPAND for a migration that actually drops a constraint — requires the hook to do semantic analysis, not just annotation checking.
