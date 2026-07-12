# Transcript: Your Agent Produces at 100x. Your Org Reviews at 3x. That's the Problem.

**URL:** https://www.youtube.com/watch?v=kVPVmz0qJvY
**Segments:** 625
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 21:13
**Uploaded:** 2026-04-05

---

## Full Text

The scary thing about the OpenClaw stories is that so many of them are real. You can actually build a complete $320,000 value SAS replacement suite by hooking your OpenClaw up to APIs. Yes, and that's true. You can also build a complete CRM replacement in just a few days with OpenClaw. Also true. Also a verified story. Yes, you can scale your ad created from 20 to 2,000. Also true. Also a verified story. And the point of all of that is that you are taking a tool that is designed to be a general purpose agent and using it to cover over a lot of your own existing issues. And that's what I want to talk about today. Because when we talk about Open Claw, what we're talking about is the enthusiasm and the energy that comes from the world's first widely available general purpose agent. And I love all that hype. I love that energy. I love that you actually can do this stuff with OpenClaw. But what I don't love is that so many people are taking it as a blank slate permission slip and just saying, you know what, it doesn't matter. It's okay. I don't have to think about my data anymore. I don't have to think about my best practices anymore. I don't have to think about my software anymore. OpenClaw will make it better. No, it won't. Open Claw will not fix those things. Look, I've spent the last couple of years arguing that the biggest risk that we face in software is not taking our entire stack seriously when we bring AI into it. If we're going to do a true reinvention for AI, we need to actually take seriously the idea that AI will need to be at the heart of a reinvented stack. We cannot just stick an open claw agent over the top, paper over all of the data issues, and pretend it's going to work. It won't. It just won't. Now, I want to be precise about what OpenClaw actually is because the discourse has gotten very muddy with all of the hype and the hundreds of thousands of GitHub stars and everything else. OpenClaw is an open-source self-hosted model agnostic AI agent framework. It runs as a persistent Damon on your machine. It connects to your messaging app, Slack, WhatsApp, Telegram, Signal, you name it. And it acts on your behalf through shell access, browser automation, file operations, email, etc. It has a skill system that lets the agent extend itself into a bunch of communitybuilt capabilities and it has a set of memory that was originally stored as markdown files and is now undergoing some changes. The combination of all of those things as a modular architecture is new and was extremely explosive when it came out. We all know that. I've told that story. The problem is we are now a few months into the open claw story and what we're finding is that the story gets more complicated as you try and use your open claw agent to paper over inefficiencies and weaknesses in your stack. And that's what I want to warn you about because you can absolutely do incredible things with openclaw 100%. But you have to make sure that you are building the layers of your software stack so that you can do that correctly. I think the simplest way to tell this story is to talk about real builds that we've had with OpenClaw and the risks that you have in that OpenClaw architecture if you don't take care of the rest of the stack. So build number one, I talked about the CRM. It's a real story. It was a real non-coder who was able to build a real CRM using OpenClaw. That is both a tremendous accomplishment, a mark of how far agents have come and also something that is absolutely terrifying if you understand how CRM are built. Not because we want to go slow, we want to go really fast and there are real speed ups available. It's because CRM are fundamentally not pieces of software. We think of them as pieces of software. And the piece that came out, well, you can vibe code this in 12 days or whatever it was, it painted it as if OpenClaw built software that replaced a SAS. But but but that is not really what a CRM is. What a CRM is is encoded workflow logic that reflects the reality of your business in a way that makes sense for your sales process and for your customer care process. All of the things you know about your customers and how they buy and how they choose to make purchasing decisions and how they choose to keep their purchase and how they choose to expand and upgrade their purchase with you, all of that needs to have a place in your CRM. And when we talk about people who are choosing not to go with Salesforce, who are vibe coding their own CRM, and this is one of N, right? There's so many. What we see when they're at their best is that people are moving quickly. They're encoding something and they make specific decisions about their CRM that reflect what they want out of the customer relationship, why their business model exists the way it is. They have that intent, that clarity of intent. I talk about clarity of intent a lot for a reason. They have that intent across their data structures and across their workflows. And all their agent does, all their open claw does is it helps them instantiate that intent. That's all. That's it. If you have any lack of clarity in your intent. If you just point your open claw at a CRM, say, "I want to build a CRM. Please just vibe code be one." You will get trash. You will get absolute trash. Not because it's not functioning software, not because your agent can't call it, but because what is built is going to reflect generic middle-of the road a workflow that works for everybody out of the box and therefore for nobody. And you're not going to get something that actually harnesses the power of custom software, which is the whole reason you use agents in the first place. And so what I am begging you to do when you think about the promise of agentically developed software, and it is promise, and it's real, is take the high road here. There are two ways to build a Gentic software quickly. Both are fast. You're not trading speed. Number one, have clarity of intent around the workflows you are trying to encode and perhaps why they are different in the age of AI. Perhaps why your customer relationship is changing. Certainly, you should have a set of requirements that reflect what actually works on the ground in your business that's very clear, that's unique, that's different from other businesses. Otherwise, you would just buy the software, right? Then go ahead and build quickly with agents. The alternative is when you jump straight to building because that's the seductive part. That's the easy part and you don't take the time to get clear on your intent. Then you're in trouble because what you're going to get is generic average. It is whatever the average idea the LLM has of the software will be. And that's true whether you're using OpenClaw or agents uh of any kind. So that's lesson number one. It's about CRM, it's about software, it's about SAS. Lesson number two in these openclaw agent deployments that we're starting to see is that you got to get your underlying data clean. This is part of the reason I put open brain together. I wanted people to have a clean data layer. It's I don't care if it's open brain or if it's something else for you. What I worry about is that you need to use your agent on day 30, day 300 as well as you use it on day one. And if you have a dirty memory system, a memory system that is not organized, you're going to be in trouble. And why are you going to be in trouble? You're going to be in trouble because Open Claw and other agents are not by default data organizers unless you tell them to be. Unless you give them guard rails, explicit constraints that require them to respect your data schemas and keep data clean, they won't. And so you need to start to think about the world as if it is a data-shaped problem that agents can help you accelerate, but the agents themselves are going to be messy, messy data engineers unless you structure them appropriately. There is a story circulating about a team that spent $14,000 building a voice agent to handle lots of inbound calls. On paper, it seemed to work, but when you looked under the surface at the data the agent was handling, no one had specified how the schema was going to work. They found records all over the place. They had no good way to measure inbound and funnel, and it was just a complete mess, even though it was up and functioning and apparently took calls. So, take the time to get the schema right. Do not be satisfied with your open claw just because you can query it in a Slack message or a text message and it says something back. When I talk about legibility of surfaces as a key criterion for AI agents, this is what I mean. If if you just send a text message and it's like a void and you don't know what happens and then an answer comes back and you like the answer, you do not have an agent. You have a problem masquerading as a helpful answer. You really do because how do you know if it recorded it correctly? How do you know if it wrote it down anywhere? Unless you understand that stack, unless a company deliberately makes it clear and says, "We're going to be transparent. This is where your data lives. this is where it's going to be. This is how we update it. These are our guardrails. You're in trouble. And so, please, please, please, if you are building with agents, recognize that you don't want to be in the position of spending money, spending tokens on building something that looks good in a text message, but the data underneath is dirty. So, we've talked about CRM, we've talked about data clarity. You know what the next thing we need to talk about is? It is mistaking a skill for a process. I love skills. Skills are great. I've talked about how important they are. I think they're critical. Do not mistake a skill or a tool call for a process. If you have a business workflow, it should be as much as you can hardwired in. You should not be trying to take your business workflow and tell yourself it's going to work good and stick it as a skill in OpenClaw and hope it works that way for production grade data every single time. Instead, your agent should be operating across hardwired process and speeding that along. And you should be able to evaluate the success of that agent across that process. And what do I mean by that? What does that look like in practice? Let's say one of the skills your agent has is send an email. But that exists inside a larger process, right? It exists inside a larger process around triaging a ticket and talking to a customer and then recording an action. All of the stuff in between those actions like triage the ticket or write the email or contact the customer, whatever it is, when it's the in between glue, the stuff that passes the data, make that deterministic. In other words, make it as hardwired as you can because you want the agent to do the things it's really good at where it's actually composing the email in a tone that works for you and it's doing all of the wonderful things that also do. You don't want it to try to remember the whole process end to end and pretend it will follow that. You know what that's like? It's like ripping up your railroad and sticking your train on the ground and saying kind of go that way and you hope it's going to work. Don't take your rails out. Leave your rails in and let the agent do what it's good at. Agents are extremely good at text processing. Agents are actually really good at tool calling now. Agents can compose very very sharp solutions to difficult problems. But if you want an agent to follow a process the same way every time, you should be hardwiring those triggers. The agent should get the same exact trigger at the same exact time every time a ticket is open, for instance. That's how you build dependable working software. And I see a lot of people confusing this and they're like, "Well, it's a complicated process, so I'm just going to stick it all in a skill file and I'm going to I'm sure the agent will figure it out." No, it won't. Not predictably, not dependably, and I don't want to roll the dice with my customers. I hope you don't either. Please, please, please do not mistake the wonderful ability of an agent to call tools and skills with the ability to follow a workflow. Those are not the same things and we should stop thinking they are. Look, I talk to a lot of leaders. The pattern I see is fairly consistent. The first month of an agentic deployment, if you're not careful, it all feels really good. It's the second and third month that things start to get scary because then you start to look underneath and you say, "Oh, okay. Wait, we didn't actually hardwire in this process." and a lot of things are slipping through the cracks that the agent is saying it's going well, it's going great and and and we just believed it initially. You you you got to stop letting agents tell you whether they're doing a good job or not. You got to actually evaluate them. You got to actually hardwire in that process wherever you can. So, we've talked about CRM, we've talked about data, we've talked about tools and workflows and the difference between them. Now, we're going to talk about the org redesign that you're going to have to face if you take agents seriously. Because what people don't tell you, like the the story that went viral, and it's a real one about how OpenClaw scaled their number of creatives from 20 to 20,000. That sounds amazing if you're in the ad creative business. The problem is you just earned yourself a huge problem on the human side to review all that creative and figure out what you're going to do with it. So often we look at these tools as generative and we put like 10% of the thought into making these tools evaluative into making these tools critical thinkers and you can there are absolutely companies out there who are prioritizing I want my LLM to review the PRs that are sent to my GitHub repo. I want my LLM to think about how it can autofix bugs that are reported and autosubmit tickets that I can then review. and they're thinking as much about how the LLM is useful in evaluating quality as they are thinking about how the LLM could generate. We need to do more of that thinking. We cannot just sit there and hope that if we generate a bunch of stuff with our agent because it looks good on day one, it's not going to make ourselves really miserable on day 30 and day 60 when we have to evaluate it with the same size org. And the org redesign needs to reflect that reality. We need to be thinking in our org design about how people are going to move to be managers. I can't even say they're going to be moved to be like reviewers anymore. Like increasingly we need to think about getting ourselves abstracted out as much as we can of the agentic processes that are running because otherwise scale break points are going to pop up and you're going to see agents piling up work on a human's plate stressing out the human. The whole process slows down. you lose a lot of the benefits of all the tokens you're burning, etc. As much as we can, we need to be thinking about it like there is a high-speed rail in the middle of a highway where the humans are driving on the highway and nobody touches the high-speed rail where the trains go back and forth and back and forth. That's kind of like the agent layer in enterprise right now. The more we architect it as if it needs its own dedicated high-spe speed rail and we are endto end thinking about the value it produces so that it's from inception to the end of the workflow it's agentic and laid out and clean and structured and evaluated and we know it works. That is what we're looking to do because if you start to mix if you want to move the train to run it on the highway you're going to have car accidents. It's going to be a problem. And increasingly what that means is the work that we do as humans is moving from we're going to be uh transporting goods in our analogy now well now the train does that right instead we're going to be focused on the beginning and the end the handoff points the way we design the system constructing that railroad all of that stuff that is an analogy in our transport networks that really works pretty well for tech right now like we're building the agentic pipeline we're clustering around the handoff points where data goes in and where data comes out this is what the future future of jobs looks like. And I think so often we have the mini me fallacy. We sit there and we think, well, these agents are good. My mini openclaw can do what my mini me does and it's going to be great. And we never think about the org design. Your open claw should not be a mini me. Your open claw, your agents that you take seriously should actually be something at the heart of the business that is configured for them first and you're just there to make sure that you are able to bring the judgment and the overall direction that you need to bring. And that is increasingly something you need to expect down the chain from individual contributors. And it's changing what we think individual contributors do. They're now managers of agents. And that is a skill set that we need to train into people. Look, so much of the open claw story has been about security, right? I've talked about it. The fact that there are many vulnerabilities. In fact, it's such a big deal that folks like Jensen have spent a lot of time and unveiled entire tech stacks that are designed specifically to address that. safe. Open claw is now an entire category of software. The problem is deeper though. The problem is this. The reason why openclaw is unsafe is not necessarily a technical one. It's a people reason. It is because people are so hyped up on open claw and the promise of agents that they're moving really fast and they're skipping all of these foundations. They're just saying, "No, no, no, no. I'm good." And they're just moving on. Don't do that. Don't skip the foundational work. Eat your vegetables. Please, please, please take the idea that you need to have clean data seriously. That's the whole premise behind this open brain project. Take the idea that you need to have mapped out workflows seriously. That really matters. Take the idea that you need to have clarity of intent and evaluations and you need to think about these tools not just as generative but as evaluative seriously. If you don't, you are going to end up with something that is worth a cake and a party on day one and like you're going to be tearing your hair out on day 30 because it's not what you thought it was. And there are real stories. I told you some of those stories in this video. Real stories of people who spent real money on tokens, who celebrated success, who thought they launched something good, and then just like that telephone call story, the the LLM handled all the inbound calls. the open call seemed to be doing good and now they don't know where all the data was and like it's all mixed up and the data structures were never there in the first place. You got to take the rest of the stack seriously if you want agents to do good for you over the long term. Agents are not a magic wand that you can wave and fix everything. They are an incredibly powerful tool that you have to set up to use properly. So what are my commandments for OpenClaw here? Number one, if you're going to put agents into your enterprise, if you're going to try and openclaw your enterprise, audit before you automate. Commandment number one, map the actual process. Not the idealized one, the one with all the edge cases, the one with the tribal knowledge, the one with the undocumented exception handling, all the things that are in your head. Map that. That's the first thing you do. Audit before you automate. Commandment number two, fix the data before you give an agent access to it. Establish a source of truth. Define your schemas. Build your validation. Decide which system wins when there are two sources of truth that disagree. This is super boring work. It's also very essential if you want it to work well. So, audit before you automate. Fix the data. Redesign your org for the throughput that you're about to get. If the agent is going to 10x your production capacity, plan your whole org around that. Do not assume the org will magically adjust. It won't. You have to think about job roles, where people sit, what they do, what tools they need access to. I can't tell you how many times people have been excited about OpenClaw and agents and then they find the IT department wasn't told about all the excitement and the hype and they have a bunch of restrictions on their computers and they can't even use the fancy new software they got. Please, please, please think about your or its provisioning and it's and what people do before you try and just strap on a rocket ship and go. You got to think it through. So, audit, fix the data, think about your org structure, redesign as you need to. And number four, build observability from day one. Observability is not an afterthought. If you want to know if your agents are doing the scary stuff, you got to be observing them in production. You've got to actually look and see what did the agent do? What is the audit? What is the stack trace? How do you know that the agent was able to do task X or task Y and successfully get it done? Do not rely on agent self-reporting. Instead, have an independent perspective, preferably automated, that tells you if the agent got the job done correctly or not. If you don't have that, you are just rolling the dice with agents in production. Number five, so we did build observability, we did redesign the org, we did fix the data and we did audit before you automate. All of those are great. Last one, last command. We only have five commandments here. Scope authority deliberately. Decide what the agent can do and cannot do. Make sure it's very clear. Make sure it's guardrailed. And do not give the agent free access to everything. That is one of the core sources of insecurity in a lot of open cloud deployments is that people just say, "Oh yeah, I can do anything. Dangerously skip permissions. Off you go." No, don't do that. That may make it faster on day one. It does not make your life better on day 30 or even possibly day two. Look, I'm not against speed. If you're on here and you see my channel, you know I love how fast AI is making us go. I adore it. But do not get fooled by the possibility of going fast and think you can skip these thinking steps. You can't. The people who are going to go sustainably fast over a long period of time in the age of AI are people who take the formation of good intention and good structures that surround agents extremely seriously. They're the ones that are not just going to go fast on day one. They're going to go fast on day 60 and 90 and 120. They're the ones that have a system that enables sustained speed over time. And that's what I'm interested in building. I'm not interested in something where we can wave our hands and have a party on day one. I want something where we have sustained speed months and years later because we actually built our agents correctly. So listen to the five commandments for OpenClaw and good luck with your agent deployments and please please please do not dangerously skip permissions. Do not tell your agent to build something and not have clear intent. Please, please, please do not give your agent tasks to do that should properly be given to something with defined workflows, deterministic software, and excellent data underneath. Think about what each part of your stack does intentionally and you will be way way better off. I will see you on the other side and good luck with your deployments. I love OpenClaw. I love agents. I just want it done correctly because I want all of us to be able to speed up. Cheers.

