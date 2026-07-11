---
name: "ast-grep — outline: cheap structural summaries for code agents"
source_type: "Article"
status: "Done"
key_takeaways: |-
  Announces `ast-grep outline`: on-demand compact structural summaries (functions/classes/
  imports/exports with line numbers) for code agents — single file, directory export surface,
  --match symbol focus, --items imports filtering. No index (works across parallel worktrees),
  local-only, rule-based extraction. Measured 35–55% token-cost reduction on large repos
  (VS Code/Django/OkHttp scale) at 100% baseline coverage in the authors' testing; minimal
  benefit on small repos. KB pattern candidate: structural-outline-before-read for agent
  navigation. Triage verdict was ENHANCE: adopt in /repo-analyzer (structural-inventory and
  import-map dimensions), optional outline pass in /audit-artifacts — gated on repo size and
  tool availability. URL 301-redirects to astgrep.com (canonical). Est. 3 novel findings.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - tools
  - context-engineering
  - code-navigation
  - token-economy
url: "https://ast-grep.github.io/blog/ast-grep-outline.html"
authority:
  - "ast-grep.md"
findings:
  - "structural-outline-before-read-agent-navigation.md"
  - "index-free-local-code-intelligence-parallel-worktrees.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #5 — the ENHANCE
half of the verdict is applied to `/repo-analyzer` separately).
