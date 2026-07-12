# Transcript: 8 Claude Loops to Build 10x Faster

**URL:** https://www.youtube.com/watch?v=HGCHgD4uGgY
**Segments:** 593
**Channel:** Austin Marchese
**Duration:** 17:11
**Uploaded:** 2026-07-03

---

## Full Text

Loop number one is a data ingestion loop. Before we cover how to create this loop and why it's so valuable, what is an actual Claude loop? A loop is something that runs continuously or on a specific schedule until a task is complete. And to see it in action, loop one is the data ingestion loop. With AI, at the end of the day, your data is your moat. And if you want to differentiate yourself and get a better output, you have to take data aggregation and ingestion very seriously. To set this up, we first connect our data sources. If you click the plus in the desktop app and then select connectors, you can then select the specific resources that you interact with. For me, it's Slack, Gmail, and then Granola for call transcripts. Once you establish those connections, it's time to actually create a skill that aggregates the data for you, validates that it's not just contextual noise, and then ingests it into the system. On screen, you can see a prompt that I used to create a skill called a data ingestion loop. This loop will go to Slack for messages, Gmail for emails, Granola for call transcripts, read the last 24 hours, and remove all of the fluff, and only store the valuable information. For every loop we create, I'm going through a process called skill-driven loop creation, where every loop we create starts as a skill first that we manually run, confirm it works, and then we create a process to automatically run it. At this point, let's assume that we've tested it, and it's now time to actually make this automated. To do this, I use local routines, which I get to by clicking routines, plus, local routine, and then I fill in the information where the instructions is I just use the skill that I already created. In this case, I set the skill to run Mondays at 8:00 a.m. And for every loop we cover here, you can just create a routine if you want to run it automatically in the background. Now, that's just the first of eight Claude code loops that we'll go through in today's video that will help you build faster and more efficiently. And for all eight of these loops, I bucket them into three groups. The first is loops that help you ingest data, get better outputs. The next are loops that help you build faster, and the last is a series of loops that help you create a system that automatically improves over time. Loop number two is external alpha farming. So, what is an alpha farming loop? This is a loop that goes, looks for information that's valuable, and then pulls it into your system. And by sourcing the right information, you're able to get better outputs. Now, there are three parts of this loop, and so here's a prompt to create it, but I'm going to go through each step and why it's important. The first part of it is you want to establish what alpha you're actually farming. And for this, you want to be very specific. So, if you're a content creator, the alpha could be storytelling patterns or recent news topics. If you're building a product, it could be about conversion funnel benchmarks and optimization tactics. If you're a sales rep, it could be objection handling patterns from reps who are closing your exact customer. The second part of this is identify the sources of alpha. This is where you could use AI to help you create a list of options, but ultimately, this is where your human taste comes in. The question you have to ask yourself is who online is creating valuable insight about the topics that you're working on. So, YouTube creators, newsletter creators, Reddit forums, where is there valuable information online that can produce a consistent stream of up-to-date information? The third part is that you validate the source has level two analysis. Most people skip this part, but this is where it becomes an actual loop. So, level one analysis is where AI just gives you basic stuff, right? The basic framework, something that doesn't really differentiate the output. Level two analysis is the non-obvious information that brings an output from good to great. And you want to curate it so only level two information is ingested into your system. Here on screen, you can see me running the alpha farming loop, and you can see that it's actually going and fetching different resources. One thing I want to call out is that I do use an MCP called Firecall that helps me get better information across the internet. Now, before we get to the next loop, which will focus on internal alpha farming, you may find that a lot of what we're covering feels a bit technical, which brings us to today's video sponsor, nexus.ai. This is what I call an AI platform, which is a category of tools I love. And then the reason for this is that it removes all the technical skills that are normally needed to set up AI agent systems, and it can save you hundreds of dollars each month because you don't have to pay for five different AI tools. There are three specific features that I love. The first is that every flagship model is included in a single nexus login. So, ChatGPT, Claude, Gemini, Grok, 200 plus other models can all be accessed directly through Nexus. And this is critical because there's really no single best AI model. Different ones are better at different things, and Nexus AI will automatically route each prompt to the best one. The second feature is that there's zero data retention. This means that your data is never used to train their models, and that alone is one of the big reasons why I can even consider using this tool for client work. And the third feature is their no-code AI agent builder. At the end of the day, if you can use the internet, you can use Nexus to build AI agents. You just describe what you want, and Nexus will build the agent for you. And whether it's for one-time jobs like I need to do deep research on this topic like right now, or for repetitive tasks like turning your notes into a weekly report automatically, Nexus will handle all of this. For me, I have a lot of products in my ecosystem, my YouTube, my newsletter, Build Partner, so it's hard to keep track of all of this. So, what I can do is create a weekly report that analyzes my entire marketing funnel, and connect it to my Slack to send my entire team a summary of website visits, conversions, and what we need to work on. This is a task that I'd normally just never do because I just don't have the time. So, to check out Nexus, click the first link in the description you'll get 50% off. And that 50% discount is for a limited time because when I was working with them, I had to stress the importance of getting a large discount for everyone watching. So, go check that out. Now, getting to loop number three, which is internal alpha farming loop. If loop number two was all about hunting for external alpha farming, loop number three hunts for internal alpha. This will look across all the data that's already in your system, and surface what's recurring, where the gaps are, and what you should be doing about it. To set this up, it's broken down into three parts. The first part is you want to establish what internal alpha you're farming. If you're a content creator, which video concepts actually landed and performed? If you're building a product, what features do people keep requesting? If you're a sales rep, what questions or rebuttals does everyone have, and should you build that into the service? This is the exact kind of pattern that humans will miss, but a loop doesn't. And the insights from this can lead to changes that actually move the needle. The second part is that you want to point it at the right data sets. In loop number one, we set up data ingestion, so this builds on exactly this. But now, you actually have to ask, do I have the necessary data for internal alpha farming loop to actually work? And if the answer is no, this identifies gaps in your data pipeline, and you have to resolve that. And part three is the output is an action list, not a report. Essentially, every internal dashboard tells you all the information about what happened, but none of them actually tell you what to do about it. And one of the things that I tell my team is, don't bring me a problem, bring me a solution. And that's exactly what this loop is designed to do. It creates an implementation plan that passes our plan verification skill to make sure it hits our requirements for any sort of delivery plan. To create this loop, first we need to create that {slash} plan verification skill, which is a utility skill that we'll use whenever we want to verify a plan. Here's a prompt actually create that skill, which will interview you about what tools you're currently using and what you're open to and not open to implementing. The key here is that any implementation plan that this creates has to actually be a viable option. So, the skill is used to keep AI honest about any plan that it actually proposes. Then you use this prompt to create an internal alpha farming loop skill, which will create the loop, identify recurring patterns, and suggest places to improve. This loop will help you identify what you have to build next based on the data you're ingesting. As this loop runs, it'll look at the data that you're ingesting and suggest places for improvement. Now, we've covered ways to ingest data and how to actually analyze it, but the next three loops are all about improving the process in which you build. Loop number four is an optimization loop. This is a process of optimizing a system to approach a specific metric or quantifiable result. For example, it does something pass level two analysis, right? That's hard to actually quantify. But what a proper optimization loop does is it looks at something that is an objective metric. An example could be, how quickly does a website load? So, what this loop will do is it'll pick a specific goal, it'll run a loop, measure the result, if it doesn't actually fit the goal, it'll propose a solution, it'll apply it, re-measure it, and continue this loop until it gets to that final goal. On screen, you'll see a bunch of areas where an optimization loop makes sense, which is typically for more technical delivery mechanisms because these are super quantifiable. When I first started thinking about loops, I thought that all of the feedback back and forth had to happen almost instantly. Make a change, measure result, etc. But that doesn't necessarily have to be the case. So, for example, let's say you have a website and you want to try and optimize conversion rate. You could have a loop that runs, checks the conversion rate for day one, makes a tweak, checks it for day two, etc. And where this feedback loop is over a course of 24 hours. This is entirely fine, and once I kind of realized this, this opened up my brain to the realm of possibilities because initially I thought that this feedback mechanism was way too slow. Now, to create an optimization loop, here is a templated prompt that you can use, and you can fill in for whatever you're trying to work on. Now, before I get to the next loop, if this is your first video of mine, welcome to channel, but if this is your second or more, here is our anti-slop agreement. All of the stuff that I do in this video, right? The the visual, the design, the hours of research, this is for humans, not for AI robots. That's part of the reason why I put all these prompts on screen because it's easier for you to read and screenshot, and it's not for these AI robots to see. So, as part of the agreement, all I ask is that you subscribe to this channel to help this content reach more people. Also, every video I give away a Claude Mac subscription, and this video's winner is the goat I'm Jasmine. They're building a platform to help people connect faster. Absolute bangers. To enter the giveaway, comment below with what you're building, and if you already entered, you can enter again by providing an update on whatever you're working on. Bring us to loop number five, which is code build loop. This loop is specifically if you want to vibe code a product, and everyone watching this video should be vibe coding whether you have a technical background or not. And the key with anything vibe coding is you don't want to just go and grip and rip things. You need to plan before you actually do anything. And what this loop will do is your goals will get extracted. It verifies a delivery plan, and then, and only then, does it go through a loop to complete the tasks. On screen, you can see the prompt, which breaks the task into six parts, which leverages skill chaining to create the actual loop. First, it'll extract or bring in the goal. So, this can be through an interview, or you can bring in a document you already have. The second is it'll plan the delivery using Claude's built-in plan mode. The third is sign off on the plan. This is where you, the human, comes in. The fourth is it'll build it. Fifth is it'll review the code. This uses Claude's /code-review--fix. Sixth, it'll verify the behavior matches the goal. It'll use Claude's /verify to help with this. Now, I went through all six features pretty quickly there, but there are two specific concepts that are critical you understand as you take these loops and start creating your own from scratch. The first is that there's an approval gate. If you look at the third step, it says sign off on the plan. That's an approval gate. And we do this at this stage because this is what I call a critical call checkpoint. If at this point you're in the wrong direction, steps four, five, and six are just going to be entirely wrong, and you're wasting time and money. A general rule of thumb I have is that for any loop that you create, if there is any critical call checkpoint, then you need to add a human approval gate. Now, to be clear, some of these loops may have none of these, but others may have four or five. It really depends on what you're building. The second thing is dynamic workflows. This is how Anthropic divides the goal you have amongst AI agents to complete the task. This is how it actually goes and builds whatever you're trying to build. And there are six patterns that Anthropic has documented for these dynamic workflows, which you can see all of them on screen. But to 80/20 this whole thing, you don't actually have to worry about which one. It'll figure it out for you. But if you do want to play around with it, you can look at the screenshot as a good starting point. Okay, so we've gone through data ingestion as well as how you can build quickly. But loop number six is about creating a system that self-improves with the improve system loop. Of the eight loops that we're covering, this is by far my favorite because it single-handedly transformed my business. Twice a week, I run an improve system loop, Tuesday end of day and Friday end of day, and that makes it so that my entire AI system is self-improving. There are two layers to actually get this done. The first layer is you have to build the improve system skill. This is what actually looks at your system and figures out ways to improve it. So, it'll read sessions, it'll find patterns, it'll propose changes, and I've spoken about this a lot on my channel, but if you want to use the exact one I use, I do have a plugin called billpartner.ai, and you can do /bp improve system, and that's exactly what I use. Here on my screen, you can see me running this skill manually on my system, and it shows all the ways that I can currently improve it. Now that I look at it, I will have to do after filming this video. Now, the second layer for this loop is to actually create the loop, and this is wrapping the skill in a self-improving system loop. But, within this prompt, I log every change that it makes to a changelog.md file. The reason is I want to see what is actually happening in my system, and within those changes, it actually buckets it into three categories. The first bucket is auto-approve. These are all of the low-risk things that it can just automatically improve, aren't really up for debate to improve the system. This is like the self-improving component. Bucket two is need sign-off. These are higher-stakes stuff, like skill edits, or new skill candidates, or structural changes. This is anything where the wrong choice could actually degrade output quality. These changes get written to a review file as a checkbox list. For each of the suggestions, you can improve, reject, or approve and don't ask me again. This is a way to tweak the system over time. And the third bucket is more context needed. This is stuff that the loop can't decide on its own. Let's say, for example, you mention someone three times, and it can't tell if this is a new client or a one-off relationship. This will go in that same review file from bucket two. This three-bucket system is what I found is an effective middle ground to make an automated system that improves without you, makes it easy for you to label improvements, and also keeps you as the tastemaker, so that your system doesn't slowly degrade in quality from what you actually want it to produce. Loop number seven is ecosystem monitoring loop. Whenever you create a loop, more operational debt is added to your system, and this ecosystem monitoring loop is the loop that manages your other loops. This is some loop-ception type sh Now, before you say this is ridiculous, we're just going to be burning through tokens, there's some key features why this can actually save you tokens while running a more efficient system. On screen, you'll see a prompt to create the actual loop, but there are three important features to call out. The first feature is it surfaces composability opportunities across loops. As you build more loops, you'll unknowingly write the same logic twice. For example, let's say you have two loops that require fetching data from Slack. There's a chance that both of these contain the same logic. The so the ecosystem monitoring loop scans your loop library, finds repeated logic, and suggests pulling it out into a composable skill that every loop can call. That's exactly what we did with the plan verification skill back in loop number three. We built it once and then any other loop can use it. The more loops you create and the more logic that's shared between them, the more likely you're going to fall into a whack-a-mole trap. This is where you'll see a problem in one skill, you'll fix it, and then it'll pop up in another place. If the logics were used across skills, you want to abstract that into a single skill that gets called by the other loops. And to all the programmers out there, yes, it's like you're creating a reusable function. Feature number two is the health check across the stack. You can cross-reference every loop's output to see what's running successfully. But for this to work, every loop has to log its results properly. So we'll create a write run log utility skill that writes everything to this folder. On screen you can see a prompt that will create the specific skill and simultaneously enhance any existing loops that you have. We do this so that every loop writes to the same location. And if you update this specific write log skill, it'll update across every other loop that you have running. And by having an effective way to monitor loops, you're going to keep a close eye on everything that's running, and you'll quickly notice what is and isn't working. And as a result, you'll be able to turn off what isn't working, saving you tokens. I can guarantee there are probably millions of people right now running loops that don't know it, and they're just burning tokens. This helps you avoid that. And the third feature is it dynamically updates, which removes operational debt. Every loop that we've created in this video has the same naming convention. It's name-loop. And on each run of this ecosystem monitoring loop, it scans the skills for any skill that has this name. And as a result, this ecosystem monitoring loop will automatically include any additional loops that you start running. This means that there's no operational debt to actually maintain this monitoring loop because it self-corrects. And remember, for every loop that I'm covering this video, if you want to run them continuously or on a schedule, you can run routines directly through Claude Desktop app. Now, the past seven loops that I covered are game-changers for productivity, but this last one could make the biggest difference. Loop number eight is your North Star loop. If the other seven loops are instruments, this loop is the compass. This loop will monitor your activity and make sure you're actually pushing towards your goals. Simply put, this is asking, is everything that I'm doing pointed at my actual goal? And there are four parts to this loop, and you can see the prompt on screen. Part one is you lock in the North Star. This is similar to the goal extraction we did earlier, but you have to establish like what are your actual goals? Hit 100k subs, land 12 new clients, ship four paid products, get a promotion, sign four new clients. Like what are these goals that you want to be pushing towards? Part two is it'll analyze your trajectory. This will read your Claude session history, the data you're ingesting, the loop results, everything that you've been working on, and see where you're going. Part three is it summarizes it. This is about forward extrapolation. Essentially saying, if nothing changes, here's where you're going to land. For me, this is usually the biggest kick in the ass because it's like, if I don't change anything, then I'm going to be here in six months. The fourth part is proposed direction changes. If drift is detected, it'll surface what's pulling you in that direction. It'll detect this drift and then propose things that you should change instead. This is the type of loop that frankly everybody needs to start using. So, those are the eight loops that you need to build bucketed into three different groups. Loops that help you ingest data, build faster, and create a system that compounds and can be maintained over time. Now, if you like this video, you'll love this video where I dive deep into how you can set up Claude to be a self-improving system. It builds on a lot of the topics I covered here. And if you pair what I cover in that video with the loops that I walked through today, you're going to be on a whole 'nother level. So, go check that video out, and I'll see you over there. Peace.

