# Transcript: Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)

**URL:** https://www.youtube.com/watch?v=zbmuiaPuiNM
**Segments:** 638
**Channel:** Cole Medin
**Duration:** 21:55
**Uploaded:** 2026-06-25

---

## Full Text

So, a new master class on AI coding was just dropped by Google, and it is really good. It's a highle overview of pretty much everything that I teach on my channel. In fact, a couple of people actually sent this to me last week, and they said, "Hey, Cole, this literally looks like it could have been written by you. It's the cleanest packaging I've seen for everything that the industry is converging on right now as far as best practices and terminology for AI coding. It's very well written, definitely worth a read. So, I'll link to it in the description, but it's also 51 pages long, so it takes a while to get through this, which is why I wanted to make this video just to disseminate everything nice and quickly for you. And even if you're already pretty comfortable with agentic engineering and AI coding, it's worth going through this, right? The old adage is you don't truly understand something until you can teach it well. So, it's important to take the instincts you build over time and turn that into a clear visualization, mental model, and precise terminology. And so that's what we really get with this on everything the industry is converging on. And so I've reordered things a little bit what I'll show you here. I think there's a better ordering than what they present. But I want to go through this all with you along with a diagram that I have prepared and just give the good parts to you really fast. So let's get into the meat of it here. So the first big question we have to answer here is what the heck even is an SDLC? If you don't come from a technical background, you're probably not even familiar. And there's the new phrase AIdriven SDLC. that's being thrown around all of the time now. So, it's short for software development life cycle. And quite simply, it's the process to go from idea all the way to production. So, requirement gathering at the start all the way to review, deployment, and maintenance. And so, it's a lot more than just writing the code that sits in the middle. And with a traditional SDLC, you spend a good few days gathering requirements with your stakeholder meetings and the product manager creating the PRD, like all that documentation upfront. And then you have a couple of days of designing and then the implementation is usually what would take most of the time. The engineer spending weeks writing the actual code before you then go into the final steps of testing, reviewing, deploying and maintenance. And usually that would take a week. Obviously, it depends a lot per company. Just a general idea through uh generalization here. And so now with the AIdriven SDLC, the important thing here is that everything we do up front and at the very end, it's not actually that much faster. Now the specification quality is the new bottleneck. And that is so true because there's so much that still has to be human-driven with the validation at the end and the requirement gathering up front. And so really, it's only what's in the middle here. The implementation has gone from 1 to 3 weeks to minutes or hours with AI coding assistance. The same thing is dozens of times faster, especially because agents can iterate with their own system of tests and eval. And so we have the bottleneck at the start and at the end. I firmly believe that a lot of the next $1 billion plus companies are going to be platforms that help speed up the requirements gathering and the validation because we've solved way more for what we have in the middle now. And so that's why you hear so many statistics around like AI coding assistants 10xing the engineers output but not actually 10xing the output of the business is because we're bottlenecked by other parts of software engineering. Software engineering is a lot more than just writing code. But the thing is, as much as you can, you want to remove implementation as the bottleneck because that is still going to save you a considerable amount of time. And so doing that and just generally making everything else in the AIdriven SDLC as fast as possible is what this article focuses on. And so that brings us to the first thing that I want to cover in the diagram. So I took all the big long ideas from the article, made it nice and concise for you here. And so the first thing that they talk about is that AI coding is a spectrum, not a switch. And I really appreciate that because most people think of it as something that's binary. Either you're vibe coding or you're doing agentic engineering. But it is a spectrum depending on the level of your system. And so we'll talk about the system and the harness in a bit. But vibe coding is where you send in a prompt without much planning. And then your validation is, hey, does it seem like it work? Right? like you'll test the application a little bit uh and then you'll just move on to the next iteration. With structured AI assisted, we have more detailed prompts. We're doing more spot-checking and then we get all the way to aentic engineering where we have a entire engineered set of resources and workflows for our AI coding assistant with specs and automated evals and CI gates. So, the agent has a way to really iterate and figure out things that go wrong before you have to correct it. This is where the real power comes in. And so it's not like we always need agentic engineering. Sometimes vibe coding is actually enough for proof of concepts or you just want to create an MVP. I used to just always dismiss vibe coding. But I think there is genuinely a place for it. And so the spectrum Google is saying is not just like you're evolving yourself. It's you pick the right one for the job. It's just agentic engineering is usually where you want to be because this is where you're really creating reliable code. And in the article, Google also has this table that I really appreciate. It makes things nice and concrete. So for each level, what does it look like for these different dimensions? And so for intense specification, for example, which is just how do you communicate upfront what you want. For vibe coding, it's just casual natural language prompts. So you're just describing at a very high level what you're looking for. With structured AI assisted coding, the middle of the spectrum, you're getting more detail, but you still don't really have a workflow for creating formal specs, architecture docs, like when you get to aentic engineering, this is where you really have a repeatable process and you have specifications that are actually engineered just like the code. And then for verification, like we covered this a little bit already, but for Vive coding, it's more does it just seem to work. You're not doing much of a deep dive at all. With structured AI system coding, you're getting a little bit into it with more manual testing and spa-checking of the code maybe. And then for agentic engineering, this is where you have the whole process for the agent to iterate itself with tests and CI/CD gates. Also, LLM judges, you have a separate code review process for yourself and another agent. And I don't need to cover everything here, but getting down to the risk profile with vibe coding, it's high, right? like acceptable for disposable code like I was saying earlier but then if you really want the most reliable code possible that's where you want systematic verification at every stage that comes with aentic engineering okay so if aentic engineering is the way to go most of the time how do we actually do it like what separates aentic engineering from vibe coding and really everything can be wrapped up in the harness so the harness is the set of context rules tools and workflows that you bring into the AI coding assistant. It's the layer that you control. And the big thing that Google is claiming here is that the large language model that you use for your AI coding assistant is only 10% of the system or it only matters 10%. Everything else like your instructions and tools and context and guardrails and orchestration and observability like there's so much here that makes up the other 90%. And that's actually a really good thing because the model is what we don't control. The harness is what we get to create for our specific code bases, architectures, and tech stacks. And it really is true that the industry is converging on a lot of these things. Like we have this article from Anthropic that I covered a couple of weeks ago on my channel, just best practices for using cloud code in general. And one of the headlines that they have here is that the harness matters as much as the model. And so now Google and myself as well were taking this even further to say not only does it matter as much but it actually matters more than the model. Like the model only being 10%. Clearly Google is like okay you need to put your focus on the rest of the harness here. And they also have a very similar definition of what goes into the harness. So cloud code right here they say it's your global rules. It's your hooks like the deterministic actions you want in your life cycle your skills. So, the workflows that you have packaged up, uh, your ways that you search your codebase, the MCP servers, and your sub aents, like these are all of the primitives, as I call them, for working with literally any AI coding assistant. And if we go now into Google's article here, they say the agent is the model plus the harness. And they have this diagram that lays out exactly everything that goes into the harness. And you can see this is where I got the numbers, by the way. So, the model being 10%. So you have the large language model in the middle still matters to an extent because it is the brain. It is the reasoning in your system but everything else around it is a huge deal. So you have your instructions MCP servers guardrails and hooks. I mean everything is the exact same as what anthropic presented in their article. And then the layer above is where you have all of the testing infrastructure. So the eval to iterate itself. And then the top layer is more for you and for production. So the observability and tracing, the scaling, right? Like that's pretty important when you want to take anything an AI coding assistant produces and actually take it all the way to production. The sponsor of today's video is Better DB, a self-tuning Valky/Ris caching and observability platform for AI agents, and it is open-source. So, we're talking all about the AI SDLC in this video, but not covering that much tools we can use to help us with reliability and monitoring in production, that end stage of the SDLC. And better DB is a fantastic example of an AI native tool that can help us with this. So, monitoring our database in production, using our AI coding assistant with it to suggest changes and improvements based on live production data, and a semantic cache to help us scale our database. Let me show you how these things work really quick. My favorite part of Better DB is the semantic cache. Take a look at this. You'll see how it works very quickly. If I ask what's the capital of France, it's not in my Better DB cache yet, so it's a miss. And it calls a model to get the answer. But the next time I ask something that is similar, we get a cache hit. It doesn't even have to be the exact same wording because it's semantic similarity search like traditional rags. So, we get a much faster answer. And we have an MCP server so we can connect our AI coding assistance directly to our better DB cache. So we can ask how it's doing. We can have it suggest improvements and even make those directly. So it's very easy to improve our system over time with the help of AI. And then also we have a dashboard to monitor everything. So we can see how our agent and our cache is performing in production with real user data. And the best part is better DB is open source and free to get started. So I'll have a link in the description. I'd highly recommend them as a tool to help you scale manage your costs for agents you're deploying to production. And so now Google is saying with harness engineering we have the idea of the factory. So instead of the engineer writing the code or the product manager writing the PRD by hand, instead we are responsible for designing the system, creating the harness and then the agent is the one that is actually producing our code and documentation. And so this is more of an investment upfront than vibe coding because we have to create the specs and guardrails, but then we use that to then go into this repeatable system of we plan with the agent, we have it build, and then we have our quality gates at the end for testing and evaling with an iterative loop here for the agent to improve its output autonomously and then get to the point where we have something for us to review and ship. And so this entire thing, we want to delegate all of the coding to the AI coding assistant. Even with agentic engineering, you are delegating all of the coding. So this is not a spectrum of how much do we write by hand versus trust the agent. It is just a spectrum of how evolved of a system do we actually have here. So Google does get a little bit repetitive here because when they talk about the factory model for the first time and what goes into it, it's really the same thing as what goes into building a harness or the AI layer they already talked about. So it's your your context and rules, your test and quality gates, your workflows, your guardrails and your hooks, right? They have a really good visualization for where the developer actually stands in the process. Now, so we define our specs, context, and requirements up front and you use those specs for your planning agent. So every single time you build anything with an AI coding assistant when you're doing agentic engineering is you're going to have one agent that does the plan for the bug fix, for the new feature, whatever it is. And then the guard rails that you design and like the sandboxed environment, that is what's going to be used by the actual coding agent. But it's important here that you do split this into two separate sessions because your planning agent is going to build up a lot of context. You want to avoid context rod and it's going to build up a lot of bias. And so you take the plan as an artifact. You send that into the coding agent and then you do your test and verification and iterate there. And this is also where we can come in the loop to review and approve things ourselves because you definitely fall more into vibe coding if you're not reviewing the output yourself. Even if you do have quite an autonomous system, right? Like even if it's just that pull request at the end for agentic engineering, generally you want a human to be reviewing that before you mark it as pass and you go on to the rest of the process for deployment to production. And throughout this entire workflow, that's where we have our guardrails like token limits and security policies, everything that you are engineering upfront. And the really cool thing about this whole system is that we can make it better over time. Just like we evolve our codebase over time, we can evolve our system. So I I call this the system evolution mindset. Whenever you encounter an issue with your AI coding assistant, like something comes up here where it has to iterate more than you would want or you have to step in before you ship, instead of just fixing the bug and moving on, you actually talk to your coding agent like you have it do some retrospection and say, "Hey, where could we make our workflows or our rules like any part of our AI layer better so that issue is less likely to come up again?" And so that way every single time you go through this process over and over and over again, you're making it more and more reliable. And the harness is worth investing your time into. Like it it really is the 90%. I mean, there's a lot of studies that are done like terminal bench 2.0. It's one of the biggest benchmarks we have out there. Like every single time a new model comes out, this is one of the percentages that you see. There's a lot of studies done where like they were able to take a model from outside the top 30 into the top five just by creating an AI layer of rules and workflows for it to run through the things you usually test for the benchmark. Lane chain was able to increase it 13.7 points. Like that's the difference between Sonnet and Opus. Like you can make sonnet work as well as Opus if you have the right system, the right process that you're having it go through as the harness. So if the harness is the most important part of agentic engineering, then it's clear that the most important skill within that is how do we engineer each of the individual components of the harness like our rules, workflows, and a guard rails. And so we've covered the different components already, but a key delineation that Google makes here that I really like is the static context versus dynamic context. And this is really important because it's all about context management. Context is your most precious resource when working with AI coding assistants, both for the sake of cost and avoiding context rot. We don't want to fill the window of our LLM, our coding agent, too much because LLMs get overwhelmed with information just like people do. And so nice visualization here. They talk about what goes into static versus dynamic. So static context is things like your rules and core guardrails, the system prompt. It's loaded into the coding agent session guaranteed every single time. time. That makes it reliable because the agent doesn't have to seek out this information, but it's expensive because you're filling the context window up front. And so, it's important to have at least some rules and guard rails up front, but you want to make them very lean. And then everything else goes in dynamic context so it's efficient and scalable because it's information that the agent has to actually seek out. Like you might have an an agent skill for planning like it loads that skill when you want it to do the planning workflow or you have conventions for a part of the codebase you want it to load when it operates on that part of the codebase and so it's very scalable so you're not shoving it into the context up front but the risk there is the agent might not grab for that context when it should like it might not load the skill or perform the rag search when you would hope it to or when it would be optimal to do so. But large language models are getting better and better at relying on dynamic context and loading it when it should. And so like agent skills are becoming very very important right now, right? So they say rather than embedding every piece of specialized knowledge into the agent system prompt, skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure. And this is so important because the underlying lesson here is that we really only need one agent for everything and then we can make it specialized with our skills, i.e. our workflows. And so something that people used to do way too much before is they would have these really complicated multi- aent systems with all these specialists or they use a ton of these specialized sub aents they would create. And really the industry is moving away from that because we can just have one generalist agent that we make specific with the skills that we have at load. Like we can have it become a code reviewer or become a planner. That session can turn into the specialization that you need thanks to dynamic context. So keep it simple. You really only need one agent to drive most of your agentic engineering. Okay. So the article has been very valuepacked already. There's just two more things that I want to cover with you here. I want to talk about your role as the conductor and orchestrator and then also the token economics. And so an interesting thing that Google presents here is the idea of you as the engineer are going to move between two modes as you're using your AI coding assistant. And so the conductor is more how we used AI coding assistants when generative AI was first a thing. Like we had our tab complete. We're still steering every move, working in individual files. That's the conductor. The orchestrator is a lot of what people have been focusing on more recently where we have a coding agent handling much larger tasks spanning entire code bases, maybe even multiple code bases. We're reviewing the outcomes instead of changes to individual files. We have agents running in parallel. We're really scaling our output with AI coding assistance here. And almost everybody is focusing entirely on this. And this this is like the one part of the article I don't know if I agree with Google because they're saying that you actually want to move between both. Like there's still a time and place to be micromanaging the AI coding assistant at a single file level. Honestly, I don't know if I agree with this. I think when you build the harness to be reliable enough and you're confident in your rules and workflows, you can always live at this level. But they do make some interesting arguments where it's like any kind of like deeper debugging you have to do or just initial exploration like you are going to get very granular with the coding agent because that's the times where you might need to really be in the loop and guide it. So I think there's a time and place for it but I feel like when you have the right system and it's working well for you, you don't really like you kind of graduate from being the conductor. I don't think you're always moving between the two. But it is an interesting idea you know especially as an organization when you have a lot of traditional engineers and you're first getting into aentic engineering I think it is good to have this mental model just until you have the system developed where you'd graduate to only ever staying here. Cool. And then the very last thing that I want to cover here is the token economics. I really love how they frame things here. So, like we said, vibe coding, you don't always want to avoid it, but there is a big cost that comes if you lean on it too much because at first when you're first adopting AI coding assistance for yourself or a company, Vive coding is going to be cheaper. It's lower capital expenditure because you don't have to dedicate yourself or a team to design the initial harness. But the problem is it's very high operational expenditure because you start burning through millions and millions of tokens iterating on slop code because you don't have a system for your AI coding assistant to follow your workflow and your conventions. And so agentic engineering it has that high capital expenditure because you have to dedicate your time up front or you have to like in a larger organization usually you create a smaller forward deployed engineer team to build up that harness to then scale to the entire organization. So you're dedicating manpower to build something initially, but then it scales extremely well because the output of your AI coding assistants are better and better and better over time and you have that grounding in a system that you just build once upfront and evolve over time. So high capital expenditure but then low operational expenditure and you know you have that crossover that you reach extremely quickly like you want to just take the dive and build that system up front because yeah you're going to get to the point where agentic engineering is three to 10 times more reliable and cheaper than vibe coding because you're not burning through millions of tokens. So there you go. That is everything you need to know at a high level for the new AIdriven software development life cycle. It is worth building that harness and investing in it. It is an engineered resource that lives in version control just like the code itself. So, I hope that you found this useful. Let me know in the comments what kinds of content you want me to create to expand on any of these ideas here cuz this is my bread and butter. If you appreciated this video, you're looking forward to more things on Agentic Engineering, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.

