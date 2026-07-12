# Transcript: Finally, an Open Standard for the Karpathy LLM Wiki is HERE

**URL:** https://www.youtube.com/watch?v=T33iI6izAKw
**Segments:** 569
**Channel:** Cole Medin
**Duration:** 19:37
**Uploaded:** 2026-07-02

---

## Full Text

A couple months ago, Andre Karpathy released the idea of the LLM wiki. It's a pattern for building personal knowledge bases using LLMs and it totally took off and for good reason. There's a lot of power in the simplicity here. So, this single markdown document in GitHub called it gist got to 40,000 stars. And seriously, you can take this file, copy it, paste it into your coding agent, and ask it to build you an LLM wiki and it's going to be able to just basically oneshot it. So, it's really easy to get started. And the idea here is when we're building a personal knowledge base for our second brain, instead of just dumping in a bunch of documents or indexing things for rag, we can have the LLM help us build something smarter, incrementally building and maintaining a persistent wiki with structured interlink collections of markdown files. And so the idea here is as we're adding in more sources over time like meeting transcripts, plan documents, articles from online, it's going to not just index it, but it's going to read each file, extract key information, and integrate it into the existing wiki. So updating things like the entity pages that it creates over time, so we have that knowledge graph for agent to traverse through and remember all the important information that we're bringing in. So, at this point, pretty much everybody is building their own LLM wiki in their second brain. But this isn't enough. And the main problem that we have here is when you take this gist and you build your own version of an LLM wiki, it's going to be structured differently than the next person doing the same thing. There's no standard. And so, there's really not a way to share your LLM wiki with someone else. And that's a bummer. You can think of a lot of different use cases where you'd want to curate a knowledge base over time and then share it with other people like other people on your team. Maybe you want one wiki for the team that everyone's second brains are accessing independently. Maybe I want to create a wiki for my YouTube content and then share that with you. There are a million reasons. But if your agent doesn't know exactly how I've structured my wiki with the different metadata and my entity files, it's not going to be able to search through it optimally. We need a standard so that everyone's building wikis in the same way so that we can share them freely. And so that is what Google has released here with their open knowledge format. It is a beautifully simple thing just like Harpathy's LLM wiki idea where it's just a simple standard built on top so that you can guarantee you're building your wiki in a way where other people's second brains can understand it and vice versa. And so in this video I want to cover why OKF is so powerful. It really is the future of personal agents. And I want to show you how easy it is to get started with this standard, both for new LM wikis and even transferring existing ones into this format. Very easy to do that. And no matter the wiki, no matter how much you're going to share it or not, this is important even as an optimization on top of Karpathy's LM wiki idea. And I know that Google is lagging in the AI race right now. Gemini is not as good as GPT and Claude, but they have been releasing some really good stuff on how to leverage LLMs effectively. And I think that's a totally different lane than building LLMs. Well, so I think this is something really worth leaning into even if OKF doesn't end up becoming the standard down the line for personal agents. There's going to be something like this. And so it's good to understand this now. Okay. Now, let's really get into OKF. So there are two things that they're standardizing here. The first is how we are organizing information like our entity documents and our concepts. And then the second standardization is the exact fields that we're going to have in our metadata. So this is the information that we tag at the top of every single document to give the agent a richer set of information. So we can even like query based on the title or the tags. So we have categorization. This is one of the most important things to let the agent traverse through our wiki like a knowledge graph. And really the best way to make this concrete for you is to show you what a traditional Karpathy wiki looks like. So we'll take a look at this. This is one of the first wiks that I built when Karpathy released this idea. And then we'll get into some of the problems that we have here. So at the top of every single wiki is your index file. You have the agent maintain this every single time it's bringing new information in. And the index file, it reads this when it's first searching through your knowledge base, pretty much every single time. And so this just gives you a high-level overview of all the documents that you have access to in the wiki. So the article and then a quick summary so it knows if this is something that it should look into based on the user's request. And so every single time we add in new documents, this is evolving. And so the agent will read this and then based on what we asked it to do or the question, if it figures like I should look at superbase o this concept right here, this entity document, then it'll drill into this. We also have the metadata like I talked about earlier like the title and the tags so that it can also search based on this like if it wants to look at the category of security then it can filter out just those documents and so then we have the full sort of like skill.md here this is like progressive disclosure like skills where the index tells it the knowledge it has and then it can read the full document if it's appropriate and then we also link to related concepts down here and that link is what really gives us this graph view where You can see how all of our entities and other documents are connected together. So, the agent can sift through this to really get a comprehensive set of information if the question really calls for it. And so, looking at one of these documents here, it might feel like it's overwhelming to build up all this knowledge over time, but seriously, with an LLM wiki, you are just giving the reins completely over to an LLM. So, you don't have to be technical. You don't have to spend a lot of time maintaining this. Literally the whole benefit of the wiki is that up until we've had LLMs for this, it was way too tedious to create this sort of knowledge base where we're responsible for understanding related concepts and building that over time as we're adding in new information. Like there's so much tedious work here that LLM are really, really good at. But as much as they're good at this, they aren't going to create this system in the same way that someone else will with with their LLM, right? like the way that we link related concepts might be different. The way we structure information, even the metadata, like what if we don't have tags, but we have a field called categories. I mean, even something as simple as that, that that little change might make it so that if I gave the knowledge base to another person's agent, it wouldn't know how to search through things categorically. It would have to dive into the metadata first to understand that, and it might not decide to do so. I mean, all these little problems will start to compound when you don't have the same metadata, you don't have the same folders. That's what we're looking to do here with OKF. All right. So now, if you want to build with OKF, create a new knowledge base with this format or even refactor one to use the open knowledge format, look no further than their spec.md file. So, this is in their repo. I'll link to it in the description. This is just like Karpathy's gist where you copy this document. Like you literally just click this one button right here, put it into your coding agent, and tell it to either build you a wiki following the open knowledge format or even refactor an existing one. Like I said, it's going to knock either of those out of the park because this is kind of like a skill. It teaches the coding agent everything it needs to know about the standard. Like here is the terminology. Here's how we structure the bundles. I'll show you more on this in a little bit. Here is how we build the YAML front matter. different attributes that we have for each one of our documents like the tags for categorization, right? Like this single source of truth is all that it needs. And because it's such a simple format, a simple standard overall, it's not really going to get confused going through this. I mean, it's a pretty long file, but in terms of what large language models can handle these days, especially with, you know, GPT 5.5 or Opus 4.8, this is not much instruction. And it it also doesn't really matter the scale of your current knowledge base if you are refactoring because you can specifically ask it to use sub agents to work through the different sections of your knowledge base to refactor it to this format. So really easy to scale, really easy to just have the agent rip through this spec. The sponsor of today's video is Post Hog, a single place for you to understand how users are actually using your application to debug and fix issues and test and roll out all of your changes. And I'm excited for this because I am using Post Hog myself in Archon, my open-source AI coding harness builder. I'm legitimately leaning on the data insights that I get from Post Hog every single day so that I know exactly how to improve Archon in the way that users actually need. And installing Posthog is incredibly easy. You just click on the install with AI button on their homepage that I'll have linked to in the description and boom, it's a single command you can run a wizard that will essentially be a senior engineer helping you set up analytics for your entire application in just minutes. And you can also create custom data views like this is the dashboard that I'm looking at every single day to see how people are actually using Archon. And then we can also drill down to get very granular as well. So the individual runs of Archon, I can click into this here to see all the details. And so we can go very high level all the way to individual parameters as we need. It's got the analytics for everything. And so production is the time where you can't be flying blind. When you have something deployed out to the world, you need observability. And Post Hog is the best for that. So I'll have a link in the description. I would highly recommend checking them out. And I talked about this a little bit at the start of the video, but this really is the future of personal agents. It's like what MCP did for agentto tool communication, this OKF is doing for agent to knowledgebased communication. And one of the most important things in the spec here is that they talk about it being a standard both for consuming knowledge bases like searching through them, but also producing knowledge bases. How do we evolve the wiki over time? build up the entity pages like Karpathy talked about in the initial gist. We really are building on top of it. And one of the really interesting things to think about here is yes, this is fantastic for sharing knowledge bases or having a teamwide knowledge base. This is also really good though even if you're never going to share a knowledge base. Think about this. If everybody has the same standard for how they are building up their own personal knowledge base, everyone can share ideas more like, oh, here are the entity pages that are working really well for me and this is how I want to organize things under the standard. And then because you have the standard as the foundation, it's easier for other people to take those ideas. And so what we're also I think what we're going to see is like yes, I don't think OKF is going to in the end be the standard, but we're going to see something like that and we're going to see the standard evolve over time so that it's easier and easier for people to create these really rich knowledge bases without having to spend a lot of time upfront designing it with the LLM. Now, of course, sharing wikis with other people is the biggest benefit of OKF. And that leads me into the example that I have for you that's also a gift I'm very excited to share. I have built a bundle, that's what you call an OKF Wiki, that packages up all of my favorite AI coding YouTube videos on my channel. And so, here's the thing. I'm excited for this. I know that a lot of you, you don't watch my entire video every single time. You're going to sift through things. You're going to just take the transcript and feed it into your second brain and ask questions. You guys are already doing something like this, but now making it easier for you because I'm prepackaging up sets of videos. I actually want to start doing this so that you can very easily bring it into your second brain and ask questions as it relates to what you actually care about or what you are working on specifically. And so take a look at this. All you have to do is first of all take this spec and give it to your coding agent. You have it teach itself OKF. And then you go to this repo with my AI coding knowledge bundle. I'll have this linked in the description as well. And you just paste this prompt into your coding agent. That's it. You give it the link to this repo. You tell it to read the readme and set up everything and it already understands OKF. So, it links those two things together. Brings the bundle into your local Obsidian or Notion or whatever you're managing your knowledge. And then boom, you can instantly start asking questions. You don't have to bring in the transcripts yourself. This is the easiest way for just content creators in general to share their knowledge with the world. They can create bundles. I'm creating bundles for all my videos now. And so this is just one example of what OKF unlocks for us. And so I'll also show you what this bundle looks like because it's a really good example of what OKF is really doing for us. All right, let's get into the belly of the beast. Now I'll show you how I've been setting up OKF and we'll get into the example bundle as well. And so something that I do for my second brain, every single system that I build in, I always have a tople document that talks about how it works. Like this is how I'm working with OKF bundles. And then here are the different bundles that I have. So I basically have an index so it knows the different bundles that it can go into and search and read the index that we have in there. So we kind of have like two layers of indexing. And then I also built a simple CLI script. This is actually there in the example bundle that you can clone that makes it easy for it to in the command line list out my bundles to view a specific index and then you know once it finds one of those files it wants to read then we have the command line tool to read by a specific bundle and concept ID. So I've added like a little bit of organization on top of OKF with just how I manage many different bundles but otherwise I'm following the format exactly. And so let's actually look at one of these. I'll click into bundles here and we'll go into the one that I just shared the GitHub for. So, if we look at the index here, we can see that I have two different sections and this is actually a smaller bundle. So, I didn't want to do something super complicated. So, there really are just two sections. I have the videos that I've put in this bundle, which it's it's rather small. There's only four videos, but these are like the best and most up-to-date ones on my channel for AI coding. And then I have the concepts as well. So different things that I talk about throughout multiple of the videos that I want to extract into its own entity page. And so the index here says here are the sections. And then I don't actually have a list of each one of the individual files because I'm just going to have the agent read the files that we have in concepts or videos, right? Like it can list out here are all the files or it can read the index within concepts itself, right? So, however you want it to navigate, it's going to be able to go through these different layers of documents or just do a keyword search. And so, clicking into any one of these, like the PIV loop, for example, this is the primary mental model that I always teach for AI coding. Very important to have a process for yourself to plan, implement, and validate whatever you're creating with a coding agent. And so, we have the YAML front matter at the top. And the type, this is what is required by OKF. It is the single required field in the metadata because this is what gives categorization to your documents. So like this is the type of concept. If I go to a video here, the type is video. So we can search over just the videos over just the concepts which is especially powerful once you get bundles that are a lot bigger than this. Again, this is just an example here. But then we also have all of the optional titles in OKF. So title, tags, related videos. This is how we link things together, right? Like you saw with that other wiki I showed earlier, it was just things were linked at the bottom. However, this now makes it so it's easier to navigate, creating a standard for how we are linking our entities together. And so each one of these are optional. Only type is required in OKF. But just because you don't always have these doesn't mean that your agent won't understand it, right? Like if your agent is a consumer of OKF, if you gave it the spec and taught it to be a consumer, it's going to know how to leverage these fields for better searching and traversing through the knowledge graph that we have here. And so then this is just all of our information on the piv loop. I kept it nice and simple. And then also linking to videos as well, which maybe is like a little bit redundant with related videos. So I could probably make this bundle a bit better, but I just wanted to have this as an initial example. And it is something that you can immediately bring into your second brain. Just start asking questions. Like I'll show you an example here in my terminal. So first of all, at the top level of my second brain, I just asked what bundles do I have? It ran a command here. So it used that little CLI tool to list out all the bundles that I have. And then it told me that and then I just asked it a question. So not even telling it what bundle specifically to look through. I said, "What's Cole's single biggest idea for getting reliable code out of an AI coding assistant?" and it ran four commands in total. So first of all it decided to read the coal AI coding index that's the GitHub that I have for you and then based on the index it knew like okay let's take a look at the concepts here and then from the concepts it's like okay the single most important thing I don't know what in the index told it that but it's like context engineering let's read the concept of context engineering so we can see the progressive disclosure as the agent is figuring out where it needs to look down to find the answer for me and then we get the final answer here So just beautiful to watch it work. When we have something structured like this, it's so easy for it to start with really not much context at all and then drill down into exactly what we need. That's what OKF gives us as a standard. All right. So if you're not sold on the idea of having a standard for the LM wiki at this point, I don't know what to tell you. The one critique that I think is actually pretty valid with OKF is a lot of people are saying that it's too simple, right? like there's not a lot of value or substance that's actually added on top of the Karpathy wiki. So, I've I've seen that a few times just as I've been doing a lot of research. I mean, I put a lot of time into prepping for these videos. I think it's kind of valid because if we look at like what it's really doing on top of the Carpathy wiki, it's it's speaking to like exactly how you organize your different files. Like they they specifically have like indexes within the folders and a top level index like you saw in my bundle. I mean, that's something I didn't really have in wikis before. And then we have the specific fields in our metadata like the type is required. The other ones are optional but these are the ones that they recommend. Like that's pretty much it. It's how we organize and what is the metadata. That's pretty much all that we actually have in the standard. And so like the argument is kind of valid where it's like what is it really giving? Like there's there's not much there. But I think that's also the point, right? Like minimally opinionated. It's the bare minimum layer that we need on top so that we can produce and consume these wiks in exactly the same way across everyone's agents that lean into OKF. Like I think that's actually a good thing. I think that's a benefit, not a downside. The fact that there's not much substance here might seem counterintuitive, but I think that is actually a good thing. And I encourage you just try out the bundle that I have for you here. give it the spec and then give it this prompt and then just start asking questions about AI coding like how I use sub aents uh what is the piv loop like just start asking and and seeing how easy it is for your agent to grab those things for you and so that's everything that I got for you today on OKF really is the future of personal agents if you appreciated this video you're looking forward to more things on AI coding and second brains I'd really appreciate a like and a subscribe and with that I will see you in the next video.

