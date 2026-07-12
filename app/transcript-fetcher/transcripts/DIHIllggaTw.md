# Transcript: Claude Code Works Better With These 5 Agent Patterns

**URL:** https://www.youtube.com/watch?v=DIHIllggaTw
**Segments:** 501
**Channel:** Eric Tech
**Duration:** 14:29
**Uploaded:** 2026-04-10

---

## Full Text

If you're still using Claude code, one conversation at a time, then you're doing it all wrong. Most people give it a task, sit there and wait, then it's going to give another one. And that's not exactly how you run a team, that's a bottleneck. So, in this video, I'm going to show you five agent patterns that you can actually go from dead simple to fully autonomous, where you can actually have Claude code here to run it by yourself while you go grab coffee or lunch. So, with that being said, if that sounds interesting, let's get into this. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just give you an idea, this week we're actually running a Claude code masterclass where we're going to dive into how to improve Claude code's accuracy where we're going to use it to build the applications. Plus, you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in and I'll see you in a community. Now, let's take a look at the first agent pattern, which is sequential flow. And what this agent pattern does is basically having AI agent here to tackle one task one after the other. And as example here, you can see we have a skill called fix tickets. And what this fix ticket does here is basically try to automate the entire bug fix pipeline. So, let's say if you have encountered bug in your software, you basically create a Jira ticket, trigger that skill, it is going to basically trigger this entire workflow here to first read the ticket, fix it, and it's going to ship it. And to put a detail on exactly what the skill does, you can see here that it's going to first try to read the ticket by calling the Jira MCP, then it's going to trigger the Playwright CLI here to verify to see if we're able to reproduce that, then it's going to do some research, implement it, then we're going to review the changes that it did based on different sub agents, then we're going to trigger the Playwright CLI skill again, try to verify the changes that we did, then commit it, deploy it, then eventually going to push these changes into the QA session. So, you can see here that this entire workflow right here is done in sequential order one after the other. Now, obviously for this agent pattern here, it doesn't mean that you cannot have like multiple sub agents. Yes, you can. For example, you can have a sub agent being called in the QA stage, so it doesn't really consume a lot of context in the main thread. You can also have different sub agent here to do research, right? You can see here that I specifically mentioned that I have different agent teams here to do the review. And each agent here is going to micro focus on one particular area. For example, one focus on front end, one focus on back end, and the other one focusing on the testing, right? So, you can see that we can still have those capabilities, but it's just that these tasks have to be done one after the other. And of course, if you're looking to see how I build this entire workflow, make sure you check out this video right here on how I was able to automate this entire process by piecing all different skills, and having this one single workflows that's being triggered to do multiple different things in this entire bug fix pipeline. Make sure you check out this video right here. But now, from this example, we can clearly see this is how exactly we can trigger this sequential flow agent pattern. And this agent pattern here is really good if you're looking to build like workflows that you want to automate where you have to have the task here complete one after the other. Now, that was the first agent pattern. The second agent pattern we're going to take a look at is split and merge. And to put it simply, we basically try to split a single big task into different sub agents, and each sub agent here is going to tackle that and complete it, and eventually going to merge it back to the orchestrator. So, put it simply, let's say if you're going to work on a project. So, instead of having just one agent try to tackle this entire project, if this project or the task here can be done in parallel, we can have different sub agent here to complete it. This way, you're going to complete the task much more faster, and it's going to be much more accurate because you're going to avoid the context rod. But of course, more over on the accuracy for Claude code on this video right here if you want to check it out. But basically, what it does here is that it's going to break that task into different sub agents, and for each sub agent here, it's going to complete it and merge it back into one single session, right? So, after they complete the task like building, reviewing, testing, it's going to merge it back into one single session, or in this case, one single orchestrator. And a practical example for this could be like, for example, here you can see I created a skill called agent or DB audit. And what this skill does here is that it will basically try to audit my entire database by spinning up different sub agents here to audit my database. For example, I can have one sub agent here reviewing my schema, one sub agent here reviewing my security, one sub agent here try to see where we can be able to improve our query or maybe try to adding some indexes to improve the database query time, right? And maybe some of them here is going to interact with like Superbase MCP here and basically try to do the entire full audit. And eventually here, once everything is all completed, it's going to merge all the findings into one orchestrator right here. Now, of course, if you're looking to learn more about sub agents, I have a video playlist on exactly how you can get started with sub agents and how you can be able to go from beginner here to all the way to pro using sub agents. So, make sure to check it out. Now, that was basically DB audits. You can also do this with other sub agents. And one of the practical workflow that I use sub agent for is the review process. Let's say if I have pull requests that I have to review. So, instead of me having to review this manually, I can be able to pass this job here to different agents. And here you can see this is a skill that I created called review skill. And what it essentially does here is that it's going to trigger three sub agents here to working at the same time. And to put this in a more practical use case here, you can see I have bunch of review agents that I have in my tool belts. Some of them you can see here is focused on code quality. And there's also a couple of them here focused on specialized review, which for example, like silent failures, tests, design, comments, code sniffers like try to make sure that our code here is much more refactorable or much more scalable, right? And there's also bunch of multi-agent teams here that I created. For example, one focus on team review, which spin of like five reviewers, like five of them. There's also the review fix, which we have like eight parallel reviewers here automatically fix and automatically review using the Hellas agent pattern, which I'm going to show you later on this video. But clearly, you can see that that's basically the agent pattern that I have here for the second one, which is split and merge. So now, the next agent pattern here we're going to take a look at is agent teams. And compared to the previous one, which is using like sub agents, the difference here is that we have a team leader here who have a shared communications between all the sub agents. Because before for sub agents here, we can see we spin up having a orchestrator here spin up different sub agents, but the difference here is that the sub agents here, you can see they have no communication between. So, for agent team here, you can see the each sub agent that we create, we have communication, a shared communication between all of them. And right here, you can see I created a diagram here which shows exactly how agent team works. So, you can see here that each agents, they have a shared communications, and we can have a double advocate here to basically challenge or question everything that it does. So, we have someone that can always be kind of like a senior engineer or staff engineer here who always challenge things that each sub agent working on. And they could be all working on a same task, right? Maybe one sub agent here focus on idea, one focus on planning, one focusing on like execution or research, and the other one here is just doing like, you know, researching or like try to challenge things. And they all kind of have like shared plan or shared task, and they all try to work on it all that at the same time, right? And you can see that the goal here is that each of them has a fresh context window, and this will make sure that the task here will get done much more accurate, okay? And that's basically the other agent pattern here, which will basically try to, you know, break a task here into different sub agents, and having all the sub agents here to be able to communicate to each other using the agent team feature. And of course, if you want to learn more about agent team, you can check out this video right here that I did on exactly how you can set it up on your local machine, how you can be able to use it, and what are some agent teams that I created here to basically optimize my day-to-day workflow. But specifically for my day-to-day workflows here, you can see I have bunch of agent teams inside my projects. So, one of the skill that I created called review teams, which will basically try to spin up like four specialized reviewers and one double advocate here to basically have the entire agent team here to review a entire pull request. For example, I can also have a spec team here to basically do the parallel research agent here. Maybe we can have different agents to do a single research, maybe on an idea or on a topic. And we can be able to aggregate all together once we have all the agents here have done the research. Now, obviously for this type of agent pattern here, it's really best when a task here involves like interconnected components. Maybe for example, like instead of having sub agent here, one agent working on front end and one agent working on back end, maybe they're working on a same feature, right? For example, maybe the feature that they're working on is related to payment, you know, one focus on, you know, the front end for the UI, one focus on the back end, they have to have the communications. And here you can see that would be a really good use case. The worst case that you want to use agent team here is where each agent here is working on their own thing, and there's really no need for communication, then might as well just not do that with agent teams. And that's basically my two cents on when to use agent teams to not just level up, but also know exactly when to use it. Now, the next agent pattern we're going to take a look at is the operator. And essentially, what operator does here is that it's going to create a isolated environment for each Claude code session that we create. So, for example, let's say we have a Claude code session here, we open a terminal, we run Claude, and we just have them to building the applications. And let's say we want to, you know, create a brand new terminal session, and this terminal session here open a Claude code, and basically have Claude code here to working on maybe a different feature. But this feature that we want to work on, I want to have it to be in an isolated environment that's not in conflict like with this Claude code session. And this way, the good thing about this one is that you can be able to have multiple terminal session open, and each one running a Claude code session, and each one here is going to be in an isolated environment here, so there's no conflict between different, you know, terminal sessions or different Claude code sessions. Yes, for each session here, you can still run all the things that I just mentioned like sub agents or agent teams or the sequential workflows that I just mentioned, you can do that with each sessions. But they're just going to be in a different environment that they're not going to be ever being any change conflicts, right? And like I said, the good thing is that if you don't like one of the Git work trees, right? You can just completely rip it off and just continue on with the other sessions, right? Could be like, okay, I want you to design a landing page, and I have one session here design a, you know, one variation of it, and then one design a second variation, and a third one design a third variation. And all of them here has its own environment here that, you know, let's say if you don't like this one, you're just going to rip it off or we're going to, you know, delete a work tree and delete our changes, but it doesn't affect the other two, right? And if you like one of them, you can just delete the other one. You're just going to keep the one of them, and eventually merge one back to the main branch. And by doing this, you're going to have two benefits. One is that you actually can be able to build things much more faster, because you're going to have multiple terminal sessions. And second one here is that you can be able to make it much more easier here for you to AB test, right? For example, it could be like a UI changes, or for example, you're going to spin up a different session here, maybe for a back-end changes, or maybe database changes. Whatever changes might be, and they're all working on the same task. And by the end of it, you're just going to choose the one that has the most accuracy, or has the most best look, or whichever has the best results that you want, and you can just choose that one. And that's going to increase your productivity much more better, because, hey, AI agent here can make mistakes, and you can reduce that chance from making mistake by relying on just one single output. You can have multiple outputs here, compare one of them, and just choose that one to go down to. And that's exactly how it works with this agent pattern. All right, so now let's take a look at the next agent pattern, which is headless. Now, this is actually my favorite, um, which is the most used pattern that I always use. It's basically going to allow you to use Claude Co here very autonomously. So, what it essentially does here is that whenever we use Claude, right? We do like Claude, or Claude dangerously skip permissions, you can see that that's basically how we interact with Claude. We just simply just going to do it inside of Claude Co sessions, right? But what you can do here is that if you do hyphen P, you provide the prompt. For example, what is 1 + 1? It's going to give you the answer that it generates, and it's going to run this in the background. So, without you having to be interacting in the Claude session, you can do this in the terminal, right? You if you want to say, "Okay, what is 1 + 1?" Or what's the weather today? It's going to generate that in the background, and split it back in the terminal, right? Now, why is it powerful? Because you can actually be able to automate, or be able to make this completely autonomous by just simply just providing the commands, and having Claude Co session to run, right? Currently, I'm in the Claude Co session. I'm going to say, "Hey, why don't you run this?" It's going to basically run this, and what you can do here is that you can even combine that with a bunch of skills, like, "Hey, why don't you just schedule this, and run this command right here every 7:00 a.m., right?" And Claude Co here is going to do this autonomously, or every run this every 20 minutes, or run this maybe like, you know, every time when something is being triggered, right? You can do this, setting all kinds of things for this kind of task. And furthermore, what you can do here is that you can combine the power with Ralph Loop, right? Ralph Loop, basically, I actually made a video, and essentially what it does here is that you can set your AI agent here to be completely autonomous, how to fix something, maybe a bug, maybe you try to perfect the UI, or maybe you have a certain workflow, and just have it to cycle through until, you know, get it done. You just have it to set a breakpoint on, for example, "Hey, I want to you fix this." So, while it's not fixed, just continue running, right? And the power of this is that I was able to use this for reviewing process. I specify how many times it should review, like cycle through to review, and I simply just going to let it run. You You know, for example, the first iteration here is going to have like run like multiples of agent here to check to see, "Okay, is it good or not?" Right? Then we have the second iteration, the third iteration here. Each iteration here is going to review the things with a fresh context window, like we just mentioned, using the headless commands. And what essentially here is going to do is it's going to basically try to summarize everything into a single report, and it's going to aggregate that into a single result, right? So, for example, I have the first session run, done, and then second session done, third session done. That is going to aggregate all the results that I find into a single result. And that's exactly how that works. I basically package everything here into a single skill, called the iterative review. And the way how it works here, you can see this is the iterative review skill that I created. It's going to specify, "Okay, I want you to review this for five iterations." And I simply provide a pull request URL, or a branch name. It's going to review the changes. First, going to read the skill, write exactly what's the rules. Then it's basically going to trigger the script, which is a SH command. It's going to basically try to run the command right here, like, "Hey, this is the prompt, which is stored in the MD file." And each session here, we're going to have a fresh context window. And when we try to trigger this hyphen P for a fresh context for this headless operation, it's basically going to trigger like spin up like five to seven sub agents here to run in the same time. And for each time they run, it's going to get its fresh context window. And after it, it's going to aggregate all the findings that it has for after all the iterations, and summarize everything into a single report. And literally, for those bunch of sub agents we're going to spin up, we actually can be able to choose bunch of agents of our choice, just like I mentioned from the previous sections, right?

