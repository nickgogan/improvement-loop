# Transcript: OSZdFnQmgRw

**URL:** https://www.youtube.com/watch?v=OSZdFnQmgRw
**Segments:** 402

---

## Full Text

Andre Carpathy just gave us the keys to his personal Obsidian Rag system. And I put Rag in air quotes because this Obsidian power knowledge base has no vector database, no embeddings, and no complicated retrieval process. Yet, it solves the exact same problem that these more complicated rag structures claim to do, which is allow our large language model to handle large amounts of documents and answer questions and gather accurate information about them. And the best part about this Obsidian powered system is that it is very lightweight. It's essentially free and it is the perfect middle ground for a solo operator or a small team. So today I'm going to show you how Carpathy's Obsidian knowledge system works, how to set it up yourself, and how it differs between traditional rag systems so you know if this is the right option for you. So the process by which we are going to create this obsidianpowered knowledge system was laid out yesterday in a pretty comprehensive Twitter post by Andre Karpathy. Now, the big takeaway from this post is that we are able to create large language model knowledge bases that essentially act in the same way as something like light rag or rag anything or any other graph rag system with obsidian. And we're able to do so in a rather simple manner by just having a clever structure to our file system and how we actually ingest data. And the end result is that I am able to ingest a pretty significant amount of data and documents into my Obsidian vault and use cloud code to ask questions about it to figure out connections between different things. Aka the exact same thing you would do with a traditional rag system, but with none of the overhead and a way simpler setup. And as Andre lays out, the setup looks something like this. First, we have data ingestion. We are bringing in articles. We're bringing in papers. We're bringing in repos from the internet or from wherever and we're bringing it into a raw directory inside of our Obsidian vault. This is essentially the staging area before it gets turned into a wiki. We as the human being in this interaction are able to see all of this happening via Obsidian. Obsidian for all intents and purposes is our front end. Here is where I can see where all the documents are laid out. Here's where I can read all the wiks. So, it isn't sort of abstracted away in a black box like it isn't a rag system. It's kind of hard even in a graph rag setup like light rag to actually go inside of here and really see everything. I mean I can but as cool as this looks this isn't you know very efficient and from there you just do a Q&A via something like cloud code and like Andre laid out here he expected that he would have to reach out for something like rag but the large language model has been pretty good about automaintaining index files and brief summary of all the documents it reads and this is something we are going to be able to do too with a pretty simple cloudmd file which I will be giving you and you will be able to find that cla md as well as a written guide that comes with a bunch of prompts inside head of my free Chase AI community. There will be a link to that in the description of this video. And speaking of Chase AI, and you knew this was coming, quick plug for my Cloud Code Masterass. Just released this a couple weeks ago, and it is the number one place to go from zero to AI dev, especially if you do not come from a technical background. You can find a link to this in the pinned comment. So, make sure to check this out if you're serious about learning this tool. Now, before we jump into the specifics of how to set up this Obsidian system for yourself, let's go over the actual file structure because this is important to understand how data is coming into our vault and then getting turned into wikis. So, the Obsidian vault is where everything lives. As you'll see, if you've never used it before, when you download Obsidian, you are going to designate a specific folder as the vault. In my case, it is quite literally called the vault. That's where everything in Obsidian lives. As a subfolder of the vault, we are going to have the raw folder. The raw folder is where all of our research gets dumped. Anything we want to manually include in these wikis gets put. This is essentially the staging folder. So, this is where all the raw data is going to be held. This can be markdown files. This can be PDFs. And I'm going to show you how to use the Obsidian Clipper to essentially turn any web page into a markdown file that gets sent to the raw folder automatically. We will have another subfolder that is the wiki folder. So what the large language model is going to do, what cloud code will do for us is on demand or you could have it even be a skill or have it be automated is we are going to point it at the raw folder and say hey I want you to create a wiki about whatever subject you've been gathering information about. From there it will then create a wiki about that. So you can see we have three different wiks here. One for AI agents, one for rag systems and one for content creation. Now in in between the wiki folder and these sub wiki folders is the master index markdown. This is essentially just a list of all of the different wiks that have been created because the idea is when you this is you when you talk to claude code all right that's cloud code over there and say hey I want to learn more about AI agents can you ask you know I want to ask questions about my wiki well what is it going to do? Well, it's going to go to the vault because you're probably already in there. It's then going to go to the wiki folder. It's going to go to the master index folder and say, "Hey, what wikies have we created?" Oh, he wants to know about rag systems. Okay, goes down to rag and the wiki folders themselves have index files which break down all the additional content. So, what Obsidian gives us and what this file structure gives us is a very clear path to find information even if we have a ton of it floating around. And this helps claude code because it's not going to have a ton of issues finding the data. We're not going to run a million tool calls to see what's in our file structure, but it also helps you because it's very clear where to go. For example, over here on the left is my Obsidian folder. I'm in the Obsidian UI, and we'll go through the download here in a second. But if I want to see a wiki, what do I do? I just go to wiki. I have a master index which lays down everything in there. Right now, it's just three things, but if there were 3,000, it still wouldn't be too difficult. And then from there, you know, I can click on it. It takes me to the index of that specific wiki. And then I can look at different stuff inside of there. It's that simple. And it's that simple for AI, too, which is why we're able to use essentially just a markdown file structure to somewhat mimic a rag system. So, while that theory is cool, now let's go into how to actually set this up for yourself. First and foremost, you're going to need to download Obsidian. You're just going to head to obsidian.md, hit download now, go through the wizard. It's completely free and you're going to designate some folder as the vault. Just create one, call it the vault. Makes it easy for me and that'll probably work for you. After we create the vault, we now need to set up this file structure inside of it. The easiest way to do that is with Claude Code. Simply open up Claude Code in the vault. So that's the directory I'm in. And you're going to give it a prompt telling it to create this file structure. Now, luckily for you, I already created the prompt. So you can just copy this thing and paste it in the cloud code. Now, if you're like me and you've already been using Obsidian for a bit, you probably have a bunch of folders already in there. So, maybe you don't want to call it RAW. Maybe you want to call it something else. The whole point of it is you just need to designate some folder is, like I said, sort of the holding area or the staging area for where all this information is going to get dumped until it gets turned into a wiki. So, adjust as needed. Now, the next thing we want to do is create a cloud.md file. Personal assistant type projects, things like this that are very markdown heavy, claw.mds are perfect for. And this claw.md file is breaking down the knowledgebased rules as well as how to essentially traverse it. So again that we aren't wasting tokens when we ask questions. Again I have this entire claw.md template prompt you can use this claw.md file is also telling claude how to structure these markdown files. So it's very easy to traverse files with this wiki links format. Now let's talk about how we can bring things into this raw folder. How we can get data into our system in the first place. Well, a super easy way to do this is with the Obsidian Web Clipper. So, I will put a link to this in the school or you can go to obsidian.mmd/clipper. And this is just a Chrome extension which makes it super easy to turn a web page into data into a markdown file. Now, the one issue with this web clipper is it's going to struggle with images. It's just not even going to bring them in. It'll have them as a link. But I want to be able to see the images from these documents I ingest inside of Obsidian. So, what do we do? Well, we are going to use an Obsidian community skill or Obsidian community plugin to help with this. So, one of the cool things about Obsidian is the community plugins. There's thousands of them. So, if you're inside of Obsidian, I'm inside the desktop app right now. If I come down here and I hit this little gear, I'm going to go to community plugins. I'm going to go to browse. And then you're going to search for local images plus. You're going to download it, install it, and turn it on. Make sure it's enabled. You can confirm it's enabled by heading to your community plugins tab and seeing this little tab turned on. Now, if we use the Obsidian Web Clipper, and I can see that over here as an extension, you can see what happens. It immediately pulls everything. And if I hit add to Obsidian, I can see this entire article, including the images. Now, there is one thing we need to set up inside of the web clipper, and that's making sure it actually pulls it into the raw folder automatically. I don't want to have to manually do that. You're just going to head to the options on your web clipper. I just rightclicked it. And then over here on the left where it says default, I created my own new template, but you can stick on the default if you want. Where it says location and note location right here, you're want you're going want to change that from clippings to raw. And that will make sure when you use the web clipper, it automatically goes into the raw folder. So now with the Obsidian Web Clipper extension and the images community plugin, we can now turn any web page on the internet into a markdown file that will be used for our wiki. But that is just one data funnel. That's a manual one. We can have Claude Code do a bunch of heavy lifting, too. So let's say I was trying to create a wiki about Claude Code skills. So I told Claude Code, let's create a wiki about claude code skills. I already included some info in the raw folder, what we pulled in via the web clipper. go conduct your own research and bring in the relevant raw MD files to generate that wiki. So what is it going to do? It's going to go on the internet use its standard web search and it's going to create its own wiki about claude code skills. So what you see is that this raw folder this whole raw pipeline that's more for you. That's for when you mainly want to put in some information. Now you can have cloud code do that as well but cloud code is also smart enough to essentially take the research figure out what's relevant itself and just create the wiki directly. This raw folder is really for you the human being to have some level of organization. And here's what cloud code came back with. So it created the cloud code skills wiki. We see here in the master index that it's referenced here. If I click on it, this then brings us to the index of claude code skills. And right now it has four articles. So here's the skills overview article. You can see it links to websites and it also links to different articles within our obsidian vault. So if I click on skill ecosystem, here's more stuff. If I click on top skills, right? So on and so forth. There's a very clear pathway from one article to another and how these things relate. Which means when you ask cloud code questions about these articles in these subjects, it's easy and cheap for it to answer questions about them. Which then brings us to the obvious question. Do we need rag at all? You know, we look at something like this light rag setup. You watch my last few videos with light rag and rag anything. and seeing how simple the setup with Obsidian, you're probably like, "Well, why would I ever even bother with these more complicated setups at all?" And the truth is, if you're a solo dev, a solo operator, or a small team that isn't dealing with thousands of documents, the answer probably is Obsidian makes more sense for you. It's lightweight, and you really don't need Rag. These large language models, these harnesses like Cloud Code are good enough for your use case. And we can sit here and get in the weeds about the differences between the obsidian rag and true rag. But the truth is the big thing is scale, right? Are we trying to scale to millions of documents or are we not? Because at a certain scale, it's going to be cheaper and faster to use a proper rag system no matter how good cloud code is at navigating this MD file document network you've created. But this isn't a question you necessarily need to have the exact answer to right away. Why wouldn't you just start with something like obsidian? And if it's clear your scale goes well beyond the bounds of what this thing can handle, then just move into rag. I think people get really caught up in like answering this question when it's like just try it out. Just experiment. It's not costing you anything to use some sort of rag system, rag system like obsidian. And if it doesn't work, it doesn't work. Fine. Then go use light rag instead. People want to sit here as they inevitably will in the comments and like argue this back and forth. Just try it. And I think the answer will be pretty clear at a certain point when you need to move to a true rag system. But the nice thing with this is is again most people don't need a real rag system. They just don't, right? Even if they're in a small business team situation. So having a proper, you know, orchestrated system like the subsidian knowledge base, I think is a huge boon to the majority of people. So I hope this breakdown was useful to you. Definitely check out Andre's post about this. He goes into a fair amount of detail. Make sure to check out the free Chase AI school. There's a link to that in the description that has all the prompts and a written breakdown of how to actually do this if you got confused at any part. And as always, take a look at Chase AI Plus if you want to get your hands on that master class. Besides that, let me know what you thought and I'll see you

