# Claude Code — Native Memory Architecture

Dossier for the E1 memory-architecture spec's cross-framework survey (Track B). Scope: the Claude Code harness's own built-in memory mechanisms — not libraries or plugins layered on top. Written 2026-07-16; every mechanism below is version/date-stamped where the source gives one, per the recency rule.

---

## 1. Snapshot

Claude Code carries **five native, file-backed memory surfaces**, all markdown, all human-readable, none requiring an external database:

| Surface | What | Who writes | Scope |
|---|---|---|---|
| **CLAUDE.md hierarchy** | Persistent instructions (managed/user/project/local) + `.claude/rules/` | Human | Org → user → project → local, concatenated |
| **Auto memory (`MEMORY.md` + topic files)** | Claude's self-written notes (build commands, debugging insights, conventions) | Claude, autonomously | Per git repo, machine-local |
| **Subagent memory (`memory:` frontmatter)** | Per-subagent persistent directory (`user`/`project`/`local` scope) | The subagent | Per subagent name |
| **"Auto Dream" consolidation** | Background reflection pass that merges/dedupes/prunes memory files | Claude (background task) | Same scope as auto memory |
| **Context-window management** (Continue / `/rewind` / `/compact` / `/clear` / Subagents) | The working-memory substrate itself | User-invoked or automatic | Session-scoped |

