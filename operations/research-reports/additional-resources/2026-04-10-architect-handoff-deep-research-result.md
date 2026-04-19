# Research-to-Codification Pipeline: Prior Art for Artifact Contracts Between Proposer and Architect Roles

## Executive Summary

Across six substantive domains — threat detection engineering, evidence-based medicine, ML operations, compliance-as-code, pharmaceutical technology transfer, and platform governance — mature pipelines have independently converged on a recurring structural answer to the "who decides form" question: **the proposer describes behavior and evidence at a form-agnostic level; a named boundary role (detection engineer, guideline panel, model deployer, authorizing official) decides output form at a later layer.** The fully collaborative, confidence-weighted model (Option 3 in your framing) is the most common hybrid observed in practice, but it is typically implemented as a **form-agnostic proposer + mandatory human gate with dissent recording**, rather than as a symmetric confidence ballot. A pure form-deciding proposer is only stable when a regulatory authority mandates the form, as in pharmaceutical CTD submissions.

***

## Comparative Table: Five Prior-Art Approaches

| # | Name | Domain | Researcher Role | Implementer Role | Artifact Format | Who Decides Form | Conflict Mechanism | Human Gate | Primary Source |
|---|------|--------|----------------|-----------------|-----------------|------------------|--------------------|------------|----------------|
| 1 | **MITRE ATT&CK → CAR → Sigma** | Cybersecurity / Detection Engineering | ATT&CK researcher: documents adversary behavior (technique + data sources), form-agnostic | Detection engineer: selects analytic form (Sigma rule, EQL, SPL) | ATT&CK: STIX/JSON (form-agnostic). CAR: hypothesis + pseudocode. Sigma: YAML detection rule with log source, condition, false-positives | Three-layer split: ATT&CK researcher is form-agnostic; CAR provides pseudocode middle layer; org/engineer decides final form per SIEM | CAR analytic crosswalk shows coverage gaps; ATT&CK v18 Detection Strategies (DETxxxx) and Analytics (ANxxxx) are separately maintained | PR to SigmaHQ repo with peer review; internal change-management gate at org level | [car.mitre.org](https://car.mitre.org); [sigmahq.io/docs/basics/rules.html](https://sigmahq.io/docs/basics/rules.html); [attack.mitre.org/detectionstrategies/](https://attack.mitre.org/detectionstrategies/) |
| 2 | **GRADE / Cochrane → WHO EtD → Guideline** | Evidence-based medicine / Clinical guidelines | Systematic reviewer: produces Evidence Profile and Summary of Findings (SoF) table with per-outcome certainty ratings; form-agnostic | Guideline panel: deliberates using EtD framework, decides recommendation form (strong/conditional, for/against), direction, and implementation conditions | Evidence Profile (GRADE certainty scores). SoF table (tabular). Evidence-to-Decision (EtD) framework (structured fields). Final recommendation (direction + strength) | Explicit separation: reviewer is form-agnostic; multi-stakeholder panel decides form by consensus | EtD framework has explicit "dissenting views" field and records panel voting results on contested judgments; "minority opinions… should be presented to increase transparency" | Panel deliberation sessions; Authorizing Committee vote; patient representatives required since ~2020 | [gradeworkinggroup.org](https://www.gradeworkinggroup.org); [who.int/publications/i/item/9789240011908](https://www.who.int/publications/i/item/9789240011908); [pmc.ncbi.nlm.nih.gov/articles/PMC5975536/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5975536/) |
| 3 | **NIST OSCAL (Catalog → Profile → Component Def → SSP)** | Compliance-as-code / Security governance | Control framework author: publishes abstract catalog (NIST 800-53). Profile author: selects/tailors baseline. Both are form-agnostic about system-specific implementation | Component definition author (vendor/engineer): decides control implementation form. System owner: creates SSP linking components to system boundary | Catalog (XML/JSON/YAML abstract controls). Profile (tailored baseline). Component Definition (tech-specific implementation). System Security Plan (system instance record) | Layered authority: catalog author decides control semantics; profile author tailors; **component def author decides implementation form**; SSP author records actuals. "Map once, comply many" | Control Mapping model (set theory: equivalent-to, subset-of, superset-of) exposes gaps and overlaps between catalogs; crosswalk surfaces contradictions between frameworks | Authorizing Official reviews SSP; CISO signs off on component definitions; CAM pipeline validates schema compliance | [pages.nist.gov/OSCAL/learn/concepts/layer/control/](https://pages.nist.gov/OSCAL/learn/concepts/layer/control/); [pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/) |
| 4 | **MLflow Experiment → Model Registry → Model Card** | ML Operations | Data scientist: logs experiment runs (params, metrics, artifacts). Produces Model Card documenting intended use, limitations, evaluation slices. Role is form-deciding within a prescribed schema | ML engineer / platform team: reviews model via registry stage gates, promotes through Staging → Production; decides deployment configuration | Experiment run (params + metrics + artifact). Model Card (schema: model details, intended use, factors, metrics, evaluation data, ethical considerations). Registry entry with stage alias | **Form-deciding proposer** within schema (data scientist decides it's a Model Card + fills fields). Deployment engineer decides serving form. Stage gates can block promotion. SEI CMU formalized "ML Mismatch Descriptors" to make cross-role assumptions explicit | SEI CMU study identifies 5 mismatch types at DS→SWE handoff; stage-gate automated quality checks surface metric regression; Champion/Challenger registry pattern for disagreement on production readiness | Peer review required before production; stakeholder sign-off for high-impact models; automated gates (metric thresholds, schema completeness, fairness audits) | [research.google/pubs/model-cards-for-model-reporting/](https://research.google/pubs/model-cards-for-model-reporting/); [sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/](https://www.sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/) |
| 5 | **Pharma R&D → CTD / Tech Transfer Package → CDMO** | Pharmaceutical manufacturing / Regulatory | R&D scientist: prepares Technology Transfer Package (TTM). Mandatory form is ICH Common Technical Document (CTD): Module 3 (quality/CMC), Module 4 (nonclinical), Module 5 (clinical) | CDMO (implementer): executes scale-up. Must replicate process, cannot deviate from transferred methods without change control. Can flag gaps but cannot unilaterally alter package form | Tech Transfer Package (process formulation, analytical methods, in-process controls, stability data, CMC data). ICH CTD (5-module hierarchical format). Stage-gate templates per milestone | **Regulatory mandate decides form**: ICH CTD format is non-negotiable. R&D (proposer) fills the defined form; CDMO (implementer) raises gaps through formal deviation/change control process | Formal deviation reports and out-of-specification investigations; change control process requires documented rationale; regulatory submission records all decisions | Stage-gate: each gate has structured review template, risk checklist, decision protocol. Regulatory approval is the final human gate | [ich.org/products/ctd.html](https://www.ich.org/products/ctd.html); [intuitionlabs.ai/articles/pharma-tech-transfer-cdmo-guide](https://intuitionlabs.ai/articles/pharma-tech-transfer-cdmo-guide) |

***

## Deep Dives on Three Strongest Examples

### 1. MITRE ATT&CK → CAR → Sigma: The Three-Layer Separation

This is the most directly analogous pipeline to the one you are designing. MITRE explicitly separates the threat model (ATT&CK) from detection analytics (CAR) from platform-specific rules (Sigma/SIEM queries). From the CAR site itself: *"It's critical to keep how we articulate threats with ATT&CK **separate** from a set of possible ways to detect them… It's up to the organization implementing them to determine what works best for their environment and the threats they face."*[^1]

The artifact contract between each layer is well-defined:

- **ATT&CK technique entry** (STIX JSON): describes adversary behavior, required data sources, applicable platforms. Deliberately says nothing about detection form.[^1]
- **CAR analytic** (YAML): adds a *hypothesis* (why this is worth detecting), pseudocode, and optional platform-specific implementations (Splunk, EQL, etc.). The form — "this is an analytic with hypothesis + pseudocode" — is decided at this layer.[^2][^1]
- **Sigma rule** (YAML): decides the specific detection form (log source, field conditions, false-positive handling). Multi-target fan-out happens here via pySigma processing pipelines that remap fields and translate to any SIEM backend.[^3][^4][^5]

In ATT&CK v18 (October 2025), MITRE formalized Detection Strategies (DET-xxxx) and Analytics (AN-xxxx) as distinct named objects linked to techniques, replacing the older "Detections" prose fields. This creates a four-layer chain: **Technique → Detection Strategy → Analytic → Platform Implementation**, each with its own named identifier and schema.[^6]

The **canonical vocabulary** here: *Hypothesis, Pseudocode, Pipeline (processing), Backend, Detection Strategy, Analytic Coverage*.

### 2. GRADE/Cochrane EtD: The Form-Agnostic Proposer with Structured Override Trail

The GRADE Evidence-to-Decision (EtD) framework is the most mature published system for the "who decides form" problem in any domain. The separation of roles is total and enforced by the process:

- **Systematic reviewer** (researcher role): produces the Evidence Profile (per-outcome certainty ratings on five GRADE domains: risk of bias, inconsistency, indirectness, imprecision, publication bias) and Summary of Findings (SoF) table. The reviewer does NOT recommend a guideline form. The SoF table deliberately stops at "what the evidence shows" and does not prescribe whether a strong or conditional recommendation follows.[^7][^8]
- **Guideline panel** (architect/implementer role): uses the EtD framework to deliberate across seven criteria: problem priority, effect sizes, certainty of evidence, values/preferences, resource use, equity, acceptability, feasibility. The panel decides the recommendation form (strong/conditional, for/against, under what conditions).[^9][^10]

The **conflict-surfacing mechanism** is explicit and named: the EtD has a designated "additional information" field where *"dissenting views of panel members or the results of voting on judgments where there was disagreement"* must be recorded. The CDC ACIP implementation requires that *"minority opinions voiced during discussions should be presented"*. This is not a footnote — it is a first-class field in the artifact.[^11][^12][^9]

The **human gate ritual** is multi-stakeholder deliberation. Since ~2020, WHO and the Endocrine Society require patient representatives on guideline development panels, trained in GRADE methods. This is a named ritual: the *Guideline Development Panel (GDP) meeting* where the EtD is reviewed row by row.[^13]

**Canonical vocabulary**: *Evidence Profile, Summary of Findings (SoF) table, Evidence-to-Decision (EtD) framework, PICO question, Certainty of evidence, Strength of recommendation, Dissenting view, Minority opinion*.

### 3. NIST OSCAL: Layered Role Authority with Multi-Target Fan-Out

OSCAL's architecture directly solves the multi-target problem (one research finding → multiple downstream systems with different constraints) through a five-model layer stack:[^14][^15]

1. **Catalog**: Abstract control requirements (e.g., NIST 800-53 AC-2). Maintained by standards body. Form is fixed.
2. **Profile**: A *selected and tailored* subset of controls for a specific baseline (e.g., FedRAMP High). Profile author decides which controls apply and assigns parameter values. Multiple profiles can reference one catalog.
3. **Component Definition**: Vendor/platform-specific implementation of controls (e.g., "AWS S3 implements AC-2 via IAM policies"). The **component definition author** is the first role to decide the *implementation form*.[^15][^16]
4. **System Security Plan (SSP)**: System-specific record that assembles a profile + selected components + implemented controls for one system.[^17][^15]
5. **Assessment Results**: Evidence artifacts from actual testing.[^14]

The **multi-target design**: one catalog control fans out to many SSPs for different systems with different technology stacks. Each SSP is a separate artifact consuming the same upstream catalog/profile via reference, not by copy. The COMPASS/Trestle implementation of this pipeline uses a CI/CD pipeline where control providers submit Markdown or CSV, which Trestle converts to OSCAL component definitions automatically.[^16]

The **conflict-surfacing mechanism**: the Control Mapping Model expresses relationships between different catalogs using set theory — `equivalent-to`, `subset-of`, `superset-of`, `intersects-with`, `no-relationship`. When two catalogs partially overlap, the mapping model exposes the contradiction rather than averaging it away. This is explicitly a tool for downstream implementers to see unresolved tension between frameworks.[^14]

**Canonical vocabulary**: *Catalog, Profile (baseline), Component Definition, System Security Plan, Control Mapping, Crosswalk, Map once/comply many, Tailoring, Parameterization, Authorization Boundary*.

***

## Named Patterns and Canonical Vocabulary

### Form-Decision Boundaries

- **Form-agnostic proposer**: The researcher describes behavior, evidence, or requirements without prescribing output form. The MITRE ATT&CK team chose this pattern deliberately for ATT&CK because "there could be many different ways, and it's up to the organization implementing them". The Cochrane systematic reviewer is form-agnostic by design — their SoF table ends at effect sizes and certainty ratings.[^7][^1]

- **Form-deciding proposer**: The researcher includes a form decision in the artifact. Pharma CTD is the clearest case — ICH mandates the form, removing ambiguity but also flexibility. MLflow Model Cards operate similarly: Google's 2019 paper prescribes sections (model details, intended use, factors, metrics, ethical considerations), and proposers fill them.[^18][^19][^20][^21]

- **Layered form authority** (OSCAL pattern): Each pipeline layer has sovereign authority over form decisions at its level, but cannot override decisions made at a higher abstraction layer. Control semantics live in the catalog (standards body), tailoring lives in the profile (organization security team), and implementation form lives in the component definition (platform team).[^15][^14]

- **Processing pipeline** (Sigma/pySigma pattern): The proposer decides the abstract form (a Sigma YAML rule with detection logic), but actual deployment form (Splunk SPL, KQL, EQL) is decided by a composable pipeline layer that the implementer controls. The proposer and implementer are decoupled via a translation contract (field mapping + backend).[^4][^3]

### Conflict and Dissent Patterns

- **Recorded dissent** (GRADE/WHO pattern): First-class field in the artifact contract for capturing minority panel opinions and voting results on contested judgments. Not a social norm — a schema requirement.[^12][^9]

- **Rough consensus + running code** (IETF pattern): RFC 7282 defines rough consensus as *"lack of strong disagreement"*, not majority vote. A single technically substantive objection can block consensus even against a majority. Objectors must be given reasoned responses. This is the named pattern for how the IETF navigates proposer/implementer tensions over artifact form.[^22]

- **Coverage gap visualization** (MITRE pattern): CAR's Analytic Coverage Comparison crosswalk shows which ATT&CK techniques have no analytics at all, making research-to-implementation gaps visible rather than hiding them. ATT&CK v18 Detection Strategies map technique → detection intent before any implementation form is chosen, so gaps in coverage appear at the strategy layer.[^23][^6]

- **Control crosswalk / set-theoretic mapping** (OSCAL pattern): Contradictions between research findings (different catalogs making conflicting claims) are exposed using formal set-theory relationships rather than merged into an averaged recommendation.[^14]

### Human Gate Rituals

- **Stage gate** (pharma/MLOps): Structured checkpoint with predefined deliverables, risk checklist, and decision criteria. Each gate requires sign-off before proceeding. Named artifacts at each gate (e.g., "Transfer Report 1: Analytical Verification", "Process Batch #1 report").[^24][^25][^26]

- **Guideline Development Panel meeting** (GRADE): Multi-stakeholder deliberation session using the EtD framework as a structured agenda. Decision is by consensus, with dissent formally recorded. Patient representatives required since ~2020.[^9][^13]

- **Registry stage promotion** (MLOps): Candidate model must pass automated quality gates (metric thresholds, schema completeness, fairness audits) plus peer review before promotion to Staging, then Production. Each transition is logged with approver identity and justification.[^25][^27]

- **Trusted Committer review** (InnerSource Commons): A named role — Trusted Committer (TC) — sits at the research-to-implementation boundary, reviewing contributions for architecture fit, quality standards, and compliance with published contribution guidelines. TCs maintain the contribution guidelines, which are effectively the artifact contract. They have veto authority, not just advisory authority.[^28][^29][^30]

- **IETF Working Group Last Call**: Before an Internet-Draft becomes a Proposed Standard RFC, it undergoes Working Group Last Call — a period during which any objection must be addressed with a reasoned response, not just outvoted.[^31][^32]

***

## Multi-Target Handoff Patterns

When one research finding applies to multiple downstream systems with different constraints, mature organizations use one of three structural patterns:

### Abstract-then-fan-out (Sigma / MITRE CAR)
Write the finding once in an abstract representation (Sigma YAML, ATT&CK technique entry), then fan out to multiple targets via composable translation layers. Each target gets a generated artifact, not a hand-written one. The key design constraint: the abstract representation must be expressive enough that translation is mechanical, not judgment-laden. Sigma processing pipelines handle field remapping per target SIEM; `logsource` in the rule is generic, and the pipeline translates it to platform-specific log paths.[^5][^3][^4]

### One-abstract-spec-per-audience (OSCAL Catalog → multiple SSPs)
Maintain a single catalog + profile as the authoritative upstream spec. Each target system creates its own SSP by selecting components and mapping them to the profile. The SSP is authored by the system team, not the catalog team. Dependencies flow via reference (control IDs), not copy-paste. This preserves upstream authority while allowing downstream customization. The COMPASS/Trestle pipeline automates SSP generation from component definitions.[^33][^16][^15]

### Fan-out proposals per target (pharma)
For high-stakes, irreversible decisions where translation cannot be mechanical, write a separate Tech Transfer Package for each receiving site, adapted to that site's equipment, regulatory jurisdiction, and process capabilities. Module 1 of the CTD is explicitly regional and not harmonized; Modules 2-5 are shared. This is the most expensive pattern but appropriate when target heterogeneity is too high for mechanical translation.[^19][^18]

***

## Failure Modes (Documented Cases)

### Failure Mode 1: ML Mismatch at Data Scientist → Software Engineer Handoff
The CMU Software Engineering Institute ran a multi-year empirical study interviewing practitioners across data science, software engineering, and operations roles. They identified five recurring mismatch types when trained models are passed from data scientists to software engineers:[^34][^35]

- **Computing-resource mismatch**: Model requires GPU/memory not available in production
- **Data-distribution mismatch**: Training data distribution ≠ production data distribution (the most common, 36% of identified mismatches)
- **API mismatch**: Model expects input/output formats different from what the integrating system provides
- **Test-data mismatch**: Software engineers can't properly test the ML component due to inaccessible test data
- **Monitoring mismatch**: Production monitoring tools can't collect ML-relevant metrics like model accuracy drift

The root cause is consistently **implicit assumptions about the trained model artifact** — information the data scientist held but did not encode in the handoff artifact. The SEI's proposed remedy is "ML Mismatch Descriptors": a formal schema of assumptions that must be made explicit at the boundary. This is a direct analogue to your architect contract problem.[^36][^34]

**Source**: [sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/](https://www.sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/)

### Failure Mode 2: Tacit Knowledge Loss in Pharmaceutical Technology Transfer
Pharmaceutical industry surveys consistently identify tacit knowledge loss as the primary tech transfer failure mode. Development teams produce CTD documentation packages, but these capture only *explicit* process knowledge — not the undocumented expertise accumulated during R&D: operator technique, equipment behavior quirks, minor parameter adjustments made for non-obvious reasons.[^37][^38]

The receiving CDMO is then forced to "reverse-engineer" the process, which leads to failed batches and regulatory compliance failures. One documented case involved a sponsor "sending pieces of data to different contacts" rather than a master document, leading to confusion and significant delays. The PDA has formally warned that "technology transfer can impact drugs and patients". The fix requires *transfer coordinators* for each domain (process, analytical, QA) and explicit documentation of *decision history and rationale*, not just parameters.[^39][^37]

This maps directly to the **evidentiary provenance loss** failure mode in your framing.

**Source**: [intuitionlabs.ai/pdfs/pharma-tech-transfer-a-guide-to-the-r-d-to-cdmo-process.pdf](https://intuitionlabs.ai/pdfs/pharma-tech-transfer-a-guide-to-the-r-d-to-cdmo-process.pdf)

### Failure Mode 3: Detection Form Decided Without Coverage Accountability (SIEM gap study)
A 2025 empirical analysis found enterprise SIEMs detect only **21% of MITRE ATT&CK techniques**, leaving 79% uncovered. The root cause is consistent: detection form (which rules to write for which SIEM) is decided per-system, per-engineer, without systematic tracking against a shared coverage model. Teams "collect everything, but don't prove what they can actually detect".[^40][^41]

This is a structural consequence of allowing the implementer to decide form without a shared mapping back to the proposer's evidence model. The ATT&CK → Sigma → Coverage Heatmap pattern (using ATT&CK Navigator) was specifically designed to address this by making gaps in the proposer-to-implementation chain visible.[^23][^6]

This maps to your **scope creep at codification** and **too specific to reuse** failure modes — when each implementer decides form independently, coverage becomes inconsistent and non-auditable.

### Failure Mode 4: RFC Process Impedance Mismatch in Corporate Settings
Jacob Kaplan-Moss (Django co-creator, former Heroku engineering director) documented this failure mode in a widely-cited 2023 post: organizations adopt RFC processes modeled on IETF but discover they have *no built-in decision-making authority*. RFC feedback is informational by definition — "the authors of the RFC are free to incorporate it or not". In corporate settings where someone must ultimately decide, this creates ambiguity about whether the proposer's form decision is binding, advisory, or overridable.[^42][^43]

The failure mode: proposals accumulate feedback indefinitely, the proposer keeps form authority by default, and the implementer has no formal standing to override even when they have system-specific knowledge that makes the proposed form unworkable. The Kaplan-Moss critique: *"there is no clarity on collaboration versus decision-making"*.[^43]

This directly maps to your Option 1 vs Option 3 tension: a form-agnostic proposer needs a *named* downstream role with *explicit* authority to decide form — otherwise the authority drifts back to the proposer by default.

### Failure Mode 5: Abstract-to-Concrete Loss (MITRE CAR pre-v15 "hard to understand" analytics)
Before ATT&CK v15 (2024), MITRE CAR used a pseudo-format for analytics that was "hard to understand" for practitioners. The format was technically correct but didn't map to any real query language, creating a translation gap between the analytic as documented and the analytic as implementable. Detection engineers would read the pseudocode and still have to make non-trivial judgments about how to render it in Splunk or EQL. In v15, MITRE explicitly rewrote analytics into "real-world query language style (like Splunk) that is compatible with various security tools".[^44]

This is the **"too abstract to implement"** failure mode with a documented remediation: the fix required moving from pseudocode to executable query language, which increased specificity at the cost of requiring per-platform versions. MITRE's solution (ATT&CK v18) was to formalize Detection Strategies (platform-agnostic intent) as a separate object from Analytics (platform-compatible queries), effectively introducing a new abstraction layer rather than collapsing the two.[^6]

***

## Gaps in the Literature

The prior art is rich on the structural questions but thin on several issues directly relevant to your design:

### Gap 1: No Empirical Comparison of Form-Agnostic vs. Form-Deciding Proposer Outcomes
Every domain surveyed has a preferred pattern, but none has published a controlled study comparing outcomes (implementation quality, reuse rate, codification time) across the three models you describe. The GRADE/WHO community has studied EtD adoption extensively but always within their form-agnostic design. MLOps has studied ML mismatch but always within a form-deciding design. There is no cross-domain empirical study comparing the two.

### Gap 2: Override Trail Formalism Is Thin
The GRADE dissent field and IETF rough-consensus records are widely used, but no domain has published a formal schema for an *override trail* — a structured record of "proposer suggested form X, implementer decided form Y for reason Z, reviewed by W". InnerSource Trusted Committer decisions are logged in PRs, but the rationale schema is informal. This is a genuine design opportunity.

### Gap 3: Multi-Target Conflict Resolution Across Downstream Systems
When one research finding is simultaneously consumed by two downstream architect roles whose systems have contradictory constraints, no framework has a published protocol for resolving the conflict *at the proposer level*. OSCAL's control mapping model exposes framework contradictions but doesn't resolve them. Sigma's pipeline model defers resolution to each backend. GRADE applies to one population at a time. The "fan-out with conflicting system constraints" case is not addressed in the literature.

### Gap 4: AI Agent Persona / Skill Codification Is Not Modeled
No published framework directly addresses the artifact contract for AI agent skills, personas, rules, or prompt templates as codified outputs. Model Cards cover trained models; Datasheets cover datasets; OSCAL covers security controls. None of these maps cleanly onto the `skill → rule → pattern → template → agent persona` taxonomy you describe. The closest analogues are InnerSource contribution guidelines (governance of reusable code artifacts) and the MITRE CAR analytic (hypothesis + pseudocode + implementation as layered artifact), but neither covers the agentic context.

### Gap 5: Confidence Weighting at the Proposer Level Is Not Standardized
GRADE formalizes uncertainty about evidence quality (certainty ratings: High/Moderate/Low/Very Low), but this is different from a proposer's *confidence in the form decision*. No framework publishes a schema for "I believe this finding should be a Pattern with confidence 0.7; override requires written justification." The closest is IETF rough consensus, which is binary (consensus/no consensus) rather than a continuous confidence weight. The specific confidence-weighted proposer model (your Option 3) appears to have no canonical prior art — it is a novel design.

### Gap 6: Scope Creep at Codification Is Documented Anecdotally, Not Empirically
The phenomenon of "template-fitting bias" — forcing a research finding into the form of whatever artifact templates already exist — is widely discussed among practitioners but has no empirical study in the software or AI agent context. The pharma CTD literature acknowledges that CDMOs sometimes force process parameters into forms that don't match the process reality, but this is described qualitatively. No study has measured template-fitting bias across artifact types or quantified its downstream impact on implementation quality.[^39]

***

## Synthesis: Implications for Your Design

Based on the prior art, three structural recommendations emerge, each grounded in a specific domain analogy:

**On "who decides form"**: The dominant pattern across mature pipelines is a form-agnostic proposer (ATT&CK, GRADE/Cochrane, OSCAL Catalog) with a named boundary role holding form-decision authority (detection engineer, guideline panel, component definition author). The form-deciding proposer (pharma CTD) requires a mandating authority (regulatory body) to be stable — otherwise form authority drifts. If you have no equivalent mandate, the form-agnostic model with a named Architect role is more robust.

**On conflict surfacing**: The GRADE EtD dissent field is the best published model for encoding disagreement in an artifact. The key design choice is whether dissent is *in-band* (a first-class field in the proposal artifact) or *out-of-band* (a separate record). GRADE/ACIP use in-band dissent; IETF uses an out-of-band appeal process. For a knowledge-management pipeline where the artifact *is* the handoff, in-band dissent recording is simpler to maintain over time.

**On multi-target fan-out**: The OSCAL pattern (one abstract spec, multiple SSPs via reference) is more maintainable than the pharma pattern (one per target) when the abstract spec is stable and target heterogeneity is known. The Sigma pattern (one rule, mechanical translation) is most efficient when translation can be fully specified as a composable pipeline. For your system, which spans different codification forms (pattern vs. skill vs. rule vs. template), the OSCAL model — where the Proposer produces a form-agnostic finding and each Architect produces a system-specific codified artifact via reference — is more maintainable than requiring the Proposer to enumerate all target forms.

---

## References

1. [MITRE Cyber Analytics Repository: Welcome to the Cyber Analytics ...](https://car.mitre.org) - CAR analytics were developed to detect the adversary behaviors in ATT&CK. Development of an analytic...

2. [car/GLOSSARY.md at master · mitre-attack/car - GitHub](https://github.com/mitre-attack/car/blob/master/GLOSSARY.md) - MITRE ATT&CK™ is a globally-accessible knowledge base of adversary tactics and techniques based on r...

3. [Sigma Rule Translation and Automatic Queries | Optiv](https://www.optiv.com/insights/source-zero/blog/sigma-rule-translation-and-automatic-queries) - A Sigma rule can be translated to search/hunt across several SIEM and EDR platforms without the anal...

4. [An Introduction pySigma: Converting Sigma Rules to Work with Your ...](https://www.dogesec.com/blog/beginners_guide_to_using_sigma_cli_pysigma/) - Learn how to seamlessly convert Sigma Rules into queries for your SIEM. Follow along with real examp...

5. [What Are Sigma Rules? Threat Detection and Response](https://www.picussecurity.com/resource/glossary/what-is-sigma-rule) - ·

6. [What's New in MITRE ATT&CK v18: Detection Strategies and ...](https://www.picussecurity.com/resource/blog/whats-new-in-mitre-attack-v18) - # What’s New in MITRE ATT&CK v18: Detection Strategies and Analytics Unveiled

Sıla Özeren Hacıoğlu ...

7. [Chapter 14: Completing 'Summary of findings' tables and grading ...](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14) - 'Summary of findings' tables present the main findings of a review in a transparent, structured and ...

8. [How to present an informative summary of findings table for ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11795893/) - This tutorial provides guidance on creating clear and informative summary of findings tables for sys...

9. [The GRADE Evidence to Decision (EtD) framework for health system ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC5975536/) - When relevant, they may also report additional details, such as dissenting views of panel members or...

10. [Evidence-to-Decision tables - World Health Organization (WHO)](https://www.who.int/publications/i/item/9789240011908) - The purpose of EtD frameworks is to help groups of people (panels) making healthcare recommendations...

11. [[PDF] The GRADE Evidence to Decision (EtD) framework for health system ...](https://d-nb.info/1163941956/34) - When relevant, they may also report additional details, such as dissenting views of panel mem- bers ...

12. [[PDF] ACIP Evidence to Recommendation User's Guide-October 1, 2020](https://www.cdc.gov/acip/media/pdfs/2024/09/ACIP-EtR-Users-Guide_October-1-2020.pdf) - The purpose of EtR framework is to help panels making recommendations move from evidence to decision...

13. [Enhancing the Trustworthiness of the Endocrine Society's Clinical ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC9653019/) - The first of 3 new guidelines developed according to these policies and methodologies—Management of ...

14. [OSCAL Control Layer - NIST Pages](https://pages.nist.gov/OSCAL/learn/concepts/layer/control/) - In OSCAL, the controls mapping model is generalized to support mappings among any control-based arti...

15. [OSCAL Implementation Layer: System Security Plan (SSP) Model](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/) - The OSCAL system security plan (SSP) model represents a description of the control implementation of...

16. [COMPASS Part 3: Artifacts and Personas - DZone](https://dzone.com/articles/compliance-automated-standard-solution-compass-part-3-artifacts-and-personas) - The control providers also need to provide the control response and implementation status (e.g., com...

17. [Exporting Catalog, Profile, and SSP in OSCAL format - ServiceNow](https://www.servicenow.com/docs/r/xanadu/governance-risk-compliance/grc-continuous-authorization-and-monitoring-workspace/oscal-support-cam.html) - According to NIST, OSCAL SSP model enables a system owner to express the system implementation of an...

18. [Structure of the Common Technical Document (CTD)- M4 Guideline](https://biotech.com/2022/08/23/common-technical-document-ctd-m4-guideline/) - The Common Technical Document (CTD) dossier is organized into 5 Modules: · Module 1: Administrative ...

19. [Common Technical Document Overview and Benefits | GMP Pros](https://gmppros.com/common-technical-document/) - CTD consists of five modules that include administrative details, product quality, nonclinical studi...

20. [[PDF] AI Model Cards: State of the Art and Path to Automated Use](https://www.scitepress.org/Papers/2025/137066/137066.pdf) - These documents allow stakeholders to evaluate models based on inclusiveness, fairness, ethics, and ...

21. [Model Cards for Model Reporting - Google Research](https://research.google/pubs/model-cards-for-model-reporting/) - Model cards also disclose the context under which models are intended to be used, details of the per...

22. [RFC 7282 - On Consensus and Humming in the IETF](https://datatracker.ietf.org/doc/html/rfc7282) - This document explains some features of rough consensus, what is not rough consensus, how we have go...

23. [Analytic Coverage Comparison](https://car.mitre.org/coverage/) - A cross-walk of CAR, Sigma, Elastic Detection, and Splunk Security Content rules in terms of their c...

24. [Why Stage-Gate Frameworks Are the Game-Changer in Pharma ...](https://pmsoft.com/why-stage-gate-frameworks-are-the-game-changer-in-pharma-chemical-product-launches/) - Each stage focuses on specific deliverables like feasibility, formulation, validation, or technology...

25. [Model Versioning Infrastructure: Managing ML Artifacts at Scale - Introl](https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025) - Unlike traditional software versioning, ML model versioning involves tracking massive binary files, ...

26. [Pharma Tech Transfer: A Guide to the R&D to CDMO Process](https://intuitionlabs.ai/articles/pharma-tech-transfer-cdmo-guide) - Learn the critical steps for successful pharmaceutical technology transfer. This guide covers the R&...

27. [ML Model Registry | MLflow AI Platform](https://mlflow.org/docs/latest/ml/model-registry/) - The MLflow Model Registry is a centralized model store, set of APIs and a UI designed to collaborati...

28. [Trusted Committer - InnerSource Patterns](https://patterns.innersourcecommons.org/p/trusted-committer) - Achieving Trusted Committer status for a project demonstrates initiative in contributing to the comm...

29. [What Is InnerSource? A Complete Guide for 2026 | Sourcegraph Blog](https://sourcegraph.com/blog/what-is-innersource-a-complete-guide-for-2026) - Code review quality improves. When Trusted Committers review contributions from engineers outside th...

30. [Introducing the Trusted Committer Role - InnerSource Commons](https://innersourcecommons.org/learn/learning-path/trusted-committer/01/) - Think of Trusted Committers as the people in a community that you trust with important technical dec...

31. [IETF and the RFC Standards Process - catb. Org](http://www.catb.org/esr/writings/taoup/html/ietf_process.html) - The IETF standards process is designed to encourage standardization driven by practice rather than t...

32. [Running code at IETF - APNIC Blog](https://blog.apnic.net/2021/08/20/running-code-at-ietf/) - For some IETF Working Groups however, a form of requirement for implementations of a proposed specif...

33. [The NIST OSCAL Framework for State and Local Governments](https://statetechmagazine.com/article/2026/02/nist-oscal-framework-state-and-local-governments-perfcon) - NIST OSCAL replaces static security documents with machine-readable data, letting state and local ag...

34. [Characterizing and Detecting Mismatch in Machine-Learning Systems](https://www.sei.cmu.edu/blog/software-engineering-for-machine-learning-characterizing-and-detecting-mismatch-in-machine-learning-systems/) - This post describes how we are creating and assessing empirically validated practices to guide the d...

35. [Characterizing and Detecting Mismatch in Machine-Learning ...](https://www.sei.cmu.edu/library/characterizing-and-detecting-mismatch-in-machine-learning-enabled-systems/) - This paper reports findings from a study of mismatches in end-to-end development of machine-learning...

36. [Automating Mismatch Detection and Testing in ML Systems](https://www.sei.cmu.edu/annual-reviews/2022-research-review/automating-mismatch-detection-and-testing-in-ml-systems/) - We are developing a suite of tools to automate ML mismatch detection and demonstrate how to extend d...

37. [[PDF] Pharma Tech Transfer: A Guide to the R&D to CDMO ... - IntuitionLabs](https://intuitionlabs.ai/pdfs/pharma-tech-transfer-a-guide-to-the-r-d-to-cdmo-process.pdf) - Common failure modes in pharmaceutical tech transfer and recommended mitigation actions. Preventive ...

38. [Why Technology Transfer is a Bottleneck (And How to Fix It) - Mareana](https://mareana.com/blog/why-technology-transfer-is-a-bottleneck-and-how-to-fix-it/) - Summary: Technology transfer in pharma is often slowed down by fragmented data, incomplete knowledge...

39. [Tech Transfer Red Flags: 8 Early Warning Signs to Avoid Failure ...](https://www.linkedin.com/posts/carolina-ugaz-moran_scienceleadershipsoul-sls-techtransfer-activity-7404182943423909889-dFOT) - Manual quality control doesn't scale, and in pharma, even minor inspection errors can lead to recall...

40. [SIEM Threat Detection Mapped To MITRE ATT&CK And Kill Chain](https://www.netwitness.com/blog/siem-capabilities-to-mitre-attck/) - Mapping SIEM capabilities to the MITRE ATT&CK framework helps SOC teams move from collecting data to...

41. [Enterprise SIEMs miss 79% of known MITRE ATT&CK techniques](https://www.helpnetsecurity.com/2025/06/09/siem-detection-coverage/) - Enterprise SIEMs have detection coverage for just 21% of adversary techniques defined in the MITRE A...

42. [A Structured RFC Process - Phil Calçado](https://philcalcado.com/2018/11/19/a_structured_rfc_process.html) - In this document, a person or group of people will author a document describing a proposal and askin...

43. [RFC processes are a poor fit for most organizations](https://jacobian.org/2023/dec/1/against-rfcs/) - The crux of the problem with RFC processes in corporate settings is that the process, as designed, d...

44. [MITRE unveils ATT&CK v15 with upgraded detections, analytic ...](https://industrialcyber.co/threat-landscape/mitre-unveils-attck-v15-with-upgraded-detections-analytic-format-cross-domain-adversary-insights/) - Non-profit organization MITRE has unveiled ATT&CK v15, introducing improved detections, a new analyt...