---

## Timestamped Segments

**[0:00]** A couple months ago, Andre Karpathy

**[0:02]** released the idea of the LLM wiki. It's

**[0:04]** a pattern for building personal

**[0:06]** knowledge bases using LLMs and it

**[0:09]** totally took off and for good reason.

**[0:11]** There's a lot of power in the simplicity

**[0:13]** here. So, this single markdown document

**[0:16]** in GitHub called it gist got to 40,000

**[0:18]** stars. And seriously, you can take this

**[0:20]** file, copy it, paste it into your coding

**[0:23]** agent, and ask it to build you an LLM

**[0:25]** wiki and it's going to be able to just

**[0:26]** basically oneshot it. So, it's really

**[0:28]** easy to get started. And the idea here

**[0:31]** is when we're building a personal

**[0:33]** knowledge base for our second brain,

**[0:35]** instead of just dumping in a bunch of

**[0:36]** documents or indexing things for rag, we

**[0:39]** can have the LLM help us build something

**[0:41]** smarter, incrementally building and

**[0:43]** maintaining a persistent wiki with

**[0:45]** structured interlink collections of

**[0:47]** markdown files. And so the idea here is

**[0:50]** as we're adding in more sources over

**[0:52]** time like meeting transcripts, plan

**[0:54]** documents, articles from online, it's

