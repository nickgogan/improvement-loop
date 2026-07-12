# Transcript: Every Claude Code Workflow Explained (& When to Use Each)

**URL:** https://www.youtube.com/watch?v=38t5UBCa4OI
**Segments:** 562
**Channel:** Simon Scrapes
**Duration:** 17:49
**Uploaded:** 2026-04-07

---

## Full Text

If you're still using claw code one conversation at a time, you're using it wrong. And this video is going to change how you work with it. So, at the moment, you give it a task, you wait for the result, and then you move on to the next task. Everything's running at one time. But that's not how you'd run a team. You'd run teams in parallel, and you'd bring in specialists when required. And claw code is built to work exactly like that, too. But most people aren't using it that way. So, in this video, you'll see five ways on how to actually use it, from simple setups to fully hands-off workflows. so that you can stop working in one conversation and start saving some serious time. So, let's get into it. And I'll start off with something that surprised me when I first found out about it. So, every single time you use clog code, even in a basic conversation, it's already using a version of these patterns that we'll run through behind the scenes. So, it actually has already built-in sub aents that it uses automatically without you having to tell it to. So, there are actually three built-in sub aents baked into claw code. The first one is called explore. And explore is basically a fast cheap scout. So it runs on haiku which is anthropic's fastest and cheapest model. And all it can do is read your files. So it can search your files. It can look through folder structures. But it's read only. It can't change anything. So when you ask Claude something like how does my user authentication work in this project? Then Claude will often spin up an explore agent behind the scenes without you asking to. It will go off read through your files with its own set of context window and it will come back with a summary and your main conversation therefore can stay clean. It doesn't bloat the context. And you'll actually see this inside the terminal when you run these tasks. You'll see it pop up in the terminal as the explore tool. The second one is similar. It's called plan, but it specifically activates when you're in plan mode. So if you type / plan or hit shift tab twice to enter plan mode, then Claude is going to use the plan sub agent to research your codebase before it presents you with a strategy. Again, separate context window, readonly. And the third one that they've implemented behind the scenes is general purpose. And this, as it sounds, is quite general purpose. So, it's the one that does the heavy lifting. It runs on Sonnet and it has full tool access. So, it can read and write. And Claude uses it for complex multi-step tasks. So, if you're asking Claude to do something that requires both exploring the code base and making changes across multiple files, that's when it will often delegate that to a general purpose sub agent. And the key thing here is you've not told it to do anything. And Claude is deciding when to use these automatically. It's looking at the complexity of your task and routting it to the right sub aent. And all of those sub aents run with their own context window so that your main conversation never gets bloated with all the reading and searching of those files. So even before we get into the five patterns, just know that claw code is already doing some of this work for you. But when you understand the full spectrum of the patterns, you can take control and get so much more out of it. Okay. So with that context, let's start at the beginning with pattern one. And sequential flow is exactly as it sounds. You open a terminal, you start a claw code session, and every task you give it builds on the last one. So we've got you here. We assign a task. We then move to the next task. Once task one is finished, move to the next. Move to the next. And our shared context is growing over time. So it's building on the context that we've been given it throughout the different tasks. So it might be something like build me a landing page. Claude then builds it as task one or a first version of it. You say add a hero image to page one. Add a contact form. All of these are different tasks that build on the first task. And the output of task one can feed into task two. And the outputs of task one and two can feed into task three because it's all stored in the context window. And this might seem like you're not using any sub aents, but remember that Claude has those built-in sub aents. So even in this single conversation, Claude might spin up its explore plan or general purpose agents that help by actually offloading some context at the right time to get stuff done faster or more effectively on your behalf. And you'll see these pop up in the terminal, but from your perspective, it's still just one conversation flow between you and Claude. Now, the really important thing to understand about sequential flow is that it has a ceiling and that ceiling is dictated by the context window and that's shown by the little green bar on the bottom of the terminal. So the longer you work in that one session, the more the context is going to accumulate. And at that point, Claude starts forgetting things or not being able to find things, which is what we call context rot. So this is where skills and commands become super valuable because if you've got a well structured claude.md and some well ststructured skills that are described well, then Claude is able to load in that skill and any reference files at the right time and then offload it at the right time also to not bloat the conversation window. And then using commands like /clear and /compact will help you actually keep the summary of the conversation in the context. But eventually with this you're going to hit a wall and that's when we need to move to pattern two. And pattern two is called the operator. And this time you are acting as an orchestrator. So instead of running one clawed session, you're going to open up multiple terminal windows. You might have found yourself doing this already to get things done quickly. Each has its own clawed instance. So you can treat these like separate agents. terminal 1 2 3 and four completely separate agents. They have their own context window and therefore you can give them specific context for a specific task. So this time let's say you're building out a SAS app. You need a new onboarding flow built. You also need your checkout bug fix and you want to experiment with a new design for let's say your user settings page. All of these tasks that we've mentioned don't depend on each other. And that's one of the reasons why we can actually orchestrate these in completely separate terminals that don't blow each other's context because there's no connection between those terminals. We are purely coordinating. So you open three terminals like this inside VS Code. And Claude actually has now a built-in flag to do this much easier. So in the first time we type in claude-w which is important new onboarding flow. The second one claude-w checkout bug and the third one claude-wesign user settings. And you'll see that in the project folder here, we've now opened up what's called a work tree where we've got new onboarding flow, fix checkout bug, and redesign user settings. And now if we go into our doc cloud folder, we've effectively got these different work trees, which is a separate copy of your project with its own branch, and it drops it straight into the claw code session. Each one in its own isolated workspace, and they can't interfere with each other. So they all have a clean context window, so there's no context rot from other tasks. and us as the operator are the ones coordinating the efforts between these different terminals here. So you're probably at this point checking in on the different terminals, the different tasks going on. You're copy and pasting findings from one to another if you're needed and then you're going to have to decide when each one is done and when you want to merge that back into the main project. But this is a massive upgrade from this sequential flow because actually we can get multiple things done in parallel as long as they're not dependent on each other. But if they do depend on each other, then this flow isn't going to work for us. And here's the nice touch about closing a work tree session. As soon as we close this window, Claude is going to handle the cleanup for us. So if nothing's changed, it removes that workspace automatically. But if there is work to keep, then it's going to ask you what to do. And you can see as I close these sessions, they disappear from the work trees up here. So the operator pattern is you running multiple clawed sessions in parallel, each with its own isolated workspace, but you're still the one coordinating. So, it's perfect for independent tasks where you want maximum control and clean context windows where they will not interfere with each other. Now, the operator pattern is great, but as you'll have probably noticed, you can only manage a certain number of terminals at any one point. Four to five terminals and you're flicking between those terminals, it becomes really difficult checking in on all of the sessions. So, what if the claw could actually handle the parallel tasks itself? So, pattern three then is the split and merge. And this is where it gets really interesting because the core idea is that within a single claw code session one terminal claw itself can split work across multiple sub aents that then run in parallel. So if you're thinking about all four of these terminals we could effectively spin off multiple sub aents inside each terminal to get more done quicker. And then effectively at the end it's going to merge all the results back into the main agent so that you can reap the rewards. And if you remember those built-in sub aents I mentioned earlier, explore, plan, and general purpose. Those are good examples of that. But you're not limited to just those. You can create your own custom sub aents inside your doc folder. And Claude can spin up multiple of them at the same time. And here is how that works in practice. You give Claude a task. Claude is going to analyze that task and realize that it can be broken down into independent pieces. It will then fan out into multiple sub aents, each one running in its own context window. and each one focused on their specific piece of work. And then when it's all done, it will merge all those results automatically and give you the final output. So, a lot is happening in the background here that we don't have to manually tell it to do. So, let's say you ask Claude to research five different competitors for a client proposal. Instead of researching them one by one, which could take ages if we ran it in that sequential flow pattern one, Claude can spin up five sub agents, one per competitor, and they all research simultaneously. So each one is going to come back with their findings and the main agent is going to synthesize the five findings into one single report. And Boris Churnney even one of the creators of core code has talked about sometimes spinning up 15 sub aents at a time to get things done. But actually the limit on this is 10 at once. So 10 sub aents at once. Claude will actually cue any additional tasks as additional sub aents. But here's the critical limitation here. Sub agents can only report back to the main agent. So they can't actually talk to each other. So sub agent one and sub agent 3 have no idea what each other are doing. It's this like hub and spoke methodology where the main agent or our main instance where we're interacting with Claude is acting as the hub and it's receiving information back and forth from that sub agent. And if you've ever used the framework GSD or get done by Tash, this is like a framework I'd highly recommend for comprehensive projects. is basically a planning framework that will split your initial project brief into subtasks and execute on those subtasks for so it's designed for big projects but not in an enterprise fashion. We can look at their agents inside their agents folder. They've got quite a few agents in here and actually what you can do is go into the agents listed and see exactly like we do with skills the name the description. So researches a single gray area decision and returns a structured comparison table with rationale. So we're effectively giving this agent a role to do and a specific set of context that it goes out and performs a certain process as well as giving that agent a certain set of tools that it actually has access to. Now Claude will read the name of all agents in our docord folder and decide when it's suitable to offload a task to those sub agents. I.e. it will automatically use it when it thinks the task matches the description. Or you can specifically say I want to use the advisor researcher sub agent in this task. And one of the most powerful applications of this pattern is the build a validator chain. So you have one sub agent build something and then you have another sub agent actually review it. But what that requires is the sub aent one to build it first, pass it back to the main agent, pass that to the second sub aent through here and then that passes the results back to the main agent. So you can see because they can't communicate with each other that we're actually orchestrating it through this main agent. But you can effectively get a built-in quality check without doing any of the reviewing yourself by using that builder validator chain. So split and merge is claude doing the parallelization for you within a single session. So it can fan out work to those sub aents and merge the results for you. And again they keep your context window clean. So this is really powerful. So split and merge is awesome but it has one limitation. Sub agents can't talk to each other. So everything has to funnel through the main agent and for some tasks that is a genuine bottleneck. So what if your researcher agent needs to check in with your reviewer agent? Or what if you have a front-end developer that needs to coordinate with a back-end developer. So this is where the fourth pattern comes in, which is agent teams. An agent team is effectively a team of agents, as it sounds, that can share findings, challenge each other, and adapt together. So that the way that they share information is through a shared task list. So they're no longer interacting with the team lead, which is our main orchestration window. They're interacting with that shared task list. Agent one understands what tasks agent two is doing. And vice versa, they can send messages between the agents. And it's the most advanced coordination pattern. It's the newest addition to CL code and it is genuinely a gamecher for complex projects, but it should only be used in complex projects because the token usage is extremely high when you've got cross collaboration between the agents. Now, this is completely still experimental. It shipped with Opus 4.6 as a research preview. So, you need to still enable it by adding a flag to your settings.json, which is claw code experimental agent teams one. and you need to add that as an environment variable in your settings.json. But once it's enabled, you just tell Claude in your prompt that you want to use an agent team. So you must still specify that you want to use an agent team, not like sub agents where it will choose those automatically. You go in, you describe the task you want, you describe the team structure or Claude will actually determine the team structure itself and Claude will then create that team, spawn the teammates and coordinate the work. And in your terminal, you can actually navigate between the teammates using shift up and shift down. And you can message directly any teammate and bypass this team lead entirely or you can talk directly to the team lead. Now, as I mentioned, they use significantly more tokens because we've got this back and forth between the shared task list, the team lead, between the agents. And each teammate is its full CL code instance with its own context window again. So, it's got a portion of the main context passed in it from that shared task list and the team lead. And they roughly estimate it's going to be four to seven times more tokens than a single session when you're actually using agent teams. And the thing that actually matters here is you don't need agent teams for most of your work. You should actually only reach for them when sub agents or even a single session couldn't do the job. So say you're trying to build out a complex SAS application where you have a front-end developer, a backend developer, and then a testing developer that spins up tests and needs to communicate to agent one and two as they build. That is an example where you would actually want an agent team to save from back and forth between the orchestration layer. But a lot of people in the community are just saying that actually this is just a way to produce large quantities of work very quickly which isn't necessarily a good thing. You still need the work to be the right work. So it's powerful but expensive. So only reach for this when the task genuinely needs that cross collaboration. So patterns 1 through 4 all have one thing in common. You're there in the terminal. you're either typing, coordinating, or at least watching the task. But what if you didn't need to be there at all? So, this brings us on to the last pattern, which is Claude working without you. So, this is the dream of autonomous workflows, where you don't need to be in the loop. You just set a task, you walk away, and you come back to the results. And this is called headless. And it's where Claude code goes from being a tool you sit with to a team member that's going to go and work independently. This requires you having no conversation back and forth, no terminal window open, and no human in the loop at all. So when we're running this, we're using the -p flag. So we're saying Claude-P, and we're entering a prompt after the P flag. So we're saying, Claude, process this prompt. We don't want any interaction, no approvals. You've got full permissions. Just go get it done and return to me the result when you're finished. And that on its own is kind of iterating with that task cla prompt and will give us that report.json. But when it gets really groundbreaking, when it gets really powerful is like when you plug this into other systems. So if you plug this in to your Windows or your Mac scheduling function, your cron functionality that can say at 7 a.m. every day, fire in this command to my terminal and then Claude goes and iterates and gets the report and sends it back to you. That is when it genuinely becomes a gamecher because then what we're doing is actually creating workflows that can run on a schedule without your input. So it could be review yesterday's work and write a summary to a morning report.mmd. So when Claude wakes up, it's going to read all the work you did yesterday, analyze them, write the report, and then you just have to go and look at the output before you've even done anything. You didn't open a terminal, you didn't even type a prompt in. It basically just happened. Or say you're actually running content for your business. You could have a script that pulls your latest video transcript, runs it through Claude with a specific prompt, gets you back a set of social media posts, saved to a file that you can then just schedule automatically. And you can chain these together. You can add skills into the prompts that invoke specific skills. And this is all completely automated. Now, the big limitation in this is trust. You're not asking for an iterative conversation. You're giving Claude autonomy to do things on your behalf. So, you're not checking each step. So, this works best for tasks where the output is extremely easy to verify. At the moment, you probably don't want to go headless on anything that's hard to undo, but you can actually put guard rails on this as well. If you want it to only read and not write, for example, we can do d-allowed tools and then make sure that we add specific things that it can do. And some people in the community have taken this even further with things like the Ralph loop, which keeps feeding the same prompt back in so that Claude iterates on its own work until it gets it right. And each time it iterates, it understands what has been done in the last cycle. And people have actually been using this to ship entire projects overnight. So this is brilliant. This is like claude working without you. You set a task, you walk away, and you come back for the results. But like we said, it's best for batch processing things and anything where the output is really easy to verify. So there you have it, five agentic patterns for claw code. And if you want to go deeper on any of these or on building skills, creating custom sub agents, how to structure your claw MD and actually put these patterns into practice with real projects, then check out the first link to the Agentic Academy in the description below. We've got a full claw code track where we build this stuff step by step. And let me know in the comments which pattern you're looking forward to trying. And if this did save you the time of figuring out this yourself, then I'd really appreciate a like and subscribe. Thanks so much for watching.