---

## Timestamped Segments

**[0:00]** Andre Carpathy just gave us the keys to

**[0:02]** his personal Obsidian Rag system. And I

**[0:06]** put Rag in air quotes because this

**[0:08]** Obsidian power knowledge base has no

**[0:10]** vector database, no embeddings, and no

**[0:13]** complicated retrieval process. Yet, it

**[0:16]** solves the exact same problem that these

**[0:18]** more complicated rag structures claim to

**[0:20]** do, which is allow our large language

**[0:23]** model to handle large amounts of

**[0:25]** documents and answer questions and

**[0:27]** gather accurate information about them.

**[0:30]** And the best part about this Obsidian

**[0:31]** powered system is that it is very

**[0:33]** lightweight. It's essentially free and

**[0:36]** it is the perfect middle ground for a

**[0:38]** solo operator or a small team. So today

**[0:41]** I'm going to show you how Carpathy's

**[0:43]** Obsidian knowledge system works, how to

**[0:45]** set it up yourself, and how it differs

**[0:47]** between traditional rag systems so you

**[0:50]** know if this is the right option for

**[0:52]** you. So the process by which we are

**[0:53]** going to create this obsidianpowered

**[0:56]** knowledge system was laid out yesterday

**[0:58]** in a pretty comprehensive Twitter post

