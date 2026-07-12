# Transcript: GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?

**URL:** https://www.youtube.com/watch?v=Zp8lr6IzUnQ
**Segments:** 502
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 17:35
**Uploaded:** 2026-06-28

---

## Full Text

I tried GLM 5.2 and it blew my mind. By the end of this video, you should know where GLM 5.2, an open-source model, can be clawed, where it can safely replace an expensive model, and where switching models is a bit of a trap because you're not replacing a model call. You're actually replacing a whole work system. And that's the thing I want to draw through in this video. So, let me start at the beginning here. GLM 5.2 did not fake impress me. It actually impressed me because it's not just cheap, and it's very cheap to run on the cloud, it's free if you set up your own servers, and for a lot of normal work, it's incredibly good. It's It's often better than Claude. And when I say normal work, I mean the fat middle of everyday AI tasks, right? So, if you're setting up a brochure site for a client, if you have a PowerPoint outline, it's a pretty standard deck. For a first pass copy, routine synthesis, for coding tasks that are tackling familiar problem types in coding, these are tasks with familiar shapes, with lots of examples, with outputs that a human can check quickly. The nerdier phrase for this is that this is the middle of the distribution work for AI. In other words, what you are getting is what someone has tried with models millions of times before, where the answer pattern is pretty normal, and the output is pretty easy to inspect. How many different brochure sites have you seen, right? In that world, GLM 5.2 is incredible. It's fast, it's cheap, it's easy, and it's extremely high quality. It's higher quality than Claude. And a lot of those tasks, I don't think it's honest to say it's just good enough. I think it's It's more accurate to say this is the best model in the world at those center of distribution kinds of tasks, especially ones where front-end taste is important. And so, this is not a video about GLM 5.2 being bad, even though it's not my daily driver, and I'm going to explain why. And so, GLM 5.2 is incredible, but I'm still not using it every day. And in fact, a lot of companies I know are really struggling with the idea that they want to transition to more of a generic router where they can route to the cheapest model available, but it's not actually easy to do in practice. Why is that, right? We're going to talk about why that is, talk about where open source is going, talk about what the shape of work looks like in 2026, and we're going to tie it back into GLM 5.2 and the way we actually need to build to take advantage of models like this. Because cheap AI, it's not a theory anymore. Cheap incredible AI is here. In fact, it's going to be here more and more and more and more because the US government is now slowing down frontier model releases. 5.6 is the latest model to be affected. It's apparently going to be released customer by customer, which is code for we don't know when we're going to get it. For the first time, there is no defined expected cadence for future model releases that are frontier, even though the labs are still doing a phenomenal job training and reinforcement learning their models. And so we're going to have more and more of this open source conversation. And a lot of the open source conversation is frankly about moving down the cost curve, right? Because these frontier model costs are expensive. If you're running a company, they get really expensive. There are stories going around where the numbers are absolutely eye-popping. Like one engineer spending $80,000 in token costs in a week. That's a lot. So if you have that kind of pricing power, if people are spending tens of thousands of dollars a week on tokens, there's an a tremendous amount of incentive to make these models work. So why is it so hard? Why are why are we not seeing a tremendous tipping point away? Why are we still seeing Anthropic growing their revenue like crazy, OpenAI growing their revenue like crazy when these incredible good models exist? Well, there's a number of factors to that, and I want to list them for you so that you can actually understand the perspective. This is based on talking with engineers at companies as well as with leaders. The first one is the ergonomics of work. If you are just trying to get something you've heard about, seen about, you have a frontier model at you have a frontier model at home on your phone, you just want access to that. There's a lot of employee pressure around Claude and around OpenAI in a way that there just isn't for open source models. So, that's one piece. Uh, and it's not small. Like, when people are asking for it vocally saying this will help my work, overburdened IT departments tend to listen to that. Number two, it is actually very, very difficult to correctly figure out whether your task load is center of distribution or edge of distribution weighted. If it's edge distribution weighted, you actually do want the frontier models. If it's center of distribution, the open source models are going to be really, really good because they're common patterns. But, people don't They're not used to measuring their work that way. Individuals aren't, teams aren't. if you're a company trying to figure out what is your model strategy, you kind of got to tackle what is your distribution of tasks? And almost no one has asked that question properly yet. And people are trying to figure out how to measure that. The folks that have gone the farthest, actually, are folks like Flo Crivello, who is, uh, leading the Lindy team, and who very publicly wrote up his journey to a deep seek architecture away from Claude. And, you know, he saved a lot, etc., etc. But, he was also very honest about the fact that the Lindy team had to essentially rewrite their harness from scratch around deep seek, and they could not just take all of their systems for working with Claude, all of their prompts, all of the way they handle memory, all of their tool calls, and just automatically lift and shift. It doesn't work that way. These models need their own harnesses. He was incentivized to do that because he is literally serving AI as a service, and if he can deliver a cheaper and more effective service that hits his margin, and it's it's tremendously impactful. For folks who are using AI internally for coding or for back office automation, that ROI is not as clear, and the incentive to move is not as clear, either. And so, what I have seen, and I have seen anecdotes from this, not just from Flo, but from other folks that I know personally. I know entrepreneurs who are wrestling with this today. The ones who are actually making the jump to open source and dealing with the different system prob dealing with the different tool called dealing with a different memory architecture, etc. That is tuned around the fact that these are center of distribution models. Those guys or those gals are focused on ROI for a particular AI tool they have in market. Just like Lindy, they see value back in their pockets when they can cut their token costs. And for everyone else, because the incentive is not as strong, you don't have the same commitment to wade through the challenge of building a harness. And that is not a small thing. And one of the things I want you to take away from this video is that a model can be an incredible [snorts] brain in a jar. And it it just isn't useful to you without a harness. And so this is why I pay a ton of attention to harness innovations. And I want to name a couple that are top of mind as we look at GLM 5.2 in context. First, I notice that GLM 5.2 was released with its own Codex clone harness. That's one piece that I pay attention to. It looks like the open source model makers are realizing they need to deliver harnesses as well. And so I would expect more innovation in that direction. I notice that Codex is starting to call out publicly that you can use Codex the harness without using any OpenAI model. That's notable because there's a different path to value for OpenAI there. Maybe OpenAI's models are the default, but if they're calling out that they are actually the harness for all of work, it gives them a way to be stickier long term. Three, the Anthropic team is not just sitting there as all of these developments happen. They launched Claude Tag this week, and Claude Tag is an incredibly sticky product. It is a team level harness, and team level harnesses are where the energy is going because so much of the work we've got is individually productive work in AI. It's not team productive work. And we're trying to figure out, how do we align our efforts that are individually productive into something that is team productive? And Claude tag, which is just tag Claude, anyone can tag Claude and get work done in Slack, is one of the first examples of a sticky viral consumer team harness. Where like if you're an ordinary knowledge worker at a particular company, you can envision using that as as a team harness. And you don't have to know the word team harness, it's just going to work. You tag Claude and it works. But look at it strategically from Anthropic's perspective. Now they're not just getting the engineers. Now they're getting everybody who's a knowledge worker in Slack and they're reading all of the messy context that lives in Slack that no one knows how to codify and that is now getting fed into Claude automatically and it can be something that the Anthropic team learns from within privacy policies long term for Claude in the context of that company to start to own the harness itself in a way that no company can get away from. It's an incredibly sticky experience because you think about it. Let's say you you know that GLM 5.2 is a lot cheaper, which it is. It's like 98% cheaper or something like that. If it's that much cheaper than Claude and it's just about as good on most tasks, it is rational to build a routing system and assign most tasks to GLM 5.2. Except that hey, are you going to have Claude tag, right? Are you going to go to tag in Claude on that stuff? Is that convenience going to be there? Are are you going to have to restart the job of giving this AI context from your company because Claude magically acquired it in Slack and you didn't have to think about it? We have taught companies for decades that data is alpha. Data is something you have an edge with if you're serious. If data is alpha, what do we think about giving all of that data to a frontier model provider as context? Even if they don't release it into training data, even if they if the privacy policy is really good and they're behaving really ethically, which I have no reason to think they're not, you still are effectively renting your own context back to yourself because Claude is going to be in your slack as a team level harness and is going to be incredibly close to all the work your team does and it's going to be impossible to rip out. No matter how cheap the GLM 5.2 class models are, how can you rip out the model that's that close to context? And I think that the GLM 5.2 team knows this. That's why they released a harness, a Codex-like interface with their AI. It's a first stab at it. But we got to get much farther there in tech, where the companies that know they need harnesses generally cannot afford to hire the AI talent to build those harnesses unless they're extraordinary companies because that AI talent is so in demand right now that it can charge anything it wants and it usually goes to one of the hyperscalers or another large company. And so we're in the dynamic where the only companies that can build their own last-mile harnesses, their own auto routers, are companies that can afford that, that can afford the AI talent to do that, which is very scarce. And so if you actually think through this dynamic with GLM 5.2 and how it's possible but at the same time we can have an incredible open-source model that we're excited about and also that Anthropic still has pricing power to charge a lot for their tokens even though their tokens are just marginally better, it's actually not a story of intelligence. It's a story of the last-mile in AI and the fact that the talent to build the last-mile in AI is incredibly scarce. Which should, honestly, for a lot of you watching, be a source for optimism. If we have that scarce a talent, where people are ending up locked into contracts with a frontier model provider because they don't know how to build a harness for themselves, wow is there a lot of opportunity in knowing how to build an AI. Like it's an incredible opportunity right now. It is not easy to do this work. It's not easy to know this is how you handle a tool call in GLM 5.2 and how you should do it differently from Claude. So does figuring out how memory will work for that system. So does figuring out how the system prompt needs to change because it's a center of distribution model. It's a lot of technical work. And if you know how to do that work or know how to do parts of that work to essentially refactor agentic pipelines so they work with an open-source model, you are going to be incredibly in demand. Especially if you compare that with the ability to route tasks where you can take a task and recognize on the fly that it's a frontier model task and it should go to a frontier model versus everything else going to a cheaper open-source model. That is going to be a huge investment theme for companies in 2026, 2027 and they're going to keep innovating. Claude tag is a fantastic example of how of how incentives in frontier close-source models are giving us incredible experiences. If you have pricing power, you are heavily incentivized to make sure that your experience is as convenient and ergonomic as possible. And so features like Claude Claude tag are going to appear really, really fast, really rapidly, really completely from teams at Anthropic, also from OpenAI because they're incentivized to keep those those prices high and to go after that business. And with open-source models, you don't have the same margin to work with, you don't have the same cash flow to work with and you don't have the same incentive to dig in and deploy thousands of forward-deployed engineers and really make these harnesses sing. And so one of the really interesting facts that we come to after all of this can simultaneously be an incredible model, a model that a lot of entrepreneurs switch to when the ROI is clear and they're technically savvy enough to do it, and also not a model that is easy for a given company that you turn up in phone book to actually use. It any given company is going to have to think about how they use GLM 5.2 to use it usefully, and they're going to have to think a lot less to sign up for a frontier model contract that's going to fit right into their existing workflows. That last mile is literally a trillion-dollar last mile in AI. And one of the biggest open questions right now is whether we will scale our talent fast enough to enable businesses to tackle that problem set without paying so much that they can't afford it. I don't know what the answer's going to be, but that's a question we're going to have an answer to. We will all collectively answer together in the next 3 to 6 months. We are going to find out, especially as the US government has this effective pause in place on frontier model releases, and the open-source systems are going to continue to be available, we're going to find out whether companies can adjust to the fact that intelligence is 98% cheaper and takes a last mile to build. Can they actually build that last mile? Can they find teams to build that last mile? If you are in an agency or in a consulting space, this is a golden goose moment. Like you have a chance here. You can really go to town and basically promise to save people a ton of money on tokens as part of your ROI proposition, as long as you can deliver that refactor in a way that maintains quality, which is not a trivial task. If it was easy, we wouldn't be having this video. So, where does this leave us? GLM 5.2 is an incredible model. It is important not to shame a model or diss a model because it's good at center of distribution task, because by definition that is most of our work. Collectively as a species, most of our knowledge work is center of distribution, just by definition. And if that's the case, a model that's really good at that is worth taking really seriously. And if we take it seriously, that means we have to take the last mile seriously. We have to take the idea that we need a harness for that last mile seriously. And that's a lot of what I have been doing in public is starting to articulate what it takes to build a harness, whether it's open skills or open brain or open engine, which I've all talked about on this channel. How do you start to take these pieces and put them together in a way that is agent agnostic, that is model agnostic, so you can start to install those pieces and actually take advantage of all the intelligence on tap. Whether it's Claude, whether it's it's Codex, whether it's Hermes, whether it's whatever whatever system you want, whether it's your own iPhone 2, you should be able to easily build to that last mile. And and I know that there's a lot of custom work for individual companies, and that's why I keep saying this is a time for builders. But if we don't start down that path, we're essentially going to be renting our company brain and company context back from the frontier model providers. And they're going to have it. And they're going to be able to use it to continue to improve their systems and make them more useful, and they'll be incredibly convenient, incredibly sticky products. And what are we going to do? We're going to have to use them. So, this is a very pivotal moment for corporations. The firm has never faced a moment where the firm's brain has been on rent. And that is what we're on the verge of with tools like Claude Tag, which are incredibly useful. I'm not saying they're not useful, they're very useful. That's exactly the dangerous thing. So, I would encourage you if you are even if it's a tiny company, let's say you're building your own agency, you're an individual entrepreneur, think seriously, just as you would if you're a larger company leader, think seriously about whether you want to rent that context and intelligence or not. Think seriously about where you want to go with your context long term. Ask yourself, do you have an idea of the distribution of your tasks? Do you have access to technical talent that you can use to build out that last mile? What are the task sets that you would want to assign that would save you a ton in tokens? A lot of people don't sit down and get pencil and paper and actually ask themselves those kinds of questions. And I have a whole sort of question set that's in more detail that I've been going over with leaders. I put that on the Substack. Uh but this is a really serious thing. This is a moment for open source. GLON 5.2 opened that door for all of us, and it's going to be up to us to see how we take advantage of it. Good luck with that. Cheers. Bye.

