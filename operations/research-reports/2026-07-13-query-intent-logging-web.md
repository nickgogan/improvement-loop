# Query/Intent Logging with Unserved-Intent Review — Web Sweep (Session 142)

Research date: 2026-07-13. Perplexity deep-research pass, distilled. Question: which
systems log incoming queries + routing decision + served/unserved outcome and mine the
log for coverage gaps — and what is the minimal persistence mechanism for a local-first,
solo-operator Claude Code system? Input to
`project-management/design-notes/2026-07-13-memory-system-design.md` §3–§4 (demand
ledger). Raw full-length report was session-scoped; this distillation is the durable
record.

---

## 1. Precedent — three lineages, none in our exact class

**Conversational-AI platforms (oldest, most exact match).** Rasa conversation-driven
development / NLU inbox: every utterance logged with predicted intent + confidence;
fallback/low-confidence utterances land in a review queue; humans periodically decide
"add a new intent or improve training data." Dialogflow unmatched-intent analytics:
dashboards of messages matching no intent, with recurring-phrase candidates. Site-search
**zero-result-query mining** (Algolia et al.): a zero-result query = an unserved intent;
reports drive content/inventory expansion. Core logged triple everywhere: query text ·
attempted intent/route · served-vs-fallback outcome, with optional "why."

**Agent observability, 2024–26 (org-scale, cloud).** Datadog ships Claude Code skills
against its LLM-observability product — `/agent-observability-session-classify`
(labels whether user intent was satisfied per session/trace) and
`/agent-observability-trace-rca`, in a six-phase classify → RCA → evaluator-bootstrap →
dataset → experiment loop (docs.datadoghq.com/llm_observability/guide/claude_code_skills).
LangSmith Engine clusters production failures, diagnoses causes, proposes fixes and
evaluators. Arize frames each query as a trace of spans with attached evaluations.
Internalnote's "AI Agents Advanced": multi-intent messages are decomposed and **each
resolved intent is counted separately in reporting** — the analysis unit is the intent,
not the message. All cloud, all multi-tenant.

**Our class (local-first, markdown/git, solo).** No complete implementation found —
components only: **claude-mem / claude-mem-lite** capture via Claude Code hooks into
local SQLite as *distilled observations, not transcripts* (search → inspect IDs → fetch;
FTS5 + vectors); **Gbrain** writes timestamped markdown *reports* into the vault as the
reviewable artifact, indexed by a derived retrieval layer; **semantic-router**
(aurelio-labs) supplies route + similarity-score vocabulary; and CareerBuddy's
`eval-candidates.md` (already in the KB) logs real invocation phrasings + verdicts.
The full query→route→outcome→review loop at solo scale is a genuine gap — a
compose-known-parts build, and a KB-finding candidate in its own right.

## 2. Minimal persistence in Claude Code specifically

- **Transcripts already exist free**: append-only session JSONL under
  `~/.claude/projects/<encoded-dir>/` (Willison, 2025-10). But schema is undocumented
  and unstable (anthropics/claude-code#53516 requests a stable schema; external tools
  file-watch it as their only channel), files grow to hundreds of MB, and retention is
  cleanup-bounded. Verdict: backfill/troubleshooting source, not the store. Hermes-style
  deliberate full persistence would duplicate this.
- **Hooks are the robust capture path**: a `UserPromptSubmit` hook writes one structured
  line per prompt (deterministic, no LLM, no per-session friction); outcome annotation
  happens later (session-end hook or scheduled distillation). This is the
  claude-mem-lite pattern minus its machinery (5 resident processes, ~80–150MB RAM —
  the community's write-cost-outruns-read-value cautionary example).
- **OTel integration** exists for org deployments; overkill solo, but confirms Claude
  Code is instrumented for prompt/tool event emission.
- **Distillation over retention**: the converged pattern is capture-buffer → scheduled
  distill into compact structured rows; raw capture is disposable.

## 3. Schema convergence (per intent, not per message)

timestamp · session id · stable row id · query text/gist · route (skill/tool name) ·
confidence/score where routing is automated · one-line rationale ("why this route") ·
outcome (served / partial / fallback / error — fallback≠error: coverage gap vs
robustness bug) · optional latency/tokens. Multi-intent messages → one row per intent.

## 4. Review-loop mechanics and failure modes

What makes the loop actually run: review embedded in an existing workflow (a skill the
operator already runs on cadence), thresholds linking log → action ("theme at ≥N
unserved → build/route-fix decision"), and reports written into the same knowledge base
as everything else (Gbrain pattern) so they're discoverable. Failure modes: the
log-nobody-reads graveyard (worst and most common — mitigated by giving the log a named
consumer and no private reflection ritual); noise (log user queries only, not internal
steps or clarifying turns); schema fragility (own your schema via hooks; don't parse
undocumented transcript JSONL); privacy (gists over full text where sensitive; local
only).

## 5. Application (as adopted in the design note)

Demand ledger `operations/self/query-log.md` (`Q-<seq>` rows), gitignored
`UserPromptSubmit` capture buffer, distilled by the self-improve skill's scan mode in
the same retro that reads lessons/feedback; unserved themes at threshold → IB proposals
through the promotion gate; ledger doubles as the ground-truth corpus (phrasing → route
→ outcome) for the future implicit-routing harness eval set.

Key sources: docs.datadoghq.com/llm_observability/guide/claude_code_skills ·
simonwillison.net/2025/Oct/22/claude-code-logs · anthropics/claude-code#53516 ·
github.com/sdsrss/claude-mem-lite · docs.claude-mem.ai/troubleshooting ·
github.com/aurelio-labs/semantic-router · vectorize.io/articles/what-is-gbrain ·
internalnote.com/multiple-intent-handling-for-ai-agents-advanced ·
code.claude.com/docs/en/hooks · arize.com/blog/llm-observability-for-ai-agents-and-applications
