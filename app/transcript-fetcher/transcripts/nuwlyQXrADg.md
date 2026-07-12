# Transcript: Do THIS Before You Lose Access to Fable 5

**URL:** https://www.youtube.com/watch?v=nuwlyQXrADg
**Segments:** 422
**Channel:** Mark Kashef
**Duration:** 13:58
**Uploaded:** 2026-07-05

---

## Full Text

So, if you're paying for Claude right now, you have a couple days left to use Fable 5 as a part of your existing subscription, at least for now. And after that, the majority of us will be using Fable, or at least won't be using it as much, because the costs are eye-watering. They're either panicking and throwing hundreds of thousands of tokens at random tasks before the clock runs out, or they're just shrugging and barely using it to begin with. But, the goal of this video is I want to give you a third move. One that takes the single most valuable thing that I find about Fable 5 and allows you to use it well after it's out of your subscription. Now, before we initially lost Fable, I dropped a video walking through how you could go through your prior conversations to pull out its raw intelligence. But, while you still have it, we can use it in a way that pretty much nobody's talking about. And no, it's not just building every single idea you have, and it's also not building simple plan files. It's building something that's infinitely more potent and gives pretty much any model the ability to go through what Fable would have done and executed itself. So, if you want to spend the last tokens and time that you have left with model, at least for now, in the best way possible, then let's dive in. Now, if you read Anthropic's official release notes, they say that Fable is an amazing executor for long-range tasks, and you should give it a plan created by something like Opus. You shouldn't, apparently, use Fable for planning, because it's a waste of those valuable tokens. And if we're speaking purely about planning, then this advice makes sense. It's the equivalent of bringing a top-rated surgeon and asking them to write you a diagram of how you would operate on someone versus actually having them do it. So, the fix isn't asking for better plans. It's actually not asking for plans at all. A few days ago, one of the top engineers at Anthropic dropped a whole article walking through how you should use models like Fable to help you understand the unknowns of a certain project. And the big idea is that with a model this capable, you're no longer held back by raw intelligence. You're held back by the things that you don't know as the orchestrator, as the person providing the instructions, the plans, and the prompts to these kinds of models. Now, for most of us, when we start a project, we have a pretty good grasp of the known knowns and the known unknowns. But, typically, you might want to lean on the intelligence of models like Fable for things like the unknown knowns. And this could be the tacit knowledge that you assume that the language model knows, but even with that level of intelligence, might not have your level of life experience or tacit knowledge. And then you have the unknown unknowns, where you don't even know that this was an area worth exploring or asking about. So, you can implore and elicit models like Fable in the time that you have to pull these questions out and guide you in areas where you would have never thought to go before. Now, this concept is the crux of the video, and I'm not just going to walk you through it conceptually. I'm going to show you hands-on how you can implement it. Instead of creating a normal plan, where even with a model as smart as Fable, will assume linearity, a blue-sky scenario. It will break down a plan into phases, and it will create it in a way that's very logical. It's very expected that it would have a high degree of success. But, in reality, it doesn't really demonstrate what could happen if things don't go as planned. The whole point of war-gaming is that you have the AI break down every course of action move by move and every possible scenario that it could encounter based on its prior experience. So, you can think of it as three main elements. You have action, reaction, and counteraction. So, the AI makes a move, and then reality humbles it by throwing some form of error, and then it has to take some form of counteraction to try to resolve this error. And this is what we call the modern-day agentic loop. So, to make it more tangible, let's say you built an entire platform, and you wanted to use Fable to build out this new functionality that would allow users to hit an API endpoint and retrieve some form of data. A normal plan would just break down exactly how it could build this endpoint. But, a war-game would basically say, "Use this plan, but assume that at every juncture, there's going to be a couple different possible scenarios. Based on your experience, how would you handle those scenarios? If you have all of this documented, then if you give this same plan to something like an Opus 4.8 or a GPT 5.5 or maybe even a very sophisticated open-source model like GLM, then most likely it would have a much easier time to combine its harness with understanding all the possible realities that have already been simulated by Fable and execute them much more confidently. Now, as with any simulation, you need to define an end. So, I like to call this a second, third, fourth order consequence. And these are the possible things that could happen a few layers down from the initial action. So, it's not just building the website, it is thinking about all the different issues with building a website in this way. Maybe two or three different scenarios that could pop up. And this is the part where you come in and you decide how far to war-game a certain scenario. So, on the left here is what most people will have on July 8th where they temporarily lose access to Fable, which are a series of plans that kind of executed these builds kind of 80% of the way there, and then they have to go back to something like Opus 4.8 or another language model to finish executing the 20%, which ironically is typically one of the hardest things to do. However, what you could have are a series of projects and your hardest ideas fully simulated and war-gamed to the point where you can run them at your disposal and at your leisure. So, that's the conceptual, and now we'll get into the hands-on application. All right, so let's say we have 10 very meaty ideas and projects that we wish we had all the bandwidth and the tokens in the world to have Fable build out end-to-end. I'm not going to go through each one of the prompts comprehensively. I'll make all of them available to you in the second link down below, but we'll go through the very first one more in detail. Now, the prompt starts off as follows. It says, "War-game order. You are not executing this mission, you are purely war-gaming it." And a language model will know the difference between a plan and a war-game. We can also tell it a cheaper executor model will run the brief below. And this might be helpful because you could basically tell it, this will be executed by Opus, so feel free to look at all of the Anthropic documentation on Opus to tailor this prompt and this wargame in a way where it will work well with that model. And this is the core template that's the same between all the prompts. Then fight the mission on paper move by move and write it to wargames/website.markdown file. Now, the key here is I don't want you to implement all of these separately. You can prepare all of your wargame files, you basically your prompts, and have Claude fable execute all of them at once, and then we can loop to re-review and re-edit and optimize all of them. Now, one nuance here is that I'm showing you each one of these one prompt at a time, but ideally you'll do what I will show you shortly where I ran all of these ideas at the same time in bulk. Now, continuing on with the prompt, every move states its expected observation, exactly what you should see if it worked, and then conversely, what it should see if it didn't work. So, every move carries its most likely failure, the cause of its signals, and the countermove. So, it's basically assuming what could happen, pessimistic scenario and optimistic scenario. Where different models like Opus 4.8 and others fail is they're very short-sided. They look at maybe a handful of different issues. And then you'd have to bring in something like Codex to look over its shoulder to make sure it's doing the right thing and making the right assumptions. And then very similar to going through a maze, every fork gets a trigger, and if you observe X, then you should say you should take this route if this happens versus that. Then we say assumptions that your reconnaissance or due diligence could not resolve, basically flag it to us. And then we end it off by saying end with abort conditions, so at what point should the plan stop executing? If it hits a certain type of error. Let's say it has no access to some type of system, that would be a full blocker for the plan actually executing. And then below this mission brief, you outline exactly what you're trying to do. So, in this case, for the website marketing use case, we just say I'm rebuilding the marketing site for name of business, because the current one some form of problem, visitors are your ICP, your audience, and then what I want is call to action. Build a complete static website in whatever framework you want, and then these are the sections I want. Here's the URL description. I want to make it mobile first, and when you believe you are done, verify before reporting, open each page, exercise every link, etc. So, you're basically saying, what are the different testing paths that you want this wargame/plan to be aware of? And like I said, every other prompt would look very similar, where you'd have the same template at the top, you'd outline the mission briefs down below. So, for this case for writing copy, you just have to fill in the blanks for something like who you're writing the copy for, what is the ICP, what is the mental state of the person reading this copy, and then walk through the brand voice, and then you would tell it we want to draft out every section, the headline, etc. Now, here's a use case that you might have not considered. What if you use Fable 5 to help you plan out building your entire local AI setup, because it's very obvious in the not-so-distant future, we're going to be offloading more tasks to open-source and very cheap models versus dealing with all this Fable's here, Fable not drama. So, your prompt could look something like this. I want a fully local, open-source AI setup on this machine, private by default, nothing leaves the box. And then you could have AI go through your system and look for all of these different elements, like your operating system, what kind of chip you're using, your RAM, whether you have GPU, your free disk, and then you would say set up the stack that fits this machine, not a generic tutorial, pick the runtime, go through everything. You could even point it at something like LM Studio and have it go and figure out every single model that would be the best for your specific system and how many tokens per second you could get. And beyond that, when it comes to things like tax, you could have it take a look at all of your tax optimizations you've already made in your business or in the business of the company you already work for and see from an accountant's perspective what are all the different ways that you could look for optimizations. You could do the same thing for running offers. You could also, if you have an existing chatbot application or platform, we have all kinds for my community, then how can you optimize them and implement them in a way where there's some self-teaching over all the mistakes that have happened in the past. And you can apply this to all kinds of use cases across the board including bug fixing, financial models, looking at different competitor models, seeing how you can optimize your usage of them, how you can run an advisor council where you can mix and match your usage of Claude, Codex, and open source models as well. Now, naturally you have an unlimited number of use cases, but once you have your laundry list of the most pressing projects and ideas that you want to execute, then you want to move on to this next step. So, once you're ready, you could create a brand new folder. In this folder, you could call it Fables last week, obviously for now. And then within that folder, you could break it down into some sub folders, tasks, war games, a success file, and a ledger file. The success file will have your criteria that we kind of mentioned in passing in the prompt above as to what you deem as a successful war game. So, if we go to the success.md file, this is what it could look like. Yours could have more rules, less rules, more stringent rules, or even more detailed rules. And then the ledger, the whole point of it is pointing out anywhere where it's blocked. So, if it's war gaming and there's some form of variable that's undefined, it should populate a little parentheses variable placeholder for something that it needs your input on. And then last but not least, you would execute this prompt that I already ran before running this video, which is /goal. Every mission file in /tasks has a first draft war game. Go through each one, loop through, and do the recon mission for each mission, write a war games file, and then draft all 10 before polishing any. And then once we take all those drafts, you could do something like theoretically run {slash} loop every 20 minutes, loop through every first draft until you really push it to its limits. And once you start running it, it will fan out a series of parallel agents to go and execute each one of those tasks at the same time, so that a million tokens later, you could have a war games folder that's fully populated. And you can even have an assumptions file. Within here, we'll have a full markdown file breaking down every single part of the assumed inputs, the recon needed, the different routes that it could take, the different moves and considerations it could take through this process. You can see right here, very comprehensive. Every possible move it could take and the possible action, reaction, and counteraction that will be required. So theoretically, you have 10 different blueprints that you could feed to any AI to execute said projects. And like I said, if the ledger is blocked for whatever reason, it would look something like this, where it would tell you inputs needed to unblock are, let's say, what kind of business this is for, the problem we're solving, the audience, everything that you could not specify. In my case, since I'm just walking you through this as a demo, I asked it to assume different values for those variables. And like I said, you could take this to the next level by tagging a Claude Code Guide agent and then say, "I want you to tailor this war game to exactly how Sonnet 5 would execute it." Very tailored to its specific behavior. And then this would go spin up a sub agent or sub agents to go through all the documentation, maybe the system card of that model, to make sure that it is geared and tailored as much as possible. And that's pretty much it. It is not rocket science, but it's really taking the paradigm of planning and taking it to its natural extreme, where you can take all the benefit and the raw intelligence of Fable to pull out how it would do something and just emulate that with existing models that are way cheaper and hopefully won't just disappear in the snap of a finger. And like I said, I'm going to make available to you all the prompts that I showed you down below along with this folder structure, so you can emulate it if you so choose. And as always, if you want to take things to the next level in general with things like Cloud Code and Codex and agentic workflows in general, make sure to check out the first thing down below. I drop all kinds of nuggets that you'll never see on YouTube in my early adopters community. And for the rest of you, if you found this helpful and novel, I'd super appreciate a like on the video. Helps the video helps to reach and the channel, and I'll see you all in the next one.