---

## Timestamped Segments

**[0:00]** I tried GLM 5.2 and it blew my mind. By

**[0:02]** the end of this video, you should know

**[0:04]** where GLM 5.2, an open-source model, can

**[0:07]** be clawed, where it can safely replace

**[0:09]** an expensive model, and where switching

**[0:11]** models is a bit of a trap because you're

**[0:12]** not replacing a model call. You're

**[0:15]** actually replacing a whole work system.

**[0:16]** And that's the thing I want to draw

**[0:18]** through in this video. So, let me start

**[0:20]** at the beginning here. GLM 5.2 did not

**[0:22]** fake impress me. It actually impressed

**[0:25]** me because it's not just cheap, and it's

**[0:27]** very cheap to run on the cloud, it's

**[0:28]** free if you set up your own servers, and

**[0:30]** for a lot of normal work, it's

**[0:32]** incredibly good. It's It's often better

**[0:35]** than Claude. And when I say normal work,

**[0:37]** I mean the fat middle of everyday AI

**[0:39]** tasks, right? So, if you're setting up a

**[0:41]** brochure site for a client, if you have

**[0:43]** a PowerPoint outline, it's a pretty

**[0:45]** standard deck. For a first pass copy,

**[0:47]** routine synthesis, for coding tasks that

**[0:50]** are tackling familiar problem types in

