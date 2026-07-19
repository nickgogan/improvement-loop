---
type: "version-bump-proposals-report"
target_system:
  - "improvement-loop"
generated_by: "/extract-artifacts"
date: "2026-07-19"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue"
total_template_candidates: 1
proposals_emitted: 1
no_match_passthrough: 0
---

# Version-Bump Proposals — 2026-07-19

One template candidate scanned during a harvest-queue promotion run (DD-101, session 152). The DD-100 corpus scan over `extracts/templates/` found a semantic-family match; one version-bump proposal is emitted. Source: `autonomous-scheduled-agent-operation.harvest-queue.md` (row `loop-contract-anatomy-and-evolve-session-cadence::template::loop-contract-file-schema`), Status `nick-approved`. Per DD-100 this report proposes only — no existing artifact is modified here; Nick rules the version-bump/create-new target per proposal.

## Proposals

### loop-contract-anatomy-and-evolve-session-cadence

**Form:** template
**Existing template (primary match):** [[loop-anatomy-spec-template]] (current version: v1)
**Secondary matches:** [[progressmd-session-bridge-template]] (v1)

**Proposed filename (if version-bumped):** `loop-anatomy-spec-template-v2.md`

**Codifier recommendation:** create new (false positive)

**Why this match:** The primary match is the strongest possible semantic signal a DD-100 scan can find — the candidate's *own source finding* explicitly cross-references `loop-anatomy-spec-template`'s source finding (`loop-node-anatomy-schema-enforced-ralph-primitive`, listed as `rel: extends` in frontmatter) and its body names that finding directly: "The KB's Archon loop-node schema shows what schema-enforcement of the adjacent *mechanical* iteration anatomy looks like." Both templates are loop-engineering design artifacts filled in at specify-time, both are "one file per X" governance shapes, and both are cited in the same finding cluster (`autonomous-scheduled-agent-operation` guide). The secondary match, `progressmd-session-bridge-template`, shares the "single durable file surviving across many runs, git-diffable, human-skimmable" shape with the candidate's State + Log sections specifically.

**Diff sketch:**

If Nick ruled *version-bump* on the primary match, `loop-anatomy-spec-template-v2.md` would need to absorb: a `{{GOAL}}` / `{{BOUNDARIES}}` / `{{SOP}}` contract block (currently absent — the v1 template has no goal/boundary/escalation-policy fields at all, only mechanical iteration parameters), a `{{STATE}}` block (current hypothesis, open backlog, shipped-but-follow-up items — deliberately small, overwritten each update), an append-only `{{LOG}}` block (run-by-run record), and a new `{{EVOLVE_SESSION_CADENCE}}` variable (every N runs, hand the agent its own config + history + transcripts and ask for self-revision proposals). That is a near-total restructure of the schema's variable set and Body scaffold, not an incremental addition — v1's variables (`COMPLETION_SIGNAL`, `MAX_ITERATIONS`, `CONTEXT_POLICY`, `HUMAN_GATE`, `OBSERVABILITY_EVENTS`, `RESUME_STATE`) answer "how does one iteration of this loop mechanically run and stop," while the candidate answers "what is this automation *for*, what may it do alone, what does it currently believe, and what has it already tried" — a lifecycle-governance question, not an iteration-mechanics question. A v2 that tried to answer both would conflate two audiences (the harness implementer filling in iteration mechanics vs. the loop owner filling in a living contract that gets edited by evolve sessions on a completely different cadence than the loop itself runs).

**However, the honest recommendation is create-new**, because:

- **Different object.** v1 specs *one loop-node's mechanical iteration anatomy* (a design-time checklist, filled once before the harness is built, largely static thereafter). The candidate specs *the whole automation's living governance file* (goal/boundaries/SOP + state + log), explicitly designed to be edited on an ongoing basis — state is overwritten every run, log grows every run, contract is revised every 5-10 runs by a dedicated "evolve session." v1's own Contract → Reversibility field even calls it "a planning document" with no ongoing-edit expectation; the candidate is the opposite — an artifact meant to be mutated continuously across the automation's lifetime.
- **Different audience/altitude.** v1 is filled once by whoever builds the loop's harness code. The candidate is filled and maintained by (or on behalf of) whoever *owns* the automation over its operating lifetime, and is itself the input to a second artifact class (the evolve-session prompt) that v1 has no equivalent of.
- **Composable, not competing.** A single automation could reasonably have both: a `loop-anatomy-spec` fixing its mechanical iteration parameters at build time, and a `loop-contract-file` tracking its goal/boundaries/state/log across its operating lifetime. Merging them into one v2 template would force every consumer of the (currently narrow, mechanics-only) v1 template to also carry contract/state/log fields they may not want.

**Notes:** Recommendation **create new (false positive)**. Surfaced per DD-100's loose calibration precisely because the source finding itself draws the connection explicitly — silently drafting a new template without flagging the adjacency would be a worse failure than a false-positive flag here. If Nick concurs, re-invoke `/extract-artifacts --harvest-row loop-contract-anatomy-and-evolve-session-cadence::template::loop-contract-file-schema` to write the new baseline template (unsuffixed filename, not a `-v2`). If Nick instead rules version-bump, the diff sketch above is the starting point, but note it would substantially widen v1's scope rather than incrementally extend it.