---

## Timestamped Segments

**[0:00]** So, if you're paying for Claude right

**[0:01]** now, you have a couple days left to use

**[0:03]** Fable 5 as a part of your existing

**[0:05]** subscription, at least for now. And

**[0:07]** after that, the majority of us will be

**[0:09]** using Fable, or at least won't be using

**[0:10]** it as much, because the costs are

**[0:12]** eye-watering. They're either panicking

**[0:14]** and throwing hundreds of thousands of

**[0:15]** tokens at random tasks before the clock

**[0:18]** runs out, or they're just shrugging and

**[0:20]** barely using it to begin with. But, the

**[0:22]** goal of this video is I want to give you

**[0:23]** a third move. One that takes the single

**[0:25]** most valuable thing that I find about

**[0:27]** Fable 5 and allows you to use it well

**[0:30]** after it's out of your subscription.

**[0:31]** Now, before we initially lost Fable, I

**[0:33]** dropped a video walking through how you

**[0:35]** could go through your prior

**[0:36]** conversations to pull out its raw

**[0:38]** intelligence. But, while you still have

**[0:40]** it, we can use it in a way that pretty

**[0:41]** much nobody's talking about. And no,

**[0:43]** it's not just building every single idea

**[0:45]** you have, and it's also not building

**[0:47]** simple plan files. It's building

