---
title: "Secure-by-Default Posture as Organizational Invariant"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "secure-by-default-posture-as-organizational-invariant"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "platforms or frameworks where agents will interact with API endpoints, tools, or services"
    - "any system where the unconfigured default determines the security posture under deadline pressure"
    - "teams shipping agent-facing surfaces (APIs, MCP servers, tool registries) where developers may not explicitly configure security"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "medium — retrofitting deny-by-default onto a system designed with permissive defaults requires auditing all existing access patterns and may break workflows that relied on implicit open access"
  auditability: "high — compliance is verifiable by answering one diagnostic question: 'what happens to this system if nobody touches the security settings after initial deployment?'"
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem's tool permission model defaults to requiring approval for most operations. Claude Code's per-call permission system is a form of deny-by-default for MCP tool invocations."
contract:
  preconditions: "A system, platform, or API surface is being designed that agents will interact with. The system has configurable security settings (authentication requirements, access controls, permission models). The system will be operated by teams under velocity pressure."
  invariants: "The unconfigured default is deny — not open. Systems that are deployed without security configuration are secure by default, not vulnerable by default. The secure path is the path of least resistance. Granting access requires explicit action; denying access requires no action. The diagnostic 'what happens in two years if nobody touches security settings?' always answers 'denied.'"
  governance: "Owner: the platform or system architect. This is an architectural decision, not a policy decision — it is enforced by the system's default configuration, not by training or checklists. Deviation from deny-by-default (making specific surfaces permissive) requires explicit justification and documented exception."
  recovery: "If a permissive default is discovered in production: treat it as a P1 security issue, not a configuration debt item. Audit for exploitation during the window of exposure. If deadline pressure led to shipping without security configuration: the secure default protected the system — no recovery needed (this is the point). If the secure default blocks legitimate agent access: grant specific exceptions through the documented approval path, not by changing the default."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "security"
  - "organizational-design"
---

# Secure-by-Default Posture as Organizational Invariant

**Source:** [[secure-by-default-posture-as-organizational-invariant]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A system, platform, or API surface is being designed or deployed that agents will interact with. The system has configurable security settings. The question arises: what should the unconfigured default be?

## Action

**Required:** Default to deny. When nobody configures security, the system must be secure — not open. Authentication required by default. Access denied by default. Permissions restrictive by default. Every relaxation of security is an explicit, documented, auditable grant.

**Forbidden:** Defaulting to open/permissive access that relies on someone remembering to configure security. Treating security configuration as a post-launch concern. Designing systems where the fast path (shipping without security review) produces vulnerable surfaces.

## Boundary

Enforced at system design time — specifically at the moment default configurations are established. The boundary is architectural: the platform's code determines what happens when security settings are untouched.

## Enforcement

Diagnostic question applied at design review: "What happens to this system in two years if nobody touches the security settings after initial deployment?" If the answer is anything other than "denied by default," the design fails this rule. Secondary diagnostic under pressure: "What happens when the team is told to move fast — where does the technical default land?"

## Rationale

Under deadline pressure, teams ship what the defaults allow. If the default is permissive, unconfigured surfaces accumulate under normal operating conditions. The Lilly/McKinsey incident demonstrated this at scale: 22 of 200 endpoints shipped unauthenticated — not 22 individual failures, but evidence that the platform's default posture was open. In an agent-mediated world, permissive defaults are catastrophically more dangerous because agents exploit accessible surfaces at machine speed, not human speed.
