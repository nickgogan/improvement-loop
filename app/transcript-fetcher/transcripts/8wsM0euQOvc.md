# Transcript: 5 Insane Claude Loops You Need To Use Right Now

**URL:** https://www.youtube.com/watch?v=8wsM0euQOvc
**Segments:** 417
**Channel:** AI LABS
**Duration:** 13:25
**Uploaded:** 2026-07-09

---

## Full Text

You've probably already heard about agent loops since everyone is hyping them up a lot right now. And you might think they're just a way for these AI companies to get you spending more on their products since these loops chew through a lot of tokens. But that only happens when you're using the wrong type of loop for the job. As you already know, we're a software company and we've been experimenting with these loops in our AI coding tasks. Along the way, we've mapped out the different types of loops and which use cases each one is actually suited for. So, out of all the loops we've set up, we're going to share the ones we found genuinely useful. We'll also show you how to set up each one and how each loop is going to impact your workflow. Before we [snorts] get into the different types of loops, let's quickly recap what loop engineering actually is for those of you who are new here. We won't go deep here, but if you want the full breakdown, we covered it in a previous video on the channel. The core idea of loop engineering is that you stop being the person writing the prompts that drive the agent and you turn it into a system that writes the loop itself. Instead of spending your time setting things up and writing long, carefully structured prompts just to get it to build, you let the agent handle everything on its own. It learns as it goes, grows from the problems it hits along the way, and figures out what it needs to do next. That's what an agent loop really is. In that previous video, we split loops into two types based on the outcome you get, the deterministic loop and the non-deterministic loop. A deterministic loop is the kind where you already know the outcome. So, the agent has a solid way to check its own work against it and it keeps working until it gets there. A non-deterministic loop is the kind where you don't, so there's no solid way for the agent to check its work, which means you need other ways to handle it. But that was a broad split and we showed just one way to set each of them up. They can be built in a lot of different ways and each setup changes what you can do. The first type is one most of you have probably already used. It's basically the building block of every other loop and the clearest example is the goal command. We call it the stateless loop and basically it means the loop doesn't hold on to anything or improve itself as it works. There's no part where it learns from what happened and gets better. That's exactly what makes these the simplest loops there are. The one you've probably already seen of this type is the Ralph loop, and it's stateless because it never kept any memory. It just ran the same task again and again, and the moment it saw the task was finished, it stopped. As you might already know about the goal command, it is the best example of the stateless loop. To use it, you tell it what you want to build right after the goal command. From there, Claude sets that as the goal and starts working on it. Then every time the main agent decides a task is done, it uses a smaller model to double-check the work. In Claude code, that smaller model is Haiku. It checks everything the agent did against the requirements you gave in the prompt, and if the task isn't fully done, it reprompts the agent to finish what it missed. But there's a problem with this loop. It leans entirely on the model to decide whether a task's done with no standard to measure the work against. That's why it works best on features whose requirements you can check in some hard concrete way. One way to do that is with tests. Like we talked about in our previous video, we write the tests before asking Claude to build any feature. That way, if Claude changes that feature in a way it shouldn't, the tests throw an error and tell Claude its implementation is off. And once we've got tests for every feature, we can hand the agent real autonomy and let it work without worrying it'll break the other features or build the one we want the wrong way. Once you've written the tests, you can ask Claude code to set the goal as getting that feature to pass all the tests. And it keeps writing code, running the tests to check itself, and keeps going until every test passes. Once they all pass, that means the feature's built correctly, and Claude will mark the goal as complete. Since the agent's working on its own, you'll want to add one line to your Claude.md file. That line tells the agent to save every working version of the app. That way, if it breaks the app somewhere down the line, it can just roll back to the last version that worked and carry on from there instead of trying to undo changes from memory. But before we move on to more types, let's have a word by our sponsor, Minimax. Minimax just dropped M3 and it's the first open weight model to hit the frontier on three things at once, coding, a 1 million token context, and native multimodality. So, we plug the M3 API straight into Claude code and gave it one real job, research the top electric cars on sale now and build a live comparison dashboard. M3 took it from there on its own. It browsed the web, pulled real specs and prices, then shipped a working dashboard from scratch. You can search different EV brands, browse their latest models, and everything updates in real time. On autonomous browsing, it beats Opus 4.7 and its million token context held every page plus the whole code base in one window. But, agent runs like this burn a lot of tokens and that's where the Minimax token plan comes in. Pick token plan for fixed costs or pay as you go for flexibility. Text, image, speech, and music share the same token pool with the highest quotas. Plans start at just $20 per month. So, hit the first link in the description and get an exclusive 12% off. The stateless loop we just walked through holds no state. It does everything on its own from the instructions with no self-improvement in the process. The next type works the opposite way and we call it the learning loop. A learning loop works differently. Instead of just getting a task done and stopping like a stateless loop or the gold command, it focuses on improving something you'll use repeatedly, whether that's a skill or a workflow. The way it does that is simple. It runs the skill, observes how it performed, and then improves it based on what it learned, keeping a complete record of every lesson along the way. So, that when you run the skill, when you're actually using it, the agent knows what caused issues in past, so it won't lean towards that. You can put this kind of loop to work for a lot of things. For example, on the community website of ours, we built multiple skills to handle different repeated workflows while putting the site together. But, building a skill raises an obvious question, which is how you'd even know whether it's working the way it should. So, to answer that, we set up a full learning loop. We did it by creating a skill loop command that triggers the loop. This command contains instructions to call a skill improver agent and keep calling it until there is no more improvements left. This skill improver is actually an agent we created, which improves the skill by assessing its quality, testing it across multiple areas, and watching for the issues that come up. To use it, you just run the command and pass in whichever skill you want to improve, and it gets to work. This loop runs in multiple rounds. In each round, it runs a set of tests and checks after making its changes. Then it launches a separate Claude session that works only on the prompt you pass it, running in the background without stopping to ask permission for anything, and reporting the output back. Inside those sessions, it runs the implementation two ways, one with the skill and one without, so it can measure the actual impact the skill has. That comparison lets it pin down exactly what needs improving, and it makes those changes directly. But, the most important part is the learning.md file it creates. This file gives the agent a way to know what works and what doesn't, and it lives inside the skill itself. It's basically an improvement journal that documents everything the agent learns in a structured format. It records what it tried and what the result was, both with the skill and without it, then lists the lessons it picked up across all the rounds it worked through. And that's how it keeps going round after round until the skill is refined into the best possible version of itself. You can use the same setup to improve any workflow you've got. In our previous video, we showed how to build a loop agents, one that handles the implementation and another that reviews the work and reports back fixes for the implementation agent to apply. There's a problem with that setup, which is that a single review agent is handling every aspect of the review on its own. But, a review is never about just one aspect. It always comes from different perspectives, and that's too much ground for one agent to cover alone. It's better to split those across different agents, because when multiple agents review across multiple dimensions, they cover the blind spots any single agent would miss, and that makes the review way more complete. The idea is close to the LLM council that Andrej Karpathy released, which is a council of multiple agents that talk to each other and argue over a topic you hand them. Using the reasoning of several models to land on the right answer. For creating a multi-agent loop, you need to create multiple agents. So, for example, we created four agents in the loop we set up. The first checks for factual correctness, and it comes with tools like web search, so it can ground itself in real sources. The second is a domain checker agent, which checks whether whatever is being reviewed is actually relevant to what we're trying to do. The third is a safety critic agent, which looks at the safety issues like sensitive content along with security risks and policy violations that could cause problems down the line. And the last is the style critic, which makes sure the content is clear and well-written and tailored to the style we're after. You can use these agents for any task, whether it's coding or not. What ties these four together is an orchestrate command that we created. contains the detailed instructions for how it should manage and coordinate all four agents and handle the feedback each one reports back. To start the loop, you run the orchestrate command and ask it to review whatever you want, and it spins up all the agents for the process. The orchestrate command runs in multiple rounds, too, spinning up every agent in each round. The main agent applies all the fixes reported in round one, then spins them all up again for the next round. By the end of the final pass, you're left with the app in way better shape. If you'd rather the agents communicate directly, you can use the agent teams workflow we covered in a previous video, which gives you more of the LLM council experience without one agent handling all the communication. But, we chose the orchestrator because one agent needs to hold the context of the previous rounds to coordinate the workflow properly. Another [snorts] type we reach for often is the verification loop. It uses multiple agents as well, where one does the implementing and the other scores that implementation, and the implementer's whole job is to get that score as high as possible against a set metric. To set that up, we created a command that coordinates the entire loop, running the whole review workflow on its own. As you already know that cursor has thermonuclear review. It's actually a really powerful review skill that checks how clean and healthy the code is, so it stays easy to build on later. It audits all of the code and hands back an in-depth review with non-negotiable standards, so you're guaranteed the highest quality review it can produce. To do that, it runs a dynamic workflow. The review has to span a lot of categories and a dynamic workflow is the best way to handle that, since it fans the work out across multiple sub-agents that each take on a different aspect at once. Like we mentioned earlier, we created two agents that act as the players in this loop. The first is the implementer, whose job is to read the PRD and then build the required functionality. The second is the thermonuclear code reviewer, and its only job is to hand back a review score. Since all it does is review and score, it doesn't have tools for editing. To trigger it, you run the review loop command. by understanding what the app is meant to build, then kicks off a thermonuclear review for round one. That first review flags the issues it finds, including a critical one that's stopping the app from even starting. It records the findings in a JSON file and spins up the implementer agent to fix them. The loop keeps going from there, but keep one thing in mind. Because it's reviewing across so many dimensions, it takes a really long time and eats up a lot of tokens, since the dynamic workflow driving it fans the work across a whole set of sub-agents at once. So, we wouldn't recommend it unless you've already built the whole app at a larger scale and want it thoroughly reviewed. You can also build this same loop without the dynamic workflow by using a normal reviewer agent, which takes less time and burns through way fewer tokens. And if you're enjoying the video so far, subscribe to the channel and hit the hype button. This small gesture of support goes a long way for us. Out of every loop we've shown you so far, none of them had a separate step for improving the loop itself. But that's really a core of what a loop is meant to do. That's where the workflow improvement loop comes in. What this loop does is go a step beyond just repeating the task. Instead of just running it again and again, it looks at the process itself and suggests improvements to the workflow. Now, you might think the learning loop from earlier already does this. But, there's a real difference. The learning loop improves a skill, one piece inside the process. This one improves the loop itself, the whole process you've set up. The entry point is an iterate command that acts as the orchestrator for everything that happens during each run. There are three agents this time. The first is a builder agent, which handles the implementation and delivers one of the app's requirements on each run. The second is a scorer that checks that implementation against a rubric we defined to act as the app's quality guardrail and scores the work out of 100. And the third is the process optimizer agent, which is the one that actually handles self-improvement. Normally, a loop runs through the same cycle where it plans, implements, verifies, and repeats. But, this agent adds an extra step of going back over the loop iteration and suggesting ways to make it better. To use it, you just run the command iterate all. By all, we mean we're implementing the entire app broken into parts inside a single workflow. The loop starts by spinning up the builder agent, then the scorer evaluates what it built against the rubric and records the score in a JSON file that tracks every round. Then, the process optimizer agent kicks in, going through the conversation to spot anything that could improve the workflow, making sure the app is built to a high quality, and the right steps are being followed. So, by the end of this workflow, you don't just walk away with a built app. You walk away with a workflow that's been tested and refined, with every step validated as one that actually needs to be there. That brings us to the end of this video. If you'd like to support the channel and help us keep making videos like this, you can do so by using the Super Thanks button below. As always, thank you for watching, and I'll see you in the next one.