**[0:49]** something that's infinitely more potent

**[0:51]** and gives pretty much any model the

**[0:52]** ability to go through what Fable would

**[0:55]** have done and executed itself. So, if

**[0:57]** you want to spend the last tokens and

**[0:59]** time that you have left with model, at

**[1:01]** least for now, in the best way possible,

**[1:03]** then let's dive in. Now, if you read

**[1:04]** Anthropic's official release notes, they

**[1:07]** say that Fable is an amazing executor

**[1:09]** for long-range tasks, and you should

**[1:11]** give it a plan created by something like

**[1:13]** Opus. You shouldn't, apparently, use

**[1:15]** Fable for planning, because it's a waste

**[1:17]** of those valuable tokens. And if we're

**[1:19]** speaking purely about planning, then

**[1:20]** this advice makes sense. It's the

**[1:22]** equivalent of bringing a top-rated

**[1:24]** surgeon and asking them to write you a

**[1:26]** diagram of how you would operate on

**[1:28]** someone versus actually having them do

**[1:30]** it. So, the fix isn't asking for better

**[1:33]** plans. It's actually not asking for

**[1:35]** plans at all. A few days ago, one of the

**[1:37]** top engineers at Anthropic dropped a

**[1:39]** whole article walking through how you

**[1:41]** should use models like Fable to help you