**[0:53]** coding, these are tasks with familiar

**[0:54]** shapes, with lots of examples, with

**[0:56]** outputs that a human can check quickly.

**[0:59]** The nerdier phrase for this is that this

**[1:01]** is the middle of the distribution work

**[1:03]** for AI. In other words, what you are

**[1:05]** getting is what someone has tried with

**[1:07]** models millions of times before, where

**[1:10]** the answer pattern is pretty normal, and

**[1:12]** the output is pretty easy to inspect.

**[1:14]** How many different brochure sites have

**[1:16]** you seen, right? In that world, GLM 5.2

**[1:19]** is incredible. It's fast, it's cheap,

**[1:21]** it's easy, and it's extremely high

**[1:23]** quality. It's higher quality than

**[1:25]** Claude. And a lot of those tasks, I

**[1:27]** don't think it's honest to say it's just

**[1:29]** good enough. I think it's It's more

**[1:31]** accurate to say this is the best model

**[1:34]** in the world at those center of

**[1:36]** distribution kinds of tasks, especially

**[1:39]** ones where front-end taste is important.

**[1:41]** And so, this is not a video about GLM

**[1:43]** 5.2 being bad, even though it's not my

**[1:46]** daily driver, and I'm going to explain

**[1:48]** why. And so, GLM 5.2 is incredible, but