---

## Timestamped Segments

**[0:00]** If you're still using claw code one

**[0:01]** conversation at a time, you're using it

**[0:03]** wrong. And this video is going to change

**[0:06]** how you work with it. So, at the moment,

**[0:08]** you give it a task, you wait for the

**[0:09]** result, and then you move on to the next

**[0:11]** task. Everything's running at one time.

**[0:13]** But that's not how you'd run a team.

**[0:14]** You'd run teams in parallel, and you'd

**[0:16]** bring in specialists when required. And

**[0:18]** claw code is built to work exactly like

**[0:20]** that, too. But most people aren't using

**[0:22]** it that way. So, in this video, you'll

**[0:23]** see five ways on how to actually use it,

**[0:26]** from simple setups to fully hands-off

**[0:28]** workflows. so that you can stop working

**[0:30]** in one conversation and start saving

**[0:32]** some serious time. So, let's get into

**[0:34]** it. And I'll start off with something

**[0:36]** that surprised me when I first found out

**[0:38]** about it. So, every single time you use

**[0:40]** clog code, even in a basic conversation,

**[0:43]** it's already using a version of these

**[0:44]** patterns that we'll run through behind

**[0:46]** the scenes. So, it actually has already

**[0:48]** built-in sub aents that it uses

**[0:50]** automatically without you having to tell

