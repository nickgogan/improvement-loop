---
title: "Design for the Most-Restricted Surface, Declare Compatibility for the Rest"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-cross-surface-portability-with-constraints"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "designing-agent-tools.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors of a packaged, reusable agent capability (a skill, plugin, or extension folder) intended to run on more than one deployment surface"
    - "teams or platform maintainers distributing the same capability package to environments with different runtime profiles — some sandboxed and offline, some with full local access"
  platform_coupling: "agnostic — the evidencing example is one vendor's skill ecosystem (three surfaces sharing a folder format but differing in network access, package-install rights, and filesystem model), but the discipline — build for the most-restricted floor, declare anything beyond it — applies to any packaged-capability format shipped across multiple runtime environments with a manifest or frontmatter mechanism for declaring requirements"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — declaring a requirement in the manifest is a trivial edit, but retrofitting a skill's actual implementation to function within a more restricted floor (removing a network call, an ambient package install, an assumed filesystem write) can require redesigning the skill's core logic, not just relabeling it"
  auditability: "high for the declaration itself — a requirements/compatibility field is a lintable manifest value, and a corpus scan can flag operations (network calls, package installs, filesystem access beyond a sandbox) that lack a matching declaration; lower for whether the declaration is actually correct, since that requires running the skill on the real restricted surface rather than just reading its source"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "The per-surface capability matrix and the compatibility-declaration mechanism are both already part of one vendor's published skill specification and documented consistently across its canonical sources; no confirmation found of design-for-the-floor being applied as a checked authoring discipline in that ecosystem's own skill catalogs at time of extraction."
contract:
  preconditions: "A packaged capability (skill, plugin, extension) is intended to run, or is already running, on two or more deployment surfaces whose runtime profiles differ in at least one capability dimension (network access, package-install rights, filesystem access, execution sandboxing). The packaging format or hosting environment provides a manifest, frontmatter, or equivalent field for declaring requirements beyond a baseline. The author can enumerate, or look up, the capability floor of the most-restricted surface the package targets."
  invariants: "The package's core behavior functions correctly under the most-restricted target surface's capability floor unless the package explicitly declares a requirement for something beyond that floor. Every capability the package's implementation actually depends on beyond the floor (network calls, runtime package installation, filesystem access outside a sandbox, or equivalent) has a corresponding declaration in the requirements/compatibility field. The declaration is kept current as the implementation changes — a capability added to the code without an updated declaration is a defect, not a documentation lag."
  governance: "Owner: whoever authors or maintains the capability package. Authoring guidance and templates for the package format should prompt authors to identify each target surface's constraints and populate the requirements/compatibility field accordingly. Platform or catalog maintainers who publish packages across multiple surfaces enforce the declaration at publish time — either as a manual review step or lint tooling. Consumer-side audit tooling that reviews capability packages checks that the declared requirements are consistent with what the implementation actually does."
  recovery: "If a package fails at runtime on a given surface because it silently assumed a capability the surface doesn't offer (a network call fails on an offline surface, a package-install step fails on a locked-down surface) → treat as an authoring defect, not a platform bug; either refactor the implementation to work within that surface's floor, or add/correct the requirements declaration and restrict deployment to surfaces that meet it. If a requirements declaration exists but was authored without testing against the actual restricted surface → verify it before treating it as reliable; an untested declaration is a claim, not a guarantee. If the same package is deployed independently to multiple surfaces and drifts (one copy updated, others stale) → resynchronize from the maintained source before relying on cross-surface behavioral parity."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-design"
  - "portability"
  - "compatibility"
---

# Design for the Most-Restricted Surface, Declare Compatibility for the Rest

