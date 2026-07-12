# Transcript: Your SaaS Bill Just Got a Second Meter. You're About to Pay It.

**URL:** https://www.youtube.com/watch?v=adNErrz2aA0
**Segments:** 475
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 16:23
**Uploaded:** 2026-05-15

---

## Full Text

Salesforce just reported that Agent Force, their agent product, hit $800 million run rate in ARR, up 169% year-over-year with 2.4 billion agentic work units processed. That is not tokens, that is work units. Salesforce is now counting the actions agents complete inside the platform and billing according to those actions, not the token. Similar patterns are cropping up other places. In the same week, Microsoft Agent 365 went generally available. It costs $15 per user per month, and the governance license specifically manages how agents act inside your Microsoft environment, and the Microsoft environment acts as the control plane. So, if you're building agents that touch Salesforce, that touch Microsoft systems, you're going to start to see this price tag show up. Most builders are going to start to need to face what it costs to implement agentic workflows across larger context systems at scale. And it won't just be model billing costs. Increasingly, it's going to be other players involved who are effectively setting up toll booths along the way to make sure that they get their piece of the value you're creating. So, the question you need to answer before your next vendor renewal is this. What are you paying for when the work moves from a person to a machine? Because a machine can do it now, but the toll booth, the pricing looks different. I want to open up four questions that are underneath that big overarching question. Number one, what is the pricing meter here, and does it make sense for your business? Number two, what counts as a fair agent license versus one that's just effectively SaaS seat protection in a new costume? Number three, where is a vendor using policy language that might lock out your agents? And number four, what does a cost to wear agent look like in production? Because that's the thing that's going to matter long term. For two decades, SaaS pricing ran on a very simple trick. You turn work into seats, which leads to predictable revenue, which leads to predictable growth in and and because we continued to need to introduce more work to computers, do more work on computers, have specialized software for the workforce using computers, that whole model turned into an absolute bonanza of cash flow for SaaS companies. We all know that is in jeopardy at this point. The model of having 10 people sitting on a CRM and billing for 10 seats is in question. And this affects some of the biggest names in the business, right? HR can run on Workday, engineering on Jira, marketing on Hub Spot, IT on ServiceNow. Everybody's having to rethink their business models, and the companies I just named are at very different spots on that rethinking agentic spectrum. Some are much farther along, some are not. But regardless, before the agentic workflow revolution started, every vendor could point to a group of humans and say, "These are the people who use our software, so these are the people that need licenses." And that model worked because the human was the unit of software value. A person logged in and clicked and updated records and did workflows, and the vendor charged for that person's access, and now that doesn't work anymore. AI agents just break that entirely because an agent can use software without sitting in the software. It can read from the CRM, update a support ticket, grab a ServiceNow workflow, update a Jira issue. You get the idea, right? The work still happens, the vendor's system still carries the data and the permissions and the audit trail, but the idea of using the software just doesn't capture the value exchange anymore, and companies are getting savvy to that. And that is why all the vendors out there are effectively the vendors formerly known as SaaS at this point, and they're all building toward different versions of a new pricing model. And we need to understand what that pricing model is in order to make sure we make smart decisions about the real cost of agentic workflows going forward. Let me walk through three versions so you can start to see the pattern here. First, Salesforce is the cleanest example because they're not hiding the shift at all. Agent Force pricing uses flex credits and agentic work units. You update a record, you summarize a case, you answer an inquiry, execute a prompt, run a workflow, whatever. Each one draws from the same meter. The old model was the service rep has a seat, and the new model is, at least according to Salesforce, the rep might have a seat, but the agent that identifies the customer and retrieves prior cases and triggers the workflow also burns credits. The seat is still there, it just isn't the whole bill anymore. Now, Microsoft is example two, and I think it's a hybrid model like this, but it's at obviously a massive scale, right? Microsoft 365 Copilot absolutely still uses seat pricing, but Copilot Studio pricing makes that second agentic meter extremely explicit. Copilot credits measure agent usage in different features, consume credits at different rates, right? Answers, generative answers, agent actions, uh grounding in the graph, flow actions, premium reasoning, whatever that means. And so, the realistic monthly cost for a 100-seat company running modest agent workloads starts to scale up as you run these runtime credits. It's not necessarily going to be a very low bill for you if you are running premium credits and premium reasoning and premium workflow. Again, someone who's trying to figure out how to plan agentic workflows is facing this this forest of pricing complexity in what used to be a very clear per-seat cost. Do I use premium reasoning for Copilot? How much do I use reasoning? And and and no one's ready to answer that because everything is changing so quickly. I was talking to a developer just this past week who has used 8 billion tokens in the last month. 8 billion in a month. Uh that was not the case in 2025. We are scaling token usage really really fast, and it makes it difficult to plan when the SaaS survival model is to charge you per token and hope that you'll figure it out. This is part of why I talked to a lot of CTOs and CIOs who are very very frustrated with the procurement landscape right now. ServiceNow comes at this from the operational side. It's our third example. The action fabric re-frames ServiceNow from a place where employees click around into a system where agents trigger real operational work through governed pathways with identity and permissions and audit all sort of attached. These are units of operational work, not API calls. If an agent provisions access and escalates an incident and kicks off onboarding or opens a change request, then ServiceNow has a claim that it is providing the workflow substrate and the operational reliability around that action charge accordingly. So, these three vendors, right? Microsoft, Salesforce, ServiceNow, they are all making kind of the same move, right? The seat is staying and they're turning on a second meter for delegated work. Now, I have a full eight-vendor breakdown in the Substack post for today including Zendesk outcome pricing, HubSpot's per resolution model, Workday's agent system of record, and Atlassian's soft launch credit pattern with Rovo. And with that pricing model comes new pricing rules. And I want you to watch this carefully because the new pricing rules are going to feel, in some cases, anti-developer and anti-agent. SAP's 2026 API policy draws a very hard line around how customers and third-party systems can use SAP APIs. This made the news recently. I talked about it briefly, including restrictions on AI systems that plan, select, or execute sequences of API calls outside of SAP endorsed architectures. Translation, if you want an outside agent, an internal agent, another vendor's assistant to act on your SAP data, the first question is going to be contractual, not technical, cuz contractually you're going to have to ask, "Is this even allowed under the under the terms of the engagement that we signed?" And so, if you're building agents that need to touch SAP data systems, you have to understand that SAP is at minimum going to want a toll booth, but may not even allow you to at all. And so, I think that the question I have for you is, "How do you think about pushing back?" And I have some suggested policy language to push back for vendors in the Substack here. If you're in an active negotiation, I've got some suggested language. But, the larger conversation you need to have is you need to talk during the procurement and negotiation process with the vendor and say, "Look, our agents are from X or Y provider, right? Claude, OpenAI, whatever. We need to have them be able to access your system in X, Y, and Z ways. How do we make sure that that's something that remains inside a particular budget and cost envelope, and how do we make sure that the developer experience is clean enough that we can get value?" And I don't see those conversations happening very often. And part of why they're not happening very frequently is that the vendors don't want them to happen very frequently because pricing follows platform control. The vendor that defines the new work primitive earns the argument that it should price the work. And all of the vendors I'm talking about are thinking about that really actively right now. Salesforce meters agent actions because Salesforce defines many of the actions inside the customer relationship workflow. ServiceNow operational actions because ServiceNow defines a large part of the enterprise action layer. Microsoft wants Copilot credits because Microsoft sits across the productivity graph. SAP wants sanctioned pathways because SAP owns high-consequence systems where uncontrolled agent execution is an operational risk. If you build on these platforms without understanding their incentives and how they're inclined to meter, your agent's economics end up belonging to somebody else. So, what does a fair agent license actually look like, and what does one that's more of a rent-seeking approach look like? I I think let's keep it simple here. A fair version, it the meter has to be visible, and the unit has to make sense and be transparent. The customer has to be able to forecast usage. Failed or low-value work cannot be billed the same as completed work. Third-party agents need to have a governed path, not a blocked path. And the vendor needs to distinguish between reading, drafting, writing, approving, and executing for agents and bill accordingly. The buyer needs to be able to set caps. Usage data needs to be exportable. The rate card cannot shift after you've adopted these agents. Now, what is a rent-seeking version like? Right? The above is like what the buyer is going to want. A an unscrupulous vendor, and I'm not saying any of these vendors are unscrupulous, just to be clear. But but I have seen patterns like this from other vendors. A rent-seeking version from a vendor looks like this. It charges for vague AI access without explaining what's consumed. It makes the vendor's own agent the only practical route while treating outside agents as hostile. It charges customers to use their own data in their own workflows. It will count failed work as billable work. It will hide the meter until renewal. It will bundle credits that expire unused while billing overages right away. It'll dress up commercial lock-ins in security language. Look, if you have a confusing mess of a contract with seat counts and API clauses and bot policies and a pile of AI pilot scattered across departments, you don't have a solution that touches production workflows, and you don't have any kind of cost envelope that lets you figure out how much that's going to be. I've put together a full checklist in the Substack with nine different traits around agent licenses, specific flags that you can look at that pick out these rent-seeking clauses, but I want the larger point to be this. You need to be aware that the agentic revolution looks like dollar signs to a lot of companies who are going to be selling you agentic solutions. Many of those are going to be good, and some of those are going to be rent-seeking. And you need to start asking very, very specific questions in the conversation to ensure that the pricing model used contractually reflects the likely scale-up in agentic workflows that you will experience over the next 12 months, because it is absolutely exploding. That 8 billion token conversation, you know, the best part of that is I wasn't even surprised cuz I know other developers who burnt 8 billion tokens, too. That's just how it goes now. And this is the part where I want to talk to developers. Because if you're building agents, most agentic teams do not pay enough attention to the actual cost structure of their agents. It's not just tokens anymore. If you heard the first part of this video, it's workflow units. It depends on your contracts. Your prototype may work because you built it and you know how it works and the volumes are tiny. You need to ask yourself as a builder if the API policy your company signed permits autonomous execution. You need to ask yourself, what is the billing unit? Is it successfully completed work? Is it any completed work? Is it attempts at work? Is it tokens? And then you need to optimize for that because I guarantee you your CTO will be asked, how are we optimizing this massive scale up in agentic workflow around costs? What is the budget cap here? Is this a reasonable thing for us to be doing or are we just turning dollars into tokens for little output? And so you need to start to look at your operation classifications in detail. You need to understand where are your agents going to be spending tokens to read versus write versus approve versus execute. What's the blast radius and impact of that from a work value perspective? And those distinctions matter because they may directly impact the pricing on the vendor meter. And all of this, all of this is about deployable agents that matter, right? An agent that knows which tools are expensive, which actions are reversible, when to read versus when to write is an agent that a company can put into production. An agent that treats every tool call the same way regardless of the budget is an incident waiting to happen. So I put together on the Substack a full operation taxonomy for this and a cost dashboard I would use for an enterprise agent product. It is something that as a developer or as a builder, you have to have an eye on if you want to actually deploy these agents in production. And I do know many developers who pay attention to this. This is not all developers, but I just want you to be aware that most developers I'm talking to who are cost-aware still think in terms of tokens. And at the contractual level, it is shifting past tokens now. You have to think more broadly and talk more deeply about the contracts with legal and with your CTO. There's just no other way around it. So, what do you actually do with this before your next renewal conversation? The worst move you could do is to wait until your usage is embedded because you have no leverage then, right? If employees use the agent every day, if customer workflows depend on it, the power dynamic shifts. The vendor knows the work has moved and the value is in the agents and turning it off will hurt and they will charge you accordingly. So, the the better move is to negotiate agent access up front before agent usage becomes mission critical. Be very clear what is included in current seats. Ask whether agents acting on behalf of users are covered. Ask whether an independent agent requires its own entitlement. Ask whether third-party agents can use the same governed path as the vendor's own agent. Ask which actions are going to consume credits or not. Ask whether failed actions count. Ask whether the rate card is fixed for the term. Ask whether usage logs can be exported. Ask whether caps can be set by department, by workflow, by agent. Most importantly, ask how the commercial model changes if the agent reduces human seats. Because that question cuts at the SaaS economics in play here. If an AI agent resolves a huge volume of customer support requests, can you reduce your support seats? If a sales agent keeps your records updated, can occasional CRM users move to lighter access? If an HR agent handles routine questions about vacation, does every employee need the same tier? Sometimes the answer is no for good reasons, but the question needs to be asked. Otherwise, you end up with the worst possible hybrid, an old seat count plus a new and untransparent agent consumption bill. So, I have the full renewal question list over on Substack with 15 questions organized by what to ask before you sign, what to ask about the agent's access path, and what to ask about the commercial model when agent work starts replacing human work in some fashion, which is not the same as replacing jobs, by the way. Anyway, you can go get it. The agent era is changing the commercial unit of software. It's not just changing the interface. The seat was always a proxy for human work and value created, and the agent license is becoming a meter for that same unit of value, except now that it's been delegated. Builders who understand that distinction between how agent work bills and how human work bills are going to design and negotiate much better deals and avoid the trap of shipping an agent that works until the bill shows up. So, if you want to keep learning how to build with AI, hit subscribe, and for that deep version on this one, check out the Substack. Happy building. Make sure you understand what you're signing when you get those contracts. Cheers.