**[0:52]** it to. So, there are actually three

**[0:53]** built-in sub aents baked into claw code.

**[0:56]** The first one is called explore. And

**[0:58]** explore is basically a fast cheap scout.

**[1:01]** So it runs on haiku which is anthropic's

**[1:03]** fastest and cheapest model. And all it

**[1:05]** can do is read your files. So it can

**[1:07]** search your files. It can look through

**[1:09]** folder structures. But it's read only.

**[1:11]** It can't change anything. So when you

**[1:12]** ask Claude something like how does my

**[1:14]** user authentication work in this

**[1:16]** project? Then Claude will often spin up

**[1:17]** an explore agent behind the scenes

**[1:19]** without you asking to. It will go off

**[1:21]** read through your files with its own set

**[1:23]** of context window and it will come back

**[1:26]** with a summary and your main

**[1:27]** conversation therefore can stay clean.

**[1:29]** It doesn't bloat the context. And you'll

**[1:31]** actually see this inside the terminal

**[1:32]** when you run these tasks. You'll see it

**[1:34]** pop up in the terminal as the explore

**[1:36]** tool. The second one is similar. It's

**[1:38]** called plan, but it specifically

**[1:39]** activates when you're in plan mode. So

**[1:41]** if you type / plan or hit shift tab

**[1:43]** twice to enter plan mode, then Claude is

