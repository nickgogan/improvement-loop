# Transcript: The 7 Levels of Using Claude Context Explained in 24 min

**URL:** https://www.youtube.com/watch?v=l5Diqeoffa4
**Segments:** 762
**Channel:** Ben AI
**Duration:** 24:10
**Uploaded:** 2026-04-11

---

## Full Text

AI agents on cloud code, co-work, and codecs can now automate workflows, write code, and run entire business processes autonomously. But no matter how good they get, they'll only get as good as the context you provide them. And the people and the businesses that will get the most out of these tools are the ones with the best context infrastructures. So in this video, I'll explain all seven levels of using context in cloud, from chat to projects to a second brain to a full business OS. Show you what changes at each level, why it matters, and how to transition. and I'll show you how I set up the final level, a full business agentic OS with shared context and skills across my team with permission settings. Now, before explaining the levels, let me quickly explain why understanding this context infrastructure is key. As said, we're all seeing these AI agents becoming more capable by the day and with fast developments in MCPs, connectors, browser use, they're starting to become really good at using our softwares and the internet. and with skills, plugins, sub agents, uh, schedule tasks, and other developments, they're getting the capabilities to actually start executing work for us more and more autonomously. But in order for all of this to actually be useful for us or our business, agents need lots of context um, to actually know how to do work for us. And that's why context is the fundamental layer to get right in the upcoming months. I can tell you from my experience that having this context layer set up well has made a huge impact on how I and my business work together with AI and is allowing us to make co-work and cloud code become more and more of our primary operating system. But it is a topic that is not straightforward and requires some effort uh and takes some time to develop. But the earlier you start with this the better because the context compounds. So if you start the day your agents will be far more useful for you and your business in a couple of weeks or months. Now, I'll explain all the levels of using context from simple chat context all the way to an entire shared context infrastructure across a business and show you exactly how to level up no matter what level you are uh at right now. You can also jump to the level that's most relevant to you. But even if you're a bit more advanced, I think this breakdown will hopefully help you wrap your head around it a bit better. Now level one is where unfortunately most people in the world are still stuck which is by providing context to a language model in each chat manually or even worse not providing models with any context at all. Again no matter how good these models get if you don't give AI context using AI usually becomes a frustrating experience. If I give a prompt like write me a LinkedIn post on why setting up a context infrastructure is the key to making AI agents useful. I get a very generic piece of content with m dashes that screams AI. Now, of course, most people know this and have figured out that you need to provide some context to actually get good outputs. But what context do you give it? This of course depends on the specific task. But an easy way you can think about what context you need to provide to get better outputs on most types of tasks are first giving context around who you are and what your business does. Second, context around who this is for like your ICP, your customer or the recipient. Third, which is probably most important, which is showing AI what good looks like for this task. for example, through examples, references or descriptions. And lastly, defining what the roles and guardrails are for this task. So, if I give that same prompt, but with that context, we instantly get a far better response. No am dashes, formatted like a LinkedIn post, more my tone of voice, and more relevant to my ICP and an aligned call to action. But of course, the limitation here is that it's extremely inefficient, timeconuming to copy and paste or rewrite context in each new chat. Which brings us to level two, which is cloud chat projects. Again, most people have figured this out, but projects in cloud chat were of course developed to solve the copying and pasting and rewriting of context problem. In a project in cloud chat, we can just add the context files once together with a system prompt here. We can also add a broader scope of context. And each time you want to write a new LinkedIn post or do a repetitive task, we can just give a simple prompt here while still getting good output. But the downsides of these projects are that first they live in isolated chat windows. So we have to hop between different projects for all our different tasks. Second, clot can't actually create, update or edit any of these context files or the instructions itself. So anytime you want to adjust the process, update a context doc or anything else. We need to manually update it inside of the cloud project. Thirdly, these chat projects are usually limited to a specific task and work best when I have separated projects for each task. I'd need to set up a separate project for YouTube packaging, YouTube intro writing and ideation because I'll follow a different process and have some different context files. And lastly, it's hard to actually test and improve these projects without you extensively using it and updating it manually. Which brings us to the next level, skills, which instantly resolve all of these limitations and why I highly encourage you to start using co-work or cloud code if you're still in level two and working in a cloud chat. Because for skills, we need to make this transition. skills are very comparable to these projects. We have the skill MD this and this is essentially the instruction or the system prompt just like in projects laying out the process and when to use the different context files. For example, here I have my LinkedIn writer skill that includes a skill MD that lays out the process it should follow and when to read the context files and inside the skill we have a references folder with all the different context files. But skills in contrast to projects can be used in any chat at any moment you want. This means for example that mid conversation here in a YouTube ideation chat I had I can turn a good insight into a LinkedIn post instantly by just telling claude write a LinkedIn post based on the topic we discussed using the LinkedIn writer skill and he went ahead followed the SOP and wrote me a LinkedIn post. Skills are also far easier to build than projects. With Enthropics built-in skill creator skill, we can build them by simply telling Claude to build us a skill. For example, help me build an infographic skill. We can also build them out of any conversation you had with Claude by just clicking here and select turn into skill or by just telling Claude in the chat, make me a skill based on the process we followed in this chat. We can also easily share these skills with our team through zip files by just asking clot, can you create a zip file out of the LinkedIn writer skill which anyone in your team can upload by going to customize skills and clicking on the plus icon here and create skills upload skill. Or if you're on a team plan in co-work specifically, you can just add them to your organizational skills. We can also easily adapt Enthropics built-in skills, for example, these by just telling CLA you want to customize them or clicking here on edit. And we can easily import skills from other people and businesses by just going here to browse plugins and then going to entropics and partner. There are also dozens of skill marketplaces around the internet. And with built-in evals, we can immediately test our skills and improve them fast to make sure they actually work and give us good outputs consistently. For example, here I created a newsletter writer skill and then just told Claude, "Please test this skill." The criteria for the test are, "Is this skill functional? Is the word count similar to my newsletter examples? Is the sentence structure similar? and is my tone of voice similar? It then ran pre-ests in parallel and gives me an eval report with a summary of the results and suggested fixes which you can apply immediately. You can even autonomously let them improve themselves through an auto research loop which I recently did a video on which I'll make sure to link in the description below too if you haven't seen it yet. So, if you haven't yet, you really want to start building out these skills around your repetitive tasks and processes. We've been building out more than 60 skills across all our business processes, which if you're interested, you can also download and customize for yourself if you check out my AI accelerator in the link in the description. And lastly, skills can also be scheduled, which means we can now trigger them autonomously through Claude, which I'll show you some examples of later in this video. Now, skills are amazing, but skills are best for pre-established processes of work, and much of our day-to-day work isn't actually a pre-established workflow. So, this brings me to the next level, which is using file access together with skills. Because for many, if not most tasks that AI can help us with, it doesn't actually follow a pre-established process or workflow. We have one-off tasks. We have tasks like ideiation, planning, strategy, or using AI for decision-m. And for many of these, we don't necessarily need or want skills. But we do want AI to have more context around you, your business, and your goals. And this is where file access in cloud code or cloud co-work becomes powerful. Because with every new chat we open in cloth coowork or cloth code, I can now give cloth access to a folder on my computer. For example, here I selected a file with relevant YouTube documents. And in that folder, I have some documents about my YouTube strategy, some old transcripts, a hookbank, etc. And if I now just want to ideulate or plan a new video together with Claude, I'll get instantly better outputs because it has context on my strategy, me, my channel, and what's important to me. For example, here I wanted to ideulate on the video I'm recording. And you can see it pulled some data and context like my brand, my ICP, my YouTube voice, and my YouTube strategy in order to give me more relevant ideas to plan out my video. And because it has more context, it even pushes back on some things. Because, for example, now it knows most of my audience is non-technical and I explain something that's too technical. When we start working with file access, we also start working with the cloud MD, which is basically an instruction on how to navigate the folder, which becomes more relevant if the context grows. But I'll cover the cloud MD in more detail later in this video. And if you haven't yet, you really want to start using this file access consistently because you'll be surprised how much more relevant your answers get. And it allows AI to become much more of a strategic sparring partner. And secondly, because it now has access to a file on your computer, it can't just read those files. It can also instantly update the files. You can save new files or assets like presentations, Excel sheets, Google Docs directly into the folder. So any uh update you want to make in a context docu, good outputs you want to save or assets you want to save, cloud can instantly do it. And essentially what this means is the more you start using file access, the more this folder will grow with context naturally. Now, and if you're just starting at this level, I'd highly recommend putting in some effort and setting up some of these important context documents. I've added a free resource also in the link in the description below that's basically a questionnaire where you can go through and I highly recommend taking 30 minutes with a tool like Whisper Flow where you can talk to your computer and you just do a brain dump and by answering all of these questions you can then feed that brain dump into Claude and he'll create these structured context documents that are important to have as an initial start. I've also added in some example reference files so you get an idea of what these look like. in my AI accelerator. We also have a full step-by-step walkthrough on how to set this up efficiently together with best practices and uh unlimited one-on-one life tech help. So, if you want some help, you can also check out um the link in the description below. Now, when you're starting to use this more and more and the context in your folder is growing, it's natural to go into the next level, which is using cloud co-work projects. This can also be done through cloud code. The same principle applies if you use cloud code. and projects on cloud co-work is essentially just a better way to organize your context across different areas of work. Now this is different than a chat projects because chat projects are very task based. Co-work projects can be used on a higher level for areas of work. For example, I have projects here set up for sales analytics, operations, agency clients, community management and YouTube. And projects are essentially the same as file access but in this case we just predefined the file here with the relevant context for this area of work. So now when I want to idate on a new YouTube video, I can just directly go into that YouTube project and the f folder will already be selected. We'll also have all our chats around this area of work organized here below. We still use skills for the repetitive task of course. For example, in this chat when I was planning the video and I got the concept clearer, I used the YouTube intro writer skill to give me some intro ideas and variations according to my framework. We can also see our scheduled task that are relevant for this project. For example, my YouTube ideation skill runs every morning to give me new ideas. But besides this better organization, there's one more added feature to these projects, which are instructions and memory on the project level. And these allow us to add in specific rules and guardrails and specific memory for specific areas of work. For example, my YouTube project, I have a specific memory that it needs to push back during ideiation because I want to have alternative framing and factchecking. And you can make these memories or rules by just telling clot in a chat that it has to memorize this. Now when you're at this level and you really start to use projects skills, schedule tasks more and more and consistently and really start connecting it more and more with your softwares, you'll start using AI more and more as your operating system. And honestly, if you use this infrastructure well, you can already get a lot out of AI for yourself and your business. But when you start to use this more and more and your context and your projects are growing, you'll notice that even with this project infrastructure, the growing context will become harder to manage. You'll have shared context files across multiple projects, across multiple skills, for example, common docs like an ICP doc. And when something needs to be updated, it needs to be updated across all of these different projects and folders and skills separately. So that's where we want to start looking at the next level, which is setting up a second brain or a personal operating system. Now, even when you're planning to roll this out across a business on a companywide level, which will be level seven, I still highly recommend you start with level six. Once you've set it up and it works for yourself, then think about level seven, where you actually start syncing this across your team with permission settings, etc. Now, in this second brain setup, all we do is we just add all of the context and centralize it into one folder. And this becomes very powerful when we have a lot of context because we'll now have persistent up-to-date context around an entire business or life across any chat or AI provider. We can do that by opening that file through cloud code or just doing it with file select in co-work or by setting up one project connected to the personal OS folder. But I can also do this in codeex or any other AI provider that allows for file access. And as I said, we're still doing the same. We're just adding all of that context into one big folder. And this becomes an advantage when you start using AI and context around more and more areas of work in your business or around more departments because when you have a lot of contacts, it's better because we now just have one folder to structure and organize. And this also means that context docs don't have to be updated across multiple projects or skills. I can have all my projects or business departments inside of the same folder. And this is also the level where we can start to add real-time context by automatically adding your meeting transcripts uh your daily task updates or analytics through scheduled tasks. This schedule task for example automatically updates my second brain with all of the uh meeting transcripts across my team every day by using Firefly connector. I also have a schedule task here for team task roll up which checks every day what my team has been working on and updates that to the second brain. You can also do this for analytics. And then I can also do things like a morning brief where it pulls context from my second brain, knows my priorities, knows our to-do list across the business and gives me an overview of what's important today. With this setup, it also allows us to build better skills and build them faster because through this setup, we already have in-depth context around our business, which we can refer the skill to. So all we need to do is lay out SOPs or workflows and link them to which files in the second brain it needs to read to get more context. So in this setup, I highly recommend starting to build your skills a little bit differently. So instead of adding context docks into the reference files inside of the skill, you actually want to make the skill reference where it can find the reference files in your second brain. For example, as you can see, I did in this one, it only has a skill MD with references to where it can find the different reference files to do its job better. And this means when I make an update on my ICP document, all my skills that refer to that file are instantly updated to. You can do this by just telling cloud I want to adapt the intro scale. I want you to add the reference files to the ben iOS and make the scale reference the files instead of having them in the reference files inside the scale. Now a couple of things become important at this level. Firstly the setup and the file structure are important to get right because of course you're managing a large amount of context. Now that's why I highly recommend you use Obsidian which is basically a free tool that helps you visualize a folder on your computer with some extra benefits. You can download Obsidian for free by just going to their website. But it's important to understand that Obsidian is not a cloud-based software. It's just a tool that helps you visualize, organize, and structure a folder on your computer in a better way. As you can see here, because of course trying to do that inside of the actual folder with a growing context like this, it becomes hard to do. We also get a nice graph view here to see all the relations and connections between all of our context files. And then for this file structure here, it is a nuance topic. There are some best practices, but it will depend on your unique situation, your business, and your way of doing work. Now, I recently did a full tutorial where I show initial file structure that I've seen work well for most businesses or solopreneurs, which I'll add in the link in the description below, too, together with a plug-in that we've develop developed that you can install in cloud code or cloud co-work that walks you through setting up this initial file structure with the context for yourself. Now, that plugin you can download and use together with all our other plugins and skills we're building out internally in my AI accelerator in the first link in the description below. You also have more in-depth step-by-step guides on helping you set up this OS and one-on-one uh live help and multiple Q&As every week. So, if that's interesting, you can check it out in the first link in the description. But you can definitely set this up yourself. I think my last video will help you a lot wrap your head around the file structure. And it's also important to understand that the file structure and the context will grow naturally and fall into place more and more uh the more you use this. So the important thing is to just get started. Now secondly uh your cloud MD becomes a much more important to optimize at this level together with potential index files. Now what is the cloud MD? The cloud MD is essentially an instruction layer between your agent and the Obsidian vault or your OS folder. And it basically makes sure cloud knows where to pull context from in a situation and where to update it. So it's just routing it to the right place which you can imagine becomes a lot more important when the context grows. So you can see here in this chat in coowwork where I give it access to my OS folder. It has an instructions document or the clock MD here. And this basically lays out how to use and navigate the folder. instructions on what to do at the start of every conversation, how to route between knowledge with information on how the folder is structured, information on Obsidian syntax, how to add wiki links, and rules on how to use context inside of this folder. Now, again, even the Cloud MD will naturally evolve and get better the more you use it. And Clot can create the initial version itself. Our plug-in will also help you with a cloud MD instruction that worked well for us. And then Andre Karpathy, one of the leading AI researchers, recently added a new layer to this too where if your context grows even more, you can start using index files in each of the subfolders. So your agent understands better how to navigate each of the separate subfolders. For example, you can see on the shared context file, I have another cloud MD, which in this case we just called cloud MD, but it could also be called an index file with more information on how this specific subfolder is structured, which cloth can read to know how to navigate this folder. And we have another one here for each of the subfolders. Again, this is something you want to start thinking about when context is growing. And Cloud can help you out with building uh these documents, of course. Now, thirdly, what's going to be important is you probably need some of these scheduled tasks to make sure your second brain is up to date, just like I showed you with the meeting transcripts, but we can also do this for your daily analytics, task lists, your CRM pipeline, whatever is relevant to you. And fourthly, uh which is an important one, uh is there is a maintenance aspect to this. I'd highly suggest going through your files on a weekly basis to make sure things are going right. Are there no duplicates? Are the documents put in the right place? Are there any conflicts in the context? And you do want to dedicate some time to this, especially at the beginning because it will take time to get this right. And lastly, you will need to start using this cons consistently. The only way this is going to work for you is when you use it a lot because the more you use it, the better it will get. And there is some learning curve attached to this. I can tell you I'm definitely not there yet, but it is getting better and better and it's making a big impact on the relevancy of my AI outputs across me and my team's chats. But it does take time to figure out what file structure makes sense for you and to test its capabilities. Generally, I try to approach this with a mindset of trying to let AI clock code or clockwork or wherever you use AI become your main operating system for work because if you do that, you'll slowly but surely fill in the gaps to actually make it become your main operating system. And this is where we're heading anyway. So you might as well be early. Now if you want to take it to the last level, which is going to be a game changer for anyone who runs a business, is to actually roll this out and sync this entire context data set and the skills across the entire team. So all of your team members, AI agents instantly become far more powerful for your business. Now, when rolling this out for teams, a few things of course become important. First, the file structure will probably have to change a bit, and you'll need some more files for using this across a team. For example, in my business OS, you can see I have a few more folders like my departments, my team and their roles and plugins and skills so they can be easily shared across the team. Again, if you want to learn more about the file structure, I covered it in full in that last video which will be in the link in the description below. Now, for your team members to get to this initial setup, you can of course just share a zip file with them uh of the entire context doc so they can install it. And then second of course when you want to share this across the team updates need to actually be synced across the team and ideally in real time. Now we've explored multiple options of doing this and because of course they are local files it's not extremely straightforward to do but for syncing across a team uh you have multiple options. First you can use GitHub. Second you can use Obsidian sync which is a feature of Obsidian. Third you can even uh launch a self-hosted solution to do this. But the best option we found which we're currently using is a plugin inside of Obsidian called Relay. Now this is a community plugin inside of Obsidian which you can find here by going to settings, clicking on community plugins, go to browse, type in relay and from there you can install it. Once you've installed it, it'll be listed under your community plugins. And through relay now I can decide for each of the folder to which of my team members these updates need to be synced to. And through this any change anyone in my team makes in any of these contact stocks will it will automatically be synced and updated across anyone in the team in real time. And you can use relay uh for up to three people uh for free. But with this setup of course uh permission settings become important too. Not every team member should be able to update every file or not even uh every team member should be able to see or access any file. So you as a business owner of course need to control some of these permission settings. Now, unfortunately, this is not very straightforward to do on Relay yet. We actually talked to the founder of Relay and this feature is in their pipeline. But in the meantime, we've built our own version or custom setup on top of this relay plugin that actually gives us these permission settings. And see that we have installed here our Beni relay plugin, which is just our version of this app with permission settings. And now, for example, I can still make updates in this general context folder uh with the important documents, route, strategy, etc. But my uh team members only get read access. So they can still use these documents but they can't actually update them. This is what one of my team members would see a little lock with this is a readonly file. Now this setup is a little bit more technical. Um so if you want to set this up we have full guides together with all the other guides on how to sync across team members with GitHub and other ways. So if that's interesting to you and you want access to our customized plug-in again you could check out the AI accelerator. And then lastly, of course, once you have set this up, it is key to have one person in the business really be the operator and the manager of this context layer because it does require maintenance. It requires effort to actually keep this updated and well functioning across the business and this is going to take some time. So someone needs to be responsible. Now again, I think syncing and permission settings become a lot easier very soon because there are a lot of businesses trying to figure this out and there will be more of an infrastructure around this very soon. Um, but this is the way you can do it right now. Now, that's it for this video. Thank you so much for watching. Again, if you want more step-by-step guidance on setting this up for yourself, uh, multiple weekly Q&As and unlimited one-on-one live tech help, you can check out my AI accelerator in the link in the description below. Thank you so much for watching. If you got any value out of it, I highly appreciate a like and a subscribe. It really does help me. And if you want to learn more about cloth co-work and obsidian setup, you can check out the video here above.

