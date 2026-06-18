# Transcript: uhMCy25NBfw

**URL:** https://www.youtube.com/watch?v=uhMCy25NBfw
**Segments:** 518

---

## Full Text

So, if you've been using claw code for a while, you'll remember the old problem. The output was never good enough. You had to babysit everything, and you'd end up telling it to fix its own mistakes. But now, that's completely changed. Now, the agents are actually good. They can run full tasks. They can handle real workflows and get surprisingly close to what you want. And that's created a new problem. You've got multiple agents running at once, five terminal tabs open, and you're clicking between them trying to remember what each one is doing. So every time you switch, you're losing context. And it's not claw code that's slowing you down anymore. It's the way that you're using it. So I've spent the last 3 or 4 months building full business systems inside claw code, running multiple agents in parallel, managing my business using it. And this is the bottleneck that nobody's talking about. So I went out looking for a better way. And I tried everything. T-Mox, the desktop app, Vibe Camban, Paperclip, and they all have the same issue. They're all built for developers managing code, not for business owners managing goals. So, I decided to build something different. And in this video, I'll show you what's out there, why it doesn't work, why it breaks down, and the command center that I built that actually fixes it. So, let's get straight into it. And first, let me paint a picture of what's actually happening. So, you're going to start a Claw Code session. You're working on something, whether it's a content system, a lead genen workflow, whatever it is. Claude is running, doing its thing for, let's say, 5 to 10 minutes. and your mind starts wondering. So, you decide to start another task. So, you open up another terminal tab and then another one for the next task. And before you know it, you've got five terminals open because that's the max you can handle. And you're clicking through them all going, "Which one was building my landing page? Which one was doing my research?" And this is the thing that gets me. Claude Code has honestly gotten so good at doing the work autonomously. The agents are faster. They're smarter. They can handle more complex tasks without you having to watch them. We can run them on auto mode most of the time. But our interface for actually managing those agents has not changed at all. We're still flicking between these terminal windows. And you guessed it, every time you switch between the terminals, you have to reread what's happening. You have to figure out where things are at. And all of that mental overhead does genuinely add up and it slows you down massively and stops you from doing other tasks, which let's be honest is why you wanted to actually use claw code in the first place. So the problem isn't claw code. The problem is that we need to abstract one layer higher. So we need to start managing goals and tasks not managing terminals. So naturally I went looking for solutions online and there are actually quite a few options out there. So let me walk you through what I found and these can be pulled into kind of five main approaches. So option one is T-Max. The first thing that most techled clawed code users or developers try is T-Max. And if you don't know what that is, it lets you split your terminals into multiple panes. So you can see several claw code sessions running at the same time. You can see multiple agents working side by side and have a chat to those individual agents in one window. But it still has one major limitation. You are still in that terminal. You can't see the big picture and you can't drag tasks around. You can't see progress at a glance. You're still just having a chat interface conversation back and forth. And then when you start to think about passing this to a client, imagine passing that to your non-technical client and asking them to manage the agents that you've implemented for them. So then on the other end of the spectrum, we have Anthropic's own desktop app. And honestly, the UI is really nice for this and it's improving all the time. It's clean and it gives you a proper chat interface instead of that terminal. But there are two problems with it. First, setting up things like environment variables and MCP servers is harder in the desktop app than it is files in your terminal. In the terminal, we literally just add av file with our keys or a settings.json file. And second, this is the big one, you're still managing one conversation at a time. You've got a nicer window, but it's still one window and you're flicking back and forth between your conversation topics to actually get those individual tasks done. You don't have that abstracted higher level view. Now, this is where it gets really interesting. Vibe canban is a canban board designed specifically for managing coding agents. So, you can create issues, drag them into in progress, and it automatically spins up separate claw code sessions. And the UI is genuinely very nice. But this is the key thing. It's designed for developers who are managing code. So it talks about GitHub commits, pull requests, branches, diffs, and if you're a software engineer orchestrating coding agents, that's brilliant. But if you're a business owner who just wants to say get this goal done, it's too much for your use case. And then if you want to abstract one level higher, we've got paperclipip. So paperclip is an open-source framework, and you can think of this as an operating system for running an autonomous company. So, it's set out like a traditional company. You create org charts, assign roles like CEO, CTO, and set budgets for specific roles. And conceptually, I get where this is going, but in practice, it's way too much for most of us. You don't need an org chart to write a LinkedIn post and build a landing page. You just need to get jobs done faster. So, Paperclip, although it looks brilliant, is solving a problem that most of us don't even have yet because we still want to manage those outputs. And then there are tools like claude code board claude code task viewer open clause mission control and a bunch of others and some of them are really polished but again they're all oriented around coding sessions code review developer workflows technical users only. So every tool out there is solving the same problem. How do I manage multiple coding sessions? But that's not actually the problem for business users. Their question is how do I manage multiple business goals? let Claude code figure out the rest for me, but still have a handle on and maintain and supervise the outputs. And this is the gap that none of these tools fill. So, let me explain what it's actually missing. Every tool I just showed started from the bottom up. So, they start with the session in the terminal. They start with the code and then they try to add a project management layer on top of it. But what we actually need is the opposite. We need to start from the top and work our way downwards. So we need to start with the goal like I want to build a lead generation system and then let the system figure out what sessions to spin up, how in-depth the planning should be, how many agents are needed, what skills to use and how to get it done, i.e. all the technical overhead. And it's much like hiring a competent employee. You give that employee a goal. You say, "Here's the deadline. Go and figure it out and update me when you've made some progress." That's the level of abstraction as business owners that we need. And there's also one more thing that none of these tools handle at the moment. None of them have the operating system in the back end that stores your business context, your brand voice, your client details, your content strategy, your target audience. None of these camban tools show anything about your business. They're just managing coding sessions in a complete vacuum. So, what we need is a tool that thinks in goals, not sessions. It knows your business context and lets you manage everything from one place with minimal interaction with the terminal. So, that's exactly what I built. So, let me show you the command center. So, it sits on top of the Aentic OS that we've built out in previous videos. So, quick recap if you're new here. The Aentic OS is your entire business brain living inside Cloud Code that you can spin up in just 10 minutes using our plug-and-play templates. So, it contains your brand voice, your content strategy, all your ICP details, and it's all connected through skills that actually work together with memories of what you've previously worked on. Now, the core idea of the command center on top of the Aentic OS is really simple. Instead of managing terminal interfaces, we're going to be managing our business goals. So you can think of this as a sort of canban board for your business. But if we have a look at traditional canban, you'll see why it's different when we're considering not human workforce but a genic workforce. So say we have the traditional canban board here. We have not started and we want to actually create a content repurposing system for our business. So we would then push the task to Claude. Claude would then start the task, do a bunch of research, spin out some subtasks. They'd appear in this view here. Claude would then take on the subtask. We might at some point get to a point where we have to review the outputs. So it pass it to the review stage. This is very sequential at this point, but actually the way that we operate with agents and claw code is not sequential. It's actually iterative. So the next stage would be I give feedback. Claude goes back into progress. Claude does some more work. It then gives me back for review, back to Claude, back to me. You see how it's so iterative like this? So what we've done is just extracted the iterative nature of the clawed conversation and actually built it out into our own canban board. And on the left hand side we've got our turn which is all the stuff that we need to review. And you can see we're stacking different tasks, different goals on the your turn here. And on the right hand side we have Claude's turn. Now you'll notice here it's not a coding canban board. You've got your goals, your active task, what's in progress, and what's done or been achieved. Down here we've got the scheduled task. We've got the recent outputs and the history and we can separate it per client. But none of this talks about GitHub commits, pull requests, or anything technical. This is all about managing business goals. But we're doing that through effectively different tasks which spin up different agents in your terminal. And all we need to do is describe our goal. So we can use some of the plug-and-play commands here as part of the agent OS or we can come in and say build me a content repurposing system for my YouTube channel. We can decide what permissions to give it. The default permissions that we've already assigned in settings.j or JSON or the fully automatic i.e. dangerously skip permissions. And then we can give it a level of task. So is this a quick task? Is it a campaign with multiple deliverables where it has to break out subtasks or is this a deep build where it needs to go into way more detail with the planning? We're going to hit quick task for this. Send it to Claude. And you can see it's now in Claude's queue. So this is spinning up an instance inside Claude that we can actually click inside and see the activity as it built out with Claude. So we can see the full logs of exactly what Claude is doing inside this conversation history of the goal that we're trying to achieve. So Claude's going to work out exactly what planning level is needed for that given task. It's going to come back to us seeking feedback where required and it's going to use the skills that we've got built into the system which we'll come to. and it's come back to me because it's reflected on all of the memory that it has inside the history of the repository and said before I scope this out further are you looking to expand beyond newsletters or is this about refining or fixing the newsletter system from yesterday so it understands that yesterday we input exactly the same task to build out this content repurposing system and is starting to build on that memory yesterday we can see the full conversation history or just actually reply at a glance without needing to see and scroll through all the conversation history for demonstration I'm going to mark this one as done and it will pop into the achieved or I can drag it down here and we basically move that into already completed to close that terminal session. Now if we look at an example I created earlier when we click into a task we've got a full view of the last two messages between us which are the most important messages cuz it's what information did I give Claude? What information did it give back? So this is about a LinkedIn post on claw code and codeex. And what I want to point out here is not only can we reply and actually use our built-in commands like we can in claw code add our attachments but we can actually see all of the outputs in one place that it's produced. So if I wanted to see this LinkedIn post I could effectively look at this preview and actually scroll down and see this in a markdown preview and then take that either download it directly here or take that directly to LinkedIn. But what we're not doing is actually going through and just having a standard conversation with Claude. What we're doing is managing six plus tasks at a glance from this dashboard and able to actually get that summary view inside by clicking on each task. You can see the deeper builds have full phases that we're able to execute with many many files that link to those phases. If we're working across multiple clients, then we might want to see just the tasks or the files in that client and what's been achieved. or we just want to see across all of our projects what tasks are we looking to manage and at a glance we can see all scheduled tasks that we've built i.e. we have a monthly learnings health check so it checks all of the learnings and all the feedback that we've given it and consolidates that every month we have a weekly activity digest and a skill update check that runs at 9:00 a.m. every single day to make sure that our docs are up to date with all the skills that we've installed. And then down here we have all of our recent output. So, at a glance, we can see without having to go into the individual tasks, all of these MD files and actually click into, let's use the LinkedIn post as an example. Click into and see the preview of the markdown down here as well. So, you're able to totally abstract away from the terminal here and manage a series of tasks that flick between your turn and Claude's turn in this canban style. Now, this is definitely still under construction, by the way. It's not perfect yet, but it's becoming better by the day, and we're going to launch it for all members in the community in the next week or so once we've ironed out the bugs. And we've already alluded to this, but not only do we have this feed, which gives us an overview, but we've also got scheduled tasks. So, in Claw Code, we can actually interact with your Mac or your Windows machine and run things on a schedule. So, you can set up tasks that fire every single morning, every week, every month, whatever period you want. Say for example our skill update check. We can see at last round one day ago there was a success message and we've got a link to the output file here which gives us a log of exactly what happened. Now we can test run these. We can activate and deactivate or we can actually delete them directly from here and that will affect the underlying files in our VS Code at the base. Now next up we've got skills management. And this is something I'm really excited about because you can see all of your skills in one place. So not buried in different file folders somewhere. They're right here. So you can search through the skills. You can see we've got 21 skills installed. You can search through the skills by category and see exactly what those skills are and actually modify them from the interface. So if we go into our copywriting skill, we've got the skill.md file, but also we can see all of the reference files in there. And what we can do is actually go in directly and edit this markdown inside here. And that will affect the underlying file. And every time now the skill runs, those changes take effect. But you can see how this directly compares to actually looking at this exact skill inside the VS code terminal. So we go into doclude skills the skill.md file and then we have this markdown that's quite hard to visually understand and read versus the markdown that's actually rendered on the site. We can make a change and it will update it directly. And just to prove that I'm going to save this to test markdown copywriting test. And you can see that that's immediately rendered in here. Marketing copywriting test. and we'll go back to all skills. Now, the important thing here is we've got a meta skill creator built in that builds on anthropics skill creator and adapts skills to fit this agentic OS. So, what we can actually do is use that in the add a skill and we can either put like a GitHub reference to a specific skill we want to emulate or just give it a description or upload the skill directly and what that will do is use the skill creator to create that new skill inside here. And then let's not also forget about the documentation. So when you're writing out your claude.mmd, your readme.md, all your brand context where we store things like your community links, your personal links, your YouTube handles, stuff you use again and again are all saved into this system. And we've built this out in a similar way to OpenClaw where we've got things like the sold MD which feeds into how the agent works every single day with your tasks. And again, all super easy to edit and manage from this dashboard. And this is all done on a per client basis. So if I go back to the feed and filter by client one that has no brand context set up, then the docs are going to be relevant for client one only. So you can see there's very few docs available for client one, but they still have access to all the skills which are installed at the root level. We can switch back to root and see all of the tasks that are remaining. So that is the command center. You can think of this as one dashboard where you manage your goals instead of terminals. And like we said, we've got the business context built in. We've got scheduled tasks being built, all your skills management, your docs, multi-client support, and it's basically a way to work at a higher level and get more done faster without ever needing you to flick between multiple terminals as a business owner. So, let me wrap this up. The terminal was actually fine when we were running one claw code session at a time. But agents have actually got so good and they can handle so much more that now we need to abstract one layer higher to be able to actually leverage the productivity gains. And whether you use one of the tools I showed you like Vibe Camban or Pulsia or whether you build something custom like the command center for yourself, the point is still the same. We need to stop managing terminals and start managing goals to improve our outputs. So if you want to see how the Aentic OS works under the hood for powering this command center, then watch this next video or grab the whole system including the command center in the academy link in the description. The command center first version is launching next

