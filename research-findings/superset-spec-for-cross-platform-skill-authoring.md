---
name: 'Superset Spec — Author Skills Against the Full Field Superset, Then Port Down'
summary: 'Maintain one authoritative reference document that catalogs the complete superset of SKILL.md fields and body rules across all target platforms, tagging every field as portable (open-standard), harness-specific (e.g. Claude Code extension), or proposed (convention only). Authors write against the superset and consciously port down: a skill built only from portable-tagged elements is guaranteed to run anywhere; any harness-specific field use makes non-portability explicit and forces a compatibility declaration. CareerBuddy operationalized this as the spine of its meta-skill-author toolchain.'
implementation_notes: 'Directly relevant to the engine''s portable-governance-kernel vision: the same author-to-superset/port-down move applies to governance artifacts, not just skills. The engine''s /design-skill draws on IL guide substrate but has no per-field portability tagging; the imported /meta-skill-author carries this superset-spec as a reference doc — the overlap between the two toolchains is a flagged open question for the restructure program''s Phase 2 audit. A machine-checkable field-constraints table (caps, char classes, failure modes per field) is the cheapest first adoption: it slots into /assess-skill as a deterministic pre-pass.'
category: Agent Design
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- skill-authoring
- portability
- cross-platform
- open-standard
---

# Superset Spec — Author Skills Against the Full Field Superset, Then Port Down

## Why It Matters

When you author skills for more than one AI harness, the failure mode is silent non-portability: a skill quietly uses a Claude-Code-only field (`when_to_use`, `context: fork`, `paths`) and simply stops working — or worse, silently degrades — on another platform. The superset-spec pattern makes portability a visible, per-field decision at authoring time instead of a surprise at deployment time. For the engine, which wants a portable governance kernel, this is the reference-artifact shape that makes "portable" an auditable property rather than an aspiration.

## What It Is

A single reference document (CareerBuddy's `superset-spec.md`, ~330 lines) that is the authoritative union of all SKILL.md fields and body-structure rules across five platforms (Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Perplexity). Every field carries exactly one of three tags:

- **portable** — defined by the Agent Skills open standard (agentskills.io); the six-field floor is `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`
- **harness-specific** — e.g. the ~13 Claude Code extension fields (`when_to_use`, `disable-model-invocation`, `user-invocable`, `context`/`agent`, `paths`, `hooks`, `model`, `effort`, `shell`, ...); using any of these obligates a `compatibility: claude-code` declaration
- **proposed** — surfaced by research but not yet in any shipping spec (e.g. `specializes`, `rollback_procedure`, `max_permission_scope`, `defaultMode`, per-action autonomy tiers); implementable as team conventions

## How It Works

- The doc pairs every field with its mechanical constraints (e.g. `name`: 1–64 chars, `[a-z0-9-]`, no reserved words `anthropic`/`claude`, no XML, must match directory name) and the *failure mode* when violated (e.g. description past the 1,536-char combined Claude Code cap truncates and strips trigger keywords before the model sees them).
- It resolves apparent spec contradictions explicitly — e.g. the open standard's 1,024-char `description` cap vs. Claude Code's 1,536-char `description`+`when_to_use` budget govern different fields; the derived authoring rule is "target ≤ 800 chars for description alone."
- A machine-checkable constraints table (field × hard cap × char class × portability × failure mode) sits at the end, feeding deterministic validation (`skills-ref validate`) before any LLM review.
- Body-structure rules are also tagged: the five-element body model, three-level progressive disclosure (L0 ~100-token abstract / L2 body ≤ 500 lines / L3 references), and pointers-over-copies are all portable; `$ARGUMENTS` substitution and `` !`cmd` `` dynamic injection are harness-specific.
- Design guideline that falls out: design for the most restricted target surface, and use `compatibility` to declare when a skill expects more.

## How It Could Fail

The superset is a maintained artifact: every platform spec change (new extension field, changed cap) must be folded in, or the tags rot and "portable" becomes false confidence. The doc also inherits the "vendor extensions become the de-facto standard" risk — if authors habitually reach for harness-specific fields, the portable floor is nominal. Mitigation in the source: proposed/extension fields are quarantined in their own sections, so the portable floor stays visually distinct.