---

## Timestamped Segments

**[0:00]** AI agents on cloud code, co-work, and

**[0:02]** codecs can now automate workflows, write

**[0:04]** code, and run entire business processes

**[0:06]** autonomously. But no matter how good

**[0:08]** they get, they'll only get as good as

**[0:09]** the context you provide them. And the

**[0:11]** people and the businesses that will get

**[0:12]** the most out of these tools are the ones

**[0:14]** with the best context infrastructures.

**[0:16]** So in this video, I'll explain all seven

**[0:18]** levels of using context in cloud, from

**[0:20]** chat to projects to a second brain to a

**[0:22]** full business OS. Show you what changes

**[0:25]** at each level, why it matters, and how

**[0:27]** to transition. and I'll show you how I

**[0:28]** set up the final level, a full business

**[0:31]** agentic OS with shared context and

**[0:33]** skills across my team with permission

**[0:35]** settings. Now, before explaining the

**[0:37]** levels, let me quickly explain why

**[0:38]** understanding this context

**[0:40]** infrastructure is key. As said, we're

**[0:42]** all seeing these AI agents becoming more

**[0:44]** capable by the day and with fast

**[0:45]** developments in MCPs, connectors,

**[0:48]** browser use, they're starting to become

**[0:50]** really good at using our softwares and