---

## Timestamped Segments

**[0:00]** Salesforce just reported that Agent

**[0:02]** Force, their agent product, hit $800

**[0:04]** million run rate in ARR, up 169%

**[0:06]** year-over-year with 2.4 billion agentic

**[0:10]** work units processed. That is not

**[0:11]** tokens, that is work units. Salesforce

**[0:13]** is now counting the actions agents

**[0:16]** complete inside the platform and billing

**[0:18]** according to those actions, not the

**[0:20]** token. Similar patterns are cropping up

**[0:22]** other places. In the same week,

**[0:24]** Microsoft Agent 365 went generally

**[0:26]** available. It costs $15 per user per

**[0:29]** month, and the governance license

**[0:31]** specifically manages how agents act

**[0:33]** inside your Microsoft environment, and

**[0:35]** the Microsoft environment acts as the

**[0:37]** control plane. So, if you're building

**[0:39]** agents that touch Salesforce, that touch

**[0:41]** Microsoft systems, you're going to start

**[0:44]** to see this price tag show up. Most

**[0:45]** builders are going to start to need to

**[0:48]** face

**[0:49]** what it costs to implement agentic

**[0:52]** workflows across larger context systems

**[0:55]** at scale. And it won't just be model

**[0:57]** billing costs. Increasingly, it's going

