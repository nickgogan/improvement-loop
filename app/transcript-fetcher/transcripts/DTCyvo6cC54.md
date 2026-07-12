# Transcript: Every Level of a Claude Second Brain Explained

**URL:** https://www.youtube.com/watch?v=DTCyvo6cC54
**Segments:** 1048
**Channel:** Nate Herk | AI Automation
**Duration:** 30:59
**Uploaded:** 2026-06-17

---

## Full Text

Today, I'm going to explain the different levels of building your own AI second brain. You can see here we have a visual of three very different types of data. This one is where we have our context really starting to form and we're starting to see some relationships and we're starting to see some different nodes and entities form. And then as we continue to scale this up, add more knowledge, more knowledge, more relationships, we start to get something that looks a little bit more like this where we have clearly different clusters and inside of all of these nodes we can see how they relate to each other. And then over here we're taking all of those relationships a step farther and we're able to then start to see how everything really pieces together rather than just having files that sort of link back to each other. This is relationship mapping. And so really the idea of an AI second brain has blown up because we're all trying to get as much information out of our heads into our systems as possible. That's the true value. Your moat is your data, it's your IP. But the process of organizing that into a system so that you can use it with a bunch of different AI models and so that it can actually recall things in a way that makes sense rather than just hallucinating or spending a bunch of your time and tokens trying to look through everything. That's the issue. So clearly all of this is my real data and this is what the actual project looks like. It is my Hercule project. I have a bunch of folders and files here and at the end of the day that's basically all it is. It is markdown files that are organized in a way that I understand and that my agents understand. And so yes, I'm going to walk you guys through what I have here and how it works, but I also have this other project where I'm going to show you if you're starting from scratch or if you feel like maybe you're in between level two and three, how we can actually look at the differences and what it might look like to scale up your own systems and start to add context in different ways. So super excited to dig into this today and I don't want to waste any of you guys' time, so let's just start looking at these five levels and how they differ. All right, so every level of a Claude Code second brain and I'm going to be obviously kind of referring to Claude Code a lot, but keep in mind this can be used with any AI model. I use my second brain all the time with Codex as well. I use it with Hermes Agent. This can be used by different agent harnesses because it's just files and folders. So, what is the actual job of a second brain? A lot of people probably define this differently, but the way that I think about it is that it's a place for me to save notes, meeting recordings, ClickUp threads, stuff like that. I can save it there, and then it helps me basically ingest it and get it into the right spots so that it can actually find it later. And so that's really the thing to think about is can your agent find it again, and could you find it again? Because if the answer is no, then you probably don't have the right routing or folder architecture set up, which is what I'm here to talk about today. And one other sort of mindset thing that I want to get out there before we dive into these five levels is that you kind of have to work backwards. You want to reverse engineer based on the question. So this will start to make more sense as we get into it, but really what you should be thinking about is how do I want to use this data in the future? Because how it's going to be accessed and recalled determines the way that you put it in in the first place. For example, a basketball hoop and a basketball. We know what shape the hoop is, and we know that the ball needs to go through. So why would we ever design the ball to be a giant square? Because it just wouldn't fit through the hoop, so that would make no sense. So you need to start with the end in mind a little bit. Once again, I will show you exactly what I mean by that as we continue on. Because remember, we're trying to get to the point where your second brain knows everything about your business, about you, your relationships. It knows everything to the point where it probably can recall stuff better than you can because it has a better memory, and it can search through things way faster than you can. So we've got five different levels to talk about, and they each kind of have different questions. So level one is, can you find the file or the info by looking for an exact word or name? Level two is, can you pull everything on a certain topic together? Level three is, I search for different words than I wrote, so semantic search, you're searching for meaning rather than an exact word match. And then trace relationship chains. Can you ask about topic X, and then trace that all the way back to topic A? And then level five is just kind of making this whole second brain thing super autonomous to the point that you don't even have to think about it. And by the way, this isn't me saying that number five is best. I have some arguments about why I do not currently sit on level five. The point I'm trying to make here is each level is different and you want to find the simplest level or the lowest level that actually fits your needs. If you don't have a pain point in your system, then I don't really think there's a need to go experiment or develop a new sort of, you know, architecture. If there's not pain, then why create more? Okay, so level one is pretty simple and this is where you always start. So you start with a claw.md or if you're using codex or something, you would start with an agents.md. But you start with a claw.md which is kind of, you know, that gets loaded up. That's almost like the system prompt for that session for that project. And then you've just got a bunch of folders and files. But the key part there is the claw.md is kind of treated as a router. So yes, you've got some, hey, this is your role, here is what's important, but you also have routing rules. If you ever need to find information about me personally, look in this folder. If you need information about our quarter one priorities, look in this folder. Because if you've ever had a point where you ask Claude to do something and then it asks you, hey, can you give me more info? I don't know what you're talking about, but you know there's files and folders in your project, then you probably just didn't give Claude the knowledge to go look there. It's not just going to go search your entire code base automatically. I mean, you wouldn't want it to do that cuz it's going to waste your time and your tokens. So if it doesn't know if something lives somewhere, then it's probably not going to be able to find it. So when this is properly set up, you will stop having to re-explain things, you will talk to it and it will just know where to go look and why. But the problems with this is that if it grows too big, it can start to get messy and feel ignored. And this is typically more of like an exact words type of search depending on the way that you route. So if I open up my um example project here, let's open up level one. So in level one, what you can see, pretend this is its own Claude project, we've got a claw.md. So let me click into that. We can see here it says, this file loads automatically every time you open Claude Code in this folder. It is the one file that tells the AI who you are, how you work, and where things live. At level one, this file plus a few folders is your entire second brain. So, here's kind of like that basic knowledge, and then right here, it's this simple, where things live. In the context folder, always true background about you and how you work, read this first. Projects, decision log, and that's basically it. So, right here you can see there's a context folder, we have an about me file, which you could grow. We have stack and conversations file. We have decisions, so this is a decision log where you can have your Claude at MD always append new decisions and dates whenever you make a big change to your project or to your life or to your business. And then we have projects, so this is where you could have a markdown file or even folders within the projects for all of your ongoing projects, all of your ongoing clients, whatever it is, however you want to organize it, that's where you can have some projects. And you can even start to organize these things by dates if you want. So, if you want to just have one that's for like May, and then you have all of those stuff, and you have one for June. The thing that I really want to stress here with level one, and the thing that I answer a lot in my community in the comments, is that there is not yet a standard way that has been proven the best way to set up your projects or your second brain besides some of the most common things like your contexts and your Claude at MD and your, you know, whatnot. But, the point I'm trying to make there is don't see what I do and think that that's the right way, or see what someone else you watch does and think that that's the only right way. All that matters is do you have proper routing in place, and does it make sense to you, and does it make sense to your AI? Okay, so let's say I have my Hercule project right here, and I need to find something in here, but I can't ask AI for some reason. What I need to find is easy because I understand the drill downs. You know, I understand my base folders, and let's say I'm looking for the HTML slide deck I built for my ranking Claude code features video. I would come into here and I say, okay, I know that's a project, so I'll go there. Within my projects, I've got another project for YouTube videos, I'll open that up. And now I know I made this video right here, May 30th Claude code top 50 features. In here, I have the actual tier list deck, and when I open that up, now I have the slide deck, and not only can I find it easily, but my agent can find it because it all makes sense and I have routing rules. Real quick, guys, if you're watching this video, you're probably interested in building your own AI operating system. Lucky for you, I have a full free course on that in my free school community. The link for that is down in the description. Join the free school community, hop in here, take the 7-day challenge, build your own AI operating system, and apply these principles into building your second brain, which will make your AI operating system even more powerful. So, link's in the description. Let's get back to the video. Awesome. Okay, so that is how you start. Now, as you move up to level two, you might be able to start to work in some things like the LLM Wiki, which is what I've got set up for a few different things. This is the whole Karpathy LLM Wiki, which I did make a full video about if you want to check that out. I'll tag that right up here. But, this is when you start to have more files and and they start to take a bit of a different shape, and you want to organize them together in a bit of a different way. So, it could be really good for researching all on a certain project. It could be really good for, you know, a few of the ones that I've got set up is my YouTube transcripts all live in their own Wiki. I've got all of like my meeting transcripts that live in their own Wiki. So, for example, this is the Obsidian view of my Wiki for all of my YouTube video transcripts. You can see here if I go to Wiki, you can see there's main concepts like agentic workflows, AI coding market, context window. And all of these in here start to relate back to other tools and concepts and videos and stuff like that. So, we've got the sources, we've got platforms, we've got um context management techniques. And all of this was auto-created by our Claude code when I told it to ingest this YouTube transcript into our Wiki. So, I'm not going to dive super super deep into all of this right now, but definitely check out that YouTube video I linked. Now, what else is cool about this is this transcript Wiki actually lives within my main Herc 2 project. So, here's Herc 2. If I go right here to Other Worlds, and then I go down to YouTube OS, and I click into the transcript Wiki right here, this is what we were just looking at in Obsidian. We could see the concepts, we could see the comparisons, we could see the sources, techniques. This is what we were looking at in Obsidian. So, all Obsidian is is it basically just visualizes your markdown files. You see here, wiki, concepts, comparisons, techniques. This is what we were just looking at. All we get now is we just get a visual view of all that. And so, the reason I wanted to bring that up as well is because I think a lot of people obviously get pretty infatuated by that visual view. And obviously, I started the video with that because I think that's what hooks a lot of people in. But, all that really matters is can your system grab that and give it to you? If you are a visual person and you really want that view, then by all means, install Obsidian and set it up. It's super easy. But, I'm saying that you don't always need that visual layer if it's not beneficial to you. I hardly ever open Obsidian, just to be honest, because I know that it all lives here and I know that my second brain and my OS can find all of that. So, anyways, in level two here, let's look at this. It's very similar in shape to level one. It's just building on top of it because now we have our claw.md, which starts to route to some other things because it routes to the wiki and it still routes to contexts, projects, decisions, but it's also routing to references and memory.md. So, we're just starting to add a bit more of these routing rules inside of the claw.md. We can grow the context, we can grow the decisions, we can grow projects and references, and we can also start to get this idea of memory. And what's really cool about this is you can turn on auto memory in Claude Code. And the AI will basically start to write this file and update it on its own. So, you don't have to think about it. If you come in here and you do {slash} memory, it'll say auto memory on or off. And if it's off, if you want to turn that on, just turn it on. And now, one thing to think about is I mentioned earlier that we want to make our second brains tool agnostic. And this is one thing that's pretty specific about Claude Code is it uses claw.md and it uses this memory.md and it keeps that updated on its own. So, if you wanted to move this over to Codex, what you would do is you would first of all transition your claw.md. You'd make a copy of it called agents.md. As you can see here in my Herc 2, I've got my, if I scroll down, claw.md right here, and then I've got agents.md right here. And they're essentially the exact same file. Just so Codex can read this one and Claude code can read this one. But because Claude code keeps that auto memory, all you need to do is make sure you have that memory.md file and just tell Codex, "Hey, by the way, for memories, look in our memory.md file." It's all about the routing there. Anyways, just felt like that was important to throw out. But at a certain point, when you have these, you know, wikis, they do start to degrade a little bit. Because what's what's great about them is that they have indexes, right? So, when your AI starts to look in the wiki, it knows, "Okay, if the user's asking about a genetic workflow, I'm probably going to start here. And then from here, I'm going to drill down and read this to see what else is important to them." Maybe they're asking about the WATC framework, and then I can drill into that. And maybe from there, I need to learn a little bit more about the Claude at MD system prompt, and then I will drill into that. So, there are relationships here a little bit, but this isn't the same as like semantic relationships or knowledge graph relationships that have more meaning. This is more about just actually following a trail and reading the page in its entirety. And I'll be fully honest with you guys, I pretty much sit my entire PERC 2 project in this level, in level two. Because this has been working really well for me. Like I mentioned earlier, I haven't felt a pain yet big enough to switch over to level two. And here's what I meant by that. My wiki has links, isn't that a knowledge graph? Not exactly. Because this doesn't have connections of how they are related, like this is endorsed by this or this has cron to here. These just have connections because it's like a a see also. It's like backlinks. So, they're very similar, and yes, they can achieve a similar effect, but it's still a little bit different. Anyways, let's take a look at level three, which is where you start to do things like semantic search. Whether you do that in Obsidian, whether you do that with Pine Cone or Supabase, however you start to grab the actual semantic search, that is what level three is. And so, just as a quick visual for you guys, let's take a look at this quadrant cluster of images. So, every one of these vector points is an image. And what we see in here is the payload is stuff like the file name, the URL, the name of the author or the artist, and the URL. But, we don't actually see like what's in the image. We don't get a description. So, what we have to do is we have to organize these images by meaning or by similarity. So, when I open up this graph and we start to visualize the stuff here, what you see is that we have this main image, these owls, these kind of like I don't even know. Um it's a very trippy style, like hallucinogenic style. Anyways, then this one is kind of similar, right? It's got those colors, it's got the paints. This one is also similar, but they're not the same. They just share similarities. And as we start to expand these more and more, we can start to get into different styles. So, this one has like some creepy eyes and mushrooms or whatever. This one is kind of more down that fantasy lane. And as we start to build out more of these relationships and meanings, we can expand and grow away from them. And so, Quadrant really just gives you a visualization here. I mean, it's a it has clusters and vector store. But, [snorts] the reason I pulled this up as a demo is just because we start to see the actual relationships form here based on meaning. And that's what's important about semantic search is that we're no longer doing keyword matching, we're searching based on meaning. So, here in my YouTube transcript second brain, if I go to the smart lookup over here, this is very different from just the regular search. So, for example, if I search here for um feedback, let's say. We're actually doing a match on the word feedback, and it's only showing me where that word actually appears inside of our second brain. But, if I come over here in the smart lookup and I search for feedback, we are getting matches that have things in here that mean feedback. So, live test results, cloud code skills, which was uh talking about evaluations and stuff. So, there's a big difference between keyword matching and semantic search, you know, similarity matching. This one over here is saying X equals X, and this one is saying X is similar to X, Y, and Z. And so, this all just goes back to vector databases. I've talked so, so much about vector databases, so I'm not going to dive super deep in. I've got so many resources on my channel. But basically, what it is is we take a document, so let's just say YouTube transcript, we chunk it up, and then each chunk is ran through an embeddings model. And the embeddings model puts that chunk of text onto like a three-dimensional space where space is related to meaning. And so it decides, okay, this chunk is about a company, so we're going to put it up here. This chunk is about finances, so it's going to go here. And we start to see these vectors form near other similar vectors. Now, do you guys remember how I said earlier, like you want to think about how is the data going to be used? What type of questions are you going to ask? This is a reason why that's so important. So think about this. Let's say I put my meeting transcript of March 5th meeting into my second brain. And I put those in as, you know, vectorized chunks. So let's say when I vectorize that meeting, we actually get, you know, like 20 chunks. It actually creates 20 chunks, or however many that is. And then when I say, "Hey, Mr. AI agent, can you summarize the meeting on March 5th?" It will basically search for March 5th meeting summary, and it will pull chunks that are similar to March 5th meeting summary. And then even if it gets the right chunks, it's going to only summarize those five chunks. It's not able to look at the entire meeting summary, or sorry, like meeting transcript in entirety. So it doesn't really know a summary. It might be missing a lot of key information. Now yes, there are things you can start to play with there like metadata and other things like that to make these results better, but at the end of the day, people kind of assumed that a vector database was some magic solution where it could always pull back what you need, but that is very false. And I mean, think about it like this. Let's say we have a table, and we say, "Hey, which week did we have the highest sales?" Okay, the agent looks for highest sales, it maybe grabs this chunk outlined in gray of data, and then it looks at, "Okay, week six here was the highest sales, so that must be the answer." But in reality, you can see week 14 was higher, week 19 was higher. So when you need something that has actual full context, then you can't do the vector database chunking. That's where you'd rather just have a markdown file of March 5th, and then all this agent would have to do is read that entire markdown file and then give you a summary. And that's just going to be more accurate. So, in this project, if we open up level three, you can see it's very similar because you can still have context files, decision files, you can still have all that, and then you might identify, "Okay, actually, this one specific unit of my business, maybe my YouTube transcripts, maybe I want just that to be a vector database, but I still want my context and my projects and my decisions to be markdown files." So, another point I'm trying to make here is just because you have a second brain, and just because you have a massive, you know, folder here with a bunch of folders and files, doesn't mean that the whole folder needs to be one style. It doesn't mean that everything needs graph rack. It doesn't mean that everything is just LLM Wiki. It means that you're able to decide, based on the type of data and the way you use it, how can you structure this specific folder in the way you want it. So, here we have a vector index folder, and we click on the house search works. It works by chunking, embedding, search, hybrid, re-ranking. There's some things you can get really, really nitty-gritty on when it comes to semantic search. But what vector retrieval is really, really good at is looking at tons and tons of data, typically just like a lot of text, and when you need a very specific answer, something that's very similar. So, if you had a thousand rules that you needed to store, and you basically said, "Hey, um can you remind me what rule 17 was?" That might be a really good use case for vector search because it's able to search for rule 17, pull in those chunks, and just give you a little snippet because it would be a waste of time and tokens for your agent to read the entire markdown file of all 1,000 rules if you just needed rule 17. So, that's kind of the difference there. Like I said, I've got so many videos on vector stuff on my channel, but really you could say, "Hey, to your cloud code agent, I have this data. Here's how I want to use it. Do you think this would be better for now as markdown files, or should I do semantic search? Like what would actually make more sense here?" And it will help walk you through the way that you should actually set that up. So, now I hope you guys are starting to understand why I said, you know, moving up on or I'm sorry, like moving up on levels, moving down doesn't necessarily mean better. It's all about figuring out what is the pain point with what you're currently doing and where would a different level help you out and fix that pain point. Okay, so now let's take a look at level four. This is where we start to get into like knowledge graphs and relationship graphs, which typically are going to be the most complex and sometimes the most expensive as well. If you're doing it on a certain platform, you could always use open source software, but anyways, knowledge graphs. And I also want to be up front. I've played with these a lot, but I do not actually use these on the day-to-day because I found out just other ways to use routing files and wikis that fit my needs. Now, my work is very different than what a lot of you guys' work may be. Mine is very project-based and it is very, you know, content-heavy. I don't have a massive CRM to manage with a bunch of different businesses and clients, you know? And if I did, maybe a knowledge graph would make a lot more sense and it probably would. But typically, the cool part about that is if you identify that you needed a knowledge graph, let's say for all your projects, you needed you wanted to put all of this in a knowledge graph, the data probably already exists here. And that's the thing about building out these relationships in your knowledge graph is that the system, whatever software you use, is typically going to be pretty good at embedding that and creating that. But the problem that you have to solve is you have to give it enough data. And so, one thing that I really like to do is I like to have these brainstorm sessions, as you can see. And what I do with these brainstorm sessions is I use a skill called Grill Me. So, if you see here, I have a skill called Grill Me, which I originally got from Matt Pocock. I customize it a little bit. I'll leave the skill for Grill Me in my free school community. The link for that is down in the description. All you have to do is hop in here, go to classroom, click on all YouTube resources, and you can find all the skills and everything like that. But the skill, what that does, is it basically just grills me. It interviews me relentlessly about a certain topic and it creates a brainstorm file here. It only stops when it knows everything about it. So, if you wanted to start building up a knowledge graph for all your clients and businesses, just say "Grill me about client A. Grill me about client B. Grill me about business A." And it would just ask you questions and you can feed it files. You can give it stuff. You can feed it in transcripts. You can feed it in, you know, contracts, whatever it is. And that's how you can start to form a lot of data. Hey guys, me again. Real quick, I'm editing this video and I realized that I needed to throw out one thing here, which is that obviously, if you're putting all of this data and you're sending it all to Anthropic, to Claude models, then that's not private. So, if you feel comfortable with that, that's fine. I am putting a lot of my data in there and it is my business stuff and that's what I'm doing. But, if you don't feel comfortable with that or you, you know, don't want to send client data, of course you don't, then maybe you want to do that through open-source models and maybe Claude code isn't where you have the second brain that has every single piece of information about you and your business and your client's business. So, the point I'm trying to make here is just this is what I'm doing. I'm obviously aware of the fact that my data goes to Anthropic when I process it through Claude. And if you guys are doing that, then you should also be aware of that. But, there are other options if you can't do that. So, I wanted to throw that out there. I am planning to make a ton of videos here soon about local AI and open-source models and all this stuff cuz it's a really, really exciting space that I think is going to start becoming bigger and bigger. So, yeah, keep that in mind. Back to the video. I think sometimes that's a misconception about how I got here and how people build their own AI OS or second brain is that they think the problem is the system not retrieving it great, which sometimes it is, but sometimes it seems like the bigger problem is getting everything out of your brain into the system. So, before you blame AI, take a look at your folders and files and say, "Is this actually holistic? Is this Does this have all the nuance that I have in my brain?" Anyways, from there, when you open up level four, you can see that it's it's, you know, very similar still. We're just adding on a few things. You can see here we've added an agents.md, which is the exact same as the claude.md. And what else is cool is you can literally just reference inside of your claude.md at agents.md and then you can delete all this because this basically just like injects that file into here. But I just wanted to show that. But anyways, you can see we're still following the same principles. We have a wiki. We've also added a knowledge graph layer. We've still got the same where things live with the routing with all these just regular folders and boring markdown, but boring is beautiful. You can see that our memory is still here. It's starting to grow, and we just keep building on top of this. So what one thing we added here as you can see was our knowledge graph folder. And so what happens here is we get different entities, right? So like we can see okay Jordan is a person. Acme is a company. And then we can start to form relationships between all these things. So Jordan works at Acme. Acme is endorsed by Postpilot. Postpilot is a competitor of Cadently. And it starts to build out not only these entities, but it shows you how they're all related. And so that's why when I said that I really like using, you know, this um what's it called? LLM Wiki is because I have enough of that feel of all these relationships because I've put so much time and effort into ingesting these in the right way and giving it context. The thing about this one is that it has to read every single file it wants. Maybe it was looking at AI video production and all it needed to know was ElevenLabs, it still would have read this entire file first. And so that's where sometimes the knowledge graph is actually more lightweight in that sense. And this is the example I showed at the beginning of the video where we have Lightrag. And forgive me, I'm going to have to blur some of this stuff out because this is like legitimately my entire second brain in our business. But as I really zoom in here and this kind of slows down my computer because there's so much. But what you'll notice is that we actually start to get relationships. I probably shouldn't have done this with so much data, but you can see like we have this collaborates with that. We have this builds that. And so if I really started to open up all of these little you know, circles, we could see what was going on and how they're all related. We could see that our 7-day AI challenge it was provided from YouTube. It connects to the onboarding process of AIS Plus. It was developed by Aiden. And so we can basically follow around these relationships, as you see. And even though it's pretty much the same data that you see here in Obsidian, we're not getting that same level of relationships between these different entities. So, anyways, if you guys want to see, you know, a full breakdown video on something like Logseq or um Graphir or all the other solutions that there are out there for more of a knowledge graph relationship graph, then let me know. But, that is kind of the difference there. So, if you don't need those sort of relationship chains, and you're not worried about that semantic type of relationships, then you probably don't need to use something like a knowledge graph. And then, level five, we have more of the always-on Brain OS, and something like Gbrain. Garry Tan, CEO of Y Combinator, he created this thing called Gbrain, which pairs really well with G stack. But, Gbrain is kind of the idea of everything we've talked about here. Wikis, routing, relationships, tools. But, Gbrain has kind of that always-on element, because it is like constantly syncing and refreshing memories and adding more stuff. So, adding in Gbrain to something like a Hermes agent would be really, really good. You could still do it in cloud code, but you'd have to handle those crons and get all that stuff set up, which is why I don't currently run Gbrain at the moment, but I have been playing around with it with my Hermes agent. So, anyways, the point here is that it's very similar to everything else we've just talked about. It's just having that auto-updating feel, more of the autonomous, always-on feel. But, I will say, another thing that I kind of that kind of scares me about that is you have this whole dilemma of, you know, when do you have too much context? And when does it get to the point where it's actually doing more damage than it's doing good? And the reason I bring that up is because I am in complete control of what my second brain ingests. I will run a skill to go grab all of my meeting transcripts from the week. I will say, "Hey, here's something. Help me figure out like how many brains are about this, and then let's ingest it together." And for me, I really like being in that control, because in my mind, there's a big difference between a few types of data. If you guys remember in my like AI OS videos, I've talked about the four C's. So, context, connections, capabilities, and cadence. And for the second brain, I mainly think about it as just these first two. So, context and connections. And so, when I think of context, that's stuff like, you know, what my business has done. So, if I come into here, into my my second brain, and you can see here if I go to um up at OTAs. So, OTAs are basically just our projects for the quarter. And so, here I can see all the Q1 ones, right? I can look at all those and I can click at them and see decisions that we've made in the statuses. And I can also see Q2 OTAs. So, I can see what's going on here. And my second brain's able to see that because that has been basically those are locked in decisions. This is what we're doing this quarter, and then I'm updating the statuses of that stuff. So, that's like context. That's what's going on in the business. But when it comes to connections, if I go back to this, this is more of like the real data that isn't as evergreen. This is stuff that changes. This is like Slack threads. This is emails. This is a customer data. And that type of data you don't want to ingest into a second brain because that's just noise then. Then you have to go back every month and like delete old stuff. So, the way that I like to think about my actual second brain is stuff that I'm not going to delete. This is stuff that is like, okay, in a year, will it be good for me to have this memory in here? Yes. Otherwise, it's just adding noise. So, when you're adding data into your project, think about it like the context and connections. Think about if this is kind of like more evergreen, holistic data, or if this is more things that are going to change next week. So, you probably shouldn't pull it in, but you should make sure that your second brain has access to go grab it. So, that way if I said to my second brain, "Hey, can you just take a look real quick at what John and I were talking about last week about, you know, OTA number seven?" It would first go to our OTA file, and it would search through there and it it would try to find it there. If it couldn't find it there, it would look through the Wiki and it would look through meeting transcripts and see what we talked about there. And if it couldn't find it there, it would finally go to ClickUp itself, pull real data in from me and John's conversations, and see if the answer lived there. And so, that in my mind is still a second brain because I'm able to ask a vague question, and the second brain knows exactly where to look in what order to find that real-time data, and then give me back the answer that I need. That's the question I ask myself is, "Does this thing understand where my data lives and where to look, and can to give me accurate answers. So, as far as finding your level, remember your whole project doesn't fit into one level. Maybe this folder's level two, maybe this folder's level four, maybe this folder's level three. Here's some things to think about. If you were re-explaining your setup and you need to find things by exact words or files, look at level one. If you have 30 plus notes and you keep forgetting what's in them, look at level two. That's where you sort of like ingest them and get that wiki with relationships. If your project is just completely whiffing on notes that you know exist and your routing isn't working, then maybe you want to look for something more like a semantic search that doesn't rely on an exact word level match. If you're looking for relationships and to be able to follow chains of questions and thoughts, then you probably want to look for something like a knowledge graph. you're running agents offline and you've got so much data and you want to sync up a bunch of Hermes agents together, then you probably are looking for something like level five, something like G brain. And another topic that I get some questions about, which I'm not going to fully address in this video, but I will briefly bring up is the fact that you are building your own second brain OS. So are other people on your team. The next question is, how do you actually make sure that everyone's data is syncing together and how do you have more of like your team second brain? There's a lot of different ways to solve that. I think once again, it's not an issue of, oh, do we use Google Drive or Notion or GitHub or cloud plugins? I think the issue to figure out with your team is how do we actually make sure that we all have it shift so that this stuff is actually useful and not just noise. How do we make sure that process owners are updating their docs and syncing their stuff there? How do we make sure that other people are pulling from that rather than always just pinging the same people for questions and answers all the time? I think the adoption and the change management question is the bigger one. The tech and the way it actually functionally rolls out is a little bit less. But what I do know is that you getting set up with your own first and understanding how it works, how you should route, how you should make the decisions of where the data should live, that's the first hurdle. You can only solve the team-wide problem once you feel comfortable about the way you run it every single day and then it works for you. That is going to do it for today. Like I said, you guys can grab all the skills and everything that you need from this free community. The link for that is down in the description. I will also include the slide deck if you guys are interested in flipping through. So, if you guys enjoyed the video or you learned something new, please give it a like. It helps me out a ton. And as always, I appreciate you guys making it to the end of the video, and I will see you all in the next one. Thanks, guys.

