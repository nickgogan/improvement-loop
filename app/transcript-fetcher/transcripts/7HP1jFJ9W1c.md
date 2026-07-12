# Transcript: The Missing Orchestration Layer Destroying Teams Right Now

**URL:** https://www.youtube.com/watch?v=7HP1jFJ9W1c
**Segments:** 677
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 22:53
**Uploaded:** 2026-04-06

---

## Full Text

Right now, a new infrastructure stack is being assembled in public for AI, and most of us aren't paying attention to it. It's got billions and billions of capital behind it. It's not software. It's not agents. It's the layer underneath both of them. It's the layer that lets agents actually do things in the world. And the problem right now is that almost nobody on the outside of that category can figure out what's real and what's hype. And this video is all about disentangling that, giving you a way to understand this new infrastructure category for agents that's being created and helping you make sense of what the big pieces of this category are and how you can think about what's needed for your agents and your deployments. I want to be clear, we have seen this movie before. In fact, we've seen it twice before. Between 2006 and 2010, computing infrastructure shifted from onremise servers into the cloud. Uh EC2, S3, Lambda, all of these like cloud compute interfaces. The builders who understood the new stack started companies that are now dominant like AWS. And then between 2012 and 2016, we saw the movie again. Monolithic applications gave way very rapidly into decomposed applications with APIs in between them and what we call our microservices architecture. Now we're watching yet another shift. We're moving from human first tools to agent first primitives. I believe it is foundational in the same way that moving to cloud was foundational. So the new customer for infrastructure is going to be the agent in the same way that the new customer for compute became the enterprise renting compute from data centers in the 2010s. We are talking about a shift at least as big as cloud when we're moving to agentic primitives. But because it's so new and because most of the startups are so small, it's been really, really hard to distinguish the noise in the space from the actual signal. And so I'm going to break the category down for you here. And first, a word of warning. I love Legos. You know that. These are not the same thing as Lego bricks for agents. I want them to be. That's the hope. They'll sell you as Lego bricks for agents, but right now, you don't have the same degree of composability and predictability that you would have in a Lego analogy. These are not all bricks with the same size knobs that you can just slap together and they're going to make a little wall. Right now, it's as if you have Legos and wooden blocks and they're all marketing themselves as Legos. You don't know which is which and you don't know how to snap them together. And that is one of the biggest problems in the space right now. I think a more reliable analogy for where we're at in the space today is something like system calls. Agents need defined, reliable interfaces that help them figure out identity, that help them figure out compute, that help them figure out memory and persistence and communication and payments. And the companies that are building those system calls are essentially building the operating system that agents will need to do their work in the new economy. And I want to go through and com decompose that stack and give you layer by layer what agents look like and where the agent primitives are going in this economy. Number one, layer one, compute and sandboxing. This one is perhaps the most productionready in the stack. It's already bearing the load for agents. And what's the premise? It's really simple. The agent needs somewhere safe to run code. It should not run on your laptop. It should not run in production. And it should not run unsupervised. It needs isolated, sandboxed, auditable execution. I I think that this layer has the most mature competition at this point. Right. E2B has roughly $32 million in funding. It uses firecracker microVMs. It has the same tech as AWS Lambda has. And it's intended to give each agent a session with its own dedicated kernel. But it's not the only one, right? Daytona raised a $24 million series A recently and took a different architectural bet. They have Docker containers with a shared kernel and it's optimized for speed. I think they claim a 90 millisecond cold start which is insanely fast and also a persistent state. Uh Modal is a startup that targets GPUheavy workloads. browser base is valued at $300 billion after the series B and it focuses on headless browser automation giving agents the ability to interact with web pages as if they were human users and then there's newer entrance in the space uh Alibaba's open sandbox is a good example the interesting split in this space is really philosophical are you going to be ephemeral with your agents or are you going to be persistent E2B treats sandboxes as disposable you spin one up you run code you spin it down and sprites treat these spaces as longived and they assume that your agent can install dependencies that it can create files and that your agent in some sense will come back later. They assume a degree of agentic persistence. This is not a style preference. This is not optional for you to think about. This is an architectural bet from these startups on how long agent sessions in the new economy will run and whether state matters for those agent sessions. Both camps will probably survive because the Asian economy is going to be that big. But you're going to have to think about what your workloads need. If you want to look at this part of the stack, this is a really high durability component, right? Whatever you want to bet on, whether you want to bet on persistent agents or disposable agents, your agents need safe spaces to run code. And it totally makes sense that they're going to have virtual boxes to do it on. There will be a lot more startups working to solve this problem over the next year or so. But this is an area where it's relatively mature now and you have multiple options and you need to think about which one you want to use if you want to deploy your agents in any kind of computing environment that is virtual. What is layer two on top of the compute piece? Layer two is identity and communication. This is in a weird space. It's transitional and I think that we need to be thoughtful about what we consider basic in this space. So right now we know that an agent needs to exist on the internet as an entity. It needs to send and receive messages of some sort. It needs to authenticate with services. It needs to hold some kind of verifiable identity that other systems can recognize. And today one of the pragmatic answers to that is well the agent needs an email address. So Agent Mail raised a $6 million seed round from General Catalyst a couple of weeks ago. uh and Paul Graham and HubSpot CTO Dharmmes Shaw are both angels on agent mail. The API lets you programmatically create email inboxes for for agents. Real addresses, full threading, attachment, labels, search. The onboarding API even lets agents sign themselves up. So far so good. The thesis is very sharp. Agent mail CEO frames email not as a communication tool, but as a fundamental identity layer. And he's not the only one, by the way. There's like half a dozen startups in the space going after email. Email is today a universal key to the internet. Every SAS service needs one at signup. Every verification flow sends codes to it. If you give an agent email address, the idea goes, you're essentially giving it an identity. But what if that is a shim? Email works today because it's everywhere, not because it's the right protocol for agents, but because it's the right protocol for humans who built the internet. And right now, we all have problems with email as humans, right? Threading is brittle. We have rate limits designed to prevent spam and automated agents in particular. We have a signal to noise ratio that's terrible for agent context windows. The real need underneath the presenting need for email is a need to give an agent identity and communication protocols something that doesn't require pretending to be human. And multiple teams are working on this right you have uh onchain agent identity options. You have dedicated Ato communication standard. You have MCPbased service discovery. Nothing has a defined right to win yet in this space. If you are in this space, be thoughtful about what an agent native protocol looks like. Now, by the way, I am not the person to bet against email. Email has been famously cockroachlike in its ability to survive lots and lots of revolutions. It just seems to stick around. So, I'm not the one to say agents will never use email. But you should be aware if you're betting on agent email that you're making a pragmatic bet, not necessarily an architectural bet. Okay. So, agents need compute. That's a layer that's kind of mature. Agents need identity and communication. That one's really in flux. Agents need memory and statefulness. This is early. This is real. And the platform risk is just as real. Now, the need is clear, right? Agents need to be able to remember what happened in many cases, not just within a session, but across many sessions, many tasks, many days. Uh, Mem0ero is the clear leader here. They've raised $24 million, hit 41,000 some GitHub stars and 14 million downloads and were selected by AWS as the exclusive memory provider for its agent SDK. So, of course, their API has done very well. Call call volume has gone up fivefold, the whole thing. What Mem Zero gets right is the insight that memory isn't there to save the conversation, which is the old chat way of doing things. It's actually that memory is an act of active curation. So their system will store important information. It will it will it will deliberately forget outdated conflicting details and only recall relevant context when you are inferring something with an LLM query. So the architecture is very much a hybrid data store to reflect that. It has a network graph. It has a vector database. And it also has a key value store. And those three different formats allows me zero to treat memory as managed infrastructure, not just a feature bolted onto the model. And you get better results. Right? On the locomo benchmark, they outperform OpenAI's built-in memory by 26% on accuracy with 91% faster latency and 90% reduced token usage. It's a it's a clear win. But keep in mind that every Frontier lab is obsessed with building memory into its models. OpenAI already has big investments in long-term memory and is going to continue working on it. Anthropic is building memory into claude. If memory becomes a model level feature that the labs build in the same way that search got sort of built into Chad GPT and not as a separate feature, then all of these standalone memory companies are at risk because the model makers can just grab them. Now, if you're on Mezero side of things, the counter thesis is portability, right? And we've talked about this the idea that no one should own your memory. That's a really important concept that you should be able to own your memory. I've talked about this in relation to the frontier project that OpenAI is doing with AWS. Do you feel confident with your context layer which is a step above memory being something that a company owns and not you own? So I think the question here is really it's a question of which thesis wins and I think it's a very uncertain outlook. Will this be a situation where the market decides that they want a memory solution that does not belong to a hyperscaler? Or is it a situation where the convenience the hyperscalers offer is so compelling that the market as a whole just decides to go with it and throw memory at the hyperscalers and say you can solve the problem. And we look back in two years and we see companies like Memz and we say yeah they didn't last because they just weren't convenient enough. I don't know. It feels a little bit like a coin flip and I think we get to shape that by what we demand. Okay, so we've talked about compute and sandboxes. We've talked about identity and communication. We've talked about agent memory and state. Let's talk about tools and integration for agents. This one is growing explosively quickly as a layer and it solves real and immediate pain points. Any agent needs to interact with tools to do its work, right? whether it's interacting with Slack or with Jira or with Salesforce or with GitHub or with Google Workspace and those are all integrations or with basic primitives like it's running Unix or it's running Python or whatever it is and you have to have those tools if you're going to do work at an enterprise level and you have to have those integrations. Anything that makes that easier is going to coin. And so Compose with $29 million in funding from Lightseed provides a managed integration layer for agents, right? provides authentication handling without complicated ooth flows. It provides pre-built connectors to a couple of hundred solutions and it provides observability on every tool call. So they don't necessarily build agents. All they're doing is equipping agents with the plumbing that the agents need to navigate enterprise environments successfully and safe and safely. The problem is the classic NSM integration nightmare. Right? without middleware. Every single agent builder independently is going to manage their credentials, their off flows, their rate limits, their error handling, their API schema changes for every single tool that agent touches, which is just an enormous combinatorial problem. That's unsustainable at small scale. That is why it's N* M, right? It's it's the number of middleware times an infinite number. And at enterprise scale where an agent might need to touch your CRM, your ticketing, your email, your calendar, it's just impossible to keep up with. And so I would argue that this space is a very durable space to operate in. If you're building, as long as the ecosystem for tools remains fragmented, and if anything, it's going to fragment more as companies build their own stuff, agents are going to need an integration layer. The long-term risk here is standardization. If MCP truly becomes a universal, the value of a managed integration is going to start to diminish. So you're essentially betting if you're building in the space like Composeio that agents are going to need something to handle all of the massive enterprise integration touch points for a long time to come because so many of these companies are going to be slow to roll out MCPs and then slow many of the enterprises that have those tools are going to be slow to adopt those MCPS and that gap is where your entire company thesis sits if you're compos that one's going to stick around for a while. I do not believe in fastch changing enterprises at scale. I think a lot of enterprises move like dinosaurs and it's going to it's going to stick around. Okay, so compute and sandbox is done, identity done, memory done, tool access, we've talked about that. Layer five for agents, provisioning and billing. This is just brand new is the trust layer and it's just starting to arrive now. Agents essentially need to be able to acquire services and pay for them securely. And this is where Stripe Projects fits. It launched this past week. It's the first credible trust layer for agent to service transactions. The agent uses the same CLI commands as a human does and it can provision its own database. It can upgrade a hosting tier. Stripe can tokenize payment credentials for that agent. And the developers raw card details never leave Stripe's vault. The problem is very simple. Since the start of this year, agents have been able to do almost everything when it comes to spinning up a project except for the part where they need to create accounts and provision infrastructure because that has always required a human for authentication. And that's the gap that Stripe is closing here. Their databases are ready in roughly 350 milliseconds or a third of a second. They're free to start. They scale to zero when inactive. Every design choice is optimized for how quickly an agent can provision something that the agent is building. It's not for human speed dashboard clicking. You are assuming a terminal access here. We still have some missing pieces here. I think we're going to see growth around agentto agent payments. We're going to see growth around metered billing that maps to agent compute patterns. We're going to see growth around dynamic budget allocation where like agent A can spend so many dollars without human approval and agent B can spend so many dollars with human approval. We're going to have a lot of like observability layers that we build in. I think this is a case where Stripe as usual has made an excellent product decision. Uh they're known for that and this is something that's going to stick around. like this is immediately looking like fundamental infrastructure for how agents build on the web. I think we're going to see a few more players in this space, but fundamentally it's going to be focused not on human readability first, but on agent legibility and agent buildability and then human observability over the top. But regardless, like any Agentic economy future, you're going to have provisioning and billing. And so it's it's newly here, but it's here to stay. Okay, the last layer is orchestration and coordination. This is the biggest opportunity in the stack because you can leverage the power of multiple agents. It's also a big gap right now. So, the agent needs to work with other agents reliably at scale, with fallback handling, with audit trails, with cost controls, and it it it matters a lot to get that right. And there's just so little done well around this. And it's not for lack of interest. Like, Gartner reported a 1,445% surge. I don't even know what is that 14x surge in multi- aent system inquiries between Q1 2024 and Q2 2025 let alone 2026 which is going to be up again. Look quite bluntly the current tooling is at the framework level not the infrastructure level. So lang chain lets you stand up a multi- aent workflow right but the gap between I can spin up three agents in a notebook and I can reliably run 50 agents across enterprise systems with failure recovery and cost controls and audit logging and human escalation paths. that latter piece that we all need, that is something that we're all hand rolling right now. And so individual agent capabilities are something we've largely solved. What's been missing is the layer that makes those capabilities composable and parallel and reliable. And so if you're building in this space, here's what doesn't exist yet that needs to exist. Number one, you need a scheduling and life cycle layer for agents. Not in the container sense, right? I'm not saying that it's a Kubernetes container. I'm saying that you need something that handles agent creation and assignment and health checking and scaling and termination as a managed service. Number two, you need merge and coordination infrastructure that is built from the ground up for parallel agent work. Right? When five agents work on related tasks simultaneously, you need merge cues, you need conflict detection, you need resolution protocols. And today this is like a bunch of duct tape and a bunch of get work trees. Like it can be so much better. You need number three, supervision hierarchies, right? Meta agents that monitor and evaluate and course correct other agents. Not as a framework pattern you have to code yourself, which so many of us have to do now, but as infrastructure that you can configure. You need financial observability, right? Across multiple agent workflows, what what did this agent spend? Uh what was the outcome quality? What's the cost per successful task? This is like Finnops for agents and it's brand new. It barely exists. Last but not least, you need standard failure patterns and standard recovery patterns. So when an agent's tool call fails, instead of making it up on an individual team basis, you have to have some like standard provisioning around what happens, right? You shouldn't have to depend on the tool, the framework, and what the PM had for lunch that day to decide whether or not your agent recovered. Look, this layer, this orchestration layer, this is the layer where the next infrastructure defining company is going to get built. The orchestration problem for agents is structurally analogous to the container orchestration problem that Kubernetes solved. Right? Not the compute itself, but the scheduling, the scaling, the health checking, the life cycle management that makes compute usable at enterprise scale. So, whoever solves orchestration at infrastructure grade is going to own the most valuable position in the agent stack. And it is too early to call a winner. So, what does all of this mean? You've seen the six layers of the stack. What does it mean for builders right now? I want to give you three lessons that you should take away if you're building on the agent stack today that are truisms for 2026. I don't think they're going to change a lot this year. The stack has to evolve significantly. Number one, right now, reliability is compounding in the wrong direction. When your agent depends on five different primitives, your endto-end reliability is the product of five different reliability. So if each delivers 99% uptime your system delivers only 95%. If it's at 97% each it's at 86. You get the idea. Essentially you are stacking the liabilities of all your agentic primitives right now because you have to compose so much of this layer by hand. Reliability is really hard to engineer these days. Number two transitional lockin is a real risk this year. Right? Building on shims like email as identity creates migration costs when native protocols arrive. Every single shim you adopt is a bet that it either becomes the standard or it becomes something that you're willing to swap out. So think about your choices and think strategically about what is truly agent native and what is something that is a practical bet and make a choice about what you think is going to be correct over the next two or three years. We're all living through this together. I can't tell you if email like a wonderful cockroach is going to survive forever because it might or if we're actually going to get true agent to agent communication that is post email. Number three, and this is a big one, agent sprawl is coming. This is the same problem that plagued microservices back in 2018 when when when you would get people literally walking into startups from places like Amazon and Microsoft and the first thing they did when when this little startup had a tiny little codebase and just wanted to ship, they would say, "Well, it all needs to be a microservices architecture." Did it? No, it didn't. It's a monolith. Shift fast. In the same way, people are looking at agents and they're saying everything needs to be an agent and it's sprawling all over the enterprise and they're taking unexpected actions and you don't have observability and you don't have an orchestration layer and so you're just kind of guessing and vibing. That is going to be a bigger and bigger problem over the course of 2026 unless people invest now in orchestration layers that yes, you're going to have to hand roll. Look, I've talked about what I think the new builder skills are. I'll just reiterate them for you here. Context engineering matters a lot these days because what you feed the agent matters for the outcomes you drive. Eval driven development matters because you have to be able to get the agent to autonomously drive against a result to avoid a lot of the bottlenecks that comes from human reviewed code and stack literacy is going to be really important right you have to know which layer in the stack is your competitive advantage and why and you have to build relentlessly against that. In the world of agents, the builders who survive, and I don't care if you're building in the space as an entrepreneur, if you're building as an individual with your open claw, or if you're building as a leader and you're building on top of the stack and you need to get agents implemented regardless, the ones who survive, you're going to have to have stack literacy. You're going to have to understand how these six layers work. You're going to have to keep a weather eye on which pieces of the stack are changing and how they affect your business. There is no excuse for lack of stack literacy. And part of the reason this matters, part of the reason I'm talking about it in this channel is because if you don't have that, even as a business leader, even as a non-CTO, non- tech leader, you are going to be in big trouble because agents drive so much business outcome and business leverage now that is so dependent on these pieces of the stack. And so if you want to have an agent that has tremendous blast radius across your customer success, you got to understand what's driving that. What parts of the stack actually work? What parts of the stack are you hand rolling? What are your shims that you're betting on? If you don't have that detailed understanding, you're just kind of hoping and praying that the agent works. That's not a good strategy for the long term. And so, we need to have better stack literacy. And that's why this video is important. So, share it with someone who doesn't understand the agent stack because I guarantee you there are a lot of people who are walking around with a lot of LinkedIn buzzwords in their heads and they don't understand the agent stack. And that's going to lead to a lot of suffering and pain. Frankly, for a lot of IC engineering teams, they're going to be asked to build stuff that doesn't make any sense. Best of luck with that. Cheers.

