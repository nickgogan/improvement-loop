# Changelog

Notable changes to the **ops-vision-to-plan** package. Format:
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning:
[SemVer](https://semver.org/) via `metadata.version` in SKILL.md.

---

## [0.3.0] — 2026-07-10

### Added
- **`evals/trigger-eval.md`** — distilled install-acceptance trigger-eval set
  (20 queries + expected verdicts, generic by construction) per meta-skill-author
  §2.1/§6. Landed 2026-07-09 with workspace milestone MV22; recorded here at the
  MV20 paste-bundle refresh.

### Changed
- **Ports re-derived** — both port manifests gain the `evals/trigger-eval.md` row
  (travels with every port); the Glean port's install steps gain the
  self-administered acceptance check; source-version stamps re-pinned.

## [0.2.0] — 2026-07-09

### Added
- **`capability-contract.yaml`** — machine-readable capability sidecar per
  meta-skill-author §4.0 (workspace lesson L-11 backfill): `human-approval-channel`
  as **required**-tier (the section gate is the method — inert without it) plus
  three optional capabilities (durable-document-store, reference-bundle-attachment,
  versioned-checkpoints) with degradations from the generic's contract table. The
  generic's progress-reconciliation row stays a process-level dependency outside
  the host-capability vocabulary.
- **`compatibility` frontmatter prose** derived from the sidecar.
- **"Host capabilities required" block in `ports/glean-agent.md`** — the sidecar
  rendered against the Glean adapter's `## Provides` inventory.

## [0.1.0] — 2026-07-09

### Added
- **Distribution package retrofit.** README, this CHANGELOG, SOURCES.md (upstream-method
  map: BMAD planning arc, Superpowers execution discipline), and semver-normalized
  `metadata.version` (`0.1` → `0.1.0`), required by the skill's
  `distribution-scope: "exportable"` declaration (meta-skill-author §1.3/§6).
- **`ports/generic.md`** — stage-1 harness/workspace-neutral canon per
  meta-skill-author §4.0: capability contract (durable documents, section templates,
  approval channel, versioned checkpoints, progress-reconciliation process),
  parameterized invocation inputs, platform-neutral bundled-file manifest.
- **`ports/glean-agent.md`** — stage-2 paste-ready Glean Agent Builder port.

### Pre-changelog history

The skill shipped at 0.1 (its only prior version); its origin — distilling the BMAD
planning arc and Superpowers execution discipline into this workspace's native PM
system — is recorded in the source workspace's git log and HISTORY.md.