---

## Timestamped Segments

**[0:00]** You've probably already heard about

**[0:01]** agent loops since everyone is hyping

**[0:03]** them up a lot right now. And you might

**[0:05]** think they're just a way for these AI

**[0:07]** companies to get you spending more on

**[0:09]** their products since these loops chew

**[0:11]** through a lot of tokens. But that only

**[0:12]** happens when you're using the wrong type

**[0:14]** of loop for the job. As you already

**[0:16]** know, we're a software company and we've

**[0:18]** been experimenting with these loops in

**[0:20]** our AI coding tasks. Along the way,

**[0:22]** we've mapped out the different types of

**[0:23]** loops and which use cases each one is

**[0:25]** actually suited for. So, out of all the

**[0:27]** loops we've set up, we're going to share

**[0:29]** the ones we found genuinely useful.

**[0:31]** We'll also show you how to set up each

**[0:33]** one and how each loop is going to impact

**[0:35]** your workflow. Before we [snorts] get

**[0:37]** into the different types of loops, let's

**[0:39]** quickly recap what loop engineering

**[0:41]** actually is for those of you who are new

**[0:43]** here. We won't go deep here, but if you

**[0:45]** want the full breakdown, we covered it

**[0:47]** in a previous video on the channel. The

**[0:48]** core idea of loop engineering is that