**[0:56]** going to not just index it, but it's

**[0:58]** going to read each file, extract key

**[1:01]** information, and integrate it into the

**[1:03]** existing wiki. So updating things like

**[1:04]** the entity pages that it creates over

**[1:07]** time, so we have that knowledge graph

**[1:09]** for agent to traverse through and

**[1:11]** remember all the important information

**[1:12]** that we're bringing in. So, at this

**[1:14]** point, pretty much everybody is building

**[1:16]** their own LLM wiki in their second

**[1:18]** brain. But this isn't enough. And the

**[1:21]** main problem that we have here is when

**[1:23]** you take this gist and you build your

**[1:25]** own version of an LLM wiki, it's going

**[1:27]** to be structured differently than the

**[1:29]** next person doing the same thing.

**[1:31]** There's no standard. And so, there's

**[1:32]** really not a way to share your LLM wiki

**[1:35]** with someone else. And that's a bummer.

**[1:37]** You can think of a lot of different use

**[1:38]** cases where you'd want to curate a

**[1:40]** knowledge base over time and then share

**[1:42]** it with other people like other people

**[1:43]** on your team. Maybe you want one wiki

**[1:45]** for the team that everyone's second

**[1:47]** brains are accessing independently.

**[1:49]** Maybe I want to create a wiki for my

