---
name: CareerBuddy ops-doc-sync — C1-C16 deterministic audit battery
source_type: "Repository"
status: Done
key_takeaways: CareerBuddy enforces its documentation-governance surface with one stdlib-only read-only Python script running 16 named checks (registry completeness, dead links, index bidirectionality, separability/privacy boundaries, size budgets, sha256 manifest-hash freshness), each with error/warn severity and an embedded remediation instruction. The wrapping SKILL.md composes it with an LLM fidelity sweep under strict sequencing — audit before edit, fidelity not delta, re-run to exit 0 before the single commit. Grounds the engine restructure program's "deterministic enforcement as first-class citizen" principle with a production reference design.
relevance: High
added_by: Nick
tags: [deterministic-enforcement, doc-governance, drift-detection, audit-script, content-hashing]
url: https://github.com/nickgogan/CareerBuddy (.github/skills/ops-doc-sync/)
authority: []
findings:
- deterministic-doc-audit-battery.md
- manifest-hash-drift-detection-for-derived-docs.md
- two-layer-ci-plus-llm-review-gate.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-12'
---

# CareerBuddy ops-doc-sync — C1-C16 deterministic audit battery

The `ops-doc-sync` skill from CareerBuddy (Nick's other agentic system): a documentation-governance audit built around `scripts/audit_docs.py`, a single ~580-line stdlib-only script implementing 16 deterministic checks (C1-C16) over the workspace's doc surface — governance-registry completeness, dead relative links, load-order routing anchors, HUMANS/AGENTS pairs, bidirectional skills-index integrity, export-set separability (user-id leak scan), volatile-metric warnings, workflows-cookbook coverage, control-surface purity, wiring-manifest sha256 drift (against `onboarding/wiring-manifest.json` written by the producing skill), root-file whitelisting, PROGRESS line budgets (soft/hard caps), artifact-matrix cross-referencing, distribution-package completeness, system-contract integrity, and trigger-eval coverage. The SKILL.md wraps the script in a four-step workflow (deterministic audit → LLM fidelity sweep → one human-gated fix batch → apply, re-run to exit 0, single commit) with reversibility-tiered autonomy and stop rules. Extracted 2026-07-12 from a local clone as grounding for the engine restructure program's deterministic-enforcement design principle and the Phase 2 ops-doc-sync pattern-lift.