---

## Timestamped Segments

**[0:00]** So, a new master class on AI coding was

**[0:02]** just dropped by Google, and it is really

**[0:06]** good. It's a highle overview of pretty

**[0:08]** much everything that I teach on my

**[0:10]** channel. In fact, a couple of people

**[0:11]** actually sent this to me last week, and

**[0:13]** they said, "Hey, Cole, this literally

**[0:14]** looks like it could have been written by

**[0:16]** you. It's the cleanest packaging I've

**[0:19]** seen for everything that the industry is

**[0:22]** converging on right now as far as best

**[0:24]** practices and terminology for AI coding.

**[0:27]** It's very well written, definitely worth

**[0:28]** a read. So, I'll link to it in the

**[0:30]** description, but it's also 51 pages

**[0:33]** long, so it takes a while to get through

**[0:34]** this, which is why I wanted to make this

**[0:36]** video just to disseminate everything

**[0:38]** nice and quickly for you. And even if

**[0:40]** you're already pretty comfortable with

**[0:42]** agentic engineering and AI coding, it's

**[0:44]** worth going through this, right? The old

**[0:46]** adage is you don't truly understand

**[0:48]** something until you can teach it well.

**[0:49]** So, it's important to take the instincts

**[0:51]** you build over time and turn that into a