---

## Timestamped Segments

**[0:00]** Right now, a new infrastructure stack is

**[0:02]** being assembled in public for AI, and

**[0:04]** most of us aren't paying attention to

**[0:05]** it. It's got billions and billions of

**[0:07]** capital behind it. It's not software.

**[0:09]** It's not agents. It's the layer

**[0:10]** underneath both of them. It's the layer

**[0:13]** that lets agents actually do things in

**[0:15]** the world. And the problem right now is

**[0:17]** that almost nobody on the outside of

**[0:19]** that category can figure out what's real

**[0:22]** and what's hype. And this video is all

**[0:24]** about disentangling that, giving you a

**[0:26]** way to understand this new

**[0:27]** infrastructure category for agents

**[0:29]** that's being created and helping you

**[0:30]** make sense of what the big pieces of

**[0:33]** this category are and how you can think

**[0:35]** about what's needed for your agents and

**[0:37]** your deployments. I want to be clear, we

**[0:39]** have seen this movie before. In fact,

**[0:40]** we've seen it twice before. Between 2006

**[0:42]** and 2010, computing infrastructure

**[0:45]** shifted from onremise servers into the

**[0:47]** cloud. Uh EC2, S3, Lambda, all of these

**[0:50]** like cloud compute interfaces. The

**[0:51]** builders who understood the new stack