---

## Timestamped Segments

**[0:00]** Today, I'm going to explain the

**[0:00]** different levels of building your own AI

**[0:02]** second brain. You can see here we have a

**[0:04]** visual of three very different types of

**[0:07]** data. This one is where we have our

**[0:08]** context really starting to form and

**[0:10]** we're starting to see some relationships

**[0:12]** and we're starting to see some different

**[0:13]** nodes and entities form. And then as we

**[0:15]** continue to scale this up, add more

**[0:17]** knowledge, more knowledge, more

**[0:18]** relationships, we start to get something

**[0:20]** that looks a little bit more like this

**[0:21]** where we have clearly different clusters

**[0:23]** and inside of all of these nodes we can

**[0:24]** see how they relate to each other. And

**[0:26]** then over here we're taking all of those

**[0:27]** relationships a step farther and we're

**[0:29]** able to then start to see how everything

**[0:31]** really pieces together rather than just

**[0:32]** having files that sort of link back to

**[0:34]** each other. This is relationship

**[0:37]** mapping. And so really the idea of an AI

**[0:39]** second brain has blown up because we're

**[0:41]** all trying to get as much information

**[0:42]** out of our heads into our systems as

**[0:45]** possible. That's the true value. Your

**[0:47]** moat is your data, it's your IP. But the

