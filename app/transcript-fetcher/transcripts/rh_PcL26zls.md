# Transcript: You Can't Run AI Agents Without This

**URL:** https://www.youtube.com/watch?v=rh_PcL26zls
**Segments:** 427
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 14:20
**Uploaded:** 2026-06-21

---

## Full Text

The fastest way to make an AI agent dangerous, I'm convinced of this, is to let everyone use it and nobody own it. And I want to start there because I think we've made agents sound way more confusing than they really need to be. A lot of us hear the word agent and we immediately think, okay, this is some fully autonomous thing running in the background. Is this a digital employee? Is this a model? Is this Codex? Is this Claude? Is this chat GPT with a custom trench coat? What are we talking about? And that confusion matters because the word agent means kind of all of those things in different contexts. And if you're still stuck asking, am I even using an agent? You are probably not asking the most important question. Who's responsible for the work that this thing is now doing? So, this video is going to be very simple. I want to make the basics clear, how to know if something is close enough to an agent that you should care, what to do with it once you have it, what care and feeding means, and when this becomes a teamwork flow. Because the big shift here is not that everyone needs to become an AI engineer. The big shift is that more of us are going to have little systems that do work for us. And if those systems can read files and draft messages and maybe change code or summarize customers or update records, somebody needs to own them. Not philosophically, not on an org chart, operationally. So, let's make this really concrete. Let's say you open chat GPT, you can go ahead and do that, type a question, get an answer, and then you move on about your day. That is an assistant interaction. You asked, it answered, you decide what to do next. Now, let's say you have a custom GPT that reads your notes every week, it prepares your Monday priorities, it follows your rules, and it produces a work product you actually use. That is close enough to an agent for this conversation. Let's say you open Claude and ask it to help write a paragraph, same thing. That's mostly an assistant. But if you have a Claude project with files and instructions and examples and a repeated job, or if you use Claude code to inspect files and make changes and issue commands and come back with a result, now you're in agent territory. And many uses of Codex are very clearly in this category. If you give Codex a repo and say inspect this code, fix the bug, run the test, show me the diff, it's doing work across steps with tools and real consequences. It may be supervised, it may ask for approval, it may not be autonomous in the sci-fi sense, but it's an agentic workflow. The brand name, the word agent, is not the point. ChatGPT, Claude, Codex, Cursor, a workflow tool, they can all be agents. The label doesn't matter, the job does. And once you delegate a job, your job of owning starts. And I think this is where people get tripped up because the AI conversation is still obsessed with building. Build an agent, make an agent, launch an agent, connect tools, automate the workflow. And sure that matters. I like building. I want people to build. But the moment after the initial build demo is where your real responsibility for that agent over the long term begins. Useful agents don't stay in demo land on day one and two. They start becoming part of how daily work gets done for you, for your team. A research agent has to find sources you trust every single day. A writing agent has to work with your voice as it evolves every single day. A coding agent changes files and has to be trusted to do that. A support agent shapes what customers hear from the company. That's critical. A product agent shapes what shows up in the backlog for engineering. And if no one owns that agent and feels like they have skin in the game, the danger can feel ordinary until it's not. The agent will use an old policy. Maybe it'll pull from stale docs. Maybe it'll repeat a bad pattern. Maybe it will draft something plausible but wrong and you'll say, "Oh, ChatGPT's hallucinating again." Maybe it'll turn an assumption into a recommendation. And because the output looks really clean, people will stop noticing where it came from. And that's the risk. It's not evil AI, it's the unowned work starts to have real consequences over time because people don't check it and care for it. So, what do you do with your agent? I I start with four things and I want to keep this really, really simple. Give it a job, give it a diet, give it boundaries, and give it a review loop. The job is what this agent is supposed to do. Not help with a product on something vague, right? Not make me more productive. A real job that matters. Like prepare first-pass backlog items for refinement. Draft refund replies for this ticket type. Inspect a pull request for risky changes. Build me a weekly research brief from these sources. If you can't say the job in a sentence, the agent is probably too vague. The diet is what the agent reads. This matters a lot more than people think. Agents eat context, right? They eat docs and tickets and transcripts and repo instructions and examples and whatever else you put in front of them. If the diet is stale or bloated, the agent can get stale and bloated. If the diet is messy, the agent can get messy. If the diet uses incorrect examples, the agent learns bad habits. This is why the little Pokémon analogy works so well for me. Collecting the Pokémons isn't the point. You have to know what each Pokémon is good at. You have to know where not to use it. You have to know what it has been trained on, and you have to notice when it starts picking up bad habits. And that sounds kind of silly, but the responsibility for care is real. And then come the boundaries. What can this agent touch? Can it read files? Can it draft? Can it write to the system? Can it send or delete? Can it update Jira? These are not the same level of risk. A draft-only agent is one thing. An agent that can write into a system of record is much, much more serious. An agent that can send a customer message or merge code is in a different category entirely. And your sense of ownership should move with that. You should feel emotional stakes. So, the rule's simple. Start with read-only. Start with draft-only if you're unsure. Let the agent earn more permission, and make sure you're comfortable moving outside that narrow job. And then the review loop is how you keep it healthy. And this is one of the phrases people like to use: loop, system, workflow. It's getting used a lot, and I think it can sound more complicated than it is. A loop just means the work comes back around. The agent runs, a human reviews, maybe another agent reviews in some cases, mostly a human reviews. You notice what was good and what was bad, you update the instructions, the sources, the permission, the agent runs again. There's the loop. It's not magic, it's not a giant governance process, it's not the best thing since sliced bread, it's just a way work gets done with agents. Run, review, improve, run again. So, let me give you a product team version because this is where this becomes really obvious with a specific example. Imagine a scrum team building a new onboarding flow. Every week before backlog refinement, someone has to do the same messy prep. You read the customer tickets, you check the PRD, you look at the design changes, you review the backlog, you pull the pain, and you turn it into acceptance criteria, and dependencies, and tickets. It's real work. It's a lot of product managers weeks. So, the PM starts to build a story prep agent to help themselves. And the first vision is simple. It's going to read the current PRD, the design brief, the tagged support tickets, the backlog, and a few examples of good stories. And then it's going to prepare a refinement package. Not final tickets, just a package. It's going to say, "Here are the candidate stories, here's the customer evidence, here are the acceptance criteria, here are the dependencies, here are the assumptions I'm making, and here's the open decisions my human needs to make." It's a great agent job to start with. You can do that in Codex or Claude. But now imagine the team starts relying on that package every week. It's now a team agent. Now the agent is shaping the sprint. If the PRD is old, old product assumptions are going to enter real work. If the support tickets are noisy, agent oversight starts to matter. If the design changed yesterday and the agent didn't pick up on that because of a job conflict, that's going to matter. It's not going to be an explosion or a robot takeover, right? But it's going to be an issue for the team. So, what does ownership look like in that context? The product manager owns the job because the product manager owns backlog quality. The operating team has to own the operating agent. And the maintenance loop is not complicated. So, what does ownership look like? The product manager owns the job and is the single-threaded owner that should care about whether the agent works or not. That simple. The engineering lead can help with technical assumptions. The QA team can help with testability. The AI team might help with tooling in some cases. And the maintenance loop for that agent is not as complicated as it might sound, even though it's an agent that does a lot of work. Before refinement, the agent prepares the packet, and the PM should review that. During refinement, the team can notice where it helped and where it confused the discussion. After the sprint, the owner, the PM, should check a few stories. Did engineers have to rewrite them? Did QA understand them? Did dependencies show up late? If you can fix the inputs to the agent and change your output, you can fix the system. So, remove the stale PRD. Add a better example. Change what it is allowed to read. That's care and feeding. And that's how you go beyond prompting and start to work like you're in 2026 with agents and loops. Prompting is asking. Agent work is giving context and care and feeding to the agent so it can do its job. There's a big difference between asking, "Write acceptance criteria for this feature, please." and giving an agent a job. The job might look like, "Read the PRD, the last 20 support tickets, the design brief, and our three best backlog examples. Draft the stories for refinement, attach the customer evidence, mark assumptions, and don't create Jira tickets. Put everything into review so I can look at it first." Do you feel that difference? One is a prompt, and the PM may feel more productive, but it may not hit the team. The other is a job with sources and boundaries and output and a review loop, and it absolutely affects the entire team. And this is the move that most people need to make in 2026 from prompts to jobs. Now, if you're thinking about this as a team leader, the question becomes bigger, but it doesn't need to become more abstract. This is a dangerous spot where agents can go unowned. Nobody owns the HR agent that summarizes performance notes before calibration, so nobody tracks whether it's pulling from stale manager feedback or flattening important context. That's a real example, by the way. Nobody owns the recruiting agent that drafts candidate scorecards, so no one's accountable when it drifts. No one knows the support triage agent. So, refund policy may be stale and may be misapplied. You see the same thing cropping up all over the business when you have projects that parachute in from an AI team and that end up unowned in those target teams. Finance can have the same thing, right? You're going to need an agent roster as a team lead. Not a big database, right? Just a list of agents your team is using. This is our story prep agent. This is our release note agent. This is our customer call summary agent. This is our PR review agent. And for each of them, you should know who the owner is. You should know who what the sources are the agent can look at, what the permissions are, the review cadence, and the known failure modes. And that's it. Because once the agent is visible, you can manage it. As a team leader, you can manage it. If it's invisible, it just becomes this weird shadow process where work is moving through tools and nobody can explain how the output got there. And there's these anecdotes that people will bring up in performance reviews that say an AI native now. That's not productive. And I get it. The energy right now is build, build, build. But if every ambitious person in the company creates three agents, you don't necessarily have more productivity if you don't scale that ownership. I love the build energy. It's not bad. It's powerful, but powerful things need owners. And if you want the simplest version of this, here is the owner card that you should take with you. For every agent that matters, write down the name, the owner, the job, the sources, what it can do, what it can't do, and the failure mode you need to watch for. I said that was a spreadsheet for team leaders, but that card can also be the agent ownership card for individuals. Literally, you can make a Slack channel with a bunch of agent owner cards where you can say, "This is my agent. This is what it does." And like people can share them. And this is something where if you're trying to create agent-to-agent collaboration in the company, which a lot of people are doing through Slack, you kind of need a way for the humans to understand what these agents are doing at the top and to have almost an agent registry so the humans can understand what's going on. And yes, this is on purpose a little bit like Google's A2A protocol. Google's A2A protocol assumes that agents need introduction cards like that to each other. That's great, but what about the humans? We need a sense of ownership, almost like a certificate for the agent. And I find the companies that have that mindset, regardless of what they call it, do better because they take agent ownership more seriously and they should than agent building. Just building a new agent, you shouldn't get credit for these days. Owning an agent and using it to deliver value, that's what you should get credit for. And I think this is what catching up with AI actually looks like today. It's not having the most agents. It's not knowing every tool. It's not winning a vocabulary argument about loops and eval's. It's having a small number of agents that you own and that deliver real value in workflows. You know what they do. You know what they eat. You know what they can touch. You know how you review them. You know when to trust them and when not to do. They're your pet Pokemons. You know what work you delegated and what responsibility you kept. This is the grown-up version of agent adoption. Ironically, as a child of the '80s and '90s, Pokemon prepared me well. Prompting was the first skill for us, right? Back in 2023, we had to learn how to ask better questions. And that's still a useful skill because it forces us to articulate. Delegation was the next skill. We had to learn how to hand over real work. That's a very 2025 thing. Maintenance is a 2026 skill because useful agents become our responsibility. So, here's your decision rule, very easy. If a system can read important context, produce work you act on or your team acts on, touch a workflow other people depend on, it needs an owner now. If it's yours, you own it. If it belongs to the team, the team needs to one person as an owner. And if nobody's willing to own it, it probably shouldn't be doing important work and you should think about decommissioning it. Look, I put the deeper checklist and the owner card and the whole guide for how to sort of develop an agent registry at the company or frankly for you, your Pokémon collection agent set over on Substack because that works much better as a written guide. But the mental model really is this simple. Stop asking only whether you can build an agent. Start asking whether you can care and feed it. Every agent needs an owner. Not because agents are bad, because useful agents must become part of our work in 2026. That is the bar. So, take care of your little Pokémon agents. I hope this has helped clear up a lot of the buzz and the confusion around what an agent is and what our job is with agents in 2026. I'll see you next time.