**[0:53]** started companies that are now dominant

**[0:55]** like AWS. And then between 2012 and

**[0:58]** 2016, we saw the movie again. Monolithic

**[1:01]** applications gave way very rapidly into

**[1:04]** decomposed applications with APIs in

**[1:07]** between them and what we call our

**[1:08]** microservices architecture. Now we're

**[1:11]** watching yet another shift. We're moving

**[1:13]** from human first tools to agent first

**[1:16]** primitives. I believe it is foundational

**[1:19]** in the same way that moving to cloud was

**[1:21]** foundational. So the new customer for

**[1:23]** infrastructure is going to be the agent

**[1:27]** in the same way that the new customer

**[1:30]** for compute became the enterprise

**[1:33]** renting compute from data centers in the

**[1:35]** 2010s. We are talking about a shift at

**[1:38]** least as big as cloud when we're moving

**[1:40]** to agentic primitives. But because it's

**[1:43]** so new and because most of the startups

**[1:45]** are so small, it's been really, really

**[1:46]** hard to distinguish the noise in the

**[1:49]** space from the actual signal. And so I'm

**[1:50]** going to break the category down for you

**[1:52]** here. And first, a word of warning. I

**[1:54]** love Legos. You know that. These are not

**[1:56]** the same thing as Lego bricks for

