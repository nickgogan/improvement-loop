# Transcript: zP6TnEiueEc

**URL:** https://www.youtube.com/watch?v=zP6TnEiueEc
**Segments:** 564

---

## Full Text

Google IO opens today, May 19th. There will be a ton of agent demos. I can guarantee you that I will get into coverage for Google at another time. The more interesting story is what is happening underneath Google IO, including in many of the protocols Google is putting out there to drive the Agentic Revolution. I want to talk today about six agent protocols that have launched in the last year and how they underly agentic systems. Why do we do that? Because it turns out that the substrates for agents actually shape the customer experience. What are those six? MCP, A2A, AGUI, A2UI, AP2, and X42. It's not Star Wars robots. It's actually real protocols. And if you're building an AI agent product right now, that list is really hard to wrestle with and understand. It feels like a standard scrum. New acronyms are popping up all the time. There's new diagrams. There's new claims that some missing piece of the agent stack has been solved with a new protocol. Here is my read. Three of the six that I just named are becoming the actual agent stack. The other three are very much in contested layers that we need to be honest are still under debate. So, we're going to talk about all six today and we're going to talk about the three that are part of the core standard stack first. But before we get into which three are the standard, I want to lay out the overall landscape for agentic protocols. What are the questions that we're trying to answer with agentic protocols? I want to suggest three for you. Number one, what can the agent use? Number two, who else can the agent work with? And number three, how does the human stay in control while the agent is working? Keep those three in mind because they shape the customer experiences that we're trying to drive at the end of the day, whether we're building for internal or external customers. And they also help us to understand what really matters when there's a bunch of standards out there. Now, three of those six protocols directly map onto those three questions. MCP, that's a tool and data layer. It's the protocol an agent uses to discover and invoke the systems where your work lives. ADA, that's an agent coordination layer. It's the protocol one agent uses to discover and delegate to another agent across product or company boundaries. AGUI is a human interaction layer. It's a protocol that lets a longunning back-end agent share state and events and approvals and interruptions with a userfacing app. The other three protocols, A2UI, AP2X42, they all sit in a different spot in the stack. A2 UI is about how agents render structured interfaces. AP2 is about authorizing agent-led purchases. X42 is about machine to-achine payment at the HTTP layer on the web. All are really important and all are still contested or very domain specific. I break down all six protocols layer by layer on the Substack with source links, name partner list. If you want the full version, you know where to get it. We're going to move on in this video to MCP, perhaps the most popular and most well-known protocol stack in AI. MCP won share first because it solves the most immediate pain in agentic building. An agent sits in a chat box and has no access to tools and cannot do work. Right? It can only advise. It can summarize. It can draft. It's a 2024 world. The work itself lives somewhere else. It lives in GitHub. It lives in Slack. It lives in Drive and Postgress and Stripe and Linear and Salesforce in some internal API in a calendar. Before MCP, every integration with all of the tools I just named looked like custom glue to your chatbot, right? You had to have tool definitions and authentication patterns and parameter schemas and error handling all written from scratch every time. The beauty and power of MCP is that it standardizes all of that. A server exposes tools and resources. An agent host connects to it. The model receives a usable description of what can be done. New capabilities composed without every single agent platform rebuilding every connector. Cloud Desktop supports local MCP servers and so do most of the other agent tools out there including Codeex. Uh Google has support for it. There are more than 14,000 MCP servers now. And it's tempting to treat MCP as if it makes tools safe just because it's a standard across the internet. It doesn't. Tool access enables arbitrary code execution and arbitrary data access. And that's good because MCP is designed to allow agents to use tools in arbitrary ways to get task done. That's the reason it was created. But that also means that MCP was created for a high trust environment. And we now have to think about how we configure security and security stances around a tool using agent experience. MCP was not designed for that at root. And so there are other challenges that we have to solve if we are trying to build secure agents. You know, Invariant Labs has already published research on what they call tool poisoning attacks, which are malicious instructions that can hide inside tool descriptions that can be exposed via MCP. And those malicious instructions can influence an agent through the very metadata that's supposed to make the tool discoverable. So tool access is not a feature toggle even though it's treated that way in a lot of user interfaces. Now it is a security boundary that you're crossing. If your team is shipping MCP servers, you still need scopes and approval flows and audit trails and a real answer to which tools the agent can see in which context. MCP does get the agent close to the work. It does not decide whether the agent should do the work. And if you're interested in digging into the security side of things, the Substack piece goes deep on the Invariant Labs tool poisoning research, what that means for how we design our scopes, how we design our approvals. If your team's already running MCP servers, you definitely need to dig into that topic. You need to understand what you're exposing. For now, we're going to move to A to A and the delegation layer. So MCP gets agents reach, right? The second problem arrives the moment the agent actually starts working. So the agent can't know everything. It can't own every capability. A procurement agent will need a supplier agent. A travel agent needs a hotel agent. A finance agent may need a tax agent. Uh a software agent may need a security reviewer. In fact, I know it does. Work is distributed across owners and permissions and domains and expertise. No one agent does it all. So A to A turns that distribution into something that agents can reason about. And the important primitive in that stack is the agent card. A remote agent publishes a card that describes what it is, what it does, which skills it exposes, where it can be reached, and how another agent ought to interact with it. The agent card is the first version of an operating contract. It has real terms and real interfaces and real responsibility. Google launched ADA with a bunch of partners, right, with Atlassian and Box and Coher and MongoDB and PayPal and Workday. more than 50. The list matters because A toa A only works if agents really can cross product and company boundaries. So you want a world where you have discoverable delegation for agents, not just a bunch of swarms that look good on paper. But there's a cost here. Coordination isn't free. A toa adds another surface where you can have latency and failure and permissions and observability issues. If an agent asks another agent to do work, it certainly makes the agents workflow more flexible, but it also makes it less predictable. So A to A isn't the right answer for every product. A single product with a small set of tools may not need agent coordination at all. The right question to ask is whether this workflow requires delegated expertise or authority outside the primary agent. If the answer is yes, you need to think about what that looks like ahead of time. Decide what your agent can say about itself. decide what it can accept, decide what it can't share, decide what requires human approval, decide how a downstream result gets validated. The agent card is Google's attempt to make part of that process standard, but it's still missing a control layer, and that's where we get to AGUI. Now, I know it's easy to underestimate AGUI because most people who hear about it think it is about driving the user interface. I don't think that's the best reading. I think a better reading is that AGUI helps us to ensure trust in agentic workflows. An agent that's longunning, that's non-deterministic, and that's capable of touching external systems needs a lot more than a final answer for a human to see. Humans need to be able to observe that agent as it works, approve sensitive steps, correct course, inspect state, understand why the agent is waiting. And traditional web apps are just built for call and response. They don't really handle the streaming work that agents do. They don't handle the fact that agents may discover new information mid task. The chatbot experience is not enough for that and neither are most traditional apps. So AGUI is the open candidate for the human control layer. The docs talk about what agent apps actually need, right? Streaming, shared state, front-end tool calls, backend tool rendering, custom events, steering, sub aent composition. This is the layer many teams will ignore until their agents start doing real work and generating real bucks. So they'll wire a model to tools. They'll wire up a nice chat component. And then they'll discover what their agent is really doing. And then they'll say, "Oh no, we need approval buttons. Oh no, we need logs. We need a progress spinner." None of those things by themselves are fixes for the root issue, which is about finding the right control points, understanding what the agent is trying to do, understanding what it's waiting for, and then figuring out where the user needs to approve or deny or edit or cancel. So, AGUI belongs with MCP and ADA in the core stack even if the specific protocol is earlier in the adoption curve. AGUI itself may win that race, maybe a close cousin does. But the point is that an agent that can't show its work becomes supervision debt for humans. And this is a way to address that and actually at root think about the control problem for agents and build systems that allow humans to interact at the right moments with running agent workflows. Now, if AGUI is new for you, if you want to dive deeper, the Substack piece gets into all the elements in the ecosystem. It talks about AGUI with Langraph and Crew AI and Amazon Bedrock Agent Core and Pidantic AI and Mastra and Copilot Kit. If you're picking a framework, that's where you want to dive in and look. Now, we need to get to the other three protocols, the one that I said weren't part of the core stack, because we need to understand why. Because they won't tell you they're not part of the core stack. Every protocol thinks it's a standard. Why are these not standards? And what does that tell us about the state of the agent race? So the other three are A2 UI, AP2, and X42. A2UI is Google's project for agent generated interfaces. Instead of sending arbitrary HTML or JavaScript from a remote agent, which is frankly a security disaster waiting to happen, A2UI sends a structured declarative UI representation. The client renders using trusted components. The agent asks for components from an approved catalog. It cannot execute arbitrary interface code and that is absolutely the right direction to be running in. But it's much narrower from a solution space than the human control problem that AGUI is solving. A2 UI is just one piece of the overall rendering question and it doesn't try and establish a whole user control layer like AGUI. And so that's why I see A2 UI as being useful and helpful for driving some kinds of generated experiences, but maybe not as focused on the substrate that many many agents will need to drive successful workflows in the new Agentic economy. AP2 meanwhile is Google's Agentic payments protocol. 60 plus collaborators jumped onto this. You might think that makes it a standard, but not in payments. Uh the collaborators include Auden and American Express and Coinbase and Mastercard and PayPal and Salesforce and Union Pay and World Pay. That the key mechanic here is what's called the mandate, a cryptographically signed proof of what the user authorized. AP2 is trying to answer the most difficult question in Agentic Commerce. How does the ecosystem know the agent was authorized to buy? Meanwhile, X42 is Coinbase's HTTP native payment protocol. Cloudflare's adopted it. The use case is very much agent-gagent payment for resources. An agent buys an API call or a data source or a document or a benchmark run and it doesn't have to set up an account or negotiate a subscription. So AP2 and X42 are very much adjacent, but they're not the same thing. AP2 is about commercial trust and user authorization, and X42 is about how do you settle payments for resources for agents. And this this is not the end of the story. The protocol pile gets really big with payments because payments are a very valuable space to be in. If you're interested in diving deeper, I did an entire video recently on Stripe and its role in the payment space. That is definitely a video you want to check out if you're looking at payments and agent protocols. They've done a phenomenal job understanding that you are driving human trust in Aentic Commerce. And that is why their suggested experience of just sending an agent to a link to get an authorization token feels so smooth. So the protocols are going to keep piling up in the payment space even beyond Stripe. You have uh Mastercard with Aentic tokens. Visa with intelligent commerce. American Express has an Aentic commerce experiences developer kit. PayPal is supporting AP2 but is also building its own commerce layer. The payment space is so valuable, everyone wants to jump in. And if you're a builder right now, I would encourage you to think in the customer obsessed way that you see from recent Stripe launches because what you want to do is think about for my customers who have to trust agents. How do I ensure that the payment space is something that they feel they can participate in, authorize an agent to transact in, and feel good that their wallet is secure, the payment is authorized, the payment will be completed, and their order will be done as they expected. And so, don't look at payment protocols in particular as just a technical choice. They're very much a customer experience choice. Okay, stepping back here. How do you think about how substrates shape the customer experience? And how do you think about wrestling with them and getting into that problem space? If you've been assigned to ship an AI strategy or make an AI agent or complete a workflow with AI agents first and foremost, I've talked about this before. Get into the specifics, understand what you're really doing. Are you tackling support triage or procurement or sales territory analysis? Are you doing customer renewal prep? uh what what are you actually doing right understand that and then start to ask how does the substrate we are talking about shape the agentic experience for the customer right the MCP layer is absolutely going to be part of the conversation in most cases because you're going to want to have the option to bring that agent close to the work the ATA layer is narrower but can be very important if you're trying to understand how agents need to reason across other agent workflows. The AGUI layer is where you want to think about the ability to handle humanapproved longunning agent workflows. So for example, where the CSM might see a packet being assembled for the customer and might need to approve whether billing context should be included on the fly. Now, something like A2 UI might matter if the agent renders a particular usage chart or particular contract chart that helps someone understand what the agent is producing and you want some control and some guarantee that those components are real. And in this world, you need to be going through and asking yourself how your specific workflows map to the specific nuances of those protocols. And I'll give you an example from payments. So payments are complicated because payments are unique in different geographies. And one of the things that's really interesting about the payments experience with agents is that you have to blend in multiple competing protocols with multiple competing geographies as far as where customers are comfortable transacting, what payments methods they have, how they feel about using agents and compute when they're doing payments, etc. So there's a whole gnarly customer experience. There's a bunch of competing substrates. And if you want to put together an experience that is compelling, it is up to you to understand that a given payments experience may be biased toward the United States, toward US payment methods, given payments experience may be biased towards an assumption that humans will not make microp payments. And I I think that one of the things that I want to encourage you to do is to look at the things that may seem boring about these protocols. things like how fees are handled, things like how returns are handled, things like how delivery is handled, things like how uh authorization is handled and how long authorization runs for. And recognize that those have real customer implications. If your customer is not comfortable reauthorizing and you have a short-term token that you're driving for payment authorization and and your customer just wants it done and doesn't want to reauthorize every 30 minutes, you're going to have a very frustrated customer on your hands and that may be built into the protocol as a friendly default because it assumes a different customer. So, so protocols can be opinionated and that's okay, but you have to think about what that means for you. And I prepared six questions to help you start to dig into that. Number one, what tools and data does the agent need? Does the agent need to get into the MCP layer? Find out, right? Number two, what other agent surfaces or specialists does it need to call? Right? That's the A to A layer. Three, where does the user need to approve or edit or interrupt or steer the work? That's the AGUI layer, the control layer. Does the workflow need structured UI beyond text? That would be number four. A2 UI would help there. Number five, does the agent need to spend money? Does the agent need to authorize a transaction? Maybe that's an AP2 use case. Number six, does the agent need to autonomously pay for a resource programmatically? Maybe that's X42. Maybe it's something else. In general, most teams are overfocused on model selection, and they're very underspecified on the operating surface around the model. They know which LLM they want. They don't know which tools the agent can or should see. They may have a prototype that can call APIs, but they don't have an interaction model for user approval. They can imagine multiple agents coordinating, but they don't have any way to enforce or validate that. The actual work lives in those kinds of questions. So, I know we began this video talking about Google IO. There's going to be a lot of Agentic demos. I want you to watch at Google IO for one thing. Does Google make the agent stack feel like a single operating model? Does Gemini Enterprise stitch ADA agents and MCP tools and A2 UI interfaces and AP2 payments into something a builder can chip against? Or does IO give us a new set of standards, another another two or three standards to add to the pile? Because this is a year where the agent stack needs to stop being a list of acronyms and needs to start being really really buildable. And the companies that figure out how to build against the protocol stack in ways that shape customer experiences, they're they're going to be the ones that win, right? And we're going to look back in six months and realize that because agent workflows for developers unlocked in the first half of 2026, this was a golden time for building what really mattered. Now, if you want to dive into those six questions and how you understand how to think about agentic workflows with an eye on the customer and an eye on how these protocol substrates drive the customer experience in detail. I get into all that on the substack, right? We'll talk about Salesforce and Snowflake and Drive and Slack all how they operate at the MCP layer. We'll talk about billing and legal agents at the ADA layer. There's a dive on CSM facing approval services at the AGUI layer and how you think about that. So, if you want to get a quick start on copying some of those pieces for your team, you can grab that link. It's great. I hope that this dive into the substrate of agents has been helpful. It may not feel sexy to talk about why agent substrates drive customer experiences, but it's profoundly impactful and it's something I don't see coming up enough in conversations with build teams as they think about their agent workflow. So, I thought it was important to lay it out, lay out the standards really clearly and help you understand how to think about these standards and of course the next one that's going to come along next week. I'll see you on the next one. Cheers.

