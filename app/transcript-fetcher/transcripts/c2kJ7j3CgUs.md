# Transcript: c2kJ7j3CgUs

**URL:** https://www.youtube.com/watch?v=c2kJ7j3CgUs
**Segments:** 1266

---

## Full Text

So, take a look at this for a second. Install a skill, set a schedule for an automated job, and then get the result delivered to you on your phone. That's it. That is the pitch for Hermes and the pitch for OpenClaw pretty much, too. And honestly, when I first saw this, I was completely sold because in reality, this is exactly what every business owner wants. The work's going to get done in the background. You're going to get the good result. There's no babysitting. There's no back and forth. But then you actually go to try it, and the setup's super messy and technical. And if you want the best models, you're going to pay extra because it's not available on Claude subscription. So, in reality, it looks simple, but it's actually not. And I know a lot of you are in this exact same spot because I've seen your comments on my YouTube videos. Some of you are testing Hermes, trying OpenClaw, or even thinking about building your own. And I was there, too. And while I was going through it, I ended up actually just building my own version. One that runs on Claude subscription. So, it doesn't cost me a fortune because every single thing in this diagram, you can already do inside Claude code. And for a business owner, the claw code version is actually better because you can see exactly what's going on inside the blackbox. So in this video, I'm going to break down the five features that actually make a system like this and share what I learned along the way. So if you're thinking about using Hermes, OpenClaw, or even just building your own, you'll know exactly what to focus on to get started. So when I ran Hermes and OpenC Claw side by side with my own setup, I noticed that they all have different rappers, different UIs, different channels you can contact them from, but underneath it's actually just the same five features driving everything. So the first is persistent memory. So think about memory that actually learns about you as you work with it. Then you've got skills that create themselves first of all and then get better over time. The third is how you actually interact with it, which is way bigger than just a chat interface on your phone, by the way. Then we've got scheduled tasks that actually run themselves. So not being at the computer window and still getting things done. And then finally, this is the big one, business context. How to inject the right context at the right time to make all your results contextualized to your business and produce therefore better outputs. So get all of these five inside claw code and you don't need a separate framework like openclaw or Hermes. And you can even run it on Claude's most powerful models like Opus 4.7 released just days ago without paying for the API credits. So you can use it on your Pro and Mac subscription. So let me first start with the one that most people get wrong and that's persistent memory. It's probably the biggest selling point of Hermes and Open Claw. So unlike temporary chat rappers, they're supposed to maintain long-term searchable memory of past conversations and projects. And this is what gets us hooked initially because the idea that my agent will actually remember what we worked on yesterday last week and therefore contextualize and be better for the results going forward sounds amazing. And if you've worked with claw code for more than just a few sessions, you'll know just how important context management actually is for getting high quality outputs. But claw code actually already has all the ingredients for this. We just need to set them up properly. So I've distilled this into just four memory layers that you can use. The first is claude.mmd or agents.mmd if you want to actually use this with different models. So think of this just as your agents operating instructions. Who it is, how it behaves, what rules it follows and it's going to load into every single session. Most of you will have this layer already. Now layer two is brand context. So this is where your business context is actually going to live. Think your brand voice, how you speak, ICP, your positioning, all your client details will live in this brand context shared folder. And therefore, every skill inside the repository can pull from the same folder. So when Claude writes a LinkedIn post for you, when it's doing client research, when it's building out your landing page, it's going to pull from the exact same business brain. And as you imagine, it gets much better outputs that are hyperfocused on your business. Now, layer three builds on top of that. And this is what makes agents like openclaw and hermes and those frameworks feel so personal. So this is the agent context folder. So we have things like the sold.md and the user.md which describe how it should act and feel and the actions that you as a user using it commonly do. So it feels like it understands you. And finally layer four we have project memory. So each project you run actually keeps a history of exactly what's happened as well as a plan that you can refer to. So when you actually come back to a content repurposing project that you did 3 weeks later, Claude is going to know exactly what you built, what worked, what didn't work, and where we need to pick up on that. Now, from this four layer framework, here's the first key learning that I wanted to share with you. It doesn't matter how you set this up. You can put your project briefs anywhere. Use whatever planning frameworks you like to write the plans. So for example, we use GSD or the get done frameworks for more complex projects, for example. But the core ingredients are that actually you're just loading in the right context at the right time. So you're not bloating context and experiencing context rot where the outputs are getting worse the more context you feed in. So your claw.md shouldn't be 2,000 lines long. It shouldn't even be a thousand lines long. It should actually just reference the most important process steps that are going to get loaded in at the start of the conversation. So any additional context that needs to be pulled in at a specific point needs to be stored in a separate reference file. So now I keep my agents.mmd if you want to work across models or your claw.md succinct and to the point and then just point it to reference files. So see here where I've separated my brand context and tell it to load it in only when it needs it. That way claw can actually load and offload into separate agents and maintain highquality outputs because we're not bloating the context. And we use exactly the same approach with every single skill. short entry skill.mmd file detailed references which are only loaded and offloaded when needed. So the first feature then is a memory layer. This is just about organizing context in a way that actually suits your business and your needs. So you just need to structure it properly, segment your context, point it to reference files and not overload those context files. And by the way, there are a bunch of different memory and context storage solutions that you can choose from. So you've got Obsidian, you've got the open claw style setup which we're showing here. We've got Karpathy's LLM wiki and even people are building customuilt frameworks for memory management. So there's a whole host of ones with different benefits depending on your use cases. So if you do actually want a comparison of these different memory models and when you use which, then drop a comment below and I'll do a full comparison about which one works for which use cases to help you get this memory system set up for your business. But anyway, that's memory. So let's look at what actually uses that memory to get the work done, which is skills. So Hermes has two features that often get bundled together in all the demos. The first is a persistent learning loop. So think of skills that actually improve themselves over time. So an agent does a task, evaluates its performance, and then it's going to refine that skill over time. And the second is automatic skill creation. So you can generate a new skill and then apparently share them via agentskills.io. And this is genuinely some seriously important features knowing now what I know about how important skills are for actual output quality. So skills are basically importing expertise to improve our output quality by giving it a really refined process document for a specific task. So you might have LinkedIn post creation skills, you might have copywriting skills, you might have lead generation research skills, all of those will be ported into skills. But again, if we reflect on the Claude code ecosystem, you can actually just build in yourself to that system. And the benefit of doing that is you know exactly how it works too and you can refine and iterate on it over time. So if we tackle creating skills first, claude code has the skill creator skill which you might have seen before. It's built by Anthropic themselves and basically you give it a description of what skill you want or you point it to a GitHub repo with an existing skill or describe a process from scratch on how you do it. And it's going to build out the entire thing, the name, the description, and that determines the success rate of whether it's called or not. And then obviously the step-by-step process document of the actual skill.md file itself. And if we reflect back on how we manage context, what we want to do is keep a refined skill.md file less than 200 lines and then strip out everything that's unnecessary. So we've actually adapted the anthropic skill creator skill to do exactly that. Strip out the surplus information and keep that separate and only load it into context exactly when you need it. Now on top of creating skills, every skill you build should have a self-arning loop baked in. So you have a skill definition inside your skill.md file. You have its reference files for additional context and you can go one step further with a learnings.mmd file or just a rule segment actually inside your skill.md which are basically non-negotiable rules that each time you use that skill or each time Claude is going to use that skill it will get better at abiding by those specific rules that we've added in. So as part of the skill process as one of the steps in the skill.md you get it to ask you for feedback. So it effectively takes the feedback then that you give it applies any rules inside your learnings.mmd or inside that skill file and then always sticks to by those rules when you use that skill again and again. So it's effectively a self-learning loop where the skills get better over time. So inside claw code you can replace that functionality by actually just using the skill creator skill and then you make them get better by applying rules inside the learnings.mmd or just rules inside the skill document itself if it's asking you for feedback every time. So, so far we've got memory and we've got skills that create themselves and get smarter over time. The next big question is how do you actually interact with this system dayto-day? So, it's no secret that every agentic framework in 2026 so far is been competing on interfaces. So, open claw gave you telegram, discord, slack, WhatsApp. Hermes is similar and claw code has been bringing out features left, right and center to try and replicate this to give people access to message their agents from phone. So you can kick off a task while you're out, check the output whilst you're on the move, and that's all great, but here's the thing that nobody is actually talking about. The interface question, in my opinion, isn't just, "Can I chat from an agent from my phone?" The real question now that agents are so good is how do we manage multiple conversations and multiple goals at the same time. The models are now so good that it's pushing us into a different role. We're now jumping into a supervisor role when we need a better way to actually be able to manage multiple agents and multiple projects on the goto. And all of the frameworks I've seen give you one conversation at a time. So you're going to open Telegram, you chat to one agent, you get one output back, which is great for a single task, but what happens when you've got six business goals all running in parallel? What happens when you want to set up a zero employee company and you run multiple departments through different agents? Like flicking between those chat threads and trying to remember which one was which, which one was writing your newsletter, which one has filled its contact window is actually pretty difficult. So, let me show you how you can get claw code to handle this and how I did it myself. So, first for quick asks, you've got the claw code inbuilt channels feature. So, this is Anthropic's official feature that's going to work with Telegram, iMessage, and Discord out the box. So, you don't need to do anything to actually access your conversation at your phone already. So, exactly what Hermes promises, but shipped natively by Anthropic. Now, and here's where it gets really interesting. If you're running a real business on claw code, managing multiple conversations, then you need to actually abstract that and build a UI layer on top. So I did exactly that and I call it the command center. And the idea is really simple. So instead of managing terminals or chat threads, you just manage your business goals. So you drop in a business outcome. Claude is going to spin up an instance to handle it and it's going to show up on your canban style board where you've got full visibility of all your goals running in parallel. you're able to click into one and see the full conversation and you can have sub chats inside those conversations too. And you can even have the plan on the right hand side next to the chat window. So you could have four agents working on different features here and then the plan on the right hand side which is going to auto update as you run through the plan. So this is set out for larger more complex projects. You still have the granularity of the individual chat interface, but you're able to abstract yourself to a supervisor role because you can see how the chats are working against a plan and how that is all working against an individual business goal as well as then dig into the other business goals that you've currently got on the go. So, the workflow becomes then quick conversations while you're out and about. You can just fire it into Telegram via the channels feature. But if you've got a big goal that you want to manage over a day or a week or a complex project, then for example, I would drop it into my command center and come back to actually review the outputs here and manage multiple goals inside that. All of this, for example, you can build exactly for yourself. You can follow this structure that I'm showing you on screen. And it all runs locally and acts as just a UI wrapper on top of your terminal. So, it abides by Anthropic's Oorth usage policies, meaning you can actually use it with your Pro and Mac subscriptions. And if you want to get this up and running without having to build it yourself, it's just a oneline install as part of our paid community in the description below. And it includes all the underlying Aentic operating system logic that we're covering today, too. So full business context out of the box, 20 plus skills, scheduled workflows, the lot, all set up extremely quickly to handle tasks on behalf of you or your business. So check out the link in the description below if you're interested in that. So, how you interact with it matters way more than most people think. Most people are just jumping to actually interact with it on the phone, but phones are only good for quick asks and you can use claw code channels for that. But if you want to build out something managing multiple goals, then you need your own interaction layer. Now, the one caveat I'll put on this. Claude have just updated their own claw desktop to actually accommodate for managing multiple goals. However, it's still very technical, very focused on GitHub commits and not focused on that highle planning view with built-in planning frameworks like the way I've built it out for myself. So, it depends what you're looking for as to what is the right solution for you. And that's how we interact with claw code in a similar way to like open clause mission control for example. So, we've got memory, we've got skills, we've got the interaction layer. Now, let's look at the stuff that you should just be able to let run without you actually interfering with it. So Hermes lets you set up automated jobs on a schedule. So you can install a skill, create a recurring job, and then it's going to run automatically. And in claw code, you can do exactly the same with the new routines feature inside their desktop app. But right now, the feature is limited to built-in connectors. So it's quite difficult to interact with apps that aren't in their native built-in connectors, especially when you can actually build this out using claw code to leverage the built-in functionality on your Mac or Windows machine. So you don't need a virtual private server. You don't need extra infrastructure. Pro code can actually set up this logic for you in less than a few hours so that you can just control your scheduled jobs from a few files. When they're noted as active, we're going to run those scheduled jobs. And when they're not active, we're not going to run those scheduled jobs. Now, most people are creating scheduled jobs to just insert a simple prompt. But actually, the smartest people are actually using scheduled workflows to chain skills together inside a prompt. So, you can schedule a task that's effectively going to run multiple skills in sequence. You might have a weekly content digest that runs every Monday at 9:00 a.m. So, it's going to pull the previous week's YouTube videos, run an analysis across those, and then generate three LinkedIn posts using your voice profile, and then drop them into a review folder. So, you come in on Monday morning, you've got all of those already ready in the review folder. And they're contextualized and followed all of the skill process documents that produce high-quality outputs. So many different skills all chained together to produce one output that you come back and you can approve or supervise. And the biggest learning when I started building this out, my original aim was to build out fully autonomous scheduled workflows, run the whole thing, ship the output, post it to LinkedIn, whatever. But it was actually pretty bad because 20% of the time something wouldn't be quite right. So instead, I've actually built this framework now around doing 80% of the work automatically, the research, the narrowing of different topics. But what I've added in is always having a human checkpoint before anything goes live. So I'm never going to post content that's just AI generated stuff. I'm always going to have that human supervisor in the process until we can get to a level of quality where things can run autonomously and we're happy with them. So all of my content drafts, for example, land in a folder so that I can actually come in and supervise them and review them and approve the outputs. So it's basically giving you the speed of the automation without the risk of shipping something that's just pure AI slop, which we do not want to contribute. So you can effectively use scheduled jobs to chain multiple skills together and then add in a human checkpoint to actually approve or make sure the quality is high. Right? So that is four amazing features. Each one you can build inside claw code using what's already there in just a few days. But here's the fifth and honestly this is the one that made me stop looking at Hermes and OpenClaw because I did not see enough capacity for it to do this well. Now because Hermes and OpenClaw are built solely to be agent frameworks, they're very tool focused. So, it's all about installing a skill, running a job, getting an output, but they don't know anything really about your business. You can, of course, install ways to actually give it information about your business, but they don't out the box know your brand voice, know your ICP, they don't know your positioning, they don't know who your clients are, what your tone in your emails usually is. All of these things are critical for high quality outputs. And it's the equivalent of basically starting from zero when you run a new skill. And this is what shifted me away from systems like Hermes and Open Claw to build my own system because I realized that the real unlock isn't actually the agents. The agents and the models are getting better and better. It's the layer underneath the context that we discussed at the start. The brand context folder, the voice profile, the audience avatar, all of that preloaded pulling into the right skill at the right time is what actually generates high quality outputs. So I actually pulled together myself a set of skills that help me generate my voice profile and I make sure that when I build out my skills using the skill creator skill all of them reference the right context at the right time. So if I have a skill that builds out LinkedIn posts for example it will always reference my brand voice. It will understand the positioning because it understands who my clients are. And I used content as an example because it's relatable to a lot of different businesses. It doesn't mean you need to use these systems to actually generate your content. And the way that we've done this is basically moving everything, all of that context for my business into a single brand context folder that every skill is able to reference. So you update the information once and every skill gets that update when it runs. So business context is that compounding advantage that you cannot get right now. So build this, right? And this totally underpins all of the other pillars that we've talked about today. You need to inject the right context at the right time. And that starts with actually having a shared context folder that focuses on your brand and you. So when you bring this all together, this is exactly how it looks in a three-step process to compare to the one we showed at the start. We have your own agentic operating system where we have the business brain which underpins and powers cloud code by injecting the right context at the right time. We're able to then actually just write goals whether that's to create a scheduled job or to manage multiple business goals in one place. Claude is then going to do the work in the background to break it down into subtasks, choose the right skills, etc. And what that enables is your system to deliver you a highquality result that's contextualized by your business context completely replacing the need for a framework like Hermes or Open Claw and without all of the technical overhead and cost implications of moving off the pro and max plans from Claude. So that's the five features that actually matter and how to build each one of them inside Claude code yourself. And if you're building out your own version right now, which a lot of you in the comments have told me you are, here's my honest advice from three months of getting this wrong and rebuilding it. Start with this business brain. Don't start with the agents. Don't start with the multi- aent orchestration. I made this same mistake. Every feature I just walked through gets multiplied by having the solid context, the foundation layer underneath it. And none of them are going to work without that layer. And if you just want to skip the setup and grab the whole thing plugandplay today, then check out the link below in the description for the Aentic Academy. So, we've got the Aentic Os, the command center that you saw today with the dashboard and all 20 plus skills ready to go with a oneline install. And if you want to see exactly why I built out the command center in the first place, then check out the next video. Thanks for watching. So, take a look at this for a second. Install a skill, set a schedule for an automated job, and then get the result delivered to you on your phone. That's it. That is the pitch for Hermes and the pitch for OpenClaw pretty much, too. And honestly, when I first saw this, I was completely sold because in reality, this is exactly what every business owner wants. The work's going to get done in the background. You're going to get the good result. There's no babysitting. There's no back and forth. But then you actually go to try it, and the setup's super messy and technical. And if you want the best models, you're going to pay extra because it's not available on Claude subscription. So, in reality, it looks simple, but it's actually not. And I know a lot of you are in this exact same spot because I've seen your comments on my YouTube videos. Some of you are testing Hermes, trying OpenClaw, or even thinking about building your own. And I was there, too. And while I was going through it, I ended up actually just building my own version. One that runs on Claude subscription. So, it doesn't cost me a fortune because every single thing in this diagram, you can already do inside Claude code. And for a business owner, the claw code version is actually better because you can see exactly what's going on inside the blackbox. So in this video, I'm going to break down the five features that actually make a system like this and share what I learned along the way. So if you're thinking about using Hermes, OpenClaw, or even just building your own, you'll know exactly what to focus on to get started. So when I ran Hermes and OpenC Claw side by side with my own setup, I noticed that they all have different rappers, different UIs, different channels you can contact them from, but underneath it's actually just the same five features driving everything. So the first is persistent memory. So think about memory that actually learns about you as you work with it. Then you've got skills that create themselves first of all and then get better over time. The third is how you actually interact with it, which is way bigger than just a chat interface on your phone, by the way. Then we've got scheduled tasks that actually run themselves. So not being at the computer window and still getting things done. And then finally, this is the big one, business context. How to inject the right context at the right time to make all your results contextualized to your business and produce therefore better outputs. So get all of these five inside claw code and you don't need a separate framework like openclaw or Hermes. And you can even run it on Claude's most powerful models like Opus 4.7 released just days ago without paying for the API credits. So you can use it on your Pro and Mac subscription. So let me first start with the one that most people get wrong and that's persistent memory. It's probably the biggest selling point of Hermes and Open Claw. So unlike temporary chat rappers, they're supposed to maintain long-term searchable memory of past conversations and projects. And this is what gets us hooked initially because the idea that my agent will actually remember what we worked on yesterday last week and therefore contextualize and be better for the results going forward sounds amazing. And if you've worked with claw code for more than just a few sessions, you'll know just how important context management actually is for getting high quality outputs. But claw code actually already has all the ingredients for this. We just need to set them up properly. So I've distilled this into just four memory layers that you can use. The first is claude.mmd or agents.mmd if you want to actually use this with different models. So think of this just as your agents operating instructions. Who it is, how it behaves, what rules it follows and it's going to load into every single session. Most of you will have this layer already. Now layer two is brand context. So this is where your business context is actually going to live. Think your brand voice, how you speak, ICP, your positioning, all your client details will live in this brand context shared folder. And therefore, every skill inside the repository can pull from the same folder. So when Claude writes a LinkedIn post for you, when it's doing client research, when it's building out your landing page, it's going to pull from the exact same business brain. And as you imagine, it gets much better outputs that are hyperfocused on your business. Now, layer three builds on top of that. And this is what makes agents like openclaw and hermes and those frameworks feel so personal. So this is the agent context folder. So we have things like the sold.md and the user.md which describe how it should act and feel and the actions that you as a user using it commonly do. So it feels like it understands you. And finally layer four we have project memory. So each project you run actually keeps a history of exactly what's happened as well as a plan that you can refer to. So when you actually come back to a content repurposing project that you did 3 weeks later, Claude is going to know exactly what you built, what worked, what didn't work, and where we need to pick up on that. Now, from this four layer framework, here's the first key learning that I wanted to share with you. It doesn't matter how you set this up. You can put your project briefs anywhere. Use whatever planning frameworks you like to write the plans. So for example, we use GSD or the get done frameworks for more complex projects, for example. But the core ingredients are that actually you're just loading in the right context at the right time. So you're not bloating context and experiencing context rot where the outputs are getting worse the more context you feed in. So your claw.md shouldn't be 2,000 lines long. It shouldn't even be a thousand lines long. It should actually just reference the most important process steps that are going to get loaded in at the start of the conversation. So any additional context that needs to be pulled in at a specific point needs to be stored in a separate reference file. So now I keep my agents.mmd if you want to work across models or your claw.md succinct and to the point and then just point it to reference files. So see here where I've separated my brand context and tell it to load it in only when it needs it. That way claw can actually load and offload into separate agents and maintain highquality outputs because we're not bloating the context. And we use exactly the same approach with every single skill. short entry skill.mmd file detailed references which are only loaded and offloaded when needed. So the first feature then is a memory layer. This is just about organizing context in a way that actually suits your business and your needs. So you just need to structure it properly, segment your context, point it to reference files and not overload those context files. And by the way, there are a bunch of different memory and context storage solutions that you can choose from. So you've got Obsidian, you've got the open claw style setup which we're showing here. We've got Karpathy's LLM wiki and even people are building customuilt frameworks for memory management. So there's a whole host of ones with different benefits depending on your use cases. So if you do actually want a comparison of these different memory models and when you use which, then drop a comment below and I'll do a full comparison about which one works for which use cases to help you get this memory system set up for your business. But anyway, that's memory. So let's look at what actually uses that memory to get the work done, which is skills. So Hermes has two features that often get bundled together in all the demos. The first is a persistent learning loop. So think of skills that actually improve themselves over time. So an agent does a task, evaluates its performance, and then it's going to refine that skill over time. And the second is automatic skill creation. So you can generate a new skill and then apparently share them via agentskills.io. And this is genuinely some seriously important features knowing now what I know about how important skills are for actual output quality. So skills are basically importing expertise to improve our output quality by giving it a really refined process document for a specific task. So you might have LinkedIn post creation skills, you might have copywriting skills, you might have lead generation research skills, all of those will be ported into skills. But again, if we reflect on the Claude code ecosystem, you can actually just build in yourself to that system. And the benefit of doing that is you know exactly how it works too and you can refine and iterate on it over time. So if we tackle creating skills first, claude code has the skill creator skill which you might have seen before. It's built by Anthropic themselves and basically you give it a description of what skill you want or you point it to a GitHub repo with an existing skill or describe a process from scratch on how you do it. And it's going to build out the entire thing, the name, the description, and that determines the success rate of whether it's called or not. And then obviously the step-by-step process document of the actual skill.md file itself. And if we reflect back on how we manage context, what we want to do is keep a refined skill.md file less than 200 lines and then strip out everything that's unnecessary. So we've actually adapted the anthropic skill creator skill to do exactly that. Strip out the surplus information and keep that separate and only load it into context exactly when you need it. Now on top of creating skills, every skill you build should have a self-arning loop baked in. So you have a skill definition inside your skill.md file. You have its reference files for additional context and you can go one step further with a learnings.mmd file or just a rule segment actually inside your skill.md which are basically non-negotiable rules that each time you use that skill or each time Claude is going to use that skill it will get better at abiding by those specific rules that we've added in. So as part of the skill process as one of the steps in the skill.md you get it to ask you for feedback. So it effectively takes the feedback then that you give it applies any rules inside your learnings.mmd or inside that skill file and then always sticks to by those rules when you use that skill again and again. So it's effectively a self-learning loop where the skills get better over time. So inside claw code you can replace that functionality by actually just using the skill creator skill and then you make them get better by applying rules inside the learnings.mmd or just rules inside the skill document itself if it's asking you for feedback every time. So, so far we've got memory and we've got skills that create themselves and get smarter over time. The next big question is how do you actually interact with this system dayto-day? So, it's no secret that every agentic framework in 2026 so far is been competing on interfaces. So, open claw gave you telegram, discord, slack, WhatsApp. Hermes is similar and claw code has been bringing out features left, right and center to try and replicate this to give people access to message their agents from phone. So you can kick off a task while you're out, check the output whilst you're on the move, and that's all great, but here's the thing that nobody is actually talking about. The interface question, in my opinion, isn't just, "Can I chat from an agent from my phone?" The real question now that agents are so good is how do we manage multiple conversations and multiple goals at the same time. The models are now so good that it's pushing us into a different role. We're now jumping into a supervisor role when we need a better way to actually be able to manage multiple agents and multiple projects on the goto. And all of the frameworks I've seen give you one conversation at a time. So you're going to open Telegram, you chat to one agent, you get one output back, which is great for a single task, but what happens when you've got six business goals all running in parallel? What happens when you want to set up a zero employee company and you run multiple departments through different agents? Like flicking between those chat threads and trying to remember which one was which, which one was writing your newsletter, which one has filled its contact window is actually pretty difficult. So, let me show you how you can get claw code to handle this and how I did it myself. So, first for quick asks, you've got the claw code inbuilt channels feature. So, this is Anthropic's official feature that's going to work with Telegram, iMessage, and Discord out the box. So, you don't need to do anything to actually access your conversation at your phone already. So, exactly what Hermes promises, but shipped natively by Anthropic. Now, and here's where it gets really interesting. If you're running a real business on claw code, managing multiple conversations, then you need to actually abstract that and build a UI layer on top. So I did exactly that and I call it the command center. And the idea is really simple. So instead of managing terminals or chat threads, you just manage your business goals. So you drop in a business outcome. Claude is going to spin up an instance to handle it and it's going to show up on your canban style board where you've got full visibility of all your goals running in parallel. you're able to click into one and see the full conversation and you can have sub chats inside those conversations too. And you can even have the plan on the right hand side next to the chat window. So you could have four agents working on different features here and then the plan on the right hand side which is going to auto update as you run through the plan. So this is set out for larger more complex projects. You still have the granularity of the individual chat interface, but you're able to abstract yourself to a supervisor role because you can see how the chats are working against a plan and how that is all working against an individual business goal as well as then dig into the other business goals that you've currently got on the go. So, the workflow becomes then quick conversations while you're out and about. You can just fire it into Telegram via the channels feature. But if you've got a big goal that you want to manage over a day or a week or a complex project, then for example, I would drop it into my command center and come back to actually review the outputs here and manage multiple goals inside that. All of this, for example, you can build exactly for yourself. You can follow this structure that I'm showing you on screen. And it all runs locally and acts as just a UI wrapper on top of your terminal. So, it abides by Anthropic's Oorth usage policies, meaning you can actually use it with your Pro and Mac subscriptions. And if you want to get this up and running without having to build it yourself, it's just a oneline install as part of our paid community in the description below. And it includes all the underlying Aentic operating system logic that we're covering today, too. So full business context out of the box, 20 plus skills, scheduled workflows, the lot, all set up extremely quickly to handle tasks on behalf of you or your business. So check out the link in the description below if you're interested in that. So, how you interact with it matters way more than most people think. Most people are just jumping to actually interact with it on the phone, but phones are only good for quick asks and you can use claw code channels for that. But if you want to build out something managing multiple goals, then you need your own interaction layer. Now, the one caveat I'll put on this. Claude have just updated their own claw desktop to actually accommodate for managing multiple goals. However, it's still very technical, very focused on GitHub commits and not focused on that highle planning view with built-in planning frameworks like the way I've built it out for myself. So, it depends what you're looking for as to what is the right solution for you. And that's how we interact with claw code in a similar way to like open clause mission control for example. So, we've got memory, we've got skills, we've got the interaction layer. Now, let's look at the stuff that you should just be able to let run without you actually interfering with it. So Hermes lets you set up automated jobs on a schedule. So you can install a skill, create a recurring job, and then it's going to run automatically. And in claw code, you can do exactly the same with the new routines feature inside their desktop app. But right now, the feature is limited to built-in connectors. So it's quite difficult to interact with apps that aren't in their native built-in connectors, especially when you can actually build this out using claw code to leverage the built-in functionality on your Mac or Windows machine. So you don't need a virtual private server. You don't need extra infrastructure. Pro code can actually set up this logic for you in less than a few hours so that you can just control your scheduled jobs from a few files. When they're noted as active, we're going to run those scheduled jobs. And when they're not active, we're not going to run those scheduled jobs. Now, most people are creating scheduled jobs to just insert a simple prompt. But actually, the smartest people are actually using scheduled workflows to chain skills together inside a prompt. So, you can schedule a task that's effectively going to run multiple skills in sequence. You might have a weekly content digest that runs every Monday at 9:00 a.m. So, it's going to pull the previous week's YouTube videos, run an analysis across those, and then generate three LinkedIn posts using your voice profile, and then drop them into a review folder. So, you come in on Monday morning, you've got all of those already ready in the review folder. And they're contextualized and followed all of the skill process documents that produce high-quality outputs. So many different skills all chained together to produce one output that you come back and you can approve or supervise. And the biggest learning when I started building this out, my original aim was to build out fully autonomous scheduled workflows, run the whole thing, ship the output, post it to LinkedIn, whatever. But it was actually pretty bad because 20% of the time something wouldn't be quite right. So instead, I've actually built this framework now around doing 80% of the work automatically, the research, the narrowing of different topics. But what I've added in is always having a human checkpoint before anything goes live. So I'm never going to post content that's just AI generated stuff. I'm always going to have that human supervisor in the process until we can get to a level of quality where things can run autonomously and we're happy with them. So all of my content drafts, for example, land in a folder so that I can actually come in and supervise them and review them and approve the outputs. So it's basically giving you the speed of the automation without the risk of shipping something that's just pure AI slop, which we do not want to contribute. So you can effectively use scheduled jobs to chain multiple skills together and then add in a human checkpoint to actually approve or make sure the quality is high. Right? So that is four amazing features. Each one you can build inside claw code using what's already there in just a few days. But here's the fifth and honestly this is the one that made me stop looking at Hermes and OpenClaw because I did not see enough capacity for it to do this well. Now because Hermes and OpenClaw are built solely to be agent frameworks, they're very tool focused. So, it's all about installing a skill, running a job, getting an output, but they don't know anything really about your business. You can, of course, install ways to actually give it information about your business, but they don't out the box know your brand voice, know your ICP, they don't know your positioning, they don't know who your clients are, what your tone in your emails usually is. All of these things are critical for high quality outputs. And it's the equivalent of basically starting from zero when you run a new skill. And this is what shifted me away from systems like Hermes and Open Claw to build my own system because I realized that the real unlock isn't actually the agents. The agents and the models are getting better and better. It's the layer underneath the context that we discussed at the start. The brand context folder, the voice profile, the audience avatar, all of that preloaded pulling into the right skill at the right time is what actually generates high quality outputs. So I actually pulled together myself a set of skills that help me generate my voice profile and I make sure that when I build out my skills using the skill creator skill all of them reference the right context at the right time. So if I have a skill that builds out LinkedIn posts for example it will always reference my brand voice. It will understand the positioning because it understands who my clients are. And I used content as an example because it's relatable to a lot of different businesses. It doesn't mean you need to use these systems to actually generate your content. And the way that we've done this is basically moving everything, all of that context for my business into a single brand context folder that every skill is able to reference. So you update the information once and every skill gets that update when it runs. So business context is that compounding advantage that you cannot get right now. So build this, right? And this totally underpins all of the other pillars that we've talked about today. You need to inject the right context at the right time. And that starts with actually having a shared context folder that focuses on your brand and you. So when you bring this all together, this is exactly how it looks in a three-step process to compare to the one we showed at the start. We have your own agentic operating system where we have the business brain which underpins and powers cloud code by injecting the right context at the right time. We're able to then actually just write goals whether that's to create a scheduled job or to manage multiple business goals in one place. Claude is then going to do the work in the background to break it down into subtasks, choose the right skills, etc. And what that enables is your system to deliver you a highquality result that's contextualized by your business context completely replacing the need for a framework like Hermes or Open Claw and without all of the technical overhead and cost implications of moving off the pro and max plans from Claude. So that's the five features that actually matter and how to build each one of them inside Claude code yourself. And if you're building out your own version right now, which a lot of you in the comments have told me you are, here's my honest advice from three months of getting this wrong and rebuilding it. Start with this business brain. Don't start with the agents. Don't start with the multi- aent orchestration. I made this same mistake. Every feature I just walked through gets multiplied by having the solid context, the foundation layer underneath it. And none of them are going to work without that layer. And if you just want to skip the setup and grab the whole thing plugandplay today, then check out the link below in the description for the Aentic Academy. So, we've got the Aentic Os, the command center that you saw today with the dashboard and all 20 plus skills ready to go with a oneline install. And if you want to see exactly why I built out the command center in the first place, then check out the next video. Thanks for watching.