---

## Timestamped Segments

**[0:00]** Loop number one is a data ingestion

**[0:01]** loop. Before we cover how to create this

**[0:03]** loop and why it's so valuable, what is

**[0:04]** an actual Claude loop? A loop is

**[0:06]** something that runs continuously or on a

**[0:08]** specific schedule until a task is

**[0:10]** complete. And to see it in action, loop

**[0:11]** one is the data ingestion loop. With AI,

**[0:14]** at the end of the day, your data is your

**[0:15]** moat. And if you want to differentiate

**[0:17]** yourself and get a better output, you

**[0:18]** have to take data aggregation and

**[0:20]** ingestion very seriously. To set this

**[0:22]** up, we first connect our data sources.

**[0:24]** If you click the plus in the desktop app

**[0:26]** and then select connectors, you can then

**[0:27]** select the specific resources that you

**[0:29]** interact with. For me, it's Slack,

**[0:31]** Gmail, and then Granola for call

**[0:32]** transcripts. Once you establish those

**[0:34]** connections, it's time to actually

**[0:35]** create a skill that aggregates the data

**[0:37]** for you, validates that it's not just

**[0:39]** contextual noise, and then ingests it

**[0:41]** into the system. On screen, you can see

**[0:42]** a prompt that I used to create a skill

