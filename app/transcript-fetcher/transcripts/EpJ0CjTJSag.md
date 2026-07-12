# Transcript: Anthropic And OpenAI Just Admitted The Model Isn't Enough.

**URL:** https://www.youtube.com/watch?v=EpJ0CjTJSag
**Segments:** 606
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 20:48
**Uploaded:** 2026-05-10

---

## Full Text

$20, 2 hours, to get full read and write access to the AI platform that 70% of McKinsey's 40,000 consultants use every single day. This was an autonomous agent that spent 20 bucks with no credentials and zero insider help to get access to tens of millions of chat messages, access to tens of thousands of user accounts, and every system prompt governing how the platform reasons. All of them writable access, not just readable, writable. In other words, an attacker could have silently rewritten how the AI advises consultants who advise the largest firms in the world. The platform, it's called Lily. The startup that broke the news is called Code Wall, and the date was February 28th. Because it's taken the industry a couple of months to figure out what this agentic pattern looks like, what the lessons learned are, and how we change the way we purchase, invest, and build in software in response. And that's what I want to talk about today. First, this exploit wasn't exotic. It was SQL injection. The first documented case of SQL injection is in 1998. It's taught in every introductory web security course. And McKinsey, they have a great engineering team. Lily had been in production for more than 2 years. So, how did this happen? The answer has implications for your AI roadmap, for the platform that you signed up for last quarter. Most companies have a platform they signed up for last quarter. We have a lot of AI purchasing going on right now. And of course, for the deal that you're probably considering. Because again, most companies at most scales are considering an AI purchase this quarter. Three things to cover in this video. One, why calling Lily a security failure misses the point. Two, the procurement sequence most companies still use and why agents are breaking it now. And three, two questions you can ask this week that will tell you whether your AI investment is actual strategy or just an unpriced liability. I'm putting a further six-question checklist for your technical team on Substack, because that's part of the answer to how we avoid situations like the Lily story. So, first, here's what most of the analysis did with the Lily story. Code Wall disclosed responsibly on March 9th. They did not use this maliciously. McKinsey patched it up within hours, credit to them. The postmortem said what postmortems typically say. You should authenticate your endpoints, you should sanitize your inputs, treat your AI platform like production. That's not wrong, it's correct, it's true, but it's not the story. If you stop there, you walk away thinking the lesson is a story of technical hygiene, but it's not. The technical hygiene was never the issue here. McKinsey has many, many great engineers who know how to authenticate an endpoint. That defense is trivial to implement at this point. There's no organization on Earth where this is a hard engineering problem. So, let's run the pattern backward and let's ask ourselves deeper questions. 22 of 200 endpoints shipped with no authentication. 22 of them. At that scale, that's not a random mistake. That's that's a pattern. That's a platform where maybe the default or maybe the assumption is that you can push to prod without that level of scrutiny on your endpoint. Because just to be clear, for those of you not familiar with APIs, this is not they forgot to lock the door. That framing puts the failure on a single person, some engineer on some Friday who skipped a checklist. If that's what happened, the fix would be training and it would be easy. But if you have 22 of these, and in particular, if the exploit that happened happened because one of the endpoints allowed production right access without authentication, that's a much deeper engineering culture and structure problem that needs to be fixed, that depends on a deeper knowledge of what agents are capable of today. And let me be clear, this is not they forgot to lock the door. I know that not everyone's familiar with APIs here. It's not that like you should lock the door on the API and it would be fixed, because that framing puts the failure on an individual. Like some engineer, some Friday, someone skipped a checklist. If that's what happened, the fix would be training, but if that's what happened, we would not see 22 of these endpoints in production. I don't believe. I don't think that's what happened. I don't think that's the root cause. I think the root cause is closer to no one asking whether the API endpoint itself was the correct shape for assuming strong agentic access on the web. We need to be assuming that the production software we put into place is going to meet AI agents, and it looks like that consideration did not happen. And if the people who would ask those questions, probably technical people, probably engineers, are not in the room with space to talk, then a lot of the shape of the software we're putting out as AI software is going to be determined by executives and business teams working to a deadline, rather than technical folks who can speak to where this agentic impact is going to show up in business results, which is exactly what happened here. When when Lily first came out 2 years ago, we didn't have autonomous AI agents that could hack through a public endpoint and get to production data. That is something that is very normal in 2026. If we want to build software and purchase software that has lasting value, we need technical voices at the table that can anticipate that kind of trajectory and speak to it in a way that helps us to shape our purchase path. And this is where I have a lot of sympathy for the McKinsey team. I don't believe this is really a McKinsey story per se. I think McKinsey is the version that made the news because the consequences were vivid, the report was good, and frankly the brand is very large. But I've seen the inside of enough enterprise AI programs this year to tell you that the shape of this failure shows up in a lot of places. The shape is that governance and thoughtful technical perspective tend to arrive late, and the exploit just happens to show up in some cases as like a receipt. But knowing the shape of failure by itself isn't the useful part. The useful piece here is understanding the process that keeps producing it, because once you see the process, you can change your pattern and actually update it and do better next time. Here's the process. Most enterprise software has been bought for the last 15 years or more in the same sequence. Strategic decision at the top, procurement negotiates the contract, security and compliance review, IT plans and integration, developers build against whatever platform already got purchased. That sequence works great for SaaS. It worked for Salesforce, Workday, ServiceNow, the entire generation of cloud applications most companies run on today. And worked because SaaS is bounded. The vendor gives you an admin console, a set of integration points, a published API, and a permissions model that maps cleanly to roles. You're configuring software. That's not that much to build, right? For agents, that same sequence leads to disaster. Walk through what an agent actually does on a single real run inside a company in 2026 now. The user says, "Prepare the renewal brief for our largest customer." It's April 2026. The agent has to figure out which systems hold the answer. It pulls from the CRM, from support tickets, from contract management, from product usage data, from call transcripts, from internal wiki. It crosses permission boundaries that for a human are mediated by what's visible on a screen, but for an agent may be mediated by tokens and roles and scopes that have to actually exist as code written by someone. When a human consultant pulls a renewal brief together, none of this complexity that I just described is visible to them. They open Salesforce, they glance at the support history, they check the contract, they scan a Slack thread from last quarter. They don't notice the contract management tool has its own permissions. The support system has its own audit log. The CRM treats their access differently from the analyst's access. They don't notice half the wiki pages they're reading are stale. They don't have to notice. Their eyes do the work. The screen is the permissions model. If they shouldn't see something, the screen doesn't show it. An agent has no eyes. The agent is asking each of those systems in code, "Am I allowed to read this?" And every one of those systems has to have a clear answer. And every one of those has to be auditable. And every one One audits has to compose with every other one when a regulator asks what happened in the sequence. None of this exists by default. All of it is engineering work that someone has to do against a deadline before the agent ships. And that's just for one task. Multiply that by all the workflows your roadmap promises to automate and you see the shape of what we're committing to as a community. The SAS environment that we've described for procurement was a very bounded place. I just described how clean it is to grab software, install it, and then maybe you build a few integrations. What I'm describing with cross-workflow integrations is not that. It's extremely unbounded and we are signing up for that. And that is part of why this is so complex and why the procurement process is breaking. With agents, the implementation question isn't downstream of a strategic decision. It's effectively the strategic decision itself. If the agent can't authenticate against the system it needs, the strategy isn't going to work. If the permissions model only thinks about humans clicking through screens, the strategy doesn't work >> either. If If every run reassembles the same business context from scratch and your token bill goes up by 3x, the strategy doesn't work. If you can't audit what the agent did, the strategy is not going to get past legal and shouldn't. None of these are implementation details to be worked out later. Every one of them is enough to change how the roadmap actually is shaped. So, when you put implementation and your dev team last in the buying sequence, you're committing capital to a strategy whose viability has not been tested. And you don't find that out with a demo. You find it out 6 months in when your team is trying to push the workflow into production and discovering one boundary at a time that the platform you purchased wasn't buildable for the work you bought it to do. The vendors know this now. That's what this week has made clear and that closes the circle on the February conversation and what happened with Code Wallet Lilly. Because in the last week or so, Anthropic and OpenAI have both stood up enterprise services companies with billions of dollars behind them to put engineers inside customer build rooms for this exact complexity. SAP acquired Dreamio and Prior Labs to bring a unified data layer and tabular foundation models to the place where actual business data lives, the ledgers of the business, right? Not marketing copy. Pinecone launched Nexus, which is essentially stop making your agent rebuild the business from scratch every time it runs. Salesforce shipped headless 360, which exposes their platform as APIs and tools and command line commands because agents don't click through screens. ServiceNow opened up action fabric so outside agents can trigger governed workflows, playbooks, approvals, catalogs through a controlled surface with identity and audit attached. You see how this ties in, right? Six different announcements all within the last week or so, one story. Every single one of those vendors is now selling you the thing your AI roadmap was supposed to already have, reachable surfaces, governed action, permission aware data, cheaper context assembly, forward deployed humans who can actually wire up your workflows. I'm not saying that this is a silver bullet, but I'm saying it's a signal. The signal is that the model was never the hard part. The hard part is exactly what the Lilly incident surfaced, whether the agent can reach the right data, use the right permissions, trigger the right workflow, leave the right audit trail, and do all of it at a cost the company can live with. So, the question isn't which vendor you pick from that list. I'm not asking about that. The question is how do you know before you sign with a vendor whether any of what they are promising is going to deliver actual value. You might be wondering, why are we talking about an external hack of Lilly, which was a system that McKinsey stood up on its own, and the rest of this video is about purchasing software from other people? I'll give you a real clear answer. The build versus buy conversation comes down to this regardless. Like whether you are building internally or whether you are buying. Whether you are building your version of Lilly or whether you are buying, you still have to deal with this cross-workflow complexity that agents bring to the table, which means you still have to involve your technical teams to get it right. And when we go back through the Lilly experience and the incident that happened and understand what Code Wall did with their exploit, what we see here are failures that are taught in computer science 101. What we see are basic failures at a scale. 22 out of 200, over 10% endpoints not authenticated, especially especially endpoints that were writable. Endpoints writable to production that were unauthenticated. Question number one, does your AI platform really know the difference between a human user and an AI agent? Let's go back to the McKinsey story just to illustrate. Perhaps a senior consultant at McKinsey using Lilly might have legitimate read access to X client accounts, say 40, built up over 5 years. Perhaps an agent running on a particular client account should only touch that client account. That seems pretty logical, right? You want to bound the agent's permissions to what the agent is supposed to do. If the platform doesn't enforce that boundary I just described, one incident becomes a company-wide exposure event. That is not an IT problem, right? That's a board-level liability conversation. Second, audit. If something goes wrong, regulators don't ask, "What did the user do?" They ask, "What did the system do on behalf of the user and can you prove it?" If your platform can't answer that question for agents specifically, your compliance team is going to find out the hard way that the audit trail has a gap in it the size of every agent action in your organization, which is a fairly large gap given how capable agents are. Third, control. Can someone unplug this agent now? Not delete it, not file a ticket, not wait for a code deploy. Can someone from a console revoke the agent's access in the next 5 minutes while you figure out what happened? If the answer is no, your incident response plan has a big hole in it, and you will not discover that hole either until you do a tabletop exercise or until you discovered it at 3:00 a.m. when there's a big problem. The Codewall agent walked up to Lily's API and the API didn't ask who was calling. There was nothing to authenticate because the system wasn't built with the concept of an agent in it to authenticate at all. So, your liability question, the first one, is already answered. The blast radius is unbounded. There is no this agent to bound. And that's again part of why this incident is so important. We cannot design our software for a world where humans click through screens and where agents are bolted on afterward. We also cannot design our software in a world where technical teams cannot be at the table talking about the complexities of implementation of agentic workflows as first-class business problems. So, that's the first core question and I hope you see why it matters. You have to have a system that distinguishes between agents and humans. You should be asking that. Second core question Second question, what happens on your platform when the team is under pressure? This is an organizational question more than a technical question. It's a question about our our defaults as a team more than policies, right? Here's what I mean. There were 200 API endpoints, 22 of them shipped with no authentication including this critical one that enabled write access to production. So, the question we should be asking is why didn't one individual catch that? The question we should be asking is why wasn't there a default behavior set that would have captured this error as a team default operating procedure before any endpoint shipped at all. That is the deeper question and it gets at organizational design, not technology. Because that is an organizational design question, not a technology question. If the default is that a technical architect's opinion about what matters is really important in the business, then that is going to shape conversations in a way that you won't get if you leave the technical architecture to deal with whatever happens at 3:00 a.m. when there's an incident and you have to clean up afterward. And when I'm evaluating an AI platform, I don't just ask, does it support security controls in sort of an abstract way? I ask much more specific questions that get at this idea of team dynamics and how this particular piece of software shapes them. I ask what happens when my team can't configure them. I ask what the out-of-the-box posture I ask what the platform looks like in a couple of years if nobody touches the security settings after an initial setup event. Because that's going to be the version you're running. And by the way, if you're building a system, you need to ask the same team dynamic questions internally as I'm suggesting you ask externally. Because a vendor might say, well, we have a comprehensive authentication framework. Well, that may be true. Or all our authentication options are documented in the developer guide. I believe that. Or our enterprise customers have full flexibility to configure policies. I am sure that is true. But those kinds of sentences don't answer the core question. Because the core question that is asked is what happens when your team is told to move quickly? What is the technical default? What is true if the technical team does not have time to talk with the business about a particular piece of architecture? Where do we go? Do we go toward a default not not authenticated state? Do we go toward a default not authenticated state? Do we go toward a default where agents can be in charge and have fairly unlimited write access and that's the default and and therefore we should assume technical teams going fast are going to run into that at some point. So, if you're a decision maker and you can't answer the questions that I'm posing, this is going to be a challenge for you. If you can't answer whether your stack separately authenticates humans and agents and whether your stack is able to handle going quickly and respecting technical team concerns, that's something I would suggest you start focusing on. Because I think that if we don't have both of those covered, we run the risk inside of our our organizations of basically rolling the dice and waiting for another Lilly-like incident to happen. I don't think Lilly was an isolated thing that is special to McKinsey. As I've said before, lots of organizations struggle with this and I think McKinsey got unlucky. So, as I've shared, I'm putting a six-question technical checklist into the Substack today. These are the questions your developers need to ask your vendors or frankly if you're building something, your developers need to ask themselves. They cover the two areas I talked about, plus a couple more. How permissions compound when agents delegate to other agents, that's a very technical question. What actual token cost looks like at scale. Whether your audit trail can answer a regulator quickly. And what's reversible when an agent makes a mistake. These kinds of questions have specific failure modes that you would rather catch up front so that you can be confident that the technical default you're running with isn't going to end up in an unauthenticated endpoint that an agent on the internet can access and write to your production database. This is the intervention that helps us to take the lessons the industry has learned since February and that the industry is implementing as a bunch of solutions they're selling and actually apply them internally. So, no. In the end, I don't think Lilly was a security failure. I think it was a procurement and build failure that happened to surface as a security incident. I think yes, the exploit may have happened by SQL injection, but that's not the particular attack vector I worry about. The larger concern I worry about is do we have technical teams who are able to be at the table with business and clearly articulate the disproportionate impact that agents have across our data structures when we expect them and empower them to do the work they are capable of doing today. That is not traditional SaaS. It requires a complete rethink of how permissions and security works across those workflows. And I don't think we are asking questions of our vendors or questions of our teams that we listen to that allow us to get to the bottom of that. And because we're not doing so, I think it opens a lot of us internally to a frankly liability that we are going to end up rolling the dice on and hopefully hopefully avoiding, but maybe getting into the news on, right? Getting into the news in a way that we don't want to be because a security incident happens. And when you peel the onion on that security incident, it's a people challenge. It's about listening to your technical teams and empowering them to be at the table with business and describe how these agents make software purchasing different. Ultimately, the cheapest thing you can do this quarter is to move the technical developer review, a deep architectural review of whatever solution you're assessing earlier in the process. Bring your developers up to the table quicker and give them more influence on timeline, on deployment. Have people who understand architecture weigh in on the business timelines and the impact of that on these complex cross-agentic workflows. Because the most expensive thing you could do is to just keep the existing procurement process the way it is and pretend that these complex multi-agent workflows work like SaaS when they don't. So, I will see you next time. We're going to cover a lot more fun model news this week. The full six-question developer checklist is in the Substack today with the failure modes, the vendor answer rubric, and the playbook to do if you've already signed something that doesn't pass those tests. I didn't get a chance to talk about that today, but we have the repair playbook as well. Link in the description. I'll see you next time.

