# Transcript: The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)

**URL:** https://www.youtube.com/watch?v=muwRbfuKbR4
**Segments:** 626
**Channel:** Cole Medin
**Duration:** 21:14
**Uploaded:** 2026-07-03

---

## Full Text

Everyone is using AI coding assistance very differently. You'd be surprised how large the spectrum is even for companies that are using these tools to ship production code. And the best explanation I found for the different ways we can use coding agents is from Dan Shapiro. So in this blog post, the five levels from spicy auto complete to the dark factory. And it's really important for you to understand the level that you're currently at and what you should be shooting for. And the level that's best for you also changes over time as you create a more structured approach to AI coding. And so in this video, I want to break down each one of the levels in nice and simple for you and help you understand where you should be at right now. And I just want to share some honest thoughts especially on some of the last levels especially with the dark factory. I see a lot of companies go for this right now and I've even built my own. But there are a lot of downsides to the dark factory as powerful as it is. And so we'll get into the meat of that as well. All right, so let's get right into the different levels of AI coding. And this entire article uses the analogy of driving a vehicle cuz there's a company in 2013 that created the five levels of driving automation. And it's very neat because we can map each one of these levels directly to how we interact with AI coding assistants. How much are we leaning on them versus keeping our hands on the driver's wheel when we are interacting with them and having them create the code for us. And so level number one is spicy auto complete. I love this name by the way. And here you're still writing every single line of code yourself. You're just using the coding agent as a reference tool or some kind of enhanced search. So it's like a smarter stack overflow. And so it never has the final say. It doesn't get to write a line of code, but you're constantly leaning on it for how should I architect this or how should I write this function. And so it's like your parents Volvo. So maybe even having automatic transition. This is the most manual you can possibly be. You have to manage the car at a very fundamental level. And so, you can see that it's actually level zero because we're not really having the coding agent do anything for us. And so, then we get into level one. And so, this is like the coding intern. Or when you're driving a car, you have cruise control. It's that first level of autonomy where there's at least one part of the car that's being managed on your behalf. And so, here your coding agent is going to write the unimportant or boilerplate code. And so, setting up your initial repository, maybe installing packages, writing unit tests, doing simple refactors, that kind of thing. You're not leaning on it for anything that takes true reasoning, but you're still saving a good amount of time here. And then level two takes us to the junior developer. This is where you really start to lean on the coding agent or lean on the car to operate pretty autonomously, but only in some situations. So, when you're driving, it's like you have autopilot on the highway. But when you're actually driving in the city and there's a lot of turns and rules that need to be followed, you can't trust it anymore. So, it's a junior developer where you're doing a lot of pair programming. You are handing off a lot of the boring work, but there still are going to be those things where you don't trust it entirely and you're driving the process very manually. And there's a good chance that this is where you are at right now. Because if you don't have a very established system for how to leverage AI coding assistants and have them evolve over time, and we'll talk about that in a little bit, then you probably don't trust it for every kind of task. There are certain things where you think it's just going to be better for you to do it yourself, especially if you're more technically inclined. And I do really encourage you to get past level two. So, when we start to talk about level three here, this is where I really want you to be. And so, it's easy to get here because you're trusting it with the easy stuff, like autopilot on the highway. But when you really create a system for planning and implementing and validating, that's when you go into level three, the developer. This is where you get to the point where your coding agent is writing a majority of the code base, which is what it says right here, but honestly, I would take this a little bit further. When you get to level three, and this is mostly where I operate, this is where you're delegating all of the coding to your agent. And I myself haven't written a single line of code for over a year now, which is crazy to think because I've spent years and years of my life writing code every single day. And so, as an engineer, it took a while to get to the point where I had the system and built the trust to get to level three. But there's a good chance this is where you should be. This is the sweet spot of reliability and autonomy. Cuz as it relates to driving a car, it's like a Waymo with a safety driver. You're letting the coding agent really go, or you're letting the car do all the driving, but you're still in the driver's seat. You're still attentive, you're still driving the process. And so, what I like to say here for level three is the only reason that we delegate all the coding to the agent and trust it to do that is because we're sandwiching the implementation with a lot of planning and a lot of validation that we are very much a part of. And so, you delegate all the coding, but you still remain in the driver's seat. But that starts to change once we get to level four. This is the level where we reach the engineering team. You're handing off much larger sets of work for the coding agent to knock out autonomously. And so, you're still at the helm, but you're sleeping for long periods of time because we're letting the agent rip through larger sets of work based on something like an epic, a PRD, or a spec. Level three is more like each individual task. We're doing the planning and validation with the coding agent, but here we're just doing the very high-level direction setting up front, and then the validation at the very end. Like a set of pull requests, for example. And so, we're letting it go, go, go based on a larger spec. And so, it's not quite the dark factory. We'll talk about this in just a second where there's not even a driver's seat. Like right like we still have control of the system to an extent, but we're just not doing that very often. And at this level, this is where your reliability really starts to tank until you have a trusted and really well-established workflow for AI coding going from idea all the way to production. And it takes a while to get there. That's why I recommend you stay at level three or you at least stay here for a long time because you build up that system and then you can start to make your coding agent more autonomous. So really just taking the system that you were more a part of and then taking out the human in the loop as you go to get to levels four and five. And so I'll talk about in a little bit what it actually takes to create this system. What actually is a system for AI coding, but first let's talk about the dark factory for a bit. So at level five, it really isn't even a car anymore. Let me zoom in on this you can see this image well. There is no driver's wheel. We can't even take control and grab the reins even if we wanted to. Now there's still a console in this vehicle, whatever it is, this spaceship. So the console allows us to still input our highest-level directions possible, but yeah, we're not controlling any of the development. And so the way that a dark factory works is your input is your spec, the large document that outlines everything you want to build. And what you get out of the dark factory is shipped code. And so that's probably the biggest difference between level five and four. Level four, you're not trusting the coding agent to ship right to production, but in level five, you actually are. And if that sounds kind of scary, it should. And that's why I'm saying you have to be very careful when you get to this level of autonomy. Cuz if there's one thing you have described wrong in the spec or the coding agent just make some kind of incorrect assumption, that could lead to dozens of shipped deployments that are just botching what you wanted to actually create. But in the end, the dark factory is ideal. If your business can get to the point where you have a process where you can send in a spec and get out shipped code, that, my friend, is the dream. And we're starting to get to the point where the dark factory is becoming realistic. Now, I I want to be very careful how I put this right now because I don't want you to just reach for the dark factory immediately. But, I think that there is a possibility you can get here with the current tooling and LLMs we have available. And so, you can probably jump to level three very fast. I mean, that's what I teach on my YouTube channel and in the Dynamis community. Like, creating the system where you're still in the loop for each individual build, but you have quite a bit of autonomy. You're delegating all the coding to the agents. So, you start here. This is where I want you to be. And then, you take out the human in the loop as you create that system where you really trust that it understands your code base and your workflows and things are reliable. And so, there are some companies that are starting to come out of the woodwork sharing how they do have a dark factory that's actually running. StrongDM is one example. I'll link to an article on that in the description. A lot of other companies aren't really documenting anything like StrongDM, so it's just some rumors that are starting to surface of companies that are doing this successfully. Even in the banking industry, even when the code has to be perfect when it's shipped to production. So, it's definitely possible, but we need the system to get there. And so, with that, let's actually get into what does a system for AI coding look like and how do we build something that can even take the form of the dark factory? The sponsor of today's video is Sonar. They're making big moves in the AI coding space right now. The reality is that these days AI is writing a huge chunk of new code, and that, my friend, is not slowing down. But, the problem is traditional code reviews and quality gates were never made for volume at this speed. And so, bugs slip through and AI errors compound on themselves and your code base gets fragile quickly. That is why Sonar has acquired Gitarr. Gitarr is AI code review that actually fixes your code. It's not just another agent you throw at the problem, it's an entire harness for validation, making your code more reliable with full visibility as well. The way that Gitarr works is you connect it to any of your GitHub or GitLab repositories and then as soon as you open up a pull request, we can see Gitarr here running a comprehensive code review. And not only does it do the code review but can also fix the issues that it finds automatically as well. So right here, it identified and fixed a SQL injection vulnerability that I have in this pull request. And the best part for all of this is every single time it makes a fix, it automatically validates it against your CI. So it's just increasing the reliability even more. It even reads your CI failures for you. So it can do things like dedupe your errors, help you identify flaky tests, and clean up your build and lint failures not drowning in logs. And you can see this is all very in line with Sonar's agent-centric development life cycle, a framework that's based on the three pillars of guide, verify, and solve. And Gitarr fits very well into their verify pillar. And teams using Sonar are 44% less likely to hit production outages caused by AI generated code. And it's not about replacing your human judgment, it's just a serious safety net under everything your agent ships. And Gitarr has a 14-day free pro trial, no credit card required. I'll link to it in the description. All right, so I put a lot of time into thinking about how I can quickly describe what a system is to you for AI coding. And I want to be concise because that's really not the point of this video to dive super deep into the weeds of system engineering or context engineering, but I wanted to give you an idea of what you're going to be creating and evolving to trust your coding agent to be more autonomous over time. And so I decided to pull from the Dynamis Agentic Coding Course. So, taking a couple of the things that I have there and just showing it really fast. And so, I want to start by talking about the AI layer because these are the different components that you build on top of your coding agent. Things like your rules and skills. So, your coding agent understands your conventions, your context of your code base, and your workflows. And when you think about harness engineering, which is building the system for AI coding, it really starts at layer zero with the tool that you pick. So, you don't control this, but you get to pick the coding agent. And the coding agent, it really is a harness because it wraps the large language model with the tools and instructions to make it operate as an AI coding assistant. And then we build the layer on top. This is what we control because we wrap the coding agent that it itself wraps the LLM to provide a context not on how to be an AI coding assistant, but how we want it to be a coding agent specifically on our code base, with our workflows. And so, there's really six components that we're building up here. We create our rules. These are the conventions we want our coding agent to follow. We have our sub agents, how we want to delegate work and manage our context. And then we have our skills, our packaged up workflows. Like this is how we want our coding agent to do planning. Here's how we want it to implement. What's the procedure we want it to work itself through based on the input we give it for what we want to build. And I don't need to get into the details for all six components here of the AI layer. I have a video that I'll link to right here where I really get into all this. Just know that these are the components we create to make our coding agent understand our conventions and process. We build these up and we compose them together to create our full workflow. And that is the system. And so, I'll cover this diagram really quickly because this is the flow, right? Like we build up the AI layer, and now here's how we use it. And so, we create it at first. That's what this stage represents for both green field or brown field. We're either going to be building up our initial rules and workflows from the idea of what we want to create if we're starting from scratch or if we're working on top of an existing code base, we're going to understand the code and document it. We're going to document our conventions, build up our workflows. And then either way, it's going to converge into the exact same process that I call the R Piv Loop. This is how I build any new feature or fix any bug in any code base. And so I start by researching, just exploring how we're going to be tackling this problem. And then from there, I do structured planning. And again, I have rules and sub agents and skills that drive this more higher-level process. That is the system. So I create a structured plan that has things like my validation strategy and the task list that I have for the agent. And like I said earlier, when you are at level three, which is what I recommend, you're very much a part of the process here. We're having the conversation with the coding agent to establish things, having it grill us with questions to remove assumptions, and then we create that final plan that we then send into implementation. So we have another skill, another workflow for it to operate on that plan that we create. And of course, we have a lot of validation at the end. And so the system here for how the coding agent can run unit tests and even do full end-to-end testing. And then human validation if you want to really make sure that your reliability is top-notch. So there you go. That is the fastest I've ever blitzed through helping you understand a full system for AI coding. So I hope that makes sense at a high level. We build the components that create our harness, and then this is the flow to leverage it. And I won't talk about system evolution too much here, but we also have the whole idea of every single time your coding agent makes a mistake, it's worth not just patching it and moving on, but having that conversation with your coding agent to figure out what part of our AI layer can we improve so that issue doesn't happen again or at least it's less likely to happen again. Like maybe there's a workflow we can refine or a new rule that we can add to address the issue that the coding agent created. And so going back to the article now, when you get to level three, that's when you really start to have the system that I showed you just now very briefly. You have for yourself or even as a team standard the rules and skills, everything in the AI layer, and then you're composing that together in the flow that I described. And so how exactly you're going to with your coding agent go through all the steps it takes to go from idea to production or pull request. And so when you do that system evolution, every single R pivot, if you're figuring out how can I make the AI layer, how can I make my process better over time, you'll start to get to the point where when you have a new request come in, you're like, "You know what? I think my coding agent or I know my coding agent is just going to knock this out of the park." Like I don't even really have to iterate on the plan. Or I don't even think I have to validate things besides a couple of quick spot checks. When you get to that point, that's when you know you can start to go to level four and maybe even level five. You start to sort of build that muscle of what you can trust your system to accomplish, you grow that muscle, you grow that system over time, and you can start to trust it with multiple tasks operating through it autonomously. That's level four. And then dark factory, that's when you have to take your system even beyond what I've showed you. So last thing I want to cover here is just talking about what goes into really taking a system like I described and turning it into a fully fledged dark factory. So I found this article that I'll link to in the description that I think very nicely puts how you want to build up a dark factory. What are all the different components? Cuz like they say right here, a dark factory isn't just AI writes code. It's a system with distinct components that handle different stages of the development pipeline. If we're going to go from massive spec all the way to ship code, we have to have a lot of different agents operating to triage the different tasks from the spec, to build each one of them, to review the pull requests, to manage the deployments, to do the regression testing. There is so much that goes into a dark factory. In fact, I did quite a few live streams on my YouTube channel. I'll link to one right here where I built a dark factory live and I used Arkon, my open source harness builder, to create a lot of the workflows to manage all these different parts of the development pipeline and it was a lot of work and there were still a million things I needed to do to truly make it reliable. It's just more of an experiment that I did. I called it my dark factory experiment. But anyway, it starts with a planning agent. So, once we have the larger spec distributed into individual tasks, we need an agent to handle the planning for that one task. And so, it's just like what I showed you in the system earlier where we want to create that structured markdown document, our plan of attack for that specific feature or bug. And then, we send that into the code generation agent. So, we have a handoff there where usually it's a markdown document is passed to another agent to execute and create that pull request. And then, the validation layer to review that pull request. It's important to not do your code review in the same context window where you do the implementation cuz there's a lot of bias that's built up there. And then, of course, we have the deployment system. Again, no human in the loop going straight into production. So, we want an agent that manages that, maybe doing things like regression testing as well. And then, we need the orchestration layer. We need that higher-level agent to take the spec and split it into tasks, to manage the handoffs between the different agents and make sure that we don't have duplicate work or that one agent is stalling waiting for inputs that are never going to arrive. I mean, even just reading through this, you can start to imagine all of the complexities, the millions of things that can go wrong because agents can veer off of your initial spec and have a ton of tasks that don't make any sense. They can stall waiting for a handoff from another agent that crashed. If there's no human in the loop, you risk that those failures happening without much visibility because the whole point of it is you don't have to pay attention to it. And so you really got to make sure that things are reliable before you ever get to this point. And building the orchestration layer on top of your existing system is also an engineering effort of its own. So it's not even just like get the system to a point where it's reliable, it's get to the point where it's reliable and then you have to build the next layer on top of it. So it is a lot of work to get here. So again, the dark factory is the dream, but yes, it takes a lot of engineering effort. And if you want to read the rest of the article, I would encourage you to do so. A lot of good stuff here. And they cover some things I've been working on with Arkon as well. Like deterministic and agentic nodes. Sometimes you need the reasoning capability of an LLM for a step in a workflow, but other times you don't. And you can make it more reliable by having some things that are handled deterministically just with code. Like formatting code, running a linter, triggering a deployment, you don't always need an LLM. And so that's one of the things I have built into Arkon. It's just the idea of engineering harnesses to drive these things. Like what Stripe did with Stripe Minions. And then they also go into the different failure modes that we talked about here, like cascading failures. Evaluation gaming is another really interesting one. These are the things we have to engineer for to make it so the dark factory is realistic at all. And yes, it can be kind of daunting when you look at something like this and think about what really goes into making it reliable, but this is also the future of AI coding. We already see companies that are starting to engineer these things successfully, and it's only going to get more realistic as coding agents and LLMs get more and more powerful. And so this is something that I'm really leaning into and I encourage you to do as well. I've already done some experimentation with it like I talked about earlier, and I do want to do more content on building a dark factory. So also let me know in the comments if you'd be interested in that. And so with that, that's all I got for you today. If you appreciate this video and you're looking forward to more things on agentic engineering and maybe dark factory building as well. I would really appreciate a like and a subscribe. And with that, I will see you in the next video.