**[1:44]** understand the unknowns of a certain

**[1:45]** project. And the big idea is that with a

**[1:47]** model this capable, you're no longer

**[1:49]** held back by raw intelligence. You're

**[1:51]** held back by the things that you don't

**[1:53]** know as the orchestrator, as the person

**[1:55]** providing the instructions, the plans,

**[1:57]** and the prompts to these kinds of

**[1:59]** models. Now, for most of us, when we

**[2:00]** start a project, we have a pretty good

**[2:02]** grasp of the known knowns and the known

**[2:04]** unknowns. But, typically, you might want

**[2:07]** to lean on the intelligence of models

**[2:09]** like Fable for things like the unknown

**[2:11]** knowns. And this could be the tacit

**[2:13]** knowledge that you assume that the

**[2:15]** language model knows, but even with that

**[2:17]** level of intelligence, might not have

**[2:19]** your level of life experience or tacit

**[2:21]** knowledge. And then you have the unknown

**[2:23]** unknowns, where you don't even know that

**[2:25]** this was an area worth exploring or

**[2:27]** asking about. So, you can implore and

**[2:29]** elicit models like Fable in the time

**[2:31]** that you have to pull these questions

**[2:33]** out and guide you in areas where you

**[2:35]** would have never thought to go before.

**[2:36]** Now, this concept is the crux of the

**[2:38]** video, and I'm not just going to walk

**[2:40]** you through it conceptually. I'm going