**[0:44]** called a data ingestion loop. This loop

**[0:46]** will go to Slack for messages, Gmail for

**[0:48]** emails, Granola for call transcripts,

**[0:50]** read the last 24 hours, and remove all

**[0:52]** of the fluff, and only store the

**[0:53]** valuable information. For every loop we

**[0:55]** create, I'm going through a process

**[0:57]** called skill-driven loop creation, where

**[0:58]** every loop we create starts as a skill

**[1:00]** first that we manually run, confirm it

**[1:03]** works, and then we create a process to

**[1:05]** automatically run it. At this point,

**[1:07]** let's assume that we've tested it, and

**[1:08]** it's now time to actually make this

**[1:10]** automated. To do this, I use local

**[1:12]** routines, which I get to by clicking

**[1:13]** routines, plus, local routine, and then

**[1:16]** I fill in the information where the

**[1:18]** instructions is I just use the skill

**[1:20]** that I already created. In this case, I

**[1:22]** set the skill to run Mondays at 8:00

**[1:24]** a.m. And for every loop we cover here,

**[1:25]** you can just create a routine if you

**[1:27]** want to run it automatically in the

**[1:28]** background. Now, that's just the first

**[1:29]** of eight Claude code loops that we'll go

**[1:31]** through in today's video that will help