---

## Timestamped Segments

**[0:00]** If you're still using Claude code, one

**[0:01]** conversation at a time, then you're

**[0:03]** doing it all wrong. Most people give it

**[0:04]** a task, sit there and wait, then it's

**[0:06]** going to give another one. And that's

**[0:08]** not exactly how you run a team, that's a

**[0:10]** bottleneck. So, in this video, I'm going

**[0:12]** to show you five agent patterns that you

**[0:14]** can actually go from dead simple to

**[0:16]** fully autonomous, where you can actually

**[0:17]** have Claude code here to run it by

**[0:18]** yourself while you go grab coffee or

**[0:20]** lunch. So, with that being said, if that

**[0:22]** sounds interesting, let's get into this.

**[0:24]** Now, before we continue, I recently

**[0:25]** launched our school community where I

**[0:27]** help you to master AI agents,

**[0:28]** automations, and so much more. And

**[0:30]** that's all coming from someone who used

**[0:32]** to work as a senior AI software engineer

**[0:34]** at companies like Amazon and Microsoft.

**[0:37]** And in this community, you're going to

**[0:38]** get over 100 plus video materials like

**[0:40]** templates and workflows that I

**[0:42]** personally built and sold over 100 plus

**[0:44]** times. On top of that, you're also going

**[0:45]** to get access to our weekly live calls.