**[1:45]** going to use the plan sub agent to

**[1:47]** research your codebase before it

**[1:48]** presents you with a strategy. Again,

**[1:50]** separate context window, readonly. And

**[1:52]** the third one that they've implemented

**[1:53]** behind the scenes is general purpose.

**[1:55]** And this, as it sounds, is quite general

**[1:57]** purpose. So, it's the one that does the

**[1:58]** heavy lifting. It runs on Sonnet and it

**[2:01]** has full tool access. So, it can read

**[2:03]** and write. And Claude uses it for

**[2:04]** complex multi-step tasks. So, if you're

**[2:07]** asking Claude to do something that

**[2:09]** requires both exploring the code base

**[2:10]** and making changes across multiple

**[2:12]** files, that's when it will often

**[2:13]** delegate that to a general purpose sub

**[2:16]** agent. And the key thing here is you've

**[2:17]** not told it to do anything. And Claude

**[2:19]** is deciding when to use these

**[2:20]** automatically. It's looking at the

**[2:22]** complexity of your task and routting it

**[2:24]** to the right sub aent. And all of those

**[2:25]** sub aents run with their own context

**[2:27]** window so that your main conversation

**[2:29]** never gets bloated with all the reading

**[2:31]** and searching of those files. So even

**[2:33]** before we get into the five patterns,

**[2:35]** just know that claw code is already

**[2:37]** doing some of this work for you. But

**[2:38]** when you understand the full spectrum of

**[2:40]** the patterns, you can take control and

**[2:42]** get so much more out of it. Okay. So

**[2:44]** with that context, let's start at the

**[2:46]** beginning with pattern one. And

**[2:47]** sequential flow is exactly as it sounds.

**[2:49]** You open a terminal, you start a claw

**[2:52]** code session, and every task you give it

**[2:54]** builds on the last one. So we've got you

**[2:56]** here. We assign a task. We then move to

**[2:58]** the next task. Once task one is

**[2:59]** finished, move to the next. Move to the

**[3:01]** next. And our shared context is growing

**[3:03]** over time. So it's building on the

**[3:05]** context that we've been given it

**[3:07]** throughout the different tasks. So it

**[3:09]** might be something like build me a

**[3:10]** landing page. Claude then builds it as

**[3:12]** task one or a first version of it. You

**[3:14]** say add a hero image to page one. Add a

**[3:17]** contact form. All of these are different

**[3:18]** tasks that build on the first task. And

**[3:20]** the output of task one can feed into

**[3:22]** task two. And the outputs of task one

**[3:25]** and two can feed into task three because

**[3:26]** it's all stored in the context window.

**[3:28]** And this might seem like you're not

**[3:29]** using any sub aents, but remember that

**[3:31]** Claude has those built-in sub aents. So

**[3:33]** even in this single conversation, Claude

