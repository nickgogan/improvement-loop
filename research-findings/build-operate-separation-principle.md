---
notion_id: 32b1e08b-9b34-8181-9c52-e27a49327397
name: Build/Operate Separation Principle
summary: 'A foundational architectural principle: builder tools (S3: Claude Code, Cursor, vault) are strictly separated from operator tools (S2: Notion, Custom Agents). S3 deploys to S2 via MCP and Playwright;
  S2 never calls back to S3. Governs all cross-system architectural decisions.'
implementation_notes: null
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
proposer_priority: Not Flagged
applicability:
- General
adopted_in:
- General / Cross-System
sources:
- four-system-separation-session-research.md
proposals: []
date_discovered: '2026-03-16'
last_updated: '2026-04-19'
related_findings:
- file: skill-vs-process-distinction-deterministic-rails.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Build/Operate Separation Principle

## What It Is
A foundational architectural principle that enforces strict separation between build-time and run-time systems. S3 (Claude Code + Cursor + vault) is the builder: it authors, tests, and deploys system components. S2 (Notion + Custom Agents) is the operator: it runs those components in production. Deployment flows one way — S3 pushes to S2 via MCP and Playwright. S2 never reaches back into S3. The principle is encoded in system-boundary.md and the Four-System Architecture Notion page.

## Why It Matters
Without this boundary, build-time and run-time concerns blur. Operators start making ad-hoc modifications to components they should only consume. Builders get entangled in operational concerns. The separation creates a clean contract: S3 owns the system's design and correctness; S2 owns its execution. This makes the system auditable, stable, and easier to evolve.

## Why People Are Using It
The principle emerged from 14-video analysis of production multi-agent architectures combined with direct architectural insight. It is a DD-29 level decision — one that constrains dozens of downstream choices. Its adoption is already reflected in the Four-System Architecture and governs how all future integrations are designed. Nate B Jones reinforces this from the enterprise agent deployment angle: agents should not decide workflow sequencing, only execute within hardwired process rails. His "clarity of intent" prerequisite maps directly -- the builder must encode intent into deterministic structures before the operator (agent) touches them. Without this separation, agents produce "generic average" output that "works for everybody and therefore for nobody."

## Potential Improvements
The principle could be formalized as a machine-readable constraint that agents check before taking cross-system actions, rather than relying solely on documentation. A boundary-violation detection step in the improvement loop could flag cases where S2 actions implicitly depend on S3 artifacts not yet deployed.

## Potential Failure Modes
The boundary erodes during "quick fix" moments — when an operator-side issue seems easier to patch directly than to route through a proper S3 build cycle. One-off exceptions accumulate into undefined hybrid states. Without enforcement tooling, the principle lives only in documentation and can be forgotten or overridden under time pressure.