**[1:51]** I'm still not using it every day. And in

**[1:53]** fact, a lot of companies I know are

**[1:55]** really struggling with the idea that

**[1:57]** they want to transition to more of a

**[2:00]** generic router where they can route to

**[2:02]** the cheapest model available, but it's

**[2:04]** not actually easy to do in practice. Why

**[2:06]** is that, right? We're going to talk

**[2:07]** about why that is, talk about where open

**[2:10]** source is going, talk about what the

**[2:12]** shape of work looks like in 2026, and

**[2:14]** we're going to tie it back into GLM 5.2

**[2:16]** and the way we actually need to build to

**[2:19]** take advantage of models like this.

**[2:21]** Because cheap AI, it's not a theory

**[2:23]** anymore. Cheap incredible AI is here. In

**[2:26]** fact, it's going to be here more and

**[2:28]** more and more and more because the US

**[2:30]** government is now slowing down frontier

**[2:32]** model releases. 5.6 is the latest model

**[2:35]** to be affected. It's apparently going to

**[2:36]** be released customer by customer, which

**[2:38]** is code for we don't know when we're

**[2:40]** going to get it. For the first time,

**[2:41]** there is no defined expected cadence for

**[2:44]** future model releases that are frontier,

**[2:46]** even though the labs are still doing a

**[2:48]** phenomenal job training and

**[2:50]** reinforcement learning their models. And

**[2:52]** so we're going to have more and more of

**[2:53]** this open source conversation. And a lot

**[2:55]** of the open source conversation is

**[2:57]** frankly about moving down the cost

**[3:00]** curve, right? Because these frontier

**[3:01]** model costs are expensive. If you're

**[3:04]** running a company, they get really

**[3:05]** expensive. There are stories going

**[3:07]** around where the numbers are absolutely

**[3:09]** eye-popping. Like one engineer spending

**[3:11]** $80,000 in token costs in a week. That's

**[3:13]** a lot. So if you have that kind of

**[3:15]** pricing power, if people are spending

**[3:17]** tens of thousands of dollars a week on

**[3:19]** tokens, there's an a tremendous amount

**[3:21]** of incentive to make these models work.

**[3:22]** So why is it so hard? Why are why are we

**[3:25]** not seeing a tremendous tipping point

**[3:26]** away? Why are we still seeing Anthropic