---

## Timestamped Segments

**[0:00]** The scary thing about the OpenClaw

**[0:01]** stories is that so many of them are

**[0:02]** real. You can actually build a complete

**[0:06]** $320,000 value SAS replacement suite by

**[0:09]** hooking your OpenClaw up to APIs. Yes,

**[0:11]** and that's true. You can also build a

**[0:14]** complete CRM replacement in just a few

**[0:16]** days with OpenClaw. Also true. Also a

**[0:18]** verified story. Yes, you can scale your

**[0:20]** ad created from 20 to 2,000. Also true.

**[0:22]** Also a verified story. And the point of

**[0:25]** all of that is that you are taking a

**[0:29]** tool that is designed to be a general

**[0:32]** purpose agent and using it to cover over

**[0:35]** a lot of your own existing issues. And

**[0:37]** that's what I want to talk about today.

**[0:39]** Because when we talk about Open Claw,

**[0:41]** what we're talking about is the

**[0:42]** enthusiasm and the energy that comes

**[0:44]** from the world's first widely available

**[0:47]** general purpose agent. And I love all

**[0:49]** that hype. I love that energy. I love

**[0:50]** that you actually can do this stuff with

**[0:52]** OpenClaw. But what I don't love is that

**[0:54]** so many people are taking it as a blank