**[1:00]** by Andre Karpathy. Now, the big takeaway

**[1:03]** from this post is that we are able to

**[1:05]** create large language model knowledge

**[1:07]** bases that essentially act in the same

**[1:09]** way as something like light rag or rag

**[1:11]** anything or any other graph rag system

**[1:15]** with obsidian. And we're able to do so

**[1:18]** in a rather simple manner by just having

**[1:20]** a clever structure to our file system

**[1:23]** and how we actually ingest data. And the

**[1:26]** end result is that I am able to ingest a

**[1:29]** pretty significant amount of data and

**[1:31]** documents into my Obsidian vault and use

**[1:34]** cloud code to ask questions about it to

**[1:36]** figure out connections between different

**[1:38]** things. Aka the exact same thing you

**[1:40]** would do with a traditional rag system,

**[1:43]** but with none of the overhead and a way

**[1:45]** simpler setup. And as Andre lays out,

**[1:47]** the setup looks something like this.

**[1:49]** First, we have data ingestion. We are

**[1:51]** bringing in articles. We're bringing in

**[1:53]** papers. We're bringing in repos from the

**[1:56]** internet or from wherever and we're

**[1:57]** bringing it into a raw directory inside

**[2:00]** of our Obsidian vault. This is

**[2:02]** essentially the staging area before it

