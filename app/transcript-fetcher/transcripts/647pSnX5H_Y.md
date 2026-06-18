# Transcript: 647pSnX5H_Y

**URL:** https://www.youtube.com/watch?v=647pSnX5H_Y
**Segments:** 809

---

## Full Text

What do you do when you get underneath an agent's skin and understand how it works? It's not just an LLM. I talk a lot about these other components and it feels really abstract. I talk about prompts and skills and MCPs and connectors and hooks and scripts and all of this stuff. And if you're deep in the engineering world, these are short hands, these are words that you understand. It's easy to make sense of. But for most people, it feels like a foggy middle layer between the model is smart and the work got done. And how do you set up your model to do that is one of the most common questions I get. Not because Codex in particular can connect to lots of apps, although that is certainly a useful thing. Claude does that, too. Not because everybody suddenly needs to become a plugin developer, although you can if you want, it's never been easier. And not even because the plugin directory is the most exciting part of Codex. The real reason why you should care about this is because you need to understand how the secret sauce for an AI agent works. What is the scaffolding that you put an AI agent inside of so it actually works? It's like Darth Vader has a mech suit, right? And that's how Darth Vader works. Or Transformers have these huge metal suits and that's how they get the job done. This is how LLMs work. They have these suits around them that help them get work done. And Codex plugins are a really handy way to understand that. And so the story is not that 5.5 GPT 5.5 suddenly got smarter, although it did. The story is not just that Codex happens to have extensions. The story is that agents are becoming capable enough to do very rich work and we are now at a point with simplicity and understanding of these tools that we can actually confidently, not even as engineers, build the scaffolding around the agent ourselves. Which means we can customize what they can do. We can customize the mech suit, right? A little prompt engineering here, a local script there, a little work on an MCP server, maybe. These are all real things that I know lots of people who are not engineers are able to do. So, in this video, I want to give you a product handle on this whole rich scaffold. I want to make the map clear for you. What's a prompt for? Why and when do you use it? By contrast, what's a skill for? What do you use a skill for and when? How does that contrast with a prompt, right? It's often confused. What's a plugin for? Why do we care about plugins? When do we use plugins and not skills? When do we use plugins and not prompts? What do MCP servers and connectors do? Why Why should we care about those? To be honest, for most of us, we don't understand the relationship. We can't name that. And if we can't name those things, it's really hard to build strong, stable, agentic systems. And so, this is about how you customize your agentic system so that you understand what you want done and are confident your agent can do it and can actually get it done. The super practical do-it-now workbook version is going to go on Substack. And so, it has the workflow audit and the decision tree for prompt versus skill versus plugin versus MCP. It'll have examples of what belongs in a skill.dat markdown file, a starter plugin structure, a testing checklist, and the trust questions you should ask before you install or build something so you feel safe doing it. OpenAI describes ChatGPT 5.5 as better at messy multipart work, like planning and using tools and checking its work and navigating ambiguity. Did you hear it? This is the part, messy multipart work. If you want to do that real frontier work, what I'm finding is most people get stuck not because they don't have the tool, but because they don't have the understanding of the harness to use it. There's not been a clean, clear instruction set that says this is what all these things are for. So, that's why we're doing it now. So, here's how we're going to tackle this video. We're going to go through in order prompts, skills, plugins that package up a workflow, right? And then, after plugins, we're going to also tackle as a bonus MCPs and connectors so you understand how agents access tools. And in addition, no, we're not done yet. We're also going to tackle hooks and scripts and how they work and how they relate to all the other things I just named. And then last but not least, we're going to talk about how marketplaces work because marketplaces are becoming the mechanism by which we distribute all of this. So, it's a busy video. Let's jump into it. First, prompts. A prompt is what you do when you want to do something once. That is where we're at in 2026. If the task is temporary, if it's small, if it's highly specific to the moment, you probably don't need any of the rest of the infrastructure. But, a prompt is not a great home for anything that you repeat constantly or consistently. A prompt can describe a process, sure, but it doesn't really package up a workflow in a way that's repeatable. It doesn't really carry tools with it. A prompt is just a single piece of text you stick in, right? It doesn't carry permissions. And so, a prompt is really useful when you have those one-off asks. But, I find in general most people index really highly here and they they don't realize that they're putting so much into the prompt that generates hours and hours and hours a week of wasted effort because too much is going into the prompt. Can you share your prompt with your team? Well, there are little tools for that. So, a prompt doesn't carry most of what we need it to carry if it's going to be reusable. And that is where we start to think about skills, right? So, a skill is where you teach a tool. It could be Codex, it could be Claude, a very reusable process. For example, your team might have a particular way of reviewing pull requests or a particular way of writing marketing documents. You want to be clear about what that is and how you do it. It is your house style and you want to make sure that whatever LLM you use always uses that across your whole team. That is what a skill is for. Now, a skill, amazingly enough, is just a clear markdown document that describes in good detail how you do that work. And yes, there's skills to write skills. I've made skills to write skills over on the Substack. It's absolutely something where you can get AI to help you. But my suggestion for you, if you're trying to understand the prompt versus a skill difference, is to think of prompts like one-offs, and to think of skills as anything that you want to reuse and reinvoke. And because skills are so universal, you don't have to worry, really, oh, is this a Codex skill? Oh, is this a Claude code skill? You just write the skill, and then you use it with whatever tool you end up using it with, and it's going to be great. You don't have to worry about it from there on out. So, the thing on skills, if you're looking for a concrete example of skill versus prompt, think of it as I would prompt if I had a one-off note to a client that was complicated, and I needed to put some custom backstory in. I would skill if I knew I was sending a bunch of cold outbound notes with particular content I wanted to pull in from a particular set of documents, and I needed to be customized to that individual, but I needed a consistent skill for how to do that. I would write the skill that basically says, this is what a good structured outbound email looks like, these are the paragraphs in it, these are the data we want to pull in, uh, and this is the beginning, middle, and end and how you write a strong close. Just a just a quick example. You can write skills for marketing, for customer service, for success, literally anything that you think the LM can do more than once. All of those engineering tasks, those are skills, too. Skills are super flexible, and actually what I find, once people get the idea of skills, the biggest issue is that people write so many skills, it's hard to keep track of them. And yes, there are tricks for that, too. I would encourage you to think about how you divide and conquer with your skills, right? Think about your skills as essentially having a power law relationship, which is a fancy way of saying that 20% of your skills are going to be worth 80% of the value, and you have to find the right 20% that are going to be repeated often, constantly, with high sensitivity to what goes right or what goes wrong and just jump in. So, that's a little tidbit on skills and now let's jump right into it to plugins, which is the next thing. So, if a skill is a way to do a thing consistently, a plugin is a bigger package around that. So, we've gone from prompts to skills, now we're at plugins. A plugin can include skills, but it can also include app integrations, MCP servers, hooks, assets, commands, metadata. It basically takes a whole workflow and gives it a name and sort of wraps around it and makes it installable. And so, if you want to add like an entire workflow in one go and it's much bigger than a skill, that is a plugin. And what's beautiful about it is that plugins are extremely shareable. A plugin is something that your team can use without everyone manually reconstructing the setup. In my outbound email example, let's say you had to have a live connector to data to pull from Salesforce to pull in the right name and the details about the client. Fantastic. That is something that would work in a plugin that would not work in a skill. So, a skill says, "Here is how to do the work." A plugin says, "Here is the workflow package that you can install and all of it will just get magically done for you." And then everything that you need to get that whole workflow is completely accomplished in that one plugin. And so, yeah, there's real work that gets done with plugins. It's real work to set them up, but once you set them up, they're incredibly powerful. And this is why real work rarely lives entirely in the prompt. It lives other places, right? It lives in the connectors that we pull in live. So, it might pull in from Slack or from Figma, from GitHub, from other data sources. Real work can live in where we put our revisions to so we review them. Real work can live in the technical skill that we apply as we go through the process of doing this work with an AI. The thing that we need to get to is we need to understand that basically everything I'm describing is like training wheels that help the LLM understand how to do the work that matters. And so, the more we're clear about that, the easier it becomes to get the AI to do that real work. And plugins are a fantastic way to wrap up a bunch of individual components of work and say, "Hey, here's the whole thing in a nutshell. It's in a neat little package. All you have to do is copy it and get it into your app, and then you'll have the whole workflow there at your command whenever you're ready." And by the way, if you think A, AI can't do this, or B, it's too hard, I've got news for you. If you're any kind of serious AI user, you are already doing the plugin work. You are literally the human plugin, cuz you copy from one app, you paste it into the chat, you ask the model to reason, you go and get data from somewhere else, you check the result, you come back, and it goes on and on and on. You are the human plugin. If you don't want to be the human plugin, consider making an actual plugin. And no, you don't have to be an engineer to make an actual plugin. Not in 2026. You can absolutely do it without that. So, we've talked about at a high level what skills are, we've talked about what prompts are, we've talked about what plugins are, and you can think of these as three sort of different scales, right? Where plugins are the biggest. What are MCPs and app connectors? This is how an agent gets access to the systems where work actually lives. So, when you remember when I said, "Oh, we'll plugin to Salesforce for outbound," that's an MCP. That's an app connector. It plugins. It figures out where to go to get live data and comes back with that real data. And most apps are better when they have real data. And so, you can think of those tools as like internet plugs. They plug in and they get data back out, right? And I'm old enough to remember when we literally had to plug in the internet. It wasn't just Wi-Fi anymore. That is what you were doing with an MCP. It's like a universal plug to the data that you can put in, and you can get it back out. And yes, you can absolutely build an MCP, but increasingly, so many different SaaS tools and places where work is happening are aggressively building their own MCPs and building data connectors so you don't have to. And one of the reasons I am doing a plug-in video is because I think that people misunderstand and they think, "Well, an MCP connector is just the same as a plug-in, right? It's like they're all plugging into something." No, and the reason why it's confusing is that a plug-in can contain an MCP, but a plug-in typically has more to it. It is not just an MCP server. There's a whole piece of workflow that you're tackling with that plug-in, which may include a call to live data, and then have a bunch of other things that you're doing with the data along the way. So, a plug-in is more more of a larger package. So, we've talked about prompts. We've talked about prompts versus skills. Prompts and skills versus the whole package with the plug-in. How the plug-in is different from MCP and app connectors. Now, let's talk about hooks and scripts. Those are big points of confusion. Hooks and scripts are for the parts of your workflow where you should not rely on the model remembering to be careful. So, if the code needs formatting, run a formatter, right? If the schema needs validation, don't ask the model to think about it. Actually validate the schema. If the tests need to pass, run the test. Don't ask the model to imagine running the test. It has to actually go and run the script and run the test. If a generated file needs to meet a particular structural contract, like it has to be good JSON, actually check it and see if it's good JSON with a script. If a review should happen before the agent stops, build that review into the loop. This is one of the most important parts of doing good work with agents, but it's really misunderstood because people think that it's the same thing as an MCP connector. It's not. People think it should be left to the model's best judgment. It should not. Some things ought to be deterministic, by which I mean some things should not be left to the model. A good agent workflow is designed so that the parts that are deterministic are correctly framed as scripts, or correctly framed as hooks into services that are deterministic. And if that feels really confusing, don't let it. Because hooks and scripts actually fit right inside our best friend, plugins. Think of a plugin as like a grab bag present where you've got like 10 things in the box for your buddy and the plugin is the whole present around it. A plugin can contain scripts and it can contain hooks into other services as a part of the overall workflow. It you're not limited to just having a prompt in an MCP connector or something inside a plugin. A plugin package is big enough that it can hold the whole workflow to make it reusable. And that is why I think the App Store analogy is too small. We think of plugins as oh, they're apps in the App Store. No, they're not really. And it's not even as simple saying well, now Codex has extensions. It's not that that's wrong, it just really undersells the power of what I am talking about. Because if you think of plugins as add-ons, you ask well, what can I install, right? And I'm going to go passively shopping like I do in the App Store. If you think of plugins as workflow packaging, you're going to ask a much sharper question because you're going to ask yourself, what part of my work has enough repeatable structure that the agent should be able to inherit it and use it. And maybe that's something that my whole team wants to use. That's the real question. Think of your work as repeatable structures and then think of how you build plugins to support it and you're going to be in much better shape than if you're messing around with these individual things. And that's one of the secrets in this video, right? Don't think of each of these things I'm describing and defining as like individual battle bots that are all in competition with each other to find out who's going to be the best and serve your AI. That's not how it works. Think of these as Lego bricks that taken together make something bigger and more useful in terms of your workflow. And by the way, in that analogy, a plugin is a bunch of Legos all built up together into a structure. A plugin has lots of these components like scripts and hooks and connectors all inside it. And so you can ask yourself, do I want to have a plugin for architecture review? Do I want to have a plug-in for how I handle marketing documents? Do I have a plug-in for how I handle customer service requests? Those are all large workflows. Some of them are bundles of workflows. And part of our job as humans, as we start to think about the serious work these systems are capable of, is to ask ourselves, well, what's the right unit of work here? Do I want to make customer service in my tiny company one plug-in, or is it actually smarter to say, well, there's a refund uh plug-in that we're going to need to invoke, and there's also a plug-in for adding and activating customers who somehow aren't activated. We'll make that a separate plug-in. And then there's a plug-in for making sure that customers are able to upgrade when they want to, and we'll make that a separate plug-in. Totally just examples, but you get the idea. Your job is to understand the semantic meaning of the workflow and to say, this is a good unit of work that has a neat edge and boundaries around it that we can make into a plug-in. That's a great example. By the way, here's another secret in this video. That's a great example of the kind of skill that is worth a lot of money these days. Because very few people know how to look at a workflow and say, here's how I draw edges around it. Here's the boundary around this workflow. And once I have the boundary around this workflow, this is how we turn it into a plug-in that I can then repeatedly share across the team. That's gold. That's an incredible skill to have. If you don't know how to explain that the work has value in a particular bounded space, you're going to always be tempted to make a workflow too big and too wide and subject to problems, right? Cuz in the analogy I gave you on customer success, if all of that was one plug-in, could it technically work? Yeah, maybe if you were a small company and you put a ton into the plug-in, is it a good idea to do it that way? If no, probably not, because a workflow has one job, and what I described in my little example was three jobs, and probably in reality there's like eight jobs. So, no, you probably need more than one plug-in for customer success at this imaginary little company. And that's okay. Once you get into the habit of figuring out the plug-in, and I've got lots in the Substack on that, you can make that stuff, right? You can you can stamp out plug-ins and actually go to work. If we zoom back out, the difference here is really significant. Because a generic model that doesn't have a plug-in, doesn't have scaffolding as I've been describing, can say something useful at a high level. And maybe if you prompt it and repeat your prompts and waste a lot of hours, it will be specific to you. But only cuz you prompted all the time with lots of heavy prompts. But a truly scaffolded agent can review all of your work according to your standards, use the right tools, and do so effectively to get real work done, which is like a 10x bigger deal. And it's the same intelligence. It's it's not different LLMs on the inside. This is a great example of how we are a big part of the answer to making AI smarter. And I don't mean that in some dark way they're all watching us. I mean in the sense that literally, if you want smarter work done, you got to do the part to put the scaffolding in place. And you can. It is not that scary. And part of why I'm making this video now is that I really do believe, because I have seen story after story after story of people who build these, that it's not as hard as it used to be. In 2025, I couldn't make this video. In 2026, I can make this video because plug-ins are now something where I have literally seen people who do not have coding knowledge figure out how to build a plug-in to support their work. I saw someone do this for editorial work, where she needed to have a plug-in to help her take a first pass at editorial review. And there's a specific workflow for that. Here's how you read the text. Here's the three different ways you read the text. Here's the comments that you want to think about adding in the places in the text that are rough. Did it do all of the work for her? No, it did not do all of the work for her, because you still need a human to have that sort of editorial perspective. But did it save her a lot of time because it gave her a first pass with a review on where the text is rough, where the text was incoherent, where there are factual inconsistencies, in some ways much better than a person? Yeah, and it was faster, too. And she could totally build that without having to go back and re-prompt every time. And it was much bigger than a skill because it involved actually understanding more information sources than just one piece of text. And by the way, another great example for non-technical folks is around design. You can plug into Figma, you can plug into your design tool of choice, and you can actually pull down a bunch of the details of how a current design looks, but also how the design language looks. And you can start to build a workflow that accounts for all of that and pops out new work. And if you're wondering, does this align to sort of how we're starting to think about things with Claude design in the mix? Absolutely. We are moving to a world where the hyperscalers are putting in place more and more tools, more and more plugins that help you do this work effectively. Arguably, Claude design, which dropped just a couple of weeks ago, is a fancy plugin with a UI for Claude for design. It's like the plugin was so important, they made it a product. That's how much plugins matter. And if you think that you can just sit around and wait and Claude or ChatGPT will eventually launch all of your dream plugins, I got I got a bridge to sell you. I got news for you. It ain't going to work that way. You have got to be in a place where you can take proactive action and say, "No, I want this plugin for this thing. It's not perfect. It's not right the way it is now. It's too much manual work. I waste too much time in custom prompting. My skills aren't enough. I want something that has a data connector. a script inside there that checks and validates and makes sure it works. I'm going to have to have a little skill as well." That's a plugin, people. And you can totally do that. A weekly business report is a great example, right? Maybe you need spreadsheets and Slack contacts and docs and dashboards and past reports and charts. That's That's a plugin, right? I could I could give you a bunch more examples. That's the idea. And if you're wondering, I do have a ton more examples. They're all in the Substack. I have a customer brief, uh how you handle that with email and CRM, etc. I have a hiring readout and how you handle that as a plugin. Tons and tons of these. And I think it's really important to have starters for this because if you see the start of a plugin, it's easier to customize than if you're just trying to go from a blank page and you've never done a plugin before. So, that's why I made the hook. Ultimately, and I get very passionate about this, agentic scaffolding must not stay vague. If scaffolding just means some engineering stuff around the agent to most of us, then only engineers can ever participate in designing it. That is an old 2022 era problem. But now we're in 2026, and if the workflow is real, the people who understand the work must be the ones who put that knowledge in. And I have talked to person after person after person who comes from a non-technical background who figured that out, and they're now stamping out work because they know what good looks like. I talked to two of them this morning, and they're working on like complicated retail scale workflows because they figured out what works for them. They know which sources matter. They know when the output is wrong. They know which steps are always forgotten. That domain knowledge that you have as a non-technical person, quote unquote non-technical, that's always blurry in 2026, that's what matters. And that's what you can then leverage to create the custom plugins that work for you. And I think the issue is the way to encode all of this has become more unclear, not less, in the last 6 months, right? Like do you write a better prompt? Well, now we have skills. Is it a skill now? Do I ask my engineers to make an MCP? Is it an MCP server? I don't know. And I have people ask me these questions all the time, right? Is it a connector? Do we need a connector? No, maybe it is a plugin after all. Disambiguate it. Understand what each thing does. A script helps you to do predictable, deterministic things every time. A skill helps an LLM to follow a process in a way that is clear and that you can share across teams and that's consistent. A prompt is good for one-off work, and yes, it still matters to write good prompting. It does. All the work you did in 2025 paid off if you worked on your prompting. And a plugin is like a bundle around a bunch of things, right? It includes the script, it includes the skill, it includes pieces of the prompt that matter and that are reusable. And yes, it also includes MCPs and connectors because those are connectors to live data. This is the mental model I wish people had because engineers know this stuff, but it's just not getting explained to the rest of us. And then when an engineer says something like, well, this should be a skill and this needs an API and you waited 2 weeks to have this meeting, right? No, this should be a prompt. I've had these conversations where engineers basically go through and this is the level of understanding they have in their heads. They never explain it to you and they lay all of this out. It should not be a mysterious middle layer. There should not be a mysterious middle layer between the LLM and the work that gets done for you. And that is what I want to make sure that you have and that is why I have laid this video out the way I have so that you understand the mental model of how this works. And when you're ready to go deeper, the Substack is there and you can go deeper and actually look at all these practical use cases that I'm laying out. You can look at a guide that gives you a way to build plugins for what you want done and gives you starter plugins for a bunch of the workflows I've talked about and gives you a way to audit your workflow and develop a plugin. So all of that practical stuff is there, but everybody should know the mental model and that's why I'm putting this here for all of us to see and watch and talk about because even CEOs need this now. I don't want a CEO saying, should it be a skill? Should it be an MCP? If your CEO is confused about this harness stuff, show them this video, right? Because one of the things I get really passionate about is that C-suite, especially anyone but the CTO, tends to be non-technical enough in most companies that they don't get this stuff. They don't understand that a script is a deterministic check and you shouldn't just trust the model to check itself. And then they get confused and they say, why aren't you using AI? And you're like, I am using AI. I just want a deterministic script at the end. I've had that conversation. It's a real conversation. You need to give your leadership enough context on this stuff that they can actually be useful in supporting the Oregon AI transformation. And that starts with understanding what is in the box when it comes to a harness so that people don't get confused. When we're talking about the difference between an LLM, even in an agentic LLM in Codex or in Claude code, and truly useful personalized workflows, we're talking about this, right? This difference between skills and plugins and and connectors and and how they matter. Please, please, please, make sure that the people who need to see this see it in your world so you get the support you need. Because I have had to have enough conversations with senior leadership that I know for a fact most organizations, there are very senior folks who don't have any clue about this. Like none. Zero clue. They don't get it. Don't be like that. Share this with the people that need that need to hear it. Make sure everybody has the same mental model. Uh if you do it once, it's a prompt. If you do it repeatedly, it's a skill. If the workflow needs to travel or other people need to install it, if it needs tools or assets or connectors, guess what? It's a plugin. If it needs access to another system, it's an MCP or app connector. And yes, that live data can come inside a plugin and nest inside. It's It's like one brick in the larger Lego brick model. If the workflow has to be verified, you got to add a check. All of that together, if you understand that, will prevent you from wasting work. Because not everything needs to be a plugin. I hope you're getting that. I'm not saying everything needs to be a plugin. Some things should stay prompt. Some things ought to sit ought to stay skills, right? You don't need extra data. You don't need a bunch of other stuff. It just ought to say skills. Some things should be normal scripts and never touch an LLM at all. Some things should stay human as I hope you know. The The judgment to know what's good or not at the end of it is going to be human judgment. The goal is not to turn your workspace into a gigantic museum of plugins you never use. The goal is to simply understand the parts of your work that are repeated and valuable and structured enough to package and figure out the right solution so that you can do that. It's one of the most powerful ways you can do practical AI automation today. It's where the leverage is living in 2026. And that's why I get so passionate about it. I hope you've had fun following the story here of how we got to plugins from scripts and from skills and from prompts. I hope you have a clear mental model now and I will see you next time. And as always, there's more on the Substack there. So, jump in if you want to build those today. Cheers.