**[1:58]** agents. I want them to be. That's the

**[2:00]** hope. They'll sell you as Lego bricks

**[2:02]** for agents, but right now, you don't

**[2:05]** have the same degree of composability

**[2:08]** and predictability that you would have

**[2:09]** in a Lego analogy. These are not all

**[2:12]** bricks with the same size knobs that you

**[2:15]** can just slap together and they're going

**[2:16]** to make a little wall. Right now, it's

**[2:19]** as if you have Legos and wooden blocks

**[2:21]** and they're all marketing themselves as

**[2:23]** Legos. You don't know which is which and

**[2:24]** you don't know how to snap them

**[2:25]** together. And that is one of the biggest

**[2:27]** problems in the space right now. I think

**[2:28]** a more reliable analogy for where we're

**[2:30]** at in the space today is something like

**[2:32]** system calls. Agents need defined,

**[2:34]** reliable interfaces that help them

**[2:36]** figure out identity, that help them

**[2:37]** figure out compute, that help them

**[2:39]** figure out memory and persistence and

**[2:40]** communication and payments. And the

**[2:42]** companies that are building those system

**[2:44]** calls are essentially building the

**[2:46]** operating system that agents will need

**[2:49]** to do their work in the new economy. And

**[2:51]** I want to go through and com decompose

**[2:53]** that stack and give you layer by layer

**[2:55]** what agents look like and where the

**[2:57]** agent primitives are going in this

**[2:59]** economy. Number one, layer one, compute

**[3:01]** and sandboxing. This one is perhaps the

**[3:04]** most productionready in the stack. It's

**[3:06]** already bearing the load for agents. And

**[3:08]** what's the premise? It's really simple.

**[3:10]** The agent needs somewhere safe to run

**[3:12]** code. It should not run on your laptop.

**[3:14]** It should not run in production. And it

**[3:16]** should not run unsupervised. It needs

**[3:18]** isolated, sandboxed, auditable

**[3:20]** execution. I I think that this layer has

**[3:22]** the most mature competition at this

**[3:24]** point. Right. E2B has roughly $32

**[3:26]** million in funding. It uses firecracker

**[3:29]** microVMs. It has the same tech as AWS

**[3:31]** Lambda has. And it's intended to give

**[3:33]** each agent a session with its own

**[3:35]** dedicated kernel. But it's not the only

**[3:37]** one, right? Daytona raised a $24 million

**[3:39]** series A recently and took a different

**[3:41]** architectural bet. They have Docker

**[3:42]** containers with a shared kernel and it's

**[3:44]** optimized for speed. I think they claim

**[3:47]** a 90 millisecond cold start which is

**[3:49]** insanely fast and also a persistent

**[3:51]** state. Uh Modal is a startup that

**[3:53]** targets GPUheavy workloads. browser base

**[3:55]** is valued at $300 billion after the

**[3:57]** series B and it focuses on headless

**[3:59]** browser automation giving agents the

**[4:01]** ability to interact with web pages as if

**[4:03]** they were human users and then there's

**[4:05]** newer entrance in the space uh Alibaba's

**[4:07]** open sandbox is a good example the

**[4:09]** interesting split in this space is

**[4:11]** really philosophical are you going to be

**[4:14]** ephemeral with your agents or are you

**[4:16]** going to be persistent E2B treats

**[4:19]** sandboxes as disposable you spin one up

**[4:22]** you run code you spin it down and

**[4:24]** sprites treat these spaces as longived

**[4:27]** and they assume that your agent can

**[4:29]** install dependencies that it can create

**[4:31]** files and that your agent in some sense

**[4:32]** will come back later. They assume a

**[4:35]** degree of agentic persistence. This is

**[4:37]** not a style preference. This is not

**[4:39]** optional for you to think about. This is

**[4:41]** an architectural bet from these startups

**[4:44]** on how long agent sessions in the new

**[4:47]** economy will run and whether state

**[4:49]** matters for those agent sessions. Both

**[4:52]** camps will probably survive because the