---

## Timestamped Segments

**[0:00]** The fastest way to make an AI agent

**[0:02]** dangerous, I'm convinced of this, is to

**[0:04]** let everyone use it and nobody own it.

**[0:07]** And I want to start there because I

**[0:08]** think we've made agents sound way more

**[0:11]** confusing than they really need to be. A

**[0:13]** lot of us hear the word agent and we

**[0:14]** immediately think, okay, this is some

**[0:16]** fully autonomous thing running in the

**[0:18]** background. Is this a digital employee?

**[0:20]** Is this a model? Is this Codex? Is this

**[0:22]** Claude? Is this chat GPT with a custom

**[0:24]** trench coat? What are we talking about?

**[0:26]** And that confusion matters because the

**[0:28]** word agent means kind of all of those

**[0:30]** things in different contexts. And if

**[0:32]** you're still stuck asking, am I even

**[0:33]** using an agent? You are probably not

**[0:35]** asking the most important question.

**[0:37]** Who's responsible for the work that this

**[0:40]** thing is now doing? So, this video is

**[0:42]** going to be very simple. I want to make

**[0:44]** the basics clear, how to know if

**[0:46]** something is close enough to an agent

**[0:47]** that you should care, what to do with it

**[0:49]** once you have it, what care and feeding

**[0:51]** means, and when this becomes a teamwork