**[2:04]** gets turned into a wiki. We as the human

**[2:06]** being in this interaction are able to

**[2:08]** see all of this happening via Obsidian.

**[2:10]** Obsidian for all intents and purposes is

**[2:12]** our front end. Here is where I can see

**[2:14]** where all the documents are laid out.

**[2:15]** Here's where I can read all the wiks.

**[2:17]** So, it isn't sort of abstracted away in

**[2:19]** a black box like it isn't a rag system.

**[2:21]** It's kind of hard even in a graph rag

**[2:24]** setup like light rag to actually go

**[2:26]** inside of here and really see

**[2:28]** everything. I mean I can but as cool as

**[2:30]** this looks this isn't you know very

**[2:33]** efficient and from there you just do a

**[2:34]** Q&A via something like cloud code and

**[2:37]** like Andre laid out here he expected

**[2:39]** that he would have to reach out for

**[2:41]** something like rag but the large

**[2:42]** language model has been pretty good

**[2:43]** about automaintaining index files and

**[2:45]** brief summary of all the documents it

**[2:47]** reads and this is something we are going

**[2:48]** to be able to do too with a pretty

**[2:50]** simple cloudmd file which I will be

**[2:52]** giving you and you will be able to find

**[2:54]** that cla md as well as a written guide

**[2:56]** that comes with a bunch of prompts