**[0:49]** process of organizing that into a system

**[0:51]** so that you can use it with a bunch of

**[0:52]** different AI models and so that it can

**[0:54]** actually recall things in a way that

**[0:56]** makes sense rather than just

**[0:57]** hallucinating or spending a bunch of

**[0:58]** your time and tokens trying to look

**[1:00]** through everything. That's the issue. So

**[1:02]** clearly all of this is my real data and

**[1:04]** this is what the actual project looks

**[1:05]** like. It is my Hercule project. I have a

**[1:07]** bunch of folders and files here and at

**[1:08]** the end of the day that's basically all

**[1:10]** it is. It is markdown files that are

**[1:12]** organized in a way that I understand and

**[1:13]** that my agents understand. And so yes,

**[1:15]** I'm going to walk you guys through what

**[1:16]** I have here and how it works, but I also

**[1:18]** have this other project where I'm going

**[1:19]** to show you if you're starting from

**[1:20]** scratch or if you feel like maybe you're

**[1:23]** in between level two and three, how we

**[1:24]** can actually look at the differences and

**[1:26]** what it might look like to scale up your

**[1:28]** own systems and start to add context in

**[1:30]** different ways. So super excited to dig

**[1:32]** into this today and I don't want to

**[1:33]** waste any of you guys' time, so let's