**[0:51]** the internet. and with skills, plugins,

**[0:53]** sub agents, uh, schedule tasks, and

**[0:56]** other developments, they're getting the

**[0:57]** capabilities to actually start executing

**[0:59]** work for us more and more autonomously.

**[1:01]** But in order for all of this to actually

**[1:03]** be useful for us or our business, agents

**[1:06]** need lots of context um, to actually

**[1:08]** know how to do work for us. And that's

**[1:10]** why context is the fundamental layer to

**[1:13]** get right in the upcoming months. I can

**[1:14]** tell you from my experience that having

**[1:16]** this context layer set up well has made

**[1:18]** a huge impact on how I and my business

**[1:20]** work together with AI and is allowing us

**[1:22]** to make co-work and cloud code become

**[1:24]** more and more of our primary operating

**[1:26]** system. But it is a topic that is not

**[1:28]** straightforward and requires some effort

**[1:30]** uh and takes some time to develop. But

**[1:31]** the earlier you start with this the

**[1:33]** better because the context compounds. So

**[1:35]** if you start the day your agents will be

**[1:37]** far more useful for you and your

**[1:39]** business in a couple of weeks or months.

**[1:40]** Now, I'll explain all the levels of

**[1:42]** using context from simple chat context

**[1:45]** all the way to an entire shared context