**[2:42]** to show you hands-on how you can

**[2:43]** implement it. Instead of creating a

**[2:45]** normal plan, where even with a model as

**[2:47]** smart as Fable, will assume linearity, a

**[2:50]** blue-sky scenario. It will break down a

**[2:52]** plan into phases, and it will create it

**[2:54]** in a way that's very logical. It's very

**[2:56]** expected that it would have a high

**[2:58]** degree of success. But, in reality, it

**[3:00]** doesn't really demonstrate what could

**[3:02]** happen if things don't go as planned.

**[3:05]** The whole point of war-gaming is that

**[3:06]** you have the AI break down every course

**[3:09]** of action move by move and every

**[3:11]** possible scenario that it could

**[3:12]** encounter based on its prior experience.

**[3:15]** So, you can think of it as three main

**[3:16]** elements. You have action, reaction, and

**[3:19]** counteraction. So, the AI makes a move,

**[3:22]** and then reality humbles it by throwing

**[3:23]** some form of error, and then it has to

**[3:25]** take some form of counteraction to try

**[3:27]** to resolve this error. And this is what

**[3:29]** we call the modern-day agentic loop. So,

**[3:31]** to make it more tangible, let's say you

**[3:33]** built an entire platform, and you wanted

**[3:35]** to use Fable to build out this new

**[3:36]** functionality that would allow users to

**[3:38]** hit an API endpoint and retrieve some

**[3:41]** form of data. A normal plan would just

**[3:42]** break down exactly how it could build

**[3:45]** this endpoint. But, a war-game would

**[3:47]** basically say, "Use this plan, but

**[3:49]** assume that at every juncture, there's

**[3:51]** going to be a couple different possible

**[3:52]** scenarios. Based on your experience, how

**[3:55]** would you handle those scenarios? If you

**[3:57]** have all of this documented, then if you

**[3:59]** give this same plan to something like an

**[4:01]** Opus 4.8 or a GPT 5.5 or maybe even a

**[4:05]** very sophisticated open-source model

**[4:07]** like GLM, then most likely it would have

**[4:10]** a much easier time to combine its

**[4:12]** harness with understanding all the

**[4:14]** possible realities that have already

**[4:15]** been simulated by Fable and execute them

**[4:18]** much more confidently. Now, as with any

**[4:20]** simulation, you need to define an end.

**[4:22]** So, I like to call this a second, third,

**[4:24]** fourth order consequence. And these are

**[4:26]** the possible things that could happen a

**[4:29]** few layers down from the initial action.

**[4:31]** So, it's not just building the website,

**[4:33]** it is thinking about all the different

**[4:35]** issues with building a website in this

**[4:37]** way. Maybe two or three different

**[4:38]** scenarios that could pop up. And this is

**[4:40]** the part where you come in and you

**[4:41]** decide how far to war-game a certain

**[4:44]** scenario. So, on the left here is what

**[4:46]** most people will have on July 8th where

**[4:48]** they temporarily lose access to Fable,

**[4:50]** which are a series of plans that kind of

**[4:52]** executed these builds kind of 80% of the

**[4:55]** way there, and then they have to go back

**[4:57]** to something like Opus 4.8 or another

**[4:59]** language model to finish executing the

**[5:01]** 20%, which ironically is typically one

**[5:03]** of the hardest things to do. However,

**[5:05]** what you could have are a series of

**[5:06]** projects and your hardest ideas fully

**[5:08]** simulated and war-gamed to the point

**[5:10]** where you can run them at your disposal

**[5:12]** and at your leisure. So, that's the

**[5:13]** conceptual, and now we'll get into the

**[5:15]** hands-on application. All right, so

**[5:17]** let's say we have 10 very meaty ideas

**[5:20]** and projects that we wish we had all the

**[5:21]** bandwidth and the tokens in the world to

**[5:23]** have Fable build out end-to-end. I'm not

**[5:25]** going to go through each one of the

**[5:26]** prompts comprehensively. I'll make all

**[5:28]** of them available to you in the second