---

## Timestamped Segments

**[0:00]** So, if you've been using claw code for a

**[0:01]** while, you'll remember the old problem.

**[0:03]** The output was never good enough. You

**[0:05]** had to babysit everything, and you'd end

**[0:07]** up telling it to fix its own mistakes.

**[0:10]** But now, that's completely changed. Now,

**[0:12]** the agents are actually good. They can

**[0:14]** run full tasks. They can handle real

**[0:16]** workflows and get surprisingly close to

**[0:18]** what you want. And that's created a new

**[0:20]** problem. You've got multiple agents

**[0:21]** running at once, five terminal tabs

**[0:24]** open, and you're clicking between them

**[0:26]** trying to remember what each one is

**[0:28]** doing. So every time you switch, you're

**[0:29]** losing context. And it's not claw code

**[0:32]** that's slowing you down anymore. It's

**[0:34]** the way that you're using it. So I've

**[0:35]** spent the last 3 or 4 months building

**[0:37]** full business systems inside claw code,

**[0:40]** running multiple agents in parallel,

**[0:42]** managing my business using it. And this

**[0:44]** is the bottleneck that nobody's talking

**[0:46]** about. So I went out looking for a

**[0:48]** better way. And I tried everything.

**[0:50]** T-Mox, the desktop app, Vibe Camban,

