# Design-Question Checklist: Agent "Second Brain" (Persistent Learning/Memory Store)

*(Reconstructed verbatim from session-142 context after scratchpad rotation; original written 2026-07-12. Companion deep-dive: `2026-07-13-memory-architecture-deepdive-web.md`.)*

Research date: 2026-07-12. Grounded in frontier practitioner systems and papers, 2025-2026: Hermes Agent, OpenClaw (Dreaming → MEMORY.md), Gbrain, OKF v0.1, Anthropic memory tool / Claude Code auto-memory / claude-mem, MemGPT/Letta (context repositories, sleep-time compute), Mem0, A-MEM, LongMemEval, ACE (Agentic Context Engineering), and "second brain for agents" discourse (timetobuildbob, Tony Xu, PARA/Zettelkasten-for-agents).

Framing: questions are ordered so the first block discriminates **build vs. don't-build**; the second block covers **write path**; the third **read path**; the fourth **lifecycle and safety**. Each question has a one-line "why," a source pointer, and the frontier's convergent answer pattern where one exists.

---

## Part 1 — Design questions

### A. Build vs. don't-build discriminators

**Q1. What concrete, observed failure would this store have prevented — can you name three incidents?**
- Why: memory stores built speculatively become write-only graveyards; the frontier builds against measured failure classes (info extraction, knowledge updates, temporal reasoning, abstention), not vibes.
- Source: LongMemEval defines exactly these five failure classes and shows even GPT-4o-class systems drop 30–60% on them (arxiv.org/abs/2410.10813; xiaowu0162.github.io/long-mem-eval).
- Convergent answer: build only for the failure class you can demonstrate; benchmark-driven design. If you can't name the incidents, the answer is "don't build yet."

**Q2. Who reads it, and what is the retrieval trigger? Name the exact moment in the workflow.**
- Why: unread memory is functionally identical to no memory — the read path, not the write path, is where stores die.
- Source: Anthropic memory tool ("Claude checks its memory directory before starting a task", platform.claude.com/docs/.../memory-tool); Letta injects memory-count metadata into prompts to trigger agent-initiated search (letta.com/blog/context-repositories).
- Convergent answer: just-in-time, task-triggered reads (session start injection for a small pinned layer + on-demand tool search for the rest). If no workflow step names the read, don't build the store.

**Q3. Is git history + existing artifacts already the memory? What question can't be answered by grep + git log + your current routed stores?**
- Why: for markdown/git systems, git already provides a versioned, append-only episodic record for free; a new store must beat "free."
- Source: Letta Code makes git-backed context repositories the memory substrate — "every change to memory is automatically versioned with informative commit messages" (letta.com/blog/context-repositories); OKF: knowledge is "just markdown, just files" in a git repo (github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md); timetobuildbob: "use git so changes stay visible and reversible."
- Convergent answer: files + git IS the episodic layer for file-based systems. A new mechanism is justified only for what git can't answer: aggregation across sessions (calibration measurements, sparse telemetry, recurrence counts) — things that need to be *tallied*, not *found*.

**Q4. What is the curation cost per week, and who pays it? Is that sustainable at your scale, forever?**
- Why: neglected curation is the default outcome; stores degrade into graveyards or drift unless someone (human or scheduled agent) owns upkeep.
- Source: Letta ships dedicated defragmentation/reflection subagents precisely because manual curation doesn't scale (letta.com/blog/context-repositories); OpenClaw makes Dreaming opt-in-with-cron for the same reason (docs.openclaw.ai/concepts/memory).
- Convergent answer: either automate curation (scheduled consolidation pass) or cap the store so hard that curation is trivial. For a single operator, the hard cap is cheaper than the machinery.

**Q5. What is the kill criterion — how will you know in 90 days whether the store earned its keep?**
- Why: retrieval-hit telemetry is the only honest measure; "feels useful" is how graveyards persist.
- Source: OpenClaw's promotion gates (minRecallCount, minUniqueQueries) double as usage telemetry — entries must *prove* recall value (mem0.ai/blog/openclaw-vs-hermes-agent-memory-comparison); WorkOS recommends logging retrieval patterns for weeks before trusting the store (workos.com/blog/ai-agent-memory-poisoning).
- Convergent answer: track reads per entry; entries never retrieved in N sessions get pruned; a store whose entries are never retrieved gets deleted. Decide N before building.

### B. Write path