**[0:59]** to be other players involved who are

**[1:01]** effectively setting up toll booths along

**[1:04]** the way to make sure that they get their

**[1:07]** piece of the value you're creating. So,

**[1:09]** the question you need to answer before

**[1:11]** your next vendor renewal is this. What

**[1:13]** are you paying for when the work moves

**[1:16]** from a person to a machine? Because a

**[1:18]** machine can do it now, but the toll

**[1:19]** booth, the pricing looks different. I

**[1:21]** want to open up four questions that are

**[1:23]** underneath that big overarching

**[1:25]** question. Number one, what is the

**[1:26]** pricing meter here, and does it make

**[1:28]** sense for your business? Number two,

**[1:30]** what counts as a fair agent license

**[1:32]** versus one that's just effectively SaaS

**[1:34]** seat protection in a new costume? Number

**[1:36]** three,

**[1:37]** where is a vendor using policy language

**[1:39]** that might lock out your agents? And

**[1:41]** number four, what does a cost to wear

**[1:43]** agent look like in production? Because

**[1:45]** that's the thing that's going to matter

**[1:46]** long term. For two decades, SaaS pricing

**[1:49]** ran on a very simple trick. You turn

**[1:51]** work into seats, which leads to

**[1:52]** predictable revenue, which leads to