---

## Timestamped Segments

**[0:00]** $20, 2 hours, to get full read and write

**[0:03]** access to the AI platform that 70% of

**[0:06]** McKinsey's 40,000 consultants use every

**[0:09]** single day. This was an autonomous agent

**[0:11]** that spent 20 bucks with no credentials

**[0:13]** and zero insider help to get access to

**[0:16]** tens of millions of chat messages,

**[0:18]** access to tens of thousands of user

**[0:20]** accounts, and every system prompt

**[0:22]** governing how the platform reasons. All

**[0:24]** of them writable access, not just

**[0:26]** readable, writable. In other words, an

**[0:27]** attacker could have silently rewritten

**[0:30]** how the AI advises consultants who

**[0:32]** advise the largest firms in the world.

**[0:34]** The platform, it's called Lily. The

**[0:35]** startup that broke the news is called

**[0:37]** Code Wall, and the date was February

**[0:39]** 28th. Because it's taken the industry a

**[0:41]** couple of months to figure out what this

**[0:44]** agentic pattern looks like, what the

**[0:46]** lessons learned are, and how we change

**[0:48]** the way we purchase, invest, and build

**[0:50]** in software in response. And that's what

**[0:52]** I want to talk about today. First, this

**[0:54]** exploit wasn't exotic. It was SQL