**[3:28]** growing their revenue like crazy, OpenAI

**[3:30]** growing their revenue like crazy when

**[3:32]** these incredible good models exist?

**[3:34]** Well, there's a number of factors to

**[3:36]** that, and I want to list them for you so

**[3:37]** that you can actually understand the

**[3:39]** perspective. This is based on talking

**[3:40]** with engineers at companies as well as

**[3:42]** with leaders. The first one is the

**[3:44]** ergonomics of work. If you are just

**[3:47]** trying to get something you've heard

**[3:49]** about, seen about, you have a frontier

**[3:50]** model at you have a frontier model at

**[3:53]** home on your phone, you just want access

**[3:55]** to that. There's a lot of employee

**[3:56]** pressure around Claude and around OpenAI

**[3:59]** in a way that there just isn't for open

**[4:01]** source models. So, that's one piece. Uh,

**[4:03]** and it's not small. Like, when people

**[4:04]** are asking for it vocally saying this

**[4:06]** will help my work, overburdened IT

**[4:08]** departments tend to listen to that.

**[4:09]** Number two, it is actually very, very

**[4:12]** difficult to correctly figure out

**[4:16]** whether your task load is center of

**[4:19]** distribution or edge of distribution

**[4:22]** weighted. If it's edge distribution

**[4:23]** weighted, you actually do want the

**[4:25]** frontier models. If it's center of

**[4:26]** distribution, the open source models are

**[4:28]** going to be really, really good because

**[4:30]** they're common patterns. But, people

**[4:32]** don't They're not used to measuring

**[4:34]** their work that way. Individuals aren't,

**[4:35]** teams aren't. if you're a company trying

**[4:37]** to figure out what is your model

**[4:38]** strategy, you kind of got to tackle

**[4:41]** what is your distribution of tasks? And

**[4:43]** almost no one has asked that question

**[4:45]** properly yet. And people are trying to

**[4:47]** figure out how to measure that. The

**[4:48]** folks that have gone the farthest,

**[4:50]** actually, are folks like Flo Crivello,

**[4:52]** who is, uh, leading the Lindy team, and

**[4:55]** who very publicly wrote up his journey

**[4:57]** to a deep seek architecture away from

**[5:00]** Claude. And, you know, he saved a lot,

**[5:02]** etc., etc. But, he was also very honest

**[5:05]** about the fact that the Lindy team had

**[5:07]** to essentially rewrite their harness

**[5:10]** from scratch around deep seek, and they

**[5:13]** could not just take all of their systems

**[5:15]** for working with Claude, all of their

**[5:17]** prompts, all of the way they handle

**[5:19]** memory, all of their tool calls, and

**[5:20]** just automatically lift and shift. It

**[5:22]** doesn't work that way. These models need

**[5:24]** their own harnesses.

**[5:25]** He was incentivized to do that because

**[5:27]** he is literally serving AI as a service,

**[5:29]** and if he can deliver a cheaper and more

**[5:31]** effective service that hits his margin,

**[5:33]** and it's it's tremendously impactful.

**[5:35]** For folks who are using AI internally

**[5:37]** for coding or for back office

**[5:38]** automation, that ROI is not as clear,

**[5:40]** and the incentive to move is not as

**[5:42]** clear, either. And so, what I have seen,

**[5:44]** and I have seen anecdotes from this, not

**[5:46]** just from Flo, but from other folks that

**[5:48]** I know personally. I know entrepreneurs

**[5:49]** who are wrestling with this today. The

**[5:52]** ones who are actually making the jump to

**[5:54]** open source and dealing with the

**[5:56]** different system prob dealing with the

**[5:57]** different tool called dealing with a

**[5:58]** different memory architecture, etc. That

**[6:00]** is tuned around the fact that these are

**[6:02]** center of distribution models. Those

**[6:04]** guys or those gals are focused on ROI

**[6:09]** for a particular AI tool they have in

**[6:12]** market. Just like Lindy, they see value

**[6:15]** back in their pockets when they can cut

**[6:17]** their token costs. And for everyone

**[6:19]** else, because the incentive is not as

**[6:21]** strong, you don't have the same

**[6:24]** commitment to wade through the challenge

**[6:26]** of building a harness. And that is not a

**[6:28]** small thing. And one of the things I

**[6:30]** want you to take away from this video is

**[6:32]** that a model can be an incredible

**[6:34]** [snorts] brain in a jar. And it it just

**[6:37]** isn't useful to you without a harness.

**[6:39]** And so this is why I pay a ton of

**[6:41]** attention to harness innovations. And I

**[6:43]** want to name a couple that are top of

**[6:45]** mind as we look at GLM 5.2 in context.

**[6:48]** First, I notice that GLM 5.2 was

**[6:51]** released with its own Codex clone

**[6:53]** harness. That's one piece that I pay