**[4:53]** Asian economy is going to be that big.

**[4:55]** But you're going to have to think about

**[4:57]** what your workloads need. If you want to

**[4:58]** look at this part of the stack, this is

**[5:00]** a really high durability component,

**[5:02]** right? Whatever you want to bet on,

**[5:03]** whether you want to bet on persistent

**[5:05]** agents or disposable agents, your agents

**[5:07]** need safe spaces to run code. And it

**[5:10]** totally makes sense that they're going

**[5:11]** to have virtual boxes to do it on. There

**[5:14]** will be a lot more startups working to

**[5:15]** solve this problem over the next year or

**[5:17]** so. But this is an area where it's

**[5:18]** relatively mature now and you have

**[5:20]** multiple options and you need to think

**[5:22]** about which one you want to use if you

**[5:24]** want to deploy your agents in any kind

**[5:26]** of computing environment that is

**[5:28]** virtual. What is layer two on top of the

**[5:30]** compute piece? Layer two is identity and

**[5:33]** communication. This is in a weird space.

**[5:35]** It's transitional and I think that we

**[5:37]** need to be thoughtful about what we

**[5:39]** consider basic in this space. So right

**[5:42]** now we know that an agent needs to exist

**[5:45]** on the internet as an entity. It needs

**[5:47]** to send and receive messages of some

**[5:49]** sort. It needs to authenticate with

**[5:51]** services. It needs to hold some kind of

**[5:52]** verifiable identity that other systems

**[5:55]** can recognize. And today one of the

**[5:58]** pragmatic answers to that is well the

**[6:00]** agent needs an email address. So Agent

**[6:02]** Mail raised a $6 million seed round from

**[6:04]** General Catalyst a couple of weeks ago.

**[6:06]** uh and Paul Graham and HubSpot CTO

**[6:09]** Dharmmes Shaw are both angels on agent

**[6:11]** mail. The API lets you programmatically

**[6:14]** create email inboxes for for agents.

**[6:16]** Real addresses, full threading,

**[6:18]** attachment, labels, search. The

**[6:21]** onboarding API even lets agents sign

**[6:23]** themselves up. So far so good. The

**[6:25]** thesis is very sharp. Agent mail CEO

**[6:28]** frames email not as a communication

**[6:30]** tool, but as a fundamental identity

**[6:32]** layer. And he's not the only one, by the

**[6:33]** way. There's like half a dozen startups

**[6:34]** in the space going after email. Email is

**[6:37]** today a universal key to the internet.

**[6:39]** Every SAS service needs one at signup.

**[6:41]** Every verification flow sends codes to

**[6:43]** it. If you give an agent email address,

**[6:45]** the idea goes, you're essentially giving

**[6:47]** it an identity. But what if that is a

**[6:50]** shim? Email works today because it's

**[6:52]** everywhere, not because it's the right

**[6:54]** protocol for agents, but because it's

**[6:56]** the right protocol for humans who built

**[6:58]** the internet. And right now, we all have

**[7:00]** problems with email as humans, right?

**[7:01]** Threading is brittle. We have rate

**[7:03]** limits designed to prevent spam and

**[7:05]** automated agents in particular. We have

**[7:07]** a signal to noise ratio that's terrible

**[7:09]** for agent context windows. The real need

**[7:13]** underneath the presenting need for email

**[7:15]** is a need to give an agent identity and

**[7:18]** communication protocols something that

**[7:20]** doesn't require pretending to be human.

**[7:23]** And multiple teams are working on this

**[7:25]** right you have uh onchain agent identity

**[7:27]** options. You have dedicated Ato

**[7:29]** communication standard. You have

**[7:30]** MCPbased service discovery. Nothing has

**[7:33]** a defined right to win yet in this

**[7:35]** space. If you are in this space, be

**[7:39]** thoughtful about what an agent native

**[7:41]** protocol looks like. Now, by the way, I

**[7:43]** am not the person to bet against email.

**[7:45]** Email has been famously cockroachlike in

**[7:47]** its ability to survive lots and lots of

**[7:49]** revolutions. It just seems to stick

**[7:51]** around. So, I'm not the one to say

**[7:53]** agents will never use email. But you

**[7:56]** should be aware if you're betting on

**[7:57]** agent email that you're making a

**[7:59]** pragmatic bet, not necessarily an

**[8:01]** architectural bet. Okay. So, agents need

**[8:03]** compute. That's a layer that's kind of

**[8:04]** mature. Agents need identity and

**[8:06]** communication. That one's really in

**[8:07]** flux. Agents need memory and

**[8:10]** statefulness. This is early. This is

**[8:13]** real. And the platform risk is just as

**[8:16]** real. Now, the need is clear, right?

**[8:17]** Agents need to be able to remember what

**[8:19]** happened in many cases, not just within

**[8:21]** a session, but across many sessions,

**[8:22]** many tasks, many days. Uh, Mem0ero is

**[8:26]** the clear leader here. They've raised

**[8:27]** $24 million, hit 41,000 some GitHub

**[8:30]** stars and 14 million downloads and were

**[8:33]** selected by AWS as the exclusive memory

**[8:35]** provider for its agent SDK. So, of

**[8:38]** course, their API has done very well.

**[8:39]** Call call volume has gone up fivefold,

**[8:41]** the whole thing. What Mem Zero gets

**[8:43]** right is the insight that memory isn't

**[8:45]** there to save the conversation, which is

**[8:47]** the old chat way of doing things. It's

**[8:49]** actually that memory is an act of active

**[8:52]** curation. So their system will store

**[8:54]** important information. It will it will

**[8:56]** it will deliberately forget outdated

**[8:58]** conflicting details and only recall

**[9:00]** relevant context when you are inferring

**[9:03]** something with an LLM query. So the

**[9:05]** architecture is very much a hybrid data

**[9:07]** store to reflect that. It has a network

**[9:09]** graph. It has a vector database. And it

**[9:11]** also has a key value store. And those

**[9:13]** three different formats allows me zero

**[9:16]** to treat memory as managed

**[9:18]** infrastructure, not just a feature

**[9:20]** bolted onto the model. And you get

**[9:22]** better results. Right? On the locomo

**[9:24]** benchmark, they outperform OpenAI's

**[9:26]** built-in memory by 26% on accuracy with

**[9:29]** 91% faster latency and 90% reduced token

**[9:32]** usage. It's a it's a clear win. But keep

**[9:34]** in mind that every Frontier lab is

