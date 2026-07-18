# Harness/Orchestration-Layer Terminology and Taxonomy

Dossier for the E1 memory-spec's harness-landscape survey (Track C). Scope: the field's own vocabulary for the layer that wraps a model into an agent — dated evidence per term, then a proposed taxonomy that separates real systems better than the marketing labels do. Written 2026-07-16; every claim below is date-stamped where a primary source gives one. Recency rule applied: 2026/late-2025 usage is weighted over older usage, and drift is called out explicitly where the evidence shows it.

**Confidence key:** ✓ = confirmed against a primary source (vendor blog/docs, arxiv paper, an author's own post/tweet). ~ = confirmed against a credible secondary source (practitioner blog, journalism) but not independently traced to a primary. ? = single-source or contested; treat as provisional.

---

## §1. Glossary

### 1.1 Agent harness (and "harness" bare)

**Etymological root (background, not separately dated):** "test harness" is a decades-old software-engineering term for code that exercises a system under test. The LLM-agent sense borrows the word's connotation — a rig that holds something in place and lets it do controlled work — but is a distinct, much more recent coinage. Not evidenced further here; noted only because it explains why "harness" felt available to reach for in 2023-2024.

**Predecessor in the evals lineage (✓ 2023-03-23):** OpenAI's GPT-4 System Card documents the Alignment Research Center (ARC, led by Paul Christiano — the org that later renamed to **METR**) evaluating autonomous-replication capability: *"ARC created four simple agents by combining GPT-4 and Claude with scaffolding programs, and evaluated these agents on 12 tasks."* This is "scaffolding," not "harness" — see §1.2. It is the direct technical and institutional ancestor of what Anthropic would later call a "harness."

**Earliest specialist-literature attestation of the phrase "agent harness" (✓ 2024-12-18):** *TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks* (arxiv 2412.14161) describes the OpenHands project as providing *"a stable and strong agent harness for both web browsing and coding."* Note the usage is matter-of-fact, not a coinage announcement — the term was plausibly already circulating informally (Twitter/Discord/GitHub) before this paper, but this is the earliest dated citable instance found.

**Anthropic's adoption and canonization — the term's center of gravity in 2025-2026 (✓, primary, dated):**
- **2025-11-26**, "Effective harnesses for long-running agents" (anthropic.com/engineering): *"The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather context, plan, and execute."* First explicit lab-level "general-purpose agent harness" framing.
- **2026-01-09**, "Demystifying evals for AI agents" (anthropic.com/engineering) — the closest thing to a formal Anthropic definition: *"An agent harness (or scaffold) is the system that enables a model to act as an agent: it processes inputs, orchestrates tool calls, and returns results. When we evaluate 'an agent,' we're evaluating the harness and the model working together... Claude Code is a flexible agent harness."* Note this post also separately defines an **evaluation harness** ("the infrastructure that runs evals end-to-end") as a *different* thing that happens to share the word — a same-term/different-referent trap worth flagging when reading Anthropic's corpus.
- **2026-03-24**, "Harness design for long-running application development": harness design has "a substantial impact on the effectiveness of long running agentic coding," describes a three-agent (planner/generator/evaluator) harness architecture.
- **2026-04-08**, "Scaling Managed Agents: Decoupling the brain from the hands": decomposes **harness** (the loop that calls Claude and routes tool calls — now a stateless service) from **session** (append-only external log) from **sandbox** (execution environment) — and coins **meta-harness** for the product itself (see §1.7).

**METR's own current usage — notably *not* "harness" (✓, checked live 2026-07-16):** METR's Autonomy Evaluation Resources (evaluations.metr.org) center on **"scaffolding"** and **"elicitation"** — *"elicitation [is] the process of modifying the scaffolding around an agent to give it the best shot at succeeding"* at a task suite. "Harness" does not appear to be METR's own preferred term even now; it is the vocabulary that grew up around Anthropic/practitioner discourse, not the ARC-Evals/METR lineage that the task asked about. Also load-bearing: METR's own Time Horizon research found that Claude Code's specialized scaffold beat a generic ReAct-style baseline in only 50.7% of bootstrap samples (statistically indistinguishable from chance), and a Codex-based scaffold *underperformed* METR's own generic "Triframe" scaffold (~2026-03-04, reported via adambaitch.substack.com, secondary but citing METR's published results — flagged ~). See §4.4.

**"Harness engineering" as a named discipline — contested coinage (✓/~ 2026-02 through 2026-03):**
- **2026-02-05:** Mitchell Hashimoto (HashiCorp co-founder) publishes "My AI Adoption Journey," the earliest dated use of the phrase per available tracing.
- **2026-02-17:** Viv Trivedy (LangChain) publishes "Improving Deep Agents with Harness Engineering" (langchain.com/blog).
- **2026-03-10:** Trivedy's follow-up, "The Anatomy of an Agent Harness" (langchain.com/blog/the-anatomy-of-an-agent-harness), goes viral (~733K views, ~4.8K bookmarks on X per secondary reporting) and becomes the post the rest of the field cites. Trivedy's formula — *"Agent = Model + Harness. If you're not the model, you're the harness."* — is now the most-quoted one-line definition in the corpus (echoed by Addy Osmani 2026-04-19, O'Reilly Radar, Wikipedia's "Agent harness" article).
- Net effect: Hashimoto has priority of publication; Trivedy has the coinage the field actually adopted. The corpus itself hasn't resolved which "counts" — see §4.2.
- A **Wikipedia article titled "Agent harness"** now exists (undated, evidently created mid-2026) — itself a signal of terminology consolidation. It cites Birgitta Böckeler (Thoughtworks) drawing an **inner harness** (provided by the model builder, e.g. Claude Code's own loop) / **outer harness** (user-assembled around it) distinction, and reports the term reaching academic papers by mid-2026 (e.g., "Self-Harness," "Harness-1" — not independently verified here, flagged ~).

**Non-Anthropic vendor usage — a narrower, product-specific sense (✓):** Microsoft's Agent Framework names **"Harness"** as one of three top-level categories (alongside "Agents" and "Workflows"): *"an opinionated agent with batteries-included capabilities for long, multi-step tasks — planning and todo tracking, context compaction, file access and memory, don't-ask-again tool approval, and observability."* This is narrower than Anthropic's usage: Microsoft's Harness is one specific, swappable agent template *shipped inside* a broader framework, not the label for the whole runtime layer.

**Simon Willison's framing (✓, recurring across many dated posts 2024-2026):** *"An agent runs tools in a loop to achieve a goal"* — Willison treats "the loop" as the unit worth designing, largely orthogonal to whether you call the wrapper a harness, scaffold, or framework. His security writing (hooks, "the lethal trifecta for AI agents") is the field's clearest primary source for **enforcement living inside the harness** rather than in the prompt — see taxonomy D3.

**Denotation vs. connotation:** Denotes the code/infrastructure layer around a model that supplies state, tool dispatch, context management, and stop conditions — "everything that isn't the model" (Osmani, paraphrasing Trivedy). Connotes restraint and engineering rigor (a harness catches you if you fall) and, increasingly through 2026, a rhetorical claim that *this* is where the real engineering leverage is, not the model — a claim METR's own data complicates (§4.4).

---

### 1.2 Scaffold / scaffolding

**Earliest evidence found (✓ 2023-03-23):** OpenAI's GPT-4 System Card, describing ARC's autonomous-replication evaluation: *"ARC created four simple agents by combining GPT-4 and Claude with scaffolding programs."* This predates any documented "agent harness" usage by roughly 21 months and is the direct root of METR's present-day vocabulary (ARC Evals renamed to METR later in 2023).

**Looser, earlier metaphor lineage (? unverified):** Several secondary sources (a practitioner lexicon aggregator) assert the general "scaffolding around a model" metaphor circulated informally since "the early GPT-3 era" (2020-2021) for prompt templates and wrapper code. No specific dated primary citation for this looser claim was found in this pass — treat as plausible but unconfirmed.

**Current 2025-2026 usage — a live split:**
- **METR (✓, checked live 2026-07-16):** still the primary vocabulary — "scaffolding" and "elicitation," not "harness." This is the one clearly-identified organization for whom the older evals-era word remains dominant rather than superseded.
- **Anthropic (✓ 2026-01-09):** treats "harness" and "scaffold" as *interchangeable synonyms* — "An agent harness (or scaffold)..." (see §1.1).
- **HuggingFace's "AI Agent Glossary" (✓ 2026-05-25, huggingface.co/blog/agent-glossary):** explicitly *rejects* the synonym reading and proposes a layered relationship instead: **"Scaffolding"** = *"the behavior-defining layer around the model: system prompt, tool descriptions, how the model's responses get parsed, what it remembers across steps (context management)"* — i.e., the prompt/config content. **"Harness"** = *"the execution layer inside the agent: it calls the model, handles its tool calls, decides when to stop"* — i.e., the control-loop mechanism. Under this reading, scaffold is a *component inside* the harness, not a synonym for it. The glossary explicitly flags the ambiguity it's pushing back on: *"Products like Claude Code, Codex, and Antigravity CLI call the whole thing a harness."*

This is a genuine, currently-live (as of this dossier's writing) terminology dispute, not settled by the evidence gathered. See §4.1.

**Who uses it:** Practitioners and the safety/evals research lineage (METR/ARC) more than product vendors; Anthropic uses it as a gloss on "harness" rather than as its own preferred term; academics writing agent-benchmark papers use it descriptively ("agent scaffold," "evaluation scaffold") without much definitional fuss.

---

### 1.3 Agent framework / orchestration framework

**Technical denotation (synthesized across vendor docs, ✓):** An **agent framework** is a library/SDK exposing programmable abstractions for building agents — model clients, tool integration, memory/state, collaboration patterns. An **orchestration framework** coordinates *multiple* agents/tools/steps into workflows — routing, concurrency, durable execution, human-in-the-loop. The two are frequently bundled in one product but some vendors split them explicitly.

**The cleanest primary-source split found (✓, docs.langchain.com):** LangChain's own docs state the division outright: *"LangChain is the agent framework: abstractions and integrations for models, tools, and agent loops"* vs. *"LangGraph is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence."* This is the single most explicit framework-vs-orchestration statement found in any vendor's own words.

**Vendor self-descriptions, verbatim (✓, all current as of this research pass):**
- **LangChain:** "open source AI agent framework... pre-built agent architectures and integrations for any model or tool" (langchain.com/langchain).
- **CrewAI:** "an open-source agent framework with high-level abstractions and low-level APIs for building complex, agent-driven workflows"; GitHub tagline: "a lean, fast Python framework built specifically for **orchestrating** autonomous AI agents" — CrewAI's own marketing straddles both labels at once.
- **Microsoft Agent Framework (MAF):** the explicit successor to AutoGen + Semantic Kernel; defines *three* categories inside one product — **Agents** (individual), **Harness** (opinionated, batteries-included — §1.1), **Workflows** (graph-based orchestration: "type-safe routing, checkpointing, and human-in-the-loop support"). Rare case of one vendor using "framework," "harness," and "orchestration/workflow" simultaneously with distinct, documented meanings — the closest thing to a Rosetta stone in this corpus (learn.microsoft.com/agent-framework).
- **Google ADK (Agent Development Kit):** "the open-source agent development framework that lets you build, debug, and deploy reliable AI agents at enterprise scale" (Python/TypeScript/Go/Java/Kotlin) (adk.dev).
- **AutoGen** (Microsoft Research): "an open-source programming framework for building AI agents and facilitating cooperation among multiple agents to solve tasks."
- **Semantic Kernel Agent Orchestration:** ships named coordination patterns — concurrent, sequential, handoff, group chat, Magentic — as an "experimental" module distinct from the core Agent Framework, requiring a separate `Agents.Runtime.InProcess` package.
- **OpenAI Agents SDK:** avoids "framework" language; frames the choice as Responses API (developer "owns the loop") vs. Agents SDK ("the SDK runs it" — a managed loop).
- **Temporal:** pre-LLM, general-purpose durable-workflow orchestrator, increasingly used as the substrate *under* agent frameworks for retries/state/durability — orchestration in the classical distributed-systems sense, agent-agnostic.

**Earliest notable usage in the LLM context:** Diffuse — no single coinage moment identified. AutoGen (Microsoft Research, ~2023) and LangChain's progressive rebrand toward "agent framework" language (2023-2024) are the clearest early anchors. This is a term that accreted through repeated vendor branding rather than launching in one paper or post.

**Who uses it:** Overwhelmingly vendor marketing (LangChain, CrewAI, Microsoft, Google, OpenAI); practitioners use it loosely and often interchangeably with "orchestration framework"; academics prefer "multi-agent systems" or "agentic AI" over either specific phrase.

---

### 1.4 Agent runtime

**Technical denotation (✓, synthesized across docs):** The execution environment that actually runs agent loops/workflows — schedules steps, persists state, streams output, supports human-in-the-loop pauses/resumption, survives process restarts. Positioned by multiple vendors as "the execution half" of an orchestration framework.

**Primary examples:**
- **LangGraph's `Runtime` object** (docs.langchain.com/oss/python/langchain/runtime): exposes context (static deps like user ID/DB connections), a long-term-memory store, a stream writer, execution info (thread ID/run ID/retry count), and server info (assistant ID/graph ID) — dependency injection for tools and middleware.
- **LangChain's "The Runtime Behind Production Deep Agents"** (langchain.com/blog): frames durable execution — survive restarts, pause for human approval, run for hours — as the defining runtime capability that separates prototypes from production agents.
- **AutoGen v0.4:** an asynchronous, event-driven architecture functioning as a multi-agent runtime; per third-party reporting (dev.to/maximsaplin), Microsoft folded this into Semantic Kernel as a distinct `Agents.Runtime.InProcess` package.
- **OpenAI Agents SDK:** implicitly defines "runtime" as whichever side "owns the loop" — a managed runtime when you use the Agents SDK, a self-built one when you use the bare Responses API.

**Connotation:** production-grade robustness, operational control, platform-level reusability across multiple frameworks; a lock-in risk connotation when the runtime is proprietary/managed.

**Relationship to harness:** A harness (Claude Code, Microsoft's Harness) is typically built *on top of* a runtime, consuming its state/scheduling/persistence primitives while presenting a simplified, opinionated interface. "Runtime" denotes the engine; "harness" denotes the finished, opinionated vehicle built on that engine.

---

### 1.5 Agent OS / LLM OS / AIOS

Three related-but-distinct threads, in chronological order — useful precisely because the gap between the earliest (rigorous, narrow) and the latest (loose, broad) usage is unusually wide.

**(a) MemGPT's "LLM as Operating System" (✓ 2023-10-12, arxiv 2310.08560):** *"MemGPT: Towards LLMs as Operating Systems,"* Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph E. Gonzalez (UC Berkeley). Technical core: **virtual context management**, explicitly modeled on OS hierarchical/virtual memory — a small in-context "scratchpad" (physical-RAM analog) plus a much larger paged "external context" (disk analog), with interrupts managing control flow between tiers. Evaluated on document analysis (exceeding native context limits) and multi-session chat (long-term memory across sessions). MemGPT's authors later founded **Letta**, carrying the OS metaphor into a commercial product (§1.6).

**(b) Karpathy's "LLM OS" (✓ 2023-11-09, x.com/karpathy/status/1723140519554105733):** *"LLM OS. Bear with me I'm still cooking. Specs: - LLM: OpenAI GPT-4 Turbo 256 core (batch size) processor @ 20Hz (tok/s) - RAM: 128Ktok - Filesystem: Ada002..."* Maps LLM→CPU, context window→RAM, an embeddings-based vector store→filesystem, tools/internet/other-LLMs→peripherals. Purely evocative/pedagogical — a viral tweet and conference-talk framing, never a shipped system — but, per multiple secondary sources, it was "a hot topic" through 2024 and is widely cited as the popular on-ramp to the "LLM/agent OS" framing that MemGPT had already formalized a month earlier.

**(c) AIOS — the one genuine kernel implementation (✓, arxiv 2403.16971, submitted 2024-03-25, later published as a conference paper at COLM 2025):** *"AIOS: LLM Agent Operating System,"* Rutgers University (Kai Mei, Zelong Li, et al.). Proposes an actual **AIOS kernel** isolating LLM-specific services from agent applications: **Agent Scheduler** (prioritizes/schedules agent requests to optimize LLM utilization), **Context Manager** (snapshot/restore intermediate generation state), **Memory Manager**, **Storage Manager**, **Tool Manager** (external API calls), **Access Manager**, and an **"LLM system call interface."** Reports up to 2.1× faster execution serving agents built on various existing agent frameworks. This is the most literally OS-shaped of the three — kernel, scheduler, and syscalls are proposed subsystems, not just metaphor.

**(d) 2025-2026 vendor dilution (✓/~ dated):** "Agent OS" as enterprise marketing has drifted far from (a)-(c)'s technical content:
- **Fiserv "agentOS"** (✓, investors.fiserv.com, launched 2026-05-14, "widely available by ~August 2026" per reporting): an enterprise banking orchestration/governance layer for deploying agents across financial-institution workflows. No scheduler, no memory-paging concept.
- **PwC's "agent OS"** (✓, pwc.com/us/en/services/ai/agent-os.html): a multi-vendor agent-orchestration-and-oversight layer for enterprises, framed around "platform-agnostic" governance and state management.
- **Agno's "AgentOS"** (~): open-source, closer to the academic sense in spirit — serves agents/teams/workflows as FastAPI APIs with shared memory/knowledge/MCP tool access — but it is a serving/deployment framework, not a memory-paging kernel.
- **buildermethods/agent-os** (GitHub, ✓ exists as of this research pass): a spec-driven-development toolkit for injecting codebase standards into coding-agent workflows — arguably the furthest drift, using "OS" essentially as a brand suffix unrelated to any kernel or scheduling concept.

Four unrelated things ("agentOS"/"AgentOS"/"agent-os"/"agent OS") shipped under near-identical names within about a year of each other, none of them implementing what AIOS or MemGPT actually proposed. See §4.5.

---

### 1.6 ADE — Letta's Agent Development Environment

**Company background (✓):** Letta is the renamed/spun-out company built by the MemGPT research team (UC Berkeley); emerged from stealth September 2024 with a $10M seed round.

**Product launch (✓ 2025-01-15, per x.com/Letta_AI/status/1879575590191432011 and letta.com/blog/introducing-the-agent-development-environment):** **ADE (Agent Development Environment)** launched to public beta. Letta's own framing: *"a visual development environment that brings unprecedented transparency to agent design and debugging."*

**What it does (✓, docs.letta.com/guides/ade/overview):** A Context Window Viewer (exact contents of an agent's context at any point), a Core Memory panel (read/edit memory blocks directly), an archival-memory browser with search, and a tool editor (write/test Python tool code with mock inputs before attaching it to an agent). Explicit selling point: transparency into an agent's context window and memory systems — a debugging/design tool for *stateful* agents specifically, consistent with Letta's MemGPT lineage.

**Generic usage:** No evidence found of "ADE" being adopted as a generic industry category label the way "IDE" is for code editors in general. It functions as a **single-vendor product name**, not (yet) a term other vendors have picked up for their own equivalent tooling. This is worth stating plainly: unlike "harness," "framework," or "runtime," which multiple vendors independently converged on, ADE has exactly one referent in the evidence gathered.

---

### 1.7 Meta-harness / agent platform (the Databricks Agent Bricks pattern)

Two threads worth separating carefully: (i) Anthropic's own explicit "meta-harness" coinage, which is contested even within its own micro-lineage; and (ii) the broader "platform that wraps, runs, evaluates, and optimizes agents" pattern, which the field mostly calls **agent platform**, and for which Databricks Agent Bricks is the canonical, best-documented example.

**(i) Anthropic's "meta-harness" (✓ 2026-04-08, "Scaling Managed Agents: Decoupling the brain from the hands," anthropic.com/engineering/managed-agents):**
> *"Managed Agents is a meta-harness in the same spirit, unopinionated about the specific harness that Claude will need in the future. Rather, it is a system with general interfaces that allow many different harnesses."*
> *"Meta-harness design means being opinionated about the interfaces around Claude"* while staying implementation-agnostic.

Three decoupled primitives underlie this: **harness** (the loop that calls Claude and routes tool calls — now a stateless service, no longer fused to a container), **session** (the append-only external log of everything that happened — durable, queryable, independent of which harness is running), **sandbox** (the execution environment where Claude runs code/edits files — a swappable tool interface). In this sense, meta-harness = a hosting/abstraction substrate that many different, possibly swappable, harnesses run on top of — structurally analogous to a hypervisor sitting "above" the VMs it hosts. Anthropic explicitly names Claude Code as one harness this substrate can run: *"Claude Code is an excellent harness that we use widely across tasks."*

**(ii) A conflicting "meta-harness" sense, same word (~, alexlavaee.me/blog/meta-harness-automated-agent-optimization/):** Defines meta-harness as *"a harness that optimizes harnesses — one level of abstraction above the agent scaffolding itself"*: a coding agent (Claude Code with Opus) that iteratively proposes, evaluates, and rewrites *other* harnesses' source code — ~20 iterations over ~60 harness candidates, benchmarked on TerminalBench-2. This is a **self-improving optimizer agent**, not a hosting substrate — genuinely incompatible with Anthropic's sense despite near-identical coinage timing and identical wording. See §4.3.

**(iii) Databricks Agent Bricks — the canonical eval/optimize-loop platform (✓, dated):**
- **2025-06-11:** Announced at Data + AI Summit 2025, launched in **Beta** (databricks.com/blog/introducing-agent-bricks).
- What it does, per Databricks' own description: a developer specifies the agent's *purpose* plus natural-language quality guidance; Agent Bricks auto-generates a task-specific evaluation suite (synthetic data + "custom judges," powered by MLflow 3 and Mosaic AI Research techniques), then auto-optimizes the agent by searching/combining prompt engineering, model fine-tuning, reward models, and "test-adaptive optimization (TAO)" — with a user-facing choice between cost-optimized and quality-optimized outputs.
- **2026-06 (Data + AI Summit 2026):** reached **General Availability** (databricks.com/blog/agent-bricks-dais-2026), reporting 100,000+ agents built and 1+ quadrillion tokens/year processed through the product by that point.
- Structurally: Agent Bricks is a **build → eval → optimize → redeploy loop wrapped around an agent**, operated continuously as an ops-layer service. It does not define a new agent-authoring framework; it operates *on* agents authored elsewhere.

**(iv) Other instances of the same pattern (✓/~, 2026 landscape):**
- **Braintrust "Loop"** (braintrust.dev): *"automates the improvement cycle by analyzing failure patterns, generating better prompts, creating targeted datasets, and writing new scorers"* — trace-to-dataset integration, automated prompt optimization, CI/CD quality gates.
- **LangSmith "Engine"** (per LangChain's own langsmith-vs-braintrust comparison): clusters production traces into prioritized issues automatically, suggests a PR to fix the issue, and auto-creates offline evals to prevent regression — ties development, eval, monitoring, and improvement into what LangChain calls "a single loop."
- **Galileo** (~, per third-party comparison at latitude.so): has a strong eval-to-guardrail runtime-safety lifecycle but, per that comparison, narrower auto-improvement tooling than Braintrust/LangSmith — a useful negative case showing this pattern is a spectrum, not a binary "has it / doesn't."

**(v) "Agent platform" as a broader, looser umbrella, independent of any auto-optimize loop (~, rierino.com "What Is an Agentic Platform? A 2026 Guide"):** defines an agentic platform as combining *"autonomous decision-making with cross-domain execution under enterprise governance... the operating layer beneath every agent the business runs,"* distinguished from open-source frameworks (*"libraries... you're responsible for production-grade observability, retry logic, state persistence, and governance"*) mainly by being managed/hosted, typically at enterprise pricing (one source cites "$300K+/year for the incumbents"). Vendors named in this 2026 landscape include Microsoft, Salesforce, IBM, ServiceNow, Google, AWS, and UiPath — note that most of these do **not** necessarily ship an auto-eval-optimize loop the way Agent Bricks/Loop/Engine do. "Agent platform" is the broader enterprise-governance umbrella; the closed-loop-optimization pattern the task specifically asked about is a narrower thing living inside some, not all, "agent platforms." Keep these two senses distinct — collapsing them overstates how many "platforms" actually do what Agent Bricks does.

---

### 1.8 Code-first vs. LLM-first (workflow vs. agent / "who owns the loop")

Yes — this is explicitly named in the field, with a clear primary-source origin and at least one directly traceable descendant.

**Origin (✓ 2024-12-19, anthropic.com/research/building-effective-agents, "Building Effective Agents"):**
> **Workflows** are *"systems where LLMs and tools are orchestrated through predefined code paths."*
> **Agents** are *"systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."*

The essay frames workflows as decomposing a task into "a sequence of steps" with "programmatic checks" at predetermined points — suited to well-defined tasks with a fixed/predictable subtask count — versus agents, which "plan and operate independently" on open-ended problems where the number of required steps can't be predicted in advance. This *is* explicitly a control-flow-ownership distinction: who decides "what happens next" — code written in advance, or the model reasoning live.

**Direct descendant (✓ 2025-04-17, OpenAI, "A Practical Guide to Building Agents," openai.com / cdn.openai.com PDF):** Converges on essentially the same axis roughly four months later, in OpenAI's own vocabulary rather than Anthropic's: *"a workflow is a sequence of steps that must be executed to meet the user's goal"* vs. an agent defined by possessing several capabilities together, including that it *"leverages an LLM to manage workflow execution and make decisions,"* *"recognizes when a workflow is complete"* and can *"halt execution and transfer control back to the user"* on failure, and *"dynamically selects the appropriate tools."* The line is drawn in the same place — who manages execution and decides completion/failure — via independently-worded convergence, not copied language. This is good evidence the axis is real and not just one lab's branding.

**Practitioner naming of the same axis, different words (~, no single canonical coiner found):** "Who owns the control flow" — "a human writing code in advance, or a model reasoning at runtime" / "code-driven" vs. "model-driven" — recurs across multiple 2025-2026 secondary sources (orkes.io "Agentic AI Explained: Workflows vs Agents," machinelearningmastery.com, IntuitionLabs) as a distillation of Anthropic's original essay rather than an independent coinage event.

**A different "code-first" sense — action-space form, not loop ownership (? emerging, 2026 arxiv preprints, not yet peer-reviewed as far as verified):** "LLM-as-Code: Agentic Programming for Agent Harness" (arxiv 2606.15874) and "Code as Agent Harness" (arxiv 2605.18747) propose that an agent's *action space* should be executable code rather than a fixed menu of JSON/text tool-calls — reporting up to 20% higher task-success versus JSON-based action formats, attributed to code's native support for composition, dynamic revision, and self-debugging via a REPL. **This is a different axis than workflow-vs-agent** — it's about the *form* of what the model emits (code vs. structured tool-call), not about who decides the next step. The two "code-first" senses share a word but not a referent; conflating them would be a mistake. Flagged as emerging/unsettled given the recency and lack of independent replication found.

**Adjacent framing, not quite the same axis (✓ 2025-09-30, simonwillison.net/2025/Sep/30/designing-agentic-loops/):** Simon Willison's "Designing agentic loops" and his recurring one-liner *"an agent runs tools in a loop to achieve a goal"* treat "the loop" as the unit of design regardless of nominal ownership — a slightly different emphasis (loop-as-artifact) than the workflow/agent binary (loop-ownership-as-classifier). Maps more cleanly onto taxonomy dimension D3 (enforcement locus) than onto D1 below.

**State-of-the-field reality check (~, IntuitionLabs 2025 analysis):** *"AI workflows — not fully autonomous agents — won the production battle in 2025: workflows remain the dominant pattern behind successful generative AI deployments, while fully autonomous multi-agent systems are still largely exploratory outside of narrow domains."* Useful dated data point: the code-first/workflow pole is currently winning in production even as the model-first/agent pole dominates discourse.

---

## §2. Proposed taxonomy dimensions

The marketing terms in §1 do not cleanly separate real systems — the same word ("harness," "OS," "platform") gets used for architecturally unrelated things, and architecturally identical things get marketed under different words depending on vendor. The six dimensions below are proposed as a better cut: each is a real technical axis with observable poles, evidenced by the vendor/academic sources above, and largely independent of the others (a system's position on one doesn't determine its position on another).

### D1 — Control-loop ownership: code-driven ↔ model-driven
**What it separates:** who decides "what happens next" at each step.
- **Pole A, code-driven ("workflow"):** the sequence of LLM calls is fixed at write time; the model fills content into slots but doesn't choose which step runs next. *Examples: Anthropic's prompt-chaining/routing/parallelization workflow patterns; LangGraph graphs with code-defined edges; Semantic Kernel's "sequential"/"concurrent" orchestration patterns.*
- **Pole B, model-driven ("agent"):** the model chooses the next tool call and decides termination; code supplies only loop mechanics and tool implementations. *Examples: Claude Code / Claude Agent SDK; OpenAI Agents SDK in agent mode; bare ReAct loops; METR's generic scaffold baseline.*
- Genuinely a spectrum, not a binary: most production systems (CrewAI crews, Semantic Kernel's "handoff"/"group chat" patterns, MS Agent Framework's graph Workflows connecting Agent nodes) mix both — code owns macro-structure, the model owns micro-decisions inside each node.

### D2 — Persistence model: ephemeral ↔ durable external state
**What it separates:** what, if anything, survives between invocations, and where it lives relative to the running process.
- **Pole A, ephemeral:** state lives entirely in the current context window; nothing survives process exit except what a user manually saves. *Examples: a bare ReAct loop; METR's "simple scaffold" baseline; a single Responses-API call.*
- **Pole B, durable external store, decoupled from the runtime process:** memory/session data lives in a separately persisted store, addressable independent of which harness process is currently running. *Examples: Letta/MemGPT's tiered memory (in-context + paged archival); Anthropic Managed Agents' "session" object (explicitly decoupled from the harness process, 2026-04-08); AIOS's Context Manager (snapshot/restore); LangGraph's checkpointing/persistence layer.*

### D3 — Enforcement locus: prompted/advisory ↔ structurally enforced
**What it separates:** whether a guardrail is a request the model can be talked out of, or something the surrounding system makes physically impossible to violate.
- **Pole A, advisory (prompt-level):** guardrails are natural-language instructions (system prompt, CLAUDE.md/AGENTS.md, "don't do X") that a sufficiently adversarial context can still override. *Examples: plain system-prompt policies; most out-of-the-box scaffold "guidelines."*
- **Pole B, structurally enforced (code/sandbox-level):** the harness or its sandbox makes the disallowed action impossible regardless of what the model decides. *Examples: Claude Code's hooks (PreToolUse/PostToolUse — Willison's framing: hooks separate "I told the agent to do X" from "the system enforces X"); Anthropic Managed Agents' decoupled sandbox primitive; MCP tool allow-lists; MS Agent Framework's Harness "don't-ask-again tool approval" gates.*
- This is the axis the field names least explicitly as its own thing, but it's real and load-bearing: two systems can be identical on D1 (both "agents," model-driven) and completely different in enforcement posture.

### D4 — Coordination topology: single-loop ↔ fixed multi-agent graph ↔ dynamic/emergent multi-agent
**What it separates:** how many agents are involved, and whether their interaction structure is fixed at design time or negotiated at runtime.
- **Pole A, single-loop:** one model, one loop, N tools. *Examples: a bare Claude Code session; a lone ReAct agent.*
- **Pole B, fixed multi-agent graph:** multiple agents/roles, topology defined in code ahead of time. *Examples: CrewAI "crews"; Semantic Kernel's sequential/concurrent/handoff patterns; MS Agent Framework's graph-based Workflows.*
- **Pole C, dynamic/emergent multi-agent:** agents spawn other agents or negotiate handoffs at runtime; full topology isn't known until execution. *Examples: Claude Code subagents (spawned on demand mid-session); AutoGen's event-driven group chat; Semantic Kernel's Magentic-style orchestration; Anthropic's generator/evaluator/planner architecture (2026-03-24 post).*

### D5 — Lifecycle layer: dev-time ↔ run-time ↔ ops-time
**What it separates:** *when* in the software lifecycle the tool operates — while a human designs/debugs the agent, while the agent executes live, or after deployment while monitoring/improving it. This is the dimension that most cleanly resolves the apparent overlap between ADE, harness, and meta-harness/agent-platform — three terms that sound like competitors but actually occupy three different lifecycle stages.
- **Pole A, dev-time:** used by a human designing/debugging an agent, off the production execution path. *Examples: Letta's ADE (context-window viewer, memory editor, tool tester); Google ADK's debugging tooling.*
- **Pole B, run-time:** executes as part of the live agent loop, on the critical path of every task. *Examples: Claude Code / Claude Agent SDK; LangGraph's Runtime object; AIOS kernel's scheduler/context manager during execution.*
- **Pole C, ops-time:** wraps already-deployed agents from outside, observing and improving them without sitting in the per-turn critical path. *Examples: Databricks Agent Bricks (auto-eval + auto-optimize loop); Braintrust Loop; LangSmith Engine.*

### D6 — Packaging/control layer: assemble-it-yourself library ↔ opinionated product ↔ infrastructure substrate ↔ managed service
**What it separates:** how much is pre-decided for you, and at what altitude the vendor is actually selling.
- **Pole A, library/SDK ("framework"):** primitives + integrations; you write the glue and own operations. *Examples: LangChain; Google ADK; AutoGen; Semantic Kernel's Agent Framework.*
- **Pole B, opinionated finished product ("harness"):** batteries-included, specific defaults, but still something you run yourself. *Examples: Claude Code; Cursor; MS Agent Framework's "Harness" category.*
- **Pole C, infrastructure substrate ("OS"/"kernel"/Anthropic's "meta-harness"):** virtualizes resources (memory, scheduling, tool access) that multiple agents or harnesses share underneath. *Examples: AIOS kernel; MemGPT's virtual-context-management layer; Anthropic Managed Agents (its own "meta-harness" sense).*
- **Pole D, managed/hosted service ("platform"):** the vendor runs it for you, usually with an eval/governance/optimization loop and enterprise pricing; you supply intent, not infrastructure. *Examples: Databricks Agent Bricks; Anthropic Managed Agents (also here — it straddles C and D); enterprise "agentic platforms" (PwC agent OS, Fiserv agentOS).*

---

## §3. Term → dimension mapping table

How the marketing terms from §1 collapse onto the dimensions from §2. Where a term maps to more than one dimension, the dominant one is listed first.

| Marketing term | Primary dimension(s) | Typical pole(s) | Notes |
|---|---|---|---|
| **agent harness** / bare "harness" | D6 (packaging), D5 (lifecycle) | D6→B (opinionated product); D5→B (run-time) | Anthropic explicitly separates plain "harness" (D6-B, D5-B) from its own "meta-harness" (D6-C/D) — same root word, different taxonomy cell |
| **scaffold / scaffolding** | D6 (packaging) | D6→B, or narrower per HF's reading (the config/prompt sub-layer *inside* D6-B) | METR's usage skews to the narrower sense: modifiable configuration around a fixed loop, not the whole loop |
| **agent framework** | D6 (packaging) | D6→A (library) | Sometimes bundles a harness as a shipped sub-product (MS Agent Framework ships "Harness" as one of its own categories) |
| **orchestration framework** | D4 (coordination topology), D6 | D4→B (fixed multi-agent graph); D6→A | LangGraph self-labels "orchestration runtime," blending D6-A marketing language with a D5-B (run-time) function |
| **agent runtime** | D5 (lifecycle: run-time), D2 (persistence) | D5→B; D2→B (durable, checkpointed) | Marketed as "the execution half" of an orchestration framework — i.e., D4's mechanism made concrete |
| **agent OS / LLM OS / AIOS** | D6 (packaging: substrate), D2 (persistence) | D6→C; D2→B | 2025-2026 enterprise usage (Fiserv, PwC) drifts to D6→D (platform) despite the "OS" name — the academic sense (AIOS, MemGPT) stays honestly at D6→C |
| **ADE** | D5 (lifecycle: dev-time) | D5→A | Single-vendor term; carries no independent D1/D4/D6 content of its own — purely a lifecycle-stage label |
| **meta-harness** (Anthropic sense) | D6 (packaging: substrate) | D6→C | "Unopinionated about the specific harness" is literally the D6-C definition |
| **meta-harness** (alexlavaee.me sense) | D5 (ops-time) crossed with self-application of D1 | Not a hosting layer at all — an ops-time optimizer that *targets* other systems' D1/D6 properties | Conflicts with Anthropic's sense; §4.3 |
| **agent platform** / Agent Bricks pattern | D5 (ops-time), D6 (managed service) | D5→C; D6→D | The clearest current real-world instance of D5-C combined with D6-D |
| **workflow** (in "workflow vs agent") | D1 (control loop) | D1→A | |
| **agent** (in "workflow vs agent") | D1 (control loop), D4 | D1→B; D4 varies | "Agent" alone says nothing about D4 — a single-loop ReAct agent and a dynamic multi-agent swarm are both "agents" on D1 |
| **code-first / "LLM-as-Code"** | Looks like D1 but is actually orthogonal to it — a separate axis (action-space form: code emission vs. structured tool-call emission) | N/A on D1 as defined here | Risk of conflating with workflow-vs-agent is real and worth guarding against explicitly (§1.8) |

---

## §4. Open disputes

Places where the evidence gathered shows the field genuinely disagreeing, not just using imprecise language.

### 4.1 Is "scaffold" a synonym for "harness," or a component inside one?
Anthropic (2026-01-09) treats them as interchangeable: "an agent harness (or scaffold)." HuggingFace's AI Agent Glossary (2026-05-25) explicitly rejects that reading, making scaffold the prompt/context-shaping content *inside* a harness's execution-loop mechanism — scaffold ⊆ harness, not scaffold = harness. Both sources are current as of this dossier and neither cites or rebuts the other. Unresolved.

### 4.2 Who coined "harness engineering" — and does priority or popularization decide?
Mitchell Hashimoto published the phrase first (2026-02-05). Viv Trivedy's later post (2026-03-10) is what actually made the term stick industry-wide (733K views, the formula everyone now quotes). The corpus hasn't settled whether "coined" means "published first" or "made it a real category" — most retrospective pieces hedge by crediting both, unevenly.

### 4.3 "Meta-harness" — hosting substrate, or self-optimizing agent?
Anthropic's Managed Agents sense (2026-04-08): infrastructure that is agnostic to which harness runs on top of it — a hypervisor-like substrate. alexlavaee.me's sense (dated close to the same window): a harness whose *job* is to iteratively rewrite and improve other harnesses' code — a self-improving optimizer. These are not compatible readings of the same word, and both surfaced in roughly the same few months of 2026 with no evidence either author was aware of the other's usage.

### 4.4 Does the harness actually matter more than the model — or is that itself contested?
A whole genre of 2026 posts (MongoDB's blog, citing Princeton's CORE-Bench; Cursor's own research; aakashdhar.me; the general "harness > model" rhetorical move repeated across a dozen sources in this research pass) claims scaffold/harness choice swings benchmark scores by 30+ points and matters more than model selection. METR's own Time Horizon research — from the organization with the longest continuous history of building and studying these things — found close to the opposite on their benchmark: Claude Code's specialized scaffold beat a generic ReAct baseline in only 50.7% of bootstrap samples (statistically a coin flip), and a Codex-based scaffold *underperformed* METR's own generic "Triframe" scaffold. This is not merely a terminology dispute; it's an empirical disagreement between the term's most prolific 2026 popularizers and the term's original technical home, and the dossier's evidence does not resolve it either way.

### 4.5 Is "Agent OS" a real infrastructure category, or has the name outrun the concept?
AIOS (Rutgers, COLM 2025) and MemGPT (Berkeley, 2023) use "OS" for genuinely kernel-shaped subsystems — a scheduler, a syscall interface, paged memory management. 2025-2026 enterprise products (Fiserv agentOS, PwC agent OS, and arguably buildermethods/agent-os) use "OS" for governance, orchestration, or coding-standards layers with no scheduler or memory-paging concept anywhere in them. At least four unrelated products now carry near-identical "agent OS" branding. Whether this is healthy category consolidation or pure name-borrowing from an evocative academic metaphor is not resolvable from the evidence gathered — it reads more like the latter, but no source directly addresses the question.

### 4.6 Framework vs. platform — an architectural distinction, or a pricing tier?
The 2026 enterprise-vendor framing (rierino.com and similar) distinguishes "framework" (open-source library, you own the ops burden) from "platform" (managed, governed, "$300K+/year for the incumbents") largely along commercial lines. Anthropic's own session/harness/sandbox decoupling (§1.7-i) suggests there *is* a real architectural distinction available (decoupled, swappable primitives vs. a monolithic library) — but the broader enterprise-vendor evidence gathered doesn't cleanly show whether "platform" vendors are actually shipping that kind of decoupled architecture, or whether "platform" is mostly a repackaging of similar capabilities at enterprise pricing with a governance veneer. Flagged as unresolved rather than answered.

---

## Sources consulted (primary, by date)

- 2023-03-23 — OpenAI, *GPT-4 System Card* (ARC/scaffolding) — cdn.openai.com/papers/gpt-4-system-card.pdf
- 2023-10-12 — Packer et al., *MemGPT: Towards LLMs as Operating Systems* — arxiv.org/abs/2310.08560
- 2023-11-09 — Karpathy, "LLM OS" — x.com/karpathy/status/1723140519554105733
- 2024-03-25 — Mei et al., *AIOS: LLM Agent Operating System* — arxiv.org/abs/2403.16971 (COLM 2025)
- 2024-12-18 — *TheAgentCompany* — arxiv.org/abs/2412.14161
- 2024-12-19 — Anthropic, "Building Effective Agents" — anthropic.com/research/building-effective-agents
- 2025-01-15 — Letta, "Introducing the Agent Development Environment" — letta.com/blog
- 2025-04-17 — OpenAI, "A Practical Guide to Building Agents" — openai.com
- 2025-06-11 — Databricks, "Introducing Agent Bricks" — databricks.com/blog
- 2025-09-30 — Willison, "Designing agentic loops" — simonwillison.net
- 2025-11-26 — Anthropic, "Effective harnesses for long-running agents" — anthropic.com/engineering
- 2026-01-09 — Anthropic, "Demystifying evals for AI agents" — anthropic.com/engineering
- 2026-02-05 — Hashimoto, "My AI Adoption Journey" (harness engineering, first published use)
- 2026-02-17 / 2026-03-10 — Trivedy (LangChain), "Improving Deep Agents with Harness Engineering" / "The Anatomy of an Agent Harness" — langchain.com/blog
- 2026-03-24 — Anthropic, "Harness design for long-running application development" — anthropic.com/engineering
- 2026-04-08 — Anthropic, "Scaling Managed Agents: Decoupling the brain from the hands" — anthropic.com/engineering/managed-agents
- 2026-05-14 — Fiserv, "agentOS" launch — investors.fiserv.com
- 2026-05-25 — HuggingFace, "AI Agent Glossary" — huggingface.co/blog/agent-glossary
- 2026-06 — Databricks, "Agent Bricks: Data + AI Summit 2026" (GA) — databricks.com/blog

Plus vendor docs without a single dated post (checked live 2026-07-16): learn.microsoft.com/agent-framework, docs.langchain.com (LangGraph/LangChain runtime), docs.letta.com/guides/ade, evaluations.metr.org, adk.dev, langchain.com/langchain, crewai.com, mongodb.com/company/blog (harness-vs-platform), rierino.com (agentic platform definition), en.wikipedia.org/wiki/Agent_harness.