**[5:30]** link down below, but we'll go through

**[5:31]** the very first one more in detail. Now,

**[5:33]** the prompt starts off as follows. It

**[5:35]** says, "War-game order. You are not

**[5:37]** executing this mission, you are purely

**[5:39]** war-gaming it." And a language model

**[5:41]** will know the difference between a plan

**[5:43]** and a war-game. We can also tell it a

**[5:45]** cheaper executor model will run the

**[5:48]** brief below. And this might be helpful

**[5:50]** because you could basically tell it,

**[5:51]** this will be executed by Opus, so feel

**[5:53]** free to look at all of the Anthropic

**[5:55]** documentation on Opus to tailor this

**[5:58]** prompt and this wargame in a way where

**[6:00]** it will work well with that model. And

**[6:02]** this is the core template that's the

**[6:03]** same between all the prompts. Then fight

**[6:05]** the mission on paper move by move and

**[6:08]** write it to wargames/website.markdown

**[6:11]** file. Now, the key here is I don't want

**[6:13]** you to implement all of these

**[6:15]** separately. You can prepare all of your

**[6:17]** wargame files, you basically your

**[6:18]** prompts, and have Claude fable execute

**[6:22]** all of them at once, and then we can

**[6:23]** loop to re-review and re-edit and

**[6:26]** optimize all of them. Now, one nuance

**[6:28]** here is that I'm showing you each one of

**[6:29]** these one prompt at a time, but ideally

**[6:32]** you'll do what I will show you shortly

**[6:33]** where I ran all of these ideas at the

**[6:36]** same time in bulk. Now, continuing on

**[6:38]** with the prompt, every move states its

**[6:40]** expected observation, exactly what you

**[6:42]** should see if it worked, and then

**[6:44]** conversely, what it should see if it

**[6:46]** didn't work. So, every move carries its

**[6:48]** most likely failure, the cause of its

**[6:50]** signals, and the countermove. So, it's

**[6:51]** basically assuming what could happen,

**[6:54]** pessimistic scenario and optimistic

**[6:56]** scenario. Where different models like

**[6:58]** Opus 4.8 and others fail is they're very

**[7:01]** short-sided. They look at maybe a

**[7:02]** handful of different issues. And then

**[7:04]** you'd have to bring in something like

**[7:05]** Codex to look over its shoulder to make

**[7:07]** sure it's doing the right thing and

**[7:09]** making the right assumptions. And then

**[7:10]** very similar to going through a maze,

**[7:12]** every fork gets a trigger, and if you

**[7:13]** observe X, then you should say you

**[7:15]** should take this route if this happens

**[7:17]** versus that. Then we say assumptions

**[7:19]** that your reconnaissance or due

**[7:20]** diligence could not resolve, basically

**[7:23]** flag it to us. And then we end it off by

**[7:24]** saying end with abort conditions, so at

**[7:27]** what point should the plan stop

**[7:29]** executing? If it hits a certain type of

**[7:31]** error. Let's say it has no access to

**[7:34]** some type of system, that would be a

**[7:35]** full blocker for the plan actually

**[7:37]** executing. And then below this mission

**[7:39]** brief, you outline exactly what you're

**[7:41]** trying to do. So, in this case, for the

**[7:42]** website marketing use case, we just say

**[7:45]** I'm rebuilding the marketing site for

**[7:47]** name of business, because the current

**[7:48]** one some form of problem, visitors are

**[7:51]** your ICP, your audience, and then what I

**[7:54]** want is call to action. Build a complete

**[7:56]** static website in whatever framework you

**[7:59]** want, and then these are the sections I

**[8:00]** want. Here's the URL description. I want

**[8:03]** to make it mobile first, and when you

**[8:05]** believe you are done, verify before

**[8:06]** reporting, open each page, exercise

**[8:09]** every link, etc. So, you're basically

**[8:10]** saying, what are the different testing

**[8:12]** paths that you want this wargame/plan to

**[8:15]** be aware of? And like I said, every

**[8:17]** other prompt would look very similar,

**[8:18]** where you'd have the same template at