**[1:47]** infrastructure across a business and

**[1:49]** show you exactly how to level up no

**[1:50]** matter what level you are uh at right

**[1:52]** now. You can also jump to the level

**[1:54]** that's most relevant to you. But even if

**[1:55]** you're a bit more advanced, I think this

**[1:57]** breakdown will hopefully help you wrap

**[1:58]** your head around it a bit better. Now

**[2:00]** level one is where unfortunately most

**[2:02]** people in the world are still stuck

**[2:03]** which is by providing context to a

**[2:05]** language model in each chat manually or

**[2:08]** even worse not providing models with any

**[2:10]** context at all. Again no matter how good

**[2:12]** these models get if you don't give AI

**[2:14]** context using AI usually becomes a

**[2:16]** frustrating experience. If I give a

**[2:17]** prompt like write me a LinkedIn post on

**[2:19]** why setting up a context infrastructure

**[2:20]** is the key to making AI agents useful. I

**[2:23]** get a very generic piece of content with

**[2:25]** m dashes that screams AI. Now, of

**[2:27]** course, most people know this and have

**[2:29]** figured out that you need to provide

**[2:30]** some context to actually get good

**[2:31]** outputs. But what context do you give

**[2:33]** it? This of course depends on the

**[2:35]** specific task. But an easy way you can

**[2:37]** think about what context you need to

**[2:38]** provide to get better outputs on most

**[2:40]** types of tasks are first giving context

**[2:43]** around who you are and what your

**[2:44]** business does. Second, context around

**[2:47]** who this is for like your ICP, your

**[2:49]** customer or the recipient. Third, which

**[2:51]** is probably most important, which is

**[2:53]** showing AI what good looks like for this

**[2:56]** task. for example, through examples,

**[2:57]** references or descriptions. And lastly,

**[3:00]** defining what the roles and guardrails

**[3:02]** are for this task. So, if I give that

**[3:03]** same prompt, but with that context, we

**[3:06]** instantly get a far better response. No

**[3:08]** am dashes, formatted like a LinkedIn

**[3:11]** post, more my tone of voice, and more

**[3:13]** relevant to my ICP and an aligned call

**[3:15]** to action. But of course, the limitation

**[3:17]** here is that it's extremely inefficient,

**[3:19]** timeconuming to copy and paste or

**[3:20]** rewrite context in each new chat. Which

**[3:23]** brings us to level two, which is cloud

**[3:25]** chat projects. Again, most people have

**[3:27]** figured this out, but projects in cloud

**[3:29]** chat were of course developed to solve

**[3:31]** the copying and pasting and rewriting of

**[3:33]** context problem. In a project in cloud

**[3:36]** chat, we can just add the context files

**[3:38]** once together with a system prompt here.

**[3:40]** We can also add a broader scope of

**[3:42]** context. And each time you want to write

**[3:44]** a new LinkedIn post or do a repetitive

**[3:46]** task, we can just give a simple prompt

**[3:48]** here while still getting good output.

**[3:50]** But the downsides of these projects are

**[3:52]** that first they live in isolated chat

**[3:54]** windows. So we have to hop between

**[3:56]** different projects for all our different

**[3:57]** tasks. Second, clot can't actually

**[4:00]** create, update or edit any of these

**[4:02]** context files or the instructions

**[4:04]** itself. So anytime you want to adjust

**[4:06]** the process, update a context doc or

**[4:08]** anything else. We need to manually

**[4:09]** update it inside of the cloud project.

**[4:11]** Thirdly, these chat projects are usually

**[4:13]** limited to a specific task and work best

**[4:15]** when I have separated projects for each

**[4:17]** task. I'd need to set up a separate

**[4:19]** project for YouTube packaging, YouTube

**[4:21]** intro writing and ideation because I'll

**[4:23]** follow a different process and have some

**[4:25]** different context files. And lastly,

**[4:27]** it's hard to actually test and improve

**[4:29]** these projects without you extensively

**[4:31]** using it and updating it manually. Which

**[4:33]** brings us to the next level, skills,

**[4:35]** which instantly resolve all of these

**[4:37]** limitations and why I highly encourage

**[4:39]** you to start using co-work or cloud code

**[4:41]** if you're still in level two and working

**[4:43]** in a cloud chat. Because for skills, we

**[4:45]** need to make this transition. skills are

**[4:47]** very comparable to these projects. We

**[4:49]** have the skill MD this and this is

**[4:51]** essentially the instruction or the

**[4:52]** system prompt just like in projects

**[4:55]** laying out the process and when to use

**[4:57]** the different context files. For

**[4:58]** example, here I have my LinkedIn writer

**[5:00]** skill that includes a skill MD that lays

**[5:03]** out the process it should follow and

**[5:05]** when to read the context files and

**[5:08]** inside the skill we have a references

**[5:10]** folder with all the different context

**[5:12]** files. But skills in contrast to

**[5:14]** projects can be used in any chat at any