**[0:54]** Paperclip, and they all have the same

**[0:55]** issue. They're all built for developers

**[0:58]** managing code, not for business owners

**[1:00]** managing goals. So, I decided to build

**[1:02]** something different. And in this video,

**[1:04]** I'll show you what's out there, why it

**[1:06]** doesn't work, why it breaks down, and

**[1:08]** the command center that I built that

**[1:10]** actually fixes it. So, let's get

**[1:12]** straight into it. And first, let me

**[1:13]** paint a picture of what's actually

**[1:15]** happening. So, you're going to start a

**[1:16]** Claw Code session. You're working on

**[1:18]** something, whether it's a content

**[1:20]** system, a lead genen workflow, whatever

**[1:21]** it is. Claude is running, doing its

**[1:24]** thing for, let's say, 5 to 10 minutes.

**[1:26]** and your mind starts wondering. So, you

**[1:27]** decide to start another task. So, you

**[1:29]** open up another terminal tab and then

**[1:31]** another one for the next task. And

**[1:33]** before you know it, you've got five

**[1:34]** terminals open because that's the max

**[1:36]** you can handle. And you're clicking

**[1:37]** through them all going, "Which one was

**[1:39]** building my landing page? Which one was

**[1:41]** doing my research?" And this is the

**[1:42]** thing that gets me. Claude Code has