**Q6. Where does the write happen — inline during work, or in a scheduled offline pass?**
- Why: inline curation taxes every session (friction → nothing gets written, or noise gets written); offline consolidation is the frontier's answer to both.
- Source: Letta sleep-time compute (letta.com/blog/sleep-time-compute); OpenClaw Dreaming runs as a cron-managed background sweep, disabled by default (docs.openclaw.ai/concepts/memory); claude-mem does capture via non-blocking hooks + compression at SessionEnd (docs.claude-mem.ai/hooks-architecture).
- Convergent answer: capture is automatic and low-friction (hooks, daily logs, transcripts already exist); *promotion to durable memory* is a separate, scheduled, reviewable pass. Never make the working agent curate long-term memory mid-task.

**Q7. What must an entry earn to be promoted from episodic capture to durable memory?**
- Why: without promotion gates you get one of two bad outcomes — everything lands in memory (bloat/noise) or nothing does (loss).
- Source: OpenClaw Deep Sleep requires all three gates: composite score, recall frequency (minRecallCount), and query diversity (minUniqueQueries) — "it earns its way in" (docs.openclaw.ai/concepts/memory; youtube.com/watch?v=CwCu8UnQukk).
- Convergent answer: promotion requires *demonstrated repeated relevance across distinct contexts* — i.e., recurrence evidence, not single occurrence. Raw episodes are disposable once distilled.

**Q8. Episodic vs. semantic: which layer is append-only raw, which is the curated distillate, and what process moves material between them?**
- Why: systems relying only on raw logs don't scale; systems storing only summaries lose provenance and detail — every frontier system splits the two.
- Source: OpenClaw `memory/YYYY-MM-DD.md` (working layer, searchable, not injected) vs `MEMORY.md` (curated, injected at session start) (docs.openclaw.ai/concepts/memory); MemGPT recall/core/archival split (Letta docs); timetobuildbob: "journal should be append-only and chronological; the knowledge base should be curated and synthesized."
- Convergent answer: two layers minimum — disposable append-only episodic capture + small curated semantic layer — with a scheduled distillation step between them. Most systems distill episodic→semantic on a schedule; raw episodes decay or archive.

**Q9. What is the size budget of the always-loaded layer, and what enforces it?**
- Why: the cap is the curation-forcing function; unbounded pinned memory is a per-session token tax that grows forever.
- Source: Hermes hard-caps MEMORY.md at 2,200 chars (~800 tokens) and USER.md at 1,375 (hermes-agent.nousresearch.com/docs/.../memory); Claude Code auto-memory loads only the first 200 lines / 25KB of MEMORY.md (code.claude.com/docs/en/memory); OpenClaw truncates the injected copy past its bootstrap budget.
- Convergent answer: hard cap the pinned layer (hundreds of tokens to low-thousands); overflow forces triage into on-demand topic files. Character caps beat token caps (model-independent).

**Q10. When a stored fact changes, do you append, replace, or version — and who reconciles contradictions?**
- Why: append-only fact stores accumulate contradictions → stale-memory drift, the most common non-adversarial failure.
- Source: MemGPT core memory has explicit `replace` semantics ("James is the boyfriend" → "ex-boyfriend" example, Letta); Gbrain's "compiled truth + timeline" — current judgment at the top, immutable evidence timeline below (100user.com/blog/gbrain-open-source-second-brain-ai-agents); LongMemEval "knowledge updates" is a named failure category.
- Convergent answer: replace-in-place for current facts, with the history preserved elsewhere (git, timeline section). Separate conclusions from evidence.

**Q11. How are updates applied — targeted deltas or whole-store rewrites?**
- Why: asking an LLM to rewrite accumulated memory causes *context collapse* (documented: 18,282 tokens → 122 tokens in one rewrite step, accuracy 66.7% → 57.1%) and *brevity bias* (compression strips the domain detail that made entries useful).
- Source: ACE paper (arxiv.org/abs/2510.04618) — incremental delta updates merged deterministically, itemized bullets with helpful/harmful counters; Mastra's LongMemEval work found whole-memory rewrites introduced errors vs targeted updates (youtube.com/watch?v=FTokJt1ioeg).
- Convergent answer: itemized entries + incremental delta edits, merged by deterministic logic (not LLM rewrite). Never hand the whole store to a model for "cleanup" in one shot.

