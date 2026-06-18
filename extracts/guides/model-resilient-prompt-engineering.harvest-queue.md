# Co-occurrence Harvest Queue — Model-Resilient Prompt Engineering

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-05-24 | extracted | rule | [[layered-prompt-assembly-stable-segment-caching]] | Never inline ephemeral turn state into cached prompt layers | extracted to [[never-inline-ephemeral-into-cached-layers]] |
| 2026-05-24 | extracted | template | [[layered-prompt-assembly-stable-segment-caching]] | Seven-layer prompt assembly template with cache-control annotations | extracted to [[seven-layer-prompt-assembly-with-cache-control]] |
| 2026-05-25 | extracted | rule | [[programmatic-snippet-extraction-via-shell-anti-hallucination]] | "Extract code snippets via shell tools, never from model memory" | extracted to [[extract-snippets-via-shell]] |

## Per-row details

### layered-prompt-assembly-stable-segment-caching::rule::never-inline-ephemeral-into-cached-layers

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[layered-prompt-assembly-stable-segment-caching]]
- **Source excerpt:**
  > "Ephemeral layers injected as separate content blocks to avoid cache invalidation. Key insight: decouple caching boundary from prompt structure boundary."
- **Codifier's reading:** This is a hard invariant that governs prompt assembly in any multi-turn API context — not a recommendation but a constraint with clear failure mode (cache invalidation every turn). Rule form is appropriate: it's a "never" statement with a testable violation condition. Applies broadly across agent systems using Anthropic caching.
- **Suggested headline:** Never inline ephemeral turn state into cached prompt layers
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[never-inline-ephemeral-into-cached-layers]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[never-ask-claude-to-compact-claudemd]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[never-ask-claude-to-compact-claudemd]] via manual queue edit (or future skill mode).

Extracted 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — to [[never-inline-ephemeral-into-cached-layers]]. Nick ruled "create new" per extension proposals report; false positive on corpus match.

### programmatic-snippet-extraction-via-shell-anti-hallucination::rule::extract-snippets-via-shell

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[programmatic-snippet-extraction-via-shell-anti-hallucination]]
- **Source excerpt:**
  > "When an agent produces output that contains code snippets quoted from a codebase, instruct it to extract the snippets via shell tools — sed, grep, cat, or equivalent — rather than typing or reconstructing the code from its understanding. Shell-extracted snippets are byte-accurate; hand-typed snippets are reconstructed from the model's working understanding of the file, which may differ from the actual bytes in subtle ways."
- **Codifier's reading:** Clear imperative directive: "use shell tools for code extraction, never reconstruct from memory." Machine-enforceable as a hook that diffs quoted code blocks against actual file content. Prevents both direct hallucination and stale mental model failures. The rule stands independently of the broader pattern about documentation generation workflows.
- **Suggested headline:** extract-snippets-via-shell
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[extract-snippets-via-shell]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[agent-self-reporting-unreliability-independent-eval]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[agent-self-reporting-unreliability-independent-eval]] via manual queue edit (or future skill mode).

Extracted 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — to [[extract-snippets-via-shell]]. Nick ruled "create new" per extension proposals report; false positive on corpus match.

### layered-prompt-assembly-stable-segment-caching::template::seven-layer-prompt-assembly

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[layered-prompt-assembly-stable-segment-caching]]
- **Source excerpt:**
  > "Seven ordered layers: core role/persona, SOUL.md, MEMORY.md + USER.md, skills metadata, project context, provider-specific instructions, ephemeral layers."
- **Codifier's reading:** The seven-layer ordering is a reusable structural scaffold — stable enough to be a fill-in-the-blanks template for any agent system prompt. Combining the layer ordering with cache-control annotation guidance makes this a practical template, not just a concept. Distinct from Template 1 (model-resilient prompt structure) in the guide, which focuses on a single prompt's ROLE/AUTHORITY/GOAL/CONTEXT/FORMAT block rather than multi-layer system prompt assembly.
- **Suggested headline:** Seven-layer system prompt assembly template with cache-control annotations
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[seven-layer-prompt-assembly-with-cache-control]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[seven-layer-prompt-assembly-with-cache-control]].