**[0:56]** injection. The first documented case of

**[0:58]** SQL injection is in 1998. It's taught in

**[1:00]** every introductory web security course.

**[1:02]** And McKinsey, they have a great

**[1:03]** engineering team. Lily had been in

**[1:05]** production for more than 2 years. So,

**[1:06]** how did this happen? The answer has

**[1:08]** implications for your AI roadmap, for

**[1:10]** the platform that you signed up for last

**[1:12]** quarter. Most companies have a platform

**[1:14]** they signed up for last quarter. We have

**[1:15]** a lot of AI purchasing going on right

**[1:17]** now. And of course, for the deal that

**[1:18]** you're probably considering. Because

**[1:20]** again, most companies at most scales are

**[1:23]** considering an AI purchase this quarter.

**[1:25]** Three things to cover in this video.

**[1:26]** One, why calling Lily a security failure

**[1:29]** misses the point. Two, the procurement

**[1:32]** sequence most companies still use and

**[1:35]** why agents are breaking it now. And

**[1:37]** three, two questions you can ask this

**[1:39]** week that will tell you whether your AI

**[1:40]** investment is actual strategy or just an

**[1:43]** unpriced liability. I'm putting a

**[1:44]** further six-question checklist for your

**[1:46]** technical team on Substack, because

**[1:48]** that's part of the answer to how we