**[0:54]** clear visualization, mental model, and

**[0:56]** precise terminology. And so that's what

**[0:58]** we really get with this on everything

**[1:00]** the industry is converging on. And so

**[1:02]** I've reordered things a little bit what

**[1:04]** I'll show you here. I think there's a

**[1:05]** better ordering than what they present.

**[1:07]** But I want to go through this all with

**[1:08]** you along with a diagram that I have

**[1:10]** prepared and just give the good parts to

**[1:13]** you really fast. So let's get into the

**[1:15]** meat of it here. So the first big

**[1:17]** question we have to answer here is what

**[1:19]** the heck even is an SDLC? If you don't

**[1:21]** come from a technical background, you're

**[1:23]** probably not even familiar. And there's

**[1:24]** the new phrase AIdriven SDLC. that's

**[1:27]** being thrown around all of the time now.

**[1:30]** So, it's short for software development

**[1:32]** life cycle. And quite simply, it's the

**[1:34]** process to go from idea all the way to

**[1:36]** production. So, requirement gathering at

**[1:38]** the start all the way to review,

**[1:40]** deployment, and maintenance. And so,

**[1:41]** it's a lot more than just writing the

**[1:43]** code that sits in the middle. And with a

**[1:46]** traditional SDLC, you spend a good few

