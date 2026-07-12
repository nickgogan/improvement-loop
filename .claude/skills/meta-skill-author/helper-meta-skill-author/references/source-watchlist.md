# Source Watchlist

> Reference doc for the `helper-meta-skill-author` internal helper.
> Path basis: bare package paths (`SKILL.md`, `references/`, `adapters/`,
> `SOURCES.md`) are relative to the **target `meta-skill-author` package root**
> — i.e. `../` from this helper. The helper resolves them one level up.
> Enumerates the sources Detect mode checks for changes, with refresh
> cadence and diff strategy per source. Portable across all five
> platforms (Claude Code, Cursor, GitHub Copilot, OpenAI Codex,
> Perplexity). No platform-specific features referenced.
> Every substantive claim cites a finding from the master inventory.

---

## 1. Watchlist Table

Sources are listed only if they are directly referenced in the
existing skill package (SKILL.md, references/, adapters/, SOURCES.md).
No sources have been invented; every row traces to a finding citation
or adapter document in the package.

For each row, the **Confirmed?** column indicates whether the source's
content is confirmed by findings (`Yes — [finding]`) or whether the
documentation state is unknown and must be verified against current
docs (`Unknown — verify`). This status comes directly from the
adapter documents in `adapters/`.

| # | Source | Type | URL or Path | Diff Strategy | Cadence | Last-Snapshot Field |
|---|--------|------|-------------|---------------|---------|---------------------|
| 1 | Research findings corpus | directory | `<corpus-root>/research-findings/` | File-hash + content-hash per file (§4.1 of change-manifest-format.md) | Every refresh run | `snapshot.corpus_hashes` |
| 2 | Anthropic Claude Code skills docs | platform_doc | https://docs.anthropic.com/en/docs/claude-code/skills | Section content hash per anchored section | Monthly | `snapshot.platform_docs["anthropic-claude-code-skills"]` |
| 3 | Anthropic equipping-agents blog post | platform_doc | https://docs.anthropic.com/en/docs/claude-code/skills (see finding `anthropic-equipping-agents-with-agent-skills.md`) | Full-page content hash (no stable anchors) | Monthly | `snapshot.platform_docs["anthropic-equipping-agents"]` |
| 4 | Anthropic Complete Guide to Building Skills PDF | platform_doc | see `/research-findings/anthropic-complete-guide-building-skills-pdf.md` for URL | Full-page or PDF content hash | Monthly | `snapshot.platform_docs["anthropic-complete-guide-pdf"]` |
| 5 | agentskills.io open standard | platform_doc | https://agentskills.io | Section content hash | Monthly | `snapshot.platform_docs["agentskills-io"]` |
| 6 | Cursor docs — context/rules | platform_doc | https://docs.cursor.com/context/rules | Section content hash per anchored section | Monthly | `snapshot.platform_docs["cursor-context-rules"]` |
| 7 | GitHub Copilot AGENTS.md / custom instructions docs | platform_doc | Unknown — verify against current Copilot docs | Section content hash once URL confirmed | Monthly | `snapshot.platform_docs["copilot-agents-docs"]` |
| 8 | OpenAI Codex / AGENTS.md docs | platform_doc | Unknown — verify against current Codex docs | Section content hash once URL confirmed | Monthly | `snapshot.platform_docs["codex-agents-docs"]` |
| 9 | Perplexity custom skills docs | platform_doc | Unknown — verify against current Perplexity docs | Section content hash once URL confirmed | Monthly | `snapshot.platform_docs["perplexity-skills-docs"]` |
| 10 | BMAD-METHOD GitHub repo | platform_doc | https://github.com/bmad-code-org/BMAD-METHOD | Commit hash on default branch | Monthly | `snapshot.platform_docs["bmad-method"]` |
| 11 | MemPalace GitHub repo | platform_doc | https://github.com/MemPalace/mempalace | Commit hash on default branch | Monthly | `snapshot.platform_docs["mempalace"]` |
| 12 | HyperAgents arXiv paper | platform_doc | https://arxiv.org/abs/26.03.19461 | Full-page hash (arXiv papers are versioned; compare version number) | Quarterly | `snapshot.platform_docs["hyperagents-arxiv"]` |
| 13 | ETH Zurich context-files paper | platform_doc | https://arxiv.org/abs/2602.11988 | Full-page hash (arXiv versioned) | Quarterly | `snapshot.platform_docs["eth-zurich-arxiv"]` |
| 14 | productcompass.pm intent engineering article | platform_doc | https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents | Full-page content hash | Quarterly | `snapshot.platform_docs["productcompass-intent-eng"]` |
| 15 | Nate B. Jones OB1 repo | platform_doc | https://github.com/NateBJones-Projects/OB1 | Commit hash on default branch | Quarterly | `snapshot.platform_docs["ob1-repo"]` |
| 16 | LangGraph repo | platform_doc | https://github.com/langchain-ai/langgraph | Commit hash on default branch (for CLAUDE.md / AGENTS.md files specifically) | Quarterly | `snapshot.platform_docs["langgraph-repo"]` |
| 17 | Anthropic Trustworthy Agents docs | platform_doc | see `/research-findings/anthropic-trustworthy-agents-in-practice.md` | Section content hash | Monthly | `snapshot.platform_docs["anthropic-trustworthy-agents"]` |
| 18 | Anthropic demystifying evals docs | platform_doc | see `/research-findings/anthropic-demystifying-evals-for-ai-agents.md` | Section content hash | Monthly | `snapshot.platform_docs["anthropic-demystifying-evals"]` |
| 19 | arXiv / academic — skill authoring and agent evals | search_query | Query: "agent skill authoring evaluation" site:arxiv.org | Results delta (new papers since last snapshot) | Monthly | `snapshot.academic["arxiv-skill-authoring"]` |
| 20 | User's research knowledge base | external | Placeholder — user-configurable path or URL | User-defined | User-defined | `snapshot.external["user-kb"]` |
| 21 | Glean Agents docs (Agent Builder, How agents work, Triggers, Memory, Execution limits, Agent library, Sharing) | platform_doc | https://docs.glean.com/agents/ | Section content hash per doc page | Monthly | `snapshot.platform_docs["glean-agents-docs"]` |