**[5:16]** moment you want. This means for example

**[5:18]** that mid conversation here in a YouTube

**[5:20]** ideation chat I had I can turn a good

**[5:23]** insight into a LinkedIn post instantly

**[5:25]** by just telling claude write a LinkedIn

**[5:27]** post based on the topic we discussed

**[5:29]** using the LinkedIn writer skill and he

**[5:31]** went ahead followed the SOP and wrote me

**[5:33]** a LinkedIn post. Skills are also far

**[5:35]** easier to build than projects. With

**[5:37]** Enthropics built-in skill creator skill,

**[5:40]** we can build them by simply telling

**[5:41]** Claude to build us a skill. For example,

**[5:44]** help me build an infographic skill. We

**[5:46]** can also build them out of any

**[5:47]** conversation you had with Claude by just

**[5:49]** clicking here and select turn into skill

**[5:52]** or by just telling Claude in the chat,

**[5:54]** make me a skill based on the process we

**[5:56]** followed in this chat. We can also

**[5:57]** easily share these skills with our team

**[5:59]** through zip files by just asking clot,

**[6:01]** can you create a zip file out of the

**[6:02]** LinkedIn writer skill which anyone in

**[6:04]** your team can upload by going to

**[6:06]** customize skills and clicking on the

**[6:08]** plus icon here and create skills upload

**[6:11]** skill. Or if you're on a team plan in

**[6:13]** co-work specifically, you can just add

**[6:15]** them to your organizational skills. We

**[6:17]** can also easily adapt Enthropics

**[6:19]** built-in skills, for example, these by

**[6:21]** just telling CLA you want to customize

**[6:22]** them or clicking here on edit. And we

**[6:24]** can easily import skills from other

**[6:26]** people and businesses by just going here

**[6:28]** to browse plugins and then going to

**[6:29]** entropics and partner. There are also

**[6:31]** dozens of skill marketplaces around the

**[6:33]** internet. And with built-in evals, we

**[6:36]** can immediately test our skills and

**[6:37]** improve them fast to make sure they

**[6:39]** actually work and give us good outputs

**[6:41]** consistently. For example, here I

**[6:42]** created a newsletter writer skill and

**[6:44]** then just told Claude, "Please test this

**[6:46]** skill." The criteria for the test are,

**[6:48]** "Is this skill functional? Is the word

**[6:50]** count similar to my newsletter examples?

**[6:51]** Is the sentence structure similar? and

**[6:53]** is my tone of voice similar? It then ran

**[6:55]** pre-ests in parallel and gives me an

**[6:57]** eval report with a summary of the

**[6:59]** results and suggested fixes which you

**[7:01]** can apply immediately. You can even

**[7:03]** autonomously let them improve themselves

**[7:05]** through an auto research loop which I

**[7:07]** recently did a video on which I'll make

**[7:09]** sure to link in the description below

**[7:10]** too if you haven't seen it yet. So, if

**[7:12]** you haven't yet, you really want to

**[7:13]** start building out these skills around

**[7:14]** your repetitive tasks and processes.

**[7:16]** We've been building out more than 60

**[7:18]** skills across all our business

**[7:19]** processes, which if you're interested,

**[7:21]** you can also download and customize for

**[7:23]** yourself if you check out my AI

**[7:25]** accelerator in the link in the

**[7:26]** description. And lastly, skills can also

**[7:28]** be scheduled, which means we can now

**[7:29]** trigger them autonomously through

**[7:31]** Claude, which I'll show you some

**[7:32]** examples of later in this video. Now,

**[7:33]** skills are amazing, but skills are best

**[7:35]** for pre-established processes of work,

**[7:37]** and much of our day-to-day work isn't

**[7:39]** actually a pre-established workflow. So,

**[7:41]** this brings me to the next level, which

**[7:43]** is using file access together with

**[7:45]** skills. Because for many, if not most

**[7:47]** tasks that AI can help us with, it

**[7:49]** doesn't actually follow a

**[7:50]** pre-established process or workflow. We

**[7:52]** have one-off tasks. We have tasks like

**[7:54]** ideiation, planning, strategy, or using

**[7:57]** AI for decision-m. And for many of

**[7:59]** these, we don't necessarily need or want

**[8:01]** skills. But we do want AI to have more

**[8:04]** context around you, your business, and

**[8:06]** your goals. And this is where file

**[8:08]** access in cloud code or cloud co-work

**[8:10]** becomes powerful. Because with every new

**[8:12]** chat we open in cloth coowork or cloth

**[8:13]** code, I can now give cloth access to a

**[8:15]** folder on my computer. For example, here

**[8:17]** I selected a file with relevant YouTube

**[8:19]** documents. And in that folder, I have

**[8:21]** some documents about my YouTube

**[8:22]** strategy, some old transcripts, a

**[8:24]** hookbank, etc. And if I now just want to

**[8:27]** ideulate or plan a new video together

**[8:29]** with Claude, I'll get instantly better

**[8:31]** outputs because it has context on my

**[8:32]** strategy, me, my channel, and what's

**[8:34]** important to me. For example, here I

**[8:36]** wanted to ideulate on the video I'm

**[8:38]** recording. And you can see it pulled

**[8:39]** some data and context like my brand, my

**[8:42]** ICP, my YouTube voice, and my YouTube

**[8:44]** strategy in order to give me more

**[8:46]** relevant ideas to plan out my video. And

**[8:48]** because it has more context, it even

**[8:49]** pushes back on some things. Because, for

**[8:51]** example, now it knows most of my

**[8:53]** audience is non-technical and I explain

**[8:55]** something that's too technical. When we

**[8:57]** start working with file access, we also

**[8:58]** start working with the cloud MD, which

**[9:00]** is basically an instruction on how to

**[9:02]** navigate the folder, which becomes more

**[9:03]** relevant if the context grows. But I'll

**[9:06]** cover the cloud MD in more detail later

**[9:07]** in this video. And if you haven't yet,

**[9:09]** you really want to start using this file

**[9:11]** access consistently because you'll be

**[9:12]** surprised how much more relevant your

**[9:14]** answers get. And it allows AI to become

**[9:17]** much more of a strategic sparring

**[9:18]** partner. And secondly, because it now

**[9:20]** has access to a file on your computer,

**[9:21]** it can't just read those files. It can

**[9:23]** also instantly update the files. You can

**[9:25]** save new files or assets like

**[9:27]** presentations, Excel sheets, Google Docs

**[9:29]** directly into the folder. So any uh

**[9:32]** update you want to make in a context

**[9:34]** docu, good outputs you want to save or

**[9:36]** assets you want to save, cloud can

**[9:38]** instantly do it. And essentially what

**[9:39]** this means is the more you start using

**[9:41]** file access, the more this folder will

**[9:43]** grow with context naturally. Now, and if

**[9:45]** you're just starting at this level, I'd

**[9:46]** highly recommend putting in some effort

**[9:48]** and setting up some of these important