---

## Timestamped Segments

**[0:00]** Google IO opens today, May 19th. There

**[0:02]** will be a ton of agent demos. I can

**[0:04]** guarantee you that I will get into

**[0:06]** coverage for Google at another time. The

**[0:08]** more interesting story is what is

**[0:10]** happening underneath Google IO,

**[0:12]** including in many of the protocols

**[0:14]** Google is putting out there to drive the

**[0:16]** Agentic Revolution. I want to talk today

**[0:18]** about six agent protocols that have

**[0:21]** launched in the last year and how they

**[0:23]** underly agentic systems. Why do we do

**[0:26]** that? Because it turns out that the

**[0:27]** substrates for agents actually shape the

**[0:30]** customer experience. What are those six?

**[0:32]** MCP, A2A, AGUI, A2UI, AP2, and X42. It's

**[0:38]** not Star Wars robots. It's actually real

**[0:40]** protocols. And if you're building an AI

**[0:42]** agent product right now, that list is

**[0:45]** really hard to wrestle with and

**[0:46]** understand. It feels like a standard

**[0:48]** scrum. New acronyms are popping up all

**[0:50]** the time. There's new diagrams. There's

**[0:52]** new claims that some missing piece of

**[0:54]** the agent stack has been solved with a

**[0:56]** new protocol. Here is my read. Three of