**[1:44]** honestly gotten so good at doing the

**[1:46]** work autonomously. The agents are

**[1:48]** faster. They're smarter. They can handle

**[1:50]** more complex tasks without you having to

**[1:51]** watch them. We can run them on auto mode

**[1:54]** most of the time. But our interface for

**[1:56]** actually managing those agents has not

**[1:58]** changed at all. We're still flicking

**[1:59]** between these terminal windows. And you

**[2:01]** guessed it, every time you switch

**[2:03]** between the terminals, you have to

**[2:04]** reread what's happening. You have to

**[2:06]** figure out where things are at. And all

**[2:08]** of that mental overhead does genuinely

**[2:10]** add up and it slows you down massively

**[2:12]** and stops you from doing other tasks,

**[2:14]** which let's be honest is why you wanted

**[2:16]** to actually use claw code in the first

**[2:17]** place. So the problem isn't claw code.

**[2:19]** The problem is that we need to abstract

**[2:21]** one layer higher. So we need to start

**[2:23]** managing goals and tasks not managing

**[2:25]** terminals. So naturally I went looking

**[2:28]** for solutions online and there are

**[2:30]** actually quite a few options out there.

**[2:31]** So let me walk you through what I found

**[2:33]** and these can be pulled into kind of

**[2:34]** five main approaches. So option one is

**[2:37]** T-Max. The first thing that most techled

**[2:40]** clawed code users or developers try is

**[2:43]** T-Max. And if you don't know what that

**[2:44]** is, it lets you split your terminals

**[2:46]** into multiple panes. So you can see

**[2:48]** several claw code sessions running at

**[2:50]** the same time. You can see multiple

**[2:52]** agents working side by side and have a

**[2:54]** chat to those individual agents in one

**[2:56]** window. But it still has one major

**[2:57]** limitation. You are still in that

**[2:59]** terminal. You can't see the big picture

**[3:01]** and you can't drag tasks around. You

**[3:03]** can't see progress at a glance. You're

**[3:05]** still just having a chat interface

**[3:07]** conversation back and forth. And then

**[3:08]** when you start to think about passing

**[3:10]** this to a client, imagine passing that

**[3:12]** to your non-technical client and asking

**[3:14]** them to manage the agents that you've

**[3:16]** implemented for them. So then on the

**[3:18]** other end of the spectrum, we have

**[3:19]** Anthropic's own desktop app. And

**[3:21]** honestly, the UI is really nice for this

**[3:24]** and it's improving all the time. It's