**[1:51]** YouTube content and then share that with

**[1:53]** you. There are a million reasons. But if

**[1:56]** your agent doesn't know exactly how I've

**[1:58]** structured my wiki with the different

**[2:00]** metadata and my entity files, it's not

**[2:02]** going to be able to search through it

**[2:03]** optimally. We need a standard so that

**[2:05]** everyone's building wikis in the same

**[2:07]** way so that we can share them freely.

**[2:10]** And so that is what Google has released

**[2:12]** here with their open knowledge format.

**[2:14]** It is a beautifully simple thing just

**[2:16]** like Harpathy's LLM wiki idea where it's

**[2:19]** just a simple standard built on top so

**[2:22]** that you can guarantee you're building

**[2:24]** your wiki in a way where other people's

**[2:26]** second brains can understand it and vice

**[2:29]** versa. And so in this video I want to

**[2:31]** cover why OKF is so powerful. It really

**[2:33]** is the future of personal agents. And I

**[2:36]** want to show you how easy it is to get

**[2:37]** started with this standard, both for new

**[2:40]** LM wikis and even transferring existing

**[2:43]** ones into this format. Very easy to do

**[2:45]** that. And no matter the wiki, no matter

**[2:47]** how much you're going to share it or

**[2:48]** not, this is important even as an

**[2:50]** optimization on top of Karpathy's LM

**[2:53]** wiki idea. And I know that Google is

**[2:56]** lagging in the AI race right now. Gemini

**[2:58]** is not as good as GPT and Claude, but

**[3:01]** they have been releasing some really

**[3:02]** good stuff on how to leverage LLMs

**[3:04]** effectively. And I think that's a

**[3:06]** totally different lane than building

**[3:08]** LLMs. Well, so I think this is something

**[3:10]** really worth leaning into even if OKF

**[3:13]** doesn't end up becoming the standard

**[3:14]** down the line for personal agents.

**[3:16]** There's going to be something like this.

**[3:18]** And so it's good to understand this now.

**[3:20]** Okay. Now, let's really get into OKF. So

**[3:23]** there are two things that they're

**[3:24]** standardizing here. The first is how we

**[3:27]** are organizing information like our

**[3:28]** entity documents and our concepts. And

**[3:31]** then the second standardization is the

**[3:33]** exact fields that we're going to have in

**[3:35]** our metadata. So this is the information

**[3:38]** that we tag at the top of every single

**[3:40]** document to give the agent a richer set

**[3:43]** of information. So we can even like

**[3:44]** query based on the title or the tags. So

**[3:47]** we have categorization. This is one of

**[3:49]** the most important things to let the

**[3:50]** agent traverse through our wiki like a

**[3:52]** knowledge graph. And really the best way

**[3:55]** to make this concrete for you is to show

**[3:57]** you what a traditional Karpathy wiki

**[4:00]** looks like. So we'll take a look at

**[4:02]** this. This is one of the first wiks that

**[4:03]** I built when Karpathy released this