**[0:48]** And just give you an idea, this week

**[0:49]** we're actually running a Claude code

**[0:50]** masterclass where we're going to dive

**[0:52]** into how to improve Claude code's

**[0:54]** accuracy where we're going to use it to

**[0:55]** build the applications. Plus, you're

**[0:57]** also going to get full community support

**[0:58]** where you're going to get a chance to

**[0:59]** ask questions and get direct answers

**[1:01]** back. So, if you're ready to level up,

**[1:03]** make sure you jump right in and I'll see

**[1:04]** you in a community. Now, let's take a

**[1:06]** look at the first agent pattern, which

**[1:07]** is sequential flow. And what this agent

**[1:09]** pattern does is basically having AI

**[1:10]** agent here to tackle one task one after

**[1:12]** the other. And as example here, you can

**[1:14]** see we have a skill called fix tickets.

**[1:16]** And what this fix ticket does here is

**[1:18]** basically try to automate the entire bug

**[1:20]** fix pipeline. So, let's say if you have

**[1:21]** encountered bug in your software, you

**[1:23]** basically create a Jira ticket, trigger

**[1:25]** that skill, it is going to basically

**[1:26]** trigger this entire workflow here to

**[1:28]** first read the ticket, fix it, and it's

**[1:30]** going to ship it. And to put a detail on