**Q12. What is the atomic unit and its minimum metadata?**
- Why: prose blobs can't be tallied, deduplicated, expired, or scored; structure is what makes lifecycle mechanics possible.
- Source: OKF v0.1 requires exactly one frontmatter field (`type`) per concept file — the deliberately minimal contract (github.com/GoogleCloudPlatform/knowledge-catalog); ACE bullets carry utility counters; A-MEM notes carry tags/keywords/links (Zettelkasten atomic-note principle).
- Convergent answer: one small entry per fact/observation, YAML frontmatter with type + timestamp + provenance at minimum. Markdown-with-frontmatter is the 2026 lingua franca (OKF, OpenClaw, Hermes, Claude Code all converge here).

### C. Read path

**Q13. Does the agent need mid-session freshness, or is a session-start snapshot enough?**
- Why: this is a real fork with real costs — re-injecting memory every turn invalidates prompt-prefix caching; frozen snapshots mean the agent can't see what it just wrote.
- Source: Hermes deliberately freezes memory at session start to preserve prefix cache (glukhov.org/.../hermes-agent-memory-system); OpenClaw re-injects MEMORY.md every turn for immediate visibility — two coherent opposite answers (mem0.ai/blog/openclaw-vs-hermes-agent-memory-comparison).
- Convergent answer: session-start snapshot is the default; pay the freshness cost only if you have a demonstrated within-session recall need.

**Q14. What retrieval mechanism is proportional to store size — and at what size does grep stop working?**
- Why: index infrastructure (embeddings, hybrid search, worker daemons) is a standing cost; small stores don't need it.
- Source: OpenClaw uses hybrid BM25+vector only over the large daily-notes layer (gaodalie.substack.com/p/i-studied-openclaw-memory-system); claude-mem runs a resident worker + SQLite + Chroma — criticized as ~80–150MB RAM + API calls per session for what a 47ms local function can approximate (dev.to/zzallirog/what-i-learned-building-memory-for-claude-code...).
- Convergent answer: below a few hundred entries, plain file reads + ripgrep beat any index. Add search infrastructure only when files stop fitting in a read. "Search first, then inject" replaces "load everything" only at scale.

**Q15. What happens when memory is wrong, stale, or missing — does the agent verify or trust?**
- Why: memory treated as authority amplifies staleness; LongMemEval's "abstention" category and PersistBench's 97% memory-induced-sycophancy rate show models over-trust their stores.
- Source: LongMemEval abstention task (arxiv.org/abs/2410.10813); PersistBench (Feb 2026): median 53% cross-domain leakage, 97% memory-induced sycophancy (liveinthefuture.org/stories/sleeper-memory-poisoning-ai-agents-permanent-corruption); Tony Xu's read protocol: "check source exports if the note may be stale; answer with uncertainty if the evidence is thin" (tonyxu.io/blog/my-second-brain-setup).
- Convergent answer: memory is a hint, never an authority — for consequential actions, verify against the source of truth (the repo, the file, the live system). Design the store so entries point back to their evidence.

### D. Lifecycle and safety

**Q16. What decays, on what schedule, and what is exempt?**
- Why: a store where nothing expires becomes a graveyard by construction; stale entries actively mislead (agent confidently uses a preference you changed months ago).
- Source: Mem0 platform `expiration_date` per memory; LangGraph store TTL with `refresh_on_read`; AWS AgentCore tiered `eventExpiryDuration`; OpenClaw deep-sleep half-life/max-age aging (dev.to/sudarshangouda/ai-agent-memory-part-2-the-case-for-intelligent-forgetting-4i48; crewclaw.com/blog/openclaw-memory-dreaming-explained).
- Convergent answer: tiered decay — durable rulings/preferences near-immortal, observations and measurements time-boxed; usage refreshes lifetime (spacing effect). Decide the TTL per entry *type* at design time.

**Q17. Can you tell where each entry came from — and are observations distinguishable from instructions?**
- Why: entries derived from untrusted or generated content that read like instructions are the poisoning vector; even single-operator systems ingest web content, transcripts, and their own agent's speculative output.
- Source: MemoryGraft — poisoned "successful experiences" planted via ordinary docs, retrieved and imitated weeks later (arxiv.org/html/2512.16962v1); OpenClaw's own bug where Dreaming wrote raw undistilled candidates into MEMORY.md and re-ingested them (github.com/openclaw/openclaw/issues/67580); Microsoft AI failure-mode taxonomy names memory poisoning as needing write validation (microsoft.com/en-us/security/blog/2025/04/24/...).
- Convergent answer: provenance field per entry (source + date); generated/derived content lands in a lower-trust staging area and is promoted only after review; behavioral instructions and factual observations never share a bucket.