**[1:50]** avoid situations like the Lily story.

**[1:52]** So, first, here's what most of the

**[1:54]** analysis did with the Lily story. Code

**[1:56]** Wall disclosed responsibly on March 9th.

**[1:58]** They did not use this maliciously.

**[2:00]** McKinsey patched it up within hours,

**[2:01]** credit to them. The postmortem said what

**[2:03]** postmortems typically say. You should

**[2:05]** authenticate your endpoints, you should

**[2:06]** sanitize your inputs, treat your AI

**[2:08]** platform like production. That's not

**[2:09]** wrong, it's correct, it's true, but it's

**[2:11]** not the story. If you stop there, you

**[2:13]** walk away thinking the lesson is a story

**[2:15]** of technical hygiene, but it's not. The

**[2:17]** technical hygiene was never the issue

**[2:18]** here. McKinsey has many, many great

**[2:21]** engineers who know how to authenticate

**[2:23]** an endpoint. That defense is trivial to

**[2:25]** implement at this point. There's no

**[2:27]** organization on Earth where this is a

**[2:28]** hard engineering problem. So, let's run

**[2:30]** the pattern backward and let's ask

**[2:32]** ourselves deeper questions. 22 of 200

**[2:35]** endpoints shipped with no

**[2:36]** authentication. 22 of them. At that

**[2:39]** scale, that's not a random mistake.

**[2:40]** That's that's a pattern. That's a

**[2:42]** platform where maybe the default or

**[2:44]** maybe the assumption is that you can

**[2:46]** push to prod without that level of

**[2:49]** scrutiny on your endpoint. Because just

**[2:52]** to be clear, for those of you not

**[2:53]** familiar with APIs, this is not they

**[2:55]** forgot to lock the door. That framing

**[2:57]** puts the failure on a single person,

**[2:59]** some engineer on some Friday who skipped

**[3:01]** a checklist. If that's what happened,

**[3:03]** the fix would be training and it would

**[3:04]** be easy. But if you have 22 of these,

**[3:06]** and in particular, if the exploit that

**[3:09]** happened happened because one of the

**[3:11]** endpoints allowed production right

**[3:13]** access without authentication, that's a

**[3:15]** much deeper engineering culture and

**[3:18]** structure problem that needs to be

**[3:20]** fixed, that depends on a deeper

**[3:22]** knowledge of what agents are capable of

**[3:24]** today. And let me be clear, this is not

**[3:26]** they forgot to lock the door. I know

**[3:29]** that not everyone's familiar with APIs

**[3:30]** here. It's not that like you should lock

**[3:32]** the door on the API and it would be

**[3:34]** fixed, because that framing puts the

**[3:35]** failure on an individual. Like some

**[3:38]** engineer, some Friday, someone skipped a

**[3:39]** checklist. If that's what happened, the

**[3:41]** fix would be training, but if that's

**[3:43]** what happened, we would not see 22 of

**[3:45]** these endpoints in production. I don't

**[3:47]** believe. I don't think that's what

**[3:48]** happened. I don't think that's the root

**[3:49]** cause. I think the root cause is closer

**[3:52]** to no one asking whether the API

**[3:55]** endpoint itself was the correct shape

**[3:58]** for assuming strong agentic access on

**[4:03]** the web. We need to be assuming that the