**[0:58]** slate permission slip and just saying,

**[1:00]** you know what, it doesn't matter. It's

**[1:01]** okay. I don't have to think about my

**[1:02]** data anymore. I don't have to think

**[1:04]** about my best practices anymore. I don't

**[1:06]** have to think about my software anymore.

**[1:07]** OpenClaw will make it better. No, it

**[1:09]** won't. Open Claw will not fix those

**[1:11]** things. Look, I've spent the last couple

**[1:13]** of years arguing that the biggest risk

**[1:15]** that we face in software is not taking

**[1:18]** our entire stack seriously when we bring

**[1:21]** AI into it. If we're going to do a true

**[1:23]** reinvention for AI, we need to actually

**[1:26]** take seriously the idea that AI will

**[1:28]** need to be at the heart of a reinvented

**[1:30]** stack. We cannot just stick an open claw

**[1:33]** agent over the top, paper over all of

**[1:35]** the data issues, and pretend it's going

**[1:37]** to work. It won't. It just won't. Now, I

**[1:40]** want to be precise about what OpenClaw

**[1:42]** actually is because the discourse has

**[1:43]** gotten very muddy with all of the hype

**[1:45]** and the hundreds of thousands of GitHub

**[1:46]** stars and everything else. OpenClaw is

**[1:48]** an open-source self-hosted model

