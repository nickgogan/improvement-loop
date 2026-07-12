# Transcript: Anthropic Might Buy Atlassian For $40B. Here's Why It Makes Sense.

**URL:** https://www.youtube.com/watch?v=FDkvRl1RlT0
**Segments:** 891
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 29:07
**Uploaded:** 2026-05-02

---

## Full Text

This is the story of one of the most surprising software categories of 2026. And I'm talking about the issue trackers that are the substrate for AI agents now and were never built to be that. They weren't. Sometimes the programs we build for ourselves turn out to be accidentally useful to agents. I think it's one of the most fascinating stories of 2026 and they weren't ever designed for AI. They still aren't. They became useful because they happened to encode something that agents desperately need like state, like ownership, like permissions or history, or even a clean idea of what should happen next. Issue trackers is my favorite example. It's the most boring software in the engineering stack. I'm not going to pretend to you it's exciting. It's the thing people complain about. It's Jira, right? It's the thing that feels like process overhead, the thing everyone wants to make simpler and lighter and invisible. And yet, the issue tracker is quietly becoming one of the most important pieces of agent infrastructure out there right now. Because if you want agents to do real work, the hard part is not just making the model smarter. The hard part is giving the agent a place to find the work, a place to understand who owns the work, to know what state it's in, to see what changed, to ask for a review, and to hand the result back. That's exactly what issue trackers were built to do for people. They were built for handoffs, for memory, for accountability, for dependencies, for review. And by accident, those are almost exactly the things agents need. And that is why one small product story from the last month matters a lot more than it looks. Linear CEO published a letter saying issue tracking is dead. And just a little over a month later, OpenAI published Symphony, an open-source Codex orchestration spec whose central idea is to use an issue tracker, specifically a Linear board, as the control plane for autonomous coding agents. That is the entire contradiction of this space in 2026. The issue tracking experience might be dying, the issue tracking substrate is getting promoted. The old habit of humans manually translating messy reality into tickets, that's absolutely under pressure. But the underlying structure of the issue tracker, the state machine, the assignee field, the audit trail, the dependency graph, it's all underneath that UI, that's becoming more valuable, not less. And once you see why issue trackers work for agents, you can start spotting the same pattern in a lot of other places. CRMs, service desks, ERPs, calendars, source control, HR systems, finance systems, a lot of the programs we've already written are more agent useful than they look. And so this video, yeah, it's about issue trackers, but it's also about a much larger question. Which boring tools did we accidentally build that agents are going to need? And I want to walk through four pieces of that. First, why agents need something that looks suspiciously like an issue tracker. Second, why the boring infrastructure we built for human coordination turns out to fit agent coordination almost perfectly. Third, why Atlassian, Linear, Salesforce, ServiceNow, and a bunch of unsexy enterprise tools are suddenly sitting on something much more strategic than people realized. And fourth, how to tell which tools in your company are going to become that kind of agent infrastructure and which ones are going to get wrapped up or replaced. But the short version is this, the boring tools are winning in 2026. The really interesting question now is which boring tools win next and why. Let's go back to that Linear letter for a minute because the argument that Karri made was actually very reasonable. So on March 24th, uh Karri, the CEO of Linear, published a page called Issue Tracking Is Dead. And the basic idea was that issue trackers were built for a handoff model of software development. Uh they were built for a world where the product manager scopes the work and someone else writes the ticket and someone else picks it up later and the ticket moves through various statuses and people argue about priority and acceptance criteria and ownership and roadmaps and dependencies, whether something is a bug or a feature, and very slowly the system that was supposed to help the work becomes a big part of the work. This gets at what Linear was originally designed to solve and it is a real problem. And I want to emphasize that I have used both Linear and Jira. I see why we switched to Linear. Linear is fast, it's intuitive. I get why if you're using an issue tracker to solve this problem, you make the switch. But regardless of whether you've used Linear personally, you've probably used a ticketing system. If you've worked inside Jira or any heavily customized project management system, you know exactly what this feels like. The ticket ends up being a translation layer between reality and the team. A customer has a problem, a designer has an idea to solve it, an engineer sees a bug, a support person hears the same complaint five times. All of that messy context has to go somewhere. It gets It gets compressed into a record with a title and a description and an owner and a state and maybe a due date. That compression is useful, but it's also expensive. And so when Kari Saarinen was writing his essay, he pointed out agents change this picture. Agents can read more of the underlying context. They can look at raw customer feedback and internal discussion and product decisions at code at docs. They don't necessarily need a human to do as much of that translation step first. And Linear's answer is to become less like a place where people manually move tickets around and more like a shared product system where context turns into execution. Linear agent skills, automations, code intelligence, code depths, and eventually a coding agent that writes code and fixes bugs with native Linear context. That's the part where I think he's right. The interface is changing. The human ceremony around tickets is shrinking. The world where a person spends half their week turning messy reality into well-behaved tickets, that's not our end state anymore. But then, OpenAI published Symphony. And Symphony makes the opposite point just as clearly. Symphony says, "Take a project management board like Linear, read the tasks, create a dedicated workspace for every issue, run the agents continuously, and just let humans review the results." OpenAI says some internal team saw a 500% increase in landed pull requests when using this model. And the OpenAI spec actually does use Linear as the tracker of choice in their roll out of Symphony. So, Symphony defines polling, per issue workspaces, active and terminal states, retries, observability, concurrency limits, and handoff states, human review is an example handoff state. In other words, the issue tracker in the Symphony world did not die. It got promoted. It stopped being the only user interface for human coordination and became the data layer for agent coordination. And that distinction matters. That human translation step that Kari was talking about killing, that can die. But the underlying substrate of why we have issue trackers can get stronger at the same time. The part humans hated, manually grooming tickets and manually translating messy reality, can go away. Well, the part agents need, which is actually tracking stuff over time, becomes essential. And once you see that, once you see that distinction between what humans need and agents need, everything starts to look different. And once you have the core insight that agents need to work against a stateful ticketing system, you see the whole history of the issue tracking category differently. And the reason that's the case goes all the way back to 1998. Bugzilla was one of the first canonical issue trackers. Terry Weissman wrote it for Mozilla to replace the internal defect tracker that Netscape had been using. It was originally written in TCL and moved to Pearl with MySQL underneath. The first public deployment was in April of 1998. The important thing about Bugzilla is that it was narrow on purpose. The Bugzilla team explicitly said they wanted to focus on tracking software defects. They were not trying to build a general project management system or a support queue or a universal business process engine. They were just trying to solve one problem. When a lot of people are building software asynchronously, how do you make sure the bugs don't just disappear into the ether and never get worked on? And that narrow problem produced a very powerful shape. A bug had durable state outside anyone person's head. It was not in someone's inbox. It was not in a hallway conversation. It was a record in a database. It had a state machine. It could be new, assigned, resolved, verified, or closed. And of course, there's the infamous won't fix, which was one of the most emotionally honest software states ever invented. But, the system had ownership. The assignee field made it clear whose turn it was. It even defined verbs we still use today like create, comment, assign, resolve, reopen, mark duplicate, block another bug. It had dependencies. This bug blocks this release. This issue depends on that issue. It had audit history. Who changed what, when, and from what to what? None of that was designed for AI. There was no AI in the relevant sense. This This was just a bunch of humans trying to coordinate software work across time zones, across teams, across release trains, and across memory gaps. But, those human constraints turn out to be close to agent constraints. Humans forget context. Well, agents lose context. Humans need handoff. Well, agents need handoffs, too. Humans need accountability. Turns out, agents need observability. Humans need permissions. Agents need permissions even more. Humans need a shared source of truth. When work stretches across days and weeks, it turns out agents need that because the context window's not a source of truth. That is the accident, in the sense that we didn't intend it that way. Although, I would argue that a lot of the way we designed agents is to mimic people, so maybe it wasn't as accidental as we thought. Regardless of whether you think agents were designed like us on accident or on purpose, the system we built to compensate for human weakness does compensate very, very well for agent weaknesses, too. And that's why the old issue tracker shape just keeps surviving. You can see the same pattern in the way the category evolved. Bugzilla escaped from Mozilla and became the default tracker for a generation of open source projects. And then Jira showed up in 2002 and took the same basic model to the enterprise. Jira added workflows and custom fields and project hierarchy and permissions and integrations and enough configurability to map almost any company's internal process into the tool. That was the commercial genius of Jira. It could become your company. It is also why developers hated it. Every Jira deployment became its own local maze. The underlying primitives were good, but the configuration surface to make it sailable was so large that the tool could absorb every organizational dysfunction around it. Linear came later with a different philosophy. Linear did not say, "Bring us your org chart and every weird approval process and we will lovingly recreate it in software." Linear said, "This is your problem. Use our model, it's a cleaner model." Issues live in cycles, cycles connect to projects. The UI is fast, the opinion is strong, the customization surface is much smaller. And that is why Linear felt so good compared to Jira. It was not that Linear invented a new substrate, the basic data model was the same: issue, state, assignee, priority, dependency, history. Linear's innovation was making that model pleasant enough that people use it voluntarily and consistently. And that's the part that counterintuitively matters for agents, because you see good UX ends up getting more human involvement, which produces cleaner data, which is useful to agents. When people hate a tool, they work around it. They leave fields blank. They put important decisions in Slack. They use fake statuses. They create tickets after the work is done. They use the tracker because someone made them, not because it reflects reality. When people like the tool, more of the real work ends up in the tool and in the system, and that means the state is cleaner and the descriptions are better and the ownership is current and the dependencies are less made up. The audit history happens to be actually useful. Linear was a UX win. The UX win became a data win because people used good UX, and the data win matters much, much more once agents arrive. Because an agent does not care whether your project management tool feels elegant, it cares whether the state inside it is reliable enough to act on. That's the first big lesson. The best agent substrate may not be the tool with the most AI features, it may be the tool your team has been using cleanly for years because they love it. And yes, this is a plea for good UX. Good human UX in 2026, we still need it. Now let's talk about why agents want this particular shape of product so badly. An agent loop desperately needs a durable state. The context window does not count. It can be summarized, it can drift, it can get truncated, it can get reset. If the work spans multiple runs, multiple agents, multiple days, the state needs to live somewhere outside the model. A ticket does that. The agent can read the ticket at the beginning of a run and write back what happened at the end. The next run can pick up the work because the state is not trapped inside the previous conversation. That sounds really boring, but I promise you it's not boring. It is one of the biggest differences between a demo and a working agentic system. The agent also needs handoff semantics. Who owns that right now? Is the agent supposed to work on it? Is it waiting for a human? Is it blocked by another task? Is it ready for review? Is it done? In a good tracker, you don't depend on memory for this, you don't depend on vibes. These are fields. The assigning answers part of that problem, the status answers part of that problem, the dependency graph answers part of that problem, and the comment history answers part of it. Together, those fields become something like a protocol, and that's what Symphony is exploiting. The board is not just a visual planning surface. The board is a state machine. It's a way for agents to track their status over time, and that turns out to be critical for agents to actually get meaningful work done. An agent system also needs a way to coordinate many, many workers at once. This is where the Cursor long-running agents work is useful. Cursor wrote about running hundreds of agents on large coding projects and discovered that naive coordination breaks down very quickly when you get serious. So, if you have a flat agent system where every agent runs to the ball, agents hold locks too long, they forget to release them, they wait on each other, they become risk-averse and pick easy stuff, they take small little tasks instead of the hard end-to-end work they need to do. In other words, flat orgs of agents have a coordination problem, and issue trackers are coordination tools. They already have a unit of work, they already have claiming, they already have status, they already have blockers, they already have priority, they already have a way for humans to see what is happening without opening 20 terminals. So, the agent system does not have to invent a coordination layer from scratch. It can use the one the company already trusts. The next thing agents need is auditability. And this is where a lot of enterprise AI starts to kind of break at the edges. The demo will work, the pilot looks very good, I'm sure, and then something goes wrong in production and nobody can answer really basic questions about the defect. What did the agent see? What did it decide? What did it change? Who approved it? What state was the work in before and after? Issue trackers have ironically been logging this kind of history for decades. They did it because humans working asynchronously needed replayable history across time zones. Now, that same history is what makes agent work investigatable. Last but not least, agents need permissions. The whole security story for autonomous agents is about scoped access. What can the agent read? What can it write? Which systems can it touch? Which actions require approval? Which actions are blocked entirely? Enterprise issue trackers already live inside permission models. Jira projects have roles. Linear workspaces have permissions. Atlassian's Rovo MCP server respects the user's existing access controls. These systems were not built for agents, but they were built for controlled work. And that gives you a simple rule. The agent should not get to do more than the human assignee would be able to do. And that is a much easier rule to implement when the work is already inside a permission system with records and owners and actions and history. So, when you put all of this together, the fit between agents and ticketing systems becomes very obvious. Agents need durable state, they need clear ownership, they need legal transitions and bounded permissions and audit history. Issue trackers already have those things. And that is why Symphony looks so obvious after you see it. The surprising part is not that OpenAI used Linear per se, the surprising part is that we ever expected the agent layer to replace the work tracker instead of running through it. This also makes Atlassian look really different. For the last decade, a lot of people looked at Jira as the old world. It was powerful, it was entrenched, it was annoying, it was too configurable, it was deeply embedded in the enterprise process. But if issue trackers are agent substrates, then Atlassian owns one of the largest installed bases of agent readable work state in the world. And that changes the frame, doesn't it? In May 2025, Atlassian introduced its remote MCP server in beta. And the pitch was really simple. Let AI tools interact with Jira and Confluence data starting with Claude as the first official partner with Cloudflare infrastructure underneath. By February 2026, Atlassian said the Robo MCP server was generally available, right? It supports a broad set of clients. It can search and summarize Jira and Confluence and Compass. It can create and update issues and pages. It uses OAuth. It respects existing permissions. It supports admin controls and white listing. This is not just an integration. This is Atlassian making Jira and Confluence agent readable and agent writable. Mechanically, this is the same pattern Symphony assumes with linear. Take the system where work already lives, expose it through a controlled interface, and let agents operate against the work graph. This is why the Atlassian and Anthropic relationship is super interesting. Atlassian launched its remote MCP work, and Anthropic was the first one they picked, right? And in February, Anthropic signed a multi-year partnership with Atlassian Williams Racing, making Claude the team's official thinking partner and integrating Claude across Williams internal operations. But that F1 deal is not the main story here, right? Sponsorships are sponsorships. The brand alignment is more chilling. You have an AI lab that wants to be the enterprise agent layer sitting very close to the company that owns Jira and Confluence. And then you get the rumors. Online chatter started circulating that Anthropic might buy Atlassian at a premium. Treat that as rumor. That's not information. There's no formal announcement. There's no SEC filing. There's no deal. And there's no confirmation it will ever happen. But the rumor is still interesting for one reason. A few years ago, Frontier AI lab buys Atlassian would have sounded really bizarre. Why would the model company buy the issue tracker company? But now the logic is obvious enough that people will take it seriously even if the specific rumor goes nowhere. Because the issue tracker is no longer just a ticketing product. It is a map of how work happens inside the enterprise. It would benefit Anthropic to know that stuff. It knows the projects, it knows the dependencies, it knows the owners, it knows the history, it knows the approvals, it knows which work matters and which work is blocked. That's exactly the kind of context agents need. So the real headline is not Anthropic might buy Atlassian. The real headline is, in the agent era, Jira looks like infrastructure. And once you see Jira that way, a lot of other software starts to reprice in your head. And this is the part that jumps way beyond software engineering and way beyond ticketing systems into a larger strategy. Because the substrate hypothesis is real. Tools that have persistent records, defined verbs, ownership, permissions, and audit history become agent usable across software almost by accident. Tools that don't have those properties need a very expensive wrapper to be agent usable. And the agent layer has to invent structure that the underlying product never had. So which tools are like issue trackers? The first and obvious one is the CRM. Salesforce and HubSpot are issue trackers for revenue. They have accounts and contacts and opportunities and owners and stages and next steps and history and permissions and integrations. Sales teams already live inside the state machine there. A deal moves from prospecting to qualification to proposal to negotiation to closed one or closed lost. That is agent substrate. The agent can research an account, it can draft a follow-up, it can update fields, it can flag risk, it can prepare the next meeting, it can ask for human approval before sending something externally. The CRM is already a durable state layer. The second obvious category is service desk software. Zendesk, ServiceNow, Intercom, Jira Service Management. These are the issue trackers for customer problems. They have tickets and assignees and statuses and SLAs and escalation paths and macros and customer history and audit trails, and permissions all built in. If you were designing a customer support agent from scratch, you would rebuild a bunch of that. So, the agent will not replace the service desk, it will operate through it. The third category is ERP and business process systems. SAP, Oracle, Workday, NetSuite, these are not fun tools. Nobody wakes up excited to spend their day in an approval workflow, but they have records. They have business objects. They have permissions. They have approvals. They have audit trails. They encode how money and people and inventory and procurement and payroll and compliance move through the business. That is exactly the kind of boring structure agents need if they're going to do real work. And then you have some smaller but still important cases. Calendars are issue trackers for time. They have events and attendees and owners and rooms and availability and changes and history. Source control is an issue tracker for code change. Branches and commits and pull requests and reviewers and checks and merge status and blame and history. Procurement tools, they're issue trackers for spend. HR information systems are issue trackers for employees and roles. Finance systems are issue trackers for money movement. The pattern repeats. If a system was built to coordinate people asynchronously around really important work, it probably has the bones of an agent substrate. And the weaker candidates in this story are just as important. Email has a state, it has a history, it has permissions, but the verbs are really weak, right? Reply, forward, archive, label. There's not a native way to assign it or resolve it or block it or approve it in the general email model. That means agents can help with email, but email itself is not a very clean control plane. It's very It's too conversational. Slack and Teams are similar. They contain a huge amount of context, but the structure is mostly transcript structure. A thread is a pile of messages, the state of the work is often implied rather than encoded. Agents will and do read Slack, absolutely. They will summarize Slack. They are in Slack now. They will extract tasks from Slack. And Slack has reaped the benefits of being the place where humans are because agents end up getting built into Slack. But, if Slack is the only place your work state lives, the agent has to infer too much. Documentation tools, they kind of sit in the middle in this framework. Confluence, Notion, Google Docs, they have permissions, they have version history, they have comments, sometimes they have databases, but ownership is often very fuzzy and the verbs are usually edit and comment and share. That's useful context, but it's weaker as a substrate for serious work. Spreadsheets are the strangest middle-of-the-road case out there. They have rows, they have columns, they have formulas and structure, but the schema is user-defined and often implicit. The spreadsheet can be incredibly structured if the human designed it well, and also can be completely impossible if the human designed it like a personal scratchpad. So, spreadsheet agents will get better, but spreadsheets are not the easy case. The agent has to infer the user's schema before it can act. All of this gives you a very simple diagnostic for every tool in your stack. Just ask five questions. Does this tool have records or does it mostly just have content? Does it have a state machine or does it just have labels? Is ownership an explicit field or is it something people infer from conversation? Are the verbs structural or are they just conversational? I've given you examples of both. Is the history queryable or is it just visible? Tools that score well on these questions become agent infrastructure. Tools that score poorly become context sources at best, and in many cases they become places where someone else builds the real substrate around them. That's a very different way to evaluate software. It means the most important question is not does this product have an AI chatbot? The better question is, can an agent safely understand and change the state of work inside the product? Those are not the same set of questions, are they? It means the most important question is not does this product have an AI chatbot? The most important question is, can an agent safely understand and change the state of work inside this particular product? Totally different question. Now, what What you do with all this? For builders, I think the implication is really straightforward. Your data model is a strategic surface now. If you're building a product that you want agents to use later, don't start by bolting the chat into the UI. That's a very 2024 approach. Start by making the underlying state clean. Expose your records, define your verbs, make ownership really explicit, preserve your history, build permissions into the model, make the really important actions available through a real API or an MCP server. If your product is opaque, the agent's going to have to scrape the UI or guess what the user meant, and that's very fragile. If your product exposes really clean state and really clean verbs, the agent can operate through it. And that's the difference between we added AI for the board and actually we became part of the agent stack and no one's going to disrupt us. And that's the difference between just we added AI for show and we actually became part of the agent stack. For teams, the implication is more uncomfortable. Your work tracking choice is becoming your agent infrastructure choice and you have to get used to that. The Jira versus Linear decision used to feel like a UX and a workflow decision. Which tool do the engineers like? Which one fits our planning process? Which one integrates with GitHub? Which one annoys people less? And those questions do still matter, but now there's another question. Which substrate do you want your agents to run on? If your work data is clean, your agents get a head start. If your work data is spread across Slack threads and half-filled tickets and mystery spreadsheets and undocumented tribal knowledge, agents will struggle in exactly the places you want them to help. This is one of the hidden costs of messy operations. Messy operations used to be a human tax. People could compensate with meetings and memory and relationships and heroics. Agents are worse at those things. Agents really need the business to be legible. And that means the boring part of cleaning up your workflows and consolidating systems and enforcing fields and keeping ownership current and making sure status actually means something is not just good hygiene, it's AI readiness. For leaders, that implication is very strategic, right? That boring infrastructure your company already runs on, that's repricing. The tickets and records and workflows and approvals and comments and histories and permissions and dependency graphs, those are not just stuff your team happens to produce. They're the map agents are going to use to build on your business. That definitely favors incumbents, right? Folks like Atlassian and Salesforce and ServiceNow and Microsoft and Oracle and SAP and Workday. These companies own systems of record. They may not have the flashiest demos. They may not feel like the future, but they own that substrate agents build on, and the substrate is hard to displace. And that's why I'm a little bit skeptical of a lot of the greenfield agent platform stories. If the agent platform does not own the records, the permissions, the history, the workflows, or the user habits, it has to borrow those from somewhere. It has to borrow them from incumbent systems. It becomes a wrapper. Now, wrappers can be valuable. Some wrappers become very big companies, but owning the substrate is better than being the thing that sits on top of someone else's substrate. That's the strategic lesson from issue trackers. The 30-year accumulation of human coordination infrastructure is not going to disappear just cuz agents arrived. It's going to become the surface agents consume. Some companies will wrap around it, sure. Some companies will choose to expose it. Some companies are going to figure out how to own and drive against it deliberately. You want to know which side of that line you're ending up on. So, come back to the start of the story. Carissa said issue tracking is dead. OpenAI published a system that uses the issue tracker as the control pane for autonomous coding agents. It's not a contradiction if you understand the substrate story. The old user experience is dying. Carissa was right. The ritual of humans translating every bit of context is going away. That world is shrinking. But the substrate underneath it isn't dying. The substrate agents need to work against is a durable state. Uh the substrate needs ownership and permissions and a state machine and history for the agents to do work. So, why throw out the issue tracker that we're already putting good data into? That's where we're going to develop a shared map of work. And agents need that map more than humans do. And that is why issue trackers have won, and they won in the most boring possible way. They became too useful to replace. Not because everyone loved them, although Linear has its fans. Not because they were built for AI. They They won because they encoded coordination. And it turns out that the hard part of coordinating humans and the hard part of coordinating agents is a lot more overlap than a lot of us expected. So, the next time you look at a super boring enterprise tool, don't ask whether it has an AI assistant in the corner. Ask whether it has records and states and owners and verbs and permissions and history. And ask if they're willing to expose that. If it does, and if they are, that tool is probably more important than it looks. And if it doesn't, someone is going to build the agent substrate around it. And the difference between building on that substrate and owning that substrate and just kind of pretending it isn't there or dumping it out of the side and saying we don't need it anymore, that's going to matter a lot. Sure, the human translation step that Cary wrote about is dying. But the need to keep track of things over time is a persistent need agents have as well. The boring tools win. And the job now is figuring out which boring tools are next and how do we stitch these boring tools together so they form a useful agentic substrate for our businesses. Because I got to tell you, every business has a unique patchwork of these agent substrates. And a lot of the work of good agentic pipelines at the heart of the business is mapping your agentic substrate and figuring out how do you stitch together your ERP and your CRM and how do you stitch it with your tickets and how do you stitch it with your voice of customer? That's where the rubber meets the road, and that is why we need to take the current data we have in these systems seriously. Because you can't do real work by just wiping all of that away and setting it up clean and new. Instead, you need to be in a position where you can say, "This is how I audit the current system I'm in, and this is how I start to plan across the database schemas for these different systems of record to figure out how I can install an agentic pipeline that takes this data seriously based on actual live connectors. And if you're curious to do that more, I put together a complete guide for that over on the Substack. And if you're like, "Man, boring tools are boring." I promise we'll be back to covering the exciting hyperscalers soon. Subscribe and I'll see you next time. Cheers.