---

## Timestamped Segments

**[0:00]** So, take a look at this for a second.

**[0:01]** Install a skill, set a schedule for an

**[0:04]** automated job, and then get the result

**[0:06]** delivered to you on your phone. That's

**[0:08]** it. That is the pitch for Hermes and the

**[0:10]** pitch for OpenClaw pretty much, too. And

**[0:12]** honestly, when I first saw this, I was

**[0:13]** completely sold because in reality, this

**[0:15]** is exactly what every business owner

**[0:17]** wants. The work's going to get done in

**[0:18]** the background. You're going to get the

**[0:20]** good result. There's no babysitting.

**[0:21]** There's no back and forth. But then you

**[0:23]** actually go to try it, and the setup's

**[0:24]** super messy and technical. And if you

**[0:26]** want the best models, you're going to

**[0:28]** pay extra because it's not available on

**[0:29]** Claude subscription. So, in reality, it

**[0:31]** looks simple, but it's actually not. And

**[0:33]** I know a lot of you are in this exact

**[0:35]** same spot because I've seen your

**[0:37]** comments on my YouTube videos. Some of

**[0:39]** you are testing Hermes, trying OpenClaw,

**[0:41]** or even thinking about building your

**[0:42]** own. And I was there, too. And while I

**[0:44]** was going through it, I ended up