**[0:59]** the six that I just named are becoming

**[1:01]** the actual agent stack. The other three

**[1:04]** are very much in contested layers that

**[1:07]** we need to be honest are still under

**[1:09]** debate. So, we're going to talk about

**[1:10]** all six today and we're going to talk

**[1:12]** about the three that are part of the

**[1:13]** core standard stack first. But before we

**[1:16]** get into which three are the standard, I

**[1:19]** want to lay out the overall landscape

**[1:21]** for agentic protocols. What are the

**[1:22]** questions that we're trying to answer

**[1:24]** with agentic protocols? I want to

**[1:25]** suggest three for you. Number one, what

**[1:28]** can the agent use? Number two, who else

**[1:31]** can the agent work with? And number

**[1:32]** three, how does the human stay in

**[1:35]** control while the agent is working? Keep

**[1:37]** those three in mind because they shape

**[1:38]** the customer experiences that we're

**[1:40]** trying to drive at the end of the day,

**[1:41]** whether we're building for internal or

**[1:43]** external customers. And they also help

**[1:46]** us to understand what really matters

**[1:47]** when there's a bunch of standards out

**[1:49]** there. Now, three of those six protocols

**[1:51]** directly map onto those three questions.

**[1:54]** MCP, that's a tool and data layer. It's