**[1:50]** agnostic AI agent framework. It runs as

**[1:53]** a persistent Damon on your machine. It

**[1:55]** connects to your messaging app, Slack,

**[1:56]** WhatsApp, Telegram, Signal, you name it.

**[1:58]** And it acts on your behalf through shell

**[2:01]** access, browser automation, file

**[2:03]** operations, email, etc. It has a skill

**[2:06]** system that lets the agent extend itself

**[2:08]** into a bunch of communitybuilt

**[2:09]** capabilities and it has a set of memory

**[2:12]** that was originally stored as markdown

**[2:14]** files and is now undergoing some

**[2:15]** changes. The combination of all of those

**[2:18]** things as a modular architecture is new

**[2:22]** and was extremely explosive when it came

**[2:24]** out. We all know that. I've told that

**[2:26]** story. The problem is we are now a few

**[2:28]** months into the open claw story and what

**[2:31]** we're finding is that the story gets

**[2:34]** more complicated as you try and use your

**[2:36]** open claw agent to paper over

**[2:39]** inefficiencies and weaknesses in your

**[2:40]** stack. And that's what I want to warn

**[2:42]** you about because you can absolutely do

**[2:45]** incredible things with openclaw 100%.

**[2:49]** But you have to make sure that you are

**[2:51]** building the layers of your software

**[2:52]** stack so that you can do that correctly.

**[2:54]** I think the simplest way to tell this

**[2:55]** story is to talk about real builds that

**[2:57]** we've had with OpenClaw and the risks

**[2:59]** that you have in that OpenClaw

**[3:00]** architecture if you don't take care of

**[3:02]** the rest of the stack. So build number

**[3:04]** one, I talked about the CRM. It's a real

**[3:06]** story. It was a real non-coder who was

**[3:08]** able to build a real CRM using OpenClaw.

**[3:11]** That is both a tremendous

**[3:13]** accomplishment, a mark of how far agents

**[3:15]** have come and also something that is

**[3:17]** absolutely terrifying if you understand

**[3:19]** how CRM are built. Not because we want

**[3:21]** to go slow, we want to go really fast

**[3:23]** and there are real speed ups available.

**[3:24]** It's because CRM are fundamentally not

**[3:26]** pieces of software. We think of them as

**[3:28]** pieces of software. And the piece that

**[3:30]** came out, well, you can vibe code this

**[3:32]** in 12 days or whatever it was, it

**[3:33]** painted it as if OpenClaw built software

**[3:36]** that replaced a SAS. But but but that is

**[3:40]** not really what a CRM is. What a CRM is

**[3:43]** is encoded workflow logic that reflects

**[3:46]** the reality of your business in a way

**[3:49]** that makes sense for your sales process

**[3:51]** and for your customer care process. All

**[3:53]** of the things you know about your

**[3:55]** customers and how they buy and how they

**[3:57]** choose to make purchasing decisions and

**[3:58]** how they choose to keep their purchase

**[4:00]** and how they choose to expand and

**[4:01]** upgrade their purchase with you, all of

**[4:03]** that needs to have a place in your CRM.

**[4:06]** And when we talk about people who are

**[4:08]** choosing not to go with Salesforce, who

**[4:10]** are vibe coding their own CRM, and this

**[4:11]** is one of N, right? There's so many.

**[4:14]** What we see when they're at their best

**[4:16]** is that people are moving quickly.

**[4:18]** They're encoding something and they make

**[4:20]** specific decisions about their CRM that

**[4:23]** reflect what they want out of the

**[4:26]** customer relationship, why their