**[6:55]** attention to. It looks like the open

**[6:57]** source model makers are realizing they

**[6:59]** need to deliver harnesses as well. And

**[7:00]** so I would expect more innovation in

**[7:02]** that direction. I notice that Codex is

**[7:04]** starting to call out publicly that you

**[7:07]** can use Codex the harness without using

**[7:09]** any OpenAI model. That's notable because

**[7:13]** there's a different path to value for

**[7:15]** OpenAI there. Maybe OpenAI's models are

**[7:17]** the default, but if they're calling out

**[7:19]** that they are actually the harness for

**[7:20]** all of work, it gives them a way to be

**[7:22]** stickier long term. Three, the Anthropic

**[7:25]** team is not just sitting there as all of

**[7:27]** these developments happen. They launched

**[7:28]** Claude Tag this week, and Claude Tag is

**[7:31]** an incredibly sticky product. It is a

**[7:34]** team level harness, and team level

**[7:35]** harnesses are where the energy is going

**[7:37]** because so much of the work we've got is

**[7:39]** individually productive work in AI. It's

**[7:42]** not team productive work. And we're

**[7:44]** trying to figure out, how do we align

**[7:46]** our efforts that are individually

**[7:47]** productive into something that is team

**[7:49]** productive? And Claude tag, which is

**[7:51]** just tag Claude, anyone can tag Claude

**[7:53]** and get work done in Slack, is one of

**[7:56]** the first examples of a sticky viral

**[7:58]** consumer team harness. Where like if

**[8:01]** you're an ordinary knowledge worker at a

**[8:03]** particular company, you can envision

**[8:05]** using that as as a team harness. And you

**[8:07]** don't have to know the word team

**[8:08]** harness, it's just going to work. You

**[8:09]** tag Claude and it works. But look at it

**[8:12]** strategically from Anthropic's

**[8:13]** perspective. Now they're not just

**[8:15]** getting the engineers. Now they're

**[8:16]** getting everybody who's a knowledge

**[8:17]** worker in Slack and they're reading all

**[8:19]** of the messy context that lives in Slack

**[8:23]** that no one knows how to codify and that

**[8:25]** is now getting fed into Claude

**[8:27]** automatically and it can be something

**[8:30]** that the Anthropic team learns from

**[8:31]** within privacy policies long term for

**[8:34]** Claude in the context of that company to

**[8:38]** start to own the harness itself in a way

**[8:44]** that no company can get away from. It's

**[8:45]** an incredibly sticky experience because

**[8:47]** you think about it. Let's say you you

**[8:49]** know that GLM 5.2 is a lot cheaper,

**[8:51]** which it is. It's like 98% cheaper or

**[8:53]** something like that. If it's that much

**[8:55]** cheaper than Claude and it's just about

**[8:57]** as good on most tasks, it is rational to

**[9:00]** build a routing system and assign most

**[9:02]** tasks to GLM 5.2. Except that hey, are

**[9:05]** you going to have Claude tag, right? Are

**[9:07]** you going to go to tag in Claude on that

**[9:08]** stuff? Is that convenience going to be

**[9:09]** there? Are are you going to have to

**[9:12]** restart the job of giving this AI

**[9:14]** context from your company because Claude

**[9:16]** magically acquired it in Slack and you

**[9:18]** didn't have to think about it? We have

**[9:20]** taught companies for decades that data

**[9:23]** is alpha. Data is something you have an

**[9:25]** edge with if you're serious. If data is

**[9:28]** alpha, what do we think about giving all

**[9:32]** of that data to a frontier model

**[9:34]** provider as context? Even if they don't

**[9:37]** release it into training data, even if

**[9:38]** they if the privacy policy is really

**[9:40]** good and they're behaving really

**[9:42]** ethically, which I have no reason to

**[9:43]** think they're not, you still are

**[9:45]** effectively renting your own context

**[9:47]** back to yourself because Claude is going

**[9:50]** to be in your slack as a team level

**[9:51]** harness and is going to be incredibly

**[9:53]** close to all the work your team does and

**[9:55]** it's going to be impossible to rip out.

**[9:57]** No matter how cheap the GLM 5.2 class

**[10:00]** models are,

**[10:01]** how can you rip out the model that's

**[10:02]** that close to context? And I think that

**[10:05]** the GLM 5.2 team knows this. That's why

**[10:07]** they released a harness, a Codex-like

**[10:09]** interface with their AI. It's a first

**[10:12]** stab at it. But we got to get much

**[10:14]** farther there in tech, where the

**[10:16]** companies that know they need harnesses

**[10:19]** generally cannot afford to hire the AI

**[10:22]** talent to build those harnesses unless

**[10:24]** they're extraordinary companies because

**[10:27]** that AI talent is so in demand right now

**[10:30]** that it can charge anything it wants and

**[10:31]** it usually goes to one of the