**[1:56]** the protocol an agent uses to discover

**[1:59]** and invoke the systems where your work

**[2:00]** lives. ADA, that's an agent coordination

**[2:04]** layer. It's the protocol one agent uses

**[2:06]** to discover and delegate to another

**[2:08]** agent across product or company

**[2:09]** boundaries. AGUI is a human interaction

**[2:12]** layer. It's a protocol that lets a

**[2:14]** longunning back-end agent share state

**[2:16]** and events and approvals and

**[2:18]** interruptions with a userfacing app. The

**[2:21]** other three protocols, A2UI, AP2X42,

**[2:25]** they all sit in a different spot in the

**[2:27]** stack. A2 UI is about how agents render

**[2:29]** structured interfaces. AP2 is about

**[2:32]** authorizing agent-led purchases. X42 is

**[2:35]** about machine to-achine payment at the

**[2:37]** HTTP layer on the web. All are really

**[2:40]** important and all are still contested or

**[2:44]** very domain specific. I break down all

**[2:46]** six protocols layer by layer on the

**[2:48]** Substack with source links, name partner

**[2:50]** list. If you want the full version, you

**[2:52]** know where to get it. We're going to

**[2:53]** move on in this video to MCP, perhaps

**[2:56]** the most popular and most well-known

**[2:58]** protocol stack in AI. MCP won share

**[3:02]** first because it solves the most

**[3:04]** immediate pain in agentic building. An

**[3:07]** agent sits in a chat box and has no

**[3:09]** access to tools and cannot do work.

**[3:11]** Right? It can only advise. It can

**[3:13]** summarize. It can draft. It's a 2024

**[3:15]** world. The work itself lives somewhere

**[3:17]** else. It lives in GitHub. It lives in

**[3:19]** Slack. It lives in Drive and Postgress

**[3:21]** and Stripe and Linear and Salesforce in

**[3:23]** some internal API in a calendar. Before

**[3:26]** MCP, every integration with all of the

**[3:29]** tools I just named looked like custom

**[3:31]** glue to your chatbot, right? You had to

**[3:33]** have tool definitions and authentication

**[3:35]** patterns and parameter schemas and error

**[3:37]** handling all written from scratch every

**[3:39]** time. The beauty and power of MCP is

**[3:42]** that it standardizes all of that. A

**[3:44]** server exposes tools and resources. An

**[3:46]** agent host connects to it. The model

**[3:48]** receives a usable description of what

**[3:50]** can be done. New capabilities composed

**[3:53]** without every single agent platform

**[3:54]** rebuilding every connector. Cloud

**[3:56]** Desktop supports local MCP servers and

**[3:58]** so do most of the other agent tools out

**[4:00]** there including Codeex. Uh Google has

**[4:02]** support for it. There are more than

**[4:04]** 14,000 MCP servers now. And it's

**[4:06]** tempting to treat MCP as if it makes

**[4:08]** tools safe just because it's a standard

**[4:10]** across the internet. It doesn't. Tool