---

## Timestamped Segments

**[0:00]** What do you do when you get underneath

**[0:01]** an agent's skin and understand how it

**[0:03]** works? It's not just an LLM. I talk a

**[0:05]** lot about these other components and it

**[0:06]** feels really abstract. I talk about

**[0:08]** prompts and skills and MCPs and

**[0:10]** connectors and hooks and scripts and all

**[0:12]** of this stuff. And if you're deep in the

**[0:13]** engineering world, these are short

**[0:15]** hands, these are words that you

**[0:16]** understand. It's easy to make sense of.

**[0:18]** But for most people, it feels like a

**[0:21]** foggy middle layer between the model is

**[0:23]** smart and the work got done. And how do

**[0:25]** you set up your model to do that is one

**[0:27]** of the most common questions I get. Not

**[0:30]** because Codex in particular can connect

**[0:32]** to lots of apps, although that is

**[0:34]** certainly a useful thing. Claude does

**[0:36]** that, too. Not because everybody

**[0:37]** suddenly needs to become a plugin

**[0:39]** developer, although you can if you want,

**[0:41]** it's never been easier. And not even

**[0:43]** because the plugin directory is the most

**[0:45]** exciting part of Codex. The real reason

**[0:48]** why you should care about this is

**[0:50]** because you need to understand how the

