---
name: "Feature Flag Lifecycle as Deployment Governance"
summary: "5-stage feature flag promotion lifecycle (add → dogfood → preview → stable → remove) with explicit file-change recipes per stage, validation steps, and follow-up issue creation for cleanup. Each stage has a defined blast radius and rollback mechanism. Keeps flags for 1-2 release cycles after stable promotion for safe rollback."
implementation_notes: null
category: "Governance"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
pipeline_status: "extracted"
consumed_by:
  - "skills/feature-flag-lifecycle-deployment-governance.md"
---

# Feature Flag Lifecycle as Deployment Governance

## Pattern

A 5-stage promotion lifecycle for feature flags, each with explicit file-change recipes:

| Stage | Mechanism | Blast Radius | Rollback |
|-------|-----------|--------------|----------|
| **Add** | Create FeatureFlag variant | Nobody | Delete variant |
| **Dogfood** | Add to `DOGFOOD_FLAGS` array | Internal team | Remove from array |
| **Preview** | Add to `PREVIEW_FLAGS` (auto-includes dogfood) | Preview channel | Remove from array |
| **Stable** | Add to Cargo `default` features + lib.rs bridge | All users | Remove from `default` |
| **Remove** | Delete flag, dead code branches, config entries | N/A (cleanup) | N/A |

**Key constraints:**
- Do NOT remove the flag immediately after stable promotion (keep 1-2 release cycles for rollback)
- Each promotion stage has 1-3 specific files to change (documented in skill)
- Validation step after each change (cargo fmt + clippy)
- Follow-up Linear issue created for cleanup

**Dual-layer flag system:**
- **Runtime**: Arrays in `features.rs` (DOGFOOD_FLAGS, PREVIEW_FLAGS, RELEASE_FLAGS) — enabled per-channel at startup
- **Compile-time**: Cargo features in `Cargo.toml` + `#[cfg(feature = ...)]` bridge in `lib.rs`

## Why It Matters

Gives deployment governance the same rigor as code review. Each promotion is a deliberate decision with known blast radius and rollback path. The staged approach prevents premature exposure while the "keep for rollback" rule prevents premature cleanup. The recipe-style skill definition means agents can execute promotions correctly without deep system knowledge.

## How It Could Fail

- Flag proliferation (too many active flags create combinatorial testing burden)
- Cleanup debt (follow-up issues get deprioritized)
- Runtime/compile-time mismatch if bridge isn't maintained
- Agent executes promotion recipe without understanding the feature's readiness

## Evidence

Warp (warpdotdev/warp) — `promote-feature` skill with detailed recipes per stage, `remove-feature-flag` skill for cleanup, `add-feature-flag` skill for creation. `warp_core/src/features.rs` with flag arrays. Production-tested across the Warp product.

## Extraction Note — 2026-05-24
Extracted as **skill**: [[feature-flag-lifecycle-deployment-governance]] in `extracts/skills/`