**Source:** [[skill-cross-surface-portability-with-constraints]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A packaged, reusable agent capability — a skill folder, plugin, or extension — is authored for deployment to more than one runtime surface, and those surfaces do not guarantee identical capabilities. Typical differences: network access (available vs. blocked), package installation (local installs allowed vs. pre-installed-only), and filesystem access (full vs. sandboxed). The packaging format provides a manifest or frontmatter field where the author can declare requirements beyond a shared baseline.

## Action

**Required:** Design the package's core behavior to function correctly under the most-restricted target surface's capability floor — the surface with the least network access, the most locked-down package-install policy, and the tightest filesystem sandbox among the surfaces the package targets. When the package genuinely needs a capability beyond that floor, declare it explicitly in the requirements/compatibility field rather than relying on it silently.

**Forbidden:** Authoring a package that assumes capabilities present only on the richest surface (ambient network access, arbitrary package installation, unrestricted filesystem writes) without declaring that dependency. Shipping a package to a restricted surface without having tested it there, when the only evidence of compatibility is that it worked on a richer surface during development.

## Boundary

Enforced at package-authoring time — when the implementation is written and the requirements/compatibility field is populated — and at pre-publish or pre-deployment review, before the package is made available on a given surface. Applies per surface: a package deployed to several surfaces must satisfy this discipline (floor-compliant, or floor-compliant-plus-declared) independently for each one.

Does not apply to a package deliberately scoped to a single surface with no portability intent — that package can assume whatever the one surface offers, since there is no cross-surface mismatch to guard against.

## Enforcement

- **Mechanism:** Review or lint the package's implementation for operations that imply an elevated capability — outbound network calls, package-manager invocations, filesystem writes outside an expected sandbox root — and cross-check each against the requirements/compatibility field. An undeclared elevated-capability operation is a flag.
- **Check (deterministic):** `(implementation contains an elevated-capability operation) IMPLIES (requirements/compatibility field declares the corresponding requirement)`. False → violation. Separately: `(package claims compatibility with surface X) IMPLIES (package has been run, or reviewed against documented constraints, on surface X)`. False → unverified compatibility claim, flagged but not necessarily blocking.
- **Violation response:**
  - *Undeclared elevated-capability operation found:* either remove/guard the operation so the package works within the floor, or add the missing declaration and scope deployment to surfaces that satisfy it.
  - *Compatibility claimed but untested:* run or review the package against the claimed surface's actual constraints before trusting the claim; downgrade the claim to "declared, unverified" until then.
- **Cannot be self-certified:** An author's belief that "it should work" on a surface they haven't tested against is not evidence; the surface's actual constraint profile (network policy, install policy, filesystem model) is the ground truth, and testing or documented-constraint review against it is what closes the loop.

## Rationale

A packaging format can guarantee file-shape portability — the same folder, the same manifest fields — while leaving runtime portability entirely open. A capability that works because a rich development surface happened to allow it (network access, local installs) is not evidence the package works everywhere the format is nominally supported. Designing for the most-restricted surface first makes the default behavior portable by construction; declaring elevated requirements explicitly, rather than discovering them as runtime failures on a stricter surface, turns an implicit assumption into a checkable fact. This also makes a package's actual footprint reviewable before deployment — a security- or platform-reviewer can read the declaration instead of having to run the package on every surface to find out what it needs.

## Failure Modes

- **Developed and tested only on the richest surface.** The package works throughout development because the author's environment allows everything; it fails the first time it runs on a more restricted surface, and the failure looks like a platform bug rather than an authoring gap. Mitigation: test on the most-restricted claimed surface before considering the package done, not just the surface the author happens to be using.
- **Stale declaration.** The implementation gains a new elevated-capability dependency over time (a new network call added in a later revision) but the requirements field is never updated to match. Mitigation: treat capability declarations as part of the change under review whenever the implementation changes, not a one-time setup step.
- **Declared but unverified.** An author declares a requirement defensively ("might need network") without confirming what the package actually needs, producing an over-broad or under-specific declaration that downstream reviewers can't rely on. Mitigation: derive the declaration from what the implementation demonstrably does, not from a guess.
- **Independent per-surface copies drift.** The same package, deployed separately to each surface rather than synced from one maintained source, is patched on one surface and left stale on another; the "same skill" is no longer actually the same behavior across surfaces. Mitigation: maintain a single source of truth and treat each surface deployment as a sync target, not an independent fork.

## Contract

### Preconditions
A packaged capability (skill, plugin, extension) is intended to run, or is already running, on two or more deployment surfaces whose runtime profiles differ in at least one capability dimension (network access, package-install rights, filesystem access, execution sandboxing). The packaging format or hosting environment provides a manifest, frontmatter, or equivalent field for declaring requirements beyond a baseline. The author can enumerate, or look up, the capability floor of the most-restricted surface the package targets.

### Invariants
The package's core behavior functions correctly under the most-restricted target surface's capability floor unless the package explicitly declares a requirement for something beyond that floor. Every capability the package's implementation actually depends on beyond the floor (network calls, runtime package installation, filesystem access outside a sandbox, or equivalent) has a corresponding declaration in the requirements/compatibility field. The declaration is kept current as the implementation changes — a capability added to the code without an updated declaration is a defect, not a documentation lag.

### Governance
Owner: whoever authors or maintains the capability package. Authoring guidance and templates for the package format should prompt authors to identify each target surface's constraints and populate the requirements/compatibility field accordingly. Platform or catalog maintainers who publish packages across multiple surfaces enforce the declaration at publish time — either as a manual review step or lint tooling. Consumer-side audit tooling that reviews capability packages checks that the declared requirements are consistent with what the implementation actually does.

### Recovery
If a package fails at runtime on a given surface because it silently assumed a capability the surface doesn't offer (a network call fails on an offline surface, a package-install step fails on a locked-down surface) → treat as an authoring defect, not a platform bug; either refactor the implementation to work within that surface's floor, or add/correct the requirements declaration and restrict deployment to surfaces that meet it. If a requirements declaration exists but was authored without testing against the actual restricted surface → verify it before treating it as reliable; an untested declaration is a claim, not a guarantee. If the same package is deployed independently to multiple surfaces and drifts (one copy updated, others stale) → resynchronize from the maintained source before relying on cross-surface behavioral parity.