**[0:54]** secret sauce for an AI agent works. What

**[0:57]** is the scaffolding that you put an AI

**[1:00]** agent inside of so it actually works?

**[1:02]** It's like Darth Vader has a mech suit,

**[1:04]** right? And that's how Darth Vader works.

**[1:06]** Or Transformers have these huge metal

**[1:08]** suits and that's how they get the job

**[1:09]** done. This is how LLMs work. They have

**[1:11]** these suits around them that help them

**[1:13]** get work done. And Codex plugins are a

**[1:15]** really handy way to understand that. And

**[1:17]** so the story is not that 5.5 GPT 5.5

**[1:21]** suddenly got smarter, although it did.

**[1:23]** The story is not just that Codex happens

**[1:26]** to have extensions. The story is that

**[1:27]** agents are becoming capable enough to do

**[1:29]** very rich work and we are now at a point

**[1:33]** with simplicity and understanding of

**[1:36]** these tools that we can actually

**[1:39]** confidently, not even as engineers,

**[1:41]** build the scaffolding around the agent

**[1:44]** ourselves. Which means we can customize

**[1:46]** what they can do. We can customize the

**[1:48]** mech suit, right? A little prompt

**[1:49]** engineering here, a local script there,

**[1:52]** a little work on an MCP server, maybe.