**[3:26]** clean and it gives you a proper chat

**[3:27]** interface instead of that terminal. But

**[3:29]** there are two problems with it. First,

**[3:32]** setting up things like environment

**[3:33]** variables and MCP servers is harder in

**[3:36]** the desktop app than it is files in your

**[3:38]** terminal. In the terminal, we literally

**[3:40]** just add av file with our keys or a

**[3:43]** settings.json file. And second, this is

**[3:45]** the big one, you're still managing one

**[3:47]** conversation at a time. You've got a

**[3:49]** nicer window, but it's still one window

**[3:51]** and you're flicking back and forth

**[3:52]** between your conversation topics to

**[3:54]** actually get those individual tasks

**[3:56]** done. You don't have that abstracted

**[3:57]** higher level view. Now, this is where it

**[3:59]** gets really interesting. Vibe canban is

**[4:01]** a canban board designed specifically for

**[4:03]** managing coding agents. So, you can

**[4:06]** create issues, drag them into in

**[4:08]** progress, and it automatically spins up

**[4:10]** separate claw code sessions. And the UI

**[4:12]** is genuinely very nice. But this is the

**[4:14]** key thing. It's designed for developers

**[4:17]** who are managing code. So it talks about

**[4:19]** GitHub commits, pull requests, branches,

**[4:21]** diffs, and if you're a software engineer

**[4:23]** orchestrating coding agents, that's

**[4:25]** brilliant. But if you're a business

**[4:26]** owner who just wants to say get this

**[4:28]** goal done, it's too much for your use

**[4:30]** case. And then if you want to abstract

**[4:32]** one level higher, we've got paperclipip.

**[4:34]** So paperclip is an open-source

**[4:36]** framework, and you can think of this as

**[4:37]** an operating system for running an

**[4:39]** autonomous company. So, it's set out

**[4:41]** like a traditional company. You create

**[4:42]** org charts, assign roles like CEO, CTO,

**[4:46]** and set budgets for specific roles. And

**[4:48]** conceptually, I get where this is going,

**[4:50]** but in practice, it's way too much for

**[4:52]** most of us. You don't need an org chart

**[4:54]** to write a LinkedIn post and build a

**[4:56]** landing page. You just need to get jobs

**[4:58]** done faster. So, Paperclip, although it

**[5:00]** looks brilliant, is solving a problem

**[5:02]** that most of us don't even have yet

**[5:03]** because we still want to manage those

**[5:05]** outputs. And then there are tools like

**[5:06]** claude code board claude code task

**[5:09]** viewer open clause mission control and a

**[5:12]** bunch of others and some of them are

**[5:13]** really polished but again they're all

**[5:15]** oriented around coding sessions code

**[5:18]** review developer workflows technical

**[5:20]** users only. So every tool out there is

**[5:22]** solving the same problem. How do I

**[5:24]** manage multiple coding sessions? But

**[5:26]** that's not actually the problem for

**[5:28]** business users. Their question is how do

**[5:30]** I manage multiple business goals? let

**[5:32]** Claude code figure out the rest for me,

**[5:34]** but still have a handle on and maintain

**[5:36]** and supervise the outputs. And this is

**[5:38]** the gap that none of these tools fill.

**[5:40]** So, let me explain what it's actually

**[5:42]** missing. Every tool I just showed

**[5:44]** started from the bottom up. So, they

**[5:45]** start with the session in the terminal.

**[5:47]** They start with the code and then they

**[5:48]** try to add a project management layer on

**[5:50]** top of it. But what we actually need is

**[5:52]** the opposite. We need to start from the

**[5:54]** top and work our way downwards. So we

**[5:56]** need to start with the goal like I want

**[5:57]** to build a lead generation system and

**[5:59]** then let the system figure out what

**[6:01]** sessions to spin up, how in-depth the

**[6:03]** planning should be, how many agents are

**[6:05]** needed, what skills to use and how to

**[6:08]** get it done, i.e. all the technical

**[6:10]** overhead. And it's much like hiring a

**[6:11]** competent employee. You give that

**[6:13]** employee a goal. You say, "Here's the

**[6:15]** deadline. Go and figure it out and

**[6:16]** update me when you've made some

**[6:17]** progress." That's the level of

**[6:19]** abstraction as business owners that we

**[6:20]** need. And there's also one more thing

**[6:22]** that none of these tools handle at the

**[6:23]** moment. None of them have the operating

**[6:25]** system in the back end that stores your

**[6:27]** business context, your brand voice, your

**[6:29]** client details, your content strategy,

**[6:31]** your target audience. None of these

**[6:33]** camban tools show anything about your

**[6:35]** business. They're just managing coding

**[6:37]** sessions in a complete vacuum. So, what

**[6:39]** we need is a tool that thinks in goals,

**[6:41]** not sessions. It knows your business

