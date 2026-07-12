# Transcript: Full Archon Guide - Build AI Coding Harnesses That Actually Ship (LIVE)

**URL:** https://www.youtube.com/watch?v=srx9iwnjK2M
**Segments:** 4435
**Channel:** Cole Medin
**Duration:** 2:45:30
**Uploaded:** 2026-04-11

---

## Full Text

All right, we are live. Welcome everybody to the Archon live stream. We're going to be diving into everything with Archon today. So, I posted a YouTube video just this week introducing the new version of Archon. Uh, but now we get to actually go deep into using it. And there are a couple of things I have up my sleeve today that are kind of interesting. So, I'm going to be building a what's called a dark factory this month. If it sounds spooky or interesting to you, we'll talk about that more uh in a little bit. Um that'll be kind of like the tail end of our live stream today. So, yeah, but I want to start by actually introducing Archon to you guys. Uh just to give a whole, you know, overview of the tool. I know that I talked about it on Wednesday in the YouTube video, but I I want to be pretty comprehensive in the live stream today. And then we'll build some workflows together. I'll show you what it looks like to use Archon, how I use it on the daily basis, and then we'll get into the the dark factory stuff. I'm pretty excited. So, uh yeah, I'm sitting down right now. I'm like actually like always standing in my live streams and my YouTube videos, but uh I had a couple leg days like in a row. Um, and my legs are like toasted right now, so it's really It actually kind of like hurts to stand right now. It's pretty crazy. Um, so yeah, I'm actually sitting down for a live stream. I've like never done that before. Um, but yeah. Anyway, so I've got my left monitor here with all of the comments from you guys that I'm watching. And then I've got my right monitor where I have my streaming software. So when you see me look around, that's what I'm doing. And then obviously I'm sharing my screen on the main monitor right here. So, I can actually switch to share my screen here and then I can pop up chats like this right here. Hey, Cole, looking forward to this one. I appreciate very much. Yeah, so I I was checking out the chat as I was getting things started here. It's exciting to see uh everyone in here already. Congrats on the launch. Love seeing the structure for AI workflows. Still wrapping my head around its potential, you know. I appreciate Thomas and I still am as well because it's actually kind of crazy. Um, maybe we'll talk about this a little bit today, but we can use Archon for a lot more than just AI coding. Like you can use it for any kind of agentic workflow, for deep research or any kind of like content creation. Um, I'm not going to build anything around that now, but that's going to be more coming soon in videos and future live streams. So, yeah, the the possibilities are pretty limitless here. And I think as I really introduce Archon to you guys right now, you'll see what I'm talking about. Cool. All good sitting down. You still look great, Cole. Appreciate it, Eric. Yeah, it feels weird to me, but um yeah, I definitely need it right now. It's exactly right. Never skip leg day. Yeah. So, so I I started doing so I was doing a lot of CrossFit last year and um I took a break. I just like started going to like a regular commercial gym and I'm now I'm back to doing CrossFit again. And uh the workouts were pretty intense last couple days for the legs. Um so yesterday was a lot of uh Bulgarian split squats, jumping lunges, uh wall balls, and um and biking. So yeah, I'm pretty cooked, but it's good. Uh all right, cool. So, I'm going to go ahead and pop up my uh Obsidian vault here. So, I've got the diagram to really introduce why I built Archon in the first place. And I I also want to be clear here. I did not build Archon by myself. There are a couple of people that helped me a lot with Archon. Uh Raasmus and Thomas are the two that have really helped me the most with the project. Uh Thomas is here. He's a DIY smart code. Uh so he's here. I see him in the chat. Shout out to Thomas. Not sure why there's an echo for the stream, Thomas, but yeah, thank you for all the work that you've done on Archon. Rasmus, I don't know if he's here. Uh but yeah, big shout out to him as well. Um yeah, I don't think he is for today, but that's all good. So yeah, I' I've had I've had a lot of help building Archon and of course I've had a lot of help from Claude Code building Archon as well. Uh let me tell you, I am using Archon to build Archon constantly. I'll show you guys what that looks like today as well. But let's talk about the evolution here. Why we care about Archon? Why why did I care about building it in the first place? So allow me to like talk about this for a little bit. U because I really want to get you guys on board with the vision that I have here. And it is a big vision. So it's everyone knows that like prompt engineering was a big thing when generative AI first became a thing back in 2022. So we had like you know the release of GPT 3.5 Turbo. That's when everyone started giving uh a lot of hoots and hollers about generative AI and people are obsessed with prompt engineering. And the idea behind prompt engineering is how can we craft our prompts to the LLM to get the single best output. So at this point people are very much like caring about just uh you know that very next turn with the LLM. How do we get it to do or output what we want? And then uh that evolved in 2025 to the idea of context engineering. So now we don't care about just single outputs. Now we care about entire sessions especially for AI coding sessions. Context engineering is the idea of uh you know how can we curate the perfect context nothing more than the coding agent needs but exactly what it needs to uh have all the context it needs to plausibly do the task. So this was popularized by a lot of people like Toby the CEO of Shopify of course Andre Karpathy because whenever he posts something of course it goes viral. Uh but context engineering it's a very powerful evolution because it's treating the context for our coding agents as an engineered resource. So we evolve our AI layer as I like to call it just like we evolve our code base. So we version control our rules and our commands and our skills. And whenever there's a problem that comes up with our um system like there's a bug that our coding agent produces instead of just fixing the bug and moving on. The idea behind context engineering is we look into our process like what could we make better with our commands or what could we make better with our rules so that that issue doesn't happen again or at least that's the goal of evolving our context. So it's a very powerful concept and I created a lot of content last year around context engineering. Now the important thing is these different evolutions it's not like they replace each other. Context engineering does not replace prompt engineering. In fact prompt engineering is a part of context engineering. So it's it's a evolution where it builds on top of itself. And so this year we have evolved to harness engineering. And this is what archon is all about. So harness engineering can mean a lot of different things, but in essence, a harness is a layer on top of the coding agent. It's the tooling and the process that you build on top of the coding agent to make it more reliable and basically taking your whole you know process for building software and you know building the the layer on top of the coding agent where you enforce that process. So, a lot of different strategies out there like BMAD and GitHub spec kit and GSD, you could consider them harnesses because you're you're wrapping the coding agent in this higher level layer of your strategy for engineering. And we have a stripe minions. Uh the Ralph loop is a harness. Enthropic has open sourced quite a few harnesses. I've covered some on my channel. really every single big company is converging on the idea of harnesses. Instead of focusing on making the model better or making the tool better, like the coding agent better, it's it's all about like how do we create the system that wraps the coding agent, right? And so there's a lot of studies that have been done that have shown like even if you are using the exact same model, you're not improving the underlying model or tool, you can go from a 6.7% pull request acceptance rate to almost 70%. And the only thing is to harness. So building in your strategies around context curation and validation and your approach for planning, right? Like we we'll talk about all that today when we cover building harnesses with Archon, but it's a big deal. Like uh maybe you guys heard of Stripe Minions. This went like super viral last month because Stripe they built their own internal harness. It's kind of like a more powerful version of the Ralph loop that allows them to ship 1,300 AI only generated pull requests every single week. And like Claude code itself is starting to build a lot of of harness into the tool. So not just calling the coding agent um you know calling the LLM with the coding agent but how can we like orchestrate many different cloud code sessions together. So like claude code has support for agent teams and they're doing a ton with sub aents right now. So when they had their source code leak last month, um it it was shown that like 60% of the code is still like wrapping the the underlying model itself like Sonnet and Opus and Haiku, but then 40% of their code is with these more like harness features like agent teams. And so all that to say, it's the direction that all of these companies are heading where they're building harnesses. The coding tools themselves are building this. All of the biggest companies like Stripe and Shopify and AWS, they're all building their own internal harnesses. But the problem with all these harnesses is they're not open- source and they're not custom to you. What if you want to take your software development life cycle, your process for working with AI coding assistants and what if you want to package it up into your own harness? Well, that is the value proposition of Archon. Archon is the harness builder. So, for the first time ever, we have an open- source platform that makes it easy for you to build your own harness. Up until this point, you either had to build something internally like Stripe did, but obviously that's a massive amount of effort, or you just had to use a harness that's already out there like the Ralph Loop or BMAD or whatever it is. And like, yeah, those tools are very powerful, but they're not custom to you. And you you guys know if you've been following my content that uh I'm always a big proponent of like build it yourself. Take inspiration from what's already out there. And I'll even show you what it looks like to build something like a BMAD or GSD harness in Archon because we can take inspiration from the beautiful minds that are out there but still make something that works how we want to work. And that's the unlock that I have for you guys here with Archon. And um the other thing that I want to cover here is um you know everyone already has their own skills and commands and rules. So I'm not I'm not expecting you to like start from zero. I know that you already have a process that you built around your AI coding assistant. Like you have skills for validation. You have commands for planning and maybe you have your PRD template whatever that might be. And so it's not like Archon replaces what you already do. It's that Archon allows you to package everything together into a workflow that combines your skills and commands, right? Like the whole idea is before you have a harness, you have your commands and skills and you have to remember the order that you use them. You have to work between different AI coding sessions because you definitely don't want to do your planning in the same session where you do your implementation because your coding agent builds up a lot of bias. But if you don't have a harness to connect those steps together, you have to be the one to orchestrate that. I call it shephering, right? Like you you go through some kind of PRD process with your coding agent. You create a PRD and then you're like, "Okay, good. Let me go over to a new Cloud Code session or a new codec session or whatever and let me go and create a plan for the first phase." And then you get your plan and then you go and you create a new session and you go into implementation and then you have a new session where you do a review on the pull request or on the code whatever it is. And so you're still even though you have your commands and skills and things to automate different parts of your workflow, you still have to walk the different coding agent sessions through each one. And Archon is kind of like the next evolution of that. It allows you to run longer tasks but still keep yourself in the loop. And so I have an example here of just what an archon workflow can look like. And and by the way, if you if you did watch the video on Wednesday, I am repeating myself a little bit here. So I covered this diagram in the video, but uh just consider this a refresher if you watched it. And I just want to make sure that for those of you tuning into this live stream who didn't watch the video, I can like give you a really solid overview of what Archon is. Um, so yeah, here's just one example of the kind of workflow you can build with Archon. And uh, you'll have to excuse the the images are like not rendering right now for some reason for some of the icons, but my point can still be made here. Uh, but yeah, so anyway, with Archon, you obviously have some kind of trigger for your workflow. So, traditionally without a harness, it would just be like sending a prompt into claude code, right? Like that is your trigger. But with Archon, there's a quite a few different ways that we can use it, and I'll I'll show you guys that today. We have the CLI so we can have our cloud code or codeex whatever um instance like trigger an archon workflow so we can dispatch work to delegate behind the scenes so we can do a lot of work in parallel. I also have a whole web interface and uh I'll definitely show that off today as well. Uh that's the wrong link. This is it. So we have the whole web interface where we can manage our workflows and we can uh kick off workflows uh from the web UI directly. And uh so there's basically like a a coding agent sitting behind the web interface. So we can ask it to do work on our different repositories that we have registered with archon and it'll automatically route the request. it'll pick the right workflow and it will dispatch it and we can do a ton of workflows in parallel if you want as well. So I'll I'll show you all of that today. But we have the web UI and then we even have different adapters so that you can for example talk to Archon directly in Slack. So you can say like hey there's a GitHub issue for um this repo go and you know handle that issue. I want to see a pull request in the end with a fix for that issue. And you can do that through Slack. And we have different conversations that you can manage through different threads in Slack. So for every single platform, we support parallel execution. Archon handles work trees and isolation under the hood. So you don't even have to worry about it. That's one of the other big unlocks with Archon is how it supports working on things in parallel. And so I can go into my clawed code and I can have it use the CLI to fix eight GitHub issues at the exact same time. and they all run in different work trees so they don't step on each other's toes. They don't override each other's changes and we don't have to deal with merge conflicts just to get the pull requests created. It's really powerful. And so we start with our trigger and then um again this is just an example of a workflow we can create. So we could go like into planning mode. So maybe there's a new feature that we want to build. We want to start by going through the planning process with our coding agent. And so we have a step in our archon workflow where we are prompting our coding agent like here is the feature we want to build. Now help me plan like do research, do codebase analysis, whatever that is. And when in archon we can add in human in the loop. And so we can have essentially a loop here where we give feedback to have the coding agent revise the plan until we approve it and then it moves into the coding stage. And we do this in a brand new coding agent session because your planning session can get pretty bogged down and you can build up a lot of bias over time. And so you want to produce an artifact that you send into the next node for implementation. If you're in the Dynamis community, this is the piv loop. You know what I'm talking about. I've covered it on my channel as well. The plan, implement, validate. And we used to have to do that between different coding agent sessions, but now we can package this all up as a single archon workflow. And then after the code is done, then we go into the testing step. And this is another one of the very big value propositions of archon. Our workflows do not have to be just prompts to a coding agent. Sometimes there are steps that we want to run deterministically. We want to take the control away from the coding agent to make sure that our process is followed to a T. If you've used any coding agent for a good amount of time, you know that like sometimes you'll tell the coding agent run the tests after you write the code and it won't listen to that. It's so frustrating. Or it'll do some of the testing like unit testing and linting, but it won't do the endto-end testing. It's so frustrating. And so what we can do in Archon is we can have certain steps of the workflow where we're just running code like we're doing some kind of context pulling or we're running our tests like we're doing right here. We're guaranteeing that that happens after the implementation and then if there's any failures, we'll prompt the coding agent to fix those things. So we have like a little bit of a feedback loop as well built directly into Archon. And then after everything passes and the coding agent figures that it's done, then we have the human approval. And so even though we are building longer running tasks with archon workflows, we're not taking ourselves out of the loop. We can inject oursel wherever we want in an archon workflow. So no matter how you typically work with your coding agents, if you don't trust it that much and you want to validate it every step of the way, you can do that if you want. We have support built in to the web UI, the CLI, every single adapter for human in the loop. And that's one of the most important things because a lot of times when you have these harnesses, especially like the Ralph loop, for example, the Ralph loop went viral a couple of months ago, but to me it felt like vibe coding, right? Because you were giving it a and it basically an entire PRD, like many different phases of work, and you would just have a coding agent rip through everything. And the problem with that is if the coding agent makes a mistake in the first iteration of the Ralph loop, that issue can kind of propagate and like blow up from the rest of the loop because the coding agent is going to through each loop build on top of a code base that's already wrong, right? Like not aligned with what you actually want to create. And so the issues just compound on themselves. And so the idea that I wanted to be uh very confident in for Archon is that it's not just enabling vibe coding that we actually have like deterministic steps that enforce our process. We have human in the loop, right? And then we have the pull request at the end and then we can review that ourself before we merge as well. And so yeah, that's that's sort of I I like to call it the hybrid secret for Archon. And um this this sometimes rubs people the wrong way, but I actually think it's smart to take as many decisions from away from the coding agent as you possibly can because they're non-deterministic. They don't make the same decisions every time even if you give it the same prompt. And so there's a lot of inherent risk with that. The biggest reason why a lot of developers and companies are hesitant to adopt coding agents is because they're unreliable by nature. And so Archon is the harness builder that allows you to take the process that you consider reliable and build it into the way you work with coding agents. And so we have different nodes like if you have your testing strategy, if you have your strategy for like pulling information from Confluence, like whatever steps you have that like you want to have performed every single time, you build those nodes into Archon. And then the rest of the workflow is still going to be like you adding in your commands and skills and sub agents. Like everything that you already have, you can build in. So you're not losing anything either. That's another thing that I want to be very clear on here is that you don't have to replace how you already work. Archon just allows you to package it up, right? Like that's the goal of a harness builder. So I'm I'm so excited for this and I'll I'll actually like install it from scratch with you guys today as well. So, uh, right here I got the link to Archon. I'm going to go ahead and drop this in the chat. So, if you guys want to, um, try it out right now, even like install it along with me, I would highly encourage you to. It's very easy to install Archon because we can ask our coding agent to set it up and I have an archon skill that it loads automatically and it'll walk you through the entire process even installing the dependencies for you. So I'll show you that live in a sec. But yeah, it's so easy to get it installed. Um yeah, so one other thing I want to show really quick. So this is the readme for the new version of Archon. I want to show what a workflow actually looks like. So, this might look a little bit intimidating, but uh don't worry, you can use your coding agent to help you build workflows as well. I'll also show you that. Um, so this whole like YAML structure, it's it's quite beautifully simple, honestly. And uh but like even even so, like when you're trying to package up your entire workflow, it can start to look a little intimidating. So it's really nice to use a coding agent to help you define these workflows. But just an example here. So within the diagram here, I showed the whole like piv loop workflow. And that that workflow can be summed up with this right here. So this is a a kind of a bit of a simplification just so it fits nicely in the readme, but it gives a good idea here. So you start with the node for your planning and then you go into implementation and you can see that we have we support loops in archon as well. So, uh, maybe I can even go into the UI. Let's see if I have it run with the loop. I want to give like a demo of like what it actually looks like. Yeah, here we go. So, like we have we support loops in Archon. So, by the way, this is what the logs look like. When you invoke a workflow and you view the logs in the web UI, you can see like all the tool calls that your coding agent is making behind the scenes. You can see like the the node flow and like where it's currently running. So like we have a loop right here that has like a certain number of iterations. And if I go to like a more fancy one like a GitHub issue fix, we can see like you can get pretty comprehensive with the workflows that you define. This is one of the the breadand butter workflows in archon uh the fix GitHub issue. So you can throw this on any GitHub issue in any repository and it works through this entire process of uh you know classifying the issue. Is this a a new feature we have to plan or is it a bug we have to investigate? And then it'll do some research. It'll fix the issues after investigating and then it will validate and then create a pull request and review it after. So it's like super comprehensive workflow and and yes having this many steps does take a good amount of tokens. But another really powerful thing you can do in archon is specify the model the at the individual node level. So when you're classifying or investigating maybe you only need to use haik coup and so it might only be the case that like a single node like the fixed issue this is the only one where we'd want to use opus or we'd want to use high reasoning GPT codeex for example and so you can make things very token efficient by determining at each at each individual level what model do we want to use and the other really powerful thing about harnesses like I showed in this diagram here is you get insane results building a harness on top of a model. So the harness elevates the model. I've had better results using archon with sonnet than I have using opus by itself in cloud code. And so uh another really cool thing is like you know this um archon kind of comes with good timing here because anthropic has made their rate limits a lot worse for clawed code recently. It's really unfortunate, but it's forced me to like start using Sonnet more for my coding because I hit my rate limits so incredibly fast. But with Archon, I feel like I'm not really losing the code quality, like the output quality because the workflows, they package up such a comprehensive process and like using this whole thing with Sonnet is still cheaper than like asking Cloud Code to fix an issue by itself with Opus because Opus is just so much more expensive. So anyway, I got off track a little bit showing you guys the web UI here, but yeah, so we have the loop like we can, you know, implement a plan task by task in a loop and then we run the validation. And the important thing is this is no AI. It is deterministic. So we're guaranteed that our validation runs. That's powerful. And then we run the reviews afterwards. And then we have some kind of approval process with a human in the loop before we create our final pull request. And because we have archon as a CLI and a skill, when you have it loaded into your cloud code or your codeex, all you have to do is tell it to use archon. And that like literally that's all your request has to be and it'll automatically dispatch like create an archon workflow. So it'll run like let's say for example this idea to PR workflow. It'll create the work tree under the hood so you can keep working on your codebase in parallel and then it goes through the different stages and you can have your coding agent monitor the workflow and or monitor it in the web UI like I showed right here. So like obviously this is a completed run right now. But uh if this was in the middle of executing you could like see the logs come in in real time and see like you know like what stage of the workflow the coding agent is currently on. And as far as as which coding agents we support right now, we have support for cloud code and then codeex is almost done. And then also we are working on uh or we want to add in support for other coding agents as well. So like right now it's claude and codeex but uh we have a priority item right now to add support for pi as well. So pi also has an SDK. Uh we're also interested in AMP and open code. I mean really like archon, remember archon is the layer above the coding agent because it's the harness builder, right? So we don't really care about what coding agent you're using under the hood. We just have to build a little bit of support for like calling the SDK for the coding agent. So like Codeex has the SDK, Claude has the agent SDK. That's what Archon uses under the hood. So when you use Claude with Archon, it is running Claude code. It's just running it programmatically through the SDK. And um so you can you are allowed to use your anthropic and codec subscriptions with Archon. You don't have to pay for API credits. Um and and that's that's a very important thing because a lot of people right now are getting their anthropic subscriptions banned when they use it with Open Claw and Open Code. But the problem with those they're third party harnesses. They're kind of doing a workaround to use the subscription. And that's against the Anthropic terms of service, but Anthropic has made it very clear. A couple of their team members like posted on X saying that like you are allowed to use your Anthropic subscription with the Claude agent SDK as long as it is for personal use. And Archon is for personal use, right? Like you're running it on your computer. You're hosting it yourself and there aren't other people using your subscript subscription through a production deployed agent. So it's a different story. If other people are using your subscription through a cloud agent SDK agent you have like deployed to some production platform then that's against the terms of service. But if it's a an application you're running yourself and is using the claw agent SDK then you are allowed. So I've been using my subscription with Archon for you know months and months now. And the same thing with my second brain as well. And so they've made that very very clear. I don't have the exact tweet up right now, so I can't show you the exact thing, but uh Boris Churnney, he's the creator of Claude Code. He um he clarified like he made it super clear like yes, you can use your subscription for personal use with the agent SDK. So, we're good. And I get that I get asked that question all the time as I'm doing my second brain content on YouTube and I've you know started showcasing Archon and it is a fair question because um yeah like people are really nervous about getting their subscription banned but you are good with Archon and yeah I see some things in the chat here. People are excited for the Pi support. Uh yeah I'm excited for that as well because then it you will have like support for pretty much running any model that you want with Archon. All right, cool. Um, all right. So, yeah, I'm going to go ahead and uh answer some questions in the chat here, and then we'll get right into installing Archon. So, I have an instance already spun up uh in the cloud. I I installed Archon from scratch on my computer for the video on Wednesday. I don't really want to like reinstall it on my computer because I already have some things going with it. So, I'm going to reinstall it on a Linux VPS that I created just in Digital Ocean. Uh, but the installation process is going to be the same pretty much no matter your operating system. So, whether you're installing it on a VPS or on your Linux, Mac or Windows system, it's pretty much going to be the same. And the readme has good instructions for that. And I'll I'll walk you through it right now as well. But yeah, before we do that, I'm going to uh switch here to my full frame. Uh, let's let's chat a little bit. So, I'll I'll pop up some questions in the chat here and uh spend some time for a Q&A. All right. Uh Jared said, "He said the magic words, customize BMAD for inspiration in a custom workflow." That's exactly right. Um so it works the way you need it, just the way I need it. This is fire. What I've been looking for. Yeah, I appreciate it a lot. Um, and that exactly like that's that's the thing is you can just like fork BMAD and you can just run it and change it yourself, but that's a lot more involved than creating an Archon workflow. I'll show you in a little bit what it looks like to customize um a workflow taking inspiration from something like BMAD. I'm going to use GSD as an example because it's a bit simpler and easier to do, but you could do the same thing with BMAD. Um, all right. So basically, we could call archons stripe minions but open source. Exactly. Yep. And I'd even go further to say that like stripe minions is just a single harness. Archon can allow you to build anything like Archon allows you to build stripe minions but for your company or yourself. Yeah. Um, can a node be simply an execution node? No AI model used? Yep. Yep. So we have support for running uh bash, python and typescript scripts. So anything like any part of the workflow where you're like I want this thing to happen exactly like no AI model to mess it up then you can run it as a node in archon. Yeah. Uh where does this differ from n? You know uh that's a really good question actually. Here I'm going to switch uh back to my scene here. I'm going to share my screen because if we look at the the builder here and u sorry I'm going to the wrong tabs. We're actually adding support soon for a visual builder. So you can like connect the nodes like this. And so it is going to be kind of similar to N8N. In fact, in the readme here, we say think N8N but for software development. And so for those of you who use N8N or have used it in the past, this might actually click really nicely for you is like N8N doesn't really have direct connections with cloud code and they don't have things like workree isolation support, right? Like you don't use N8N for AI coding. You use it to build automations for your business, whether it's like LLM workflows or not. But u Archon is going to allow you to build kind of like n workflows, but specifically for AI coding. So you're stringing together these coding agent sessions and deterministic steps like bash and python scripts. And it's for coding processes. Uh, and so like there's a lot of things we have built in behind the scenes with Archon for how it integrates with our different coding agents and handles work trees and things like that that N8N doesn't have at all. So like there's no way you could build this kind of thing in N8N. You're you're not going to be able to build a coding agent harness in N8N or at least it'd be very difficult and not really what the tool is meant for. Um, so this is a very different use case, but you can think of it like N8N for AI coding. So yeah, I appreciate you asking that. All right. Um, how can we know that the plan step is complete? Do we have human an approval gate for that? Uh, yes. So, you can have the coding agent decide itself that the plan is complete or you can make it so that you have to approve. And so, like going back to the diagram here, this step right here is what you're talking about like planning. And so what it does is it'll output some artifact and you can have I know that I only show the human approval gate here, but you could like add that as a node right here as well. So like you get to look at the artifact and it'll like give you a summary of it or it'll give you like the full file. So you can like go through the markdown if you want and then you can give feedback. So you can say like hey you didn't do enough validation, right? So or like you didn't add enough u planning around validation. So like go back edit the plan and then let me review again. So you can add that for any step in Archon or you can have it just decide itself. Like if you want it to be a little bit more hands-off, like you want to do something like the Ralph loop, which by the way, we have a Ralph loop workflow built into Archon for you to use out of the box. Um then you don't have to have the human in the loop. Like you can have it kind of like iterate by itself and kind of critique itself and then decide when it's ready to move on, which obviously that's a bit more or a lot more non-deterministic, but you can do whatever you'd like. And um speaking of that, actually like workflows in Archon, we have a lot of Archon workflows that come shipped with the platform. So when you install Archon, all of these workflows here are ready for you to use immediately. So you can build your own. If you want to create your own harness, build your own workflows, you can. But if you just want to poke around with Archon initially, I have all of these ready for you guys to use. So we have like a human in the loop interactive PRD to like walk you through creating PRDs. Uh we have the whole like plan to pull request. We have the Ralph loop one if you want to do the Ralph loop in Archon. It's actually like a beautifully simple workflow. Most of it is just prompting here, but it'll walk you through like creating the PRD. It'll validate it and then it'll go through the whole Ralph loop and like manage the state through uh like JSON and markdown files just like the Ralph loop does, the original Ralph loop. Uh what else do we have? We have the uh GitHub issue fix. This is the one that I use the most out of all of the workflows in Archon because I'll I'll throw this on the issues that we have in Archon. Like I'll I'll say like, "All right, Claude Code, uh, we have a few people that have just opened up issues for Archon. We got, you know, like 10,82, 80, 76, 72. I want you to spin up four GitHub issue fix archon workflows in parallel and then monitor them and let me know when they're done and I can review the poll request." Or I could even have it like run the validate PR poll request after as well. Um, so yeah, like I said, I'm always using Archon to build Archon. All right, visualization is fantastic. I appreciate it. I assume you're talking about the the web UI here, but yeah, there's a lot of work that we've been putting into the visualization here. Um, can I use this with open code? Uh, yeah, so not yet, but we want to add support for open code. So pretty much Archon is going to be able to be integrated with any coding agent that supports an SDK. So like like I said with Cloud, we have the agent SDK. Codeex has their SDK, PI has one, Open Code has one, and AMP has one. Uh Gemini CLI does not. That's another one that I wish I could add, but they don't have an SDK. Um now you can just run the coding agent in headless mode, but uh it's it works better to use the coding agent programmatically. So this entire codebase is Typescript almost entirely TypeScript because that's the language most of the SDKs are written in. So the cloud agent SDK has both a Python and TypeScript version but Codeex is only TypeScript. So that's why I decided to go TypeScript for for this codebase here. Um and in the end like the actual language you pick doesn't matter a ton because coding agents can just rock everything, right? In fact, Typescript is even a bit better for coding agents than Python because um it has the type safety built right in. All right, cool. Um All right. So, yeah, there are so many good questions in the chat here. It's going to be hard for me to get to everything, but I'll answer a couple more here and then I'll get on to the demo where I'll I'll install it from scratch with you guys and show you how I use it on the day-to-day. Um, why have you made this open source? That's a good question. So, open source has always been a really big part of my ethos. So, as I created started creating YouTube content um, in 2024, I I really just had a passion for sharing my knowledge and everything that I'm diving into with the whole world. And open source is my way to share it the most I possibly can because otherwise if I close source it I'm going to tell you guys about it but then you won't really care because it's either going to be some paid product that you have to shell out a bunch for or it's meant for enterprises or whatever and then like no one is going to care about it. So, open source is my way to get the most eyes on it, which it also is helpful for me because then I get the most feedback for it. And um obviously like for my channel, it helps because then everyone has a reason to care about it. If it's not something that's open source, I can share what I'm building, but then maybe if you want to like follow along with my journey, that's interesting. But otherwise, it's like nothing you can really try yourself. So, I feel like it just you can be kind of like a brick wall you hit. if I make a YouTube video on Archon, it's like look at this cool thing I built and then you can't even try it. It's like what's the point? U so definitely like with YouTube being my primary like platform for sharing things with the world like what I share has to be open source in my opinion. So yeah, it's a fair question though. All right. Um yeah, so another person asked about this in NN. So, I talked about that already, but yeah, I appreciate you guys asking about that. Uh, will it include the GitHub CLI, GitHub Copilot CLI in the future? So, if they build an SDK, yes, but I don't think they have an SDK. Um, oh, wait a second. Do they actually look at this? When was this released? They Oh, okay. So there is a SDK. So actually we could integrate GitHub Copilot with Archon as well. That's pretty cool. And yep, they support TypeScript, which is what we would need for Archon. So yeah, this is yet another one. And okay, here's the really cool thing. I I haven't really talked about this yet too much. I mean this gets more technical but um let me let me tell you there is so much effort that I put into architecting the initial codebase for archon before I I ever wrote a single line of code. So I have like a sort of like generic interface implementation for every single adapter and every single coding agent. So when I built the initial version of archon I supported claude and I supported telegram. So like Telegram was the way to talk to it remotely and Claude was the only coding agent but I built it in a way where it wasn't like super coupled with that specific tool like Telegram or Claude. And so when I asked Archon to build support for Slack as well as Telegram or or GitHub we like support you can like talk to Archon directly and GitHub issues as well. It just one-shotted it like I didn't even have to iterate. it built it perfectly and then when I asked it to build support for codeex like following the pattern that I did for claude it oneshotted that as well and so if you wanted to create a poll request adding support for GitHub copilot you could you could literally oneshot it because the documentation is there the coding agent can reference that if you have like claude code open up in the archon repository or codeex and um and then also like it can just copy how we already have it set up for an existing coding agent. So we have Archon set up in a way where the codebase is very easy to evolve because everything is set up as like super easy patterns to understand like the coding agent can understand very easily like here's how I add a new coding agent here's how I add a new adapter uh whatever we want to do to evolve the system um can workflows be told to obey token rates and limits so I think that's actually something we have an open issue for cuz there's not a way to like set a max budget for tokens, but it would be pretty easy to add that like on a per node level. It's like I want you to stop if this is taking more than 100,000 tokens cuz this that definitely means that like the coding agent is going off the rails here or whatever. So, we don't have support for that yet. But um I think I mean I I don't really want to like go on a hunt here and try to find this exact one, but uh there are there is definitely an issue that we have out for for that. Let's see if I can find it. So mo most of these issues that we have right now are actually created by uh Raasmus. So like I said, he's one of the guys that's been helping me an insane amount with Archon. So most of these things are like just us kind of listing out things that we want to uh improve in in Archon. Um, we had to port over. So, we were working on kind of like a private repo that was like just for the Dynamus community at one point. So, we had to port over a lot of the issues. I don't know. We might have changed the names for some of them, but that's definitely something we have on our radar. Um, yeah, not sure if we I can't find it exactly right now, but yes, that's one of the things is just like all of the different parameters that we have in like codecs and cloud code. We want to make sure that we can support those. So you can build it directly into the configuration for each node of an archon workflow. All right. Yeah. And so yeah, one thing I I uh want to mention really quick is like when we were first working on Archon, we were doing it like as an internal project in the Dynamis community. So we called it the actually I still need I still need to archive this repository here, but we have the remote coding agent. It's funny because Archon, the new version of Archon started as a a resource that I built for the Dynamus Agentic coding course because it originally wasn't a harness builder. It was just a platform that allowed you to talk to cloud code or codecs uh in a remote environment like Slack, GitHub or Telegram like I was talking about earlier. So that's how it started and then it evolved into this beautiful thing where now you can like build any AI coding workflow as an archon harness. Uh but this this is like the origin of archon. So it's cool for everyone in the Dynamis community. You guys got to like see it evolve to the point where it is now and obviously you got early access to it. Another thing is um within the Dynamus community, I am going to be doing a lot more workshops the next couple of months, like getting like really deep into using Archon, like building custom workflows. I'll show you guys more like how to build your own harnesses. Um it's it's always the place to be if you want to like be a part of Archon and get the the inside scoop on how to use the tool the best and like the evolutions that I'm doing to it. U so yeah, I just want to call out really quick for Dynamus. I'm going to put a link in the chat here. Uh I actually have a little live stream special for you guys for Dynamis. So it's uh 10% off the uh public price for the community. This discount here is going to go away uh by the time our live stream is done here. So it's a special for literally just this live stream. So, if you like what I'm working on with Archon, if you want to be a part of of this and um also all the other course content that I have in Dynamus, definitely check this out. I put the link in the chat just now. So, another big thing that I did in Dynamus recently is I did a 4hour boot camp on building your own AI second brain. So, I took the entire second brain that I built for myself that literally saves me 20 hours a week and I showed you how to build it from scratch. So, I did a a live workshop and I'm also turning this into the third course for Dynamus as well. We also have the AI agent mastery and agentic coding courses and I referenced the Agentic coding course already because that was the origin of the this new version of Archon. So, yeah, lot a lot of value packed into Dynamist. I do weekly workshops as well. And so, that's where I'll be doing some more stuff with Archon if you are interested. So, all right. Uh, with that here, I'm going to go ahead and show you guys how to install Archon from scratch. And, uh, like I said, I'm going to be doing it on a VPS just because I don't want to wipe my installation on my computer again. I I already reinstalled Archon from scratch um, four times this week as I was testing things to get ready for the open source release. And so I'm going to install it on the VPS where I'm going to build my dark factory. This is the exciting like last part of the live stream that I'll be covering with you guys here. Um yeah, I'm I'm actually pretty stoked for this. I don't know if you guys know what a dark factory is. Um it's kind of like a a term that was coined in the last Well, actually it was a a term that was coined in the late uh 1900s. Uh that sounds weird. Like 1990s, I think. Like the idea of a dark factory is um you have a factory without lights because it's robots running the entire thing and then recently people have been talking about like dark factory as it relates to code bases and basically a dark factory is a code base that self-evolves like AI is the only one writing code ever on the codebase and so an experiment that I want to run I'm giving you a little bit of a teaser to what I'll talk about at the end of the workshop here an experiment I want to run is a public dark factory factory codebase where every single evolution of the codebase like every pull request, every release is managed by Archon workflows because we can build our process like we can define exactly how we want to manage issues and pull requests and releases. We can define it as archon workflows. So, we basically use Archon as a dark factory harness, which sounds kind of it sounds silly, but I'm actually like really excited to try this as a um kind of like public experiment here. Like I I literally wanted to get to the point where like anyone can create an issue and then I'll have Archon like figure out is this an issue that we should address for this codebase and then it'll handle it automatically all the way to like pull requests and reviewing and merging into the main branch. So, we'll talk about that, but obviously we got to get Archon uh spun up for the first time here. So, I'll show you guys the installation. I'll show you what it looks like to run workflows with Archon, and then I want to build a workflow with you guys, and then we'll do some of the dark factory fancy stuff at the end. All right, so I'm going to go into the read me here. So, I'll put a link to Archon in the chat again. If you guys want to follow along and install with me on your machine or a VPS, if we scroll down to the get started, this is where we're going to work right now. So, literally all you have to have installed before you run Archon is your coding agent and the GitHub CLI. In fact, I list bun as a prerequisite, but the setup process is going to even install this automatically if you don't have it yet. So, I do list cla code as a prerec. You can use codeex as well that's also supported with archon. It's just not quite as stable right now as cloud code. So I'll definitely be updating the docs as I address that or as we address that. But then obviously the GitHub CLI is an important uh dependency as well. You don't need the GitHub CLI for every Archon workflow, but um yeah, being able to work with GitHub is a very core part of Archon because most workflows are relying on having the issue or pull requests be like the starting point, right? Like reviewing pull requests or fixing GitHub issues. Most of the time when I'm working with Archon, it's it's dealing with artifacts in GitHub essentially, right? So that's why I have that as a prerequisite. So once you have those things installed, um, we have the binary. So we're working on making it so there's like a single install script. So you can do this if you want. I'm just going to show you that my my approach of like cloning the repository and setting up from there cuz that's what I'm more comfortable with. This is like a newer thing that we're working on to make it like even easier to set up archon. So I'm going to install it this way. So I'll I'll copy this command to clone the repository and I'll do that within my VPS here. So there we go. Clone Archon and then obviously change my directory into Archon. And then check this out. So I'm going to run in dangerously skip permission mode just because I don't want to have to deal with approving things right now. Open up the folder. Uh yes, I accept. There we go. All right. Now watch this. All I have to do is say setup archon. I don't have to say anything else. It's going to walk me through the entire process. So if you have the prerex and then you clone the repo, you just go into your clott codeex and you say set up archon and that's it. So first it's going to see like what we already have set up. It's going to realize that we haven't set up anything. And then what it should do is it should load the archon skill. So we have this skill that like walks it through how to help us with claude or with the the whole setup of archon with claude. All right, I guess I have to wait for it to to work here. And by the way, if we see it um I just did like control O to see the output here. It's just like understanding the codebase. I'm actually surprised I didn't load the archon skill. Um you're in the Let's see. What is it saying here? No. All right, hold on. Load the archon skill and walk through the setup. I've actually never had to do this before, but it uh for some reason didn't load the archon skill. So, I'm just going to tell it to do that, but we're still going to get the same effect here. It'll be super easy to go through everything. All right, there we go. So, now it's reading the setup guide. So, this is like a part of the skill that uh tells it how to walk us through everything. So, it's going to check all the prerequisites like making sure we have git and bun, things like that, which we already do on this machine. Um, there we go. So now the first question that it'll ask you in the setup is where like what's the repository that you want to use to work on with archon, right? So like when we use archon, we want it to invoke workflows on another repository because we're going to use it to work on something else. So that's why it says this should be your own project, not the archon repo. And so I can either clone a repository from GitHub or I can just give it a local path if I want it to work on a a project that I already have installed on my machine. So number two is actually probably what you would end up doing because usually there's already something you're in the middle of working on that you want to use archon to like build a harness around, right? Um now since I'm on a VPS, I am just going to clone something from GitHub here. So, I will select that. And then it just says like, "Please provide the repo URL." Um, I need to actually find one here. I'll I'll just do Let me open this up. I'll pull some like random um let's see. Let's just do this one. I'll just copy this rep. I just need kind of like a random one here to register. So, what this is going to do is it's going to register your first repository with Archon. So whenever you um run the Archon CLI on a repo for the first time, it will register. So like Archon has a database under the hood or behind the scenes that like keeps track of the projects that you're using Archon with and like all the conversations you've had where you've invoked Archon workflows on those code bases. So you do the automatic registration that way. And then also in the web UI like I showed earlier, you can register projects this way too. So you just click the plus icon here and then you can give it the GitHub URL or the local path. So also in the web UI you can register your repos. And the cool thing is for all the projects that you have registered in the web UI the agent automatically understands. So if I say like what projects and workflows do I have the archon agent that runs in the web UI either using cloud code or codeex it it has the context injected for all of the archon workflows it can invoke and the different projects that it can invoke it in. And so when we say like, hey, I want to fix this GitHub issue for this project, it will know like, okay, let me use the fix GitHub issue workflow and I'll route it to the rag YouTube chat repository. And the the web UI is one of the things that we can spin up once we go through the setup here. So first it asks what platforms do you want to set up? So the CLI is always included by default. I can also set up uh you know like Telegram. you just do, you know, like um enter to select or unselect. Uh for this, I'm going to keep it really simple and just do the CLI. Um yeah, but you you can set up like all the adapters that we support in Archon right here. So you specify the ones that you want and then in a little bit it'll go through a process where we can give our API keys, but it's a separate process because we don't want to just send our API keys directly into a coding agent or an an LLM. So I'll submit these answers here. So I just want to set up the CLI so I can run workflows there. So the CLI and the web UI obviously don't require you to have any additional parameters or API keys. So they'll just come they'll work right out the gate. So then what it does here is it creates archon as a global command. So that way we can just run you know like archon uh workflow run whatever. So we can use the CLI to invoke workflows. But trust me you're never going to do this yourself. You're just going to have your coding agent run archon workflow. So you don't really have to understand the CLI yourself. That's the beauty of having an archon skill is your coding agent can load the skill and then it knows how to invoke the archon CLI to kick off workflows for you. All right. And so now what happens is it helps you configure your credentials, but it runs this in a separate terminal because we don't want our coding agent to see our API keys. That would be a huge security risk. And so it uh it will automatically spin up a new terminal for you to go through the setup, but depending on your operating system, it might not there might not be support to like automatically start a new terminal. And so uh you might need to just use do this yourself. And so for me, because I'm running in a VPS, there's no like automatic terminal spin up. So I just have to connect into the machine again. So let me do that. So, I gotta uh remember the path to my SSH key. Uh, there we go. Goodness, I can't type today. Gosh. All right. And then, um, I forgot the IP of my machine. Shoot. What is the IP address of my machine here? I'm going to pull this up on another monitor here. Um, all right. Pull this up. There we go. Okay. All right. So, SSH in and then I will go to uh the path here. Dark Factory Archon. Wait, that's not it. Dark Factory. Uh oh, yeah, capital A. Okay. All right. So then all you have to do in a separate terminal is run the archon setup command and it it walks you through this here. If it doesn't spin up the terminal automatically, you just do that yourself. And now we just go through the setup process. So I'll zoom in on this here. So first, what database do you want to use? SQLite is the easiest to set up. And so I recommend that you can use Postgress though if you want to have an external database you connect to. Uh which shoot I accidentally entered that. So let me go through the setup again. So, SQLite and then here's where it asks what coding agent you want to use. And so, these are the two we support right now. Like I talked about, we want to add more as well. So, space to select and then enter to confirm. And then it asks, how do you want to authenticate with claude? And so, there's three options here. We can give an ooth token like if you want to just run, you know, the claude like setup- token command and get an ooth token. You can give your API key, which I wouldn't recommend because it's going to get expensive. And then like I said, we are allowed to use our enthropic subscription with claude code with the claian SDK and archon. So I'm just going to use my global off. So on this instance, I've already authenticated with claude. If you use cloud code a lot and you're installing archon on your machine, then the authentication is already set, right? Like you don't even have to set up any other environment variable. And then it asks what platforms do I want to connect? As in what ones do I want to enter in an API key for? I'm not actually going to I mean I guess I'll just do GitHub right now just so I can show you one of these. So you do um space to select and then enter to confirm. And then what it'll do is for each of the platforms that you select that you want to install Archon with. This is very similar to the um Open Claw setup. If you guys have installed OpenClaw before is for each one of the platforms it'll like give you instructions like here's how you get your your GitHub personal access token. And so I'm going to u off camera obviously go ahead and uh get that and copy it. So let me go to there we go. So I'll paste it in because it automatically hides it which is good. I would want to show that on the live stream but yeah it gives you instructions for how to do that. It'll be the same for every single one of your platforms that you configure. And then another thing obviously for the sake of security is we for each of of the platforms that we set up like GitHub and Slack and Telegram we want to have a commaepparated list of users that are allowed to invoke archon because if I have archon running on a public repository I don't necessarily want anyone to be able to just say like you know at archon fix this issue because then it's spending my tokens and it's not me invoking it. So I'll just say like this is the only user that's allowed to use it. And then you can change the mention name. So like in GitHub you do at@ archon and then you give it the request like that's how you talk to it. So I'm good with with that as the default. Um so I don't need to set up anything separate. And then the other thing is that also for that repository that we've we registered. So this repo that I found just as like a a random one. Where was it? Yeah, this one. So like I I gave it this to register as the first repository. Um we can also copy the archon skill into that project. And the the reason I want to do that is then I can open up my coding agent directly in that codebase and since the archon skill is there, it knows how to use the archon CLI. So that way I don't have to open my coding agent in the archon repo in order to work on another repository. Because as long as the archon skill is there, the archon CLI is a global CLI. So we can invoke it from anywhere on our machine. Like I can just open up my terminal right here and just say like archon, right? And then that automatically works uh because it's a globally registered command. But our coding agent only knows how to use it like use all the different commands and options if we have the skill. So I just want to copy it over into uh the codebase. So all right. And then uh the docs directory. We don't have to worry about that right now. And there we go. Our setup is complete. And so we go through all of this and then we go back here and we just say done. So like we finished and uh now it's going to validate all the credentials and make sure that we're good to go. And then it'll actually test the Archon CLI. So it'll run a workflow for us to make sure that everything is all configured properly. So we'll let that run here as well. All right. So there we go. Running a quick test here. So we can see that it is using the archon CLI. So thanks to the skill, it knows how to. You never have to worry about running it yourself. You just ask the coding agent to do so. So it's running the archon assist workflow and it is doing it on our uh repo that we registered, the first repo that we registered. And so it's just, you know, say hello, like a really basic test to make sure that it worked. And there we go. It's good. So, yep. I'll copy the skill over. I guess it asks us here as well. Maybe that's something to touch up. Uh, but anyway, so every single time that you invoke a workflow from the CLI, it's going to run as a background process. So, Cloud Code or Codeex like it has access to um the full logs from the workflow. So, it you can like ask it for a status if it's a longer running workflow or you can, you know, say like, "Hey, summarize what happened in the workflow." like it it's able to basically you know communicate with the workflow that it runs because all the logs are right there in the background process. So there we go our setup is complete. So it tells us what is configured and then it gives us next steps as well. So take a look at this. We are immediately ready to use archon in our codebase now and we can register it with any other codebase we want as well. So like I could just say like you know I'll go into my speech to text tool here and I'll say like use the GitHub issue fix workflow to fix issue number two on u XYZ repository right like I can send off this request and it will automatically if if I you know give it obviously the path to the repo here it'll use the archon CLI to run the GitHub fix issue workflow on this repo and then that also automatically registers that repository with archon so So it knows about it going forward if the repository wasn't registered already. And then the other thing is wherever I have the archon skill copied which if you want to copy it yourself in the archon repo it's just within.claude skills. So this and and I'll put a link to this in the chat right now as well. This skill which you can just ask your coding agent to copy it into your new like whatever repo you want to start using archon with. But this skill tells it how to use the CLI. Like this is literally the only requirement. So another thing is if you want to use your second brain with Archon, all you have to do is put this skill into your second brain repo and then it'll immediately be able to start using Archon workflow. So you can basically add Archon as the coding arm for your second brain. So you can create your own harnesses, your own workflows, and then you can tell your second brain to invoke it on whatever repo you you want. As long as you give it the path, and it loads the archon skill, then it knows how to use the CLI. And so for anything here, if it's like confusing like, okay, what repo do I open up or like how do I get the skill or how do I register projects? Like you literally just ask Archon and it knows how to do everything because the skill walks it through everything. So let me actually show you this here. So in this other terminal here, I'm going to um clear and then so it says I can change my directory into the claude memory compiler and then I can run claude to launch claude here. So I'll do uh the dangerously skip permissions again or I guess I don't here. I'll just have to type it out manually. So, claw dangerously skip permissions. And then, um, you can see that since I copied over the skill to this repo during the setup, I can just say load the archon skill. Not that you have to say this explicitly every time, but I'm just demonstrating that like we have the archon skill in this repo. So, now it's going to know how to invoke any uh workflow. And then within the repo here, okay, we actually have a couple of issues. Cool. Uh, this 6pm thing is very edgy. I've never actually seen this issue before, by the way. This is a public repo. Um, that's okay. Massive token consumption. Interesting. All right. Well, I'm trying to find one that's actually like um seed existing. Okay. Well, let's try this one. This is kind of random, but I'm just going to pick a random issue like number one here. So, like watch this. All I have to do is say, uh, I want you to use Archon to fix issue number one. That's it. It's so simple because it knows the workflows it has access to. It's going to pick the right one, right? Like it's going to pick the Archon fix GitHub issue. It knows how to use the CLI. Boom. That is it. And we have this full process running now. So Archon fix GitHub issue is running in the background. It's going to check on the progress periodically. And um Oh, hold on. The workflow failed because you're not logged into the GitHub CLI. Oh, that's a bummer. Okay, hold on. I guess I have to do that. I thought I already did the login here. Um, let's see. Paste authentication token. Hold on. I'm going to do this off camera quick. Um, I thought I already did that part of the setup, so it's kind of weird that it says, but I'm just going to try the login here. All right. So, yeah. See, it says I'm already logged into this account. I think Claude might be tripping right now. Uh, let me try resuming the conversation. Let's see. Uh, I logged in. Also, it says I already was. So, I am confused. There might be something else I forgot to or I messed up in my configuration on this machine. Um, let's see. But it's cool. like it can just rerun the workflow, right? Like we can just talk to Claude as we normally would and so it can use archon as a tool just like it would use sub agents or just like it would use skills. Uh it says it exited again. Um the error is actually from the claude code off the not logged in is coming from the claude code agent that archon spawns. Um the check cla Oh, I think I know what it is. I think it's because of the uh it's because of this specific repo. I have the cloud folder, the settings.json. If I just remove this, I might just do the demo on my computer instead of this VPS because I I think it's just this specific codebase that I have some like claw code hooks that are running. It's a whole thing. Oh, wait. Oh, wait. I know what's wrong. It's because I have this already set up to use Miniax M2.7 for the dark factory stuff I was going to show you guys. That's my bad. Ah, okay. I have to I have to demo this on another machine here. By the way, we were using Miniax 2.7 for everything. Um because I was getting some stuff set up ahead of time for the live stream here. Sorry guys, I'm complicating things more than I um than I need to because I I'm I have some other things prepared for you guys here. So, okay, here's what I'm going to do. I'm going to show you a demonstration by doing it right from Archon. So, um this will be better anyway because then I can show you guys the web UI. Uh which by the way, if you want to start the Archon web UI, all you have to do is go into the Archon codebase and say start the backend and front end of Archon. That's it. Um start the back end and front end of Archon. I guess my speech text got cut off, but that's all you have to do. So I hope that like the pattern is clear here for your setup for getting things up and running for running Archon. It just comes down to like the Archon skill guides it through everything all workflow execution managing the application super super easy. So within my archon here, let's go ahead and uh zoom in a bit. Let's say I just wanted to handle an issue. So this is going to be kind of meta because I'm using archon to improve archon. Uh, but like I said, you could do this on any codebase where we have the Archon skill. Um, so I'm going to find an issue. There's quite a few issues that have been created in the last couple of days because we're we have a lot of eyes on Archon right now. We're at 16.2,000 stars, which I'm honored, by the way. Um, okay. Uh, let's see. So, okay, this is a good one. So, chat UI fails silently when the Claude Oath refresh token is expired. So, this is issue number 176. So, watch this. I'm gonna go in this just like I was trying to do in the VPS. I just have things uh configured. We'll talk about the Dark Factory stuff in a bit because I want to use Miniax. Um anyway, so I'll go in here and I'll say uh use Archon to fix uh issue number 176. There we go. All right. Now, now we'll see it in action. So, uh again, it'll load the archon skill. Well, I guess first it'll view the GitHub issue and then Yep. load the archon skill so it knows how to invoke workflows and then it'll kick off the workflow. So archon fix GitHub issue and then uh we're doing it in a branch. So it's going to do this in a work tree. So we have isolation and there we go. So now the workflow is running in a background process. So cloud code has support for this. I don't know if codeex does as well because I haven't used codeex in a while if I'm going to be honest. But if you click into the shell here, like if I if I press the down arrow and then hit enter, I can see the details and the logs of the workflow as it's running. So we can monitor it here. And then the cool thing is because it runs as a background process, I can continue. I can run more archon workflows. I can keep just talking to the agent here. I can also say give me a status update. So it can look into the logs for the background process and then tell me what stage of the workflow it's in. So if I want to check in because this is a longer running workflow, it can say like oh it's currently investigating or it's in the middle of classifying the issue. So it it reads like I know it looks kind of long here but this is the the logs that are stored internally on my machine for the background process and then it says all right cool. So work tree is created it extracted the issue number and it classified the issue. So it's currently running the web research step and if we go to the web UI here I can actually see that. So take a look at this. We have it currently running. So I can see it in my chat. If I go to the mission control right here, I can also see all of my running workflows at a high level. This one is currently running. It has been for a minute and a half. And if I view the logs, take a look at this. I can see what steps have completed, where I currently am, and I can see the tool calls as they come in, which a lot of times for Archon workflows, you're just going to fire and forget, right? Like you just want to have it handle something in the background, and then you'll come back once there's a pull request for you to review. So, it's not like you're always going to be watching your workflows in the web UI, but especially as you're building your own custom workflows. It can be really, really useful when you're first debugging things to dive into a workflow log and like make sure that things are actually happening as you intend them to. And so, we can see the logs. I know like this one specifically the the web searching it it's um a longer step but like we can see all these tool calls come in live as uh as it's working. Um and then we can invoke a ton of different workflows in parallel and we can watch them all here. We can click between the logs for them. Uh it's pretty cool. So yeah and so we can monitor it here or in the web UI. And uh you know what? Just for the sake of of getting kind of fancy here, I'm going to uh I'm going to show you guys how I how I actually use Archon every single day because here's the thing. I am not just working on one issue at a time with Archon. Um the fix GitHub issue workflow is my most often used, but I'm using it in parallel a lot. So take a look at this. I'm going to go into my speechto text tool. I'm going to say, okay, I also want to handle more issues. So, let's see here. Uh, let's tackle issue number 167. Um, let's see. Let's also do um, 182 and 1,087. All right. So, I'm going to send this in. Uh, by the way, usually I'll do even more than this at once, but I just want to make sure that I don't hit my rate limits for Claude right now because it like I mean we're doing a lot of work in parallel here. Not that Archon is token inefficient. In fact, we've been doing a lot of things to make it more token efficient, but still like there is a a bunch that I'm doing at the same time right here. And watch this. Not only can I say, you know, spin up the workflows in parallel, but I can say I want you to, you know, run these workflows in parallel. I want you to wait until all of them are done. So monitor the workflows until we have pull requests for every single one of them. Then once we have pull requests for every single one of them, then I also want you to run the validate PR workflow on all these in parallel. And then when it produces the comments and the PRs, I want you to view the poll requests, look at all of the issues that we need to address. I want you to address them and push the changes to the branches for the pull request. And I could even combine all this into a single workflow if I wanted as well. But just like look at how comprehensive this is. We are going all the way from issue to a final validated pull request and we're doing it in parallel. So it's spinning up all of these at the exact same time as background processes. So now if I go into the four shells that I have open here in cloud code, we can see that they're they're all currently running. And then I can go hit enter to view the logs for any one of them. And um then of course I can see them all running in the web UI as well. So let's go back to the dashboard. And there we go. We got all four of them running. So, we have each of them running in the last 20 seconds here. And then this one that's been going on for five minutes now. Pretty cool. So, yeah, we're still doing the web research on this one here. But, yeah, that that's how I use Archon on the day-to-day. Like, most of the time when I'm working on a codebase, I'm I'm going to be filing things as issues. whether it's a bug that I'm going to be working on or it's a new feature that I want to add. Like both of those those fit as GitHub issues. And it's also nice because this is kind of like my personal mission control for everything I want to work on. And so that's why we see like Raasmus opening up so many GitHub issues. Like we're using this more than you know other people are because this is where we document all the things that we want to work on. Like Raasmus is opening up issue after issue for, you know, bugs and feature requests. And so that's also really nice because GitHub is where we're going to keep track of the versioning of Archon. Like as you evolve your codebase and you want your coding agent to remember things that you've worked on in the past, you're going to rely on git commits. I actually love using the git log as longterm memory for my coding agents. And so I'm already keeping track of all my work in in uh as like git commits and so I might as well like track things in is in issues as well for like the upcoming work that I have. So you can of course hook in like a MCP server or skill for Archon to use another external platform like Linear or Jira for your task management. I personally just love using GitHub as my task management. So that's why the GitHub CLI is so crucial for me for pretty much all of my Archon workflows. Now, of course, there are Archon workflows that don't have anything to do with GitHub. So, like for example, if I want to create a PRD, I can say, you know, use Archon to walk me through creating a PRD. And so, this is going to uh, you know, hopefully load the Archon skill here and then walk me through the interactive PRD workflow. So, I'm just showing off another workflow really quickly. And this one's actually pretty cool because it has human in the loop. So, it asks you some questions, it starts building the PRD, and then it stops to ask you more questions. So, maybe we'll see this in action really quick here. And then I also I do want to get into the other um the other thing I wanted to show you guys like building a workflow based on GSD. Okay. Um pick your starting point. Let's see. Okay. So, it actually tells me like here's a few different workflows. Um I want to use the interactive PRD workflow. So, let's have it kick that off for us here. Okay. Interactive workflows. Uh, got it. The interactive PRD workflow is a guided conversation where AI asks questions and rounds to build out a PRD. Cool. So, um, I don't know. I want to build support for PI agents in Archon. I mean, I think it's kind of an interesting example to let me make sure it actually my speech text tool spells that right. And I'll just say uh with the SDK. Not that I'll build this right now, but I'll I'll show you guys quickly what it looks like to go through a different workflow because like I get so hyperfocused on using the fix GitHub issue workflow. I want to show you guys something a little bit different here. Okay. So there we go. So now it kicks off the archon investigate or sorry interactive PRD. So the workflow is running. It's going to explore the codebase before it starts asking us some questions here. And we can obviously go and like view it in the logs along with the other ones. So this workflow is actually in a pause state now. So you can see in the web UI we have support for this where it'll show us like here is where we have a human in loop step. So while the all the other workflows are running this one we're more interacting with. So uh let me so it says it's paused. Let me grab the output. So it's going to read the logs and it's going to ask us some questions here. Right. So we the workflow is in a pause state for us to give feedback. And this is very similar to what I was showing in the uh example in the diagram earlier where we could have like human in the loop for a planning step but we get to actually review the plan and have the coding agent iterate on this before we go to the next step. So asking some foundation questions. Uh let's see. So who has this problem? Um everyone using archon. I think it's kind of a weird question actually. What problems are they facing? Uh the problem they're facing right now is there are a lot of people that don't want to use claw or codec specifically. They want to use different models. PI is more of a general agent that makes it really easy to uh to use other models. Um let's see. Why can't they solve it today? Uh well, we don't have support for PI yet. And I want to build this now because we're currently working on making big improvements to Archon and Pi is one of our priorities. We will know when it's solved. success. Looks like we can use pi, any model in pi with all of our archon workflows. So these questions um if you aren't familiar, these are like really standard questions for product managers to ask when they're first creating a PRD. So we have like a lot of like product manager best practices built into this workflow. Um, now the some of the questions were a little awkward for me right now just for the demonstration here, but they they are like legitimately good questions to ask when you're first creating a product requirements document. So now you can see that um using the archon skill, archon knows like, okay, let's resume the workflow with an approved state. So we're approving and then it's giving our feedback in. So it passed our answers through. So now the workflow is it went out of the pause state into the running state. And we can of course view the logs here to see what's going on. So this is the first node that it ran and then it asked us some questions. Now we move on to the next one. So it's kind of just like a process of like asking us questions and going in a loop here. All right. Um Oh, is it paused again? Hold on. No, it's still running. Okay. So we'll wait for it again. Although I might actually not continue with this demonstration because I think you guys get the idea. It really just does this in a loop where it has like a set of questions that it uh goes through for each one of the the prompts that we have right here. So I think you guys get the point. But there's an example of a workflow where um it doesn't really have anything to do with GitHub because not all of them have to. That's what I wanted to show. The final artifact obviously of this workflow is going to be a markdown document which is our PRD. So then we would, you know, break that up into tasks and and go through piv loops as a separate archon workflow to uh knock out all the phases that we have in that PRD. And then if you really wanted to get fancy, you could even if you wanted to make it so that the whole like pimploo process and PRD creation, like everything is a single archon workflow. Like I said, your entire software development life cycle, you can package that all up as an archon workflow. All right, cool. So, yeah, I think with that, I want to show you guys how to create a workflow from scratch because it's actually beautifully easy. So, I'm going to open up another Archon session here. And, you know, before I do that, I do want to spend some more time with Q&A with you guys. So, let me uh go back to the full frame here, and I will open up some more questions. All right. So, give me a second to kind of read through what we got here and then I think uh yeah, so Raasmus is is here in the live stream now answering questions. Appreciate it a lot, Raasmus. And then thank you Thomas as well. Um let's see. What is the simplest path to get this to work with linear tasks instead of GitHub issues? Yeah, so my recommendation would be to use either the linear MCP or create a skill to use the linear API and then you would build a custom workflow. So instead of like fix GitHub issue, it would be like fix linear issue or like handle linear task. And you could even have Archon reference the fix GitHub issue workflow and use that as a starting point where you would just mold things to be all linear instead of all GitHub. So it's actually very easy to uh integrate any platform that you want into Archon because for every single node you can inject skills or MCP servers. Um, so for the case of GitHub, like coding agents are so good at using the GitHub CLI that I don't need a GitHub CLI skill. You might need that for linear though or like I said the MCP server. But seriously, all you have to do, and I'll show you this in a second, is you like, okay, watch this. Um, I don't know. I don't think I'll actually run this right now, but I Oh, here. Let me go back to my scene so you guys can see my screen. I forgot I wasn't sharing my screen. So, I can say like, uh, load the archon skill. I want to create a version of the GitHub fix issue workflow, but specifically for linear instead of GitHub. Like that is all you have to do. Now, obviously, you're going to probably have to iterate quite a bit on the prompting and like really making things specific to you. Uh so this is this is certainly an oversimplification, but like this literally could be your starting point. Like this is what you you send in. Um and so yeah, after a little bit of Q&A here, I'll show you what it looks like to create a workflow. Like man, the archon skill is so beautiful because it just it knows everything. It'll it'll walk you through everything. And and another thing I love doing with coding agents is I like asking it to ask me questions. And so maybe I would send in, let me go back to my Aqua voice here. So I paste this back in. Um and I could say like, you know, ask me questions to make sure you understand uh my linear setup and exactly how I want the workflow to function, right? So that way you're you're kind of reducing the assumptions that it makes up front. Um, and so what it produces in the end is going to be better aligned with what you actually want before you go into iterating. You'll probably still have to iterate, but that's the idea here is like we go through a bit of a planning process with Archon before it um before it creates the workflow for us. All right, cool. What else do we got here? Um, with the session management within the workflows, how is context persistence handled? Is the data and context passed through the nodes? Okay, that is a really good question and we have a few different ways to handle context persistence here. So, uh, I'm trying to think if I have a good workflow to demonstrate this. instead of poking around, I might just more answer your question at a high level. Um, but yeah, one of the core things that we have in Archon is a parameter for each node that specifies if we want to continue the session from the prior node or start fresh. And so that that flexibility is pretty powerful because maybe you want a different node where you inject different skills or you just want to like have a new node for some reason because you want to like switch models or something but you want to still continue the same conversation from the previous node. You can do that or you can say like I actually want to start completely from scratch in this node. And then another thing that we have in archon is we have like outputs like we can output artifacts and so like for in this case we have the planning step and it's going to output a plan to our artifact directory for our current workflow execution. So this is like one of the primitives we have in workflows. It's like the artifact dur. And then we when we go in a brand new session in the implement stage, we are going to prompt it to read the plan from the artifact directory. So if I look at the archon fix issue command, let me open this up here because we you you can prompt inline. I've shown that in some of the workflows, you can you can have the prompt right in the YAML for the workflow or if you want to and you want it to like kind of be more organized, you can have it reference a command in the commands folder. So we'll go to archon um fix issue. There's a lot of commands here. So I have to find the right one. There we go. So archon fix issue. You'll see here that the argument is the artifact path. So archon is smart enough to know like once we are done with the planning and we have our plan here, we're going to prompt in a brand new session for our coding agent to read that plan, right? like go to the artifact directory and read that plan and then go through the implementation here. So, it's a brand new session, but then we're still passing some context or like I said, you can just uh have the context be like continue instead of fresh. So, it's up to you like flexibility depending on how you typically work. All right, let's see what else we got here. Let's see. Have you really given anything other than Opus a real try at Agenta coding tasks? I haven't. Uh, so I I do mostly use Opus for my implementation. However, I have tested a lot of using Sonnet for my archon workflows. So I I talked about this a little bit at the start of the live stream, but I get better results using Sonnet to fix GitHub issues with this workflow than just using Opus by itself in Cloud Code because of all the the context engineering that goes into you know like this. I guess you could call this like a GitHub issue harness like a fixer harness. U so I have run this with sonnet. So sonnet is actually the default model for all the nodes here. Uh now for the implementation itself I think we have it set to yeah so we have it set to using opus so like the default workflow as it stands uses opus specifically for implementation but obviously if you just delete this it'll use sonnet as the default or um you know you can change the model manually or whatever but so like at one point I had it set to sonnet and I was using it sonnet for everything sonnet or haiku for everything here and I was still getting really good results obviously obviously the best model is always going to give you the best results. Um, but for the sake of like making sure you don't hit your rate limits and stuff, you can use Sonnet for these workflows. And you can even like ask it to adjust the model at the default level or the specific node level before you run it if you want to. All right. People like seeing you failing. Pretty sure makes you a normal human. I assume you you referenced that when I was having all of the issues here in the VPS. So, I appreciate that. Uh, we'll talk about why I have those issues in a second because I have a Claude code. Um, I'm not actually authenticated with Claude. I am authenticated with the Miniax API. That's what was causing the problems on the VPS because I'm getting things set up for the dark factory. All right. How many tokens does start the app take? So, when I asked it to just like spin up the front end and back end of Archon, I mean, I don't know exactly, but it's probably just going to be a couple hundred, unless it's like running into an issue for some reason. It's not going to take that many tokens. And uh, by the way, you can see here that uh, it's already kicking off the whole process here, helping me create the linear version of the workflow. So, asking me some questions here. I'll answer those and then it'll create the workflow and test it for me and everything. Like I won't go through this whole process here, but for the question earlier on on migrating to linear, like it's just so easy to have it walk through cuz pretty much like here's the thing. All of the default workflows we have in Archon, there's two there's two uses for them. One is you can just use them directly out of the box if if there is one that like matches how you already work. But the other maybe even like more important part of these default workflows is it's a reference point for your coding agent to build something that's actually custom to you. And so even if you're building something that's like super different than everything we have here, like some kind of like refactoring workflow for example, um actually we have that as well. So maybe that's not the best example, but even if you have some like super different workflow that's like not even close to anything we have here, you still want your coding agent like loaded in the archon repo to look at these as a reference to understand like the different parameters we have for nodes and how we handle loops or whatever else like deterministic nodes, whatever you might want in your workflow. So very easy to pretty much build any I'll I'll show that in a second, but I just want to answer a couple more questions here because you guys have a lot of really good ones. All right, let's see. All right. Yep. Pi next week. Yeah, not not a promise that like we'll have it ready ready next week, but I'm definitely going to be working on me or Rasmus will be working on the pull request for adding in pi. Um, could I make a node to use codec spark in a workflow? Um, I mean there's nothing stopping you. You can make a node do literally anything because it can be a prompt to a coding agent or it can be a script. Even if you wanted to use a coding agent that's not supported by Archon directly, you can just make a script that invokes that like the Yeah, the world's your oyster here. All right. Um, let's see. What about create a node to mention other workflow, not only a command? I I think what you're asking about here is if we can nest workflows like if we can have a workflow that calls another workflow and uh that is something that we are planning on adding support for. Yep. So I haven't added that yet like subworkflow execution like you have in N8N. I haven't added that yet because I haven't found a a clear use for it for me personally but uh you're not the first one to ask about it and so like we are definitely interested in adding support for that. show some love and hit the like. I appreciate it a lot. Yeah, if you guys want to like the stream, I of course would appreciate that. Like the stream and uh and subscribe because I'm gonna be putting out a lot of content on Archon because like yeah, I'm getting pretty deep into the live stream here, but certainly a lot more I can show about like creating custom workflows and things that I'll be doing with future YouTube content and then of course in the Dynamis community as well. Uh so yeah, I just want to mention this again. I am planning on doing a lot of of workshops around archon um in Dynamus coming up here in the next couple of months, including using Archon with your second brain and some strategies to show like how I use my second brain to delegate work across my code bases with Archon. It's a bit of outside of the scope for our live stream here, but yeah, certainly the second brain is another really big part of of what I've been doing and what I'm covering in the Dynamis community. So, if you don't know, I I did a full 4hour course on building your own AI second brain in Dynamis. So, I took the entire system that saves me like no exaggeration at least 20 hours a week and I built it like from the ground up in a live stream so that you can follow along. And so, I am turning it into the third course for Dynamus. Um, and so you I'll put this link in the chat again if if you're interested in uh really like being on the forefront of Archon and uh going through these workshops and all the courses and building your own second brain. There's so much value packed into the community, not to mention all of the amazing minds in there sharing ideas every single day. Um, come join us in Dynamis. I' I'd love to have you there. Uh, and I I appreciate it. Dynamus community is great. Yeah. Thank you very much for all of you guys who are in the community uh here in the stream. always appreciate you guys being a part of it. Yeah, appreciate your passion and sharing of knowledge. Yeah, you're very welcome. It is my pleasure. Yeah, I mean I'm I'm excited. Like we had the question earlier of like why open source archon? I mean to me like there's not an alternative. I can't I can't imagine building something like this and just like hiding it from the world. Like I just I want people to to see what is possible with AI coding. Like in the end, that's like my number one goal with my I guess you could call it like my career. Like my with my career in business, like my number one goal is just to uh show people like what is possible with AI and also to just like cut through a lot of the fluff. Like I want to be real but inspirational at the same time. You know what I mean? Like there's a lot of people that are saying like you can vibe code everything and it's going to be perfect and you can make millions of dollars. Like I'm not one of those persons that's people that's like here's how to vibe code to make $10,000. Like no, I'm realistic. Like you have to have human in the loop. You can't just vibe code. Things take time. Coding agents make mistakes. Like I'm real on all of that. But then that's also why I'm building these tools specifically to add in deterministic steps. Human in the loop. Like building these harnesses because then that allows you to circumvent a lot of these real problems that a lot of people are ignoring. And so, uh, actually going to my YouTube channel here. It's funny because like, wait, hold on. I think I still have this in my YouTube channel. Um, yeah. Yeah. So, I've had this like oneliner for my YouTube channel. Um, for like literally ever since I started my channel in 2024, I've always had this sentence um, join me as I push the limits of what's possible with AI. And I've always kept this sentence because that is really what I'm trying to do here. like in a realistic way. Like don't you can't just vibe code a $10,000 a month site in a week. In a realistic way, I am showing what it's like to push limits of AI and and I really think that like harness engineering is the forefront of AI right now, which is why I'm so excited about Archon. So, yeah, there there's my little spiel on on on my my vision and and why I want to make sure that Archon is available to everyone. Cool. All right, John said, "My brain is online thanks to Cole and the community. Couldn't have done it without the crew." I appreciate a lot, John. Yeah, I appreciate you being an active member of the community. Aron just joined the community. Thank you very much. Welcome to Dynamus, my friend. I'm going to be um so yeah, I'm I'm in Dynamus like literally every single day. So, I've been prepping for the live stream today. Haven't gotten to the posts in the last like 12 hours, but uh yeah, I mean like I'm replying to everything like every single day. So, I'll be sure to to greet you if you want to make an introduction post as well. I'd love to see that. All right. Let's see. Any plans to utilize local LLMs? So, that is actually one of the reasons I want to add in PI because PI will make it easier to use local LLMs. And then also within cloud code, you can integrate it with um things like Olama to use local models. So I I know that so Miniax M2.7 I'm not using that's not obviously running locally because it's a massive model. Uh but this is a demonstration of like I do actually have Claude working with a different model. Like check check this out. If I go back into Claude and I say what model are you like this isn't just a gimmick. It is actually using Miniax M2.7 through the MiniAX API. So you can change cloud code to work with other providers like GLM, MiniAX, Olama so that you can talk to local models. So I'm adding in PI because it'll make it easier and it's more like natively supported. Uh hold on, I got a sneeze coming. Excuse me. Um but yeah, you can you can connect cloud code like you can already use archon with local models if you wanted to try like there's been a couple people in the Dynamis community that have actually used Gemma 4 with Archon workflows. like Gemma for kind of driving the whole ship. So definitely possible already. Pi will make it even easier though. Yeah. Uh is there a way to override some settings like the model without changing the default YAML files? So I think there is a parameter to change the default model, but if it's overridden at the individual node configuration, there's not a way to change that right now. Uh, but like you shouldn't be afraid to just ask Archon to change the YAML for you, even if it's just like a temporary thing where it like revert it after it's done with the workflow. Um, it can definitely do that. Like I've actually been doing that a lot recently with cloud code skills where the skill will like change its own scripts as before it runs them and then just like revert it after I'm done with that set of work for any kind of like PowerPoint diagram or PDF generation. I've been doing that. So I wouldn't be afraid to but but still like that maybe that is like a real suggest like not maybe that is a good suggestion to make it even easier. Um let me actually ask it right here. Uh so based on the archon skill what can you tell me about support for changing the model without having to change the YAML itself? Like is there a flag for the CLI to change the model that's used? So, I'm I guess I'm kind of like validating the answer that I gave you quick here because I mean Archon's such a massive codebase. It's hard for me to remember like everything that we've decided, especially because like I said, Thomas and Raasmus have been helping me a lot in Archon as well. So, I'm also not the one that's built everything in the platform. Okay, let's see. There's no model CLI flag. Okay, so yeah, I guess I have to take that back. We don't have a way to do it right now. uh you would just have to edit the YAML directly which again like feel free to do that but also like that that is a good suggestion even if you wanted to make a GitHub issue for that in the Archon repo I'd be down to to address that because I'm just going to have it uh okay so I will say that like when I use Archon to work on your guys's issues in Archon like don't worry I am actually reviewing your issues and reviewing the poll requests as well so I am like legitimately considering the the things that you guys bring Um but yeah just like as the I delegate the coding to the agent itself 100%. We can see that this workflow actually we are almost done here with the GitHub issue fix and then if I look at my clawed rate limits I'm actually curious where we are at with that. Uh let's take a look. Okay, it's actually not too bad. Okay. So, here here's my claw rate limits for right now. This is this is not too bad. So, um I've used 37% of my 5 hour limit in the past like three hour or four 3 hours and 45 minutes, right? And we're only at 37%. before. So, there's a lot of stuff I was doing to prep for the stream today, this morning before I started. So, we were already at like 15 to 20% before I kicked off all these workflows. And we've been doing quite a bit with Claude recently. I mean, we have so many workflows running right now and it it it used less than 20% of my 5 hour limit and we're almost done with all these workflows. Like, they're pretty token efficient. You could you could run the fix GitHub issue workflow like doz like at least a couple of dozen of times um and and until you hit your five hour limit and like that's a lot of work that Claude is doing. Uh now the really unfortunate thing is my limit reset yesterday and I'm already at 32% for the week. That is a huge bummer. Like I'm probably going to hit my weekly limit around Tuesday or Wednesday. It's unfortunate. Uh, so yeah, there there are always people that tell me they have like, you know, two, three, four claw subscriptions. I'm not one of those people, but honestly, after Anthropic u making things making the rate limits more harsh recently, I might have to get a second subscription. I feel bad saying that cuz it's like Anthropic is being kind of frustrating recently and then I'm just giving them more money when it's like, well, what can you do? like I I don't really want to switch over to codeex because I test codecs from time to time and I I just I think claude code is better. But anyway, so yeah, it's yeah, these workflows are pretty token efficient for how much they're actually doing. Like keep in mind, it's not just asking cloud code to fix an issue. It's going through deep investigation, deep research, deep implementation, and deep code review using the right model at the right time. So it's not uh super tokenheavy. All right. Uh, working on something similar and yeah, thank you for the $5 donation. I appreciate it a lot. Uh, would love to discuss with you about how we could potentially partner if there's something you are open to. Yeah. So, Archon is an open source repo and for me that means that partnerships would be like I'd love to chat and see what your ideas are. Uh, but I I wouldn't really want to like go and work on a separate repo. But if you're interested in like contributing to Archon and partnering in that way, um I am considering creating sort of like a core maintainer team for Archon. I think that would be the way to partner because I wouldn't want to like turn this into a separate venture. I like I said with like my core vision and and mission for Archon and my career as a whole is to be open source and share with the world. And so I I don't want this to like create spin-offs that I'm dedicating time to. instead of working on Archon as the core open- source repository. But I'm always open to uh collaborations, maybe even I'm thinking like I said making the maintainer team always open to issues and poll requests. And um yeah, sometimes open source can get overwhelming. So also like I don't always get to issues and pull requests uh even within the same week because it it gets a lot let me tell you guys from all the open source work that I did. But also, it's more and more realistic to handle everything over time as I have coding agents help me and a maintainer team. And then like I said, like we kind of already have a maintainer team with me, Raasmus, and Thomas. Um, but uh also like thinking of extending that to just like the general, you know, you guys in the YouTube community and in the Dynamus community. All right, cool. Is it open source available on GitHub? Well, I assume that was a question to someone else because yes, Archon is and and Thomas knows that. All right. Is it possible to add Gemini? So, the Gemini CLI I don't think has an SDK. Gemini CLI SDK. So that's the thing is is for any coding agent that we integrate with Archon, it does need to have an SDK because I I work with the coding agents programmatically in Typescript instead of using the headless mode for the CLI. That's like another way that you can automate the usage of um of coding agents. I've I've been checking on this a lot though because this is another one of the tools that I would obviously want to integrate. A lot of people love using Gemini, especially because Gemini 3 seems to be like the best model for building frontends. Like people always use anti-gravity with Gemini 3 to build frontends and um so I I would love to add support for but they don't have an SDK. Um however, you could always use the PI SDK with Gemini. So we add support for that then it would work. Um, I guess I can't find an exact link, but um Oh, wait. What's this? This must not be Hold on. Google Genai SDK. That's I think that's for general agents, not Yeah, that's not for AI coding. So, that's not that's not an SDK for the Gemini CLI, unfortunately. All right. uh to reach these limits, you have to have the product first because you can't code multiple things without having verticals that do not conflict. That's true. Yeah. Yeah. When you're first getting started, it's like you can't really do as much work in parallel. It's more once you have the thing established and you're just working through different issues, like granular sets of work for improvements or bug fixes, then that's definitely when you're going to start hitting the limits 100%. All right. Um let's see. I'm on the $200 max plan. That is true. Would you hit limits much faster on the lower plan? I think yes. I mean, yeah. The answer 100% is yes, cuz the um $20 plan doesn't take you very far to be honest. And then the $100 plan, like you can you can do quite a bit, but you still hit your rate limits decently quickly. I believe that the $200 month plan is four times better rate limits than the $100 month plan. And then the $200 is 20 times better than the $20 plan. There's a quite a big difference there. All right. Let's see. How is this different than uh BMAD version six? So, okay, here's the thing. BMAD is a harness. Archon is a harness builder. So, BMAD is a an opinionated approach to building software. It's a good approach. I think it's kind of overengineered to be honest, but it's a it's a really inspirational approach and you can literally take ideas from BMAD and build it into your own archon workflows and then customize it more for yourself. So the big thing that I want to be clear on here is that uh Archon is not competing with GitHub specit or BMAD or Cloudflow or GSD. It's more like those tools are great, but what if you want to build your own? That's why it's a harness builder. And so, um, yeah, in a second here, I'll show you what it looks like to literally just like take inspiration from GSD and like build it as an Archon workflow. Archon is very powerful. Going to scrap the GitLab AI reviewer I developed yesterday and use Archon instead. Archon offers much more room for expansion. Very cool. Yeah, I appreciate it. Uh, and you know what you can do is not scrap what you built, but uh, point the Archon repo to look at what you built for inspiration to turn it into an Archon workflow. And and so yet another thing that I want to, you know, re-emphasize here is you don't have to ditch what you already have if you want to build archon workflows because you can bring in your skills and commands. You can reference other other frameworks or other tools that you built to use as inspiration either for the prompting or just like the general process that you'd want to lay out at in a node by node basis. you're always able to um work with what you already have because I don't I don't want to that's another one of the problems with with all the other harnesses that are out there. Like they're cool, but they require you to pretty much change how you work fundamentally. And that's just not going to fly. Especially if you're working on a team, like if you're at an enterprise level and you already have a process for your software development life cycle, it's really really hard for you as a an enterprise level like as a team to adopt something like BMAD because you have to change how you work. But with Archon, you don't change how you work because you're building the layer on top of the coding agent that actually enforces that. So you get to even um in a better way take how you work and use coding agents with that. Um yep Rasmus same here. Use it every day since November. No bans using the cloud agent SDK with the anthropic subscription. Oh yeah. When are there going to be archon hoodies and merch? I would be interested. Yeah. Um, yeah. I mean, merch for Dynamis and or Archon would be pretty cool. I don't know like how much of an interest there would really be for that, but it could be cool. I mean, my man Nate Herk is always rocking his um his merch in his uh YouTube videos now. It would be cool to have a a sweatshirt or sweater or something that I wear when I'm recording. Yeah. All right. Yeah. Very cool. Well, meld archon and my QA bot. That's the way to do it. Meld it with what you've already got 100%. All right. At peak, I had 30 something archon workflows running in parallel across four projects. You know, with the anthropic rate limits now, you probably won't be able to do that, but uh that's very cool. We we've been spoiled at some points. So, uh, within the like, you know, the last couple of weeks up until this week, Archon or not Archon, Anthropic was doing a special where it's like in off hours you had, uh, two times lower rate limits. And trust me, I was taking advantage of that, chugging through like eight poll requests in parallel for like the entire day straight, multiple days. Well, not the entire day straight, but like during the off hours. Uh, so yeah, it's it's a little unfortunate, but I am I am doing some experimentation with like other models that like, you know, Miniax. It's just not as good as Opus, but you still get quite a bit of power. So, if you have the right harness, you can get really good results even with something like Miniax M2.7. So, I am experimenting with some things that'll get into the dark factory we'll talk about in a bit. I am experimenting with some things though to be able to scale the number of workflows I can run in parallel and not have to worry about rate limits. It'll get a little costly, but I mean the point of using these smaller models is it won't get too costly. All right. Yeah, that's right, Sean. Spicy mango shirts. And man, spicy mango hasn't come up in a while now. I'll I'll need to fit that into more YouTube videos, but it's like an ongoing joke where um I don't even remember where it originated. It was like something with GPT where like I was asking for recipes in a YouTube video and it kept like bringing up spicy mango even between conversations where there's no long-term memory. So, it just kind of became a joke from there. All right. Let's see. All right. Um, you know what? So, man, there's so many good questions in the chat still. But I do want to get to the next part here where I will uh build a workflow with you guys. So, let's let's go back into our repository. I'm going to close out of this session and start a new one. All right. So, here, hold on. Let me clear. There we go. All right. So, what I want to show you guys now is how to build a custom workflow in Archon. And there are a million different ways or different kinds of workflows you can build. And like I said, you can take inspiration from all these existing ones, even pointing archon to look at these to, you know, understand best practices and how we've been building workflows already. But as a as an example, like I've teased already, I want to build GSD as an archon workflow. So GSD, it's a a lightweight and powerful metaprompting context engineering spec driven development system. Little bit of word salad there, but basically it's a simplistic approach to going from planning all the way to getting your work done with coding agents. It's it's it's nice. and um he I actually really appreciate the inspiration behind the project. So he says other spectrum and development tools exist like BMAD and SpecKit, but they all seem to make things way more complicated than they need to be which I agree with this. I actually already said this in the live stream where these tools are very inspirational, but just like it's more than you really want in your process and they're so opinionated. You've got your sprint ceremonies and story points and stakeholder syncs and retrospectives and jurro workflows. I'm not a 50 person software company. I don't want to play enterprise theater. And like preach, man. Like that's good. So I built GSD. The complexity is in the system, not in your workflow. So the the system gives Claude everything it needs to do the work and verify it, right? Like that's that's the harness here is it's a system for planning, implementing, and validating. A lot of like what I've already been talking about. I trust the workflow. It does it just does a good job. It just gets it done. And so I want to take some of the these ideas here. So I'm not like, okay, I'm not going to build this like step by step in Archon. I'm not going to build a replica, but I'm going to take the general flow of the different phases like discussing and planning and executing and some of their strategies for splitting up work into different stages and their verification. I want to take inspiration from this, but I'm going to do it with Claude. So watch this. I'm going to copy this repo. I'm going to paste it in and I'm just going to say load the archon skill. I want you to help me make an archon workflow that uh takes very heavy inspiration from GSD, the repo that I gave you the path to here. So, I want you to analyze the repo. I want you to dig deep into the process here and how it goes through the different phases, how it manages tasks and does verification. And I want you to analyze other workflows in Archon, some of the defaults to get an idea for like how those work and how we could translate ideas from GSD into a new workflow that we'll create that'll basically go through the same process having human approval gates for different steps of the way within planning and validation. So, and actually one more thing that I want to add to the prompt here is I'll say I want you to after you do your research, ask me questions. to make sure that we're aligned on what this workflow does and how we're going to take inspiration from GSD. And so, I mean, if you wanted to go so far, you could pretty much replicate all of GSD as an archon workflow. That would take a lot of work. I think that would take too long to do in this live stream, which is why I'm doing it more like and like, you know, let's just take inspiration from GSD versus replicate it. Exactly. But we'll still get something pretty similar here. I actually did already test this before the live stream and the results were were pretty good. Now, it is going to take a while to do the research initially or at least a decent amount of time. So, I'll answer some more questions while we let this run. Uh, but I think this is a nice demo because without getting too complex here, just showing you at a high level how it's like no matter what you want to build, just describe your process, have it look at existing workflows for reference. And of course, Archon skill helps and then just start building with it. In fact, one of the workflows that we have is a workflow builder. It's very meta, but whenever we want to build a workflow, we can use this. It just kind of provides some more structure, right? It's a harness around building more custom workflows. A harness around building harnesses. If I had a dime for every time I said harness in this live stream, I would just go retire. All right. Let's see. By the way, I built Colm for agent memory context engine. Close to 100 stars already. It's pretty cool. Congratulations. Yeah, long-term memory for AI coding is uh it's very powerful, very needed. Let's see. Um, do you have the possibility to temporarily run commands from the web UI like running a dev server from your work tree to check the look and feel of your change from your workree? Yeah. So, we have played around with the idea of having like a basic terminal in the web UI to do things like that, but we haven't built that yet. Um, it's one of those things where it's like, let's see if people really need that before we build it. A lot of what we built into Archon up until this point has been like, you know, just, you know, only like three people really sharing their opinions. And well, okay, obviously it's not just three people because we've had this in the Dynamis community for a while as well, but for the most part, we haven't had like hundreds of people using it yet or thousands of people using it yet like we are about to. We kind of already have now this week. And so, we'll see how people really use it. And I'm thinking about um getting like feedback from the YouTube and Dynamis community as a whole for what kind of features we want. Things like this we might want to build, but I just want to be careful with feature bloat. I want to make sure like there are a lot of things that sound good on paper, but like maybe people don't actually end up needing that. So, for the old version of Archon that I was building over last summer and like released in August, that one we we made the mistake of building in way too many things up front. Like there was a ton of different configuration parameters and stuff that like sounded really good on paper, but then like no one ever actually used it. Like I'd constantly like show things like that on live streams or in Dynamus workshops and people would be like, "Wow, I didn't even know that was a thing." like I well I like saw it but I just like glazed over it because I didn't really care about it. So that that's the kind of thing I want to look out for. Um but yeah, I definitely would be interested in like adding more support in the web UI for being able to like actually manage everything yourself, not just relying on Archcom. Now the other thing is you could just ask Archon to spin up the site in the work tree, right? Like it it could take care of that even by itself. So you don't necessarily need a place for like you to run the commands yourself when you can just ask the coding agent to do it. But I I still think that that could definitely be a good addition to the web UI. All right. Let's see. How do you pause all or a graceful pause? Yeah, there no way to do that right now in Archon because the pause is reserved for human in the loop workflows. So, it really is like you either abandon the workflow. Well, okay. Actually, there there kind of is support for it. It's just not direct cuz you can abandon a workflow and then you can uh resume it later. It's just if you click abandon, it's not going to like show up in the web UI as something you can resume. But there is a CLI option to resume a workflow. So you could just if you have to like shut it down for whatever reason, you could just say like, hey, like I want you to interrupt and stop these workflows. And then later on you could tell Claude like, okay, resume these workflows. And if it's in the same session, it'll it'll remember the workflow ids that are stored in the you know the SQLite database or Postgress database under the hood so that it can it can pick up where it left off. So it'll basically just like retry the node that it that was interrupted and then continue the workflow from there. So yeah, just kind of thing you just ask the agent to do it. It knows how to to how to do that. All right, cool. So we got we're only at 50% and it resets in 55 minutes. So our limit is good here and it's going through. So you can see that it um finished all of the GitHub fix issue workflows. Now it's just doing the validation here. So if I go back to Archon um man I have so many sessions open up. Uh which one was it? Yeah, this one here. So let's see. So it's checking in on all the workflows over time. Um done. There we go. So, yeah, you can see that all of the fixed workflows were done. We have the pull requests created and then it launches the validate PR in parallel. So, sorry, I know I'm jumping around a little bit here, but I just want to show you the other thing that we've had running this entire time. We created the pull requests, those four in parallel, and now we're doing the the reviews all in parallel as well. And that's what we're seeing in the the web UI here as well. And then we have the interactive PRD that I'm just going to kind of abandon because I don't want to spend time on that right now. All right. Oh, yeah. Thank you very much. Yeah, congrats on the 200,000 subs. I appreciate it. Yeah, so that happened literally just yesterday. I I reached 200,000 subscribers. So, yeah, pretty big milestone. I don't get a plaque for that like the 100,000 unfortunately, but it still feels really good to get to that point. So, yeah, thank you. All right, cool. So, all right, let's see what we got here. So, we got the core summary of GSD. It implements a spec driven pipeline with these phases, questioning, parallel research, requirements, road map, uh, perphase loop, and then um, we get our complete milestone. So, that's like the end result of going through the whole spec driven flow. lists out some key patterns here like the plan checker as a gatekeeper before execution, goal backward verification, which um yeah, I mean that this is the thing with all these frameworks is there's so much like word soup, word salad, like what does that even mean? And obviously it's not that hard to like get into the read me and stuff, but I don't even remember exactly what all these things mean. And I've used GST before. Uh okay, so here's what Archon supports for us. The closest existing workflow is the archon piv loop which yeah that's like literally the workflow that I described here in the diagram. So this is the closest to GSD because it has the same stages of planning and then implementing and then validating. Okay, so now it asks us some questions here. Uh wow, it asks us seven questions. Okay, let me try to get through these really quick. So uh is this a full project or a single feature? GSD covers an entire project life cycle. Archon workflows typically target a single feature or issue. Um, wait a second. I'm actually kind of confused by the question. Oh, I see. So, it's like, do we want to have it build an entire PRD for like an entire project or is it more like a workflow that takes a PRD or feature description and runs GSC style plan? Actually, let's do that. Yeah. So, for question number one, let's do something in between. So workload takes a PRD or a feature description and runs GSD style plan execute verify. That makes more sense. Um for the planning rigger, yes, I want the full planning rigger of GSD. Uh I do want all layers of verification like GSD. Where should human humans have approval? Let's just do the same as GSD. Actually, a lot of these questions aren't that good because it's just saying like, hey, what part of GSD you want? I really do want all parts of GSD for the sake of the demo here. And uh yep. So we'll do parallel research 100%. Uh where does the progress live? Yes, I want to create similar structured state files as GSD in the artifacts directory. That makes sense. Uh naming and positioning. How do you want to position this relative to existing workflows? Something like archon GSD or archon rigorous dev? Uh, yeah, let's just call it archon j-gsd. All right. Okay. Honestly, I wasn't that impressed with the questions it asked me there because mostly it was like, do you really want all this parts of GST? Which maybe that kind of speaks to how GST is a little overengineered. Like they they claim to be the simple version of things like BMAB, but I still think it has a little much. Um, but also like people get good results with it. Like trust me, it's popular for a reason. So I I do want to build an archon workflow here that that uh really takes inspiration from every part of GSD. So all right, we'll let it continue to rip here. So it's reading through uh some example workflows here, reading through the rule, my rules for workflows and how to build them, gathering context to then create the YAML for me here. Um open code integration. Yeah, so open code is one of the the uh coding agents we are we are considering adding that and PI agents. Yep. We'd love to add more. All right, let's see. Um, Archon doesn't work on Windows because it can't find the cloud code executable at runtime. Looks like it's a a known crossplatform issue between Linux, Mac, and Windows builds. Uh, so I'm running on Windows myself. I've never had that problem before. Um, so I'm not sure why that would be the case. If you installed through the binary, there might be a bug in the binary. I would try doing the installation method that's higher up in the readme where you clone the repo and then you go into claude and you just ask it to help you set up archon. I would try that instead. That's the only thing I could think of. Otherwise, I'm not sure why it would say it can't find the claude code executable because when you're running archon, it's just using claude under the hood and it's just using it in the same way that you if you ran claude from the terminal. So, it shouldn't be different. Uh what inspired me to build archon? Ah good question. So yeah, I kind of talked about things related to this in the stream already, but uh really it's like I see the direction that we're heading with AI coding. So this is what I talked about at the very very start of the stream. So maybe you weren't there at the start of the stream, which I mean probably a lot of you guys watching right now weren't, which is all good. Uh but like AI started with prompt engineering, generative AI like that was the big deal. Like how can we get the single best output from a model and then that evolved into context engineering especially for AI coding. It's like creating a whole ecosystem of context for our agent to handle longer running tasks. And that's like the big thing in 2025. And now this year it's like how do we create a system that combines coding agent sessions together to do longer work and how do we like really build our coding process as an agentic coding workflow. So the harness is the layer that wraps the coding agent to combine sessions together and add in more control for us. That's how we really get reliable results with coding agents. And so I've been really really doing a lot of research and deep dives into harness engineering over the past few months. But the problem is we have all of these closed source harnesses like Stripe shared stripe minions and Shopify is Shopify roast and adws is building their internal harnesses and and we have things like Ralph loops which are open source but also like not very intricate or like I mean the main problem is there's nothing out there that's like custom to you. So I wanted to build a tool that allows you to build your own harness. So no matter what your process looks like for AI coding, you can create it as a full workflow in Archon and then also run it at scale because we support the parallel execution like I've been demoing in the live stream here. So that's the inspiration. It's like I see where AI coding is heading and there's nothing like Archon right now. Like literally the only examples we have of anything like Archon is is a single harness. So it's not custom to you. It's very opinionated. Most of them are closed source and now this is the layer that build where you can build any of them or build your own. Yeah. All right. Thank you very much for your donation. I appreciate it a lot. All right. Cool. So, let's see what else we got here. Um, I do like cancel over abandon as well. More severe and implies the token use loss, right? Yeah, I mean you can resume it, but then you're restarting the last node that interrupted, which is Yeah, I guess kind of what you're getting at. All right. Um, so anyway, true story. This is the missing link. Glad you think so. Yeah, I mean I I really do like this all signal points to this. This is the most important thing. this year for AI coding, building software in general, and there's just not enough people paying attention to it. Like, okay, as much as I appreciate how much people are focusing on the new features in cloud code, like mo it seems like most people making AI content right now are just like covering the new things in claude code like over and over and over again. And like yeah, Anthropic is doing some very incredible things. It's like it is important to cover that but also it's like like look look past that like what what's what what are like the real ways to actually get good results with AI coding assistance. It's not just being hyperfocused on the individual features from anthropic releasing the cloud code. It it's focusing on how you build systems around AI coding. That's what I feel feel like people aren't paying enough attention to and what I'm really trying to focus on myself. All right, cool. So, let me open up. Let's see where we're at right now. Okay, actually I I just saw it finish. Good. So, perfect timing here. All right. So, yeah. One moment. I'm just looking at something on my other monitor here. Okay. All right. So, it built the full workflow. Um, actually, let me take a look at what it did here. Okay. So, it built out the YAML. It registered it as one of my default workflows. So, I I could actually like ship this to Archon today. I might actually do that, but I'll probably have to do a lot of validation of this before I actually push this live. But, it could be a cool workflow for you guys to use. All right. Um, and then so it ran the validate command to make sure that all the parameters are good. So, we have some things built into the CLI to validate workflows as well. I haven't tested end to end yet, but we can definitely do that as well. And so, okay, here's our pipeline. So, we spin up four agents to research in parallel. We synthesize everything into a summary and then we extract requirements with acceptance criteria and then we have an interactive loop to lock in the context. We create the plant. This is pretty comprehensive. GSD does a lot like it does more than you'd think when they claim to be something simple, but this is cool. It's really cool that we built this as a full archon workflow. And then we verify the plan, we have the human review, and then we execute. And then we do our verification, code review, and human acceptance at the end. Man, that is that is a lot. But there we go. That's what we just built. So, let's actually take a look at this here. So, if I go in, we have the new workflow, and it's pretty long. I mean, it's it's over,200 lines long, but that's just because all the prompts are in line. So, if I were to like really make this concise, what I would do is I would take all of these really long inline prompts and I would make them as commands like we saw in the GitHub issue fix workflow. Like this step is so much nicer looking because the whole prompt is just a command. So, it references the external markdown document. But anyway, we can address that. It's kind of nice to see it all in one place at first anyway, which is why I have it build like that. Um, so okay. So, for research, we decided to use Sonnet. Maybe we'd want to change that to ha coup. Totally up to you. Obviously doing that in a fresh session. So you are one of four parallel research agents. Your focus is on technology stack dependencies and development environment. And then we have researching the features. We're doing that in parallel as well. Um cool. And then yeah so we just have a bunch of research agents here. So four research agents running in parallel. And then we have the uh research synthesis. So it depends on all these being done, right? So these four can run in parallel but now this one has to run after. So it depends on these four being done and then we do our synthesis. So these agents uh have exported in parallel. Now we need to bring everything together into a single document and then we send that into the requirements gathering. So I mean most of what we're doing copying and GSD is just their prompting right and then like the different nodes for the different stages. So what do we have here? Okay. Yeah. So here's where we have the human approval gate. So we send the message to the user. Here's what you have to approve. Like here's the document that we just produced with the whole plan of attack split out into phases or whatever it does here. Uh so yeah, I don't I don't really want to like go into the details of every single node here. That's not really the point. But what we can do is we can also view the workflow in the web UI. So if I go to workflows here, I scroll down. Uh well, actually, hold on. I might need to restart the back end. No, it's right here. Yeah. So if I click edit, um take a look at this. Look at that. That's pretty cool. So we can also see the workflow in the UI. So we can see that we have these four running in parallel. So that that's set up that correctly. And then we do the research, synthesis, requirements, blah blah blah. I mean, this is a lot. I I probably won't be able to run this whole thing with you guys right now. Uh but I could I could get started. I think I have Yeah, I should be good on my limits here. So, let's let's try this right now. Um trying to think what a good example would be to run this. We're we're not going to be able to see this run to completion because this is going to take way too long. Um, but at least just showing you guys the start of it because then that that's like the full life cycle of like we had an idea for a workflow, we had Archon research how to build it, we built it, and then we run it. Like it's that easy to build anything. And so maybe what I'll do is I'll run GSD to handle a GitHub issue. I guess we could do that. Um, or no, you know, here's what we'll We'll have it we'll have it create uh the PI agent like okay I want you to uh run the GSD workflow here to build support for the PI agent SDK into archon as the third coding agent. And then uh let me make sure I knew it would say that wrong. PI agent SDK I could do open code. I could handle an issue. I I could do whatever. Right. This GSD workflow is very general. It's going to walk us through this very comprehensive process to build anything. So there we go. So we'll have it kick off the the CLI here. So we can monitor it in the web UI. We could even kick this off from the web UI as well. And I know I haven't really showed that in this live stream here, but we can run our workflows directly from the web UI as well. Like for example, check this out. I can go into the chat here and I can say um use the archon assist workflow to summarize the readme for archon. So I just want to do kind of like a a faster example here. But anything that we're doing from the CLI where we're asking claude code to invoke the CLI, we can just do it right from the web UI. So if you want to like have this deployed to a VPS running remotely, you can definitely do that. So you can see that it dispatches the workflow. It picks the so it routes to the right repository out of our registered projects because it has knowledge of all of that injected into its context. And then we can also view the logs for the workflow in real time as well. This is just a simple single node workflow. obviously but yeah we'll get the results here and then we can see that uh populate in the chat as well. So this is like the the main chat here is like your orchestrator, right? And then you can click into the logs for any individual workflow. Uh I don't know why that had that blip there, but yeah. Anyway, so you can click in and view the logs for individual workflows. Um and then here, let me click in. So we have our um GSD workflow running as well. So we can view the logs for this. We can see that it is currently in the middle of we can see that the like loading indicator for all of the initial research. So all these four are running in parallel right now and we can see the logs coming in in real time right here as it's going through all the tool calls. So basically all the tool calls from these nodes running in parallel are just being pushed here if we want to see what they're doing. Pretty cool. Uh yeah, this will definitely take a while to go through this process. But I I am actually keen on going through this full GSD workflow. I'm going to end with a poll request for the PI Asian SDK and then I'll I'll circle back with Raasmus and see what he thinks if this was actually a good implementation because he's working on this as well. Um, but yeah, I I might actually push this GSD workflow as one of the default bundled ones because I think it's just such a good example of how we can take a harness that's already out there and build it into Archon. Not that there's necessarily a huge reason to use Archon over just running GSD directly, but more just to show how like Archon goes above any existing harness because it allows you to build any of them. That's the power of it. All right. Um, okay. What if this could also be task centric? Pick the right workflow and the workflow combinations according to the task. I mean, you can basically already do that because you can have Archon load the Archon skill, look at all the workflows that it has access to, and then you can describe a larger scope of work and have it figure out the workflows to run. Or maybe it's just like a single workflow because you can't wrap up your entire process. But I like where your head's at with that because I mean, yeah, certainly. And like this kind of gets into um integrating Archon with your second brain. Your second brain, it learns how you work over time, right? So it kind of knows like based on Cole how Cole likes to work, I think like these archon workflows are what we should invoke to like handle this thing he wants to build. So that's definitely like a different discussion for another day. But I I could do a whole live stream or a whole Dynamus workshop on that. All right. Very cool. So yeah, while we wait for this to run here uh to for it to get to the next step, I'm going to chat about Dynamus with you guys really quick here as well. Oh, look. It looks like two of the workflows ran or the nodes are done. So, there's just two more we're waiting on here. But yeah, um Archon, a lot more workshops coming in in the Dynamus community soon here. And then also we got Okay, man. This 4hour workshop that I did last week in Dynamus went so incredibly well. Like there there are dozens of people in the community that are building their second brains right now and like sharing what they're doing and like how they're adapting things to be more specific to them. Like there's so much energy in the community right now for people building their own second brains and like going off of like the template that I gave in the workshop. It's so cool to see. So if you want to be a part of that like here I'm going to I'm going to put a link to to this in the chat here. There's a a special that I'm running for just this live stream. So, if you go to the link here, we got a special 10% off the uh the usual price for the community. And this special is going to end once the live stream is done. So, this is your chance to join the community and get in on everything that I'm doing more workshops for Archon coming and uh also the whole like third course that I'm adding to Dynamus for the second based on the second brain boot camp. And then I got the AI agent mastery and agent coding courses as well. Um, so yeah, all of everything that I'm doing with Archon, I've used all of my strategies that I cover in the Agentic coding course in order to build Archon. So I definitely um I don't just like, you know, say do as I say, not as I do, right? Like I I actually like use all the approaches every single day that I cover in the courses and the workshops I do in the community. So I'd love to see you join the community. And uh uh yeah, again, for everyone who's in the community in the stream already, always appreciate your guys' support and being here. So, all right, let's see where we're at now. Um, okay. So, it's still running actually. Let's see. Thought the research would be done by now. Um, oh no. Okay, it's almost getting there. So, well, no. Oh, the research is done, but it has to create the plan before it gets our approval. So, we haven't reached the next approval step yet, which is why the workflow is um still running in the background. But once it's done and it gets to the first human approval gate, then the workflow will pause and we'll get some output here questions for us or whatever. Like it'll give us the plan to review if we want. All right, cool. Um why define a model in the workflow? But what if we want AI to judge the model on the fly based on complexity? That's a that's a very fair question. So the main reason is how do you tell like the the the main AI agent that invokes the workflow? It doesn't really have a good idea of how powerful the models are. And it's a really tricky problem to solve. like how do I describe what haiku is capable of or what sonnet is capable of like you'd have to be very confident in your prompting in order to like really like give that control to the agent which is why we haven't really built that at this point. Now if if you do want to like really take your time to build out some kind of framework for the agent to figure out like how powerful each model is or like you tell it how powerful each model is so it can figure out what nodes need what models. you definitely could leave it up to the agent and and um that's definitely something we thought about adding support for is making it so that instead of it being hardcoded for each node, it's like the agent reads the workflow, picks the model for each step, and then sends it off based on the specific task because maybe the research for one specific implementation is actually going to be very complicated. So, we would want to use Opus for the research and then maybe we only need Sonnet for the verification because we think the research is going to be good enough. I don't know. I'm just kind of throwing a random example out there, but definitely like that could be a really good addition to Archon. All right. Super cool that I can use my subscription with this tool we'll be driving in today. Yeah, sounds great. And yeah, it it's fantastic. It if I couldn't use my Anthropic subscription with Archon, I would be using Codeex instead with Archon 100%. Yep. Okay. So anyway, the workflow completed its first three phases and it's now paused at the requirements approval gate. Very good. So here's what it finished and um now it's saying do the requirements look good. So obviously I need to know where the requirements are. That might be something that I need to address. So the workflow didn't like clearly state where the requirements are. So I I have to ask it. I mean that probably something I should improve in the workflow. So keep in mind that like just like your code bases, when you use Archon to build a workflow, it probably isn't going to be perfect first time around. You're going to have to iterate on the prompting and the nodes. So like right here, it's kind of annoying that I have to ask like, you know, where where's the requirements document? Like give me the exact path so that I can actually read through this. Um because right now it just kind of left me in the dark. So I mean, it's not a huge deal that I just asked for the path, but it's a little annoying. So let's get that then we'll actually take a look quick. Okay. So, this here is the path to it. Okay. So, I'll open this up in my IDE and we'll go to the summary. I think yeah, so I'm I'm building this so quickly live that like I don't have my head wrapped around the whole workflow right now. But I think the summary is is the synthesis from all So, these are like the research documents from each of the agents in parallel. And then this is the the synthesis that I'm going to have to review myself. So we're adding the PI agent SDK as a third AI coding agent into archon along with the existing cloud and codecs. Uh keep findings what already exists. So okay, this is good. This is what I talked about a little bit earlier in the stream. It is going to be so easy to build more coding agents into archon because it just has to reference how we've built things already for cloud and codecs. It's definitely going to oneshot this. So make sure we research PI agent first. We'll create the PI assistant defaults. So just again based off the patterns that we already have for cloud and codecs. We'll implement we'll follow the cloud.ts structure lazy logger async generator to send the query into PI. You guys probably don't care about the details here. I'm actually pretty interested in this. It it really understands what to do here. Um defining uh hooks and MCP and skills. Love that. uh laying out the critical risks as well, like things that we have to make sure we validate and be extra careful with or do more research for. And then it has open questions for us as well. And um so maybe what I'll do right here is I will answer the open questions and then send it off like approve the the workflow to continue with the rest here. So okay. All right. There are some open questions in the summary. I'm going to answer this quickly and then I want you to approve the workflow to continue. So for the PI agent SDK package name u well you know actually I don't know that. So I need you to search the web u for that. Um oh actually none of these questions are for me. These are all things that it has to research. So I I need you to research each of the uh answers to the open questions in the summary and then send that in as context to approve the workflow. Okay. So little bit of a pivot there. I thought it was like questions to align with me, but it was more just like uh you know mechanically how does the PI agent SDK work? So, we'll have it figure these things out. I thought that it would find those things in its own research, but I guess it's just like these are the gaps in the research that weren't covered by the other agents. So, yeah. Okay. So, it'll research these and then fill it in and then continue the workflow. So, it's pretty cool. We have a combination here of like we continue to work with Claude ourself and then we like pass context into the workflow when we want to continue it. And like that's the flexibility that I love with Archon is we aren't like once we send off the workflow as long as we have human approval gates. We don't have to just like let it go blindly and then end with that like final result. like we get to work with it along the way and even talk to our main Asian orchestrator to help us like guide the workflow if we really want to make the process reliable and how we usually work. So it takes a bit more time to do that, but in the end it's going to save you time when we have a process that's so elaborate like this with the human approval gates and everything. All right, cool. Um, okay. So, one thing I got to be honest with you guys on is uh the stream is going on so long that I I don't think Oops, I didn't mean to do that. Uh I don't think I'll be able to do the Dark Factory stuff today, but I might do, you know, I probably will do a separate live stream uh next week for the dark factory stuff. This is going to get very involved. So, I did a lot of prep for this. I'm like really excited for this, but it would take me at least another hour and a half to like go through the whole setup here with you guys. Um, and I've just had such a blast like helping you guys understand the value propositions of Archon and how to use it and how to build workflows and going through all your questions. I really appreciate all of your guys' questions today. And so I I'd much rather like focus on on that and have more of an introduction to Archon live stream versus like trying to force in this really fancy dark factory thing that's going to be quite involved. Um, okay. So cool. Now we got the research sending into the workflow. We'll let that run in the background. So I hope that sounds good to you guys because I I might also make a YouTube video on the dark factory stuff as well. I think that'd be super interesting. Um just to like maybe even kind of do like a build in public series where I show like how I'm setting up the archon workflows to manage different parts of the dark factory. How I have the code base kind of like self-evolve with AI managing literally all of the code review and codew writing. I think that could be cool. So, I'm curious what you guys think as well if you like the idea of that. Um, yeah, a lot of lot of ideas I have swimming around in my mind right now for content for the next week. A lot of exciting things with Archon and Second Brain content and just general strategies for AI coding. Okay. Wow, the workflow is already done. Is there another human approval gate? Let me see what Oh, curious what happened here. Oh, it's now in the discussion phase. It's reasking the open questions because the research answers didn't fully propagate the discussion node. Oh, okay. There might have been a problem in the workflow. So, again, there always option or opportunities to improve your workflow when you run it for the first time. Okay, let's check what our usage is at right now. Okay, we're at uh 60%. Not bad. We've been doing a lot with with Archon workflows this live stream and we've only you we've used about 43% of our 5h hour limit in this live stream, but there's a lot of work. We we handled five or four GitHub issues, validated them entirely. We're running a GSD workflow and there's a ton of other stuff that I've been prompting with Claude to like create workflows and stuff as well. Like it's pretty token efficient. So when you create your own workflows, just be careful that you're not using Opus for literally everything if you're using quad code or or make sure you're not using like the high reasoning GPT 5.4 codecs if you're using codecs uh for everything. So, but as long as you're for the pro the nodes that don't require as much reasoning, you're not using like the best model for everything. The workflows can be very comprehensive but really token efficient at the same time. Okay. So, there we go. We're we're continuing now in the workflow. All right. So, I think what I'm going to do here is I'm going to answer a couple more questions and then I will um end the stream. I think we'll call it there. But yeah, I definitely want to answer some more questions for you guys. We'll see how far we can get in this workflow here. One thing I just realized though is I think my my YouTube chat might be frozen. I might need to refresh. Yeah, hold on. Let me let me do something quick. Sorry, guys. I got to pop out the chat again. pop out chat. Sorry, my my streaming software is being like finicky right now. For some reason, I'm not seeing the chats come in on my other platform. Uh oh, I just lost them all. Shoot. That's unfortunate. Well, I can answer some questions, but I won't be able to show it on my screen. Uh let's see if I can blitz through a couple here. Let's see. Yeah. Oh yeah. So someone mentioned Anthropics advisor mode. Yeah. So I I am interested in building that into archon. So the advisor mode is basically you can use less powerful anthropic models to do like the grunt work the implementation and then you have it like call into a larger model like opus or maybe mythos if that's really going to become a thing for us. And then it like kind of like just asks it for guidance and then it continues to do the implementation or planning or whatever. That's pretty cool. All right. And yes, Joe, you can use and you can use Archon 3 or anthropic subscription. Yep, 100%. All right. Um, can we let the user decide which models he wants to allocate to his task? Um, or is it kind of hardcoded at the node workflow level? So, you can have your coding agent edit the workflow live. Otherwise, it is hardcoded. Not it is something we are interested in adding though support for like defining the models up front or like live during the live execution. Yeah. All right. Um, let's see. What about rag and storing previous questions on SDKs and such? I wouldn't want every workflow that works with Python to search the SDK. So, well, the thing about archon is you can build in your own memory system. Like, if you have a way using git logs or claude mem or or rag like whatever you have for memories for your agent, you can build that into archon workflows because you can give it the skill or the MCP or or just like the prompting for it to use whatever. Um so that the flexibility of archon is like you don't have to abandon any approach or wait for us to support it directly. Like if you want to use linear you can just attach in the MCP or skill or like if you want to use the claude mem framework or beads or whatever like you can build that directly into the uh archon workflow. All right. Uh remind us what is the dark factory. Okay. Yeah. Um I'll I'll bring I'll talk about that for a sec here. So okay the dark factory it's the concept of having a code base that is entirely managed by coding agents. The coding agents handle the coding the reviewing the the pull requests and the releases. And so the only thing that the human gives is the issues for bugs or new features that we're requesting. But there's no human approval allowed. all code just go straight to the main branch once coding agents finish it. And for a public experiment, I'm actually really excited for this. For a public experiment, I want to have a repository that is a dark factory and it's managed entirely by Archon workflows. I think it's going to be so cool and it's going to show the power of Archon because we're going to have workflows to triage issues like figure out which ones we actually want to address and then like do the implementation, do the review, manage the releases, deploy things to production. It's going to be so cool. So, I was going to like maybe get started with that in the live stream today, but there's no way like I gota I got to do that in a separate live stream or maybe even make a YouTube series on it. So, that's what's up with the Dark Factory. It's kind of a silly name, but it's also kind of a really cool name. So, that's what I'm calling it. A lot of people have been like thinking about this kind of thing. There's a use case out there or like a anecdote out there from Strong DM. If you guys have heard of Strong DM, they basically built an internal dark factory. StrongDM dark factory. So, they're they're a uh company that so a strong DM AI lab with a simple premise. how best to maximize building software with AI. So they've created a and this is like more internal so it's not like open source like what I'm going to do but they've built a system where like they are pushing thousands and thousands of lines to production like like humans never review. Not that I recommend that as the way to go to get the most reliable production software but the point is like it's an experiment and I'm really excited to try that out. So that's the plan. All right. Um, can we use local AI? Yeah. So, you can you can have cloud code integrate with Olama directly to use local AI within Archon 100%. I would just uh look into like the Olama or Claude code. They have uh direct integration if you want to look into how to do that. Yeah. What does a dark factory do on a sunny day? Well, you just have no windows. That's what you do. Um, what is the domain idea or function for my dark factory project? Yes. So, this is going to be another big thing. Where is my repo? I have so many things open right now. This is another big project that I'm going to work on. And uh the dark factory is going to be this is going to be the use case for the dark factory. I want to create an application that allows you to basically chat with my YouTube content. So, you can ask questions and it's basically like you're talking to me directly because it performs rag over all my YouTube content. And then for those of you in the Dynamis community, I also wanted to ingest all of my course and workshop content in the community. So, it's basically like your own personal AI coach that has access to all my information and maybe even going so far as to like ingest um you know like community posts and things like that as well. I think this is going to be such a cool example for the dark factory because it's a relatively um complex application like the whole rag pipeline and the searching and the web UI and everything but also it's going to be very easily testable because we can just like test conversations with like the agent browser CLI. So you can have like browser automation for the dark factory to run like every time it does validation on the codebase or like for a specific issue. Um so that this is this is what I'm planning on having as the use case for the dark factory and then it'll also be like a huge value ad to the Dynamus community because then it'll give you like a chat platform to talk and ask any questions about any of the courses or workshops or even like point you to the videos in the courses or the workshops to watch for things that you want to learn. So yeah, I'm really really excited for this. I wish I had time to cover in the live stream today, but yeah, I'm definitely I'm definitely going to have to cover this later, but I'll be using Archon workflows to like guide the entire process of managing issues and pull requests and reviews and things like that. So, it's going to be pretty exciting. And yeah, there there is there's so much content in the Dynamis community that like it's it's hard to like really navigate through it all. I mean, I make it easy obviously to like look through past workshops and I'm always like letting you know like the things that I'm working on and the courses and stuff, but like there's a lot of stuff there. So, I think this is going to be a really big value ad. So, just yet another one of those things coming to the Dynamus community. So, you know, as I end the live stream here, I just want to give a link to this one more time because there is the special discount for Dynamus that's going away when the live stream ends. And so if you're interested in really being on the forefront of archon and AI coding, if you want to be a part of the weekly workshops that I do and the new uh 4hour second brain boot camp that I just did last week, then come join and be a part of the Dynamist community. I would love to have you. So yeah, I know there there's a lot of uh really really good questions that I didn't get to in the chat. It's always unfortunate. I I love doing these live streams and I love all your guys' questions. It's just hard cuz there's like so much. Um, but yeah, if you ever have any questions like feel free to, you know, comment on my YouTube videos as I do more on Second Brain and and Archon content or, you know, always available in the community to answer your questions there. Uh, so yeah, I'm going to go ahead and uh call the live stream here, but stay tuned for more content on Archon and the Dark Factory stuff as I start doing that. It's going to be a really really fun experiment. And yeah, thank you everyone for for being here. This is a really fun live stream. I just I'm so passionate about Archon right now. So, it's really cool to just demonstrate everything to you guys and answer your questions and build workflows live. Uh might even push that GSD1 to the repo if it works well. Probably to, you know, iterate on that though. But yeah, anyway, thank you everyone for being here. I hope that you guys have a fantastic weekend and I will see you all on the channel and in the Dynamus community. Take care everyone.

---

## Timestamped Segments

**[0:04]** All right, we are live.

**[0:07]** Welcome everybody to the Archon live

**[0:11]** stream. We're going to be diving into

**[0:14]** everything with Archon today. So, I

**[0:16]** posted a YouTube video just this week

**[0:19]** introducing the new version of Archon.

**[0:22]** Uh, but now we get to actually go deep

**[0:24]** into using it. And there are a couple of

**[0:27]** things I have up my sleeve today that

**[0:30]** are kind of interesting. So, I'm going

**[0:32]** to be building a what's called a dark

**[0:35]** factory this month. If it sounds spooky

**[0:37]** or interesting to you, we'll talk about

**[0:39]** that more uh in a little bit. Um that'll

**[0:42]** be kind of like the tail end of our live

**[0:45]** stream today. So, yeah, but I want to

**[0:48]** start by actually introducing Archon to

**[0:50]** you guys. Uh just to give a whole, you

**[0:53]** know, overview of the tool. I know that

**[0:55]** I talked about it on Wednesday in the

**[0:57]** YouTube video, but I I want to be pretty

**[0:59]** comprehensive in the live stream today.

**[1:01]** And then we'll build some workflows

**[1:02]** together. I'll show you what it looks

**[1:03]** like to use Archon, how I use it on the

**[1:06]** daily basis, and then we'll get into the

**[1:08]** the dark factory stuff. I'm pretty

**[1:11]** excited. So, uh yeah, I'm sitting down

**[1:14]** right now. I'm like actually like always

**[1:16]** standing in my live streams and my

**[1:18]** YouTube videos, but uh I had a couple

**[1:21]** leg days like in a row. Um, and my legs

**[1:25]** are like toasted right now, so it's

**[1:27]** really It actually kind of like hurts to

**[1:28]** stand right now. It's pretty crazy. Um,

**[1:31]** so yeah, I'm actually sitting down for a

**[1:33]** live stream. I've like never done that

**[1:34]** before. Um, but yeah. Anyway, so I've

**[1:37]** got my left monitor here with all of the

**[1:39]** comments from you guys that I'm

**[1:41]** watching. And then I've got my right

**[1:43]** monitor where I have my streaming

**[1:45]** software. So when you see me look

**[1:46]** around, that's what I'm doing. And then

**[1:48]** obviously I'm sharing my screen on the

**[1:50]** main monitor right here. So, I can

**[1:52]** actually switch to share my screen here

**[1:55]** and then I can pop up chats like this

**[1:58]** right here. Hey, Cole, looking forward

**[1:59]** to this one. I appreciate very much.

**[2:01]** Yeah, so I I was checking out the chat

**[2:03]** as I was getting things started here.

**[2:05]** It's exciting to see uh everyone in here

**[2:07]** already. Congrats on the launch. Love

**[2:09]** seeing the structure for AI workflows.

**[2:11]** Still wrapping my head around its

**[2:12]** potential, you know. I appreciate Thomas

**[2:15]** and I still am as well because it's

**[2:18]** actually kind of crazy. Um, maybe we'll

**[2:20]** talk about this a little bit today, but

**[2:22]** we can use Archon for a lot more than

**[2:24]** just AI coding. Like you can use it for

**[2:27]** any kind of agentic workflow, for deep

**[2:29]** research or any kind of like content

**[2:32]** creation. Um, I'm not going to build

**[2:34]** anything around that now, but that's

**[2:36]** going to be more coming soon in videos

**[2:38]** and future live streams. So, yeah, the

**[2:41]** the possibilities are pretty limitless

**[2:43]** here. And I think as I really introduce

**[2:46]** Archon to you guys right now, you'll see

**[2:48]** what I'm talking about.

**[2:50]** Cool. All good sitting down. You still

**[2:52]** look great, Cole. Appreciate it, Eric.

**[2:54]** Yeah, it feels weird to me, but um yeah,

**[2:58]** I definitely need it right now. It's

**[3:00]** exactly right. Never skip leg day. Yeah.

**[3:03]** So, so I I started doing so I was doing

**[3:06]** a lot of CrossFit last year

**[3:09]** and um I took a break. I just like

**[3:12]** started going to like a regular

**[3:13]** commercial gym and I'm now I'm back to

**[3:15]** doing CrossFit again. And uh the

**[3:18]** workouts were pretty intense last couple

**[3:20]** days for the legs. Um so yesterday was a

**[3:23]** lot of uh Bulgarian split squats,

**[3:26]** jumping lunges, uh wall balls, and um

**[3:30]** and biking.

**[3:32]** So yeah, I'm pretty cooked, but it's

**[3:35]** good.

**[3:36]** Uh all right, cool. So, I'm going to go

**[3:40]** ahead and

**[3:42]** pop up my uh Obsidian vault here. So,

**[3:46]** I've got the diagram to really introduce

**[3:50]** why I built Archon in the first place.

**[3:54]** And I I also want to be clear here. I

**[3:56]** did not build Archon by myself. There

**[3:59]** are a couple of people that helped me a

**[4:01]** lot with Archon. Uh Raasmus and Thomas

**[4:05]** are the two that have really helped me

**[4:08]** the most with the project. Uh Thomas is

**[4:10]** here. He's a DIY smart code. Uh so he's

**[4:13]** here. I see him in the chat. Shout out

**[4:15]** to Thomas. Not sure why there's an echo

**[4:17]** for the stream, Thomas, but yeah, thank

**[4:19]** you for all the work that you've done on

**[4:21]** Archon. Rasmus, I don't know if he's

**[4:22]** here. Uh but yeah, big shout out to him

**[4:25]** as well.

**[4:27]** Um yeah, I don't think he is for today,

**[4:30]** but that's all good. So yeah, I' I've

**[4:32]** had I've had a lot of help building

**[4:34]** Archon and of course I've had a lot of

**[4:36]** help from Claude Code building Archon as

**[4:39]** well. Uh let me tell you, I am using

**[4:41]** Archon to build Archon constantly. I'll

**[4:44]** show you guys what that looks like today

**[4:46]** as well. But let's talk about the

**[4:48]** evolution here. Why we care about

**[4:50]** Archon? Why why did I care about

**[4:52]** building it in the first place? So allow

**[4:54]** me to like talk about this for a little

**[4:56]** bit. U because I really want to get you

**[4:57]** guys on board with the vision that I

**[4:59]** have here. And it is a big vision. So

**[5:03]** it's everyone knows that like prompt

**[5:05]** engineering was a big thing when

**[5:08]** generative AI first became a thing back

**[5:11]** in 2022. So we had like you know the

**[5:13]** release of GPT 3.5 Turbo. That's when

**[5:17]** everyone started giving uh a lot of

**[5:19]** hoots and hollers about generative AI

**[5:21]** and people are obsessed with prompt

**[5:23]** engineering. And the idea behind prompt

**[5:26]** engineering is how can we craft our

**[5:28]** prompts to the LLM to get the single

**[5:31]** best output. So at this point people are

**[5:33]** very much like caring about just uh you

**[5:36]** know that very next turn with the LLM.

**[5:38]** How do we get it to do or output what we

**[5:40]** want?

**[5:42]** And then uh that evolved in 2025 to the

**[5:46]** idea of context engineering. So now we

**[5:48]** don't care about just single outputs.

**[5:50]** Now we care about entire sessions

**[5:52]** especially for AI coding sessions.

**[5:55]** Context engineering is the idea of uh

**[5:57]** you know how can we curate the perfect

**[6:00]** context nothing more than the coding

**[6:02]** agent needs but exactly what it needs to

**[6:05]** uh have all the context it needs to

**[6:07]** plausibly do the task. So this was

**[6:10]** popularized by a lot of people like Toby

**[6:12]** the CEO of Shopify of course Andre

**[6:15]** Karpathy because whenever he posts

**[6:17]** something of course it goes viral. Uh

**[6:19]** but context engineering it's a very

**[6:21]** powerful evolution because it's treating

**[6:24]** the context for our coding agents as an

**[6:27]** engineered resource. So we evolve our AI

**[6:31]** layer as I like to call it just like we

**[6:33]** evolve our code base. So we version

**[6:36]** control our rules and our commands and

**[6:38]** our skills. And whenever there's a

**[6:40]** problem that comes up with our um system

**[6:43]** like there's a bug that our coding agent

**[6:45]** produces instead of just fixing the bug

**[6:47]** and moving on. The idea behind context

**[6:50]** engineering is we look into our process

**[6:52]** like what could we make better with our

**[6:54]** commands or what could we make better

**[6:55]** with our rules so that that issue

**[6:57]** doesn't happen again or at least that's

**[6:59]** the goal of evolving our context. So

**[7:02]** it's a very powerful concept and I

**[7:05]** created a lot of content last year

**[7:06]** around context engineering. Now the

**[7:09]** important thing is these different

**[7:10]** evolutions it's not like they replace

**[7:13]** each other. Context engineering does not

**[7:15]** replace prompt engineering. In fact

**[7:17]** prompt engineering is a part of context

**[7:20]** engineering. So it's it's a evolution

**[7:22]** where it builds on top of itself.

**[7:25]** And so this year we have evolved to

**[7:27]** harness engineering. And this is what

**[7:30]** archon is all about. So harness

**[7:32]** engineering can mean a lot of different

**[7:34]** things, but in essence, a harness is a

**[7:39]** layer on top of the coding agent. It's

**[7:41]** the tooling and the process that you

**[7:43]** build on top of the coding agent to make

**[7:46]** it more reliable and basically taking

**[7:50]** your whole you know process for building

**[7:52]** software

**[7:54]** and you know building the the layer on

**[7:56]** top of the coding agent where you

**[7:58]** enforce that process. So, a lot of

**[8:02]** different strategies out there like BMAD

**[8:04]** and GitHub spec kit and GSD, you could

**[8:07]** consider them harnesses because you're

**[8:09]** you're wrapping the coding agent in this

**[8:11]** higher level layer of your strategy for

**[8:14]** engineering. And we have a stripe

**[8:16]** minions. Uh the Ralph loop is a harness.

**[8:19]** Enthropic has open sourced quite a few

**[8:21]** harnesses. I've covered some on my

**[8:23]** channel. really every single big company

**[8:26]** is converging on the idea of harnesses.

**[8:30]** Instead of focusing on making the model

**[8:32]** better or making the tool better, like

**[8:34]** the coding agent better, it's it's all

**[8:36]** about like how do we create the system

**[8:38]** that wraps the coding agent, right? And

**[8:41]** so there's a lot of studies that have

**[8:43]** been done that have shown like even if

**[8:44]** you are using the exact same model,

**[8:46]** you're not improving the underlying

**[8:48]** model or tool, you can go from a 6.7%

**[8:50]** pull request acceptance rate to almost

**[8:52]** 70%. And the only thing is to harness.

**[8:56]** So building in your strategies around

**[8:58]** context curation and validation and your

**[9:01]** approach for planning, right? Like we

**[9:03]** we'll talk about all that today when we

**[9:05]** cover building harnesses with Archon,

**[9:07]** but it's a big deal. Like uh maybe you

**[9:09]** guys heard of Stripe Minions. This went

**[9:11]** like super viral last month because

**[9:12]** Stripe they built their own internal

**[9:15]** harness. It's kind of like a more

**[9:17]** powerful version of the Ralph loop that

**[9:19]** allows them to ship 1,300 AI only

**[9:22]** generated pull requests every single

**[9:24]** week. And like Claude code itself is

**[9:26]** starting to build a lot of of harness

**[9:30]** into the tool. So not just calling the

**[9:32]** coding agent um you know calling the LLM

**[9:35]** with the coding agent but how can we

**[9:36]** like orchestrate many different cloud

**[9:38]** code sessions together. So like claude

**[9:40]** code has support for agent teams and

**[9:43]** they're doing a ton with sub aents right

**[9:44]** now. So when they had their source code

**[9:46]** leak last month, um it it was shown that

**[9:49]** like 60% of the code is still like

**[9:51]** wrapping the the underlying model itself

**[9:54]** like Sonnet and Opus and Haiku, but then

**[9:57]** 40% of their code is with these more

**[9:59]** like harness features like agent teams.

**[10:02]** And so all that to say, it's the

**[10:05]** direction that all of these companies

**[10:06]** are heading where they're building

**[10:08]** harnesses. The coding tools themselves

**[10:10]** are building this. All of the biggest

**[10:12]** companies like Stripe and Shopify and

**[10:15]** AWS, they're all building their own

**[10:16]** internal harnesses. But the problem with

**[10:19]** all these harnesses is they're not open-

**[10:20]** source and they're not custom to you.

**[10:23]** What if you want to take your software

**[10:26]** development life cycle, your process for

**[10:29]** working with AI coding assistants and

**[10:31]** what if you want to package it up into

**[10:33]** your own harness? Well, that is the

**[10:35]** value proposition of Archon. Archon is

**[10:38]** the harness builder. So, for the first

**[10:40]** time ever, we have an open- source

**[10:42]** platform that makes it easy for you to

**[10:44]** build your own harness. Up until this

**[10:47]** point, you either had to build something

**[10:50]** internally like Stripe did, but

**[10:52]** obviously that's a massive amount of

**[10:53]** effort, or you just had to use a harness

**[10:57]** that's already out there like the Ralph

**[10:58]** Loop or BMAD or whatever it is. And

**[11:01]** like, yeah, those tools are very

**[11:02]** powerful, but they're not custom to you.

**[11:05]** And you you guys know if you've been

**[11:07]** following my content that uh I'm always

**[11:10]** a big proponent of like build it

**[11:12]** yourself. Take inspiration from what's

**[11:14]** already out there. And I'll even show

**[11:16]** you what it looks like to build

**[11:17]** something like a BMAD or GSD harness in

**[11:20]** Archon because we can take inspiration

**[11:22]** from the beautiful minds that are out

**[11:24]** there but still make something that

**[11:26]** works how we want to work. And that's

**[11:28]** the unlock that I have for you guys here

**[11:30]** with Archon.

**[11:32]** And um the other thing that I want to

**[11:34]** cover here is um you know everyone

**[11:37]** already has their own skills and

**[11:39]** commands and rules. So I'm not I'm not

**[11:42]** expecting you to like start from zero. I

**[11:44]** know that you already have a process

**[11:47]** that you built around your AI coding

**[11:49]** assistant. Like you have skills for

**[11:50]** validation. You have commands for

**[11:53]** planning and maybe you have your PRD

**[11:55]** template whatever that might be. And so

**[11:57]** it's not like Archon replaces what you

**[12:00]** already do. It's that Archon allows you

**[12:03]** to package everything together into a

**[12:06]** workflow that combines your skills and

**[12:09]** commands, right? Like the whole idea is

**[12:12]** before you have a harness, you have your

**[12:15]** commands and skills and you have to

**[12:17]** remember the order that you use them.

**[12:19]** You have to work between different AI

**[12:21]** coding sessions because you definitely

**[12:23]** don't want to do your planning in the

**[12:24]** same session where you do your

**[12:25]** implementation because your coding agent

**[12:27]** builds up a lot of bias. But if you

**[12:30]** don't have a harness to connect those

**[12:31]** steps together, you have to be the one

**[12:34]** to orchestrate that. I call it

**[12:35]** shephering, right? Like you you go

**[12:37]** through some kind of PRD process with

**[12:40]** your coding agent. You create a PRD and

**[12:42]** then you're like, "Okay, good. Let me go

**[12:44]** over to a new Cloud Code session or a

**[12:46]** new codec session or whatever and let me

**[12:48]** go and create a plan for the first

**[12:50]** phase." And then you get your plan and

**[12:52]** then you go and you create a new session

**[12:54]** and you go into implementation and then

**[12:56]** you have a new session where you do a

**[12:57]** review on the pull request or on the

**[12:59]** code whatever it is. And so you're still

**[13:01]** even though you have your commands and

**[13:03]** skills and things to automate different

**[13:05]** parts of your workflow, you still have

**[13:07]** to walk the different coding agent

**[13:08]** sessions through each one. And Archon is

**[13:12]** kind of like the next evolution of that.

**[13:15]** It allows you to run longer tasks but

**[13:18]** still keep yourself in the loop. And so

**[13:20]** I have an example here of just what an

**[13:23]** archon workflow can look like. And and

**[13:26]** by the way, if you if you did watch the

**[13:29]** video on Wednesday, I am repeating

**[13:31]** myself a little bit here. So I covered

**[13:33]** this diagram in the video, but uh just

**[13:35]** consider this a refresher if you watched

**[13:36]** it. And I just want to make sure that

**[13:38]** for those of you tuning into this live

**[13:40]** stream who didn't watch the video, I can

**[13:42]** like give you a really solid overview of

**[13:44]** what Archon is. Um, so yeah, here's just

**[13:46]** one example of the kind of workflow you

**[13:48]** can build with Archon. And uh, you'll

**[13:50]** have to excuse the the images are like

**[13:52]** not rendering right now for some reason

**[13:54]** for some of the icons, but my point can

**[13:56]** still be made here. Uh, but yeah, so

**[13:58]** anyway, with Archon, you obviously have

**[14:00]** some kind of trigger for your workflow.

**[14:03]** So, traditionally without a harness, it

**[14:05]** would just be like sending a prompt into

**[14:07]** claude code, right? Like that is your

**[14:08]** trigger. But with Archon, there's a

**[14:10]** quite a few different ways that we can

**[14:12]** use it, and I'll I'll show you guys that

**[14:13]** today. We have the CLI so we can have

**[14:16]** our cloud code or codeex whatever um

**[14:19]** instance like trigger an archon workflow

**[14:21]** so we can dispatch work to delegate

**[14:24]** behind the scenes so we can do a lot of

**[14:26]** work in parallel. I also have a whole

**[14:28]** web interface and uh I'll definitely

**[14:31]** show that off today as well. Uh that's

**[14:33]** the wrong link. This is it. So we have

**[14:35]** the whole web interface where we can

**[14:37]** manage our workflows

**[14:39]** and we can uh kick off workflows

**[14:43]** uh from the web UI directly. And uh so

**[14:46]** there's basically like a a coding agent

**[14:48]** sitting behind the web interface. So we

**[14:51]** can ask it to do work on our different

**[14:53]** repositories that we have registered

**[14:55]** with archon and it'll automatically

**[14:57]** route the request. it'll pick the right

**[14:59]** workflow and it will dispatch it and we

**[15:02]** can do a ton of workflows in parallel if

**[15:04]** you want as well. So I'll I'll show you

**[15:06]** all of that today. But we have the web

**[15:08]** UI and then we even have different

**[15:09]** adapters so that you can for example

**[15:12]** talk to Archon directly in Slack. So you

**[15:14]** can say like hey there's a GitHub issue

**[15:16]** for um this repo go and you know handle

**[15:20]** that issue. I want to see a pull request

**[15:21]** in the end with a fix for that issue.

**[15:23]** And you can do that through Slack. And

**[15:25]** we have different conversations that you

**[15:27]** can manage through different threads in

**[15:29]** Slack. So for every single platform, we

**[15:31]** support parallel execution. Archon

**[15:34]** handles work trees and isolation under

**[15:37]** the hood. So you don't even have to

**[15:38]** worry about it. That's one of the other

**[15:40]** big unlocks with Archon is how it

**[15:42]** supports working on things in parallel.

**[15:44]** And so I can go into my clawed code and

**[15:47]** I can have it use the CLI to fix eight

**[15:50]** GitHub issues at the exact same time.

**[15:52]** and they all run in different work trees

**[15:54]** so they don't step on each other's toes.

**[15:56]** They don't override each other's changes

**[15:57]** and we don't have to deal with merge

**[15:59]** conflicts just to get the pull requests

**[16:01]** created. It's really powerful. And so we

**[16:03]** start with our trigger and then um again

**[16:06]** this is just an example of a workflow we

**[16:08]** can create. So we could go like into

**[16:09]** planning mode. So maybe there's a new

**[16:11]** feature that we want to build. We want

**[16:13]** to start by going through the planning

**[16:15]** process with our coding agent. And so we

**[16:19]** have a step in our archon workflow where

**[16:22]** we are prompting our coding agent like

**[16:24]** here is the feature we want to build.

**[16:26]** Now help me plan like do research, do

**[16:28]** codebase analysis, whatever that is. And

**[16:30]** when in archon we can add in human in

**[16:33]** the loop. And so we can have essentially

**[16:36]** a loop here where we give feedback to

**[16:38]** have the coding agent revise the plan

**[16:40]** until we approve it and then it moves

**[16:42]** into the coding stage. And we do this in

**[16:44]** a brand new coding agent session because

**[16:47]** your planning session can get pretty

**[16:48]** bogged down and you can build up a lot

**[16:50]** of bias over time. And so you want to

**[16:53]** produce an artifact that you send into

**[16:56]** the next node for implementation.

**[16:59]** If you're in the Dynamis community, this

**[17:01]** is the piv loop. You know what I'm

**[17:02]** talking about. I've covered it on my

**[17:04]** channel as well. The plan, implement,

**[17:05]** validate. And we used to have to do that

**[17:07]** between different coding agent sessions,

**[17:09]** but now we can package this all up as a

**[17:11]** single archon workflow. And then after

**[17:14]** the code is done, then we go into the

**[17:16]** testing step. And this is another one of

**[17:19]** the very big value propositions of

**[17:22]** archon. Our workflows do not have to be

**[17:26]** just prompts to a coding agent.

**[17:28]** Sometimes there are steps that we want

**[17:30]** to run deterministically. We want to

**[17:33]** take the control away from the coding

**[17:35]** agent to make sure that our process is

**[17:38]** followed to a T. If you've used any

**[17:41]** coding agent for a good amount of time,

**[17:43]** you know that like sometimes you'll tell

**[17:45]** the coding agent run the tests after you

**[17:48]** write the code and it won't listen to

**[17:50]** that. It's so frustrating. Or it'll do

**[17:52]** some of the testing like unit testing

**[17:54]** and linting, but it won't do the

**[17:55]** endto-end testing. It's so frustrating.

**[17:58]** And so what we can do in Archon is we

**[18:00]** can have certain steps of the workflow

**[18:02]** where we're just running code like we're

**[18:04]** doing some kind of context pulling or

**[18:07]** we're running our tests like we're doing

**[18:09]** right here. We're guaranteeing that that

**[18:11]** happens after the implementation and

**[18:13]** then if there's any failures, we'll

**[18:15]** prompt the coding agent to fix those

**[18:16]** things. So we have like a little bit of

**[18:18]** a feedback loop as well built directly

**[18:21]** into Archon.

**[18:23]** And then after everything passes and the

**[18:25]** coding agent figures that it's done,

**[18:27]** then we have the human approval. And so

**[18:30]** even though we are building longer

**[18:32]** running tasks with archon workflows,

**[18:35]** we're not taking ourselves out of the

**[18:36]** loop. We can inject oursel wherever we

**[18:39]** want in an archon workflow. So no matter

**[18:41]** how you typically work with your coding

**[18:42]** agents, if you don't trust it that much

**[18:44]** and you want to validate it every step

**[18:47]** of the way, you can do that if you want.

**[18:49]** We have support built in to the web UI,

**[18:52]** the CLI, every single adapter for human

**[18:55]** in the loop. And that's one of the most

**[18:56]** important things because a lot of times

**[18:58]** when you have these harnesses,

**[19:00]** especially like the Ralph loop, for

**[19:02]** example, the Ralph loop went viral a

**[19:04]** couple of months ago, but to me it felt

**[19:06]** like vibe coding, right? Because you

**[19:08]** were giving it a and it basically an

**[19:10]** entire PRD, like many different phases

**[19:13]** of work, and you would just have a

**[19:15]** coding agent rip through everything. And

**[19:17]** the problem with that is if the coding

**[19:19]** agent makes a mistake in the first

**[19:21]** iteration of the Ralph loop, that issue

**[19:24]** can kind of propagate and like blow up

**[19:26]** from the rest of the loop because the

**[19:27]** coding agent is going to through each

**[19:29]** loop build on top of a code base that's

**[19:32]** already wrong, right? Like not aligned

**[19:34]** with what you actually want to create.

**[19:36]** And so the issues just compound on

**[19:38]** themselves. And so the idea that I

**[19:41]** wanted to be uh very confident in for

**[19:44]** Archon is that it's not just enabling

**[19:46]** vibe coding that we actually have like

**[19:48]** deterministic steps that enforce our

**[19:50]** process. We have human in the loop,

**[19:52]** right? And then we have the pull request

**[19:54]** at the end and then we can review that

**[19:55]** ourself before we merge as well. And so

**[19:59]** yeah, that's that's sort of I I like to

**[20:00]** call it the hybrid secret for Archon.

**[20:03]** And um this this sometimes rubs people

**[20:06]** the wrong way, but I actually think it's

**[20:08]** smart to take as many decisions from

**[20:11]** away from the coding agent as you

**[20:13]** possibly can because they're

**[20:15]** non-deterministic. They don't make the

**[20:17]** same decisions every time even if you

**[20:19]** give it the same prompt. And so there's

**[20:21]** a lot of inherent risk with that. The

**[20:24]** biggest reason why a lot of developers

**[20:26]** and companies are hesitant to adopt

**[20:29]** coding agents is because they're

**[20:31]** unreliable by nature. And so Archon is

**[20:34]** the harness builder that allows you to

**[20:37]** take the process that you consider

**[20:39]** reliable and build it into the way you

**[20:42]** work with coding agents. And so we have

**[20:44]** different nodes like if you have your

**[20:46]** testing strategy, if you have your

**[20:48]** strategy for like pulling information

**[20:50]** from Confluence, like whatever steps you

**[20:52]** have that like you want to have

**[20:53]** performed every single time, you build

**[20:55]** those nodes into Archon. And then the

**[20:57]** rest of the workflow is still going to

**[20:59]** be like you adding in your commands and

**[21:01]** skills and sub agents. Like everything

**[21:02]** that you already have, you can build in.

**[21:04]** So you're not losing anything either.

**[21:06]** That's another thing that I want to be

**[21:07]** very clear on here is that you don't

**[21:10]** have to replace how you already work.

**[21:12]** Archon just allows you to package it up,

**[21:14]** right? Like that's the goal of a harness

**[21:16]** builder. So I'm I'm so excited for this

**[21:20]** and I'll I'll actually like install it

**[21:22]** from scratch with you guys today as

**[21:23]** well. So, uh, right here I got the link

**[21:26]** to Archon. I'm going to go ahead and

**[21:28]** drop this in the chat.

**[21:31]** So, if you guys want to,

**[21:35]** um, try it out right now, even like

**[21:37]** install it along with me, I would highly

**[21:40]** encourage you to. It's very easy to

**[21:42]** install Archon because we can ask our

**[21:46]** coding agent to set it up and I have an

**[21:49]** archon skill that it loads automatically

**[21:51]** and it'll walk you through the entire

**[21:53]** process even installing the dependencies

**[21:55]** for you. So I'll show you that live in a

**[21:58]** sec. But yeah, it's so easy to get it

**[22:00]** installed.

**[22:01]** Um yeah, so one other thing I want to

**[22:04]** show really quick. So this is the readme

**[22:06]** for the new version of Archon. I want to

**[22:09]** show what a workflow actually looks

**[22:10]** like. So, this might look a little bit

**[22:13]** intimidating, but uh don't worry, you

**[22:16]** can use your coding agent to help you

**[22:18]** build workflows as well. I'll also show

**[22:21]** you that. Um, so this whole like YAML

**[22:24]** structure, it's it's quite beautifully

**[22:26]** simple, honestly.

**[22:28]** And uh but like even even so, like when

**[22:31]** you're trying to package up your entire

**[22:32]** workflow, it can start to look a little

**[22:34]** intimidating. So it's really nice to use

**[22:36]** a coding agent to help you define these

**[22:39]** workflows. But just an example here. So

**[22:42]** within the diagram here, I showed the

**[22:44]** whole like piv loop workflow. And that

**[22:47]** that workflow can be summed up with this

**[22:49]** right here. So this is a a kind of a bit

**[22:51]** of a simplification just so it fits

**[22:53]** nicely in the readme, but it gives a

**[22:54]** good idea here. So you start with the

**[22:56]** node for your planning and then you go

**[22:58]** into implementation and you can see that

**[23:00]** we have we support loops in archon as

**[23:03]** well. So, uh, maybe I can even go into

**[23:05]** the UI. Let's see if I have it run with

**[23:08]** the loop. I want to give like a demo of

**[23:11]** like what it actually looks like. Yeah,

**[23:12]** here we go. So, like we have we support

**[23:15]** loops in Archon. So, by the way, this is

**[23:17]** what the logs look like. When you invoke

**[23:19]** a workflow and you view the logs in the

**[23:20]** web UI, you can see like all the tool

**[23:22]** calls that your coding agent is making

**[23:23]** behind the scenes. You can see like the

**[23:25]** the node flow and like where it's

**[23:28]** currently running. So like we have a

**[23:29]** loop right here that has like a certain

**[23:31]** number of iterations. And if I go to

**[23:34]** like a more fancy one like a GitHub

**[23:35]** issue fix, we can see like you can get

**[23:38]** pretty comprehensive with the workflows

**[23:40]** that you define. This is one of the the

**[23:42]** breadand butter workflows in archon uh

**[23:45]** the fix GitHub issue. So you can throw

**[23:47]** this on any GitHub issue in any

**[23:50]** repository and it works through this

**[23:52]** entire process of uh you know

**[23:54]** classifying the issue. Is this a a new

**[23:58]** feature we have to plan or is it a bug

**[24:00]** we have to investigate? And then it'll

**[24:02]** do some research. It'll fix the issues

**[24:05]** after investigating and then it will

**[24:07]** validate and then create a pull request

**[24:09]** and review it after. So it's like super

**[24:11]** comprehensive workflow and and yes

**[24:13]** having this many steps does take a good

**[24:15]** amount of tokens. But another really

**[24:17]** powerful thing you can do in archon is

**[24:19]** specify the model the at the individual

**[24:22]** node level. So when you're classifying

**[24:24]** or investigating maybe you only need to

**[24:26]** use haik coup and so it might only be

**[24:28]** the case that like a single node like

**[24:30]** the fixed issue this is the only one

**[24:32]** where we'd want to use opus or we'd want

**[24:34]** to use high reasoning GPT codeex for

**[24:36]** example and so you can make things very

**[24:39]** token efficient by determining at each

**[24:41]** at each individual level what model do

**[24:43]** we want to use and the other really

**[24:46]** powerful thing about harnesses like I

**[24:48]** showed in this diagram here is you get

**[24:50]** insane results building a harness on top

**[24:53]** of a model. So the harness elevates the

**[24:55]** model. I've had better results using

**[24:58]** archon with sonnet than I have using

**[25:00]** opus by itself in cloud code. And so uh

**[25:04]** another really cool thing is like you

**[25:06]** know this um archon kind of comes with

**[25:09]** good timing here because anthropic has

**[25:11]** made their rate limits a lot worse for

**[25:13]** clawed code recently. It's really

**[25:15]** unfortunate, but it's forced me to like

**[25:18]** start using Sonnet more for my coding

**[25:20]** because I hit my rate limits so

**[25:22]** incredibly fast. But with Archon, I feel

**[25:24]** like I'm not really losing the code

**[25:27]** quality, like the output quality because

**[25:30]** the workflows, they package up such a

**[25:33]** comprehensive process and like using

**[25:35]** this whole thing with Sonnet is still

**[25:37]** cheaper than like asking Cloud Code to

**[25:39]** fix an issue by itself with Opus because

**[25:41]** Opus is just so much more expensive. So

**[25:44]** anyway, I got off track a little bit

**[25:46]** showing you guys the web UI here, but

**[25:48]** yeah, so we have the loop like we can,

**[25:50]** you know, implement a plan task by task

**[25:52]** in a loop and then we run the

**[25:53]** validation. And the important thing is

**[25:55]** this is no AI. It is deterministic. So

**[25:57]** we're guaranteed that our validation

**[26:00]** runs. That's powerful. And then we run

**[26:02]** the reviews afterwards. And then we have

**[26:04]** some kind of approval process with a

**[26:06]** human in the loop before we create our

**[26:08]** final pull request.

**[26:10]** And because we have archon as a CLI and

**[26:13]** a skill, when you have it loaded into

**[26:16]** your cloud code or your codeex, all you

**[26:19]** have to do is tell it to use archon. And

**[26:22]** that like literally that's all your

**[26:23]** request has to be and it'll

**[26:25]** automatically dispatch like create an

**[26:27]** archon workflow. So it'll run like let's

**[26:29]** say for example this idea to PR

**[26:31]** workflow. It'll create the work tree

**[26:33]** under the hood so you can keep working

**[26:34]** on your codebase in parallel and then it

**[26:36]** goes through the different stages and

**[26:38]** you can have your coding agent monitor

**[26:40]** the workflow and or monitor it in the

**[26:44]** web UI like I showed right here. So like

**[26:46]** obviously this is a completed run right

**[26:47]** now. But uh if this was in the middle of

**[26:51]** executing you could like see the logs

**[26:52]** come in in real time and see like you

**[26:54]** know like what stage of the workflow the

**[26:57]** coding agent is currently on.

**[27:00]** And as far as as which coding agents we

**[27:02]** support right now, we have support for

**[27:05]** cloud code and then codeex is almost

**[27:08]** done. And then also we are working on uh

**[27:12]** or we want to add in support for other

**[27:14]** coding agents as well. So like right now

**[27:16]** it's claude and codeex but uh we have a

**[27:19]** priority item right now to add support

**[27:21]** for pi as well. So pi also has an SDK.

**[27:25]** Uh we're also interested in AMP and open

**[27:27]** code. I mean really like archon,

**[27:29]** remember archon is the layer above the

**[27:31]** coding agent because it's the harness

**[27:33]** builder, right? So we don't really care

**[27:35]** about what coding agent you're using

**[27:37]** under the hood. We just have to build a

**[27:39]** little bit of support for like calling

**[27:41]** the SDK for the coding agent. So like

**[27:44]** Codeex has the SDK, Claude has the agent

**[27:47]** SDK. That's what Archon uses under the

**[27:49]** hood. So when you use Claude with

**[27:51]** Archon, it is running Claude code. It's

**[27:53]** just running it programmatically through

**[27:55]** the SDK.

**[27:57]** And um so you can you are allowed to use

**[28:01]** your anthropic and codec subscriptions

**[28:03]** with Archon. You don't have to pay for

**[28:06]** API credits. Um and and that's that's a

**[28:09]** very important thing because a lot of

**[28:11]** people right now are getting their

**[28:13]** anthropic subscriptions banned when they

**[28:15]** use it with Open Claw and Open Code. But

**[28:20]** the problem with those they're third

**[28:21]** party harnesses. They're kind of doing a

**[28:24]** workaround to use the subscription. And

**[28:26]** that's against the Anthropic terms of

**[28:28]** service, but Anthropic has made it very

**[28:31]** clear. A couple of their team members

**[28:33]** like posted on X saying that like you

**[28:35]** are allowed to use your Anthropic

**[28:37]** subscription with the Claude agent SDK

**[28:41]** as long as it is for personal use. And

**[28:44]** Archon is for personal use, right? Like

**[28:46]** you're running it on your computer.

**[28:48]** You're hosting it yourself and there

**[28:50]** aren't other people using your subscript

**[28:52]** subscription through a production

**[28:54]** deployed agent. So it's a different

**[28:56]** story. If other people are using your

**[28:58]** subscription through a cloud agent SDK

**[29:01]** agent you have like deployed to some

**[29:02]** production platform then that's against

**[29:04]** the terms of service. But if it's a an

**[29:06]** application you're running yourself and

**[29:08]** is using the claw agent SDK then you are

**[29:11]** allowed. So I've been using my

**[29:13]** subscription with Archon for you know

**[29:16]** months and months now. And the same

**[29:17]** thing with my second brain as well. And

**[29:19]** so they've made that very very clear. I

**[29:22]** don't have the exact tweet up right now,

**[29:24]** so I can't show you the exact thing, but

**[29:26]** uh Boris Churnney, he's the creator of

**[29:28]** Claude Code. He um he clarified like he

**[29:31]** made it super clear like yes, you can

**[29:33]** use your subscription for personal use

**[29:36]** with the agent SDK. So, we're good. And

**[29:38]** I get that I get asked that question all

**[29:40]** the time as I'm doing my second brain

**[29:42]** content on YouTube and I've you know

**[29:44]** started showcasing Archon and it is a

**[29:46]** fair question because um yeah like

**[29:48]** people are really nervous about getting

**[29:50]** their subscription banned but you are

**[29:52]** good with Archon and yeah I see some

**[29:56]** things in the chat here. People are

**[29:57]** excited for the Pi support. Uh yeah I'm

**[29:59]** excited for that as well because then it

**[30:02]** you will have like support for pretty

**[30:03]** much running any model that you want

**[30:04]** with Archon.

**[30:08]** All right, cool.

**[30:11]** Um, all right. So, yeah, I'm going to go

**[30:13]** ahead and uh answer some questions in

**[30:15]** the chat here, and then we'll get right

**[30:18]** into installing Archon. So, I have an

**[30:20]** instance already spun up uh in the

**[30:24]** cloud. I I installed Archon from scratch

**[30:26]** on my computer for the video on

**[30:28]** Wednesday. I don't really want to like

**[30:29]** reinstall it on my computer because I

**[30:31]** already have some things going with it.

**[30:33]** So, I'm going to reinstall it on a Linux

**[30:35]** VPS that I created just in Digital

**[30:37]** Ocean. Uh, but the installation process

**[30:39]** is going to be the same pretty much no

**[30:41]** matter your operating system. So,

**[30:42]** whether you're installing it on a VPS or

**[30:44]** on your Linux, Mac or Windows system,

**[30:46]** it's pretty much going to be the same.

**[30:48]** And the readme has good instructions for

**[30:50]** that. And I'll I'll walk you through it

**[30:51]** right now as well. But yeah, before we

**[30:53]** do that, I'm going to uh switch here to

**[30:56]** my full frame. Uh, let's let's chat a

**[30:59]** little bit. So, I'll I'll pop up some

**[31:00]** questions in the chat here and uh spend

**[31:04]** some time for a Q&A.

**[31:08]** All right. Uh Jared said, "He said the

**[31:10]** magic words, customize BMAD for

**[31:12]** inspiration in a custom workflow."

**[31:14]** That's exactly right. Um so it works the

**[31:17]** way you need it, just the way I need it.

**[31:19]** This is fire. What I've been looking

**[31:20]** for. Yeah, I appreciate it a lot. Um,

**[31:24]** and that exactly like that's that's the

**[31:25]** thing is you can just like fork BMAD and

**[31:29]** you can just run it and change it

**[31:31]** yourself, but that's a lot more involved

**[31:33]** than creating an Archon workflow. I'll

**[31:35]** show you in a little bit what it looks

**[31:37]** like to customize um a workflow taking

**[31:40]** inspiration from something like BMAD.

**[31:42]** I'm going to use GSD as an example

**[31:44]** because it's a bit simpler and easier to

**[31:46]** do, but you could do the same thing with

**[31:47]** BMAD.

**[31:51]** Um, all right.

**[31:55]** So basically, we could call archons

**[31:58]** stripe minions but open source. Exactly.

**[32:01]** Yep. And I'd even go further to say that

**[32:03]** like stripe minions is just a single

**[32:05]** harness. Archon can allow you to build

**[32:07]** anything like Archon allows you to build

**[32:10]** stripe minions but for your company or

**[32:12]** yourself. Yeah.

**[32:16]** Um, can a node be simply an execution

**[32:18]** node? No AI model used? Yep. Yep. So we

**[32:21]** have support for running uh bash, python

**[32:24]** and typescript scripts. So anything like

**[32:27]** any part of the workflow where you're

**[32:28]** like I want this thing to happen exactly

**[32:30]** like no AI model to mess it up then you

**[32:33]** can run it as a node in archon. Yeah.

**[32:37]** Uh where does this differ from n? You

**[32:40]** know uh that's a really good question

**[32:42]** actually. Here I'm going to switch uh

**[32:44]** back to my scene here. I'm going to

**[32:45]** share my screen because if we look at

**[32:47]** the the builder here and u sorry I'm

**[32:50]** going to the wrong tabs. We're actually

**[32:51]** adding support soon for a visual

**[32:53]** builder. So you can like connect the

**[32:55]** nodes like this. And so it is going to

**[32:58]** be kind of similar to N8N. In fact, in

**[33:00]** the readme here, we say think N8N but

**[33:04]** for software development. And so for

**[33:06]** those of you who use N8N or have used it

**[33:08]** in the past, this might actually click

**[33:09]** really nicely for you is like N8N

**[33:12]** doesn't really have direct connections

**[33:13]** with cloud code and they don't have

**[33:15]** things like workree isolation support,

**[33:17]** right? Like you don't use N8N for AI

**[33:19]** coding. You use it to build automations

**[33:21]** for your business, whether it's like LLM

**[33:23]** workflows or not. But u Archon is going

**[33:27]** to allow you to build kind of like n

**[33:31]** workflows, but specifically for AI

**[33:33]** coding. So you're stringing together

**[33:35]** these coding agent sessions and

**[33:37]** deterministic steps like bash and python

**[33:40]** scripts. And it's for coding processes.

**[33:43]** Uh, and so like there's a lot of things

**[33:45]** we have built in behind the scenes with

**[33:46]** Archon for how it integrates with our

**[33:48]** different coding agents and handles work

**[33:50]** trees and things like that that N8N

**[33:52]** doesn't have at all. So like there's no

**[33:54]** way you could build this kind of thing

**[33:56]** in N8N. You're you're not going to be

**[33:58]** able to build a coding agent harness in

**[34:00]** N8N or at least it'd be very difficult

**[34:01]** and not really what the tool is meant

**[34:03]** for. Um, so this is a very different use

**[34:05]** case, but you can think of it like N8N

**[34:08]** for AI coding. So yeah, I appreciate you

**[34:10]** asking that.

**[34:13]** All right.

**[34:16]** Um, how can we know that the plan step

**[34:18]** is complete? Do we have human an

**[34:20]** approval gate for that? Uh, yes. So, you

**[34:24]** can have the coding agent decide itself

**[34:26]** that the plan is complete or you can

**[34:28]** make it so that you have to approve. And

**[34:31]** so, like going back to the diagram here,

**[34:35]** this step right here is what you're

**[34:36]** talking about like planning. And so what

**[34:39]** it does is it'll output some artifact

**[34:42]** and you can have I know that I only show

**[34:44]** the human approval gate here, but you

**[34:45]** could like add that as a node right here

**[34:47]** as well. So like you get to look at the

**[34:49]** artifact and it'll like give you a

**[34:51]** summary of it or it'll give you like the

**[34:53]** full file. So you can like go through

**[34:54]** the markdown if you want and then you

**[34:57]** can give feedback. So you can say like

**[34:59]** hey you didn't do enough validation,

**[35:01]** right? So or like you didn't add enough

**[35:03]** u planning around validation. So like go

**[35:05]** back edit the plan and then let me

**[35:06]** review again. So you can add that for

**[35:09]** any step in Archon or you can have it

**[35:11]** just decide itself. Like if you want it

**[35:13]** to be a little bit more hands-off, like

**[35:15]** you want to do something like the Ralph

**[35:16]** loop, which by the way, we have a Ralph

**[35:18]** loop workflow built into Archon for you

**[35:21]** to use out of the box. Um then you don't

**[35:23]** have to have the human in the loop. Like

**[35:25]** you can have it kind of like iterate by

**[35:27]** itself and kind of critique itself and

**[35:29]** then decide when it's ready to move on,

**[35:32]** which obviously that's a bit more or a

**[35:33]** lot more non-deterministic, but you can

**[35:36]** do whatever you'd like. And um speaking

**[35:38]** of that, actually like workflows in

**[35:40]** Archon, we have a lot of Archon

**[35:42]** workflows that come shipped with the

**[35:44]** platform. So when you install Archon,

**[35:47]** all of these workflows here are ready

**[35:50]** for you to use immediately. So you can

**[35:52]** build your own. If you want to create

**[35:53]** your own harness, build your own

**[35:54]** workflows, you can. But if you just want

**[35:56]** to poke around with Archon initially, I

**[35:58]** have all of these ready for you guys to

**[35:59]** use. So we have like a human in the loop

**[36:01]** interactive PRD to like walk you through

**[36:04]** creating PRDs. Uh we have the whole like

**[36:07]** plan to pull request. We have the Ralph

**[36:09]** loop one if you want to do the Ralph

**[36:11]** loop in Archon. It's actually like a

**[36:13]** beautifully simple workflow. Most of it

**[36:15]** is just prompting here, but it'll walk

**[36:16]** you through like creating the PRD. It'll

**[36:19]** validate it and then it'll go through

**[36:20]** the whole Ralph loop and like manage the

**[36:24]** state through uh like JSON and markdown

**[36:26]** files just like the Ralph loop does, the

**[36:28]** original Ralph loop. Uh what else do we

**[36:31]** have? We have the uh GitHub issue fix.

**[36:33]** This is the one that I use the most out

**[36:35]** of all of the workflows in Archon

**[36:37]** because I'll I'll throw this on the

**[36:39]** issues that we have in Archon. Like I'll

**[36:41]** I'll say like, "All right, Claude Code,

**[36:43]** uh, we have a few people that have just

**[36:45]** opened up issues for Archon. We got, you

**[36:48]** know, like 10,82, 80, 76, 72. I want you

**[36:51]** to spin up four GitHub issue fix archon

**[36:54]** workflows in parallel and then monitor

**[36:56]** them and let me know when they're done

**[36:57]** and I can review the poll request." Or I

**[36:59]** could even have it like run the validate

**[37:01]** PR poll request after as well. Um, so

**[37:04]** yeah, like I said, I'm always using

**[37:05]** Archon to build Archon.

**[37:10]** All right, visualization is fantastic. I

**[37:13]** appreciate it. I assume you're talking

**[37:14]** about the the web UI here, but yeah,

**[37:16]** there's a lot of work that we've been

**[37:17]** putting into the visualization here.

**[37:21]** Um, can I use this with open code? Uh,

**[37:24]** yeah, so not yet, but we want to add

**[37:25]** support for open code. So pretty much

**[37:28]** Archon is going to be able to be

**[37:30]** integrated with any coding agent that

**[37:33]** supports an SDK. So like like I said

**[37:36]** with Cloud, we have the agent SDK.

**[37:37]** Codeex has their SDK, PI has one, Open

**[37:40]** Code has one, and AMP has one. Uh Gemini

**[37:43]** CLI does not. That's another one that I

**[37:46]** wish I could add, but they don't have an

**[37:47]** SDK. Um now you can just run the coding

**[37:50]** agent in headless mode, but uh it's it

**[37:53]** works better to use the coding agent

**[37:55]** programmatically. So this entire

**[37:57]** codebase is Typescript

**[38:00]** almost entirely TypeScript because

**[38:02]** that's the language most of the SDKs are

**[38:04]** written in. So the cloud agent SDK has

**[38:07]** both a Python and TypeScript version but

**[38:10]** Codeex is only TypeScript. So that's why

**[38:12]** I decided to go TypeScript for for this

**[38:15]** codebase here. Um and in the end like

**[38:17]** the actual language you pick doesn't

**[38:19]** matter a ton because coding agents can

**[38:21]** just rock everything, right? In fact,

**[38:23]** Typescript is even a bit better for

**[38:25]** coding agents than Python because um it

**[38:27]** has the type safety built right in.

**[38:31]** All right,

**[38:34]** cool. Um All right. So, yeah, there are

**[38:37]** so many good questions in the chat here.

**[38:39]** It's going to be hard for me to get to

**[38:40]** everything, but I'll answer a couple

**[38:43]** more here and then I'll get on to the

**[38:45]** demo where I'll I'll install it from

**[38:47]** scratch with you guys and show you how I

**[38:49]** use it on the day-to-day.

**[38:51]** Um, why have you made this open source?

**[38:55]** That's a good question. So, open source

**[38:58]** has always been a really big part of my

**[39:00]** ethos. So, as I created started creating

**[39:02]** YouTube content um, in 2024, I I really

**[39:07]** just had a passion for sharing my

**[39:09]** knowledge and everything that I'm diving

**[39:11]** into with the whole world. And open

**[39:13]** source is my way to share it the most I

**[39:16]** possibly can because otherwise if I

**[39:19]** close source it I'm going to tell you

**[39:21]** guys about it but then you won't really

**[39:22]** care because it's either going to be

**[39:24]** some paid product that you have to shell

**[39:25]** out a bunch for or it's meant for

**[39:27]** enterprises or whatever and then like no

**[39:29]** one is going to care about it. So, open

**[39:31]** source is my way to get the most eyes on

**[39:33]** it, which it also is helpful for me

**[39:35]** because then I get the most feedback for

**[39:37]** it. And um obviously like for my

**[39:40]** channel, it helps because then everyone

**[39:43]** has a reason to care about it. If it's

**[39:44]** not something that's open source, I can

**[39:46]** share what I'm building, but then maybe

**[39:48]** if you want to like follow along with my

**[39:49]** journey, that's interesting. But

**[39:51]** otherwise, it's like nothing you can

**[39:52]** really try yourself. So, I feel like it

**[39:54]** just you can be kind of like a brick

**[39:56]** wall you hit. if I make a YouTube video

**[39:58]** on Archon, it's like look at this cool

**[40:00]** thing I built and then you can't even

**[40:01]** try it. It's like what's the point? U so

**[40:03]** definitely like with YouTube being my

**[40:06]** primary like platform for sharing things

**[40:10]** with the world like what I share has to

**[40:12]** be open source in my opinion. So yeah,

**[40:16]** it's a fair question though.

**[40:19]** All right. Um yeah, so another person

**[40:21]** asked about this in NN. So, I talked

**[40:23]** about that already, but yeah, I

**[40:25]** appreciate you guys asking about that.

**[40:28]** Uh, will it include the GitHub CLI,

**[40:31]** GitHub Copilot CLI in the future? So, if

**[40:34]** they build an SDK, yes, but I don't

**[40:36]** think they have an SDK.

**[40:40]** Um, oh, wait a second. Do they actually

**[40:44]** look at this? When was this released?

**[40:48]** They Oh, okay. So there is a SDK. So

**[40:53]** actually we could integrate GitHub

**[40:55]** Copilot with Archon as well.

**[40:59]** That's pretty cool. And yep, they

**[41:00]** support TypeScript, which is what we

**[41:01]** would need for Archon. So yeah, this is

**[41:04]** yet another one. And okay, here's the

**[41:06]** really cool thing. I I haven't really

**[41:08]** talked about this yet too much. I mean

**[41:11]** this gets more technical but um let me

**[41:14]** let me tell you there is so much effort

**[41:17]** that I put into architecting the initial

**[41:20]** codebase for archon before I I ever

**[41:22]** wrote a single line of code. So I have

**[41:25]** like a sort of like generic interface

**[41:28]** implementation for every single adapter

**[41:31]** and every single coding agent. So when I

**[41:34]** built the initial version of archon I

**[41:36]** supported claude and I supported

**[41:39]** telegram. So like Telegram was the way

**[41:40]** to talk to it remotely and Claude was

**[41:42]** the only coding agent but I built it in

**[41:44]** a way where it wasn't like super coupled

**[41:46]** with that specific tool like Telegram or

**[41:49]** Claude. And so when I asked Archon to

**[41:52]** build support for Slack as well as

**[41:54]** Telegram or or GitHub we like support

**[41:56]** you can like talk to Archon directly and

**[41:58]** GitHub issues as well. It just

**[42:00]** one-shotted it like I didn't even have

**[42:02]** to iterate. it built it perfectly and

**[42:03]** then when I asked it to build support

**[42:04]** for codeex like following the pattern

**[42:07]** that I did for claude it oneshotted that

**[42:10]** as well and so if you wanted to create a

**[42:12]** poll request adding support for GitHub

**[42:14]** copilot you could you could literally

**[42:16]** oneshot it because the documentation is

**[42:18]** there the coding agent can reference

**[42:20]** that if you have like claude code open

**[42:22]** up in the archon repository or codeex

**[42:25]** and um and then also like it can just

**[42:27]** copy how we already have it set up for

**[42:29]** an existing coding agent. So we have

**[42:31]** Archon set up in a way where the

**[42:33]** codebase is very easy to evolve because

**[42:36]** everything is set up as like super easy

**[42:38]** patterns to understand like the coding

**[42:40]** agent can understand very easily like

**[42:42]** here's how I add a new coding agent

**[42:44]** here's how I add a new adapter uh

**[42:46]** whatever we want to do to evolve the

**[42:48]** system

**[42:53]** um can workflows be told to obey token

**[42:56]** rates and limits so I think that's

**[43:00]** actually something we have an open issue

**[43:01]** for cuz there's not a way to like set a

**[43:04]** max budget for tokens, but it would be

**[43:07]** pretty easy to add that like on a per

**[43:09]** node level. It's like I want you to stop

**[43:11]** if this is taking more than 100,000

**[43:13]** tokens cuz this that definitely means

**[43:15]** that like the coding agent is going off

**[43:16]** the rails here or whatever. So, we don't

**[43:18]** have support for that yet. But um I

**[43:21]** think I mean I I don't really want to

**[43:23]** like go on a hunt here and try to find

**[43:24]** this exact one, but uh there are there

**[43:27]** is definitely an issue that we have out

**[43:29]** for for that. Let's see if I can find

**[43:32]** it. So mo most of these issues that we

**[43:35]** have right now are actually created by

**[43:36]** uh Raasmus. So like I said, he's one of

**[43:38]** the guys that's been helping me an

**[43:39]** insane amount with Archon. So most of

**[43:42]** these things are like just us kind of

**[43:44]** listing out things that we want to uh

**[43:46]** improve in in Archon.

**[43:50]** Um, we had to port over. So, we were

**[43:52]** working on kind of like a private repo

**[43:54]** that was like just for the Dynamus

**[43:55]** community at one point. So, we had to

**[43:57]** port over a lot of the issues. I don't

**[43:59]** know. We might have changed the names

**[44:01]** for some of them, but that's definitely

**[44:03]** something we have on our radar.

**[44:07]** Um, yeah, not sure if we I can't find it

**[44:10]** exactly right now, but yes, that's one

**[44:12]** of the things is just like all of the

**[44:13]** different parameters that we have in

**[44:14]** like codecs and cloud code. We want to

**[44:16]** make sure that we can support those. So

**[44:18]** you can build it directly into the

**[44:20]** configuration for each node of an archon

**[44:22]** workflow.

**[44:25]** All right. Yeah. And so yeah, one thing

**[44:27]** I I uh want to mention really quick is

**[44:29]** like when we were first working on

**[44:32]** Archon, we were doing it like as an

**[44:35]** internal project in the Dynamis

**[44:37]** community. So we called it the actually

**[44:39]** I still need I still need to archive

**[44:41]** this repository here, but we have the

**[44:43]** remote coding agent. It's funny because

**[44:45]** Archon, the new version of Archon

**[44:47]** started as a a resource that I built for

**[44:51]** the Dynamus Agentic coding course

**[44:54]** because it originally wasn't a harness

**[44:56]** builder. It was just a platform that

**[44:58]** allowed you to talk to cloud code or

**[45:00]** codecs uh in a remote environment like

**[45:03]** Slack, GitHub or Telegram like I was

**[45:05]** talking about earlier. So that's how it

**[45:07]** started and then it evolved into this

**[45:10]** beautiful thing where now you can like

**[45:12]** build any AI coding workflow as an

**[45:14]** archon harness. Uh but this this is like

**[45:16]** the origin of archon. So it's cool for

**[45:19]** everyone in the Dynamis community. You

**[45:21]** guys got to like see it evolve to the

**[45:23]** point where it is now and obviously you

**[45:24]** got early access to it. Another thing is

**[45:27]** um within the Dynamus community, I am

**[45:31]** going to be doing a lot more workshops

**[45:32]** the next couple of months, like getting

**[45:34]** like really deep into using Archon, like

**[45:37]** building custom workflows. I'll show you

**[45:38]** guys more like how to build your own

**[45:39]** harnesses. Um it's it's always the place

**[45:42]** to be if you want to like be a part of

**[45:44]** Archon and get the the inside scoop on

**[45:47]** how to use the tool the best and like

**[45:49]** the evolutions that I'm doing to it. U

**[45:51]** so yeah, I just want to call out really

**[45:53]** quick for Dynamus. I'm going to put a

**[45:55]** link in the chat here. Uh I actually

**[45:57]** have a little live stream special for

**[45:59]** you guys for Dynamis. So it's uh 10% off

**[46:03]** the uh public price for the community.

**[46:06]** This discount here is going to go away

**[46:10]** uh by the time our live stream is done

**[46:12]** here. So it's a special for literally

**[46:14]** just this live stream. So, if you like

**[46:16]** what I'm working on with Archon, if you

**[46:18]** want to be a part of of this and um also

**[46:21]** all the other course content that I have

**[46:23]** in Dynamus, definitely check this out. I

**[46:25]** put the link in the chat just now. So,

**[46:27]** another big thing that I did in Dynamus

**[46:29]** recently is I did a 4hour boot camp on

**[46:32]** building your own AI second brain. So, I

**[46:35]** took the entire second brain that I

**[46:37]** built for myself that literally saves me

**[46:39]** 20 hours a week and I showed you how to

**[46:41]** build it from scratch. So, I did a a

**[46:43]** live workshop and I'm also turning this

**[46:45]** into the third course for Dynamus as

**[46:48]** well. We also have the AI agent mastery

**[46:50]** and agentic coding courses and I

**[46:53]** referenced the Agentic coding course

**[46:54]** already because that was the origin of

**[46:56]** the this new version of Archon. So,

**[46:59]** yeah, lot a lot of value packed into

**[47:01]** Dynamist. I do weekly workshops as well.

**[47:04]** And so, that's where I'll be doing some

**[47:05]** more stuff with Archon if you are

**[47:07]** interested.

**[47:08]** So, all right. Uh, with that here, I'm

**[47:11]** going to go ahead and show you guys how

**[47:13]** to install Archon from scratch. And, uh,

**[47:17]** like I said, I'm going to be doing it on

**[47:19]** a VPS

**[47:21]** just because I don't want to wipe my

**[47:24]** installation on my computer again. I I

**[47:27]** already reinstalled Archon from scratch

**[47:29]** um, four times this week as I was

**[47:32]** testing things to get ready for the open

**[47:34]** source release. And so I'm going to

**[47:36]** install it on the VPS where I'm going to

**[47:39]** build my dark factory. This is the

**[47:41]** exciting like last part of the live

**[47:43]** stream that I'll be covering with you

**[47:44]** guys here. Um yeah, I'm I'm actually

**[47:46]** pretty stoked for this. I don't know if

**[47:48]** you guys know what a dark factory is. Um

**[47:50]** it's kind of like a a term that was

**[47:53]** coined in the last Well, actually it was

**[47:55]** a a term that was coined in the late uh

**[47:58]** 1900s. Uh that sounds weird. Like 1990s,

**[48:02]** I think. Like the idea of a dark factory

**[48:05]** is um you have a factory without lights

**[48:07]** because it's robots running the entire

**[48:08]** thing and then recently people have been

**[48:11]** talking about like dark factory as it

**[48:12]** relates to code bases and basically a

**[48:15]** dark factory is a code base that

**[48:17]** self-evolves like AI is the only one

**[48:19]** writing code ever on the codebase and so

**[48:23]** an experiment that I want to run I'm

**[48:25]** giving you a little bit of a teaser to

**[48:26]** what I'll talk about at the end of the

**[48:27]** workshop here an experiment I want to

**[48:29]** run is a public dark factory factory

**[48:32]** codebase where every single evolution of

**[48:35]** the codebase like every pull request,

**[48:38]** every release is managed by Archon

**[48:40]** workflows because we can build our

**[48:43]** process like we can define exactly how

**[48:45]** we want to manage issues and pull

**[48:47]** requests and releases. We can define it

**[48:49]** as archon workflows. So, we basically

**[48:51]** use Archon as a dark factory harness,

**[48:54]** which sounds kind of it sounds silly,

**[48:57]** but I'm actually like really excited to

**[48:59]** try this as a um kind of like public

**[49:01]** experiment here. Like I I literally

**[49:03]** wanted to get to the point where like

**[49:05]** anyone can create an issue and then I'll

**[49:07]** have Archon like figure out is this an

**[49:09]** issue that we should address for this

**[49:11]** codebase and then it'll handle it

**[49:12]** automatically all the way to like pull

**[49:14]** requests and reviewing and merging into

**[49:16]** the main branch. So, we'll talk about

**[49:19]** that, but obviously we got to get Archon

**[49:21]** uh spun up for the first time here. So,

**[49:24]** I'll show you guys the installation.

**[49:26]** I'll show you what it looks like to run

**[49:27]** workflows with Archon, and then I want

**[49:29]** to build a workflow with you guys, and

**[49:31]** then we'll do some of the dark factory

**[49:34]** fancy stuff at the end. All right, so

**[49:38]** I'm going to go into the read me here.

**[49:42]** So, I'll put a link to Archon in the

**[49:45]** chat again.

**[49:47]** If you guys want to follow along and

**[49:49]** install with me on your machine or a

**[49:50]** VPS, if we scroll down to the get

**[49:53]** started, this is where we're going to

**[49:55]** work right now. So, literally all you

**[49:58]** have to have installed before you run

**[50:00]** Archon is your coding agent and the

**[50:03]** GitHub CLI. In fact, I list bun as a

**[50:06]** prerequisite, but the setup process is

**[50:08]** going to even install this automatically

**[50:10]** if you don't have it yet.

**[50:13]** So, I do list cla code as a prerec. You

**[50:15]** can use codeex as well that's also

**[50:17]** supported with archon. It's just not

**[50:19]** quite as stable right now as cloud code.

**[50:22]** So I'll definitely be updating the docs

**[50:24]** as I address that or as we address that.

**[50:28]** But then obviously the GitHub CLI is an

**[50:30]** important uh dependency as well. You

**[50:32]** don't need the GitHub CLI for every

**[50:34]** Archon workflow, but um yeah, being able

**[50:38]** to work with GitHub is a very core part

**[50:41]** of Archon because most workflows are

**[50:44]** relying on having the issue or pull

**[50:47]** requests be like the starting point,

**[50:49]** right? Like reviewing pull requests or

**[50:51]** fixing GitHub issues. Most of the time

**[50:53]** when I'm working with Archon, it's it's

**[50:55]** dealing with artifacts in GitHub

**[50:57]** essentially, right? So that's why I have

**[50:59]** that as a prerequisite. So once you have

**[51:02]** those things installed, um, we have the

**[51:04]** binary. So we're working on making it so

**[51:06]** there's like a single install script. So

**[51:08]** you can do this if you want. I'm just

**[51:10]** going to show you that my my approach of

**[51:12]** like cloning the repository and setting

**[51:14]** up from there cuz that's what I'm more

**[51:15]** comfortable with. This is like a newer

**[51:17]** thing that we're working on to make it

**[51:18]** like even easier to set up archon. So

**[51:21]** I'm going to install it this way. So

**[51:22]** I'll I'll copy this command to clone the

**[51:24]** repository and I'll do that within my

**[51:27]** VPS here.

**[51:30]** So there we go. Clone Archon and then

**[51:31]** obviously change my directory into

**[51:33]** Archon. And then check this out. So I'm

**[51:36]** going to run in dangerously skip

**[51:38]** permission mode just because I don't

**[51:40]** want to have to deal with approving

**[51:41]** things right now. Open up the folder. Uh

**[51:44]** yes, I accept. There we go. All right.

**[51:47]** Now watch this. All I have to do is say

**[51:49]** setup archon. I don't have to say

**[51:52]** anything else. It's going to walk me

**[51:53]** through the entire process. So if you

**[51:55]** have the prerex and then you clone the

**[51:57]** repo, you just go into your clott codeex

**[51:59]** and you say set up archon and that's it.

**[52:03]** So first it's going to see like what we

**[52:05]** already have set up. It's going to

**[52:07]** realize that we haven't set up anything.

**[52:09]** And then what it should do is it should

**[52:10]** load the archon skill. So we have this

**[52:13]** skill that like walks it through how to

**[52:15]** help us with claude or with the the

**[52:18]** whole setup of archon with claude.

**[52:23]** All right,

**[52:26]** I guess I have to wait for it to to work

**[52:28]** here.

**[52:30]** And by the way, if we see it um I just

**[52:34]** did like control O to see the output

**[52:36]** here. It's just like understanding the

**[52:38]** codebase. I'm actually surprised I

**[52:39]** didn't load the archon skill.

**[52:42]** Um you're in the Let's see. What is it

**[52:46]** saying here? No. All right, hold on.

**[52:49]** Load the archon skill and walk through

**[52:52]** the setup. I've actually never had to do

**[52:53]** this before, but it uh for some reason

**[52:56]** didn't load the archon skill. So, I'm

**[52:58]** just going to tell it to do that, but

**[52:59]** we're still going to get the same effect

**[53:01]** here. It'll be super easy to go through

**[53:02]** everything.

**[53:05]** All right,

**[53:07]** there we go. So, now it's reading the

**[53:08]** setup guide. So, this is like a part of

**[53:09]** the skill that uh tells it how to walk

**[53:12]** us through everything.

**[53:15]** So, it's going to check all the

**[53:16]** prerequisites like making sure we have

**[53:17]** git and bun, things like that, which we

**[53:19]** already do on this machine.

**[53:22]** Um, there we go. So now the first

**[53:24]** question that it'll ask you in the setup

**[53:26]** is where like what's the repository that

**[53:29]** you want to use to work on with archon,

**[53:32]** right? So like when we use archon, we

**[53:34]** want it to invoke workflows on another

**[53:37]** repository because we're going to use it

**[53:38]** to work on something else. So that's why

**[53:40]** it says this should be your own project,

**[53:42]** not the archon repo.

**[53:44]** And so I can either clone a repository

**[53:47]** from GitHub or I can just give it a

**[53:50]** local path if I want it to work on a a

**[53:52]** project that I already have installed on

**[53:54]** my machine. So number two is actually

**[53:56]** probably what you would end up doing

**[53:58]** because usually there's already

**[53:59]** something you're in the middle of

**[54:00]** working on that you want to use archon

**[54:02]** to like build a harness around, right?

**[54:05]** Um now since I'm on a VPS, I am just

**[54:06]** going to clone something from GitHub

**[54:08]** here. So, I will select that. And then

**[54:11]** it just says like, "Please provide the

**[54:13]** repo URL." Um, I need to actually find

**[54:16]** one here. I'll I'll just do Let me open

**[54:19]** this up. I'll pull some like random

**[54:23]** um let's see. Let's just do this one.

**[54:26]** I'll just copy this rep. I just need

**[54:27]** kind of like a random one here to

**[54:28]** register. So, what this is going to do

**[54:31]** is it's going to register your first

**[54:33]** repository with Archon. So whenever you

**[54:37]** um run the Archon CLI on a repo for the

**[54:41]** first time, it will register. So like

**[54:43]** Archon has a database under the hood or

**[54:46]** behind the scenes that like keeps track

**[54:48]** of the projects that you're using Archon

**[54:49]** with and like all the conversations

**[54:51]** you've had where you've invoked Archon

**[54:53]** workflows on those code bases. So you do

**[54:56]** the automatic registration that way. And

**[54:58]** then also in the web UI like I showed

**[55:00]** earlier, you can register projects this

**[55:02]** way too. So you just click the plus icon

**[55:04]** here and then you can give it the GitHub

**[55:06]** URL or the local path. So also in the

**[55:07]** web UI you can register your repos. And

**[55:11]** the cool thing is for all the projects

**[55:12]** that you have registered in the web UI

**[55:15]** the agent automatically understands. So

**[55:16]** if I say like what projects and

**[55:18]** workflows do I have the archon agent

**[55:23]** that runs in the web UI either using

**[55:25]** cloud code or codeex it it has the

**[55:27]** context injected for all of the archon

**[55:30]** workflows it can invoke and the

**[55:32]** different projects that it can invoke it

**[55:33]** in. And so when we say like, hey, I want

**[55:35]** to fix this GitHub issue for this

**[55:37]** project, it will know like, okay, let me

**[55:40]** use the fix GitHub issue workflow and

**[55:42]** I'll route it to the rag YouTube chat

**[55:45]** repository.

**[55:47]** And the the web UI is one of the things

**[55:49]** that we can spin up once we go through

**[55:50]** the setup here. So first it asks what

**[55:52]** platforms do you want to set up? So the

**[55:54]** CLI is always included by default. I can

**[55:56]** also set up uh you know like Telegram.

**[55:58]** you just do, you know, like um enter to

**[56:01]** select or unselect. Uh for this, I'm

**[56:04]** going to keep it really simple and just

**[56:06]** do the CLI. Um yeah, but you you can set

**[56:09]** up like all the adapters that we support

**[56:11]** in Archon right here. So you specify the

**[56:13]** ones that you want and then in a little

**[56:15]** bit it'll go through a process where we

**[56:17]** can give our API keys, but it's a

**[56:19]** separate process because we don't want

**[56:21]** to just send our API keys directly into

**[56:23]** a coding agent or an an LLM. So I'll

**[56:26]** submit these answers here. So I just

**[56:28]** want to set up the CLI so I can run

**[56:30]** workflows there. So the CLI and the web

**[56:33]** UI obviously don't require you to have

**[56:35]** any additional parameters or API keys.

**[56:37]** So they'll just come they'll work right

**[56:39]** out the gate. So then what it does here

**[56:42]** is it creates archon as a global

**[56:44]** command. So that way we can just run you

**[56:46]** know like archon uh workflow run

**[56:48]** whatever. So we can use the CLI to

**[56:50]** invoke workflows. But trust me you're

**[56:52]** never going to do this yourself. You're

**[56:53]** just going to have your coding agent run

**[56:55]** archon workflow. So you don't really

**[56:57]** have to understand the CLI yourself.

**[56:59]** That's the beauty of having an archon

**[57:01]** skill is your coding agent can load the

**[57:03]** skill and then it knows how to invoke

**[57:05]** the archon CLI to kick off workflows for

**[57:08]** you.

**[57:11]** All right. And so now what happens is it

**[57:14]** helps you configure your credentials,

**[57:16]** but it runs this in a separate terminal

**[57:18]** because we don't want our coding agent

**[57:20]** to see our API keys. That would be a

**[57:22]** huge security risk. And so it uh it will

**[57:26]** automatically spin up a new terminal for

**[57:29]** you to go through the setup, but

**[57:31]** depending on your operating system, it

**[57:33]** might not there might not be support to

**[57:34]** like automatically start a new terminal.

**[57:37]** And so uh you might need to just use do

**[57:40]** this yourself. And so for me, because

**[57:42]** I'm running in a VPS, there's no like

**[57:44]** automatic terminal spin up. So I just

**[57:46]** have to connect into the machine again.

**[57:48]** So

**[57:50]** let me do that. So, I gotta uh remember

**[57:52]** the path to my SSH key.

**[57:55]** Uh, there we go.

**[57:59]** Goodness, I can't type today. Gosh. All

**[58:02]** right. And then, um, I forgot the IP of

**[58:04]** my machine. Shoot. What is the IP

**[58:07]** address of my machine here? I'm going to

**[58:09]** pull this up on another monitor here.

**[58:14]** Um,

**[58:17]** all right. Pull this up.

**[58:23]** There we go. Okay.

**[58:26]** All right. So, SSH in and then I will go

**[58:29]** to uh the path here. Dark Factory

**[58:34]** Archon.

**[58:36]** Wait, that's not it.

**[58:41]** Dark Factory. Uh oh, yeah, capital A.

**[58:44]** Okay. All right. So then all you have to

**[58:47]** do in a separate terminal is run the

**[58:48]** archon setup command and it it walks you

**[58:51]** through this here. If it doesn't spin up

**[58:53]** the terminal automatically, you just do

**[58:54]** that yourself. And now we just go

**[58:56]** through the setup process. So I'll zoom

**[58:57]** in on this here. So first, what database

**[58:59]** do you want to use? SQLite is the

**[59:02]** easiest to set up. And so I recommend

**[59:04]** that you can use Postgress though if you

**[59:06]** want to have an external database you

**[59:08]** connect to. Uh which shoot I

**[59:10]** accidentally entered that. So let me go

**[59:12]** through the setup again. So, SQLite and

**[59:14]** then here's where it asks what coding

**[59:15]** agent you want to use. And so, these are

**[59:17]** the two we support right now. Like I

**[59:19]** talked about, we want to add more as

**[59:20]** well. So, space to select and then enter

**[59:23]** to confirm. And then it asks, how do you

**[59:25]** want to authenticate with claude? And

**[59:27]** so, there's three options here. We can

**[59:29]** give an ooth token like if you want to

**[59:31]** just run, you know, the claude like

**[59:33]** setup- token command and get an ooth

**[59:35]** token. You can give your API key, which

**[59:36]** I wouldn't recommend because it's going

**[59:37]** to get expensive. And then like I said,

**[59:39]** we are allowed to use our enthropic

**[59:41]** subscription with claude code with the

**[59:43]** claian SDK and archon. So I'm just going

**[59:45]** to use my global off. So on this

**[59:47]** instance, I've already authenticated

**[59:50]** with claude. If you use cloud code a lot

**[59:52]** and you're installing archon on your

**[59:54]** machine, then the authentication is

**[59:56]** already set, right? Like you don't even

**[59:57]** have to set up any other environment

**[59:59]** variable. And then it asks what

**[1:00:01]** platforms do I want to connect? As in

**[1:00:03]** what ones do I want to enter in an API

**[1:00:04]** key for? I'm not actually going to I

**[1:00:08]** mean I guess I'll just do GitHub right

**[1:00:09]** now just so I can show you one of these.

**[1:00:11]** So you do um space to select and then

**[1:00:15]** enter to confirm. And then what it'll do

**[1:00:18]** is for each of the platforms that you

**[1:00:19]** select that you want to install Archon

**[1:00:21]** with. This is very similar to the um

**[1:00:24]** Open Claw setup. If you guys have

**[1:00:26]** installed OpenClaw before is for each

**[1:00:28]** one of the platforms it'll like give you

**[1:00:30]** instructions like here's how you get

**[1:00:31]** your your GitHub personal access token.

**[1:00:34]** And so I'm going to u off camera

**[1:00:37]** obviously go ahead and uh get that and

**[1:00:39]** copy it. So let me go to

**[1:00:43]** there we go.

**[1:00:45]** So I'll paste it in because it

**[1:00:46]** automatically hides it

**[1:00:49]** which is good. I would want to show that

**[1:00:50]** on the live stream but yeah it gives you

**[1:00:52]** instructions for how to do that. It'll

**[1:00:53]** be the same for every single one of your

**[1:00:56]** platforms that you configure. And then

**[1:00:57]** another thing obviously for the sake of

**[1:00:59]** security is we for each of of the

**[1:01:02]** platforms that we set up like GitHub and

**[1:01:03]** Slack and Telegram we want to have a

**[1:01:06]** commaepparated list of users that are

**[1:01:08]** allowed to invoke archon because if I

**[1:01:10]** have archon running on a public

**[1:01:12]** repository I don't necessarily want

**[1:01:14]** anyone to be able to just say like you

**[1:01:16]** know at archon fix this issue because

**[1:01:19]** then it's spending my tokens and it's

**[1:01:20]** not me invoking it. So I'll just say

**[1:01:22]** like this is the only user that's

**[1:01:24]** allowed to use it. And then you can

**[1:01:26]** change the mention name. So like in

**[1:01:28]** GitHub you do at@ archon and then you

**[1:01:30]** give it the request like that's how you

**[1:01:31]** talk to it. So I'm good with with that

**[1:01:33]** as the default. Um so I don't need to

**[1:01:36]** set up anything separate.

**[1:01:38]** And then the other thing is that also

**[1:01:41]** for that repository that we've we

**[1:01:43]** registered. So this repo that I found

**[1:01:46]** just as like a a random one. Where was

**[1:01:49]** it? Yeah, this one. So like I I gave it

**[1:01:50]** this to register as the first

**[1:01:52]** repository. Um we can also copy the

**[1:01:56]** archon skill into that project. And the

**[1:01:59]** the reason I want to do that is then I

**[1:02:03]** can open up my coding agent directly in

**[1:02:05]** that codebase and since the archon skill

**[1:02:08]** is there, it knows how to use the archon

**[1:02:11]** CLI. So that way I don't have to open my

**[1:02:13]** coding agent in the archon repo in order

**[1:02:16]** to work on another repository.

**[1:02:18]** Because as long as the archon skill is

**[1:02:20]** there, the archon CLI is a global CLI.

**[1:02:24]** So we can invoke it from anywhere on our

**[1:02:26]** machine. Like I can just open up my

**[1:02:28]** terminal right here and just say like

**[1:02:29]** archon, right? And then that

**[1:02:31]** automatically works uh because it's a

**[1:02:33]** globally registered command. But our

**[1:02:35]** coding agent only knows how to use it

**[1:02:37]** like use all the different commands and

**[1:02:39]** options if we have the skill. So I just

**[1:02:41]** want to copy it over into uh the

**[1:02:43]** codebase. So all right. And then uh the

**[1:02:47]** docs directory. We don't have to worry

**[1:02:48]** about that right now. And there we go.

**[1:02:49]** Our setup is complete. And so we go

**[1:02:51]** through all of this and then we go back

**[1:02:54]** here and we just say done. So like we

**[1:02:57]** finished and uh now it's going to

**[1:02:59]** validate all the credentials and make

**[1:03:02]** sure that we're good to go. And then

**[1:03:03]** it'll actually test the Archon CLI. So

**[1:03:05]** it'll run a workflow for us to make sure

**[1:03:09]** that everything is all configured

**[1:03:11]** properly.

**[1:03:12]** So we'll let that run here as well.

**[1:03:19]** All right.

**[1:03:21]** So there we go. Running a quick test

**[1:03:22]** here. So we can see that it is using the

**[1:03:24]** archon CLI. So thanks to the skill, it

**[1:03:27]** knows how to. You never have to worry

**[1:03:29]** about running it yourself. You just ask

**[1:03:30]** the coding agent to do so. So it's

**[1:03:32]** running the archon assist workflow and

**[1:03:35]** it is doing it on our uh repo that we

**[1:03:38]** registered, the first repo that we

**[1:03:40]** registered. And so it's just, you know,

**[1:03:42]** say hello, like a really basic test to

**[1:03:44]** make sure that it worked. And there we

**[1:03:45]** go. It's good. So, yep. I'll copy the

**[1:03:48]** skill over. I guess it asks us here as

**[1:03:50]** well. Maybe that's something to touch

**[1:03:51]** up. Uh, but anyway, so every single time

**[1:03:54]** that you

**[1:03:56]** invoke a workflow from the CLI, it's

**[1:03:59]** going to run as a background process.

**[1:04:01]** So, Cloud Code or Codeex like it has

**[1:04:03]** access to

**[1:04:05]** um the full logs from the workflow. So,

**[1:04:08]** it you can like ask it for a status if

**[1:04:10]** it's a longer running workflow or you

**[1:04:12]** can, you know, say like, "Hey, summarize

**[1:04:13]** what happened in the workflow." like it

**[1:04:15]** it's able to basically you know

**[1:04:16]** communicate with the workflow that it

**[1:04:18]** runs because all the logs are right

**[1:04:20]** there in the background process. So

**[1:04:23]** there we go our setup is complete. So it

**[1:04:25]** tells us what is configured and then it

**[1:04:27]** gives us next steps as well. So take a

**[1:04:29]** look at this. We are immediately ready

**[1:04:32]** to use archon in our codebase now and we

**[1:04:36]** can register it with any other codebase

**[1:04:39]** we want as well. So like I could just

**[1:04:41]** say like you know I'll go into my speech

**[1:04:43]** to text tool here and I'll say like use

**[1:04:44]** the GitHub issue fix workflow to fix

**[1:04:47]** issue number two on u XYZ repository

**[1:04:51]** right like I can send off this request

**[1:04:54]** and it will automatically if if I you

**[1:04:56]** know give it obviously the path to the

**[1:04:58]** repo here it'll use the archon CLI to

**[1:05:01]** run the GitHub fix issue workflow on

**[1:05:05]** this repo and then that also

**[1:05:06]** automatically registers that repository

**[1:05:08]** with archon so So it knows about it

**[1:05:10]** going forward if the repository wasn't

**[1:05:12]** registered already. And then the other

**[1:05:15]** thing is wherever I have the archon

**[1:05:17]** skill copied which if you want to copy

**[1:05:20]** it yourself in the archon repo it's just

**[1:05:23]** within.claude skills. So this and and

**[1:05:26]** I'll put a link to this in the chat

**[1:05:28]** right now as well. This skill which you

**[1:05:31]** can just ask your coding agent to copy

**[1:05:33]** it into your new like whatever repo you

**[1:05:36]** want to start using archon with. But

**[1:05:38]** this skill tells it how to use the CLI.

**[1:05:40]** Like this is literally the only

**[1:05:41]** requirement. So another thing is if you

**[1:05:44]** want to use your second brain with

**[1:05:47]** Archon, all you have to do is put this

**[1:05:50]** skill into your second brain repo and

**[1:05:53]** then it'll immediately be able to start

**[1:05:54]** using Archon workflow. So you can

**[1:05:56]** basically add Archon as the coding arm

**[1:05:59]** for your second brain. So you can create

**[1:06:01]** your own harnesses, your own workflows,

**[1:06:03]** and then you can tell your second brain

**[1:06:04]** to invoke it on whatever repo you you

**[1:06:06]** want. As long as you give it the path,

**[1:06:08]** and it loads the archon skill, then it

**[1:06:09]** knows how to use the CLI.

**[1:06:12]** And so for anything here, if it's like

**[1:06:14]** confusing like, okay, what repo do I

**[1:06:15]** open up or like how do I get the skill

**[1:06:17]** or how do I register projects? Like you

**[1:06:19]** literally just ask Archon and it knows

**[1:06:22]** how to do everything because the skill

**[1:06:23]** walks it through everything. So let me

**[1:06:25]** actually show you this here. So in this

**[1:06:27]** other terminal here, I'm going to um

**[1:06:32]** clear and then so it says I can change

**[1:06:34]** my directory into the claude memory

**[1:06:36]** compiler

**[1:06:38]** and then I can run claude to launch

**[1:06:41]** claude here. So I'll do uh the

**[1:06:43]** dangerously skip permissions again or I

**[1:06:46]** guess I don't here. I'll just have to

**[1:06:48]** type it out manually. So, claw

**[1:06:49]** dangerously skip permissions.

**[1:06:53]** And then, um, you can see that since I

**[1:06:55]** copied over the skill to this repo

**[1:06:56]** during the setup, I can just say load

**[1:06:58]** the archon skill. Not that you have to

**[1:07:00]** say this explicitly every time, but I'm

**[1:07:01]** just demonstrating that like we have the

**[1:07:03]** archon skill in this repo. So, now it's

**[1:07:05]** going to know how to invoke any uh

**[1:07:08]** workflow. And then within the repo here,

**[1:07:11]** okay, we actually have a couple of

**[1:07:13]** issues. Cool.

**[1:07:15]** Uh, this 6pm thing is very edgy. I've

**[1:07:18]** never actually seen this issue before,

**[1:07:20]** by the way. This is a public repo.

**[1:07:22]** Um,

**[1:07:25]** that's okay. Massive token consumption.

**[1:07:28]** Interesting. All right. Well, I'm trying

**[1:07:30]** to find one that's actually like

**[1:07:35]** um seed existing. Okay. Well, let's try

**[1:07:37]** this one. This is kind of random, but

**[1:07:39]** I'm just going to pick a random issue

**[1:07:40]** like number one here. So, like watch

**[1:07:42]** this. All I have to do is say, uh, I

**[1:07:46]** want you to use Archon to fix issue

**[1:07:48]** number one. That's it. It's so simple

**[1:07:51]** because it knows the workflows it has

**[1:07:53]** access to. It's going to pick the right

**[1:07:55]** one, right? Like it's going to pick the

**[1:07:56]** Archon fix GitHub issue. It knows how to

**[1:07:58]** use the CLI. Boom. That is it. And we

**[1:08:02]** have this full process running now. So

**[1:08:04]** Archon fix GitHub issue is running in

**[1:08:06]** the background. It's going to check on

**[1:08:08]** the progress periodically. And um Oh,

**[1:08:12]** hold on. The workflow failed because

**[1:08:14]** you're not logged into the GitHub CLI.

**[1:08:17]** Oh, that's a bummer. Okay, hold on. I

**[1:08:19]** guess I have to do that. I thought I

**[1:08:21]** already did the login here.

**[1:08:24]** Um, let's see. Paste authentication

**[1:08:26]** token. Hold on. I'm going to do this off

**[1:08:29]** camera quick.

**[1:08:31]** Um, I thought I already did that part of

**[1:08:33]** the setup, so it's kind of weird that it

**[1:08:35]** says, but I'm just going to try the

**[1:08:37]** login here.

**[1:08:39]** All right. So,

**[1:08:42]** yeah. See, it says I'm already logged

**[1:08:44]** into this account. I think Claude might

**[1:08:46]** be tripping right now. Uh, let me try

**[1:08:48]** resuming the conversation.

**[1:08:51]** Let's see. Uh, I logged in. Also, it

**[1:08:55]** says I already was. So, I am confused.

**[1:08:58]** There might be something else I forgot

**[1:09:00]** to or I messed up in my configuration on

**[1:09:02]** this machine. Um, let's see.

**[1:09:06]** But it's cool. like it can just rerun

**[1:09:08]** the workflow, right? Like we can just

**[1:09:09]** talk to Claude as we normally would and

**[1:09:12]** so it can use archon as a tool just like

**[1:09:14]** it would use sub agents or just like it

**[1:09:16]** would use skills. Uh it says it exited

**[1:09:18]** again. Um the error is actually from the

**[1:09:21]** claude code off the not logged in is

**[1:09:23]** coming from the claude code agent that

**[1:09:25]** archon spawns.

**[1:09:27]** Um

**[1:09:32]** the check cla

**[1:09:34]** Oh, I think I know what it is. I think

**[1:09:36]** it's because of the

**[1:09:39]** uh it's because of this specific repo. I

**[1:09:41]** have the cloud folder, the

**[1:09:44]** settings.json. If I just remove this,

**[1:09:48]** I might just do the demo on my computer

**[1:09:50]** instead of this VPS because I I think

**[1:09:52]** it's just this specific codebase that I

**[1:09:55]** have some like claw code hooks that are

**[1:09:56]** running. It's a whole thing. Oh, wait.

**[1:09:59]** Oh, wait. I know what's wrong. It's

**[1:10:02]** because I have this already set up to

**[1:10:03]** use Miniax M2.7 for the dark factory

**[1:10:06]** stuff I was going to show you guys.

**[1:10:07]** That's my bad. Ah, okay. I have to I

**[1:10:10]** have to demo this on another machine

**[1:10:12]** here. By the way, we were using Miniax

**[1:10:14]** 2.7 for everything.

**[1:10:17]** Um because I was getting some stuff set

**[1:10:18]** up ahead of time for the live stream

**[1:10:20]** here. Sorry guys, I'm complicating

**[1:10:22]** things more than I

**[1:10:25]** um than I need to because I I'm I have

**[1:10:29]** some other things prepared for you guys

**[1:10:30]** here. So, okay, here's what I'm going to

**[1:10:32]** do. I'm going to show you a

**[1:10:33]** demonstration by doing it right from

**[1:10:35]** Archon. So, um this will be better

**[1:10:38]** anyway because then I can show you guys

**[1:10:39]** the web UI. Uh which by the way, if you

**[1:10:41]** want to start the Archon web UI, all you

**[1:10:44]** have to do is go into the Archon

**[1:10:46]** codebase and say start the backend and

**[1:10:48]** front end of Archon. That's it. Um start

**[1:10:51]** the back end and front end of Archon. I

**[1:10:53]** guess my speech text got cut off, but

**[1:10:55]** that's all you have to do. So I hope

**[1:10:57]** that like the pattern is clear here for

**[1:11:00]** your setup for getting things up and

**[1:11:01]** running for running Archon. It just

**[1:11:03]** comes down to like the Archon skill

**[1:11:06]** guides it through everything all

**[1:11:08]** workflow execution managing the

**[1:11:11]** application super super easy. So within

**[1:11:14]** my archon here, let's go ahead and uh

**[1:11:16]** zoom in a bit. Let's say I just wanted

**[1:11:18]** to handle an issue. So this is going to

**[1:11:20]** be kind of meta because I'm using archon

**[1:11:21]** to improve archon. Uh, but like I said,

**[1:11:24]** you could do this on any codebase where

**[1:11:25]** we have the Archon skill. Um, so I'm

**[1:11:28]** going to find an issue. There's quite a

**[1:11:30]** few issues that have been created in the

**[1:11:31]** last couple of days because we're we

**[1:11:32]** have a lot of eyes on Archon right now.

**[1:11:34]** We're at 16.2,000 stars, which I'm

**[1:11:37]** honored, by the way. Um,

**[1:11:40]** okay. Uh, let's see. So, okay, this is a

**[1:11:43]** good one. So, chat UI fails silently

**[1:11:45]** when the Claude Oath refresh token is

**[1:11:47]** expired. So, this is issue number 176.

**[1:11:50]** So, watch this. I'm gonna go in this

**[1:11:52]** just like I was trying to do in the VPS.

**[1:11:55]** I just have things uh configured. We'll

**[1:11:57]** talk about the Dark Factory stuff in a

**[1:11:59]** bit because I want to use Miniax. Um

**[1:12:02]** anyway, so I'll go in here and I'll say

**[1:12:04]** uh use Archon to fix uh issue number

**[1:12:09]** 176.

**[1:12:10]** There we go. All right. Now, now we'll

**[1:12:13]** see it in action. So, uh again, it'll

**[1:12:15]** load the archon skill. Well, I guess

**[1:12:17]** first it'll view the GitHub issue and

**[1:12:19]** then Yep. load the archon skill so it

**[1:12:21]** knows how to invoke workflows and then

**[1:12:23]** it'll kick off the workflow. So archon

**[1:12:26]** fix GitHub issue and then uh we're doing

**[1:12:28]** it in a branch. So it's going to do this

**[1:12:30]** in a work tree. So we have isolation and

**[1:12:32]** there we go. So now the workflow is

**[1:12:34]** running in a background process. So

**[1:12:36]** cloud code has support for this. I don't

**[1:12:38]** know if codeex does as well because I

**[1:12:39]** haven't used codeex in a while if I'm

**[1:12:41]** going to be honest. But if you click

**[1:12:43]** into the shell here, like if I if I

**[1:12:46]** press the down arrow and then hit enter,

**[1:12:48]** I can see the details and the logs of

**[1:12:51]** the workflow as it's running. So we can

**[1:12:54]** monitor it here. And then the cool thing

**[1:12:57]** is because it runs as a background

**[1:12:58]** process, I can continue. I can run more

**[1:13:00]** archon workflows. I can keep just

**[1:13:02]** talking to the agent here. I can also

**[1:13:04]** say give me a status update. So it can

**[1:13:07]** look into the logs for the background

**[1:13:09]** process and then tell me what stage of

**[1:13:10]** the workflow it's in. So if I want to

**[1:13:12]** check in because this is a longer

**[1:13:13]** running workflow, it can say like oh

**[1:13:15]** it's currently investigating or it's in

**[1:13:16]** the middle of classifying the issue. So

**[1:13:18]** it it reads like I know it looks kind of

**[1:13:20]** long here but this is the the logs that

**[1:13:22]** are stored internally on my machine for

**[1:13:24]** the background process and then it says

**[1:13:26]** all right cool. So work tree is created

**[1:13:29]** it extracted the issue number and it

**[1:13:31]** classified the issue. So it's currently

**[1:13:32]** running the web research step and if we

**[1:13:35]** go to the web UI here I can actually see

**[1:13:38]** that. So take a look at this. We have it

**[1:13:40]** currently running. So I can see it in my

**[1:13:42]** chat. If I go to the mission control

**[1:13:44]** right here, I can also see all of my

**[1:13:46]** running workflows at a high level. This

**[1:13:48]** one is currently running. It has been

**[1:13:49]** for a minute and a half. And if I view

**[1:13:51]** the logs, take a look at this. I can see

**[1:13:54]** what steps have completed, where I

**[1:13:56]** currently am, and I can see the tool

**[1:13:58]** calls as they come in, which a lot of

**[1:14:00]** times for Archon workflows, you're just

**[1:14:01]** going to fire and forget, right? Like

**[1:14:03]** you just want to have it handle

**[1:14:05]** something in the background, and then

**[1:14:06]** you'll come back once there's a pull

**[1:14:07]** request for you to review. So, it's not

**[1:14:10]** like you're always going to be watching

**[1:14:11]** your workflows in the web UI, but

**[1:14:13]** especially as you're building your own

**[1:14:15]** custom workflows. It can be really,

**[1:14:17]** really useful when you're first

**[1:14:19]** debugging things to dive into a workflow

**[1:14:22]** log and like make sure that things are

**[1:14:24]** actually happening as you intend them

**[1:14:26]** to.

**[1:14:27]** And so, we can see the logs. I know like

**[1:14:29]** this one specifically the the web

**[1:14:31]** searching it it's um a longer step but

**[1:14:34]** like we can see all these tool calls

**[1:14:36]** come in live as uh as it's working.

**[1:14:40]** Um and then we can invoke a ton of

**[1:14:42]** different workflows in parallel and we

**[1:14:44]** can watch them all here. We can click

**[1:14:45]** between the logs for them. Uh it's

**[1:14:48]** pretty cool. So yeah and so we can

**[1:14:51]** monitor it here or in the web UI.

**[1:14:54]** And uh you know what? Just for the sake

**[1:14:56]** of of getting kind of fancy here, I'm

**[1:14:59]** going to uh I'm going to show you guys

**[1:15:01]** how I how I actually use Archon every

**[1:15:03]** single day because here's the thing.

**[1:15:06]** I am not just working on one issue at a

**[1:15:09]** time with Archon. Um the fix GitHub

**[1:15:12]** issue workflow is my most often used,

**[1:15:15]** but I'm using it in parallel a lot. So

**[1:15:17]** take a look at this. I'm going to go

**[1:15:19]** into my speechto text tool. I'm going to

**[1:15:21]** say, okay, I also want to handle more

**[1:15:25]** issues. So, let's see here. Uh, let's

**[1:15:28]** tackle issue number 167.

**[1:15:32]** Um,

**[1:15:34]** let's see. Let's also do

**[1:15:39]** um, 182

**[1:15:42]** and 1,087.

**[1:15:45]** All right. So, I'm going to send this

**[1:15:46]** in. Uh, by the way, usually I'll do even

**[1:15:48]** more than this at once, but I just want

**[1:15:50]** to make sure that I don't hit my rate

**[1:15:52]** limits for Claude right now because it

**[1:15:54]** like I mean we're doing a lot of work in

**[1:15:56]** parallel here. Not that Archon is token

**[1:15:58]** inefficient. In fact, we've been doing a

**[1:15:59]** lot of things to make it more token

**[1:16:01]** efficient, but still like there is a a

**[1:16:04]** bunch that I'm doing at the same time

**[1:16:05]** right here. And watch this. Not only can

**[1:16:08]** I say, you know, spin up the workflows

**[1:16:11]** in parallel, but I can say I want you

**[1:16:13]** to, you know, run these workflows in

**[1:16:15]** parallel. I want you to wait until all

**[1:16:17]** of them are done. So monitor the

**[1:16:19]** workflows until we have pull requests

**[1:16:21]** for every single one of them. Then once

**[1:16:23]** we have pull requests for every single

**[1:16:24]** one of them, then I also want you to run

**[1:16:26]** the validate PR workflow on all these in

**[1:16:30]** parallel. And then when it produces the

**[1:16:32]** comments and the PRs, I want you to view

**[1:16:34]** the poll requests, look at all of the

**[1:16:36]** issues that we need to address. I want

**[1:16:37]** you to address them and push the changes

**[1:16:39]** to the branches for the pull request.

**[1:16:41]** And I could even combine all this into a

**[1:16:43]** single workflow if I wanted as well. But

**[1:16:44]** just like look at how comprehensive this

**[1:16:46]** is. We are going all the way from issue

**[1:16:48]** to a final validated pull request and

**[1:16:52]** we're doing it in parallel. So it's

**[1:16:54]** spinning up all of these at the exact

**[1:16:56]** same time as background processes. So

**[1:16:58]** now if I go into the four shells that I

**[1:17:00]** have open here in cloud code, we can see

**[1:17:02]** that they're they're all currently

**[1:17:03]** running. And then I can go hit enter to

**[1:17:05]** view the logs for any one of them. And

**[1:17:07]** um then of course I can see them all

**[1:17:09]** running in the web UI as well. So let's

**[1:17:12]** go back to the dashboard. And there we

**[1:17:13]** go. We got all four of them running. So,

**[1:17:15]** we have each of them running in the last

**[1:17:17]** 20 seconds here. And then this one

**[1:17:18]** that's been going on for five minutes

**[1:17:19]** now.

**[1:17:22]** Pretty cool.

**[1:17:24]** So, yeah, we're still doing the web

**[1:17:25]** research on this one here.

**[1:17:28]** But, yeah, that that's how I use Archon

**[1:17:30]** on the day-to-day. Like, most of the

**[1:17:31]** time when I'm working on a codebase, I'm

**[1:17:35]** I'm going to be filing things as issues.

**[1:17:38]** whether it's a bug that I'm going to be

**[1:17:39]** working on or it's a new feature that I

**[1:17:42]** want to add. Like both of those those

**[1:17:44]** fit as GitHub issues. And it's also nice

**[1:17:47]** because this is kind of like my personal

**[1:17:49]** mission control for everything I want to

**[1:17:50]** work on. And so that's why we see like

**[1:17:52]** Raasmus opening up so many GitHub

**[1:17:54]** issues. Like we're using this more than

**[1:17:57]** you know other people are because this

**[1:17:59]** is where we document all the things that

**[1:18:00]** we want to work on. Like Raasmus is

**[1:18:02]** opening up issue after issue for, you

**[1:18:04]** know, bugs and feature requests. And so

**[1:18:07]** that's also really nice because GitHub

**[1:18:09]** is where we're going to keep track of

**[1:18:11]** the versioning of Archon. Like as you

**[1:18:13]** evolve your codebase and you want your

**[1:18:15]** coding agent to remember things that

**[1:18:16]** you've worked on in the past, you're

**[1:18:18]** going to rely on git commits. I actually

**[1:18:20]** love using the git log as longterm

**[1:18:22]** memory for my coding agents. And so I'm

**[1:18:24]** already keeping track of all my work in

**[1:18:26]** in uh as like git commits and so I might

**[1:18:28]** as well like track things in is in

**[1:18:30]** issues as well for like the upcoming

**[1:18:32]** work that I have. So you can of course

**[1:18:34]** hook in like a MCP server or skill for

**[1:18:36]** Archon to use another external platform

**[1:18:39]** like Linear or Jira for your task

**[1:18:41]** management. I personally just love using

**[1:18:44]** GitHub as my task management. So that's

**[1:18:46]** why the GitHub CLI is so crucial for me

**[1:18:49]** for pretty much all of my Archon

**[1:18:50]** workflows. Now, of course, there are

**[1:18:53]** Archon workflows that don't have

**[1:18:55]** anything to do with GitHub. So, like for

**[1:18:57]** example, if I want to create a PRD, I

**[1:18:59]** can say, you know, use Archon to walk me

**[1:19:01]** through creating a PRD. And so, this is

**[1:19:04]** going to uh, you know, hopefully load

**[1:19:06]** the Archon skill here and then walk me

**[1:19:08]** through the interactive PRD workflow.

**[1:19:10]** So, I'm just showing off another

**[1:19:11]** workflow really quickly. And this one's

**[1:19:13]** actually pretty cool because it has

**[1:19:14]** human in the loop. So, it asks you some

**[1:19:17]** questions, it starts building the PRD,

**[1:19:19]** and then it stops to ask you more

**[1:19:20]** questions. So, maybe we'll see this in

**[1:19:22]** action really quick here. And then I

**[1:19:25]** also I do want to get into the other

**[1:19:28]** um the other thing I wanted to show you

**[1:19:30]** guys like building a workflow based on

**[1:19:32]** GSD.

**[1:19:34]** Okay. Um

**[1:19:37]** pick your starting point. Let's see.

**[1:19:40]** Okay. So, it actually tells me like

**[1:19:42]** here's a few different workflows. Um I

**[1:19:43]** want to use the interactive PRD

**[1:19:45]** workflow.

**[1:19:47]** So, let's have it kick that off for us

**[1:19:49]** here.

**[1:19:53]** Okay.

**[1:19:55]** Interactive workflows.

**[1:19:58]** Uh, got it. The interactive PRD workflow

**[1:20:00]** is a guided conversation where AI asks

**[1:20:02]** questions and rounds to build out a PRD.

**[1:20:05]** Cool. So, um, I don't know. I want to

**[1:20:09]** build support for PI agents in Archon. I

**[1:20:12]** mean, I think it's kind of an

**[1:20:13]** interesting example to let me make sure

**[1:20:15]** it actually my speech text tool spells

**[1:20:17]** that right. And I'll just say uh with

**[1:20:20]** the SDK. Not that I'll build this right

**[1:20:23]** now, but I'll I'll show you guys quickly

**[1:20:24]** what it looks like to go through a

**[1:20:26]** different workflow because like I get so

**[1:20:28]** hyperfocused on using the fix GitHub

**[1:20:30]** issue workflow. I want to show you guys

**[1:20:31]** something a little bit different here.

**[1:20:33]** Okay. So there we go. So now it kicks

**[1:20:35]** off the archon investigate or sorry

**[1:20:37]** interactive PRD. So the workflow is

**[1:20:40]** running. It's going to explore the

**[1:20:41]** codebase before it starts asking us some

**[1:20:43]** questions here. And we can obviously go

**[1:20:45]** and like view it in the logs along with

**[1:20:48]** the other ones. So this workflow is

**[1:20:49]** actually in a pause state now. So you

**[1:20:51]** can see in the web UI we have support

**[1:20:52]** for this where it'll show us like here

**[1:20:54]** is where we have a human in loop step.

**[1:20:56]** So while the all the other workflows are

**[1:20:58]** running this one we're more interacting

**[1:21:00]** with. So uh let me so it says it's

**[1:21:02]** paused. Let me grab the output. So it's

**[1:21:04]** going to read the logs and it's going to

**[1:21:06]** ask us some questions here. Right. So we

**[1:21:08]** the workflow is in a pause state for us

**[1:21:10]** to give feedback. And this is very

**[1:21:12]** similar to what I was showing in the uh

**[1:21:14]** example in the diagram earlier where we

**[1:21:16]** could have like human in the loop for a

**[1:21:17]** planning step but we get to actually

**[1:21:20]** review the plan and have the coding

**[1:21:22]** agent iterate on this before we go to

**[1:21:24]** the next step. So asking some foundation

**[1:21:26]** questions. Uh let's see. So who has this

**[1:21:30]** problem? Um everyone using archon. I

**[1:21:33]** think it's kind of a weird question

**[1:21:35]** actually. What problems are they facing?

**[1:21:37]** Uh the problem they're facing right now

**[1:21:39]** is there are a lot of people that don't

**[1:21:40]** want to use claw or codec specifically.

**[1:21:42]** They want to use different models. PI is

**[1:21:44]** more of a general agent that makes it

**[1:21:46]** really easy to uh to use other models.

**[1:21:50]** Um let's see. Why can't they solve it

**[1:21:53]** today? Uh well, we don't have support

**[1:21:55]** for PI yet. And I want to build this now

**[1:21:57]** because we're currently working on

**[1:21:59]** making big improvements to Archon and Pi

**[1:22:01]** is one of our priorities. We will know

**[1:22:04]** when it's solved. success. Looks like we

**[1:22:06]** can use pi, any model in pi with all of

**[1:22:09]** our archon workflows.

**[1:22:12]** So these questions um if you aren't

**[1:22:13]** familiar, these are like really standard

**[1:22:15]** questions for product managers to ask

**[1:22:17]** when they're first creating a PRD. So we

**[1:22:19]** have like a lot of like product manager

**[1:22:21]** best practices built into this workflow.

**[1:22:25]** Um, now the some of the questions were a

**[1:22:27]** little awkward for me right now just for

**[1:22:29]** the demonstration here, but they they

**[1:22:31]** are like legitimately good questions to

**[1:22:33]** ask when you're first creating a product

**[1:22:34]** requirements document. So now you can

**[1:22:36]** see that um using the archon skill,

**[1:22:39]** archon knows like, okay, let's resume

**[1:22:41]** the workflow with an approved state. So

**[1:22:43]** we're approving and then it's giving our

**[1:22:45]** feedback in. So it passed our answers

**[1:22:48]** through. So now the workflow is it went

**[1:22:51]** out of the pause state into the running

**[1:22:52]** state. And we can of course view the

**[1:22:54]** logs here to see what's going on.

**[1:22:57]** So this is the first node that it ran

**[1:23:01]** and then it asked us some questions. Now

**[1:23:02]** we move on to the next one. So it's kind

**[1:23:04]** of just like a process of like asking us

**[1:23:06]** questions and going in a loop here.

**[1:23:10]** All right. Um Oh, is it paused again?

**[1:23:12]** Hold on. No, it's still running. Okay.

**[1:23:14]** So we'll wait for it again.

**[1:23:18]** Although I might actually not continue

**[1:23:19]** with this demonstration because I think

**[1:23:20]** you guys get the idea. It really just

**[1:23:22]** does this in a loop where it has like a

**[1:23:24]** set of questions that it uh goes through

**[1:23:26]** for each one of the the prompts that we

**[1:23:28]** have right here. So I think you guys get

**[1:23:31]** the point. But there's an example of a

**[1:23:33]** workflow where um it doesn't really have

**[1:23:35]** anything to do with GitHub because not

**[1:23:37]** all of them have to. That's what I

**[1:23:39]** wanted to show. The final artifact

**[1:23:41]** obviously of this workflow is going to

**[1:23:42]** be a markdown document which is our PRD.

**[1:23:45]** So then we would, you know, break that

**[1:23:46]** up into tasks and and go through piv

**[1:23:49]** loops as a separate archon workflow to

**[1:23:52]** uh knock out all the phases that we have

**[1:23:53]** in that PRD. And then if you really

**[1:23:56]** wanted to get fancy, you could even if

**[1:23:58]** you wanted to make it so that the whole

**[1:24:00]** like pimploo process and PRD creation,

**[1:24:03]** like everything is a single archon

**[1:24:05]** workflow. Like I said, your entire

**[1:24:07]** software development life cycle, you can

**[1:24:09]** package that all up as an archon

**[1:24:12]** workflow.

**[1:24:15]** All right,

**[1:24:18]** cool. So, yeah, I think with that, I

**[1:24:20]** want to show you guys how to create a

**[1:24:23]** workflow from scratch because it's

**[1:24:26]** actually beautifully easy. So, I'm going

**[1:24:28]** to open up another Archon session here.

**[1:24:30]** And, you know, before I do that, I do

**[1:24:32]** want to spend some more time with Q&A

**[1:24:34]** with you guys. So, let me uh go back to

**[1:24:37]** the full frame here, and I will open up

**[1:24:40]** some more questions.

**[1:24:44]** All right. So, give me a second to kind

**[1:24:46]** of read through what we got here and

**[1:24:49]** then I think uh yeah, so Raasmus is is

**[1:24:51]** here in the live stream now answering

**[1:24:53]** questions. Appreciate it a lot, Raasmus.

**[1:24:55]** And then thank you Thomas as well.

**[1:24:59]** Um let's see.

**[1:25:07]** What is the simplest path to get this to

**[1:25:09]** work with linear tasks instead of GitHub

**[1:25:11]** issues?

**[1:25:13]** Yeah, so my recommendation would be to

**[1:25:15]** use either the linear MCP or create a

**[1:25:18]** skill to use the linear API and then you

**[1:25:21]** would build a custom workflow. So

**[1:25:24]** instead of like fix GitHub issue, it

**[1:25:26]** would be like fix linear issue or like

**[1:25:28]** handle linear task. And you could even

**[1:25:31]** have Archon reference the fix GitHub

**[1:25:34]** issue workflow

**[1:25:37]** and use that as a starting point where

**[1:25:38]** you would just mold things to be all

**[1:25:40]** linear instead of all GitHub. So it's

**[1:25:44]** actually very easy to uh integrate any

**[1:25:46]** platform that you want into Archon

**[1:25:49]** because for every single node you can

**[1:25:51]** inject skills or MCP servers.

**[1:25:54]** Um, so for the case of GitHub, like

**[1:25:56]** coding agents are so good at using the

**[1:25:58]** GitHub CLI that I don't need a GitHub

**[1:26:00]** CLI skill. You might need that for

**[1:26:02]** linear though or like I said the MCP

**[1:26:04]** server.

**[1:26:06]** But seriously, all you have to do, and

**[1:26:08]** I'll show you this in a second, is you

**[1:26:09]** like, okay, watch this. Um, I don't

**[1:26:13]** know. I don't think I'll actually run

**[1:26:14]** this right now, but I Oh, here. Let me

**[1:26:15]** go back to my scene so you guys can see

**[1:26:17]** my screen. I forgot I wasn't sharing my

**[1:26:19]** screen. So, I can say like, uh, load the

**[1:26:21]** archon skill. I want to create a version

**[1:26:24]** of the GitHub fix issue workflow, but

**[1:26:27]** specifically for linear instead of

**[1:26:28]** GitHub. Like that is all you have to do.

**[1:26:32]** Now, obviously, you're going to probably

**[1:26:33]** have to iterate quite a bit on the

**[1:26:35]** prompting and like really making things

**[1:26:36]** specific to you. Uh so this is this is

**[1:26:39]** certainly an oversimplification, but

**[1:26:40]** like this literally could be your

**[1:26:42]** starting point. Like this is what you

**[1:26:44]** you send in. Um and so yeah, after a

**[1:26:47]** little bit of Q&A here, I'll show you

**[1:26:48]** what it looks like to create a workflow.

**[1:26:50]** Like man, the archon skill is so

**[1:26:52]** beautiful because it just it knows

**[1:26:54]** everything. It'll it'll walk you through

**[1:26:56]** everything. And and another thing I love

**[1:26:57]** doing with coding agents is I like

**[1:27:00]** asking it to ask me questions. And so

**[1:27:03]** maybe I would send in, let me go back to

**[1:27:05]** my Aqua voice here.

**[1:27:08]** So I paste this back in. Um and I could

**[1:27:09]** say like, you know, ask me questions to

**[1:27:12]** make sure you understand uh my linear

**[1:27:14]** setup and exactly how I want the

**[1:27:16]** workflow to function, right? So that way

**[1:27:18]** you're you're kind of reducing the

**[1:27:19]** assumptions that it makes up front.

**[1:27:23]** Um, and so what it produces in the end

**[1:27:25]** is going to be better aligned with what

**[1:27:26]** you actually want before you go into

**[1:27:28]** iterating. You'll probably still have to

**[1:27:29]** iterate, but that's the idea here is

**[1:27:31]** like we go through a bit of a planning

**[1:27:32]** process with Archon before it um before

**[1:27:36]** it creates the workflow for us.

**[1:27:42]** All right,

**[1:27:46]** cool. What else do we got here?

**[1:27:51]** Um, with the session management within

**[1:27:52]** the workflows, how is context

**[1:27:54]** persistence handled? Is the data and

**[1:27:57]** context passed through the nodes? Okay,

**[1:28:00]** that is a really good question and we

**[1:28:03]** have a few different ways to handle

**[1:28:05]** context persistence here.

**[1:28:08]** So, uh, I'm trying to think if I have a

**[1:28:11]** good workflow to demonstrate this.

**[1:28:13]** instead of poking around, I might just

**[1:28:15]** more answer your question at a high

**[1:28:16]** level. Um, but yeah, one of the core

**[1:28:19]** things that we have in Archon is a

**[1:28:22]** parameter for each node that specifies

**[1:28:24]** if we want to continue the session from

**[1:28:27]** the prior node or start fresh.

**[1:28:31]** And so that that flexibility is pretty

**[1:28:32]** powerful because maybe you want a

**[1:28:34]** different node where you inject

**[1:28:36]** different skills or you just want to

**[1:28:38]** like have a new node for some reason

**[1:28:40]** because you want to like switch models

**[1:28:42]** or something but you want to still

**[1:28:44]** continue the same conversation from the

**[1:28:45]** previous node. You can do that or you

**[1:28:48]** can say like I actually want to start

**[1:28:49]** completely from scratch in this node.

**[1:28:53]** And then another thing that we have in

**[1:28:54]** archon is we have like outputs like we

**[1:28:57]** can output artifacts and so like for in

**[1:29:00]** this case we have the planning step and

**[1:29:04]** it's going to output a plan to our

**[1:29:06]** artifact directory for our current

**[1:29:08]** workflow execution. So this is like one

**[1:29:10]** of the primitives we have in workflows.

**[1:29:12]** It's like the artifact dur. And then we

**[1:29:15]** when we go in a brand new session in the

**[1:29:18]** implement stage, we are going to prompt

**[1:29:21]** it to read the plan from the artifact

**[1:29:23]** directory. So if I look at the archon

**[1:29:25]** fix issue command, let me open this up

**[1:29:28]** here because we you you can prompt

**[1:29:30]** inline. I've shown that in some of the

**[1:29:32]** workflows, you can you can have the

**[1:29:33]** prompt right in the YAML for the

**[1:29:35]** workflow or if you want to and you want

**[1:29:37]** it to like kind of be more organized,

**[1:29:39]** you can have it reference a command in

**[1:29:41]** the commands folder. So we'll go to

**[1:29:43]** archon um fix issue. There's a lot of

**[1:29:47]** commands here. So I have to find the

**[1:29:48]** right one. There we go. So archon fix

**[1:29:52]** issue. You'll see here that the argument

**[1:29:55]** is the artifact path. So archon is smart

**[1:29:58]** enough to know like once we are done

**[1:30:00]** with the planning and we have our plan

**[1:30:02]** here, we're going to prompt in a brand

**[1:30:05]** new session for our coding agent to read

**[1:30:08]** that plan, right? like go to the

**[1:30:10]** artifact directory and read that plan

**[1:30:12]** and then go through the implementation

**[1:30:14]** here. So, it's a brand new session, but

**[1:30:16]** then we're still passing some context or

**[1:30:19]** like I said, you can just uh have the

**[1:30:21]** context be like continue instead of

**[1:30:23]** fresh.

**[1:30:25]** So, it's up to you like flexibility

**[1:30:26]** depending on how you typically work.

**[1:30:31]** All right,

**[1:30:38]** let's see what else we got here.

**[1:30:43]** Let's see. Have you really given

**[1:30:44]** anything other than Opus a real try at

**[1:30:46]** Agenta coding tasks? I haven't. Uh, so I

**[1:30:50]** I do mostly use Opus for my

**[1:30:51]** implementation. However, I have tested a

**[1:30:54]** lot of using Sonnet for my archon

**[1:30:56]** workflows. So I I talked about this a

**[1:30:58]** little bit at the start of the live

**[1:30:59]** stream, but I get better results using

**[1:31:02]** Sonnet to fix GitHub issues with this

**[1:31:05]** workflow than just using Opus by itself

**[1:31:07]** in Cloud Code because of all the the

**[1:31:10]** context engineering that goes into you

**[1:31:13]** know like this. I guess you could call

**[1:31:14]** this like a GitHub issue harness like a

**[1:31:16]** fixer harness. U so I have run this with

**[1:31:19]** sonnet. So sonnet is actually the

**[1:31:22]** default model for all the nodes here. Uh

**[1:31:24]** now for the implementation itself I

**[1:31:27]** think we have it set to yeah so we have

**[1:31:29]** it set to using opus so like the default

**[1:31:31]** workflow as it stands uses opus

**[1:31:33]** specifically for implementation but

**[1:31:35]** obviously if you just delete this it'll

**[1:31:38]** use sonnet as the default or um you know

**[1:31:40]** you can change the model manually or

**[1:31:43]** whatever but so like at one point I had

**[1:31:44]** it set to sonnet and I was using it

**[1:31:47]** sonnet for everything sonnet or haiku

**[1:31:49]** for everything here and I was still

**[1:31:51]** getting really good results obviously

**[1:31:53]** obviously the best model is always going

**[1:31:55]** to give you the best results. Um, but

**[1:31:57]** for the sake of like making sure you

**[1:31:59]** don't hit your rate limits and stuff,

**[1:32:00]** you can use Sonnet for these workflows.

**[1:32:02]** And you can even like ask it to adjust

**[1:32:05]** the model at the default level or the

**[1:32:07]** specific node level before you run it if

**[1:32:09]** you want to.

**[1:32:13]** All right.

**[1:32:15]** People like seeing you failing. Pretty

**[1:32:17]** sure makes you a normal human. I assume

**[1:32:19]** you you referenced that when I was

**[1:32:21]** having all of the issues here in the

**[1:32:23]** VPS. So, I appreciate that. Uh, we'll

**[1:32:25]** talk about why I have those issues in a

**[1:32:28]** second because I have a Claude code. Um,

**[1:32:30]** I'm not actually authenticated with

**[1:32:31]** Claude. I am authenticated with the

**[1:32:34]** Miniax API. That's what was causing the

**[1:32:36]** problems on the VPS because I'm getting

**[1:32:38]** things set up for the dark factory.

**[1:32:41]** All right. How many tokens does start

**[1:32:43]** the app take? So, when I asked it to

**[1:32:46]** just like spin up the front end and back

**[1:32:48]** end of Archon, I mean, I don't know

**[1:32:50]** exactly, but it's probably just going to

**[1:32:52]** be a couple hundred, unless it's like

**[1:32:54]** running into an issue for some reason.

**[1:32:56]** It's not going to take that many tokens.

**[1:32:59]** And uh, by the way, you can see here

**[1:33:00]** that uh, it's already kicking off the

**[1:33:02]** whole process here, helping me create

**[1:33:04]** the linear version of the workflow. So,

**[1:33:06]** asking me some questions here. I'll

**[1:33:08]** answer those and then it'll create the

**[1:33:10]** workflow and test it for me and

**[1:33:11]** everything. Like I won't go through this

**[1:33:13]** whole process here, but for the question

**[1:33:15]** earlier on on migrating to linear, like

**[1:33:17]** it's just so easy to have it walk

**[1:33:19]** through cuz pretty much like here's the

**[1:33:21]** thing. All of the default workflows we

**[1:33:23]** have in Archon, there's two there's two

**[1:33:26]** uses for them. One is you can just use

**[1:33:28]** them directly out of the box if if there

**[1:33:31]** is one that like matches how you already

**[1:33:32]** work. But the other maybe even like more

**[1:33:35]** important part of these default

**[1:33:36]** workflows is it's a reference point for

**[1:33:39]** your coding agent to build something

**[1:33:41]** that's actually custom to you. And so

**[1:33:44]** even if you're building something that's

**[1:33:45]** like super different than everything we

**[1:33:47]** have here, like some kind of like

**[1:33:48]** refactoring workflow for example, um

**[1:33:50]** actually we have that as well. So maybe

**[1:33:52]** that's not the best example, but even if

**[1:33:54]** you have some like super different

**[1:33:55]** workflow that's like not even close to

**[1:33:58]** anything we have here, you still want

**[1:34:00]** your coding agent like loaded in the

**[1:34:02]** archon repo to look at these as a

**[1:34:04]** reference to understand like the

**[1:34:05]** different parameters we have for nodes

**[1:34:07]** and how we handle loops or whatever else

**[1:34:09]** like deterministic nodes, whatever you

**[1:34:10]** might want in your workflow. So very

**[1:34:13]** easy to pretty much build any I'll I'll

**[1:34:15]** show that in a second, but I just want

**[1:34:16]** to answer a couple more questions here

**[1:34:18]** because you guys have a lot of really

**[1:34:19]** good ones.

**[1:34:21]** All right,

**[1:34:24]** let's see.

**[1:34:27]** All right.

**[1:34:30]** Yep. Pi next week. Yeah, not not a

**[1:34:32]** promise that like we'll have it ready

**[1:34:34]** ready next week, but I'm definitely

**[1:34:35]** going to be working on me or Rasmus will

**[1:34:37]** be working on the pull request for

**[1:34:39]** adding in pi.

**[1:34:42]** Um, could I make a node to use codec

**[1:34:44]** spark in a workflow?

**[1:34:47]** Um, I mean there's nothing stopping you.

**[1:34:49]** You can make a node do literally

**[1:34:51]** anything because it can be a prompt to a

**[1:34:53]** coding agent or it can be a script. Even

**[1:34:55]** if you wanted to use a coding agent

**[1:34:57]** that's not supported by Archon directly,

**[1:35:01]** you can just make a script that invokes

**[1:35:03]** that like the Yeah, the world's your

**[1:35:04]** oyster here.

**[1:35:08]** All right.

**[1:35:12]** Um, let's see. What about create a node

**[1:35:15]** to mention other workflow, not only a

**[1:35:17]** command? I I think what you're asking

**[1:35:19]** about here is if we can nest workflows

**[1:35:21]** like if we can have a workflow that

**[1:35:23]** calls another workflow

**[1:35:25]** and uh that is something that we are

**[1:35:27]** planning on adding support for. Yep. So

**[1:35:30]** I haven't added that yet like

**[1:35:32]** subworkflow execution like you have in

**[1:35:34]** N8N. I haven't added that yet because I

**[1:35:36]** haven't found a a clear use for it for

**[1:35:39]** me personally but uh you're not the

**[1:35:41]** first one to ask about it and so like we

**[1:35:43]** are definitely interested in adding

**[1:35:45]** support for that.

**[1:35:47]** show some love and hit the like. I

**[1:35:49]** appreciate it a lot. Yeah, if you guys

**[1:35:50]** want to like the stream, I of course

**[1:35:52]** would appreciate that. Like the stream

**[1:35:55]** and uh and subscribe because I'm gonna

**[1:35:58]** be putting out a lot of content on

**[1:35:59]** Archon because like yeah, I'm getting

**[1:36:01]** pretty deep into the live stream here,

**[1:36:03]** but certainly a lot more I can show

**[1:36:05]** about like creating custom workflows and

**[1:36:07]** things that I'll be doing with future

**[1:36:08]** YouTube content and then of course in

**[1:36:10]** the Dynamis community as well. Uh so

**[1:36:12]** yeah, I just want to mention this again.

**[1:36:14]** I am planning on doing a lot of of

**[1:36:17]** workshops around archon um in Dynamus

**[1:36:21]** coming up here in the next couple of

**[1:36:22]** months, including using Archon with your

**[1:36:24]** second brain and some strategies to show

**[1:36:26]** like how I use my second brain to

**[1:36:29]** delegate work across my code bases with

**[1:36:32]** Archon. It's a bit of outside of the

**[1:36:33]** scope for our live stream here, but

**[1:36:36]** yeah, certainly the second brain is

**[1:36:37]** another really big part of of what I've

**[1:36:40]** been doing and what I'm covering in the

**[1:36:41]** Dynamis community. So, if you don't

**[1:36:43]** know, I I did a full 4hour course on

**[1:36:46]** building your own AI second brain in

**[1:36:47]** Dynamis. So, I took the entire system

**[1:36:50]** that saves me like no exaggeration at

**[1:36:52]** least 20 hours a week and I built it

**[1:36:54]** like from the ground up in a live stream

**[1:36:57]** so that you can follow along. And so, I

**[1:36:59]** am turning it into the third course for

**[1:37:01]** Dynamus. Um, and so you I'll put this

**[1:37:03]** link in the chat again if if you're

**[1:37:05]** interested in uh really like being on

**[1:37:07]** the forefront of Archon and uh going

**[1:37:10]** through these workshops and all the

**[1:37:12]** courses and building your own second

**[1:37:13]** brain. There's so much value packed into

**[1:37:15]** the community, not to mention all of the

**[1:37:17]** amazing minds in there sharing ideas

**[1:37:19]** every single day. Um, come join us in

**[1:37:21]** Dynamis. I' I'd love to have you there.

**[1:37:24]** Uh, and I I appreciate it. Dynamus

**[1:37:26]** community is great. Yeah. Thank you very

**[1:37:28]** much for all of you guys who are in the

**[1:37:29]** community uh here in the stream. always

**[1:37:31]** appreciate you guys being a part of it.

**[1:37:35]** Yeah, appreciate your passion and

**[1:37:37]** sharing of knowledge. Yeah, you're very

**[1:37:39]** welcome. It is my pleasure. Yeah, I mean

**[1:37:41]** I'm I'm excited. Like we had the

**[1:37:43]** question earlier of like why open source

**[1:37:45]** archon? I mean to me like there's not an

**[1:37:47]** alternative. I can't I can't imagine

**[1:37:48]** building something like this and just

**[1:37:50]** like hiding it from the world. Like I

**[1:37:53]** just I want people to to see what is

**[1:37:56]** possible with AI coding. Like in the

**[1:37:59]** end, that's like my number one goal with

**[1:38:01]** my I guess you could call it like my

**[1:38:03]** career. Like my with my career in

**[1:38:04]** business, like my number one goal is

**[1:38:06]** just to uh show people like what is

**[1:38:09]** possible with AI and also to just like

**[1:38:12]** cut through a lot of the fluff. Like I

**[1:38:14]** want to be real but inspirational at the

**[1:38:16]** same time. You know what I mean? Like

**[1:38:18]** there's a lot of people that are saying

**[1:38:19]** like you can vibe code everything and

**[1:38:21]** it's going to be perfect and you can

**[1:38:22]** make millions of dollars. Like I'm not

**[1:38:24]** one of those persons that's people

**[1:38:25]** that's like here's how to vibe code to

**[1:38:26]** make $10,000. Like no, I'm realistic.

**[1:38:29]** Like you have to have human in the loop.

**[1:38:32]** You can't just vibe code. Things take

**[1:38:34]** time. Coding agents make mistakes. Like

**[1:38:36]** I'm real on all of that. But then that's

**[1:38:39]** also why I'm building these tools

**[1:38:40]** specifically to add in deterministic

**[1:38:43]** steps. Human in the loop. Like building

**[1:38:45]** these harnesses because then that allows

**[1:38:47]** you to circumvent a lot of these real

**[1:38:50]** problems that a lot of people are

**[1:38:51]** ignoring. And so, uh, actually going to

**[1:38:54]** my YouTube channel here. It's funny

**[1:38:55]** because like, wait, hold on. I think I

**[1:38:58]** still have this in my YouTube channel.

**[1:39:00]** Um, yeah. Yeah. So, I've had this like

**[1:39:03]** oneliner for my YouTube channel. Um, for

**[1:39:07]** like literally ever since I started my

**[1:39:09]** channel in 2024, I've always had this

**[1:39:11]** sentence um, join me as I push the

**[1:39:13]** limits of what's possible with AI. And

**[1:39:15]** I've always kept this sentence because

**[1:39:17]** that is really what I'm trying to do

**[1:39:19]** here. like in a realistic way. Like

**[1:39:21]** don't you can't just vibe code a $10,000

**[1:39:24]** a month site in a week. In a realistic

**[1:39:26]** way, I am showing what it's like to push

**[1:39:29]** limits of AI and and I really think that

**[1:39:31]** like harness engineering is the

**[1:39:33]** forefront of AI right now, which is why

**[1:39:35]** I'm so excited about Archon.

**[1:39:38]** So, yeah, there there's my little spiel

**[1:39:39]** on on on my my vision and and why I want

**[1:39:42]** to make sure that Archon is available to

**[1:39:43]** everyone.

**[1:39:46]** Cool.

**[1:39:47]** All right, John said, "My brain is

**[1:39:49]** online thanks to Cole and the community.

**[1:39:51]** Couldn't have done it without the crew."

**[1:39:53]** I appreciate a lot, John. Yeah, I

**[1:39:54]** appreciate you being an active member of

**[1:39:56]** the community.

**[1:39:59]** Aron just joined the community. Thank

**[1:40:01]** you very much. Welcome to Dynamus, my

**[1:40:03]** friend. I'm going to be um so yeah, I'm

**[1:40:05]** I'm in Dynamus like literally every

**[1:40:07]** single day. So, I've been prepping for

**[1:40:08]** the live stream today. Haven't gotten to

**[1:40:10]** the posts in the last like 12 hours, but

**[1:40:12]** uh yeah, I mean like I'm replying to

**[1:40:15]** everything like every single day. So,

**[1:40:16]** I'll be sure to to greet you if you want

**[1:40:18]** to make an introduction post as well.

**[1:40:20]** I'd love to see that.

**[1:40:23]** All right.

**[1:40:25]** Let's see.

**[1:40:28]** Any plans to utilize local LLMs? So,

**[1:40:31]** that is actually one of the reasons I

**[1:40:34]** want to add in PI because PI will make

**[1:40:36]** it easier to use local LLMs. And then

**[1:40:40]** also within cloud code, you can

**[1:40:42]** integrate it with um things like Olama

**[1:40:44]** to use local models. So I I know that so

**[1:40:47]** Miniax M2.7 I'm not using that's not

**[1:40:50]** obviously running locally because it's a

**[1:40:52]** massive model. Uh but this is a

**[1:40:54]** demonstration of like I do actually have

**[1:40:56]** Claude working with a different model.

**[1:40:59]** Like check check this out. If I go back

**[1:41:00]** into Claude and I say what model are you

**[1:41:03]** like this isn't just a gimmick. It is

**[1:41:05]** actually using Miniax M2.7 through the

**[1:41:07]** MiniAX API. So you can change cloud code

**[1:41:11]** to work with other providers like GLM,

**[1:41:13]** MiniAX, Olama so that you can talk to

**[1:41:16]** local models. So I'm adding in PI

**[1:41:18]** because it'll make it easier and it's

**[1:41:19]** more like natively supported. Uh hold

**[1:41:21]** on, I got a sneeze coming.

**[1:41:23]** Excuse me. Um but yeah, you can you can

**[1:41:26]** connect cloud code like you can already

**[1:41:28]** use archon with local models if you

**[1:41:30]** wanted to try like there's been a couple

**[1:41:32]** people in the Dynamis community that

**[1:41:33]** have actually used Gemma 4 with Archon

**[1:41:36]** workflows. like Gemma for kind of

**[1:41:38]** driving the whole ship. So definitely

**[1:41:40]** possible already. Pi will make it even

**[1:41:41]** easier though.

**[1:41:45]** Yeah.

**[1:41:46]** Uh is there a way to override some

**[1:41:48]** settings like the model without changing

**[1:41:50]** the default YAML files? So I think there

**[1:41:54]** is a parameter to change the default

**[1:41:56]** model, but if it's overridden at the

**[1:41:58]** individual node configuration, there's

**[1:42:00]** not a way to change that right now. Uh,

**[1:42:02]** but like you shouldn't be afraid to just

**[1:42:05]** ask Archon to change the YAML for you,

**[1:42:08]** even if it's just like a temporary thing

**[1:42:10]** where it like revert it after it's done

**[1:42:11]** with the workflow. Um, it can definitely

**[1:42:13]** do that. Like I've actually been doing

**[1:42:15]** that a lot recently with cloud code

**[1:42:17]** skills where the skill will like change

**[1:42:20]** its own scripts as before it runs them

**[1:42:23]** and then just like revert it after I'm

**[1:42:24]** done with that set of work for any kind

**[1:42:26]** of like PowerPoint diagram or PDF

**[1:42:28]** generation. I've been doing that. So I

**[1:42:31]** wouldn't be afraid to but but still like

**[1:42:33]** that maybe that is like a real suggest

**[1:42:35]** like not maybe that is a good suggestion

**[1:42:37]** to make it even easier. Um let me

**[1:42:40]** actually ask it right here.

**[1:42:42]** Uh so based on the archon skill what can

**[1:42:44]** you tell me about support for changing

**[1:42:47]** the model without having to change the

**[1:42:49]** YAML itself? Like is there a flag for

**[1:42:51]** the CLI to change the model that's used?

**[1:42:56]** So, I'm I guess I'm kind of like

**[1:42:57]** validating the answer that I gave you

**[1:42:58]** quick here because I mean Archon's such

**[1:43:00]** a massive codebase. It's hard for me to

**[1:43:01]** remember like everything that we've

**[1:43:03]** decided, especially because like I said,

**[1:43:05]** Thomas and Raasmus have been helping me

**[1:43:06]** a lot in Archon as well. So, I'm also

**[1:43:08]** not the one that's built everything in

**[1:43:10]** the platform.

**[1:43:13]** Okay, let's see.

**[1:43:16]** There's no model CLI flag.

**[1:43:19]** Okay, so yeah, I guess I have to take

**[1:43:20]** that back. We don't have a way to do it

**[1:43:22]** right now. uh you would just have to

**[1:43:24]** edit the YAML directly which again like

**[1:43:27]** feel free to do that but also like that

**[1:43:28]** that is a good suggestion even if you

**[1:43:31]** wanted to make a GitHub issue for that

**[1:43:33]** in the Archon repo I'd be down to to

**[1:43:35]** address that because I'm just going to

**[1:43:36]** have it uh okay so I will say that like

**[1:43:40]** when I use Archon to work on your guys's

**[1:43:43]** issues in Archon like don't worry I am

**[1:43:45]** actually reviewing your issues and

**[1:43:47]** reviewing the poll requests as well so I

**[1:43:49]** am like legitimately considering the the

**[1:43:52]** things that you guys bring

**[1:43:53]** Um but yeah just like as the I delegate

**[1:43:57]** the coding to the agent itself 100%.

**[1:44:00]** We can see that this workflow actually

**[1:44:02]** we are almost done here

**[1:44:05]** with the GitHub issue fix and then if I

**[1:44:08]** look at my clawed rate limits I'm

**[1:44:10]** actually curious where we are at with

**[1:44:12]** that.

**[1:44:14]** Uh let's take a look.

**[1:44:17]** Okay, it's actually not too bad.

**[1:44:21]** Okay. So, here here's my claw rate

**[1:44:24]** limits for right now.

**[1:44:27]** This is this is not too bad. So, um

**[1:44:32]** I've used 37% of my 5 hour limit in the

**[1:44:35]** past

**[1:44:37]** like three hour or four 3 hours and 45

**[1:44:40]** minutes, right? And we're only at 37%.

**[1:44:44]** before. So, there's a lot of stuff I was

**[1:44:46]** doing to prep for the stream today, this

**[1:44:49]** morning before I started. So, we were

**[1:44:51]** already at like 15 to 20% before I

**[1:44:56]** kicked off all these workflows. And

**[1:44:57]** we've been doing quite a bit with Claude

**[1:44:59]** recently. I mean, we have so many

**[1:45:01]** workflows running right now and it it it

**[1:45:03]** used less than 20% of my 5 hour limit

**[1:45:06]** and we're almost done with all these

**[1:45:08]** workflows. Like, they're pretty token

**[1:45:09]** efficient.

**[1:45:11]** You could you could run the fix GitHub

**[1:45:13]** issue workflow like doz like at least a

**[1:45:16]** couple of dozen of times um and and

**[1:45:19]** until you hit your five hour limit and

**[1:45:21]** like that's a lot of work that Claude is

**[1:45:23]** doing. Uh now the really unfortunate

**[1:45:26]** thing is my limit reset yesterday and

**[1:45:29]** I'm already at 32% for the week. That is

**[1:45:32]** a huge bummer. Like I'm probably going

**[1:45:34]** to hit my weekly limit around Tuesday or

**[1:45:36]** Wednesday. It's unfortunate. Uh, so

**[1:45:39]** yeah, there there are always people that

**[1:45:42]** tell me they have like, you know, two,

**[1:45:43]** three, four claw subscriptions. I'm not

**[1:45:46]** one of those people, but honestly, after

**[1:45:48]** Anthropic u making things making the

**[1:45:50]** rate limits more harsh recently, I might

**[1:45:52]** have to get a second subscription. I

**[1:45:54]** feel bad saying that cuz it's like

**[1:45:55]** Anthropic is being kind of frustrating

**[1:45:57]** recently and then I'm just giving them

**[1:45:59]** more money when it's like, well, what

**[1:46:01]** can you do? like I I don't really want

**[1:46:03]** to switch over to codeex because I test

**[1:46:05]** codecs from time to time and I I just I

**[1:46:07]** think claude code is better.

**[1:46:11]** But anyway, so yeah, it's yeah, these

**[1:46:14]** workflows are pretty token efficient for

**[1:46:15]** how much they're actually doing. Like

**[1:46:17]** keep in mind, it's not just asking cloud

**[1:46:19]** code to fix an issue. It's going through

**[1:46:21]** deep investigation, deep research, deep

**[1:46:23]** implementation, and deep code review

**[1:46:25]** using the right model at the right time.

**[1:46:27]** So it's not uh super tokenheavy.

**[1:46:32]** All right.

**[1:46:33]** Uh, working on something similar and

**[1:46:35]** yeah, thank you for the $5 donation. I

**[1:46:37]** appreciate it a lot. Uh, would love to

**[1:46:39]** discuss with you about how we could

**[1:46:40]** potentially partner if there's something

**[1:46:41]** you are open to. Yeah. So, Archon is an

**[1:46:45]** open source repo and for me that means

**[1:46:47]** that partnerships would be like I'd love

**[1:46:49]** to chat and see what your ideas are. Uh,

**[1:46:52]** but I I wouldn't really want to like go

**[1:46:53]** and work on a separate repo. But if

**[1:46:56]** you're interested in like contributing

**[1:46:57]** to Archon and partnering in that way, um

**[1:47:00]** I am considering creating sort of like a

**[1:47:02]** core maintainer team for Archon. I think

**[1:47:04]** that would be the way to partner because

**[1:47:06]** I wouldn't want to like turn this into a

**[1:47:08]** separate venture. I like I said with

**[1:47:11]** like my core vision and and mission for

**[1:47:14]** Archon and my career as a whole is to be

**[1:47:16]** open source and share with the world.

**[1:47:17]** And so I I don't want this to like

**[1:47:19]** create spin-offs that I'm dedicating

**[1:47:21]** time to. instead of working on Archon as

**[1:47:24]** the core open- source repository.

**[1:47:27]** But I'm always open to uh

**[1:47:29]** collaborations, maybe even I'm thinking

**[1:47:31]** like I said making the maintainer team

**[1:47:32]** always open to issues and poll requests.

**[1:47:35]** And um yeah, sometimes open source can

**[1:47:37]** get overwhelming. So also like I don't

**[1:47:39]** always get to issues and pull requests

**[1:47:41]** uh even within the same week because it

**[1:47:44]** it gets a lot let me tell you guys from

**[1:47:45]** all the open source work that I did. But

**[1:47:47]** also, it's more and more realistic to

**[1:47:48]** handle everything over time as I have

**[1:47:50]** coding agents help me and a maintainer

**[1:47:53]** team. And then like I said, like we kind

**[1:47:54]** of already have a maintainer team with

**[1:47:56]** me, Raasmus, and Thomas. Um, but uh also

**[1:47:59]** like thinking of extending that to just

**[1:48:01]** like the general, you know, you guys in

**[1:48:05]** the YouTube community and in the Dynamus

**[1:48:07]** community.

**[1:48:09]** All right,

**[1:48:12]** cool.

**[1:48:14]** Is it open source available on GitHub?

**[1:48:17]** Well, I assume that was a question to

**[1:48:18]** someone else because yes, Archon is and

**[1:48:20]** and Thomas knows that.

**[1:48:22]** All right. Is it possible to add Gemini?

**[1:48:26]** So, the Gemini CLI I don't think has an

**[1:48:30]** SDK. Gemini CLI SDK.

**[1:48:34]** So that's the thing is is for any coding

**[1:48:36]** agent that we integrate with Archon, it

**[1:48:38]** does need to have an SDK

**[1:48:40]** because I I work with the coding agents

**[1:48:43]** programmatically in Typescript instead

**[1:48:45]** of using the headless mode for the CLI.

**[1:48:47]** That's like another way that you can

**[1:48:48]** automate the usage of um of coding

**[1:48:51]** agents.

**[1:48:53]** I've I've been checking on this a lot

**[1:48:55]** though because this is another one of

**[1:48:56]** the tools that I would obviously want to

**[1:48:58]** integrate. A lot of people love using

**[1:49:00]** Gemini, especially because Gemini 3

**[1:49:02]** seems to be like the best model for

**[1:49:04]** building frontends. Like people always

**[1:49:06]** use anti-gravity with Gemini 3 to build

**[1:49:08]** frontends and um so I I would love to

**[1:49:11]** add support for but they don't have an

**[1:49:12]** SDK.

**[1:49:15]** Um however, you could always use the PI

**[1:49:17]** SDK with Gemini. So we add support for

**[1:49:20]** that then it would work.

**[1:49:23]** Um, I guess I can't find an exact link,

**[1:49:25]** but

**[1:49:28]** um Oh, wait. What's this? This must not

**[1:49:31]** be Hold on. Google Genai SDK. That's I

**[1:49:34]** think that's for general agents, not

**[1:49:36]** Yeah, that's not for AI coding. So,

**[1:49:38]** that's not that's not an SDK for the

**[1:49:39]** Gemini CLI, unfortunately.

**[1:49:44]** All right.

**[1:49:49]** uh to reach these limits, you have to

**[1:49:51]** have the product first because you can't

**[1:49:52]** code multiple things without having

**[1:49:53]** verticals that do not conflict. That's

**[1:49:56]** true. Yeah. Yeah. When you're first

**[1:49:57]** getting started, it's like you can't

**[1:49:58]** really do as much work in parallel. It's

**[1:50:00]** more once you have the thing established

**[1:50:02]** and you're just working through

**[1:50:03]** different issues, like granular sets of

**[1:50:05]** work for improvements or bug fixes, then

**[1:50:07]** that's definitely when you're going to

**[1:50:09]** start hitting the limits 100%.

**[1:50:13]** All right.

**[1:50:15]** Um let's see. I'm on the $200 max plan.

**[1:50:18]** That is true. Would you hit limits much

**[1:50:20]** faster on the lower plan? I think yes. I

**[1:50:22]** mean, yeah. The answer 100% is yes, cuz

**[1:50:25]** the um $20 plan doesn't take you very

**[1:50:28]** far to be honest. And then the $100

**[1:50:30]** plan, like you can you can do quite a

**[1:50:33]** bit, but you still hit your rate limits

**[1:50:35]** decently quickly. I believe that the

**[1:50:37]** $200 month plan is four times better

**[1:50:40]** rate limits than the $100 month plan.

**[1:50:43]** And then the $200 is 20 times better

**[1:50:46]** than the $20 plan. There's a quite a big

**[1:50:49]** difference there.

**[1:50:51]** All right.

**[1:50:54]** Let's see. How is this different than uh

**[1:50:56]** BMAD version six? So, okay, here's the

**[1:51:00]** thing. BMAD is a harness. Archon is a

**[1:51:03]** harness builder. So, BMAD is a an

**[1:51:07]** opinionated approach to building

**[1:51:08]** software. It's a good approach. I think

**[1:51:10]** it's kind of overengineered to be

**[1:51:11]** honest, but it's a it's a really

**[1:51:13]** inspirational approach and you can

**[1:51:15]** literally take ideas from BMAD and build

**[1:51:18]** it into your own archon workflows and

**[1:51:19]** then customize it more for yourself. So

**[1:51:21]** the big thing that I want to be clear on

**[1:51:23]** here is that uh Archon is not competing

**[1:51:26]** with GitHub specit or BMAD or Cloudflow

**[1:51:28]** or GSD.

**[1:51:30]** It's more like those tools are great,

**[1:51:32]** but what if you want to build your own?

**[1:51:33]** That's why it's a harness builder.

**[1:51:37]** And so, um, yeah, in a second here, I'll

**[1:51:39]** show you what it looks like to literally

**[1:51:40]** just like take inspiration from GSD and

**[1:51:43]** like build it as an Archon workflow.

**[1:51:47]** Archon is very powerful. Going to scrap

**[1:51:49]** the GitLab AI reviewer I developed

**[1:51:50]** yesterday and use Archon instead. Archon

**[1:51:52]** offers much more room for expansion.

**[1:51:55]** Very cool. Yeah, I appreciate it. Uh,

**[1:51:57]** and you know what you can do is not

**[1:51:59]** scrap what you built, but uh, point the

**[1:52:01]** Archon repo to look at what you built

**[1:52:03]** for inspiration to turn it into an

**[1:52:05]** Archon workflow.

**[1:52:07]** And and so yet another thing that I want

**[1:52:09]** to, you know, re-emphasize here is you

**[1:52:12]** don't have to ditch what you already

**[1:52:14]** have if you want to build archon

**[1:52:16]** workflows because you can bring in your

**[1:52:17]** skills and commands. You can reference

**[1:52:20]** other other frameworks or other tools

**[1:52:22]** that you built to use as inspiration

**[1:52:25]** either for the prompting or just like

**[1:52:26]** the general process that you'd want to

**[1:52:28]** lay out at in a node by node basis.

**[1:52:30]** you're always able to um work with what

**[1:52:33]** you already have because I don't I don't

**[1:52:34]** want to that's another one of the

**[1:52:36]** problems with with all the other

**[1:52:38]** harnesses that are out there. Like

**[1:52:40]** they're cool, but they require you to

**[1:52:42]** pretty much change how you work

**[1:52:44]** fundamentally. And that's just not going

**[1:52:46]** to fly. Especially if you're working on

**[1:52:48]** a team, like if you're at an enterprise

**[1:52:50]** level and you already have a process for

**[1:52:54]** your software development life cycle,

**[1:52:56]** it's really really hard for you as a an

**[1:52:59]** enterprise level like as a team to adopt

**[1:53:01]** something like BMAD because you have to

**[1:53:03]** change how you work. But with Archon,

**[1:53:05]** you don't change how you work because

**[1:53:06]** you're building the layer on top of the

**[1:53:08]** coding agent that actually enforces

**[1:53:10]** that. So you get to even um in a better

**[1:53:13]** way take how you work and use coding

**[1:53:16]** agents with that.

**[1:53:20]** Um yep Rasmus same here. Use it every

**[1:53:22]** day since November. No bans using the

**[1:53:24]** cloud agent SDK with the anthropic

**[1:53:26]** subscription.

**[1:53:33]** Oh yeah. When are there going to be

**[1:53:34]** archon hoodies and merch? I would be

**[1:53:37]** interested. Yeah. Um, yeah. I mean,

**[1:53:41]** merch for Dynamis and or Archon would be

**[1:53:43]** pretty cool. I don't know like how much

**[1:53:46]** of an interest there would really be for

**[1:53:47]** that, but it could be cool. I mean, my

**[1:53:50]** man Nate Herk is always rocking his um

**[1:53:53]** his merch in his uh YouTube videos now.

**[1:53:55]** It would be cool to have a a sweatshirt

**[1:53:57]** or sweater or something that I wear when

**[1:53:59]** I'm recording. Yeah.

**[1:54:03]** All right.

**[1:54:06]** Yeah. Very cool. Well, meld archon and

**[1:54:08]** my QA bot. That's the way to do it. Meld

**[1:54:11]** it with what you've already got 100%.

**[1:54:17]** All right.

**[1:54:20]** At peak, I had 30 something archon

**[1:54:22]** workflows running in parallel across

**[1:54:24]** four projects. You know, with the

**[1:54:27]** anthropic rate limits now, you probably

**[1:54:29]** won't be able to do that, but uh that's

**[1:54:31]** very cool. We we've been spoiled at some

**[1:54:34]** points. So, uh, within the like, you

**[1:54:36]** know, the last couple of weeks up until

**[1:54:38]** this week, Archon or not Archon,

**[1:54:41]** Anthropic was doing a special where it's

**[1:54:43]** like in off hours you had, uh, two times

**[1:54:46]** lower rate limits. And trust me, I was

**[1:54:48]** taking advantage of that, chugging

**[1:54:51]** through like eight poll requests in

**[1:54:53]** parallel for like the entire day

**[1:54:55]** straight, multiple days.

**[1:54:57]** Well, not the entire day straight, but

**[1:54:58]** like during the off hours. Uh, so yeah,

**[1:55:01]** it's it's a little unfortunate, but I am

**[1:55:04]** I am doing some experimentation with

**[1:55:06]** like other models that like, you know,

**[1:55:07]** Miniax.

**[1:55:09]** It's just not as good as Opus, but you

**[1:55:11]** still get quite a bit of power. So, if

**[1:55:12]** you have the right harness, you can get

**[1:55:14]** really good results even with something

**[1:55:16]** like Miniax M2.7. So, I am experimenting

**[1:55:19]** with some things that'll get into the

**[1:55:20]** dark factory we'll talk about in a bit.

**[1:55:22]** I am experimenting with some things

**[1:55:24]** though to be able to scale the number of

**[1:55:27]** workflows I can run in parallel and not

**[1:55:29]** have to worry about rate limits. It'll

**[1:55:30]** get a little costly, but I mean the

**[1:55:32]** point of using these smaller models is

**[1:55:33]** it won't get too costly.

**[1:55:37]** All right. Yeah, that's right, Sean.

**[1:55:39]** Spicy mango shirts. And man, spicy mango

**[1:55:42]** hasn't come up in a while now. I'll I'll

**[1:55:44]** need to fit that into more YouTube

**[1:55:46]** videos, but it's like an ongoing joke

**[1:55:47]** where um I don't even remember where it

**[1:55:50]** originated. It was like something with

**[1:55:51]** GPT where like I was asking for recipes

**[1:55:54]** in a YouTube video and it kept like

**[1:55:55]** bringing up spicy mango even between

**[1:55:57]** conversations where there's no long-term

**[1:55:59]** memory. So, it just kind of became a

**[1:56:01]** joke from there.

**[1:56:03]** All right.

**[1:56:07]** Let's see.

**[1:56:10]** All right. Um, you know what? So, man,

**[1:56:13]** there's so many good questions in the

**[1:56:14]** chat still. But I do want to get to the

**[1:56:16]** next part here where I will uh build a

**[1:56:19]** workflow with you guys.

**[1:56:22]** So, let's let's go back into our

**[1:56:25]** repository.

**[1:56:27]** I'm going to close out of this session

**[1:56:29]** and start a new one.

**[1:56:32]** All right. So, here, hold on. Let me

**[1:56:34]** clear. There we go. All right. So, what

**[1:56:37]** I want to show you guys now is how to

**[1:56:41]** build a custom workflow in Archon.

**[1:56:45]** And there are a million different ways

**[1:56:48]** or different kinds of workflows you can

**[1:56:50]** build.

**[1:56:52]** And like I said, you can take

**[1:56:53]** inspiration from all these existing

**[1:56:55]** ones, even pointing archon to look at

**[1:56:57]** these to, you know, understand best

**[1:57:00]** practices and how we've been building

**[1:57:01]** workflows already. But as a as an

**[1:57:03]** example, like I've teased already, I

**[1:57:05]** want to build GSD

**[1:57:08]** as an archon workflow. So GSD, it's a a

**[1:57:12]** lightweight and powerful metaprompting

**[1:57:14]** context engineering spec driven

**[1:57:16]** development system. Little bit of word

**[1:57:18]** salad there, but basically it's a

**[1:57:20]** simplistic approach to going from

**[1:57:22]** planning all the way to getting your

**[1:57:24]** work done with coding agents. It's it's

**[1:57:26]** it's nice.

**[1:57:28]** and um he I actually really appreciate

**[1:57:31]** the inspiration behind the project. So

**[1:57:33]** he says other spectrum and development

**[1:57:34]** tools exist like BMAD and SpecKit, but

**[1:57:37]** they all seem to make things way more

**[1:57:38]** complicated than they need to be which I

**[1:57:41]** agree with this. I actually already said

**[1:57:42]** this in the live stream where these

**[1:57:44]** tools are very inspirational, but just

**[1:57:46]** like it's more than you really want in

**[1:57:48]** your process and they're so opinionated.

**[1:57:51]** You've got your sprint ceremonies and

**[1:57:53]** story points and stakeholder syncs and

**[1:57:55]** retrospectives and jurro workflows.

**[1:57:57]** I'm not a 50 person software company. I

**[1:58:00]** don't want to play enterprise theater.

**[1:58:02]** And like preach, man. Like that's good.

**[1:58:05]** So I built GSD. The complexity is in the

**[1:58:07]** system, not in your workflow.

**[1:58:10]** So the the system gives Claude

**[1:58:11]** everything it needs to do the work and

**[1:58:13]** verify it, right? Like that's that's the

**[1:58:15]** harness here is it's a system for

**[1:58:16]** planning, implementing, and validating.

**[1:58:18]** A lot of like what I've already been

**[1:58:19]** talking about. I trust the workflow. It

**[1:58:21]** does it just does a good job. It just

**[1:58:23]** gets it done.

**[1:58:26]** And so I want to take some of the these

**[1:58:28]** ideas here. So I'm not like, okay, I'm

**[1:58:29]** not going to build this like step by

**[1:58:32]** step in Archon. I'm not going to build a

**[1:58:34]** replica, but I'm going to take the

**[1:58:36]** general flow of the different phases

**[1:58:39]** like discussing and planning and

**[1:58:41]** executing and some of their strategies

**[1:58:43]** for splitting up work into different

**[1:58:44]** stages and their verification. I want to

**[1:58:46]** take inspiration from this, but I'm

**[1:58:49]** going to do it with Claude. So watch

**[1:58:50]** this. I'm going to copy this repo. I'm

**[1:58:53]** going to paste it in and I'm just going

**[1:58:55]** to say load the archon skill. I want you

**[1:58:57]** to help me make an archon workflow

**[1:59:01]** that uh takes very heavy inspiration

**[1:59:04]** from GSD, the repo that I gave you the

**[1:59:06]** path to here. So, I want you to analyze

**[1:59:08]** the repo. I want you to dig deep into

**[1:59:10]** the process here and how it goes through

**[1:59:12]** the different phases, how it manages

**[1:59:14]** tasks and does verification. And I want

**[1:59:16]** you to analyze other workflows in

**[1:59:18]** Archon, some of the defaults to get an

**[1:59:21]** idea for like how those work and how we

**[1:59:23]** could translate ideas from GSD into a

**[1:59:26]** new workflow that we'll create that'll

**[1:59:28]** basically go through the same process

**[1:59:30]** having human approval gates for

**[1:59:32]** different steps of the way within

**[1:59:33]** planning and validation.

**[1:59:36]** So, and actually one more thing that I

**[1:59:37]** want to add to the prompt here is I'll

**[1:59:39]** say I want you to after you do your

**[1:59:41]** research, ask me questions. to make sure

**[1:59:43]** that we're aligned on what this workflow

**[1:59:45]** does and how we're going to take

**[1:59:46]** inspiration from GSD.

**[1:59:49]** And so, I mean, if you wanted to go so

**[1:59:51]** far, you could pretty much replicate all

**[1:59:53]** of GSD as an archon workflow. That would

**[1:59:55]** take a lot of work. I think that would

**[1:59:57]** take too long to do in this live stream,

**[1:59:59]** which is why I'm doing it more like and

**[2:00:01]** like, you know, let's just take

**[2:00:02]** inspiration from GSD versus replicate

**[2:00:04]** it. Exactly. But we'll still get

**[2:00:06]** something pretty similar here. I

**[2:00:08]** actually did already test this before

**[2:00:10]** the live stream and the results were

**[2:00:11]** were pretty good.

**[2:00:14]** Now, it is going to take a while to do

**[2:00:17]** the research initially or at least a

**[2:00:19]** decent amount of time. So, I'll answer

**[2:00:20]** some more questions while we let this

**[2:00:21]** run. Uh, but I think this is a nice demo

**[2:00:24]** because without getting too complex

**[2:00:26]** here, just showing you at a high level

**[2:00:28]** how it's like no matter what you want to

**[2:00:30]** build, just describe your process, have

**[2:00:32]** it look at existing workflows for

**[2:00:34]** reference. And of course, Archon skill

**[2:00:36]** helps and then just start building with

**[2:00:38]** it. In fact, one of the workflows that

**[2:00:40]** we have is a workflow builder. It's very

**[2:00:43]** meta, but whenever we want to build a

**[2:00:45]** workflow, we can use this. It just kind

**[2:00:48]** of provides some more structure, right?

**[2:00:50]** It's a harness around building more

**[2:00:51]** custom workflows. A harness around

**[2:00:53]** building harnesses. If I had a dime for

**[2:00:56]** every time I said harness in this live

**[2:00:57]** stream, I would just go retire.

**[2:01:02]** All right.

**[2:01:05]** Let's see.

**[2:01:08]** By the way, I built Colm for agent

**[2:01:10]** memory context engine. Close to 100

**[2:01:12]** stars already. It's pretty cool.

**[2:01:14]** Congratulations.

**[2:01:16]** Yeah, long-term memory for AI coding is

**[2:01:18]** uh it's very powerful, very needed.

**[2:01:24]** Let's see. Um, do you have the

**[2:01:27]** possibility to temporarily run commands

**[2:01:28]** from the web UI like running a dev

**[2:01:30]** server from your work tree to check the

**[2:01:32]** look and feel of your change from your

**[2:01:34]** workree?

**[2:01:35]** Yeah. So, we have played around with the

**[2:01:38]** idea of having like a basic terminal in

**[2:01:41]** the web UI to do things like that, but

**[2:01:44]** we haven't built that yet.

**[2:01:46]** Um, it's one of those things where it's

**[2:01:48]** like, let's see if people really need

**[2:01:49]** that before we build it. A lot of what

**[2:01:52]** we built into Archon up until this point

**[2:01:53]** has been like, you know, just, you know,

**[2:01:56]** only like three people really sharing

**[2:01:58]** their opinions. And well, okay,

**[2:02:00]** obviously it's not just three people

**[2:02:01]** because we've had this in the Dynamis

**[2:02:03]** community for a while as well, but for

**[2:02:04]** the most part, we haven't had like

**[2:02:06]** hundreds of people using it yet or

**[2:02:08]** thousands of people using it yet like we

**[2:02:10]** are about to. We kind of already have

**[2:02:11]** now this week. And so, we'll see how

**[2:02:13]** people really use it. And I'm thinking

**[2:02:16]** about um getting like feedback from the

**[2:02:18]** YouTube and Dynamis community as a whole

**[2:02:20]** for what kind of features we want.

**[2:02:21]** Things like this we might want to build,

**[2:02:23]** but I just want to be careful with

**[2:02:25]** feature bloat. I want to make sure like

**[2:02:27]** there are a lot of things that sound

**[2:02:28]** good on paper, but like maybe people

**[2:02:30]** don't actually end up needing that. So,

**[2:02:32]** for the old version of Archon that I was

**[2:02:34]** building over last summer and like

**[2:02:36]** released in August, that one we we made

**[2:02:39]** the mistake of building in way too many

**[2:02:40]** things up front. Like there was a ton of

**[2:02:42]** different configuration parameters and

**[2:02:44]** stuff that like sounded really good on

**[2:02:45]** paper, but then like no one ever

**[2:02:47]** actually used it. Like I'd constantly

**[2:02:49]** like show things like that on live

**[2:02:51]** streams or in Dynamus workshops and

**[2:02:53]** people would be like, "Wow, I didn't

**[2:02:54]** even know that was a thing." like I well

**[2:02:56]** I like saw it but I just like glazed

**[2:02:57]** over it because I didn't really care

**[2:02:59]** about it. So that that's the kind of

**[2:03:00]** thing I want to look out for. Um but

**[2:03:03]** yeah, I definitely would be interested

**[2:03:04]** in like adding more support in the web

**[2:03:06]** UI for being able to like actually

**[2:03:08]** manage everything yourself, not just

**[2:03:10]** relying on Archcom. Now the other thing

**[2:03:12]** is you could just ask Archon to spin up

**[2:03:13]** the site in the work tree, right? Like

**[2:03:15]** it it could take care of that even by

**[2:03:17]** itself. So you don't necessarily need a

**[2:03:19]** place for like you to run the commands

**[2:03:20]** yourself when you can just ask the

**[2:03:22]** coding agent to do it. But I I still

**[2:03:25]** think that that could definitely be a

**[2:03:26]** good addition to the web UI.

**[2:03:32]** All right.

**[2:03:35]** Let's see. How do you pause all or a

**[2:03:37]** graceful pause? Yeah, there no way to do

**[2:03:40]** that right now in Archon because the

**[2:03:43]** pause is reserved for human in the loop

**[2:03:44]** workflows. So, it really is like you

**[2:03:47]** either abandon the workflow. Well, okay.

**[2:03:50]** Actually, there there kind of is support

**[2:03:51]** for it. It's just not direct cuz you can

**[2:03:53]** abandon a workflow

**[2:03:56]** and then you can uh resume it later.

**[2:04:00]** It's just if you click abandon, it's not

**[2:04:02]** going to like show up in the web UI as

**[2:04:03]** something you can resume. But there is a

**[2:04:05]** CLI option to resume a workflow. So you

**[2:04:08]** could just if you have to like shut it

**[2:04:10]** down for whatever reason, you could just

**[2:04:12]** say like, hey, like I want you to

**[2:04:13]** interrupt and stop these workflows. And

**[2:04:15]** then later on you could tell Claude

**[2:04:16]** like, okay, resume these workflows. And

**[2:04:18]** if it's in the same session, it'll it'll

**[2:04:20]** remember the workflow ids that are

**[2:04:22]** stored in the you know the SQLite

**[2:04:24]** database or Postgress database under the

**[2:04:26]** hood so that it can it can pick up where

**[2:04:28]** it left off. So it'll basically just

**[2:04:30]** like retry the node that it that was

**[2:04:34]** interrupted and then continue the

**[2:04:35]** workflow from there. So yeah, just kind

**[2:04:38]** of thing you just ask the agent to do

**[2:04:39]** it. It knows how to to how to do that.

**[2:04:43]** All right, cool. So we got we're only at

**[2:04:45]** 50% and it resets in 55 minutes. So our

**[2:04:48]** limit is good here and it's going

**[2:04:49]** through. So you can see that it um

**[2:04:51]** finished all of the GitHub fix issue

**[2:04:53]** workflows. Now it's just doing the

**[2:04:54]** validation here. So if I go back to

**[2:04:57]** Archon um man I have so many sessions

**[2:04:59]** open up. Uh which one was it? Yeah, this

**[2:05:02]** one here. So let's see.

**[2:05:06]** So it's checking in on all the workflows

**[2:05:08]** over time.

**[2:05:13]** Um done.

**[2:05:16]** There we go. So, yeah, you can see that

**[2:05:19]** all of the fixed workflows were done. We

**[2:05:21]** have the pull requests created and then

**[2:05:24]** it launches the validate PR in parallel.

**[2:05:26]** So, sorry, I know I'm jumping around a

**[2:05:28]** little bit here, but I just want to show

**[2:05:29]** you the other thing that we've had

**[2:05:31]** running this entire time. We created the

**[2:05:33]** pull requests, those four in parallel,

**[2:05:34]** and now we're doing the the reviews all

**[2:05:37]** in parallel as well. And that's what

**[2:05:38]** we're seeing in the the web UI here as

**[2:05:40]** well. And then we have the interactive

**[2:05:42]** PRD that I'm just going to kind of

**[2:05:44]** abandon because I don't want to spend

**[2:05:46]** time on that right now.

**[2:05:48]** All right.

**[2:05:51]** Oh, yeah. Thank you very much. Yeah,

**[2:05:52]** congrats on the 200,000 subs. I

**[2:05:55]** appreciate it. Yeah, so that happened

**[2:05:56]** literally just yesterday. I I reached

**[2:05:58]** 200,000 subscribers. So, yeah, pretty

**[2:06:01]** big milestone. I don't get a plaque for

**[2:06:03]** that like the 100,000 unfortunately, but

**[2:06:05]** it still feels really good to get to

**[2:06:07]** that point. So, yeah, thank you.

**[2:06:10]** All right, cool. So, all right, let's

**[2:06:12]** see what we got here. So, we got the

**[2:06:14]** core summary of GSD. It implements a

**[2:06:17]** spec driven pipeline with these phases,

**[2:06:19]** questioning, parallel research,

**[2:06:20]** requirements, road map, uh, perphase

**[2:06:23]** loop, and then um, we get our complete

**[2:06:26]** milestone.

**[2:06:28]** So, that's like the end result of going

**[2:06:30]** through the whole spec driven flow.

**[2:06:32]** lists out some key patterns here like

**[2:06:34]** the plan checker as a gatekeeper before

**[2:06:36]** execution, goal backward verification,

**[2:06:39]** which um yeah, I mean that this is the

**[2:06:42]** thing with all these frameworks is

**[2:06:43]** there's so much like word soup, word

**[2:06:45]** salad, like what does that even mean?

**[2:06:47]** And obviously it's not that hard to like

**[2:06:48]** get into the read me and stuff, but I

**[2:06:51]** don't even remember exactly what all

**[2:06:52]** these things mean. And I've used GST

**[2:06:54]** before. Uh okay, so here's what Archon

**[2:06:57]** supports for us.

**[2:06:59]** The closest existing workflow is the

**[2:07:01]** archon piv loop which yeah that's like

**[2:07:04]** literally the workflow that I described

**[2:07:05]** here in the diagram. So this is the

**[2:07:07]** closest to GSD because it has the same

**[2:07:10]** stages of planning and then implementing

**[2:07:12]** and then validating.

**[2:07:14]** Okay, so now it asks us some questions

**[2:07:16]** here. Uh wow, it asks us seven

**[2:07:19]** questions. Okay, let me try to get

**[2:07:20]** through these really quick. So uh is

**[2:07:22]** this a full project or a single feature?

**[2:07:26]** GSD covers an entire project life cycle.

**[2:07:29]** Archon workflows typically target a

**[2:07:31]** single feature or issue.

**[2:07:33]** Um,

**[2:07:35]** wait a second. I'm actually kind of

**[2:07:36]** confused by the question.

**[2:07:42]** Oh, I see. So, it's like, do we want to

**[2:07:43]** have it build an entire PRD for like an

**[2:07:45]** entire project or is it more like a

**[2:07:47]** workflow that takes a PRD or feature

**[2:07:49]** description and runs GSC style plan?

**[2:07:51]** Actually, let's do that. Yeah. So, for

**[2:07:54]** question number one, let's do something

**[2:07:55]** in between. So workload takes a PRD or a

**[2:07:58]** feature description and runs GSD style

**[2:08:00]** plan execute verify. That makes more

**[2:08:02]** sense. Um for the planning rigger,

**[2:08:07]** yes, I want the full planning rigger of

**[2:08:09]** GSD.

**[2:08:11]** Uh I do want all layers of verification

**[2:08:14]** like GSD.

**[2:08:16]** Where should human humans have approval?

**[2:08:19]** Let's just do the same as GSD. Actually,

**[2:08:21]** a lot of these questions aren't that

**[2:08:22]** good because it's just saying like, hey,

**[2:08:23]** what part of GSD you want? I really do

**[2:08:25]** want all parts of GSD for the sake of

**[2:08:27]** the demo here. And uh yep. So we'll do

**[2:08:30]** parallel research 100%.

**[2:08:33]** Uh where does the progress live?

**[2:08:38]** Yes, I want to create similar structured

**[2:08:40]** state files as GSD in the artifacts

**[2:08:43]** directory. That makes sense.

**[2:08:47]** Uh naming and positioning. How do you

**[2:08:48]** want to position this relative to

**[2:08:50]** existing workflows? Something like

**[2:08:51]** archon GSD or archon rigorous dev? Uh,

**[2:08:54]** yeah, let's just call it archon j-gsd.

**[2:08:58]** All right. Okay. Honestly, I wasn't that

**[2:09:00]** impressed with the questions it asked me

**[2:09:01]** there because mostly it was like, do you

**[2:09:03]** really want all this parts of GST? Which

**[2:09:05]** maybe that kind of speaks to how GST is

**[2:09:08]** a little overengineered. Like they they

**[2:09:09]** claim to be the simple version of things

**[2:09:11]** like BMAB, but I still think it has a

**[2:09:12]** little much. Um, but also like people

**[2:09:16]** get good results with it. Like trust me,

**[2:09:17]** it's popular for a reason. So I I do

**[2:09:19]** want to build an archon workflow here

**[2:09:21]** that that uh really takes inspiration

**[2:09:23]** from every part of GSD.

**[2:09:26]** So all right, we'll let it continue to

**[2:09:28]** rip here. So it's reading through uh

**[2:09:30]** some example workflows here, reading

**[2:09:32]** through the rule, my rules for workflows

**[2:09:34]** and how to build them, gathering context

**[2:09:36]** to then create the YAML for me here.

**[2:09:40]** Um open code integration. Yeah, so open

**[2:09:42]** code is one of the the uh coding agents

**[2:09:44]** we are we are considering adding that

**[2:09:46]** and PI agents. Yep. We'd love to add

**[2:09:49]** more.

**[2:09:51]** All right,

**[2:09:54]** let's see. Um, Archon doesn't work on

**[2:09:58]** Windows because it can't find the cloud

**[2:10:01]** code executable at runtime. Looks like

**[2:10:03]** it's a a known crossplatform issue

**[2:10:06]** between Linux, Mac, and Windows builds.

**[2:10:10]** Uh, so I'm running on Windows myself.

**[2:10:12]** I've never had that problem before. Um,

**[2:10:15]** so I'm not sure why that would be the

**[2:10:17]** case. If you installed through the

**[2:10:19]** binary, there might be a bug in the

**[2:10:21]** binary. I would try doing the

**[2:10:22]** installation method that's higher up in

**[2:10:24]** the readme where you clone the repo and

**[2:10:27]** then you go into claude and you just ask

**[2:10:28]** it to help you set up archon. I would

**[2:10:30]** try that instead. That's the only thing

**[2:10:31]** I could think of. Otherwise, I'm not

**[2:10:33]** sure why it would say it can't find the

**[2:10:34]** claude code executable because when

**[2:10:36]** you're running archon, it's just using

**[2:10:39]** claude under the hood and it's just

**[2:10:42]** using it in the same way that you if you

**[2:10:43]** ran claude from the terminal. So, it

**[2:10:45]** shouldn't be different.

**[2:10:50]** Uh what inspired me to build archon? Ah

**[2:10:53]** good question. So yeah, I kind of talked

**[2:10:56]** about things related to this in the

**[2:10:58]** stream already, but uh really it's like

**[2:11:01]** I see the direction that we're heading

**[2:11:02]** with AI coding. So this is what I talked

**[2:11:05]** about at the very very start of the

**[2:11:06]** stream. So maybe you weren't there at

**[2:11:07]** the start of the stream, which I mean

**[2:11:08]** probably a lot of you guys watching

**[2:11:09]** right now weren't, which is all good. Uh

**[2:11:12]** but like AI started with prompt

**[2:11:14]** engineering, generative AI like that was

**[2:11:16]** the big deal. Like how can we get the

**[2:11:17]** single best output from a model and then

**[2:11:20]** that evolved into context engineering

**[2:11:22]** especially for AI coding. It's like

**[2:11:23]** creating a whole ecosystem of context

**[2:11:25]** for our agent to handle longer running

**[2:11:27]** tasks. And that's like the big thing in

**[2:11:29]** 2025.

**[2:11:31]** And now this year it's like how do we

**[2:11:33]** create a system that combines coding

**[2:11:35]** agent sessions together to do longer

**[2:11:37]** work and how do we like really build our

**[2:11:40]** coding process as an agentic coding

**[2:11:42]** workflow. So the harness is the layer

**[2:11:44]** that wraps the coding agent to combine

**[2:11:47]** sessions together and add in more

**[2:11:49]** control for us. That's how we really get

**[2:11:52]** reliable results with coding agents. And

**[2:11:55]** so I've been really really doing a lot

**[2:11:57]** of research and deep dives into harness

**[2:11:59]** engineering over the past few months.

**[2:12:01]** But the problem is we have all of these

**[2:12:03]** closed source harnesses like Stripe

**[2:12:05]** shared stripe minions and Shopify is

**[2:12:08]** Shopify roast and adws is building their

**[2:12:10]** internal harnesses and and we have

**[2:12:13]** things like Ralph loops which are open

**[2:12:14]** source but also like not very intricate

**[2:12:17]** or like I mean the main problem is

**[2:12:19]** there's nothing out there that's like

**[2:12:20]** custom to you. So I wanted to build a

**[2:12:23]** tool that allows you to build your own

**[2:12:25]** harness. So no matter what your process

**[2:12:27]** looks like for AI coding, you can create

**[2:12:29]** it as a full workflow in Archon and then

**[2:12:32]** also run it at scale because we support

**[2:12:33]** the parallel execution like I've been

**[2:12:35]** demoing in the live stream here. So

**[2:12:37]** that's the inspiration. It's like I see

**[2:12:39]** where AI coding is heading and there's

**[2:12:41]** nothing like Archon right now. Like

**[2:12:43]** literally the only examples we have of

**[2:12:45]** anything like Archon is is a single

**[2:12:48]** harness. So it's not custom to you. It's

**[2:12:50]** very opinionated. Most of them are

**[2:12:51]** closed source and now this is the layer

**[2:12:53]** that build where you can build any of

**[2:12:55]** them or build your own. Yeah.

**[2:13:00]** All right. Thank you very much for your

**[2:13:02]** donation. I appreciate it a lot.

**[2:13:06]** All right.

**[2:13:09]** Cool. So,

**[2:13:12]** let's see what else we got here.

**[2:13:21]** Um,

**[2:13:24]** I do like cancel over abandon as well.

**[2:13:26]** More severe and implies the token use

**[2:13:28]** loss, right? Yeah, I mean you can resume

**[2:13:31]** it, but then you're restarting the last

**[2:13:33]** node that interrupted, which is Yeah, I

**[2:13:34]** guess kind of what you're getting at.

**[2:13:37]** All right. Um, so anyway, true story.

**[2:13:40]** This is the missing link. Glad you think

**[2:13:42]** so. Yeah, I mean I I really do like this

**[2:13:45]** all signal points to this. This is the

**[2:13:48]** most important thing. this year for AI

**[2:13:50]** coding, building software in general,

**[2:13:52]** and there's just not enough people

**[2:13:53]** paying attention to it.

**[2:13:56]** Like, okay, as much as I appreciate how

**[2:13:59]** much people are focusing on the new

**[2:14:00]** features in cloud code, like mo it seems

**[2:14:03]** like most people making AI content right

**[2:14:05]** now are just like covering the new

**[2:14:07]** things in claude code like over and over

**[2:14:09]** and over again. And like yeah, Anthropic

**[2:14:11]** is doing some very incredible things.

**[2:14:13]** It's like it is important to cover that

**[2:14:14]** but also it's like like look look past

**[2:14:17]** that like what what's what what are like

**[2:14:20]** the real ways to actually get good

**[2:14:21]** results with AI coding assistance. It's

**[2:14:23]** not just being hyperfocused on the

**[2:14:24]** individual features from anthropic

**[2:14:26]** releasing the cloud code. It it's

**[2:14:28]** focusing on how you build systems around

**[2:14:30]** AI coding. That's what I feel feel like

**[2:14:32]** people aren't paying enough attention to

**[2:14:34]** and what I'm really trying to focus on

**[2:14:36]** myself.

**[2:14:39]** All right, cool. So, let me open up.

**[2:14:44]** Let's see where we're at right now.

**[2:14:45]** Okay, actually I I just saw it finish.

**[2:14:47]** Good. So, perfect timing here.

**[2:14:50]** All right.

**[2:14:54]** So, yeah. One moment. I'm just looking

**[2:14:55]** at something on my other monitor here.

**[2:14:59]** Okay.

**[2:15:01]** All right. So, it built the full

**[2:15:02]** workflow.

**[2:15:05]** Um, actually, let me take a look at what

**[2:15:07]** it did here.

**[2:15:09]** Okay. So, it built out the YAML.

**[2:15:12]** It registered it as one of my default

**[2:15:14]** workflows. So, I I could actually like

**[2:15:16]** ship this to Archon today. I might

**[2:15:17]** actually do that, but I'll probably have

**[2:15:19]** to do a lot of validation of this before

**[2:15:21]** I actually push this live. But, it could

**[2:15:24]** be a cool workflow for you guys to use.

**[2:15:27]** All right. Um, and then so it ran the

**[2:15:30]** validate command to make sure that all

**[2:15:32]** the parameters are good. So, we have

**[2:15:33]** some things built into the CLI to

**[2:15:35]** validate workflows as well. I haven't

**[2:15:37]** tested end to end yet, but we can

**[2:15:39]** definitely do that as well.

**[2:15:41]** And so, okay, here's our pipeline. So,

**[2:15:43]** we spin up four agents to research in

**[2:15:45]** parallel. We synthesize everything into

**[2:15:47]** a summary and then we extract

**[2:15:49]** requirements with acceptance criteria

**[2:15:52]** and then we have an interactive loop to

**[2:15:54]** lock in the context. We create the

**[2:15:57]** plant. This is pretty comprehensive. GSD

**[2:15:59]** does a lot like it does more than you'd

**[2:16:01]** think when they claim to be something

**[2:16:02]** simple, but this is cool. It's really

**[2:16:04]** cool that we built this as a full archon

**[2:16:06]** workflow. And then we verify the plan,

**[2:16:09]** we have the human review, and then we

**[2:16:11]** execute.

**[2:16:13]** And then we do our verification, code

**[2:16:15]** review, and human acceptance at the end.

**[2:16:17]** Man, that is that is a lot. But there we

**[2:16:20]** go. That's what we just built. So, let's

**[2:16:22]** actually take a look at this here. So,

**[2:16:24]** if I go in, we have the new workflow,

**[2:16:27]** and it's pretty long. I mean, it's it's

**[2:16:29]** over,200 lines long, but that's just

**[2:16:30]** because all the prompts are in line. So,

**[2:16:33]** if I were to like really make this

**[2:16:35]** concise, what I would do is I would take

**[2:16:36]** all of these really long inline prompts

**[2:16:39]** and I would make them as commands like

**[2:16:41]** we saw in the GitHub issue fix workflow.

**[2:16:44]** Like this step is so much nicer looking

**[2:16:46]** because the whole prompt is just a

**[2:16:48]** command. So, it references the external

**[2:16:49]** markdown document. But anyway, we can

**[2:16:52]** address that. It's kind of nice to see

**[2:16:53]** it all in one place at first anyway,

**[2:16:56]** which is why I have it build like that.

**[2:16:58]** Um, so okay. So, for research, we

**[2:17:00]** decided to use Sonnet. Maybe we'd want

**[2:17:02]** to change that to ha coup. Totally up to

**[2:17:04]** you. Obviously doing that in a fresh

**[2:17:06]** session. So you are one of four parallel

**[2:17:08]** research agents. Your focus is on

**[2:17:10]** technology stack dependencies and

**[2:17:11]** development environment. And then we

**[2:17:13]** have researching the features. We're

**[2:17:15]** doing that in parallel as well. Um

**[2:17:19]** cool.

**[2:17:21]** And then yeah so we just have a bunch of

**[2:17:23]** research agents here. So four research

**[2:17:25]** agents running in parallel.

**[2:17:28]** And then we have the uh research

**[2:17:30]** synthesis. So it depends on all these

**[2:17:32]** being done, right? So these four can run

**[2:17:33]** in parallel but now this one has to run

**[2:17:35]** after. So it depends on these four being

**[2:17:39]** done and then we do our synthesis. So

**[2:17:41]** these agents

**[2:17:43]** uh have exported in parallel. Now we

**[2:17:45]** need to bring everything together into a

**[2:17:46]** single document and then we send that

**[2:17:48]** into the requirements gathering. So I

**[2:17:52]** mean most of what we're doing copying

**[2:17:54]** and GSD is just their prompting right

**[2:17:57]** and then like the different nodes for

**[2:17:59]** the different stages. So

**[2:18:02]** what do we have here? Okay. Yeah. So

**[2:18:04]** here's where we have the human approval

**[2:18:05]** gate. So we send the message to the

**[2:18:07]** user. Here's what you have to approve.

**[2:18:09]** Like here's the document that we just

**[2:18:10]** produced with the whole plan of attack

**[2:18:12]** split out into phases or whatever it

**[2:18:14]** does here. Uh so yeah, I don't I don't

**[2:18:16]** really want to like go into the details

**[2:18:18]** of every single node here. That's not

**[2:18:19]** really the point. But what we can do is

**[2:18:21]** we can also view the workflow in the web

**[2:18:22]** UI. So if I go to workflows here, I

**[2:18:25]** scroll down.

**[2:18:28]** Uh well, actually, hold on. I might need

**[2:18:29]** to restart the back end. No, it's right

**[2:18:31]** here. Yeah. So if I click edit, um take

**[2:18:34]** a look at this. Look at that. That's

**[2:18:36]** pretty cool. So we can also see the

**[2:18:38]** workflow in the UI. So we can see that

**[2:18:39]** we have these four running in parallel.

**[2:18:41]** So that that's set up that correctly.

**[2:18:44]** And then we do the research, synthesis,

**[2:18:45]** requirements, blah blah blah. I mean,

**[2:18:47]** this is a lot. I I probably won't be

**[2:18:49]** able to run this whole thing with you

**[2:18:50]** guys right now. Uh but I could I could

**[2:18:53]** get started. I think I have Yeah, I

**[2:18:55]** should be good on my limits here. So,

**[2:18:57]** let's let's try this right now. Um

**[2:19:00]** trying to think what a good example

**[2:19:02]** would be to run this. We're we're not

**[2:19:05]** going to be able to see this run to

**[2:19:06]** completion because this is going to take

**[2:19:07]** way too long. Um, but at least just

**[2:19:10]** showing you guys the start of it because

**[2:19:12]** then that that's like the full life

**[2:19:14]** cycle of like we had an idea for a

**[2:19:16]** workflow, we had Archon research how to

**[2:19:18]** build it, we built it, and then we run

**[2:19:20]** it. Like it's that easy to build

**[2:19:21]** anything. And so maybe what I'll do is

**[2:19:24]** I'll run GSD to handle a GitHub issue. I

**[2:19:27]** guess we could do that. Um, or no, you

**[2:19:29]** know, here's what we'll We'll have it

**[2:19:30]** we'll have it create uh the PI agent

**[2:19:32]** like okay I want you to uh run the GSD

**[2:19:36]** workflow here to build support for the

**[2:19:39]** PI agent SDK into archon as the third

**[2:19:42]** coding agent.

**[2:19:45]** And then uh let me make sure I knew it

**[2:19:47]** would say that wrong. PI agent SDK

**[2:19:51]** I could do open code. I could handle an

**[2:19:53]** issue. I I could do whatever. Right.

**[2:19:55]** This GSD workflow is very general. It's

**[2:19:57]** going to walk us through this very

**[2:19:59]** comprehensive process to build anything.

**[2:20:02]** So there we go. So we'll have it kick

**[2:20:03]** off the the CLI here. So we can monitor

**[2:20:05]** it in the web UI. We could even kick

**[2:20:08]** this off from the web UI as well. And I

**[2:20:10]** know I haven't really showed that in

**[2:20:11]** this live stream here, but we can run

**[2:20:13]** our workflows directly from the web UI

**[2:20:15]** as well. Like for example, check this

**[2:20:17]** out. I can go into the chat here and I

**[2:20:19]** can say um use the archon assist

**[2:20:22]** workflow to summarize the readme for

**[2:20:23]** archon. So I just want to do kind of

**[2:20:25]** like a a faster example here. But

**[2:20:28]** anything that we're doing from the CLI

**[2:20:29]** where we're asking claude code to invoke

**[2:20:31]** the CLI, we can just do it right from

**[2:20:32]** the web UI. So if you want to like have

**[2:20:34]** this deployed to a VPS running remotely,

**[2:20:36]** you can definitely do that. So you can

**[2:20:37]** see that it dispatches the workflow. It

**[2:20:40]** picks the so it routes to the right

**[2:20:41]** repository out of our registered

**[2:20:43]** projects because it has knowledge of all

**[2:20:45]** of that injected into its context. And

**[2:20:47]** then we can also view the logs for the

**[2:20:49]** workflow in real time as well. This is

**[2:20:50]** just a simple single node workflow.

**[2:20:52]** obviously

**[2:20:54]** but yeah we'll get the results here and

**[2:20:56]** then we can see that uh populate in the

**[2:20:58]** chat as well. So this is like the the

**[2:21:01]** main chat here is like your

**[2:21:02]** orchestrator, right? And then you can

**[2:21:04]** click into the logs for any individual

**[2:21:06]** workflow. Uh I don't know why that had

**[2:21:08]** that blip there, but yeah. Anyway, so

**[2:21:09]** you can click in and view the logs for

**[2:21:11]** individual workflows.

**[2:21:13]** Um and then here, let me click in. So we

**[2:21:15]** have our um GSD workflow running as

**[2:21:18]** well. So we can view the logs for this.

**[2:21:21]** We can see that it is currently in the

**[2:21:22]** middle of we can see that the like

**[2:21:25]** loading indicator for all of the initial

**[2:21:26]** research. So all these four are running

**[2:21:28]** in parallel right now and we can see the

**[2:21:30]** logs coming in in real time right here

**[2:21:32]** as it's going through all the tool

**[2:21:34]** calls. So basically all the tool calls

**[2:21:36]** from these nodes running in parallel are

**[2:21:38]** just being pushed here if we want to see

**[2:21:40]** what they're doing.

**[2:21:42]** Pretty cool. Uh yeah, this will

**[2:21:44]** definitely take a while to go through

**[2:21:46]** this process. But I I am actually keen

**[2:21:48]** on going through this full GSD workflow.

**[2:21:51]** I'm going to end with a poll request for

**[2:21:53]** the PI Asian SDK and then I'll I'll

**[2:21:55]** circle back with Raasmus and see what he

**[2:21:57]** thinks if this was actually a good

**[2:21:59]** implementation because he's working on

**[2:22:00]** this as well. Um, but yeah, I I might

**[2:22:03]** actually push this GSD workflow as one

**[2:22:06]** of the default bundled ones because I

**[2:22:09]** think it's just such a good example of

**[2:22:11]** how we can take a harness that's already

**[2:22:13]** out there and build it into Archon. Not

**[2:22:15]** that there's necessarily a huge reason

**[2:22:17]** to use Archon over just running GSD

**[2:22:19]** directly, but more just to show how like

**[2:22:21]** Archon goes above any existing harness

**[2:22:24]** because it allows you to build any of

**[2:22:26]** them. That's the power of it.

**[2:22:30]** All right.

**[2:22:34]** Um, okay. What if this could also be

**[2:22:36]** task centric? Pick the right workflow

**[2:22:38]** and the workflow combinations according

**[2:22:40]** to the task. I mean, you can basically

**[2:22:42]** already do that because you can have

**[2:22:44]** Archon load the Archon skill, look at

**[2:22:47]** all the workflows that it has access to,

**[2:22:49]** and then you can describe a larger scope

**[2:22:50]** of work and have it figure out the

**[2:22:52]** workflows to run. Or maybe it's just

**[2:22:54]** like a single workflow because you can't

**[2:22:56]** wrap up your entire process. But I like

**[2:22:59]** where your head's at with that because I

**[2:23:01]** mean, yeah, certainly. And like this

**[2:23:02]** kind of gets into um integrating Archon

**[2:23:05]** with your second brain. Your second

**[2:23:07]** brain, it learns how you work over time,

**[2:23:10]** right? So it kind of knows like based on

**[2:23:12]** Cole how Cole likes to work, I think

**[2:23:14]** like these archon workflows are what we

**[2:23:16]** should invoke to like handle this thing

**[2:23:17]** he wants to build. So that's definitely

**[2:23:19]** like a different discussion for another

**[2:23:21]** day.

**[2:23:23]** But I I could do a whole live stream or

**[2:23:25]** a whole Dynamus workshop on that.

**[2:23:30]** All right. Very cool. So yeah, while we

**[2:23:33]** wait for this to run here uh to for it

**[2:23:35]** to get to the next step, I'm going to

**[2:23:37]** chat about Dynamus with you guys really

**[2:23:38]** quick here as well. Oh, look. It looks

**[2:23:40]** like two of the workflows ran or the

**[2:23:43]** nodes are done. So, there's just two

**[2:23:44]** more we're waiting on here. But yeah, um

**[2:23:48]** Archon, a lot more workshops coming in

**[2:23:50]** in the Dynamus community soon here. And

**[2:23:53]** then also we got Okay, man. This 4hour

**[2:23:56]** workshop that I did last week in Dynamus

**[2:23:59]** went so incredibly well. Like there

**[2:24:02]** there are dozens of people in the

**[2:24:04]** community that are building their second

**[2:24:06]** brains right now and like sharing what

**[2:24:07]** they're doing and like how they're

**[2:24:08]** adapting things to be more specific to

**[2:24:10]** them. Like there's so much energy in the

**[2:24:12]** community right now for people building

**[2:24:14]** their own second brains and like going

**[2:24:16]** off of like the template that I gave in

**[2:24:17]** the workshop. It's so cool to see. So if

**[2:24:20]** you want to be a part of that like here

**[2:24:21]** I'm going to I'm going to put a link to

**[2:24:23]** to this in the chat here. There's a a

**[2:24:24]** special that I'm running for just this

**[2:24:27]** live stream. So, if you go to the link

**[2:24:29]** here, we got a special 10% off the uh

**[2:24:32]** the usual price for the community. And

**[2:24:34]** this special is going to end once the

**[2:24:36]** live stream is done. So, this is your

**[2:24:37]** chance to join the community and get in

**[2:24:39]** on everything that I'm doing more

**[2:24:41]** workshops for Archon coming and uh also

**[2:24:44]** the whole like third course that I'm

**[2:24:46]** adding to Dynamus for the second based

**[2:24:48]** on the second brain boot camp. And then

**[2:24:50]** I got the AI agent mastery and agent

**[2:24:53]** coding courses as well. Um, so yeah, all

**[2:24:56]** of everything that I'm doing with

**[2:24:57]** Archon, I've used all of my strategies

**[2:25:00]** that I cover in the Agentic coding

**[2:25:02]** course in order to build Archon. So I

**[2:25:04]** definitely um I don't just like, you

**[2:25:07]** know, say do as I say, not as I do,

**[2:25:10]** right? Like I I actually like use all

**[2:25:12]** the approaches every single day that I

**[2:25:14]** cover in the courses and the workshops I

**[2:25:16]** do in the community. So I'd love to see

**[2:25:17]** you join the community. And uh uh yeah,

**[2:25:20]** again, for everyone who's in the

**[2:25:21]** community in the stream already, always

**[2:25:23]** appreciate your guys' support and being

**[2:25:25]** here.

**[2:25:27]** So, all right, let's see where we're at

**[2:25:29]** now.

**[2:25:31]** Um,

**[2:25:33]** okay. So, it's still running actually.

**[2:25:34]** Let's see. Thought the research would be

**[2:25:36]** done by now. Um, oh no. Okay, it's

**[2:25:39]** almost getting there. So, well, no. Oh,

**[2:25:42]** the research is done, but it has to

**[2:25:43]** create the plan before it gets our

**[2:25:44]** approval. So, we haven't reached the

**[2:25:46]** next approval step yet, which is why the

**[2:25:48]** workflow is um still running in the

**[2:25:50]** background. But once it's done and it

**[2:25:51]** gets to the first human approval gate,

**[2:25:53]** then the workflow will pause and we'll

**[2:25:56]** get some output here questions for us or

**[2:25:58]** whatever. Like it'll give us the plan to

**[2:26:00]** review if we want.

**[2:26:04]** All right,

**[2:26:07]** cool.

**[2:26:09]** Um why define a model in the workflow?

**[2:26:11]** But what if we want AI to judge the

**[2:26:12]** model on the fly based on complexity?

**[2:26:16]** That's a that's a very fair question. So

**[2:26:19]** the main reason is

**[2:26:22]** how do you tell like

**[2:26:25]** the the the main AI agent that invokes

**[2:26:29]** the workflow? It doesn't really have a

**[2:26:31]** good idea of how powerful the models

**[2:26:33]** are. And it's a really tricky problem to

**[2:26:35]** solve. like how do I describe what haiku

**[2:26:38]** is capable of or what sonnet is capable

**[2:26:41]** of like you'd have to be very confident

**[2:26:44]** in your prompting in order to like

**[2:26:46]** really like give that control to the

**[2:26:48]** agent which is why we haven't really

**[2:26:50]** built that at this point. Now if if you

**[2:26:53]** do want to like really take your time to

**[2:26:55]** build out some kind of framework for the

**[2:26:57]** agent to figure out like how powerful

**[2:26:58]** each model is or like you tell it how

**[2:27:00]** powerful each model is so it can figure

**[2:27:01]** out what nodes need what models. you

**[2:27:04]** definitely could leave it up to the

**[2:27:05]** agent and and um that's definitely

**[2:27:07]** something we thought about adding

**[2:27:08]** support for is making it so that instead

**[2:27:11]** of it being hardcoded for each node,

**[2:27:12]** it's like the agent reads the workflow,

**[2:27:15]** picks the model for each step, and then

**[2:27:17]** sends it off based on the specific task

**[2:27:19]** because maybe the research for one

**[2:27:21]** specific implementation is actually

**[2:27:23]** going to be very complicated. So, we

**[2:27:25]** would want to use Opus for the research

**[2:27:26]** and then maybe we only need Sonnet for

**[2:27:28]** the verification because we think the

**[2:27:29]** research is going to be good enough. I

**[2:27:31]** don't know. I'm just kind of throwing a

**[2:27:32]** random example out there, but definitely

**[2:27:34]** like that could be a really good

**[2:27:36]** addition to Archon.

**[2:27:39]** All right.

**[2:27:40]** Super cool that I can use my

**[2:27:42]** subscription with this tool we'll be

**[2:27:43]** driving in today. Yeah, sounds great.

**[2:27:45]** And yeah, it it's fantastic. It if I

**[2:27:48]** couldn't use my Anthropic subscription

**[2:27:50]** with Archon, I would be using Codeex

**[2:27:52]** instead with Archon 100%.

**[2:27:55]** Yep.

**[2:27:57]** Okay. So anyway, the workflow completed

**[2:27:59]** its first three phases and it's now

**[2:28:01]** paused at the requirements approval

**[2:28:03]** gate. Very good. So here's what it

**[2:28:04]** finished and um

**[2:28:08]** now it's saying do the requirements look

**[2:28:11]** good. So obviously I need to know where

**[2:28:15]** the requirements are. That might be

**[2:28:17]** something that I need to address. So the

**[2:28:20]** workflow didn't like clearly state where

**[2:28:22]** the requirements are. So I I have to ask

**[2:28:24]** it. I mean that probably something I

**[2:28:25]** should improve in the workflow. So keep

**[2:28:27]** in mind that like just like your code

**[2:28:29]** bases, when you use Archon to build a

**[2:28:32]** workflow, it probably isn't going to be

**[2:28:34]** perfect first time around. You're going

**[2:28:35]** to have to iterate on the prompting and

**[2:28:37]** the nodes. So like right here, it's kind

**[2:28:39]** of annoying that I have to ask like, you

**[2:28:41]** know, where where's the requirements

**[2:28:43]** document? Like give me the exact path so

**[2:28:45]** that I can actually read through this.

**[2:28:46]** Um because right now it just kind of

**[2:28:47]** left me in the dark. So I mean, it's not

**[2:28:49]** a huge deal that I just asked for the

**[2:28:50]** path, but it's a little annoying.

**[2:28:53]** So let's get that then we'll actually

**[2:28:54]** take a look quick. Okay. So, this here

**[2:28:57]** is the path to it.

**[2:29:00]** Okay.

**[2:29:03]** So, I'll open this up in my IDE and

**[2:29:05]** we'll go to the summary.

**[2:29:08]** I think yeah, so I'm I'm building this

**[2:29:11]** so quickly live that like I don't have

**[2:29:12]** my head wrapped around the whole

**[2:29:14]** workflow right now. But I think the

**[2:29:15]** summary is is the synthesis from all So,

**[2:29:17]** these are like the research documents

**[2:29:19]** from each of the agents in parallel. And

**[2:29:22]** then this is the the synthesis that I'm

**[2:29:24]** going to have to review myself. So we're

**[2:29:27]** adding the PI agent SDK as a third AI

**[2:29:29]** coding agent into archon along with the

**[2:29:31]** existing cloud and codecs. Uh keep

**[2:29:34]** findings what already exists. So okay,

**[2:29:37]** this is good. This is what I talked

**[2:29:38]** about a little bit earlier in the

**[2:29:39]** stream. It is going to be so easy to

**[2:29:41]** build more coding agents into archon

**[2:29:43]** because it just has to reference how

**[2:29:45]** we've built things already for cloud and

**[2:29:47]** codecs. It's definitely going to oneshot

**[2:29:49]** this. So make sure we research PI agent

**[2:29:52]** first. We'll create the PI assistant

**[2:29:54]** defaults. So just again based off the

**[2:29:56]** patterns that we already have for cloud

**[2:29:58]** and codecs.

**[2:29:59]** We'll implement we'll follow the

**[2:30:01]** cloud.ts structure lazy logger async

**[2:30:04]** generator to send the query into PI. You

**[2:30:07]** guys probably don't care about the

**[2:30:08]** details here. I'm actually pretty

**[2:30:09]** interested in this. It it really

**[2:30:11]** understands what to do here. Um defining

**[2:30:14]** uh hooks and MCP and skills. Love that.

**[2:30:18]** uh laying out the critical risks as

**[2:30:20]** well, like things that we have to make

**[2:30:21]** sure we validate and be extra careful

**[2:30:23]** with or do more research for. And then

**[2:30:25]** it has open questions for us as well.

**[2:30:28]** And um so maybe what I'll do right here

**[2:30:30]** is I will answer the open questions and

**[2:30:33]** then send it off like approve the the

**[2:30:36]** workflow to continue with the rest here.

**[2:30:37]** So okay. All right. There are some open

**[2:30:41]** questions in the summary. I'm going to

**[2:30:42]** answer this quickly and then I want you

**[2:30:44]** to approve the workflow to continue. So

**[2:30:47]** for the PI agent SDK package name u well

**[2:30:50]** you know actually I don't know that. So

**[2:30:52]** I need you to search the web u for that.

**[2:30:56]** Um

**[2:30:58]** oh actually none of these questions are

**[2:30:59]** for me. These are all things that it has

**[2:31:01]** to research. So I I need you to research

**[2:31:02]** each of the uh answers to the open

**[2:31:04]** questions in the summary and then send

**[2:31:06]** that in as context to approve the

**[2:31:08]** workflow. Okay. So little bit of a pivot

**[2:31:10]** there. I thought it was like questions

**[2:31:12]** to align with me, but it was more just

**[2:31:14]** like uh you know mechanically how does

**[2:31:16]** the PI agent SDK work? So, we'll have it

**[2:31:18]** figure these things out. I thought that

**[2:31:20]** it would find those things in its own

**[2:31:22]** research, but I guess it's just like

**[2:31:23]** these are the gaps in the research that

**[2:31:25]** weren't covered by the other agents. So,

**[2:31:28]** yeah. Okay. So, it'll research these and

**[2:31:29]** then fill it in and then continue the

**[2:31:31]** workflow. So, it's pretty cool. We have

**[2:31:32]** a combination here of like we continue

**[2:31:35]** to work with Claude ourself and then we

**[2:31:37]** like pass context into the workflow when

**[2:31:39]** we want to continue it. And like that's

**[2:31:41]** the flexibility that I love with Archon

**[2:31:43]** is we aren't like once we send off the

**[2:31:45]** workflow as long as we have human

**[2:31:47]** approval gates. We don't have to just

**[2:31:49]** like let it go blindly and then end with

**[2:31:51]** that like final result. like we get to

**[2:31:52]** work with it along the way and even talk

**[2:31:54]** to our main Asian orchestrator to help

**[2:31:56]** us like guide the workflow if we really

**[2:31:58]** want to make the process reliable and

**[2:32:01]** how we usually work.

**[2:32:04]** So it takes a bit more time to do that,

**[2:32:06]** but in the end it's going to save you

**[2:32:07]** time when we have a process that's so

**[2:32:10]** elaborate like this with the human

**[2:32:11]** approval gates and everything.

**[2:32:15]** All right,

**[2:32:18]** cool. Um, okay. So, one thing I got to

**[2:32:20]** be honest with you guys on is uh the

**[2:32:23]** stream is going on so long that I I

**[2:32:25]** don't think Oops, I didn't mean to do

**[2:32:26]** that. Uh I don't think I'll be able to

**[2:32:28]** do the Dark Factory stuff today, but I

**[2:32:32]** might do, you know, I probably will do a

**[2:32:34]** separate live stream uh next week for

**[2:32:36]** the dark factory stuff. This is going to

**[2:32:38]** get very involved. So, I did a lot of

**[2:32:40]** prep for this. I'm like really excited

**[2:32:42]** for this, but it would take me at least

**[2:32:44]** another hour and a half to like go

**[2:32:46]** through the whole setup here with you

**[2:32:48]** guys. Um, and I've just had such a blast

**[2:32:51]** like helping you guys understand the

**[2:32:53]** value propositions of Archon and how to

**[2:32:55]** use it and how to build workflows and

**[2:32:56]** going through all your questions. I

**[2:32:58]** really appreciate all of your guys'

**[2:32:59]** questions today. And so I I'd much

**[2:33:02]** rather like focus on on that and have

**[2:33:05]** more of an introduction to Archon live

**[2:33:08]** stream versus like trying to force in

**[2:33:10]** this really fancy dark factory thing

**[2:33:12]** that's going to be quite involved.

**[2:33:15]** Um, okay. So cool. Now we got the

**[2:33:17]** research sending into the workflow.

**[2:33:18]** We'll let that run in the background. So

**[2:33:20]** I hope that sounds good to you guys

**[2:33:21]** because I I might also make a YouTube

**[2:33:23]** video on the dark factory stuff as well.

**[2:33:25]** I think that'd be super interesting.

**[2:33:29]** Um just to like maybe even kind of do

**[2:33:31]** like a build in public series where I

**[2:33:34]** show like how I'm setting up the archon

**[2:33:37]** workflows to manage different parts of

**[2:33:39]** the dark factory. How I have the code

**[2:33:41]** base kind of like self-evolve with AI

**[2:33:42]** managing literally all of the code

**[2:33:44]** review and codew writing. I think that

**[2:33:46]** could be cool. So, I'm curious what you

**[2:33:47]** guys think as well if you like the idea

**[2:33:49]** of that.

**[2:33:51]** Um, yeah, a lot of lot of ideas I have

**[2:33:55]** swimming around in my mind right now for

**[2:33:56]** content for the next week. A lot of

**[2:33:58]** exciting things with Archon and Second

**[2:34:00]** Brain content and just general

**[2:34:02]** strategies for AI coding.

**[2:34:06]** Okay. Wow, the workflow is already done.

**[2:34:08]** Is there another human approval gate?

**[2:34:10]** Let me see what Oh, curious what

**[2:34:12]** happened here.

**[2:34:16]** Oh, it's now in the discussion phase.

**[2:34:18]** It's reasking the open questions because

**[2:34:20]** the research answers didn't fully

**[2:34:21]** propagate the discussion node. Oh, okay.

**[2:34:24]** There might have been a problem in the

**[2:34:25]** workflow. So, again, there always option

**[2:34:28]** or opportunities to improve your

**[2:34:29]** workflow when you run it for the first

**[2:34:31]** time.

**[2:34:33]** Okay,

**[2:34:35]** let's check what our usage is at right

**[2:34:37]** now.

**[2:34:39]** Okay, we're at uh 60%.

**[2:34:44]** Not bad. We've been doing a lot with

**[2:34:47]** with Archon workflows this live stream

**[2:34:49]** and we've only you we've used about 43%

**[2:34:54]** of our 5h hour limit in this live

**[2:34:56]** stream, but there's a lot of work. We we

**[2:34:58]** handled five or four GitHub issues,

**[2:35:01]** validated them entirely. We're running a

**[2:35:03]** GSD workflow and there's a ton of other

**[2:35:05]** stuff that I've been prompting with

**[2:35:06]** Claude to like create workflows and

**[2:35:07]** stuff as well. Like it's pretty token

**[2:35:10]** efficient.

**[2:35:12]** So when you create your own workflows,

**[2:35:14]** just be careful that you're not using

**[2:35:15]** Opus for literally everything if you're

**[2:35:17]** using quad code or or make sure you're

**[2:35:19]** not using like the high reasoning GPT

**[2:35:21]** 5.4 codecs if you're using codecs uh for

**[2:35:24]** everything. So, but as long as you're

**[2:35:26]** for the pro the nodes that don't require

**[2:35:28]** as much reasoning, you're not using like

**[2:35:30]** the best model for everything. The

**[2:35:31]** workflows can be very comprehensive but

**[2:35:33]** really token efficient at the same time.

**[2:35:36]** Okay. So, there we go. We're we're

**[2:35:37]** continuing now in the workflow.

**[2:35:40]** All right. So, I think what I'm going to

**[2:35:41]** do here is I'm going to answer a couple

**[2:35:44]** more questions

**[2:35:46]** and then I will um end the stream.

**[2:35:52]** I think we'll call it there. But yeah, I

**[2:35:53]** definitely want to answer some more

**[2:35:54]** questions for you guys. We'll see how

**[2:35:55]** far we can get in this workflow here.

**[2:35:58]** One thing I just realized though is I

**[2:36:01]** think my

**[2:36:06]** my YouTube chat might be frozen. I might

**[2:36:08]** need to refresh.

**[2:36:12]** Yeah, hold on. Let me let me do

**[2:36:15]** something quick.

**[2:36:17]** Sorry, guys. I got to pop out the chat

**[2:36:19]** again.

**[2:36:24]** pop out chat. Sorry, my my streaming

**[2:36:26]** software is being like finicky right

**[2:36:27]** now. For some reason, I'm not seeing the

**[2:36:30]** chats come in on my other platform.

**[2:36:35]** Uh oh, I just lost them all. Shoot.

**[2:36:38]** That's unfortunate. Well, I can answer

**[2:36:40]** some questions, but I won't be able to

**[2:36:41]** show it on my screen.

**[2:36:44]** Uh let's see if I can blitz through a

**[2:36:45]** couple here.

**[2:36:48]** Let's see.

**[2:36:51]** Yeah. Oh yeah. So someone mentioned

**[2:36:52]** Anthropics advisor mode. Yeah. So I I am

**[2:36:56]** interested in building that into archon.

**[2:36:58]** So the advisor mode is basically you can

**[2:37:01]** use less powerful anthropic models to do

**[2:37:04]** like the grunt work the implementation

**[2:37:06]** and then you have it like call into a

**[2:37:09]** larger model like opus or maybe mythos

**[2:37:11]** if that's really going to become a thing

**[2:37:13]** for us. And then it like kind of like

**[2:37:16]** just asks it for guidance and then it

**[2:37:18]** continues to do the implementation or

**[2:37:20]** planning or whatever. That's pretty

**[2:37:22]** cool.

**[2:37:24]** All right.

**[2:37:27]** And yes, Joe, you can use and you can

**[2:37:29]** use Archon 3 or anthropic subscription.

**[2:37:31]** Yep, 100%.

**[2:37:35]** All right.

**[2:37:40]** Um, can we let the user decide which

**[2:37:42]** models he wants to allocate to his task?

**[2:37:44]** Um, or is it kind of hardcoded at the

**[2:37:46]** node workflow level? So, you can have

**[2:37:48]** your coding agent edit the workflow

**[2:37:50]** live. Otherwise, it is hardcoded. Not it

**[2:37:52]** is something we are interested in adding

**[2:37:53]** though support for like defining the

**[2:37:55]** models up front or like live during the

**[2:37:58]** live execution.

**[2:38:00]** Yeah.

**[2:38:02]** All right. Um, let's see. What about rag

**[2:38:05]** and storing previous questions on SDKs

**[2:38:07]** and such? I wouldn't want every workflow

**[2:38:10]** that works with Python to search the

**[2:38:11]** SDK.

**[2:38:14]** So, well, the thing about archon is you

**[2:38:16]** can build in your own memory system.

**[2:38:18]** Like, if you have a way using git logs

**[2:38:19]** or claude mem or or rag like whatever

**[2:38:22]** you have for memories for your agent,

**[2:38:24]** you can build that into archon workflows

**[2:38:26]** because you can give it the skill or the

**[2:38:27]** MCP or or just like the prompting for it

**[2:38:29]** to use whatever. Um so that the

**[2:38:32]** flexibility of archon is like you don't

**[2:38:34]** have to abandon any approach or wait for

**[2:38:36]** us to support it directly. Like if you

**[2:38:38]** want to use linear you can just attach

**[2:38:41]** in the MCP or skill or like if you want

**[2:38:43]** to use the claude mem framework or beads

**[2:38:45]** or whatever like you can build that

**[2:38:47]** directly into the uh archon workflow.

**[2:38:53]** All right. Uh remind us what is the dark

**[2:38:54]** factory. Okay. Yeah. Um

**[2:38:59]** I'll I'll bring I'll talk about that for

**[2:39:00]** a sec here. So okay the dark factory

**[2:39:04]** it's the concept of having a code base

**[2:39:07]** that is entirely managed by coding

**[2:39:09]** agents. The coding agents handle the

**[2:39:11]** coding the reviewing the the pull

**[2:39:13]** requests and the releases. And so the

**[2:39:16]** only thing that the human gives is the

**[2:39:18]** issues for bugs or new features that

**[2:39:20]** we're requesting.

**[2:39:22]** But there's no human approval allowed.

**[2:39:25]** all code just go straight to the main

**[2:39:26]** branch once coding agents finish it. And

**[2:39:29]** for a public experiment, I'm actually

**[2:39:31]** really excited for this. For a public

**[2:39:33]** experiment,

**[2:39:35]** I want to have a repository that is a

**[2:39:38]** dark factory and it's managed entirely

**[2:39:41]** by Archon workflows. I think it's going

**[2:39:43]** to be so cool and it's going to show the

**[2:39:45]** power of Archon because we're going to

**[2:39:46]** have workflows to triage issues like

**[2:39:48]** figure out which ones we actually want

**[2:39:49]** to address and then like do the

**[2:39:51]** implementation, do the review, manage

**[2:39:53]** the releases, deploy things to

**[2:39:55]** production. It's going to be so cool.

**[2:39:57]** So, I was going to like maybe get

**[2:39:59]** started with that in the live stream

**[2:40:00]** today, but there's no way like I gota I

**[2:40:04]** got to do that in a separate live stream

**[2:40:05]** or maybe even make a YouTube series on

**[2:40:07]** it. So, that's what's up with the Dark

**[2:40:09]** Factory. It's kind of a silly name, but

**[2:40:11]** it's also kind of a really cool name.

**[2:40:13]** So, that's what I'm calling it. A lot of

**[2:40:15]** people have been like thinking about

**[2:40:17]** this kind of thing. There's a use case

**[2:40:19]** out there or like a anecdote out there

**[2:40:21]** from Strong DM. If you guys have heard

**[2:40:23]** of Strong DM, they basically built an

**[2:40:26]** internal dark factory. StrongDM dark

**[2:40:29]** factory.

**[2:40:31]** So, they're they're a uh company that

**[2:40:34]** so a strong DM AI lab with a simple

**[2:40:36]** premise. how best to maximize building

**[2:40:38]** software with AI. So they've created a

**[2:40:42]** and this is like more internal so it's

**[2:40:43]** not like open source like what I'm going

**[2:40:45]** to do but they've built a system where

**[2:40:47]** like they are pushing thousands and

**[2:40:49]** thousands of lines to production like

**[2:40:50]** like humans never review.

**[2:40:53]** Not that I recommend that as the way to

**[2:40:54]** go to get the most reliable production

**[2:40:56]** software but the point is like it's an

**[2:40:58]** experiment and I'm really excited to try

**[2:41:00]** that out. So that's the plan.

**[2:41:04]** All right.

**[2:41:08]** Um, can we use local AI? Yeah. So, you

**[2:41:11]** can you can have cloud code integrate

**[2:41:13]** with Olama directly to use local AI

**[2:41:15]** within Archon 100%. I would just uh look

**[2:41:18]** into like the Olama

**[2:41:23]** or Claude code. They have uh direct

**[2:41:26]** integration if you want to look into how

**[2:41:28]** to do that.

**[2:41:30]** Yeah.

**[2:41:32]** What does a dark factory do on a sunny

**[2:41:34]** day? Well, you just have no windows.

**[2:41:37]** That's what you do. Um, what is the

**[2:41:40]** domain idea or function for my dark

**[2:41:42]** factory project? Yes. So, this is going

**[2:41:45]** to be another big thing. Where is my

**[2:41:48]** repo? I have so many things open right

**[2:41:49]** now. This is another big project that

**[2:41:51]** I'm going to work on. And uh the dark

**[2:41:53]** factory is going to be this is going to

**[2:41:55]** be the use case for the dark factory. I

**[2:41:58]** want to create an application that

**[2:42:00]** allows you to basically chat with my

**[2:42:04]** YouTube content. So, you can ask

**[2:42:06]** questions and it's basically like you're

**[2:42:08]** talking to me directly because it

**[2:42:09]** performs rag over all my YouTube

**[2:42:11]** content.

**[2:42:13]** And then for those of you in the Dynamis

**[2:42:15]** community, I also wanted to ingest all

**[2:42:17]** of my course and workshop content in the

**[2:42:20]** community. So, it's basically like your

**[2:42:21]** own personal AI coach that has access to

**[2:42:24]** all my information and maybe even going

**[2:42:26]** so far as to like ingest um you know

**[2:42:28]** like community posts and things like

**[2:42:29]** that as well. I think this is going to

**[2:42:31]** be such a cool example for the dark

**[2:42:34]** factory because it's a relatively um

**[2:42:36]** complex application like the whole rag

**[2:42:39]** pipeline and the searching and the web

**[2:42:40]** UI and everything but also it's going to

**[2:42:42]** be very easily testable because we can

**[2:42:44]** just like test conversations with like

**[2:42:46]** the agent browser CLI. So you can have

**[2:42:48]** like browser automation for the dark

**[2:42:51]** factory to run like every time it does

**[2:42:53]** validation on the codebase or like for a

**[2:42:55]** specific issue. Um so that this is this

**[2:42:58]** is what I'm planning on having as the

**[2:43:00]** use case for the dark factory and then

**[2:43:02]** it'll also be like a huge value ad to

**[2:43:04]** the Dynamus community because then it'll

**[2:43:05]** give you like a chat platform to talk

**[2:43:07]** and ask any questions about any of the

**[2:43:09]** courses or workshops or even like point

**[2:43:11]** you to the videos in the courses or the

**[2:43:13]** workshops to watch for things that you

**[2:43:14]** want to learn. So yeah, I'm really

**[2:43:17]** really excited for this. I wish I had

**[2:43:18]** time to cover in the live stream today,

**[2:43:20]** but yeah, I'm definitely I'm definitely

**[2:43:22]** going to have to cover this later, but

**[2:43:24]** I'll be using Archon workflows to like

**[2:43:26]** guide the entire process of managing

**[2:43:27]** issues and pull requests and reviews and

**[2:43:29]** things like that. So, it's going to be

**[2:43:31]** pretty exciting.

**[2:43:33]** And yeah, there there is there's so much

**[2:43:35]** content in the Dynamis community that

**[2:43:38]** like it's it's hard to like really

**[2:43:41]** navigate through it all. I mean, I make

**[2:43:43]** it easy obviously to like look through

**[2:43:45]** past workshops and I'm always like

**[2:43:46]** letting you know like the things that

**[2:43:48]** I'm working on and the courses and

**[2:43:50]** stuff, but like there's a lot of stuff

**[2:43:51]** there. So, I think this is going to be a

**[2:43:52]** really big value ad. So, just yet

**[2:43:54]** another one of those things coming to

**[2:43:56]** the Dynamus community. So, you know, as

**[2:43:59]** I end the live stream here, I just want

**[2:44:00]** to give a link to this one more time

**[2:44:01]** because there is the special discount

**[2:44:03]** for Dynamus that's going away when the

**[2:44:05]** live stream ends. And so if you're

**[2:44:07]** interested in really being on the

**[2:44:09]** forefront of archon and AI coding, if

**[2:44:11]** you want to be a part of the weekly

**[2:44:13]** workshops that I do and the new uh 4hour

**[2:44:17]** second brain boot camp that I just did

**[2:44:19]** last week, then come join and be a part

**[2:44:21]** of the Dynamist community. I would love

**[2:44:22]** to have you. So yeah, I know there

**[2:44:25]** there's a lot of uh really really good

**[2:44:27]** questions that I didn't get to in the

**[2:44:29]** chat. It's always unfortunate. I I love

**[2:44:31]** doing these live streams and I love all

**[2:44:34]** your guys' questions. It's just hard cuz

**[2:44:35]** there's like so much. Um, but yeah, if

**[2:44:38]** you ever have any questions like feel

**[2:44:39]** free to, you know, comment on my YouTube

**[2:44:41]** videos as I do more on Second Brain and

**[2:44:43]** and Archon content or, you know, always

**[2:44:46]** available in the community to answer

**[2:44:47]** your questions there. Uh, so yeah, I'm

**[2:44:50]** going to go ahead and uh call the live

**[2:44:52]** stream here, but stay tuned for more

**[2:44:55]** content on Archon and the Dark Factory

**[2:44:58]** stuff as I start doing that. It's going

**[2:44:59]** to be a really really fun experiment.

**[2:45:01]** And yeah, thank you everyone for for

**[2:45:03]** being here. This is a really fun live

**[2:45:05]** stream. I just I'm so passionate about

**[2:45:07]** Archon right now. So, it's really cool

**[2:45:08]** to just demonstrate everything to you

**[2:45:10]** guys and answer your questions and build

**[2:45:11]** workflows live. Uh might even push that

**[2:45:14]** GSD1 to the repo if it works well.

**[2:45:16]** Probably to, you know, iterate on that

**[2:45:17]** though. But yeah, anyway, thank you

**[2:45:19]** everyone for being here. I hope that you

**[2:45:21]** guys have a fantastic weekend and I will

**[2:45:24]** see you all on the channel and in the

**[2:45:26]** Dynamus community. Take care everyone.