**[0:45]** actually just building my own version.

**[0:47]** One that runs on Claude subscription.

**[0:48]** So, it doesn't cost me a fortune because

**[0:50]** every single thing in this diagram, you

**[0:52]** can already do inside Claude code. And

**[0:54]** for a business owner, the claw code

**[0:56]** version is actually better because you

**[0:58]** can see exactly what's going on inside

**[1:00]** the blackbox. So in this video, I'm

**[1:02]** going to break down the five features

**[1:03]** that actually make a system like this

**[1:06]** and share what I learned along the way.

**[1:07]** So if you're thinking about using

**[1:08]** Hermes, OpenClaw, or even just building

**[1:10]** your own, you'll know exactly what to

**[1:12]** focus on to get started. So when I ran

**[1:14]** Hermes and OpenC Claw side by side with

**[1:16]** my own setup, I noticed that they all

**[1:18]** have different rappers, different UIs,

**[1:20]** different channels you can contact them

**[1:22]** from, but underneath it's actually just

**[1:24]** the same five features driving

**[1:25]** everything. So the first is persistent

**[1:27]** memory. So think about memory that

**[1:29]** actually learns about you as you work

**[1:31]** with it. Then you've got skills that

**[1:32]** create themselves first of all and then

**[1:35]** get better over time. The third is how