**[4:05]** idea. And then we'll get into some of

**[4:07]** the problems that we have here. So at

**[4:09]** the top of every single wiki is your

**[4:12]** index file. You have the agent maintain

**[4:14]** this every single time it's bringing new

**[4:16]** information in. And the index file, it

**[4:18]** reads this when it's first searching

**[4:20]** through your knowledge base, pretty much

**[4:21]** every single time. And so this just

**[4:23]** gives you a high-level overview of all

**[4:25]** the documents that you have access to in

**[4:28]** the wiki. So the article and then a

**[4:30]** quick summary so it knows if this is

**[4:31]** something that it should look into based

**[4:33]** on the user's request. And so every

**[4:35]** single time we add in new documents,

**[4:37]** this is evolving. And so the agent will

**[4:40]** read this and then based on what we

**[4:41]** asked it to do or the question, if it

**[4:43]** figures like I should look at superbase

**[4:45]** o this concept right here, this entity

**[4:47]** document, then it'll drill into this. We

**[4:50]** also have the metadata like I talked

**[4:51]** about earlier like the title and the

**[4:53]** tags so that it can also search based on

**[4:56]** this like if it wants to look at the

**[4:58]** category of security then it can filter

**[5:00]** out just those documents and so then we

**[5:03]** have the full sort of like skill.md here

**[5:05]** this is like progressive disclosure like

**[5:07]** skills where the index tells it the

**[5:09]** knowledge it has and then it can read

**[5:11]** the full document if it's appropriate

**[5:13]** and then we also link to related

**[5:15]** concepts down here and that link is what

**[5:17]** really gives us this graph view where

**[5:19]** You can see how all of our entities and

**[5:22]** other documents are connected together.

**[5:24]** So, the agent can sift through this to

**[5:26]** really get a comprehensive set of

**[5:27]** information if the question really calls

**[5:30]** for it. And so, looking at one of these

**[5:32]** documents here, it might feel like it's

**[5:35]** overwhelming to build up all this

**[5:36]** knowledge over time, but seriously, with

**[5:38]** an LLM wiki, you are just giving the

**[5:40]** reins completely over to an LLM. So, you

**[5:42]** don't have to be technical. You don't

**[5:44]** have to spend a lot of time maintaining

**[5:46]** this. Literally the whole benefit of the

**[5:48]** wiki is that up until we've had LLMs for

**[5:52]** this, it was way too tedious to create

**[5:54]** this sort of knowledge base where we're

**[5:56]** responsible for understanding related

**[5:58]** concepts and building that over time as

**[6:00]** we're adding in new information. Like

**[6:01]** there's so much tedious work here that

**[6:03]** LLM are really, really good at. But as

**[6:05]** much as they're good at this, they

**[6:07]** aren't going to create this system in

**[6:10]** the same way that someone else will with

**[6:12]** with their LLM, right? like the way that

**[6:14]** we link related concepts might be

**[6:16]** different. The way we structure

**[6:17]** information, even the metadata, like

**[6:20]** what if we don't have tags, but we have

**[6:22]** a field called categories. I mean, even

**[6:24]** something as simple as that, that that

**[6:26]** little change might make it so that if I

**[6:28]** gave the knowledge base to another

**[6:29]** person's agent, it wouldn't know how to

**[6:32]** search through things categorically. It

**[6:34]** would have to dive into the metadata

**[6:36]** first to understand that, and it might

**[6:38]** not decide to do so. I mean, all these

**[6:40]** little problems will start to compound

**[6:42]** when you don't have the same metadata,

**[6:43]** you don't have the same folders. That's

**[6:45]** what we're looking to do here with OKF.

**[6:47]** All right. So now, if you want to build

**[6:49]** with OKF, create a new knowledge base

**[6:51]** with this format or even refactor one to

**[6:54]** use the open knowledge format, look no

**[6:56]** further than their spec.md file. So,

**[6:58]** this is in their repo. I'll link to it

**[7:00]** in the description. This is just like

**[7:02]** Karpathy's gist where you copy this

**[7:05]** document. Like you literally just click

**[7:06]** this one button right here, put it into

**[7:09]** your coding agent, and tell it to either

**[7:11]** build you a wiki following the open

**[7:12]** knowledge format or even refactor an

**[7:14]** existing one. Like I said, it's going to

**[7:15]** knock either of those out of the park

**[7:18]** because this is kind of like a skill. It

**[7:20]** teaches the coding agent everything it

**[7:22]** needs to know about the standard. Like

**[7:24]** here is the terminology. Here's how we

**[7:26]** structure the bundles. I'll show you

**[7:27]** more on this in a little bit. Here is

**[7:29]** how we build the YAML front matter.

**[7:31]** different attributes that we have for

**[7:33]** each one of our documents like the tags

**[7:35]** for categorization, right? Like this

**[7:37]** single source of truth is all that it

**[7:40]** needs. And because it's such a simple

**[7:42]** format, a simple standard overall, it's

**[7:44]** not really going to get confused going

**[7:46]** through this. I mean, it's a pretty long

**[7:48]** file, but in terms of what large

**[7:49]** language models can handle these days,

**[7:51]** especially with, you know, GPT 5.5 or

**[7:53]** Opus 4.8, this is not much instruction.

**[7:56]** And it it also doesn't really matter the

**[7:59]** scale of your current knowledge base if