**[1:54]** predictable growth in and

**[1:55]** and because we continued to need to

**[1:58]** introduce more work to computers, do

**[2:00]** more work on computers, have specialized

**[2:02]** software for the workforce using

**[2:04]** computers, that whole model turned into

**[2:06]** an absolute bonanza of cash flow for

**[2:09]** SaaS companies. We all know that is in

**[2:12]** jeopardy at this point. The model of

**[2:13]** having 10 people sitting on a CRM and

**[2:16]** billing for 10 seats is in question. And

**[2:19]** this affects some of the biggest names

**[2:20]** in the business, right? HR can run on

**[2:22]** Workday, engineering on Jira, marketing

**[2:24]** on Hub Spot, IT on ServiceNow.

**[2:26]** Everybody's having to rethink their

**[2:28]** business models, and the companies I

**[2:29]** just named are at very different spots

**[2:31]** on that rethinking agentic spectrum.

**[2:33]** Some are much farther along, some are

**[2:35]** not. But regardless, before the agentic

**[2:39]** workflow revolution started, every

**[2:41]** vendor could point to a group of humans

**[2:43]** and say, "These are the people who use

**[2:45]** our software, so these are the people

**[2:46]** that need licenses." And that model

**[2:48]** worked because the human was the unit of

**[2:50]** software value. A person logged in and

**[2:52]** clicked and updated records and did

**[2:53]** workflows, and the vendor charged for

**[2:55]** that person's access, and now that

**[2:57]** doesn't work anymore. AI agents just

**[2:58]** break that entirely because an agent can

**[3:00]** use software without sitting in the

**[3:01]** software. It can read from the CRM,

**[3:03]** update a support ticket, grab a

**[3:05]** ServiceNow workflow, update a Jira

**[3:07]** issue. You get the idea, right? The work

**[3:09]** still happens, the vendor's system still

**[3:12]** carries the data and the permissions and

**[3:14]** the audit trail, but the idea of using

**[3:16]** the software just doesn't capture the

**[3:18]** value exchange anymore, and companies