**[10:33]** hyperscalers or another large company.

**[10:35]** And so we're in the dynamic where the

**[10:36]** only companies that can build their own

**[10:38]** last-mile harnesses, their own auto

**[10:40]** routers, are companies that can afford

**[10:42]** that, that can afford the AI talent to

**[10:44]** do that, which is very scarce. And so if

**[10:46]** you actually think through this dynamic

**[10:48]** with GLM 5.2 and how it's possible but

**[10:50]** at the same time we can have an

**[10:52]** incredible open-source model that we're

**[10:54]** excited about and also that Anthropic

**[10:56]** still has pricing power to charge a lot

**[10:59]** for their tokens even though their

**[11:00]** tokens are just marginally better, it's

**[11:02]** actually not a story of intelligence.

**[11:03]** It's a story of the last-mile in AI and

**[11:06]** the fact that the talent to build the

**[11:09]** last-mile in AI is incredibly scarce.

**[11:12]** Which should, honestly, for a lot of you

**[11:14]** watching, be a source for optimism. If

**[11:17]** we have that scarce a talent, where

**[11:19]** people are ending up locked into

**[11:20]** contracts with a frontier model provider

**[11:23]** because they don't know how to build a

**[11:25]** harness for themselves, wow is there a

**[11:27]** lot of opportunity in knowing how to

**[11:29]** build an AI. Like it's an incredible

**[11:31]** opportunity right now. It is not easy to

**[11:33]** do this work. It's not easy to know this

**[11:36]** is how you handle a tool call in GLM 5.2

**[11:39]** and how you should do it differently

**[11:40]** from Claude. So does figuring out how

**[11:42]** memory will work for that system. So

**[11:44]** does figuring out how the system prompt

**[11:46]** needs to change because it's a center of

**[11:48]** distribution model. It's a lot of

**[11:50]** technical work. And if you know how to

**[11:52]** do that work or know how to do parts of

**[11:54]** that work to essentially refactor

**[11:56]** agentic pipelines so they work with an

**[11:59]** open-source model, you are going to be

**[12:01]** incredibly in demand. Especially if you

**[12:04]** compare that with the ability to route

**[12:06]** tasks where you can take a task and

**[12:08]** recognize on the fly that it's a

**[12:10]** frontier model task and it should go to

**[12:11]** a frontier model versus everything else

**[12:13]** going to a cheaper open-source model.

**[12:15]** That is going to be a huge investment

**[12:17]** theme for companies in 2026, 2027 and

**[12:20]** they're going to keep innovating. Claude

**[12:21]** tag is a fantastic example of how of how

**[12:24]** incentives in frontier close-source

**[12:26]** models are giving us incredible

**[12:29]** experiences. If you have pricing power,

**[12:30]** you are heavily incentivized to make

**[12:33]** sure that your experience is as

**[12:34]** convenient and ergonomic as possible.

**[12:36]** And so features like Claude Claude tag

**[12:38]** are going to appear really, really fast,

**[12:41]** really rapidly, really completely from

**[12:44]** teams at Anthropic, also from OpenAI

**[12:46]** because they're incentivized to keep

**[12:48]** those those prices high and to go after

**[12:51]** that business. And with open-source

**[12:53]** models, you don't have the same margin

**[12:55]** to work with, you don't have the same

**[12:56]** cash flow to work with and you don't

**[12:58]** have the same incentive to dig in and

**[13:00]** deploy thousands of forward-deployed

**[13:01]** engineers and really make these

**[13:03]** harnesses sing. And so one of the really

**[13:06]** interesting facts that we come to after

**[13:08]** all of this can simultaneously be an

**[13:11]** incredible model, a model that a lot of

**[13:13]** entrepreneurs switch to when the ROI is

**[13:15]** clear and they're technically savvy

**[13:16]** enough to do it, and also not a model

**[13:19]** that is easy for a given company that

**[13:22]** you turn up in phone book to actually

**[13:25]** use. It any given company is going to

**[13:28]** have to think about how they use GLM 5.2

**[13:30]** to use it usefully, and they're going to

**[13:32]** have to think a lot less to sign up for

**[13:34]** a frontier model contract that's going

**[13:35]** to fit right into their existing

**[13:37]** workflows. That last mile is literally a

**[13:40]** trillion-dollar last mile in AI. And one

**[13:43]** of the biggest open questions right now

**[13:46]** is whether we will scale our talent fast

**[13:49]** enough to enable businesses to tackle

**[13:52]** that problem set without paying so much

**[13:57]** that they can't afford it. I don't know

**[13:58]** what the answer's going to be, but

**[13:59]** that's a question we're going to have an

**[14:01]** answer to. We will all collectively

**[14:03]** answer together in the next 3 to 6

**[14:07]** months. We are going to find out,

**[14:09]** especially as the US government has this

**[14:11]** effective pause in place on frontier