**[1:32]** exactly what the skill does, you can see

**[1:34]** here that it's going to first try to

**[1:35]** read the ticket by calling the Jira MCP,

**[1:38]** then it's going to trigger the

**[1:39]** Playwright CLI here to verify to see if

**[1:40]** we're able to reproduce that, then it's

**[1:42]** going to do some research, implement it,

**[1:44]** then we're going to review the changes

**[1:45]** that it did based on different sub

**[1:46]** agents, then we're going to trigger the

**[1:48]** Playwright CLI skill again, try to

**[1:49]** verify the changes that we did, then

**[1:51]** commit it, deploy it, then eventually

**[1:53]** going to push these changes into the QA

**[1:54]** session. So, you can see here that this

**[1:56]** entire workflow right here is done in

**[1:57]** sequential order one after the other.

**[2:00]** Now, obviously for this agent pattern

**[2:01]** here, it doesn't mean that you cannot

**[2:02]** have like multiple sub agents. Yes, you

**[2:04]** can. For example, you can have a sub

**[2:05]** agent being called in the QA stage, so

**[2:08]** it doesn't really consume a lot of

**[2:09]** context in the main thread. You can also

**[2:11]** have different sub agent here to do

**[2:12]** research, right? You can see here that I

**[2:14]** specifically mentioned that I have

**[2:15]** different agent teams here to do the

**[2:16]** review. And each agent here is going to

**[2:18]** micro focus on one particular area. For

**[2:21]** example, one focus on front end, one

**[2:22]** focus on back end, and the other one

**[2:23]** focusing on the testing, right? So, you

**[2:25]** can see that we can still have those

**[2:27]** capabilities, but it's just that these

**[2:29]** tasks have to be done one after the

**[2:31]** other. And of course, if you're looking

**[2:32]** to see how I build this entire workflow,

**[2:34]** make sure you check out this video right

**[2:35]** here on how I was able to automate this

**[2:37]** entire process by piecing all different

**[2:39]** skills, and having this one single

**[2:41]** workflows that's being triggered to do

**[2:42]** multiple different things in this entire

**[2:44]** bug fix pipeline. Make sure you check

**[2:46]** out this video right here. But now, from

**[2:48]** this example, we can clearly see this is

**[2:49]** how exactly we can trigger this

**[2:51]** sequential flow agent pattern. And this

**[2:53]** agent pattern here is really good if

**[2:54]** you're looking to build like workflows

**[2:56]** that you want to automate where you have

