---
name: 'Wiring Canon — Abstract-Then-Adapt Doc Structure with a Two-Source Change Model'
summary: 'Harness wiring is documented as a numbered set of platform-agnostic canon docs, each with three fixed sections: Canon (the requirement any platform must satisfy), Adapter-delegated (what each platform decides), and Harness-specific examples (illustrations, never requirements). Change enters from exactly two sides — the system changed (gated canon regeneration, never hand-edits) or a platform changed (dated survey → diff → gated plan) — and adapter-side findings that imply the canon is wrong are flagged and routed to the canon side, never patched locally.'
implementation_notes: 'This is the documentation architecture for the engine''s portable governance kernel: write each kernel concern (entry file, registry, memory, skills, session spine) once as harness-neutral canon with an explicit adapter-delegated seam, instead of writing Claude-Code-shaped docs and porting by rewrite. The three-section format is directly reusable; the two-source change model maps onto the engine''s existing gated-regeneration habits (FOUNDATIONS.md, /translate-governance drift detection). Also note the router-guard idea: the canon folder tells live-session agents "this is not your entry point" to prevent install docs leaking into runtime context.'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: synthesized
consumed_by:
- building-agentic-systems.md
tags:
- wiring-canon
- abstract-then-adapt
- doc-architecture
- change-model
---
# Wiring Canon — Abstract-Then-Adapt Doc Structure with a Two-Source Change Model

## What It Is

A documentation architecture for the harness-wiring layer of an agentic system: one
numbered doc per wiring concern (always-on instructions, path-scoped rules, governance
registry, memory scopes, skill registry, cold-start chain, invocation context,
operational quirks), each written platform-agnostically with three fixed sections —
**Canon** (the requirement), **Adapter-delegated** (per-platform decisions, including
the named fallback when a platform lacks the mechanism), and **Harness-specific
examples** (labeled illustrations from the current install, never requirements). The
folder opens with an agent router stating who may use it and when.

## Why It Matters

Plain English: most agentic systems document their wiring in the vocabulary of the
harness they happen to run on — so moving platforms means rewriting the docs and
rediscovering which parts were essential versus incidental. Writing the requirement once
(canon) and quarantining the platform detail into labeled sections makes the essential/
incidental split explicit *at authoring time*, which is what makes the system contract's
wiring rows derivable and the whole system portable. The disciplined change model keeps
the abstraction true as both the system and the platforms drift.

## How It Works

- **Three-section format per doc:** *Canon* states what must exist on any platform
  (e.g. "both rule-sets exist and auto-apply on their trees"); *Adapter-delegated*
  names what each platform decides (mechanism, paths, whether native enforcement can
  replace prose) plus the fallback when the capability is absent; *Harness-specific
  examples* carry the current platform's mechanics, explicitly marked
  (`harness-specific: vscode-copilot`) so a future adapter re-derives instead of
  copying.
- **Router guard:** the folder's AGENTS.md tells any agent operating in the live
  workspace "this folder is not your entry point" and routes back to the live
  cold-start chain — install-time docs are kept out of runtime context. Legitimate
  uses are enumerated: generalizing, adapting, receiving, auditing.
- **Two-source change model:** (1) canon-side — the system changed → a gated
  regeneration by the owning meta-skill ("diff live wiring vs. these docs; propose
  amendments, never silent rewrites"); staged platform adapters may then need
  restaging. (2) adapter-side — a platform changed → a dated survey → diff → gated
  plan. If an adapter-side finding implies the canon itself is wrong, it is flagged
  and routed to source 1 — adapt mode never edits the canon.
- **Gated ownership:** the canon folder is governance-tier (registry-classified);
  edits are deliberate and human-approved, normally via the owning skill's gated flow.
  Controlled vocabularies referenced by the canon are gated package changes on their
  owning skills, never casual edits.
- **Derivation chain:** canon docs → system contract wiring rows (one row per doc) →
  hash manifest over the wired files — three artifacts that must agree, with audits
  checking each seam.

## How It Could Fail

The abstraction is only worth its maintenance when a second platform is real — for a
single-harness system, canon + adapter is a layer without a second consumer (the
abstractions-earn-their-keep test applies). Examples drift into requirements when the
harness-specific label is skipped. If regeneration is gated but never run, the canon
quietly diverges from live wiring — the hash manifest exists precisely to make that
divergence loud.