---

## Timestamped Segments

**[0:00]** Everyone is using AI coding assistance

**[0:02]** very differently. You'd be surprised how

**[0:04]** large the spectrum is even for companies

**[0:07]** that are using these tools to ship

**[0:09]** production code. And the best

**[0:11]** explanation I found for the different

**[0:13]** ways we can use coding agents is from

**[0:15]** Dan Shapiro. So in this blog post, the

**[0:18]** five levels from spicy auto complete to

**[0:20]** the dark factory. And it's really

**[0:22]** important for you to understand the

**[0:24]** level that you're currently at and what

**[0:26]** you should be shooting for. And the

**[0:28]** level that's best for you also changes

**[0:30]** over time as you create a more

**[0:32]** structured approach to AI coding. And so

**[0:34]** in this video, I want to break down each

**[0:36]** one of the levels in nice and simple for

**[0:38]** you and help you understand where you

**[0:41]** should be at right now. And I just want

**[0:44]** to share some honest thoughts especially

**[0:45]** on some of the last levels especially

**[0:47]** with the dark factory. I see a lot of

**[0:50]** companies go for this right now and I've

**[0:52]** even built my own. But there are a lot

**[0:55]** of downsides to the dark factory as

**[0:57]** powerful as it is. And so we'll get into

**[0:59]** the meat of that as well. All right, so