**[1:32]** you build faster and more efficiently.

**[1:34]** And for all eight of these loops, I

**[1:35]** bucket them into three groups. The first

**[1:37]** is loops that help you ingest data, get

**[1:39]** better outputs. The next are loops that

**[1:41]** help you build faster, and the last is a

**[1:43]** series of loops that help you create a

**[1:45]** system that automatically improves over

**[1:47]** time. Loop number two is external alpha

**[1:50]** farming. So, what is an alpha farming

**[1:51]** loop? This is a loop that goes, looks

**[1:53]** for information that's valuable, and

**[1:55]** then pulls it into your system. And by

**[1:57]** sourcing the right information, you're

**[1:58]** able to get better outputs. Now, there

**[2:00]** are three parts of this loop, and so

**[2:01]** here's a prompt to create it, but I'm

**[2:03]** going to go through each step and why

**[2:04]** it's important. The first part of it is

**[2:06]** you want to establish what alpha you're

**[2:07]** actually farming. And for this, you want

**[2:09]** to be very specific. So, if you're a

**[2:10]** content creator, the alpha could be

**[2:12]** storytelling patterns or recent news

**[2:14]** topics. If you're building a product, it

**[2:15]** could be about conversion funnel

**[2:17]** benchmarks and optimization tactics. If

**[2:20]** you're a sales rep, it could be

**[2:21]** objection handling patterns from reps

**[2:23]** who are closing your exact customer. The

**[2:25]** second part of this is identify the

**[2:26]** sources of alpha. This is where you

**[2:28]** could use AI to help you create a list

**[2:30]** of options, but ultimately, this is

**[2:32]** where your human taste comes in. The

**[2:33]** question you have to ask yourself is who

**[2:35]** online is creating valuable insight

**[2:36]** about the topics that you're working on.

**[2:38]** So, YouTube creators, newsletter

**[2:39]** creators, Reddit forums, where is there

**[2:41]** valuable information online that can

**[2:43]** produce a consistent stream of

**[2:45]** up-to-date information? The third part

**[2:47]** is that you validate the source has

**[2:49]** level two analysis. Most people skip

**[2:51]** this part, but this is where it becomes

**[2:52]** an actual loop. So, level one analysis

**[2:55]** is where AI just gives you basic stuff,

**[2:56]** right? The basic framework, something

**[2:58]** that doesn't really differentiate the

**[2:59]** output. Level two analysis is the

**[3:01]** non-obvious information that brings an

**[3:03]** output from good to great. And you want

**[3:05]** to curate it so only level two

**[3:06]** information is ingested into your

**[3:08]** system. Here on screen, you can see me

**[3:10]** running the alpha farming loop, and you

**[3:12]** can see that it's actually going and

**[3:13]** fetching different resources. One thing

**[3:15]** I want to call out is that I do use an

**[3:16]** MCP called Firecall that helps me get

**[3:18]** better information across the internet.

**[3:20]** Now, before we get to the next loop,

**[3:21]** which will focus on internal alpha

**[3:23]** farming, you may find that a lot of what

**[3:24]** we're covering feels a bit technical,

**[3:26]** which brings us to today's video

**[3:27]** sponsor, nexus.ai. This is what I call

**[3:30]** an AI platform, which is a category of

