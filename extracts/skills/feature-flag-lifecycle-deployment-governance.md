---
title: "Feature Flag Lifecycle as Deployment Governance"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "feature-flag-lifecycle-deployment-governance"
extraction_date: "2026-05-24"
last_change_session: 92
last_change_sl: "session-92-codifier-identify-extract"
identification_report: "2026-05-24-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Teams shipping a product to multiple user segments (internal, beta, general) who need controlled feature rollout with known blast radius at each stage"
    - "Projects where features need independent rollback paths after going to production without a full revert of the release"
    - "Codebases with both runtime feature gating (per-channel enablement) and compile-time feature gating (conditional compilation), requiring both layers to stay in sync"
    - "Agent-assisted development workflows where an AI agent executes deployment steps and needs an unambiguous, recipe-style procedure to follow without requiring deep system knowledge"
  platform_coupling: "specific:Rust/Cargo"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "medium — each stage has a documented rollback, but stable promotion exposes all users and rollback requires a coordinated deployment; remove stage is irreversible without a full git revert"
  auditability: "High: every promotion stage produces a diff in version-controlled source files. The follow-up issue provides an external audit trail for cleanup obligation. CI lint gates confirm structural correctness after each change."
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A dual-layer flag system (runtime arrays + compile-time build manifest) is already in place and operational. The codebase has a working lint/format pipeline. A Linear or equivalent issue tracker is available for cleanup follow-up. The flag being promoted exists at the stated current stage."
  invariants: "Every active flag has exactly one current stage; no flag occupies two stages simultaneously. The runtime PREVIEW_FLAGS array always includes all DOGFOOD_FLAGS entries (superset invariant). A follow-up cleanup issue exists for every flag that has reached stable and has not yet been removed. Flags are never removed in the same release cycle they reach stable."
  governance: "Owned by the team responsible for the product's deployment pipeline. Stage 3 (stable) promotions require human sign-off — agents may not self-authorize. Stage 4 (remove) requires confirmation that 1-2 release cycles have elapsed since stable promotion. The follow-up cleanup issue is the audit trail."
  recovery: "If a regression is detected after stable promotion, execute the documented rollback (remove from default features and lib.rs bridge) immediately. If the runtime/compile-time bridge is inconsistent, treat it as a blocking bug and re-execute the affected promotion stage from scratch. If cleanup debt exceeds the agreed maximum active-flag count, freeze new flag additions until the backlog is cleared."
tags:
  - "extracted-artifact"
  - "skill"
  - "deployment"
  - "governance"
---

# Feature Flag Lifecycle as Deployment Governance

**Source:** [[feature-flag-lifecycle-deployment-governance]]
**Form:** skill
**Extraction date:** 2026-05-24

## Inputs

- A feature flag identifier (name/key) and a description of the feature it gates
- The target promotion stage: `add`, `dogfood`, `preview`, `stable`, or `remove`
- The current stage of the flag (required for all stages except `add`)
- A dual-layer flag system: runtime arrays (e.g., `DOGFOOD_FLAGS`, `PREVIEW_FLAGS`, `RELEASE_FLAGS`) in a features module, and compile-time Cargo features in the build manifest
- A Linear (or equivalent) issue tracker for cleanup follow-up

## Outputs

- Specific source files modified per stage, validated by `cargo fmt` + `cargo clippy` (or equivalent)
- A follow-up issue when the flag reaches `stable` (cleanup reminder for 1-2 release cycles later)
- Updated flag arrays and/or build manifest reflecting the new promotion stage
- For `remove`: all flag references, dead code branches, and config entries deleted; follow-up issue closed

## Steps

### Stage 0 — Add

1. Create a new `FeatureFlag` variant in the flag enum (e.g., `features.rs`). Do not add it to any runtime array yet.
2. Wrap the new feature's code paths with `#[cfg(feature = "flag-name")]` or the runtime flag check.
3. Run `cargo fmt && cargo clippy`. Confirm no warnings.
4. **Blast radius:** Nobody. **Rollback:** Delete the variant and its code branches.

### Stage 1 — Dogfood

1. Add the flag name to the `DOGFOOD_FLAGS` array in `features.rs`.
2. Run `cargo fmt && cargo clippy`. Confirm no warnings.
3. Deploy to internal team only. Validate behavior before proceeding.
4. **Blast radius:** Internal team. **Rollback:** Remove the entry from `DOGFOOD_FLAGS`.

### Stage 2 — Preview

1. Add the flag name to the `PREVIEW_FLAGS` array. (The system automatically includes `DOGFOOD_FLAGS` entries in preview — verify this invariant holds.)
2. Run `cargo fmt && cargo clippy`. Confirm no warnings.
3. Deploy to preview/beta channel. Collect feedback before proceeding.
4. **Blast radius:** Preview channel users. **Rollback:** Remove the entry from `PREVIEW_FLAGS`.

### Stage 3 — Stable

1. Add the flag to Cargo default features in `Cargo.toml`.
2. Add the compile-time bridge in `lib.rs`.
3. Run `cargo fmt && cargo clippy`. Confirm no warnings.
4. **Do NOT remove the flag yet.** Keep it active for 1-2 release cycles for rollback.
5. Open a follow-up issue titled "Remove feature flag: [flag-name]" targeted at the next or next+1 release milestone.
6. **Blast radius:** All users. **Rollback:** Remove from default features and `lib.rs` bridge.

### Stage 4 — Remove

1. Delete the `FeatureFlag` variant from the enum.
2. Delete all `#[cfg(feature = "flag-name")]` branches and dead code gated behind the flag.
3. Remove the flag from all runtime arrays if still present.
4. Remove from `Cargo.toml` features and the `lib.rs` bridge.
5. Run `cargo fmt && cargo clippy`. Confirm no warnings and no dead-code warnings.
6. Close the follow-up cleanup issue.
7. **Blast radius:** None (cleanup only). **Rollback:** Not applicable.

## Failure Modes

- **Flag proliferation.** Too many active flags create combinatorial testing burden. Mitigate by enforcing a maximum active-flag count and making cleanup issues blocking items for the next milestone.

- **Cleanup debt.** Follow-up issues accumulate and get deprioritized. Mitigate by attaching cleanup issues to a specific milestone at creation time and including active-flag count in release readiness checklists.

- **Runtime/compile-time bridge mismatch.** A flag enabled at runtime but absent from Cargo default features produces inconsistent behavior. The `cargo clippy` step should surface dead-code warnings; make this a CI gate.

- **Premature stable promotion.** An agent executes the Stage 3 recipe correctly but the feature isn't ready for all users. Mitigate by requiring human sign-off before Stage 3; agents should not self-authorize stable promotions.

- **Skipped stage.** An agent or developer jumps from `add` directly to `stable`. Enforce stage ordering by requiring the previous-stage entry as a precondition.

## Contract

### Preconditions
A dual-layer flag system is in place and operational. A working lint/format pipeline exists. An issue tracker is available. The flag exists at the stated current stage.

### Invariants
Every active flag has exactly one current stage. PREVIEW_FLAGS includes all DOGFOOD_FLAGS entries. A cleanup issue exists for every flag at stable. Flags are never removed in the same release cycle they reach stable.

### Governance
Owned by the deployment pipeline team. Stable promotions require human sign-off. Remove stage requires 1-2 release cycles elapsed since stable. The follow-up issue is the audit trail.

### Recovery
On regression after stable promotion: rollback immediately. On runtime/compile-time inconsistency: treat as blocking bug, re-execute the affected stage. On cleanup debt exceeding max flag count: freeze new flag additions.