**[0:51]** you stop being the person writing the

**[0:52]** prompts that drive the agent and you

**[0:54]** turn it into a system that writes the

**[0:56]** loop itself. Instead of spending your

**[0:58]** time setting things up and writing long,

**[1:00]** carefully structured prompts just to get

**[1:02]** it to build, you let the agent handle

**[1:03]** everything on its own. It learns as it

**[1:05]** goes, grows from the problems it hits

**[1:07]** along the way, and figures out what it

**[1:09]** needs to do next. That's what an agent

**[1:11]** loop really is. In that previous video,

**[1:13]** we split loops into two types based on

**[1:15]** the outcome you get, the deterministic

**[1:17]** loop and the non-deterministic loop. A

**[1:19]** deterministic loop is the kind where you

**[1:21]** already know the outcome. So, the agent

**[1:23]** has a solid way to check its own work

**[1:25]** against it and it keeps working until it

**[1:27]** gets there. A non-deterministic loop is

**[1:29]** the kind where you don't, so there's no

**[1:31]** solid way for the agent to check its

**[1:33]** work, which means you need other ways to

**[1:35]** handle it. But that was a broad split

**[1:36]** and we showed just one way to set each

**[1:38]** of them up. They can be built in a lot

**[1:40]** of different ways and each setup changes