**[8:20]** the top, you'd outline the mission

**[8:22]** briefs down below. So, for this case for

**[8:24]** writing copy, you just have to fill in

**[8:26]** the blanks for something like who you're

**[8:27]** writing the copy for, what is the ICP,

**[8:30]** what is the mental state of the person

**[8:32]** reading this copy, and then walk through

**[8:35]** the brand voice, and then you would tell

**[8:36]** it we want to draft out every section,

**[8:38]** the headline, etc. Now, here's a use

**[8:40]** case that you might have not considered.

**[8:42]** What if you use Fable 5 to help you plan

**[8:45]** out building your entire local AI setup,

**[8:47]** because it's very obvious in the

**[8:49]** not-so-distant future, we're going to be

**[8:51]** offloading more tasks to open-source and

**[8:53]** very cheap models versus dealing with

**[8:56]** all this Fable's here, Fable not drama.

**[8:58]** So, your prompt could look something

**[9:00]** like this. I want a fully local,

**[9:02]** open-source AI setup on this machine,

**[9:04]** private by default, nothing leaves the

**[9:06]** box. And then you could have AI go

**[9:08]** through your system and look for all of

**[9:10]** these different elements, like your

**[9:11]** operating system, what kind of chip

**[9:13]** you're using, your RAM, whether you have

**[9:15]** GPU, your free disk, and then you would

**[9:17]** say set up the stack that fits this

**[9:19]** machine, not a generic tutorial, pick

**[9:22]** the runtime, go through everything. You

**[9:24]** could even point it at something like LM

**[9:25]** Studio and have it go and figure out

**[9:28]** every single model that would be the

**[9:29]** best for your specific system and how

**[9:32]** many tokens per second you could get.

**[9:33]** And beyond that, when it comes to things

**[9:35]** like tax, you could have it take a look

**[9:37]** at all of your tax optimizations you've

**[9:39]** already made in your business or in the

**[9:41]** business of the company you already work

**[9:42]** for and see from an accountant's

**[9:44]** perspective what are all the different

**[9:46]** ways that you could look for

**[9:47]** optimizations.

**[9:49]** You could do the same thing for running

**[9:50]** offers. You could also, if you have an

**[9:52]** existing chatbot application or

**[9:54]** platform, we have all kinds for my

**[9:56]** community, then how can you optimize

**[9:58]** them and implement them in a way where

**[10:00]** there's some self-teaching over all the

**[10:02]** mistakes that have happened in the past.

**[10:04]** And you can apply this to all kinds of

**[10:06]** use cases across the board including bug

**[10:08]** fixing, financial models, looking at

**[10:10]** different competitor models, seeing how

**[10:12]** you can optimize your usage of them, how

**[10:14]** you can run an advisor council where you

**[10:16]** can mix and match your usage of Claude,

**[10:18]** Codex, and open source models as well.

**[10:20]** Now, naturally you have an unlimited

**[10:22]** number of use cases, but once you have

**[10:24]** your laundry list of the most pressing

**[10:26]** projects and ideas that you want to

**[10:28]** execute, then you want to move on to

**[10:30]** this next step. So, once you're ready,

**[10:31]** you could create a brand new folder. In

**[10:33]** this folder, you could call it Fables

**[10:35]** last week, obviously for now. And then

**[10:37]** within that folder, you could break it

**[10:39]** down into some sub folders, tasks, war

**[10:41]** games, a success file, and a ledger

**[10:44]** file. The success file will have your

**[10:46]** criteria that we kind of mentioned in

**[10:47]** passing in the prompt above as to what

**[10:50]** you deem as a successful war game. So,

**[10:52]** if we go to the success.md file, this is

**[10:54]** what it could look like. Yours could

**[10:56]** have more rules, less rules, more

**[10:58]** stringent rules, or even more detailed

**[11:01]** rules. And then the ledger, the whole

**[11:02]** point of it is pointing out anywhere

**[11:04]** where it's blocked. So, if it's war

**[11:06]** gaming and there's some form of variable