**[6:43]** context and lets you manage everything

**[6:45]** from one place with minimal interaction

**[6:47]** with the terminal. So, that's exactly

**[6:49]** what I built. So, let me show you the

**[6:51]** command center. So, it sits on top of

**[6:53]** the Aentic OS that we've built out in

**[6:55]** previous videos. So, quick recap if

**[6:57]** you're new here. The Aentic OS is your

**[6:59]** entire business brain living inside

**[7:01]** Cloud Code that you can spin up in just

**[7:04]** 10 minutes using our plug-and-play

**[7:05]** templates. So, it contains your brand

**[7:07]** voice, your content strategy, all your

**[7:09]** ICP details, and it's all connected

**[7:11]** through skills that actually work

**[7:13]** together with memories of what you've

**[7:15]** previously worked on. Now, the core idea

**[7:16]** of the command center on top of the

**[7:19]** Aentic OS is really simple. Instead of

**[7:21]** managing terminal interfaces, we're

**[7:23]** going to be managing our business goals.

**[7:24]** So you can think of this as a sort of

**[7:27]** canban board for your business. But if

**[7:29]** we have a look at traditional canban,

**[7:30]** you'll see why it's different when we're

**[7:32]** considering not human workforce but a

**[7:34]** genic workforce. So say we have the

**[7:35]** traditional canban board here. We have

**[7:37]** not started and we want to actually

**[7:39]** create a content repurposing system for

**[7:41]** our business. So we would then push the

**[7:43]** task to Claude. Claude would then start

**[7:45]** the task, do a bunch of research, spin

**[7:47]** out some subtasks. They'd appear in this

**[7:49]** view here. Claude would then take on the

**[7:50]** subtask. We might at some point get to a

**[7:52]** point where we have to review the

**[7:53]** outputs. So it pass it to the review

**[7:55]** stage. This is very sequential at this

**[7:57]** point, but actually the way that we

**[7:59]** operate with agents and claw code is not

**[8:01]** sequential. It's actually iterative. So

**[8:04]** the next stage would be I give feedback.

**[8:06]** Claude goes back into progress. Claude

**[8:08]** does some more work. It then gives me

**[8:10]** back for review, back to Claude, back to

**[8:12]** me. You see how it's so iterative like

**[8:14]** this? So what we've done is just

**[8:16]** extracted the iterative nature of the

**[8:17]** clawed conversation and actually built

**[8:20]** it out into our own canban board. And on

**[8:22]** the left hand side we've got our turn

**[8:24]** which is all the stuff that we need to

**[8:26]** review. And you can see we're stacking

**[8:27]** different tasks, different goals on the

**[8:29]** your turn here. And on the right hand

**[8:31]** side we have Claude's turn. Now you'll

**[8:33]** notice here it's not a coding canban

**[8:35]** board. You've got your goals, your

**[8:37]** active task, what's in progress, and

**[8:40]** what's done or been achieved. Down here

**[8:41]** we've got the scheduled task. We've got

**[8:43]** the recent outputs and the history and

**[8:45]** we can separate it per client. But none

**[8:47]** of this talks about GitHub commits, pull

**[8:50]** requests, or anything technical. This is

**[8:52]** all about managing business goals. But

**[8:53]** we're doing that through effectively

**[8:55]** different tasks which spin up different

**[8:57]** agents in your terminal. And all we need

**[8:59]** to do is describe our goal. So we can

**[9:01]** use some of the plug-and-play commands

**[9:02]** here as part of the agent OS or we can

**[9:04]** come in and say build me a content

**[9:06]** repurposing system for my YouTube

**[9:08]** channel. We can decide what permissions

**[9:09]** to give it. The default permissions that

**[9:11]** we've already assigned in settings.j or

**[9:12]** JSON or the fully automatic i.e.

**[9:14]** dangerously skip permissions. And then

**[9:16]** we can give it a level of task. So is

**[9:18]** this a quick task? Is it a campaign with

**[9:20]** multiple deliverables where it has to

**[9:21]** break out subtasks or is this a deep

**[9:24]** build where it needs to go into way more

**[9:26]** detail with the planning? We're going to

**[9:27]** hit quick task for this. Send it to

**[9:29]** Claude. And you can see it's now in

**[9:30]** Claude's queue. So this is spinning up

**[9:32]** an instance inside Claude that we can

**[9:34]** actually click inside and see the

**[9:36]** activity as it built out with Claude. So

**[9:38]** we can see the full logs of exactly what

**[9:40]** Claude is doing inside this conversation

**[9:42]** history of the goal that we're trying to

**[9:44]** achieve. So Claude's going to work out

**[9:46]** exactly what planning level is needed

**[9:48]** for that given task. It's going to come

**[9:50]** back to us seeking feedback where

**[9:52]** required and it's going to use the

**[9:54]** skills that we've got built into the