**[8:01]** you are refactoring because you can

**[8:03]** specifically ask it to use sub agents to

**[8:06]** work through the different sections of

**[8:07]** your knowledge base to refactor it to

**[8:10]** this format. So really easy to scale,

**[8:12]** really easy to just have the agent rip

**[8:13]** through this spec. The sponsor of

**[8:16]** today's video is Post Hog, a single

**[8:18]** place for you to understand how users

**[8:20]** are actually using your application to

**[8:22]** debug and fix issues and test and roll

**[8:24]** out all of your changes. And I'm excited

**[8:26]** for this because I am using Post Hog

**[8:29]** myself in Archon, my open-source AI

**[8:31]** coding harness builder. I'm legitimately

**[8:34]** leaning on the data insights that I get

**[8:36]** from Post Hog every single day so that I

**[8:38]** know exactly how to improve Archon in

**[8:40]** the way that users actually need. And

**[8:43]** installing Posthog is incredibly easy.

**[8:45]** You just click on the install with AI

**[8:46]** button on their homepage that I'll have

**[8:48]** linked to in the description and boom,

**[8:50]** it's a single command you can run a

**[8:52]** wizard that will essentially be a senior

**[8:54]** engineer helping you set up analytics

**[8:56]** for your entire application in just

**[8:59]** minutes. And you can also create custom

**[9:01]** data views like this is the dashboard

**[9:03]** that I'm looking at every single day to

**[9:05]** see how people are actually using

**[9:06]** Archon. And then we can also drill down

**[9:08]** to get very granular as well. So the

**[9:10]** individual runs of Archon, I can click

**[9:13]** into this here to see all the details.

**[9:15]** And so we can go very high level all the

**[9:17]** way to individual parameters as we need.

**[9:20]** It's got the analytics for everything.

**[9:22]** And so production is the time where you

**[9:25]** can't be flying blind. When you have

**[9:27]** something deployed out to the world, you

**[9:29]** need observability. And Post Hog is the

**[9:31]** best for that. So I'll have a link in

**[9:32]** the description. I would highly

**[9:34]** recommend checking them out. And I

**[9:36]** talked about this a little bit at the

**[9:37]** start of the video, but this really is

**[9:39]** the future of personal agents. It's like

**[9:41]** what MCP did for agentto tool

**[9:44]** communication, this OKF is doing for

**[9:47]** agent to knowledgebased communication.

**[9:50]** And one of the most important things in

**[9:51]** the spec here is that they talk about it

**[9:53]** being a standard both for consuming

**[9:56]** knowledge bases like searching through

**[9:57]** them, but also producing knowledge

**[10:00]** bases. How do we evolve the wiki over

**[10:01]** time? build up the entity pages like

**[10:04]** Karpathy talked about in the initial

**[10:06]** gist. We really are building on top of

**[10:08]** it. And one of the really interesting

**[10:10]** things to think about here is yes, this

**[10:13]** is fantastic for sharing knowledge bases

**[10:15]** or having a teamwide knowledge base.

**[10:18]** This is also really good though even if

**[10:19]** you're never going to share a knowledge

**[10:20]** base. Think about this. If everybody has

**[10:23]** the same standard for how they are

**[10:25]** building up their own personal knowledge

**[10:27]** base, everyone can share ideas more

**[10:30]** like, oh, here are the entity pages that

**[10:33]** are working really well for me and this

**[10:34]** is how I want to organize things under

**[10:36]** the standard. And then because you have

**[10:37]** the standard as the foundation, it's

**[10:39]** easier for other people to take those

**[10:41]** ideas. And so what we're also I think

**[10:43]** what we're going to see is like yes, I

**[10:45]** don't think OKF is going to in the end

**[10:47]** be the standard, but we're going to see

**[10:48]** something like that and we're going to

**[10:50]** see the standard evolve over time so

**[10:52]** that it's easier and easier for people

**[10:54]** to create these really rich knowledge

**[10:56]** bases without having to spend a lot of

**[10:58]** time upfront designing it with the LLM.

**[11:01]** Now, of course, sharing wikis with other

**[11:03]** people is the biggest benefit of OKF.

**[11:05]** And that leads me into the example that

**[11:08]** I have for you that's also a gift I'm

**[11:10]** very excited to share. I have built a

**[11:13]** bundle, that's what you call an OKF

**[11:14]** Wiki, that packages up all of my

**[11:17]** favorite AI coding YouTube videos on my

**[11:20]** channel. And so, here's the thing. I'm

**[11:23]** excited for this. I know that a lot of

**[11:25]** you, you don't watch my entire video

**[11:27]** every single time. You're going to sift

**[11:29]** through things. You're going to just

**[11:30]** take the transcript and feed it into

**[11:32]** your second brain and ask questions. You

**[11:34]** guys are already doing something like

**[11:35]** this, but now making it easier for you

**[11:37]** because I'm prepackaging up sets of

**[11:40]** videos. I actually want to start doing

**[11:41]** this so that you can very easily bring

**[11:43]** it into your second brain and ask

**[11:45]** questions as it relates to what you

**[11:46]** actually care about or what you are

**[11:48]** working on specifically. And so take a

**[11:51]** look at this. All you have to do is

**[11:53]** first of all take this spec and give it

**[11:55]** to your coding agent. You have it teach

