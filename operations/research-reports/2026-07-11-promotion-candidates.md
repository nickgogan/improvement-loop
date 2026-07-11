# Promotion Candidates — omnigent + opencode analyses (Session 131)

Dedup-checked candidate table from `/promote-findings` Steps 1–3 over
`watched-libraries/analysis/omnigent-analysis.md` (16 candidates) and
`opencode-analysis.md` (15 candidates). **No findings written — Nick gates selection**
(promote-findings Rule 1). On selection, Steps 4–7 run: category mapping, finding
creation (P3 default for single-source repo intake), analysis-doc `→` annotations.

## Candidate Table

| # | Candidate | Dimension | Dedup Status | Source Analysis |
|---|-----------|-----------|--------------|-----------------|
| O1 | Phase-asymmetric fail-closed policy defaults | Governance | Partial (`skill-security-scanner-fail-closed.md`) | omnigent |
| O2 | Natural-language policies inside a hardened framework envelope | Governance | Partial (`policy-guarded-tool-execution.md`) | omnigent |
| O3 | Label taint-tracking as composable policy state | Governance | **New** | omnigent |
| O4 | Registry-as-allowlist against callable injection | Governance | Partial (`explicit-permission-allow-listing-for-agent-resou.md`) | omnigent |
| O5 | Three-scope cost governance with hard-cap-as-model-downgrade | Governance | Partial (`budget-governance-with-hard-stop.md`) | omnigent |
| O6 | Orchestration-surface guardrails | Governance × Orchestration | Partial (`capability-restricted-agent-spawning-via-allowlist.md`) | omnigent |
| O7 | Declared-then-bench-verified harness capability flags | Evaluation × Tools | **New** | omnigent |
| O8 | Injection/observation split (bridge + forwarder) | Agentic Systems × Tools | **New** | omnigent |
| O9 | Inbox-over-polling + dispatch-then-end-turn fanout | Orchestration | Partial (`monitor-vs-loop-event-driven-vs-time-driven.md`) | omnigent |
| O10 | Different-vendor cross-review as structural rule | Orchestration × Evaluation | Partial (`cross-model-verification-for-bug-finding.md`) | omnigent |
| O11 | Dual-evaluation approval channel | Governance × Orchestration | Partial (`mcp-elicitation-for-user-input.md`) | omnigent |
| O12 | Client-vs-server state placement doctrine | Agentic Systems | Partial (`brain-hands-decoupling-architecture.md`) | omnigent |
| O13 | Harness-neutral context-file resolution, first-found-wins | Context Engineering | Partial (`cross-platform-context-file-strategy.md`) | omnigent |
| O14 | Conditional skill-menu injection keyed on tool presence | Context Engineering | Partial (`progressive-skill-loading.md`) | omnigent |
| O15 | Verifiability-as-protocol dev skills | Evaluation | Partial (`confirm-failure-first-tdd-agent-discipline.md`) | omnigent |
| O16 | Intent-based authorization | Intent Engineering | Partial (`claude-code-auto-mode-ai-driven-permission-classif.md`) | omnigent |
| C1 | Read-triggered chain-loading of nested AGENTS.md | Context Engineering | Partial (`monorepo-context-distribution-three-strategies.md`) | opencode |
| C2 | `/learn` as the memory write-path | Context Engineering | Partial (`gsd-global-learnings-store-cross-session-persistence.md`) | opencode |
| C3 | Ubiquitous-language glossary with explicit anti-terms | Context Engineering × Prompt | **New** | opencode |
| C4 | Mode = agent = permission ruleset, user-gated transitions | Agent Design × Governance | Full (`static-tool-set-mode-changes-as-callable-tools.md`) — fold as cross-repo corroboration + upgrade candidate | opencode |
| C5 | Context Epoch / Mid-Conversation System Message model | Context Engineering | Full (`append-only-context-updates-system-reminder-injection.md`) — fold as named independent implementation | opencode |
| C6 | Transcript-as-state-machine | Agentic Systems × Orchestration | Partial (`session-as-append-only-event-log.md`) | opencode |
| C7 | Doom-loop breaker as a permission, not an error | Governance × Evaluation | Full (`loop-detection-hash-based-sliding-window.md`) — fold as third response-strategy variant | opencode |
| C8 | Default-on prompt-cache policy with breakpoint math | Model Selection × Context | Full (`layered-prompt-assembly-stable-segment-caching.md`) — fold; also cross-links to the new caching cluster | opencode |
| C9 | Plugins are SDK clients | Tool Integration | **New** | opencode |
| C10 | Two-tier tool contracts as complexity firewall | Tool Integration | **New** | opencode |
| C11 | LLM-generated arity dictionary for bash permission generalization | Governance | Partial (`tiered-permission-system-bash-safety.md`) | opencode |
| C12 | Rejection-with-feedback as a first-class permission verdict | Governance × Intent | Partial (`interrupt-command-primitives-human-in-the-loop.md`) | opencode |
| C13 | Deny-shrinks-toolset | Governance | Partial — **contradicts** `static-tool-set-mode-changes-as-callable-tools.md` (see tensions) | opencode |
| C14 | Asymmetric subagent permission inheritance | Governance × Orchestration | Partial (`permission-compounding-across-agent-delegation-chains.md`) | opencode |
| C15 | Time-boxed automated PR compliance | Governance (repo-level) | **New** | opencode |

## Notable tensions and cross-repo pairs

1. **C13 vs the caching cluster:** opencode deliberately removes denied tools from the
   advertised toolset; the Claude Code team's `static-tool-set-mode-changes-as-callable-tools`
   argues the tool surface must stay static for cache stability. Opposing positions on the
   same design axis — if C13 promotes, add a `contradicts` link. One of the most valuable
   tensions in the batch.
2. **Unknown → conservative default, split verdicts:** omnigent fails closed to DENY
   pre-execution (O1); opencode defaults to ASK on no-match (C11/C12 substrate). Ecosystem
   norm corroborated; the DENY-vs-ASK split is itself an axis worth recording if either
   promotes.
3. **Permission channel as universal escalation/steering bus:** O11 + C7 + C12 converge —
   candidate for one synthesized cross-repo finding rather than three thin ones.
4. **Message-mediated orchestration:** O9 (inbox + end-turn) ↔ C6 (directives as transcript
   parts) — same-problem pair if both promote.
5. **Runtime capability-surface shaping:** O14 ↔ C13.

## Recommendations (Promoter's, non-binding)

- **Safest New promotions:** O3, O7, O8, C3, C9, C10, C15 (7 — no KB coverage).
- **Fold, don't promote:** C4, C5, C7, C8 (Full matches — route the opencode evidence into
  the existing findings as corroboration/variants; C4 and C5 are evidence-strength upgrade
  candidates since they now have independent cross-harness implementations).
- **Judgment calls:** O2 (promote only framed as `extends` of `policy-guarded-tool-execution`),
  C13 (promote for the tension value with the `contradicts` link), the O11+C7+C12 synthesis.
- Partials default to P3 on promotion (single-source repo intake) per the shared triage
  contract.