**[3:36]** might spin up its explore plan or

**[3:37]** general purpose agents that help by

**[3:39]** actually offloading some context at the

**[3:42]** right time to get stuff done faster or

**[3:44]** more effectively on your behalf. And

**[3:46]** you'll see these pop up in the terminal,

**[3:47]** but from your perspective, it's still

**[3:49]** just one conversation flow between you

**[3:50]** and Claude. Now, the really important

**[3:52]** thing to understand about sequential

**[3:54]** flow is that it has a ceiling and that

**[3:56]** ceiling is dictated by the context

**[3:57]** window and that's shown by the little

**[3:58]** green bar on the bottom of the terminal.

**[4:00]** So the longer you work in that one

**[4:02]** session, the more the context is going

**[4:03]** to accumulate. And at that point, Claude

**[4:06]** starts forgetting things or not being

**[4:07]** able to find things, which is what we

**[4:09]** call context rot. So this is where

**[4:11]** skills and commands become super

**[4:12]** valuable because if you've got a well

**[4:13]** structured claude.md and some well

**[4:15]** ststructured skills that are described

**[4:17]** well, then Claude is able to load in

**[4:19]** that skill and any reference files at

**[4:21]** the right time and then offload it at

**[4:23]** the right time also to not bloat the

**[4:25]** conversation window. And then using

**[4:26]** commands like /clear and /compact will

**[4:29]** help you actually keep the summary of

**[4:31]** the conversation in the context. But

**[4:33]** eventually with this you're going to hit

**[4:35]** a wall and that's when we need to move

**[4:37]** to pattern two. And pattern two is

**[4:39]** called the operator. And this time you

**[4:41]** are acting as an orchestrator. So

**[4:43]** instead of running one clawed session,

**[4:45]** you're going to open up multiple

**[4:46]** terminal windows. You might have found

**[4:47]** yourself doing this already to get

**[4:49]** things done quickly. Each has its own

**[4:50]** clawed instance. So you can treat these

**[4:52]** like separate agents. terminal 1 2 3 and

**[4:55]** four completely separate agents. They

**[4:57]** have their own context window and

**[4:58]** therefore you can give them specific

**[5:00]** context for a specific task. So this

**[5:02]** time let's say you're building out a SAS

**[5:03]** app. You need a new onboarding flow

**[5:05]** built. You also need your checkout bug

**[5:07]** fix and you want to experiment with a

**[5:09]** new design for let's say your user

**[5:12]** settings page. All of these tasks that

**[5:13]** we've mentioned don't depend on each

**[5:15]** other. And that's one of the reasons why

**[5:17]** we can actually orchestrate these in

**[5:19]** completely separate terminals that don't

**[5:21]** blow each other's context because

**[5:22]** there's no connection between those

**[5:24]** terminals. We are purely coordinating.

**[5:26]** So you open three terminals like this

**[5:28]** inside VS Code. And Claude actually has

**[5:30]** now a built-in flag to do this much

**[5:32]** easier. So in the first time we type in

**[5:34]** claude-w

**[5:36]** which is important new onboarding flow.

**[5:38]** The second one claude-w

**[5:40]** checkout bug and the third one

**[5:42]** claude-wesign

**[5:44]** user settings. And you'll see that in

**[5:46]** the project folder here, we've now

**[5:48]** opened up what's called a work tree

**[5:50]** where we've got new onboarding flow, fix

**[5:52]** checkout bug, and redesign user

**[5:54]** settings. And now if we go into our doc

**[5:56]** cloud folder, we've effectively got

**[5:57]** these different work trees, which is a

**[5:59]** separate copy of your project with its

**[6:01]** own branch, and it drops it straight

**[6:03]** into the claw code session. Each one in

**[6:05]** its own isolated workspace, and they

**[6:07]** can't interfere with each other. So they

**[6:09]** all have a clean context window, so

**[6:10]** there's no context rot from other tasks.

**[6:12]** and us as the operator are the ones

**[6:14]** coordinating the efforts between these

**[6:16]** different terminals here. So you're

**[6:18]** probably at this point checking in on

**[6:19]** the different terminals, the different

**[6:20]** tasks going on. You're copy and pasting

**[6:22]** findings from one to another if you're

**[6:24]** needed and then you're going to have to

**[6:26]** decide when each one is done and when

**[6:28]** you want to merge that back into the

**[6:29]** main project. But this is a massive

**[6:31]** upgrade from this sequential flow

**[6:33]** because actually we can get multiple

**[6:34]** things done in parallel as long as

**[6:36]** they're not dependent on each other. But

**[6:38]** if they do depend on each other, then

**[6:40]** this flow isn't going to work for us.

**[6:41]** And here's the nice touch about closing

**[6:43]** a work tree session. As soon as we close

**[6:45]** this window, Claude is going to handle

**[6:47]** the cleanup for us. So if nothing's

**[6:49]** changed, it removes that workspace

**[6:51]** automatically. But if there is work to

**[6:53]** keep, then it's going to ask you what to

**[6:55]** do. And you can see as I close these

**[6:57]** sessions, they disappear from the work

**[7:00]** trees up here. So the operator pattern

**[7:02]** is you running multiple clawed sessions

**[7:04]** in parallel, each with its own isolated