---

## Timestamped Segments

**[0:00]** This is the story of one of the most

**[0:01]** surprising software categories of 2026.

**[0:04]** And I'm talking about the issue trackers

**[0:06]** that are the substrate for AI agents now

**[0:09]** and were never built to be that. They

**[0:11]** weren't. Sometimes the programs we build

**[0:13]** for ourselves turn out to be

**[0:15]** accidentally useful to agents. I think

**[0:16]** it's one of the most fascinating stories

**[0:18]** of 2026 and they weren't ever designed

**[0:21]** for AI. They still aren't. They became

**[0:23]** useful because they happened to encode

**[0:25]** something that agents desperately need

**[0:27]** like state, like ownership, like

**[0:29]** permissions or history, or even a clean

**[0:31]** idea of what should happen next. Issue

**[0:33]** trackers is my favorite example. It's

**[0:36]** the most boring software in the

**[0:37]** engineering stack. I'm not going to

**[0:38]** pretend to you it's exciting. It's the

**[0:40]** thing people complain about. It's Jira,

**[0:42]** right? It's the thing that feels like

**[0:44]** process overhead, the thing everyone

**[0:45]** wants to make simpler and lighter and

**[0:47]** invisible. And yet, the issue tracker is

**[0:50]** quietly becoming one of the most

