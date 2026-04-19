---
title: "Tech Stack Pinning Table for Library Drift Prevention"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "tech-stack-pinning-table-for-drift-prevention"
confidence: "HIGH"
tier: "auto"
reason_codes:
  - "scaffold"
  - "named-variables"
  - "repeatable-generation"
  - "build-artifact"
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Dependency choices made. Update authority designated. Rendered file configured as always-loaded agent context."
  invariants: "Pinning table is single source of truth for authorized dependencies. Agents never install unlisted packages or bump versions without approval. Table reviewed at specified cadence."
  governance: "Owner: project owner. Version bumps follow embedded protocol. Template structure changes require Meta-System DD. Scoped per-project."
  recovery: "Unlisted package installed: revert and flag. Stale table: block new work until reviewed. Security vulnerability: emergency bump with async approval and documentation."
tags:
  - "extracted-artifact"
  - "template"
---

# Tech Stack Pinning Table for Library Drift Prevention

**Source:** [[tech-stack-pinning-table-for-drift-prevention]]
**Form:** template
**Extraction date:** 2026-04-19

A governance artifact that pins authorized technologies and version constraints for agent-driven development projects. Loaded as always-on context to prevent agents from silently substituting packages when encountering friction.

## Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `{{PROJECT_NAME}}` | string | Yes | Name of the project this pinning table governs. |
| `{{LAST_REVIEWED}}` | ISO 8601 date | Yes | Date of last human review of the pinning table. |
| `{{REVIEW_CADENCE}}` | string | Yes | How often the table should be reviewed (e.g., "monthly", "per-milestone", "quarterly"). |
| `{{RUNTIME_ENTRIES}}` | table rows | Yes | Runtime dependency entries (one row per pinned package). |
| `{{DEV_ENTRIES}}` | table rows | Yes | Dev/build dependency entries (one row per pinned package). |
| `{{INFRA_ENTRIES}}` | table rows | No | Infrastructure tool entries (e.g., Docker, Terraform versions). |
| `{{FORBIDDEN_PACKAGES}}` | table rows | No | Packages explicitly forbidden with rationale. |
| `{{UPDATE_AUTHORITY}}` | string | Yes | Who can authorize version bumps (e.g., "Nick", "Architect agent + Nick approval"). |

## Body

```markdown
---
title: "Tech Stack Pinning Table — {{PROJECT_NAME}}"
type: "governance"
category: "project-lifecycle"
stage: "active"
created: "{{LAST_REVIEWED}}"
updated: "{{LAST_REVIEWED}}"
author: "nick"
tags:
  - "tech-stack"
  - "dependency-management"
  - "drift-prevention"
---

# Tech Stack Pinning Table — {{PROJECT_NAME}}

> **For agents:** This file is loaded on every execution. You MUST use ONLY the packages and versions listed below. If a pinned dependency causes an error, fix the error — do NOT install an alternative package. If a version bump is genuinely required (security vulnerability, critical bug), flag it for human review rather than making the change.

**Last reviewed:** {{LAST_REVIEWED}}
**Review cadence:** {{REVIEW_CADENCE}}
**Update authority:** {{UPDATE_AUTHORITY}}

## Runtime Dependencies

| Package | Version Constraint | Rationale | Alternatives Considered |
|---------|-------------------|-----------|------------------------|
{{RUNTIME_ENTRIES}}

## Dev / Build Dependencies

| Package | Version Constraint | Rationale | Alternatives Considered |
|---------|-------------------|-----------|------------------------|
{{DEV_ENTRIES}}

## Infrastructure

| Tool | Version Constraint | Rationale |
|------|-------------------|----------|
{{INFRA_ENTRIES}}

## Forbidden Packages

These packages MUST NOT be installed under any circumstances.

| Package | Reason |
|---------|--------|
{{FORBIDDEN_PACKAGES}}

## Version Bump Protocol

1. Agent encounters a genuine blocker with a pinned version (not a usage error).
2. Agent documents: the error, the pinned version, the minimum version that fixes it, and the changelog delta.
3. Agent flags for human review — does NOT make the change.
4. {{UPDATE_AUTHORITY}} reviews and either approves the bump or provides a workaround.
5. If approved: update this table, commit with rationale, and note the change in the system log.

## Staleness Warning

If `{{LAST_REVIEWED}}` is older than the `{{REVIEW_CADENCE}}` interval, this table may be stale. Flag for review before starting new work.
```

## Usage

Render this template when initializing a new agent-driven development project or when retrofitting dependency governance onto an existing project. The rendered file should be placed in the project root (e.g., `tech-stack.md`) and configured as an always-loaded context file via `dev-load-always-files` or equivalent mechanism.

## Variation Axis

- **Project type:** Web app, CLI tool, data pipeline, infrastructure — determines which dependency categories are populated.
- **Maturity:** Greenfield projects may have sparse tables; mature projects will have extensive pinning with rationale.
- **Team size:** Single-agent projects may use simpler version constraints; multi-agent setups need stricter pinning because different agents have different package preferences.
- **Language ecosystem:** Package manager conventions vary (npm semver ranges vs. Python pinning vs. Go module versions). The Version Constraint column format adapts to the ecosystem.

## Contract

### Preconditions
- The project's dependency choices have been made (this template documents decisions, it does not make them).
- An update authority is designated.
- The rendered file is configured as always-loaded agent context.

### Invariants
- The pinning table is the single source of truth for authorized dependencies in the project.
- Agents never install packages not listed in the table.
- Agents never bump versions without human approval via the Version Bump Protocol.
- The table is reviewed at the specified cadence.

### Governance
- **Owner:** The project owner (typically the Architect agent + Nick).
- **Modification gate:** Version bumps follow the protocol in the template. Structural changes to the template itself require a Meta-System DD.
- **Scope:** Per-project. Each project has its own rendered instance.

### Recovery
- If an agent installs an unlisted package: revert the change, flag the package for evaluation, and add it to the Forbidden list or the pinning table after review.
- If the table is stale (past review cadence): block new development work until the table is reviewed and `{{LAST_REVIEWED}}` is updated.
- If a pinned version has a known security vulnerability: emergency bump protocol — update authority can approve asynchronously, but the bump must still be documented.