**[4:28]** business model exists the way it is.

**[4:30]** They have that intent, that clarity of

**[4:31]** intent. I talk about clarity of intent a

**[4:33]** lot for a reason. They have that intent

**[4:36]** across their data structures and across

**[4:38]** their workflows. And all their agent

**[4:40]** does, all their open claw does is it

**[4:42]** helps them instantiate that intent.

**[4:43]** That's all. That's it. If you have any

**[4:47]** lack of clarity in your intent. If you

**[4:49]** just point your open claw at a CRM, say,

**[4:50]** "I want to build a CRM. Please just vibe

**[4:52]** code be one." You will get trash. You

**[4:55]** will get absolute trash. Not because

**[4:57]** it's not functioning software, not

**[4:59]** because your agent can't call it, but

**[5:00]** because what is built is going to

**[5:02]** reflect generic middle-of the road a

**[5:04]** workflow that works for everybody out of

**[5:06]** the box and therefore for nobody. And

**[5:08]** you're not going to get something that

**[5:10]** actually harnesses the power of custom

**[5:12]** software, which is the whole reason you

**[5:14]** use agents in the first place. And so

**[5:16]** what I am begging you to do when you

**[5:18]** think about the promise of agentically

**[5:20]** developed software, and it is promise,

**[5:22]** and it's real, is take the high road

**[5:25]** here. There are two ways to build a

**[5:26]** Gentic software quickly. Both are fast.

**[5:28]** You're not trading speed. Number one,

**[5:31]** have clarity of intent around the

**[5:33]** workflows you are trying to encode and

**[5:35]** perhaps why they are different in the

**[5:36]** age of AI. Perhaps why your customer

**[5:39]** relationship is changing. Certainly, you

**[5:41]** should have a set of requirements that

**[5:43]** reflect what actually works on the

**[5:45]** ground in your business that's very

**[5:46]** clear, that's unique, that's different

**[5:48]** from other businesses. Otherwise, you

**[5:49]** would just buy the software, right? Then

**[5:52]** go ahead and build quickly with agents.

**[5:54]** The alternative is when you jump

**[5:56]** straight to building because that's the

**[5:58]** seductive part. That's the easy part and

**[6:00]** you don't take the time to get clear on

**[6:02]** your intent. Then you're in trouble

**[6:03]** because what you're going to get is

**[6:04]** generic average. It is whatever the

**[6:07]** average idea the LLM has of the software

**[6:09]** will be. And that's true whether you're

**[6:10]** using OpenClaw or agents uh of any kind.

**[6:14]** So that's lesson number one. It's about

**[6:16]** CRM, it's about software, it's about

**[6:17]** SAS. Lesson number two in these openclaw

**[6:20]** agent deployments that we're starting to

**[6:21]** see is that you got to get your

**[6:22]** underlying data clean. This is part of

**[6:24]** the reason I put open brain together. I

**[6:26]** wanted people to have a clean data

**[6:28]** layer. It's I don't care if it's open

**[6:30]** brain or if it's something else for you.

**[6:31]** What I worry about is that you need to

**[6:33]** use your agent on day 30, day 300 as

**[6:36]** well as you use it on day one. And if

**[6:38]** you have a dirty memory system, a memory

**[6:41]** system that is not organized, you're

**[6:43]** going to be in trouble. And why are you

**[6:45]** going to be in trouble? You're going to

**[6:46]** be in trouble because Open Claw and

**[6:49]** other agents are not by default data

**[6:51]** organizers unless you tell them to be.

**[6:53]** Unless you give them guard rails,

**[6:55]** explicit constraints that require them

**[6:58]** to respect your data schemas and keep

**[6:59]** data clean, they won't. And so you need

**[7:02]** to start to think about the world as if

**[7:04]** it is a data-shaped problem that agents

**[7:07]** can help you accelerate, but the agents

**[7:09]** themselves are going to be messy, messy

**[7:12]** data engineers unless you structure them

**[7:14]** appropriately. There is a story

**[7:15]** circulating about a team that spent

**[7:18]** $14,000

**[7:19]** building a voice agent to handle lots of

**[7:21]** inbound calls. On paper, it seemed to

**[7:23]** work, but when you looked under the

**[7:25]** surface at the data the agent was

**[7:26]** handling, no one had specified how the

**[7:29]** schema was going to work. They found

**[7:30]** records all over the place. They had no

**[7:32]** good way to measure inbound and funnel,

**[7:34]** and it was just a complete mess, even

**[7:35]** though it was up and functioning and

**[7:37]** apparently took calls. So, take the time

**[7:41]** to get the schema right. Do not be

**[7:43]** satisfied with your open claw just

**[7:45]** because you can query it in a Slack

**[7:46]** message or a text message and it says

**[7:48]** something back. When I talk about

**[7:50]** legibility of surfaces as a key

**[7:54]** criterion for AI agents, this is what I

**[7:56]** mean. If if you just send a text message

**[7:58]** and it's like a void and you don't know

**[8:00]** what happens and then an answer comes

**[8:01]** back and you like the answer, you do not

**[8:04]** have an agent. You have a problem

**[8:05]** masquerading as a helpful answer. You

**[8:08]** really do because how do you know if it

**[8:10]** recorded it correctly? How do you know

**[8:11]** if it wrote it down anywhere? Unless you

**[8:13]** understand that stack, unless a company

**[8:14]** deliberately makes it clear and says,

**[8:16]** "We're going to be transparent. This is

**[8:17]** where your data lives. this is where

**[8:18]** it's going to be. This is how we update

**[8:19]** it. These are our guardrails. You're in

**[8:21]** trouble. And so, please, please, please,

**[8:24]** if you are building with agents,

**[8:26]** recognize that you don't want to be in

**[8:28]** the position of spending money, spending

**[8:30]** tokens on building something that looks

**[8:32]** good in a text message, but the data

**[8:33]** underneath is dirty. So, we've talked

