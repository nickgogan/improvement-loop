---
name: "Personal Knowledge Hoard as Agent Recombination Substrate"
summary: "A distributed personal corpus of blog posts, small GitHub repos, TIL notes, single-page tools, and local code snippets becomes the raw material an AI agent recombines into new artifacts. The hoard is cheap to maintain (everything is small, hand-authored once) and expensive to replace (your idioms, your frameworks, your worked examples). Plain English: your shelf of small solved problems is substrate for AI. If you keep a few hundred small, worked examples around, the AI has your priors on tap and stops producing generic answers."
implementation_notes: "For MetaSystem: the IL's research findings + watched-libraries + authorities already function as an IL-scoped hoard for agents operating on the KB. Personal hoard is Nick-scoped; IL hoard is IL-scoped. Pattern generalizes across scopes."
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented at scale — 1,000+ repos)"
adoption_status: "Partially Adopted"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "simon-willison-hoard-things.md"
related_findings:
  - file: context-infrastructure-seven-level-maturity-model.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A distributed personal corpus optimized for agent recombination rather than direct human reference. Four properties:

1. **Small units, narrowly scoped.** Each artifact solves one problem — a 40-line HTML tool, a 200-word TIL post, a 50-line proof-of-concept repo. Not a monolithic knowledge-base; a library of idioms.
2. **Multiple surfaces.** Blog for prose, TIL for short discoveries, GitHub for runnable code, tools.simonwillison.net for HTML/JS apps, local notes for patterns. Different content types live in the surface that fits their discovery/access cost.
3. **Agent-reachable.** Everything is addressable via URL (blog posts, GitHub repos, hosted tools) or local path (notes). Agents can fetch by URL, clone repos, grep local directories.
4. **Recombination-first organization.** Not sorted by project or chronology; sorted for lookup-and-combine — "I have an OCR example and a PDF-rendering example, the agent can splice them into a PDF-to-searchable-text tool."

The hoard functions as personalized in-context substrate — agents fetching from it get your idioms and your solved-problem priors rather than a generic model's guess.

## Why It Matters

Foundation-model output quality depends heavily on context. Good prompts with specific examples produce better output than generic prompts. A personal hoard industrializes "specific examples" — instead of copy-pasting snippets into each prompt, the agent fetches the relevant examples itself.

For MetaSystem specifically:
- **IL's research-findings directory is already a mid-scale hoard.** 500+ markdown findings, addressable by filename, readable by agents. The hoard pattern formalizes what the IL has been doing intuitively.
- **Personal knowledge management (Nick's Obsidian vault) maps directly.** The vault is already Nick-scoped; making it agent-reachable is a small extension.
- **Hoard substrate for `/research-query`, `/assess-*` skills.** Skills that need examples should preferentially source from hoarded content before generating new examples.
- **Pattern generalizes across scopes.** Personal hoard (Nick), system-scoped hoard (IL, MetaSystem), organizational hoard (a company's collection). Same mechanics, different audiences.

Also connects to the "durable verticals" thesis ([[five-durable-verticals-ai-cannot-replace]]): context is one of the five things AI can't produce for itself. A personal hoard is a concrete instance of personal context ownership.

## Why People Are Using It

Observed in [Simon Willison's Agentic Engineering Patterns, Hoard things chapter](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/) — see [[simon-willison-hoard-things]] for the source entry. Simon's own scale: 1,000+ public GitHub repositories plus a dedicated TIL blog, blog posts on techniques, hosted HTML tools at tools.simonwillison.net, and a research repo (simonw/research) for complex examples. Concrete recombination example: combining two prior experiments (Tesseract.js OCR library + PDF.js rendering) into a functional PDF-to-searchable-text tool by referencing both in a single prompt.

The hoard's compounding property: each artifact's marginal cost of addition is low (a single afternoon of work plus a blog/repo push), and each marginal addition increases the recombinatorial surface. Unlike a curated documentation site that requires ongoing structural maintenance, a hoard ages gracefully — old artifacts stay useful as recombination material even when they stop being top-of-mind.

## Potential Alternatives

- **Curated documentation site.** Higher quality, higher maintenance, narrower topic coverage. Better for public-facing content; worse for personal recombination substrate.
- **Private wiki (Notion, Confluence, local).** Similar coverage properties; less agent-reachable unless the agent has API access.
- **Code-only repositories.** GitHub-centric hoard without the prose surfaces. Loses the "why I did it this way" context that blog posts and TIL entries provide.
- **RAG over personal corpus.** Embed the hoard and retrieve by semantic similarity. More sophisticated, less transparent — agent doesn't know which artifact it used.
- **In-context-only prompt libraries.** Copy-paste examples into every prompt. Doesn't scale; doesn't recombine automatically.

## Potential Improvements

- **Agent-readable index.** A `llms.txt` or `hoard-index.json` at each surface listing contents with 1-line descriptions, so agents can scan the hoard structure without fetching every artifact.
- **Cross-surface linkage.** Blog posts link to their GitHub repos link to their hosted tools. Agents following one link reach the full context.
- **Hoard-level CLAUDE.md.** A top-level context file describing the hoard's scope, conventions, and preferred patterns, so agents consuming the hoard inherit the author's preferences.
- **Semantic deduplication.** As the hoard grows, near-duplicate artifacts accumulate. Agent-powered deduplication + cross-link insertion would keep the hoard's recombination surface clean.
- **Hoard-as-skill.** Individual hoarded patterns can be promoted to skills (SKILL.md files) when they stabilize. Bidirectional: skills that prove unreusable can be demoted to hoarded examples.

## Potential Failure Modes

- **Sprawl.** Past a certain size the hoard becomes un-indexable even for agents; retrieval quality degrades. Mitigation: agent-readable index + pruning old content that no longer recombines.
- **Staleness.** Old tools use old APIs; agents recombine around obsolete patterns. Mitigation: date-stamp artifacts; agents weight recent over old; occasional prune-or-update passes.
- **Discovery friction.** If the agent doesn't know about a particular surface of the hoard, it won't fetch from there. Mitigation: central README listing all surfaces; tagged indexes so agents can filter by topic.
- **Single-author fragility.** Hoard reflects one person's priors; useful for that person, less useful for others. Mitigation: treat hoard as personal tooling, not team artifact; teams build shared hoards separately.
- **Privacy/IP.** Personal hoards often contain client work, experimental ideas, half-baked thoughts. Publishing all of it isn't appropriate. Mitigation: clear public/private boundaries; agents with access to both; careful surface naming.