**[3:31]** tools I love. And then the reason for

**[3:33]** this is that it removes all the

**[3:34]** technical skills that are normally

**[3:35]** needed to set up AI agent systems, and

**[3:38]** it can save you hundreds of dollars each

**[3:39]** month because you don't have to pay for

**[3:41]** five different AI tools. There are three

**[3:43]** specific features that I love. The first

**[3:45]** is that every flagship model is included

**[3:47]** in a single nexus login. So, ChatGPT,

**[3:49]** Claude, Gemini, Grok, 200 plus other

**[3:51]** models can all be accessed directly

**[3:53]** through Nexus. And this is critical

**[3:54]** because there's really no single best AI

**[3:56]** model. Different ones are better at

**[3:58]** different things, and Nexus AI will

**[4:00]** automatically route each prompt to the

**[4:02]** best one. The second feature is that

**[4:03]** there's zero data retention. This means

**[4:05]** that your data is never used to train

**[4:07]** their models, and that alone is one of

**[4:09]** the big reasons why I can even consider

**[4:11]** using this tool for client work. And the

**[4:13]** third feature is their no-code AI agent

**[4:15]** builder. At the end of the day, if you

**[4:16]** can use the internet, you can use Nexus

**[4:18]** to build AI agents. You just describe

**[4:20]** what you want, and Nexus will build the

**[4:21]** agent for you. And whether it's for

**[4:23]** one-time jobs like I need to do deep

**[4:24]** research on this topic like right now,

**[4:27]** or for repetitive tasks like turning

**[4:28]** your notes into a weekly report

**[4:30]** automatically, Nexus will handle all of

**[4:32]** this. For me, I have a lot of products

**[4:33]** in my ecosystem, my YouTube, my

**[4:34]** newsletter, Build Partner, so it's hard

**[4:36]** to keep track of all of this. So, what I

**[4:38]** can do is create a weekly report that

**[4:39]** analyzes my entire marketing funnel, and

**[4:41]** connect it to my Slack to send my entire

**[4:43]** team a summary of website visits,

**[4:45]** conversions, and what we need to work

**[4:46]** on. This is a task that I'd normally

**[4:48]** just never do because I just don't have

**[4:49]** the time. So, to check out Nexus, click

**[4:50]** the first link in the description you'll

**[4:52]** get 50% off. And that 50% discount is

**[4:54]** for a limited time because when I was

**[4:56]** working with them, I had to stress the

**[4:57]** importance of getting a large discount

**[4:59]** for everyone watching. So, go check that

**[5:01]** out. Now, getting to loop number three,

**[5:02]** which is internal alpha farming loop. If

**[5:04]** loop number two was all about hunting

**[5:06]** for external alpha farming, loop number

**[5:08]** three hunts for internal alpha. This

**[5:11]** will look across all the data that's

**[5:12]** already in your system, and surface

**[5:14]** what's recurring, where the gaps are,

**[5:16]** and what you should be doing about it.

**[5:17]** To set this up, it's broken down into

**[5:18]** three parts. The first part is you want

**[5:20]** to establish what internal alpha you're

**[5:22]** farming. If you're a content creator,

**[5:24]** which video concepts actually landed and

**[5:26]** performed? If you're building a product,

**[5:28]** what features do people keep requesting?

**[5:29]** If you're a sales rep, what questions or

**[5:31]** rebuttals does everyone have, and should

**[5:33]** you build that into the service? This is

**[5:35]** the exact kind of pattern that humans

**[5:36]** will miss, but a loop doesn't. And the

**[5:38]** insights from this can lead to changes

**[5:40]** that actually move the needle. The

**[5:42]** second part is that you want to point it

**[5:43]** at the right data sets. In loop number

**[5:45]** one, we set up data ingestion, so this

**[5:47]** builds on exactly this. But now, you

**[5:49]** actually have to ask, do I have the

**[5:50]** necessary data for internal alpha

**[5:53]** farming loop to actually work? And if

**[5:54]** the answer is no, this identifies gaps

**[5:57]** in your data pipeline, and you have to

**[5:58]** resolve that. And part three is the

**[6:00]** output is an action list, not a report.

**[6:03]** Essentially, every internal dashboard

**[6:04]** tells you all the information about what

**[6:06]** happened, but none of them actually tell

**[6:08]** you what to do about it. And one of the

**[6:10]** things that I tell my team is, don't

**[6:11]** bring me a problem, bring me a solution.

**[6:13]** And that's exactly what this loop is

**[6:15]** designed to do. It creates an

**[6:16]** implementation plan that passes our plan

**[6:18]** verification skill to make sure it hits

**[6:20]** our requirements for any sort of

**[6:22]** delivery plan. To create this loop,

**[6:24]** first we need to create that {slash}

**[6:25]** plan verification skill, which is a

**[6:27]** utility skill that we'll use whenever we

**[6:29]** want to verify a plan. Here's a prompt

**[6:31]** actually create that skill, which will

**[6:33]** interview you about what tools you're

**[6:34]** currently using and what you're open to

**[6:37]** and not open to implementing. The key

**[6:38]** here is that any implementation plan

**[6:40]** that this creates has to actually be a

**[6:42]** viable option. So, the skill is used to

**[6:44]** keep AI honest about any plan that it

**[6:46]** actually proposes. Then you use this

**[6:48]** prompt to create an internal alpha

**[6:50]** farming loop skill, which will create

**[6:52]** the loop, identify recurring patterns,

**[6:54]** and suggest places to improve. This loop

**[6:56]** will help you identify what you have to

**[6:57]** build next based on the data you're

**[6:59]** ingesting. As this loop runs, it'll look