**[8:34]** about CRM, we've talked about data

**[8:36]** clarity. You know what the next thing we

**[8:37]** need to talk about is? It is mistaking a

**[8:40]** skill for a process. I love skills.

**[8:43]** Skills are great. I've talked about how

**[8:44]** important they are. I think they're

**[8:45]** critical. Do not mistake a skill or a

**[8:48]** tool call for a process. If you have a

**[8:52]** business workflow, it should be as much

**[8:55]** as you can hardwired in. You should not

**[8:58]** be trying to take your business workflow

**[9:00]** and tell yourself it's going to work

**[9:02]** good and stick it as a skill in OpenClaw

**[9:04]** and hope it works that way for

**[9:05]** production grade data every single time.

**[9:07]** Instead, your agent should be operating

**[9:10]** across hardwired process and speeding

**[9:13]** that along. And you should be able to

**[9:15]** evaluate the success of that agent

**[9:17]** across that process. And what do I mean

**[9:20]** by that? What does that look like in

**[9:21]** practice? Let's say one of the skills

**[9:23]** your agent has is send an email. But

**[9:25]** that exists inside a larger process,

**[9:26]** right? It exists inside a larger process

**[9:28]** around triaging a ticket and talking to

**[9:30]** a customer and then recording an action.

**[9:31]** All of the stuff in between those

**[9:33]** actions like triage the ticket or write

**[9:35]** the email or contact the customer,

**[9:37]** whatever it is, when it's the in between

**[9:39]** glue, the stuff that passes the data,

**[9:41]** make that deterministic. In other words,

**[9:43]** make it as hardwired as you can because

**[9:45]** you want the agent to do the things it's

**[9:47]** really good at where it's actually

**[9:50]** composing the email in a tone that works

**[9:51]** for you and it's doing all of the

**[9:53]** wonderful things that also do. You don't

**[9:55]** want it to try to remember the whole

**[9:57]** process end to end and pretend it will

**[10:00]** follow that. You know what that's like?

**[10:01]** It's like ripping up your railroad and

**[10:03]** sticking your train on the ground and

**[10:05]** saying kind of go that way and you hope

**[10:07]** it's going to work. Don't take your

**[10:08]** rails out. Leave your rails in and let

**[10:10]** the agent do what it's good at. Agents

**[10:12]** are extremely good at text processing.

**[10:14]** Agents are actually really good at tool

**[10:15]** calling now. Agents can compose very

**[10:19]** very sharp solutions to difficult

**[10:21]** problems. But if you want an agent to

**[10:24]** follow a process the same way every

**[10:26]** time, you should be hardwiring those

**[10:28]** triggers. The agent should get the same

**[10:30]** exact trigger at the same exact time

**[10:32]** every time a ticket is open, for

**[10:33]** instance. That's how you build

**[10:35]** dependable working software. And I see a

**[10:37]** lot of people confusing this and they're

**[10:38]** like, "Well, it's a complicated process,

**[10:41]** so I'm just going to stick it all in a

**[10:42]** skill file and I'm going to I'm sure the

**[10:44]** agent will figure it out." No, it won't.

**[10:46]** Not predictably, not dependably, and I

**[10:48]** don't want to roll the dice with my

**[10:49]** customers. I hope you don't either.

**[10:51]** Please, please, please do not mistake

**[10:54]** the wonderful ability of an agent to

**[10:56]** call tools and skills with the ability

**[10:58]** to follow a workflow. Those are not the

**[11:00]** same things and we should stop thinking

**[11:02]** they are. Look, I talk to a lot of

**[11:04]** leaders. The pattern I see is fairly

**[11:06]** consistent. The first month of an

**[11:08]** agentic deployment, if you're not

**[11:09]** careful, it all feels really good. It's

**[11:12]** the second and third month that things

**[11:14]** start to get scary because then you

**[11:16]** start to look underneath and you say,

**[11:17]** "Oh, okay. Wait, we didn't actually

**[11:19]** hardwire in this process." and a lot of

**[11:21]** things are slipping through the cracks

**[11:22]** that the agent is saying it's going

**[11:24]** well, it's going great and and and we

**[11:26]** just believed it initially. You you you

**[11:28]** got to stop letting agents tell you

**[11:29]** whether they're doing a good job or not.

**[11:30]** You got to actually evaluate them. You

**[11:32]** got to actually hardwire in that process

**[11:33]** wherever you can. So, we've talked about

**[11:34]** CRM, we've talked about data, we've

**[11:36]** talked about tools and workflows and the

**[11:38]** difference between them. Now, we're

**[11:39]** going to talk about the org redesign

**[11:41]** that you're going to have to face if you

**[11:43]** take agents seriously. Because what

**[11:45]** people don't tell you, like the the

**[11:46]** story that went viral, and it's a real

**[11:48]** one about how OpenClaw scaled their

**[11:49]** number of creatives from 20 to 20,000.

**[11:52]** That sounds amazing if you're in the ad

**[11:53]** creative business. The problem is you

**[11:56]** just earned yourself a huge problem on

**[11:59]** the human side to review all that

**[12:00]** creative and figure out what you're

**[12:01]** going to do with it. So often we look at

**[12:03]** these tools as generative and we put

**[12:06]** like 10% of the thought into making

**[12:08]** these tools evaluative into making these

**[12:11]** tools critical thinkers and you can

**[12:15]** there are absolutely companies out there

**[12:17]** who are prioritizing I want my LLM to

**[12:21]** review the PRs that are sent to my

**[12:23]** GitHub repo. I want my LLM to think

**[12:25]** about how it can autofix bugs that are

**[12:27]** reported and autosubmit tickets that I

**[12:29]** can then review. and they're thinking as

**[12:31]** much about how the LLM is useful in

**[12:33]** evaluating quality as they are thinking

**[12:36]** about how the LLM could generate. We

**[12:38]** need to do more of that thinking. We

**[12:40]** cannot just sit there and hope that if

**[12:43]** we generate a bunch of stuff with our