**[1:42]** what you can do. The first type is one

**[1:44]** most of you have probably already used.

**[1:46]** It's basically the building block of

**[1:48]** every other loop and the clearest

**[1:50]** example is the goal command. We call it

**[1:52]** the stateless loop and basically it

**[1:53]** means the loop doesn't hold on to

**[1:55]** anything or improve itself as it works.

**[1:57]** There's no part where it learns from

**[1:59]** what happened and gets better. That's

**[2:00]** exactly what makes these the simplest

**[2:02]** loops there are. The one you've probably

**[2:04]** already seen of this type is the Ralph

**[2:06]** loop, and it's stateless because it

**[2:08]** never kept any memory. It just ran the

**[2:10]** same task again and again, and the

**[2:11]** moment it saw the task was finished, it

**[2:13]** stopped. As you might already know about

**[2:15]** the goal command, it is the best example

**[2:17]** of the stateless loop. To use it, you

**[2:19]** tell it what you want to build right

**[2:21]** after the goal command. From there,

**[2:22]** Claude sets that as the goal and starts

**[2:25]** working on it. Then every time the main

**[2:26]** agent decides a task is done, it uses a

**[2:29]** smaller model to double-check the work.

**[2:31]** In Claude code, that smaller model is

**[2:33]** Haiku. It checks everything the agent

**[2:35]** did against the requirements you gave in

**[2:36]** the prompt, and if the task isn't fully