**[9:49]** context documents. I've added a free

**[9:51]** resource also in the link in the

**[9:52]** description below that's basically a

**[9:54]** questionnaire where you can go through

**[9:55]** and I highly recommend taking 30 minutes

**[9:58]** with a tool like Whisper Flow where you

**[9:59]** can talk to your computer and you just

**[10:01]** do a brain dump and by answering all of

**[10:03]** these questions you can then feed that

**[10:04]** brain dump into Claude and he'll create

**[10:07]** these structured context documents that

**[10:09]** are important to have as an initial

**[10:10]** start. I've also added in some example

**[10:13]** reference files so you get an idea of

**[10:14]** what these look like. in my AI

**[10:15]** accelerator. We also have a full

**[10:17]** step-by-step walkthrough on how to set

**[10:18]** this up efficiently together with best

**[10:20]** practices and uh unlimited one-on-one

**[10:22]** life tech help. So, if you want some

**[10:24]** help, you can also check out um the link

**[10:25]** in the description below. Now, when

**[10:26]** you're starting to use this more and

**[10:28]** more and the context in your folder is

**[10:29]** growing, it's natural to go into the

**[10:31]** next level, which is using cloud co-work

**[10:33]** projects. This can also be done through

**[10:35]** cloud code. The same principle applies

**[10:37]** if you use cloud code. and projects on

**[10:39]** cloud co-work is essentially just a

**[10:41]** better way to organize your context

**[10:43]** across different areas of work. Now this

**[10:45]** is different than a chat projects

**[10:47]** because chat projects are very task

**[10:48]** based. Co-work projects can be used on a

**[10:50]** higher level for areas of work. For

**[10:53]** example, I have projects here set up for

**[10:55]** sales analytics, operations, agency

**[10:57]** clients, community management and

**[10:58]** YouTube. And projects are essentially

**[11:00]** the same as file access but in this case

**[11:03]** we just predefined the file here with

**[11:05]** the relevant context for this area of

**[11:07]** work. So now when I want to idate on a

**[11:09]** new YouTube video, I can just directly

**[11:10]** go into that YouTube project and the f

**[11:12]** folder will already be selected. We'll

**[11:14]** also have all our chats around this area

**[11:16]** of work organized here below. We still

**[11:18]** use skills for the repetitive task of

**[11:20]** course. For example, in this chat when I

**[11:22]** was planning the video and I got the

**[11:23]** concept clearer, I used the YouTube

**[11:25]** intro writer skill to give me some intro

**[11:27]** ideas and variations according to my

**[11:29]** framework. We can also see our scheduled

**[11:31]** task that are relevant for this project.

**[11:33]** For example, my YouTube ideation skill

**[11:35]** runs every morning to give me new ideas.

**[11:38]** But besides this better organization,

**[11:39]** there's one more added feature to these

**[11:41]** projects, which are instructions and

**[11:43]** memory on the project level. And these

**[11:45]** allow us to add in specific rules and

**[11:48]** guardrails and specific memory for

**[11:50]** specific areas of work. For example, my

**[11:52]** YouTube project, I have a specific

**[11:54]** memory that it needs to push back during

**[11:56]** ideiation because I want to have

**[11:58]** alternative framing and factchecking.

**[12:00]** And you can make these memories or rules

**[12:01]** by just telling clot in a chat that it

**[12:03]** has to memorize this. Now when you're at

**[12:05]** this level and you really start to use

**[12:06]** projects skills, schedule tasks more and

**[12:09]** more and consistently and really start

**[12:11]** connecting it more and more with your

**[12:12]** softwares, you'll start using AI more

**[12:14]** and more as your operating system. And

**[12:16]** honestly, if you use this infrastructure

**[12:18]** well, you can already get a lot out of

**[12:19]** AI for yourself and your business. But

**[12:21]** when you start to use this more and more

**[12:23]** and your context and your projects are

**[12:25]** growing, you'll notice that even with

**[12:26]** this project infrastructure, the growing

**[12:28]** context will become harder to manage.

**[12:30]** You'll have shared context files across

**[12:32]** multiple projects, across multiple

**[12:34]** skills, for example, common docs like an

**[12:37]** ICP doc. And when something needs to be

**[12:39]** updated, it needs to be updated across

**[12:41]** all of these different projects and

**[12:42]** folders and skills separately. So that's

**[12:44]** where we want to start looking at the

**[12:46]** next level, which is setting up a second

**[12:48]** brain or a personal operating system.

**[12:50]** Now, even when you're planning to roll

**[12:51]** this out across a business on a

**[12:52]** companywide level, which will be level

**[12:54]** seven, I still highly recommend you

**[12:56]** start with level six. Once you've set it

**[12:58]** up and it works for yourself, then think

**[13:00]** about level seven, where you actually

**[13:01]** start syncing this across your team with

**[13:03]** permission settings, etc. Now, in this

**[13:05]** second brain setup, all we do is we just

**[13:07]** add all of the context and centralize it

**[13:09]** into one folder. And this becomes very

**[13:11]** powerful when we have a lot of context

**[13:13]** because we'll now have persistent

**[13:15]** up-to-date context around an entire

**[13:17]** business or life across any chat or AI

**[13:20]** provider. We can do that by opening that

**[13:22]** file through cloud code or just doing it

**[13:24]** with file select in co-work or by

**[13:26]** setting up one project connected to the

**[13:28]** personal OS folder. But I can also do

**[13:31]** this in codeex or any other AI provider

**[13:33]** that allows for file access. And as I

**[13:35]** said, we're still doing the same. We're

**[13:36]** just adding all of that context into one

**[13:38]** big folder. And this becomes an

**[13:40]** advantage when you start using AI and

**[13:41]** context around more and more areas of

**[13:43]** work in your business or around more

**[13:45]** departments because when you have a lot

**[13:47]** of contacts, it's better because we now

**[13:49]** just have one folder to structure and

**[13:50]** organize. And this also means that

**[13:52]** context docs don't have to be updated

**[13:55]** across multiple projects or skills. I

**[13:57]** can have all my projects or business

**[13:59]** departments inside of the same folder.

**[14:01]** And this is also the level where we can

**[14:02]** start to add real-time context by

**[14:04]** automatically adding your meeting

**[14:05]** transcripts uh your daily task updates

**[14:08]** or analytics through scheduled tasks.

**[14:10]** This schedule task for example

**[14:12]** automatically updates my second brain

**[14:14]** with all of the uh meeting transcripts

**[14:16]** across my team every day by using

**[14:18]** Firefly connector. I also have a

**[14:20]** schedule task here for team task roll up

**[14:23]** which checks every day what my team has

**[14:25]** been working on and updates that to the

**[14:27]** second brain. You can also do this for

**[14:29]** analytics. And then I can also do things

**[14:31]** like a morning brief where it pulls

**[14:33]** context from my second brain, knows my

**[14:36]** priorities, knows our to-do list across

**[14:38]** the business and gives me an overview of

**[14:39]** what's important today. With this setup,

