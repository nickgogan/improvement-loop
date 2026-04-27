---
title: "CLAUDE.md Is a Symlink to AGENTS.md at Every Governance Boundary — Multi-Tool Compatibility Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "distributed-boundary-guides"
identification_report: "agent-governance-and-trust.harvest-queue.md::distributed-boundary-guides::rule::claudemd-symlink-to-agentsmd-at-every-governance-boundary"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "projects that distribute governance files (CLAUDE.md, AGENTS.md, or equivalent) across subsystem boundaries"
    - "codebases that need multi-tool AI compatibility — Claude Code reading CLAUDE.md while another tool reads AGENTS.md or a different convention file"
    - "monorepos and multi-package layouts where governance is scoped per subdirectory rather than centralized at the root"
  platform_coupling: "specific:filesystems-with-symlink-support"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — replacing a symlink with a regular file (or vice versa) is a single command and leaves no migration debt"
  auditability: "high when CI checks symlink targets at every governance boundary; medium when checked only at PR review; low when relied on by convention"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-observed in OpenClaw at 4+ subsystem boundaries. Pattern is a pragmatic engineering solution to multi-tool compatibility; no widespread published adoption beyond practitioner reports."
contract:
  preconditions: "The project maintains governance files (CLAUDE.md, AGENTS.md, or equivalent) at one or more directory boundaries. The project supports symlinks at the platform level — Linux, macOS, and modern Windows configurations qualify; restricted Windows environments may not. The project has a designated canonical governance filename (typically AGENTS.md, but parameterizable per project policy)."
  invariants: "At every governance boundary in the project, the canonical governance file exists as a regular file, and every other tool-specific convention name at the same boundary (CLAUDE.md, .cursorrules, etc.) exists as a symlink pointing to that canonical file. No two regular governance files exist at the same boundary — exactly one canonical, plus zero or more symlinks. The symlink targets are local (same directory), never cross-directory or absolute, so the boundary remains self-contained when files are moved together."
  governance: "Owner: any policy that establishes the canonical governance filename for the project (a root README, a CONTRIBUTING.md, a project-policy doc, or equivalent). The rule must declare which filename is canonical and which are symlinks. CI tooling enforces the invariant at every governance-file location: a check that walks every directory containing any governance-named file, identifies the canonical, and verifies all other governance-named files are symlinks pointing at that canonical. Exemptions (a tool that mandates a regular file, not a symlink) must be declared explicitly with a stated scope and justification."
  recovery: "If a regular file exists where a symlink should be: diff against the canonical to identify drift, reconcile content into the canonical, replace the regular file with a symlink, commit. If a symlink points outside the boundary or to the wrong target: re-point or recreate. If symlinks are not supported in a downstream environment (a CI system, a Windows developer's machine without symlink support): fall back to the explicit-mirror exemption — declare the regular-file copies in policy, automate their generation from the canonical at build time, and validate equality in CI."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance-files"
  - "multi-tool-compatibility"
  - "symlink"
  - "distributed-governance"
---

# CLAUDE.md Is a Symlink to AGENTS.md at Every Governance Boundary — Multi-Tool Compatibility Rule