**[11:57]** itself OKF. And then you go to this repo

**[12:00]** with my AI coding knowledge bundle. I'll

**[12:02]** have this linked in the description as

**[12:04]** well. And you just paste this prompt

**[12:06]** into your coding agent. That's it. You

**[12:08]** give it the link to this repo. You tell

**[12:10]** it to read the readme and set up

**[12:12]** everything and it already understands

**[12:14]** OKF. So, it links those two things

**[12:15]** together. Brings the bundle into your

**[12:18]** local Obsidian or Notion or whatever

**[12:20]** you're managing your knowledge. And then

**[12:21]** boom, you can instantly start asking

**[12:23]** questions. You don't have to bring in

**[12:24]** the transcripts yourself. This is the

**[12:27]** easiest way for just content creators in

**[12:29]** general to share their knowledge with

**[12:31]** the world. They can create bundles. I'm

**[12:33]** creating bundles for all my videos now.

**[12:35]** And so this is just one example of what

**[12:37]** OKF unlocks for us. And so I'll also

**[12:40]** show you what this bundle looks like

**[12:41]** because it's a really good example of

**[12:43]** what OKF is really doing for us. All

**[12:45]** right, let's get into the belly of the

**[12:47]** beast. Now I'll show you how I've been

**[12:48]** setting up OKF and we'll get into the

**[12:50]** example bundle as well. And so something

**[12:52]** that I do for my second brain, every

**[12:55]** single system that I build in, I always

**[12:57]** have a tople document that talks about

**[12:59]** how it works. Like this is how I'm

**[13:01]** working with OKF bundles. And then here

**[13:03]** are the different bundles that I have.

**[13:05]** So I basically have an index so it knows

**[13:07]** the different bundles that it can go

**[13:08]** into and search and read the index that

**[13:11]** we have in there. So we kind of have

**[13:12]** like two layers of indexing. And then I

**[13:15]** also built a simple CLI script. This is

**[13:18]** actually there in the example bundle

**[13:20]** that you can clone that makes it easy

**[13:22]** for it to in the command line list out

**[13:24]** my bundles to view a specific index and

**[13:27]** then you know once it finds one of those

**[13:28]** files it wants to read then we have the

**[13:30]** command line tool to read by a specific

**[13:33]** bundle and concept ID. So I've added

**[13:36]** like a little bit of organization on top

**[13:38]** of OKF with just how I manage many

**[13:41]** different bundles but otherwise I'm

**[13:43]** following the format exactly. And so

**[13:45]** let's actually look at one of these.

**[13:46]** I'll click into bundles here and we'll

**[13:48]** go into the one that I just shared the

**[13:50]** GitHub for. So, if we look at the index

**[13:53]** here, we can see that I have two

**[13:55]** different sections and this is actually

**[13:57]** a smaller bundle. So, I didn't want to

**[13:59]** do something super complicated. So,

**[14:00]** there really are just two sections. I

**[14:02]** have the videos that I've put in this

**[14:04]** bundle, which it's it's rather small.

**[14:06]** There's only four videos, but these are

**[14:08]** like the best and most up-to-date ones

**[14:10]** on my channel for AI coding. And then I

**[14:12]** have the concepts as well. So different

**[14:14]** things that I talk about throughout

**[14:16]** multiple of the videos that I want to

**[14:18]** extract into its own entity page. And so

**[14:22]** the index here says here are the

**[14:23]** sections. And then I don't actually have

**[14:25]** a list of each one of the individual

**[14:27]** files because I'm just going to have the

**[14:29]** agent read the files that we have in

**[14:32]** concepts or videos, right? Like it can

**[14:33]** list out here are all the files or it

**[14:35]** can read the index within concepts

**[14:38]** itself, right? So, however you want it

**[14:40]** to navigate, it's going to be able to go

**[14:42]** through these different layers of

**[14:43]** documents or just do a keyword search.

**[14:45]** And so, clicking into any one of these,

**[14:47]** like the PIV loop, for example, this is

**[14:49]** the primary mental model that I always

**[14:51]** teach for AI coding. Very important to

**[14:53]** have a process for yourself to plan,

**[14:56]** implement, and validate whatever you're

**[14:58]** creating with a coding agent. And so, we

**[15:00]** have the YAML front matter at the top.

**[15:02]** And the type, this is what is required

**[15:04]** by OKF. It is the single required field

**[15:07]** in the metadata because this is what

**[15:09]** gives categorization to your documents.

**[15:12]** So like this is the type of concept. If

**[15:14]** I go to a video here, the type is video.

**[15:17]** So we can search over just the videos

**[15:18]** over just the concepts which is

**[15:20]** especially powerful once you get bundles

**[15:22]** that are a lot bigger than this. Again,

**[15:24]** this is just an example here. But then

**[15:26]** we also have all of the optional titles

**[15:28]** in OKF. So title, tags, related videos.

**[15:31]** This is how we link things together,

**[15:33]** right? Like you saw with that other wiki

**[15:34]** I showed earlier, it was just things

**[15:36]** were linked at the bottom. However, this

**[15:39]** now makes it so it's easier to navigate,

**[15:41]** creating a standard for how we are

**[15:43]** linking our entities together. And so

**[15:46]** each one of these are optional. Only

**[15:48]** type is required in OKF. But just

**[15:51]** because you don't always have these