**Currency note:** Auto memory shipped **v2.1.59, ~2026-02-27** and is on by default. Subagent `memory:` shipped **v2.1.33, ~2026-02** (per third-party dating; first-party docs don't date it). The five-tool context-management framing (Continue/rewind/compact/clear/subagent) was canonicalized by Anthropic's own product blog, **2026-04-15** (Thariq Shihipar). The `/doctor` CLAUDE.md-trim proposal requires **v2.1.206+**. The `MEMORY.md`-over-limit write-time nudge requires **v2.1.210+**; the frontmatter/comment-stripping fix to that check requires **v2.1.211+**.

**Important caveat on "Auto Dream":** this consolidation feature is documented across ~8 independent third-party blogs (claudefa.st, MindStudio, zenvanriel, antoniocortes.com, wmedia.es, decodethefuture.org, easyclaw.com) with consistent mechanical detail (24hr + 5-session dual-gate trigger, 4-phase orient/gather/consolidate/prune-index cycle) — but it is **absent from the first-party `code.claude.com/docs/en/memory` page as fetched today (2026-07-16)**, which describes auto memory in detail and does not mention dreaming, consolidation, or a background pass at all. One of the third-party sources (a GitHub repo, `grandamenium/dream-skill`) explicitly bills itself as replicating "Anthropic's **unreleased** auto-dream feature." Read this as: real, feature-flagged, rolling out unevenly, and not yet stable/documented first-party — treat every claim about it below as unconfirmed pending direct verification against a live `/memory` menu.

---

## 2. Memory model by type

### Working / short-term memory
**Substrate:** the context window itself — system prompt (~4.2K tokens, fixed), auto memory index, environment info, CLAUDE.md/rules, invoked skill bodies, conversation turns, tool outputs. This is the only memory type Claude Code treats as *the* memory system in casual usage; everything else exists to manage this one's decay.

**Write path:** every turn appends to it automatically; no separate "write" step.

**Injection/recall:** automatic and total until a management action is taken. Anthropic's canonical decision matrix (2026-04-15 blog) names five tools: **Continue** (do nothing — everything is load-bearing), **`/rewind`** (`Esc Esc`; jump to a checkpoint, keep useful file reads, drop the failed branch — the *default correction*, not forward-patching), **`/compact <hint>`** (lossy summarization, low effort), **`/clear`** (full reset, zero rot, user controls what carries forward), **Subagent** (fresh child window; only the conclusion returns to the parent). `/rewind` supports four restoration granularities: conversation-only, code-only, both, or "summarize from here."

**Consolidation/reflection:** `/compact` is the in-band consolidation step. Anthropic's stated rationale (2026-04-15): *"the model is at its least intelligent point when compacting"* — so compact **proactively**, at a stable checkpoint, not reactively at the hard cutoff. The 1M context window (Fable 5, Sonnet 5, Opus 4.6+, Sonnet 4.6) does not remove this pressure, only defers it — deferral makes the eventual compaction worse because there's more to summarize. A parallel finding (Robert Matsuoka, hyperdev.matsuoka.com, **2025-12-10**) reports Anthropic quietly moved the *automatic* compaction trigger from ~90%+ down to ~75% utilization specifically to preserve a ~50K-token reasoning buffer — i.e., Anthropic's own infra already encodes "compact earlier than you think."

**Decay/forgetting/supersession, precisely (first-party, `code.claude.com/docs/en/context-window`, "What survives compaction" table):**

| Mechanism | After `/compact` |
|---|---|
| System prompt / output style | Unchanged (not message history) |
| Project-root CLAUDE.md + unscoped rules | **Re-injected from disk** |
| Auto memory | **Re-injected from disk** |
| Rules with `paths:` frontmatter | Lost until a matching file is read again |
| Nested CLAUDE.md in subdirectories | Lost until a file in that subdirectory is read again |
| Invoked skill bodies | Re-injected, capped 5,000 tok/skill and 25,000 tok total; oldest dropped first, truncation keeps the file's *start* |
| Hooks | N/A — code, not context |

This table is the single most load-bearing fact in this dossier: **compaction is not uniformly lossy** — file-backed, root-level memory survives it structurally; only in-conversation-only and path-triggered content is at risk.

### Episodic memory (specific past events/sessions)
**Substrate:** auto memory's `MEMORY.md` + topic files (`debugging.md`, `api-conventions.md`, `build-commands.md`, arbitrary others Claude creates) at `~/.claude/projects/<project>/memory/`; also raw session transcripts (reachable via `/resume`) and git commit history when the agent commits as it works.

**Write path:** Claude writes autonomously, mid-session, whenever it judges something "would be useful in a future conversation" — no fixed cadence, no user action required (visible in the UI as "Writing memory"). Trigger examples from docs: user corrections ("always use pnpm, not npm"), discovered build commands, debugging insights. This is genuinely **agent-judged salience**, not a scripted extraction pipeline.

**Injection/recall:** first 200 lines *or* 25KB of `MEMORY.md` (whichever comes first) loads into every session automatically, before the first turn. Topic files beyond that are **not** auto-loaded — Claude reads them on demand with ordinary file tools if it navigates there. This is agentic re-discovery, not vector/semantic retrieval — there is no native embedding index over past sessions.

**Consolidation/reflection:** "Auto Dream" (see caveat in §1) is the only native reflection pass, if genuine: 24hr + 5-session dual-gate trigger, four phases (orient → gather signal from session transcripts → consolidate: merge overlaps, resolve contradicted facts, absolute-date relative dates, drop stale entries → prune/reindex `MEMORY.md` under 200 lines). Read-only on project code; lockfile-guarded against concurrent runs; one reported run processed 913 sessions in ~8-9 minutes. Absent Auto Dream, there is **no other native consolidation** — `MEMORY.md` grows by accretion until the write-time nudge (v2.1.210+) or hard error (over-limit write still succeeds; everything past the limit silently stops loading).

**Decay/supersession:** survives `/compact` (re-injected from disk, per the table above). Machine-local — `~/.claude/projects/<project>/memory/` keys off the git repo, shared across worktrees of the same repo, but **not synced across machines or team members** (see §4 sentiment). No native expiry; only Auto Dream (if active) prunes stale entries, otherwise it's edit-forever via `/memory`.

### Semantic memory (general facts/rules about the codebase, world, conventions)
**Substrate:** CLAUDE.md hierarchy (human-authored) is the primary semantic store; auto memory's consolidated topic files (post-Auto-Dream, if active) are the agent-authored counterpart. `.claude/rules/` provides path-scoped semantic fragments (e.g., "API endpoints must include input validation" — only relevant when touching `src/api/**`).

**Write path:** CLAUDE.md is entirely human-written (or human-approved via `/init`'s reviewable-proposal flow). `/doctor` (v2.1.206+) proposes trims — cutting content Claude can re-derive from the codebase (directory layouts, dependency lists) while keeping pitfalls/rationale/non-default conventions. Auto memory topic files are Claude-authored per the episodic write path above; the distinction between "episodic note" and "semantic fact" isn't structurally enforced — it's a product of what Auto Dream consolidates over time.

**Injection/recall:** CLAUDE.md and unscoped rules load **in full at every session launch**, concatenated root-to-leaf (broadest scope first: managed policy → user → project → local; within the directory tree, ancestor directories before the working directory; `CLAUDE.local.md` appended last within each level). Nested CLAUDE.md files in subdirectories load lazily, only when Claude reads a file in that subdirectory. `.claude/rules/` without `paths:` frontmatter loads unconditionally at launch like `.claude/CLAUDE.md`; path-scoped rules load only when a matching file is touched. `@path` imports (max depth 4) expand at launch. `AGENTS.md` is not natively read — Claude Code reads `CLAUDE.md` only; interop is via `@AGENTS.md` import or symlink.

**Consolidation/reflection:** none automatic for CLAUDE.md — it is explicitly a human-maintained artifact. Anthropic's own guidance (first-party, and independently corroborated by the internal KB finding `catastrophic-context-collapse-risk-during-claudemd.md`) is: **never ask Claude to summarize/compact CLAUDE.md itself** — doing so carries a small, cumulative, per-attempt probability of "catastrophic rewrite," collapsing the file to ~100-200 tokens and dropping post-collapse accuracy to ~57% of pre-collapse performance (below the no-CLAUDE.md baseline). `/doctor`'s trim proposal is the sanctioned alternative — deterministic, reviewable, derivation-aware rather than a blind summarize pass.

**Decay/supersession:** project-root CLAUDE.md and unscoped rules survive `/compact` (re-injected from disk). No size cap is enforced — Claude Code will load an arbitrarily long CLAUDE.md — but adherence degrades past ~200 lines (first-party recommendation, soft not hard). Managed-policy CLAUDE.md cannot be excluded by any downstream setting; project/user CLAUDE.md can be selectively excluded via `claudeMdExcludes` in monorepos.

### Procedural memory (how to do things — skills, workflows)
**Substrate:** Skills (`SKILL.md`, invoked on demand, not loaded at launch), hooks (`settings.json`-defined, run as shell code at lifecycle events — `SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`, `PreCompact`, etc.), slash commands.

**Explicitly not natively handled:** Claude Code has **no native mechanism for auto-memory to graduate into a skill.** Auto memory captures *what Claude learned*; skills encode *how to do a repeatable task*; nothing in the shipped harness converts the former into the latter. (This gap is exactly what the internal KB finding `memory-file-to-skill-migration.md` and IL's own `/self-improve` promotion pipeline exist to backfill — external practice, not native Claude Code behavior.) Hooks are the one genuinely deterministic procedural-memory surface: they are code, not context, so they are immune to compaction/decay by construction (per the survives-compaction table: "Hooks — Not applicable; hooks run as code, not context").

**Write path:** skills and hooks are entirely human-authored (or human-approved via `/init`'s multi-phase flow, which can propose skills alongside CLAUDE.md and hooks).

**Injection/recall:** skills load on invocation, not at launch — either explicit (`/skill-name`) or when Claude determines relevance from the prompt. Post-`/compact`, invoked skill bodies are re-injected but truncated (5,000 tok/skill, 25,000 tok total budget, oldest dropped first, truncation preserves the file's start — so front-load the important instructions in `SKILL.md`).

**Consolidation/decay:** none native — skills don't self-prune or self-merge. This is squarely a human-governed artifact, same posture as CLAUDE.md.

---

## 3. Lifecycle trace — one auto-memory item, end to end

1. **Session A, mid-conversation.** Nick tells Claude "always use pnpm, not npm." Claude judges this durable-future-value and writes it to `~/.claude/projects/<project>/memory/MEMORY.md` (or a topic file) *during* the session — visible in the UI as "Writing memory." No user action beyond the correction itself triggers the write; no explicit "remember this" command is required (though asking directly works too, per docs: *"remember that the API tests require a local Redis instance"* → auto memory).
2. **Budget check (v2.1.210+).** After the write, Claude Code measures `MEMORY.md` against the 200-line/25KB cap. If near the limit, Claude gets a soft reminder to shorten (one line per entry, push detail to topic files, merge/drop stale entries). If over the limit, the write still succeeds but Claude Code returns an error telling Claude to rewrite the index — because everything past the limit silently stops loading on the next session.
3. **Mid-session compaction (if it fires).** If Session A itself runs long enough to hit `/compact` (proactive or automatic), auto memory is **re-injected from disk** afterward — it survives, unlike path-scoped rules or nested CLAUDE.md.
4. **Session A ends.**
5. **Background consolidation window (if Auto Dream is active — unconfirmed first-party, see §1).** Once 24 hours have elapsed *and* 5+ sessions have accumulated, a background pass re-reads recent session transcripts, merges the pnpm note with any related entries, resolves it against contradicting notes if the preference changed, converts any relative dating, and rewrites the index — read-only on project code, lock-guarded against concurrent runs.
6. **Session B starts**, possibly days later, same git repo (any worktree — auto memory is keyed to the repo, not the directory). Before the first turn, Claude Code loads the first 200 lines/25KB of `MEMORY.md` automatically, alongside CLAUDE.md, system prompt, and environment info.
7. **Recall.** Claude sees "use pnpm, not npm" already in context and acts on it without Nick re-stating the correction — the compounding-improvement mechanism the docs describe.
8. **On-demand deep recall.** If more detail lives in a topic file beyond the 200-line cutoff, Claude only sees it if it actively reads that file via standard file tools during Session B — there is no automatic semantic search pulling it in; discovery is agentic, not retrieval-triggered.
9. **Auditability.** At any point, Nick can run `/memory` to browse/edit/delete the raw markdown, or `/context` to see exactly what loaded into the current session's budget.

---

## 4. Practitioner sentiment (dated)

**Auto memory doesn't sync across team/machines — 2026-04-14** (kumaran srinivasan, Medium, "Claude Code Has Memory Now. Here's What It Still Can't Do"): *"Auto Memory lives in `~/.claude/`. It's not in the repo. It doesn't sync across machines."* Consequence: corrections made on one dev's machine are invisible to teammates cloning the repo — everyone re-teaches the same lessons. Also flags no survival across machine wipes, no CI/CD applicability (it requires a human catching errors in the loop), and Auto Dream (if enabled) as opaque — no audit trail for code review. Proposed workaround: a hand-maintained `lessons.md` at the *repo* layer (team-visible, versioned) as a deliberate escalation path out of machine-local auto memory.

**Subagents don't share memory — 2026-05-06** (Hindsight/vectorize.io blog): *"every subagent invocation starts fresh"* — knowledge stays siloed per subagent *name*, and a subagent's entire exploration trail (rejected approaches, intermediate findings) vanishes once only its final summary returns to the parent. Concrete failure modes cited: sequential Explore agents re-grep the same files; parallel subagents independently rediscover the same architectural quirk requiring manual reconciliation; a custom code-reviewer subagent re-flags patterns the team already rejected across multiple PRs. This directly corroborates the internal KB finding `subagent-persistent-memory-directory.md`'s own listed failure mode ("cross-subagent memory sharing" as an unmet need) — two independent sources, same gap, ~2 weeks apart.

**Compaction is the most complained-about mechanism — spans 2025-12 through 2026-05.** Representative dated claims:
- **2025-12-10** (Robert Matsuoka, hyperdev.matsuoka.com): documents Anthropic quietly tightening the automatic-compaction trigger from ~90%+ to ~75% utilization specifically because *"Claude performs much worse when the context window approaches its limit"* — an infra fix predating the April product-blog guidance that made the same point explicit and user-facing.
- **2026-03-18** (bytebell.ai): user quote, *"Auto compact is the worst. Every time it happens I feel like Claude Code has forgotten everything."* Documents concrete degradation: post-compaction the agent forgets exact file:line references and the debugging hypothesis chain, degrading progressively across repeated compactions until it edits wrong files. Workarounds recommended: manual `/compact` with preservation hints before auto-fires, frequent git commits as an external durability layer, fresh sessions per distinct task, staying under 50% utilization before considering compaction.
- **GitHub issue #33026**, `anthropics/claude-code` (undated in search results but active in 2026): feature request — *"Allow Claude to self-initiate context compaction"* — practitioner demand for the model to trigger proactive compaction itself, which is precisely what Anthropic's 2026-04-15 blog recommends humans do manually; the request suggests the tooling hadn't yet closed that loop as of filing.
- One Medium account (Coding Nexus, undated precisely, 2026) reports a developer who rebuilt lost context 40+ times before adopting a file-based persistence workaround, at ~20 min/rebuild — over 13 hours of pure rework attributed to compaction loss.

**CLAUDE.md bloat / context rot — ongoing through 2026, no single fix date.** Aggregate 2026 reporting (Towards Data Science, "Governed Context") frames context rot as *"the single most common cause of perceived quality drops"* in Claude Code sessions. Concrete cost example cited (March 2026 reports): $200/month-plan users watching 5-hour usage windows exhausted in 90 minutes when skill/rule bloat inflates every-turn token cost. A separate report: 160 registered skills eating ~25K tokens/call could waste ~1.25M tokens in one session, with skills never invoked in 56% of evaluated test cases (Vercel eval) — an efficiency complaint adjacent to, not strictly about, memory, but it shapes how practitioners think about what belongs in always-loaded context vs on-demand skills.

**What's working, per the same sources:** the 2026-04-15 five-tool matrix (Continue/rewind/compact/clear/subagent) is broadly treated as the new canonical vocabulary — cited approvingly and reused verbatim across multiple 2026 blogs rather than disputed. The survives-compaction guarantee for project-root CLAUDE.md and auto memory (re-injection from disk) is the mechanism practitioners lean on as the *fix* for compaction loss — "put it in CLAUDE.md/auto-memory, not just conversation" is the recurring prescriptive advice across the bytebell.ai (2026-03-18) and Coding Nexus pieces.

---

## 5. Verdict

**Strengths (lean on these):**
- **File-as-substrate, not black box.** Every native memory surface (CLAUDE.md, auto memory, subagent memory) is plain markdown on disk, editable/deletable/auditable via `/memory`, and version-controllable at project scope. This is a strong match for MetaSystem's own governance posture (frontmatter-as-source-of-truth, no opaque DB) and for the "files as source of truth, memory tools as accelerators" principle already in the KB (`three-scope-memory-files-as-source-of-truth.md`).
- **The survives-compaction table is a real, load-bearing guarantee**, not a marketing claim — project-root CLAUDE.md and auto memory are structurally protected from the harness's own lossiest operation. An engine built on Claude Code should treat "durable = root-level CLAUDE.md or auto-memory-scoped file" as a hard design rule, and treat anything conversation-only or path-scoped-rule-only as ephemeral by construction.
- **Subagent `memory:` scoping (user/project/local)** maps almost directly onto the IL engine's own agent taxonomy (Owner/Researcher/Codifier/Librarian) — each could plausibly get a `project`-scope memory directory today, zero-cost, no new infrastructure.
- **Proactive-compaction guidance is now first-party and explicit**, giving the engine a concrete operational rule to inherit rather than invent: compact at a stable checkpoint with a steering hint, never let the hard cutoff decide.
- **Hooks are compaction-immune by construction** (code, not context) — the correct place to put anything the engine needs to survive *unconditionally*, including memory capture/injection logic itself (the KB's `hook-based-transparent-memory-injection.md` and `claude-code-hooks-for-automatic-session-memory.md` findings describe exactly this pattern, external to Claude Code but built entirely on native hook primitives).

**Failure modes (work around these):**
- **No team/machine sync, by design.** Auto memory is explicitly machine-local, keyed to the git repo. For a multi-session, potentially multi-machine engine (Nick's actual usage pattern), this means auto memory alone cannot be the durable layer for anything that must be shared — it has to be treated as a *personal scratch cache*, with the repo's own governed files (DDs, PROGRESS.md, HISTORY.md) as the actual source of truth, exactly as the workspace's existing Process Rule 2 already assumes for PROGRESS.md. This is independent confirmation, not new information — but it's now dated and sourced (2026-04-14).
- **No native semantic retrieval over episodic history.** Beyond the 200-line/25KB `MEMORY.md` window, recall is agentic file-reading, not embedding search. An engine that wants "what did we learn about X three months ago" needs its own indexing layer on top (KB findings already flag this design space — `verbatim-storage-thesis-for-memory.md`, `mongodb-single-store-polymorphic-evidence-memory.md` — this survey confirms Claude Code itself supplies none of it natively).
- **Subagent memory is siloed and unshared**, both by first-party design and independently confirmed by practitioner complaint (2026-05-06). Any engine plan that assumes subagents pool learnings needs an explicit cross-subagent handoff mechanism (file-mediated, per the existing `file-mediated-subagent-handoff-workspace.md` finding) — Claude Code will not do this for you.
- **"Auto Dream" is not solid ground.** Given the absence from first-party docs fetched today, do not design any load-bearing engine mechanism around Auto Dream existing, being stable, or behaving as third-party blogs describe. If genuine, it's a bonus; if a design needs guaranteed consolidation, build it explicitly (this is exactly what `/self-improve`'s scan mode already does, independent of the harness).
- **Compaction remains the sharpest edge.** Even with proactive guidance and the survives-compaction table, in-conversation-only reasoning (the "why," not just the "what") is lost at every compaction, confirmed by both the first-party docs (implicitly — only specific mechanisms are re-injected, not general reasoning) and heavy 2026 practitioner complaint volume. Anything the engine needs Claude to *reason about consistently across a compaction boundary* — not just *recall as a fact* — has to be written down as a fact/rule (CLAUDE.md, memory, or a DD), not left as accumulated conversational inference.

**Bottom line for E1:** build the engine's durable memory on the native file surfaces (CLAUDE.md hierarchy, auto memory, subagent `memory:` scopes, hooks) rather than around them — they're free, compaction-resilient by design where it matters, and already governance-compatible. Reserve custom infrastructure for exactly the three gaps Claude Code doesn't cover natively: cross-machine/team sync, semantic retrieval over episodic depth, and cross-subagent knowledge pooling.
