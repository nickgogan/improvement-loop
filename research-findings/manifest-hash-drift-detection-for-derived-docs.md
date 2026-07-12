---
name: 'Manifest-Hash Drift Detection for Derived Documentation'
summary: 'When one agent skill distills source files into derived documentation (canon, onboarding docs, summaries), the producer writes a manifest recording the sha256 of every surveyed source file. A cheap deterministic check later compares live hashes against the manifest: any mismatch means the derived docs may be stale, and the failure message names the exact regeneration skill to run. Staleness of LLM-derived content becomes script-detectable without any LLM re-read.'
implementation_notes: 'The engine has several derived surfaces this fits exactly: FOUNDATIONS.md is generated from foundational DDs (the pre-commit hook already enforces sync — a hash manifest is the generalization), /repo-analyzer analysis docs derive from cloned repos, schematics derive from upstream sources (/detect-drift does source-drift scanning and could adopt the hash-manifest mechanic instead of heavier comparison), and guides synthesize findings. Pattern-lift for Phase 2: each producer skill writes <output-dir>/manifest.json {generated, note, files: {path: sha256}} at generation time; a single audit check (or pre-commit hook) verifies hashes and names the producing skill in its failure message. Cost is ~10 lines per producer plus one shared check. Also catches the inverse drift: new source files matching the surveyed glob but absent from the manifest.'
category: Governance
evidence_strength: Medium (practitioner-documented, single production system, script-verifiable)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-doc-sync-audit-battery.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: deterministic-doc-audit-battery.md
  rel: extends
- file: docs-split-by-lifespan-not-topic.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
tags:
- drift-detection
- content-hashing
- derived-docs
- deterministic-enforcement
---

# Manifest-Hash Drift Detection for Derived Documentation

## Why It Matters

Any doc an LLM distills from other files starts rotting the moment a source file changes — and nothing announces it. The usual "fixes" are bad: re-run the expensive distillation on a schedule (wasteful), or have an LLM diff the docs against the sources (slow, token-heavy, unreliable). CareerBuddy's mechanic makes staleness of LLM-generated content a five-line deterministic check: hash the inputs at generation time, re-hash at audit time, mismatch = stale. It converts "is this derived doc still true?" — a judgment question — into "did its inputs change?" — a yes/no a script answers in milliseconds. Stale derived docs are worse than none: they steer agents confidently in outdated directions.

## What It Is

A producer/checker contract split across two skills:

- **Producer** (`meta-harness-author`): whenever it distills the live harness wiring into the `onboarding/` canon, it writes `onboarding/wiring-manifest.json` — `{generated: <date>, note: <what this is + what a mismatch means + the remedy>, files: {<repo-relative path>: <sha256 of file bytes>}}` covering every source file it surveyed.
- **Checker** (`ops-doc-sync` audit check C10): for each manifest entry, error if the file was removed ("canon may be stale") or its live sha256 differs ("run a meta-harness-author generalize refresh"). Additionally, any NEW file matching the surveyed class (path-scoped rule files) that is absent from the manifest also errors — catching under-coverage drift, not just modification drift.

## How It Works

Mechanics that make it durable:

1. **Hash the inputs, not the output.** The manifest records the sources the derivation consumed, so hand-edits to the derived docs stay legal; only source change signals staleness.
2. **Manifest as message.** The JSON embeds a human/agent-readable `note` explaining who writes it, who checks it, and what a mismatch means — self-describing infrastructure.
3. **Asymmetric ownership.** The producer owns writing the manifest (only it knows what it surveyed); the checker only compares. Neither regenerates anything — the failure message routes to the producing skill.
4. **Two failure directions.** Modified/removed sources (recorded but changed) AND unrecorded new members of the surveyed file class (present but never distilled).
5. **Composes into the battery.** It is one check ID (C10) inside the 16-check audit script — freshness of derived content sits alongside link integrity and index completeness as one more deterministic gate.

## How It Could Fail

- The mechanic detects that inputs changed, not that the derived doc is wrong — trivial source edits (typo fixes) trigger full regeneration prompts; there is no materiality threshold.
- If the producer forgets to rewrite the manifest after regenerating, the check fails forever on a fresh canon — the write must be part of the producer's definition of done.
- The new-file sweep only covers file classes the checker knows to glob for; sources outside that class can drift invisibly.