**[14:41]** it also allows us to build better skills

**[14:43]** and build them faster because through

**[14:45]** this setup, we already have in-depth

**[14:47]** context around our business, which we

**[14:48]** can refer the skill to. So all we need

**[14:50]** to do is lay out SOPs or workflows and

**[14:53]** link them to which files in the second

**[14:55]** brain it needs to read to get more

**[14:56]** context. So in this setup, I highly

**[14:58]** recommend starting to build your skills

**[15:00]** a little bit differently. So instead of

**[15:02]** adding context docks into the reference

**[15:04]** files inside of the skill, you actually

**[15:06]** want to make the skill reference where

**[15:08]** it can find the reference files in your

**[15:10]** second brain. For example, as you can

**[15:12]** see, I did in this one, it only has a

**[15:13]** skill MD with references to where it can

**[15:16]** find the different reference files to do

**[15:18]** its job better. And this means when I

**[15:19]** make an update on my ICP document, all

**[15:21]** my skills that refer to that file are

**[15:23]** instantly updated to. You can do this by

**[15:26]** just telling cloud I want to adapt the

**[15:27]** intro scale. I want you to add the

**[15:29]** reference files to the ben iOS and make

**[15:30]** the scale reference the files instead of

**[15:32]** having them in the reference files

**[15:33]** inside the scale. Now a couple of things

**[15:36]** become important at this level. Firstly

**[15:38]** the setup and the file structure are

**[15:40]** important to get right because of course

**[15:42]** you're managing a large amount of

**[15:43]** context. Now that's why I highly

**[15:45]** recommend you use Obsidian which is

**[15:47]** basically a free tool that helps you

**[15:49]** visualize a folder on your computer with

**[15:51]** some extra benefits. You can download

**[15:53]** Obsidian for free by just going to their

**[15:55]** website. But it's important to

**[15:56]** understand that Obsidian is not a

**[15:57]** cloud-based software. It's just a tool

**[15:59]** that helps you visualize, organize, and

**[16:01]** structure a folder on your computer in a

**[16:03]** better way. As you can see here, because

**[16:05]** of course trying to do that inside of

**[16:07]** the actual folder with a growing context

**[16:09]** like this, it becomes hard to do. We

**[16:11]** also get a nice graph view here to see

**[16:13]** all the relations and connections

**[16:15]** between all of our context files. And

**[16:17]** then for this file structure here, it is

**[16:19]** a nuance topic. There are some best

**[16:20]** practices, but it will depend on your

**[16:22]** unique situation, your business, and

**[16:24]** your way of doing work. Now, I recently

**[16:26]** did a full tutorial where I show initial

**[16:28]** file structure that I've seen work well

**[16:30]** for most businesses or solopreneurs,

**[16:32]** which I'll add in the link in the

**[16:34]** description below, too, together with a

**[16:35]** plug-in that we've develop developed

**[16:37]** that you can install in cloud code or

**[16:38]** cloud co-work that walks you through

**[16:40]** setting up this initial file structure

**[16:42]** with the context for yourself. Now, that

**[16:44]** plugin you can download and use together

**[16:46]** with all our other plugins and skills

**[16:48]** we're building out internally in my AI

**[16:49]** accelerator in the first link in the

**[16:50]** description below. You also have more

**[16:52]** in-depth step-by-step guides on helping

**[16:54]** you set up this OS and one-on-one uh

**[16:56]** live help and multiple Q&As every week.

**[16:59]** So, if that's interesting, you can check

**[17:00]** it out in the first link in the

**[17:01]** description. But you can definitely set

**[17:02]** this up yourself. I think my last video

**[17:04]** will help you a lot wrap your head

**[17:05]** around the file structure. And it's also

**[17:07]** important to understand that the file

**[17:08]** structure and the context will grow

**[17:10]** naturally and fall into place more and

**[17:12]** more uh the more you use this. So the

**[17:15]** important thing is to just get started.

**[17:16]** Now secondly uh your cloud MD becomes a

**[17:19]** much more important to optimize at this

**[17:21]** level together with potential index

**[17:23]** files. Now what is the cloud MD? The

**[17:25]** cloud MD is essentially an instruction

**[17:28]** layer between your agent and the

**[17:30]** Obsidian vault or your OS folder. And it

**[17:32]** basically makes sure cloud knows where

**[17:34]** to pull context from in a situation and

**[17:37]** where to update it. So it's just routing

**[17:39]** it to the right place which you can

**[17:41]** imagine becomes a lot more important

**[17:42]** when the context grows. So you can see

**[17:45]** here in this chat in coowwork where I

**[17:46]** give it access to my OS folder. It has

**[17:48]** an instructions document or the clock MD

**[17:50]** here. And this basically lays out how to

**[17:53]** use and navigate the folder.

**[17:56]** instructions on what to do at the start

**[17:58]** of every conversation, how to route

**[18:00]** between knowledge with information on

**[18:02]** how the folder is structured,

**[18:04]** information on Obsidian syntax, how to

**[18:06]** add wiki links, and rules on how to use

**[18:09]** context inside of this folder. Now,

**[18:11]** again, even the Cloud MD will naturally

**[18:13]** evolve and get better the more you use

**[18:15]** it. And Clot can create the initial

**[18:16]** version itself. Our plug-in will also

**[18:18]** help you with a cloud MD instruction

**[18:20]** that worked well for us. And then Andre

**[18:22]** Karpathy, one of the leading AI

**[18:23]** researchers, recently added a new layer

**[18:25]** to this too where if your context grows

**[18:27]** even more, you can start using index

**[18:30]** files in each of the subfolders. So your

**[18:32]** agent understands better how to navigate

**[18:34]** each of the separate subfolders. For

**[18:35]** example, you can see on the shared

**[18:37]** context file, I have another cloud MD,

**[18:39]** which in this case we just called cloud

**[18:40]** MD, but it could also be called an index

**[18:42]** file with more information on how this

**[18:44]** specific subfolder is structured, which

**[18:46]** cloth can read to know how to navigate

**[18:48]** this folder. And we have another one

**[18:49]** here for each of the subfolders. Again,

**[18:51]** this is something you want to start

**[18:52]** thinking about when context is growing.

**[18:54]** And Cloud can help you out with building

**[18:56]** uh these documents, of course. Now,

**[18:58]** thirdly, what's going to be important is

**[18:59]** you probably need some of these

**[19:00]** scheduled tasks to make sure your second

**[19:02]** brain is up to date, just like I showed

**[19:04]** you with the meeting transcripts, but we

**[19:06]** can also do this for your daily

**[19:07]** analytics, task lists, your CRM

**[19:10]** pipeline, whatever is relevant to you.

**[19:12]** And fourthly, uh which is an important

**[19:13]** one, uh is there is a maintenance aspect

**[19:16]** to this. I'd highly suggest going

**[19:17]** through your files on a weekly basis to

**[19:20]** make sure things are going right. Are

**[19:22]** there no duplicates? Are the documents

