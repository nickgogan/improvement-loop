# Co-occurrence Harvest Queue — Agent Safety and Permissions

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | extracted | rule | [[shell-injection-vector-taxonomy-agent-bash-security]] | "bash-hook-injection-vector-checklist" | extracted to [[bash-hook-injection-vector-checklist]] |
| 2026-07-16 | extracted | rule | [[sandbox-architecture-by-threat-model-microvm-vs-container]] | "untrusted-code-requires-hardware-isolation" | extracted to [[untrusted-code-requires-hardware-isolation]] |
| 2026-07-16 | extracted | rule | [[skill-security-audit-obligation]] | "audit-skills-before-install" | extracted to [[audit-skills-before-install]] |

## Per-row details

### shell-injection-vector-taxonomy-agent-bash-security::rule::bash-hook-injection-vector-checklist

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[shell-injection-vector-taxonomy-agent-bash-security]]
- **Source excerpt:**
  > "Teams building bash-access agents need an enumerated injection-vector list, not just an allowlist of known-safe commands. [...] Publish an IL rule-checklist: for any proposed bash hook, confirm defenses against each named vector — Zsh equals expansion (`=curl` bypassing a `curl` allowlist), unicode zero-width-space insertion in command names, IFS null-byte injection, and a malformed-token bypass found during a HackerOne bug-bounty review."
- **Codifier's reading:** Imperative, machine-checkable audit directive ("for any proposed bash hook, confirm defenses against each named vector") with a closed enumerated checklist — fits the rule form's machine-enforceable-directive criterion. The finding itself proposes the rule-checklist as an improvement, so extraction intent is explicit in the source.
- **Suggested headline:** bash-hook-injection-vector-checklist
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[bash-hook-injection-vector-checklist]]

Extracted 2026-07-19 — Session 152 — [[agent-safety-and-permissions.harvest-queue]] — to [[bash-hook-injection-vector-checklist]].

### sandbox-architecture-by-threat-model-microvm-vs-container::rule::untrusted-code-requires-hardware-isolation

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[sandbox-architecture-by-threat-model-microvm-vs-container]]
- **Source excerpt:**
  > "The right choice is determined by 'is the code untrusted?' — not by latency or pricing. [...] Untrusted-code workload mis-routed to container-based sandbox → container escape is a realistic compromise path."
- **Codifier's reading:** The finding is pattern-shaped overall, but its core decision criterion compresses to an imperative directive ("never route untrusted/model-generated code to a shared-kernel sandbox; require hardware isolation") that is binary-testable at architecture-review time — rule form.
- **Suggested headline:** untrusted-code-requires-hardware-isolation
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[untrusted-code-requires-hardware-isolation]]

Extracted 2026-07-19 — Session 152 — [[agent-safety-and-permissions.harvest-queue]] — to [[untrusted-code-requires-hardware-isolation]].

### skill-security-audit-obligation::rule::audit-skills-before-install

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[skill-security-audit-obligation]]
- **Source excerpt:**
  > "'Install skills only from trusted sources' — implies a provenance check before install. 'Thoroughly audit it before use' — review SKILL.md, scripts, bundled resources. [...] 'Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources' — fetched content can carry injected instructions."
- **Codifier's reading:** Imperative install-time obligations ("install only from trusted sources", "audit before use") with three enumerated attack surfaces to check — machine-enforceable as a pre-install gate; fits rule form. Finding is still `pipeline_status: raw` with no prior extraction, so no merge target exists.
- **Suggested headline:** audit-skills-before-install
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[audit-skills-before-install]]

Extracted 2026-07-19 — Session 152 — [[agent-safety-and-permissions.harvest-queue]] — to [[audit-skills-before-install]].