**[9:36]** obsessed with building memory into its

**[9:38]** models. OpenAI already has big

**[9:40]** investments in long-term memory and is

**[9:42]** going to continue working on it.

**[9:43]** Anthropic is building memory into

**[9:45]** claude. If memory becomes a model level

**[9:47]** feature that the labs build in the same

**[9:49]** way that search got sort of built into

**[9:51]** Chad GPT and not as a separate feature,

**[9:54]** then all of these standalone memory

**[9:56]** companies are at risk because the model

**[9:57]** makers can just grab them. Now, if

**[10:00]** you're on Mezero side of things, the

**[10:01]** counter thesis is portability, right?

**[10:03]** And we've talked about this the idea

**[10:04]** that no one should own your memory.

**[10:06]** That's a really important concept that

**[10:07]** you should be able to own your memory.

**[10:09]** I've talked about this in relation to

**[10:10]** the frontier project that OpenAI is

**[10:12]** doing with AWS. Do you feel confident

**[10:14]** with your context layer which is a step

**[10:17]** above memory being something that a

**[10:18]** company owns and not you own? So I think

**[10:21]** the question here is really it's a

**[10:22]** question of which thesis wins and I

**[10:24]** think it's a very uncertain outlook.

**[10:27]** Will this be a situation where the

**[10:29]** market decides that they want a memory

**[10:31]** solution that does not belong to a

**[10:33]** hyperscaler? Or is it a situation where

**[10:35]** the convenience the hyperscalers offer

**[10:37]** is so compelling that the market as a

**[10:40]** whole just decides to go with it and

**[10:42]** throw memory at the hyperscalers and say

**[10:44]** you can solve the problem. And we look

**[10:46]** back in two years and we see companies

**[10:48]** like Memz and we say yeah they didn't

**[10:49]** last because they just weren't

**[10:50]** convenient enough. I don't know. It

**[10:53]** feels a little bit like a coin flip and

**[10:54]** I think we get to shape that by what we

**[10:56]** demand. Okay, so we've talked about

**[10:57]** compute and sandboxes. We've talked

**[10:59]** about identity and communication. We've

**[11:00]** talked about agent memory and state.

**[11:02]** Let's talk about tools and integration

**[11:04]** for agents.

**[11:06]** This one is growing explosively quickly

**[11:08]** as a layer and it solves real and

**[11:10]** immediate pain points. Any agent needs

**[11:12]** to interact with tools to do its work,

**[11:14]** right? whether it's interacting with

**[11:15]** Slack or with Jira or with Salesforce or

**[11:17]** with GitHub or with Google Workspace and

**[11:19]** those are all integrations or with basic

**[11:21]** primitives like it's running Unix or

**[11:23]** it's running Python or whatever it is

**[11:25]** and you have to have those tools if

**[11:28]** you're going to do work at an enterprise

**[11:30]** level and you have to have those

**[11:31]** integrations. Anything that makes that

**[11:33]** easier is going to coin. And so Compose

**[11:36]** with $29 million in funding from

**[11:38]** Lightseed provides a managed integration

**[11:40]** layer for agents, right? provides

**[11:42]** authentication handling without

**[11:43]** complicated ooth flows. It provides

**[11:45]** pre-built connectors to a couple of

**[11:46]** hundred solutions and it provides

**[11:48]** observability on every tool call. So

**[11:50]** they don't necessarily build agents. All

**[11:52]** they're doing is equipping agents with

**[11:54]** the plumbing that the agents need to

**[11:56]** navigate enterprise environments

**[11:57]** successfully and safe and safely. The

**[11:59]** problem is the classic NSM integration

**[12:02]** nightmare. Right? without middleware.

**[12:04]** Every single agent builder independently

**[12:06]** is going to manage their credentials,

**[12:07]** their off flows, their rate limits,

**[12:09]** their error handling, their API schema

**[12:11]** changes for every single tool that agent

**[12:12]** touches, which is just an enormous

**[12:14]** combinatorial problem. That's

**[12:16]** unsustainable at small scale. That is

**[12:18]** why it's N* M, right? It's it's the

**[12:20]** number of middleware times an infinite

**[12:22]** number. And at enterprise scale where an

**[12:24]** agent might need to touch your CRM, your

**[12:26]** ticketing, your email, your calendar,

**[12:27]** it's just impossible to keep up with.

**[12:29]** And so I would argue that this space is

**[12:31]** a very durable space to operate in. If

**[12:33]** you're building, as long as the

**[12:35]** ecosystem for tools remains fragmented,

**[12:38]** and if anything, it's going to fragment

**[12:39]** more as companies build their own stuff,

**[12:42]** agents are going to need an integration

**[12:43]** layer. The long-term risk here is

**[12:46]** standardization. If MCP truly becomes a

**[12:49]** universal, the value of a managed

**[12:51]** integration is going to start to

**[12:52]** diminish. So you're essentially betting

**[12:54]** if you're building in the space like

**[12:56]** Composeio that agents are going to need

**[12:59]** something to handle all of the massive

**[13:00]** enterprise integration touch points for

**[13:03]** a long time to come because so many of

**[13:04]** these companies are going to be slow to

**[13:06]** roll out MCPs and then slow many of the

**[13:09]** enterprises that have those tools are

**[13:10]** going to be slow to adopt those MCPS and

**[13:12]** that gap is where your entire company

**[13:14]** thesis sits if you're compos that one's

**[13:16]** going to stick around for a while. I do

**[13:18]** not believe in fastch changing

**[13:19]** enterprises at scale. I think a lot of

**[13:21]** enterprises move like dinosaurs and it's

**[13:23]** going to it's going to stick around.

**[13:24]** Okay, so compute and sandbox is done,

**[13:26]** identity done, memory done, tool access,

**[13:28]** we've talked about that. Layer five for

**[13:30]** agents, provisioning and billing. This

**[13:33]** is just brand new is the trust layer and

**[13:36]** it's just starting to arrive now. Agents

**[13:38]** essentially need to be able to acquire

**[13:40]** services and pay for them securely. And

**[13:43]** this is where Stripe Projects fits. It

**[13:45]** launched this past week. It's the first

**[13:47]** credible trust layer for agent to

**[13:49]** service transactions. The agent uses the

**[13:51]** same CLI commands as a human does and it

**[13:54]** can provision its own database. It can

**[13:56]** upgrade a hosting tier. Stripe can

**[13:57]** tokenize payment credentials for that