**[1:37]** you actually interact with it, which is

**[1:39]** way bigger than just a chat interface on

**[1:41]** your phone, by the way. Then we've got

**[1:42]** scheduled tasks that actually run

**[1:44]** themselves. So not being at the computer

**[1:46]** window and still getting things done.

**[1:47]** And then finally, this is the big one,

**[1:50]** business context. How to inject the

**[1:52]** right context at the right time to make

**[1:54]** all your results contextualized to your

**[1:56]** business and produce therefore better

**[1:58]** outputs. So get all of these five inside

**[2:01]** claw code and you don't need a separate

**[2:03]** framework like openclaw or Hermes. And

**[2:06]** you can even run it on Claude's most

**[2:07]** powerful models like Opus 4.7 released

**[2:10]** just days ago without paying for the API

**[2:12]** credits. So you can use it on your Pro

**[2:13]** and Mac subscription. So let me first

**[2:15]** start with the one that most people get

**[2:17]** wrong and that's persistent memory. It's

**[2:19]** probably the biggest selling point of

**[2:21]** Hermes and Open Claw. So unlike

**[2:23]** temporary chat rappers, they're supposed

**[2:25]** to maintain long-term searchable memory

**[2:27]** of past conversations and projects. And

**[2:30]** this is what gets us hooked initially

**[2:31]** because the idea that my agent will

**[2:33]** actually remember what we worked on

**[2:34]** yesterday last week and therefore

**[2:36]** contextualize and be better for the

**[2:38]** results going forward sounds amazing.

**[2:40]** And if you've worked with claw code for

**[2:42]** more than just a few sessions, you'll

**[2:43]** know just how important context

**[2:45]** management actually is for getting high

**[2:47]** quality outputs. But claw code actually

**[2:50]** already has all the ingredients for

**[2:51]** this. We just need to set them up

**[2:53]** properly. So I've distilled this into

**[2:55]** just four memory layers that you can

**[2:56]** use. The first is claude.mmd or

**[2:59]** agents.mmd if you want to actually use

**[3:01]** this with different models. So think of

**[3:03]** this just as your agents operating

**[3:04]** instructions. Who it is, how it behaves,

**[3:07]** what rules it follows and it's going to

**[3:09]** load into every single session. Most of

**[3:11]** you will have this layer already. Now

**[3:13]** layer two is brand context. So this is

**[3:16]** where your business context is actually

**[3:18]** going to live. Think your brand voice,

**[3:20]** how you speak, ICP, your positioning,

**[3:23]** all your client details will live in

**[3:24]** this brand context shared folder. And

**[3:27]** therefore, every skill inside the

**[3:28]** repository can pull from the same

**[3:30]** folder. So when Claude writes a LinkedIn

**[3:32]** post for you, when it's doing client

**[3:33]** research, when it's building out your

**[3:35]** landing page, it's going to pull from

**[3:36]** the exact same business brain. And as

**[3:38]** you imagine, it gets much better outputs

**[3:41]** that are hyperfocused on your business.

**[3:43]** Now, layer three builds on top of that.

**[3:45]** And this is what makes agents like

**[3:46]** openclaw and hermes and those frameworks

**[3:49]** feel so personal. So this is the agent

**[3:50]** context folder. So we have things like

**[3:52]** the sold.md and the user.md which

**[3:54]** describe how it should act and feel and

**[3:56]** the actions that you as a user using it

**[3:59]** commonly do. So it feels like it

**[4:00]** understands you. And finally layer four

**[4:02]** we have project memory. So each project

**[4:04]** you run actually keeps a history of

**[4:06]** exactly what's happened as well as a

**[4:08]** plan that you can refer to. So when you

**[4:10]** actually come back to a content

**[4:11]** repurposing project that you did 3 weeks

**[4:13]** later, Claude is going to know exactly

**[4:15]** what you built, what worked, what didn't

**[4:17]** work, and where we need to pick up on

**[4:19]** that. Now, from this four layer

**[4:20]** framework, here's the first key learning

**[4:22]** that I wanted to share with you. It

**[4:24]** doesn't matter how you set this up. You

**[4:26]** can put your project briefs anywhere.

**[4:28]** Use whatever planning frameworks you

**[4:30]** like to write the plans. So for example,

**[4:31]** we use GSD or the get done

**[4:33]** frameworks for more complex projects,

**[4:35]** for example. But the core ingredients

**[4:37]** are that actually you're just loading in

**[4:40]** the right context at the right time. So

**[4:42]** you're not bloating context and

**[4:44]** experiencing context rot where the

**[4:45]** outputs are getting worse the more

**[4:47]** context you feed in. So your claw.md

**[4:49]** shouldn't be 2,000 lines long. It

**[4:51]** shouldn't even be a thousand lines long.

**[4:52]** It should actually just reference the

**[4:54]** most important process steps that are

**[4:56]** going to get loaded in at the start of

**[4:58]** the conversation. So any additional

**[4:59]** context that needs to be pulled in at a

**[5:01]** specific point needs to be stored in a

**[5:03]** separate reference file. So now I keep

**[5:06]** my agents.mmd if you want to work across

**[5:08]** models or your claw.md succinct and to

**[5:11]** the point and then just point it to

**[5:13]** reference files. So see here where I've

**[5:15]** separated my brand context and tell it

**[5:16]** to load it in only when it needs it.

**[5:19]** That way claw can actually load and

**[5:20]** offload into separate agents and

**[5:23]** maintain highquality outputs because

**[5:24]** we're not bloating the context. And we

**[5:26]** use exactly the same approach with every

**[5:28]** single skill. short entry skill.mmd file

**[5:31]** detailed references which are only

**[5:33]** loaded and offloaded when needed. So the

**[5:35]** first feature then is a memory layer.

**[5:37]** This is just about organizing context in

**[5:39]** a way that actually suits your business

**[5:40]** and your needs. So you just need to

**[5:42]** structure it properly, segment your

**[5:44]** context, point it to reference files and

**[5:46]** not overload those context files. And by

**[5:48]** the way, there are a bunch of different

**[5:49]** memory and context storage solutions

**[5:51]** that you can choose from. So you've got

**[5:52]** Obsidian, you've got the open claw style

**[5:54]** setup which we're showing here. We've

**[5:56]** got Karpathy's LLM wiki and even people

**[5:58]** are building customuilt frameworks for

**[6:00]** memory management. So there's a whole

**[6:01]** host of ones with different benefits

**[6:03]** depending on your use cases. So if you

**[6:04]** do actually want a comparison of these

**[6:06]** different memory models and when you use

**[6:08]** which, then drop a comment below and

**[6:09]** I'll do a full comparison about which

**[6:11]** one works for which use cases to help

**[6:13]** you get this memory system set up for

**[6:15]** your business. But anyway, that's

**[6:16]** memory. So let's look at what actually

**[6:18]** uses that memory to get the work done,

**[6:20]** which is skills. So Hermes has two

**[6:22]** features that often get bundled together

**[6:24]** in all the demos. The first is a

**[6:26]** persistent learning loop. So think of

**[6:28]** skills that actually improve themselves

**[6:30]** over time. So an agent does a task,

**[6:32]** evaluates its performance, and then it's

**[6:33]** going to refine that skill over time.

**[6:35]** And the second is automatic skill

**[6:38]** creation. So you can generate a new

**[6:40]** skill and then apparently share them via

**[6:41]** agentskills.io. And this is genuinely

**[6:44]** some seriously important features

**[6:45]** knowing now what I know about how

**[6:47]** important skills are for actual output

**[6:50]** quality. So skills are basically

**[6:51]** importing expertise to improve our

**[6:54]** output quality by giving it a really

**[6:56]** refined process document for a specific

**[6:58]** task. So you might have LinkedIn post

**[7:00]** creation skills, you might have

**[7:01]** copywriting skills, you might have lead

**[7:03]** generation research skills, all of those

**[7:05]** will be ported into skills. But again,

**[7:07]** if we reflect on the Claude code

**[7:09]** ecosystem, you can actually just build

**[7:11]** in yourself to that system. And the

**[7:13]** benefit of doing that is you know

**[7:14]** exactly how it works too and you can

**[7:16]** refine and iterate on it over time. So

**[7:18]** if we tackle creating skills first,

**[7:20]** claude code has the skill creator skill

**[7:22]** which you might have seen before. It's

**[7:23]** built by Anthropic themselves and

**[7:25]** basically you give it a description of

**[7:26]** what skill you want or you point it to a

**[7:28]** GitHub repo with an existing skill or

**[7:30]** describe a process from scratch on how

**[7:32]** you do it. And it's going to build out

**[7:34]** the entire thing, the name, the

**[7:35]** description, and that determines the

**[7:37]** success rate of whether it's called or

**[7:38]** not. And then obviously the step-by-step

**[7:40]** process document of the actual skill.md

**[7:42]** file itself. And if we reflect back on

**[7:44]** how we manage context, what we want to

**[7:46]** do is keep a refined skill.md file less

**[7:49]** than 200 lines and then strip out

**[7:51]** everything that's unnecessary. So we've

**[7:52]** actually adapted the anthropic skill

**[7:54]** creator skill to do exactly that. Strip

**[7:56]** out the surplus information and keep

**[7:58]** that separate and only load it into

**[8:00]** context exactly when you need it. Now on

**[8:02]** top of creating skills, every skill you

**[8:04]** build should have a self-arning loop

**[8:06]** baked in. So you have a skill definition

**[8:08]** inside your skill.md file. You have its

**[8:11]** reference files for additional context

**[8:12]** and you can go one step further with a

**[8:15]** learnings.mmd file or just a rule

**[8:17]** segment actually inside your skill.md

**[8:19]** which are basically non-negotiable rules

**[8:21]** that each time you use that skill or

**[8:23]** each time Claude is going to use that

**[8:24]** skill it will get better at abiding by