**[4:13]** access enables arbitrary code execution

**[4:15]** and arbitrary data access. And that's

**[4:18]** good because MCP is designed to allow

**[4:20]** agents to use tools in arbitrary ways to

**[4:23]** get task done. That's the reason it was

**[4:24]** created. But that also means that MCP

**[4:28]** was created for a high trust

**[4:30]** environment. And we now have to think

**[4:32]** about how we configure security and

**[4:35]** security stances around a tool using

**[4:39]** agent experience. MCP was not designed

**[4:41]** for that at root. And so there are other

**[4:44]** challenges that we have to solve if we

**[4:47]** are trying to build secure agents. You

**[4:49]** know, Invariant Labs has already

**[4:50]** published research on what they call

**[4:52]** tool poisoning attacks, which are

**[4:54]** malicious instructions that can hide

**[4:56]** inside tool descriptions that can be

**[4:58]** exposed via MCP. And those malicious

**[5:01]** instructions can influence an agent

**[5:03]** through the very metadata that's

**[5:05]** supposed to make the tool discoverable.

**[5:07]** So tool access is not a feature toggle

**[5:10]** even though it's treated that way in a

**[5:12]** lot of user interfaces. Now it is a

**[5:14]** security boundary that you're crossing.

**[5:16]** If your team is shipping MCP servers,

**[5:18]** you still need scopes and approval flows

**[5:21]** and audit trails and a real answer to

**[5:23]** which tools the agent can see in which

**[5:25]** context. MCP does get the agent close to

**[5:28]** the work. It does not decide whether the

**[5:31]** agent should do the work. And if you're

**[5:33]** interested in digging into the security

**[5:35]** side of things, the Substack piece goes

**[5:37]** deep on the Invariant Labs tool

**[5:39]** poisoning research, what that means for

**[5:41]** how we design our scopes, how we design

**[5:43]** our approvals. If your team's already

**[5:45]** running MCP servers, you definitely need

**[5:47]** to dig into that topic. You need to

**[5:49]** understand what you're exposing. For

**[5:50]** now, we're going to move to A to A and

**[5:52]** the delegation layer. So MCP gets agents

**[5:55]** reach, right? The second problem arrives

**[5:58]** the moment the agent actually starts

**[6:00]** working. So the agent can't know

**[6:02]** everything. It can't own every

**[6:03]** capability. A procurement agent will

**[6:06]** need a supplier agent. A travel agent

**[6:08]** needs a hotel agent. A finance agent may

**[6:10]** need a tax agent. Uh a software agent

**[6:12]** may need a security reviewer. In fact, I

**[6:14]** know it does. Work is distributed across

**[6:18]** owners and permissions and domains and

**[6:19]** expertise. No one agent does it all. So

**[6:22]** A to A turns that distribution into

**[6:24]** something that agents can reason about.

**[6:26]** And the important primitive in that

**[6:28]** stack is the agent card. A remote agent

**[6:30]** publishes a card that describes what it

**[6:32]** is, what it does, which skills it

**[6:34]** exposes, where it can be reached, and

**[6:36]** how another agent ought to interact with

**[6:37]** it. The agent card is the first version

**[6:40]** of an operating contract. It has real

**[6:42]** terms and real interfaces and real

**[6:44]** responsibility. Google launched ADA with

**[6:46]** a bunch of partners, right, with

**[6:47]** Atlassian and Box and Coher and MongoDB

**[6:50]** and PayPal and Workday. more than 50.

**[6:52]** The list matters because A toa A only

**[6:55]** works if agents really can cross product

**[6:58]** and company boundaries. So you want a

**[7:00]** world where you have discoverable

**[7:02]** delegation for agents, not just a bunch

**[7:04]** of swarms that look good on paper. But

**[7:07]** there's a cost here. Coordination isn't

**[7:09]** free. A toa adds another surface where

**[7:11]** you can have latency and failure and

**[7:13]** permissions and observability issues. If

**[7:15]** an agent asks another agent to do work,

**[7:17]** it certainly makes the agents workflow

**[7:19]** more flexible, but it also makes it less

**[7:22]** predictable. So A to A isn't the right

**[7:24]** answer for every product. A single

**[7:26]** product with a small set of tools may

**[7:27]** not need agent coordination at all. The

**[7:30]** right question to ask is whether this

**[7:32]** workflow requires delegated expertise or

**[7:34]** authority outside the primary agent. If

**[7:37]** the answer is yes, you need to think

**[7:39]** about what that looks like ahead of

**[7:41]** time. Decide what your agent can say

**[7:43]** about itself. decide what it can accept,

**[7:45]** decide what it can't share, decide what

**[7:47]** requires human approval, decide how a

**[7:50]** downstream result gets validated. The

**[7:52]** agent card is Google's attempt to make

**[7:54]** part of that process standard, but it's

**[7:57]** still missing a control layer, and

**[7:59]** that's where we get to AGUI. Now, I know

**[8:02]** it's easy to underestimate AGUI because

**[8:04]** most people who hear about it think it

**[8:06]** is about driving the user interface. I

**[8:09]** don't think that's the best reading. I

**[8:11]** think a better reading is that AGUI

**[8:13]** helps us to ensure trust in agentic

**[8:15]** workflows. An agent that's longunning,

**[8:17]** that's non-deterministic, and that's

**[8:19]** capable of touching external systems

**[8:21]** needs a lot more than a final answer for