**[15:53]** doesn't mean that your agent won't

**[15:54]** understand it, right? Like if your agent

**[15:56]** is a consumer of OKF, if you gave it the

**[15:58]** spec and taught it to be a consumer,

**[16:00]** it's going to know how to leverage these

**[16:02]** fields for better searching and

**[16:04]** traversing through the knowledge graph

**[16:06]** that we have here. And so then this is

**[16:08]** just all of our information on the piv

**[16:10]** loop. I kept it nice and simple. And

**[16:11]** then also linking to videos as well,

**[16:13]** which maybe is like a little bit

**[16:14]** redundant with related videos. So I

**[16:17]** could probably make this bundle a bit

**[16:18]** better, but I just wanted to have this

**[16:20]** as an initial example. And it is

**[16:21]** something that you can immediately bring

**[16:23]** into your second brain. Just start

**[16:24]** asking questions. Like I'll show you an

**[16:26]** example here in my terminal. So first of

**[16:29]** all, at the top level of my second

**[16:31]** brain, I just asked what bundles do I

**[16:32]** have? It ran a command here. So it used

**[16:35]** that little CLI tool to list out all the

**[16:37]** bundles that I have. And then it told me

**[16:39]** that and then I just asked it a

**[16:40]** question. So not even telling it what

**[16:42]** bundle specifically to look through. I

**[16:44]** said, "What's Cole's single biggest idea

**[16:46]** for getting reliable code out of an AI

**[16:48]** coding assistant?" and it ran four

**[16:50]** commands in total. So first of all it

**[16:52]** decided to read the coal AI coding index

**[16:55]** that's the GitHub that I have for you

**[16:57]** and then based on the index it knew like

**[16:59]** okay let's take a look at the concepts

**[17:01]** here and then from the concepts it's

**[17:03]** like okay the single most important

**[17:04]** thing I don't know what in the index

**[17:06]** told it that but it's like context

**[17:08]** engineering let's read the concept of

**[17:10]** context engineering so we can see the

**[17:12]** progressive disclosure as the agent is

**[17:14]** figuring out where it needs to look down

**[17:16]** to find the answer for me and then we

**[17:19]** get the final answer here So just

**[17:21]** beautiful to watch it work. When we have

**[17:23]** something structured like this, it's so

**[17:25]** easy for it to start with really not

**[17:27]** much context at all and then drill down

**[17:29]** into exactly what we need. That's what

**[17:31]** OKF gives us as a standard. All right.

**[17:34]** So if you're not sold on the idea of

**[17:36]** having a standard for the LM wiki at

**[17:39]** this point, I don't know what to tell

**[17:40]** you. The one critique that I think is

**[17:43]** actually pretty valid with OKF is a lot

**[17:46]** of people are saying that it's too

**[17:47]** simple, right? like there's not a lot of

**[17:49]** value or substance that's actually added

**[17:51]** on top of the Karpathy wiki. So, I've

**[17:54]** I've seen that a few times just as I've

**[17:56]** been doing a lot of research. I mean, I

**[17:57]** put a lot of time into prepping for

**[17:59]** these videos. I think it's kind of valid

**[18:00]** because if we look at like what it's

**[18:02]** really doing on top of the Carpathy

**[18:04]** wiki, it's it's speaking to like exactly

**[18:06]** how you organize your different files.

**[18:09]** Like they they specifically have like

**[18:10]** indexes within the folders and a top

**[18:13]** level index like you saw in my bundle. I

**[18:15]** mean, that's something I didn't really

**[18:16]** have in wikis before. And then we have

**[18:18]** the specific fields in our metadata like

**[18:20]** the type is required. The other ones are

**[18:22]** optional but these are the ones that

**[18:24]** they recommend. Like that's pretty much

**[18:25]** it. It's how we organize and what is the

**[18:28]** metadata. That's pretty much all that we

**[18:30]** actually have in the standard. And so

**[18:34]** like the argument is kind of valid where

**[18:35]** it's like what is it really giving? Like

**[18:37]** there's there's not much there. But I

**[18:39]** think that's also the point, right? Like

**[18:41]** minimally opinionated. It's the bare

**[18:44]** minimum layer that we need on top so

**[18:47]** that we can produce and consume these

**[18:50]** wiks in exactly the same way across

**[18:52]** everyone's agents that lean into OKF.

**[18:55]** Like I think that's actually a good

**[18:56]** thing. I think that's a benefit, not a

**[18:58]** downside. The fact that there's not much

**[18:59]** substance here might seem

**[19:01]** counterintuitive, but I think that is

**[19:03]** actually a good thing. And I encourage

**[19:05]** you just try out the bundle that I have

**[19:08]** for you here. give it the spec and then

**[19:10]** give it this prompt and then just start

**[19:11]** asking questions about AI coding like

**[19:13]** how I use sub aents uh what is the piv

**[19:16]** loop like just start asking and and

**[19:18]** seeing how easy it is for your agent to

**[19:20]** grab those things for you and so that's

**[19:22]** everything that I got for you today on

**[19:24]** OKF really is the future of personal

**[19:26]** agents if you appreciated this video

**[19:29]** you're looking forward to more things on

**[19:30]** AI coding and second brains I'd really

**[19:32]** appreciate a like and a subscribe and

**[19:34]** with that I will see you in the next

**[19:36]** video.