**[19:23]** put in the right place? Are there any

**[19:25]** conflicts in the context? And you do

**[19:28]** want to dedicate some time to this,

**[19:29]** especially at the beginning because it

**[19:31]** will take time to get this right. And

**[19:33]** lastly, you will need to start using

**[19:35]** this cons consistently. The only way

**[19:36]** this is going to work for you is when

**[19:38]** you use it a lot because the more you

**[19:40]** use it, the better it will get. And

**[19:42]** there is some learning curve attached to

**[19:44]** this. I can tell you I'm definitely not

**[19:45]** there yet, but it is getting better and

**[19:47]** better and it's making a big impact on

**[19:49]** the relevancy of my AI outputs across me

**[19:52]** and my team's chats. But it does take

**[19:54]** time to figure out what file structure

**[19:56]** makes sense for you and to test its

**[19:57]** capabilities. Generally, I try to

**[20:00]** approach this with a mindset of trying

**[20:01]** to let AI clock code or clockwork or

**[20:03]** wherever you use AI become your main

**[20:05]** operating system for work because if you

**[20:07]** do that, you'll slowly but surely fill

**[20:09]** in the gaps to actually make it become

**[20:11]** your main operating system. And this is

**[20:13]** where we're heading anyway. So you might

**[20:14]** as well be early. Now if you want to

**[20:16]** take it to the last level, which is

**[20:17]** going to be a game changer for anyone

**[20:19]** who runs a business, is to actually roll

**[20:21]** this out and sync this entire context

**[20:23]** data set and the skills across the

**[20:25]** entire team. So all of your team

**[20:27]** members, AI agents instantly become far

**[20:29]** more powerful for your business. Now,

**[20:32]** when rolling this out for teams, a few

**[20:34]** things of course become important.

**[20:35]** First, the file structure will probably

**[20:37]** have to change a bit, and you'll need

**[20:39]** some more files for using this across a

**[20:41]** team. For example, in my business OS,

**[20:43]** you can see I have a few more folders

**[20:44]** like my departments, my team and their

**[20:47]** roles and plugins and skills so they can

**[20:49]** be easily shared across the team. Again,

**[20:51]** if you want to learn more about the file

**[20:53]** structure, I covered it in full in that

**[20:54]** last video which will be in the link in

**[20:56]** the description below. Now, for your

**[20:58]** team members to get to this initial

**[20:59]** setup, you can of course just share a

**[21:01]** zip file with them uh of the entire

**[21:03]** context doc so they can install it. And

**[21:05]** then second of course when you want to

**[21:07]** share this across the team updates need

**[21:09]** to actually be synced across the team

**[21:10]** and ideally in real time. Now we've

**[21:12]** explored multiple options of doing this

**[21:14]** and because of course they are local

**[21:16]** files it's not extremely straightforward

**[21:17]** to do but for syncing across a team uh

**[21:20]** you have multiple options. First you can

**[21:21]** use GitHub. Second you can use Obsidian

**[21:24]** sync which is a feature of Obsidian.

**[21:26]** Third you can even uh launch a

**[21:28]** self-hosted solution to do this. But the

**[21:30]** best option we found which we're

**[21:32]** currently using is a plugin inside of

**[21:34]** Obsidian called Relay. Now this is a

**[21:36]** community plugin inside of Obsidian

**[21:38]** which you can find here by going to

**[21:39]** settings, clicking on community plugins,

**[21:41]** go to browse, type in relay and from

**[21:44]** there you can install it. Once you've

**[21:46]** installed it, it'll be listed under your

**[21:48]** community plugins. And through relay now

**[21:51]** I can decide for each of the folder to

**[21:52]** which of my team members these updates

**[21:54]** need to be synced to. And through this

**[21:57]** any change anyone in my team makes in

**[21:59]** any of these contact stocks will it will

**[22:01]** automatically be synced and updated

**[22:03]** across anyone in the team in real time.

**[22:05]** And you can use relay uh for up to three

**[22:07]** people uh for free. But with this setup

**[22:09]** of course uh permission settings become

**[22:11]** important too. Not every team member

**[22:13]** should be able to update every file or

**[22:16]** not even uh every team member should be

**[22:17]** able to see or access any file. So you

**[22:20]** as a business owner of course need to

**[22:21]** control some of these permission

**[22:23]** settings. Now, unfortunately, this is

**[22:25]** not very straightforward to do on Relay

**[22:27]** yet. We actually talked to the founder

**[22:28]** of Relay and this feature is in their

**[22:30]** pipeline. But in the meantime, we've

**[22:32]** built our own version or custom setup on

**[22:34]** top of this relay plugin that actually

**[22:36]** gives us these permission settings. And

**[22:37]** see that we have installed here our Beni

**[22:39]** relay plugin, which is just our version

**[22:41]** of this app with permission settings.

**[22:43]** And now, for example, I can still make

**[22:45]** updates in this general context folder

**[22:48]** uh with the important documents, route,

**[22:50]** strategy, etc. But my uh team members

**[22:52]** only get read access. So they can still

**[22:54]** use these documents but they can't

**[22:56]** actually update them. This is what one

**[22:58]** of my team members would see a little

**[23:00]** lock with this is a readonly file. Now

**[23:02]** this setup is a little bit more

**[23:03]** technical. Um so if you want to set this

**[23:05]** up we have full guides together with all

**[23:07]** the other guides on how to sync across

**[23:08]** team members with GitHub and other ways.

**[23:10]** So if that's interesting to you and you

**[23:12]** want access to our customized plug-in

**[23:14]** again you could check out the AI

**[23:16]** accelerator. And then lastly, of course,

**[23:18]** once you have set this up, it is key to

**[23:20]** have one person in the business really

**[23:21]** be the operator and the manager of this

**[23:24]** context layer because it does require

**[23:27]** maintenance. It requires effort to

**[23:29]** actually keep this updated and well

**[23:31]** functioning across the business and this

**[23:33]** is going to take some time. So someone

**[23:34]** needs to be responsible. Now again, I

**[23:36]** think syncing and permission settings

**[23:38]** become a lot easier very soon because

**[23:39]** there are a lot of businesses trying to

**[23:41]** figure this out and there will be more

**[23:43]** of an infrastructure around this very

**[23:44]** soon. Um, but this is the way you can do

**[23:46]** it right now. Now, that's it for this

**[23:48]** video. Thank you so much for watching.

**[23:49]** Again, if you want more step-by-step

**[23:51]** guidance on setting this up for

**[23:52]** yourself, uh, multiple weekly Q&As and

**[23:55]** unlimited one-on-one live tech help, you

**[23:56]** can check out my AI accelerator in the

**[23:58]** link in the description below. Thank you

**[24:00]** so much for watching. If you got any

**[24:01]** value out of it, I highly appreciate a

**[24:02]** like and a subscribe. It really does

**[24:04]** help me. And if you want to learn more

**[24:06]** about cloth co-work and obsidian setup,

**[24:08]** you can check out the video here above.