**[3:20]** are getting savvy to that. And that is

**[3:22]** why all the vendors out there are

**[3:23]** effectively the vendors formerly known

**[3:25]** as SaaS at this point, and they're all

**[3:26]** building toward different versions of a

**[3:28]** new pricing model. And we need to

**[3:30]** understand what that pricing model is in

**[3:32]** order to make sure we make smart

**[3:33]** decisions about the real cost of agentic

**[3:36]** workflows going forward. Let me walk

**[3:38]** through three versions so you can start

**[3:40]** to see the pattern here.

**[3:41]** First, Salesforce is the cleanest

**[3:44]** example because they're not hiding the

**[3:45]** shift at all. Agent Force pricing uses

**[3:47]** flex credits and agentic work units. You

**[3:50]** update a record, you summarize a case,

**[3:51]** you answer an inquiry, execute a prompt,

**[3:54]** run a workflow, whatever. Each one draws

**[3:56]** from the same meter. The old model was

**[3:59]** the service rep has a seat, and the new

**[4:00]** model is, at least according to

**[4:02]** Salesforce, the rep might have a seat,

**[4:04]** but the agent that identifies the

**[4:05]** customer and retrieves prior cases and

**[4:07]** triggers the workflow also burns

**[4:09]** credits. The seat is still there, it

**[4:12]** just isn't the whole bill anymore. Now,

**[4:14]** Microsoft is example two, and I think

**[4:17]** it's a hybrid model like this, but it's

**[4:18]** at obviously a massive scale, right?

**[4:20]** Microsoft 365 Copilot absolutely still

**[4:23]** uses seat pricing, but Copilot Studio

**[4:25]** pricing makes that second agentic meter

**[4:28]** extremely explicit. Copilot credits

**[4:30]** measure agent usage in different

**[4:32]** features, consume credits at different

**[4:33]** rates, right? Answers, generative

**[4:35]** answers, agent actions,

**[4:37]** uh grounding in the graph, flow actions,

**[4:40]** premium reasoning, whatever that means.

**[4:42]** And so, the realistic monthly cost for a

**[4:44]** 100-seat company running modest agent

**[4:46]** workloads starts to scale up as you run

**[4:49]** these runtime credits. It's not

**[4:51]** necessarily going to be a very low bill

**[4:54]** for you if you are running premium

**[4:56]** credits and premium reasoning and

**[4:58]** premium workflow. Again, someone who's

**[5:00]** trying to figure out how to plan agentic

**[5:01]** workflows is facing this this forest of

**[5:05]** pricing complexity in what used to be a

**[5:07]** very clear per-seat cost. Do I use

**[5:10]** premium reasoning for Copilot? How much

**[5:11]** do I use reasoning? And and and no one's

**[5:13]** ready to answer that because everything

**[5:15]** is changing so quickly. I was talking to

**[5:17]** a developer just this past week who has

**[5:21]** used 8 billion tokens in the last month.

**[5:25]** 8 billion in a month.

**[5:27]** Uh that was not the case in 2025. We are

**[5:29]** scaling token usage really really fast,

**[5:31]** and it makes it difficult to plan when

**[5:34]** the SaaS survival model is to charge you

**[5:37]** per token and hope that you'll figure it

**[5:39]** out. This is part of why I talked to a

**[5:42]** lot of CTOs and CIOs who are very very

**[5:44]** frustrated with the procurement

**[5:45]** landscape right now. ServiceNow comes at

**[5:47]** this from the operational side. It's our

**[5:49]** third example. The action fabric

**[5:50]** re-frames ServiceNow from a place where

**[5:52]** employees click around into a system

**[5:54]** where agents trigger real operational

**[5:56]** work through governed pathways with

**[5:57]** identity and permissions and audit all

**[5:59]** sort of attached. These are units of

**[6:01]** operational work, not API calls. If an

**[6:03]** agent provisions access and escalates an

**[6:05]** incident and kicks off onboarding or

**[6:07]** opens a change request, then ServiceNow

**[6:09]** has a claim that it is providing the

**[6:12]** workflow substrate and the operational

**[6:14]** reliability around that action charge

**[6:16]** accordingly. So, these three vendors,

**[6:19]** right? Microsoft, Salesforce,

**[6:21]** ServiceNow, they are all making kind of

**[6:23]** the same move, right? The seat is

**[6:24]** staying and they're turning on a second

**[6:26]** meter for delegated work.

**[6:29]** Now, I have a full eight-vendor

**[6:30]** breakdown in the Substack post for today

**[6:32]** including Zendesk outcome pricing,