**[7:01]** at the data that you're ingesting and

**[7:02]** suggest places for improvement. Now,

**[7:04]** we've covered ways to ingest data and

**[7:06]** how to actually analyze it, but the next

**[7:07]** three loops are all about improving the

**[7:09]** process in which you build. Loop number

**[7:11]** four is an optimization loop. This is a

**[7:13]** process of optimizing a system to

**[7:15]** approach a specific metric or

**[7:17]** quantifiable result. For example, it

**[7:19]** does something pass level two analysis,

**[7:21]** right? That's hard to actually quantify.

**[7:23]** But what a proper optimization loop does

**[7:25]** is it looks at something that is an

**[7:27]** objective metric. An example could be,

**[7:29]** how quickly does a website load? So,

**[7:31]** what this loop will do is it'll pick a

**[7:32]** specific goal, it'll run a loop, measure

**[7:35]** the result, if it doesn't actually fit

**[7:36]** the goal, it'll propose a solution,

**[7:38]** it'll apply it, re-measure it, and

**[7:41]** continue this loop until it gets to that

**[7:43]** final goal. On screen, you'll see a

**[7:45]** bunch of areas where an optimization

**[7:47]** loop makes sense, which is typically for

**[7:49]** more technical delivery mechanisms

**[7:50]** because these are super quantifiable.

**[7:52]** When I first started thinking about

**[7:53]** loops, I thought that all of the

**[7:54]** feedback back and forth had to happen

**[7:56]** almost instantly. Make a change, measure

**[7:58]** result, etc. But that doesn't

**[7:59]** necessarily have to be the case. So, for

**[8:01]** example, let's say you have a website

**[8:03]** and you want to try and optimize

**[8:04]** conversion rate. You could have a loop

**[8:06]** that runs, checks the conversion rate

**[8:07]** for day one, makes a tweak, checks it

**[8:10]** for day two, etc. And where this

**[8:12]** feedback loop is over a course of 24

**[8:14]** hours. This is entirely fine, and once I

**[8:16]** kind of realized this, this opened up my

**[8:18]** brain to the realm of possibilities

**[8:20]** because initially I thought that this

**[8:22]** feedback mechanism was way too slow.

**[8:24]** Now, to create an optimization loop,

**[8:25]** here is a templated prompt that you can

**[8:27]** use, and you can fill in for whatever

**[8:29]** you're trying to work on. Now, before I

**[8:30]** get to the next loop, if this is your

**[8:31]** first video of mine, welcome to channel,

**[8:33]** but if this is your second or more, here

**[8:35]** is our anti-slop agreement. All of the

**[8:37]** stuff that I do in this video, right?

**[8:39]** The the visual, the design, the hours of

**[8:41]** research, this is for humans, not for AI

**[8:44]** robots. That's part of the reason why I

**[8:45]** put all these prompts on screen because

**[8:47]** it's easier for you to read and

**[8:48]** screenshot, and it's not for these AI

**[8:50]** robots to see. So, as part of the

**[8:51]** agreement, all I ask is that you

**[8:53]** subscribe to this channel to help this

**[8:55]** content reach more people. Also, every

**[8:56]** video I give away a Claude Mac

**[8:58]** subscription, and this video's winner is

**[9:00]** the goat I'm Jasmine. They're building a

**[9:01]** platform to help people connect faster.

**[9:04]** Absolute bangers. To enter the giveaway,

**[9:05]** comment below with what you're building,

**[9:07]** and if you already entered, you can

**[9:08]** enter again by providing an update on

**[9:10]** whatever you're working on. Bring us to

**[9:11]** loop number five, which is code build

**[9:13]** loop. This loop is specifically if you

**[9:14]** want to vibe code a product, and

**[9:16]** everyone watching this video should be

**[9:18]** vibe coding whether you have a technical

**[9:19]** background or not. And the key with

**[9:20]** anything vibe coding is you don't want

**[9:21]** to just go and grip and rip things. You

**[9:24]** need to plan before you actually do

**[9:25]** anything. And what this loop will do is

**[9:27]** your goals will get extracted. It

**[9:28]** verifies a delivery plan, and then, and

**[9:31]** only then, does it go through a loop to

**[9:33]** complete the tasks. On screen, you can

**[9:35]** see the prompt, which breaks the task

**[9:36]** into six parts, which leverages skill

**[9:39]** chaining to create the actual loop.

**[9:41]** First, it'll extract or bring in the

**[9:42]** goal. So, this can be through an

**[9:43]** interview, or you can bring in a

**[9:44]** document you already have. The second is

**[9:46]** it'll plan the delivery using Claude's

**[9:48]** built-in plan mode. The third is sign

**[9:50]** off on the plan. This is where you, the

**[9:51]** human, comes in. The fourth is it'll

**[9:53]** build it. Fifth is it'll review the

**[9:55]** code. This uses Claude's

**[9:57]** /code-review--fix.

**[9:59]** Sixth, it'll verify the behavior matches

**[10:01]** the goal. It'll use Claude's /verify to

**[10:03]** help with this. Now, I went through all

**[10:05]** six features pretty quickly there, but

**[10:06]** there are two specific concepts that are

**[10:08]** critical you understand as you take

**[10:09]** these loops and start creating your own

**[10:11]** from scratch. The first is that there's

**[10:13]** an approval gate. If you look at the

**[10:14]** third step, it says sign off on the

**[10:15]** plan. That's an approval gate. And we do

**[10:17]** this at this stage because this is what

**[10:19]** I call a critical call checkpoint. If at

**[10:21]** this point you're in the wrong

**[10:22]** direction, steps four, five, and six are