**[0:53]** flow. Because the big shift here is not

**[0:56]** that everyone needs to become an AI

**[0:57]** engineer. The big shift is that more of

**[1:00]** us are going to have little systems that

**[1:01]** do work for us. And if those systems can

**[1:03]** read files and draft messages and maybe

**[1:05]** change code or summarize customers or

**[1:07]** update records, somebody needs to own

**[1:10]** them. Not philosophically, not on an org

**[1:12]** chart, operationally. So, let's make

**[1:15]** this really concrete. Let's say you open

**[1:17]** chat GPT, you can go ahead and do that,

**[1:18]** type a question, get an answer, and then

**[1:20]** you move on about your day. That is an

**[1:22]** assistant interaction. You asked, it

**[1:24]** answered, you decide what to do next.

**[1:26]** Now, let's say you have a custom GPT

**[1:28]** that reads your notes every week, it

**[1:29]** prepares your Monday priorities, it

**[1:31]** follows your rules, and it produces a

**[1:33]** work product you actually use. That is

**[1:35]** close enough to an agent for this

**[1:37]** conversation. Let's say you open Claude

**[1:39]** and ask it to help write a paragraph,

**[1:41]** same thing. That's mostly an assistant.

**[1:42]** But if you have a Claude project with

**[1:44]** files and instructions and examples and