**[1:55]** These are all real things that I know

**[1:56]** lots of people who are not engineers are

**[1:58]** able to do. So, in this video, I want to

**[2:00]** give you a product handle on this whole

**[2:03]** rich scaffold. I want to make the map

**[2:05]** clear for you. What's a prompt for? Why

**[2:08]** and when do you use it? By contrast,

**[2:10]** what's a skill for? What do you use a

**[2:12]** skill for and when? How does that

**[2:13]** contrast with a prompt, right? It's

**[2:15]** often confused. What's a plugin for? Why

**[2:17]** do we care about plugins? When do we use

**[2:19]** plugins and not skills? When do we use

**[2:20]** plugins and not prompts? What do MCP

**[2:23]** servers and connectors do? Why Why

**[2:25]** should we care about those? To be

**[2:26]** honest, for most of us, we don't

**[2:28]** understand the relationship. We can't

**[2:29]** name that. And if we can't name those

**[2:31]** things, it's really hard to build

**[2:33]** strong, stable, agentic systems. And so,

**[2:37]** this is about how you customize your

**[2:38]** agentic system so that you understand

**[2:42]** what you want done and are confident

**[2:43]** your agent can do it and can actually

**[2:45]** get it done. The super practical

**[2:47]** do-it-now workbook version is going to

**[2:49]** go on Substack. And so, it has the

**[2:50]** workflow audit and the decision tree for

**[2:52]** prompt versus skill versus plugin versus

**[2:55]** MCP. It'll have examples of what belongs

**[2:57]** in a skill.dat markdown file, a starter

**[2:59]** plugin structure, a testing checklist,

**[3:01]** and the trust questions you should ask

**[3:03]** before you install or build something so

**[3:05]** you feel safe doing it. OpenAI describes

**[3:07]** ChatGPT 5.5 as better at messy multipart

**[3:10]** work, like planning and using tools and

**[3:12]** checking its work and navigating

**[3:13]** ambiguity. Did you hear it? This is the

**[3:16]** part, messy multipart work. If you want

**[3:18]** to do that real frontier work, what I'm

**[3:20]** finding is most people get stuck not

**[3:23]** because they don't have the tool, but

**[3:24]** because they don't have the

**[3:25]** understanding of the harness to use it.

**[3:28]** There's not been a clean, clear

**[3:29]** instruction set that says this is what

**[3:31]** all these things are for. So, that's why

**[3:32]** we're doing it now. So, here's how we're

**[3:34]** going to tackle this video. We're going

**[3:35]** to go through in order prompts, skills,

**[3:38]** plugins that package up a workflow,

**[3:41]** right? And then, after plugins, we're

**[3:43]** going to also tackle as a bonus MCPs and

**[3:46]** connectors so you understand how agents

**[3:48]** access tools. And in addition, no, we're

**[3:50]** not done yet. We're also going to tackle

**[3:51]** hooks and scripts and how they work and

**[3:53]** how they relate to all the other things

**[3:55]** I just named. And then last but not

**[3:57]** least, we're going to talk about how

**[3:59]** marketplaces work because marketplaces

**[4:01]** are becoming the mechanism by which we

**[4:03]** distribute all of this. So, it's a busy

**[4:04]** video. Let's jump into it. First,

**[4:06]** prompts. A prompt is what you do when

**[4:09]** you want to do something once. That is

**[4:11]** where we're at in 2026. If the task is

**[4:13]** temporary, if it's small, if it's highly

**[4:15]** specific to the moment, you probably

**[4:17]** don't need any of the rest of the

**[4:18]** infrastructure. But, a prompt is not a

**[4:21]** great home for anything that you repeat

**[4:24]** constantly or consistently. A prompt can

**[4:26]** describe a process, sure, but it doesn't

**[4:28]** really package up a workflow in a way

**[4:30]** that's repeatable. It doesn't really

**[4:31]** carry tools with it. A prompt is just a

**[4:34]** single piece of text you stick in,

**[4:36]** right? It doesn't carry permissions. And

**[4:38]** so, a prompt is really useful when you

**[4:40]** have those one-off asks. But, I find in

**[4:42]** general most people index really highly

**[4:45]** here and they they don't realize that

**[4:47]** they're putting so much into the prompt

**[4:49]** that generates hours and hours and hours

**[4:52]** a week of wasted effort because too much

**[4:55]** is going into the prompt. Can you share

**[4:57]** your prompt with your team? Well, there

**[4:58]** are little tools for that. So, a prompt

**[5:01]** doesn't carry most of what we need it to

**[5:04]** carry if it's going to be reusable. And

**[5:06]** that is where we start to think about

**[5:07]** skills, right? So, a skill is where you

**[5:10]** teach a tool. It could be Codex, it

**[5:12]** could be Claude, a very reusable

**[5:14]** process. For example, your team might

**[5:17]** have a particular way of reviewing pull

**[5:19]** requests or a particular way of writing

**[5:21]** marketing documents. You want to be

**[5:23]** clear about what that is and how you do

**[5:26]** it. It is your house style and you want

**[5:28]** to make sure that whatever LLM you use

**[5:30]** always uses that across your whole team.

**[5:32]** That is what a skill is for. Now, a

**[5:35]** skill, amazingly enough, is just a clear

**[5:39]** markdown document that describes in good

**[5:43]** detail how you do that work. And yes,

**[5:45]** there's skills to write skills. I've