**[13:59]** agent. And the developers raw card

**[14:01]** details never leave Stripe's vault. The

**[14:04]** problem is very simple. Since the start

**[14:05]** of this year, agents have been able to

**[14:07]** do almost everything when it comes to

**[14:09]** spinning up a project except for the

**[14:11]** part where they need to create accounts

**[14:13]** and provision infrastructure because

**[14:14]** that has always required a human for

**[14:16]** authentication. And that's the gap that

**[14:18]** Stripe is closing here. Their databases

**[14:21]** are ready in roughly 350 milliseconds or

**[14:23]** a third of a second. They're free to

**[14:25]** start. They scale to zero when inactive.

**[14:28]** Every design choice is optimized for how

**[14:31]** quickly an agent can provision something

**[14:34]** that the agent is building. It's not for

**[14:36]** human speed dashboard clicking. You are

**[14:38]** assuming a terminal access here. We

**[14:41]** still have some missing pieces here. I

**[14:42]** think we're going to see growth around

**[14:43]** agentto agent payments. We're going to

**[14:45]** see growth around metered billing that

**[14:46]** maps to agent compute patterns. We're

**[14:48]** going to see growth around dynamic

**[14:49]** budget allocation where like agent A can

**[14:52]** spend so many dollars without human

**[14:54]** approval and agent B can spend so many

**[14:56]** dollars with human approval. We're going

**[14:58]** to have a lot of like observability

**[15:00]** layers that we build in. I think this is

**[15:01]** a case where Stripe as usual has made an

**[15:04]** excellent product decision. Uh they're

**[15:06]** known for that and this is something

**[15:07]** that's going to stick around. like this

**[15:09]** is immediately looking like fundamental

**[15:12]** infrastructure for how agents build on

**[15:14]** the web. I think we're going to see a

**[15:16]** few more players in this space, but

**[15:17]** fundamentally it's going to be focused

**[15:19]** not on human readability first, but on

**[15:21]** agent legibility and agent buildability

**[15:23]** and then human observability over the

**[15:25]** top. But regardless, like any Agentic

**[15:28]** economy future, you're going to have

**[15:29]** provisioning and billing. And so it's

**[15:31]** it's newly here, but it's here to stay.

**[15:33]** Okay, the last layer is orchestration

**[15:35]** and coordination. This is the biggest

**[15:38]** opportunity in the stack because you can

**[15:40]** leverage the power of multiple agents.

**[15:42]** It's also a big gap right now. So, the

**[15:44]** agent needs to work with other agents

**[15:46]** reliably at scale, with fallback

**[15:48]** handling, with audit trails, with cost

**[15:49]** controls, and it it it matters a lot to

**[15:52]** get that right. And there's just so

**[15:54]** little done well around this. And it's

**[15:57]** not for lack of interest. Like, Gartner

**[15:59]** reported a 1,445%

**[16:02]** surge. I don't even know what is that

**[16:03]** 14x surge in multi- aent system

**[16:05]** inquiries between Q1 2024 and Q2 2025

**[16:09]** let alone 2026 which is going to be up

**[16:10]** again. Look quite bluntly the current

**[16:12]** tooling is at the framework level not

**[16:14]** the infrastructure level. So lang chain

**[16:16]** lets you stand up a multi- aent workflow

**[16:18]** right but the gap between I can spin up

**[16:21]** three agents in a notebook and I can

**[16:23]** reliably run 50 agents across enterprise

**[16:25]** systems with failure recovery and cost

**[16:27]** controls and audit logging and human

**[16:29]** escalation paths. that latter piece that

**[16:32]** we all need, that is something that

**[16:33]** we're all hand rolling right now. And so

**[16:35]** individual agent capabilities are

**[16:37]** something we've largely solved. What's

**[16:39]** been missing is the layer that makes

**[16:40]** those capabilities composable and

**[16:42]** parallel and reliable. And so if you're

**[16:45]** building in this space, here's what

**[16:47]** doesn't exist yet that needs to exist.

**[16:49]** Number one, you need a scheduling and

**[16:51]** life cycle layer for agents. Not in the

**[16:54]** container sense, right? I'm not saying

**[16:55]** that it's a Kubernetes container. I'm

**[16:57]** saying that you need something that

**[16:58]** handles agent creation and assignment

**[17:00]** and health checking and scaling and

**[17:01]** termination as a managed service. Number

**[17:03]** two, you need merge and coordination

**[17:06]** infrastructure that is built from the

**[17:08]** ground up for parallel agent work.

**[17:10]** Right? When five agents work on related

**[17:12]** tasks simultaneously, you need merge

**[17:15]** cues, you need conflict detection, you

**[17:18]** need resolution protocols. And today

**[17:20]** this is like a bunch of duct tape and a

**[17:22]** bunch of get work trees. Like it can be

**[17:24]** so much better. You need number three,

**[17:26]** supervision hierarchies, right? Meta

**[17:28]** agents that monitor and evaluate and

**[17:30]** course correct other agents. Not as a

**[17:32]** framework pattern you have to code

**[17:33]** yourself, which so many of us have to do

**[17:35]** now, but as infrastructure that you can

**[17:37]** configure. You need financial

**[17:39]** observability, right? Across multiple

**[17:41]** agent workflows, what what did this

**[17:43]** agent spend? Uh what was the outcome

**[17:45]** quality? What's the cost per successful

**[17:47]** task? This is like Finnops for agents

**[17:50]** and it's brand new. It barely exists.

**[17:53]** Last but not least, you need standard

**[17:55]** failure patterns and standard recovery

**[17:57]** patterns. So when an agent's tool call

**[17:59]** fails, instead of making it up on an

**[18:01]** individual team basis, you have to have

**[18:03]** some like standard provisioning around

**[18:05]** what happens, right? You shouldn't have

**[18:07]** to depend on the tool, the framework,

**[18:08]** and what the PM had for lunch that day

**[18:10]** to decide whether or not your agent

**[18:12]** recovered. Look, this layer, this

**[18:14]** orchestration layer, this is the layer

**[18:16]** where the next infrastructure defining

**[18:18]** company is going to get built. The

**[18:20]** orchestration problem for agents is

**[18:22]** structurally analogous to the container

**[18:24]** orchestration problem that Kubernetes

**[18:26]** solved. Right? Not the compute itself,

**[18:28]** but the scheduling, the scaling, the

**[18:30]** health checking, the life cycle

**[18:32]** management that makes compute usable at