**[4:05]** production software we put into place is

**[4:08]** going to meet AI agents, and it looks

**[4:11]** like that consideration did not happen.

**[4:12]** And if the people who would ask those

**[4:14]** questions, probably technical people,

**[4:16]** probably engineers, are not in the room

**[4:19]** with space to talk, then a lot of the

**[4:21]** shape of the software we're putting out

**[4:23]** as AI software is going to be determined

**[4:25]** by executives and business teams working

**[4:28]** to a deadline, rather than technical

**[4:31]** folks who can speak to where this

**[4:34]** agentic impact is going to show up in

**[4:37]** business results, which is exactly what

**[4:39]** happened here. When when Lily first came

**[4:41]** out 2 years ago, we didn't have

**[4:43]** autonomous AI agents that could hack

**[4:46]** through a public endpoint and get to

**[4:48]** production data. That is something that

**[4:50]** is very normal in 2026. If we want to

**[4:53]** build software and purchase software

**[4:55]** that has lasting value, we need

**[4:57]** technical voices at the table that can

**[5:00]** anticipate that kind of trajectory and

**[5:03]** speak to it in a way that helps us to

**[5:05]** shape our purchase path. And this is

**[5:07]** where I have a lot of sympathy for the

**[5:08]** McKinsey team. I don't believe this is

**[5:10]** really a McKinsey story per se. I think

**[5:13]** McKinsey is the version that made the

**[5:14]** news because the consequences were

**[5:16]** vivid, the report was good, and frankly

**[5:18]** the brand is very large. But I've seen

**[5:20]** the inside of enough enterprise AI

**[5:22]** programs this year to tell you that the

**[5:23]** shape of this failure shows up in a lot

**[5:25]** of places. The shape is that governance

**[5:27]** and thoughtful technical perspective

**[5:30]** tend to arrive late, and the exploit

**[5:32]** just happens to show up in some cases as

**[5:35]** like a receipt. But knowing the shape of

**[5:37]** failure by itself isn't the useful part.

**[5:39]** The useful piece here is understanding

**[5:41]** the process that keeps producing it,

**[5:43]** because once you see the process, you

**[5:45]** can change your pattern and actually

**[5:46]** update it and do better next time.

**[5:48]** Here's the process. Most enterprise

**[5:51]** software has been bought for the last 15

**[5:54]** years or more in the same sequence.

**[5:56]** Strategic decision at the top,

**[5:58]** procurement negotiates the contract,

**[6:00]** security and compliance review, IT plans

**[6:02]** and integration, developers build

**[6:04]** against whatever platform already got

**[6:05]** purchased. That sequence works great for

**[6:08]** SaaS. It worked for Salesforce, Workday,

**[6:10]** ServiceNow, the entire generation of

**[6:11]** cloud applications most companies run on

**[6:14]** today. And worked because SaaS is

**[6:16]** bounded. The vendor gives you an admin

**[6:18]** console, a set of integration points, a

**[6:20]** published API, and a permissions model

**[6:22]** that maps cleanly to roles. You're

**[6:24]** configuring software. That's not that

**[6:26]** much to build, right? For agents, that

**[6:29]** same sequence leads to disaster. Walk

**[6:32]** through what an agent actually does on a

**[6:33]** single real run inside a company in 2026

**[6:36]** now. The user says, "Prepare the renewal

**[6:38]** brief for our largest customer." It's

**[6:39]** April 2026. The agent has to figure out

**[6:41]** which systems hold the answer. It pulls

**[6:43]** from the CRM, from support tickets, from

**[6:45]** contract management, from product usage

**[6:46]** data, from call transcripts, from

**[6:48]** internal wiki. It crosses permission

**[6:50]** boundaries that for a human are mediated

**[6:52]** by what's visible on a screen, but for

**[6:54]** an agent may be mediated by tokens and

**[6:56]** roles and scopes that have to actually

**[6:57]** exist as code written by someone. When a

**[6:59]** human consultant pulls a renewal brief

**[7:01]** together, none of this complexity that I

**[7:03]** just described is visible to them. They

**[7:05]** open Salesforce, they glance at the

**[7:07]** support history, they check the

**[7:08]** contract, they scan a Slack thread from

**[7:10]** last quarter. They don't notice the

**[7:12]** contract management tool has its own

**[7:13]** permissions. The support system has its

**[7:15]** own audit log. The CRM treats their

**[7:17]** access differently from the analyst's

**[7:19]** access. They don't notice half the wiki

**[7:21]** pages they're reading are stale. They

**[7:22]** don't have to notice. Their eyes do the

**[7:24]** work. The screen is the permissions

**[7:26]** model. If they shouldn't see something,

**[7:28]** the screen doesn't show it. An agent has

**[7:30]** no eyes. The agent is asking each of

**[7:32]** those systems in code, "Am I allowed to

**[7:34]** read this?" And every one of those

**[7:35]** systems has to have a clear answer. And

**[7:37]** every one of those has to be auditable.

**[7:39]** And every one One audits has to compose

**[7:41]** with every other one when a regulator

**[7:43]** asks what happened in the sequence. None

**[7:45]** of this exists by default. All of it is

**[7:47]** engineering work that someone has to do

**[7:49]** against a deadline before the agent

**[7:51]** ships. And that's just for one task.

**[7:53]** Multiply that by all the workflows your

**[7:55]** roadmap promises to automate and you see

**[7:57]** the shape of what we're committing to as

**[7:59]** a community. The SAS environment that

**[8:02]** we've described for procurement was a

**[8:04]** very bounded place. I just described how

**[8:06]** clean it is to grab software, install

**[8:08]** it, and then maybe you build a few

**[8:09]** integrations. What I'm describing with

