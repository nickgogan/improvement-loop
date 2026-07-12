---
name: "Claude Code's Entire Source Code Was Just Leaked via npm Source Maps — DEV Community"
source_type: "Blog"
status: "Done"
date_processed: "2026-04-23"
date_published: "2026-03-31"
key_takeaways: "Gabriel Anhaia's DEV Community writeup on the March 31 2026 Claude Code source leak. Corroborates claudefa.st's architectural findings; adds that Anthropic confirmed the leak and the fix was to add `*.map` to `.npmignore`. Frames the leak's significance as proving that the bash security + tool-registry + permission-system primitives 'aren't Anthropic-specific — they're structural requirements of any agent that has to work for real' (also separately ported to Python and Rust after the leak). Useful independent second source for the bash-security architecture details."
relevance: "Medium"
added_by: "Claude"
tags: ["claude-code", "security", "source-leak", "secondary-corroboration"]
url: "https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo"
authority: []
findings:
  - "shell-injection-vector-taxonomy-agent-bash-security.md"
date_added: "2026-04-23"
---