**[9:56]** system which we'll come to. and it's

**[9:57]** come back to me because it's reflected

**[9:59]** on all of the memory that it has inside

**[10:02]** the history of the repository and said

**[10:04]** before I scope this out further are you

**[10:06]** looking to expand beyond newsletters or

**[10:08]** is this about refining or fixing the

**[10:09]** newsletter system from yesterday so it

**[10:11]** understands that yesterday we input

**[10:13]** exactly the same task to build out this

**[10:15]** content repurposing system and is

**[10:17]** starting to build on that memory

**[10:18]** yesterday we can see the full

**[10:19]** conversation history or just actually

**[10:21]** reply at a glance without needing to see

**[10:24]** and scroll through all the conversation

**[10:26]** history for demonstration I'm going to

**[10:27]** mark this one as done and it will pop

**[10:29]** into the achieved or I can drag it down

**[10:31]** here and we basically move that into

**[10:34]** already completed to close that terminal

**[10:36]** session. Now if we look at an example I

**[10:38]** created earlier when we click into a

**[10:40]** task we've got a full view of the last

**[10:42]** two messages between us which are the

**[10:44]** most important messages cuz it's what

**[10:46]** information did I give Claude? What

**[10:47]** information did it give back? So this is

**[10:49]** about a LinkedIn post on claw code and

**[10:52]** codeex. And what I want to point out

**[10:53]** here is not only can we reply and

**[10:55]** actually use our built-in commands like

**[10:57]** we can in claw code add our attachments

**[11:00]** but we can actually see all of the

**[11:01]** outputs in one place that it's produced.

**[11:03]** So if I wanted to see this LinkedIn post

**[11:05]** I could effectively look at this preview

**[11:07]** and actually scroll down and see this in

**[11:09]** a markdown preview and then take that

**[11:11]** either download it directly here or take

**[11:13]** that directly to LinkedIn. But what

**[11:15]** we're not doing is actually going

**[11:17]** through and just having a standard

**[11:18]** conversation with Claude. What we're

**[11:20]** doing is managing six plus tasks at a

**[11:23]** glance from this dashboard and able to

**[11:26]** actually get that summary view inside by

**[11:28]** clicking on each task. You can see the

**[11:30]** deeper builds have full phases that

**[11:32]** we're able to execute with many many

**[11:34]** files that link to those phases. If

**[11:36]** we're working across multiple clients,

**[11:38]** then we might want to see just the tasks

**[11:40]** or the files in that client and what's

**[11:42]** been achieved. or we just want to see

**[11:43]** across all of our projects what tasks

**[11:45]** are we looking to manage and at a glance

**[11:47]** we can see all scheduled tasks that

**[11:49]** we've built i.e. we have a monthly

**[11:51]** learnings health check so it checks all

**[11:53]** of the learnings and all the feedback

**[11:54]** that we've given it and consolidates

**[11:55]** that every month we have a weekly

**[11:57]** activity digest and a skill update check

**[11:59]** that runs at 9:00 a.m. every single day

**[12:01]** to make sure that our docs are up to

**[12:03]** date with all the skills that we've

**[12:04]** installed. And then down here we have

**[12:05]** all of our recent output. So, at a

**[12:07]** glance, we can see without having to go

**[12:09]** into the individual tasks, all of these

**[12:11]** MD files and actually click into, let's

**[12:14]** use the LinkedIn post as an example.

**[12:16]** Click into and see the preview of the

**[12:18]** markdown down here as well. So, you're

**[12:19]** able to totally abstract away from the

**[12:21]** terminal here and manage a series of

**[12:24]** tasks that flick between your turn and

**[12:26]** Claude's turn in this canban style. Now,

**[12:28]** this is definitely still under

**[12:29]** construction, by the way. It's not

**[12:30]** perfect yet, but it's becoming better by

**[12:32]** the day, and we're going to launch it

**[12:34]** for all members in the community in the

**[12:36]** next week or so once we've ironed out

**[12:37]** the bugs. And we've already alluded to

**[12:39]** this, but not only do we have this feed,

**[12:41]** which gives us an overview, but we've

**[12:43]** also got scheduled tasks. So, in Claw

**[12:45]** Code, we can actually interact with your

**[12:47]** Mac or your Windows machine and run

**[12:49]** things on a schedule. So, you can set up

**[12:51]** tasks that fire every single morning,

**[12:53]** every week, every month, whatever period

**[12:54]** you want. Say for example our skill

**[12:56]** update check. We can see at last round

**[12:59]** one day ago there was a success message

**[13:01]** and we've got a link to the output file

**[13:03]** here which gives us a log of exactly

**[13:05]** what happened. Now we can test run

**[13:06]** these. We can activate and deactivate or

**[13:09]** we can actually delete them directly

**[13:10]** from here and that will affect the

