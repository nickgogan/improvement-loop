# Letta & Supermemory — Cross-Framework Memory Survey

Dossier for the E1 memory-architecture spec's cross-framework survey (Track B). Written 2026-07-16. Internal grounding (Letta analysis dated 2026-05-25, v0.16.8; Supermemory analysis dated 2026-04-23) is 6-12 weeks stale against external evidence gathered today — every section below flags where the two diverge. Perplexity's research/ask tools timed out repeatedly during this session (5-minute timeouts, both providers, both frameworks); external evidence here comes from WebSearch, WebFetch (including the HN Algolia API), and the `gh` CLI against live GitHub issue trackers as of 2026-07-16-17.

---

## Letta (formerly MemGPT)

### 1. Snapshot

**What it is:** Open-source platform (Apache 2.0, Python) for stateful agents with self-editing, hierarchical memory. Descends directly from the MemGPT research project (UC Berkeley Sky Computing Lab). As of mid-2026 the company's center of gravity has shifted to **Letta Code**, a memory-first terminal coding agent (launched Dec 2025) — ranked #1 model-agnostic open-source agent on Terminal-Bench (42.5%) as of a June 2026 report. LettaBot (a separate chat product) was archived into Letta Code as "Channels" in May 2026; a desktop app shipped April 2026.

**Memory scope:** single-agent and multi-agent (round-robin, supervisor, dynamic, sleeptime/reflection, swarm) stateful memory; used for both long-horizon conversational agents and now, primarily, coding agents.

**Currency of this dossier's info:** Internal grounding (repo-analysis, 2026-05-25, v0.16.8) describes `SleeptimeMultiAgentV4` as the current background-memory pattern. External evidence (GitHub issue #3294, filed and closed 2026-04-08 — *before* the internal analysis date but not reflected in it) shows Letta was **already migrating from server-side "sleeptime" agents to client-side "reflection" subagents** at that point, with v0.19.0 adding parent-agent memory access for reflection agents. As of 2026-07-16 the repo still contains `sleeptime_multi_agent_v4.py` per the analysis, but the product-facing terminology and default path are `reflection`. Treat "sleeptime" and "reflection" as the same lineage mid-rename; do not assume the internal analysis's code-level detail is the current default UX. Repo stats as of 2026-07-16: 23,822 stars, 2,526 forks, 49 open issues, last push 2026-07-03.

### 2. Memory model by type

**Working / short-term memory**
- *Substrate:* the LLM context window — in-context message buffer plus the compiled system prompt (core memory blocks + tool-usage rules + memory metadata + directories/skills).
- *Write path:* every turn appends to the message buffer automatically; no separate write step.
- *Injection/recall:* `_rebuild_memory_async()` runs before every LLM call — refreshes blocks from the DB, recompiles the XML-rendered system prompt (`Memory.compile()`), injects into `system message[0]`. Provider-adaptive: Anthropic models get line-numbered memory blocks; other providers get standard rendering.
- *Consolidation/reflection:* summarization triggers when context exceeds a threshold. Four modes: `all` (summarize entire evicted window), `sliding_window` (summarize evicted prefix, keep recent), `self_compact_all` / `self_compact_sliding_window` (agent self-summarizes). Default summarizer models vary by provider (Haiku 4.5 for Anthropic, GPT-5-mini for OpenAI, Gemini 2.5 Flash for Google).
- *Decay/forgetting:* evicted messages are gone from the live buffer once summarized; the summary persists, raw messages do not (unless recall memory is separately queried).