**[1:00]** let's get right into the different

**[1:02]** levels of AI coding. And this entire

**[1:04]** article uses the analogy of driving a

**[1:06]** vehicle cuz there's a company in 2013

**[1:09]** that created the five levels of driving

**[1:11]** automation. And it's very neat because

**[1:13]** we can map each one of these levels

**[1:15]** directly to how we interact with AI

**[1:17]** coding assistants. How much are we

**[1:20]** leaning on them versus keeping our hands

**[1:22]** on the driver's wheel when we are

**[1:24]** interacting with them and having them

**[1:25]** create the code for us. And so level

**[1:27]** number one is spicy auto complete. I

**[1:30]** love this name by the way. And here

**[1:32]** you're still writing every single line

**[1:35]** of code yourself. You're just using the

**[1:37]** coding agent as a reference tool or some

**[1:39]** kind of enhanced search. So it's like a

**[1:41]** smarter stack overflow. And so it never

**[1:43]** has the final say. It doesn't get to

**[1:45]** write a line of code, but you're

**[1:47]** constantly leaning on it for how should

**[1:48]** I architect this or how should I write

**[1:50]** this function. And so it's like your

**[1:52]** parents Volvo. So maybe even having

**[1:54]** automatic transition. This is the most

**[1:56]** manual you can possibly be. You have to