**[1:49]** days gathering requirements with your

**[1:50]** stakeholder meetings and the product

**[1:52]** manager creating the PRD, like all that

**[1:54]** documentation upfront. And then you have

**[1:56]** a couple of days of designing and then

**[1:58]** the implementation is usually what would

**[2:00]** take most of the time. The engineer

**[2:02]** spending weeks writing the actual code

**[2:05]** before you then go into the final steps

**[2:07]** of testing, reviewing, deploying and

**[2:09]** maintenance. And usually that would take

**[2:10]** a week. Obviously, it depends a lot per

**[2:13]** company. Just a general idea through uh

**[2:15]** generalization here. And so now with the

**[2:18]** AIdriven SDLC, the important thing here

**[2:20]** is that everything we do up front and at

**[2:23]** the very end, it's not actually that

**[2:25]** much faster. Now the specification

**[2:27]** quality is the new bottleneck. And that

**[2:30]** is so true because there's so much that

**[2:32]** still has to be human-driven with the

**[2:34]** validation at the end and the

**[2:37]** requirement gathering up front. And so

**[2:39]** really, it's only what's in the middle

**[2:40]** here. The implementation has gone from 1

**[2:43]** to 3 weeks to minutes or hours with AI

**[2:47]** coding assistance. The same thing is

**[2:49]** dozens of times faster, especially

**[2:51]** because agents can iterate with their

**[2:53]** own system of tests and eval.

**[2:57]** And so we have the bottleneck at the

**[2:58]** start and at the end. I firmly believe

**[3:01]** that a lot of the next $1 billion plus

**[3:03]** companies are going to be platforms that

**[3:05]** help speed up the requirements gathering

**[3:08]** and the validation because we've solved

**[3:11]** way more for what we have in the middle

**[3:13]** now. And so that's why you hear so many

**[3:15]** statistics around like AI coding

**[3:17]** assistants 10xing the engineers output

**[3:19]** but not actually 10xing the output of

**[3:21]** the business is because we're

**[3:22]** bottlenecked by other parts of software

**[3:24]** engineering. Software engineering is a

**[3:26]** lot more than just writing code. But the

**[3:29]** thing is, as much as you can, you want

**[3:31]** to remove implementation as the

**[3:33]** bottleneck because that is still going

**[3:34]** to save you a considerable amount of

**[3:36]** time. And so doing that and just

**[3:38]** generally making everything else in the

**[3:39]** AIdriven SDLC as fast as possible is

**[3:42]** what this article focuses on. And so

**[3:44]** that brings us to the first thing that I

**[3:47]** want to cover in the diagram. So I took

**[3:48]** all the big long ideas from the article,

**[3:51]** made it nice and concise for you here.

**[3:53]** And so the first thing that they talk

**[3:55]** about is that AI coding is a spectrum,

**[3:58]** not a switch. And I really appreciate

**[4:00]** that because most people think of it as

**[4:01]** something that's binary. Either you're

**[4:03]** vibe coding or you're doing agentic

**[4:05]** engineering. But it is a spectrum

**[4:08]** depending on the level of your system.

**[4:11]** And so we'll talk about the system and

**[4:13]** the harness in a bit. But vibe coding is

**[4:16]** where you send in a prompt without much

**[4:18]** planning. And then your validation is,

**[4:20]** hey, does it seem like it work? Right?

**[4:22]** like you'll test the application a

**[4:23]** little bit uh and then you'll just move

**[4:25]** on to the next iteration. With

**[4:27]** structured AI assisted, we have more

**[4:29]** detailed prompts. We're doing more

**[4:31]** spot-checking and then we get all the

**[4:32]** way to aentic engineering where we have

**[4:34]** a entire engineered set of resources and

**[4:38]** workflows for our AI coding assistant

**[4:41]** with specs and automated evals and CI