**[2:58]** inside head of my free Chase AI

**[3:00]** community. There will be a link to that

**[3:01]** in the description of this video. And

**[3:03]** speaking of Chase AI, and you knew this

**[3:05]** was coming, quick plug for my Cloud Code

**[3:07]** Masterass. Just released this a couple

**[3:09]** weeks ago, and it is the number one

**[3:10]** place to go from zero to AI dev,

**[3:12]** especially if you do not come from a

**[3:13]** technical background. You can find a

**[3:16]** link to this in the pinned comment. So,

**[3:18]** make sure to check this out if you're

**[3:20]** serious about learning this tool. Now,

**[3:22]** before we jump into the specifics of how

**[3:24]** to set up this Obsidian system for

**[3:27]** yourself, let's go over the actual file

**[3:30]** structure because this is important to

**[3:32]** understand how data is coming into our

**[3:34]** vault and then getting turned into

**[3:35]** wikis. So, the Obsidian vault is where

**[3:38]** everything lives. As you'll see, if

**[3:40]** you've never used it before, when you

**[3:41]** download Obsidian, you are going to

**[3:43]** designate a specific folder as the

**[3:45]** vault. In my case, it is quite literally

**[3:47]** called the vault. That's where

**[3:48]** everything in Obsidian lives. As a

**[3:50]** subfolder of the vault, we are going to

**[3:53]** have the raw folder. The raw folder is

**[3:56]** where all of our research gets dumped.

**[3:58]** Anything we want to manually include in

**[4:00]** these wikis gets put. This is

**[4:01]** essentially the staging folder. So, this

**[4:03]** is where all the raw data is going to be

**[4:04]** held. This can be markdown files. This

**[4:07]** can be PDFs. And I'm going to show you

**[4:08]** how to use the Obsidian Clipper to

**[4:11]** essentially turn any web page into a

**[4:13]** markdown file that gets sent to the raw

**[4:15]** folder automatically. We will have

**[4:17]** another subfolder that is the wiki

**[4:18]** folder. So what the large language model

**[4:21]** is going to do, what cloud code will do

**[4:22]** for us is on demand or you could have it

**[4:25]** even be a skill or have it be automated

**[4:27]** is we are going to point it at the raw

**[4:29]** folder and say hey I want you to create

**[4:31]** a wiki about whatever subject you've

**[4:33]** been gathering information about. From

**[4:35]** there it will then create a wiki about

**[4:37]** that. So you can see we have three

**[4:40]** different wiks here. One for AI agents,

**[4:42]** one for rag systems and one for content

**[4:44]** creation. Now in in between the wiki

**[4:47]** folder and these sub wiki folders is the

**[4:51]** master index markdown. This is

**[4:53]** essentially just a list of all of the

**[4:56]** different wiks that have been created

**[4:58]** because the idea is when you this is you

**[5:02]** when you talk to claude code all right

**[5:04]** that's cloud code over there and say hey

**[5:06]** I want to learn more about AI agents can

**[5:09]** you ask you know I want to ask questions

**[5:11]** about my wiki well what is it going to

**[5:13]** do? Well, it's going to go to the vault

**[5:15]** because you're probably already in

**[5:16]** there. It's then going to go to the wiki

**[5:18]** folder. It's going to go to the master

**[5:19]** index folder and say, "Hey, what wikies

**[5:22]** have we created?" Oh, he wants to know

**[5:24]** about rag systems. Okay, goes down to

**[5:27]** rag and the wiki folders themselves have

**[5:30]** index files which break down all the

**[5:32]** additional content. So, what Obsidian

**[5:34]** gives us and what this file structure

**[5:36]** gives us is a very clear path to find

**[5:38]** information even if we have a ton of it

**[5:40]** floating around. And this helps claude

**[5:42]** code because it's not going to have a

**[5:44]** ton of issues finding the data. We're

**[5:46]** not going to run a million tool calls to

**[5:48]** see what's in our file structure, but it