**[7:06]** workspace, but you're still the one

**[7:08]** coordinating. So, it's perfect for

**[7:10]** independent tasks where you want maximum

**[7:12]** control and clean context windows where

**[7:14]** they will not interfere with each other.

**[7:15]** Now, the operator pattern is great, but

**[7:17]** as you'll have probably noticed, you can

**[7:18]** only manage a certain number of

**[7:20]** terminals at any one point. Four to five

**[7:22]** terminals and you're flicking between

**[7:24]** those terminals, it becomes really

**[7:25]** difficult checking in on all of the

**[7:27]** sessions. So, what if the claw could

**[7:28]** actually handle the parallel tasks

**[7:31]** itself? So, pattern three then is the

**[7:33]** split and merge. And this is where it

**[7:35]** gets really interesting because the core

**[7:37]** idea is that within a single claw code

**[7:39]** session one terminal claw itself can

**[7:42]** split work across multiple sub aents

**[7:44]** that then run in parallel. So if you're

**[7:46]** thinking about all four of these

**[7:47]** terminals we could effectively spin off

**[7:49]** multiple sub aents inside each terminal

**[7:52]** to get more done quicker. And then

**[7:54]** effectively at the end it's going to

**[7:55]** merge all the results back into the main

**[7:57]** agent so that you can reap the rewards.

**[7:59]** And if you remember those built-in sub

**[8:00]** aents I mentioned earlier, explore,

**[8:02]** plan, and general purpose. Those are

**[8:04]** good examples of that. But you're not

**[8:06]** limited to just those. You can create

**[8:08]** your own custom sub aents inside your

**[8:10]** doc folder. And Claude can spin up

**[8:12]** multiple of them at the same time. And

**[8:15]** here is how that works in practice. You

**[8:17]** give Claude a task. Claude is going to

**[8:19]** analyze that task and realize that it

**[8:21]** can be broken down into independent

**[8:22]** pieces. It will then fan out into

**[8:24]** multiple sub aents, each one running in

**[8:27]** its own context window. and each one

**[8:29]** focused on their specific piece of work.

**[8:31]** And then when it's all done, it will

**[8:32]** merge all those results automatically

**[8:34]** and give you the final output. So, a lot

**[8:36]** is happening in the background here that

**[8:38]** we don't have to manually tell it to do.

**[8:40]** So, let's say you ask Claude to research

**[8:41]** five different competitors for a client

**[8:43]** proposal. Instead of researching them

**[8:45]** one by one, which could take ages if we

**[8:47]** ran it in that sequential flow pattern

**[8:49]** one, Claude can spin up five sub agents,

**[8:51]** one per competitor, and they all

**[8:53]** research simultaneously. So each one is

**[8:56]** going to come back with their findings

**[8:57]** and the main agent is going to

**[8:58]** synthesize the five findings into one

**[9:01]** single report. And Boris Churnney even

**[9:04]** one of the creators of core code has

**[9:05]** talked about sometimes spinning up 15

**[9:07]** sub aents at a time to get things done.

**[9:09]** But actually the limit on this is 10 at

**[9:12]** once. So 10 sub aents at once. Claude

**[9:14]** will actually cue any additional tasks

**[9:17]** as additional sub aents. But here's the

**[9:19]** critical limitation here. Sub agents can

**[9:21]** only report back to the main agent. So

**[9:23]** they can't actually talk to each other.

**[9:25]** So sub agent one and sub agent 3 have no

**[9:28]** idea what each other are doing. It's

**[9:30]** this like hub and spoke methodology

**[9:32]** where the main agent or our main

**[9:33]** instance where we're interacting with

**[9:35]** Claude is acting as the hub and it's

**[9:37]** receiving information back and forth

**[9:38]** from that sub agent. And if you've ever

**[9:40]** used the framework GSD or get done

**[9:43]** by Tash, this is like a framework I'd

**[9:45]** highly recommend for comprehensive

**[9:47]** projects. is basically a planning

**[9:49]** framework that will split your initial

**[9:50]** project brief into subtasks and execute

**[9:53]** on those subtasks for so it's designed

**[9:55]** for big projects but not in an

**[9:57]** enterprise fashion. We can look at their

**[9:59]** agents inside their agents folder.

**[10:00]** They've got quite a few agents in here

**[10:02]** and actually what you can do is go into

**[10:04]** the agents listed and see exactly like

**[10:06]** we do with skills the name the

**[10:09]** description. So researches a single gray

**[10:11]** area decision and returns a structured

**[10:13]** comparison table with rationale. So

**[10:15]** we're effectively giving this agent a

**[10:16]** role to do and a specific set of context

**[10:20]** that it goes out and performs a certain

**[10:22]** process as well as giving that agent a

**[10:25]** certain set of tools that it actually

**[10:26]** has access to. Now Claude will read the

**[10:28]** name of all agents in our docord folder

**[10:31]** and decide when it's suitable to offload

**[10:33]** a task to those sub agents. I.e. it will

**[10:35]** automatically use it when it thinks the

**[10:37]** task matches the description. Or you can

**[10:39]** specifically say I want to use the

**[10:41]** advisor researcher sub agent in this

**[10:43]** task. And one of the most powerful

**[10:44]** applications of this pattern is the