**[4:43]** gates. So, the agent has a way to really

**[4:45]** iterate and figure out things that go

**[4:46]** wrong before you have to correct it.

**[4:49]** This is where the real power comes in.

**[4:51]** And so it's not like we always need

**[4:53]** agentic engineering. Sometimes vibe

**[4:55]** coding is actually enough for proof of

**[4:57]** concepts or you just want to create an

**[4:59]** MVP. I used to just always dismiss vibe

**[5:03]** coding. But I think there is genuinely a

**[5:04]** place for it. And so the spectrum Google

**[5:07]** is saying is not just like you're

**[5:08]** evolving yourself. It's you pick the

**[5:11]** right one for the job. It's just agentic

**[5:13]** engineering is usually where you want to

**[5:15]** be because this is where you're really

**[5:16]** creating reliable code. And in the

**[5:19]** article, Google also has this table that

**[5:21]** I really appreciate. It makes things

**[5:22]** nice and concrete. So for each level,

**[5:24]** what does it look like for these

**[5:26]** different dimensions? And so for intense

**[5:28]** specification, for example, which is

**[5:30]** just how do you communicate upfront what

**[5:32]** you want. For vibe coding, it's just

**[5:34]** casual natural language prompts. So

**[5:36]** you're just describing at a very high

**[5:38]** level what you're looking for. With

**[5:39]** structured AI assisted coding, the

**[5:41]** middle of the spectrum, you're getting

**[5:43]** more detail, but you still don't really

**[5:44]** have a workflow for creating formal

**[5:47]** specs, architecture docs, like when you

**[5:48]** get to aentic engineering, this is where

**[5:50]** you really have a repeatable process and

**[5:53]** you have specifications that are

**[5:54]** actually engineered just like the code.

**[5:57]** And then for verification, like we

**[5:58]** covered this a little bit already, but

**[6:00]** for Vive coding, it's more does it just

**[6:01]** seem to work. You're not doing much of a

**[6:03]** deep dive at all. With structured AI

**[6:05]** system coding, you're getting a little

**[6:06]** bit into it with more manual testing and

**[6:08]** spa-checking of the code maybe. And then

**[6:11]** for agentic engineering, this is where

**[6:12]** you have the whole process for the agent

**[6:14]** to iterate itself with tests and CI/CD

**[6:17]** gates. Also, LLM judges, you have a

**[6:19]** separate code review process for

**[6:20]** yourself and another agent. And I don't

**[6:23]** need to cover everything here, but

**[6:25]** getting down to the risk profile with

**[6:27]** vibe coding, it's high, right? like

**[6:29]** acceptable for disposable code like I

**[6:32]** was saying earlier but then if you

**[6:34]** really want the most reliable code

**[6:36]** possible that's where you want

**[6:38]** systematic verification at every stage

**[6:40]** that comes with aentic engineering okay

**[6:43]** so if aentic engineering is the way to

**[6:45]** go most of the time how do we actually

**[6:47]** do it like what separates aentic

**[6:50]** engineering from vibe coding and really

**[6:53]** everything can be wrapped up in the

**[6:54]** harness so the harness is the set of

**[6:58]** context rules tools and workflows that

**[7:00]** you bring into the AI coding assistant.

**[7:03]** It's the layer that you control. And the

**[7:06]** big thing that Google is claiming here

**[7:08]** is that the large language model that

**[7:10]** you use for your AI coding assistant is

**[7:13]** only 10% of the system or it only

**[7:16]** matters 10%.

**[7:18]** Everything else like your instructions

**[7:20]** and tools and context and guardrails and

**[7:22]** orchestration and observability like

**[7:24]** there's so much here that makes up the

**[7:26]** other 90%. And that's actually a really

**[7:28]** good thing because the model is what we

**[7:31]** don't control. The harness is what we

**[7:33]** get to create for our specific code

**[7:35]** bases, architectures, and tech stacks.

**[7:38]** And it really is true that the industry

**[7:40]** is converging on a lot of these things.

**[7:42]** Like we have this article from Anthropic

**[7:44]** that I covered a couple of weeks ago on

**[7:45]** my channel, just best practices for

**[7:48]** using cloud code in general. And one of

**[7:50]** the headlines that they have here is

**[7:52]** that the harness matters as much as the

**[7:54]** model. And so now Google and myself as

**[7:57]** well were taking this even further to

**[7:59]** say not only does it matter as much but

**[8:01]** it actually matters more than the model.

**[8:03]** Like the model only being 10%. Clearly

**[8:05]** Google is like okay you need to put your

**[8:07]** focus on the rest of the harness here.

**[8:10]** And they also have a very similar

**[8:12]** definition of what goes into the

**[8:14]** harness. So cloud code right here they

**[8:16]** say it's your global rules. It's your

**[8:18]** hooks like the deterministic actions you

**[8:20]** want in your life cycle your skills. So,

**[8:22]** the workflows that you have packaged up,

**[8:24]** uh, your ways that you search your

**[8:26]** codebase, the MCP servers, and your sub

**[8:28]** aents, like these are all of the

**[8:30]** primitives, as I call them, for working

**[8:32]** with literally any AI coding assistant.

**[8:35]** And if we go now into Google's article

**[8:37]** here, they say the agent is the model

**[8:39]** plus the harness. And they have this

**[8:41]** diagram that lays out exactly everything

**[8:43]** that goes into the harness. And you can

**[8:45]** see this is where I got the numbers, by

**[8:47]** the way. So, the model being 10%. So you

**[8:49]** have the large language model in the

**[8:51]** middle still matters to an extent

**[8:52]** because it is the brain. It is the

**[8:54]** reasoning in your system but everything

**[8:56]** else around it is a huge deal. So you

**[8:58]** have your instructions MCP servers

**[9:01]** guardrails and hooks. I mean everything

**[9:03]** is the exact same as what anthropic

**[9:05]** presented in their article. And then the