**[2:00]** manage the car at a very fundamental

**[2:01]** level. And so, you can see that it's

**[2:03]** actually level zero because we're not

**[2:06]** really having the coding agent do

**[2:07]** anything for us. And so, then we get

**[2:09]** into level one. And so, this is like the

**[2:12]** coding intern. Or when you're driving a

**[2:13]** car, you have cruise control. It's that

**[2:16]** first level of autonomy where there's at

**[2:18]** least one part of the car that's being

**[2:21]** managed on your behalf. And so, here

**[2:24]** your coding agent is going to write the

**[2:25]** unimportant or boilerplate code. And so,

**[2:28]** setting up your initial repository,

**[2:30]** maybe installing packages, writing unit

**[2:32]** tests, doing simple refactors, that kind

**[2:35]** of thing. You're not leaning on it for

**[2:36]** anything that takes true reasoning, but

**[2:38]** you're still saving a good amount of

**[2:39]** time here. And then level two takes us

**[2:41]** to the junior developer. This is where

**[2:43]** you really start to lean on the coding

**[2:45]** agent or lean on the car to operate

**[2:47]** pretty autonomously, but only in some

**[2:49]** situations. So, when you're driving,

**[2:52]** it's like you have autopilot on the

**[2:53]** highway. But when you're actually

**[2:55]** driving in the city and there's a lot of

**[2:57]** turns and rules that need to be

**[2:58]** followed, you can't trust it anymore.

**[3:00]** So, it's a junior developer where you're

**[3:02]** doing a lot of pair programming. You are

**[3:04]** handing off a lot of the boring work,

**[3:06]** but there still are going to be those

**[3:07]** things where you don't trust it entirely

**[3:09]** and you're driving the process very

**[3:11]** manually. And there's a good chance that

**[3:13]** this is where you are at right now.

**[3:16]** Because if you don't have a very

**[3:17]** established system for how to leverage

**[3:19]** AI coding assistants and have them

**[3:21]** evolve over time, and we'll talk about

**[3:23]** that in a little bit, then you probably

**[3:25]** don't trust it for every kind of task.

**[3:27]** There are certain things where you think

**[3:29]** it's just going to be better for you to

**[3:30]** do it yourself, especially if you're

**[3:32]** more technically inclined. And I do

**[3:35]** really encourage you to get past level

**[3:37]** two. So, when we start to talk about

**[3:39]** level three here, this is where I really

**[3:41]** want you to be. And so, it's easy to get

**[3:44]** here because you're trusting it with the

**[3:46]** easy stuff, like autopilot on the

**[3:48]** highway. But when you really create a

**[3:50]** system for planning and implementing and

**[3:52]** validating, that's when you go into

**[3:54]** level three, the developer. This is

**[3:57]** where you get to the point where your

**[3:58]** coding agent is writing a majority of

**[4:00]** the code base, which is what it says

**[4:01]** right here, but honestly, I would take

**[4:03]** this a little bit further. When you get

**[4:05]** to level three, and this is mostly where

**[4:06]** I operate, this is where you're

**[4:08]** delegating all of the coding to your

**[4:10]** agent. And I myself haven't written a

**[4:13]** single line of code for over a year now,

**[4:15]** which is crazy to think because I've

**[4:17]** spent years and years of my life writing

**[4:19]** code every single day. And so, as an

**[4:22]** engineer, it took a while to get to the

**[4:24]** point where I had the system and built

**[4:25]** the trust to get to level three. But

**[4:27]** there's a good chance this is where you

**[4:29]** should be. This is the sweet spot of