### Confirmed Status Notes

Sources 2–5 (Anthropic docs, agentskills.io): **Confirmed by findings** — extensively
cited across B1, B6, B9 buckets [skill-md-frontmatter-as-discovery-trigger-primitive]
[skills-as-open-portable-standard] [skill-as-directory-progressive-disclosure-three-levels].

Source 6 (Cursor): **Confirmed that `.cursorrules` path exists** — but the specific
docs URL is cited as "verify against Cursor docs" in `adapters/cursor.md`
[multi-ide-portability-via-installer-templates]. The URL above is the best-known
current location; verify before adding to snapshot.

Sources 7–9 (Copilot, Codex, Perplexity): **Unknown — verify against current docs.**
The adapter documents for these platforms (`adapters/copilot.md`, `adapters/codex.md`,
`adapters/perplexity.md`) explicitly label most capabilities as "Unknown — verify"
per the platform-matrix.md conventions [multi-ide-portability-via-installer-templates].
These watchlist rows exist as placeholders; a human must supply the confirmed URL
before these rows become active snapshot sources.

Sources 10–11 (BMAD, MemPalace): **Confirmed** — GitHub repos directly cited as
upstream sources in SOURCES.md [multi-ide-portability-via-installer-templates]
[shared-instructions-multi-harness-plugin-wrappers].

Sources 12–16 (arXiv, productcompass, OB1, LangGraph): **Confirmed** — appear in
the multiply-cited sources table in SOURCES.md §4 of the master inventory as
upstream sources for named findings.

Source 21 (Glean Agents docs): **Confirmed** — added 2026-07-09 when
`adapters/glean.md` was authored; the adapter's format claims were verified against
these docs pages via the Glean MCP server. A drift here stales the Glean adapter and
every `ports/glean-agent.md` derived from it.

---

## 2. Snapshot Storage

The snapshot records the last-known state of every watched source.
It lives at:

```
refresh-runs/snapshot.yaml
```

### 2.1 Snapshot Schema

```yaml
# refresh-runs/snapshot.yaml
---
snapshot_version: "1.0"
last_updated: "<ISO-8601 datetime>"
updated_by_run_id: "<run_id>"

corpus_hashes:
  "<relative-path-to-finding-file>":
    filename_hash: "<sha256>"
    content_hash: "<sha256>"
    last_seen: "<ISO-8601 date>"
  # ... one entry per finding file

platform_docs:
  "<source-key>":
    url: "<URL>"
    anchor: "<fragment-id or 'none'>"
    content_hash: "<sha256>"
    commit_hash: "<git-hash or null>"
    last_fetched: "<ISO-8601 date>"
    status: confirmed        # confirmed | unknown-verify | placeholder
  # ... one entry per platform_doc row in the watchlist

academic:
  "<query-key>":
    query: "<search query string>"
    last_result_count: 0
    last_result_hashes:
      - "<sha256 of result set>"
    last_fetched: "<ISO-8601 date>"

external:
  "<source-key>":
    description: "User-configurable; leave blank until user configures"
    last_fetched: null
    content_hash: null

regression_baseline_pass_rate: 0.95    # updated by Apply mode after each successful commit
```

### 2.2 Initializing the Snapshot

On first use, Detect mode must initialize `snapshot.yaml`:
1. Walk the corpus directory and record `filename_hash` + `content_hash`
   for every finding file.
2. Fetch each confirmed platform_doc URL and record the content hash
   (or commit hash for GitHub repos).
3. Mark all `unknown-verify` rows with `status: placeholder` and
   `content_hash: null`.
4. Set `regression_baseline_pass_rate` to `null` (it is populated
   after the first successful Apply run).

Until a row's status is `confirmed`, Detect mode skips it and
emits a one-time warning recommending verification.

---

## 3. Cadence Recommendations