**[5:50]** also helps you because it's very clear

**[5:52]** where to go. For example, over here on

**[5:54]** the left is my Obsidian folder. I'm in

**[5:56]** the Obsidian UI, and we'll go through

**[5:58]** the download here in a second. But if I

**[5:59]** want to see a wiki, what do I do? I just

**[6:01]** go to wiki. I have a master index which

**[6:05]** lays down everything in there. Right

**[6:06]** now, it's just three things, but if

**[6:07]** there were 3,000, it still wouldn't be

**[6:09]** too difficult. And then from there, you

**[6:11]** know, I can click on it. It takes me to

**[6:14]** the index of that specific wiki. And

**[6:16]** then I can look at different stuff

**[6:17]** inside of there. It's that simple. And

**[6:19]** it's that simple for AI, too, which is

**[6:21]** why we're able to use essentially just a

**[6:23]** markdown file structure to somewhat

**[6:25]** mimic a rag system. So, while that

**[6:27]** theory is cool, now let's go into how to

**[6:29]** actually set this up for yourself. First

**[6:31]** and foremost, you're going to need to

**[6:32]** download Obsidian. You're just going to

**[6:34]** head to obsidian.md,

**[6:36]** hit download now, go through the wizard.

**[6:38]** It's completely free and you're going to

**[6:40]** designate some folder as the vault. Just

**[6:43]** create one, call it the vault. Makes it

**[6:45]** easy for me and that'll probably work

**[6:47]** for you. After we create the vault, we

**[6:49]** now need to set up this file structure

**[6:51]** inside of it. The easiest way to do that

**[6:53]** is with Claude Code. Simply open up

**[6:55]** Claude Code in the vault. So that's the

**[6:58]** directory I'm in. And you're going to

**[7:00]** give it a prompt telling it to create

**[7:02]** this file structure. Now, luckily for

**[7:04]** you, I already created the prompt. So

**[7:05]** you can just copy this thing and paste

**[7:07]** it in the cloud code. Now, if you're

**[7:08]** like me and you've already been using

**[7:10]** Obsidian for a bit, you probably have a

**[7:13]** bunch of folders already in there. So,

**[7:15]** maybe you don't want to call it RAW.

**[7:17]** Maybe you want to call it something

**[7:18]** else. The whole point of it is you just

**[7:19]** need to designate some folder is, like I

**[7:22]** said, sort of the holding area or the

**[7:23]** staging area for where all this

**[7:25]** information is going to get dumped until

**[7:26]** it gets turned into a wiki. So, adjust

**[7:28]** as needed. Now, the next thing we want

**[7:29]** to do is create a cloud.md file.

**[7:31]** Personal assistant type projects, things

**[7:33]** like this that are very markdown heavy,

**[7:35]** claw.mds are perfect for. And this

**[7:37]** claw.md file is breaking down the

**[7:40]** knowledgebased rules as well as how to

**[7:42]** essentially traverse it. So again that

**[7:43]** we aren't wasting tokens when we ask

**[7:45]** questions. Again I have this entire

**[7:47]** claw.md template prompt you can use this

**[7:51]** claw.md file is also telling claude how

**[7:53]** to structure these markdown files. So

**[7:55]** it's very easy to traverse files with

**[7:58]** this wiki links format. Now let's talk

**[8:00]** about how we can bring things into this

**[8:02]** raw folder. How we can get data into our

**[8:05]** system in the first place. Well, a super

**[8:06]** easy way to do this is with the Obsidian

**[8:09]** Web Clipper. So, I will put a link to

**[8:11]** this in the school or you can go to

**[8:14]** obsidian.mmd/clipper.

**[8:16]** And this is just a Chrome extension

**[8:18]** which makes it super easy to turn a web

**[8:20]** page into data into a markdown file.

**[8:23]** Now, the one issue with this web clipper

**[8:25]** is it's going to struggle with images.