**[8:11]** cross-workflow integrations is not that.

**[8:13]** It's extremely unbounded and we are

**[8:16]** signing up for that. And that is part of

**[8:18]** why this is so complex and why the

**[8:19]** procurement process is breaking. With

**[8:22]** agents, the implementation question

**[8:24]** isn't downstream of a strategic

**[8:26]** decision. It's effectively the strategic

**[8:28]** decision itself. If the agent can't

**[8:30]** authenticate against the system it

**[8:32]** needs, the strategy isn't going to work.

**[8:35]** If the permissions model only thinks

**[8:37]** about humans clicking through screens,

**[8:38]** the strategy doesn't work

**[8:40]** >> either. If If every run reassembles the

**[8:42]** same business context from scratch and

**[8:44]** your token bill goes up by 3x, the

**[8:47]** strategy doesn't work. If you can't

**[8:49]** audit what the agent did, the strategy

**[8:51]** is not going to get past legal and

**[8:52]** shouldn't. None of these are

**[8:54]** implementation details to be worked out

**[8:56]** later. Every one of them is enough to

**[8:58]** change how the roadmap actually is

**[9:00]** shaped. So, when you put implementation

**[9:02]** and your dev team last in the buying

**[9:04]** sequence, you're committing capital to a

**[9:06]** strategy whose viability has not been

**[9:09]** tested.

**[9:10]** And you don't find that out with a demo.

**[9:13]** You find it out 6 months in when your

**[9:14]** team is trying to push the workflow into

**[9:17]** production and discovering one boundary

**[9:19]** at a time that the platform you

**[9:20]** purchased wasn't buildable for the work

**[9:23]** you bought it to do.

**[9:25]** The vendors know this now. That's what

**[9:27]** this week has made clear and that closes

**[9:28]** the circle on the February conversation

**[9:31]** and what happened with Code Wallet

**[9:32]** Lilly. Because in the last week or so,

**[9:34]** Anthropic and OpenAI have both stood up

**[9:37]** enterprise services companies with

**[9:38]** billions of dollars behind them to put

**[9:40]** engineers inside customer build rooms

**[9:43]** for this exact complexity. SAP acquired

**[9:45]** Dreamio and Prior Labs to bring a

**[9:47]** unified data layer and tabular

**[9:49]** foundation models to the place where

**[9:51]** actual business data lives, the ledgers

**[9:53]** of the business, right? Not marketing

**[9:54]** copy. Pinecone launched Nexus, which is

**[9:56]** essentially stop making your agent

**[9:58]** rebuild the business from scratch every

**[9:59]** time it runs. Salesforce shipped

**[10:01]** headless 360, which exposes their

**[10:03]** platform as APIs and tools and command

**[10:05]** line commands because agents don't click

**[10:07]** through screens. ServiceNow opened up

**[10:09]** action fabric so outside agents can

**[10:11]** trigger governed workflows, playbooks,

**[10:14]** approvals, catalogs through a controlled

**[10:16]** surface with identity and audit

**[10:17]** attached. You see how this ties in,

**[10:19]** right? Six different announcements all

**[10:21]** within the last week or so, one story.

**[10:23]** Every single one of those vendors is now

**[10:25]** selling you the thing your AI roadmap

**[10:27]** was supposed to already have, reachable

**[10:29]** surfaces, governed action, permission

**[10:31]** aware data, cheaper context assembly,

**[10:34]** forward deployed humans who can actually

**[10:36]** wire up your workflows. I'm not saying

**[10:37]** that this is a silver bullet, but I'm

**[10:39]** saying it's a signal. The signal is that

**[10:41]** the model was never the hard part. The

**[10:43]** hard part is exactly what the Lilly

**[10:45]** incident surfaced, whether the agent can

**[10:47]** reach the right data, use the right

**[10:49]** permissions, trigger the right workflow,

**[10:51]** leave the right audit trail, and do all

**[10:53]** of it at a cost the company can live

**[10:55]** with. So, the question isn't which

**[10:58]** vendor you pick from that list. I'm not

**[10:59]** asking about that. The question is how

**[11:01]** do you know before you sign with a

**[11:03]** vendor whether any of what they are

**[11:05]** promising is going to deliver actual

**[11:07]** value. You might be wondering, why are

**[11:08]** we talking about an external hack of

**[11:10]** Lilly, which was a system that McKinsey

**[11:12]** stood up on its own, and the rest of

**[11:14]** this video is about purchasing software

**[11:17]** from other people? I'll give you a real

**[11:18]** clear answer. The build versus buy

**[11:20]** conversation comes down to this

**[11:22]** regardless. Like whether you are

**[11:24]** building internally or whether you are

**[11:26]** buying. Whether you are building your

**[11:27]** version of Lilly or whether you are

**[11:28]** buying, you still have to deal with this

**[11:32]** cross-workflow complexity that agents

**[11:35]** bring to the table, which means you

**[11:36]** still have to involve your technical

**[11:38]** teams to get it right. And when we go

**[11:41]** back through the Lilly experience and

**[11:43]** the incident that happened and

**[11:44]** understand what Code Wall did with their

**[11:45]** exploit, what we see here are failures

**[11:49]** that are taught in computer science 101.

**[11:51]** What we see are basic failures at a

**[11:53]** scale. 22 out of 200, over 10% endpoints

**[11:57]** not authenticated, especially especially

**[11:59]** endpoints that were writable. Endpoints

**[12:01]** writable to production that were

**[12:03]** unauthenticated. Question number one,

**[12:05]** does your AI platform really know the

**[12:08]** difference between a human user and an

**[12:10]** AI agent? Let's go back to the McKinsey

**[12:12]** story just to illustrate. Perhaps a

**[12:14]** senior consultant at McKinsey using