**[4:32]** reliability and autonomy. Cuz as it

**[4:34]** relates to driving a car, it's like a

**[4:36]** Waymo with a safety driver. You're

**[4:37]** letting the coding agent really go, or

**[4:40]** you're letting the car do all the

**[4:41]** driving, but you're still in the

**[4:42]** driver's seat. You're still attentive,

**[4:44]** you're still driving the process. And

**[4:46]** so, what I like to say here for level

**[4:48]** three is the only reason that we

**[4:50]** delegate all the coding to the agent and

**[4:52]** trust it to do that is because we're

**[4:55]** sandwiching the implementation with a

**[4:57]** lot of planning and a lot of validation

**[4:59]** that we are very much a part of. And so,

**[5:01]** you delegate all the coding, but you

**[5:02]** still remain in the driver's seat. But

**[5:05]** that starts to change once we get to

**[5:07]** level four. This is the level where we

**[5:10]** reach the engineering team. You're

**[5:11]** handing off much larger sets of work for

**[5:13]** the coding agent to knock out

**[5:15]** autonomously. And so, you're still at

**[5:17]** the helm, but you're sleeping for long

**[5:19]** periods of time because we're letting

**[5:22]** the agent rip through larger sets of

**[5:23]** work based on something like an epic, a

**[5:25]** PRD, or a spec. Level three is more like

**[5:28]** each individual task. We're doing the

**[5:30]** planning and validation with the coding

**[5:33]** agent, but here we're just doing the

**[5:34]** very high-level direction setting up

**[5:36]** front, and then the validation at the

**[5:38]** very end. Like a set of pull requests,

**[5:40]** for example. And so, we're letting it

**[5:42]** go, go, go based on a larger spec. And

**[5:45]** so, it's not quite the dark factory.

**[5:46]** We'll talk about this in just a second

**[5:48]** where there's not even a driver's seat.

**[5:50]** Like right like we still have control of

**[5:53]** the system to an extent, but we're just

**[5:55]** not doing that very often. And at this

**[5:57]** level, this is where your reliability

**[5:59]** really starts to tank until you have a

**[6:02]** trusted and really well-established

**[6:04]** workflow for AI coding going from idea

**[6:07]** all the way to production. And it takes

**[6:09]** a while to get there. That's why I

**[6:10]** recommend you stay at level three or you

**[6:12]** at least stay here for a long time

**[6:14]** because you build up that system and

**[6:16]** then you can start to make your coding

**[6:18]** agent more autonomous. So really just

**[6:20]** taking the system that you were more a

**[6:22]** part of and then taking out the human in

**[6:24]** the loop as you go to get to levels four

**[6:27]** and five. And so I'll talk about in a

**[6:29]** little bit what it actually takes to

**[6:31]** create this system. What actually is a

**[6:33]** system for AI coding, but first let's

**[6:36]** talk about the dark factory for a bit.

**[6:38]** So at level five, it really isn't even a

**[6:40]** car anymore. Let me zoom in on this you

**[6:42]** can see this image well. There is no

**[6:44]** driver's wheel. We can't even take

**[6:46]** control and grab the reins even if we

**[6:48]** wanted to. Now there's still a console

**[6:50]** in this vehicle, whatever it is, this

**[6:52]** spaceship. So the console allows us to

**[6:55]** still input our highest-level directions

**[6:57]** possible, but yeah, we're not

**[6:59]** controlling any of the development. And

**[7:01]** so the way that a dark factory works is

**[7:03]** your input is your spec, the large

**[7:06]** document that outlines everything you

**[7:08]** want to build. And what you get out of

**[7:10]** the dark factory is shipped code. And so

**[7:12]** that's probably the biggest difference

**[7:14]** between level five and four. Level four,

**[7:16]** you're not trusting the coding agent to

**[7:18]** ship right to production, but in level

**[7:19]** five, you actually are. And if that

**[7:22]** sounds kind of scary, it should. And

**[7:24]** that's why I'm saying you have to be

**[7:26]** very careful when you get to this level

**[7:27]** of autonomy. Cuz if there's one thing

**[7:30]** you have described wrong in the spec or

**[7:32]** the coding agent just make some kind of

**[7:33]** incorrect assumption, that could lead to

**[7:35]** dozens of shipped deployments that are

**[7:38]** just botching what you wanted to

**[7:40]** actually create. But in the end, the

**[7:42]** dark factory is ideal. If your business

**[7:45]** can get to the point where you have a

**[7:46]** process where you can send in a spec and

**[7:49]** get out shipped code, that, my friend,

**[7:51]** is the dream. And we're starting to get

**[7:55]** to the point where the dark factory is

**[7:57]** becoming realistic. Now, I I want to be

**[7:59]** very careful how I put this right now

**[8:01]** because I don't want you to just reach

**[8:03]** for the dark factory immediately. But, I

**[8:05]** think that there is a possibility you

**[8:07]** can get here with the current tooling

**[8:09]** and LLMs we have available. And so, you

**[8:11]** can probably jump to level three very

**[8:13]** fast. I mean, that's what I teach on my

**[8:15]** YouTube channel and in the Dynamis

**[8:16]** community. Like, creating the system

**[8:18]** where you're still in the loop for each

**[8:20]** individual build, but you have quite a

**[8:22]** bit of autonomy. You're delegating all

**[8:24]** the coding to the agents. So, you start

**[8:25]** here. This is where I want you to be.

**[8:27]** And then, you take out the human in the

**[8:30]** loop as you create that system where you

**[8:32]** really trust that it understands your

**[8:34]** code base and your workflows and things

**[8:36]** are reliable.

**[8:37]** And so, there are some companies that

**[8:39]** are starting to come out of the woodwork

**[8:41]** sharing how they do have a dark factory

**[8:43]** that's actually running. StrongDM is one