**[8:26]** It's just not even going to bring them

**[8:27]** in. It'll have them as a link. But I

**[8:29]** want to be able to see the images from

**[8:30]** these documents I ingest inside of

**[8:32]** Obsidian. So, what do we do? Well, we

**[8:34]** are going to use an Obsidian community

**[8:36]** skill or Obsidian community plugin to

**[8:38]** help with this. So, one of the cool

**[8:40]** things about Obsidian is the community

**[8:42]** plugins. There's thousands of them. So,

**[8:44]** if you're inside of Obsidian, I'm inside

**[8:46]** the desktop app right now. If I come

**[8:48]** down here and I hit this little gear,

**[8:50]** I'm going to go to community plugins.

**[8:52]** I'm going to go to browse. And then

**[8:54]** you're going to search for local images

**[8:56]** plus. You're going to download it,

**[8:58]** install it, and turn it on. Make sure

**[9:00]** it's enabled. You can confirm it's

**[9:02]** enabled by heading to your community

**[9:04]** plugins tab and seeing this little tab

**[9:07]** turned on. Now, if we use the Obsidian

**[9:10]** Web Clipper, and I can see that over

**[9:12]** here as an extension, you can see what

**[9:14]** happens. It immediately pulls

**[9:16]** everything. And if I hit add to

**[9:18]** Obsidian, I can see this entire article,

**[9:20]** including the images. Now, there is one

**[9:22]** thing we need to set up inside of the

**[9:24]** web clipper, and that's making sure it

**[9:26]** actually pulls it into the raw folder

**[9:28]** automatically. I don't want to have to

**[9:29]** manually do that. You're just going to

**[9:31]** head to the options on your web clipper.

**[9:34]** I just rightclicked it. And then over

**[9:36]** here on the left where it says default,

**[9:38]** I created my own new template, but you

**[9:40]** can stick on the default if you want.

**[9:42]** Where it says location

**[9:46]** and note location right here, you're

**[9:48]** want you're going want to change that

**[9:49]** from clippings to raw. And that will

**[9:52]** make sure when you use the web clipper,

**[9:54]** it automatically goes into the raw

**[9:56]** folder. So now with the Obsidian Web

**[9:58]** Clipper extension and the images

**[10:00]** community plugin, we can now turn any

**[10:02]** web page on the internet into a markdown

**[10:06]** file that will be used for our wiki. But

**[10:08]** that is just one data funnel. That's a

**[10:10]** manual one. We can have Claude Code do a

**[10:12]** bunch of heavy lifting, too. So let's

**[10:14]** say I was trying to create a wiki about

**[10:16]** Claude Code skills. So I told Claude

**[10:18]** Code, let's create a wiki about claude

**[10:19]** code skills. I already included some

**[10:21]** info in the raw folder, what we pulled

**[10:23]** in via the web clipper. go conduct your

**[10:25]** own research and bring in the relevant

**[10:27]** raw MD files to generate that wiki. So

**[10:29]** what is it going to do? It's going to go

**[10:30]** on the internet use its standard web

**[10:32]** search and it's going to create its own

**[10:34]** wiki about claude code skills. So what

**[10:37]** you see is that this raw folder this

**[10:40]** whole raw pipeline that's more for you.

**[10:42]** That's for when you mainly want to put

**[10:43]** in some information. Now you can have

**[10:44]** cloud code do that as well but cloud

**[10:46]** code is also smart enough to essentially

**[10:49]** take the research figure out what's

**[10:51]** relevant itself and just create the wiki

**[10:53]** directly. This raw folder is really for

**[10:55]** you the human being to have some level

**[10:56]** of organization. And here's what cloud

**[10:58]** code came back with. So it created the

**[11:01]** cloud code skills wiki. We see here in

**[11:03]** the master index that it's referenced

**[11:05]** here. If I click on it, this then brings

**[11:08]** us to the index of claude code skills.

**[11:10]** And right now it has four articles. So