**[1:35]** just start looking at these five levels

**[1:36]** and how they differ. All right, so every

**[1:39]** level of a Claude Code second brain and

**[1:41]** I'm going to be obviously kind of

**[1:42]** referring to Claude Code a lot, but keep

**[1:43]** in mind this can be used with any AI

**[1:46]** model. I use my second brain all the

**[1:47]** time with Codex as well. I use it with

**[1:48]** Hermes Agent. This can be used by

**[1:50]** different agent harnesses because it's

**[1:52]** just files and folders. So, what is the

**[1:55]** actual job of a second brain? A lot of

**[1:57]** people probably define this differently,

**[1:58]** but the way that I think about it is

**[1:59]** that it's a place for me to save notes,

**[2:02]** meeting recordings, ClickUp threads,

**[2:04]** stuff like that. I can save it there,

**[2:06]** and then it helps me basically ingest it

**[2:08]** and get it into the right spots so that

**[2:10]** it can actually find it later. And so

**[2:12]** that's really the thing to think about

**[2:13]** is can your agent find it again, and

**[2:16]** could you find it again? Because if the

**[2:17]** answer is no, then you probably don't

**[2:19]** have the right routing or folder

**[2:20]** architecture set up, which is what I'm

**[2:22]** here to talk about today. And one other

**[2:24]** sort of mindset thing that I want to get

**[2:26]** out there before we dive into these five

**[2:28]** levels is that

**[2:29]** you kind of have to work backwards. You

**[2:30]** want to reverse engineer based on the

**[2:33]** question. So this will start to make

**[2:34]** more sense as we get into it, but really

**[2:36]** what you should be thinking about is how

**[2:38]** do I want to use this data in the

**[2:39]** future? Because how it's going to be

**[2:42]** accessed and recalled determines the way

**[2:44]** that you put it in in the first place.

**[2:46]** For example, a basketball hoop and a

**[2:48]** basketball. We know what shape the hoop

**[2:51]** is, and we know that the ball needs to

**[2:52]** go through. So why would we ever design

**[2:54]** the ball to be a giant square? Because

**[2:58]** it just wouldn't fit through the hoop,

**[2:59]** so that would make no sense. So you need

**[3:00]** to start with the end in mind a little

**[3:02]** bit. Once again, I will show you exactly

**[3:04]** what I mean by that as we continue on.

**[3:06]** Because remember, we're trying to get to

**[3:07]** the point where your second brain knows

**[3:10]** everything about your business, about

**[3:11]** you, your relationships. It knows

**[3:13]** everything to the point where

**[3:14]** it probably can recall stuff better than

**[3:16]** you can because it has a better memory,

**[3:18]** and it can search through things way

**[3:19]** faster than you can. So we've got five

**[3:21]** different levels to talk about, and they

**[3:23]** each kind of have different questions.

**[3:25]** So level one is, can you find the file

**[3:27]** or the info by looking for an exact word

**[3:29]** or name? Level two is, can you pull

**[3:31]** everything on a certain topic together?

**[3:33]** Level three is, I search for different

**[3:35]** words than I wrote, so semantic search,

**[3:37]** you're searching for meaning rather than

**[3:38]** an exact word match. And then trace

**[3:41]** relationship chains. Can you ask about

**[3:44]** topic X, and then trace that all the way

**[3:46]** back to topic A? And then level five is

**[3:49]** just kind of making this whole second

**[3:50]** brain thing super autonomous to the

**[3:52]** point that you don't even have to think

**[3:53]** about it. And by the way, this isn't me

**[3:55]** saying that number five is best. I have

**[3:57]** some arguments about why I do not

**[3:59]** currently sit on level five. The point

**[4:00]** I'm trying to make here is each level is

**[4:02]** different and you want to find the

**[4:04]** simplest level or the lowest level that

**[4:06]** actually fits your needs. If you don't

**[4:08]** have a pain point in your system, then I

**[4:10]** don't really think there's a need to go

**[4:12]** experiment or develop a new sort of, you

**[4:15]** know, architecture. If there's not pain,

**[4:17]** then why create more? Okay, so level one

**[4:20]** is pretty simple and this is where you

**[4:22]** always start. So you start with a

**[4:23]** claw.md or if you're using codex or

**[4:25]** something, you would start with an

**[4:26]** agents.md.

**[4:28]** But you start with a claw.md which is

**[4:29]** kind of, you know, that gets loaded up.

**[4:31]** That's almost like the system prompt for

**[4:32]** that session for that project. And then

**[4:34]** you've just got a bunch of folders and

**[4:35]** files. But the key part there is the

**[4:37]** claw.md is kind of treated as a router.

**[4:39]** So yes, you've got some, hey, this is

**[4:41]** your role, here is what's important, but

**[4:43]** you also have routing rules. If you ever

**[4:45]** need to find information about me

**[4:46]** personally, look in this folder. If you

**[4:48]** need information about our quarter one

**[4:49]** priorities, look in this folder. Because

**[4:51]** if you've ever had a point where you ask

**[4:52]** Claude to do something and then it asks

**[4:54]** you, hey, can you give me more info? I

**[4:56]** don't know what you're talking about,

**[4:57]** but you know there's files and folders

**[4:58]** in your project, then you probably just

**[5:00]** didn't give Claude the knowledge to go

**[5:03]** look there. It's not just going to go

**[5:04]** search your entire code base

**[5:06]** automatically. I mean, you wouldn't want

**[5:07]** it to do that cuz it's going to waste

**[5:08]** your time and your tokens. So if it

**[5:10]** doesn't know if something lives

**[5:11]** somewhere, then it's probably not going

**[5:13]** to be able to find it. So when this is

**[5:14]** properly set up, you will stop having to

**[5:16]** re-explain things, you will talk to it

**[5:18]** and it will just know where to go look

**[5:19]** and why. But the problems with this is

**[5:21]** that if it grows too big, it can start

**[5:23]** to get messy and feel ignored. And this

**[5:25]** is typically more of like an exact words

**[5:27]** type of search depending on the way that

**[5:29]** you route. So if I open up my um example

**[5:32]** project here, let's open up level one.

**[5:34]** So in level one, what you can see,

**[5:35]** pretend this is its own Claude project,

**[5:37]** we've got a claw.md. So let me click

**[5:39]** into that. We can see here it says, this

**[5:41]** file loads automatically every time you

**[5:43]** open Claude Code in this folder. It is

**[5:44]** the one file that tells the AI who you

**[5:46]** are, how you work, and where things

**[5:47]** live. At level one, this file plus a few

**[5:49]** folders is your entire second brain. So,

**[5:51]** here's kind of like that basic

**[5:52]** knowledge, and then right here, it's

**[5:53]** this simple, where things live. In the

**[5:55]** context folder, always true background

**[5:58]** about you and how you work, read this

**[5:59]** first. Projects, decision log, and

**[6:01]** that's basically it. So, right here you

**[6:03]** can see there's a context folder, we

**[6:04]** have an about me file, which you could

**[6:06]** grow. We have stack and conversations

**[6:08]** file. We have decisions, so this is a

**[6:10]** decision log where you can have your

**[6:11]** Claude at MD always append new decisions

**[6:14]** and dates whenever you make a big change

**[6:16]** to your project or to your life or to

**[6:17]** your business. And then we have

**[6:19]** projects, so this is where you could

**[6:20]** have a markdown file or even folders

**[6:22]** within the projects for all of your

**[6:23]** ongoing projects, all of your ongoing

**[6:25]** clients, whatever it is, however you

**[6:26]** want to organize it, that's where you

**[6:28]** can have some projects. And you can even

**[6:29]** start to organize these things by dates