**[0:51]** important pieces of agent infrastructure

**[0:53]** out there right now. Because if you want

**[0:55]** agents to do real work, the hard part is

**[0:57]** not just making the model smarter. The

**[0:59]** hard part is giving the agent a place to

**[1:01]** find the work, a place to understand who

**[1:03]** owns the work, to know what state it's

**[1:05]** in, to see what changed, to ask for a

**[1:07]** review, and to hand the result back.

**[1:08]** That's exactly what issue trackers were

**[1:11]** built to do for people. They were built

**[1:13]** for handoffs, for memory, for

**[1:14]** accountability, for dependencies, for

**[1:16]** review. And by accident, those are

**[1:18]** almost exactly the things agents need.

**[1:20]** And that is why one small product story

**[1:22]** from the last month matters a lot more

**[1:24]** than it looks. Linear CEO published a

**[1:26]** letter saying issue tracking is dead.

**[1:29]** And just a little over a month later,

**[1:31]** OpenAI published Symphony, an

**[1:33]** open-source Codex orchestration spec

**[1:35]** whose central idea is to use an issue

**[1:37]** tracker, specifically a Linear board, as

**[1:39]** the control plane for autonomous coding

**[1:41]** agents. That is the entire contradiction

**[1:44]** of this space in 2026. The issue