**[2:57]** to have the task here complete one after

**[2:59]** the other. Now, that was the first agent

**[3:01]** pattern. The second agent pattern we're

**[3:03]** going to take a look at is split and

**[3:04]** merge. And to put it simply, we

**[3:06]** basically try to split a single big task

**[3:08]** into different sub agents, and each sub

**[3:10]** agent here is going to tackle that and

**[3:12]** complete it, and eventually going to

**[3:13]** merge it back to the orchestrator. So,

**[3:15]** put it simply, let's say if you're going

**[3:16]** to work on a project. So, instead of

**[3:18]** having just one agent try to tackle this

**[3:20]** entire project, if this project or the

**[3:22]** task here can be done in parallel, we

**[3:24]** can have different sub agent here to

**[3:25]** complete it. This way, you're going to

**[3:27]** complete the task much more faster, and

**[3:29]** it's going to be much more accurate

**[3:30]** because you're going to avoid the

**[3:31]** context rod. But of course, more over on

**[3:33]** the accuracy for Claude code on this

**[3:35]** video right here if you want to check it

**[3:37]** out. But basically, what it does here is

**[3:38]** that it's going to break that task into

**[3:40]** different sub agents, and for each sub

**[3:41]** agent here, it's going to complete it

**[3:43]** and merge it back into one single

**[3:45]** session, right? So, after they complete

**[3:47]** the task like building, reviewing,

**[3:48]** testing, it's going to merge it back

**[3:50]** into one single session, or in this

**[3:51]** case, one single orchestrator. And a

**[3:53]** practical example for this could be

**[3:54]** like, for example, here you can see I

**[3:56]** created a skill called agent or DB

**[3:58]** audit. And what this skill does here is

**[3:59]** that it will basically try to audit my

**[4:01]** entire database by spinning up different

**[4:02]** sub agents here to audit my database.

**[4:04]** For example, I can have one sub agent

**[4:06]** here reviewing my schema, one sub agent

**[4:08]** here reviewing my security, one sub

**[4:10]** agent here try to see where we can be

**[4:11]** able to improve our query or maybe try

**[4:13]** to adding some indexes to improve the

**[4:16]** database query time, right? And maybe

**[4:18]** some of them here is going to interact

**[4:19]** with like Superbase MCP here and

**[4:21]** basically try to do the entire full

**[4:22]** audit. And eventually here, once

**[4:23]** everything is all completed, it's going

**[4:25]** to merge all the findings into one

**[4:27]** orchestrator right here. Now, of course,

**[4:28]** if you're looking to learn more about

**[4:30]** sub agents, I have a video playlist on

**[4:32]** exactly how you can get started with sub

**[4:34]** agents and how you can be able to go

**[4:35]** from beginner here to all the way to pro

**[4:37]** using sub agents. So, make sure to check

**[4:39]** it out. Now, that was basically DB

**[4:40]** audits. You can also do this with other

**[4:42]** sub agents. And one of the practical

**[4:44]** workflow that I use sub agent for is the

**[4:46]** review process. Let's say if I have pull

**[4:48]** requests that I have to review. So,

**[4:50]** instead of me having to review this

**[4:51]** manually, I can be able to pass this job

**[4:53]** here to different agents. And here you

**[4:54]** can see this is a skill that I created

**[4:55]** called review skill. And what it

**[4:57]** essentially does here is that it's going

**[4:58]** to trigger three sub agents here to

**[5:00]** working at the same time. And to put

**[5:01]** this in a more practical use case here,

**[5:03]** you can see I have bunch of review

**[5:04]** agents that I have in my tool belts.

**[5:06]** Some of them you can see here is focused

**[5:07]** on code quality. And there's also a

**[5:09]** couple of them here focused on

**[5:10]** specialized review, which for example,

**[5:12]** like silent failures, tests, design,

**[5:15]** comments, code sniffers like try to make

**[5:17]** sure that our code here is much more

**[5:19]** refactorable or much more scalable,

**[5:21]** right? And there's also bunch of

**[5:22]** multi-agent teams here that I created.

**[5:24]** For example, one focus on team review,

**[5:26]** which spin of like five reviewers, like

**[5:27]** five of them. There's also the review

**[5:29]** fix, which we have like eight parallel

**[5:32]** reviewers here automatically fix and

**[5:34]** automatically review using the Hellas

**[5:36]** agent pattern, which I'm going to show

**[5:37]** you later on this video. But clearly,

**[5:39]** you can see that that's basically the

**[5:40]** agent pattern that I have here for the

**[5:42]** second one, which is split and merge. So

**[5:44]** now, the next agent pattern here we're