**[8:23]** a human to see. Humans need to be able

**[8:25]** to observe that agent as it works,

**[8:27]** approve sensitive steps, correct course,

**[8:30]** inspect state, understand why the agent

**[8:32]** is waiting. And traditional web apps are

**[8:34]** just built for call and response. They

**[8:36]** don't really handle the streaming work

**[8:38]** that agents do. They don't handle the

**[8:40]** fact that agents may discover new

**[8:42]** information mid task. The chatbot

**[8:45]** experience is not enough for that and

**[8:48]** neither are most traditional apps. So

**[8:50]** AGUI is the open candidate for the human

**[8:53]** control layer. The docs talk about what

**[8:55]** agent apps actually need, right?

**[8:57]** Streaming, shared state, front-end tool

**[8:59]** calls, backend tool rendering, custom

**[9:01]** events, steering, sub aent composition.

**[9:03]** This is the layer many teams will ignore

**[9:06]** until their agents start doing real work

**[9:08]** and generating real bucks. So they'll

**[9:09]** wire a model to tools. They'll wire up a

**[9:11]** nice chat component. And then they'll

**[9:12]** discover what their agent is really

**[9:14]** doing. And then they'll say, "Oh no, we

**[9:15]** need approval buttons. Oh no, we need

**[9:17]** logs. We need a progress spinner." None

**[9:19]** of those things by themselves are fixes

**[9:22]** for the root issue, which is about

**[9:23]** finding the right control points,

**[9:25]** understanding what the agent is trying

**[9:27]** to do, understanding what it's waiting

**[9:29]** for, and then figuring out where the

**[9:31]** user needs to approve or deny or edit or

**[9:33]** cancel. So, AGUI

**[9:36]** belongs with MCP and ADA in the core

**[9:38]** stack even if the specific protocol is

**[9:40]** earlier in the adoption curve. AGUI

**[9:43]** itself may win that race, maybe a close

**[9:46]** cousin does. But the point is that an

**[9:48]** agent that can't show its work becomes

**[9:50]** supervision debt for humans. And this is

**[9:53]** a way to address that and actually at

**[9:55]** root think about the control problem for

**[9:57]** agents and build systems that allow

**[9:59]** humans to interact at the right moments

**[10:01]** with running agent workflows. Now, if

**[10:03]** AGUI is new for you, if you want to dive

**[10:05]** deeper, the Substack piece gets into all

**[10:08]** the elements in the ecosystem. It talks

**[10:10]** about AGUI with Langraph and Crew AI and

**[10:12]** Amazon Bedrock Agent Core and Pidantic

**[10:15]** AI and Mastra and Copilot Kit. If you're

**[10:17]** picking a framework, that's where you

**[10:18]** want to dive in and look. Now, we need

**[10:21]** to get to the other three protocols, the

**[10:22]** one that I said weren't part of the core

**[10:24]** stack, because we need to understand

**[10:26]** why. Because they won't tell you they're

**[10:27]** not part of the core stack. Every

**[10:29]** protocol thinks it's a standard. Why are

**[10:30]** these not standards? And what does that

**[10:32]** tell us about the state of the agent

**[10:34]** race? So the other three are A2 UI, AP2,

**[10:37]** and X42.

**[10:39]** A2UI is Google's project for agent

**[10:42]** generated interfaces. Instead of sending

**[10:44]** arbitrary HTML or JavaScript from a

**[10:46]** remote agent, which is frankly a

**[10:48]** security disaster waiting to happen,

**[10:50]** A2UI sends a structured declarative UI

**[10:53]** representation. The client renders using

**[10:56]** trusted components. The agent asks for

**[10:59]** components from an approved catalog. It

**[11:01]** cannot execute arbitrary interface code

**[11:03]** and that is absolutely the right

**[11:05]** direction to be running in. But it's

**[11:06]** much narrower from a solution space than

**[11:09]** the human control problem that AGUI is

**[11:12]** solving. A2 UI is just one piece of the

**[11:15]** overall rendering question and it

**[11:17]** doesn't try and establish a whole user

**[11:20]** control layer like AGUI. And so that's

**[11:23]** why I see A2 UI as being useful and

**[11:25]** helpful for driving some kinds of

**[11:27]** generated experiences, but maybe not as

**[11:31]** focused on the substrate that many many

**[11:33]** agents will need to drive successful

**[11:36]** workflows in the new Agentic economy.

**[11:38]** AP2 meanwhile is Google's Agentic

**[11:40]** payments protocol. 60 plus collaborators

**[11:43]** jumped onto this. You might think that

**[11:44]** makes it a standard, but not in

**[11:46]** payments. Uh the collaborators include

**[11:47]** Auden and American Express and Coinbase

**[11:50]** and Mastercard and PayPal and Salesforce

**[11:52]** and Union Pay and World Pay. That the

**[11:54]** key mechanic here is what's called the

**[11:56]** mandate, a cryptographically signed

**[11:59]** proof of what the user authorized. AP2

**[12:02]** is trying to answer the most difficult

**[12:04]** question in Agentic Commerce. How does

**[12:06]** the ecosystem know the agent was

**[12:08]** authorized to buy? Meanwhile, X42 is

**[12:12]** Coinbase's HTTP native payment protocol.

**[12:14]** Cloudflare's adopted it. The use case is

**[12:16]** very much agent-gagent payment for

**[12:18]** resources. An agent buys an API call or