**[8:26]** those specific rules that we've added

**[8:28]** in. So as part of the skill process as

**[8:30]** one of the steps in the skill.md you get

**[8:33]** it to ask you for feedback. So it

**[8:35]** effectively takes the feedback then that

**[8:37]** you give it applies any rules inside

**[8:39]** your learnings.mmd or inside that skill

**[8:41]** file and then always sticks to by those

**[8:43]** rules when you use that skill again and

**[8:44]** again. So it's effectively a

**[8:46]** self-learning loop where the skills get

**[8:47]** better over time. So inside claw code

**[8:49]** you can replace that functionality by

**[8:51]** actually just using the skill creator

**[8:52]** skill and then you make them get better

**[8:55]** by applying rules inside the

**[8:56]** learnings.mmd or just rules inside the

**[8:58]** skill document itself if it's asking you

**[9:01]** for feedback every time. So, so far

**[9:02]** we've got memory and we've got skills

**[9:04]** that create themselves and get smarter

**[9:06]** over time. The next big question is how

**[9:08]** do you actually interact with this

**[9:10]** system dayto-day? So, it's no secret

**[9:12]** that every agentic framework in 2026 so

**[9:15]** far is been competing on interfaces. So,

**[9:18]** open claw gave you telegram, discord,

**[9:20]** slack, WhatsApp. Hermes is similar and

**[9:22]** claw code has been bringing out features

**[9:24]** left, right and center to try and

**[9:26]** replicate this to give people access to

**[9:29]** message their agents from phone. So you

**[9:31]** can kick off a task while you're out,

**[9:33]** check the output whilst you're on the

**[9:35]** move, and that's all great, but here's

**[9:36]** the thing that nobody is actually

**[9:38]** talking about. The interface question,

**[9:39]** in my opinion, isn't just, "Can I chat

**[9:42]** from an agent from my phone?" The real

**[9:44]** question now that agents are so good is

**[9:45]** how do we manage multiple conversations

**[9:47]** and multiple goals at the same time. The

**[9:49]** models are now so good that it's pushing

**[9:51]** us into a different role. We're now

**[9:53]** jumping into a supervisor role when we

**[9:55]** need a better way to actually be able to

**[9:57]** manage multiple agents and multiple

**[9:59]** projects on the goto. And all of the

**[10:00]** frameworks I've seen give you one

**[10:02]** conversation at a time. So you're going

**[10:04]** to open Telegram, you chat to one agent,

**[10:06]** you get one output back, which is great

**[10:08]** for a single task, but what happens when

**[10:10]** you've got six business goals all

**[10:12]** running in parallel? What happens when

**[10:13]** you want to set up a zero employee

**[10:15]** company and you run multiple departments

**[10:17]** through different agents? Like flicking

**[10:19]** between those chat threads and trying to

**[10:21]** remember which one was which, which one

**[10:23]** was writing your newsletter, which one

**[10:25]** has filled its contact window is

**[10:26]** actually pretty difficult. So, let me

**[10:28]** show you how you can get claw code to

**[10:30]** handle this and how I did it myself. So,

**[10:32]** first for quick asks, you've got the

**[10:34]** claw code inbuilt channels feature. So,

**[10:36]** this is Anthropic's official feature

**[10:38]** that's going to work with Telegram,

**[10:39]** iMessage, and Discord out the box. So,

**[10:41]** you don't need to do anything to

**[10:42]** actually access your conversation at

**[10:44]** your phone already. So, exactly what

**[10:46]** Hermes promises, but shipped natively by

**[10:48]** Anthropic. Now, and here's where it gets

**[10:50]** really interesting. If you're running a

**[10:52]** real business on claw code, managing

**[10:53]** multiple conversations, then you need to

**[10:55]** actually abstract that and build a UI

**[10:58]** layer on top. So I did exactly that and

**[11:00]** I call it the command center. And the

**[11:01]** idea is really simple. So instead of

**[11:03]** managing terminals or chat threads, you

**[11:06]** just manage your business goals. So you

**[11:07]** drop in a business outcome. Claude is

**[11:09]** going to spin up an instance to handle

**[11:11]** it and it's going to show up on your

**[11:12]** canban style board where you've got full

**[11:14]** visibility of all your goals running in

**[11:15]** parallel. you're able to click into one

**[11:17]** and see the full conversation and you

**[11:19]** can have sub chats inside those

**[11:21]** conversations too. And you can even have

**[11:23]** the plan on the right hand side next to

**[11:26]** the chat window. So you could have four

**[11:27]** agents working on different features

**[11:29]** here and then the plan on the right hand

**[11:31]** side which is going to auto update as

**[11:33]** you run through the plan. So this is set

**[11:34]** out for larger more complex projects.

**[11:37]** You still have the granularity of the

**[11:39]** individual chat interface, but you're

**[11:40]** able to abstract yourself to a

**[11:42]** supervisor role because you can see how

**[11:44]** the chats are working against a plan and

**[11:46]** how that is all working against an

**[11:47]** individual business goal as well as then

**[11:49]** dig into the other business goals that

**[11:52]** you've currently got on the go. So, the

**[11:53]** workflow becomes then quick

**[11:55]** conversations while you're out and

**[11:56]** about. You can just fire it into

**[11:58]** Telegram via the channels feature. But

**[12:00]** if you've got a big goal that you want

**[12:01]** to manage over a day or a week or a

**[12:03]** complex project, then for example, I

**[12:05]** would drop it into my command center and

**[12:07]** come back to actually review the outputs

**[12:09]** here and manage multiple goals inside

**[12:11]** that. All of this, for example, you can

**[12:13]** build exactly for yourself. You can

**[12:14]** follow this structure that I'm showing

**[12:16]** you on screen. And it all runs locally

**[12:17]** and acts as just a UI wrapper on top of

**[12:20]** your terminal. So, it abides by

**[12:21]** Anthropic's Oorth usage policies,

**[12:23]** meaning you can actually use it with

**[12:25]** your Pro and Mac subscriptions. And if

**[12:26]** you want to get this up and running

**[12:28]** without having to build it yourself,

**[12:29]** it's just a oneline install as part of

**[12:31]** our paid community in the description

**[12:33]** below. And it includes all the

**[12:34]** underlying Aentic operating system logic

**[12:37]** that we're covering today, too. So full

**[12:39]** business context out of the box, 20 plus

**[12:42]** skills, scheduled workflows, the lot,

**[12:44]** all set up extremely quickly to handle

**[12:47]** tasks on behalf of you or your business.

**[12:49]** So check out the link in the description

**[12:50]** below if you're interested in that. So,

**[12:52]** how you interact with it matters way

**[12:55]** more than most people think. Most people

**[12:56]** are just jumping to actually interact

**[12:58]** with it on the phone, but phones are

**[12:59]** only good for quick asks and you can use

**[13:02]** claw code channels for that. But if you

**[13:03]** want to build out something managing

**[13:05]** multiple goals, then you need your own

**[13:06]** interaction layer. Now, the one caveat

**[13:08]** I'll put on this. Claude have just

**[13:10]** updated their own claw desktop to

**[13:12]** actually accommodate for managing

**[13:13]** multiple goals. However, it's still very

**[13:15]** technical, very focused on GitHub

**[13:17]** commits and not focused on that highle

**[13:19]** planning view with built-in planning

**[13:21]** frameworks like the way I've built it

**[13:23]** out for myself. So, it depends what

**[13:24]** you're looking for as to what is the

**[13:26]** right solution for you. And that's how

**[13:27]** we interact with claw code in a similar

**[13:30]** way to like open clause mission control

**[13:32]** for example. So, we've got memory, we've

**[13:34]** got skills, we've got the interaction

**[13:35]** layer. Now, let's look at the stuff that

**[13:37]** you should just be able to let run

**[13:38]** without you actually interfering with

**[13:40]** it. So Hermes lets you set up automated

**[13:42]** jobs on a schedule. So you can install a

**[13:44]** skill, create a recurring job, and then

**[13:46]** it's going to run automatically. And in

**[13:48]** claw code, you can do exactly the same

**[13:49]** with the new routines feature inside

**[13:52]** their desktop app. But right now, the

**[13:54]** feature is limited to built-in

**[13:55]** connectors. So it's quite difficult to

**[13:57]** interact with apps that aren't in their

**[13:59]** native built-in connectors, especially

**[14:00]** when you can actually build this out

**[14:02]** using claw code to leverage the built-in

**[14:04]** functionality on your Mac or Windows

**[14:06]** machine. So you don't need a virtual

**[14:07]** private server. You don't need extra

**[14:09]** infrastructure. Pro code can actually

**[14:10]** set up this logic for you in less than a

**[14:13]** few hours so that you can just control

**[14:15]** your scheduled jobs from a few files.

**[14:17]** When they're noted as active, we're

**[14:19]** going to run those scheduled jobs. And

**[14:20]** when they're not active, we're not going

**[14:22]** to run those scheduled jobs. Now, most

**[14:23]** people are creating scheduled jobs to

**[14:25]** just insert a simple prompt. But

**[14:27]** actually, the smartest people are

**[14:28]** actually using scheduled workflows to

**[14:30]** chain skills together inside a prompt.

**[14:33]** So, you can schedule a task that's

**[14:35]** effectively going to run multiple skills

**[14:37]** in sequence. You might have a weekly

**[14:39]** content digest that runs every Monday at

**[14:42]** 9:00 a.m. So, it's going to pull the

**[14:43]** previous week's YouTube videos, run an

**[14:46]** analysis across those, and then generate

**[14:48]** three LinkedIn posts using your voice

**[14:50]** profile, and then drop them into a

**[14:52]** review folder. So, you come in on Monday

**[14:54]** morning, you've got all of those already

**[14:56]** ready in the review folder. And they're

**[14:57]** contextualized and followed all of the

**[14:59]** skill process documents that produce

**[15:01]** high-quality outputs. So many different

**[15:03]** skills all chained together to produce

**[15:05]** one output that you come back and you

**[15:07]** can approve or supervise. And the

**[15:08]** biggest learning when I started building

**[15:10]** this out, my original aim was to build

**[15:11]** out fully autonomous scheduled

**[15:14]** workflows, run the whole thing, ship the

**[15:16]** output, post it to LinkedIn, whatever.

**[15:18]** But it was actually pretty bad because

**[15:20]** 20% of the time something wouldn't be

**[15:22]** quite right. So instead, I've actually

**[15:24]** built this framework now around doing

**[15:26]** 80% of the work automatically, the

**[15:28]** research, the narrowing of different

**[15:30]** topics. But what I've added in is always

**[15:33]** having a human checkpoint before

**[15:34]** anything goes live. So I'm never going

**[15:36]** to post content that's just AI generated

**[15:38]** stuff. I'm always going to have that

**[15:40]** human supervisor in the process until we

**[15:42]** can get to a level of quality where

**[15:44]** things can run autonomously and we're

**[15:46]** happy with them. So all of my content

**[15:47]** drafts, for example, land in a folder so

**[15:49]** that I can actually come in and

**[15:50]** supervise them and review them and

**[15:52]** approve the outputs. So it's basically

**[15:54]** giving you the speed of the automation

**[15:55]** without the risk of shipping something

**[15:57]** that's just pure AI slop, which we do

**[15:59]** not want to contribute. So you can

**[16:00]** effectively use scheduled jobs to chain

**[16:03]** multiple skills together and then add in

**[16:05]** a human checkpoint to actually approve

**[16:07]** or make sure the quality is high. Right?

**[16:09]** So that is four amazing features. Each