**[5:45]** going to take a look at is agent teams.

**[5:47]** And compared to the previous one, which

**[5:48]** is using like sub agents, the difference

**[5:50]** here is that we have a team leader here

**[5:52]** who have a shared communications between

**[5:53]** all the sub agents. Because before for

**[5:55]** sub agents here, we can see we spin up

**[5:57]** having a orchestrator here spin up

**[5:59]** different sub agents, but the difference

**[6:00]** here is that the sub agents here, you

**[6:02]** can see they have no communication

**[6:03]** between. So, for agent team here, you

**[6:05]** can see the each sub agent that we

**[6:07]** create, we have communication, a shared

**[6:09]** communication between all of them.

**[6:11]** And right here, you can see I created a

**[6:12]** diagram here which shows exactly how

**[6:14]** agent team works. So, you can see here

**[6:16]** that each agents, they have a shared

**[6:18]** communications, and we can have a double

**[6:20]** advocate here to basically challenge or

**[6:22]** question everything that it does. So, we

**[6:24]** have someone that can always be kind of

**[6:25]** like a senior engineer or staff engineer

**[6:27]** here who always challenge things that

**[6:29]** each sub agent working on. And they

**[6:31]** could be all working on a same task,

**[6:33]** right? Maybe one sub agent here focus on

**[6:35]** idea, one focus on planning, one

**[6:37]** focusing on like execution or research,

**[6:39]** and the other one here is just doing

**[6:41]** like, you know, researching or like try

**[6:42]** to challenge things. And they all kind

**[6:44]** of have like shared plan or shared task,

**[6:47]** and they all try to work on it all that

**[6:49]** at the same time, right? And you can see

**[6:50]** that the goal here is that each of them

**[6:52]** has a fresh context window, and this

**[6:54]** will make sure that the task here will

**[6:55]** get done much more accurate, okay? And

**[6:57]** that's basically the other agent pattern

**[6:59]** here, which will basically try to, you

**[7:00]** know, break a task here into different

**[7:02]** sub agents, and having all the sub

**[7:04]** agents here to be able to communicate to

**[7:06]** each other using the agent team feature.

**[7:08]** And of course, if you want to learn more

**[7:09]** about agent team, you can check out this

**[7:11]** video right here that I did on exactly

**[7:12]** how you can set it up on your local

**[7:14]** machine, how you can be able to use it,

**[7:15]** and what are some agent teams that I

**[7:16]** created here to basically optimize my

**[7:18]** day-to-day workflow. But specifically

**[7:20]** for my day-to-day workflows here, you

**[7:21]** can see I have bunch of agent teams

**[7:23]** inside my projects. So, one of the skill

**[7:25]** that I created called review teams,

**[7:27]** which will basically try to spin up like

**[7:28]** four specialized reviewers and one

**[7:30]** double advocate here to basically have

**[7:32]** the entire agent team here to review a

**[7:34]** entire pull request. For example, I can

**[7:36]** also have a spec team here to basically

**[7:38]** do the parallel research agent here.

**[7:40]** Maybe we can have different agents to do

**[7:42]** a single research, maybe on an idea or

**[7:44]** on a topic. And we can be able to

**[7:46]** aggregate all together once we have all

**[7:48]** the agents here have done the research.

**[7:50]** Now, obviously for this type of agent

**[7:51]** pattern here, it's really best when a

**[7:53]** task here involves like interconnected

**[7:55]** components. Maybe for example, like

**[7:57]** instead of having sub agent here, one

**[7:59]** agent working on front end and one agent

**[8:00]** working on back end, maybe they're

**[8:02]** working on a same feature, right? For

**[8:03]** example, maybe the feature that they're

**[8:05]** working on is related to payment, you

**[8:07]** know, one focus on, you know, the front

**[8:09]** end for the UI, one focus on the back

**[8:10]** end, they have to have the

**[8:11]** communications. And here you can see

**[8:13]** that would be a really good use case.

**[8:15]** The worst case that you want to use

**[8:16]** agent team here is where each agent here

**[8:18]** is working on their own thing, and

**[8:20]** there's really no need for

**[8:21]** communication, then might as well just

**[8:22]** not do that with agent teams. And that's

**[8:24]** basically my two cents on when to use

**[8:26]** agent teams to not just level up, but

**[8:28]** also know exactly when to use it. Now,

**[8:30]** the next agent pattern we're going to

**[8:31]** take a look at is the operator. And

**[8:33]** essentially, what operator does here is

**[8:34]** that it's going to create a isolated

**[8:36]** environment for each Claude code session

**[8:37]** that we create. So, for example, let's

**[8:39]** say we have a Claude code session here,