**[9:07]** layer above is where you have all of the

**[9:09]** testing infrastructure. So the eval

**[9:12]** to iterate itself. And then the top

**[9:14]** layer is more for you and for

**[9:16]** production. So the observability and

**[9:18]** tracing, the scaling, right? Like that's

**[9:21]** pretty important when you want to take

**[9:23]** anything an AI coding assistant produces

**[9:25]** and actually take it all the way to

**[9:26]** production. The sponsor of today's video

**[9:29]** is Better DB, a self-tuning Valky/Ris

**[9:32]** caching and observability platform for

**[9:35]** AI agents, and it is open-source. So,

**[9:38]** we're talking all about the AI SDLC in

**[9:40]** this video, but not covering that much

**[9:42]** tools we can use to help us with

**[9:44]** reliability and monitoring in

**[9:46]** production, that end stage of the SDLC.

**[9:49]** And better DB is a fantastic example of

**[9:52]** an AI native tool that can help us with

**[9:54]** this. So, monitoring our database in

**[9:56]** production, using our AI coding

**[9:58]** assistant with it to suggest changes and

**[10:01]** improvements based on live production

**[10:03]** data, and a semantic cache to help us

**[10:05]** scale our database. Let me show you how

**[10:07]** these things work really quick. My

**[10:09]** favorite part of Better DB is the

**[10:10]** semantic cache. Take a look at this.

**[10:12]** You'll see how it works very quickly. If

**[10:14]** I ask what's the capital of France, it's

**[10:16]** not in my Better DB cache yet, so it's a

**[10:18]** miss. And it calls a model to get the

**[10:19]** answer. But the next time I ask

**[10:20]** something that is similar, we get a

**[10:22]** cache hit. It doesn't even have to be

**[10:24]** the exact same wording because it's

**[10:26]** semantic similarity search like

**[10:27]** traditional rags. So, we get a much

**[10:30]** faster answer. And we have an MCP server

**[10:32]** so we can connect our AI coding

**[10:34]** assistance directly to our better DB

**[10:37]** cache. So we can ask how it's doing. We

**[10:39]** can have it suggest improvements and

**[10:40]** even make those directly. So it's very

**[10:42]** easy to improve our system over time

**[10:44]** with the help of AI. And then also we

**[10:46]** have a dashboard to monitor everything.

**[10:48]** So we can see how our agent and our

**[10:50]** cache is performing in production with

**[10:52]** real user data. And the best part is

**[10:54]** better DB is open source and free to get

**[10:56]** started. So I'll have a link in the

**[10:58]** description. I'd highly recommend them

**[10:59]** as a tool to help you scale manage your

**[11:01]** costs for agents you're deploying to

**[11:03]** production. And so now Google is saying

**[11:05]** with harness engineering we have the

**[11:07]** idea of the factory. So instead of the

**[11:09]** engineer writing the code or the product

**[11:11]** manager writing the PRD by hand, instead

**[11:14]** we are responsible for designing the

**[11:16]** system, creating the harness and then

**[11:18]** the agent is the one that is actually

**[11:20]** producing our code and documentation.

**[11:23]** And so this is more of an investment

**[11:25]** upfront than vibe coding because we have

**[11:26]** to create the specs and guardrails, but

**[11:28]** then we use that to then go into this

**[11:30]** repeatable system of we plan with the

**[11:32]** agent, we have it build, and then we

**[11:34]** have our quality gates at the end for

**[11:35]** testing and evaling with an iterative

**[11:37]** loop here for the agent to improve its

**[11:39]** output autonomously and then get to the

**[11:41]** point where we have something for us to

**[11:42]** review and ship. And so this entire

**[11:45]** thing, we want to delegate all of the

**[11:47]** coding to the AI coding assistant. Even

**[11:50]** with agentic engineering, you are

**[11:51]** delegating all of the coding. So this is

**[11:53]** not a spectrum of how much do we write

**[11:56]** by hand versus trust the agent. It is

**[11:58]** just a spectrum of how evolved of a

**[12:00]** system do we actually have here. So

**[12:02]** Google does get a little bit repetitive

**[12:04]** here because when they talk about the

**[12:06]** factory model for the first time and

**[12:07]** what goes into it, it's really the same

**[12:09]** thing as what goes into building a

**[12:10]** harness or the AI layer they already

**[12:12]** talked about. So it's your your context

**[12:14]** and rules, your test and quality gates,

**[12:16]** your workflows, your guardrails and your

**[12:17]** hooks, right? They have a really good

**[12:19]** visualization for where the developer

**[12:21]** actually stands in the process. Now, so

**[12:23]** we define our specs, context, and

**[12:25]** requirements up front and you use those

**[12:27]** specs for your planning agent. So every

**[12:29]** single time you build anything with an

**[12:31]** AI coding assistant when you're doing

**[12:33]** agentic engineering is you're going to

**[12:35]** have one agent that does the plan for

**[12:37]** the bug fix, for the new feature,

**[12:39]** whatever it is. And then the guard rails

**[12:41]** that you design and like the sandboxed

**[12:43]** environment, that is what's going to be

**[12:44]** used by the actual coding agent. But

**[12:46]** it's important here that you do split

**[12:49]** this into two separate sessions because

**[12:51]** your planning agent is going to build up

**[12:53]** a lot of context. You want to avoid

**[12:55]** context rod and it's going to build up a

**[12:57]** lot of bias. And so you take the plan as

**[12:59]** an artifact. You send that into the

**[13:01]** coding agent and then you do your test

**[13:02]** and verification and iterate there. And

**[13:04]** this is also where we can come in the

**[13:05]** loop to review and approve things

**[13:07]** ourselves because you definitely fall

**[13:09]** more into vibe coding if you're not

**[13:12]** reviewing the output yourself. Even if

**[13:14]** you do have quite an autonomous system,