**[11:08]** that's undefined, it should populate a

**[11:10]** little parentheses variable placeholder

**[11:12]** for something that it needs your input

**[11:14]** on. And then last but not least, you

**[11:16]** would execute this prompt that I already

**[11:18]** ran before running this video, which is

**[11:20]** /goal. Every mission file in /tasks has

**[11:24]** a first draft war game. Go through each

**[11:26]** one, loop through, and do the recon

**[11:29]** mission for each mission, write a war

**[11:31]** games file, and then draft all 10 before

**[11:33]** polishing any. And then once we take all

**[11:35]** those drafts, you could do something

**[11:37]** like theoretically run {slash} loop

**[11:39]** every 20 minutes, loop through every

**[11:41]** first draft until you really push it to

**[11:44]** its limits. And once you start running

**[11:45]** it, it will fan out a series of parallel

**[11:48]** agents to go and execute each one of

**[11:50]** those tasks at the same time, so that a

**[11:52]** million tokens later, you could have a

**[11:55]** war games folder that's fully populated.

**[11:57]** And you can even have an assumptions

**[11:58]** file.

**[11:59]** Within here, we'll have a full markdown

**[12:01]** file breaking down every single part of

**[12:05]** the assumed inputs,

**[12:07]** the recon needed, the different routes

**[12:09]** that it could take, the different moves

**[12:11]** and considerations it could take through

**[12:13]** this process. You can see right here,

**[12:15]** very comprehensive. Every possible move

**[12:17]** it could take and the possible action,

**[12:19]** reaction, and counteraction that will be

**[12:21]** required. So theoretically, you have 10

**[12:23]** different blueprints that you could feed

**[12:25]** to any AI to execute said projects. And

**[12:28]** like I said, if the ledger is blocked

**[12:30]** for whatever reason, it would look

**[12:31]** something like this, where it would tell

**[12:33]** you inputs needed to unblock are, let's

**[12:35]** say, what kind of business this is for,

**[12:37]** the problem we're solving, the audience,

**[12:39]** everything that you could not specify.

**[12:41]** In my case, since I'm just walking you

**[12:42]** through this as a demo, I asked it to

**[12:44]** assume different values for those

**[12:46]** variables. And like I said, you could

**[12:47]** take this to the next level by tagging a

**[12:49]** Claude Code Guide agent and then say, "I

**[12:52]** want you to tailor this war game to

**[12:54]** exactly how Sonnet 5 would execute it."

**[12:57]** Very tailored to its specific behavior.

**[13:00]** And then this would go spin up a sub

**[13:01]** agent or sub agents to go through all

**[13:03]** the documentation, maybe the system card

**[13:06]** of that model, to make sure that it is

**[13:08]** geared and tailored as much as possible.

**[13:10]** And that's pretty much it. It is not

**[13:11]** rocket science, but it's really taking

**[13:13]** the paradigm of planning and taking it

**[13:15]** to its natural extreme, where you can

**[13:17]** take all the benefit and the raw

**[13:19]** intelligence of Fable to pull out how it

**[13:21]** would do something and just emulate that

**[13:24]** with existing models that are way

**[13:25]** cheaper and hopefully won't just

**[13:27]** disappear in the snap of a finger. And

**[13:29]** like I said, I'm going to make available

**[13:30]** to you all the prompts that I showed you

**[13:32]** down below along with this folder

**[13:33]** structure, so you can emulate it if you

**[13:35]** so choose. And as always, if you want to

**[13:37]** take things to the next level in general

**[13:39]** with things like Cloud Code and Codex

**[13:41]** and agentic workflows in general, make

**[13:43]** sure to check out the first thing down

**[13:44]** below. I drop all kinds of nuggets that

**[13:47]** you'll never see on YouTube in my early

**[13:49]** adopters community. And for the rest of

**[13:50]** you, if you found this helpful and

**[13:51]** novel, I'd super appreciate a like on

**[13:53]** the video. Helps the video helps to

**[13:55]** reach and the channel, and I'll see you

**[13:57]** all in the next one.