**[2:38]** done, it reprompts the agent to finish

**[2:40]** what it missed. But there's a problem

**[2:42]** with this loop. It leans entirely on the

**[2:44]** model to decide whether a task's done

**[2:46]** with no standard to measure the work

**[2:48]** against. That's why it works best on

**[2:50]** features whose requirements you can

**[2:51]** check in some hard concrete way. One way

**[2:54]** to do that is with tests. Like we talked

**[2:56]** about in our previous video, we write

**[2:58]** the tests before asking Claude to build

**[3:00]** any feature. That way, if Claude changes

**[3:02]** that feature in a way it shouldn't, the

**[3:04]** tests throw an error and tell Claude its

**[3:06]** implementation is off. And once we've

**[3:07]** got tests for every feature, we can hand

**[3:09]** the agent real autonomy and let it work

**[3:12]** without worrying it'll break the other

**[3:13]** features or build the one we want the

**[3:15]** wrong way. Once you've written the

**[3:16]** tests, you can ask Claude code to set

**[3:19]** the goal as getting that feature to pass

**[3:21]** all the tests. And it keeps writing

**[3:22]** code, running the tests to check itself,

**[3:25]** and keeps going until every test passes.

**[3:27]** Once they all pass, that means the

**[3:29]** feature's built correctly, and Claude

**[3:30]** will mark the goal as complete. Since

**[3:32]** the agent's working on its own, you'll

**[3:34]** want to add one line to your Claude.md

**[3:37]** file. That line tells the agent to save

**[3:39]** every working version of the app. That

**[3:41]** way, if it breaks the app somewhere down

**[3:42]** the line, it can just roll back to the

**[3:44]** last version that worked and carry on

**[3:46]** from there instead of trying to undo

**[3:48]** changes from memory. But before we move

**[3:50]** on to more types, let's have a word by

**[3:52]** our sponsor, Minimax. Minimax just

**[3:54]** dropped M3 and it's the first open

**[3:56]** weight model to hit the frontier on

**[3:58]** three things at once, coding, a 1

**[4:01]** million token context, and native

**[4:03]** multimodality. So, we plug the M3 API

**[4:06]** straight into Claude code and gave it

**[4:08]** one real job, research the top electric

**[4:10]** cars on sale now and build a live

**[4:12]** comparison dashboard. M3 took it from

**[4:14]** there on its own. It browsed the web,

**[4:16]** pulled real specs and prices, then

**[4:18]** shipped a working dashboard from

**[4:20]** scratch. You can search different EV

**[4:22]** brands, browse their latest models, and

**[4:24]** everything updates in real time. On

**[4:25]** autonomous browsing, it beats Opus 4.7

**[4:29]** and its million token context held every

**[4:31]** page plus the whole code base in one

**[4:33]** window. But, agent runs like this burn a

**[4:35]** lot of tokens and that's where the

**[4:37]** Minimax token plan comes in. Pick token

**[4:39]** plan for fixed costs or pay as you go

**[4:41]** for flexibility. Text, image, speech,

**[4:44]** and music share the same token pool with

**[4:46]** the highest quotas. Plans start at just

**[4:48]** $20 per month. So, hit the first link in

**[4:50]** the description and get an exclusive 12%

**[4:53]** off. The stateless loop we just walked

**[4:56]** through holds no state. It does

**[4:57]** everything on its own from the

**[4:59]** instructions with no self-improvement in

**[5:01]** the process. The next type works the

**[5:03]** opposite way and we call it the learning

**[5:05]** loop. A learning loop works differently.

**[5:07]** Instead of just getting a task done and

**[5:08]** stopping like a stateless loop or the

**[5:10]** gold command, it focuses on improving

**[5:12]** something you'll use repeatedly, whether

**[5:14]** that's a skill or a workflow. The way it

**[5:16]** does that is simple. It runs the skill,

**[5:18]** observes how it performed, and then

**[5:20]** improves it based on what it learned,