### 3.1 Research Findings Corpus — Every Refresh Run

The corpus is the most actively updated source in the package's
dependency graph; new findings may appear between refresh runs,
and any finding revision can change a cited claim. Check on every
Detect run [sandbox-first-modification-validation].

### 3.2 Platform Documentation — Monthly

Platform documentation changes slowly but unpredictably — a single
API change can invalidate an adapter doc's central claim. Monthly
checks balance coverage against the cost of unnecessary runs.

Rationale: Anthropic, Cursor, GitHub Copilot, OpenAI Codex, and
Perplexity each publish documentation that may silently invalidate
claims in the adapter files. The adapter files explicitly label
unknown capabilities with "Unknown — verify" [multi-ide-portability-via-installer-templates];
monthly checks provide the verification mechanism.

### 3.3 Academic / arXiv — Monthly

arXiv signal-to-noise is low per individual result but cumulative.
A monthly search for new papers on skill authoring, agent evals,
and context file engineering catches emerging findings before they
diverge significantly from the package's citations.

### 3.4 Multiply-Cited Sources — Quarterly

The 31 sources in SOURCES.md §1 (multiply-cited across 2+ findings)
are the most stable references in the package — GitHub repos and
arXiv papers change rarely after publication. Quarterly checks
are sufficient.

Exception: If a multiply-cited source is a living documentation page
(not a paper or committed repo file), upgrade its cadence to monthly.

### 3.5 User Knowledge Base — User-Defined

The external placeholder source (row 20) is user-configured.
Leave cadence unset until the user supplies a URL and diff strategy.

---

## 4. Adding New Sources

### 4.1 Criteria for Inclusion

A source may be added to the watchlist only if it meets all three
criteria:

1. **Authoritative:** Primary source (official documentation, published
   research paper, direct GitHub repo) or convergent secondary source
   (same claim corroborated independently by multiple primary sources).
   Marketing pages, summary blog posts, and AI-generated content
   are excluded (§6).

2. **Stable URL:** The URL must be expected to remain accessible and
   content-stable enough to support hash-based comparison. GitHub
   repos and arXiv pages qualify; dynamically routed pages without
   stable anchors require a fallback strategy (full-page hash).

3. **Topically related:** The source must be directly relevant to one
   of the package's existing concept areas (skill authoring, eval
   design, HITL / safety gates, cross-platform portability, validation
   pipelines). A source that is only tangentially related adds noise
   to the Detect pass.

### 4.2 Process for Adding

1. Propose the new source via Propose mode, under the `new-concept`
   tier in the proposal schema.
2. The proposal must include: the source URL, a justification for
   each of the three criteria above, and the proposed diff strategy.
3. Human approval is required before the source is added to
   `snapshot.yaml` and the watchlist table [advisory-only-for-persistent-mutations].
4. After approval, the source is added to `snapshot.yaml` with
   `status: confirmed` and its initial content hash.

---

## 5. Removing Sources

### 5.1 When to Remove

A source should be proposed for removal when any of the following apply:

- **URL rot:** The URL returns 404 or is permanently redirected to
  unrelated content.
- **Content quality degraded:** The source has been taken over by
  different authors, substantially rewritten in ways that invalidate
  its original claims, or no longer maintained.
- **Superseded:** The source's content is fully covered by a newer,
  higher-quality primary source that is already in the watchlist.
- **No longer cited:** The finding(s) the source underpinned have
  been removed or updated to cite a different source; the watchlist
  entry now serves no package purpose.

### 5.2 Process for Removing

Same process as adding: Propose mode, human approval required before
the row is removed from `snapshot.yaml` and the watchlist table
[advisory-only-for-persistent-mutations]. The audit log records the
removal with the reason.

After removal, check whether any manifest entries or proposal
descriptions reference the removed source; update or close those
entries in the same proposal.

---

## 6. Out-of-Scope Sources

The following source types are excluded from the watchlist regardless
of topical relevance:

| Excluded type | Reason |
|---------------|--------|
| Marketing pages and product announcement posts | Signal quality too low; claims are promotional, not empirical |
| Blog posts without primary citations | Cannot trace to primary source; unfalsifiable claims |
| AI-generated content farms | Content may be plausible-sounding but not grounded in research; indistinguishable from genuine findings without primary-source verification |
| Social media threads and short-form posts | Insufficient context to evaluate claim quality; unstable URLs |
| Paywalled sources | Cannot be checked deterministically without credentials; breaks reproducibility of the Detect run |

The guiding principle: every source in the watchlist must support the
same citation standard used throughout the package — every claim
traceable to a primary source that can be independently verified
[bmad-deterministic-skill-validator].

---

*Citations: [sandbox-first-modification-validation] for corpus-check-every-run rationale;
[multi-ide-portability-via-installer-templates] for platform doc verification rationale;
[advisory-only-for-persistent-mutations] for human-approval requirement on watchlist
mutations; [bmad-deterministic-skill-validator] for source quality standard;
[skill-as-package-export-with-references] for SOURCES.md completeness requirement.*