**[12:20]** a data source or a document or a

**[12:22]** benchmark run and it doesn't have to set

**[12:24]** up an account or negotiate a

**[12:26]** subscription. So AP2 and X42 are very

**[12:28]** much adjacent, but they're not the same

**[12:30]** thing. AP2 is about commercial trust and

**[12:32]** user authorization, and X42 is about how

**[12:35]** do you settle payments for resources for

**[12:37]** agents. And this this is not the end of

**[12:39]** the story. The protocol pile gets really

**[12:41]** big with payments because payments are a

**[12:43]** very valuable space to be in. If you're

**[12:45]** interested in diving deeper, I did an

**[12:46]** entire video recently on Stripe and its

**[12:49]** role in the payment space. That is

**[12:51]** definitely a video you want to check out

**[12:52]** if you're looking at payments and agent

**[12:54]** protocols. They've done a phenomenal job

**[12:57]** understanding that you are driving human

**[13:00]** trust in Aentic Commerce. And that is

**[13:02]** why their suggested experience of just

**[13:05]** sending an agent to a link to get an

**[13:07]** authorization token feels so smooth. So

**[13:10]** the protocols are going to keep piling

**[13:11]** up in the payment space even beyond

**[13:13]** Stripe. You have uh Mastercard with

**[13:15]** Aentic tokens. Visa with intelligent

**[13:17]** commerce. American Express has an Aentic

**[13:19]** commerce experiences developer kit.

**[13:22]** PayPal is supporting AP2 but is also

**[13:24]** building its own commerce layer. The

**[13:26]** payment space is so valuable, everyone

**[13:28]** wants to jump in. And if you're a

**[13:30]** builder right now, I would encourage you

**[13:32]** to think in the customer obsessed way

**[13:35]** that you see from recent Stripe launches

**[13:38]** because what you want to do is think

**[13:40]** about for my customers who have to trust

**[13:43]** agents. How do I ensure that the payment

**[13:46]** space is something that they feel they

**[13:49]** can participate in, authorize an agent

**[13:51]** to transact in, and feel good that their

**[13:53]** wallet is secure, the payment is

**[13:55]** authorized, the payment will be

**[13:56]** completed, and their order will be done

**[13:58]** as they expected. And so, don't look at

**[14:01]** payment protocols in particular as just

**[14:03]** a technical choice. They're very much a

**[14:05]** customer experience choice. Okay,

**[14:08]** stepping back here. How do you think

**[14:10]** about how substrates shape the customer

**[14:13]** experience? And how do you think about

**[14:15]** wrestling with them and getting into

**[14:16]** that problem space? If you've been

**[14:18]** assigned to ship an AI strategy or make

**[14:20]** an AI agent or complete a workflow with

**[14:23]** AI agents first and foremost, I've

**[14:25]** talked about this before. Get into the

**[14:27]** specifics, understand what you're really

**[14:28]** doing. Are you tackling support triage

**[14:30]** or procurement or sales territory

**[14:32]** analysis? Are you doing customer renewal

**[14:35]** prep? uh what what are you actually

**[14:37]** doing right understand that and then

**[14:40]** start to ask how does the substrate we

**[14:43]** are talking about shape the agentic

**[14:46]** experience for the customer right the

**[14:48]** MCP layer is absolutely going to be part

**[14:50]** of the conversation in most cases

**[14:52]** because you're going to want to have the

**[14:54]** option to bring that agent close to the

**[14:55]** work the ATA layer is narrower but can

**[14:59]** be very important if you're trying to

**[15:01]** understand how agents need to reason

**[15:04]** across other agent workflows. The AGUI

**[15:07]** layer is where you want to think about

**[15:10]** the ability to handle humanapproved

**[15:14]** longunning agent workflows. So for

**[15:15]** example, where the CSM might see a

**[15:18]** packet being assembled for the customer

**[15:20]** and might need to approve whether

**[15:21]** billing context should be included on

**[15:23]** the fly. Now, something like A2 UI might

**[15:26]** matter if the agent renders a particular

**[15:29]** usage chart or particular contract chart

**[15:31]** that helps someone understand what the

**[15:34]** agent is producing and you want some

**[15:36]** control and some guarantee that those

**[15:38]** components are real. And in this world,

**[15:41]** you need to be going through and asking

**[15:43]** yourself how your specific workflows map

**[15:48]** to the specific nuances of those

**[15:51]** protocols. And I'll give you an example

**[15:52]** from payments. So payments are

**[15:55]** complicated because payments are unique

**[15:57]** in different geographies. And one of the

**[15:59]** things that's really interesting about

**[16:00]** the payments experience with agents is

**[16:02]** that you have to blend in multiple

**[16:05]** competing protocols with multiple

**[16:07]** competing geographies as far as where

**[16:09]** customers are comfortable transacting,

**[16:11]** what payments methods they have, how

**[16:13]** they feel about using agents and compute

**[16:15]** when they're doing payments, etc. So

**[16:17]** there's a whole gnarly customer

**[16:18]** experience. There's a bunch of competing

**[16:20]** substrates. And if you want to put

**[16:22]** together an experience that is

**[16:23]** compelling, it is up to you to

**[16:25]** understand that a given payments

**[16:28]** experience may be biased toward the

**[16:31]** United States, toward US payment

**[16:32]** methods, given payments experience may

**[16:34]** be biased towards an assumption that

**[16:38]** humans will not make microp payments.