**[1:46]** a repeated job, or if you use Claude

**[1:47]** code to inspect files and make changes

**[1:49]** and issue commands and come back with a

**[1:51]** result, now you're in agent territory.

**[1:53]** And many uses of Codex are very clearly

**[1:55]** in this category. If you give Codex a

**[1:57]** repo and say inspect this code, fix the

**[1:59]** bug, run the test, show me the diff,

**[2:01]** it's doing work across steps with tools

**[2:03]** and real consequences. It may be

**[2:05]** supervised, it may ask for approval, it

**[2:07]** may not be autonomous in the sci-fi

**[2:09]** sense, but it's an agentic workflow. The

**[2:11]** brand name, the word agent, is not the

**[2:13]** point. ChatGPT, Claude, Codex, Cursor, a

**[2:17]** workflow tool, they can all be agents.

**[2:19]** The label doesn't matter, the job does.

**[2:21]** And once you delegate a job, your job of

**[2:25]** owning starts. And I think this is where

**[2:27]** people get tripped up because the AI

**[2:28]** conversation is still obsessed with

**[2:31]** building. Build an agent, make an agent,

**[2:33]** launch an agent, connect tools, automate

**[2:34]** the workflow. And sure that matters. I

**[2:37]** like building. I want people to build.

**[2:39]** But the moment after the initial build

**[2:42]** demo is where your real responsibility

**[2:45]** for that agent over the long term

**[2:47]** begins. Useful agents don't stay in demo

**[2:50]** land on day one and two. They start