**[12:45]** agent because it looks good on day one,

**[12:46]** it's not going to make ourselves really

**[12:48]** miserable on day 30 and day 60 when we

**[12:50]** have to evaluate it with the same size

**[12:52]** org. And the org redesign needs to

**[12:55]** reflect that reality. We need to be

**[12:56]** thinking in our org design about how

**[13:00]** people are going to move to be managers.

**[13:04]** I can't even say they're going to be

**[13:05]** moved to be like reviewers anymore. Like

**[13:07]** increasingly we need to think about

**[13:09]** getting ourselves abstracted out as much

**[13:11]** as we can of the agentic processes that

**[13:14]** are running because otherwise scale

**[13:16]** break points are going to pop up and

**[13:18]** you're going to see agents piling up

**[13:20]** work on a human's plate stressing out

**[13:22]** the human. The whole process slows down.

**[13:23]** you lose a lot of the benefits of all

**[13:24]** the tokens you're burning, etc. As much

**[13:26]** as we can, we need to be thinking about

**[13:28]** it like there is a high-speed rail in

**[13:31]** the middle of a highway where the humans

**[13:32]** are driving on the highway and nobody

**[13:34]** touches the high-speed rail where the

**[13:35]** trains go back and forth and back and

**[13:37]** forth. That's kind of like the agent

**[13:39]** layer in enterprise right now. The more

**[13:41]** we architect it as if it needs its own

**[13:42]** dedicated high-spe speed rail and we are

**[13:44]** endto end thinking about the value it

**[13:47]** produces so that it's from inception to

**[13:49]** the end of the workflow it's agentic and

**[13:52]** laid out and clean and structured and

**[13:54]** evaluated and we know it works. That is

**[13:57]** what we're looking to do because if you

**[13:59]** start to mix if you want to move the

**[14:00]** train to run it on the highway you're

**[14:02]** going to have car accidents. It's going

**[14:04]** to be a problem. And increasingly what

**[14:06]** that means is the work that we do as

**[14:09]** humans is moving from we're going to be

**[14:11]** uh transporting goods in our analogy now

**[14:13]** well now the train does that right

**[14:15]** instead we're going to be focused on the

**[14:17]** beginning and the end the handoff points

**[14:19]** the way we design the system

**[14:20]** constructing that railroad all of that

**[14:23]** stuff that is an analogy in our

**[14:25]** transport networks that really works

**[14:27]** pretty well for tech right now like

**[14:28]** we're building the agentic pipeline

**[14:30]** we're clustering around the handoff

**[14:31]** points where data goes in and where data

**[14:33]** comes out this is what the future future

**[14:35]** of jobs looks like. And I think so often

**[14:38]** we have the mini me fallacy. We sit

**[14:39]** there and we think, well, these agents

**[14:41]** are good. My mini openclaw can do what

**[14:42]** my mini me does and it's going to be

**[14:44]** great. And we never think about the org

**[14:46]** design. Your open claw should not be a

**[14:48]** mini me. Your open claw, your agents

**[14:50]** that you take seriously should actually

**[14:52]** be something at the heart of the

**[14:53]** business that is configured for them

**[14:54]** first and you're just there to make sure

**[14:57]** that you are able to bring the judgment

**[14:58]** and the overall direction that you need

**[15:00]** to bring. And that is increasingly

**[15:02]** something you need to expect down the

**[15:04]** chain from individual contributors. And

**[15:06]** it's changing what we think individual

**[15:08]** contributors do. They're now managers of

**[15:10]** agents. And that is a skill set that we

**[15:12]** need to train into people. Look, so much

**[15:15]** of the open claw story has been about

**[15:17]** security, right? I've talked about it.

**[15:19]** The fact that there are many

**[15:20]** vulnerabilities. In fact, it's such a

**[15:22]** big deal that folks like Jensen have

**[15:24]** spent a lot of time and unveiled entire

**[15:26]** tech stacks that are designed

**[15:27]** specifically to address that. safe. Open

**[15:30]** claw is now an entire category of

**[15:31]** software. The problem is deeper though.

**[15:34]** The problem is this. The reason why

**[15:37]** openclaw is unsafe is not necessarily a

**[15:40]** technical one. It's a people reason. It

**[15:43]** is because people are so hyped up on

**[15:46]** open claw and the promise of agents that

**[15:48]** they're moving really fast and they're

**[15:50]** skipping all of these foundations.

**[15:52]** They're just saying, "No, no, no, no.

**[15:54]** I'm good." And they're just moving on.

**[15:57]** Don't do that. Don't skip the

**[15:59]** foundational work. Eat your vegetables.

**[16:01]** Please, please, please take the idea

**[16:03]** that you need to have clean data

**[16:05]** seriously. That's the whole premise

**[16:06]** behind this open brain project. Take the

**[16:08]** idea that you need to have mapped out

**[16:11]** workflows seriously. That really

**[16:14]** matters. Take the idea that you need to

**[16:16]** have clarity of intent and evaluations

**[16:18]** and you need to think about these tools

**[16:20]** not just as generative but as evaluative

**[16:22]** seriously. If you don't, you are going

**[16:25]** to end up with something that is worth a

**[16:28]** cake and a party on day one and like

**[16:30]** you're going to be tearing your hair out

**[16:31]** on day 30 because it's not what you

**[16:33]** thought it was. And there are real

**[16:34]** stories. I told you some of those

**[16:35]** stories in this video. Real stories of

**[16:37]** people who spent real money on tokens,

**[16:39]** who celebrated success, who thought they

**[16:41]** launched something good, and then just

**[16:43]** like that telephone call story, the the

**[16:46]** LLM handled all the inbound calls. the

**[16:48]** open call seemed to be doing good and

**[16:49]** now they don't know where all the data

**[16:50]** was and like it's all mixed up and the

**[16:52]** data structures were never there in the

**[16:53]** first place. You got to take the rest of

**[16:56]** the stack seriously if you want agents

