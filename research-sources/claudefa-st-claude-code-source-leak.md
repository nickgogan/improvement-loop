---
name: "Claude Code Source Leak: Everything Found (2026) — claudefa.st"
source_type: "Blog"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Most comprehensive public writeup of the March 31 2026 Claude Code source leak (59.8 MB .map file in npm @anthropic-ai/claude-code@2.1.88; 1,900 files / 512,000+ lines exposed). Key architectural details surfaced: (a) Claude Code runs on Bun not Node; (b) React+Ink terminal UI; (c) ~40 plugin-style tools; (d) bashSecurity.ts runs 23 numbered security checks per bash command, including 18 blocked Zsh builtins, defenses against Zsh equals expansion (=curl bypass), unicode zero-width-space injection, IFS null-byte injection, and a malformed-token bypass found during HackerOne review; (e) 44 hidden feature flags; (f) always-on KAIROS background agent; (g) employee stealth-mode for OSS contributions."
relevance: "High"
added_by: "Claude"
tags: ["claude-code", "security", "source-leak", "bash-security", "canonical-writeup"]
url: "https://claudefa.st/blog/guide/mechanics/claude-code-source-leak"
authority: []
findings:
  - "shell-injection-vector-taxonomy-agent-bash-security.md"
date_added: "2026-04-23"
---