**[6:31]** if you want. So, if you want to just

**[6:32]** have one that's for like May, and then

**[6:34]** you have all of those stuff, and you

**[6:35]** have one for June. The thing that I

**[6:36]** really want to stress here with level

**[6:37]** one, and the thing that I answer a lot

**[6:39]** in my community in the comments, is that

**[6:42]** there is not yet a standard way that has

**[6:44]** been proven the best way to set up your

**[6:46]** projects or your second brain besides

**[6:48]** some of the most common things like your

**[6:49]** contexts and your Claude at MD and your,

**[6:51]** you know, whatnot. But, the point I'm

**[6:52]** trying to make there is

**[6:55]** don't see what I do and think that

**[6:57]** that's the right way, or see what

**[6:58]** someone else you watch does and think

**[6:59]** that that's the only right way.

**[7:02]** All that matters is

**[7:03]** do you have proper routing in place, and

**[7:06]** does it make sense to you, and does it

**[7:08]** make sense to your AI? Okay, so let's

**[7:09]** say I have my Hercule project right

**[7:11]** here, and I need to find something in

**[7:13]** here, but I can't ask AI for some

**[7:14]** reason. What I need to find is easy

**[7:16]** because I understand the drill downs.

**[7:18]** You know, I understand my base folders,

**[7:20]** and let's say I'm looking for the HTML

**[7:21]** slide deck I built for my

**[7:24]** ranking Claude code features video. I

**[7:26]** would come into here and I say, okay, I

**[7:27]** know that's a project, so I'll go there.

**[7:29]** Within my projects, I've got another

**[7:30]** project for YouTube videos, I'll open

**[7:32]** that up. And now I know I made this

**[7:34]** video right here, May 30th Claude code

**[7:37]** top 50 features. In here, I have the

**[7:39]** actual tier list deck, and when I open

**[7:41]** that up, now I have the slide deck, and

**[7:43]** not only can I find it easily, but my

**[7:44]** agent can find it because it all makes

**[7:46]** sense and I have routing rules. Real

**[7:47]** quick, guys, if you're watching this

**[7:49]** video, you're probably interested in

**[7:50]** building your own AI operating system.

**[7:52]** Lucky for you, I have a full free course

**[7:54]** on that in my free school community. The

**[7:55]** link for that is down in the

**[7:56]** description. Join the free school

**[7:57]** community, hop in here, take the 7-day

**[7:59]** challenge, build your own AI operating

**[8:01]** system, and apply these principles into

**[8:03]** building your second brain, which will

**[8:04]** make your AI operating system even more

**[8:06]** powerful. So, link's in the description.

**[8:07]** Let's get back to the video. Awesome.

**[8:08]** Okay, so that is how you start. Now, as

**[8:11]** you move up to level two, you might be

**[8:13]** able to start to work in some things

**[8:14]** like the LLM Wiki, which is what I've

**[8:16]** got set up for a few different things.

**[8:18]** This is the whole Karpathy LLM Wiki,

**[8:20]** which I did make a full video about if

**[8:21]** you want to check that out. I'll tag

**[8:22]** that right up here. But, this is when

**[8:24]** you start to have more files and and

**[8:26]** they start to take a bit of a different

**[8:27]** shape, and you want to organize them

**[8:29]** together in a bit of a different way.

**[8:31]** So, it could be really good for

**[8:32]** researching all on a certain project. It

**[8:34]** could be really good for, you know, a

**[8:35]** few of the ones that I've got set up is

**[8:36]** my YouTube transcripts all live in their

**[8:38]** own Wiki. I've got all of like my

**[8:40]** meeting transcripts that live in their

**[8:41]** own Wiki. So, for example, this is the

**[8:43]** Obsidian view of my Wiki for all of my

**[8:45]** YouTube video transcripts. You can see

**[8:47]** here if I go to Wiki, you can see

**[8:49]** there's main concepts like agentic

**[8:50]** workflows, AI coding market, context

**[8:53]** window. And all of these in here start

**[8:55]** to relate back to other tools and

**[8:57]** concepts and videos and stuff like that.

**[8:59]** So, we've got the sources, we've got

**[9:00]** platforms, we've got um context

**[9:02]** management techniques. And all of this

**[9:04]** was auto-created by our Claude code when

**[9:08]** I told it to ingest this YouTube

**[9:09]** transcript into our Wiki. So, I'm not

**[9:11]** going to dive super super deep into all

**[9:12]** of this right now, but definitely check

**[9:13]** out that YouTube video I linked. Now,

**[9:15]** what else is cool about this is this

**[9:17]** transcript Wiki actually lives within my

**[9:20]** main Herc 2 project. So, here's Herc 2.

**[9:22]** If I go right here to Other Worlds, and

**[9:24]** then I go down to YouTube OS, and I

**[9:26]** click into the transcript Wiki right

**[9:28]** here, this is what we were just looking

**[9:30]** at in Obsidian. We could see the

**[9:32]** concepts, we could see the comparisons,

**[9:33]** we could see the sources, techniques.

**[9:35]** This is what we were looking at in

**[9:36]** Obsidian. So, all Obsidian is is it

**[9:38]** basically just visualizes your markdown

**[9:41]** files. You see here, wiki, concepts,

**[9:43]** comparisons, techniques. This is what we

**[9:44]** were just looking at. All we get now is

**[9:47]** we just get a visual view of all that.

**[9:48]** And so, the reason I wanted to bring

**[9:49]** that up as well is because I think a lot

**[9:51]** of people obviously get pretty

**[9:53]** infatuated by that visual view. And

**[9:55]** obviously, I started the video with that

**[9:57]** because I think that's what hooks a lot

**[9:58]** of people in. But, all that really

**[10:00]** matters is can your system grab that and

**[10:02]** give it to you? If you are a visual

**[10:03]** person and you really want that view,

**[10:06]** then by all means, install Obsidian and

**[10:08]** set it up. It's super easy. But, I'm

**[10:09]** saying that you don't always need that

**[10:11]** visual layer if it's not beneficial to

**[10:13]** you. I hardly ever open Obsidian, just

**[10:14]** to be honest, because I know that it all

**[10:16]** lives here and I know that my second

**[10:18]** brain and my OS can find all of that.

**[10:20]** So, anyways, in level two here, let's

**[10:21]** look at this. It's very similar in shape

**[10:24]** to level one. It's just building on top

**[10:26]** of it because now we have our claw.md,

**[10:28]** which starts to route to some other

**[10:29]** things because it routes to the wiki and

**[10:31]** it still routes to contexts, projects,

**[10:33]** decisions, but it's also routing to

**[10:35]** references and memory.md. So, we're just

**[10:37]** starting to add a bit more of these

**[10:39]** routing rules inside of the claw.md.

**[10:41]** We can grow the context, we can grow the

**[10:43]** decisions, we can grow projects and

**[10:44]** references, and we can also start to get

**[10:47]** this idea of memory. And what's really

**[10:48]** cool about this is you can turn on auto

**[10:50]** memory in Claude Code. And the AI will

**[10:52]** basically start to write this file and

**[10:54]** update it on its own. So, you don't have

**[10:55]** to think about it. If you come in here

**[10:57]** and you do {slash} memory, it'll say

**[10:58]** auto memory on or off. And if it's off,

**[11:01]** if you want to turn that on, just turn

**[11:02]** it on. And now, one thing to think about

**[11:03]** is I mentioned earlier that we want to

**[11:05]** make our second brains tool agnostic.

**[11:08]** And this is one thing that's pretty

**[11:10]** specific about Claude Code is it uses

**[11:11]** claw.md and it uses this memory.md and

**[11:14]** it keeps that updated on its own. So, if

**[11:16]** you wanted to move this over to Codex,

**[11:18]** what you would do is you would first of

**[11:19]** all transition your claw.md. You'd make

**[11:21]** a copy of it called agents.md. As you

**[11:23]** can see here in my Herc 2, I've got my,

**[11:25]** if I scroll down, claw.md right here,

**[11:28]** and then I've got agents.md right here.

**[11:29]** And they're essentially the exact same

**[11:30]** file. Just so Codex can read this one

**[11:32]** and Claude code can read this one. But

**[11:33]** because Claude code keeps that auto

**[11:35]** memory, all you need to do is make sure

**[11:37]** you have that memory.md file and just

**[11:39]** tell Codex, "Hey, by the way, for

**[11:41]** memories, look in our memory.md file."

**[11:43]** It's all about the routing there.

**[11:44]** Anyways, just felt like that was

**[11:45]** important to throw out. But at a certain

**[11:47]** point, when you have these, you know,

**[11:48]** wikis, they do start to degrade a little

**[11:50]** bit. Because what's what's great about

**[11:52]** them is that they have indexes, right?

**[11:53]** So, when your AI starts to look in the

**[11:56]** wiki, it knows, "Okay, if the user's

**[11:58]** asking about a genetic workflow, I'm

**[12:00]** probably going to start here. And then

**[12:01]** from here, I'm going to drill down and

**[12:03]** read this to see what else is important

**[12:05]** to them." Maybe they're asking about the

**[12:07]** WATC framework, and then I can drill

**[12:08]** into that. And maybe from there, I need

**[12:10]** to learn a little bit more about the

**[12:11]** Claude at MD system prompt, and then I

**[12:13]** will drill into that. So, there are

**[12:14]** relationships here a little bit, but

**[12:16]** this isn't the same as like semantic

**[12:19]** relationships or knowledge graph

**[12:21]** relationships that have more meaning.

**[12:22]** This is more about just actually

**[12:24]** following a trail and reading the page

**[12:26]** in its entirety. And I'll be fully

**[12:28]** honest with you guys,

**[12:30]** I pretty much sit my entire PERC 2

**[12:32]** project in this level, in level two.

**[12:34]** Because this has been working really