**[18:34]** enterprise scale. So, whoever solves

**[18:37]** orchestration at infrastructure grade is

**[18:40]** going to own the most valuable position

**[18:42]** in the agent stack. And it is too early

**[18:44]** to call a winner. So, what does all of

**[18:46]** this mean? You've seen the six layers of

**[18:48]** the stack. What does it mean for

**[18:49]** builders right now? I want to give you

**[18:51]** three lessons that you should take away

**[18:53]** if you're building on the agent stack

**[18:55]** today that are truisms for 2026. I don't

**[18:58]** think they're going to change a lot this

**[18:59]** year. The stack has to evolve

**[19:00]** significantly. Number one, right now,

**[19:03]** reliability is compounding in the wrong

**[19:05]** direction. When your agent depends on

**[19:08]** five different primitives, your

**[19:10]** endto-end reliability is the product of

**[19:12]** five different reliability. So if each

**[19:14]** delivers 99% uptime your system delivers

**[19:17]** only 95%. If it's at 97% each it's at

**[19:20]** 86. You get the idea. Essentially you

**[19:22]** are stacking the liabilities of all your

**[19:24]** agentic primitives right now because you

**[19:27]** have to compose so much of this layer by

**[19:29]** hand. Reliability is really hard to

**[19:31]** engineer these days. Number two

**[19:34]** transitional lockin is a real risk this

**[19:37]** year. Right? Building on shims like

**[19:39]** email as identity creates migration

**[19:42]** costs when native protocols arrive.

**[19:45]** Every single shim you adopt is a bet

**[19:47]** that it either becomes the standard or

**[19:50]** it becomes something that you're willing

**[19:51]** to swap out. So think about your choices

**[19:53]** and think strategically about what is

**[19:55]** truly agent native and what is something

**[19:57]** that is a practical bet and make a

**[19:59]** choice about what you think is going to

**[20:00]** be correct over the next two or three

**[20:02]** years. We're all living through this

**[20:04]** together. I can't tell you if email like

**[20:06]** a wonderful cockroach is going to

**[20:08]** survive forever because it might or if

**[20:10]** we're actually going to get true agent

**[20:12]** to agent communication that is post

**[20:14]** email. Number three, and this is a big

**[20:15]** one, agent sprawl is coming. This is the

**[20:17]** same problem that plagued microservices

**[20:19]** back in 2018 when when when you would

**[20:21]** get people literally walking into

**[20:23]** startups from places like Amazon and

**[20:24]** Microsoft and the first thing they did

**[20:26]** when when this little startup had a tiny

**[20:28]** little codebase and just wanted to ship,

**[20:30]** they would say, "Well, it all needs to

**[20:31]** be a microservices architecture."

**[20:34]** Did it? No, it didn't. It's a monolith.

**[20:36]** Shift fast. In the same way, people are

**[20:38]** looking at agents and they're saying

**[20:40]** everything needs to be an agent and it's

**[20:41]** sprawling all over the enterprise and

**[20:42]** they're taking unexpected actions and

**[20:44]** you don't have observability and you

**[20:45]** don't have an orchestration layer and so

**[20:47]** you're just kind of guessing and vibing.

**[20:48]** That is going to be a bigger and bigger

**[20:50]** problem over the course of 2026 unless

**[20:52]** people invest now in orchestration

**[20:54]** layers that yes, you're going to have to

**[20:55]** hand roll. Look, I've talked about what

**[20:57]** I think the new builder skills are. I'll

**[20:59]** just reiterate them for you here.

**[21:00]** Context engineering matters a lot these

**[21:02]** days because what you feed the agent

**[21:04]** matters for the outcomes you drive. Eval

**[21:06]** driven development matters because you

**[21:08]** have to be able to get the agent to

**[21:09]** autonomously drive against a result to

**[21:12]** avoid a lot of the bottlenecks that

**[21:13]** comes from human reviewed code and stack

**[21:16]** literacy is going to be really important

**[21:18]** right you have to know which layer in

**[21:20]** the stack is your competitive advantage

**[21:22]** and why and you have to build

**[21:24]** relentlessly against that. In the world

**[21:26]** of agents, the builders who survive, and

**[21:28]** I don't care if you're building in the

**[21:29]** space as an entrepreneur, if you're

**[21:30]** building as an individual with your open

**[21:31]** claw, or if you're building as a leader

**[21:33]** and you're building on top of the stack

**[21:34]** and you need to get agents implemented

**[21:36]** regardless, the ones who survive, you're

**[21:39]** going to have to have stack literacy.

**[21:40]** You're going to have to understand how

**[21:42]** these six layers work. You're going to

**[21:43]** have to keep a weather eye on which

**[21:45]** pieces of the stack are changing and how

**[21:47]** they affect your business. There is no

**[21:49]** excuse for lack of stack literacy. And

**[21:50]** part of the reason this matters, part of

**[21:52]** the reason I'm talking about it in this

**[21:53]** channel is because if you don't have

**[21:55]** that, even as a business leader, even as

**[21:57]** a non-CTO, non- tech leader, you are

**[22:00]** going to be in big trouble because

**[22:01]** agents drive so much business outcome

**[22:04]** and business leverage now that is so

**[22:06]** dependent on these pieces of the stack.

**[22:08]** And so if you want to have an agent that

**[22:09]** has tremendous blast radius across your

**[22:11]** customer success, you got to understand

**[22:13]** what's driving that. What parts of the

**[22:15]** stack actually work? What parts of the

**[22:16]** stack are you hand rolling? What are

**[22:18]** your shims that you're betting on? If

**[22:20]** you don't have that detailed

**[22:21]** understanding, you're just kind of

**[22:23]** hoping and praying that the agent works.

**[22:25]** That's not a good strategy for the long

**[22:26]** term. And so, we need to have better

**[22:29]** stack literacy. And that's why this

**[22:31]** video is important. So, share it with

**[22:33]** someone who doesn't understand the agent

**[22:35]** stack because I guarantee you there are

**[22:37]** a lot of people who are walking around

**[22:38]** with a lot of LinkedIn buzzwords in

**[22:40]** their heads and they don't understand

**[22:41]** the agent stack. And that's going to

**[22:43]** lead to a lot of suffering and pain.

**[22:45]** Frankly, for a lot of IC engineering

**[22:47]** teams, they're going to be asked to

**[22:48]** build stuff that doesn't make any sense.

**[22:50]** Best of luck with that. Cheers.