**[2:52]** becoming part of how daily work gets

**[2:54]** done for you, for your team. A research

**[2:56]** agent has to find sources you trust

**[2:58]** every single day. A writing agent has to

**[3:01]** work with your voice as it evolves every

**[3:03]** single day. A coding agent changes files

**[3:06]** and has to be trusted to do that. A

**[3:07]** support agent shapes what customers hear

**[3:10]** from the company. That's critical. A

**[3:11]** product agent shapes what shows up in

**[3:13]** the backlog for engineering. And if no

**[3:15]** one owns that agent and feels like they

**[3:18]** have skin in the game, the danger can

**[3:20]** feel ordinary until it's not. The agent

**[3:23]** will use an old policy. Maybe it'll pull

**[3:25]** from stale docs. Maybe it'll repeat a

**[3:26]** bad pattern. Maybe it will draft

**[3:28]** something plausible but wrong and you'll

**[3:30]** say, "Oh, ChatGPT's hallucinating

**[3:32]** again." Maybe it'll turn an assumption

**[3:33]** into a recommendation. And because the

**[3:35]** output looks really clean, people will

**[3:37]** stop noticing where it came from. And

**[3:39]** that's the risk. It's not evil AI, it's

**[3:42]** the unowned work starts to have real

**[3:45]** consequences over time because people

**[3:46]** don't check it and care for it. So, what

**[3:48]** do you do with your agent? I I start

**[3:50]** with four things and I want to keep this

**[3:52]** really, really simple. Give it a job,

**[3:54]** give it a diet, give it boundaries, and

**[3:57]** give it a review loop. The job is what

**[3:59]** this agent is supposed to do. Not help

**[4:01]** with a product on something vague,

**[4:02]** right? Not make me more productive. A

**[4:04]** real job that matters. Like prepare

**[4:06]** first-pass backlog items for refinement.

**[4:08]** Draft refund replies for this ticket

**[4:10]** type. Inspect a pull request for risky

**[4:12]** changes. Build me a weekly research

**[4:14]** brief from these sources. If you can't

**[4:16]** say the job in a sentence, the agent is

**[4:18]** probably too vague. The diet is what the

**[4:21]** agent reads. This matters a lot more

**[4:23]** than people think. Agents eat context,

**[4:25]** right? They eat docs and tickets and

**[4:27]** transcripts and repo instructions and

**[4:28]** examples and whatever else you put in

**[4:30]** front of them. If the diet is stale or

**[4:33]** bloated, the agent can get stale and

**[4:35]** bloated. If the diet is messy, the agent

**[4:37]** can get messy. If the diet uses

**[4:38]** incorrect examples, the agent learns bad

**[4:40]** habits. This is why the little Pokémon

**[4:43]** analogy works so well for me. Collecting

**[4:45]** the Pokémons isn't the point. You have

**[4:47]** to know what each Pokémon is good at.

**[4:50]** You have to know where not to use it.

**[4:52]** You have to know what it has been

**[4:53]** trained on, and you have to notice when

**[4:55]** it starts picking up bad habits. And

**[4:57]** that sounds kind of silly, but the

**[4:59]** responsibility for care is real. And

**[5:01]** then come the boundaries. What can this

**[5:03]** agent touch? Can it read files? Can it

**[5:05]** draft? Can it write to the system? Can

**[5:07]** it send or delete? Can it update Jira?

**[5:09]** These are not the same level of risk. A

**[5:11]** draft-only agent is one thing. An agent

**[5:14]** that can write into a system of record

**[5:16]** is much, much more serious. An agent

**[5:18]** that can send a customer message or

**[5:20]** merge code is in a different category

**[5:22]** entirely. And your sense of ownership

**[5:24]** should move with that. You should feel

**[5:25]** emotional stakes. So, the rule's simple.

**[5:27]** Start with read-only. Start with

**[5:29]** draft-only if you're unsure. Let the

**[5:31]** agent earn more permission, and make

**[5:33]** sure you're comfortable moving outside

**[5:35]** that narrow job. And then the review

**[5:37]** loop is how you keep it healthy. And

**[5:39]** this is one of the phrases people like

**[5:40]** to use: loop, system, workflow. It's