**[10:24]** just going to be entirely wrong, and

**[10:26]** you're wasting time and money. A general

**[10:27]** rule of thumb I have is that for any

**[10:29]** loop that you create, if there is any

**[10:31]** critical call checkpoint, then you need

**[10:33]** to add a human approval gate. Now, to be

**[10:35]** clear, some of these loops may have none

**[10:36]** of these, but others may have four or

**[10:38]** five. It really depends on what you're

**[10:39]** building. The second thing is dynamic

**[10:41]** workflows. This is how Anthropic divides

**[10:43]** the goal you have amongst AI agents to

**[10:46]** complete the task. This is how it

**[10:47]** actually goes and builds whatever you're

**[10:49]** trying to build. And there are six

**[10:50]** patterns that Anthropic has documented

**[10:52]** for these dynamic workflows, which you

**[10:54]** can see all of them on screen. But to

**[10:56]** 80/20 this whole thing, you don't

**[10:58]** actually have to worry about which one.

**[10:59]** It'll figure it out for you. But if you

**[11:01]** do want to play around with it, you can

**[11:02]** look at the screenshot as a good

**[11:03]** starting point. Okay, so we've gone

**[11:05]** through data ingestion as well as how

**[11:06]** you can build quickly. But loop number

**[11:08]** six is about creating a system that

**[11:10]** self-improves with the improve system

**[11:12]** loop. Of the eight loops that we're

**[11:14]** covering, this is by far my favorite

**[11:15]** because it single-handedly transformed

**[11:17]** my business. Twice a week, I run an

**[11:19]** improve system loop, Tuesday end of day

**[11:21]** and Friday end of day, and that makes it

**[11:23]** so that my entire AI system is

**[11:24]** self-improving. There are two layers to

**[11:26]** actually get this done. The first layer

**[11:27]** is you have to build the improve system

**[11:29]** skill. This is what actually looks at

**[11:31]** your system and figures out ways to

**[11:33]** improve it. So, it'll read sessions,

**[11:35]** it'll find patterns, it'll propose

**[11:36]** changes, and I've spoken about this a

**[11:37]** lot on my channel, but if you want to

**[11:39]** use the exact one I use, I do have a

**[11:40]** plugin called billpartner.ai, and you

**[11:42]** can do /bp improve system, and that's

**[11:44]** exactly what I use. Here on my screen,

**[11:46]** you can see me running this skill

**[11:47]** manually on my system, and it shows all

**[11:49]** the ways that I can currently improve

**[11:50]** it. Now that I look at it, I will have

**[11:52]** to do after filming this video. Now, the

**[11:54]** second layer for this loop is to

**[11:55]** actually create the loop, and this is

**[11:56]** wrapping the skill in a self-improving

**[11:58]** system loop. But, within this prompt, I

**[12:00]** log every change that it makes to a

**[12:02]** changelog.md file. The reason is I want

**[12:04]** to see what is actually happening in my

**[12:06]** system, and within those changes, it

**[12:08]** actually buckets it into three

**[12:10]** categories. The first bucket is

**[12:12]** auto-approve. These are all of the

**[12:13]** low-risk things that it can just

**[12:15]** automatically improve, aren't really up

**[12:16]** for debate to improve the system. This

**[12:18]** is like the self-improving component.

**[12:20]** Bucket two is need sign-off. These are

**[12:22]** higher-stakes stuff, like skill edits,

**[12:24]** or new skill candidates, or structural

**[12:25]** changes. This is anything where the

**[12:27]** wrong choice could actually degrade

**[12:28]** output quality. These changes get

**[12:30]** written to a review file as a checkbox

**[12:32]** list. For each of the suggestions, you

**[12:34]** can improve, reject, or approve and

**[12:36]** don't ask me again. This is a way to

**[12:38]** tweak the system over time. And the

**[12:39]** third bucket is more context needed.

**[12:41]** This is stuff that the loop can't decide

**[12:43]** on its own. Let's say, for example, you

**[12:45]** mention someone three times, and it

**[12:46]** can't tell if this is a new client or a

**[12:48]** one-off relationship. This will go in

**[12:49]** that same review file from bucket two.

**[12:51]** This three-bucket system is what I found

**[12:53]** is an effective middle ground to make an

**[12:54]** automated system that improves without

**[12:56]** you, makes it easy for you to label

**[12:57]** improvements, and also keeps you as the

**[13:00]** tastemaker, so that your system doesn't

**[13:01]** slowly degrade in quality from what you

**[13:03]** actually want it to produce. Loop number

**[13:05]** seven is ecosystem monitoring loop.

**[13:08]** Whenever you create a loop, more

**[13:09]** operational debt is added to your

**[13:10]** system, and this ecosystem monitoring

**[13:12]** loop is the loop that manages your other

**[13:14]** loops. This is some loop-ception type sh

**[13:17]** Now, before you say this is ridiculous,

**[13:19]** we're just going to be burning through

**[13:20]** tokens, there's some key features why

**[13:22]** this can actually save you tokens while

**[13:24]** running a more efficient system. On

**[13:26]** screen, you'll see a prompt to create

**[13:27]** the actual loop, but there are three

**[13:28]** important features to call out. The

**[13:30]** first feature is it surfaces

**[13:32]** composability opportunities across

**[13:34]** loops. As you build more loops, you'll

**[13:36]** unknowingly write the same logic twice.

**[13:38]** For example, let's say you have two

**[13:39]** loops that require fetching data from

**[13:41]** Slack. There's a chance that both of

**[13:42]** these contain the same logic. The so the

**[13:44]** ecosystem monitoring loop scans your

**[13:46]** loop library, finds repeated logic, and