**[12:36]** well for me. Like I mentioned earlier, I

**[12:37]** haven't felt a pain yet big enough to

**[12:40]** switch over to level two. And here's

**[12:41]** what I meant by that. My wiki has links,

**[12:43]** isn't that a knowledge graph? Not

**[12:44]** exactly. Because this doesn't have

**[12:48]** connections of how they are related,

**[12:49]** like this is endorsed by this or this

**[12:51]** has cron to here. These just have

**[12:54]** connections because it's like a a see

**[12:56]** also. It's like backlinks. So, they're

**[12:58]** very similar, and yes, they can achieve

**[13:00]** a similar effect, but it's still a

**[13:02]** little bit different. Anyways, let's

**[13:04]** take a look at level three, which is

**[13:05]** where you start to do things like

**[13:06]** semantic search. Whether you do that in

**[13:08]** Obsidian, whether you do that with Pine

**[13:10]** Cone or Supabase, however you start to

**[13:12]** grab the actual semantic search,

**[13:15]** that is what level three is. And so,

**[13:17]** just as a quick visual for you guys,

**[13:19]** let's take a look at this quadrant

**[13:21]** cluster of images. So, every one of

**[13:23]** these vector points is an image. And

**[13:26]** what we see in here is the payload is

**[13:28]** stuff like the file name, the URL, the

**[13:30]** name of the author or the artist, and

**[13:32]** the URL. But, we don't actually see like

**[13:34]** what's in the image. We don't get a

**[13:35]** description. So, what we have to do is

**[13:37]** we have to organize these images by

**[13:39]** meaning or by similarity. So, when I

**[13:41]** open up this graph and we start to

**[13:42]** visualize the stuff here, what you see

**[13:44]** is that we have this main image, these

**[13:46]** owls, these kind of like I don't even

**[13:48]** know. Um it's a very trippy style, like

**[13:51]** hallucinogenic style. Anyways, then this

**[13:53]** one is kind of similar, right? It's got

**[13:55]** those colors, it's got the paints. This

**[13:56]** one is also similar, but they're not the

**[13:58]** same. They just share similarities. And

**[14:01]** as we start to expand these more and

**[14:02]** more, we can start to get into different

**[14:04]** styles. So, this one has like some

**[14:06]** creepy eyes and mushrooms or whatever.

**[14:07]** This one is kind of more down that

**[14:09]** fantasy lane. And as we start to build

**[14:11]** out more of these relationships and

**[14:12]** meanings, we can expand and grow away

**[14:15]** from them. And so, Quadrant really just

**[14:16]** gives you a visualization here. I mean,

**[14:18]** it's a it has clusters and vector store.

**[14:21]** But, [snorts] the reason I pulled this

**[14:22]** up as a demo is just because we start to

**[14:23]** see the actual relationships form here

**[14:26]** based on meaning. And that's what's

**[14:28]** important about semantic search is that

**[14:29]** we're no longer doing keyword matching,

**[14:31]** we're searching based on meaning. So,

**[14:33]** here in my YouTube transcript second

**[14:35]** brain, if I go to the smart lookup over

**[14:38]** here, this is very different from just

**[14:40]** the regular search. So, for example, if

**[14:42]** I search here for um

**[14:45]** feedback, let's say. We're actually

**[14:47]** doing a match on the word feedback, and

**[14:49]** it's only showing me where that word

**[14:51]** actually appears inside of our second

**[14:54]** brain. But, if I come over here in the

**[14:56]** smart lookup and I search for feedback,

**[14:58]** we are getting matches that have things

**[15:00]** in here that mean feedback. So, live

**[15:02]** test results, cloud code skills, which

**[15:04]** was uh talking about evaluations and

**[15:05]** stuff. So, there's a big difference

**[15:07]** between keyword matching and semantic

**[15:09]** search, you know, similarity matching.

**[15:11]** This one over here is saying X equals X,

**[15:13]** and this one is saying X is similar to

**[15:15]** X, Y, and Z. And so, this all just goes

**[15:17]** back to vector databases. I've talked

**[15:19]** so, so much about vector databases, so

**[15:21]** I'm not going to dive super deep in.

**[15:22]** I've got so many resources on my

**[15:24]** channel. But basically, what it is is we

**[15:26]** take a document, so let's just say

**[15:28]** YouTube transcript, we chunk it up, and

**[15:30]** then each chunk is ran through an

**[15:32]** embeddings model. And the embeddings

**[15:33]** model puts that chunk of text onto like

**[15:36]** a three-dimensional space where space is

**[15:39]** related to meaning. And so it decides,

**[15:41]** okay, this chunk is about a company, so

**[15:42]** we're going to put it up here. This

**[15:44]** chunk is about finances, so it's going

**[15:45]** to go here. And we start to see these

**[15:47]** vectors form near other similar vectors.

**[15:50]** Now, do you guys remember how I said

**[15:51]** earlier, like you want to think about

**[15:53]** how is the data going to be used? What

**[15:54]** type of questions are you going to ask?

**[15:56]** This is a reason why that's so

**[15:57]** important. So think about this. Let's

**[15:59]** say I put my meeting transcript of March

**[16:02]** 5th meeting into my second brain. And I

**[16:05]** put those in as, you know, vectorized

**[16:07]** chunks. So let's say when I vectorize

**[16:08]** that meeting, we actually get, you know,

**[16:11]** like

**[16:12]** 20 chunks. It actually creates 20

**[16:14]** chunks, or however many that is. And

**[16:15]** then when I say, "Hey, Mr. AI agent, can

**[16:17]** you summarize the meeting on March 5th?"

**[16:20]** It will basically search for March 5th

**[16:22]** meeting summary, and it will pull chunks

**[16:24]** that are similar to March 5th meeting

**[16:26]** summary. And then even if it gets the

**[16:28]** right chunks, it's going to only

**[16:29]** summarize those five chunks. It's not

**[16:31]** able to look at the entire meeting

**[16:33]** summary, or sorry, like meeting

**[16:35]** transcript in entirety. So it doesn't

**[16:37]** really know a summary. It might be

**[16:38]** missing a lot of key information. Now

**[16:40]** yes, there are things you can start to

**[16:41]** play with there like metadata and other

**[16:42]** things like that to make these results

**[16:44]** better, but at the end of the day,

**[16:47]** people kind of assumed that a vector

**[16:48]** database was some magic solution where

**[16:50]** it could always pull back what you need,

**[16:52]** but that is very false. And I mean,

**[16:53]** think about it like this. Let's say we

**[16:55]** have a table, and we say, "Hey, which

**[16:56]** week did we have the highest sales?"

**[16:58]** Okay, the agent looks for highest sales,

**[17:00]** it maybe grabs this chunk outlined in

**[17:02]** gray of data, and then it looks at,

**[17:04]** "Okay, week six here was the highest

**[17:06]** sales, so that must be the answer." But

**[17:08]** in reality, you can see week 14 was

**[17:10]** higher, week 19 was higher. So when you

**[17:12]** need something that has actual full

**[17:15]** context,

**[17:16]** then you can't do the vector database

**[17:18]** chunking. That's where you'd rather just

**[17:19]** have a markdown file of March 5th, and

**[17:22]** then all this agent would have to do is

**[17:23]** read that entire markdown file and then

**[17:26]** give you a summary. And that's just

**[17:27]** going to be more accurate. So, in this

**[17:29]** project, if we open up level three, you

**[17:31]** can see it's very similar because you

**[17:32]** can still have context files, decision

**[17:34]** files, you can still have all that, and

**[17:36]** then you might identify, "Okay,

**[17:38]** actually, this one specific unit of my

**[17:40]** business, maybe my YouTube transcripts,

**[17:42]** maybe I want just that to be a vector

**[17:44]** database, but I still want my context

**[17:46]** and my projects and my decisions to be

**[17:48]** markdown files."

**[17:49]** So, another point I'm trying to make

**[17:50]** here is

**[17:51]** just because you have a second brain,

**[17:53]** and just because you have a massive, you

**[17:54]** know, folder here with a bunch of

**[17:56]** folders and files, doesn't mean that the

**[17:58]** whole folder needs to be one style. It

**[18:01]** doesn't mean that everything needs graph

**[18:02]** rack. It doesn't mean that everything is

**[18:04]** just LLM Wiki. It means that you're able

**[18:05]** to decide, based on the type of data and

**[18:07]** the way you use it, how can you

**[18:09]** structure this specific folder in the

**[18:11]** way you want it. So, here we have a

**[18:12]** vector index folder, and we click on the

**[18:14]** house search works. It works by

**[18:15]** chunking, embedding, search, hybrid,

**[18:18]** re-ranking. There's some things you can

**[18:20]** get really, really nitty-gritty on when

**[18:21]** it comes to semantic search. But what

**[18:23]** vector retrieval is really, really good

**[18:25]** at is looking at tons and tons of data,

**[18:27]** typically just like a lot of text, and

**[18:29]** when you need a very specific answer,

**[18:31]** something that's very similar. So, if

**[18:32]** you had a thousand rules that you needed

**[18:34]** to store, and you basically said, "Hey,

**[18:37]** um can you remind me what rule 17 was?"

**[18:39]** That might be a really good use case for

**[18:41]** vector search because it's able to

**[18:43]** search for rule 17, pull in those

**[18:44]** chunks, and just give you a little

**[18:45]** snippet because it would be a waste of

**[18:47]** time and tokens for your agent to read

**[18:49]** the entire markdown file of all 1,000

**[18:51]** rules if you just needed rule 17. So,

**[18:54]** that's kind of the difference there.

**[18:54]** Like I said, I've got so many videos on

**[18:56]** vector stuff on my channel, but really

**[18:59]** you could say, "Hey,

**[19:00]** to your cloud code agent, I have this

**[19:01]** data. Here's how I want to use it. Do