**[5:42]** getting used a lot, and I think it can

**[5:44]** sound more complicated than it is. A

**[5:46]** loop just means the work comes back

**[5:47]** around. The agent runs, a human reviews,

**[5:50]** maybe another agent reviews in some

**[5:51]** cases, mostly a human reviews. You

**[5:53]** notice what was good and what was bad,

**[5:55]** you update the instructions, the

**[5:56]** sources, the permission, the agent runs

**[5:58]** again. There's the loop. It's not magic,

**[6:00]** it's not a giant governance process,

**[6:02]** it's not the best thing since sliced

**[6:03]** bread, it's just a way work gets done

**[6:05]** with agents. Run, review, improve, run

**[6:07]** again. So, let me give you a product

**[6:09]** team version because this is where this

**[6:11]** becomes really obvious with a specific

**[6:12]** example. Imagine a scrum team building a

**[6:15]** new onboarding flow. Every week before

**[6:17]** backlog refinement, someone has to do

**[6:18]** the same messy prep. You read the

**[6:20]** customer tickets, you check the PRD, you

**[6:22]** look at the design changes, you review

**[6:24]** the backlog, you pull the pain, and you

**[6:26]** turn it into acceptance criteria, and

**[6:28]** dependencies, and tickets. It's real

**[6:30]** work. It's a lot of product managers

**[6:31]** weeks. So, the PM starts to build a

**[6:33]** story prep agent to help themselves. And

**[6:35]** the first vision is simple. It's going

**[6:38]** to read the current PRD, the design

**[6:40]** brief, the tagged support tickets, the

**[6:41]** backlog, and a few examples of good

**[6:43]** stories. And then it's going to prepare

**[6:44]** a refinement package. Not final tickets,

**[6:47]** just a package. It's going to say, "Here

**[6:49]** are the candidate stories, here's the

**[6:50]** customer evidence, here are the

**[6:51]** acceptance criteria, here are the

**[6:53]** dependencies, here are the assumptions

**[6:54]** I'm making, and here's the open

**[6:56]** decisions my human needs to make." It's

**[6:58]** a great agent job to start with. You can

**[7:00]** do that in Codex or Claude. But now

**[7:02]** imagine the team starts relying on that

**[7:03]** package every week. It's now a team

**[7:05]** agent. Now the agent is shaping the

**[7:07]** sprint. If the PRD is old, old product

**[7:09]** assumptions are going to enter real

**[7:10]** work. If the support tickets are noisy,

**[7:12]** agent oversight starts to matter. If the

**[7:14]** design changed yesterday and the agent

**[7:16]** didn't pick up on that because of a job

**[7:17]** conflict, that's going to matter. It's

**[7:19]** not going to be an explosion or a robot

**[7:21]** takeover, right? But it's going to be an

**[7:23]** issue for the team. So, what does

**[7:24]** ownership look like in that context? The

**[7:27]** product manager owns the job because the

**[7:28]** product manager owns backlog quality.

**[7:31]** The operating team has to own the

**[7:32]** operating agent. And the maintenance

**[7:34]** loop is not complicated. So, what does

**[7:36]** ownership look like? The product manager

**[7:39]** owns the job and is the single-threaded

**[7:41]** owner that should care about whether the

**[7:42]** agent works or not. That simple. The

**[7:44]** engineering lead can help with technical

**[7:46]** assumptions. The QA team can help with

**[7:48]** testability. The AI team might help with

**[7:50]** tooling in some cases. And the

**[7:52]** maintenance loop for that agent is not

**[7:54]** as complicated as it might sound, even

**[7:56]** though it's an agent that does a lot of

**[7:57]** work. Before refinement, the agent

**[7:59]** prepares the packet, and the PM should

**[8:01]** review that. During refinement, the team

**[8:03]** can notice where it helped and where it

**[8:04]** confused the discussion. After the

**[8:06]** sprint, the owner, the PM, should check

**[8:08]** a few stories. Did engineers have to

**[8:10]** rewrite them? Did QA understand them?

**[8:11]** Did dependencies show up late? If you

**[8:14]** can fix the inputs to the agent and

**[8:16]** change your output, you can fix the

**[8:17]** system. So, remove the stale PRD. Add a