**[6:34]** HubSpot's per resolution model,

**[6:36]** Workday's agent system of record, and

**[6:38]** Atlassian's soft launch credit pattern

**[6:40]** with Rovo. And with that pricing model

**[6:42]** comes new pricing rules. And I want you

**[6:44]** to watch this carefully because the new

**[6:45]** pricing rules are going to feel, in some

**[6:49]** cases, anti-developer and anti-agent.

**[6:51]** SAP's 2026 API policy draws a very hard

**[6:54]** line around how customers and

**[6:55]** third-party systems can use SAP APIs.

**[6:58]** This made the news recently. I talked

**[6:59]** about it briefly, including restrictions

**[7:01]** on AI systems that plan, select, or

**[7:03]** execute sequences of API calls outside

**[7:06]** of SAP endorsed architectures.

**[7:08]** Translation, if you want an outside

**[7:10]** agent, an internal agent, another

**[7:12]** vendor's assistant to act on your SAP

**[7:14]** data, the first question is going to be

**[7:16]** contractual, not technical, cuz

**[7:18]** contractually you're going to have to

**[7:19]** ask, "Is this even allowed under the

**[7:21]** under the terms of the engagement that

**[7:22]** we signed?" And so, if you're building

**[7:24]** agents that need to touch SAP data

**[7:26]** systems, you have to understand that SAP

**[7:28]** is at minimum going to want a toll

**[7:30]** booth, but may not even allow you to at

**[7:31]** all. And so, I think that the question I

**[7:34]** have for you is, "How do you think about

**[7:37]** pushing back?" And I have some suggested

**[7:38]** policy language to push back for vendors

**[7:40]** in the Substack here. If you're in an

**[7:42]** active negotiation, I've got some

**[7:44]** suggested language. But, the larger

**[7:47]** conversation you need to have is you

**[7:49]** need to talk during the procurement and

**[7:52]** negotiation process with the vendor and

**[7:55]** say, "Look,

**[7:56]** our agents are from X or Y provider,

**[8:00]** right? Claude, OpenAI, whatever. We need

**[8:02]** to have them be able to access your

**[8:04]** system in X, Y, and Z ways. How do we

**[8:06]** make sure that that's something that

**[8:07]** remains inside a particular budget and

**[8:09]** cost envelope, and how do we make sure

**[8:11]** that the developer experience is clean

**[8:13]** enough that we can get value?"

**[8:16]** And I don't see those conversations

**[8:17]** happening very often. And part of why

**[8:19]** they're not happening very frequently is

**[8:21]** that the vendors don't want them to

**[8:22]** happen very frequently because pricing

**[8:24]** follows platform control. The vendor

**[8:27]** that defines the new work primitive

**[8:29]** earns the argument that it should price

**[8:30]** the work. And all of the vendors I'm

**[8:32]** talking about are thinking about that

**[8:34]** really actively right now. Salesforce

**[8:36]** meters agent actions because Salesforce

**[8:38]** defines many of the actions inside the

**[8:41]** customer relationship workflow.

**[8:42]** ServiceNow

**[8:44]** operational actions because ServiceNow

**[8:46]** defines a large part of the enterprise

**[8:47]** action layer. Microsoft wants Copilot

**[8:50]** credits because Microsoft sits across

**[8:51]** the productivity graph.

**[8:53]** SAP wants sanctioned pathways because

**[8:55]** SAP owns high-consequence systems where

**[8:57]** uncontrolled agent execution is an

**[8:59]** operational risk. If you build on these

**[9:02]** platforms without understanding their

**[9:03]** incentives and how they're inclined to

**[9:05]** meter, your agent's economics end up

**[9:08]** belonging to somebody else. So, what

**[9:10]** does a fair agent license actually look

**[9:12]** like, and what does one that's more of a

**[9:14]** rent-seeking approach look like?

**[9:16]** I I think let's keep it simple here. A

**[9:18]** fair version, it the meter has to be

**[9:20]** visible, and the unit has to make sense

**[9:23]** and be transparent. The customer has to

**[9:25]** be able to forecast usage. Failed or

**[9:27]** low-value work cannot be billed the same

**[9:29]** as completed work. Third-party agents

**[9:32]** need to have a governed path, not a

**[9:34]** blocked path. And the vendor needs to

**[9:36]** distinguish between reading, drafting,

**[9:39]** writing, approving, and executing for

**[9:41]** agents and bill accordingly. The buyer

**[9:43]** needs to be able to set caps. Usage data

**[9:45]** needs to be exportable. The rate card