**[10:46]** build a validator chain. So you have one

**[10:48]** sub agent build something and then you

**[10:51]** have another sub agent actually review

**[10:53]** it. But what that requires is the sub

**[10:55]** aent one to build it first, pass it back

**[10:57]** to the main agent, pass that to the

**[10:59]** second sub aent through here and then

**[11:00]** that passes the results back to the main

**[11:02]** agent. So you can see because they can't

**[11:04]** communicate with each other that we're

**[11:05]** actually orchestrating it through this

**[11:06]** main agent. But you can effectively get

**[11:08]** a built-in quality check without doing

**[11:09]** any of the reviewing yourself by using

**[11:11]** that builder validator chain. So split

**[11:14]** and merge is claude doing the

**[11:15]** parallelization

**[11:17]** for you within a single session. So it

**[11:19]** can fan out work to those sub aents and

**[11:21]** merge the results for you. And again

**[11:23]** they keep your context window clean. So

**[11:25]** this is really powerful. So split and

**[11:26]** merge is awesome but it has one

**[11:28]** limitation. Sub agents can't talk to

**[11:30]** each other. So everything has to funnel

**[11:32]** through the main agent and for some

**[11:34]** tasks that is a genuine bottleneck. So

**[11:36]** what if your researcher agent needs to

**[11:38]** check in with your reviewer agent? Or

**[11:40]** what if you have a front-end developer

**[11:42]** that needs to coordinate with a back-end

**[11:43]** developer. So this is where the fourth

**[11:45]** pattern comes in, which is agent teams.

**[11:47]** An agent team is effectively a team of

**[11:49]** agents, as it sounds, that can share

**[11:51]** findings, challenge each other, and

**[11:53]** adapt together. So that the way that

**[11:54]** they share information is through a

**[11:56]** shared task list. So they're no longer

**[11:57]** interacting with the team lead, which is

**[11:59]** our main orchestration window. They're

**[12:01]** interacting with that shared task list.

**[12:03]** Agent one understands what tasks agent

**[12:05]** two is doing. And vice versa, they can

**[12:07]** send messages between the agents. And

**[12:10]** it's the most advanced coordination

**[12:11]** pattern. It's the newest addition to CL

**[12:14]** code and it is genuinely a gamecher for

**[12:16]** complex projects, but it should only be

**[12:18]** used in complex projects because the

**[12:20]** token usage is extremely high when

**[12:22]** you've got cross collaboration between

**[12:24]** the agents. Now, this is completely

**[12:26]** still experimental. It shipped with Opus

**[12:28]** 4.6 as a research preview. So, you need

**[12:31]** to still enable it by adding a flag to

**[12:33]** your settings.json, which is claw code

**[12:36]** experimental agent teams one. and you

**[12:38]** need to add that as an environment

**[12:39]** variable in your settings.json. But once

**[12:41]** it's enabled, you just tell Claude in

**[12:43]** your prompt that you want to use an

**[12:45]** agent team. So you must still specify

**[12:47]** that you want to use an agent team, not

**[12:48]** like sub agents where it will choose

**[12:50]** those automatically. You go in, you

**[12:52]** describe the task you want, you describe

**[12:54]** the team structure or Claude will

**[12:56]** actually determine the team structure

**[12:57]** itself and Claude will then create that

**[12:58]** team, spawn the teammates and coordinate

**[13:00]** the work. And in your terminal, you can

**[13:02]** actually navigate between the teammates

**[13:04]** using shift up and shift down. And you

**[13:06]** can message directly any teammate and

**[13:08]** bypass this team lead entirely or you

**[13:10]** can talk directly to the team lead. Now,

**[13:12]** as I mentioned, they use significantly

**[13:13]** more tokens because we've got this back

**[13:15]** and forth between the shared task list,

**[13:17]** the team lead, between the agents. And

**[13:19]** each teammate is its full CL code

**[13:21]** instance with its own context window

**[13:23]** again. So, it's got a portion of the

**[13:25]** main context passed in it from that

**[13:27]** shared task list and the team lead. And

**[13:29]** they roughly estimate it's going to be

**[13:31]** four to seven times more tokens than a

**[13:33]** single session when you're actually

**[13:35]** using agent teams. And the thing that

**[13:37]** actually matters here is you don't need

**[13:38]** agent teams for most of your work. You

**[13:40]** should actually only reach for them when

**[13:41]** sub agents or even a single session

**[13:43]** couldn't do the job. So say you're

**[13:45]** trying to build out a complex SAS

**[13:47]** application where you have a front-end

**[13:48]** developer, a backend developer, and then

**[13:50]** a testing developer that spins up tests

**[13:52]** and needs to communicate to agent one

**[13:54]** and two as they build. That is an

**[13:56]** example where you would actually want an

**[13:58]** agent team to save from back and forth

**[14:00]** between the orchestration layer. But a

**[14:02]** lot of people in the community are just

**[14:03]** saying that actually this is just a way

**[14:05]** to produce large quantities of work very

**[14:07]** quickly which isn't necessarily a good

**[14:09]** thing. You still need the work to be the

**[14:11]** right work. So it's powerful but

**[14:13]** expensive. So only reach for this when

**[14:15]** the task genuinely needs that cross