**[8:41]** we open a terminal, we run Claude, and

**[8:42]** we just have them to building the

**[8:44]** applications. And let's say we want to,

**[8:46]** you know, create a brand new terminal

**[8:48]** session, and this terminal session here

**[8:50]** open a Claude code, and basically have

**[8:52]** Claude code here to working on maybe a

**[8:53]** different feature. But this feature that

**[8:55]** we want to work on, I want to have it to

**[8:57]** be in an isolated environment that's not

**[8:59]** in conflict like with this Claude code

**[9:01]** session. And this way, the good thing

**[9:02]** about this one is that you can be able

**[9:03]** to have multiple terminal session open,

**[9:05]** and each one running a Claude code

**[9:07]** session, and each one here is going to

**[9:09]** be in an isolated environment here, so

**[9:10]** there's no conflict between different,

**[9:13]** you know, terminal sessions or different

**[9:14]** Claude code sessions. Yes, for each

**[9:16]** session here, you can still run all the

**[9:18]** things that I just mentioned like sub

**[9:19]** agents or agent teams or the sequential

**[9:21]** workflows that I just mentioned, you can

**[9:23]** do that with each sessions. But they're

**[9:25]** just going to be in a different

**[9:26]** environment that they're not going to be

**[9:28]** ever being any change conflicts, right?

**[9:31]** And like I said, the good thing is that

**[9:32]** if you don't like one of the Git work

**[9:34]** trees, right? You can just completely

**[9:35]** rip it off and just continue on with the

**[9:37]** other sessions, right? Could be like,

**[9:39]** okay, I want you to design a landing

**[9:40]** page, and I have one session here design

**[9:43]** a, you know, one variation of it, and

**[9:45]** then one design a second variation, and

**[9:47]** a third one design a third variation.

**[9:49]** And all of them here has its own

**[9:51]** environment here that, you know, let's

**[9:53]** say if you don't like this one, you're

**[9:54]** just going to rip it off or we're going

**[9:55]** to, you know, delete a work tree and

**[9:57]** delete our changes, but it doesn't

**[9:58]** affect the other two, right? And if you

**[10:01]** like one of them, you can just delete

**[10:02]** the other one. You're just going to keep

**[10:03]** the one of them, and eventually merge

**[10:04]** one back to the main branch. And by

**[10:06]** doing this, you're going to have two

**[10:07]** benefits. One is that you actually can

**[10:09]** be able to build things much more

**[10:10]** faster, because you're going to have

**[10:11]** multiple terminal sessions. And second

**[10:13]** one here is that you can be able to make

**[10:14]** it much more easier here for you to AB

**[10:16]** test, right? For example, it could be

**[10:18]** like a UI changes, or for example,

**[10:20]** you're going to spin up a different

**[10:20]** session here, maybe for a back-end

**[10:22]** changes, or maybe database changes.

**[10:24]** Whatever changes might be, and they're

**[10:25]** all working on the same task. And by the

**[10:27]** end of it, you're just going to choose

**[10:29]** the one that has the most accuracy, or

**[10:31]** has the most best look, or whichever has

**[10:34]** the best results that you want, and you

**[10:35]** can just choose that one. And that's

**[10:37]** going to increase your productivity much

**[10:38]** more better, because, hey, AI agent here

**[10:40]** can make mistakes, and you can reduce

**[10:42]** that chance from making mistake by

**[10:44]** relying on just one single output. You

**[10:46]** can have multiple outputs here, compare

**[10:47]** one of them, and just choose that one to

**[10:50]** go down to. And that's exactly how it

**[10:52]** works with this agent pattern. All

**[10:53]** right, so now let's take a look at the

**[10:55]** next agent pattern, which is headless.

**[10:57]** Now, this is actually my favorite, um,

**[10:59]** which is the most used pattern that I

**[11:01]** always use. It's basically going to

**[11:02]** allow you to use Claude Co here very

**[11:04]** autonomously. So, what it essentially

**[11:06]** does here is that whenever we use

**[11:07]** Claude, right? We do like Claude, or

**[11:09]** Claude dangerously skip permissions, you

**[11:12]** can see that that's basically how we

**[11:13]** interact with Claude. We just simply

**[11:15]** just going to do it inside of Claude Co

**[11:16]** sessions, right? But what you can do

**[11:18]** here is that if you do hyphen P, you

**[11:19]** provide the prompt. For example, what is

**[11:21]** 1 + 1? It's going to give you the answer

**[11:24]** that it generates, and it's going to run

**[11:26]** this in the background. So, without you

**[11:27]** having to be interacting in the Claude

**[11:29]** session, you can do this in the

**[11:31]** terminal, right? You if you want to say,