**[8:46]** example. I'll link to an article on that

**[8:47]** in the description. A lot of other

**[8:49]** companies aren't really documenting

**[8:51]** anything like StrongDM, so it's just

**[8:52]** some rumors that are starting to surface

**[8:55]** of companies that are doing this

**[8:56]** successfully. Even in the banking

**[8:58]** industry, even when the code has to be

**[9:00]** perfect when it's shipped to production.

**[9:02]** So, it's definitely possible, but we

**[9:04]** need the system to get there. And so,

**[9:06]** with that, let's actually get into what

**[9:08]** does a system for AI coding look like

**[9:10]** and how do we build something that can

**[9:13]** even take the form of the dark factory?

**[9:15]** The sponsor of today's video is Sonar.

**[9:17]** They're making big moves in the AI

**[9:19]** coding space right now. The reality is

**[9:21]** that these days AI is writing a huge

**[9:23]** chunk of new code, and that, my friend,

**[9:25]** is not slowing down. But, the problem is

**[9:28]** traditional code reviews and quality

**[9:30]** gates were never made for volume at this

**[9:32]** speed. And so, bugs slip through and AI

**[9:35]** errors compound on themselves and your

**[9:36]** code base gets fragile quickly. That is

**[9:39]** why Sonar has acquired Gitarr. Gitarr is

**[9:41]** AI code review that actually fixes your

**[9:44]** code. It's not just another agent you

**[9:45]** throw at the problem, it's an entire

**[9:47]** harness for validation, making your code

**[9:50]** more reliable with full visibility as

**[9:52]** well. The way that Gitarr works is you

**[9:54]** connect it to any of your GitHub or

**[9:56]** GitLab repositories and then as soon as

**[9:58]** you open up a pull request, we can see

**[10:00]** Gitarr here running a comprehensive code

**[10:02]** review. And not only does it do the code

**[10:04]** review but can also fix the issues that

**[10:06]** it finds automatically as well. So right

**[10:09]** here, it identified and fixed a SQL

**[10:11]** injection vulnerability that I have in

**[10:14]** this pull request. And the best part for

**[10:16]** all of this is every single time it

**[10:18]** makes a fix, it automatically validates

**[10:20]** it against your CI. So it's just

**[10:23]** increasing the reliability even more. It

**[10:25]** even reads your CI failures for you. So

**[10:28]** it can do things like dedupe your

**[10:30]** errors, help you identify flaky tests,

**[10:32]** and clean up your build and lint

**[10:34]** failures not drowning in logs. And you

**[10:37]** can see this is all very in line with

**[10:39]** Sonar's agent-centric development life

**[10:41]** cycle, a framework that's based on the

**[10:43]** three pillars of guide, verify, and

**[10:46]** solve. And Gitarr fits very well into

**[10:49]** their verify pillar. And teams using

**[10:51]** Sonar are 44% less likely to hit

**[10:54]** production outages caused by AI

**[10:56]** generated code. And it's not about

**[10:57]** replacing your human judgment, it's just

**[11:00]** a serious safety net under everything

**[11:01]** your agent ships. And Gitarr has a

**[11:04]** 14-day free pro trial, no credit card

**[11:06]** required. I'll link to it in the

**[11:08]** description. All right, so I put a lot

**[11:10]** of time into thinking about how I can

**[11:12]** quickly describe what a system is to you

**[11:14]** for AI coding. And I want to be concise

**[11:17]** because that's really not the point of

**[11:18]** this video to dive super deep into the

**[11:20]** weeds of system engineering or context

**[11:23]** engineering, but I wanted to give you an

**[11:24]** idea of what you're going to be creating

**[11:26]** and evolving to trust your coding agent

**[11:29]** to be more autonomous over time. And so

**[11:31]** I decided to pull from the Dynamis

**[11:34]** Agentic Coding Course. So, taking a

**[11:36]** couple of the things that I have there

**[11:38]** and just showing it really fast. And so,

**[11:40]** I want to start by talking about the AI

**[11:42]** layer because these are the different

**[11:44]** components that you build on top of your

**[11:46]** coding agent. Things like your rules and

**[11:48]** skills. So, your coding agent

**[11:50]** understands your conventions, your

**[11:52]** context of your code base, and your

**[11:54]** workflows. And when you think about

**[11:56]** harness engineering, which is building

**[11:58]** the system for AI coding, it really

**[12:00]** starts at layer zero with the tool that

**[12:02]** you pick. So, you don't control this,

**[12:04]** but you get to pick the coding agent.

**[12:06]** And the coding agent, it really is a

**[12:08]** harness because it wraps the large

**[12:11]** language model with the tools and

**[12:13]** instructions to make it operate as an AI

**[12:15]** coding assistant. And then we build the

**[12:17]** layer on top. This is what we control

**[12:19]** because we wrap the coding agent that it

**[12:22]** itself wraps the LLM to provide a

**[12:24]** context not on how to be an AI coding

**[12:26]** assistant, but how we want it to be a

**[12:27]** coding agent specifically on our code

**[12:30]** base, with our workflows. And so,

**[12:32]** there's really six components that we're

**[12:35]** building up here. We create our rules.

**[12:36]** These are the conventions we want our

**[12:38]** coding agent to follow. We have our sub

**[12:40]** agents, how we want to delegate work and

**[12:42]** manage our context. And then we have our

**[12:44]** skills, our packaged up workflows. Like

**[12:47]** this is how we want our coding agent to

**[12:48]** do planning. Here's how we want it to

**[12:50]** implement. What's the procedure we want

**[12:52]** it to work itself through based on the

**[12:54]** input we give it for what we want to

**[12:56]** build. And I don't need to get into the

**[12:58]** details for all six components here of

**[13:00]** the AI layer. I have a video that I'll

**[13:02]** link to right here where I really get