**[1:46]** tracking experience might be dying, the

**[1:48]** issue tracking substrate is getting

**[1:51]** promoted. The old habit of humans

**[1:53]** manually translating messy reality into

**[1:55]** tickets, that's absolutely under

**[1:57]** pressure. But the underlying structure

**[1:59]** of the issue tracker, the state machine,

**[2:02]** the assignee field, the audit trail, the

**[2:04]** dependency graph, it's all underneath

**[2:05]** that UI, that's becoming more valuable,

**[2:08]** not less. And once you see why issue

**[2:11]** trackers work for agents, you can start

**[2:13]** spotting the same pattern in a lot of

**[2:14]** other places. CRMs, service desks, ERPs,

**[2:18]** calendars, source control, HR systems,

**[2:20]** finance systems, a lot of the programs

**[2:23]** we've already written are more agent

**[2:25]** useful than they look. And so this

**[2:27]** video, yeah, it's about issue trackers,

**[2:29]** but it's also about a much larger

**[2:30]** question. Which boring tools did we

**[2:33]** accidentally build that agents are going

**[2:35]** to need? And I want to walk through four

**[2:36]** pieces of that. First, why agents need

**[2:38]** something that looks suspiciously like

**[2:40]** an issue tracker. Second, why the boring

**[2:42]** infrastructure we built for human

**[2:43]** coordination turns out to fit agent

**[2:45]** coordination almost perfectly. Third,

**[2:47]** why Atlassian, Linear, Salesforce,

**[2:49]** ServiceNow, and a bunch of unsexy

**[2:51]** enterprise tools are suddenly sitting on

**[2:53]** something much more strategic than

**[2:54]** people realized. And fourth, how to tell

**[2:57]** which tools in your company are going to

**[2:58]** become that kind of agent infrastructure

**[3:00]** and which ones are going to get wrapped

**[3:02]** up or replaced. But the short version is

**[3:04]** this, the boring tools are winning in

**[3:07]** 2026. The really interesting question

**[3:09]** now is which boring tools win next and

**[3:12]** why. Let's go back to that Linear letter

**[3:14]** for a minute because the argument that

**[3:15]** Karri made was actually very reasonable.

**[3:17]** So on March 24th, uh Karri, the CEO of

**[3:19]** Linear, published a page called Issue

**[3:21]** Tracking Is Dead. And the basic idea was

**[3:23]** that issue trackers were built for a

**[3:25]** handoff model of software development.

**[3:26]** Uh they were built for a world where the

**[3:28]** product manager scopes the work and

**[3:29]** someone else writes the ticket and

**[3:31]** someone else picks it up later and the

**[3:32]** ticket moves through various statuses

**[3:34]** and people argue about priority and

**[3:35]** acceptance criteria and ownership and

**[3:37]** roadmaps and dependencies, whether

**[3:39]** something is a bug or a feature, and

**[3:41]** very slowly the system that was supposed

**[3:43]** to help the work becomes a big part of

**[3:45]** the work. This gets at what Linear was

**[3:47]** originally designed to solve and it is a

**[3:49]** real problem. And I want to emphasize

**[3:52]** that I have used both Linear and Jira. I

**[3:54]** see why we switched to Linear. Linear is

**[3:57]** fast, it's intuitive. I get why if

**[3:59]** you're using an issue tracker to solve

**[4:01]** this problem, you make the switch. But

**[4:03]** regardless of whether you've used Linear

**[4:05]** personally, you've probably used a

**[4:06]** ticketing system. If you've worked

**[4:08]** inside Jira or any heavily customized

**[4:11]** project management system, you know

**[4:12]** exactly what this feels like. The ticket

**[4:14]** ends up being a translation layer

**[4:16]** between reality and the team. A customer

**[4:18]** has a problem, a designer has an idea to

**[4:20]** solve it, an engineer sees a bug, a

**[4:22]** support person hears the same complaint

**[4:24]** five times. All of that messy context

**[4:26]** has to go somewhere. It gets It gets

**[4:28]** compressed into a record with a title

**[4:30]** and a description and an owner and a

**[4:31]** state and maybe a due date. That

**[4:33]** compression is useful, but it's also

**[4:35]** expensive. And so when Kari Saarinen was

**[4:38]** writing his essay, he pointed out agents

**[4:40]** change this picture. Agents can read

**[4:42]** more of the underlying context. They can

**[4:44]** look at raw customer feedback and

**[4:46]** internal discussion and product

**[4:47]** decisions at code at docs. They don't

**[4:50]** necessarily need a human to do as much

**[4:52]** of that translation step first. And

**[4:54]** Linear's answer is to become less like a

**[4:56]** place where people manually move tickets

**[4:58]** around and more like a shared product

**[5:00]** system where context turns into

**[5:02]** execution. Linear agent skills,

**[5:04]** automations, code intelligence, code

**[5:06]** depths, and eventually a coding agent

**[5:08]** that writes code and fixes bugs with

**[5:10]** native Linear context. That's the part

**[5:12]** where I think he's right. The interface

**[5:13]** is changing. The human ceremony around

**[5:15]** tickets is shrinking. The world where a

**[5:17]** person spends half their week turning

**[5:19]** messy reality into well-behaved tickets,

**[5:21]** that's not our end state anymore. But

**[5:22]** then, OpenAI published Symphony. And

**[5:25]** Symphony makes the opposite point just

**[5:26]** as clearly. Symphony says, "Take a

**[5:28]** project management board like Linear,

**[5:30]** read the tasks, create a dedicated

**[5:32]** workspace for every issue, run the

**[5:34]** agents continuously, and just let humans

**[5:36]** review the results." OpenAI says some

**[5:38]** internal team saw a 500% increase in

**[5:41]** landed pull requests when using this

**[5:42]** model. And the OpenAI spec actually does

**[5:45]** use Linear as the tracker of choice in

**[5:47]** their roll out of Symphony. So, Symphony

**[5:49]** defines polling, per issue workspaces,

**[5:51]** active and terminal states, retries,

**[5:54]** observability, concurrency limits, and

**[5:55]** handoff states, human review is an

**[5:57]** example handoff state. In other words,

**[5:59]** the issue tracker in the Symphony world