**[5:47]** made skills to write skills over on the

**[5:48]** Substack. It's absolutely something

**[5:50]** where you can get AI to help you. But my

**[5:53]** suggestion for you, if you're trying to

**[5:54]** understand the prompt versus a skill

**[5:56]** difference, is to think of prompts like

**[5:58]** one-offs, and to think of skills as

**[6:01]** anything that you want to reuse and

**[6:03]** reinvoke. And because skills are so

**[6:07]** universal, you don't have to worry,

**[6:09]** really, oh, is this a Codex skill? Oh,

**[6:11]** is this a Claude code skill? You just

**[6:13]** write the skill, and then you use it

**[6:16]** with whatever tool you end up using it

**[6:18]** with, and it's going to be great. You

**[6:19]** don't have to worry about it from there

**[6:20]** on out. So, the thing on skills, if

**[6:22]** you're looking for a concrete example of

**[6:23]** skill versus prompt, think of it as I

**[6:26]** would prompt if I had a one-off note to

**[6:29]** a client that was complicated, and I

**[6:31]** needed to put some custom backstory in.

**[6:33]** I would skill if I knew I was sending a

**[6:36]** bunch of cold outbound notes with

**[6:38]** particular content I wanted to pull in

**[6:40]** from a particular set of documents, and

**[6:42]** I needed to be customized to that

**[6:44]** individual, but I needed a consistent

**[6:46]** skill for how to do that. I would write

**[6:48]** the skill that basically says, this is

**[6:49]** what a good structured outbound email

**[6:51]** looks like, these are the paragraphs in

**[6:53]** it, these are the data we want to pull

**[6:55]** in,

**[6:56]** uh, and this is the beginning, middle,

**[6:59]** and end and how you write a strong

**[7:00]** close. Just a just a quick example. You

**[7:02]** can write skills for marketing, for

**[7:03]** customer service, for success, literally

**[7:05]** anything that you think the LM can do

**[7:07]** more than once. All of those engineering

**[7:08]** tasks, those are skills, too. Skills are

**[7:10]** super flexible, and actually what I

**[7:12]** find, once people get the idea of

**[7:13]** skills, the biggest issue is that people

**[7:15]** write so many skills, it's hard to keep

**[7:17]** track of them. And yes, there are tricks

**[7:19]** for that, too. I would encourage you to

**[7:21]** think about how you divide and conquer

**[7:24]** with your skills, right? Think about

**[7:26]** your skills as essentially having a

**[7:29]** power law relationship, which is a fancy

**[7:31]** way of saying that 20% of your skills

**[7:33]** are going to be worth 80% of the value,

**[7:35]** and you have to find the right 20% that

**[7:37]** are going to be repeated often,

**[7:39]** constantly, with high sensitivity to

**[7:41]** what goes right or what goes wrong and

**[7:42]** just jump in. So, that's a little tidbit

**[7:45]** on skills and now let's jump right into

**[7:47]** it to plugins, which is the next thing.

**[7:48]** So, if a skill is a way to do a thing

**[7:51]** consistently, a plugin is a bigger

**[7:54]** package around that. So, we've gone from

**[7:55]** prompts to skills, now we're at plugins.

**[7:57]** A plugin can include skills, but it can

**[7:59]** also include app integrations, MCP

**[8:01]** servers, hooks, assets, commands,

**[8:03]** metadata. It basically takes a whole

**[8:05]** workflow and gives it a name and sort of

**[8:08]** wraps around it and makes it

**[8:10]** installable. And so, if you want to add

**[8:12]** like an entire workflow in one go and

**[8:15]** it's much bigger than a skill, that is a

**[8:17]** plugin. And what's beautiful about it is

**[8:19]** that plugins are extremely shareable. A

**[8:21]** plugin is something that your team can

**[8:23]** use without everyone manually

**[8:25]** reconstructing the setup. In my outbound

**[8:27]** email example, let's say you had to have

**[8:29]** a live connector to data to pull from

**[8:31]** Salesforce to pull in the right name and

**[8:33]** the details about the client. Fantastic.

**[8:35]** That is something that would work in a

**[8:38]** plugin that would not work in a skill.

**[8:40]** So, a skill says, "Here is how to do the

**[8:42]** work." A plugin says, "Here is the

**[8:45]** workflow package that you can install

**[8:48]** and all of it will just get magically

**[8:50]** done for you." And then everything that

**[8:52]** you need to get that whole workflow is

**[8:54]** completely accomplished in that one

**[8:56]** plugin. And so, yeah, there's real work

**[8:58]** that gets done with plugins. It's real

**[9:00]** work to set them up, but once you set

**[9:03]** them up, they're incredibly powerful.

**[9:04]** And this is why real work rarely lives

**[9:08]** entirely in the prompt. It lives other

**[9:10]** places, right? It lives in the

**[9:12]** connectors that we pull in live. So, it

**[9:14]** might pull in from Slack or from Figma,

**[9:16]** from GitHub, from other data sources.

**[9:17]** Real work can live in where we put our

**[9:20]** revisions to so we review them. Real

**[9:23]** work can live in the technical skill

**[9:25]** that we apply as we go through the

**[9:27]** process of doing this work with an AI.

**[9:29]** The thing that we need to get to is we

**[9:31]** need to understand that basically

**[9:33]** everything I'm describing is like

**[9:35]** training wheels that help the LLM

**[9:37]** understand how to do the work that

**[9:39]** matters. And so, the more we're clear

**[9:41]** about that, the easier it becomes to get

**[9:44]** the AI to do that real work. And plugins

**[9:47]** are a fantastic way to wrap up a bunch

**[9:50]** of individual components of work and

**[9:52]** say, "Hey, here's the whole thing in a

**[9:54]** nutshell. It's in a neat little package.

**[9:57]** All you have to do is copy it and get it

**[9:59]** into your app, and then you'll have the

**[10:00]** whole workflow there at your command

**[10:01]** whenever you're ready." And by the way,

**[10:03]** if you think A, AI can't do this, or B,

**[10:05]** it's too hard, I've got news for you. If

**[10:08]** you're any kind of serious AI user, you

**[10:10]** are already doing the plugin work. You

**[10:12]** are literally the human plugin, cuz you

**[10:14]** copy from one app, you paste it into the

**[10:16]** chat, you ask the model to reason, you

**[10:19]** go and get data from somewhere else, you

**[10:20]** check the result, you come back, and it

**[10:22]** goes on and on and on. You are the human

**[10:24]** plugin. If you don't want to be the

**[10:26]** human plugin, consider making an actual

**[10:29]** plugin. And no, you don't have to be an

**[10:30]** engineer to make an actual plugin. Not

**[10:32]** in 2026. You can absolutely do it

**[10:34]** without that. So, we've talked about at

**[10:36]** a high level what skills are, we've

**[10:38]** talked about what prompts are, we've

**[10:40]** talked about what plugins are, and you

**[10:41]** can think of these as three sort of

**[10:42]** different scales, right? Where plugins

**[10:44]** are the biggest. What are MCPs and app

**[10:46]** connectors? This is how an agent gets

**[10:49]** access to the systems where work

**[10:51]** actually lives. So, when you remember

**[10:52]** when I said, "Oh, we'll plugin to

**[10:53]** Salesforce for outbound," that's an MCP.

**[10:55]** That's an app connector. It plugins. It

**[10:58]** figures out where to go to get live data

**[11:01]** and comes back with that real data. And

**[11:03]** most apps are better when they have real

**[11:05]** data. And so, you can think of those

**[11:07]** tools as like internet plugs. They plug

**[11:10]** in and they get data back out, right?

**[11:12]** And I'm old enough to remember when we

**[11:13]** literally had to plug in the internet.

**[11:15]** It wasn't just Wi-Fi anymore. That is

**[11:16]** what you were doing with an MCP. It's

