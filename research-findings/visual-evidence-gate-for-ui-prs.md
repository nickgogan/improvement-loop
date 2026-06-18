---
name: Visual Evidence Gate for UI PRs
summary: Automated PR review skill requires screenshots or screen recordings for any user-visible change. No exemptions for headless environments — suggests computer-use alternatives. Verdict is REJECT
  without visual evidence, even if no other blocking issues exist. Tests and code-path descriptions cannot substitute for visual proof.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: holdout-validation-pattern-blind-regression.md
  rel: same-problem
- file: bmad-deterministic-skill-validator.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-24'
pipeline_status: raw
---

# Visual Evidence Gate for UI PRs

## Pattern

An automated PR review policy that requires visual evidence for user-visible changes:

**Rule:**
- Any PR changing anything a user can perceive (UI components, layout, styling, copy, terminal visuals) requires attached screenshots, GIFs, or videos demonstrating the change end-to-end.

**What counts as evidence:**
- Markdown image/video embeds
- GitHub user-attachment links
- Loom links or similar hosted media

**What does NOT count:**
- Unit tests, integration tests, `git diff --check`
- Code-path descriptions or textual explanations
- An empty "Screenshots / Videos" section from the PR template

**No environment exemptions:**
- "Can't take screenshots because headless runner" is NOT an exemption
- The skill suggests computer-use alternatives (e.g., Oz with computer use enabled)
- Verdict is always `REJECT` / `Request changes` without visual evidence

**Scope exclusions:**
- Pure refactors, internal tools, build scripts, backend-only code, tests, documentation → no evidence required

## Why It Matters

Prevents UI regressions that pass all tests but look wrong to humans. Automated agents can write code that compiles and passes type checks but produces visual artifacts the user would reject. By making visual evidence a hard gate, the review process catches these before merge.

## How It Could Fail

- Slows down development velocity (every UI change needs a screenshot)
- False positives (changes classified as "user-visible" that aren't practically visible)
- Computer-use capture quality may not show subtle visual issues
- Screenshot-based review can't catch interaction/animation bugs

## Evidence

Warp (warpdotdev/warp) — `review-pr-local` skill with detailed visual evidence requirements. Verdict logic: `if (ui_change && !visual_evidence) → verdict = REJECT`. Production-tested in Warp's automated PR review workflow.