**[9:47]** cannot shift after you've adopted these

**[9:49]** agents.

**[9:50]** Now, what is a rent-seeking version

**[9:52]** like? Right? The above is like what the

**[9:53]** buyer is going to want. A an

**[9:55]** unscrupulous vendor, and I'm not saying

**[9:57]** any of these vendors are unscrupulous,

**[9:58]** just to be clear. But but I have seen

**[10:00]** patterns like this from other vendors.

**[10:03]** A rent-seeking version from a vendor

**[10:05]** looks like this. It charges for vague AI

**[10:07]** access without explaining what's

**[10:08]** consumed. It makes the vendor's own

**[10:10]** agent the only practical route while

**[10:12]** treating outside agents as hostile. It

**[10:14]** charges customers to use their own data

**[10:16]** in their own workflows. It will count

**[10:18]** failed work as billable work. It will

**[10:20]** hide the meter until renewal. It will

**[10:21]** bundle credits that expire unused while

**[10:24]** billing overages right away. It'll dress

**[10:26]** up commercial lock-ins in security

**[10:28]** language. Look, if you have a confusing

**[10:32]** mess of a contract with seat counts and

**[10:33]** API clauses and bot policies and a pile

**[10:36]** of AI pilot scattered across

**[10:38]** departments, you don't have a solution

**[10:40]** that touches production workflows, and

**[10:42]** you don't have any kind of cost envelope

**[10:44]** that lets you figure out how much that's

**[10:45]** going to be. I've put together a full

**[10:47]** checklist in the Substack with nine

**[10:49]** different traits around agent licenses,

**[10:50]** specific flags that you can look at that

**[10:53]** pick out these rent-seeking clauses,

**[10:56]** but I want the larger point to be this.

**[10:58]** You need to be aware that the agentic

**[11:02]** revolution looks like dollar signs to a

**[11:04]** lot of companies who are going to be

**[11:07]** selling you agentic solutions. Many of

**[11:09]** those are going to be good, and some of

**[11:12]** those are going to be rent-seeking. And

**[11:15]** you need to start asking very, very

**[11:17]** specific questions in the conversation

**[11:19]** to ensure that the pricing model used

**[11:21]** contractually reflects the likely

**[11:24]** scale-up in agentic workflows that you

**[11:27]** will experience over the next 12 months,

**[11:28]** because it is absolutely exploding. That

**[11:30]** 8 billion token conversation, you know,

**[11:32]** the best part of that is I wasn't even

**[11:34]** surprised cuz I know other developers

**[11:36]** who burnt 8 billion tokens, too.

**[11:38]** That's just how it goes now.

**[11:40]** And this is the part where I want to

**[11:41]** talk to developers. Because if you're

**[11:43]** building agents,

**[11:45]** most agentic teams do not pay enough

**[11:48]** attention to the actual cost structure

**[11:50]** of their agents. It's not just tokens

**[11:52]** anymore. If you heard the first part of

**[11:53]** this video, it's workflow units. It

**[11:55]** depends on your contracts. Your

**[11:57]** prototype may work because you built it

**[12:00]** and you know how it works and the

**[12:01]** volumes are tiny. You need to ask

**[12:03]** yourself as a builder if the API policy

**[12:06]** your company signed permits autonomous

**[12:08]** execution. You need to ask yourself,

**[12:10]** what is the billing unit? Is it

**[12:11]** successfully completed work? Is it any

**[12:13]** completed work? Is it attempts at work?

**[12:15]** Is it tokens? And then you need to

**[12:17]** optimize for that because I guarantee

**[12:19]** you your CTO will be asked, how are we

**[12:22]** optimizing this massive scale up in

**[12:24]** agentic workflow around costs? What is

**[12:26]** the budget cap here? Is this a

**[12:28]** reasonable thing for us to be doing or

**[12:31]** are we just turning dollars into tokens

**[12:33]** for little output?

**[12:35]** And so you need to start to look at your

**[12:36]** operation classifications in detail. You

**[12:39]** need to understand where are your agents

**[12:41]** going to be spending tokens to read

**[12:43]** versus write versus approve versus

**[12:45]** execute. What's the blast radius and

**[12:46]** impact of that from a work value

**[12:48]** perspective? And those distinctions

**[12:50]** matter because they may directly impact

**[12:53]** the pricing on the vendor meter. And all

**[12:55]** of this, all of this is about deployable

**[12:58]** agents that matter, right? An agent that

**[12:59]** knows which tools are expensive, which

**[13:02]** actions are reversible, when to read

**[13:03]** versus when to write is an agent that a