**[13:16]** right? Like even if it's just that pull

**[13:17]** request at the end for agentic

**[13:19]** engineering, generally you want a human

**[13:21]** to be reviewing that before you mark it

**[13:23]** as pass and you go on to the rest of the

**[13:25]** process for deployment to production.

**[13:28]** And throughout this entire workflow,

**[13:30]** that's where we have our guardrails like

**[13:32]** token limits and security policies,

**[13:34]** everything that you are engineering

**[13:36]** upfront. And the really cool thing about

**[13:39]** this whole system is that we can make it

**[13:42]** better over time. Just like we evolve

**[13:44]** our codebase over time, we can evolve

**[13:45]** our system. So I I call this the system

**[13:47]** evolution mindset. Whenever you

**[13:49]** encounter an issue with your AI coding

**[13:51]** assistant, like something comes up here

**[13:53]** where it has to iterate more than you

**[13:55]** would want or you have to step in before

**[13:56]** you ship, instead of just fixing the bug

**[13:58]** and moving on, you actually talk to your

**[14:01]** coding agent like you have it do some

**[14:02]** retrospection and say, "Hey, where could

**[14:04]** we make our workflows or our rules like

**[14:07]** any part of our AI layer better so that

**[14:09]** issue is less likely to come up again?"

**[14:11]** And so that way every single time you go

**[14:13]** through this process over and over and

**[14:15]** over again, you're making it more and

**[14:17]** more reliable. And the harness is worth

**[14:20]** investing your time into. Like it it

**[14:22]** really is the 90%. I mean, there's a lot

**[14:24]** of studies that are done like terminal

**[14:26]** bench 2.0. It's one of the biggest

**[14:28]** benchmarks we have out there. Like every

**[14:30]** single time a new model comes out, this

**[14:32]** is one of the percentages that you see.

**[14:34]** There's a lot of studies done where like

**[14:35]** they were able to take a model from

**[14:37]** outside the top 30 into the top five

**[14:40]** just by creating an AI layer of rules

**[14:43]** and workflows for it to run through the

**[14:45]** things you usually test for the

**[14:46]** benchmark. Lane chain was able to

**[14:48]** increase it 13.7 points. Like that's the

**[14:50]** difference between Sonnet and Opus. Like

**[14:53]** you can make sonnet work as well as Opus

**[14:56]** if you have the right system, the right

**[14:58]** process that you're having it go through

**[15:00]** as the harness. So if the harness is the

**[15:03]** most important part of agentic

**[15:05]** engineering, then it's clear that the

**[15:07]** most important skill within that is how

**[15:09]** do we engineer each of the individual

**[15:11]** components of the harness like our

**[15:13]** rules, workflows, and a guard rails. And

**[15:15]** so we've covered the different

**[15:16]** components already, but a key

**[15:18]** delineation that Google makes here that

**[15:19]** I really like is the static context

**[15:22]** versus dynamic context. And this is

**[15:25]** really important because it's all about

**[15:27]** context management. Context is your most

**[15:30]** precious resource when working with AI

**[15:32]** coding assistants, both for the sake of

**[15:34]** cost and avoiding context rot. We don't

**[15:36]** want to fill the window of our LLM, our

**[15:39]** coding agent, too much because LLMs get

**[15:42]** overwhelmed with information just like

**[15:44]** people do. And so nice visualization

**[15:46]** here. They talk about what goes into

**[15:48]** static versus dynamic. So static context

**[15:51]** is things like your rules and core

**[15:53]** guardrails, the system prompt. It's

**[15:55]** loaded into the coding agent session

**[15:56]** guaranteed every single time. time. That

**[15:58]** makes it reliable because the agent

**[16:00]** doesn't have to seek out this

**[16:01]** information, but it's expensive because

**[16:03]** you're filling the context window up

**[16:05]** front. And so, it's important to have at

**[16:07]** least some rules and guard rails up

**[16:09]** front, but you want to make them very

**[16:10]** lean. And then everything else goes in

**[16:13]** dynamic context so it's efficient and

**[16:15]** scalable because it's information that

**[16:16]** the agent has to actually seek out. Like

**[16:19]** you might have an an agent skill for

**[16:21]** planning like it loads that skill when

**[16:23]** you want it to do the planning workflow

**[16:24]** or you have conventions for a part of

**[16:26]** the codebase you want it to load when it

**[16:28]** operates on that part of the codebase

**[16:29]** and so it's very scalable so you're not

**[16:31]** shoving it into the context up front but

**[16:33]** the risk there is the agent might not

**[16:35]** grab for that context when it should

**[16:38]** like it might not load the skill or

**[16:39]** perform the rag search when you would

**[16:41]** hope it to or when it would be optimal

**[16:43]** to do so. But large language models are

**[16:46]** getting better and better at relying on

**[16:49]** dynamic context and loading it when it

**[16:51]** should. And so like agent skills are

**[16:52]** becoming very very important right now,

**[16:55]** right? So they say rather than embedding

**[16:56]** every piece of specialized knowledge

**[16:58]** into the agent system prompt, skills

**[17:00]** allow the agent to remain a lightweight

**[17:03]** generalist that flexes into specialist

**[17:05]** roles on demand through progressive

**[17:07]** disclosure. And this is so important

**[17:09]** because the underlying lesson here is

**[17:12]** that we really only need one agent for

**[17:14]** everything and then we can make it

**[17:16]** specialized with our skills, i.e. our

**[17:18]** workflows. And so something that people

**[17:20]** used to do way too much before is they

**[17:22]** would have these really complicated

**[17:24]** multi- aent systems with all these

**[17:26]** specialists or they use a ton of these

**[17:27]** specialized sub aents they would create.

**[17:29]** And really the industry is moving away

**[17:31]** from that because we can just have one

**[17:34]** generalist agent that we make specific

**[17:37]** with the skills that we have at load.

**[17:39]** Like we can have it become a code

