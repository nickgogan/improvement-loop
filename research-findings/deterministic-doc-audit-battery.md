---
name: Deterministic Documentation-Audit Battery (C1-C16)
summary: CareerBuddy enforces its entire documentation-governance surface with a single stdlib-only Python script running 16 named checks (C1-C16) — registry completeness, dead links, index bidirectionality,
  data-boundary hygiene, size budgets, manifest-hash freshness. Every check has a stable ID, error-vs-warn severity, and a remediation instruction embedded in its failure message. The LLM never re-derives
  consistency from memory; the script is the ground truth and exit 0 is the gate.
implementation_notes: 'Direct grounding for the restructure program''s "deterministic enforcement as first-class citizen" principle. The engine already has the seed: a pre-commit hook enforcing frontmatter
  validity, FOUNDATIONS sync, and the PROGRESS line budget (warn >150, block >250 — same soft/hard-cap shape as C12). Phase 2 plans an ops-doc-sync pattern-lift for whatever second-brain shape lands; this
  battery is the reference design. Engine-specific check candidates: skills-index bidirectionality (CLAUDE.md skill tables vs .claude/skills/ dirs, per C5), dead relative links in critical-path docs (C2),
  root-hygiene whitelist (C11), sources↔findings linkage (currently /linkage-repair, could become a check), and no-hardcoded-counts (C7 is exactly workspace Process Rule 3, mechanized). Key transferable
  properties: stable check IDs, remediation-in-error-message, read-only script, warnings never block.'
category: Governance
evidence_strength: Medium (practitioner-documented, single production system, script-verifiable)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-doc-sync-audit-battery.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: two-layer-ci-plus-llm-review-gate.md
  rel: same-problem
- file: manifest-hash-drift-detection-for-derived-docs.md
  rel: extends
- file: ide-first-claude-code-with-deterministic-hooks.md
  rel: same-problem
- file: skill-frontmatter-validation-rules.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
tags:
- deterministic-enforcement
- doc-governance
- drift-detection
- audit-script
---

# Deterministic Documentation-Audit Battery (C1-C16)

## Why It Matters

Documentation drift is the default state of any agentic workspace: indexes forget skills, links die, budgets creep, user data leaks into exportable folders — and asking an LLM "are the docs consistent?" burns tokens on a question a script answers exactly, for free, every time. CareerBuddy's answer is to make every doc-consistency rule that CAN be a script BE a script: one read-only Python file, 16 named checks, exit 0 or a list of failures each carrying its own fix instruction. The LLM's judgment is reserved for what scripts genuinely cannot see. For the engine, this is the strongest single piece of evidence for "deterministic enforcement as first-class citizen."

## What It Is

`audit_docs.py` — a single ~580-line stdlib-only Python script (no YAML dependency; deliberate line/regex parsing) inside the `ops-doc-sync` skill. Read-only, never modifies the tree. Exit codes: 0 = clean (warnings allowed), 1 = any error, 2 = usage. Each check is a pure function over the repo root, registered in a flat list; each finding prints `[FAIL]`/`[warn]` with a stable check ID.

## How It Works

The 16 checks, grouped by the drift class they catch:

**Index/registry completeness (bidirectional):**
- **C1** — every root `*.md` is classified in the governance-files registry
- **C5** — every skill dir is in the skills index AND every index entry exists on disk; skill frontmatter `name` matches its directory
- **C8** — every indexed skill appears in the `docs/workflows.md` user-manual cookbook (helper-* exempt)
- **C13** — every artifact-matrix row names an existing producing skill and a QA gate; matrix ↔ input-contracts routing table cross-reference complete in both directions

**Referential integrity:**
- **C2** — relative markdown links in critical-path docs resolve to real files
- **C3** — entry-point docs (copilot-instructions, AGENTS.md, ARCHITECTURE.md) all reference the vision-layer anchors (PRD/ARCHITECTURE/PROGRESS) — the load-order routing chain is intact

**Structural convention conformance:**
- **C4** — key folders each carry a HUMANS.md + AGENTS.md pair
- **C11** — repo root carries only whitelisted files; byproducts belong under `ops/` with a lifecycle
- **C14** — every SKILL.md declares distribution-scope (warn if absent); exportable skills carry README, CHANGELOG, capability-contract.yaml, a version, and SOURCES.md when the body cites findings
- **C15** — system-contract.yaml integrity: one wiring row per numbered canon doc, controlled-vocabulary capability IDs only, tier + invariant on every row
- **C16** — every skill package carries `evals/trigger-eval.md` with both should-trigger and should-not-trigger sections

**Data-boundary hygiene (privacy/separability):**
- **C6** — no user identifier (derived from `users/` folder names, incl. display-name variants) appears anywhere in the export set; full-id match = error, bare name token = warn
- **C9** — root PROGRESS/HISTORY are system-only: user display names banned; user ids allowed only inside `users/<id>/` path pointers

**Token-economy budgets:**
- **C7** — (warn) count-like phrases (`\d{2,} words|lines|files`) in PROGRESS.md — volatile metrics rot
- **C12** — PROGRESS.md line budget: warn > 150 (soft cap), fail > 250 (hard cap); the failure message says "run route-then-compact," never "raise the cap"

**Derived-content freshness:**
- **C10** — sha256 hashes in `onboarding/wiring-manifest.json` match the live wiring files; any new path-scoped rule missing from the manifest also fails (see the companion manifest-hash finding)

Design properties that make the battery durable: stable check IDs referenced by skills and commit messages; error/warn severity split (warnings inform, only errors gate); every failure message embeds its remediation ("run ops-session-handoff," "run a meta-harness-author refresh"); the wrapping SKILL.md mandates "audit before edit" (run the script first, never propose fixes from memory) and "re-run must exit 0" after applying fixes.

## How It Could Fail

- Checks encode structure assumptions (table formats, heading names) in regex; a doc reformat silently breaks parsing — the script guards this with "parsed to zero rows" meta-errors, a pattern worth copying.
- A green exit 0 proves structural consistency only, not content truth — CareerBuddy pairs it with an explicit LLM judgment sweep for that reason (see the two-layer finding).
- Battery growth is monotonic; without a retirement discipline, dead checks accumulate maintenance cost.