**[14:17]** collaboration. So patterns 1 through 4

**[14:19]** all have one thing in common. You're

**[14:21]** there in the terminal. you're either

**[14:23]** typing, coordinating, or at least

**[14:25]** watching the task. But what if you

**[14:27]** didn't need to be there at all? So, this

**[14:29]** brings us on to the last pattern, which

**[14:31]** is Claude working without you. So, this

**[14:33]** is the dream of autonomous workflows,

**[14:35]** where you don't need to be in the loop.

**[14:37]** You just set a task, you walk away, and

**[14:38]** you come back to the results. And this

**[14:40]** is called headless. And it's where

**[14:41]** Claude code goes from being a tool you

**[14:43]** sit with to a team member that's going

**[14:45]** to go and work independently. This

**[14:47]** requires you having no conversation back

**[14:49]** and forth, no terminal window open, and

**[14:52]** no human in the loop at all. So when

**[14:54]** we're running this, we're using the -p

**[14:56]** flag. So we're saying Claude-P, and

**[14:58]** we're entering a prompt after the P

**[15:00]** flag. So we're saying, Claude, process

**[15:02]** this prompt. We don't want any

**[15:04]** interaction, no approvals. You've got

**[15:06]** full permissions. Just go get it done

**[15:08]** and return to me the result when you're

**[15:10]** finished. And that on its own is kind of

**[15:12]** iterating with that task cla prompt and

**[15:15]** will give us that report.json. But when

**[15:18]** it gets really groundbreaking, when it

**[15:20]** gets really powerful is like when you

**[15:22]** plug this into other systems. So if you

**[15:24]** plug this in to your Windows or your Mac

**[15:27]** scheduling function, your cron

**[15:29]** functionality that can say at 7 a.m.

**[15:31]** every day, fire in this command to my

**[15:33]** terminal and then Claude goes and

**[15:34]** iterates and gets the report and sends

**[15:37]** it back to you. That is when it

**[15:38]** genuinely becomes a gamecher because

**[15:39]** then what we're doing is actually

**[15:41]** creating workflows that can run on a

**[15:43]** schedule without your input. So it could

**[15:45]** be review yesterday's work and write a

**[15:47]** summary to a morning report.mmd. So when

**[15:50]** Claude wakes up, it's going to read all

**[15:52]** the work you did yesterday, analyze

**[15:53]** them, write the report, and then you

**[15:55]** just have to go and look at the output

**[15:57]** before you've even done anything. You

**[15:59]** didn't open a terminal, you didn't even

**[16:00]** type a prompt in. It basically just

**[16:02]** happened. Or say you're actually running

**[16:04]** content for your business. You could

**[16:05]** have a script that pulls your latest

**[16:07]** video transcript, runs it through Claude

**[16:09]** with a specific prompt, gets you back a

**[16:11]** set of social media posts, saved to a

**[16:13]** file that you can then just schedule

**[16:15]** automatically. And you can chain these

**[16:16]** together. You can add skills into the

**[16:18]** prompts that invoke specific skills. And

**[16:21]** this is all completely automated. Now,

**[16:23]** the big limitation in this is trust.

**[16:26]** You're not asking for an iterative

**[16:28]** conversation. You're giving Claude

**[16:30]** autonomy to do things on your behalf.

**[16:32]** So, you're not checking each step. So,

**[16:34]** this works best for tasks where the

**[16:35]** output is extremely easy to verify. At

**[16:38]** the moment, you probably don't want to

**[16:39]** go headless on anything that's hard to

**[16:42]** undo, but you can actually put guard

**[16:44]** rails on this as well. If you want it to

**[16:45]** only read and not write, for example, we

**[16:48]** can do d-allowed tools and then make

**[16:50]** sure that we add specific things that it

**[16:51]** can do. And some people in the community

**[16:52]** have taken this even further with things

**[16:55]** like the Ralph loop, which keeps feeding

**[16:57]** the same prompt back in so that Claude

**[16:59]** iterates on its own work until it gets

**[17:01]** it right. And each time it iterates, it

**[17:03]** understands what has been done in the

**[17:05]** last cycle. And people have actually

**[17:06]** been using this to ship entire projects

**[17:08]** overnight. So this is brilliant. This is

**[17:10]** like claude working without you. You set

**[17:12]** a task, you walk away, and you come back

**[17:14]** for the results. But like we said, it's

**[17:16]** best for batch processing things and

**[17:17]** anything where the output is really easy

**[17:19]** to verify. So there you have it, five

**[17:22]** agentic patterns for claw code. And if

**[17:23]** you want to go deeper on any of these or

**[17:25]** on building skills, creating custom sub

**[17:27]** agents, how to structure your claw MD

**[17:29]** and actually put these patterns into

**[17:31]** practice with real projects, then check

**[17:32]** out the first link to the Agentic

**[17:34]** Academy in the description below. We've

**[17:36]** got a full claw code track where we

**[17:37]** build this stuff step by step. And let

**[17:39]** me know in the comments which pattern

**[17:41]** you're looking forward to trying. And if

**[17:43]** this did save you the time of figuring

**[17:44]** out this yourself, then I'd really

**[17:46]** appreciate a like and subscribe. Thanks

**[17:48]** so much for watching.