**[19:03]** you think this would be better for now

**[19:04]** as markdown files, or should I do

**[19:06]** semantic search? Like what would

**[19:08]** actually make more sense here?" And it

**[19:09]** will help walk you through the way that

**[19:10]** you should actually set that up. So, now

**[19:12]** I hope you guys are starting to

**[19:13]** understand why I said, you know, moving

**[19:16]** up on or I'm sorry, like moving up on

**[19:18]** levels, moving down doesn't necessarily

**[19:19]** mean better. It's all about figuring out

**[19:21]** what is the pain point with what you're

**[19:23]** currently doing and where would a

**[19:24]** different level help you out and fix

**[19:27]** that pain point. Okay, so now let's take

**[19:28]** a look at level four. This is where we

**[19:30]** start to get into like knowledge graphs

**[19:32]** and relationship graphs, which typically

**[19:34]** are going to be the most complex and

**[19:35]** sometimes the most expensive as well. If

**[19:37]** you're doing it on a certain platform,

**[19:38]** you could always use open source

**[19:39]** software, but anyways, knowledge graphs.

**[19:42]** And I also want to be up front. I've

**[19:43]** played with these a lot, but I do not

**[19:45]** actually use these on the day-to-day

**[19:47]** because I found out just other ways to

**[19:49]** use routing files and wikis that fit my

**[19:52]** needs. Now, my work is very different

**[19:53]** than what a lot of you guys' work may

**[19:55]** be. Mine is very project-based and it is

**[19:57]** very, you know, content-heavy. I don't

**[19:59]** have a massive CRM to manage with a

**[20:01]** bunch of different businesses and

**[20:03]** clients, you know? And if I did, maybe a

**[20:05]** knowledge graph would make a lot more

**[20:06]** sense and it probably would. But

**[20:08]** typically, the cool part about that is

**[20:10]** if you identify that you needed a

**[20:11]** knowledge graph, let's say for all your

**[20:13]** projects, you needed you wanted to put

**[20:15]** all of this in a knowledge graph,

**[20:16]** the data probably already exists here.

**[20:19]** And that's the thing about building out

**[20:20]** these relationships in your knowledge

**[20:23]** graph is that the system, whatever

**[20:24]** software you use, is typically going to

**[20:26]** be pretty good at embedding that and

**[20:27]** creating that. But the problem that you

**[20:29]** have to solve is you have to give it

**[20:30]** enough data. And so, one thing that I

**[20:32]** really like to do is I like to have

**[20:33]** these brainstorm sessions, as you can

**[20:34]** see. And what I do with these brainstorm

**[20:37]** sessions is I use a skill called Grill

**[20:38]** Me. So, if you see here, I have a skill

**[20:40]** called Grill Me, which I originally got

**[20:42]** from Matt Pocock. I customize it a

**[20:43]** little bit. I'll leave the skill for

**[20:46]** Grill Me in my free school community.

**[20:47]** The link for that is down in the

**[20:48]** description. All you have to do is hop

**[20:49]** in here, go to classroom, click on all

**[20:51]** YouTube resources, and you can find all

**[20:53]** the skills and everything like that. But

**[20:55]** the skill, what that does, is it

**[20:56]** basically just grills me. It interviews

**[20:58]** me relentlessly about a certain topic

**[21:00]** and it creates a brainstorm file here.

**[21:02]** It only stops when it knows everything

**[21:03]** about it. So, if you wanted to start

**[21:05]** building up a knowledge graph for all

**[21:06]** your clients and businesses, just say

**[21:08]** "Grill me about client A. Grill me about

**[21:10]** client B. Grill me about business A."

**[21:12]** And it would just ask you questions and

**[21:13]** you can feed it files. You can give it

**[21:15]** stuff. You can feed it in transcripts.

**[21:16]** You can feed it in, you know, contracts,

**[21:18]** whatever it is. And that's how you can

**[21:19]** start to form a lot of data.

**[21:22]** Hey guys, me again. Real quick, I'm

**[21:23]** editing this video and I realized that I

**[21:24]** needed to throw out one thing here,

**[21:26]** which is that obviously, if you're

**[21:29]** putting all of this data and you're

**[21:30]** sending it all to Anthropic, to Claude

**[21:32]** models, then

**[21:33]** that's not private. So, if you feel

**[21:36]** comfortable with that, that's fine. I am

**[21:37]** putting a lot of my data in there and it

**[21:39]** is my business stuff and

**[21:41]** that's what I'm doing. But, if you don't

**[21:43]** feel comfortable with that or you, you

**[21:44]** know, don't want to send client data, of

**[21:45]** course you don't, then maybe you want to

**[21:48]** do that through open-source models and

**[21:49]** maybe Claude code isn't where you have

**[21:50]** the second brain that has every single

**[21:52]** piece of information about you and your

**[21:54]** business and your client's business. So,

**[21:56]** the point I'm trying to make here is

**[21:57]** just this is what I'm doing. I'm

**[21:58]** obviously aware of the fact that my data

**[22:01]** goes to Anthropic when I process it

**[22:03]** through Claude. And if you guys are

**[22:04]** doing that, then you should also be

**[22:06]** aware of that. But, there are other

**[22:07]** options if you can't do that. So, I

**[22:08]** wanted to throw that out there. I am

**[22:10]** planning to make a ton of videos here

**[22:11]** soon about local AI and open-source

**[22:13]** models and all this stuff cuz it's a

**[22:15]** really, really exciting space that I

**[22:16]** think is going to start becoming bigger

**[22:18]** and bigger. So, yeah, keep that in mind.

**[22:20]** Back to the video. I think sometimes

**[22:22]** that's a misconception about how I got

**[22:25]** here and how people build their own AI

**[22:27]** OS or second brain is that

**[22:29]** they think the problem is the system not

**[22:31]** retrieving it great, which sometimes it

**[22:33]** is, but sometimes it seems like the

**[22:34]** bigger problem is getting everything out

**[22:36]** of your brain into the system. So,

**[22:38]** before you blame AI, take a look at your

**[22:42]** folders and files and say, "Is this

**[22:43]** actually holistic? Is this Does this

**[22:46]** have all the nuance that I have in my

**[22:47]** brain?" Anyways, from there, when you

**[22:49]** open up level four, you can see that

**[22:50]** it's it's, you know, very similar still.

**[22:52]** We're just adding on a few things. You

**[22:53]** can see here we've added an agents.md,

**[22:55]** which is the exact same as the

**[22:56]** claude.md. And what else is cool is you

**[22:58]** can literally just reference inside of

**[22:59]** your claude.md at agents.md and then you

**[23:01]** can delete all this because this

**[23:03]** basically just like injects that file

**[23:05]** into here. But I just wanted to show

**[23:06]** that. But anyways, you can see we're

**[23:08]** still following the same principles. We

**[23:09]** have a wiki. We've also added a

**[23:11]** knowledge graph layer. We've still got

**[23:13]** the same where things live with the

**[23:14]** routing with all these just regular

**[23:16]** folders and boring markdown, but boring

**[23:18]** is beautiful. You can see that our

**[23:19]** memory is still here. It's starting to

**[23:21]** grow, and we just keep building on top

**[23:23]** of this. So what one thing we added here

**[23:25]** as you can see was our knowledge graph

**[23:26]** folder. And so what happens here is we

**[23:28]** get different entities, right? So like

**[23:29]** we can see okay Jordan is a person. Acme

**[23:31]** is a company. And then we can start to

**[23:33]** form relationships between all these

**[23:34]** things. So Jordan works at Acme. Acme is

**[23:38]** endorsed by Postpilot. Postpilot is a

**[23:40]** competitor of Cadently. And it starts to

**[23:42]** build out not only these entities, but

**[23:43]** it shows you how they're all related.

**[23:45]** And so that's why when I said that I

**[23:47]** really like using, you know, this um

**[23:49]** what's it called? LLM Wiki is because I

**[23:52]** have enough of that feel of all these

**[23:54]** relationships because I've put so much

**[23:55]** time and effort into ingesting these in

**[23:58]** the right way and giving it context. The

**[24:00]** thing about this one is that it has to

**[24:02]** read every single file it wants. Maybe

**[24:04]** it was looking at AI video production

**[24:06]** and all it needed to know was

**[24:07]** ElevenLabs, it still would have read

**[24:09]** this entire file first. And so that's

**[24:12]** where sometimes the knowledge graph is

**[24:13]** actually more lightweight in that sense.

**[24:16]** And this is the example I showed at the

**[24:17]** beginning of the video where we have

**[24:18]** Lightrag. And forgive me, I'm going to

**[24:20]** have to blur some of this stuff out

**[24:21]** because this is like legitimately my

**[24:23]** entire second brain in our business. But

**[24:24]** as I really zoom in here and this kind

**[24:26]** of slows down my computer because

**[24:27]** there's so much. But what you'll notice

**[24:29]** is that we actually start to get

**[24:31]** relationships. I probably shouldn't have

**[24:32]** done this with so much data, but you can

**[24:34]** see like we have this collaborates with

**[24:36]** that. We have this builds that. And so

**[24:39]** if I really started to open up all of

**[24:41]** these little

**[24:42]** you know, circles, we could see what was

**[24:45]** going on and how they're all related. We

**[24:46]** could see that our 7-day AI challenge it

**[24:48]** was provided from YouTube. It connects

**[24:52]** to the onboarding process of AIS Plus.

**[24:54]** It was developed by Aiden. And so we can

**[24:56]** basically follow around these

**[24:57]** relationships, as you see. And even

**[24:59]** though it's pretty much the same data

**[25:00]** that you see here in Obsidian, we're not

**[25:02]** getting that same level of relationships

**[25:03]** between these different entities. So,

**[25:05]** anyways, if you guys want to see, you

