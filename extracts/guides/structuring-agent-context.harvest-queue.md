# Co-occurrence Harvest Queue — Structuring and Loading Agent Context

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | extracted | rule | [[hub-and-spoke-two-tier-skill-taxonomy]] | "hub-at-eight-siblings-never-below" | extracted to [[hub-at-eight-siblings-never-below]] |
| 2026-07-16 | extracted | rule | [[skill-description-budget-context-overflow]] | "skill-description-char-caps" | extracted to [[skill-description-char-caps]] |
| 2026-07-16 | extracted | rule | [[evergreen-vs-volatile-ingestion-rule]] | "evergreen-only-ingestion-gate" | extracted to [[evergreen-only-ingestion-gate]] |
| 2026-07-16 | extracted | rule | [[always-on-context-minimalism-pointer-only-entry]] | "always-on-minimal-pointer-only-state" | extracted to [[always-on-minimal-pointer-only-state]] |
| 2026-07-16 | extracted | skill | [[cold-start-chain-and-cold-start-test]] | "cold-start-regression-test" | extracted to [[cold-start-regression-test]] |
| 2026-07-16 | extracted | rule | [[branch-analysis-externalization-rule-skill-reference]] | "branch-analysis-reference-placement" | extracted to [[branch-analysis-reference-placement]] |

## Per-row details

### hub-and-spoke-two-tier-skill-taxonomy::rule::hub-at-eight-siblings-never-below

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[hub-and-spoke-two-tier-skill-taxonomy]]
- **Source excerpt:**
  > "**The ≥8-sibling threshold.** A family is consolidated into a hub when it has, or is expected to reach, ≥8 sibling skills. Below that, skills stay standalone top-level entries — a hub over 3 spokes adds an indirection hop without meaningfully shrinking the index."
- **Codifier's reading:** A countable, machine-checkable imperative directive with an explicit threshold and a symmetric prohibition (never hub below) — canonical rule shape per the form rubric's "machine-enforceable directive" criterion.
- **Suggested headline:** hub-at-eight-siblings-never-below
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[hub-at-eight-siblings-never-below]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[hub-at-eight-siblings-never-below]].

### skill-description-budget-context-overflow::rule::skill-description-char-caps

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[skill-description-budget-context-overflow]]
- **Source excerpt:**
  > "Soft > 1000 chars — Medium finding — description is getting expensive. Hard > 1536 chars — High finding — harness truncation risk. ... their generated-artifact contract requires new descriptions to fit ≤1000 chars at creation time."
- **Codifier's reading:** Two numeric caps with severities, independently corroborated (Anthropic docs harness cap + enterprise audit tooling) — a lintable authoring rule for any skill library.
- **Suggested headline:** skill-description-char-caps
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[skill-description-char-caps]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[skill-description-char-caps]].

### evergreen-vs-volatile-ingestion-rule::rule::evergreen-only-ingestion-gate

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[evergreen-vs-volatile-ingestion-rule]]
- **Source excerpt:**
  > "The ingestion-time test: 'in a year, will it be good for me to have this memory in here? Yes → ingest. Otherwise it's just adding noise.' ... Volatile data — Slack threads, emails, live customer records — stays in its system of record; the brain gets ACCESS to those systems, not copies."
- **Codifier's reading:** A binary ingestion gate with a stated test and a routing consequence (pointer instead of copy) — imperative, enforceable at every ingest step; the finding is itself named a rule.
- **Suggested headline:** evergreen-only-ingestion-gate
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[evergreen-only-ingestion-gate]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[evergreen-only-ingestion-gate]].

### always-on-context-minimalism-pointer-only-entry::rule::always-on-minimal-pointer-only-state

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[always-on-context-minimalism-pointer-only-entry]]
- **Source excerpt:**
  > "always-on = minimal; everything else loads on demand ... the file names the active `{user-id}` and routes to that user's scope; it never restates user facts, targets, or status — 'those go stale and leak.' Volatile facts live in exactly one surface and are pointed to everywhere else."
- **Codifier's reading:** A design law stated as a pair of always/never directives over the entry file's contents — auditable against any CLAUDE.md/AGENTS.md ("does the always-on surface restate anything that lives elsewhere?"), which the finding itself flags as an /assess-agent criterion.
- **Suggested headline:** always-on-minimal-pointer-only-state
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[always-on-minimal-pointer-only-state]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[always-on-minimal-pointer-only-state]].

### cold-start-chain-and-cold-start-test::skill::cold-start-regression-test

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[cold-start-chain-and-cold-start-test]]
- **Source excerpt:**
  > "The **test**: a fresh session, loading only the standard entry points, must be able to state the system's purpose and the next unit of work with zero guidance. ... run the test as a push report — the fresh session must echo what actually composed ... with zero guidance. If the echo fails or misstates any of these, the install is not done; return to the failing row and re-run."
- **Codifier's reading:** A repeatable procedure with defined inputs (standard entry points only), a pass/fail condition, an output shape (the echo report), and a recovery loop — skill shape, not rule shape; it is run, not enforced.
- **Suggested headline:** cold-start-regression-test
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[cold-start-regression-test]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[cold-start-regression-test]].

### branch-analysis-externalization-rule-skill-reference::rule::branch-analysis-reference-placement

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[branch-analysis-externalization-rule-skill-reference]]
- **Source excerpt:**
  > "Reference used on **every branch** stays inline in SKILL.md (externalizing it just adds a read round-trip that always happens). Reference used on **only some branches** moves behind a context pointer — a one-line 'if you need X, read `<file>`' pointing at a markdown file bundled in the skill folder."
- **Codifier's reading:** A two-clause decision rule with a deterministic test (enumerate branches, check usage per branch) — enforceable during skill authoring and audit; the finding's own name labels it a rule.
- **Suggested headline:** branch-analysis-reference-placement
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[branch-analysis-reference-placement]]

Extracted 2026-07-19 — Session 152 — [[structuring-agent-context.harvest-queue]] — to [[branch-analysis-reference-placement]].