**[6:01]** did not die. It got promoted. It stopped

**[6:04]** being the only user interface for human

**[6:06]** coordination and became the data layer

**[6:08]** for agent coordination. And that

**[6:09]** distinction matters. That human

**[6:10]** translation step that Kari was talking

**[6:13]** about killing, that can die. But the

**[6:15]** underlying substrate of why we have

**[6:18]** issue trackers can get stronger at the

**[6:19]** same time. The part humans hated,

**[6:21]** manually grooming tickets and manually

**[6:23]** translating messy reality, can go away.

**[6:26]** Well, the part agents need, which is

**[6:28]** actually tracking stuff over time,

**[6:30]** becomes essential. And once you see

**[6:31]** that, once you see that distinction

**[6:33]** between what humans need and agents

**[6:35]** need, everything starts to look

**[6:37]** different. And once you have the core

**[6:39]** insight that agents need to work against

**[6:41]** a stateful ticketing system, you see the

**[6:44]** whole history of the issue tracking

**[6:45]** category differently. And the reason

**[6:48]** that's the case goes all the way back to

**[6:49]** 1998. Bugzilla was one of the first

**[6:52]** canonical issue trackers. Terry Weissman

**[6:54]** wrote it for Mozilla to replace the

**[6:55]** internal defect tracker that Netscape

**[6:57]** had been using. It was originally

**[6:58]** written in TCL and moved to Pearl with

**[7:00]** MySQL underneath. The first public

**[7:02]** deployment was in April of 1998. The

**[7:05]** important thing about Bugzilla is that

**[7:06]** it was narrow on purpose. The Bugzilla

**[7:09]** team explicitly said they wanted to

**[7:10]** focus on tracking software defects. They

**[7:12]** were not trying to build a general

**[7:13]** project management system or a support

**[7:15]** queue or a universal business process

**[7:17]** engine. They were just trying to solve

**[7:19]** one problem. When a lot of people are

**[7:20]** building software asynchronously, how do

**[7:23]** you make sure the bugs don't just

**[7:24]** disappear into the ether and never get

**[7:26]** worked on? And that narrow problem

**[7:28]** produced a very powerful shape. A bug

**[7:30]** had durable state outside anyone

**[7:32]** person's head. It was not in someone's

**[7:34]** inbox. It was not in a hallway

**[7:36]** conversation. It was a record in a

**[7:37]** database. It had a state machine. It

**[7:39]** could be new, assigned, resolved,

**[7:42]** verified, or closed. And of course,

**[7:44]** there's the infamous won't fix, which

**[7:46]** was one of the most emotionally honest

**[7:47]** software states ever invented. But, the

**[7:49]** system had ownership. The assignee field

**[7:51]** made it clear whose turn it was. It even

**[7:53]** defined verbs we still use today like

**[7:55]** create, comment, assign, resolve,

**[7:57]** reopen, mark duplicate, block another

**[7:59]** bug. It had dependencies. This bug

**[8:01]** blocks this release. This issue depends

**[8:03]** on that issue. It had audit history. Who

**[8:05]** changed what, when, and from what to

**[8:06]** what? None of that was designed for AI.

**[8:08]** There was no AI in the relevant sense.

**[8:10]** This This was just a bunch of humans

**[8:12]** trying to coordinate software work

**[8:14]** across time zones, across teams, across

**[8:16]** release trains, and across memory gaps.

**[8:18]** But, those human constraints turn out to

**[8:20]** be close to agent constraints. Humans

**[8:22]** forget context. Well, agents lose

**[8:24]** context. Humans need handoff. Well,

**[8:26]** agents need handoffs, too. Humans need

**[8:28]** accountability. Turns out, agents need

**[8:30]** observability. Humans need permissions.

**[8:32]** Agents need permissions even more.

**[8:34]** Humans need a shared source of truth.

**[8:36]** When work stretches across days and

**[8:37]** weeks, it turns out agents need that

**[8:39]** because the context window's not a

**[8:40]** source of truth. That is the accident,

**[8:44]** in the sense that we didn't intend it

**[8:46]** that way. Although, I would argue that a

**[8:47]** lot of the way we designed agents is to

**[8:49]** mimic people, so maybe it wasn't as

**[8:51]** accidental as we thought. Regardless of

**[8:53]** whether you think agents were designed

**[8:55]** like us on accident or on purpose, the

**[8:57]** system we built to compensate for human

**[8:59]** weakness does compensate very, very well

**[9:02]** for agent weaknesses, too. And that's

**[9:04]** why the old issue tracker shape just

**[9:06]** keeps surviving. You can see the same

**[9:08]** pattern in the way the category evolved.

**[9:10]** Bugzilla escaped from Mozilla and became

**[9:12]** the default tracker for a generation of

**[9:13]** open source projects. And then Jira

**[9:15]** showed up in 2002 and took the same

**[9:18]** basic model to the enterprise. Jira

**[9:20]** added workflows and custom fields and

**[9:22]** project hierarchy and permissions and

**[9:23]** integrations and enough configurability

**[9:25]** to map almost any company's internal

**[9:27]** process into the tool. That was the

**[9:29]** commercial genius of Jira. It could

**[9:31]** become your company. It is also why

**[9:33]** developers hated it. Every Jira

**[9:35]** deployment became its own local maze.

**[9:37]** The underlying primitives were good, but

**[9:39]** the configuration surface to make it

**[9:41]** sailable was so large that the tool

**[9:44]** could absorb every organizational

**[9:45]** dysfunction around it. Linear came later

**[9:47]** with a different philosophy. Linear did

**[9:50]** not say, "Bring us your org chart and

**[9:52]** every weird approval process and we will

**[9:53]** lovingly recreate it in software."

**[9:55]** Linear said, "This is your problem. Use

**[9:58]** our model, it's a cleaner model." Issues

**[10:00]** live in cycles, cycles connect to

**[10:01]** projects. The UI is fast, the opinion is

**[10:04]** strong, the customization surface is

**[10:06]** much smaller. And that is why Linear

**[10:08]** felt so good compared to Jira. It was

**[10:09]** not that Linear invented a new

**[10:11]** substrate, the basic data model was the

**[10:13]** same: issue, state, assignee, priority,

**[10:15]** dependency, history. Linear's innovation

**[10:17]** was making that model pleasant enough

**[10:19]** that people use it voluntarily and

**[10:21]** consistently. And that's the part that

**[10:23]** counterintuitively matters for agents,

**[10:25]** because you see good UX ends up getting

**[10:27]** more human involvement, which produces

**[10:29]** cleaner data, which is useful to agents.

**[10:32]** When people hate a tool, they work

**[10:33]** around it. They leave fields blank. They

**[10:35]** put important decisions in Slack. They

**[10:37]** use fake statuses. They create tickets

**[10:39]** after the work is done. They use the

**[10:41]** tracker because someone made them, not

**[10:42]** because it reflects reality. When people

**[10:44]** like the tool, more of the real work

**[10:46]** ends up in the tool and in the system,

**[10:48]** and that means the state is cleaner and

**[10:50]** the descriptions are better and the

**[10:51]** ownership is current and the

**[10:52]** dependencies are less made up. The audit

**[10:54]** history happens to be actually useful.

**[10:56]** Linear was a UX win. The UX win became a

**[10:59]** data win because people used good UX,

**[11:01]** and the data win matters much, much more

**[11:04]** once agents arrive. Because an agent

**[11:05]** does not care whether your project

**[11:07]** management tool feels elegant, it cares

**[11:09]** whether the state inside it is reliable

**[11:12]** enough to act on. That's the first big

**[11:13]** lesson. The best agent substrate may not

**[11:16]** be the tool with the most AI features,

**[11:18]** it may be the tool your team has been

**[11:19]** using cleanly for years because they

**[11:22]** love it. And yes, this is a plea for

**[11:24]** good UX. Good human UX in 2026, we still

**[11:27]** need it. Now let's talk about why agents

**[11:30]** want this particular shape of product so

**[11:32]** badly. An agent loop desperately needs a

**[11:36]** durable state. The context window does

**[11:39]** not count. It can be summarized, it can

**[11:40]** drift, it can get truncated, it can get

**[11:42]** reset. If the work spans multiple runs,

**[11:45]** multiple agents, multiple days, the

**[11:47]** state needs to live somewhere outside

**[11:50]** the model. A ticket does that. The agent

**[11:52]** can read the ticket at the beginning of

**[11:53]** a run and write back what happened at