**Episodic memory (specific past events/sessions)**
- *Substrate:* Recall memory — a searchable message database (hybrid text + semantic similarity) via the `conversation_search` tool. Also git-backed memory repos (for `git-memory-enabled` agents): every core-memory edit is a git commit, with GCS as source-of-truth object storage and PostgreSQL as a read cache.
- *Write path:* every conversation turn is persisted to the message DB automatically; git-memory-enabled agents additionally commit each core-memory-block change to a per-agent git repo, serialized as Markdown+YAML.
- *Injection/recall:* not auto-injected — the agent must explicitly call `conversation_search` to pull past turns back into context. Git-memory agents get a `<memory_filesystem>` tree rendered into the prompt (paths as block identifiers, e.g., `system/persona`) but the actual git history requires explicit tooling to inspect.
- *Consolidation/reflection:* the sleeptime/reflection background agent is the primary consolidation mechanism (see Lifecycle trace below) — runs asynchronously at a configurable frequency, processing recent conversation into structured memory without blocking the foreground agent.
- *Decay/forgetting/supersession:* no automatic pruning of recall memory found in the analysis or external search; git history is append-only (every commit retained) unless manually squashed. **Gap, per open GitHub issue #3116 (2026-06-24, still open):** archival memory (see below) has no deduplication/consolidation mechanism at all — core memory has `rethink_memory()`/`memory_replace()` for exactly this, archival does not, so long-running agents accumulate redundant near-duplicate passages ("User's favorite color is blue" / "The user mentioned they like blue" / "User prefers blue" as four separate passages, verbatim example from the issue).