**[11:18]** like a universal plug to the data that

**[11:21]** you can put in, and you can get it back

**[11:23]** out. And yes, you can absolutely build

**[11:24]** an MCP, but increasingly, so many

**[11:27]** different SaaS tools and places where

**[11:30]** work is happening are aggressively

**[11:31]** building their own MCPs and building

**[11:33]** data connectors so you don't have to.

**[11:35]** And one of the reasons I am doing a

**[11:37]** plug-in video is because I think that

**[11:39]** people misunderstand and they think,

**[11:41]** "Well, an MCP connector is just the same

**[11:43]** as a plug-in, right? It's like they're

**[11:45]** all plugging into something." No, and

**[11:47]** the reason why it's confusing is that a

**[11:50]** plug-in can contain an MCP, but a

**[11:53]** plug-in typically has more to it. It is

**[11:55]** not just an MCP server. There's a whole

**[11:58]** piece of workflow that you're tackling

**[12:00]** with that plug-in, which may include a

**[12:01]** call to live data, and then have a bunch

**[12:03]** of other things that you're doing with

**[12:04]** the data along the way. So, a plug-in is

**[12:06]** more more of a larger package. So, we've

**[12:08]** talked about prompts. We've talked about

**[12:10]** prompts versus skills. Prompts and

**[12:12]** skills versus the whole package with the

**[12:14]** plug-in. How the plug-in is different

**[12:16]** from MCP and app connectors. Now, let's

**[12:19]** talk about hooks and scripts. Those are

**[12:21]** big points of confusion. Hooks and

**[12:23]** scripts are for the parts of your

**[12:24]** workflow where you should not rely on

**[12:26]** the model remembering to be careful. So,

**[12:28]** if the code needs formatting, run a

**[12:31]** formatter, right? If the schema needs

**[12:33]** validation, don't ask the model to think

**[12:35]** about it. Actually validate the schema.

**[12:37]** If the tests need to pass, run the test.

**[12:40]** Don't ask the model to imagine running

**[12:42]** the test. It has to actually go and run

**[12:44]** the script and run the test. If a

**[12:46]** generated file needs to meet a

**[12:47]** particular structural contract, like it

**[12:49]** has to be good JSON, actually check it

**[12:51]** and see if it's good JSON with a script.

**[12:53]** If a review should happen before the

**[12:54]** agent stops, build that review into the

**[12:57]** loop. This is one of the most important

**[12:59]** parts of doing good work with agents,

**[13:01]** but it's really misunderstood because

**[13:03]** people think that it's the same thing as

**[13:06]** an MCP connector. It's not. People think

**[13:08]** it should be left to the model's best

**[13:09]** judgment. It should not. Some things

**[13:12]** ought to be deterministic, by which I

**[13:14]** mean some things should not be left to

**[13:16]** the model. A good agent workflow is

**[13:18]** designed so that the parts that are

**[13:19]** deterministic are correctly framed as

**[13:22]** scripts, or correctly framed as hooks

**[13:24]** into services that are deterministic.

**[13:25]** And if that feels really confusing,

**[13:28]** don't let it. Because hooks and scripts

**[13:29]** actually fit right inside our best

**[13:31]** friend, plugins. Think of a plugin as

**[13:33]** like a grab bag present where you've got

**[13:35]** like 10 things in the box for your buddy

**[13:37]** and the plugin is the whole present

**[13:39]** around it. A plugin can contain scripts

**[13:42]** and it can contain hooks into other

**[13:44]** services as a part of the overall

**[13:48]** workflow. It you're not limited to just

**[13:50]** having a prompt in an MCP connector or

**[13:53]** something inside a plugin. A plugin

**[13:55]** package is big enough that it can hold

**[13:57]** the whole workflow to make it reusable.

**[13:59]** And that is why I think the App Store

**[14:01]** analogy is too small. We think of

**[14:03]** plugins as oh, they're apps in the App

**[14:05]** Store. No, they're not really. And it's

**[14:08]** not even as simple saying well, now

**[14:09]** Codex has extensions. It's not that

**[14:11]** that's wrong, it just really undersells

**[14:14]** the power of what I am talking about.

**[14:16]** Because if you think of plugins as

**[14:18]** add-ons, you ask well, what can I

**[14:20]** install, right? And I'm going to go

**[14:21]** passively shopping like I do in the App

**[14:22]** Store. If you think of plugins as

**[14:24]** workflow packaging, you're going to ask

**[14:26]** a much sharper question because you're

**[14:28]** going to ask yourself, what part of my

**[14:29]** work has enough repeatable structure

**[14:31]** that the agent should be able to inherit

**[14:33]** it and use it. And maybe that's

**[14:35]** something that my whole team wants to

**[14:36]** use. That's the real question. Think of

**[14:38]** your work as repeatable structures and

**[14:41]** then think of how you build plugins to

**[14:43]** support it and you're going to be in

**[14:44]** much better shape than if you're messing

**[14:46]** around with these individual things. And

**[14:47]** that's one of the secrets in this video,

**[14:49]** right? Don't think of each of these

**[14:52]** things I'm describing and defining as

**[14:54]** like individual battle bots that are all

**[14:56]** in competition with each other to find

**[14:57]** out who's going to be the best and serve

**[14:59]** your AI. That's not how it works. Think

**[15:01]** of these as Lego bricks that taken

**[15:03]** together make something bigger and more

**[15:06]** useful in terms of your workflow. And by

**[15:08]** the way, in that analogy, a plugin is a

**[15:10]** bunch of Legos all built up together

**[15:12]** into a structure. A plugin has lots of

**[15:14]** these components like scripts and hooks

**[15:16]** and connectors all inside it. And so you

**[15:18]** can ask yourself, do I want to have a

**[15:21]** plugin for architecture review? Do I

**[15:23]** want to have a plug-in for how I handle

**[15:25]** marketing documents? Do I have a plug-in

**[15:28]** for how I handle customer service

**[15:30]** requests? Those are all large workflows.

**[15:32]** Some of them are bundles of workflows.

**[15:34]** And part of our job as humans, as we

**[15:36]** start to think about the serious work

**[15:38]** these systems are capable of, is to ask

**[15:41]** ourselves, well, what's the right unit

**[15:43]** of work here? Do I want to make customer

**[15:45]** service in my tiny company one plug-in,

**[15:47]** or is it actually smarter to say, well,

**[15:49]** there's a refund uh plug-in that we're

**[15:50]** going to need to invoke, and there's

**[15:52]** also a plug-in for adding and activating

**[15:54]** customers who somehow aren't activated.

**[15:56]** We'll make that a separate plug-in. And

**[15:58]** then there's a plug-in for making sure

**[16:00]** that customers are able to upgrade when

**[16:02]** they want to, and we'll make that a

**[16:03]** separate plug-in. Totally just examples,

**[16:05]** but you get the idea. Your job is to

**[16:07]** understand the semantic meaning of the

**[16:09]** workflow and to say, this is a good unit

**[16:11]** of work that has a neat edge and

**[16:13]** boundaries around it that we can make

**[16:15]** into a plug-in. That's a great example.

**[16:17]** By the way, here's another secret in

**[16:18]** this video. That's a great example of

**[16:21]** the kind of skill that is worth a lot of

**[16:25]** money these days. Because very few

**[16:27]** people know how to look at a workflow

**[16:29]** and say, here's how I draw edges around

**[16:32]** it. Here's the boundary around this

**[16:33]** workflow. And once I have the boundary

**[16:35]** around this workflow, this is how we

**[16:36]** turn it into a plug-in that I can then

**[16:38]** repeatedly share across the team. That's

**[16:40]** gold. That's an incredible skill to

**[16:42]** have. If you don't know how to explain

**[16:45]** that the work has value in a particular

