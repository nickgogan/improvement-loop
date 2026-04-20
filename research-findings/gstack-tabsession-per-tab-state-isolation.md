---
name: TabSession — Per-Tab State Isolation
summary: Per-tab state isolation architecture giving each browser tab its own ref map, snapshot baseline, and frame context to prevent cross-tab collision.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gstack-v01590-v015160-changelog.md
related_findings:
- file: cloud-plan-parallel-multitasking-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---
# TabSession — Per-Tab State Isolation

## What It Is
A per-tab state isolation architecture where each browser tab gets its own ref map, snapshot baseline, and frame context. Previously, this state was global on the BrowserManager, causing cross-tab collision when multiple tabs were active simultaneously. Handler signatures now explicitly accept either TabSession (tab-scoped) or BrowserManager (global), making the scope boundary visible in the API surface. This is the foundation for parallel multi-tab operations.

## Why It Matters
Browser automation agents increasingly need to work across multiple tabs — comparing pages, filling forms in one tab based on data from another, or running parallel scraping operations. Without per-tab state isolation, snapshot references from one tab can collide with another, producing incorrect comparisons or stale data.

## Why People Are Using It
gstack refactored from global BrowserManager state to per-tab TabSession objects to support multi-tab workflows. The explicit handler signature distinction (TabSession vs BrowserManager) prevents accidental scope mixing at the API level rather than relying on runtime checks.

## Potential Improvements
Could extend the pattern to per-tab resource budgets (memory, network) for isolation beyond state. Tab groups could share state selectively for coordinated multi-tab workflows. The pattern could generalize to any multi-context agent operation (not just browser tabs).

## Potential Failure Modes
Per-tab isolation increases memory footprint linearly with tab count. Cross-tab coordination (when intentionally needed) becomes harder with strict isolation. Tab lifecycle management (cleanup on close, orphan detection) adds complexity.