**[17:40]** reviewer or become a planner. That

**[17:42]** session can turn into the specialization

**[17:44]** that you need thanks to dynamic context.

**[17:47]** So keep it simple. You really only need

**[17:49]** one agent to drive most of your agentic

**[17:52]** engineering. Okay. So the article has

**[17:54]** been very valuepacked already. There's

**[17:56]** just two more things that I want to

**[17:57]** cover with you here. I want to talk

**[17:59]** about your role as the conductor and

**[18:00]** orchestrator and then also the token

**[18:03]** economics. And so an interesting thing

**[18:05]** that Google presents here is the idea of

**[18:07]** you as the engineer are going to move

**[18:10]** between two modes as you're using your

**[18:13]** AI coding assistant. And so the

**[18:15]** conductor is more how we used AI coding

**[18:18]** assistants when generative AI was first

**[18:20]** a thing. Like we had our tab complete.

**[18:22]** We're still steering every move, working

**[18:24]** in individual files. That's the

**[18:26]** conductor. The orchestrator is a lot of

**[18:28]** what people have been focusing on more

**[18:30]** recently where we have a coding agent

**[18:32]** handling much larger tasks spanning

**[18:34]** entire code bases, maybe even multiple

**[18:37]** code bases. We're reviewing the outcomes

**[18:39]** instead of changes to individual files.

**[18:41]** We have agents running in parallel.

**[18:43]** We're really scaling our output with AI

**[18:45]** coding assistance here. And almost

**[18:47]** everybody is focusing entirely on this.

**[18:50]** And this this is like the one part of

**[18:51]** the article I don't know if I agree with

**[18:53]** Google because they're saying that you

**[18:54]** actually want to move between both. Like

**[18:56]** there's still a time and place to be

**[18:58]** micromanaging the AI coding assistant at

**[19:01]** a single file level. Honestly, I don't

**[19:04]** know if I agree with this. I think when

**[19:06]** you build the harness to be reliable

**[19:08]** enough and you're confident in your

**[19:09]** rules and workflows, you can always live

**[19:12]** at this level. But they do make some

**[19:15]** interesting arguments where it's like

**[19:16]** any kind of like deeper debugging you

**[19:18]** have to do or just initial exploration

**[19:20]** like you are going to get very granular

**[19:22]** with the coding agent because that's the

**[19:23]** times where you might need to really be

**[19:25]** in the loop and guide it. So I think

**[19:27]** there's a time and place for it but I

**[19:29]** feel like when you have the right system

**[19:30]** and it's working well for you, you don't

**[19:32]** really like you kind of graduate from

**[19:34]** being the conductor. I don't think

**[19:35]** you're always moving between the two.

**[19:37]** But it is an interesting idea you know

**[19:39]** especially as an organization when you

**[19:41]** have a lot of traditional engineers and

**[19:43]** you're first getting into aentic

**[19:45]** engineering I think it is good to have

**[19:47]** this mental model just until you have

**[19:49]** the system developed where you'd

**[19:50]** graduate to only ever staying here.

**[19:52]** Cool. And then the very last thing that

**[19:54]** I want to cover here is the token

**[19:55]** economics. I really love how they frame

**[19:57]** things here. So, like we said, vibe

**[20:00]** coding, you don't always want to avoid

**[20:02]** it, but there is a big cost that comes

**[20:04]** if you lean on it too much because at

**[20:06]** first when you're first adopting AI

**[20:08]** coding assistance for yourself or a

**[20:10]** company, Vive coding is going to be

**[20:12]** cheaper. It's lower capital expenditure

**[20:14]** because you don't have to dedicate

**[20:15]** yourself or a team to design the initial

**[20:18]** harness. But the problem is it's very

**[20:20]** high operational expenditure because you

**[20:22]** start burning through millions and

**[20:23]** millions of tokens iterating on slop

**[20:26]** code because you don't have a system for

**[20:28]** your AI coding assistant to follow your

**[20:30]** workflow and your conventions. And so

**[20:33]** agentic engineering it has that high

**[20:35]** capital expenditure because you have to

**[20:37]** dedicate your time up front or you have

**[20:39]** to like in a larger organization usually

**[20:41]** you create a smaller forward deployed

**[20:42]** engineer team to build up that harness

**[20:45]** to then scale to the entire

**[20:46]** organization. So you're dedicating

**[20:48]** manpower to build something initially,

**[20:50]** but then it scales extremely well

**[20:52]** because the output of your AI coding

**[20:53]** assistants are better and better and

**[20:55]** better over time and you have that

**[20:57]** grounding in a system that you just

**[20:58]** build once upfront and evolve over time.

**[21:01]** So high capital expenditure but then low

**[21:04]** operational expenditure and you know you

**[21:07]** have that crossover that you reach

**[21:08]** extremely quickly like you want to just

**[21:10]** take the dive and build that system up

**[21:12]** front because yeah you're going to get

**[21:15]** to the point where agentic engineering

**[21:16]** is three to 10 times more reliable and

**[21:18]** cheaper than vibe coding because you're

**[21:20]** not burning through millions of tokens.

**[21:23]** So there you go. That is everything you

**[21:24]** need to know at a high level for the new

**[21:26]** AIdriven software development life

**[21:28]** cycle. It is worth building that harness

**[21:31]** and investing in it. It is an engineered

**[21:33]** resource that lives in version control

**[21:35]** just like the code itself. So, I hope

**[21:38]** that you found this useful. Let me know

**[21:39]** in the comments what kinds of content

**[21:41]** you want me to create to expand on any

**[21:42]** of these ideas here cuz this is my bread

**[21:45]** and butter. If you appreciated this

**[21:47]** video, you're looking forward to more

**[21:48]** things on Agentic Engineering, I would

**[21:50]** really appreciate a like and a

**[21:52]** subscribe. And with that, I will see you

**[21:54]** in the next video.