**[16:11]** one you can build inside claw code using

**[16:13]** what's already there in just a few days.

**[16:15]** But here's the fifth and honestly this

**[16:18]** is the one that made me stop looking at

**[16:19]** Hermes and OpenClaw because I did not

**[16:21]** see enough capacity for it to do this

**[16:23]** well. Now because Hermes and OpenClaw

**[16:25]** are built solely to be agent frameworks,

**[16:28]** they're very tool focused. So, it's all

**[16:30]** about installing a skill, running a job,

**[16:32]** getting an output, but they don't know

**[16:33]** anything really about your business. You

**[16:36]** can, of course, install ways to actually

**[16:38]** give it information about your business,

**[16:39]** but they don't out the box know your

**[16:41]** brand voice, know your ICP, they don't

**[16:43]** know your positioning, they don't know

**[16:45]** who your clients are, what your tone in

**[16:47]** your emails usually is. All of these

**[16:49]** things are critical for high quality

**[16:50]** outputs. And it's the equivalent of

**[16:52]** basically starting from zero when you

**[16:53]** run a new skill. And this is what

**[16:55]** shifted me away from systems like Hermes

**[16:57]** and Open Claw to build my own system

**[16:59]** because I realized that the real unlock

**[17:01]** isn't actually the agents. The agents

**[17:03]** and the models are getting better and

**[17:04]** better. It's the layer underneath the

**[17:06]** context that we discussed at the start.

**[17:08]** The brand context folder, the voice

**[17:09]** profile, the audience avatar, all of

**[17:12]** that preloaded pulling into the right

**[17:14]** skill at the right time is what actually

**[17:16]** generates high quality outputs. So I

**[17:18]** actually pulled together myself a set of

**[17:20]** skills that help me generate my voice

**[17:22]** profile and I make sure that when I

**[17:24]** build out my skills using the skill

**[17:26]** creator skill all of them reference the

**[17:28]** right context at the right time. So if I

**[17:29]** have a skill that builds out LinkedIn

**[17:31]** posts for example it will always

**[17:33]** reference my brand voice. It will

**[17:35]** understand the positioning because it

**[17:36]** understands who my clients are. And I

**[17:38]** used content as an example because it's

**[17:40]** relatable to a lot of different

**[17:42]** businesses. It doesn't mean you need to

**[17:43]** use these systems to actually generate

**[17:45]** your content. And the way that we've

**[17:46]** done this is basically moving

**[17:48]** everything, all of that context for my

**[17:50]** business into a single brand context

**[17:52]** folder that every skill is able to

**[17:54]** reference. So you update the information

**[17:55]** once and every skill gets that update

**[17:57]** when it runs. So business context is

**[17:59]** that compounding advantage that you

**[18:01]** cannot get right now. So build this,

**[18:03]** right? And this totally underpins all of

**[18:05]** the other pillars that we've talked

**[18:06]** about today. You need to inject the

**[18:08]** right context at the right time. And

**[18:10]** that starts with actually having a

**[18:12]** shared context folder that focuses on

**[18:14]** your brand and you. So when you bring

**[18:16]** this all together, this is exactly how

**[18:18]** it looks in a three-step process to

**[18:20]** compare to the one we showed at the

**[18:21]** start. We have your own agentic

**[18:22]** operating system where we have the

**[18:24]** business brain which underpins and

**[18:25]** powers cloud code by injecting the right

**[18:27]** context at the right time. We're able to

**[18:29]** then actually just write goals whether

**[18:31]** that's to create a scheduled job or to

**[18:33]** manage multiple business goals in one

**[18:35]** place. Claude is then going to do the

**[18:36]** work in the background to break it down

**[18:37]** into subtasks, choose the right skills,

**[18:39]** etc. And what that enables is your

**[18:41]** system to deliver you a highquality

**[18:44]** result that's contextualized by your

**[18:46]** business context completely replacing

**[18:47]** the need for a framework like Hermes or

**[18:49]** Open Claw and without all of the

**[18:51]** technical overhead and cost implications

**[18:53]** of moving off the pro and max plans from

**[18:56]** Claude. So that's the five features that

**[18:57]** actually matter and how to build each

**[18:59]** one of them inside Claude code yourself.

**[19:01]** And if you're building out your own

**[19:02]** version right now, which a lot of you in

**[19:04]** the comments have told me you are,

**[19:06]** here's my honest advice from three

**[19:08]** months of getting this wrong and

**[19:09]** rebuilding it. Start with this business

**[19:11]** brain. Don't start with the agents.

**[19:13]** Don't start with the multi- aent

**[19:14]** orchestration. I made this same mistake.

**[19:17]** Every feature I just walked through gets

**[19:19]** multiplied by having the solid context,

**[19:21]** the foundation layer underneath it. And

**[19:23]** none of them are going to work without

**[19:25]** that layer. And if you just want to skip

**[19:26]** the setup and grab the whole thing

**[19:28]** plugandplay today, then check out the

**[19:30]** link below in the description for the

**[19:31]** Aentic Academy. So, we've got the Aentic

**[19:33]** Os, the command center that you saw

**[19:35]** today with the dashboard and all 20 plus

**[19:37]** skills ready to go with a oneline

**[19:40]** install. And if you want to see exactly

**[19:41]** why I built out the command center in

**[19:43]** the first place, then check out the next

**[19:44]** video. Thanks for watching.

**[0:00]** So, take a look at this for a second.

**[0:01]** Install a skill, set a schedule for an

**[0:04]** automated job, and then get the result

**[0:06]** delivered to you on your phone. That's

**[0:08]** it. That is the pitch for Hermes and the

**[0:10]** pitch for OpenClaw pretty much, too. And

**[0:12]** honestly, when I first saw this, I was

**[0:13]** completely sold because in reality, this

**[0:15]** is exactly what every business owner

**[0:17]** wants. The work's going to get done in

**[0:18]** the background. You're going to get the

**[0:20]** good result. There's no babysitting.

**[0:21]** There's no back and forth. But then you

**[0:23]** actually go to try it, and the setup's

**[0:24]** super messy and technical. And if you

**[0:26]** want the best models, you're going to

**[0:28]** pay extra because it's not available on

**[0:29]** Claude subscription. So, in reality, it

**[0:31]** looks simple, but it's actually not. And

**[0:33]** I know a lot of you are in this exact

**[0:35]** same spot because I've seen your

**[0:37]** comments on my YouTube videos. Some of

**[0:39]** you are testing Hermes, trying OpenClaw,

**[0:41]** or even thinking about building your

**[0:42]** own. And I was there, too. And while I

**[0:44]** was going through it, I ended up

**[0:45]** actually just building my own version.

**[0:47]** One that runs on Claude subscription.

**[0:48]** So, it doesn't cost me a fortune because

**[0:50]** every single thing in this diagram, you

**[0:52]** can already do inside Claude code. And

**[0:54]** for a business owner, the claw code

**[0:56]** version is actually better because you

**[0:58]** can see exactly what's going on inside

**[1:00]** the blackbox. So in this video, I'm

**[1:02]** going to break down the five features

**[1:03]** that actually make a system like this

**[1:06]** and share what I learned along the way.

**[1:07]** So if you're thinking about using

**[1:08]** Hermes, OpenClaw, or even just building

**[1:10]** your own, you'll know exactly what to

**[1:12]** focus on to get started. So when I ran

**[1:14]** Hermes and OpenC Claw side by side with

**[1:16]** my own setup, I noticed that they all

**[1:18]** have different rappers, different UIs,

**[1:20]** different channels you can contact them

**[1:22]** from, but underneath it's actually just

**[1:24]** the same five features driving

**[1:25]** everything. So the first is persistent

**[1:27]** memory. So think about memory that

**[1:29]** actually learns about you as you work

**[1:31]** with it. Then you've got skills that

**[1:32]** create themselves first of all and then

**[1:35]** get better over time. The third is how

**[1:37]** you actually interact with it, which is

**[1:39]** way bigger than just a chat interface on

**[1:41]** your phone, by the way. Then we've got

**[1:42]** scheduled tasks that actually run

**[1:44]** themselves. So not being at the computer

**[1:46]** window and still getting things done.

**[1:47]** And then finally, this is the big one,

**[1:50]** business context. How to inject the

**[1:52]** right context at the right time to make

**[1:54]** all your results contextualized to your

**[1:56]** business and produce therefore better

**[1:58]** outputs. So get all of these five inside

**[2:01]** claw code and you don't need a separate

**[2:03]** framework like openclaw or Hermes. And

**[2:06]** you can even run it on Claude's most

**[2:07]** powerful models like Opus 4.7 released

**[2:10]** just days ago without paying for the API

**[2:12]** credits. So you can use it on your Pro

**[2:13]** and Mac subscription. So let me first

**[2:15]** start with the one that most people get

**[2:17]** wrong and that's persistent memory. It's

**[2:19]** probably the biggest selling point of

**[2:21]** Hermes and Open Claw. So unlike

**[2:23]** temporary chat rappers, they're supposed

**[2:25]** to maintain long-term searchable memory

**[2:27]** of past conversations and projects. And

**[2:30]** this is what gets us hooked initially

**[2:31]** because the idea that my agent will

**[2:33]** actually remember what we worked on

**[2:34]** yesterday last week and therefore

**[2:36]** contextualize and be better for the

**[2:38]** results going forward sounds amazing.

**[2:40]** And if you've worked with claw code for

**[2:42]** more than just a few sessions, you'll

**[2:43]** know just how important context

**[2:45]** management actually is for getting high

**[2:47]** quality outputs. But claw code actually

**[2:50]** already has all the ingredients for

**[2:51]** this. We just need to set them up

**[2:53]** properly. So I've distilled this into

**[2:55]** just four memory layers that you can

**[2:56]** use. The first is claude.mmd or

**[2:59]** agents.mmd if you want to actually use

**[3:01]** this with different models. So think of

**[3:03]** this just as your agents operating

**[3:04]** instructions. Who it is, how it behaves,

**[3:07]** what rules it follows and it's going to

**[3:09]** load into every single session. Most of

**[3:11]** you will have this layer already. Now

**[3:13]** layer two is brand context. So this is

**[3:16]** where your business context is actually

**[3:18]** going to live. Think your brand voice,

**[3:20]** how you speak, ICP, your positioning,

**[3:23]** all your client details will live in

**[3:24]** this brand context shared folder. And

**[3:27]** therefore, every skill inside the

**[3:28]** repository can pull from the same

**[3:30]** folder. So when Claude writes a LinkedIn

**[3:32]** post for you, when it's doing client

**[3:33]** research, when it's building out your

**[3:35]** landing page, it's going to pull from

**[3:36]** the exact same business brain. And as

**[3:38]** you imagine, it gets much better outputs

**[3:41]** that are hyperfocused on your business.

**[3:43]** Now, layer three builds on top of that.

**[3:45]** And this is what makes agents like

**[3:46]** openclaw and hermes and those frameworks

**[3:49]** feel so personal. So this is the agent

**[3:50]** context folder. So we have things like

**[3:52]** the sold.md and the user.md which

**[3:54]** describe how it should act and feel and

**[3:56]** the actions that you as a user using it

**[3:59]** commonly do. So it feels like it

**[4:00]** understands you. And finally layer four

**[4:02]** we have project memory. So each project

**[4:04]** you run actually keeps a history of

**[4:06]** exactly what's happened as well as a

**[4:08]** plan that you can refer to. So when you

**[4:10]** actually come back to a content