**[12:16]** Lilly might have legitimate read access

**[12:18]** to X client accounts, say 40, built up

**[12:20]** over 5 years. Perhaps an agent running

**[12:22]** on a particular client account should

**[12:25]** only touch that client account. That

**[12:27]** seems pretty logical, right? You want to

**[12:29]** bound the agent's permissions to what

**[12:30]** the agent is supposed to do. If the

**[12:32]** platform doesn't enforce that boundary I

**[12:35]** just described, one incident becomes a

**[12:37]** company-wide exposure event. That is not

**[12:40]** an IT problem, right? That's a

**[12:41]** board-level liability conversation.

**[12:43]** Second, audit. If something goes wrong,

**[12:45]** regulators don't ask, "What did the user

**[12:48]** do?" They ask, "What did the system do

**[12:50]** on behalf of the user and can you prove

**[12:52]** it?" If your platform can't answer that

**[12:54]** question for agents specifically, your

**[12:56]** compliance team is going to find out the

**[12:58]** hard way that the audit trail has a gap

**[13:00]** in it the size of every agent action in

**[13:03]** your organization, which is a fairly

**[13:05]** large gap given how capable agents are.

**[13:07]** Third, control. Can someone unplug this

**[13:09]** agent now? Not delete it, not file a

**[13:11]** ticket, not wait for a code deploy. Can

**[13:13]** someone from a console revoke the

**[13:15]** agent's access in the next 5 minutes

**[13:17]** while you figure out what happened? If

**[13:19]** the answer is no, your incident response

**[13:21]** plan has a big hole in it, and you will

**[13:23]** not discover that hole either until you

**[13:25]** do a tabletop exercise or until you

**[13:27]** discovered it at 3:00 a.m. when there's

**[13:28]** a big problem. The Codewall agent walked

**[13:30]** up to Lily's API and the API didn't ask

**[13:32]** who was calling. There was nothing to

**[13:34]** authenticate because the system wasn't

**[13:36]** built with the concept of an agent in it

**[13:38]** to authenticate at all. So, your

**[13:39]** liability question, the first one, is

**[13:42]** already answered. The blast radius is

**[13:44]** unbounded. There is no this agent to

**[13:46]** bound. And that's again part of why this

**[13:48]** incident is so important. We cannot

**[13:51]** design our software for a world where

**[13:53]** humans click through screens and where

**[13:55]** agents are bolted on afterward. We also

**[13:58]** cannot design our software in a world

**[14:00]** where technical teams cannot be at the

**[14:03]** table talking about the complexities of

**[14:05]** implementation of agentic workflows as

**[14:07]** first-class business problems. So,

**[14:09]** that's the first core question and I

**[14:11]** hope you see why it matters. You have to

**[14:13]** have a system that distinguishes between

**[14:15]** agents and humans. You should be asking

**[14:17]** that. Second core question Second

**[14:19]** question, what happens on your platform

**[14:21]** when the team is under pressure? This is

**[14:22]** an organizational question more than a

**[14:24]** technical question. It's a question

**[14:25]** about our our defaults as a team more

**[14:28]** than policies, right? Here's what I

**[14:30]** mean. There were 200 API endpoints, 22

**[14:32]** of them shipped with no authentication

**[14:33]** including this critical one that enabled

**[14:36]** write access to production. So, the

**[14:38]** question we should be asking is why

**[14:40]** didn't one individual catch that? The

**[14:42]** question we should be asking is why

**[14:45]** wasn't there a default behavior set that

**[14:50]** would have captured this error as a team

**[14:55]** default operating procedure before any

**[14:58]** endpoint shipped at all. That is the

**[15:00]** deeper question and it gets at

**[15:02]** organizational design, not technology.

**[15:05]** Because that is an organizational design

**[15:07]** question, not a technology question. If

**[15:09]** the default is that a technical

**[15:11]** architect's opinion about what matters

**[15:13]** is really important in the business,

**[15:15]** then that is going to shape

**[15:17]** conversations

**[15:18]** in a way that you won't get if you leave

**[15:22]** the technical architecture to deal with

**[15:25]** whatever happens at 3:00 a.m. when

**[15:27]** there's an incident and you have to

**[15:29]** clean up afterward. And when I'm

**[15:31]** evaluating an AI platform, I don't just

**[15:33]** ask, does it support security controls

**[15:36]** in sort of an abstract way? I ask much

**[15:39]** more specific questions that get at this

**[15:41]** idea of team dynamics and how this

**[15:43]** particular piece of software shapes

**[15:45]** them. I ask what happens when my team

**[15:47]** can't configure them. I ask what the

**[15:48]** out-of-the-box posture I ask what the

**[15:50]** platform looks like in a couple of years

**[15:52]** if nobody touches the security settings

**[15:54]** after an initial setup event. Because

**[15:56]** that's going to be the version you're

**[15:57]** running. And by the way, if you're

**[15:59]** building a system, you need to ask the

**[16:01]** same team dynamic questions internally

**[16:03]** as I'm suggesting you ask externally.

**[16:04]** Because a vendor might say, well, we

**[16:06]** have a comprehensive authentication

**[16:08]** framework. Well, that may be true. Or

**[16:10]** all our authentication options are

**[16:11]** documented in the developer guide. I

**[16:13]** believe that. Or our enterprise

**[16:15]** customers have full flexibility to

**[16:16]** configure policies. I am sure that is

**[16:18]** true. But those kinds of sentences don't

**[16:21]** answer the core question. Because the

**[16:23]** core question that is asked is what

**[16:26]** happens when your team is told to move

**[16:28]** quickly? What is the technical default?

**[16:30]** What is true if the technical team does

**[16:33]** not have time to talk with the business