**[13:06]** company can put into production. An

**[13:07]** agent that treats every tool call the

**[13:09]** same way regardless of the budget is an

**[13:11]** incident waiting to happen. So I put

**[13:13]** together on the Substack a full

**[13:15]** operation taxonomy for this and a cost

**[13:17]** dashboard I would use for an enterprise

**[13:19]** agent product. It is something that as a

**[13:21]** developer or as a builder, you have to

**[13:23]** have an eye on if you want to actually

**[13:24]** deploy these agents in production. And I

**[13:26]** do know many developers who pay

**[13:28]** attention to this. This is not all

**[13:29]** developers, but I just want you to be

**[13:31]** aware that most developers I'm talking

**[13:33]** to who are cost-aware still think in

**[13:35]** terms of tokens. And at the contractual

**[13:37]** level, it is shifting past tokens now.

**[13:39]** You have to think more broadly and talk

**[13:41]** more deeply about the contracts with

**[13:43]** legal and with your CTO. There's just no

**[13:45]** other way around it. So, what do you

**[13:46]** actually do with this before your next

**[13:48]** renewal conversation? The worst move you

**[13:50]** could do is to wait until your usage is

**[13:52]** embedded because you have no leverage

**[13:54]** then, right? If employees use the agent

**[13:56]** every day, if customer workflows depend

**[13:58]** on it, the power dynamic shifts. The

**[13:59]** vendor knows the work has moved and the

**[14:02]** value is in the agents and turning it

**[14:03]** off will hurt and they will charge you

**[14:05]** accordingly. So, the the better move is

**[14:07]** to negotiate agent access up front

**[14:10]** before agent usage becomes mission

**[14:12]** critical. Be very clear what is included

**[14:15]** in current seats. Ask whether agents

**[14:17]** acting on behalf of users are covered.

**[14:19]** Ask whether an independent agent

**[14:20]** requires its own entitlement. Ask

**[14:22]** whether third-party agents can use the

**[14:24]** same governed path as the vendor's own

**[14:27]** agent. Ask which actions are going to

**[14:29]** consume credits or not. Ask whether

**[14:31]** failed actions count. Ask whether the

**[14:33]** rate card is fixed for the term. Ask

**[14:35]** whether usage logs can be exported. Ask

**[14:38]** whether caps can be set by department,

**[14:40]** by workflow, by agent. Most importantly,

**[14:43]** ask how the commercial model changes if

**[14:46]** the agent reduces human seats. Because

**[14:49]** that question cuts at the SaaS economics

**[14:51]** in play here. If an AI agent resolves a

**[14:54]** huge volume of customer support

**[14:56]** requests, can you reduce your support

**[14:58]** seats? If a sales agent keeps your

**[15:00]** records updated, can occasional CRM

**[15:03]** users move to lighter access? If an HR

**[15:06]** agent handles routine questions about

**[15:07]** vacation, does every employee need the

**[15:09]** same tier? Sometimes the answer is no

**[15:11]** for good reasons, but the question needs

**[15:13]** to be asked. Otherwise, you end up with

**[15:16]** the worst possible hybrid, an old seat

**[15:18]** count plus a new and untransparent agent

**[15:21]** consumption bill. So, I have the full

**[15:23]** renewal question list over on Substack

**[15:25]** with 15 questions organized by what to

**[15:27]** ask before you sign, what to ask about

**[15:30]** the agent's access path, and what to ask

**[15:31]** about the commercial model when agent

**[15:33]** work starts replacing human work in some

**[15:35]** fashion, which is not the same as

**[15:37]** replacing jobs, by the way. Anyway, you

**[15:39]** can go get it. The agent era is changing

**[15:42]** the commercial unit of software.

**[15:44]** It's not just changing the interface.

**[15:46]** The seat was always a proxy for human

**[15:48]** work and value created, and the agent

**[15:50]** license is becoming a meter for that

**[15:53]** same unit of value, except now that it's

**[15:55]** been delegated. Builders who understand

**[15:58]** that distinction between how agent work

**[16:01]** bills and how human work bills are going

**[16:03]** to design and negotiate much better

**[16:05]** deals and avoid the trap of shipping an

**[16:08]** agent that works until the bill shows

**[16:11]** up. So, if you want to keep learning how

**[16:12]** to build with AI, hit subscribe, and for

**[16:14]** that deep version on this one, check out

**[16:16]** the Substack. Happy building.

**[16:18]** Make sure you understand what you're

**[16:19]** signing when you get those contracts.

**[16:21]** Cheers.