**[16:48]** bounded space, you're going to always be

**[16:51]** tempted to make a workflow too big and

**[16:54]** too wide and subject to problems, right?

**[16:56]** Cuz in the analogy I gave you on

**[16:58]** customer success, if all of that was one

**[17:00]** plug-in, could it technically work?

**[17:02]** Yeah, maybe if you were a small company

**[17:04]** and you put a ton into the plug-in, is

**[17:06]** it a good idea to do it that way? If no,

**[17:08]** probably not, because a workflow has one

**[17:10]** job, and what I described in my little

**[17:12]** example was three jobs, and probably in

**[17:14]** reality there's like eight jobs. So, no,

**[17:16]** you probably need more than one plug-in

**[17:18]** for customer success at this imaginary

**[17:20]** little company. And that's okay. Once

**[17:22]** you get into the habit of figuring out

**[17:23]** the plug-in, and I've got lots in the

**[17:25]** Substack on that, you can make that

**[17:27]** stuff, right? You can you can stamp out

**[17:28]** plug-ins and actually go to work. If we

**[17:30]** zoom back out, the difference here is

**[17:32]** really significant. Because a generic

**[17:34]** model that doesn't have a plug-in,

**[17:35]** doesn't have scaffolding as I've been

**[17:37]** describing, can say something useful at

**[17:40]** a high level. And maybe if you prompt it

**[17:42]** and repeat your prompts and waste a lot

**[17:43]** of hours, it will be specific to you.

**[17:45]** But only cuz you prompted all the time

**[17:46]** with lots of heavy prompts. But a truly

**[17:48]** scaffolded agent can review all of your

**[17:50]** work according to your standards, use

**[17:52]** the right tools, and do so effectively

**[17:55]** to get real work done, which is like a

**[17:57]** 10x bigger deal. And it's the same

**[17:59]** intelligence. It's it's not different

**[18:01]** LLMs on the inside. This is a great

**[18:03]** example of how we are a big part of the

**[18:06]** answer to making AI smarter. And I don't

**[18:08]** mean that in some dark way they're all

**[18:09]** watching us. I mean in the sense that

**[18:11]** literally, if you want smarter work

**[18:12]** done, you got to do the part to put the

**[18:14]** scaffolding in place. And you can. It is

**[18:17]** not that scary. And part of why I'm

**[18:19]** making this video now is that I really

**[18:20]** do believe, because I have seen story

**[18:23]** after story after story of people who

**[18:25]** build these, that it's not as hard as it

**[18:27]** used to be. In 2025, I couldn't make

**[18:29]** this video. In 2026, I can make this

**[18:31]** video because plug-ins are now something

**[18:33]** where I have literally seen people who

**[18:35]** do not have coding knowledge figure out

**[18:37]** how to build a plug-in to support their

**[18:40]** work. I saw someone do this for

**[18:41]** editorial work, where she needed to have

**[18:43]** a plug-in to help her take a first pass

**[18:46]** at editorial review. And there's a

**[18:48]** specific workflow for that. Here's how

**[18:49]** you read the text. Here's the three

**[18:51]** different ways you read the text. Here's

**[18:52]** the comments that you want to think

**[18:54]** about adding in the places in the text

**[18:56]** that are rough. Did it do all of the

**[18:57]** work for her? No, it did not do all of

**[18:59]** the work for her, because you still need

**[19:00]** a human to have that sort of editorial

**[19:02]** perspective. But did it save her a lot

**[19:04]** of time because it gave her a first pass

**[19:06]** with a review on where the text is

**[19:08]** rough, where the text was incoherent,

**[19:10]** where there are factual inconsistencies,

**[19:12]** in some ways much better than a person?

**[19:13]** Yeah, and it was faster, too. And she

**[19:15]** could totally build that without having

**[19:17]** to go back and re-prompt every time. And

**[19:20]** it was much bigger than a skill because

**[19:21]** it involved actually understanding more

**[19:24]** information sources than just one piece

**[19:26]** of text. And by the way, another great

**[19:28]** example for non-technical folks is

**[19:30]** around design. You can plug into Figma,

**[19:32]** you can plug into your design tool of

**[19:35]** choice, and you can actually pull down a

**[19:37]** bunch of the details of how a current

**[19:40]** design looks, but also how the design

**[19:42]** language looks. And you can start to

**[19:44]** build a workflow that accounts for all

**[19:47]** of that and pops out new work. And if

**[19:49]** you're wondering, does this align to

**[19:51]** sort of how we're starting to think

**[19:52]** about things with Claude design in the

**[19:53]** mix? Absolutely. We are moving to a

**[19:56]** world where the hyperscalers are putting

**[19:58]** in place more and more tools, more and

**[20:00]** more plugins that help you do this work

**[20:02]** effectively. Arguably, Claude design,

**[20:05]** which dropped just a couple of weeks

**[20:07]** ago, is a fancy plugin with a UI for

**[20:10]** Claude for design. It's like the plugin

**[20:13]** was so important, they made it a

**[20:14]** product. That's how much plugins matter.

**[20:16]** And if you think that you can just sit

**[20:18]** around and wait and Claude or ChatGPT

**[20:21]** will eventually launch all of your dream

**[20:23]** plugins, I got I got a bridge to sell

**[20:25]** you. I got news for you. It ain't going

**[20:26]** to work that way. You have got to be in

**[20:28]** a place where you can take proactive

**[20:30]** action and say, "No, I want this plugin

**[20:32]** for this thing. It's not perfect. It's

**[20:34]** not right the way it is now. It's too

**[20:35]** much manual work. I waste too much time

**[20:37]** in custom prompting. My skills aren't

**[20:39]** enough. I want something that has a data

**[20:41]** connector. a script inside there that

**[20:43]** checks and validates and makes sure it

**[20:44]** works. I'm going to have to have a

**[20:46]** little skill as well." That's a plugin,

**[20:48]** people. And you can totally do that. A

**[20:50]** weekly business report is a great

**[20:51]** example, right? Maybe you need

**[20:53]** spreadsheets and Slack contacts and docs

**[20:55]** and dashboards and past reports and

**[20:56]** charts. That's That's a plugin, right? I

**[20:58]** could I could give you a bunch more

**[20:59]** examples. That's the idea. And if you're

**[21:01]** wondering, I do have a ton more

**[21:02]** examples. They're all in the Substack. I

**[21:04]** have a customer brief, uh how you handle

**[21:06]** that with email and CRM, etc. I have a

**[21:08]** hiring readout and how you handle that

**[21:10]** as a plugin. Tons and tons of these. And

**[21:12]** I think it's really important to have

**[21:13]** starters for this because if you see the

**[21:15]** start of a plugin, it's easier to

**[21:17]** customize than if you're just trying to

**[21:19]** go from a blank page and you've never

**[21:21]** done a plugin before. So, that's why I

**[21:22]** made the hook. Ultimately, and I get

**[21:23]** very passionate about this, agentic

**[21:25]** scaffolding must not stay vague. If

**[21:27]** scaffolding just means some engineering

**[21:29]** stuff around the agent to most of us,

**[21:31]** then only engineers can ever participate

**[21:34]** in designing it. That is an old 2022 era

**[21:38]** problem. But now we're in 2026, and if

**[21:40]** the workflow is real, the people who

**[21:42]** understand the work must be the ones who

**[21:44]** put that knowledge in. And I have talked

**[21:46]** to person after person after person who

**[21:48]** comes from a non-technical background

**[21:50]** who figured that out, and they're now

**[21:51]** stamping out work because they know what

**[21:54]** good looks like. I talked to two of them

**[21:56]** this morning, and they're working on

**[21:57]** like complicated retail scale workflows

**[22:01]** because they figured out what works for

**[22:04]** them. They know which sources matter.

**[22:06]** They know when the output is wrong. They