**[16:40]** And I I think that one of the things

**[16:42]** that I want to encourage you to do is to

**[16:44]** look at the things that may seem boring

**[16:46]** about these protocols. things like how

**[16:48]** fees are handled, things like how

**[16:50]** returns are handled, things like how

**[16:52]** delivery is handled, things like how uh

**[16:54]** authorization is handled and how long

**[16:56]** authorization runs for. And recognize

**[17:00]** that those have real customer

**[17:01]** implications. If your customer is not

**[17:04]** comfortable reauthorizing and you have a

**[17:06]** short-term token that you're driving for

**[17:09]** payment authorization and and your

**[17:10]** customer just wants it done and doesn't

**[17:13]** want to reauthorize every 30 minutes,

**[17:15]** you're going to have a very frustrated

**[17:17]** customer on your hands and that may be

**[17:19]** built into the protocol as a friendly

**[17:21]** default because it assumes a different

**[17:23]** customer. So, so protocols can be

**[17:24]** opinionated and that's okay, but you

**[17:27]** have to think about what that means for

**[17:29]** you. And I prepared six questions to

**[17:32]** help you start to dig into that. Number

**[17:34]** one, what tools and data does the agent

**[17:37]** need? Does the agent need to get into

**[17:39]** the MCP layer? Find out, right? Number

**[17:41]** two, what other agent surfaces or

**[17:43]** specialists does it need to call? Right?

**[17:45]** That's the A to A layer. Three, where

**[17:47]** does the user need to approve or edit or

**[17:50]** interrupt or steer the work? That's the

**[17:51]** AGUI layer, the control layer. Does the

**[17:54]** workflow need structured UI beyond text?

**[17:56]** That would be number four. A2 UI would

**[17:58]** help there. Number five, does the agent

**[18:01]** need to spend money? Does the agent need

**[18:03]** to authorize a transaction? Maybe that's

**[18:04]** an AP2 use case. Number six, does the

**[18:07]** agent need to autonomously pay for a

**[18:09]** resource programmatically?

**[18:11]** Maybe that's X42. Maybe it's something

**[18:13]** else. In general, most teams are

**[18:15]** overfocused on model selection, and

**[18:17]** they're very underspecified on the

**[18:19]** operating surface around the model. They

**[18:21]** know which LLM they want. They don't

**[18:23]** know which tools the agent can or should

**[18:25]** see. They may have a prototype that can

**[18:27]** call APIs, but they don't have an

**[18:29]** interaction model for user approval.

**[18:31]** They can imagine multiple agents

**[18:33]** coordinating, but they don't have any

**[18:34]** way to enforce or validate that. The

**[18:37]** actual work lives in those kinds of

**[18:39]** questions. So, I know we began this

**[18:41]** video talking about Google IO. There's

**[18:43]** going to be a lot of Agentic demos. I

**[18:45]** want you to watch at Google IO for one

**[18:47]** thing. Does Google make the agent stack

**[18:50]** feel like a single operating model? Does

**[18:52]** Gemini Enterprise stitch ADA agents and

**[18:55]** MCP tools and A2 UI interfaces and AP2

**[18:58]** payments into something a builder can

**[19:00]** chip against? Or does IO give us a new

**[19:03]** set of standards, another another two or

**[19:05]** three standards to add to the pile?

**[19:07]** Because this is a year where the agent

**[19:09]** stack needs to stop being a list of

**[19:11]** acronyms and needs to start being really

**[19:13]** really buildable. And the companies that

**[19:16]** figure out how to build against the

**[19:18]** protocol stack in ways that shape

**[19:20]** customer experiences, they're they're

**[19:22]** going to be the ones that win, right?

**[19:24]** And we're going to look back in six

**[19:25]** months and realize that because agent

**[19:28]** workflows for developers unlocked in the

**[19:31]** first half of 2026, this was a golden

**[19:33]** time for building what really mattered.

**[19:36]** Now, if you want to dive into those six

**[19:38]** questions and how you understand how to

**[19:40]** think about agentic workflows with an

**[19:42]** eye on the customer and an eye on how

**[19:44]** these protocol substrates drive the

**[19:47]** customer experience in detail. I get

**[19:49]** into all that on the substack, right?

**[19:50]** We'll talk about Salesforce and

**[19:52]** Snowflake and Drive and Slack all how

**[19:55]** they operate at the MCP layer. We'll

**[19:57]** talk about billing and legal agents at

**[19:59]** the ADA layer. There's a dive on CSM

**[20:01]** facing approval services at the AGUI

**[20:04]** layer and how you think about that. So,

**[20:05]** if you want to get a quick start on

**[20:07]** copying some of those pieces for your

**[20:08]** team, you can grab that link. It's

**[20:10]** great. I hope that this dive into the

**[20:13]** substrate of agents has been helpful. It

**[20:15]** may not feel sexy to talk about why

**[20:18]** agent substrates drive customer

**[20:20]** experiences, but it's profoundly

**[20:22]** impactful and it's something I don't see

**[20:24]** coming up enough in conversations with

**[20:26]** build teams as they think about their

**[20:28]** agent workflow. So, I thought it was

**[20:29]** important to lay it out, lay out the

**[20:31]** standards really clearly and help you

**[20:33]** understand how to think about these

**[20:35]** standards and of course the next one

**[20:38]** that's going to come along next week.

**[20:39]** I'll see you on the next one. Cheers.