**[25:06]** know, a full breakdown video on

**[25:08]** something like Logseq or um Graphir or

**[25:10]** all the other solutions that there are

**[25:11]** out there for more of a knowledge graph

**[25:13]** relationship graph, then let me know.

**[25:14]** But, that is kind of the difference

**[25:16]** there. So, if you don't need those sort

**[25:17]** of relationship chains, and you're not

**[25:19]** worried about that semantic type of

**[25:21]** relationships, then you probably don't

**[25:22]** need to use something like a knowledge

**[25:25]** graph. And then, level five, we have

**[25:26]** more of the always-on Brain OS, and

**[25:29]** something like Gbrain. Garry Tan, CEO of

**[25:32]** Y Combinator, he created this thing

**[25:34]** called Gbrain, which pairs really well

**[25:35]** with G stack. But, Gbrain is kind of the

**[25:37]** idea of everything we've talked about

**[25:39]** here. Wikis, routing, relationships,

**[25:41]** tools. But, Gbrain has kind of that

**[25:44]** always-on element, because it is like

**[25:45]** constantly syncing and refreshing

**[25:48]** memories and adding more stuff. So,

**[25:49]** adding in Gbrain to something like a

**[25:51]** Hermes agent would be really, really

**[25:52]** good. You could still do it in cloud

**[25:54]** code, but you'd have to handle those

**[25:55]** crons and get all that stuff set up,

**[25:57]** which is why I don't currently run

**[25:58]** Gbrain at the moment, but I have been

**[25:59]** playing around with it with my Hermes

**[26:01]** agent. So, anyways, the point here is

**[26:02]** that it's very similar to everything

**[26:04]** else we've just talked about. It's just

**[26:05]** having that auto-updating feel, more of

**[26:08]** the autonomous, always-on feel.

**[26:10]** But, I will say, another thing that I

**[26:12]** kind of that kind of scares me about

**[26:13]** that is you have this whole dilemma of,

**[26:16]** you know,

**[26:17]** when do you have too much context? And

**[26:19]** when does it get to the point where it's

**[26:20]** actually doing more damage than it's

**[26:22]** doing good? And the reason I bring that

**[26:23]** up is because I am in complete control

**[26:25]** of what my second brain ingests. I will

**[26:28]** run a skill to go grab all of my meeting

**[26:30]** transcripts from the week. I will say,

**[26:31]** "Hey, here's something. Help me figure

**[26:33]** out like how many brains are about this,

**[26:35]** and then let's ingest it together." And

**[26:36]** for me, I really like being in that

**[26:37]** control, because in my mind, there's a

**[26:39]** big difference between a few types of

**[26:41]** data. If you guys remember in my like AI

**[26:43]** OS videos, I've talked about the four

**[26:44]** C's. So, context, connections,

**[26:46]** capabilities, and cadence. And for the

**[26:47]** second brain, I mainly think about it as

**[26:49]** just these first two. So, context and

**[26:51]** connections. And so, when I think of

**[26:53]** context, that's stuff like, you know,

**[26:55]** what my business has done. So, if I come

**[26:56]** into here, into my my second brain, and

**[26:59]** you can see here if I go to

**[27:01]** um up at OTAs. So, OTAs are basically

**[27:03]** just our projects for the quarter. And

**[27:05]** so, here I can see all the Q1 ones,

**[27:06]** right? I can look at all those and I can

**[27:08]** click at them and see decisions that

**[27:09]** we've made in the statuses. And I can

**[27:11]** also see Q2 OTAs. So, I can see what's

**[27:12]** going on here. And my second brain's

**[27:14]** able to see that because that has been

**[27:16]** basically those are locked in decisions.

**[27:17]** This is what we're doing this quarter,

**[27:19]** and then I'm updating the statuses of

**[27:20]** that stuff. So, that's like context.

**[27:22]** That's what's going on in the business.

**[27:23]** But when it comes to connections, if I

**[27:25]** go back to this, this is more of like

**[27:27]** the real data that isn't as evergreen.

**[27:29]** This is stuff that changes. This is like

**[27:31]** Slack threads. This is emails. This is a

**[27:33]** customer data. And that type of data you

**[27:35]** don't want to ingest into a second brain

**[27:37]** because that's just noise then. Then you

**[27:39]** have to go back every month and like

**[27:41]** delete old stuff. So, the way that I

**[27:43]** like to think about my actual second

**[27:44]** brain is stuff that I'm not going to

**[27:45]** delete. This is stuff that is like,

**[27:47]** okay, in a year, will it be good for me

**[27:49]** to have this memory in here? Yes.

**[27:51]** Otherwise, it's just adding noise. So,

**[27:53]** when you're adding data into your

**[27:54]** project, think about it like the context

**[27:57]** and connections. Think about if this is

**[27:58]** kind of like more evergreen, holistic

**[28:00]** data, or if this is more things that are

**[28:02]** going to change next week. So, you

**[28:04]** probably shouldn't pull it in, but you

**[28:05]** should make sure that your second brain

**[28:07]** has access to go grab it. So, that way

**[28:09]** if I said to my second brain, "Hey, can

**[28:11]** you just take a look real quick at what

**[28:13]** John and I were talking about last week

**[28:14]** about, you know, OTA number seven?" It

**[28:17]** would first go to our OTA file, and it

**[28:19]** would search through there and it it

**[28:20]** would try to find it there. If it

**[28:21]** couldn't find it there, it would look

**[28:22]** through the Wiki and it would look

**[28:23]** through meeting transcripts and see what

**[28:25]** we talked about there. And if it

**[28:26]** couldn't find it there, it would finally

**[28:27]** go to ClickUp itself, pull real data in

**[28:29]** from me and John's conversations, and

**[28:31]** see if the answer lived there. And so,

**[28:33]** that in my mind is still a second brain

**[28:34]** because I'm able to ask a vague

**[28:36]** question, and the second brain knows

**[28:37]** exactly where to look in what order to

**[28:39]** find that real-time data, and then give

**[28:41]** me back the answer that I need. That's

**[28:42]** the question I ask myself is, "Does this

**[28:44]** thing understand where my data lives and

**[28:46]** where to look, and can to give me

**[28:47]** accurate answers. So, as far as finding

**[28:49]** your level, remember your whole project

**[28:51]** doesn't fit into one level. Maybe this

**[28:53]** folder's level two, maybe this folder's

**[28:54]** level four, maybe this folder's level

**[28:56]** three. Here's some things to think

**[28:57]** about. If you were re-explaining your

**[28:59]** setup and you need to find things by

**[29:00]** exact words or files, look at level one.

**[29:03]** If you have 30 plus notes and you keep

**[29:04]** forgetting what's in them, look at level

**[29:06]** two. That's where you sort of like

**[29:07]** ingest them and get that wiki with

**[29:08]** relationships. If your project is just

**[29:10]** completely whiffing on notes that you

**[29:11]** know exist and your routing isn't

**[29:13]** working, then maybe you want to look for

**[29:15]** something more like a semantic search

**[29:16]** that doesn't rely on an exact word level

**[29:19]** match. If you're looking for

**[29:20]** relationships and to be able to follow

**[29:22]** chains of questions and thoughts, then

**[29:24]** you probably want to look for something

**[29:25]** like a knowledge graph. you're running

**[29:26]** agents offline and you've got so much

**[29:27]** data and you want to sync up a bunch of

**[29:29]** Hermes agents together, then you

**[29:30]** probably are looking for something like

**[29:31]** level five, something like G brain. And

**[29:34]** another topic that I get some questions

**[29:35]** about, which I'm not going to fully

**[29:36]** address in this video, but I will

**[29:38]** briefly bring up is the fact that you

**[29:40]** are building your own second brain OS.

**[29:43]** So are other people on your team. The

**[29:45]** next question is, how do you actually

**[29:46]** make sure that everyone's data is

**[29:48]** syncing together and how do you have

**[29:49]** more of like your team second brain?

**[29:51]** There's a lot of different ways to solve

**[29:52]** that. I think once again, it's not an

**[29:54]** issue of, oh, do we use Google Drive or

**[29:56]** Notion or GitHub or cloud plugins? I

**[29:59]** think the issue to figure out with your

**[30:01]** team is how do we actually make sure

**[30:03]** that we all have it shift so that this

**[30:05]** stuff is actually useful and not just

**[30:07]** noise. How do we make sure that process

**[30:09]** owners are updating their docs and

**[30:10]** syncing their stuff there? How do we

**[30:12]** make sure that other people are pulling

**[30:13]** from that rather than always just

**[30:15]** pinging the same people for questions

**[30:17]** and answers all the time? I think the

**[30:18]** adoption and the change management

**[30:19]** question is the bigger one. The tech and

**[30:21]** the way it actually functionally rolls

**[30:23]** out is a little bit less. But what I do

**[30:26]** know is that you getting set up with

**[30:28]** your own first and understanding how it

**[30:30]** works, how you should route, how you

**[30:31]** should make the decisions of where the

**[30:32]** data should live, that's the first

**[30:34]** hurdle. You can only solve the team-wide

**[30:36]** problem once you feel comfortable about

**[30:38]** the way you run it every single day and

**[30:40]** then it works for you. That is going to

**[30:41]** do it for today. Like I said, you guys

**[30:42]** can grab all the skills and everything

**[30:44]** that you need from this free community.

**[30:46]** The link for that is down in the

**[30:47]** description. I will also include the

**[30:48]** slide deck if you guys are interested in

**[30:49]** flipping through. So, if you guys

**[30:51]** enjoyed the video or you learned

**[30:52]** something new, please give it a like. It

**[30:53]** helps me out a ton. And as always, I

**[30:54]** appreciate you guys making it to the end

**[30:56]** of the video, and I will see you all in

**[30:57]** the next one.

**[30:58]** Thanks, guys.