**[13:48]** suggests pulling it out into a

**[13:50]** composable skill that every loop can

**[13:52]** call. That's exactly what we did with

**[13:53]** the plan verification skill back in loop

**[13:55]** number three. We built it once and then

**[13:57]** any other loop can use it. The more

**[13:59]** loops you create and the more logic

**[14:01]** that's shared between them, the more

**[14:02]** likely you're going to fall into a

**[14:03]** whack-a-mole trap. This is where you'll

**[14:05]** see a problem in one skill, you'll fix

**[14:07]** it, and then it'll pop up in another

**[14:08]** place. If the logics were used across

**[14:10]** skills, you want to abstract that into a

**[14:12]** single skill that gets called by the

**[14:14]** other loops. And to all the programmers

**[14:16]** out there, yes, it's like you're

**[14:17]** creating a reusable function. Feature

**[14:19]** number two is the health check across

**[14:21]** the stack. You can cross-reference every

**[14:23]** loop's output to see what's running

**[14:24]** successfully. But for this to work,

**[14:26]** every loop has to log its results

**[14:27]** properly. So we'll create a write run

**[14:29]** log utility skill that writes everything

**[14:32]** to this folder. On screen you can see a

**[14:33]** prompt that will create the specific

**[14:35]** skill and simultaneously enhance any

**[14:37]** existing loops that you have. We do this

**[14:39]** so that every loop writes to the same

**[14:40]** location. And if you update this

**[14:42]** specific write log skill, it'll update

**[14:44]** across every other loop that you have

**[14:46]** running. And by having an effective way

**[14:47]** to monitor loops, you're going to keep a

**[14:49]** close eye on everything that's running,

**[14:51]** and you'll quickly notice what is and

**[14:53]** isn't working. And as a result, you'll

**[14:54]** be able to turn off what isn't working,

**[14:56]** saving you tokens. I can guarantee there

**[14:58]** are probably millions of people right

**[14:59]** now running loops that don't know it,

**[15:01]** and they're just burning tokens. This

**[15:03]** helps you avoid that. And the third

**[15:04]** feature is it dynamically updates, which

**[15:06]** removes operational debt. Every loop

**[15:08]** that we've created in this video has the

**[15:10]** same naming convention. It's name-loop.

**[15:12]** And on each run of this ecosystem

**[15:14]** monitoring loop, it scans the skills for

**[15:17]** any skill that has this name. And as a

**[15:19]** result, this ecosystem monitoring loop

**[15:21]** will automatically include any

**[15:23]** additional loops that you start running.

**[15:24]** This means that there's no operational

**[15:26]** debt to actually maintain this

**[15:27]** monitoring loop because it

**[15:29]** self-corrects. And remember, for every

**[15:31]** loop that I'm covering this video, if

**[15:32]** you want to run them continuously or on

**[15:34]** a schedule, you can run routines

**[15:35]** directly through Claude Desktop app.

**[15:37]** Now, the past seven loops that I covered

**[15:38]** are game-changers for productivity, but

**[15:40]** this last one could make the biggest

**[15:41]** difference. Loop number eight is your

**[15:43]** North Star loop. If the other seven

**[15:45]** loops are instruments, this loop is the

**[15:47]** compass. This loop will monitor your

**[15:49]** activity and make sure you're actually

**[15:50]** pushing towards your goals. Simply put,

**[15:52]** this is asking, is everything that I'm

**[15:54]** doing pointed at my actual goal? And

**[15:55]** there are four parts to this loop, and

**[15:57]** you can see the prompt on screen. Part

**[15:58]** one is you lock in the North Star. This

**[16:00]** is similar to the goal extraction we did

**[16:02]** earlier, but you have to establish like

**[16:03]** what are your actual goals? Hit 100k

**[16:05]** subs, land 12 new clients, ship four

**[16:07]** paid products, get a promotion, sign

**[16:09]** four new clients. Like what are these

**[16:11]** goals that you want to be pushing

**[16:12]** towards? Part two is it'll analyze your

**[16:14]** trajectory. This will read your Claude

**[16:15]** session history, the data you're

**[16:17]** ingesting, the loop results, everything

**[16:19]** that you've been working on, and see

**[16:20]** where you're going. Part three is it

**[16:22]** summarizes it. This is about forward

**[16:24]** extrapolation. Essentially saying, if

**[16:25]** nothing changes, here's where you're

**[16:26]** going to land. For me, this is usually

**[16:29]** the biggest kick in the ass because it's

**[16:30]** like, if I don't change anything, then

**[16:32]** I'm going to be here in six months. The

**[16:34]** fourth part is proposed direction

**[16:35]** changes. If drift is detected, it'll

**[16:37]** surface what's pulling you in that

**[16:39]** direction. It'll detect this drift and

**[16:41]** then propose things that you should

**[16:42]** change instead. This is the type of loop

**[16:44]** that frankly everybody needs to start

**[16:45]** using. So, those are the eight loops

**[16:47]** that you need to build bucketed into

**[16:48]** three different groups. Loops that help

**[16:50]** you ingest data, build faster, and

**[16:52]** create a system that compounds and can

**[16:54]** be maintained over time. Now, if you

**[16:55]** like this video, you'll love this video

**[16:57]** where I dive deep into how you can set

**[16:58]** up Claude to be a self-improving system.

**[17:01]** It builds on a lot of the topics I

**[17:02]** covered here. And if you pair what I

**[17:03]** cover in that video with the loops that

**[17:05]** I walked through today, you're going to

**[17:06]** be on a whole 'nother level. So, go

**[17:08]** check that video out, and I'll see you

**[17:09]** over there. Peace.