**Q18. What is the scope boundary — one global store or per-project partitions?**
- Why: cross-context bleed is a measured failure (PersistBench: 53% median cross-domain leakage) and a privacy hazard.
- Source: Anthropic per-project memory in Claude (simonwillison.net/2025/Sep/12/claude-memory/); Claude Code memory is scoped per git-repo root (code.claude.com/docs/en/memory).
- Convergent answer: scope memory to the project/system boundary; global stores are for identity/preferences only. (A single-operator single-engine system gets this almost for free — but keep operator-prefs separate from engine-learnings.)

---

## Part 2 — Where the frontier converges (summary of answer patterns)

1. **Two layers, scheduled distillation.** Append-only episodic capture (daily logs / transcripts / git) + a small curated semantic layer loaded at session start. Distillation runs on a schedule (Dreaming, sleep-time compute, session-end hooks), never inline. Raw episodes are disposable.
2. **Promotion is earned.** Entries reach durable memory via recurrence/recall evidence (OpenClaw's three gates), not on first occurrence.
3. **The pinned layer is hard-capped.** 800–2,000ish tokens (Hermes 2,200 chars; Claude Code 200 lines). The cap forces curation; overflow goes to on-demand topic files.
4. **Deltas, never rewrites.** Itemized entries updated incrementally with deterministic merges (ACE). Whole-store LLM rewrites cause context collapse and brevity bias.
5. **Files + git + frontmatter is the substrate.** Markdown with YAML frontmatter, one required `type` field, versioned in git (OKF, OpenClaw, Hermes, Claude Code, Letta context repos). Databases/vectors are an acceleration layer added later, not the source of truth.
6. **Replace facts, keep timelines.** Current judgment at top, evidence appended below (Gbrain); explicit replace semantics for changed facts (MemGPT).
7. **Reads are just-in-time and measured.** Session-start snapshot + on-demand search; retrieval hits are telemetry that drives both promotion and pruning.
8. **Forgetting is designed in.** Tiered TTL/decay by entry type; refresh-on-read; nothing is immortal by default except rulings.
9. **Memory is a hint, not an authority.** Verify against sources for consequential actions; label provenance; stage generated content before promotion.

---

## Part 3 — Documented failure stories (≤5)

1. **OpenClaw Dreaming feedback loop (2026).** Dreaming promotion wrote raw, undistilled candidate data straight into MEMORY.md; that output flowed back into memory sources and was re-ingested, degrading memory quality — the system's own consolidation pass poisoned its long-term store. Source: github.com/openclaw/openclaw/issues/67580.
2. **MemoryGraft + MINJA (Dec 2025 / NeurIPS 2025).** MemoryGraft planted fabricated "successful experiences" via a benign-looking README; weeks later the agent retrieved and imitated the malicious pattern as its own proven playbook. MINJA achieved >95% injection success against production agent architectures using only normal queries — no memory-store access needed. Sources: workos.com/blog/ai-agent-memory-poisoning; arxiv.org/html/2512.16962v1.
3. **ChatGPT "spAIware" (Sept 2024, Rehberger).** Persistent prompt injection written into ChatGPT's long-term memory survived across sessions, devices, and account restarts because memory was stored server-side — the canonical proof that memory persistence extends attack persistence. Source: summarized with follow-ups at liveinthefuture.org/stories/sleeper-memory-poisoning-ai-agents-permanent-corruption.
4. **Procurement-agent memory poisoning (2025, Lares Labs).** Over three weeks, a manufacturing firm's procurement agent was gradually memory-poisoned into believing elevated transfer limits were authorized, then transferred funds to attacker accounts — gradual drift, not a single exploit. Source: github.com/h5i-dev/awesome-ai-agent-incidents.
5. **Context collapse + assistant overwrite drift (2025).** ACE documented an agent's accumulated context collapsing from 18,282 tokens (66.7% accuracy) to 122 tokens (57.1%) in a single LLM rewrite step; LongMemEval separately found ChatGPT "tends to overwrite crucial information as the number of interaction sessions increases," with commercial assistants dropping 30–60% accuracy over sustained histories — the non-adversarial way stores rot. Sources: arxiv.org/abs/2510.04618; arxiv.org/abs/2410.10813.

(Related graveyard evidence, non-incident: claude-mem's always-on capture stack — 5 resident hook processes, ~80–150MB RAM, per-session API calls — is the community's cautionary example of write-path cost outrunning read-path value for small projects: dev.to/zzallirog/what-i-learned-building-memory-for-claude-code-measured-against-the-popular-alternative-25o.)