**[8:20]** better example. Change what it is

**[8:21]** allowed to read. That's care and

**[8:23]** feeding. And that's how you go beyond

**[8:25]** prompting and start to work like you're

**[8:27]** in 2026 with agents and loops. Prompting

**[8:29]** is asking. Agent work is giving context

**[8:33]** and care and feeding to the agent so it

**[8:35]** can do its job. There's a big difference

**[8:37]** between asking, "Write acceptance

**[8:39]** criteria for this feature, please." and

**[8:41]** giving an agent a job. The job might

**[8:42]** look like, "Read the PRD, the last 20

**[8:44]** support tickets, the design brief, and

**[8:46]** our three best backlog examples. Draft

**[8:48]** the stories for refinement, attach the

**[8:50]** customer evidence, mark assumptions, and

**[8:52]** don't create Jira tickets. Put

**[8:54]** everything into review so I can look at

**[8:55]** it first." Do you feel that difference?

**[8:58]** One is a prompt, and the PM may feel

**[9:00]** more productive, but it may not hit the

**[9:01]** team. The other is a job with sources

**[9:04]** and boundaries and output and a review

**[9:05]** loop, and it absolutely affects the

**[9:07]** entire team. And this is the move that

**[9:10]** most people need to make in 2026 from

**[9:12]** prompts to jobs. Now, if you're thinking

**[9:14]** about this as a team leader, the

**[9:16]** question becomes bigger, but it doesn't

**[9:17]** need to become more abstract. This is a

**[9:20]** dangerous spot where agents can go

**[9:21]** unowned. Nobody owns the HR agent that

**[9:25]** summarizes performance notes before

**[9:26]** calibration, so nobody tracks whether

**[9:28]** it's pulling from stale manager feedback

**[9:30]** or flattening important context. That's

**[9:32]** a real example, by the way. Nobody owns

**[9:33]** the recruiting agent that drafts

**[9:35]** candidate scorecards, so no one's

**[9:36]** accountable when it drifts. No one knows

**[9:38]** the support triage agent. So, refund

**[9:40]** policy may be stale and may be

**[9:42]** misapplied. You see the same thing

**[9:44]** cropping up all over the business when

**[9:46]** you have projects that parachute in from

**[9:48]** an AI team and that end up unowned in

**[9:52]** those target teams. Finance can have the

**[9:54]** same thing, right? You're going to need

**[9:56]** an agent roster as a team lead. Not a

**[9:58]** big database, right? Just a list of

**[10:00]** agents your team is using. This is our

**[10:02]** story prep agent. This is our release

**[10:04]** note agent. This is our customer call

**[10:05]** summary agent. This is our PR review

**[10:07]** agent. And for each of them, you should

**[10:09]** know who the owner is. You should know

**[10:11]** who what the sources are the agent can

**[10:13]** look at, what the permissions are, the

**[10:14]** review cadence, and the known failure

**[10:16]** modes. And that's it. Because once the

**[10:18]** agent is visible, you can manage it. As

**[10:20]** a team leader, you can manage it. If

**[10:22]** it's invisible, it just becomes this

**[10:23]** weird shadow process where work is

**[10:25]** moving through tools and nobody can

**[10:27]** explain how the output got there. And

**[10:29]** there's these anecdotes that people will

**[10:30]** bring up in performance reviews that say

**[10:32]** an AI native now. That's not productive.

**[10:34]** And I get it. The energy right now is

**[10:36]** build, build, build. But if every

**[10:37]** ambitious person in the company creates

**[10:40]** three agents, you don't necessarily have

**[10:42]** more productivity if you don't scale

**[10:44]** that ownership. I love the build energy.

**[10:47]** It's not bad. It's powerful, but

**[10:48]** powerful things need owners. And if you

**[10:51]** want the simplest version of this,

**[10:54]** here is the owner card that you should

**[10:57]** take with you. For every agent that

**[10:59]** matters, write down the name, the owner,

**[11:02]** the job, the sources, what it can do,

**[11:04]** what it can't do, and the failure mode

**[11:06]** you need to watch for. I said that was a

**[11:08]** spreadsheet for team leaders, but that

**[11:10]** card can also be the agent ownership

