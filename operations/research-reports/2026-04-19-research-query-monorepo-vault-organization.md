---
type: "research-query-report"
topic: "Monorepo vs multi-repo strategies and Obsidian vault organization for multi-system agentic workspaces"
dimensions: ["Orchestration", "Context Engineering", "Governance"]
persist_findings: false
date: "2026-04-19"
---

# Research Query Report — Monorepo and Vault Organization for Agentic Workspaces

## Question

How should a multi-system AI agent workspace (MetaSystem) be organized for version control and knowledge management? Specifically: monorepo vs multi-repo, git-based access control for selective sharing, Obsidian vault nesting vs single vault, and what production teams actually do.

## Existing KB Coverage

The KB had relevant findings on monorepo context distribution (n8n, Archon, LangGraph strategies), three-layer folder-as-workspace architecture, and multi-client context isolation. No findings directly adjudicated monorepo vs multi-repo as a first-class decision for agentic workspaces — the KB treated repo structure as an assumed input. No findings on Obsidian vault organization.

## Research Findings

### Key Insights

#### 1. Git Has No Path-Level Access Control
- **What:** Git fundamentally cannot restrict access to subdirectories within a repo. CODEOWNERS provides review workflow, not access control. Fine-grained PATs and GitHub Apps operate at repo level only.
- **Evidence:** Documented across GitHub docs, Nx framework docs, multiple production team reports
- **Novelty:** Novel — KB had no finding on this fundamental constraint
- **Sources:** [4][5][13][20][22]

#### 2. Monorepo + Subtree Publishing Is the Emerging Hybrid Pattern
- **What:** Production teams use a monorepo for unified agent context + separate repos (via git subtree or independent repos) for selective sharing. Not monorepo OR polyrepo — both.
- **Evidence:** Spectro Cloud 2026 analysis, multiple practitioner reports, LangGraph/CrewAI/n8n patterns
- **Novelty:** Extends existing KB findings on monorepo context distribution
- **Sources:** [1][23][31][40]

#### 3. Context Fragmentation Across Repos Degrades Agent Reasoning
- **What:** When agents operate across separate repos, they lose coherent architectural context and must reinfer dependencies. Polyrepo failure mode: agents make locally optimal but globally suboptimal decisions.
- **Evidence:** Production team reports, Spectro Cloud analysis
- **Novelty:** Extends `l-d-hypothesis-information-loss-across-agent-bound`
- **Sources:** [1][23][40]

#### 4. Nested Obsidian Vaults Are Unsupported and Risk Data Loss
- **What:** Obsidian developers strongly discourage nested vaults. Cross-vault links silently create duplicate files. Sync breaks with multiple .obsidian directories. No official documentation supports nesting.
- **Evidence:** Obsidian forum (official), 9-principle risk guide from experienced users
- **Novelty:** Novel — KB had no Obsidian-specific findings
- **Sources:** [1][2][4][39]

#### 5. Single Vault + Workspaces + Dataview Is the Production Pattern
- **What:** Power users (including Steph Ango) use single vaults with Workspaces plugin for context switching, frontmatter properties for metadata, and Dataview/Bases for filtered views. Scales to thousands of notes.
- **Evidence:** Multiple documented practitioners, Steph Ango's public vault architecture
- **Novelty:** Novel — no Obsidian organization findings in KB
- **Sources:** [7][14][18][21][31]

#### 6. AGENTS.md as Steering Document (Emerging Pattern)
- **What:** Beyond CLAUDE.md, teams create AGENTS.md files with explicit examples of tasks agents should/shouldn't handle. Gold-standard code examples and example prompts. More effective than abstract scope descriptions.
- **Evidence:** Datadog frontend team, Stack Overflow blog
- **Novelty:** Extends existing three-layer context architecture finding
- **Sources:** [31][48]

#### 7. Authorization Gap in Multi-User Agent Workspaces
- **What:** Agents operating with one user's permissions can expose data to recipients who shouldn't see it. The gap is between retrieval authorization (passes) and output authorization (not checked).
- **Evidence:** Okta security research, 2025 finding
- **Novelty:** Novel — no finding on authorization gaps in agent workspaces
- **Sources:** [26]

### Synthesis

The research strongly validates the hybrid approach: monorepo for daily work + subtree publishing for selective sharing. Git's lack of path-level access control makes this the only viable architecture when different people need access to different subsets. The Obsidian research is equally clear: single vault, never nest, use Workspaces + Dataview for scoped views.

Both decisions were implemented in this session (DD-84, DD-85).

### Gaps and Limitations

- No longitudinal data on git subtree maintenance burden at scale
- No research on Obsidian vault performance with 1000+ notes across 5+ systems
- Authorization gap finding is security-focused, not tested against knowledge management vaults
- No findings comparing git subtree vs git submodule for knowledge repos (vs code repos)

## All Sources Cited

1. https://www.spectrocloud.com/blog/will-ai-turn-2026-into-the-year-of-the-monorepo
2. https://dev.to/ujja/a-week-with-claude-code-lessons-surprises-and-smarter-workflows-23ip
4. https://git-scm.com/docs/git-sparse-checkout
5. https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
7. https://github.com/RayFernando1337/llm-cursor-rules/blob/main/generate-claude.md
9. https://github.com/webup/langgraph-up-monorepo
13. https://dev.to/davidarmendariz/git-submodules-vs-monorepos-14h8
14. https://www.youtube.com/watch?v=6UZemN4EVA0
15. https://www.datacamp.com/tutorial/git-subtree
16. https://forum.cursor.com/t/mono-repo-and-cursor-rules/140572
18. https://forum.obsidian.md/t/for-those-with-huge-vaults-anything-you-d-do-differently-or-wish-you-d-known-before-starting/99754
20. https://github.com/nrwl/nx/issues/13903
21. https://stephango.com/vault
22. https://github.com/orgs/community/discussions/153727
23. https://dev.to/subprime2010/how-to-use-claude-code-with-multiple-repositories-without-losing-context-4c77
25. https://docs.langchain.com/langsmith/monorepo-support
26. https://www.okta.com/blog/ai/ai-agent-authorization-gap/
31. https://dev.to/datadog-frontend-dev/steering-ai-agents-in-monorepos-with-agentsmd-13g0
33. https://nx.dev/docs/concepts/decisions/why-monorepos
37. https://www.anthropic.com/engineering/built-multi-agent-research-system
39. https://obsidian.md/help/manage-vaults
40. https://tianpan.co/blog/2026-04-17-coding-agents-monorepo-context-window
47. https://www.augmentcode.com/guides/git-worktrees-parallel-ai-agent-execution
48. https://stackoverflow.blog/2026/03/26/coding-guidelines-for-ai-agents-and-people-too/

## Recommended Next Steps

- Several sources (1, 23, 31, 40, 48) are strong candidates for full `/research-loop` extraction — they contain multiple patterns beyond what this report covers
- The authorization gap finding (source 26) warrants a dedicated research pass if MetaSystem ever moves to multi-user agent execution
- The AGENTS.md pattern (sources 31, 48) could inform an extension to MetaSystem's CLAUDE.md hierarchy
