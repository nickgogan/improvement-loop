---
name: "A harness for every task: dynamic workflows in Claude Code"
source_type: "Blog Post"
status: "Done"
key_takeaways: |-
  Anthropic first-party post (Thariq Shihipar & Sid Bidasaria, MTS) on dynamic
  workflows: Claude Code writes its own multi-agent harness at runtime as a
  JavaScript file (agent/parallel/pipeline primitives), custom-built per task.
  Names six composable harness patterns (classify-and-act, fan-out-and-synthesize,
  adversarial verification, generate-and-filter, tournament, loop-until-done),
  the three failure modes they cure (agentic laziness, self-preferential bias,
  goal drift), pairwise-tournament-beats-absolute-scoring judging, and
  operational guidance (token budgets in the prompt, worktree isolation choice,
  per-agent model routing, resume, saving harnesses as reusable skills).
  Primary source behind the l5rae4LMKBc digest video; fetched to upgrade
  frontier-model-as-harness-designer to first-party evidence.
relevance: "High"
added_by: "Nick"
tags:
  - "orchestration"
  - "multi-agent"
  - "claude-code"
url: "https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code"
authority:
  - "anthropic.md"
findings:
  - "frontier-model-as-harness-designer.md"
  - "harness-composition-six-pattern-taxonomy.md"
  - "pairwise-tournament-judging-over-absolute-scoring.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-06-02"
---

# A harness for every task: dynamic workflows in Claude Code

Anthropic engineering blog, 2026-06-02, by Thariq Shihipar and Sid Bidasaria.
Fetched as the primary source behind the Prompt Engineering channel digest
(`claude-can-now-build-its-own-harness.md`). Session-136 extraction notes:

- Six named patterns with when-to-use guidance; the blog's own pattern list uses
  "adversarial verification" where the digest video said "worker-critic".
- Case study: Bun rewritten from Zig to Rust via workflows (subagent per fix in
  isolated worktrees, adversarial review, merge).
- Operational: dynamic workflows cost more tokens — "parallelism and
  specialization have to earn their coordination cost"; explicit token budgets
  in the prompt; `ultracode` trigger word; save-as-skill distribution
  (`~/.claude/workflows`, referenced from SKILL.md).
- Static (Agent SDK / `claude -p`) vs dynamic distinction: static must stay
  generic across edge cases; dynamic is tailor-made per task at runtime.