**[11:33]** "Okay, what is 1 + 1?" Or what's the

**[11:35]** weather today? It's going to generate

**[11:36]** that in the background, and split it

**[11:37]** back in the terminal, right? Now, why is

**[11:39]** it powerful? Because you can actually be

**[11:41]** able to automate, or be able to make

**[11:43]** this completely autonomous by just

**[11:45]** simply just providing the commands, and

**[11:47]** having Claude Co session to run, right?

**[11:49]** Currently, I'm in the Claude Co session.

**[11:51]** I'm going to say, "Hey, why don't you

**[11:52]** run this?" It's going to basically run

**[11:53]** this, and what you can do here is that

**[11:55]** you can even combine that with a bunch

**[11:56]** of skills, like, "Hey, why don't you

**[11:58]** just schedule this, and run this command

**[12:00]** right here every 7:00 a.m., right?" And

**[12:02]** Claude Co here is going to do this

**[12:04]** autonomously, or every run this every 20

**[12:06]** minutes, or run this maybe like, you

**[12:08]** know, every time when something is being

**[12:11]** triggered, right? You can do this,

**[12:12]** setting all kinds of things for this

**[12:14]** kind of task. And furthermore, what you

**[12:16]** can do here is that you can combine the

**[12:17]** power with Ralph Loop, right? Ralph

**[12:19]** Loop, basically, I actually made a

**[12:21]** video, and essentially what it does here

**[12:23]** is that you can set your AI agent here

**[12:24]** to be completely autonomous, how to fix

**[12:26]** something, maybe a bug, maybe you try to

**[12:28]** perfect the UI, or maybe you have a

**[12:30]** certain workflow, and just have it to

**[12:32]** cycle through until, you know, get it

**[12:34]** done. You just have it to set a

**[12:36]** breakpoint on, for example, "Hey, I want

**[12:38]** to you fix this." So, while it's not

**[12:40]** fixed, just continue running, right? And

**[12:42]** the power of this is that I was able to

**[12:44]** use this for reviewing process. I

**[12:46]** specify how many times it should review,

**[12:48]** like cycle through to review, and I

**[12:49]** simply just going to let it run. You You

**[12:51]** know, for example, the first iteration

**[12:53]** here is going to have like run like

**[12:54]** multiples of agent here to check to see,

**[12:56]** "Okay, is it good or not?" Right? Then

**[12:58]** we have the second iteration, the third

**[13:00]** iteration here. Each iteration here is

**[13:02]** going to review the things with a fresh

**[13:04]** context window, like we just mentioned,

**[13:06]** using the headless commands. And what

**[13:08]** essentially here is going to do is it's

**[13:11]** going to basically try to summarize

**[13:13]** everything into a single report, and

**[13:15]** it's going to aggregate that into a

**[13:16]** single result, right? So, for example, I

**[13:18]** have the first session run, done, and

**[13:21]** then second session done, third session

**[13:23]** done. That is going to aggregate all the

**[13:24]** results that I find into a single

**[13:26]** result. And that's exactly how that

**[13:28]** works. I basically package everything

**[13:30]** here into a single skill, called the

**[13:32]** iterative review. And the way how it

**[13:34]** works here, you can see this is the

**[13:35]** iterative review skill that I created.

**[13:37]** It's going to specify, "Okay, I want you

**[13:39]** to review this for five iterations." And

**[13:41]** I simply provide a pull request URL, or

**[13:43]** a branch name. It's going to review the

**[13:45]** changes. First, going to read the skill,

**[13:47]** write exactly what's the rules. Then

**[13:49]** it's basically going to trigger the

**[13:50]** script, which is a SH command. It's

**[13:52]** going to basically try to run the

**[13:53]** command right here, like, "Hey, this is

**[13:55]** the prompt, which is stored in the MD

**[13:57]** file." And each session here, we're

**[13:59]** going to have a fresh context window.

**[14:01]** And when we try to trigger this hyphen P

**[14:03]** for a fresh context for this headless

**[14:05]** operation, it's basically going to

**[14:07]** trigger like spin up like five to seven

**[14:08]** sub agents here to run in the same time.

**[14:11]** And for each time they run, it's going

**[14:12]** to get its fresh context window. And

**[14:14]** after it, it's going to aggregate all

**[14:15]** the findings that it has for after all

**[14:17]** the iterations, and summarize everything

**[14:19]** into a single report. And literally, for

**[14:21]** those bunch of sub agents we're going to

**[14:22]** spin up, we actually can be able to

**[14:24]** choose bunch of agents of our choice,

**[14:26]** just like I mentioned from the previous

**[14:27]** sections, right?