**[5:22]** keeping a complete record of every

**[5:24]** lesson along the way. So, that when you

**[5:25]** run the skill, when you're actually

**[5:27]** using it, the agent knows what caused

**[5:29]** issues in past, so it won't lean towards

**[5:31]** that. You can put this kind of loop to

**[5:33]** work for a lot of things. For example,

**[5:35]** on the community website of ours, we

**[5:36]** built multiple skills to handle

**[5:38]** different repeated workflows while

**[5:40]** putting the site together. But, building

**[5:42]** a skill raises an obvious question,

**[5:44]** which is how you'd even know whether

**[5:46]** it's working the way it should. So, to

**[5:47]** answer that, we set up a full learning

**[5:49]** loop. We did it by creating a skill loop

**[5:51]** command that triggers the loop. This

**[5:53]** command contains instructions to call a

**[5:55]** skill improver agent and keep calling it

**[5:57]** until there is no more improvements

**[5:58]** left. This skill improver is actually an

**[6:01]** agent we created, which improves the

**[6:03]** skill by assessing its quality, testing

**[6:05]** it across multiple areas, and watching

**[6:07]** for the issues that come up. To use it,

**[6:09]** you just run the command and pass in

**[6:10]** whichever skill you want to improve, and

**[6:12]** it gets to work. This loop runs in

**[6:14]** multiple rounds. In each round, it runs

**[6:16]** a set of tests and checks after making

**[6:18]** its changes. Then it launches a separate

**[6:20]** Claude session that works only on the

**[6:22]** prompt you pass it, running in the

**[6:24]** background without stopping to ask

**[6:26]** permission for anything, and reporting

**[6:27]** the output back. Inside those sessions,

**[6:30]** it runs the implementation two ways, one

**[6:32]** with the skill and one without, so it

**[6:34]** can measure the actual impact the skill

**[6:36]** has. That comparison lets it pin down

**[6:38]** exactly what needs improving, and it

**[6:40]** makes those changes directly. But, the

**[6:41]** most important part is the learning.md

**[6:44]** file it creates. This file gives the

**[6:46]** agent a way to know what works and what

**[6:48]** doesn't, and it lives inside the skill

**[6:50]** itself. It's basically an improvement

**[6:52]** journal that documents everything the

**[6:54]** agent learns in a structured format. It

**[6:56]** records what it tried and what the

**[6:57]** result was, both with the skill and

**[6:59]** without it, then lists the lessons it

**[7:01]** picked up across all the rounds it

**[7:02]** worked through. And that's how it keeps

**[7:04]** going round after round until the skill

**[7:06]** is refined into the best possible

**[7:08]** version of itself. You can use the same

**[7:09]** setup to improve any workflow you've

**[7:11]** got. In our previous video, we showed

**[7:13]** how to build a loop agents, one that

**[7:16]** handles the implementation and another

**[7:17]** that reviews the work and reports back

**[7:19]** fixes for the implementation agent to

**[7:21]** apply. There's a problem with that

**[7:23]** setup, which is that a single review

**[7:24]** agent is handling every aspect of the

**[7:27]** review on its own. But, a review is

**[7:28]** never about just one aspect. It always

**[7:31]** comes from different perspectives, and

**[7:32]** that's too much ground for one agent to

**[7:34]** cover alone. It's better to split those

**[7:36]** across different agents, because when

**[7:38]** multiple agents review across multiple

**[7:40]** dimensions, they cover the blind spots

**[7:42]** any single agent would miss, and that

**[7:44]** makes the review way more complete. The

**[7:46]** idea is close to the LLM council that

**[7:48]** Andrej Karpathy released, which is a

**[7:50]** council of multiple agents that talk to

**[7:52]** each other and argue over a topic you

**[7:54]** hand them. Using the reasoning of

**[7:56]** several models to land on the right

**[7:58]** answer. For creating a multi-agent loop,

**[8:00]** you need to create multiple agents. So,

**[8:01]** for example, we created four agents in