**[11:14]** card for individuals. Literally, you can

**[11:17]** make a Slack channel with a bunch of

**[11:19]** agent owner cards where you can say,

**[11:20]** "This is my agent. This is what it

**[11:21]** does." And like people can share them.

**[11:23]** And this is something where if you're

**[11:24]** trying to create agent-to-agent

**[11:26]** collaboration in the company, which a

**[11:27]** lot of people are doing through Slack,

**[11:29]** you kind of need a way for the humans to

**[11:33]** understand what these agents are doing

**[11:35]** at the top and to have almost an agent

**[11:36]** registry so the humans can understand

**[11:38]** what's going on. And yes, this is on

**[11:40]** purpose a little bit like Google's A2A

**[11:42]** protocol. Google's A2A protocol assumes

**[11:45]** that agents need introduction cards like

**[11:46]** that to each other. That's great, but

**[11:49]** what about the humans? We need a sense

**[11:51]** of ownership, almost like a certificate

**[11:54]** for the agent. And I find the companies

**[11:56]** that have that mindset, regardless of

**[11:57]** what they call it, do better because

**[12:00]** they take agent ownership more seriously

**[12:03]** and they should than agent building.

**[12:05]** Just building a new agent, you shouldn't

**[12:07]** get credit for these days.

**[12:09]** Owning an agent and using it to deliver

**[12:11]** value, that's what you should get credit

**[12:12]** for. And I think this is what catching

**[12:14]** up with AI actually looks like today.

**[12:16]** It's not having the most agents. It's

**[12:18]** not knowing every tool. It's not winning

**[12:20]** a vocabulary argument about loops and

**[12:22]** eval's. It's having a small number of

**[12:24]** agents that you own and that deliver

**[12:26]** real value in workflows. You know what

**[12:29]** they do. You know what they eat. You

**[12:31]** know what they can touch. You know how

**[12:32]** you review them. You know when to trust

**[12:34]** them and when not to do. They're your

**[12:36]** pet Pokemons. You know what work you

**[12:38]** delegated and what responsibility you

**[12:40]** kept. This is the grown-up version of

**[12:42]** agent adoption. Ironically, as a child

**[12:45]** of the '80s and '90s, Pokemon prepared

**[12:47]** me well. Prompting was the first skill

**[12:49]** for us, right? Back in 2023, we had to

**[12:51]** learn how to ask better questions. And

**[12:53]** that's still a useful skill because it

**[12:55]** forces us to articulate. Delegation was

**[12:58]** the next skill. We had to learn how to

**[13:00]** hand over real work. That's a very 2025

**[13:02]** thing. Maintenance is a 2026 skill

**[13:05]** because useful agents become our

**[13:08]** responsibility. So, here's your decision

**[13:11]** rule, very easy. If a system can read

**[13:13]** important context, produce work you act

**[13:16]** on or your team acts on, touch a

**[13:17]** workflow other people depend on, it

**[13:20]** needs an owner now. If it's yours, you

**[13:22]** own it. If it belongs to the team, the

**[13:25]** team needs to one person as an owner.

**[13:27]** And if nobody's willing to own it, it

**[13:29]** probably shouldn't be doing important

**[13:31]** work and you should think about

**[13:33]** decommissioning it.

**[13:35]** Look, I put the deeper checklist and the

**[13:37]** owner card and the whole guide for how

**[13:38]** to sort of develop an agent registry at

**[13:41]** the company or frankly for you, your

**[13:44]** Pokémon collection agent set over on

**[13:47]** Substack because that works much better

**[13:49]** as a written guide. But the mental model

**[13:51]** really is this simple. Stop asking only

**[13:53]** whether you can build an agent. Start

**[13:55]** asking whether you can care and feed it.

**[13:58]** Every agent needs an owner. Not because

**[14:00]** agents are bad, because useful agents

**[14:03]** must become part of our work in 2026.

**[14:06]** That is the bar.

**[14:07]** So, take care of your little Pokémon

**[14:09]** agents. I hope this has helped clear up

**[14:11]** a lot of the buzz and the confusion

**[14:15]** around what an agent is and what our job

**[14:17]** is with agents in 2026. I'll see you

**[14:19]** next time.
