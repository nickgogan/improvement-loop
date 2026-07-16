# Co-occurrence Harvest Queue — Agent Governance and Trust

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | template | [[receipt-artifact-as-agent-trust-mechanism]] | "receipt-schema-sources-changes-approval" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[agent-owner-card-human-facing-registry]] | "seven-field-agent-owner-card" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[governance-registry-blast-radius-classification]] | "governance-files-blast-radius-registry" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[three-bucket-change-approval-tiering]] | "three-bucket-change-review-file" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[recurrence-threshold-gates-autonomy-not-direction]] | "recurrence-threshold-gates-autonomy-not-direction" | dismiss as inline |
| 2026-07-16 | queued | rule | [[root-context-file-edit-guard]] | "ask-before-editing-root-context-file" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[skill-invocation-control-side-effect-guard]] | "side-effect-skills-require-explicit-invocation" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[deterministic-doc-audit-battery]] | "deterministic-doc-audit-script-battery" | extract via /extract-artifacts |

## Per-row details

### receipt-artifact-as-agent-trust-mechanism::template::receipt-schema-sources-changes-approval

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[receipt-artifact-as-agent-trust-mechanism]]
- **Source excerpt:**
  > "A standardized artifact the agent emits whenever it stops at a human gate, answering three questions: **what sources did I use** (with addresses back into the stored, chunked originals), **what did I change**, and **what still needs your approval**. ... A standard receipt schema (sources/changes/needs-approval) embedded in skill output contracts."
- **Codifier's reading:** A fixed three-field structural scaffold meant for rendering at every human gate — the finding itself proposes it as a "standard receipt schema" for output contracts, canonical template shape per the form rubric.
- **Suggested headline:** receipt-schema-sources-changes-approval
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### agent-owner-card-human-facing-registry::template::seven-field-agent-owner-card

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[agent-owner-card-human-facing-registry]]
- **Source excerpt:**
  > "For every agent that matters, write down seven fields: name, owner, job, sources (what it is allowed to read), what it can do, what it can't do, and the failure mode you need to watch for. The card works at both scales — a team leader's spreadsheet row and an individual's ownership certificate."
- **Codifier's reading:** A fixed seven-field fillable form with placeholder semantics — pure structural scaffold. The finding's own implementation note flags it as a candidate criteria-delta for /assess-agent, strengthening the extract case.
- **Suggested headline:** seven-field-agent-owner-card
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### governance-registry-blast-radius-classification::template::governance-files-blast-radius-registry

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[governance-registry-blast-radius-classification]]
- **Source excerpt:**
  > "A single registry file that classifies every behavior-shaping file in the workspace into exactly two tiers — **governance** (deliberate, human-in-the-loop edits only) or **working/notes** (autonomous agent edits fine) — with the reasoning per entry. ... the registry is itself classified as governance, so the classification scheme cannot be loosened autonomously."
- **Codifier's reading:** A registry-file scaffold with a fixed two-tier schema, per-entry reasoning field, and a self-referential entry — a renderable structural form, not just a directive.
- **Suggested headline:** governance-files-blast-radius-registry
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### three-bucket-change-approval-tiering::template::three-bucket-change-review-file

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[three-bucket-change-approval-tiering]]
- **Source excerpt:**
  > "Written to `output/review-<date>.md` as a checkbox list; each item offers **approve / reject / approve-and-don't-ask-again** ... **More context required** — items the system cannot classify alone ... Appended to the same review file so the human reviews everything in one sitting."
- **Codifier's reading:** The dated review-file shape (checkbox list, three verdict options per item, shared more-context section) is a concrete renderable scaffold; the surrounding tiering logic stays pattern-shaped in the guide.
- **Suggested headline:** three-bucket-change-review-file
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### recurrence-threshold-gates-autonomy-not-direction::rule::recurrence-threshold-gates-autonomy-not-direction

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[recurrence-threshold-gates-autonomy-not-direction]]
- **Source excerpt:**
  > "The agent needs N occurrences before it may push a change proposal; the human needs zero. ... Crossing the threshold makes a lesson *eligible* — promotion still runs the full pipeline ... 'Nothing about the threshold weakens the gate.'"
- **Codifier's reading:** A crisp imperative directive with a deterministic check (occurrence counting) — clean rule shape. Recommendation is dismiss because the engine already operationalizes exactly this rule in /self-improve (PROMOTE flag at N=2 normal / N=1 high, operator direction overrides), so an extracts/rules/ archive copy adds no consumer.
- **Suggested headline:** recurrence-threshold-gates-autonomy-not-direction
- **Recommendation:** dismiss as inline
- **Resolution:**

### root-context-file-edit-guard::rule::ask-before-editing-root-context-file

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[root-context-file-edit-guard]]
- **Source excerpt:**
  > "make this a standing rule in the router itself. The number one rule at the top: the AI asks you before it edits the root claude.md file. That one file is what everything else depends on. It's sacred. You don't let it drift silently. You approve every change on purpose, with intention."
- **Codifier's reading:** A one-line machine-checkable imperative (ask-before-edit on a named file) that is also hook-enforceable (PreToolUse write-block on the root path) — canonical rule shape per the form rubric.
- **Suggested headline:** ask-before-editing-root-context-file
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### skill-invocation-control-side-effect-guard::rule::side-effect-skills-require-explicit-invocation

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[skill-invocation-control-side-effect-guard]]
- **Source excerpt:**
  > "**`disable-model-invocation: true`** — protects against Claude triggering on a description match. Intended for workflows with side effects where timing matters (commits, deploys, outbound messages). ... **Side-effect skill without the flag.** Author writes a `/commit` skill, ships without `disable-model-invocation: true`."
- **Codifier's reading:** Lintable authoring directive over skill frontmatter ("any skill whose procedure performs side effects sets disable-model-invocation: true") — machine-enforceable at audit time; directly consumable by /assess-skill's safety-critical classification.
- **Suggested headline:** side-effect-skills-require-explicit-invocation
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### deterministic-doc-audit-battery::skill::deterministic-doc-audit-script-battery

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[deterministic-doc-audit-battery]]
- **Source excerpt:**
  > "`audit_docs.py` — a single ~580-line stdlib-only Python script ... inside the `ops-doc-sync` skill. Read-only, never modifies the tree. Exit codes: 0 = clean (warnings allowed), 1 = any error, 2 = usage. Each check is a pure function over the repo root, registered in a flat list; each finding prints `[FAIL]`/`[warn]` with a stable check ID."
- **Codifier's reading:** A complete procedure with invocation contract (exit codes), step structure (16 registered checks), and output shape (stable IDs + embedded remediation) — skill shape with a wrapping SKILL.md discipline (audit-before-edit, re-run-to-exit-0) already documented in the source.
- **Suggested headline:** deterministic-doc-audit-script-battery
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