**[13:11]** underlying files in our VS Code at the

**[13:14]** base. Now next up we've got skills

**[13:16]** management. And this is something I'm

**[13:17]** really excited about because you can see

**[13:19]** all of your skills in one place. So not

**[13:21]** buried in different file folders

**[13:23]** somewhere. They're right here. So you

**[13:25]** can search through the skills. You can

**[13:26]** see we've got 21 skills installed. You

**[13:28]** can search through the skills by

**[13:29]** category and see exactly what those

**[13:31]** skills are and actually modify them from

**[13:33]** the interface. So if we go into our

**[13:35]** copywriting skill, we've got the

**[13:37]** skill.md file, but also we can see all

**[13:40]** of the reference files in there. And

**[13:42]** what we can do is actually go in

**[13:43]** directly and edit this markdown inside

**[13:45]** here. And that will affect the

**[13:47]** underlying file. And every time now the

**[13:49]** skill runs, those changes take effect.

**[13:51]** But you can see how this directly

**[13:53]** compares to actually looking at this

**[13:55]** exact skill inside the VS code terminal.

**[13:59]** So we go into doclude skills the

**[14:01]** skill.md file and then we have this

**[14:03]** markdown that's quite hard to visually

**[14:05]** understand and read versus the markdown

**[14:07]** that's actually rendered on the site. We

**[14:09]** can make a change and it will update it

**[14:10]** directly. And just to prove that I'm

**[14:12]** going to save this to test markdown

**[14:14]** copywriting test. And you can see that

**[14:16]** that's immediately rendered in here.

**[14:18]** Marketing copywriting test. and we'll go

**[14:20]** back to all skills. Now, the important

**[14:22]** thing here is we've got a meta skill

**[14:24]** creator built in that builds on

**[14:26]** anthropics skill creator and adapts

**[14:28]** skills to fit this agentic OS. So, what

**[14:31]** we can actually do is use that in the

**[14:33]** add a skill and we can either put like a

**[14:35]** GitHub reference to a specific skill we

**[14:37]** want to emulate or just give it a

**[14:38]** description or upload the skill directly

**[14:41]** and what that will do is use the skill

**[14:42]** creator to create that new skill inside

**[14:44]** here. And then let's not also forget

**[14:46]** about the documentation. So when you're

**[14:48]** writing out your claude.mmd, your

**[14:50]** readme.md, all your brand context where

**[14:52]** we store things like your community

**[14:54]** links, your personal links, your YouTube

**[14:56]** handles, stuff you use again and again

**[14:58]** are all saved into this system. And

**[14:59]** we've built this out in a similar way to

**[15:02]** OpenClaw where we've got things like the

**[15:04]** sold MD which feeds into how the agent

**[15:06]** works every single day with your tasks.

**[15:08]** And again, all super easy to edit and

**[15:10]** manage from this dashboard. And this is

**[15:12]** all done on a per client basis. So if I

**[15:14]** go back to the feed and filter by client

**[15:16]** one that has no brand context set up,

**[15:18]** then the docs are going to be relevant

**[15:20]** for client one only. So you can see

**[15:22]** there's very few docs available for

**[15:23]** client one, but they still have access

**[15:24]** to all the skills which are installed at

**[15:27]** the root level. We can switch back to

**[15:28]** root and see all of the tasks that are

**[15:30]** remaining. So that is the command

**[15:32]** center. You can think of this as one

**[15:33]** dashboard where you manage your goals

**[15:35]** instead of terminals. And like we said,

**[15:37]** we've got the business context built in.

**[15:39]** We've got scheduled tasks being built,

**[15:41]** all your skills management, your docs,

**[15:43]** multi-client support, and it's basically

**[15:44]** a way to work at a higher level and get

**[15:47]** more done faster without ever needing

**[15:49]** you to flick between multiple terminals

**[15:51]** as a business owner. So, let me wrap

**[15:53]** this up. The terminal was actually fine

**[15:55]** when we were running one claw code

**[15:56]** session at a time. But agents have

**[15:58]** actually got so good and they can handle

**[16:00]** so much more that now we need to

**[16:01]** abstract one layer higher to be able to

**[16:04]** actually leverage the productivity

**[16:05]** gains. And whether you use one of the

**[16:07]** tools I showed you like Vibe Camban or

**[16:09]** Pulsia or whether you build something

**[16:11]** custom like the command center for

**[16:12]** yourself, the point is still the same.

**[16:15]** We need to stop managing terminals and

**[16:16]** start managing goals to improve our

**[16:18]** outputs. So if you want to see how the

**[16:20]** Aentic OS works under the hood for

**[16:22]** powering this command center, then watch

**[16:24]** this next video or grab the whole system

**[16:26]** including the command center in the

**[16:28]** academy link in the description. The

**[16:29]** command center first version is

**[16:31]** launching next