**[11:12]** here's the skills overview article. You

**[11:15]** can see it links to websites and it also

**[11:17]** links to different articles within our

**[11:20]** obsidian vault. So if I click on skill

**[11:22]** ecosystem, here's more stuff. If I click

**[11:25]** on top skills, right? So on and so

**[11:27]** forth. There's a very clear pathway from

**[11:29]** one article to another and how these

**[11:31]** things relate. Which means when you ask

**[11:32]** cloud code questions about these

**[11:34]** articles in these subjects, it's easy

**[11:36]** and cheap for it to answer questions

**[11:39]** about them. Which then brings us to the

**[11:40]** obvious question. Do we need rag at all?

**[11:43]** You know, we look at something like this

**[11:44]** light rag setup. You watch my last few

**[11:46]** videos with light rag and rag anything.

**[11:49]** and seeing how simple the setup with

**[11:50]** Obsidian, you're probably like, "Well,

**[11:52]** why would I ever even bother with these

**[11:54]** more complicated setups at all?" And the

**[11:56]** truth is, if you're a solo dev, a solo

**[11:59]** operator, or a small team that isn't

**[12:01]** dealing with thousands of documents, the

**[12:05]** answer probably is Obsidian makes more

**[12:07]** sense for you. It's lightweight, and you

**[12:10]** really don't need Rag. These large

**[12:11]** language models, these harnesses like

**[12:13]** Cloud Code are good enough for your use

**[12:16]** case. And we can sit here and get in the

**[12:18]** weeds about the differences between the

**[12:19]** obsidian rag and true rag. But the truth

**[12:22]** is the big thing is scale, right? Are we

**[12:24]** trying to scale to millions of documents

**[12:26]** or are we not? Because at a certain

**[12:28]** scale, it's going to be cheaper and

**[12:30]** faster to use a proper rag system no

**[12:33]** matter how good cloud code is at

**[12:36]** navigating this MD file document network

**[12:39]** you've created. But this isn't a

**[12:40]** question you necessarily need to have

**[12:42]** the exact answer to right away. Why

**[12:44]** wouldn't you just start with something

**[12:46]** like obsidian? And if it's clear your

**[12:48]** scale goes well beyond the bounds of

**[12:50]** what this thing can handle, then just

**[12:52]** move into rag. I think people get really

**[12:54]** caught up in like answering this

**[12:55]** question when it's like just try it out.

**[12:57]** Just experiment. It's not costing you

**[12:59]** anything to use some sort of rag system,

**[13:01]** rag system like obsidian. And if it

**[13:04]** doesn't work, it doesn't work. Fine.

**[13:05]** Then go use light rag instead. People

**[13:06]** want to sit here as they inevitably will

**[13:08]** in the comments and like argue this back

**[13:10]** and forth. Just try it. And I think the

**[13:11]** answer will be pretty clear at a certain

**[13:13]** point when you need to move to a true

**[13:15]** rag system. But the nice thing with this

**[13:17]** is is again most people don't need a

**[13:20]** real rag system. They just don't, right?

**[13:22]** Even if they're in a small business team

**[13:24]** situation. So having a proper, you know,

**[13:27]** orchestrated system like the subsidian

**[13:29]** knowledge base, I think is a huge boon

**[13:31]** to the majority of people. So I hope

**[13:33]** this breakdown was useful to you.

**[13:35]** Definitely check out Andre's post about

**[13:37]** this. He goes into a fair amount of

**[13:38]** detail. Make sure to check out the free

**[13:40]** Chase AI school. There's a link to that

**[13:42]** in the description that has all the

**[13:44]** prompts and a written breakdown of how

**[13:46]** to actually do this if you got confused

**[13:48]** at any part. And as always, take a look

**[13:50]** at Chase AI Plus if you want to get your

**[13:51]** hands on that master class. Besides

**[13:54]** that, let me know what you thought and

**[13:56]** I'll see you