**[22:08]** know which steps are always forgotten.

**[22:09]** That domain knowledge that you have as a

**[22:11]** non-technical person, quote unquote

**[22:13]** non-technical, that's always blurry in

**[22:15]** 2026, that's what matters. And that's

**[22:18]** what you can then leverage to create the

**[22:20]** custom plugins that work for you. And I

**[22:22]** think the issue is the way to encode all

**[22:24]** of this has become more unclear, not

**[22:26]** less, in the last 6 months, right? Like

**[22:28]** do you write a better prompt? Well, now

**[22:29]** we have skills. Is it a skill now? Do I

**[22:32]** ask my engineers to make an MCP? Is it

**[22:34]** an MCP server? I don't know.

**[22:36]** And I have people ask me these questions

**[22:38]** all the time, right? Is it a connector?

**[22:40]** Do we need a connector? No, maybe it is

**[22:41]** a plugin after all. Disambiguate it.

**[22:44]** Understand what each thing does. A

**[22:46]** script helps you to do predictable,

**[22:48]** deterministic things every time. A skill

**[22:50]** helps an LLM to follow a process in a

**[22:53]** way that is clear and that you can share

**[22:55]** across teams and that's consistent. A

**[22:57]** prompt is good for one-off work, and

**[22:59]** yes, it still matters to write good

**[23:01]** prompting. It does. All the work you did

**[23:03]** in 2025 paid off if you worked on your

**[23:05]** prompting. And a plugin is like a bundle

**[23:07]** around a bunch of things, right? It

**[23:08]** includes the script, it includes the

**[23:10]** skill, it includes pieces of the prompt

**[23:12]** that matter and that are reusable. And

**[23:14]** yes, it also includes MCPs and

**[23:16]** connectors because those are connectors

**[23:17]** to live data. This is the mental model I

**[23:20]** wish people had because engineers know

**[23:22]** this stuff, but it's just not getting

**[23:24]** explained to the rest of us. And then

**[23:26]** when an engineer says something like,

**[23:27]** well, this should be a skill and this

**[23:28]** needs an API and you waited 2 weeks to

**[23:30]** have this meeting, right? No, this

**[23:31]** should be a prompt. I've had these

**[23:33]** conversations where engineers basically

**[23:34]** go through and this is the level of

**[23:36]** understanding they have in their heads.

**[23:37]** They never explain it to you and they

**[23:39]** lay all of this out. It should not be a

**[23:41]** mysterious middle layer. There should

**[23:42]** not be a mysterious middle layer between

**[23:44]** the LLM and the work that gets done for

**[23:46]** you. And that is what I want to make

**[23:47]** sure that you have and that is why I

**[23:49]** have laid this video out the way I have

**[23:51]** so that you understand the mental model

**[23:53]** of how this works. And when you're ready

**[23:55]** to go deeper, the Substack is there and

**[23:56]** you can go deeper and actually look at

**[23:58]** all these practical use cases that I'm

**[23:59]** laying out. You can look at a guide that

**[24:01]** gives you a way to build plugins for

**[24:04]** what you want done and gives you starter

**[24:06]** plugins for a bunch of the workflows

**[24:07]** I've talked about and gives you a way to

**[24:09]** audit your workflow and develop a

**[24:10]** plugin. So all of that practical stuff

**[24:11]** is there, but everybody should know the

**[24:13]** mental model and that's why I'm putting

**[24:15]** this here for all of us to see and watch

**[24:17]** and talk about because even CEOs need

**[24:19]** this now. I don't want a CEO saying,

**[24:20]** should it be a skill? Should it be an

**[24:22]** MCP? If your CEO is confused about this

**[24:25]** harness stuff, show them this video,

**[24:27]** right? Because one of the things I get

**[24:28]** really passionate about is that C-suite,

**[24:30]** especially anyone but the CTO, tends to

**[24:32]** be non-technical enough in most

**[24:34]** companies that they don't get this

**[24:36]** stuff. They don't understand that a

**[24:38]** script is a deterministic check and you

**[24:40]** shouldn't just trust the model to check

**[24:42]** itself. And then they get confused and

**[24:44]** they say, why aren't you using AI? And

**[24:45]** you're like, I am using AI. I just want

**[24:47]** a deterministic script at the end. I've

**[24:48]** had that conversation. It's a real

**[24:50]** conversation. You need to give your

**[24:52]** leadership enough context on this stuff

**[24:55]** that they can actually be useful in

**[24:57]** supporting the Oregon AI transformation.

**[24:59]** And that starts with understanding what

**[25:01]** is in the box when it comes to a harness

**[25:02]** so that people don't get confused. When

**[25:04]** we're talking about the difference

**[25:05]** between an LLM, even in an agentic LLM

**[25:08]** in Codex or in Claude code, and truly

**[25:11]** useful personalized workflows, we're

**[25:13]** talking about this, right? This

**[25:14]** difference between skills and plugins

**[25:17]** and and connectors and and how they

**[25:19]** matter. Please, please, please, make

**[25:21]** sure that the people who need to see

**[25:23]** this see it in your world so you get the

**[25:25]** support you need. Because I have had to

**[25:27]** have enough conversations with senior

**[25:29]** leadership that I know for a fact most

**[25:31]** organizations, there are very senior

**[25:33]** folks who don't have any clue about

**[25:35]** this. Like none. Zero clue. They don't

**[25:37]** get it. Don't be like that. Share this

**[25:39]** with the people that need that need to

**[25:41]** hear it. Make sure everybody has the

**[25:42]** same mental model. Uh if you do it once,

**[25:44]** it's a prompt. If you do it repeatedly,

**[25:46]** it's a skill. If the workflow needs to

**[25:48]** travel or other people need to install

**[25:50]** it, if it needs tools or assets or

**[25:52]** connectors, guess what? It's a plugin.

**[25:54]** If it needs access to another system,

**[25:55]** it's an MCP or app connector. And yes,

**[25:57]** that live data can come inside a plugin

**[25:59]** and nest inside. It's It's like one

**[26:00]** brick in the larger Lego brick model. If

**[26:02]** the workflow has to be verified, you got

**[26:04]** to add a check. All of that together, if

**[26:06]** you understand that, will prevent you

**[26:09]** from wasting work. Because not

**[26:11]** everything needs to be a plugin. I hope

**[26:13]** you're getting that. I'm not saying

**[26:14]** everything needs to be a plugin. Some

**[26:16]** things should stay prompt. Some things

**[26:18]** ought to sit ought to stay skills,

**[26:19]** right? You don't need extra data. You

**[26:21]** don't need a bunch of other stuff. It

**[26:22]** just ought to say skills. Some things

**[26:24]** should be normal scripts and never touch

**[26:26]** an LLM at all. Some things should stay

**[26:28]** human as I hope you know. The The

**[26:30]** judgment to know what's good or not at

**[26:31]** the end of it is going to be human

**[26:32]** judgment. The goal is not to turn your

**[26:34]** workspace into a gigantic museum of

**[26:37]** plugins you never use. The goal is to

**[26:40]** simply understand the parts of your work

**[26:43]** that are repeated and valuable and

**[26:45]** structured enough to package and figure

**[26:47]** out the right solution so that you can

**[26:50]** do that. It's one of the most powerful

**[26:51]** ways you can do practical AI automation

**[26:53]** today. It's where the leverage is living

**[26:55]** in 2026. And that's why I get so

**[26:57]** passionate about it. I hope you've had

**[26:58]** fun following the story here of how we

**[27:01]** got to plugins from scripts and from

**[27:03]** skills and from prompts. I hope you have

**[27:05]** a clear mental model now and I will see

**[27:08]** you next time. And as always, there's

**[27:09]** more on the Substack there. So, jump in

**[27:10]** if you want to build those today.

**[27:11]** Cheers.