**[4:11]** repurposing project that you did 3 weeks

**[4:13]** later, Claude is going to know exactly

**[4:15]** what you built, what worked, what didn't

**[4:17]** work, and where we need to pick up on

**[4:19]** that. Now, from this four layer

**[4:20]** framework, here's the first key learning

**[4:22]** that I wanted to share with you. It

**[4:24]** doesn't matter how you set this up. You

**[4:26]** can put your project briefs anywhere.

**[4:28]** Use whatever planning frameworks you

**[4:30]** like to write the plans. So for example,

**[4:31]** we use GSD or the get done

**[4:33]** frameworks for more complex projects,

**[4:35]** for example. But the core ingredients

**[4:37]** are that actually you're just loading in

**[4:40]** the right context at the right time. So

**[4:42]** you're not bloating context and

**[4:44]** experiencing context rot where the

**[4:45]** outputs are getting worse the more

**[4:47]** context you feed in. So your claw.md

**[4:49]** shouldn't be 2,000 lines long. It

**[4:51]** shouldn't even be a thousand lines long.

**[4:52]** It should actually just reference the

**[4:54]** most important process steps that are

**[4:56]** going to get loaded in at the start of

**[4:58]** the conversation. So any additional

**[4:59]** context that needs to be pulled in at a

**[5:01]** specific point needs to be stored in a

**[5:03]** separate reference file. So now I keep

**[5:06]** my agents.mmd if you want to work across

**[5:08]** models or your claw.md succinct and to

**[5:11]** the point and then just point it to

**[5:13]** reference files. So see here where I've

**[5:15]** separated my brand context and tell it

**[5:16]** to load it in only when it needs it.

**[5:19]** That way claw can actually load and

**[5:20]** offload into separate agents and

**[5:23]** maintain highquality outputs because

**[5:24]** we're not bloating the context. And we

**[5:26]** use exactly the same approach with every

**[5:28]** single skill. short entry skill.mmd file

**[5:31]** detailed references which are only

**[5:33]** loaded and offloaded when needed. So the

**[5:35]** first feature then is a memory layer.

**[5:37]** This is just about organizing context in

**[5:39]** a way that actually suits your business

**[5:40]** and your needs. So you just need to

**[5:42]** structure it properly, segment your

**[5:44]** context, point it to reference files and

**[5:46]** not overload those context files. And by

**[5:48]** the way, there are a bunch of different

**[5:49]** memory and context storage solutions

**[5:51]** that you can choose from. So you've got

**[5:52]** Obsidian, you've got the open claw style

**[5:54]** setup which we're showing here. We've

**[5:56]** got Karpathy's LLM wiki and even people

**[5:58]** are building customuilt frameworks for

**[6:00]** memory management. So there's a whole

**[6:01]** host of ones with different benefits

**[6:03]** depending on your use cases. So if you

**[6:04]** do actually want a comparison of these

**[6:06]** different memory models and when you use

**[6:08]** which, then drop a comment below and

**[6:09]** I'll do a full comparison about which

**[6:11]** one works for which use cases to help

**[6:13]** you get this memory system set up for

**[6:15]** your business. But anyway, that's

**[6:16]** memory. So let's look at what actually

**[6:18]** uses that memory to get the work done,

**[6:20]** which is skills. So Hermes has two

**[6:22]** features that often get bundled together

**[6:24]** in all the demos. The first is a

**[6:26]** persistent learning loop. So think of

**[6:28]** skills that actually improve themselves

**[6:30]** over time. So an agent does a task,

**[6:32]** evaluates its performance, and then it's

**[6:33]** going to refine that skill over time.

**[6:35]** And the second is automatic skill

**[6:38]** creation. So you can generate a new

**[6:40]** skill and then apparently share them via

**[6:41]** agentskills.io. And this is genuinely

**[6:44]** some seriously important features

**[6:45]** knowing now what I know about how

**[6:47]** important skills are for actual output

**[6:50]** quality. So skills are basically

**[6:51]** importing expertise to improve our

**[6:54]** output quality by giving it a really

**[6:56]** refined process document for a specific

**[6:58]** task. So you might have LinkedIn post

**[7:00]** creation skills, you might have

**[7:01]** copywriting skills, you might have lead

**[7:03]** generation research skills, all of those

**[7:05]** will be ported into skills. But again,

**[7:07]** if we reflect on the Claude code

**[7:09]** ecosystem, you can actually just build

**[7:11]** in yourself to that system. And the

**[7:13]** benefit of doing that is you know

**[7:14]** exactly how it works too and you can

**[7:16]** refine and iterate on it over time. So

**[7:18]** if we tackle creating skills first,

**[7:20]** claude code has the skill creator skill

**[7:22]** which you might have seen before. It's

**[7:23]** built by Anthropic themselves and

**[7:25]** basically you give it a description of

**[7:26]** what skill you want or you point it to a

**[7:28]** GitHub repo with an existing skill or

**[7:30]** describe a process from scratch on how

**[7:32]** you do it. And it's going to build out

**[7:34]** the entire thing, the name, the

**[7:35]** description, and that determines the

**[7:37]** success rate of whether it's called or

**[7:38]** not. And then obviously the step-by-step

**[7:40]** process document of the actual skill.md

**[7:42]** file itself. And if we reflect back on

**[7:44]** how we manage context, what we want to

**[7:46]** do is keep a refined skill.md file less

**[7:49]** than 200 lines and then strip out

**[7:51]** everything that's unnecessary. So we've

**[7:52]** actually adapted the anthropic skill

**[7:54]** creator skill to do exactly that. Strip

**[7:56]** out the surplus information and keep

**[7:58]** that separate and only load it into

**[8:00]** context exactly when you need it. Now on

**[8:02]** top of creating skills, every skill you

**[8:04]** build should have a self-arning loop

**[8:06]** baked in. So you have a skill definition

**[8:08]** inside your skill.md file. You have its

**[8:11]** reference files for additional context

**[8:12]** and you can go one step further with a

**[8:15]** learnings.mmd file or just a rule

**[8:17]** segment actually inside your skill.md

**[8:19]** which are basically non-negotiable rules

**[8:21]** that each time you use that skill or

**[8:23]** each time Claude is going to use that

**[8:24]** skill it will get better at abiding by

**[8:26]** those specific rules that we've added

**[8:28]** in. So as part of the skill process as

**[8:30]** one of the steps in the skill.md you get

**[8:33]** it to ask you for feedback. So it

**[8:35]** effectively takes the feedback then that

**[8:37]** you give it applies any rules inside

**[8:39]** your learnings.mmd or inside that skill

**[8:41]** file and then always sticks to by those

**[8:43]** rules when you use that skill again and

**[8:44]** again. So it's effectively a

**[8:46]** self-learning loop where the skills get

**[8:47]** better over time. So inside claw code

**[8:49]** you can replace that functionality by

**[8:51]** actually just using the skill creator

**[8:52]** skill and then you make them get better

**[8:55]** by applying rules inside the

**[8:56]** learnings.mmd or just rules inside the

**[8:58]** skill document itself if it's asking you

**[9:01]** for feedback every time. So, so far

**[9:02]** we've got memory and we've got skills

**[9:04]** that create themselves and get smarter

**[9:06]** over time. The next big question is how

**[9:08]** do you actually interact with this

**[9:10]** system dayto-day? So, it's no secret

**[9:12]** that every agentic framework in 2026 so

**[9:15]** far is been competing on interfaces. So,

**[9:18]** open claw gave you telegram, discord,

**[9:20]** slack, WhatsApp. Hermes is similar and

**[9:22]** claw code has been bringing out features

**[9:24]** left, right and center to try and

**[9:26]** replicate this to give people access to

**[9:29]** message their agents from phone. So you

**[9:31]** can kick off a task while you're out,

**[9:33]** check the output whilst you're on the

**[9:35]** move, and that's all great, but here's

**[9:36]** the thing that nobody is actually

**[9:38]** talking about. The interface question,

**[9:39]** in my opinion, isn't just, "Can I chat

**[9:42]** from an agent from my phone?" The real

**[9:44]** question now that agents are so good is

**[9:45]** how do we manage multiple conversations

**[9:47]** and multiple goals at the same time. The

**[9:49]** models are now so good that it's pushing

**[9:51]** us into a different role. We're now

**[9:53]** jumping into a supervisor role when we

**[9:55]** need a better way to actually be able to

**[9:57]** manage multiple agents and multiple

**[9:59]** projects on the goto. And all of the

**[10:00]** frameworks I've seen give you one

**[10:02]** conversation at a time. So you're going

**[10:04]** to open Telegram, you chat to one agent,

**[10:06]** you get one output back, which is great

**[10:08]** for a single task, but what happens when

**[10:10]** you've got six business goals all

**[10:12]** running in parallel? What happens when

**[10:13]** you want to set up a zero employee

**[10:15]** company and you run multiple departments

**[10:17]** through different agents? Like flicking

**[10:19]** between those chat threads and trying to

**[10:21]** remember which one was which, which one

**[10:23]** was writing your newsletter, which one

**[10:25]** has filled its contact window is

**[10:26]** actually pretty difficult. So, let me

**[10:28]** show you how you can get claw code to

**[10:30]** handle this and how I did it myself. So,

**[10:32]** first for quick asks, you've got the

**[10:34]** claw code inbuilt channels feature. So,

**[10:36]** this is Anthropic's official feature

**[10:38]** that's going to work with Telegram,

**[10:39]** iMessage, and Discord out the box. So,

**[10:41]** you don't need to do anything to

**[10:42]** actually access your conversation at

**[10:44]** your phone already. So, exactly what

**[10:46]** Hermes promises, but shipped natively by

**[10:48]** Anthropic. Now, and here's where it gets

**[10:50]** really interesting. If you're running a

**[10:52]** real business on claw code, managing

**[10:53]** multiple conversations, then you need to

**[10:55]** actually abstract that and build a UI

**[10:58]** layer on top. So I did exactly that and

**[11:00]** I call it the command center. And the

**[11:01]** idea is really simple. So instead of

**[11:03]** managing terminals or chat threads, you

**[11:06]** just manage your business goals. So you

**[11:07]** drop in a business outcome. Claude is

**[11:09]** going to spin up an instance to handle

**[11:11]** it and it's going to show up on your

**[11:12]** canban style board where you've got full

**[11:14]** visibility of all your goals running in

**[11:15]** parallel. you're able to click into one

**[11:17]** and see the full conversation and you

**[11:19]** can have sub chats inside those

**[11:21]** conversations too. And you can even have

**[11:23]** the plan on the right hand side next to

**[11:26]** the chat window. So you could have four

**[11:27]** agents working on different features

**[11:29]** here and then the plan on the right hand

**[11:31]** side which is going to auto update as

**[11:33]** you run through the plan. So this is set

**[11:34]** out for larger more complex projects.

**[11:37]** You still have the granularity of the

**[11:39]** individual chat interface, but you're

**[11:40]** able to abstract yourself to a

**[11:42]** supervisor role because you can see how

**[11:44]** the chats are working against a plan and

**[11:46]** how that is all working against an

**[11:47]** individual business goal as well as then

**[11:49]** dig into the other business goals that

**[11:52]** you've currently got on the go. So, the

**[11:53]** workflow becomes then quick

**[11:55]** conversations while you're out and

**[11:56]** about. You can just fire it into

**[11:58]** Telegram via the channels feature. But

**[12:00]** if you've got a big goal that you want

**[12:01]** to manage over a day or a week or a

**[12:03]** complex project, then for example, I