**Source:** [[distributed-boundary-guides]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

The project maintains governance files at one or more directory boundaries — root only, or root plus subsystem boundaries. Multiple AI tools or conventions read different filenames at those boundaries (Claude Code reads CLAUDE.md; other tools read AGENTS.md, .cursorrules, etc.). The project has a single source of truth for governance content per boundary.

Scope of application: file-system discipline at governance boundaries. Applies on platforms where symlinks are first-class (Linux, macOS, modern Windows configurations). Restricted environments without symlink support fall to the explicit-mirror exemption defined under Recovery.

## Action

**Required:** At every governance boundary, designate exactly one canonical governance file (typically AGENTS.md) as a regular file. Every other governance-named file at the same boundary (CLAUDE.md, .cursorrules, etc.) must be a symlink whose target is the canonical file in the same directory. Symlink targets are local (same-directory), never absolute or cross-directory.

**Forbidden:** Maintaining two or more regular governance files at the same boundary (CLAUDE.md as a regular file alongside AGENTS.md as a regular file). Symlink targets that point across directories or to absolute paths. Manual mirroring (copy-paste) of governance content between filenames at the same boundary in lieu of symlinking.

## Boundary

Enforced at any directory containing one or more governance-named files. Applies project-wide: the root, every subsystem boundary, every nested boundary. The rule does not prescribe whether a project should distribute governance across boundaries — that is a separate decision. It prescribes only the symlink discipline at each boundary that does have governance files.

Out of scope: directories with no governance file, files unrelated to governance (READMEs, contributor docs not consumed by AI tools), and tool-specific files that are not at a governance boundary.

## Enforcement

- **Mechanism:** A CI check (or pre-commit hook) walks every directory that contains any governance-named file. For each such directory, it identifies the canonical (the regular file) and verifies every other governance-named file is a symlink whose target resolves to the canonical in the same directory.
- **Check (deterministic):** For each governance directory `D`: `count(regular_governance_files in D) == 1` AND `for every other governance_named_file F in D: is_symlink(F) AND readlink(F) == basename(canonical) AND resolves_within(D)`. Any branch false → violation.
- **Violation response:**
  - *Two regular files (no symlink):* diff for content drift; reconcile into the canonical; replace the non-canonical regular file with a symlink to the canonical.
  - *Symlink points to wrong target:* re-point the symlink to the canonical in the same directory.
  - *Symlink points outside the boundary or absolute path:* recreate as a same-directory symlink.
  - *No regular file (only symlinks):* the boundary has no source of truth; promote one symlink to canonical (replace it with a regular file) and re-point the rest.
- **Exemption (explicit-mirror):** If symlinks are not supported in a downstream environment, the rule may be relaxed at boundaries that need cross-environment compatibility. The exemption requires: (a) explicit policy declaring the affected boundary, (b) automation that regenerates the mirror from the canonical at build/CI time, (c) CI equality check between the canonical and each mirror.

## Rationale

The rule exists because multiple AI tools read different governance filenames at the same boundary. Without a discipline, the natural drift is two-or-more regular files that gradually disagree — Claude Code sees one set of rules in CLAUDE.md, another tool sees a different set in AGENTS.md, and humans cannot tell which is authoritative.

The symlink solution is the minimum-viable mechanism: one canonical file as the single source of truth, every other tool-specific filename as a same-directory symlink. Tools see identical governance content; humans edit one file; drift is structurally impossible because there is only one file with content.

The rule is the positive-space restatement of the multi-name-drift anti-pattern. Rather than enumerating ways drift can occur (manual mirroring, partial updates, tool-specific edits, branch divergence), the positive invariant is "one canonical regular file per boundary; everything else is a symlink to it." One rule, deterministic enforcement.

## Failure Modes

- **Cross-platform symlink fragility.** A developer or CI system on a platform without symlink support sees broken files; the boundary fails to load. Mitigation: detect at CI time; fall to the explicit-mirror exemption with automated regeneration; never silently degrade.
- **Symlink target drift across directory moves.** A boundary directory is moved; the symlink relative-path target stays valid only if the canonical moves with it. Mitigation: keep targets local to the same directory (never cross-directory or absolute); the rule enforces this at the symlink-creation step.
- **Tooling that mandates a regular file.** Some build tools, packagers, or IDE integrations refuse to follow symlinks. Mitigation: scope the exemption explicitly; document which tool requires a regular file and why; treat such cases as known-bounded rather than ambient.
- **Canonical-name disagreement across the ecosystem.** Different tool ecosystems prefer different canonicals (AGENTS.md vs OWNERS.md vs .agent-rules). Mitigation: pick one per project and write it down; the rule does not prescribe which canonical, only that there be one per boundary.
- **Multi-canonical sprawl at one boundary.** A boundary acquires both AGENTS.md and a "second canonical" because a new tool is onboarded with its own preferred name and someone copies content rather than symlinking. Mitigation: the CI check catches this — `count(regular_governance_files) > 1` is a violation; refactor to one canonical plus symlinks.
- **Symlink-aware editor behavior.** Some editors break or follow symlinks in ways that confuse the user during edits. Mitigation: prefer editing the canonical by name; document the symlink topology in the project's contributor guide.

## Contract

### Preconditions
The project maintains governance files (CLAUDE.md, AGENTS.md, or equivalent) at one or more directory boundaries. The project supports symlinks at the platform level — Linux, macOS, and modern Windows configurations qualify; restricted Windows environments may not. The project has a designated canonical governance filename (typically AGENTS.md, but parameterizable per project policy).

### Invariants
At every governance boundary in the project, the canonical governance file exists as a regular file, and every other tool-specific convention name at the same boundary (CLAUDE.md, .cursorrules, etc.) exists as a symlink pointing to that canonical file. No two regular governance files exist at the same boundary — exactly one canonical, plus zero or more symlinks. The symlink targets are local (same directory), never cross-directory or absolute, so the boundary remains self-contained when files are moved together.

### Governance
Owner: any policy that establishes the canonical governance filename for the project (a root README, a CONTRIBUTING.md, a project-policy doc, or equivalent). The rule must declare which filename is canonical and which are symlinks. CI tooling enforces the invariant at every governance-file location: a check that walks every directory containing any governance-named file, identifies the canonical, and verifies all other governance-named files are symlinks pointing at that canonical. Exemptions (a tool that mandates a regular file, not a symlink) must be declared explicitly with a stated scope and justification.

### Recovery
If a regular file exists where a symlink should be: diff against the canonical to identify drift, reconcile content into the canonical, replace the regular file with a symlink, commit. If a symlink points outside the boundary or to the wrong target: re-point or recreate. If symlinks are not supported in a downstream environment (a CI system, a Windows developer's machine without symlink support): fall back to the explicit-mirror exemption — declare the regular-file copies in policy, automate their generation from the canonical at build time, and validate equality in CI.