**[8:03]** the loop we set up. The first checks for

**[8:05]** factual correctness, and it comes with

**[8:07]** tools like web search, so it can ground

**[8:09]** itself in real sources. The second is a

**[8:11]** domain checker agent, which checks

**[8:13]** whether whatever is being reviewed is

**[8:15]** actually relevant to what we're trying

**[8:16]** to do. The third is a safety critic

**[8:18]** agent, which looks at the safety issues

**[8:20]** like sensitive content along with

**[8:22]** security risks and policy violations

**[8:24]** that could cause problems down the line.

**[8:26]** And the last is the style critic, which

**[8:27]** makes sure the content is clear and

**[8:29]** well-written and tailored to the style

**[8:31]** we're after. You can use these agents

**[8:33]** for any task, whether it's coding or

**[8:35]** not. What ties these four together is an

**[8:37]** orchestrate command that we created.

**[8:40]** contains the detailed instructions for

**[8:42]** how it should manage and coordinate all

**[8:44]** four agents and handle the feedback each

**[8:46]** one reports back. To start the loop, you

**[8:48]** run the orchestrate command and ask it

**[8:50]** to review whatever you want, and it

**[8:52]** spins up all the agents for the process.

**[8:54]** The orchestrate command runs in multiple

**[8:56]** rounds, too, spinning up every agent in

**[8:58]** each round. The main agent applies all

**[9:00]** the fixes reported in round one, then

**[9:02]** spins them all up again for the next

**[9:04]** round. By the end of the final pass,

**[9:06]** you're left with the app in way better

**[9:07]** shape. If you'd rather the agents

**[9:09]** communicate directly, you can use the

**[9:11]** agent teams workflow we covered in a

**[9:13]** previous video, which gives you more of

**[9:14]** the LLM council experience without one

**[9:17]** agent handling all the communication.

**[9:19]** But, we chose the orchestrator because

**[9:21]** one agent needs to hold the context of

**[9:23]** the previous rounds to coordinate the

**[9:25]** workflow properly. Another [snorts] type

**[9:27]** we reach for often is the verification

**[9:28]** loop. It uses multiple agents as well,

**[9:31]** where one does the implementing and the

**[9:32]** other scores that implementation, and

**[9:34]** the implementer's whole job is to get

**[9:36]** that score as high as possible against a

**[9:38]** set metric. To set that up, we created a

**[9:40]** command that coordinates the entire

**[9:42]** loop, running the whole review workflow

**[9:44]** on its own. As you already know that

**[9:46]** cursor has thermonuclear review. It's

**[9:48]** actually a really powerful review skill

**[9:50]** that checks how clean and healthy the

**[9:52]** code is, so it stays easy to build on

**[9:54]** later. It audits all of the code and

**[9:56]** hands back an in-depth review with

**[9:58]** non-negotiable standards, so you're

**[9:59]** guaranteed the highest quality review it

**[10:01]** can produce. To do that, it runs a

**[10:03]** dynamic workflow. The review has to span

**[10:05]** a lot of categories and a dynamic

**[10:07]** workflow is the best way to handle that,

**[10:09]** since it fans the work out across

**[10:11]** multiple sub-agents that each take on a

**[10:13]** different aspect at once. Like we

**[10:15]** mentioned earlier, we created two agents

**[10:17]** that act as the players in this loop.

**[10:19]** The first is the implementer, whose job

**[10:21]** is to read the PRD and then build the

**[10:23]** required functionality. The second is

**[10:25]** the thermonuclear code reviewer, and its

**[10:27]** only job is to hand back a review score.

**[10:29]** Since all it does is review and score,

**[10:31]** it doesn't have tools for editing. To

**[10:33]** trigger it, you run the review loop

**[10:35]** command. by understanding what the app

**[10:37]** is meant to build, then kicks off a

**[10:39]** thermonuclear review for round one. That

**[10:41]** first review flags the issues it finds,

**[10:43]** including a critical one that's stopping

**[10:45]** the app from even starting. It records

