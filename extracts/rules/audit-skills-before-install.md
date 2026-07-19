---
title: "Audit Skills Before Install"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-security-audit-obligation"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-safety-and-permissions.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "individuals or teams deciding whether to install a third-party agent skill, plugin, or capability package into a working environment"
    - "platform operators or catalog maintainers responsible for vetting community-contributed capability packages before making them available to other users"
    - "security reviewers auditing an already-installed capability package for instructions that fetch external content at runtime"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "secure"
  reversibility: "low — uninstalling a compromised capability package is immediate, but actions already taken under its instructions during prior sessions (data sent, files changed, commands executed) may not be reversible"
  auditability: "high for the static portions — the package's instructions and bundled code are fully readable before install and a review record can be kept; low for any portion that fetches external content at runtime, since that content is not visible at audit time and can change after the fact"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Documented consistently across multiple canonical platform sources as the stated install-time obligation; no confirmation found of a systematic install-time audit process being run in practice at time of extraction."
contract:
  preconditions: "The agent platform supports installable capability packages consisting of natural-language instructions and, optionally, bundled executable code or resource files. A human installer has the ability to read the package's contents (instructions, code, resources) before the package is activated."
  invariants: "No capability package is installed without a provenance check on its source. Before first use, a human reads the package's instructions, any bundled executable code, and any bundled resources. Instructions that direct the agent to fetch content from an external network location at runtime receive particular scrutiny, since that fetched content is not visible at audit time and can differ from what was present when the package was reviewed. Platform-level safeguards (trust prompts, execution restrictions, naming bans) are treated as supplementary, not as a substitute for the human review step."
  governance: "Owner: whoever installs or approves the capability package for use — an individual for personal installs, or a designated reviewer/administrator for packages rolled out to multiple users. The trust boundary is install time, not run time: review happens before activation, and is repeated whenever the package's source content changes. For packages deployed to many users, the reviewer role and the installer/runner role may differ, and review outcomes must be communicated to whoever runs the package."
  recovery: "If a capability package is found, after installation, to contain harmful static instructions or bundled code: uninstall or disable it immediately, and treat any actions taken during sessions where it was active as unverified until reviewed. If a package's runtime-fetched content is found to have served malicious or injected instructions: disable the package immediately, treat every session that used it since the fetch could have occurred as potentially compromised, and do not re-enable until the fetched source is confirmed safe or the fetching instruction is removed. If review capacity cannot keep pace with the number of packages being considered: reduce the install rate or restrict installs to a smaller set of pre-vetted sources rather than skipping the review step."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "skills"
  - "supply-chain"
---

# Audit Skills Before Install

**Source:** [[skill-security-audit-obligation]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A human is about to install, or is deciding whether to install, a capability package — a bundle of natural-language instructions plus, optionally, executable scripts and other bundled resources — into an agent platform. This rule fires at that install decision, and again whenever an already-installed package's source content changes.

## Action

**Required:** Before installing, confirm the package comes from a trusted source (a known publisher, a vetted internal author, or an equivalent provenance signal) — do not install sight-unseen from an unknown source. Read the package's natural-language instructions in full. Review any bundled executable scripts and resource files, treating third-party code dependencies pulled in by those scripts as part of the review surface. Give particular scrutiny to any instruction that directs the agent to fetch content from an external network location at runtime — that fetched content is not visible at audit time, and reviewing the instruction that requests the fetch is the only inspection available before activation.

**Forbidden:** Treating platform-level defensive features (workspace trust prompts, execution restrictions, name-reservation checks, and similar guardrails) as a substitute for the human review step. Accepting a trust prompt without having actually read the package's instructions and code. Installing a package from an unknown or unverified source on the assumption that harness-level controls will catch anything harmful.

## Boundary

Enforced at install time — before a capability package is activated and its instructions begin loading into agent context. Re-enforced whenever the installed package's source content is updated, since the reviewed version and the running version must match. Not a runtime check on individual invocations; a pre-activation review gate.

## Enforcement

- **Mechanism:** The installer (or a designated reviewer, for packages distributed to multiple users) reads the package's full instruction text, bundled code, and bundled resources before activation, and records that the review occurred.
- **Check (observable):** `(source_provenance_checked == true) AND (instructions_reviewed == true) AND (bundled_code_and_resources_reviewed == true) AND (fetch_instructions_flagged_for_scrutiny == true)`. Any term false → the package is unvetted.
- **Violation response:** A package installed without a completed review is treated as unvetted regardless of whether it has caused observable harm yet; installation should not have proceeded, and the package should be reviewed retroactively or removed.

## Rationale

A capability package is valuable for the same reason it is dangerous: its instructions load directly into agent context and its bundled code runs with the local environment's privileges. Platform-level defenses reduce risk but cannot substitute for review, because the review obligation is documented as the discipline itself, not as a backstop behind automated defenses. Three attack surfaces recur across sources: static instructions (readable at audit time), bundled executable code (readable but harder to fully evaluate), and instructions that fetch external content at runtime (not visible at audit time at all, since the fetched content can differ from whatever was present when the package was reviewed). The first two are addressed by thorough reading; the third cannot be closed by review alone and instead earns extra scrutiny of the fetching instruction itself, since the fetched payload can't be inspected in advance.

## Failure Modes

- **Audit theater.** A trust prompt is accepted without the instructions or code actually being read. The review gate exists procedurally but produces no real inspection.
- **Dynamic-content blind spot.** A package that fetches external content at runtime can serve benign content at review time and different content later — the fetch itself is reviewable, but its payload is not, at any single point in time.
- **Bundled-dependency drift.** A package that pulls in a third-party code dependency is only as trustworthy as that dependency's current version; a review performed at install time does not catch a dependency compromised afterward.
- **Review fatigue at scale.** As the number of available packages grows, reviewers develop shortcuts (e.g., trusting anything from a well-known publisher) that don't generalize to every package from that publisher.
- **Reviewer/runner mismatch.** In deployments where packages are pushed to many users, the person who reviewed a package and the person who runs it are different; if review outcomes aren't communicated to runners, the review has no effect on actual usage.

## Contract

### Preconditions
The agent platform supports installable capability packages consisting of natural-language instructions and, optionally, bundled executable code or resource files. A human installer has the ability to read the package's contents (instructions, code, resources) before the package is activated.

### Invariants
No capability package is installed without a provenance check on its source. Before first use, a human reads the package's instructions, any bundled executable code, and any bundled resources. Instructions that direct the agent to fetch content from an external network location at runtime receive particular scrutiny, since that fetched content is not visible at audit time and can differ from what was present when the package was reviewed. Platform-level safeguards (trust prompts, execution restrictions, naming bans) are treated as supplementary, not as a substitute for the human review step.

### Governance
Owner: whoever installs or approves the capability package for use — an individual for personal installs, or a designated reviewer/administrator for packages rolled out to multiple users. The trust boundary is install time, not run time: review happens before activation, and is repeated whenever the package's source content changes. For packages deployed to many users, the reviewer role and the installer/runner role may differ, and review outcomes must be communicated to whoever runs the package.

### Recovery
If a capability package is found, after installation, to contain harmful static instructions or bundled code: uninstall or disable it immediately, and treat any actions taken during sessions where it was active as unverified until reviewed. If a package's runtime-fetched content is found to have served malicious or injected instructions: disable the package immediately, treat every session that used it since the fetch could have occurred as potentially compromised, and do not re-enable until the fetched source is confirmed safe or the fetching instruction is removed. If review capacity cannot keep pace with the number of packages being considered: reduce the install rate or restrict installs to a smaller set of pre-vetted sources rather than skipping the review step.