**[11:55]** the end. The next run can pick up the

**[11:57]** work because the state is not trapped

**[11:59]** inside the previous conversation. That

**[12:01]** sounds really boring, but I promise you

**[12:03]** it's not boring. It is one of the

**[12:04]** biggest differences between a demo and a

**[12:06]** working agentic system. The agent also

**[12:08]** needs handoff semantics. Who owns that

**[12:11]** right now? Is the agent supposed to work

**[12:12]** on it? Is it waiting for a human? Is it

**[12:14]** blocked by another task? Is it ready for

**[12:15]** review? Is it done? In a good tracker,

**[12:18]** you don't depend on memory for this, you

**[12:19]** don't depend on vibes. These are fields.

**[12:22]** The assigning answers part of that

**[12:24]** problem, the status answers part of that

**[12:26]** problem, the dependency graph answers

**[12:28]** part of that problem, and the comment

**[12:30]** history answers part of it. Together,

**[12:31]** those fields become something like a

**[12:33]** protocol, and that's what Symphony is

**[12:35]** exploiting. The board is not just a

**[12:37]** visual planning surface. The board is a

**[12:40]** state machine. It's a way for agents to

**[12:42]** track their status over time, and that

**[12:44]** turns out to be critical for agents to

**[12:46]** actually get meaningful work done. An

**[12:48]** agent system also needs a way to

**[12:50]** coordinate many, many workers at once.

**[12:52]** This is where the Cursor long-running

**[12:53]** agents work is useful. Cursor wrote

**[12:55]** about running hundreds of agents on

**[12:57]** large coding projects and discovered

**[13:00]** that naive coordination breaks down very

**[13:02]** quickly when you get serious. So, if you

**[13:04]** have a flat agent system where every

**[13:06]** agent runs to the ball, agents hold

**[13:08]** locks too long, they forget to release

**[13:09]** them, they wait on each other, they

**[13:10]** become risk-averse and pick easy stuff,

**[13:12]** they take small little tasks instead of

**[13:14]** the hard end-to-end work they need to

**[13:16]** do. In other words, flat orgs of agents

**[13:18]** have a coordination problem, and issue

**[13:20]** trackers are coordination tools. They

**[13:22]** already have a unit of work, they

**[13:23]** already have claiming, they already have

**[13:25]** status, they already have blockers, they

**[13:27]** already have priority, they already have

**[13:29]** a way for humans to see what is

**[13:31]** happening without opening 20 terminals.

**[13:34]** So, the agent system does not have to

**[13:36]** invent a coordination layer from

**[13:38]** scratch. It can use the one the company

**[13:39]** already trusts. The next thing agents

**[13:41]** need is auditability. And this is where

**[13:43]** a lot of enterprise AI starts to kind of

**[13:45]** break at the edges. The demo will work,

**[13:47]** the pilot looks very good, I'm sure, and

**[13:49]** then something goes wrong in production

**[13:50]** and nobody can answer really basic

**[13:52]** questions about the defect. What did the

**[13:54]** agent see? What did it decide? What did

**[13:56]** it change? Who approved it? What state

**[13:57]** was the work in before and after? Issue

**[14:00]** trackers have ironically been logging

**[14:02]** this kind of history for decades. They

**[14:04]** did it because humans working

**[14:05]** asynchronously needed replayable history

**[14:08]** across time zones. Now, that same

**[14:09]** history is what makes agent work

**[14:11]** investigatable. Last but not least,

**[14:14]** agents need permissions. The whole

**[14:16]** security story for autonomous agents is

**[14:18]** about scoped access. What can the agent

**[14:20]** read? What can it write? Which systems

**[14:22]** can it touch? Which actions require

**[14:23]** approval? Which actions are blocked

**[14:25]** entirely? Enterprise issue trackers

**[14:27]** already live inside permission models.

**[14:29]** Jira projects have roles. Linear

**[14:31]** workspaces have permissions. Atlassian's

**[14:33]** Rovo MCP server respects the user's

**[14:35]** existing access controls. These systems

**[14:37]** were not built for agents, but they were

**[14:39]** built for controlled work. And that

**[14:40]** gives you a simple rule. The agent

**[14:42]** should not get to do more than the human

**[14:44]** assignee would be able to do. And that

**[14:46]** is a much easier rule to implement when

**[14:48]** the work is already inside a permission

**[14:50]** system with records and owners and

**[14:52]** actions and history. So, when you put

**[14:54]** all of this together, the fit between

**[14:56]** agents and ticketing systems becomes

**[14:58]** very obvious. Agents need durable state,

**[15:01]** they need clear ownership, they need

**[15:02]** legal transitions and bounded

**[15:03]** permissions and audit history. Issue

**[15:05]** trackers already have those things. And

**[15:08]** that is why Symphony looks so obvious

**[15:11]** after you see it. The surprising part is

**[15:13]** not that OpenAI used Linear per se, the

**[15:15]** surprising part is that we ever expected

**[15:17]** the agent layer to replace the work

**[15:19]** tracker instead of running through it.

**[15:21]** This also makes Atlassian look really

**[15:22]** different. For the last decade, a lot of

**[15:24]** people looked at Jira as the old world.

**[15:26]** It was powerful, it was entrenched, it

**[15:27]** was annoying, it was too configurable,

**[15:29]** it was deeply embedded in the enterprise

**[15:31]** process. But if issue trackers are agent

**[15:33]** substrates, then Atlassian owns one of

**[15:36]** the largest installed bases of agent

**[15:38]** readable work state in the world. And

**[15:40]** that changes the frame, doesn't it? In

**[15:42]** May 2025, Atlassian introduced its

**[15:44]** remote MCP server in beta. And the pitch

**[15:46]** was really simple. Let AI tools interact

**[15:48]** with Jira and Confluence data starting

**[15:50]** with Claude as the first official

**[15:51]** partner with Cloudflare infrastructure

**[15:53]** underneath. By February 2026, Atlassian

**[15:55]** said the Robo MCP server was generally

**[15:57]** available, right? It supports a broad

**[15:59]** set of clients. It can search and

**[16:00]** summarize Jira and Confluence and

**[16:02]** Compass. It can create and update issues

**[16:03]** and pages. It uses OAuth. It respects

**[16:06]** existing permissions. It supports admin

**[16:07]** controls and white listing. This is not

**[16:09]** just an integration. This is Atlassian

**[16:12]** making Jira and Confluence agent

**[16:15]** readable and agent writable.

**[16:16]** Mechanically, this is the same pattern

**[16:18]** Symphony assumes with linear. Take the

**[16:20]** system where work already lives, expose

**[16:23]** it through a controlled interface, and

**[16:25]** let agents operate against the work

**[16:26]** graph. This is why the Atlassian and

**[16:28]** Anthropic relationship is super

**[16:30]** interesting. Atlassian launched its

**[16:32]** remote MCP work, and Anthropic was the

**[16:33]** first one they picked, right? And in

**[16:35]** February, Anthropic signed a multi-year

**[16:37]** partnership with Atlassian Williams

**[16:39]** Racing, making Claude the team's

**[16:40]** official thinking partner and

**[16:42]** integrating Claude across Williams

**[16:44]** internal operations. But that F1 deal is

**[16:46]** not the main story here, right?

**[16:48]** Sponsorships are sponsorships. The brand

**[16:50]** alignment is more chilling. You have an

**[16:51]** AI lab that wants to be the enterprise

**[16:53]** agent layer sitting very close to the

**[16:56]** company that owns Jira and Confluence.

**[16:59]** And then you get the rumors. Online

**[17:00]** chatter started circulating that

**[17:02]** Anthropic might buy Atlassian at a

**[17:04]** premium. Treat that as rumor. That's not

**[17:06]** information. There's no formal

**[17:07]** announcement. There's no SEC filing.

**[17:09]** There's no deal. And there's no

**[17:10]** confirmation it will ever happen. But

**[17:12]** the rumor is still interesting for one

**[17:14]** reason. A few years ago, Frontier AI lab

**[17:17]** buys Atlassian would have sounded really

**[17:18]** bizarre. Why would the model company buy

**[17:20]** the issue tracker company? But now the

**[17:22]** logic is obvious enough that people will

**[17:24]** take it seriously even if the specific

**[17:26]** rumor goes nowhere. Because the issue

**[17:27]** tracker is no longer just a ticketing

**[17:29]** product. It is a map of how work happens

**[17:31]** inside the enterprise. It would benefit