**[12:05]** would drop it into my command center and

**[12:07]** come back to actually review the outputs

**[12:09]** here and manage multiple goals inside

**[12:11]** that. All of this, for example, you can

**[12:13]** build exactly for yourself. You can

**[12:14]** follow this structure that I'm showing

**[12:16]** you on screen. And it all runs locally

**[12:17]** and acts as just a UI wrapper on top of

**[12:20]** your terminal. So, it abides by

**[12:21]** Anthropic's Oorth usage policies,

**[12:23]** meaning you can actually use it with

**[12:25]** your Pro and Mac subscriptions. And if

**[12:26]** you want to get this up and running

**[12:28]** without having to build it yourself,

**[12:29]** it's just a oneline install as part of

**[12:31]** our paid community in the description

**[12:33]** below. And it includes all the

**[12:34]** underlying Aentic operating system logic

**[12:37]** that we're covering today, too. So full

**[12:39]** business context out of the box, 20 plus

**[12:42]** skills, scheduled workflows, the lot,

**[12:44]** all set up extremely quickly to handle

**[12:47]** tasks on behalf of you or your business.

**[12:49]** So check out the link in the description

**[12:50]** below if you're interested in that. So,

**[12:52]** how you interact with it matters way

**[12:55]** more than most people think. Most people

**[12:56]** are just jumping to actually interact

**[12:58]** with it on the phone, but phones are

**[12:59]** only good for quick asks and you can use

**[13:02]** claw code channels for that. But if you

**[13:03]** want to build out something managing

**[13:05]** multiple goals, then you need your own

**[13:06]** interaction layer. Now, the one caveat

**[13:08]** I'll put on this. Claude have just

**[13:10]** updated their own claw desktop to

**[13:12]** actually accommodate for managing

**[13:13]** multiple goals. However, it's still very

**[13:15]** technical, very focused on GitHub

**[13:17]** commits and not focused on that highle

**[13:19]** planning view with built-in planning

**[13:21]** frameworks like the way I've built it

**[13:23]** out for myself. So, it depends what

**[13:24]** you're looking for as to what is the

**[13:26]** right solution for you. And that's how

**[13:27]** we interact with claw code in a similar

**[13:30]** way to like open clause mission control

**[13:32]** for example. So, we've got memory, we've

**[13:34]** got skills, we've got the interaction

**[13:35]** layer. Now, let's look at the stuff that

**[13:37]** you should just be able to let run

**[13:38]** without you actually interfering with

**[13:40]** it. So Hermes lets you set up automated

**[13:42]** jobs on a schedule. So you can install a

**[13:44]** skill, create a recurring job, and then

**[13:46]** it's going to run automatically. And in

**[13:48]** claw code, you can do exactly the same

**[13:49]** with the new routines feature inside

**[13:52]** their desktop app. But right now, the

**[13:54]** feature is limited to built-in

**[13:55]** connectors. So it's quite difficult to

**[13:57]** interact with apps that aren't in their

**[13:59]** native built-in connectors, especially

**[14:00]** when you can actually build this out

**[14:02]** using claw code to leverage the built-in

**[14:04]** functionality on your Mac or Windows

**[14:06]** machine. So you don't need a virtual

**[14:07]** private server. You don't need extra

**[14:09]** infrastructure. Pro code can actually

**[14:10]** set up this logic for you in less than a

**[14:13]** few hours so that you can just control

**[14:15]** your scheduled jobs from a few files.

**[14:17]** When they're noted as active, we're

**[14:19]** going to run those scheduled jobs. And

**[14:20]** when they're not active, we're not going

**[14:22]** to run those scheduled jobs. Now, most

**[14:23]** people are creating scheduled jobs to

**[14:25]** just insert a simple prompt. But

**[14:27]** actually, the smartest people are

**[14:28]** actually using scheduled workflows to

**[14:30]** chain skills together inside a prompt.

**[14:33]** So, you can schedule a task that's

**[14:35]** effectively going to run multiple skills

**[14:37]** in sequence. You might have a weekly

**[14:39]** content digest that runs every Monday at

**[14:42]** 9:00 a.m. So, it's going to pull the

**[14:43]** previous week's YouTube videos, run an

**[14:46]** analysis across those, and then generate

**[14:48]** three LinkedIn posts using your voice

**[14:50]** profile, and then drop them into a

**[14:52]** review folder. So, you come in on Monday

**[14:54]** morning, you've got all of those already

**[14:56]** ready in the review folder. And they're

**[14:57]** contextualized and followed all of the

**[14:59]** skill process documents that produce

**[15:01]** high-quality outputs. So many different

**[15:03]** skills all chained together to produce

**[15:05]** one output that you come back and you

**[15:07]** can approve or supervise. And the

**[15:08]** biggest learning when I started building

**[15:10]** this out, my original aim was to build

**[15:11]** out fully autonomous scheduled

**[15:14]** workflows, run the whole thing, ship the

**[15:16]** output, post it to LinkedIn, whatever.

**[15:18]** But it was actually pretty bad because

**[15:20]** 20% of the time something wouldn't be

**[15:22]** quite right. So instead, I've actually

**[15:24]** built this framework now around doing

**[15:26]** 80% of the work automatically, the

**[15:28]** research, the narrowing of different

**[15:30]** topics. But what I've added in is always

**[15:33]** having a human checkpoint before

**[15:34]** anything goes live. So I'm never going

**[15:36]** to post content that's just AI generated

**[15:38]** stuff. I'm always going to have that

**[15:40]** human supervisor in the process until we

**[15:42]** can get to a level of quality where

**[15:44]** things can run autonomously and we're

**[15:46]** happy with them. So all of my content

**[15:47]** drafts, for example, land in a folder so

**[15:49]** that I can actually come in and

**[15:50]** supervise them and review them and

**[15:52]** approve the outputs. So it's basically

**[15:54]** giving you the speed of the automation

**[15:55]** without the risk of shipping something

**[15:57]** that's just pure AI slop, which we do

**[15:59]** not want to contribute. So you can

**[16:00]** effectively use scheduled jobs to chain

**[16:03]** multiple skills together and then add in

**[16:05]** a human checkpoint to actually approve

**[16:07]** or make sure the quality is high. Right?

**[16:09]** So that is four amazing features. Each

**[16:11]** one you can build inside claw code using

**[16:13]** what's already there in just a few days.

**[16:15]** But here's the fifth and honestly this

**[16:18]** is the one that made me stop looking at

**[16:19]** Hermes and OpenClaw because I did not

**[16:21]** see enough capacity for it to do this

**[16:23]** well. Now because Hermes and OpenClaw

**[16:25]** are built solely to be agent frameworks,

**[16:28]** they're very tool focused. So, it's all

**[16:30]** about installing a skill, running a job,

**[16:32]** getting an output, but they don't know

**[16:33]** anything really about your business. You

**[16:36]** can, of course, install ways to actually

**[16:38]** give it information about your business,

**[16:39]** but they don't out the box know your

**[16:41]** brand voice, know your ICP, they don't

**[16:43]** know your positioning, they don't know

**[16:45]** who your clients are, what your tone in

**[16:47]** your emails usually is. All of these

**[16:49]** things are critical for high quality

**[16:50]** outputs. And it's the equivalent of

**[16:52]** basically starting from zero when you

**[16:53]** run a new skill. And this is what

**[16:55]** shifted me away from systems like Hermes

**[16:57]** and Open Claw to build my own system

**[16:59]** because I realized that the real unlock

**[17:01]** isn't actually the agents. The agents

**[17:03]** and the models are getting better and

**[17:04]** better. It's the layer underneath the

**[17:06]** context that we discussed at the start.

**[17:08]** The brand context folder, the voice

**[17:09]** profile, the audience avatar, all of

**[17:12]** that preloaded pulling into the right

**[17:14]** skill at the right time is what actually

**[17:16]** generates high quality outputs. So I

**[17:18]** actually pulled together myself a set of

**[17:20]** skills that help me generate my voice

**[17:22]** profile and I make sure that when I

**[17:24]** build out my skills using the skill

**[17:26]** creator skill all of them reference the

**[17:28]** right context at the right time. So if I

**[17:29]** have a skill that builds out LinkedIn

**[17:31]** posts for example it will always

**[17:33]** reference my brand voice. It will

**[17:35]** understand the positioning because it

**[17:36]** understands who my clients are. And I

**[17:38]** used content as an example because it's

**[17:40]** relatable to a lot of different

**[17:42]** businesses. It doesn't mean you need to

**[17:43]** use these systems to actually generate

**[17:45]** your content. And the way that we've

**[17:46]** done this is basically moving

**[17:48]** everything, all of that context for my

**[17:50]** business into a single brand context

**[17:52]** folder that every skill is able to

**[17:54]** reference. So you update the information

**[17:55]** once and every skill gets that update

**[17:57]** when it runs. So business context is

**[17:59]** that compounding advantage that you

**[18:01]** cannot get right now. So build this,

**[18:03]** right? And this totally underpins all of

**[18:05]** the other pillars that we've talked

**[18:06]** about today. You need to inject the

**[18:08]** right context at the right time. And

**[18:10]** that starts with actually having a

**[18:12]** shared context folder that focuses on

**[18:14]** your brand and you. So when you bring

**[18:16]** this all together, this is exactly how

**[18:18]** it looks in a three-step process to

**[18:20]** compare to the one we showed at the

**[18:21]** start. We have your own agentic

**[18:22]** operating system where we have the

**[18:24]** business brain which underpins and

**[18:25]** powers cloud code by injecting the right

**[18:27]** context at the right time. We're able to

**[18:29]** then actually just write goals whether

**[18:31]** that's to create a scheduled job or to

**[18:33]** manage multiple business goals in one

**[18:35]** place. Claude is then going to do the

**[18:36]** work in the background to break it down

**[18:37]** into subtasks, choose the right skills,

**[18:39]** etc. And what that enables is your

**[18:41]** system to deliver you a highquality

**[18:44]** result that's contextualized by your

**[18:46]** business context completely replacing

**[18:47]** the need for a framework like Hermes or

**[18:49]** Open Claw and without all of the

**[18:51]** technical overhead and cost implications

**[18:53]** of moving off the pro and max plans from

**[18:56]** Claude. So that's the five features that

**[18:57]** actually matter and how to build each

**[18:59]** one of them inside Claude code yourself.

**[19:01]** And if you're building out your own

**[19:02]** version right now, which a lot of you in

**[19:04]** the comments have told me you are,

**[19:06]** here's my honest advice from three

**[19:08]** months of getting this wrong and

**[19:09]** rebuilding it. Start with this business

**[19:11]** brain. Don't start with the agents.

**[19:13]** Don't start with the multi- aent

**[19:14]** orchestration. I made this same mistake.

**[19:17]** Every feature I just walked through gets

**[19:19]** multiplied by having the solid context,

**[19:21]** the foundation layer underneath it. And

**[19:23]** none of them are going to work without

**[19:25]** that layer. And if you just want to skip

**[19:26]** the setup and grab the whole thing

**[19:28]** plugandplay today, then check out the

**[19:30]** link below in the description for the

**[19:31]** Aentic Academy. So, we've got the Aentic

**[19:33]** Os, the command center that you saw

**[19:35]** today with the dashboard and all 20 plus

**[19:37]** skills ready to go with a oneline

**[19:40]** install. And if you want to see exactly

**[19:41]** why I built out the command center in

**[19:43]** the first place, then check out the next

**[19:44]** video. Thanks for watching.