**[16:36]** about a particular piece of

**[16:37]** architecture? Where do we go? Do we go

**[16:40]** toward a default not not authenticated

**[16:42]** state? Do we go toward a default not

**[16:44]** authenticated state? Do we go toward a

**[16:46]** default where agents can be in charge

**[16:48]** and have fairly unlimited write access

**[16:50]** and that's the default and and therefore

**[16:52]** we should assume technical teams going

**[16:54]** fast are going to run into that at some

**[16:55]** point. So, if you're a decision maker

**[16:57]** and you can't answer the questions that

**[17:00]** I'm posing, this is going to be a

**[17:02]** challenge for you. If you can't answer

**[17:03]** whether your stack separately

**[17:06]** authenticates humans and agents and

**[17:08]** whether your stack is able to handle

**[17:12]** going quickly and respecting technical

**[17:15]** team concerns, that's something I would

**[17:17]** suggest you start focusing on. Because I

**[17:19]** think that if we don't have both of

**[17:20]** those covered, we run the risk inside of

**[17:23]** our our organizations of basically

**[17:25]** rolling the dice and waiting for another

**[17:27]** Lilly-like incident to happen. I don't

**[17:29]** think Lilly was an isolated thing that

**[17:30]** is special to McKinsey. As I've said

**[17:32]** before, lots of organizations struggle

**[17:34]** with this and I think McKinsey got

**[17:35]** unlucky. So, as I've shared, I'm putting

**[17:37]** a six-question technical checklist into

**[17:39]** the Substack today. These are the

**[17:41]** questions your developers need to ask

**[17:43]** your vendors or frankly if you're

**[17:45]** building something, your developers need

**[17:46]** to ask themselves. They cover the two

**[17:49]** areas I talked about, plus a couple

**[17:51]** more. How permissions compound when

**[17:52]** agents delegate to other agents, that's

**[17:54]** a very technical question. What actual

**[17:56]** token cost looks like at scale. Whether

**[17:58]** your audit trail can answer a regulator

**[18:00]** quickly. And what's reversible when an

**[18:02]** agent makes a mistake. These kinds of

**[18:04]** questions have specific failure modes

**[18:07]** that you would rather catch up front so

**[18:09]** that you can be confident that the

**[18:10]** technical default you're running with

**[18:12]** isn't going to end up in an

**[18:13]** unauthenticated endpoint that an agent

**[18:15]** on the internet can access and write to

**[18:16]** your production database. This is the

**[18:18]** intervention that helps us to take the

**[18:21]** lessons the industry has learned since

**[18:24]** February and that the industry is

**[18:25]** implementing as a bunch of solutions

**[18:26]** they're selling and actually apply them

**[18:28]** internally. So, no. In the end, I don't

**[18:30]** think Lilly was a security failure. I

**[18:32]** think it was a procurement and build

**[18:35]** failure that happened to surface as a

**[18:36]** security incident. I think yes, the

**[18:39]** exploit may have happened by SQL

**[18:40]** injection, but that's not the particular

**[18:43]** attack vector I worry about. The larger

**[18:45]** concern I worry about is do we have

**[18:49]** technical teams who are able to be at

**[18:52]** the table with business and clearly

**[18:54]** articulate the disproportionate

**[18:57]** impact that agents have across our data

**[19:01]** structures when we expect them and

**[19:03]** empower them to do the work they are

**[19:06]** capable of doing today. That is not

**[19:08]** traditional SaaS. It requires a complete

**[19:12]** rethink of how permissions and security

**[19:14]** works across those workflows. And I

**[19:16]** don't think we are asking questions of

**[19:18]** our vendors or questions of our teams

**[19:21]** that we listen to that allow us to get

**[19:23]** to the bottom of that. And because we're

**[19:25]** not doing so, I think it opens a lot of

**[19:27]** us internally to a frankly liability

**[19:31]** that we are going to end up rolling the

**[19:33]** dice on and hopefully hopefully

**[19:35]** avoiding, but maybe getting into the

**[19:37]** news on, right? Getting into the news in

**[19:38]** a way that we don't want to be because a

**[19:40]** security incident happens. And when you

**[19:42]** peel the onion on that security

**[19:43]** incident, it's a people challenge. It's

**[19:45]** about listening to your technical teams

**[19:47]** and empowering them to be at the table

**[19:49]** with business and describe how these

**[19:51]** agents make software purchasing

**[19:53]** different. Ultimately, the cheapest

**[19:56]** thing you can do this quarter is to move

**[19:58]** the technical developer review, a deep

**[20:01]** architectural review of whatever

**[20:02]** solution you're assessing earlier in the

**[20:04]** process. Bring your developers up to the

**[20:06]** table quicker and give them more

**[20:09]** influence on timeline, on deployment.

**[20:11]** Have people who understand architecture

**[20:13]** weigh in on the business timelines and

**[20:16]** the impact of that on these complex

**[20:18]** cross-agentic workflows. Because the

**[20:20]** most expensive thing you could do is to

**[20:22]** just keep the existing procurement

**[20:24]** process the way it is and pretend that

**[20:26]** these complex multi-agent workflows work

**[20:28]** like SaaS when they don't. So, I will

**[20:31]** see you next time. We're going to cover

**[20:32]** a lot more fun model news this week. The

**[20:34]** full six-question developer checklist is

**[20:36]** in the Substack today with the failure

**[20:37]** modes, the vendor answer rubric, and the

**[20:39]** playbook to do if you've already signed

**[20:41]** something that doesn't pass those tests.

**[20:42]** I didn't get a chance to talk about that

**[20:44]** today, but we have the repair playbook

**[20:45]** as well. Link in the description. I'll

**[20:47]** see you next time.