**[17:33]** Anthropic to know that stuff. It knows

**[17:35]** the projects, it knows the dependencies,

**[17:36]** it knows the owners, it knows the

**[17:38]** history, it knows the approvals, it

**[17:39]** knows which work matters and which work

**[17:41]** is blocked. That's exactly the kind of

**[17:43]** context agents need. So the real

**[17:45]** headline is not Anthropic might buy

**[17:47]** Atlassian. The real headline is, in the

**[17:49]** agent era, Jira looks like

**[17:51]** infrastructure. And once you see Jira

**[17:52]** that way, a lot of other software starts

**[17:54]** to reprice in your head. And this is the

**[17:56]** part that jumps way beyond software

**[17:58]** engineering and way beyond ticketing

**[18:00]** systems into a larger strategy. Because

**[18:03]** the substrate hypothesis is real. Tools

**[18:06]** that have persistent records, defined

**[18:08]** verbs, ownership, permissions, and audit

**[18:10]** history become agent usable across

**[18:12]** software almost by accident. Tools that

**[18:14]** don't have those properties need a very

**[18:16]** expensive wrapper to be agent usable.

**[18:18]** And the agent layer has to invent

**[18:20]** structure that the underlying product

**[18:21]** never had. So which tools are like issue

**[18:24]** trackers? The first and obvious one is

**[18:26]** the CRM. Salesforce and HubSpot are

**[18:28]** issue trackers for revenue. They have

**[18:30]** accounts and contacts and opportunities

**[18:32]** and owners and stages and next steps and

**[18:34]** history and permissions and

**[18:35]** integrations. Sales teams already live

**[18:37]** inside the state machine there. A deal

**[18:39]** moves from prospecting to qualification

**[18:41]** to proposal to negotiation to closed one

**[18:43]** or closed lost. That is agent substrate.

**[18:45]** The agent can research an account, it

**[18:47]** can draft a follow-up, it can update

**[18:48]** fields, it can flag risk, it can prepare

**[18:50]** the next meeting, it can ask for human

**[18:52]** approval before sending something

**[18:54]** externally. The CRM is already a durable

**[18:57]** state layer. The second obvious category

**[18:59]** is service desk software. Zendesk,

**[19:01]** ServiceNow, Intercom, Jira Service

**[19:03]** Management. These are the issue trackers

**[19:05]** for customer problems. They have tickets

**[19:07]** and assignees and statuses and SLAs and

**[19:10]** escalation paths and macros and customer

**[19:12]** history and audit trails, and

**[19:13]** permissions all built in. If you were

**[19:15]** designing a customer support agent from

**[19:16]** scratch, you would rebuild a bunch of

**[19:18]** that. So, the agent will not replace the

**[19:20]** service desk, it will operate through

**[19:22]** it. The third category is ERP and

**[19:24]** business process systems. SAP, Oracle,

**[19:27]** Workday, NetSuite, these are not fun

**[19:29]** tools. Nobody wakes up excited to spend

**[19:31]** their day in an approval workflow, but

**[19:33]** they have records. They have business

**[19:34]** objects. They have permissions. They

**[19:36]** have approvals. They have audit trails.

**[19:38]** They encode how money and people and

**[19:40]** inventory and procurement and payroll

**[19:41]** and compliance move through the

**[19:43]** business. That is exactly the kind of

**[19:45]** boring structure agents need if they're

**[19:47]** going to do real work. And then you have

**[19:49]** some smaller but still important cases.

**[19:51]** Calendars are issue trackers for time.

**[19:53]** They have events and attendees and

**[19:55]** owners and rooms and availability and

**[19:57]** changes and history. Source control is

**[19:59]** an issue tracker for code change.

**[20:00]** Branches and commits and pull requests

**[20:02]** and reviewers and checks and merge

**[20:04]** status and blame and history.

**[20:05]** Procurement tools, they're issue

**[20:07]** trackers for spend. HR information

**[20:09]** systems are issue trackers for employees

**[20:11]** and roles. Finance systems are issue

**[20:12]** trackers for money movement. The pattern

**[20:14]** repeats. If a system was built to

**[20:17]** coordinate people asynchronously around

**[20:19]** really important work, it probably has

**[20:21]** the bones of an agent substrate. And the

**[20:23]** weaker candidates in this story are just

**[20:25]** as important. Email has a state, it has

**[20:27]** a history, it has permissions, but the

**[20:29]** verbs are really weak, right? Reply,

**[20:31]** forward, archive, label. There's not a

**[20:33]** native way to assign it or resolve it or

**[20:35]** block it or approve it in the general

**[20:37]** email model. That means agents can help

**[20:39]** with email, but email itself is not a

**[20:41]** very clean control plane. It's very It's

**[20:43]** too conversational. Slack and Teams are

**[20:45]** similar. They contain a huge amount of

**[20:46]** context, but the structure is mostly

**[20:49]** transcript structure. A thread is a pile

**[20:51]** of messages, the state of the work is

**[20:52]** often implied rather than encoded.

**[20:54]** Agents will and do read Slack,

**[20:56]** absolutely. They will summarize Slack.

**[20:58]** They are in Slack now. They will extract

**[21:00]** tasks from Slack. And Slack has reaped

**[21:02]** the benefits of being the place where

**[21:03]** humans are because agents end up getting

**[21:06]** built into Slack. But, if Slack is the

**[21:08]** only place your work state lives, the

**[21:10]** agent has to infer too much.

**[21:12]** Documentation tools, they kind of sit in

**[21:14]** the middle in this framework.

**[21:15]** Confluence, Notion, Google Docs, they

**[21:17]** have permissions, they have version

**[21:19]** history, they have comments, sometimes

**[21:21]** they have databases, but ownership is

**[21:22]** often very fuzzy and the verbs are

**[21:24]** usually edit and comment and share.

**[21:26]** That's useful context, but it's weaker

**[21:28]** as a substrate for serious work.

**[21:30]** Spreadsheets are the strangest

**[21:33]** middle-of-the-road case out there. They

**[21:34]** have rows, they have columns, they have

**[21:36]** formulas and structure, but the schema

**[21:38]** is user-defined and often implicit. The

**[21:40]** spreadsheet can be incredibly structured

**[21:43]** if the human designed it well, and also

**[21:44]** can be completely impossible if the

**[21:46]** human designed it like a personal

**[21:47]** scratchpad. So, spreadsheet agents will

**[21:49]** get better, but spreadsheets are not the

**[21:51]** easy case. The agent has to infer the

**[21:53]** user's schema before it can act. All of

**[21:56]** this gives you a very simple diagnostic

**[21:58]** for every tool in your stack. Just ask

**[22:00]** five questions. Does this tool have

**[22:02]** records or does it mostly just have

**[22:04]** content? Does it have a state machine or

**[22:06]** does it just have labels? Is ownership

**[22:08]** an explicit field or is it something

**[22:10]** people infer from conversation? Are the

**[22:12]** verbs structural or are they just

**[22:14]** conversational? I've given you examples

**[22:16]** of both. Is the history queryable or is

**[22:18]** it just visible? Tools that score well

**[22:20]** on these questions become agent

**[22:23]** infrastructure. Tools that score poorly

**[22:25]** become context sources at best, and in

**[22:27]** many cases they become places where

**[22:29]** someone else builds the real substrate

**[22:31]** around them. That's a very different way

**[22:33]** to evaluate software. It means the most

**[22:35]** important question is not does this

**[22:37]** product have an AI chatbot? The better

**[22:39]** question is, can an agent safely

**[22:41]** understand and change the state of work

**[22:43]** inside the product? Those are not the

**[22:45]** same set of questions, are they? It

**[22:47]** means the most important question is not

**[22:49]** does this product have an AI chatbot?

**[22:51]** The most important question is, can an

**[22:53]** agent safely understand and change the

**[22:55]** state of work inside this particular

**[22:57]** product? Totally different question.

**[22:59]** Now, what What you do with all this? For

**[23:01]** builders, I think the implication is

**[23:03]** really straightforward. Your data model

**[23:05]** is a strategic surface now. If you're

**[23:07]** building a product that you want agents

**[23:08]** to use later, don't start by bolting the

**[23:11]** chat into the UI. That's a very 2024

**[23:13]** approach. Start by making the underlying

**[23:15]** state clean. Expose your records, define

**[23:17]** your verbs, make ownership really

**[23:19]** explicit, preserve your history, build

**[23:21]** permissions into the model, make the

