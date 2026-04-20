---
notion_id: 32b1e08b-9b34-8126-a3ba-d46430fb3821
name: Mandatory User Acceptance Testing (UAT) at Phase Boundaries
summary: PAUL enforces a guided UAT at the end of every build phase before proceeding, requiring actual verification that APIs work and features are functional. GSD only checks file structure statically,
  allowing silent success assumptions to accumulate into a broken final build.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Mandatory User Acceptance Testing (UAT) at Phase Boundaries

## What It Is
Between each development phase, PAUL prompts the developer to run and confirm that the built functionality actually works end-to-end (API calls, UI flows, integrations). Only after explicit approval does it proceed to the next phase. This is contrasted with GSD, which treats file creation as proof of completion.

## Why It Matters
AI agents tend to hallucinate success — they generate code and assume it works. Without a real execution checkpoint, errors compound silently across phases, leading to a final deliverable that requires extensive debugging. PAUL's UAT forces reality checks at every phase boundary.

## Why People Are Using It
Developers building for clients who need to see working features before sign-off benefit most. The mandatory checkpoint also prevents drift from original product requirements (the requirements defined in the initial project MD).

## Potential Alternatives
Automated test suites (Vitest, Jest, Playwright) run as part of the build pipeline; CI/CD integration with staged gates; manual developer review without plugin scaffolding.

## Potential Improvements
PAUL could integrate automated test runners into its UAT step so not all verification requires manual human testing. AI-generated test cases per phase would further harden the gate.

## Potential Failure Modes
If developers rubber-stamp the UAT without genuinely testing, the safety gate becomes theater. For complex integrations (OAuth flows, third-party webhooks), UAT may be difficult to perform locally in a meaningful way.