**[14:13]** model releases,

**[14:14]** and the open-source systems are going to

**[14:16]** continue to be available, we're going to

**[14:17]** find out whether companies can adjust to

**[14:21]** the fact that intelligence is 98%

**[14:23]** cheaper and takes a last mile to build.

**[14:25]** Can they actually build that last mile?

**[14:27]** Can they find teams to build that last

**[14:28]** mile? If you are in an agency or in a

**[14:30]** consulting space, this is a golden goose

**[14:33]** moment. Like you have a chance here. You

**[14:35]** can really go to town and basically

**[14:37]** promise to save people a ton of money on

**[14:40]** tokens as part of your ROI proposition,

**[14:42]** as long as you can deliver that refactor

**[14:44]** in a way that maintains quality, which

**[14:45]** is not a trivial task. If it was easy,

**[14:47]** we wouldn't be having this video. So,

**[14:49]** where does this leave us? GLM 5.2 is an

**[14:53]** incredible model. It is important not to

**[14:56]** shame a model or diss a model because

**[14:58]** it's good at center of distribution

**[14:59]** task, because by definition that is most

**[15:01]** of our work. Collectively as a species,

**[15:04]** most of our knowledge work is center of

**[15:05]** distribution, just by definition. And if

**[15:07]** that's the case, a model that's really

**[15:09]** good at that is worth taking really

**[15:11]** seriously. And if we take it seriously,

**[15:13]** that means we have to take the last mile

**[15:15]** seriously. We have to take the idea that

**[15:16]** we need a harness for that last mile

**[15:18]** seriously. And that's a lot of what I

**[15:20]** have been doing in public is starting to

**[15:22]** articulate what it takes to build a

**[15:25]** harness, whether it's open skills or

**[15:27]** open brain or open engine, which I've

**[15:29]** all talked about on this channel. How do

**[15:32]** you start to take these pieces and put

**[15:33]** them together in a way that is agent

**[15:35]** agnostic, that is model agnostic, so you

**[15:37]** can start to install those pieces and

**[15:39]** actually take advantage of all the

**[15:41]** intelligence on tap. Whether it's

**[15:43]** Claude, whether it's it's Codex, whether

**[15:45]** it's Hermes, whether it's whatever

**[15:47]** whatever system you want, whether it's

**[15:49]** your own iPhone 2, you should be able to

**[15:52]** easily build to that last mile. And and

**[15:56]** I know that there's a lot of custom work

**[15:57]** for individual companies, and that's why

**[15:58]** I keep saying this is a time for

**[16:00]** builders. But if we don't start down

**[16:02]** that path, we're essentially going to be

**[16:03]** renting our company brain and company

**[16:05]** context back from the frontier model

**[16:09]** providers.

**[16:10]** And they're going to have it. And

**[16:11]** they're going to be able to use it to

**[16:13]** continue to improve their systems and

**[16:15]** make them more useful, and they'll be

**[16:16]** incredibly convenient, incredibly sticky

**[16:18]** products. And what are we going to do?

**[16:20]** We're going to have to use them. So,

**[16:21]** this is a very pivotal moment for

**[16:23]** corporations. The firm has never faced a

**[16:26]** moment where the firm's brain has been

**[16:29]** on rent. And that is what we're on the

**[16:30]** verge of with tools like Claude Tag,

**[16:33]** which are incredibly useful. I'm not

**[16:35]** saying they're not useful, they're very

**[16:36]** useful. That's exactly the dangerous

**[16:38]** thing. So, I would encourage you

**[16:40]** if you are even if it's a tiny company,

**[16:43]** let's say you're building your own

**[16:44]** agency, you're an individual

**[16:45]** entrepreneur, think seriously, just as

**[16:48]** you would if you're a larger company

**[16:49]** leader, think seriously about whether

**[16:51]** you want to rent that context and

**[16:53]** intelligence or not. Think seriously

**[16:56]** about where you want to go with your

**[16:57]** context long term. Ask yourself, do you

**[17:01]** have an idea of the distribution of your

**[17:03]** tasks? Do you have access to technical

**[17:05]** talent that you can use to build out

**[17:07]** that last mile? What are the task sets

**[17:10]** that you would want to assign that would

**[17:12]** save you a ton in tokens? A lot of

**[17:14]** people don't sit down and get pencil and

**[17:16]** paper and actually ask themselves those

**[17:17]** kinds of questions. And I have a whole

**[17:19]** sort of question set that's in more

**[17:20]** detail that I've been going over with

**[17:22]** leaders. I put that on the Substack. Uh

**[17:24]** but this is a really serious thing. This

**[17:26]** is a moment for open source. GLON 5.2

**[17:29]** opened that door for all of us, and it's

**[17:31]** going to be up to us to see how we take

**[17:33]** advantage of it. Good luck with that.

**[17:34]** Cheers. Bye.