**[16:58]** to do good for you over the long term.

**[17:00]** Agents are not a magic wand that you can

**[17:03]** wave and fix everything. They are an

**[17:05]** incredibly powerful tool that you have

**[17:07]** to set up to use properly. So what are

**[17:09]** my commandments for OpenClaw here?

**[17:11]** Number one, if you're going to put

**[17:12]** agents into your enterprise, if you're

**[17:13]** going to try and openclaw your

**[17:14]** enterprise, audit before you automate.

**[17:17]** Commandment number one, map the actual

**[17:18]** process. Not the idealized one, the one

**[17:21]** with all the edge cases, the one with

**[17:22]** the tribal knowledge, the one with the

**[17:24]** undocumented exception handling, all the

**[17:25]** things that are in your head. Map that.

**[17:28]** That's the first thing you do. Audit

**[17:29]** before you automate. Commandment number

**[17:31]** two, fix the data before you give an

**[17:35]** agent access to it. Establish a source

**[17:37]** of truth. Define your schemas. Build

**[17:39]** your validation. Decide which system

**[17:42]** wins when there are two sources of truth

**[17:44]** that disagree. This is super boring

**[17:45]** work. It's also very essential if you

**[17:47]** want it to work well. So, audit before

**[17:50]** you automate. Fix the data. Redesign

**[17:52]** your org for the throughput that you're

**[17:54]** about to get. If the agent is going to

**[17:56]** 10x your production capacity, plan your

**[17:58]** whole org around that. Do not assume the

**[18:00]** org will magically adjust. It won't. You

**[18:03]** have to think about job roles, where

**[18:04]** people sit, what they do, what tools

**[18:06]** they need access to. I can't tell you

**[18:08]** how many times people have been excited

**[18:10]** about OpenClaw and agents and then they

**[18:12]** find the IT department wasn't told about

**[18:15]** all the excitement and the hype and they

**[18:16]** have a bunch of restrictions on their

**[18:17]** computers and they can't even use the

**[18:19]** fancy new software they got. Please,

**[18:21]** please, please think about your or its

**[18:23]** provisioning and it's and what people do

**[18:25]** before you try and just strap on a

**[18:28]** rocket ship and go. You got to think it

**[18:30]** through. So, audit, fix the data, think

**[18:32]** about your org structure, redesign as

**[18:34]** you need to. And number four, build

**[18:37]** observability from day one.

**[18:38]** Observability is not an afterthought. If

**[18:40]** you want to know if your agents are

**[18:42]** doing the scary stuff, you got to be

**[18:43]** observing them in production. You've got

**[18:45]** to actually look and see what did the

**[18:46]** agent do? What is the audit? What is the

**[18:48]** stack trace? How do you know that the

**[18:50]** agent was able to do task X or task Y

**[18:53]** and successfully get it done? Do not

**[18:55]** rely on agent self-reporting. Instead,

**[18:58]** have an independent perspective,

**[19:00]** preferably automated, that tells you if

**[19:01]** the agent got the job done correctly or

**[19:03]** not. If you don't have that, you are

**[19:05]** just rolling the dice with agents in

**[19:06]** production. Number five, so we did build

**[19:08]** observability, we did redesign the org,

**[19:11]** we did fix the data and we did audit

**[19:13]** before you automate. All of those are

**[19:15]** great. Last one, last command. We only

**[19:17]** have five commandments here. Scope

**[19:19]** authority deliberately. Decide what the

**[19:21]** agent can do and cannot do. Make sure

**[19:23]** it's very clear. Make sure it's

**[19:25]** guardrailed. And do not give the agent

**[19:27]** free access to everything. That is one

**[19:29]** of the core sources of insecurity in a

**[19:31]** lot of open cloud deployments is that

**[19:33]** people just say, "Oh yeah, I can do

**[19:34]** anything. Dangerously skip permissions.

**[19:35]** Off you go." No, don't do that. That may

**[19:38]** make it faster on day one. It does not

**[19:39]** make your life better on day 30 or even

**[19:41]** possibly day two. Look, I'm not against

**[19:44]** speed. If you're on here and you see my

**[19:46]** channel, you know I love how fast AI is

**[19:49]** making us go. I adore it. But do not get

**[19:52]** fooled by the possibility of going fast

**[19:55]** and think you can skip these thinking

**[19:57]** steps. You can't. The people who are

**[20:00]** going to go sustainably fast over a long

**[20:02]** period of time in the age of AI are

**[20:04]** people who take the formation of good

**[20:07]** intention and good structures that

**[20:09]** surround agents extremely seriously.

**[20:12]** They're the ones that are not just going

**[20:14]** to go fast on day one. They're going to

**[20:15]** go fast on day 60 and 90 and 120.

**[20:17]** They're the ones that have a system that

**[20:19]** enables sustained speed over time. And

**[20:21]** that's what I'm interested in building.

**[20:23]** I'm not interested in something where we

**[20:25]** can wave our hands and have a party on

**[20:26]** day one. I want something where we have

**[20:28]** sustained speed months and years later

**[20:30]** because we actually built our agents

**[20:32]** correctly. So listen to the five

**[20:34]** commandments for OpenClaw and good luck

**[20:37]** with your agent deployments and please

**[20:39]** please please do not dangerously skip

**[20:42]** permissions. Do not tell your agent to

**[20:44]** build something and not have clear

**[20:45]** intent. Please, please, please do not

**[20:48]** give your agent tasks to do that should

**[20:51]** properly be given to something with

**[20:54]** defined workflows, deterministic

**[20:56]** software, and excellent data underneath.

**[20:58]** Think about what each part of your stack

**[21:01]** does intentionally and you will be way

**[21:03]** way better off. I will see you on the

**[21:04]** other side and good luck with your

**[21:06]** deployments. I love OpenClaw. I love

**[21:08]** agents. I just want it done correctly

**[21:10]** because I want all of us to be able to

**[21:12]** speed up. Cheers.