**Semantic memory (general facts/rules)**
- *Substrate:* Core memory blocks — named, labeled containers (`persona`, `human`, custom labels) with a `description` field that tells the agent *how* the block should influence behavior, a `value`, and metadata (`read_only`, character limit). Rendered as XML (`<label>`, `<description>`, `<metadata>`, `<value>`) directly in the system prompt — always in context, never retrieved.
- *Write path:* agent-initiated via `core_memory_append`, `core_memory_replace`, or the unified `memory()` tool (Anthropic's native memory tool is also supported per HN discussion, 2025-Q4 timeframe). Git-memory-enabled agents commit each write.
- *Injection/recall:* always in context by construction — no retrieval step; this is the tier MemGPT's "OS-inspired" framing is built around (RAM analogy vs recall's disk-cache and archival's cold-storage analogy, per multiple 2026 comparison blogs).
- *Consolidation/reflection:* `rethink_memory()` allows a full block rewrite; the description field can itself be edited independently of value (per internal finding), though this is undocumented as a distinct workflow.
- *Decay/forgetting/supersession:* character-limit enforcement is a hard boundary (oldest/least-relevant content must be trimmed by the agent itself to stay under limit); `read_only: true` blocks resist agent overwrite entirely. **Known bug (GitHub #3397, opened 2026-07-07, still open as of 2026-07-16):** `Memory.blocks` has no duplicate-label guard — a second block sharing a label with an existing one becomes permanently unreachable via the public API (`get_block`/`update_block_value` only ever touch the first match) but is *still rendered into the compiled prompt*, producing two contradictory `<human>` sections with no warning. The sibling `file_blocks` field already guards against this; `blocks` does not.

**Procedural memory (how to do things)**
- *Substrate:* Skills system (capability extension) and subagent composition; a declarative **tool-rule engine** (`ToolRulesSolver`) that constrains tool-call sequences — `InitToolRule`, `TerminalToolRule`, `ChildToolRule`, `ParentToolRule`, `ConditionalToolRule`, `RequiresApprovalToolRule`, and others.
- *Write path:* human-authored (tool rules, skills) at agent-configuration time, not agent-written during operation.
- *Injection/recall:* tool rules are rendered into the prompt as a `<tool_usage_rules>` XML block **and** enforced programmatically by the solver — dual enforcement (soft prompt guidance + hard code-level constraint), which the internal KB finding flags as a reliability-increasing pattern distinct from prompt-only constraint systems.
- *Consolidation/decay:* none — this is a human-governed, versioned-by-config artifact, not something the agent evolves.

### 3. Lifecycle trace — one core-memory item, end to end

1. **User message arrives.** Nick tells the agent "Actually I use TypeScript now, not plain JS." The foreground agent (`LettaAgentV3`) processes the turn.
2. **Self-edit.** The agent calls `core_memory_replace` (or `memory()`) to update the `human` block's value from "prefers JS" to "prefers TypeScript." `execute_tool_and_persist_state()` → `update_memory_if_changed()` → `block_manager.update_block()` writes the new value to the backend DB. If the agent is `git-memory-enabled`, this write is also committed to the per-agent git repo (Markdown+YAML, GCS source-of-truth, PostgreSQL cache).
3. **Next-turn rebuild.** Before the *next* LLM call, `_rebuild_memory_async()` refreshes all blocks from the DB and recompiles the system prompt — the updated `human` block is now what's rendered, replacing the stale version.
4. **Background consolidation (sleeptime/reflection, configurable frequency).** Independently of the foreground turn, a background reflection agent — with its own "memory expert" persona and dedicated memory-editing tools — processes the recent conversation asynchronously and may promote details into archival memory (e.g., "TypeScript preference confirmed across 3 sessions" as an archival passage) without blocking the user-facing response.
5. **Archival write (if triggered).** `archival_memory_insert` embeds and indexes the passage for future semantic retrieval. No dedup check runs at this step (per #3116, open) — if a similar passage already exists, both persist.
6. **Recall, sessions later.** The foreground agent calls `archival_memory_search` with a query or tag filter when it judges the info relevant; results are returned as tool output, not auto-injected.
7. **Audit.** If git-memory-enabled, `git log` on the agent's memory repo shows every core-memory edit as a discrete, diffable, revertible commit — the audit trail the internal finding highlights as the pattern's main value.

### 4. Practitioner sentiment (dated)

**Positive, 2026:**
- Terminal-Bench #1 ranking for Letta Code among model-agnostic OSS coding agents, cited as "a strong production signal" (Callsphere blog, 2026 deep-dive).
- HN "Show HN: Letta – Git-Based Memory for Coding Agents" (2026-02-15, morawr) — no comment thread retrievable at fetch time, but the post itself signals the git-backed-memory feature was framed as launch-worthy.
- HN "Letta Code: a memory-first coding agent" thread (id 46293374) — Letta team member (pacjam) frames the core differentiator as *"One agent per project, specialized, infinitely lived. No more compactions, no more forgetting"* — explicitly positioned against context-window-management approaches (like Claude Code's compact/clear cycle). A second commenter (cpfiffer) draws a parallel to MemGPT's original CLI-first philosophy, affirmed by the team as "CLI is All."
- 23.8k GitHub stars, 2.5k forks as of 2026-07-16 — sustained community size.

**Negative / friction, dated:**
- **2026-07-08 (open as of 2026-07-16), GitHub #3388:** "Cross-Session State Leakage via Persistent Core Memory Poisoning" — in continuous-execution/multi-tenant daemon deployments (e.g., shared eval clusters), an agent's malicious or accidental core-memory self-edit persists to the DB with no hard teardown between independent tasks sharing a daemon, so poisoned context leaks into unrelated subsequent runs. Filed as a sandbox-isolation failure, not yet resolved.
- **2026-07-07 (open):** duplicate-label memory-block bug (#3397, detailed above) — silently stale, contradictory core-memory content can persist in the compiled prompt with no user-facing error.
- **2026-06-24 (open):** archival memory has no consolidation/dedup mechanism (#3116) — feature gap acknowledged by the maintainers' own comparison to core memory's `rethink_memory()`.
- **2026-05-25:** "Sleeptime agent failing with Claude 4.5 (Unhandled LLM error)" (#3109) — background-agent reliability issue tied to a specific model.
- **2026-04-08 (closed same day, but the underlying gap persisted per the issue body):** sleeptime-to-reflection migration caused a capability regression for users who had customized their sleeptime agent's persona/instructions beyond memory consolidation — the client-side reflection replacement initially lacked full persona customization, chat-history access, and forced a choice between losing customization or self-hosting without Letta Cloud credits. Filed on behalf of a Discord community member.
- **2026-03-06:** "Sleeptime message grouping causes role confusion" (#3104) — background-agent message-role handling bug.
- **General architecture critique, 2026 comparison articles (vectorize.io "Mem0 vs Letta"):** *"Every memory operation also costs inference tokens"* since the agent must reason about what to store; *"Requires LLM for all memory operations. Memory decisions inherit LLM opacity"* — no interpretable non-LLM fallback. Also: architectural lock-in ("Adopting Letta means adopting an entire agent platform"), Python-only SDK vs Mem0's Python+JS, and **no published LongMemEval numbers** as of the article's writing (2026), making direct benchmark comparison impossible; LoCoMo is reported around ~83.2%.
- **"Agent eats its own context" failure mode** (Callsphere 2026 deep-dive): the agent can overwrite its own core-memory persona block until it loses track of who it is; the documented mitigation is read-only persona blocks plus per-block token caps — i.e., the platform's own answer to self-editing memory's central risk is to make part of memory *not* self-editable.

### 5. Verdict (for a markdown+git, single-operator, human-gated engine)

**Strengths:**
- **Git-backed memory versioning is the single most directly transferable pattern.** Markdown+YAML blocks in a git repo, GCS/object-storage as truth with a DB as cache, full diff/revert/audit via commands the engine already uses daily. MetaSystem's own commit-per-change discipline (Conventional Commits, `Refs:` footer) is structurally the same idea Letta applies to memory blocks.
- **Memory block as labeled semantic container with a `description` field** is a small, cheap upgrade to any frontmatter-based memory store: pairing *what's stored* with *how to use it* reduces the need for a separate "how to interpret this file" instruction layer — directly applicable to MetaSystem's finding/DD/IB frontmatter, which currently documents *what* but not always *how a consuming agent should weight it*.
- **Dual-enforcement tool rules** (rendered in-prompt *and* enforced in code) is a reliability pattern independent of memory specifically — worth carrying into any future skill/agent constraint design.

**Failure modes to weight heavily:**
- **Self-editing memory quality is entirely LLM-judgment-dependent and opaque** (own admission via vectorize.io review) — for a human-gated engine, this is close to opposite of the desired posture; MetaSystem's `/self-improve` promotion pipeline (draft → shadow-sandbox → fresh-context grade → Nick gate) is a stronger discipline than Letta's runtime self-edit-with-no-review-gate model.
- **Cross-session state leakage / memory poisoning under shared infrastructure (#3388, open)** is a direct warning against ever running shared background daemons across independent contexts without a hard reset boundary — relevant if the engine ever runs pooled subagent infrastructure rather than per-task-scoped processes.
- **API/terminology churn (sleeptime → reflection, mid-2026)** with an initial capability regression for customized deployments is a caution against building deep, code-level dependencies on any single vendor's background-agent primitive; the *pattern* (foreground/background split) is worth adopting, the *specific API* is not stable enough to depend on directly.
- **No archival-tier consolidation (#3116, open)** shows that even a well-regarded memory-first platform can ship two tiers with asymmetric maintenance (core has rethink/replace tools, archival doesn't) — a concrete argument for designing decay/consolidation into *every* memory tier from the start rather than retrofitting.

---

## Supermemory

### 1. Snapshot

**What it is:** Cloud-capable memory + context engine (MIT-licensed, TypeScript-dominant Turborepo/Bun monorepo, deployed on Cloudflare Workers). Extraction-based: an LLM parses conversations/documents into discrete memory records with typed relationships. Ships a cross-provider benchmarking framework, MemoryBench, that explicitly includes competitors.

**Memory scope:** multi-tenant SaaS (hierarchical container-tag isolation) with a newer self-hosted server line (`server-v0.0.3` → `v0.0.5` as of July 2026) that is materially less mature than the hosted product.

**Currency of this dossier's info:** internal grounding is dated 2026-04-23 ("latest, no version tag"). External evidence gathered today (2026-07-16/17) shows: (a) the self-hosted binary line has shipped and is actively being hardened — v0.0.3 and v0.0.5 both have open, unresolved severe bugs; (b) repo stats as of 2026-07-16: 28,418 stars, 2,473 forks, **80 open issues** — nearly double Letta's 49 despite comparable star count, a signal of higher current operational churn; (c) practitioner skepticism threads on HN (undated precisely by content but 2026-vintage per item IDs in the 46-47M range) directly question the product's differentiation and business viability, unresolved at fetch time.

### 2. Memory model by type

**Working / short-term memory**
- Not a distinct architectural tier — Supermemory is memory infrastructure consumed by an external agent, not a foreground conversational agent itself. The closest analog is the **dynamic** memory layer (below), which behaves as recency-weighted working context rather than a literal context-window buffer, since Supermemory has no LLM loop of its own to hold a buffer in.

**Episodic memory (specific past events/state)**
- *Substrate:* **Dynamic memories** — `isStatic: false` records reflecting recent activity/current context ("Working on auth migration," "Debugging rate limits"). Also the full version chain behind any `updates`-linked memory (every superseded version retained, queryable).
- *Write path:* `client.add()` triggers the 6-stage IngestContentWorkflow (queued → extracting → chunking → embedding → indexing → done); the extractor flags each new fact `isStatic` at write time and checks for date references and contradictions against existing memories on the same subject.
- *Injection/recall:* `profile()` API call returns `{ static: [...], dynamic: [...] }` in a single ~50ms response; dynamic memories get time-weighted retrieval priority (recent-first) rather than the static tier's always-included priority.
- *Consolidation/reflection:* none described as a distinct background pass (no sleeptime/reflection-agent analog) — consolidation happens synchronously at write time via the extraction pipeline, not asynchronously post-hoc.
- *Decay/forgetting/supersession:* **content-derived temporal expiration** — the extractor parses natural-language date references ("I have an exam tomorrow" → `expiresAt = today+1`) and auto-expires (soft-hide or hard-delete, policy-dependent) once the date passes. This is a genuinely distinct third decay strategy in the KB's design space, alongside importance-based decay and surprisal-gated writes (both observed in Memongo).

**Semantic memory (general facts)**
- *Substrate:* **Static memories** — `isStatic: true` records for permanent facts (identity, long-term preferences). The **typed-relationship graph** — three named edges: `updates` (new fact supersedes old; old retained with `isLatest: false`), `extends` (adds context without changing the original claim), `derives` (system-inferred pattern across multiple source memories, with provenance edges back to sources).
- *Write path:* same extraction pipeline as dynamic memories; `isStatic` and relationship type are both extractor-determined, not caller-specified.
- *Injection/recall:* `profile.static` list, retrieval-prioritized; `search()`/`recall` MCP tool can request latest-only (default), full version chain, or a specific version. Hybrid search runs RAG (document chunks) and Memory (user facts) together in one query.
- *Consolidation/reflection:* **automatic contradiction resolution** — a new memory contradicting an existing one on the same subject ("User lives in NYC" vs "I just moved to SF") triggers an `updates` relationship; the old memory is retained but flagged `isLatest: false`, not deleted.
- *Decay/forgetting/supersession:* superseded (`isLatest: false`) memories are retained indefinitely by default — the KB's own finding flags this as a bloat risk with no described pruning discipline ("Superseded-not-deleted bloat... needs a separate pruning discipline").

**Procedural memory**
- **Not handled.** Supermemory is memory infrastructure, not an agent framework — there is no skills/workflow/procedure tier. The closest artifact is the 6-stage IngestContentWorkflow itself, which is a *content-processing* pipeline, not agent-facing procedural memory. (This N/A determination is explicit in the internal structural analysis, which records workflow-topology as N/A for this repo with rationale.)

### 3. Lifecycle trace — one memory item, end to end

1. **Write.** An agent (via MCP `memory` tool, action `save`) or a connector (Gmail/Drive/Notion/GitHub, cron-polled every 4 hours) submits "I just moved to SF" tagged to `containerTag: org_acme_user_alice`.
2. **6-stage pipeline.** queued → extracting (LLM parses the fact) → chunking → embedding → indexing → done.
3. **Contradiction check.** Extractor finds an existing memory "User lives in NYC" on the same subject for the same container tag. A contradiction is detected.
4. **Relationship creation.** An `updates` edge is created: new memory (`isLatest: true`) supersedes old (flagged `isLatest: false`, not deleted). No date reference is present in this fact, so no expiration is set.
5. **Profile composition.** Next `profile({ containerTag: "org_acme_user_alice" })` call returns the SF fact in `static` (identity-shaped) — NYC no longer appears in the default (latest-only) response but remains queryable via full-history.
6. **Visualization (optional, human-facing).** The `memory-graph-playground` app can render the update chain as a graph — a first-class UI surface distinct from Letta's approach (no equivalent visual tool observed in Letta).
7. **Hybrid recall.** A later query "where does the user live?" runs hybrid search — memory layer returns the SF fact (user-specific, stateful); if a RAG-indexed document also mentions SF real estate, both are interleaved in the response.
8. **Multi-agent/cross-harness access.** Any of the four harness plugin repos (`claude-supermemory`, `openclaw-supermemory`, `opencode-supermemory`, `hermes-agent`) or a direct MCP client can read the same fact through the hosted MCP server (Cloudflare Durable Objects, one object per session), scoped by the same container tag.

### 4. Practitioner sentiment (dated)

**Positive / claimed, 2026:**
- Benchmark claims: #1 on LongMemEval (81.6% headlined), LoCoMo, and ConvoMem per the product's own README (as of the 2026-04-23 internal analysis). A separate 2026 comparison piece (DEV.to, "5 AI Agent Memory Systems Compared") reports Supermemory's **LongMemEval-S at 85.4% overall accuracy (92.3% single-session)** with **sub-300ms recall**, versus ~4s for Zep and 7-8s for Mem0 in the same comparison — a large latency advantage if the numbers hold up under independent testing.
- **MemoryBench** (`npx skills add supermemoryai/memorybench` → `/benchmark-context`) is a genuinely distinctive trust mechanism: an open, competitor-inclusive benchmarking harness, contrasted favorably against closed/self-reported leaderboards in both the internal KB finding and general 2026 commentary on memory-system evaluation norms.
- A different, independent 2026 comparison (vectorize.io) gives a markedly lower and explicitly hedged number: **~70% on LoCoMo, "estimated from limited published data"** — flagging that Supermemory's own benchmark disclosure is incomplete enough that third parties are estimating rather than citing hard numbers. **The two external 2026 sources disagree by double-digit points on different benchmarks and neither is a primary-source reproduction** — treat both as directional, not authoritative, consistent with the internal analysis's own note that there's "no dev/held-out split discipline visible in the repo" and "no retraction log for prior claims."

**Skepticism / friction, dated:**
- **HN thread "Is SuperMemory That Impressive?" (2026, item 46426762):** original poster's stated skepticism — questions what advantage the product offers over "a well-tuned vector DB + retrieval logic," whether the moat extends beyond UX/branding, how memory degradation and conflicting data are handled at scale, and requests real (non-demo) latency/cost numbers. No visible reply thread at fetch time — an open, unresolved question in public discourse, not refuted.
- **HN thread "Ask HN: Who is the main customer for Mem0/Supermemory, why they pay?" (2026, item 46004834):** commenter (ihsanf) skepticism about the business model — *"memory for agent getting some early hype, but I don't really understand who is gonna pay them when we have RAG and MCP to add memory layer for agents."*
- **Self-hosted deployment line is markedly immature as of 2026-07:**
  - **#1177 (opened 2026-07-16, open):** self-hosted `server-v0.0.3` on macOS OOMs (`RangeError` in `node:crypto`) once the local DB reaches ~150MB — the encrypted-snapshot path serializes the *entire* DB into one base64 string, exceeding V8's max string length. Consequence cascades into a permanent retry-cron loop (one doc ID re-marked "failed" 243 times in one log) plus lossy deletion and, per the issue, a runaway ~4-hour memory-agent process. Docs claim "local is bounded by one machine" but document no such DB-size ceiling.
  - **#1296 (2026-07-16, open):** self-hosted 0.0.5 on macOS — server enters an uninterruptible kernel wait state on SIGTERM or crash, surviving `kill -9`, holding its port until a full reboot.
  - **#1293 (2026-07-14, open):** upgrading self-hosted 0.0.3→0.0.5 skips a required `profile_buckets` migration; the profile API (the same `/v4/profile` endpoint central to the static/dynamic composition pattern) returns 500 afterward.
  - **#1237 (2026-07-13, open):** API-key auth broken in 0.0.5 — 401 errors even with a valid key.
  - **#1209 (2026-07-13, open):** self-hosted memory agent fails outright with Azure OpenAI or any OpenAI-compatible proxy — only first-party OpenAI/Anthropic endpoints work.
  - **#1247 (2026-07-12, open):** `@supermemory/ai-sdk` has drifted from `@supermemory/tools`, silently reintroducing three previously-fixed bugs — including a divergent default container-tag scope the issue author calls "the dangerous one," since an unset config in one package silently falls back to a different (and potentially wrong-scope) tag than the other package's documented default.
  - **80 open issues** as of 2026-07-16 vs Letta's 49, despite similar repo size/star count — a rough proxy for higher current defect/support load, concentrated visibly in the newer self-hosted line rather than the mature hosted SaaS.
- **Independent architecture commentary, 2026 (context-memory review pieces):** general framing that no memory vendor (Supermemory included) is evaluated on *post-retrieval* behavior — whether contradiction detection is confidence-scored, whether staleness (job/city changes) is actually caught, or whether retrieved-memory confidence tracks source-evidence quality. This echoes the internal KB finding's own listed failure mode (bi-coastal false-positive contradictions) without adding a concrete production incident report — the concern remains conceptual/design-review-level as of this research pass, not yet documented as an observed production failure.

### 5. Verdict (for a markdown+git, single-operator, human-gated engine)

**Strengths:**
- **The typed-relationship vocabulary (`updates`/`extends`/`derives`) is the most transferable idea, independent of Supermemory's infrastructure.** It gives MetaSystem a concrete, three-verb answer to "how do I evolve a governance item without losing history or falling back to delete-and-reappend" — directly applicable to `pipeline_status` transitions or DD supersession, reimplementable natively in frontmatter without adopting any Supermemory code.
- **Static/dynamic profile composition maps almost exactly onto the engine's existing session-handoff shape** (decisions/identity vs current-work/state) — formalizing that split at a "profile API" layer (even a markdown-query convention, not a real API) is a low-cost, high-clarity upgrade.
- **Content-derived temporal expiration** is a genuinely novel decay mechanism (parsing "tomorrow"/"Q2"/date references directly from content) — complementary to, not competing with, importance-based decay; worth a design note for any future engine memory-decay policy.
- **MemoryBench's competitor-inclusive benchmarking stance** is a governance pattern worth borrowing in spirit (publish evaluation apparatus, let outsiders verify) even without adopting the product.

**Failure modes to weight heavily:**
- **Benchmark claims are self-reported, disputed in magnitude by independent sources (85.4% vs ~70% on different benchmarks, neither independently reproduced), and unresolved in public skepticism threads** — treat every Supermemory performance number as a claim, not a fact, until independently reproduced (this directly matches the internal analysis's own governance-model finding: "no dev/held-out split discipline visible in the repo").
- **The self-hosted path — the only path relevant to a local-first, non-cloud engine — is markedly less mature than the hosted SaaS as of July 2026,** with data-loss-adjacent bugs (lossy deletion, broken migrations, auth failures) surfacing in the two weeks immediately preceding this research pass. This is a strong argument against depending on the *product* even where the *patterns* are worth adopting.
- **Extraction is LLM-dependent at write time** (cost + opacity, same category of concern as Letta's self-editing memory, though contradiction resolution is at least deterministic once the LLM call returns a verdict).
- **No described pruning discipline for superseded (`isLatest: false`) memories** — the graph is architecturally append-heavy; a markdown+git implementation of the same idea would need an explicit archival/compaction policy from day one (git itself doesn't solve this — a git history also grows unboundedly without deliberate squashing).

---

## Letta vs Supermemory — contrast

Both frameworks independently converge on the same core insight — **a flat key-value or vector-similarity memory store is insufficient; memory needs typed structure and an explicit evolution mechanism** — but they solve it at opposite layers. Letta pushes memory management *into the agent itself* (self-editing tools, LLM decides what to keep/promote/demote); Supermemory pushes it *into the write-time extraction pipeline* (an LLM call at ingest decides `isStatic`, detects contradictions, and creates typed edges, with no agent-side tool call required). This is the "who does the memory work" split: agent-in-the-loop (Letta) vs pipeline-in-the-loop (Supermemory) — and it recurs as the central design fork in the wider KB (verbatim-storage-thesis vs typed-relationship-graph vs importance-based-decay findings all sit on this same axis).

Both are LLM-dependent at the point where memory quality is decided, and both currently ship that dependency as opaque to the operator — neither exposes a confidence score on its automated decisions (Letta's memory edits, Supermemory's contradiction/relationship inference) as of this research pass; both KB findings independently flag this as an improvement opportunity, not a solved problem.

Maturity signals diverge sharply along the *self-hosted/local* axis specifically: Letta's core (non-Cloud) path is the primary, well-exercised path (23.8k stars, 49 open issues, git-backed memory as a first-class feature). Supermemory's primary path is hosted SaaS; its self-hosted line is new and visibly fragile (80 open issues against 28.4k stars, several July-2026 issues showing data-loss-adjacent failures). For MetaSystem's local-first, single-operator, human-gated posture, Letta's operating model is structurally closer to home even though neither framework should be adopted wholesale — Letta's git-backed versioning pattern is the more directly reusable engineering artifact; Supermemory's typed-relationship and static/dynamic vocabulary are the more directly reusable *design* artifacts, transferable without touching Supermemory's code at all.