**[13:04]** into all this. Just know that these are

**[13:05]** the components we create to make our

**[13:07]** coding agent understand our conventions

**[13:09]** and process. We build these up and we

**[13:11]** compose them together to create our full

**[13:14]** workflow. And that is the system. And

**[13:17]** so, I'll cover this diagram really

**[13:18]** quickly because this is the flow, right?

**[13:21]** Like we build up the AI layer, and now

**[13:23]** here's how we use it. And so, we create

**[13:24]** it at first. That's what this stage

**[13:26]** represents for both green field or brown

**[13:28]** field. We're either going to be building

**[13:30]** up our initial rules and workflows from

**[13:32]** the idea of what we want to create if

**[13:34]** we're starting from scratch or if we're

**[13:36]** working on top of an existing code base,

**[13:37]** we're going to understand the code and

**[13:39]** document it. We're going to document our

**[13:41]** conventions, build up our workflows. And

**[13:43]** then either way, it's going to converge

**[13:45]** into the exact same process that I call

**[13:48]** the R Piv Loop. This is how I build any

**[13:50]** new feature or fix any bug in any code

**[13:53]** base. And so I start by researching,

**[13:55]** just exploring how we're going to be

**[13:58]** tackling this problem. And then from

**[14:00]** there, I do structured planning. And

**[14:02]** again, I have rules and sub agents and

**[14:05]** skills that drive this more higher-level

**[14:07]** process. That is the system. So I create

**[14:10]** a structured plan that has things like

**[14:12]** my validation strategy and the task list

**[14:14]** that I have for the agent. And like I

**[14:16]** said earlier, when you are at level

**[14:18]** three, which is what I recommend, you're

**[14:20]** very much a part of the process here.

**[14:22]** We're having the conversation with the

**[14:23]** coding agent to establish things, having

**[14:25]** it grill us with questions to remove

**[14:27]** assumptions, and then we create that

**[14:29]** final plan that we then send into

**[14:31]** implementation. So we have another

**[14:32]** skill, another workflow for it to

**[14:35]** operate on that plan that we create. And

**[14:37]** of course, we have a lot of validation

**[14:39]** at the end. And so the system here for

**[14:41]** how the coding agent can run unit tests

**[14:43]** and even do full end-to-end testing. And

**[14:45]** then human validation if you want to

**[14:47]** really make sure that your reliability

**[14:49]** is top-notch. So there you go. That is

**[14:51]** the fastest I've ever blitzed through

**[14:53]** helping you understand a full system for

**[14:55]** AI coding. So I hope that makes sense at

**[14:57]** a high level. We build the components

**[14:59]** that create our harness, and then this

**[15:01]** is the flow to leverage it. And I won't

**[15:03]** talk about system evolution too much

**[15:05]** here, but we also have the whole idea of

**[15:07]** every single time your coding agent

**[15:08]** makes a mistake, it's worth not just

**[15:10]** patching it and moving on, but having

**[15:12]** that conversation with your coding agent

**[15:14]** to figure out what part of our AI layer

**[15:16]** can we improve so that issue doesn't

**[15:18]** happen again or at least it's less

**[15:20]** likely to happen again. Like maybe

**[15:21]** there's a workflow we can refine or a

**[15:23]** new rule that we can add to address the

**[15:25]** issue that the coding agent created. And

**[15:28]** so going back to the article now, when

**[15:29]** you get to level three, that's when you

**[15:31]** really start to have the system that I

**[15:32]** showed you just now very briefly. You

**[15:35]** have for yourself or even as a team

**[15:37]** standard the rules and skills,

**[15:39]** everything in the AI layer, and then

**[15:40]** you're composing that together in the

**[15:42]** flow that I described. And so how

**[15:45]** exactly you're going to with your coding

**[15:47]** agent go through all the steps it takes

**[15:49]** to go from idea to production or pull

**[15:52]** request. And so when you do that system

**[15:54]** evolution, every single R pivot, if

**[15:56]** you're figuring out how can I make the

**[15:57]** AI layer, how can I make my process

**[15:59]** better over time, you'll start to get to

**[16:01]** the point where when you have a new

**[16:03]** request come in, you're like, "You know

**[16:05]** what? I think my coding agent or I know

**[16:07]** my coding agent is just going to knock

**[16:09]** this out of the park." Like I don't even

**[16:10]** really have to iterate on the plan. Or I

**[16:13]** don't even think I have to validate

**[16:14]** things besides a couple of quick spot

**[16:16]** checks. When you get to that point,

**[16:19]** that's when you know you can start to go

**[16:20]** to level four and maybe even level five.

**[16:23]** You start to sort of build that muscle

**[16:25]** of what you can trust your system to

**[16:27]** accomplish, you grow that muscle, you

**[16:29]** grow that system over time, and you can

**[16:31]** start to trust it with multiple tasks

**[16:33]** operating through it autonomously.

**[16:35]** That's level four. And then dark

**[16:37]** factory, that's when you have to take

**[16:39]** your system even beyond what I've showed

**[16:41]** you. So last thing I want to cover here

**[16:43]** is just talking about what goes into

**[16:45]** really taking a system like I described

**[16:47]** and turning it into a fully fledged dark

**[16:50]** factory. So I found this article that

**[16:52]** I'll link to in the description that I

**[16:53]** think very nicely puts how you want to

**[16:56]** build up a dark factory. What are all

**[16:58]** the different components? Cuz like they

**[16:59]** say right here, a dark factory isn't

**[17:01]** just AI writes code. It's a system with

**[17:03]** distinct components that handle

**[17:05]** different stages of the development

**[17:07]** pipeline. If we're going to go from

**[17:09]** massive spec all the way to ship code,

**[17:11]** we have to have a lot of different

**[17:13]** agents operating to triage the different

**[17:15]** tasks from the spec, to build each one

