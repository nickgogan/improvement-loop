---
name: Skill Smells — Symptom-to-Cause Triage Table Layered Before the Full Audit
summary: 'A one-page, scannable "smells" table maps observable skill symptoms to likely root causes and the deep-dive reference that diagnoses each — a 30-second pre-check layered in front of the scored
  audit rubric. Smells are grouped into five categories (triggering, sizing/attention, authoring craft, evaluation/governance, safety) with a quantified verdict rule: 1–2 smells in one category → patch
  locally; 3+ smells across categories → do not patch in place, run the full audit; any safety-category smell → block, never ship-and-fix-later. Key insight: smells are behavioral and editorial, so they
  are invisible to deterministic structural validators.'
implementation_notes: 'Cheapest direct adoption from the CareerBuddy reference layer: a smells pre-pass in front of /assess-skill would let the engine triage its own growing skill roster (and audit-artifacts
  fan-outs) without paying the full composed-audit cost per artifact. The table shape — symptom you can notice without instrumentation → cause → pointer into the deep reference — also generalizes to other
  engine assessors (agents, prompts). Overlap with the imported /meta-skill-author toolchain (which ships this as skill-smells.md) vs /assess-skill is a flagged open question for the restructure program''s
  Phase 2 audit.'
category: Evaluation
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: synthesized
consumed_by:
- eval-driven-improvement-loops.md
- templates/skill-smells-triage-table.md
tags:
- skill-authoring
- anti-patterns
- triage
- audit
---

# Skill Smells — Symptom-to-Cause Triage Table Layered Before the Full Audit

## Why It Matters

Full skill audits (scored rubrics, eval suites) are expensive, so in practice they get skipped — and broken skills ship. A smells table gives you a 30-second alternative that catches most problems: you skim symptom rows against the skill in front of you, and each "yes, that's happening" points straight at a cause and a fix reference. It doesn't replace the audit; it decides *whether* the audit is needed and *where* to look — the same cheap-check-before-expensive-check layering that makes linters useful even when you have a test suite.

## What It Is

CareerBuddy's `skill-smells.md`: a triage doc explicitly positioned as the first of three audit layers (smells table → anti-pattern catalog AP-01..AP-14 → scored audit rubric). Each row is *what you notice* → *likely cause* → *go to* (the reference section that diagnoses it in depth). Five smell categories:

- **A. Triggering** — body edited but description untouched ("description drift"); description reads like a body summary instead of when-to-use; two catalog skills share most trigger keywords; no should-trigger/should-not-trigger eval queries ever written
- **B. Sizing/attention** — `wc -l SKILL.md` over 500; long pasted documentation blocks (copies instead of pointers); rules that apply to almost no session in the always-loaded body; missing L0 abstract; LLM-generated body never trimmed
- **C. Authoring craft** — "think step by step"/few-shot scaffolding (degrades frontier reasoning models); ALL-CAPS MUST/NEVER with no WHY; aspiration lists with few negative constraints; deterministic logic (parsing, math) written as prose instead of a script; a one-shot task the base model already does written as a skill
- **D. Evaluation/governance** — author graded their own skill in the same context; "output is good" acceptance criteria; high rubric score but wrong runtime behavior; capability evals saturated at ~100% without graduating to regression
- **E. Safety/side-effects** — commit/deploy/send/delete with no autonomy gating; no blast-radius × reversibility classification; retrieved external data treated as trusted instructions; never security-audited before publishing

## How It Works

The quantified verdict rule does the routing: 0 smells → run the deterministic validator and proceed; 1–2 smells in one category → patch that smell, re-check the category; 3+ smells across categories → do not patch in place, run the full scored audit before shipping; any Category E smell → block until resolved, "safety smells are never ship-and-fix-later." The doc's framing insight: a skill can pass Level-1 structural validation (`validate.sh`) "and still reek" — most smells are behavioral/editorial and invisible to any deterministic validator, which is exactly why a human/LLM-scannable layer must exist between the linter and the rubric.

## How It Could Fail

The table only stays cheap if it stays one page; growing it toward completeness turns it back into the audit it was meant to precede. Every smell row must point into a maintained deep reference — orphaned rows ("go to" targets that moved) silently kill trust in the whole table. And the 3+/cross-category threshold is a heuristic calibrated on one production system; other rosters may need different cut-offs.

## Extraction Note — 2026-07-19
Extracted as **template**: [[skill-smells-triage-table]] in `extracts/templates/`