**[23:22]** really important actions available

**[23:24]** through a real API or an MCP server. If

**[23:26]** your product is opaque, the agent's

**[23:28]** going to have to scrape the UI or guess

**[23:30]** what the user meant, and that's very

**[23:31]** fragile. If your product exposes really

**[23:33]** clean state and really clean verbs, the

**[23:36]** agent can operate through it. And that's

**[23:37]** the difference between we added AI for

**[23:40]** the board and actually we became part of

**[23:42]** the agent stack and no one's going to

**[23:44]** disrupt us. And that's the difference

**[23:46]** between just we added AI for show and we

**[23:48]** actually became part of the agent stack.

**[23:50]** For teams, the implication is more

**[23:52]** uncomfortable. Your work tracking choice

**[23:54]** is becoming your agent infrastructure

**[23:56]** choice and you have to get used to that.

**[23:57]** The Jira versus Linear decision used to

**[24:00]** feel like a UX and a workflow decision.

**[24:02]** Which tool do the engineers like? Which

**[24:03]** one fits our planning process? Which one

**[24:05]** integrates with GitHub? Which one annoys

**[24:07]** people less? And those questions do

**[24:09]** still matter, but now there's another

**[24:10]** question. Which substrate do you want

**[24:13]** your agents to run on? If your work data

**[24:15]** is clean, your agents get a head start.

**[24:18]** If your work data is spread across Slack

**[24:20]** threads and half-filled tickets and

**[24:21]** mystery spreadsheets and undocumented

**[24:23]** tribal knowledge, agents will struggle

**[24:25]** in exactly the places you want them to

**[24:27]** help. This is one of the hidden costs of

**[24:30]** messy operations. Messy operations used

**[24:32]** to be a human tax. People could

**[24:34]** compensate with meetings and memory and

**[24:36]** relationships and heroics. Agents are

**[24:39]** worse at those things. Agents really

**[24:41]** need the business to be legible. And

**[24:43]** that means the boring part of cleaning

**[24:44]** up your workflows and consolidating

**[24:46]** systems and enforcing fields and keeping

**[24:48]** ownership current and making sure status

**[24:50]** actually means something is not just

**[24:52]** good hygiene, it's AI readiness. For

**[24:55]** leaders, that implication is very

**[24:56]** strategic, right? That boring

**[24:58]** infrastructure your company already runs

**[24:59]** on, that's repricing. The tickets and

**[25:02]** records and workflows and approvals and

**[25:03]** comments and histories and permissions

**[25:05]** and dependency graphs, those are not

**[25:07]** just stuff your team happens to produce.

**[25:09]** They're the map agents are going to use

**[25:11]** to build on your business. That

**[25:12]** definitely favors incumbents, right?

**[25:14]** Folks like Atlassian and Salesforce and

**[25:16]** ServiceNow and Microsoft and Oracle and

**[25:18]** SAP and Workday. These companies own

**[25:20]** systems of record. They may not have the

**[25:22]** flashiest demos. They may not feel like

**[25:24]** the future, but they own that substrate

**[25:26]** agents build on, and the substrate is

**[25:28]** hard to displace. And that's why I'm a

**[25:29]** little bit skeptical of a lot of the

**[25:31]** greenfield agent platform stories. If

**[25:33]** the agent platform does not own the

**[25:35]** records, the permissions, the history,

**[25:37]** the workflows, or the user habits, it

**[25:39]** has to borrow those from somewhere. It

**[25:42]** has to borrow them from incumbent

**[25:43]** systems. It becomes a wrapper. Now,

**[25:45]** wrappers can be valuable. Some wrappers

**[25:47]** become very big companies, but owning

**[25:48]** the substrate is better than being the

**[25:51]** thing that sits on top of someone else's

**[25:52]** substrate. That's the strategic lesson

**[25:54]** from issue trackers. The 30-year

**[25:56]** accumulation of human coordination

**[25:58]** infrastructure is not going to disappear

**[26:00]** just cuz agents arrived. It's going to

**[26:02]** become the surface agents consume. Some

**[26:04]** companies will wrap around it, sure.

**[26:05]** Some companies will choose to expose it.

**[26:07]** Some companies are going to figure out

**[26:09]** how to own and drive against it

**[26:10]** deliberately. You want to know which

**[26:12]** side of that line you're ending up on.

**[26:14]** So, come back to the start of the story.

**[26:16]** Carissa said issue tracking is dead.

**[26:18]** OpenAI published a system that uses the

**[26:20]** issue tracker as the control pane for

**[26:22]** autonomous coding agents. It's not a

**[26:24]** contradiction if you understand the

**[26:26]** substrate story. The old user experience

**[26:28]** is dying. Carissa was right. The ritual

**[26:30]** of humans translating every bit of

**[26:31]** context is going away. That world is

**[26:33]** shrinking. But the substrate underneath

**[26:36]** it isn't dying. The substrate agents

**[26:38]** need to work against is a durable state.

**[26:40]** Uh the substrate needs ownership and

**[26:42]** permissions and a state machine and

**[26:44]** history for the agents to do work. So,

**[26:46]** why throw out the issue tracker that

**[26:47]** we're already putting good data into?

**[26:49]** That's where we're going to develop a

**[26:52]** shared map of work. And agents need that

**[26:54]** map more than humans do. And that is why

**[26:55]** issue trackers have won, and they won in

**[26:57]** the most boring possible way. They

**[26:58]** became too useful to replace. Not

**[27:00]** because everyone loved them, although

**[27:02]** Linear has its fans. Not because they

**[27:04]** were built for AI. They They won because

**[27:05]** they encoded coordination. And it turns

**[27:08]** out that the hard part of coordinating

**[27:10]** humans and the hard part of coordinating

**[27:12]** agents is a lot more overlap than a lot

**[27:14]** of us expected. So, the next time you

**[27:16]** look at a super boring enterprise tool,

**[27:18]** don't ask whether it has an AI assistant

**[27:20]** in the corner. Ask whether it has

**[27:22]** records and states and owners and verbs

**[27:24]** and permissions and history. And ask if

**[27:27]** they're willing to expose that. If it

**[27:28]** does, and if they are, that tool is

**[27:31]** probably more important than it looks.

**[27:33]** And if it doesn't, someone is going to

**[27:34]** build the agent substrate around it. And

**[27:36]** the difference between building on that

**[27:38]** substrate and owning that substrate and

**[27:40]** just kind of pretending it isn't there

**[27:41]** or dumping it out of the side and saying

**[27:43]** we don't need it anymore, that's going

**[27:44]** to matter a lot. Sure, the human

**[27:46]** translation step that Cary wrote about

**[27:48]** is dying. But the need to keep track of

**[27:51]** things over time is a persistent need

**[27:53]** agents have as well. The boring tools

**[27:56]** win. And the job now is figuring out

**[27:59]** which boring tools are next and how do

**[28:01]** we stitch these boring tools together so

**[28:03]** they form a useful agentic substrate for

**[28:07]** our businesses. Because I got to tell

**[28:08]** you, every business has a unique

**[28:10]** patchwork of these agent substrates. And

**[28:13]** a lot of the work of good agentic

**[28:14]** pipelines at the heart of the business

**[28:16]** is mapping your agentic substrate and

**[28:18]** figuring out how do you stitch together

**[28:20]** your ERP and your CRM and how do you

**[28:22]** stitch it with your tickets and how do

**[28:23]** you stitch it with your voice of

**[28:24]** customer? That's where the rubber meets

**[28:26]** the road, and that is why we need to

**[28:28]** take the current data we have in these

**[28:30]** systems seriously. Because you can't do

**[28:31]** real work by just wiping all of that

**[28:33]** away and setting it up clean and new.

**[28:35]** Instead, you need to be in a position

**[28:37]** where you can say, "This is how I audit

**[28:40]** the current system I'm in, and this is

**[28:42]** how I start to plan across the database

**[28:45]** schemas for these different systems of

**[28:47]** record to figure out how I can install

**[28:50]** an agentic pipeline that takes this data

**[28:52]** seriously based on actual live

**[28:54]** connectors. And if you're curious to do

**[28:55]** that more, I put together a complete

**[28:57]** guide for that over on the Substack. And

**[28:59]** if you're like, "Man, boring tools are

**[29:01]** boring." I promise we'll be back to

**[29:02]** covering the exciting hyperscalers soon.

**[29:04]** Subscribe and I'll see you next time.

**[29:06]** Cheers.