**[17:18]** of them, to review the pull requests, to

**[17:20]** manage the deployments, to do the

**[17:21]** regression testing. There is so much

**[17:24]** that goes into a dark factory. In fact,

**[17:26]** I did quite a few live streams on my

**[17:27]** YouTube channel. I'll link to one right

**[17:29]** here where I built a dark factory live

**[17:31]** and I used Arkon, my open source harness

**[17:34]** builder, to create a lot of the

**[17:35]** workflows to manage all these different

**[17:37]** parts of the development pipeline and it

**[17:39]** was a lot of work and there were still a

**[17:41]** million things I needed to do to truly

**[17:43]** make it reliable. It's just more of an

**[17:45]** experiment that I did. I called it my

**[17:47]** dark factory experiment. But anyway, it

**[17:49]** starts with a planning agent. So, once

**[17:51]** we have the larger spec distributed into

**[17:54]** individual tasks, we need an agent to

**[17:57]** handle the planning for that one task.

**[18:00]** And so, it's just like what I showed you

**[18:01]** in the system earlier where we want to

**[18:04]** create that structured markdown

**[18:06]** document, our plan of attack for that

**[18:08]** specific feature or bug. And then, we

**[18:11]** send that into the code generation

**[18:12]** agent. So, we have a handoff there where

**[18:15]** usually it's a markdown document is

**[18:16]** passed to another agent to execute and

**[18:18]** create that pull request. And then, the

**[18:21]** validation layer to review that pull

**[18:22]** request. It's important to not do your

**[18:24]** code review in the same context window

**[18:27]** where you do the implementation cuz

**[18:28]** there's a lot of bias that's built up

**[18:30]** there. And then, of course, we have the

**[18:32]** deployment system. Again, no human in

**[18:33]** the loop going straight into production.

**[18:35]** So, we want an agent that manages that,

**[18:37]** maybe doing things like regression

**[18:38]** testing as well. And then, we need the

**[18:40]** orchestration layer. We need that

**[18:42]** higher-level agent to take the spec and

**[18:43]** split it into tasks, to manage the

**[18:46]** handoffs between the different agents

**[18:47]** and make sure that we don't have

**[18:49]** duplicate work or that one agent is

**[18:51]** stalling waiting for inputs that are

**[18:52]** never going to arrive. I mean, even just

**[18:55]** reading through this, you can start to

**[18:56]** imagine all of the complexities, the

**[18:57]** millions of things that can go wrong

**[18:59]** because agents can veer off of your

**[19:01]** initial spec and have a ton of tasks

**[19:03]** that don't make any sense. They can

**[19:05]** stall waiting for a handoff from another

**[19:06]** agent that crashed. If there's no human

**[19:08]** in the loop, you risk that those

**[19:10]** failures happening without much

**[19:12]** visibility because the whole point of it

**[19:14]** is you don't have to pay attention to

**[19:15]** it. And so you really got to make sure

**[19:17]** that things are reliable before you ever

**[19:19]** get to this point. And building the

**[19:20]** orchestration layer on top of your

**[19:23]** existing system is also an engineering

**[19:25]** effort of its own. So it's not even just

**[19:27]** like get the system to a point where

**[19:29]** it's reliable, it's get to the point

**[19:31]** where it's reliable and then you have to

**[19:32]** build the next layer on top of it. So it

**[19:34]** is a lot of work to get here. So again,

**[19:36]** the dark factory is the dream, but yes,

**[19:39]** it takes a lot of engineering effort.

**[19:41]** And if you want to read the rest of the

**[19:43]** article, I would encourage you to do so.

**[19:44]** A lot of good stuff here. And they cover

**[19:46]** some things I've been working on with

**[19:48]** Arkon as well. Like deterministic and

**[19:50]** agentic nodes. Sometimes you need the

**[19:53]** reasoning capability of an LLM for a

**[19:55]** step in a workflow, but other times you

**[19:57]** don't. And you can make it more reliable

**[19:59]** by having some things that are handled

**[20:01]** deterministically just with code. Like

**[20:03]** formatting code, running a linter,

**[20:04]** triggering a deployment, you don't

**[20:06]** always need an LLM. And so that's one of

**[20:08]** the things I have built into Arkon. It's

**[20:09]** just the idea of engineering harnesses

**[20:12]** to drive these things. Like what Stripe

**[20:13]** did with Stripe Minions. And then they

**[20:16]** also go into the different failure modes

**[20:17]** that we talked about here, like

**[20:18]** cascading failures. Evaluation gaming is

**[20:21]** another really interesting one. These

**[20:23]** are the things we have to engineer for

**[20:25]** to make it so the dark factory is

**[20:27]** realistic at all. And yes, it can be

**[20:30]** kind of daunting when you look at

**[20:31]** something like this and think about what

**[20:32]** really goes into making it reliable, but

**[20:34]** this is also the future of AI coding. We

**[20:37]** already see companies that are starting

**[20:39]** to engineer these things successfully,

**[20:41]** and it's only going to get more

**[20:43]** realistic as coding agents and LLMs get

**[20:45]** more and more powerful. And so this is

**[20:47]** something that I'm really leaning into

**[20:49]** and I encourage you to do as well. I've

**[20:51]** already done some experimentation with

**[20:52]** it like I talked about earlier, and I do

**[20:54]** want to do more content on building a

**[20:56]** dark factory. So also let me know in the

**[20:58]** comments if you'd be interested in that.

**[21:00]** And so with that, that's all I got for

**[21:01]** you today. If you appreciate this video

**[21:03]** and you're looking forward to more

**[21:04]** things on agentic engineering and maybe

**[21:06]** dark factory building as well. I would

**[21:09]** really appreciate a like and a

**[21:10]** subscribe. And with that, I will see you

**[21:12]** in the next video.