**[10:47]** the findings in a JSON file and spins up

**[10:50]** the implementer agent to fix them. The

**[10:52]** loop keeps going from there, but keep

**[10:53]** one thing in mind. Because it's

**[10:55]** reviewing across so many dimensions, it

**[10:57]** takes a really long time and eats up a

**[10:59]** lot of tokens, since the dynamic

**[11:01]** workflow driving it fans the work across

**[11:03]** a whole set of sub-agents at once. So,

**[11:05]** we wouldn't recommend it unless you've

**[11:07]** already built the whole app at a larger

**[11:09]** scale and want it thoroughly reviewed.

**[11:11]** You can also build this same loop

**[11:12]** without the dynamic workflow by using a

**[11:15]** normal reviewer agent, which takes less

**[11:17]** time and burns through way fewer tokens.

**[11:19]** And if you're enjoying the video so far,

**[11:21]** subscribe to the channel and hit the

**[11:23]** hype button. This small gesture of

**[11:24]** support goes a long way for us. Out of

**[11:27]** every loop we've shown you so far, none

**[11:29]** of them had a separate step for

**[11:30]** improving the loop itself. But that's

**[11:32]** really a core of what a loop is meant to

**[11:34]** do. That's where the workflow

**[11:35]** improvement loop comes in. What this

**[11:37]** loop does is go a step beyond just

**[11:39]** repeating the task. Instead of just

**[11:41]** running it again and again, it looks at

**[11:43]** the process itself and suggests

**[11:45]** improvements to the workflow. Now, you

**[11:46]** might think the learning loop from

**[11:48]** earlier already does this. But, there's

**[11:49]** a real difference. The learning loop

**[11:51]** improves a skill, one piece inside the

**[11:53]** process. This one improves the loop

**[11:55]** itself, the whole process you've set up.

**[11:57]** The entry point is an iterate command

**[11:59]** that acts as the orchestrator for

**[12:00]** everything that happens during each run.

**[12:03]** There are three agents this time. The

**[12:04]** first is a builder agent, which handles

**[12:06]** the implementation and delivers one of

**[12:08]** the app's requirements on each run. The

**[12:10]** second is a scorer that checks that

**[12:12]** implementation against a rubric we

**[12:14]** defined to act as the app's quality

**[12:16]** guardrail and scores the work out of

**[12:18]** 100. And the third is the process

**[12:20]** optimizer agent, which is the one that

**[12:22]** actually handles self-improvement.

**[12:24]** Normally, a loop runs through the same

**[12:26]** cycle where it plans, implements,

**[12:28]** verifies, and repeats. But, this agent

**[12:30]** adds an extra step of going back over

**[12:32]** the loop iteration and suggesting ways

**[12:34]** to make it better. To use it, you just

**[12:36]** run the command iterate all. By all, we

**[12:38]** mean we're implementing the entire app

**[12:40]** broken into parts inside a single

**[12:41]** workflow. The loop starts by spinning up

**[12:43]** the builder agent, then the scorer

**[12:45]** evaluates what it built against the

**[12:47]** rubric and records the score in a JSON

**[12:49]** file that tracks every round. Then, the

**[12:51]** process optimizer agent kicks in, going

**[12:53]** through the conversation to spot

**[12:55]** anything that could improve the

**[12:56]** workflow, making sure the app is built

**[12:58]** to a high quality, and the right steps

**[13:00]** are being followed. So, by the end of

**[13:02]** this workflow, you don't just walk away

**[13:04]** with a built app. You walk away with a

**[13:06]** workflow that's been tested and refined,

**[13:08]** with every step validated as one that

**[13:10]** actually needs to be there. That brings

**[13:12]** us to the end of this video. If you'd

**[13:14]** like to support the channel and help us

**[13:16]** keep making videos like this, you can do

**[13:18]** so by using the Super Thanks button

**[13:20]** below. As always, thank you for

**[13:21]** watching, and I'll see you in the next

**[13:23]** one.
