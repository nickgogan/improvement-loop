# Transcript: FULL Guide to Becoming a Principled Agentic Engineer (Build Anything with AI)

**URL:** https://www.youtube.com/watch?v=luBkbzjo-TA
**Segments:** 1937
**Channel:** Cole Medin
**Duration:** 1:07:01
**Uploaded:** 2026-04-30

---

## Full Text

What I have for you today is a polished up version of a super value packed live workshop that I just did yesterday. I hosted the AI transformation workshop with Lior Weinstein. He's a big name in the AI space. It was a blast. And so what you're about to see is my portion of the event, teaching you in very simple terms how to build a foundational system for getting reliable and repeatable results with AI coding assistants. And this is important right now because people they over engineer and over complicated AI coding frameworks all of the time, making it seem like you need some fancy harness or specialized agents just to do any real work at scale. But that really isn't the case. So I boil things down into the core principles for AI coding here in three phases, teaching you how to ideate with coding agents, how to build an iterative loop, and then how to evolve your coding agents over time. A lot of this I've covered on my channel, but never in one place. There's a reason this workshop is one hour. It's super value packed. You If you go through this entire thing, you come out of it with a full system that you have a real ownership of. And the best part is it's not even that complicated. And so without further ado, here is the live workshop. Our job as an engineer is to no longer write the code, but to do the higher leverage tasks like the planning and validating. And that's the framework that I want to cover here. And um also for product managers in the room, there's a lot that I have to say that applies to you guys as well. There's a three-part process that I want to walk through with you right now. We're going to start with how do we ideate around the work that we want our coding agents to do for us for building literally anything, a website, uh funnel, uh any kind of platform. This is going to apply no matter what you want to build. And then we'll get into for the developer when we are knocking out a piece of work like a ticket in Jira or handling a GitHub issue or starting a new application, what does that process look like? It's using the PIV loop. That's my core methodology that we'll cover. And then we'll get into the system evolution mindset. And this is probably the most powerful part of the entire system, how we make our coding agents more powerful over time as we run into issues using them. And uh one disclaimer that I want to give before we get into everything here is that uh a lot of what I'm covering here is a training that I do for organizations. But usually for them it's more of a 4-hour session where I really get into the entire process. And so I've compacted everything down into 1 hour to share with you guys right now. So a high-level overview, but I'm still going to get really practical with you guys. And I'm going to give you a live demonstration of everything here so that you can come out of this 1 hour knowing exactly what the process looks like that you can mold for yourself to go from idea all the way to production code with the help of a AI coding assistant. And the important thing here is we're not vibe coding because we are putting ourselves in the driver seat along the way through all of the planning and validation that we do. That is the the core framework that I'm going to cover with you. And uh really this whole process, it applies no matter the tools that you're using. And so I'm going to be using Claude Code for our event here just because that is my favorite AI coding assistant, at least right now. And then I'm going to be using Jira as my place to manage all of the work that we scope out with the help of Claude Code. But this entire process is going to work if you're using, you know, Codex with GitHub or you're using GitHub Copilot with Linear. Really it's just you need to have one place to manage your work and organize your work and then one place to work with a large language model to create your code. That's the only requirement that I have here. Even if you do want to follow along. And also in the description for our live stream here, if you click into the description, I'm just like looking at it on my left monitor here, I have a link to a GitHub repository. And uh this GitHub repository has the demonstration application that we're going to be building on top of today. And then it also has all of the resources that I'm going to be showcasing here, my rules, my commands, my skills. We'll talk about what those look like and I'll use some of them live, but a lot of that it lives here in the dot cloud folder. So, if you see any part of my process that you really want to steal for yourself, please feel free to do so. This repository is open source, ready for you to come in and take any of the skills or all the commands that I'm using to package up my workflows. And so, really we're not going to be doing a lot of manually typing today because it's going to be here are the prompts that I've been using time and time again. I have it as a command that I can reference and have the coding agent go through that procedure that I'm using pretty much every single time that I'm delegating in the coding to AI. So, yeah, the last thing I want to say before we get into things here is there are a lot of frameworks for AI coding available to us that are open source. So, maybe you guys have explored GitHub Spec Kit or B Mad or Claude Flow or GSD, um Gas Town. I mean, I could go on naming a dozens and dozens of them. There are all of these opinionated strategies out there right now to guide you through a process kind of similar to what I'm going to show you here. Like this is a process for researching, then planning, then building, then validating with AI coding assistance driving a lot of it. And I have a lot of respect for these platforms. There are a lot of really powerful, timeless software engineering strategies built into them, but at the same time a lot of these frameworks are very over-engineered. They try to do too much at once and it's really difficult to take an existing off-the-shelf framework and mold it to your software development life cycle. So, like I said, I do a lot of corporate trainings where I teach companies how to take something very foundational like this and mold it to their existing practice because you don't want to just throw out the window the entire process your team has already been using for working with coding agents. Instead, you want to mold the process around AI, but you still are going to have some of your conventions in the way that the team works. It's not really realistic to just throw everything out the window. But, when you're using something like BDD or Gherkin, you're trying to take an off-the-shelf solution, you're kind of forced to do that because it's so bloated that it's hard to like really make it your own. And so, what I teach here is simple on purpose cuz I want to show you the foundation that you can then build on top of to mold it into your process for planning, your process for QA, whatever that looks like for each stage of the software development life cycle. And so, we'll start with planning here. And planning, this part actually applies to product managers just as much as developers. So, a lot of organizations that I work with, um the trainings that I do, they'll bring their entire uh PM team into the training as well because they're actually the first ones that have a touch point with the coding agent when you're planning the next scope of work for an application. So, the product manager is the one initially doing, you know, let's say the sprint planning. And it's important for them, just like the developers, to work with coding agents to speed up that process. Here's the application that we have right now. Here are the bugs we want to fix and the issues that we want to build or the new features we want to build for this sprint. And same thing applies to greenfield development, you're going to be building that initial scope of work for the MVP of an application. And this process applies to both. And so, what I'm going to do with you guys right now is uh I am going to show this diagram at a high level, just walk through it really quickly with you, this component right here, and then we're going to get into something very practical. I'm going to go into my uh code base here, and we are going to go through everything live. I'm going to show you what it looks like for brownfield development to take an existing application, plan out a brand new sprint with a bunch of new set sets of work we want to perform, and then I'm going to pick one of those, and we're going to go through the piv loop, the process that we're going to repeat for every single Jira ticket. And again, that could be a GitHub issue, it could be a linear ticket, whatever that is. And so, you'll see the full process end to end. There's a lot of value that I have packed into the hour for you guys here. So, okay. The beginning of the process here is as simple as it possibly can be. You are going to open up your coding agent, like I'll, you know, I'll just pop open Claude Code right here, and you're just going to have a conversation about what you want to build. There is no structure at first. And like I said earlier, it is simple on purpose, because I want the barrier to entry for you to be so incredibly low that you begin just brainstorming ideas with the coding agent, and then we're going to evolve to more structure over time. And that's the process that I'm going to share with you as I start to bring in some skills and commands that I have in my AI layer, in my AI coding system. And so, um first of all, when you have this conversation, you just do what I like to call a brain dump. Like most of the time, I'll literally I'll just use a speech-to-text tool, so that I just talk. I go on and on about what I want to build. At this point, it is helpful to be as specific as possible. And so, you would say, you know, like, "This is my application. Here are the new things that I want to build. Here are the bugs I want to fix." And then you go into the clarifying stage. And so, the most important part when you're first planning work with a coding agent is to reduce the number of assumptions that it is making, because honestly, most of the time when a coding agent does a bad job, it's not like the code is just broken. It's that it's not aligned with what you were actually looking to build. And really, the responsibility is on you there because it is your role to and and your responsibility to make sure the coding agent is really on the same page with you for what you are building. So, it's a lot of just curating this context with the help of a coding agent, being very specific for what you want to build. And so, the most powerful strategy here, and you'll see this in action in just a little bit, is to have the coding agent ask you questions. Like we will specifically ask it to ask us questions. And you can go through this process for a good 20, 30 minutes, even beyond that, if you really want to set the stage well going into the development later on. So, product managers, this is your job when you're working with Claude Code. And even if you're you know, you're a solo developer shipping things without a product manager, this is still an important step to go through. It's very important to stay high-level at first. We're not getting into the weeds right now for how we're going to test things or what files we have to change in our code base. At this point, we're just trying to figure out what are the requirements that we need to translate into code. And then we'll have a separate planning process where we're getting more into, okay, here's how we're actually going to code it and the parts of code of the code base that we need to edit. So, at this point, we're very, very high-level. And then after you have a conversation with the coding agent where you figured out exactly what you want to build, what is our scope of work for this sprint or this new application, then it's time to create your AI layer. And I have this marked as optional here just because when you are working on an existing code base, you might already have that AI layer already created. But if you don't have it, I highly recommend investing a lot of time up front building this. Now, for our 1 hour here, it's not like I have a lot of time to like really get into best practices for building your global rules and your skills and commands. But I'm just saying like this is the part of the workflow where you will create that. And so, your global rules, these are the conventions, the rules that you always want your coding agent to follow. Like here are our coding styles, here's our testing strategy, our logging strategy, things like that. And then your commands, we're going to see a lot of these in action today. And your skills, these are your reusable workflows. So, anytime you find yourself prompting something more than three times, you should turn it into a command or skill. Because that's just a prompt that you're going to load into your coding agent when the time comes. Like this is my process for planning, this is my process for creating PRDs or stories in Jira, for example. That way we don't have to type things out. And it's a reusable workflow that we can share and create a standard across with our team. Very, very important. So, we don't want to do manual prompting as much as possible, turn things into something in the AI layer that you can invoke, right? Like we can take a command and skill and say, you know, {slash} plan. Now we are going into our planning process. And so, that actually goes into the first command that we'll use here. And again, I'll show this all in action in just a little bit. So, the first command is a process guiding the coding agent from an unstructured conversation into a structured PRD. Like I said, we go from exploration to structure. So that we have a single document that is produced from this command that outlines all of the core sections for our and a PRD is short for product requirement document. So, this is like the initial scope of work for an application if we're doing greenfield development, or these are all of the tickets that we need to handle if it's a new sprint that we are planning for in Jira, for example. And then I can take the PRD and also have Claude code split it up into individual pieces of work to create as my Jira tickets. We'll see this in action. And so, it handles literally everything. It parses this document. It figures out what are the individual phases or pieces of work that we should create as tickets. And then we'll even use the Jira MCP server to create those things so that we don't have to do that backstage work like Leora was talking about of creating those tickets in Jira. We want to have our coding agent handle all of that administrative work. And so, we end with tickets in Jira and then we can pick one of them. So, this is where, you know, the product manager would hand things over to the developer to pick a ticket and then go into the full Piv loop. This is the full process we go through to handle individual sets of work with our coding agent. So, we'll get into this next, but first I want to show you a live demonstration of our ideation phase. And so, I'll go over to my code base now. And I'll it's just describe very briefly the application that I have for a demonstration here. And so, this repository, again, I have it linked in the description. I also linked it in the chat. Um actually, I didn't link it in the chat, so I'll do that right now. So, let me go out, copy this. And I'll paste this in our chat here. If you guys want to just poke around the resources that I have for you guys and or even follow along, you can feel free to do that. Uh the application for my demonstration is just the quick poll builder. So, you know, you put in your question like uh how experienced are you with AI coding? And then we have our options here like I'm a beginner, I'm intermediate, or I am advanced. All right, cool. And then I create a poll. Yeah, the point of this application is that it's super simple because I'm going to be focusing on the process, not focusing on the application itself, right? So, I want something very quick to build on top of so that I can quickly go through how I create stories, handle tickets, go through the pivot loop, and the system evolution. And so, uh what I'm going to do to begin is I'm going to go into Cloud Code, and I'm going to plan my next fictitious sprint. So, we have this very basic application right now where we can create a poll, and if I, you know, actually had the application deployed, then people could use it and go and and answer the poll, but there are a lot of features that are missing. And so, I have a prompt prepared ahead of time that I'm just going to paste in right now, just so that you guys don't have to watch paint dry as I give my initial brain dump. But again, this is your point where you just dump all of your ideas of what you want to build, being as specific as possible. So, even if you wanted to specify things like your tech stack and your architecture, if you're more technical, this is where you do that. But even if you are less technical, and you are, you know, product manager, for example, you can still stay pretty high-level here, and just describe the features that you want to build. And so, I'm saying like here's my brain dump for phase two, like the next thing that I want to build on top of the application. Let's say I want to build a live presentation mode. Like right now in the poll builder, when I I can't really like see answers come in live. Like if I click see current results, I'd have to refresh the page in order to see new entries. I also want to build a QR code generation, multi-question polls, multiple choice questions. Like there's like a lot of things that I want to build on top. This is my next sprint that I want to uh you know, my end goal is to have all these things created as uh Jira tickets that I could then pass on to developers, or pass on to my coding agents if I am a developer. And so, I've described everything here. Um usually, if I'm not just doing a live demonstration, I would make this prompt a lot longer, but I just wanted to keep it concise right now. And then the important thing here, this is what I was saying in the diagram, before you write anything, ask me clarifying questions one at a time using the ask user question tool. And so now this is where I'm going to make sure that I get on the same page with my coding agent. And so one at a time it's going to ask me these questions and in Claude code we have this ask user question tool where we can see these questions pop up with a multiple choice answers for us. So it's really easy to blitz through things cuz a lot of times what it recommends is actually what I'm going to go with, but it still gives me the opportunity if I want to say like, "Hey, no, you're wrong here. Like let's actually do it this way instead." So we can, you know, remove that that incorrect assumption that it was making. And for other coding agents that don't have this specific tool, it's this whole process is still going to work. It's just going to be a little bit slower cuz you'll have to type out each of your answers more like you're just chatting with an agent. Um but it still works in exactly the same way. So it's asking us questions here like how should real-time updates work? I'll just go with what it recommends here just for the sake of speed, but also you have this option to chat with it. So for each individual thing if you really want to dive deep with the coding agent, which a lot of times I would recommend you do, you have the opportunity to do that. And of course how deep you go does depend on how technical you really are. Like right there, you know, how should real-time updates work? That is a pretty technical question. So if you want to just go with what it recommends, that's definitely okay. But if you have that knowledge and then like really understand the architecture of the code base, it's just more power to you. You're able to to really make sure that you clear assumptions. Otherwise if you're, you know, more on the product manager side, you might have a couple of wrong assumptions that sneak into your Jira tickets, but that's why you work with the developers as you're planning things, right? Like you'd have your sprint meeting where you'd make sure you clarify these kinds of things. Uh but the goal is just for the coding agent to help us with that starting point of having all the context in Jira ready for developers to refine and pick up and work on. And so, for the sake of demo, I'm going to say let's end the questions here. Just because sometimes it can go on for, you know, a good 10-15 minutes asking us a lot of questions. I'll allow it to make some assumptions for the sake of speed. But at this point, you know, I've already shown you what I need for what this process generally looks like. And so, at the end of our chat here, this context, this short-term memory for Claude code, is what we're going to turn into the PRD. So, we are about to run our first command where we create that product requirement document. The input is the conversation. The output is a single document, a source of truth that we could, you know, then upload to Confluence or check into source control, wherever you want to store that, and then we can create the Jira tickets from that. All right. So, that was the last question there. Now, it's it's taking in my message. So, it will move on to creating our PRD. And Claude code is smart enough to know the capabilities are available. So, when I've gone through this process a lot of times, it'll just go right to loading the create PRD skill, and it'll walk itself through creating that document in exactly the structure that I'm looking for. And so, I'll go ahead and open that so we can see ahead of time what it actually looks like. And again, all of these commands that I'm about to walk through are available in the GitHub repository that I have linked in the description. So, I'll go to create PRD. That is our first command. And again, commands and skills are really just procedures. They are prompts that we get to load in in real time whenever we want. And so, create PRD. This is going to generate a comprehensive product requirements document. We are we get to also specify like where it also outputs this file. So, commands and skills support arguments. So, that's how we can make things dynamic. And we'll we'll talk about arguments quite a bit cuz most [snorts] of my procedures have arguments. So, I can make them specific to what I am doing right now. And the main thing that we are outlining in this PRD command is the structure that we're looking for. Like, we want every PRD to have an executive summary, a mission, target users. This is a lot of product manager speak. So, if you come from the product manager space, really this is your opportunity to take how you already write PRDs and make it so your coding agent does it in the exact same thing. Again, the foundations that I'm laying for here in this process is not for you to completely have a blank slate for your software development life cycle, but to take your best practices that you established as a team and teach it to your agents. That's what we're doing with skills and commands. And so, your PRDs are going to look the same, but your agent is saving you hours and hours and hours because it gets to generate this based on our conversation. And so, right here like what I can do is it kind of went through this itself like it loaded the skill automatically, but I'll just show you like if I wanted to invoke it myself, I can just do create PRD. And then I can specify the file name as an argument like this. It's just when you invoke something or similar to when you invoke something in the command line for all you developers. So, we just have space separated arguments for anything that we want the command to respect like where we're going to output it. So, we're going to have something in the dot agents folder. It'll just be like a marked out PRD in markdown file. And then of course we could you know like use the Jira MCP server to upload or the Atlassian MCP server to upload it to Confluence. We could upload this document to Google Drive or put it as context in a GitHub issue. However, you want to you know store this artifact that is like the initial source of truth for that new application or that new sprint that we are planning. And so, once we have our PRD created and it's going to take a little bit um, because it's generating a larger document here. You can see that Claude is currently thinking through the structure. So, it's taking this conversation, reasoning about everything that we we have discussed here, and then creating a document from that. Once we have our PRD, we are going to create our stories. Now, you could do this as a single command, where you create the PRD and the stories all with a single call to Claude Code. The reason I have these separated is because once you have the PRD created, it is a good time for you to validate things yourself. So, going back to the diagram here, it is important for us to delegate as much coding to the coding agent as we possibly can. That's the backstage work for developers now. But, we want to remain in the driver's seat because every single artifact that our coding agent produces, whether it's a PRD or it's a set of code, we want to review that. And we want to have human in the loop so that we can iterate on anything. And so, when we create our PRD, it's not good enough to just immediately create stories from that. Like, it's important for us to review the artifact and make sure that things are really aligned with what we are looking to do next. Because, yes, we had it ask a bunch of clarifying questions, but maybe we didn't have it ask enough questions. Or maybe it didn't quite understand our answers. That's why it's important for us to still review things. So, I I know that takes some time, and the promise with AI is that it speeds things up a lot. But, even if you do take time refining the PRD with the coding agent, it's still going to save you so many hours compared to if you did this entire process yourself. And so, for the create stories command, we run this after we have reviewed the PRD and maybe made some changes to it. And so, for this command, we give it the path to our PRD. Obviously, we want Claude code to know like this is the PRD that we want to create our stories from. And then we can also specify the Jira project and epic. And so, what I have in Jira created ahead of time is I just have a a simple project created with an epic that doesn't have any tasks in it right now. So, this is what we're going to populate live in a little bit with our create stories command. And so, I had to do a little bit of manual work to actually create the epic. But after that point, I'm not doing any work myself in the Jira platform. That's all backstage. I don't want to do that myself. And so, I want to have a single process that goes from here are my ideas to everything is populated here. And it feels like magic every time this happens. So, we'll get to that in a second, but obviously, we need to have the PRD created first. And you can see that right now. It's outputting a lot of tokens cuz it's in the middle of creating that file for us. So, we just have to be patient. But uh that gives me some time here just to show you really quickly what uh we have in this command here. So, first of all, we have a phase-by-phase procedure that we're walking Claude code through. Again, commands are just prompts that we're we're having the coding agent run through. So, we're having it load the PRD cuz we can also run this in a separate Claude code session if we don't want to run it in the same one. So, we can load the PRD. That's all the context it needs. Then it's going to break down into stories, and I can render this so it looks a little bit nicer here. So, we create a user story, and we can specify the format as well. We can define the acceptance criteria. So, just like we create the structure for the PRD in the create PRD command, we can do the same thing for the stories here. So, your team probably already has a convention. Or if you're a solar solo developer, you still probably have some kind of convention for how you want to create these artifacts. Here are my tasks, here are my issues, whatever that is. And so we bake that into the command. And that makes it more reliable, repeatable, and it makes it so that you don't have to have a brand new process that everyone is extremely uncomfortable with, right? Like we want to make it easy to adopt these new tools and new processes. And so then we go on to the structure for each story. Here is exactly what you're going to create. Here's how we're going to order them. We even have some validation built in, so it kind of checks its own work to make sure that it has, you know, fully extracted all the phases out of the PRD, for example. And then we have the output. We're going to save everything to markdown documents. And then if we have the Jira integration, so I actually set this command up so that if you're not working with Jira, then you can still just work with the stories in local files. A lot of solo developers just manage their entire system with markdown. And that's totally respectable. So this command works for that. But if we do have the Jira integration, and we tell it how to check for that, then it's going to create everything in the epic that we specified um in the argument here. So like if these things are filled in, and we'll see that in just a second. So okay, we created our PRD. And so we can take a look at this. So this document, I'm not going to read through the entire thing right now, cuz it's a pretty long document. The point of uh what I'm demonstrating right here is mainly to show you that the structure that we have laid out in the create PRD command is exactly what we see in our final PRD. So we have our executive summary, our mission, our target users, everything that I showed you in the markdown here. And then we also have what is in scope. So for our phase two sprint, we want the multi-question polls, per user toggle, the full-screen presenter presentation page, uh everything that we gave in our initial brain dump. So this PRD is the result of our conversation plus the create PRD process, right? Like those two things together, this is the baby of that. And so now this PRD, we can run through our create stories command. And this is the thing is like after that initial brain dump, I'm really not doing much typing. I'm running commands, I'm answering questions, that's really all I have to do. And so I'm going to go ahead and copy this. And like I said, you could do this in a separate context window if you wanted to, but I'm just going to do it right here because it was relatively short. So I'm not going to iterate on the PRD for the sake of speed here. Um so I mean this is one moment where it's, you know, do as I say not as I do, but uh generally if I am off camera and really working through my initial planning for something, I'm going to spend a lot of time looking through each section here and making sure that everything is as I intend. And so I'll run create stories with uh the path to my PRD, and then I have to give the ID of my Jira project and also the ID of my tag. And so for those of you who are using Jira, you just get that like this is the ID of your project and then this is the ID of your epic. And then if you're doing something else like using GitHub or Linear, you're going to go through the exact same process. You're just going to use, you know, the GitHub CLI to create issues instead of the Jira MCP server or you're going to use the Linear MCP server. So again, it doesn't matter in the end what tool you're actually using. So I'm going to go ahead and run this. So it's going to break down, it's going to follow that exact process that I just showed you, breaking down the PRD, and then after a few minutes, it'll take a little bit of time for it to reason about that, we'll see all of the subtasks start to get populated here in Jira. And then at that point, we can have developers just pick them up and go through the pivot loop that I'll cover with you guys next. And that's the beauty of it is also you can have developers work on everything in parallel. They can assign themselves, you can also, you know, use the Jira MCP server to have the the developer get assigned automatically when it picks up a piece of work. You can create a system in your task management software where really agents are managing everything. It's kind of like the the whole CTO X OS that Lior was showing you guys where you have the agent managing all of the grunt work of organizing and um you know, all of the you know, CRUD operations of creating tasks and updating them and assigning them and everything. We can have agents manage all of that with the Jira MCP server. And I'll show you guys what that looks like. If if you go into Cloud Code and do {slash} MCP, you can see that I have the Atlassian uh MCP server connected. So, by the way, this also gives me access to Confluence, not just Jira. So, if you wanted to like store documents in Confluence, like you wanted to store the PRD in Confluence and then have a developer load that PRD with the Jira MC or the Atlassian MCP server, they can do that as well. Um and so, if you are an Atlassian kind of shop where you have Confluence and you have Jira, you can have your coding agents manage all of that. And it's really the same thing no matter the platform that you're using. And so, the way that I have this MCP server configured is just with this um mcp.json file. And if you're curious how I set this up, this is the crazy thing, guys, is that you can have Cloud Code help you with anything. It has access to its own documentation. So, if you say, you know, help me copy over Cole's commands, and you just give it the path, it can bring all that into your own project. Or you say, help me set up the Atlassian MCP server, it'll search the web, it'll pull the exact configuration, it knows to create a file called {dot}mcp.json, it'll set up everything for you. The the time in in our world where we had to be technical to do these kinds of things is no longer here, right? Like a product manager, a QA engineer can use Claude code to do any part of their job just like a developer can because you don't have to know how to run commands or set up MCP servers anymore. I mean, yes, it's still helpful just in case the coding agent trips up. So, it's faster for a developer. But uh also coding agents are really good at debugging things. If the MCP server doesn't connect right away, you can ask it like, "Hey, I'm getting this error. Help me figure it out." Maybe like search the web for some more Atlassian documentation, for example. And so, really for like all these things, I didn't configure that all myself. Like I have my repository of commands and skills. I pointed Claude code there and I said, "All right, Claude, for this AI transformation workshop that I'm doing with Lior, I want you to set up a brand new repository and bring in my resources and customize it to work with Jira instead of GitHub, for example." And it just did all of that for me. So, a little bit meta there, but I hope that demonstration is um is cool just to see like how easy it is to get anything configured in your AI coding environment. And so, for all these resources that I share with you, you don't even have to bring them in yourself. So, we can see that it created all of the stories here, and then it asked me a question like, "Do you want to push to Jira now?" So, I said, yes, and now it's going to take advantage of that Atlassian MCP server to populate everything. And so, I don't think we'll have it yet. Let me refresh the page, but we'll in just a second here, we'll start to see things get populated. I think it's in the middle of reasoning through that. Okay. Yep, so we can see that the token count go up as it is formulating those tool calls, basically. So, the agent is performing these operations under the hood. And we're almost done with the first step, by the way. And once we get into the pivot loop, things go pretty quickly because we're doing so much of the work up front with our ideation. So, we're getting to this stage right now where we are getting our tickets in Jira, and then we'll pick a ticket, and then this is where we just rip through the implementation with the pivot loop. So, all right, let's go back to Claude and see where we are at. All right, so calling at Atlassian seven times. You can also in Claude do control O so that you can see the full tool call if you want some more visibility into what it's doing. So, it's using the create issue MCP tool. It's got my ID, the project, all the things that we specified as parameters like the epic, and the green circle here means that the tool call actually finished. So, I'll do control O to decompress again, and then go back over, and now when I refresh, we'll see some or maybe even all of the issues created. Or tickets, I should say. Take a look at that. So, we don't have all of them yet. It's in the middle of running those tool calls, but we have things populated already. And the cool thing here is if we click into any one of these, like let's say I'll just click into the first one for example, AT-14. If I click into this, we have a lot of context given here in the ticket as well. So, another really cool thing is like for a product manager, usually your description isn't even going to be this good because you don't have full context for the more technical details. So, you can also use Claude to provide more context to the developers up front if you want to work with it to, you know, create this kind of issue description. And of course, for the ticket descriptions, it's entirely up to you and your commands for what exactly you'd put here. Like in my create stories command, I specifically said I want the story and acceptance criteria. And then we could even add more context here. Like we could have some more research on how the coding agent would recommend doing this. We could put that as a comment here. Sometimes my Claude code will actually do that by itself. It's cool to see. Um so, yeah, it's actually it is so it's adding technical notes as comments to each of the issues. So, not only are we creating issues, but we're providing more context as the coding agent has done some research for each of the implementations. Like looking into the code base, providing those initial suggestions for how we'd build each one of these things. And so, I'll let that run in the background here cuz that's not like super important for me to have finished before I go to the next thing for you guys. And the next thing is really like let's just pick one of these and let's work on it. Right? Like at this point at an organization level, the product manager would take this list list and send it over to the development team. You know, you might have some scrum meeting or whatever to talk about these things and and again refine things if you uh need to like fix up any of these issues. And then you go on to the development. Or if you are a solo developer, then these might be GitHub issues that you're now going to handle one at a time. And so, we just need to pick one of these to work on. And uh let's see. I'm trying to think like uh maybe the audience vote page would be a good one. As an audience, I want mobile first page that shows only active questions, lets me submit my answer, auto advances when the presenter moves on. That's a decent one. What else could I work on here? I mean, there's a lot of good features. I'm trying to like think of like the best one that would be good for a live demonstration. Uh presenter projection page. Actually, this this is a good one here cuz that's actually what I was planning for my prep. So, I want a full screen page that shows active questions, animated bar chart, real-time updates as things are coming in. That's definitely something that we're we're missing right now cuz this looks pretty bland for the results page. So, we'll tackle this issue first. And the really cool thing is the input into our development process just is this issue. And that's actually something I've been doing a lot more recently with AI coding assistance is my input to writing the code is always some artifact. Like for me personally, uh I do a lot kind of as more of like a solo developer or I'm working on open source projects. So, usually the GitHub issues is actually my entry point. So, I'll put my artifacts here. I just wanted to show Jira because that's how so many teams work. But, uh your Jira tickets, like that is the input. And so, going into the pivot loop here, we're going to go through a similar first step where we're just going to explore our solution. And the input into this is just one of the tickets that we pick. So, the developer takes that work. You can use the Jira MCP to assign yourself. And then, we start exploring the solution. And so, for planning with AI coding, you always have two layers. You have the project level planning, and that's everything that we did here. Right? Like this is like the PM level planning. And then, you have the task planning. And that is the individual ticket level. And the important thing that I I've already explained a little bit here, but I just want to be like really clear on this, is the layer one planning is higher level. Here are the features that we want to build or the bugs we want to fix. At this point, we are not digging into the code. Now that we're taking a single ticket for layer two, this is where we get more in the weeds of things. This is where we're going to analyze the code base, the documentation, figure out what parts of the code base we actually have to touch. We're starting to dive that deep. And it's really helpful for the coding agent to do this two-step process because then now that we're getting really into the weeds of things, we already have a lot of context for what we want to build overall. At this point, the ticket has translated the stakeholder or business requirements, whatever you want to call it, and we may be even have some higher-level recommendations for what part of the code we want to touch. And now, we're just really getting into that. So, just like creating our PRD, when we are creating the actual implementation, we start very unstructured. We're just going to have a conversation with our coding agent figuring out how should we go about solving this problem, fixing this bug, you know, implementing this new feature, whatever that is. And then we go from unstructured to structured. So, this is very similar, like creating a plan for implementation is very similar to creating a PRD. And we're going to have a command for planning out the feature and just like we have a command for creating our PRD. And so, I'll show you guys what this looks like right now. So, I'm going to go back into my code base here. And I'm going to begin a brand new conversation. So, let me escape out of this. I have a brand new conversation with Claude. Because you can imagine that like you as a developer, you are picking up a single ticket and you don't have any context around creating the PRD or stories or anything. So, we're going to pretend like this conversation doesn't exist because it's going to be a someone else doing this or maybe you doing it at a different time. So, brand new conversation. The first thing that I always do when I am preparing for an implementation is I run what is called a prime command. So, another example of if you're going to prompt a coding agent to do something over and over again, just turn it into a prompt, turn it into a command. Cuz that way we don't have to type it out again. And so, this prime command, quite simply, its job is to walk a coding agent through understanding the code base. We want to know what we already have to help us think about what comes next, right? So, we're going to load external context, which this is where we can specify Confluence pages or Jira tickets that we wanted to understand. In our case, we are actually going to specify a Jira issue, right? We're going to understand the code base from the lens of this Jira ticket, this new thing that we want to build. But also, aside from that, we're just going to generally understand the code base. So, we're going to study the features, we're going to study app routes, we're going to check recent Git commits. I love using Git as long-term memory for my coding agents. So, a lot of times, what you've done recently in a code base is going to help guide what you do next, cuz you're going to look at like the code patterns you followed for recent commits and things like that. This is a a very, very powerful part of any new conversation with a coding agent. And obviously, the steps that you want your coding agent to go through to analyze the code base is very custom to your code base. So, all of the commands that I have here are starting points for you, but you're always going to get the most out of them if you customize the commands to your process, your architecture, your code bases. And so, I'll start by running a {slash} prime here. And one of the arguments that we have is a comma-separated list of Jira issues. And so, for example, uh going back to our browser here in Jira, um I just want to use um this issue right here. So, the ID for it is AT23 for our uh presenter projection page. So, I'll do {slash} prime and then just AT23. So, it's going to understand the entire code base, but also from the lens of this issue. So, first it'll use the Atlassian or Jira MCP to pull that context. I can do control O and we can see right here that uh first it's listing accessible resources, and then it's going to call the tool to get that specific issue. Performing a bunch of reads here, also looking at the Git logs in parallel. There's just a ton of context loading that it's doing at the exact same time here. Now, you want to be careful to not load too much context into your coding agent, cuz it's not like you want, you know, 50% of your coding agent's context window to be just loaded with a bunch of research it's doing. But we definitely want to load in the core files and the core history of what we've done recently. And so if you ever want to, you know, tweak that lever of how much context you're bringing into a session up front, it's just you change the prime command, right? Like you change this over time. Like maybe you only load in the first part of a Jira issue or you only read from this part of the code base. It's totally up to you for how you formulate your commands to optimize things for your process. So here we go. Project context loaded. We are going to be handling the presenter projection page, so pulled full context there. Gives me a quick summary of my code base. And um yeah, I think we're we're good to go. Um though it actually it actually says something interesting here. So this is really cool. This is a good uh live teaching moment. It is able to recognize, based on querying my state in Jira, that there are some blockers that we need to take care of before we could really go on to AT-23. So it understands the dependency mapping. That is actually one of the things that I have built into create stories here where it can help you understand dependencies. So maybe we would actually have to handle AT-22 with a QR code first. And um I think this is this is something that we'll take on. So maybe we'll do like, "Okay, look at AT-22. What do we need to implement for that?" Right? We're starting very unstructured in our planning here. We're actually shifting gears right away, which is totally okay, but we're just going to have it get a little bit of understanding of this feature that we want to build. And we'll start to ideate there. So we're going to explore how we want to build this, understand the code base, and then get into that uh structure plan that we'll go and send into implementation. And so at this point uh we have full context from the issue, but now we just do a little bit of exploration. And what this looks like totally is up to your own process. In fact, this is one of the things that I don't actually have as a command because it's very free form at this point. So, I can, you know, for example, go into my speech text tool and say, "All right, let's build AT-22. I want you to spin up a few sub-agents to research the code base and help me ideate around uh how I would build this new feature into our poll application." So, just like a really quick prompt here. And also showing you sub-agents because sub-agents is something that I use all of the time for research. If you aren't familiar, sub-agents is basically a way for you to spin up a uh sub-process, another agent that runs under the hood to go and look at a bunch of things or perform a bunch of work and then report back a summary to our main Claude code agent here. And it's really powerful for research because when we are exploring a code base or doing web research, we are loading in tens of thousands of tokens of information. Like, you can see that this one already loaded in 32,000 tokens. We are going to completely overwhelm our main agent if we had it do all of the research by itself. And with research, you really only need a quick summary at the end, right? Like, here are generally the files that we have to edit. Or if you're doing web research, like, here are the core articles that you should read that would help with um best practices for this tech stack. So, we've already used over 100,000 tokens here, but we only have a few thousand tokens that are returned back to our main agent. And so, yes, with Claude code, with we now have the 1 million token limit with Opus, and there are a lot of other models through Codex and get out copilot and everything where you have 1 million tokens. But, here's the thing. Just because you can fit a million tokens into a large language model does not mean that you should, because they get overwhelmed just like people do. So, we want to deploy strategies for managing context well. Sub-agents is one of the best strategies for that. So, we just have to wait for these three exploration agents to finish, and then our main agent will get back a summary, so it can reason. We can see that these are all done now. So, it'll reason about what the sub-agents did, and then it'll provide me a final output here with its recommendation for how we can handle this Jira ticket. And so, at this point, going back to our diagram here, we're still at this initial exploration, right? Like, we're going to explore ideas, architecture, concepts, tech stack. I'm not going to go through each one of these things right now for the sake of speed. But, this is our chance to ask questions. Or, like we did when we created the PRD, have it ask us questions as well. Because it's important to remove assumptions going into writing the actual code. It might even be more Well, probably not more important than assumptions in the PRD, cuz the PRD is so high-stakes, but it it is very important as well. So, we go through this process where once we feel confident that we're on the same page with the coding agent, then we'll run a command that'll create a structured markdown document for our plan. We want again, we we want the output of our planning process to be a single artifact, and that artifact is going to contain all of the information that the coding agent needs to do the actual implementation. And so, I'll show what that looks like in a little bit, but first I want to actually invoke the command to create the plan, and then I'll explain more how it works, just so that we can have things move along well for us here. So, here's a synthesis with real decisions to make. Here's what we know, okay, and three decisions worth making before coding. So, it's asking me some questions here. I'm going to blitz past these for the sake of demonstration. But, it is worth taking the time with this usually. So, I'll do plan. This is my command where I can now describe the feature that I want to build. So, I'm just going to say here go with your recommendations and create the plan for AT-22. So, I'm just going to give it permission here to just pick whatever it wants. Usually though, it would be worth taking your time and answering these things and having it ask you more questions as well. So, while this planning command runs, not to be confused with the plan mode in Claude code, this is a separate command that I have created right here. It's very similar to the create PRD plan. Where we have phases laid out like here's the research you should do initially, explore the code base, make sure you have full understanding for how we're going to implement it, then create the plan file. So, just like we created a PRD.md, we're now creating a plan.md. And it has our structure. So, we want a summary, a user story. It's going to be similar to the PRD, but now we're getting into the weeds of how we're actually going to implement it. And so, for example, one thing that we definitely didn't have in our PRD command is the patterns to follow. Like here's here's how we're coding things. Here are the files that need to be changed. Here's the task order, everything we're going to execute down to the individual level of the files that we're going to create and update or maybe the commands that we're going to run for testing. So, also laying out out front. How do we want our coding agent to validate its own work? Because when we get into the implementation, we're going to send this plan into the coding agent. We are going to delegate all of the coding to the coding agent. And the only reason that I'm comfortable doing that is because I still find myself in the driver's seat because I'm a part of the planning process. I'm iterating on the plan. I'm doing the exploration and having it ask the right questions. And so, we'll have it write the code, and then we'll also have it do some of the validation, right? Like, we can have the coding agent, right after it does the implementation, we can have it write the unit tests, write the integration tests, do the linting and the type checking, and take care of all of these things. Not that it's going to be perfect, but the point is we want it to take care of as much validation as possible, so that by the time control passes back to us for our human validation, there's less that needs to be corrected. Right? We want to reduce us being the bottleneck for actually shipping the code that we're creating with the help of our coding agents. And so, I'll jump back over to the code base here, and we can see that our plan file is created. I'll take a look at this really quick. Uh just another one of those things that I don't want to spend the time iterating on too much right now, but we have the summary of our work. Uh we have the decisions that we've locked in. These are the things that we would have been working with the coding agent to establish. And then, um we even have like the individual files that need to be created and updated, and then we have the task list. So, usually the task list, you don't create Azure tickets, right? Cuz this is like so granular that this is for a single coding agent implementation. So, you let the coding agent handle an internal task list as it is writing the code. And then, we have the self-validation. So, it's going to be running the type checking and linting and unit testing. We can also have it do end-to-end testing if we wanted to use browser automation tools with um you know, the agent browser CLI, for example. So, that's actually one of the skills that I have for you guys here. It can spin up the browser and navigate through it and like create polls and and vote on the polls just like a user would. And so, for the sake of speed, I won't do that, but you can have coding agents do very, very end-to-end testing. You want it to validate as much as possible. So, the important thing here is once you have iterated on the plan and you're confident in everything, you actually don't do the implementation right here. We want to start a brand new session with Claude code. So, I'm going to open up a a fresh blank slate with Claude. The reason that I want to do this is because when you are working with AI coding assistants, you want to make sure that they are as focused as possible. And it's important to be focused in order to be focused to do your planning and implementing in separate sessions. Because also, the coding agent has probably built up a lot of bias throughout this conversation as you've been working with it. We want it to have a fresh set of eyes on the problem going into implementation. And so, of course, I have an execute command. And so, all I have to do is {slash} implement and then I give it the path to the plan that I created in the prior session. And the whole point of this markdown artifact is that it has all of the context that the coding agent needs to implement cuz it has the summary, it has the recommended files to change, and the task list, and the validation strategy. There's no reason for us to stay within this other context window in the first place. So, I can send off this command. It's going to read the plan, and then it's going to walk through the process I have in the implement command to do the implementation and the validation. And this um command that I have for implementation is actually very very concise. It's uh only like uh a couple of hundred lines long here because really it's the the plan that guides the entire development. The main thing that I'm walking it through here is just the process of, you know, loading the plan, preparing the implementation, like maybe making a new Git branch for example, like any kind of of uh process that you have in your usual software develop life cycle for how you want an engineer to work, we're just encoding that into the command here. We want to make sure that we're uh verifying any kinds of assumptions. So, we're also sort of doing like a second pass on the plan before we go into to implementation. So, yeah, then describing how we want to do validation, for example, when we want to pass control back to the user, outlining all of that for the agent. And so, going back to our diagram here, we're in this step right now. Right? We we've cut a fresh session, sent the plan into implementation, and then we'll wait for it to write the code, do all of its own validation, and then we'll also step in and we'll do a code review. Right? And it's not like you have to do this. Uh some people are are a big fan of just shipping the code right to production and having the coding agent do its own work. I'm I'm not a fan of that myself. I still the engineer in me still wants to review all the code. So, for any like serious production coding that I'm doing, I still am reviewing all of the code myself and then also doing manual testing. And so, we can see that after we do the implementation, like I'll refresh the page here and we'll we'll check out this new feature. Like we'll see the QR code that's generated and we'll make sure that's all working before we would actually be confident to, you know, merge that pull request into our main branch, for example, or whatever that looks like for your software development life cycle going into production. So, that review is important. And um you know, while we wait for the coding agent to run through everything here, you can see that it created its internal task list based on the plan. It's writing the code, doing all the testing. It's actually going to get through this feature pretty quick cuz I purposely built a simple one. Uh but as it is doing this, I want to quickly talk about the last part of the system here. Um and then of course, after this, we'll we'll quickly get into time for Q&A with uh with Lior, too. So, the last thing I want to talk about is system evolution. So, when whenever we do a pivot it is very very far from guaranteed that the implementation will be perfect. Coding agents are not perfect. They are non-deterministic by nature. Even if we work super super hard to align with it in the planning phases, there are still going to be mistakes. But the powerful part of this system is we don't have to just treat the bug as a one-off fix that we address and then move on to the next pivot loop or move on to that next ticket. We can spend some time to fix to also fix the system that allowed the bug. And what I mean by that is we can have a sort of, you know, retroactive session with the coding agent where we say, "Okay, Claude, you allowed this problem to creep into my code base. I want you to dive into your AI layer. Like take a look at the at your rules. Take a look at your commands and skills, the process, the workflow that I brought you through, and I want you to identify things that we could improve there so that this kind of issue doesn't happen again. Like for example, maybe it broke something in the polling here where um I don't know. Let's say that like all of a sudden the website looks really ugly when it when it built this new feature cuz it didn't like create the same like it didn't create the component in the same style as the rest of our code base. Well, maybe that means that there's something in our global rules that we have to update for like our style conventions. Or maybe we need to build something into our our validate workflow where whenever we validate a code base, we make sure that like any new front-end component that we build is in compliance with the styles of our other components that are already in the code base. Just kind of a random example I'm giving you there, but the point is generally when your coding agent does something wrong, there's going to be something in the context you give it that you can improve to not necessarily for sure fix the problem, but you're using it as an opportunity to continue to evolve your AI layer, making your rules more specific over time, making your workflows more reliable. And the best part of this is when you use every single Jira ticket as a potentially an opportunity to improve your system, you get to improve the whole process for everybody. Because you can check in your rules and commands and skills into source control just like your code base, the entire team can reuse these things and you can even create pull requests to update commands just like you create pull requests to update your code base. So, you can do code reviews making sure that everyone's in line with the changes you're making. I know that sounds like a decent amount of work, but it's so high leverage. Because every single time you improve a command or a skill, it might save engineers dozens and dozens of hours going forward because you've now made the validation process more reliable or you've made the style conventions respected more often, whatever that might end up looking like. And so, really like the four things that I generally improve over time in a code base is my commands, my on-demand context. This could also even mean like things in Confluence. You just, you know, optimize your documents in Confluence for AI understanding. Your global rules and then also of course like your plan and PRD templates. You might want to define and fix gaps in those over time. And so, for every single code base, I'm constantly doing this. Right? Like if I have a pivot loop where there is some kind of major issue, I step outside of the pivot loop to do this system evolution. I will update things that I created up front and then I'll go into the next pivot loop. And uh if if actually there are no issues at all and the coding agent completely rocked that Jira ticket, then literally you just go loop right back, right? You go through the planning process, you load that next Jira ticket, and you go through the process. So, it becomes very, very cyclical. There's basically two loops here. You have the inner loop when everything's working well and you're just chugging through the work with the help of your coding agent. And then you have the outer loop when you're taking some time to reflect and make your your better. So, it's not like you always have to do the outer loop, but I encourage you to do it pretty often. Because not only are you improving your your commands in other parts of your system here, but you are also customizing your process to your specific code base over time. It's like what I said, all of the commands and skills that I have for you guys here, they're a starting point, but they're more general, right? Like if you want to really optimize something for your process, you're going to start with these, find opportunities to make them more specific to your validation strategy or your planning strategy, whatever that might be. So, I hope that makes sense. I mean, that really is the whole process at a high level here. And uh so, I'm going to head back to Claude here and see where we are at. Okay, so the implementation is complete. We did it in a branch cuz our implementation command told it to. We ran all of our validation here. Here are the files that are changed. It's giving us a summary of everything that was done. It says that the implementation matched the plan. So, I also have a part of the process here. This is actually something I did recently for my system evolution where after it does the implementation, it looks at the code and compares it to the plan to make sure that we didn't deviate. And then it also used the uh MCP server from Atlassian to update the ticket. So, there's a lot of the admin work that we did as well, you know, creating the branch, creating the pull request, updating the Jira ticket. We don't have to have the developer spend their time doing that stuff retroactively. So, now if I go back and I refresh my page here in Jira, we can see that uh everything is to do except for this one piece of work that we picked up here. And I believe I think I think it also said there was even a comment. Yep, here we go. So, it also posted a comment with full details. And maybe this is more, you know, context than we'd really want as a comment on a Jira ticket, but if you have a problem with this, then that would, you know, also be an opportunity for system evolution where you just specify in the implement command, once you're done with the implementation, here Here a more concise version of context that I'd want you to comment on the Jira ticket. So now we can have this going into a code review, send it off to, you know, your VP to go and review, or you know, whatever that is. So pretty cool. And then we can also test this in the application here. So I'm going to refresh here. I'll create a new poll. Um let's say what's for lunch. And we'll just say um spicy mango chicken or spicy mango beef. All right, cool. So I'll create this poll. And uh I don't actually see the QR code. I might need to restart the application. I think that might be why. So let me go back here and say uh all right, I want you to restart the application and then use the agent browser skill so you can visit it and make sure we have the QR code. And then let let me know like how I can see the QR code myself. All right, so I yeah, I think I just have a stale version of the application. Um yeah, so I also I mean if I want to like look at more context, I can literally just go to the ticket here. So we have a server helper. I mean, this is like a bit more technical. Like honestly, I I would probably rather have a higher level overview of what was actually built. Uh again, something you could just change in the command. Um but yeah, so let me go ahead and jump back over, see what Claude said. Um code utility. There's no consumer of it yet. Oh, I got it. Okay, so it built out the code, but we need to actually make it so that the front end consumes it. Um I want you to quickly uh implement the consumer. Just really fast. No validation, no Jira ticket. Just go and add this right now so that I can see it live. Okay, so that that's my bad. I didn't catch the fact that this was just getting the pipe the piping in place. And then it is that follow-up issue that we're originally looking at that does the presentation. So that's on me. So every everything is working as intended, but we just have to Okay, so So, created a QR demo page. So we can we can quickly look at that. So, we'll see that in a second once it um once it uh does its own validation. So, I I'm also showing a live demonstration of the agent browser where we can see it open up the website. And uh it'll even like take a screenshot to and vi- validate things visually, too. And then of course, in parallel, we can do the exact same thing. So, I'll go back to the application and then I'll just do QR demo. Pretty cool. So, yeah, I know that uh this is just a placeholder here, but I told it to build something quick to validate to the piping that we put in place. And so then when we go on to the next issue, the one that was depending on this, then that's when we build in the full presentation view and actually use the the QR code for real. And again, the point of this isn't to show the full application, but just the process that uh builds these kinds of things. So, all right. Uh that that is that is really the process as a whole. We've covered it We've covered it all from planning all the way to system evolution and creating those pull requests, getting that code into production. And uh I do want to reiterate that like this process takes a good amount of time. It's It's not like you're going to blitz through something as fast as me. It It can be if you want, but uh the important thing is even if you do take a lot of time iterating on the plans and validating the code, it's still going to save you so many hours of work creating those documents, updating things in Jira, writing the code. You The The days are gone now of going to Stack Overflow in order to uh get your questions answered. You don't have to copy and paste and be a Stack Overflow warrior anymore. So, yeah, there you go. That is the full process for AI coding. It's foundational and simple enough where you can take this and mold it to whatever your software development process is, standardizing things across your team with the AI layer as well.

---

## Timestamped Segments

**[0:00]** What I have for you today is a polished

**[0:02]** up version of a super value packed live

**[0:04]** workshop that I just did yesterday. I

**[0:07]** hosted the AI transformation workshop

**[0:09]** with Lior Weinstein. He's a big name in

**[0:11]** the AI space. It was a blast. And so

**[0:14]** what you're about to see is my portion

**[0:16]** of the event, teaching you in very

**[0:18]** simple terms how to build a foundational

**[0:21]** system for getting reliable and

**[0:23]** repeatable results with AI coding

**[0:25]** assistants. And this is important right

**[0:27]** now because people they over engineer

**[0:30]** and over complicated AI coding

**[0:31]** frameworks all of the time, making it

**[0:33]** seem like you need some fancy harness or

**[0:35]** specialized agents just to do any real

**[0:38]** work at scale. But that really isn't the

**[0:41]** case. So I boil things down into the

**[0:43]** core principles for AI coding here in

**[0:46]** three phases, teaching you how to ideate

**[0:48]** with coding agents, how to build an

**[0:51]** iterative loop, and then how to evolve

**[0:53]** your coding agents over time. A lot of

**[0:55]** this I've covered on my channel, but

**[0:56]** never in one place. There's a reason

**[0:58]** this workshop is one hour. It's super

**[1:01]** value packed. You If you go through this

**[1:03]** entire thing, you come out of it with a

**[1:04]** full system that you have a real

**[1:06]** ownership of. And the best part is it's

**[1:08]** not even that complicated. And so

**[1:10]** without further ado, here is the live

**[1:12]** workshop. Our job as an engineer

**[1:15]** is to no longer write the code, but to

**[1:18]** do the higher leverage tasks like the

**[1:20]** planning and validating. And that's the

**[1:22]** framework that I want to cover here.

**[1:25]** And um also for product managers in the

**[1:28]** room, there's a lot that I have to say

**[1:29]** that applies to you guys as well.

**[1:31]** There's a three-part

**[1:33]** process that I want to walk through with

**[1:35]** you right now. We're going to start with

**[1:37]** how do we ideate around the work that we

**[1:39]** want our coding agents to do for us for

**[1:42]** building literally anything, a website,

**[1:44]** uh funnel, uh any kind of platform. This

**[1:47]** is going to apply no matter what you

**[1:49]** want to build. And then we'll get into

**[1:51]** for the developer when we are knocking

**[1:53]** out a piece of work like a ticket in

**[1:54]** Jira or handling a GitHub issue or

**[1:56]** starting a new application, what does

**[1:58]** that process look like? It's using the

**[2:00]** PIV loop. That's my core methodology

**[2:02]** that we'll cover. And then we'll get

**[2:04]** into the system evolution mindset. And

**[2:07]** this is probably the most powerful part

**[2:09]** of the entire system, how we make our

**[2:10]** coding agents more powerful over time as

**[2:13]** we run into issues using them.

**[2:16]** And uh one disclaimer that I want to

**[2:18]** give before we get into everything here

**[2:21]** is that uh a lot of what I'm covering

**[2:23]** here is a training that I do for

**[2:26]** organizations. But usually for them it's

**[2:28]** more of a 4-hour session where I really

**[2:31]** get into the entire process. And so I've

**[2:33]** compacted everything down into 1 hour to

**[2:36]** share with you guys right now. So a

**[2:37]** high-level overview, but I'm still going

**[2:39]** to get really practical with you guys.

**[2:41]** And I'm going to give you a live

**[2:42]** demonstration of everything here so that

**[2:44]** you can come out of this 1 hour knowing

**[2:47]** exactly what the process looks like that

**[2:49]** you can mold for yourself to go from

**[2:52]** idea all the way to production code with

**[2:54]** the help of a AI coding assistant. And

**[2:56]** the important thing here is we're not

**[2:57]** vibe coding because we are putting

**[2:59]** ourselves in the driver seat along the

**[3:00]** way through all of the planning and

**[3:02]** validation that we do. That is the the

**[3:04]** core framework that I'm going to cover

**[3:06]** with you.

**[3:08]** And uh really this whole process, it

**[3:11]** applies no matter the tools that you're

**[3:13]** using. And so I'm going to be using

**[3:15]** Claude Code for our event here just

**[3:18]** because that is my favorite AI coding

**[3:19]** assistant, at least right now. And then

**[3:22]** I'm going to be using Jira as my place

**[3:24]** to manage all of the work that we scope

**[3:26]** out with the help of Claude Code.

**[3:29]** But this entire process is going to work

**[3:30]** if you're using, you know, Codex with

**[3:32]** GitHub or you're using GitHub Copilot

**[3:35]** with Linear. Really it's just you need

**[3:36]** to have one place to manage your work

**[3:39]** and organize your work and then one

**[3:40]** place to work with a large language

**[3:42]** model to create your code. That's the

**[3:44]** only requirement that I have here. Even

**[3:47]** if you do want to follow along. And also

**[3:50]** in the description for our live stream

**[3:53]** here, if you click into the description,

**[3:55]** I'm just like looking at it on my left

**[3:57]** monitor here, I have a link to a GitHub

**[3:59]** repository. And uh this GitHub

**[4:01]** repository has the demonstration

**[4:04]** application that we're going to be

**[4:06]** building on top of today. And then it

**[4:08]** also has all of the resources that I'm

**[4:10]** going to be showcasing here, my rules,

**[4:12]** my commands, my skills. We'll talk about

**[4:15]** what those look like and I'll use some

**[4:17]** of them live, but a lot of that it lives

**[4:19]** here in the dot cloud folder. So, if you

**[4:21]** see any part of my process that you

**[4:23]** really want to steal for yourself,

**[4:25]** please feel free to do so. This

**[4:26]** repository is open source, ready for you

**[4:28]** to come in and take any of the skills or

**[4:30]** all the commands that I'm using to

**[4:32]** package up my workflows. And so,

**[4:35]** really we're not going to be doing a lot

**[4:36]** of manually typing today because it's

**[4:38]** going to be here are the prompts that

**[4:40]** I've been using time and time again. I

**[4:42]** have it as a command that I can

**[4:44]** reference and have the coding agent go

**[4:45]** through that procedure that I'm using

**[4:48]** pretty much every single time that I'm

**[4:50]** delegating in the coding to AI. So,

**[4:53]** yeah, the last thing I want to say

**[4:54]** before we get into things here is there

**[4:55]** are a lot of frameworks for AI coding

**[4:58]** available to us that are open source.

**[5:00]** So, maybe you guys have explored GitHub

**[5:02]** Spec Kit or B Mad or Claude Flow or GSD,

**[5:07]** um Gas Town. I mean, I could go on

**[5:08]** naming a dozens and dozens of them.

**[5:11]** There are all of these opinionated

**[5:13]** strategies out there right now to guide

**[5:15]** you through a process kind of similar to

**[5:17]** what I'm going to show you here. Like

**[5:18]** this is a process for researching, then

**[5:20]** planning, then building, then validating

**[5:23]** with AI coding assistance driving a lot

**[5:25]** of it.

**[5:26]** And I have a lot of respect for these

**[5:28]** platforms. There are a lot of really

**[5:30]** powerful, timeless software engineering

**[5:32]** strategies built into them, but at the

**[5:34]** same time a lot of these frameworks are

**[5:37]** very over-engineered. They try to do too

**[5:40]** much at once and it's really difficult

**[5:43]** to take an existing off-the-shelf

**[5:46]** framework and mold it to your software

**[5:48]** development life cycle.

**[5:50]** So, like I said, I do a lot of corporate

**[5:52]** trainings where I teach companies how to

**[5:55]** take something very foundational like

**[5:56]** this and mold it to their existing

**[5:58]** practice because you don't want to just

**[6:00]** throw out the window the entire process

**[6:03]** your team has already been using for

**[6:05]** working with coding agents. Instead, you

**[6:07]** want to mold the process around AI, but

**[6:10]** you still are going to have some of your

**[6:12]** conventions in the way that the team

**[6:13]** works. It's not really realistic to just

**[6:16]** throw everything out the window. But,

**[6:18]** when you're using something like BDD or

**[6:19]** Gherkin, you're trying to take an

**[6:20]** off-the-shelf solution, you're kind of

**[6:22]** forced to do that because it's so

**[6:24]** bloated that it's hard to like really

**[6:25]** make it your own. And so, what I teach

**[6:28]** here is simple on purpose cuz I want to

**[6:30]** show you the foundation that you can

**[6:32]** then build on top of to mold it into

**[6:34]** your process for planning, your process

**[6:36]** for QA, whatever that looks like for

**[6:38]** each stage of the software development

**[6:41]** life cycle.

**[6:42]** And so, we'll start with planning here.

**[6:44]** And planning, this part actually applies

**[6:47]** to product managers just as much as

**[6:49]** developers. So, a lot of organizations

**[6:51]** that I work with, um the trainings that

**[6:53]** I do, they'll bring their entire uh PM

**[6:56]** team into the training as well because

**[6:58]** they're actually the first ones that

**[7:00]** have a touch point with the coding agent

**[7:02]** when you're planning the next scope of

**[7:04]** work for an application. So, the product

**[7:06]** manager is the one initially doing, you

**[7:08]** know, let's say the sprint planning. And

**[7:10]** it's important for them, just like the

**[7:11]** developers, to work with coding agents

**[7:13]** to speed up that process. Here's the

**[7:15]** application that we have right now. Here

**[7:18]** are the bugs we want to fix and the

**[7:19]** issues that we want to build or the new

**[7:22]** features we want to build for this

**[7:23]** sprint. And same thing applies to

**[7:25]** greenfield development, you're going to

**[7:26]** be building that initial scope of work

**[7:29]** for the MVP of an application. And this

**[7:31]** process applies to both.

**[7:33]** And so, what I'm going to do with you

**[7:35]** guys right now

**[7:37]** is uh I am going to show this diagram at

**[7:40]** a high level, just walk through it

**[7:41]** really quickly with you, this component

**[7:43]** right here, and then we're going to get

**[7:44]** into something very practical. I'm going

**[7:46]** to go into my uh code base here,

**[7:50]** and we are going to go through

**[7:53]** everything live. I'm going to show you

**[7:54]** what it looks like for brownfield

**[7:56]** development to take an existing

**[7:57]** application, plan out a brand new sprint

**[8:00]** with a bunch of new set sets of work we

**[8:03]** want to perform,

**[8:05]** and then I'm going to pick one of those,

**[8:07]** and we're going to go through the piv

**[8:08]** loop, the process that we're going to

**[8:10]** repeat for every single Jira ticket. And

**[8:12]** again, that could be a GitHub issue, it

**[8:14]** could be a linear ticket, whatever that

**[8:15]** is. And so, you'll see the full process

**[8:18]** end to end. There's a lot of value that

**[8:19]** I have packed into the hour for you guys

**[8:22]** here. So, okay.

**[8:23]** The beginning of the process here is as

**[8:26]** simple as it possibly can be. You are

**[8:29]** going to open up your coding agent, like

**[8:31]** I'll, you know, I'll just pop open

**[8:32]** Claude Code right here, and you're just

**[8:34]** going to have a conversation about what

**[8:36]** you want to build. There is no structure

**[8:39]** at first. And like I said earlier, it is

**[8:41]** simple on purpose, because I want the

**[8:43]** barrier to entry for you to be so

**[8:45]** incredibly low that you begin just

**[8:47]** brainstorming ideas with the coding

**[8:49]** agent, and then we're going to evolve to

**[8:51]** more structure over time. And that's the

**[8:54]** process that I'm going to share with you

**[8:55]** as I start to bring in some skills and

**[8:57]** commands that I have in my AI layer, in

**[9:00]** my AI coding system.

**[9:03]** And so, um first of all, when you have

**[9:05]** this conversation, you just do what I

**[9:07]** like to call a brain dump. Like most of

**[9:09]** the time, I'll literally I'll just use a

**[9:11]** speech-to-text tool, so that I just

**[9:13]** talk. I go on and on about what I want

**[9:15]** to build. At this point, it is helpful

**[9:17]** to be as specific as possible. And so,

**[9:20]** you would say, you know, like, "This is

**[9:21]** my application. Here are the new things

**[9:22]** that I want to build. Here are the bugs

**[9:23]** I want to fix." And then you go into the

**[9:26]** clarifying stage. And so, the most

**[9:28]** important part when you're first

**[9:30]** planning work with a coding agent is to

**[9:32]** reduce the number of assumptions that it

**[9:34]** is making, because honestly, most of the

**[9:36]** time when a coding agent does a bad job,

**[9:39]** it's not like the code is just broken.

**[9:41]** It's that it's not aligned with what you

**[9:43]** were actually looking to build. And

**[9:45]** really, the responsibility is on you

**[9:46]** there because it is your role to and and

**[9:50]** your responsibility to make sure the

**[9:52]** coding agent is really on the same page

**[9:54]** with you for what you are building. So,

**[9:56]** it's a lot of just curating this context

**[9:58]** with the help of a coding agent, being

**[10:00]** very specific for what you want to

**[10:01]** build.

**[10:02]** And so, the most powerful strategy here,

**[10:04]** and you'll see this in action in just a

**[10:06]** little bit, is to have the coding agent

**[10:08]** ask you questions. Like we will

**[10:10]** specifically ask it to ask us questions.

**[10:13]** And you can go through this process for

**[10:14]** a good 20, 30 minutes, even beyond that,

**[10:16]** if you really want to set the stage well

**[10:19]** going into the development later on. So,

**[10:21]** product managers, this is your job when

**[10:23]** you're working with Claude Code. And

**[10:25]** even if you're you know, you're a solo

**[10:26]** developer shipping things without a

**[10:28]** product manager, this is still an

**[10:29]** important step to go through. It's very

**[10:32]** important to stay high-level at first.

**[10:34]** We're not getting into the weeds right

**[10:36]** now for how we're going to test things

**[10:38]** or what files we have to change in our

**[10:40]** code base. At this point, we're just

**[10:41]** trying to figure out what are the

**[10:42]** requirements that we need to translate

**[10:44]** into code. And then we'll have a

**[10:45]** separate planning process where we're

**[10:47]** getting more into, okay, here's how

**[10:49]** we're actually going to code it and the

**[10:50]** parts of code of the code base that we

**[10:52]** need to edit. So, at this point, we're

**[10:54]** very, very high-level.

**[10:56]** And then after you have a conversation

**[10:58]** with the coding agent where you figured

**[11:00]** out exactly what you want to build, what

**[11:01]** is our scope of work for this sprint or

**[11:04]** this new application, then it's time to

**[11:06]** create your AI layer. And I have this

**[11:09]** marked as optional here just because

**[11:11]** when you are working on an existing code

**[11:13]** base, you might already have that AI

**[11:15]** layer already created. But if you don't

**[11:18]** have it, I highly recommend investing a

**[11:20]** lot of time up front building this. Now,

**[11:22]** for our 1 hour here, it's not like I

**[11:25]** have a lot of time to like really get

**[11:26]** into best practices for building your

**[11:28]** global rules and your skills and

**[11:30]** commands. But I'm just saying like this

**[11:31]** is the part of the workflow where you

**[11:33]** will create that. And so, your global

**[11:35]** rules, these are the conventions, the

**[11:37]** rules that you always want your coding

**[11:39]** agent to follow. Like here are our

**[11:41]** coding styles, here's our testing

**[11:43]** strategy, our logging strategy, things

**[11:45]** like that. And then your commands, we're

**[11:47]** going to see a lot of these in action

**[11:49]** today. And your skills, these are your

**[11:51]** reusable workflows. So, anytime you find

**[11:53]** yourself prompting something more than

**[11:55]** three times, you should turn it into a

**[11:57]** command or skill. Because that's just a

**[12:00]** prompt that you're going to load into

**[12:02]** your coding agent when the time comes.

**[12:04]** Like this is my process for planning,

**[12:06]** this is my process for creating PRDs or

**[12:09]** stories in Jira, for example.

**[12:11]** That way we don't have to type things

**[12:12]** out. And it's a reusable workflow that

**[12:15]** we can share and create a standard

**[12:17]** across with our team. Very, very

**[12:19]** important. So, we don't want to do

**[12:21]** manual prompting as much as possible,

**[12:24]** turn things into something in the AI

**[12:26]** layer that you can invoke, right? Like

**[12:28]** we can take a command and skill and say,

**[12:30]** you know, {slash} plan. Now we are going

**[12:33]** into our planning process.

**[12:35]** And so, that actually goes into the

**[12:37]** first command that we'll use here. And

**[12:39]** again, I'll show this all in action in

**[12:40]** just a little bit.

**[12:42]** So, the first command is a process

**[12:45]** guiding the coding agent from an

**[12:48]** unstructured conversation into a

**[12:50]** structured PRD. Like I said, we go from

**[12:53]** exploration to structure. So that we

**[12:56]** have a single document that is produced

**[12:59]** from this command that outlines all of

**[13:02]** the core sections for our and a PRD is

**[13:05]** short for product requirement document.

**[13:06]** So, this is like the initial scope of

**[13:08]** work for an application if we're doing

**[13:11]** greenfield development, or these are all

**[13:13]** of the tickets that we need to handle if

**[13:16]** it's a new sprint that we are planning

**[13:17]** for in Jira, for example. And then I can

**[13:20]** take the PRD and also have Claude code

**[13:23]** split it up into individual pieces of

**[13:26]** work to create as my Jira tickets. We'll

**[13:28]** see this in action.

**[13:30]** And so, it handles literally everything.

**[13:32]** It parses this document. It figures out

**[13:35]** what are the individual phases or pieces

**[13:38]** of work that we should create as

**[13:39]** tickets. And then we'll even use the

**[13:41]** Jira MCP server to create those things

**[13:44]** so that we don't have to do that

**[13:47]** backstage work like Leora was talking

**[13:49]** about of creating those tickets in Jira.

**[13:51]** We want to have our coding agent handle

**[13:53]** all of that administrative work.

**[13:56]** And so, we end with tickets in Jira and

**[13:59]** then we can pick one of them. So, this

**[14:00]** is where, you know, the product manager

**[14:02]** would hand things over to the developer

**[14:04]** to pick a ticket and then go into the

**[14:06]** full Piv loop. This is the full process

**[14:08]** we go through to handle individual sets

**[14:11]** of work with our coding agent. So, we'll

**[14:13]** get into this next, but first I want to

**[14:15]** show you a live demonstration of our

**[14:18]** ideation phase.

**[14:20]** And so, I'll go over to my code base

**[14:22]** now.

**[14:24]** And I'll it's just describe very briefly

**[14:27]** the application that I have for a

**[14:29]** demonstration here.

**[14:31]** And so, this repository, again, I have

**[14:33]** it linked in the description. I also

**[14:35]** linked it in the chat.

**[14:37]** Um actually, I didn't link it in the

**[14:38]** chat, so I'll do that right now. So, let

**[14:40]** me go out, copy this.

**[14:43]** And I'll paste this in our chat here. If

**[14:45]** you guys want to just poke around the

**[14:47]** resources that I have for you guys and

**[14:49]** or even follow along, you can feel free

**[14:51]** to do that. Uh the application for my

**[14:54]** demonstration is just the quick poll

**[14:55]** builder. So, you know, you put in your

**[14:57]** question like uh how experienced are you

**[15:01]** with AI coding? And then we have our

**[15:03]** options here like I'm a beginner, I'm

**[15:05]** intermediate, or I am advanced. All

**[15:09]** right, cool. And then I create a poll.

**[15:10]** Yeah, the point of this application is

**[15:12]** that it's super simple because I'm going

**[15:13]** to be focusing on the process, not

**[15:16]** focusing on the application itself,

**[15:18]** right? So, I want something very quick

**[15:20]** to build on top of so that I can quickly

**[15:22]** go through how I create stories, handle

**[15:25]** tickets, go through the pivot loop, and

**[15:27]** the system evolution.

**[15:29]** And so, uh what I'm going to do to begin

**[15:32]** is I'm going to go into Cloud Code, and

**[15:35]** I'm going to plan my next fictitious

**[15:38]** sprint. So, we have this very basic

**[15:40]** application right now where we can

**[15:42]** create a poll, and if I, you know,

**[15:44]** actually had the application deployed,

**[15:46]** then people could use it and go and and

**[15:48]** answer the poll, but there are a lot of

**[15:50]** features that are missing. And so, I

**[15:53]** have a prompt prepared ahead of time

**[15:56]** that I'm just going to paste in right

**[15:57]** now, just so that you guys don't have to

**[15:59]** watch paint dry as I give my initial

**[16:01]** brain dump. But again, this is your

**[16:03]** point where you just dump all of your

**[16:06]** ideas of what you want to build, being

**[16:08]** as specific as possible. So, even if you

**[16:11]** wanted to specify things like your tech

**[16:13]** stack and your architecture, if you're

**[16:14]** more technical, this is where you do

**[16:16]** that. But even if you are less

**[16:18]** technical, and you are, you know,

**[16:19]** product manager, for example, you can

**[16:21]** still stay pretty high-level here, and

**[16:24]** just describe the features that you want

**[16:25]** to build.

**[16:28]** And so, I'm saying like here's my brain

**[16:29]** dump for phase two, like the next thing

**[16:31]** that I want to build on top of the

**[16:33]** application. Let's say I want to build a

**[16:35]** live presentation mode. Like right now

**[16:37]** in the poll builder, when I I can't

**[16:40]** really like see answers come in live.

**[16:41]** Like if I click see current results, I'd

**[16:43]** have to refresh the page in order to see

**[16:46]** new entries.

**[16:47]** I also want to build a QR code

**[16:49]** generation, multi-question polls,

**[16:52]** multiple choice questions. Like there's

**[16:53]** like a lot of things that I want to

**[16:55]** build on top. This is my next sprint

**[16:57]** that I want to uh you know, my end goal

**[16:59]** is to have all these things created as

**[17:02]** uh Jira tickets that I could then pass

**[17:04]** on to developers, or pass on to my

**[17:06]** coding agents if I am a developer.

**[17:09]** And so, I've described everything here.

**[17:11]** Um usually, if I'm not just doing a live

**[17:13]** demonstration, I would make this prompt

**[17:15]** a lot longer, but I just wanted to keep

**[17:17]** it concise right now. And then the

**[17:19]** important thing here, this is what I was

**[17:21]** saying in the diagram, before you write

**[17:23]** anything, ask me clarifying questions

**[17:26]** one at a time using the ask user

**[17:28]** question tool.

**[17:30]** And so now this is where I'm going to

**[17:32]** make sure that I get on the same page

**[17:34]** with my coding agent.

**[17:36]** And so one at a time it's going to ask

**[17:37]** me these questions and in Claude code we

**[17:39]** have this ask user question tool where

**[17:41]** we can see these questions pop up with a

**[17:43]** multiple choice answers for us. So it's

**[17:45]** really easy to blitz through things cuz

**[17:47]** a lot of times what it recommends is

**[17:50]** actually what I'm going to go with, but

**[17:51]** it still gives me the opportunity if I

**[17:53]** want to say like, "Hey, no, you're wrong

**[17:55]** here. Like let's actually do it this way

**[17:56]** instead." So we can, you know, remove

**[17:58]** that that incorrect assumption that it

**[18:00]** was making.

**[18:02]** And for other coding agents that don't

**[18:04]** have this specific tool, it's this whole

**[18:06]** process is still going to work. It's

**[18:08]** just going to be a little bit slower cuz

**[18:09]** you'll have to type out each of your

**[18:11]** answers more like you're just chatting

**[18:13]** with an agent. Um but it still works in

**[18:15]** exactly the same way. So it's asking us

**[18:17]** questions here like how should real-time

**[18:18]** updates work? I'll just go with what it

**[18:21]** recommends here just for the sake of

**[18:22]** speed, but also you have this option to

**[18:24]** chat with it. So for each individual

**[18:25]** thing if you really want to dive deep

**[18:27]** with the coding agent, which a lot of

**[18:28]** times I would recommend you do, you have

**[18:30]** the opportunity to do that.

**[18:33]** And of course how deep you go does

**[18:35]** depend on how technical you really are.

**[18:36]** Like right there, you know, how should

**[18:38]** real-time updates work? That is a pretty

**[18:39]** technical question. So if you want to

**[18:41]** just go with what it recommends, that's

**[18:43]** definitely okay. But if you have that

**[18:45]** knowledge and then like really

**[18:46]** understand the architecture of the code

**[18:48]** base, it's just more power to you.

**[18:50]** You're able to to really make sure that

**[18:51]** you clear assumptions. Otherwise if

**[18:53]** you're, you know, more on the product

**[18:54]** manager side, you might have a couple of

**[18:57]** wrong assumptions that sneak into your

**[18:59]** Jira tickets, but that's why you work

**[19:00]** with the developers as you're planning

**[19:02]** things, right? Like you'd have your

**[19:04]** sprint meeting where you'd make sure you

**[19:05]** clarify these kinds of things.

**[19:07]** Uh but the goal is just for the coding

**[19:09]** agent to help us with that starting

**[19:10]** point of having all the context in Jira

**[19:13]** ready for developers to refine and pick

**[19:15]** up and work on.

**[19:17]** And so, for the sake of demo, I'm going

**[19:18]** to say let's end the questions here.

**[19:22]** Just because sometimes it can go on for,

**[19:23]** you know, a good 10-15 minutes asking us

**[19:26]** a lot of questions. I'll allow it to

**[19:27]** make some assumptions for the sake of

**[19:29]** speed. But at this point, you know, I've

**[19:31]** already shown you what I need for what

**[19:33]** this process generally looks like. And

**[19:35]** so, at the end of our chat here, this

**[19:38]** context, this short-term memory for

**[19:40]** Claude code, is what we're going to turn

**[19:42]** into the PRD. So, we are about to run

**[19:46]** our first command where we create that

**[19:48]** product requirement document. The input

**[19:50]** is the conversation. The output is a

**[19:53]** single document, a source of truth that

**[19:56]** we could, you know, then upload to

**[19:57]** Confluence or check into source control,

**[19:59]** wherever you want to store that, and

**[20:01]** then we can create the Jira tickets from

**[20:03]** that.

**[20:04]** All right. So, that was the last

**[20:05]** question there. Now, it's it's taking in

**[20:07]** my message. So, it will move on to

**[20:10]** creating our PRD. And Claude code is

**[20:13]** smart enough to know the capabilities

**[20:15]** are available. So, when I've gone

**[20:17]** through this process a lot of times,

**[20:18]** it'll just go right to loading the

**[20:20]** create PRD skill, and it'll walk itself

**[20:23]** through creating that document in

**[20:25]** exactly the structure that I'm looking

**[20:27]** for.

**[20:28]** And so, I'll go ahead and open that so

**[20:31]** we can see ahead of time what it

**[20:33]** actually looks like. And again, all of

**[20:34]** these commands that I'm about to walk

**[20:36]** through are available in the GitHub

**[20:38]** repository that I have linked in the

**[20:39]** description. So, I'll go to create PRD.

**[20:42]** That is our first command. And again,

**[20:44]** commands and skills are really just

**[20:46]** procedures. They are prompts that we get

**[20:49]** to load in in real time whenever we

**[20:50]** want. And so, create PRD. This is going

**[20:54]** to generate a comprehensive product

**[20:55]** requirements document. We are we get to

**[20:57]** also specify like where it also outputs

**[20:59]** this file. So, commands and skills

**[21:01]** support arguments. So, that's how we can

**[21:03]** make things dynamic. And we'll we'll

**[21:05]** talk about arguments quite a bit cuz

**[21:07]** most [snorts] of my procedures have

**[21:09]** arguments. So, I can make them specific

**[21:11]** to what I am doing right now.

**[21:14]** And the main thing that we are outlining

**[21:16]** in this PRD

**[21:17]** command is the structure that we're

**[21:19]** looking for. Like, we want every PRD to

**[21:21]** have an executive summary, a mission,

**[21:23]** target users. This is a lot of product

**[21:26]** manager speak. So, if you come from the

**[21:27]** product manager space, really this is

**[21:29]** your opportunity to take how you already

**[21:31]** write PRDs and make it so your coding

**[21:33]** agent does it in the exact same thing.

**[21:35]** Again, the foundations that I'm laying

**[21:37]** for here in this process is not for you

**[21:39]** to completely have a blank slate for

**[21:42]** your software development life cycle,

**[21:44]** but to take your best practices that you

**[21:46]** established as a team and teach it to

**[21:48]** your agents. That's what we're doing

**[21:50]** with skills and commands. And so, your

**[21:51]** PRDs are going to look the same, but

**[21:53]** your agent is saving you hours and hours

**[21:55]** and hours because it gets to generate

**[21:57]** this based on our conversation.

**[22:01]** And so, right here like what I can do is

**[22:03]** it kind of

**[22:05]** went through this itself like it loaded

**[22:07]** the skill automatically, but I'll just

**[22:08]** show you like if I wanted to invoke it

**[22:09]** myself, I can just do create PRD. And

**[22:12]** then I can specify the file name as an

**[22:14]** argument like this. It's just when you

**[22:16]** invoke something or similar to when you

**[22:17]** invoke something in the command line for

**[22:19]** all you developers. So, we just have

**[22:21]** space separated arguments for anything

**[22:24]** that we want the command to respect like

**[22:27]** where we're going to output it. So,

**[22:28]** we're going to have something in the dot

**[22:30]** agents folder. It'll just be like a

**[22:32]** marked out PRD in markdown file. And

**[22:34]** then of course we could you know like

**[22:35]** use the Jira MCP server to upload or the

**[22:39]** Atlassian MCP server to upload it to

**[22:41]** Confluence. We could upload this

**[22:43]** document to Google Drive or put it as

**[22:46]** context in a GitHub issue. However, you

**[22:47]** want to you know store this artifact

**[22:50]** that is like the initial source of truth

**[22:52]** for that new application or that new

**[22:54]** sprint that we are planning.

**[22:57]** And so, once we have our PRD created and

**[23:00]** it's going to take a little bit um,

**[23:02]** because it's generating a larger

**[23:03]** document here. You can see that Claude

**[23:05]** is currently thinking through the

**[23:07]** structure. So, it's taking this

**[23:09]** conversation, reasoning about everything

**[23:11]** that we we have discussed here, and then

**[23:13]** creating a document from that. Once we

**[23:16]** have our PRD, we are going to create our

**[23:19]** stories. Now, you could do this as a

**[23:22]** single command, where you create the PRD

**[23:24]** and the stories all with a single call

**[23:26]** to Claude Code. The reason I have these

**[23:29]** separated is because once you have the

**[23:31]** PRD created, it is a good time for you

**[23:34]** to validate things yourself. So, going

**[23:37]** back to the diagram here,

**[23:40]** it is important for us to delegate as

**[23:42]** much coding to the coding agent as we

**[23:45]** possibly can. That's the backstage work

**[23:47]** for developers now. But, we want to

**[23:50]** remain in the driver's seat because

**[23:51]** every single artifact that our coding

**[23:53]** agent produces, whether it's a PRD or

**[23:57]** it's a set of code, we want to review

**[23:59]** that. And we want to have human in the

**[24:02]** loop so that we can iterate on anything.

**[24:04]** And so, when we create our PRD, it's not

**[24:07]** good enough to just immediately create

**[24:09]** stories from that. Like, it's important

**[24:11]** for us to review the artifact and make

**[24:13]** sure that things are really aligned with

**[24:16]** what we are looking to do next. Because,

**[24:18]** yes, we had it ask a bunch of clarifying

**[24:20]** questions, but maybe we didn't have it

**[24:22]** ask enough questions. Or maybe it didn't

**[24:24]** quite understand our answers. That's why

**[24:26]** it's important for us to still review

**[24:28]** things. So, I I know that takes some

**[24:30]** time, and the promise with AI is that it

**[24:33]** speeds things up a lot. But, even if you

**[24:36]** do take time refining the PRD with the

**[24:39]** coding agent, it's still going to save

**[24:41]** you so many hours compared to if you did

**[24:43]** this entire process yourself.

**[24:46]** And so, for the create stories command,

**[24:48]** we run this after we have reviewed the

**[24:51]** PRD and maybe made some changes to it.

**[24:54]** And so, for this command, we give it the

**[24:56]** path to our PRD. Obviously, we want

**[24:58]** Claude code to know like this is the PRD

**[25:01]** that we want to create our stories from.

**[25:03]** And then we can also specify the Jira

**[25:07]** project and epic. And so, what I have in

**[25:10]** Jira created ahead of time is I just

**[25:12]** have a a simple project created with an

**[25:16]** epic that doesn't have any tasks in it

**[25:18]** right now. So, this is what we're going

**[25:20]** to populate live in a little bit with

**[25:22]** our create stories command.

**[25:24]** And so, I had to do a little bit of

**[25:26]** manual work to actually create the epic.

**[25:28]** But after that point, I'm not doing any

**[25:31]** work myself in the Jira platform. That's

**[25:34]** all backstage. I don't want to do that

**[25:36]** myself. And so, I want to have a single

**[25:38]** process

**[25:40]** that goes from here are my ideas to

**[25:42]** everything is populated here. And it

**[25:44]** feels like magic every time this

**[25:45]** happens. So, we'll get to that in a

**[25:47]** second, but obviously, we need to have

**[25:50]** the PRD created first. And you can see

**[25:52]** that right now. It's outputting a lot of

**[25:54]** tokens cuz it's in the middle of

**[25:55]** creating that file for us. So, we just

**[25:57]** have to be patient. But uh that gives me

**[26:00]** some time here just to show you really

**[26:02]** quickly what uh we have in this command

**[26:04]** here.

**[26:05]** So, first of all,

**[26:07]** we have a phase-by-phase procedure that

**[26:09]** we're walking Claude code through.

**[26:11]** Again, commands are just prompts that

**[26:12]** we're we're having the coding agent run

**[26:14]** through.

**[26:15]** So, we're having it load the PRD cuz we

**[26:17]** can also run this in a separate Claude

**[26:19]** code session if we don't want to run it

**[26:21]** in the same one. So, we can load the

**[26:23]** PRD. That's all the context it needs.

**[26:25]** Then it's going to break down into

**[26:27]** stories, and I can render this so it

**[26:29]** looks a little bit nicer here. So, we

**[26:30]** create a user story, and we can specify

**[26:32]** the format as well. We can define the

**[26:34]** acceptance criteria. So, just like we

**[26:36]** create the structure for the PRD in the

**[26:39]** create PRD command, we can do the same

**[26:41]** thing for the stories here. So, your

**[26:43]** team probably already has a convention.

**[26:46]** Or if you're a solar solo developer, you

**[26:48]** still probably have some kind of

**[26:49]** convention for how you want to create

**[26:51]** these artifacts. Here are my tasks, here

**[26:53]** are my issues, whatever that is. And so

**[26:55]** we bake that into the command.

**[26:58]** And that makes it more reliable,

**[26:59]** repeatable, and it makes it so that you

**[27:01]** don't have to have a brand new process

**[27:04]** that everyone is extremely uncomfortable

**[27:05]** with, right? Like we want to make it

**[27:08]** easy to adopt these new tools and new

**[27:10]** processes.

**[27:12]** And so then we go on to the structure

**[27:13]** for each story. Here is exactly what

**[27:16]** you're going to create. Here's how we're

**[27:17]** going to order them. We even have some

**[27:19]** validation built in, so it kind of

**[27:20]** checks its own work to make sure that it

**[27:22]** has, you know, fully extracted all the

**[27:24]** phases out of the PRD, for example. And

**[27:26]** then we have the output. We're going to

**[27:28]** save everything to markdown documents.

**[27:31]** And then if we have the Jira

**[27:32]** integration, so I actually set this

**[27:34]** command up so that if you're not working

**[27:36]** with Jira, then you can still just work

**[27:37]** with the stories in local files. A lot

**[27:40]** of solo developers just manage their

**[27:41]** entire system with markdown. And that's

**[27:44]** totally respectable. So this command

**[27:45]** works for that. But if we do have the

**[27:47]** Jira integration,

**[27:49]** and we tell it how to check for that,

**[27:51]** then it's going to create everything in

**[27:53]** the epic that we specified um in the

**[27:56]** argument here. So like if these things

**[27:57]** are filled in, and we'll see that in

**[27:59]** just a second. So okay, we created our

**[28:01]** PRD.

**[28:02]** And so we can take a look at this.

**[28:05]** So this document, I'm not going to read

**[28:07]** through the entire thing right now, cuz

**[28:09]** it's a pretty long document. The point

**[28:11]** of uh what I'm demonstrating right here

**[28:13]** is mainly to show you that the structure

**[28:16]** that we have laid out in the create PRD

**[28:18]** command is exactly what we see in our

**[28:21]** final PRD. So we have our executive

**[28:23]** summary, our mission, our target users,

**[28:25]** everything that I showed you in the

**[28:27]** markdown here.

**[28:29]** And then we also have what is in scope.

**[28:31]** So for our phase two sprint, we want the

**[28:34]** multi-question polls, per user toggle,

**[28:37]** the full-screen presenter presentation

**[28:39]** page, uh everything that we gave in our

**[28:41]** initial brain dump.

**[28:43]** So this PRD is the result of our

**[28:46]** conversation plus the create PRD

**[28:49]** process, right? Like those two things

**[28:51]** together, this is the baby of that.

**[28:54]** And so now this PRD, we can run through

**[28:56]** our create stories command.

**[28:59]** And this is the thing is like after that

**[29:02]** initial brain dump, I'm really not doing

**[29:03]** much typing. I'm running commands, I'm

**[29:05]** answering questions, that's really all I

**[29:07]** have to do.

**[29:08]** And so I'm going to go ahead and copy

**[29:10]** this. And like I said, you could do this

**[29:12]** in a separate context window if you

**[29:14]** wanted to, but I'm just going to do it

**[29:16]** right here because it was relatively

**[29:17]** short. So I'm not going to iterate on

**[29:19]** the PRD for the sake of speed here.

**[29:22]** Um so I mean this is one moment where

**[29:24]** it's, you know, do as I say not as I do,

**[29:27]** but uh generally if I am off camera and

**[29:29]** really working through my initial

**[29:31]** planning for something, I'm going to

**[29:32]** spend a lot of time looking through each

**[29:33]** section here and making sure that

**[29:35]** everything is as I intend. And so I'll

**[29:38]** run create stories with uh the path to

**[29:41]** my PRD, and then I have to give the ID

**[29:44]** of my Jira project and also the ID of my

**[29:48]** tag. And so for those of you who are

**[29:50]** using Jira, you just get that like this

**[29:52]** is the ID of your project and then this

**[29:55]** is the ID of your epic.

**[29:57]** And then if you're doing something else

**[29:59]** like using GitHub or Linear, you're

**[30:01]** going to go through the exact same

**[30:02]** process. You're just going to use, you

**[30:03]** know, the GitHub CLI to create issues

**[30:06]** instead of the Jira MCP server or you're

**[30:08]** going to use the Linear MCP server. So

**[30:10]** again, it doesn't matter in the end what

**[30:12]** tool you're actually using. So I'm going

**[30:13]** to go ahead and run this.

**[30:16]** So it's going to break down, it's going

**[30:17]** to follow that exact process that I just

**[30:18]** showed you, breaking down the PRD, and

**[30:20]** then after a few minutes, it'll take a

**[30:22]** little bit of time for it to reason

**[30:23]** about that, we'll see all of the

**[30:25]** subtasks start to get populated here in

**[30:28]** Jira. And then at that point, we can

**[30:30]** have developers just pick them up and go

**[30:32]** through the pivot loop that I'll cover

**[30:34]** with you guys next.

**[30:35]** And that's the beauty of it is also you

**[30:38]** can have developers work on everything

**[30:39]** in parallel. They can assign themselves,

**[30:41]** you can also, you know, use the Jira MCP

**[30:43]** server to have the the developer get

**[30:45]** assigned automatically when it picks up

**[30:47]** a piece of work. You can create a system

**[30:50]** in your task management software where

**[30:52]** really agents are managing everything.

**[30:55]** It's kind of like the the whole CTO X OS

**[30:58]** that Lior was showing you guys where you

**[31:01]** have the agent managing all of the grunt

**[31:03]** work of organizing and um you know, all

**[31:06]** of the you know, CRUD operations of

**[31:08]** creating tasks and updating them and

**[31:09]** assigning them and everything. We can

**[31:11]** have agents manage all of that with the

**[31:13]** Jira MCP server.

**[31:15]** And I'll show you guys what that looks

**[31:16]** like. If if you go into Cloud Code and

**[31:18]** do {slash} MCP, you can see that I have

**[31:21]** the Atlassian

**[31:23]** uh MCP server connected. So, by the way,

**[31:24]** this also gives me access to Confluence,

**[31:27]** not just Jira. So, if you wanted to like

**[31:29]** store documents in Confluence, like you

**[31:31]** wanted to store the PRD in Confluence

**[31:33]** and then have a developer load that PRD

**[31:36]** with the Jira MC or the Atlassian MCP

**[31:38]** server, they can do that as well. Um and

**[31:41]** so, if you are an Atlassian kind of shop

**[31:43]** where you have Confluence and you have

**[31:45]** Jira, you can have your coding agents

**[31:46]** manage all of that. And it's really the

**[31:48]** same thing no matter the platform that

**[31:49]** you're using.

**[31:50]** And so, the way that I have this MCP

**[31:52]** server configured is just with this um

**[31:55]** mcp.json file. And if you're curious how

**[31:58]** I set this up,

**[32:00]** this is the crazy thing, guys, is that

**[32:02]** you can have Cloud Code help you with

**[32:04]** anything. It has access to its own

**[32:07]** documentation. So, if you say, you know,

**[32:09]** help me copy over Cole's commands, and

**[32:12]** you just give it the path, it can bring

**[32:14]** all that into your own project. Or you

**[32:16]** say, help me set up the Atlassian MCP

**[32:19]** server, it'll search the web, it'll pull

**[32:21]** the exact configuration, it knows to

**[32:23]** create a file called {dot}mcp.json,

**[32:26]** it'll set up everything for you. The the

**[32:29]** time in in our world where we had to be

**[32:32]** technical to do these kinds of things is

**[32:34]** no longer here, right? Like a product

**[32:37]** manager, a QA engineer can use Claude

**[32:40]** code to do any part of their job just

**[32:41]** like a developer can because you don't

**[32:43]** have to know how to run commands or set

**[32:45]** up MCP servers anymore. I mean, yes,

**[32:47]** it's still helpful just in case the

**[32:50]** coding agent trips up. So, it's faster

**[32:52]** for a developer.

**[32:53]** But uh also coding agents are really

**[32:55]** good at debugging things. If the MCP

**[32:57]** server doesn't connect right away, you

**[32:59]** can ask it like, "Hey, I'm getting this

**[33:01]** error. Help me figure it out." Maybe

**[33:02]** like search the web for some more

**[33:04]** Atlassian documentation, for example.

**[33:07]** And so, really for like all these

**[33:08]** things, I didn't configure that all

**[33:09]** myself. Like I have my repository of

**[33:12]** commands and skills. I pointed Claude

**[33:14]** code there and I said, "All right,

**[33:16]** Claude, for this AI transformation

**[33:17]** workshop that I'm doing with Lior, I

**[33:19]** want you to set up a brand new

**[33:21]** repository and bring in my resources and

**[33:23]** customize it to work with Jira instead

**[33:25]** of GitHub, for example." And it just did

**[33:27]** all of that for me.

**[33:29]** So, a little bit meta there, but I hope

**[33:30]** that demonstration is um is cool just to

**[33:33]** see like how easy it is to get anything

**[33:35]** configured in your AI coding

**[33:37]** environment. And so, for all these

**[33:38]** resources that I share with you, you

**[33:40]** don't even have to bring them in

**[33:42]** yourself.

**[33:44]** So, we can see that it created all of

**[33:46]** the stories here, and then it asked me a

**[33:48]** question like, "Do you want to push to

**[33:49]** Jira now?" So, I said, yes, and now it's

**[33:52]** going to take advantage of that

**[33:53]** Atlassian MCP server to populate

**[33:56]** everything.

**[33:57]** And so, I don't think we'll have it yet.

**[33:59]** Let me refresh the page, but we'll in

**[34:00]** just a second here, we'll start to see

**[34:02]** things get populated. I think it's in

**[34:03]** the middle of reasoning through that.

**[34:08]** Okay. Yep, so we can see that the token

**[34:10]** count go up as it is formulating those

**[34:13]** tool calls, basically. So, the agent is

**[34:16]** performing these operations under the

**[34:17]** hood. And we're almost done with the

**[34:19]** first step, by the way.

**[34:20]** And once we get into the pivot loop,

**[34:22]** things go pretty quickly because we're

**[34:24]** doing so much of the work up front with

**[34:26]** our ideation. So, we're getting to this

**[34:28]** stage right now where we are getting our

**[34:30]** tickets in Jira, and then we'll pick a

**[34:32]** ticket, and then this is where we just

**[34:34]** rip through the implementation with the

**[34:36]** pivot loop.

**[34:37]** So, all right, let's go back to Claude

**[34:40]** and see where we are at.

**[34:43]** All right, so calling at Atlassian seven

**[34:45]** times. You can also in Claude do control

**[34:47]** O so that you can see the full tool call

**[34:50]** if you want some more visibility into

**[34:52]** what it's doing. So, it's using the

**[34:54]** create issue MCP tool.

**[34:57]** It's got my ID, the project, all the

**[35:00]** things that we specified as parameters

**[35:02]** like the epic,

**[35:03]** and the green circle here means that the

**[35:05]** tool call actually finished. So, I'll do

**[35:07]** control O to decompress again, and then

**[35:10]** go back over, and now when I refresh,

**[35:12]** we'll see some or maybe even all of the

**[35:15]** issues created.

**[35:17]** Or tickets, I should say. Take a look at

**[35:18]** that. So, we don't have all of them yet.

**[35:20]** It's in the middle of running those tool

**[35:21]** calls, but we have things populated

**[35:23]** already. And the cool thing here is if

**[35:25]** we click into any one of these,

**[35:28]** like

**[35:29]** let's say I'll just click into the first

**[35:30]** one for example, AT-14. If I click into

**[35:33]** this, we have a lot of context given

**[35:36]** here in the ticket as well. So, another

**[35:39]** really cool thing is like for a product

**[35:41]** manager, usually your description isn't

**[35:44]** even going to be this good because you

**[35:46]** don't have full context for the more

**[35:48]** technical details. So, you can also use

**[35:50]** Claude to provide more context to the

**[35:52]** developers up front if you want to work

**[35:54]** with it to, you know, create this kind

**[35:55]** of issue description. And of course, for

**[35:57]** the ticket descriptions, it's entirely

**[35:58]** up to you and your commands for what

**[36:02]** exactly you'd put here. Like in my

**[36:04]** create stories command, I specifically

**[36:05]** said I want the story and acceptance

**[36:07]** criteria.

**[36:09]** And then we could even add more context

**[36:11]** here. Like we could have some more

**[36:12]** research on how the coding agent would

**[36:14]** recommend doing this. We could put that

**[36:15]** as a comment here. Sometimes my Claude

**[36:17]** code will actually do that by itself.

**[36:19]** It's cool to see.

**[36:21]** Um so, yeah, it's actually it is so it's

**[36:24]** adding technical notes as comments to

**[36:26]** each of the issues. So, not only are we

**[36:28]** creating issues, but we're providing

**[36:30]** more context as the coding agent has

**[36:32]** done some research for each of the

**[36:34]** implementations. Like looking into the

**[36:35]** code base, providing those initial

**[36:38]** suggestions for how we'd build each one

**[36:41]** of these things.

**[36:43]** And so, I'll let that run in the

**[36:44]** background here cuz that's not like

**[36:46]** super important for me to have finished

**[36:48]** before I go to the next thing for you

**[36:51]** guys.

**[36:52]** And the next thing is really like let's

**[36:54]** just pick one of these and let's work on

**[36:55]** it. Right? Like at this point at an

**[36:58]** organization level,

**[36:59]** the product manager would take this list

**[37:03]** list and send it over to the development

**[37:05]** team. You know, you might have some

**[37:06]** scrum meeting or whatever to talk about

**[37:08]** these things and and again refine things

**[37:11]** if you uh need to like fix up any of

**[37:14]** these issues. And then you go on to the

**[37:16]** development. Or if you are a solo

**[37:18]** developer, then these might be GitHub

**[37:20]** issues that you're now going to handle

**[37:22]** one at a time.

**[37:25]** And so, we just need to pick one of

**[37:26]** these to work on.

**[37:28]** And uh let's see.

**[37:31]** I'm trying to think like uh maybe the

**[37:32]** audience vote page would be a good one.

**[37:35]** As an audience, I want mobile first page

**[37:36]** that shows only active questions, lets

**[37:38]** me submit my answer, auto advances when

**[37:40]** the presenter moves on. That's a decent

**[37:42]** one. What else could I work on here? I

**[37:44]** mean, there's a lot of good features.

**[37:44]** I'm trying to like think of like the

**[37:45]** best one that would be good for a live

**[37:47]** demonstration.

**[37:49]** Uh presenter projection page. Actually,

**[37:51]** this this is a good one here cuz that's

**[37:52]** actually what I was planning for my

**[37:54]** prep. So, I want a full screen page that

**[37:56]** shows active questions, animated bar

**[37:58]** chart, real-time updates as things are

**[38:01]** coming in. That's definitely something

**[38:02]** that we're we're missing right now cuz

**[38:04]** this looks pretty bland for the results

**[38:06]** page.

**[38:07]** So, we'll tackle this issue first.

**[38:10]** And the really cool thing is the input

**[38:13]** into our development process just is

**[38:15]** this issue.

**[38:16]** And that's actually something I've been

**[38:18]** doing a lot more recently with AI coding

**[38:20]** assistance is

**[38:22]** my input to writing the code is always

**[38:25]** some artifact. Like for me personally,

**[38:28]** uh I do a lot kind of as more of like a

**[38:30]** solo developer or I'm working on open

**[38:32]** source projects. So, usually the GitHub

**[38:34]** issues is actually my entry point. So,

**[38:36]** I'll put my artifacts here. I just

**[38:38]** wanted to show Jira because that's how

**[38:40]** so many teams work. But, uh your Jira

**[38:42]** tickets, like that is the input.

**[38:44]** And so, going into the pivot loop here,

**[38:46]** we're going to go through a similar

**[38:49]** first step where we're just going to

**[38:51]** explore our solution. And the input into

**[38:54]** this is just one of the tickets that we

**[38:56]** pick. So, the developer takes that work.

**[38:58]** You can use the Jira MCP to assign

**[39:01]** yourself. And then, we start exploring

**[39:03]** the solution.

**[39:05]** And so, for planning with AI coding, you

**[39:09]** always have two layers. You have the

**[39:11]** project level planning, and that's

**[39:13]** everything that we did here.

**[39:15]** Right? Like this is like the PM level

**[39:17]** planning.

**[39:18]** And then, you have the task planning.

**[39:20]** And that is the individual ticket level.

**[39:23]** And the important thing that I I've

**[39:25]** already explained a little bit here, but

**[39:27]** I just want to be like really clear on

**[39:28]** this, is the layer one planning is

**[39:31]** higher level. Here are the features that

**[39:34]** we want to build or the bugs we want to

**[39:35]** fix. At this point, we are not digging

**[39:37]** into the code. Now that we're taking a

**[39:40]** single ticket for layer two, this is

**[39:43]** where we get more in the weeds of

**[39:44]** things. This is where we're going to

**[39:46]** analyze the code base, the

**[39:47]** documentation, figure out what parts of

**[39:49]** the code base we actually have to touch.

**[39:51]** We're starting to dive that deep.

**[39:54]** And it's really helpful for the coding

**[39:55]** agent to do this two-step process

**[39:58]** because then now that we're getting

**[40:00]** really into the weeds of things, we

**[40:01]** already have a lot of context for what

**[40:03]** we want to build overall. At this point,

**[40:06]** the ticket has translated the

**[40:07]** stakeholder or business requirements,

**[40:08]** whatever you want to call it, and we may

**[40:10]** be even have some higher-level

**[40:11]** recommendations for what part of the

**[40:13]** code we want to touch. And now, we're

**[40:15]** just really getting into that. So, just

**[40:18]** like creating our PRD, when we are

**[40:21]** creating the actual implementation, we

**[40:23]** start very unstructured. We're just

**[40:25]** going to have a conversation with our

**[40:27]** coding agent figuring out how should we

**[40:30]** go about solving this problem, fixing

**[40:32]** this bug, you know, implementing this

**[40:34]** new feature, whatever that is. And then

**[40:37]** we go from unstructured to structured.

**[40:39]** So, this is very similar, like creating

**[40:42]** a plan for implementation is very

**[40:44]** similar to creating a PRD. And we're

**[40:46]** going to have a command for planning out

**[40:48]** the feature and just like we have a

**[40:50]** command for creating our PRD.

**[40:53]** And so, I'll show you guys what this

**[40:55]** looks like right now. So, I'm going to

**[40:57]** go back into my code base here.

**[41:00]** And I'm going to begin a brand new

**[41:02]** conversation. So, let me escape out of

**[41:04]** this. I have a brand new conversation

**[41:05]** with Claude. Because you can imagine

**[41:07]** that like you as a developer, you are

**[41:09]** picking up a single ticket and you don't

**[41:11]** have any context around creating the PRD

**[41:14]** or stories or anything. So, we're going

**[41:15]** to pretend like this conversation

**[41:17]** doesn't exist because it's going to be a

**[41:20]** someone else doing this or maybe you

**[41:22]** doing it at a different time. So, brand

**[41:24]** new conversation. The first thing that I

**[41:26]** always do when I am preparing for an

**[41:29]** implementation is I run what is called a

**[41:32]** prime command. So, another example of if

**[41:35]** you're going to prompt a coding agent to

**[41:37]** do something over and over again, just

**[41:38]** turn it into a prompt, turn it into a

**[41:41]** command. Cuz that way we don't have to

**[41:43]** type it out again.

**[41:44]** And so, this prime command, quite

**[41:46]** simply, its job is to walk a coding

**[41:49]** agent through understanding the code

**[41:51]** base. We want to know what we already

**[41:54]** have to help us think about what comes

**[41:56]** next, right? So, we're going to load

**[41:57]** external context, which this is where we

**[42:00]** can specify Confluence pages or Jira

**[42:02]** tickets that we wanted to understand. In

**[42:04]** our case, we are actually going to

**[42:06]** specify a Jira issue, right? We're going

**[42:09]** to understand the code base from the

**[42:11]** lens of this Jira ticket, this new thing

**[42:14]** that we want to build. But also, aside

**[42:16]** from that, we're just going to generally

**[42:18]** understand the code base. So, we're

**[42:19]** going to study the features, we're going

**[42:21]** to study app routes, we're going to

**[42:23]** check recent Git commits. I love using

**[42:25]** Git as long-term memory for my coding

**[42:28]** agents. So, a lot of times, what you've

**[42:30]** done recently in a code base is going to

**[42:32]** help guide what you do next, cuz you're

**[42:34]** going to look at like the code patterns

**[42:35]** you followed for recent commits and

**[42:37]** things like that. This is a a very, very

**[42:39]** powerful part

**[42:41]** of any new conversation with a coding

**[42:42]** agent. And obviously, the steps that you

**[42:45]** want your coding agent to go through to

**[42:47]** analyze the code base is very custom to

**[42:49]** your code base. So, all of the commands

**[42:53]** that I have here are starting points for

**[42:55]** you, but you're always going to get the

**[42:57]** most out of them if you customize the

**[42:59]** commands to your process, your

**[43:01]** architecture, your code bases.

**[43:04]** And so, I'll start by running a {slash}

**[43:05]** prime here. And one of the arguments

**[43:08]** that we have is a comma-separated list

**[43:10]** of Jira issues. And so, for example, uh

**[43:14]** going back to our browser here in Jira,

**[43:18]** um I just want to use

**[43:20]** um this issue right here.

**[43:22]** So, the ID for it is AT23

**[43:26]** for our uh presenter projection page.

**[43:30]** So, I'll do {slash} prime and then just

**[43:32]** AT23. So, it's going to understand the

**[43:34]** entire code base, but also from the lens

**[43:36]** of this issue. So, first it'll use the

**[43:39]** Atlassian or Jira MCP to pull that

**[43:41]** context. I can do control O and we can

**[43:44]** see right here

**[43:45]** that uh first it's listing accessible

**[43:47]** resources, and then it's going to call

**[43:49]** the tool to get that specific issue.

**[43:52]** Performing a bunch of reads here, also

**[43:53]** looking at the Git logs in parallel.

**[43:55]** There's just a ton of context loading

**[43:57]** that it's doing at the exact same time

**[43:59]** here. Now, you want to be careful to not

**[44:01]** load too much context into your coding

**[44:03]** agent, cuz it's not like you want, you

**[44:04]** know, 50% of your coding agent's context

**[44:07]** window to be just loaded with a bunch of

**[44:09]** research it's doing.

**[44:10]** But we definitely want to load in the

**[44:12]** core files and the core history of what

**[44:16]** we've done recently. And so if you ever

**[44:18]** want to, you know, tweak that lever of

**[44:20]** how much context you're bringing into a

**[44:23]** session up front, it's just you change

**[44:25]** the prime command, right? Like you

**[44:26]** change this over time. Like maybe you

**[44:28]** only load in the first part of a Jira

**[44:30]** issue or you only read from this part of

**[44:32]** the code base. It's totally up to you

**[44:33]** for how you formulate your commands to

**[44:35]** optimize things for your process. So

**[44:38]** here we go. Project context loaded. We

**[44:40]** are going to be handling the presenter

**[44:42]** projection page, so pulled full context

**[44:44]** there. Gives me a quick summary of my

**[44:46]** code base.

**[44:49]** And um yeah, I think we're we're good to

**[44:51]** go. Um though it actually it actually

**[44:53]** says something interesting here. So this

**[44:55]** is really cool. This is a good uh live

**[44:57]** teaching moment. It is able to

**[44:59]** recognize, based on querying my state in

**[45:02]** Jira, that there are some blockers that

**[45:05]** we need to take care of before we could

**[45:08]** really go on to AT-23. So it understands

**[45:11]** the dependency mapping. That is actually

**[45:13]** one of the things that I have built into

**[45:15]** create stories here where it can help

**[45:17]** you understand dependencies. So maybe we

**[45:19]** would actually have to handle AT-22 with

**[45:21]** a QR code first. And um I think this is

**[45:24]** this is something that we'll take on. So

**[45:26]** maybe we'll do like, "Okay, look at

**[45:29]** AT-22.

**[45:30]** What do we need to implement for that?"

**[45:34]** Right? We're starting very unstructured

**[45:35]** in our planning here. We're actually

**[45:37]** shifting gears right away, which is

**[45:38]** totally okay, but we're just going to

**[45:39]** have it get a little bit of

**[45:41]** understanding of this feature that we

**[45:43]** want to build. And we'll start to ideate

**[45:45]** there.

**[45:46]** So we're going to explore how we want to

**[45:48]** build this, understand the code base,

**[45:50]** and then get into that uh structure plan

**[45:53]** that we'll go and send into

**[45:54]** implementation.

**[45:57]** And so at this point uh we have full

**[45:59]** context from the issue,

**[46:02]** but now we just do a little bit of

**[46:03]** exploration. And what this looks like

**[46:05]** totally is up to your own process. In

**[46:06]** fact, this is one of the things that I

**[46:08]** don't actually have as a command because

**[46:10]** it's very free form at this point. So, I

**[46:13]** can, you know, for example, go into my

**[46:14]** speech text tool and say,

**[46:16]** "All right, let's build AT-22. I want

**[46:19]** you to spin up a few sub-agents to

**[46:21]** research the code base and help me

**[46:23]** ideate around uh how I would build this

**[46:26]** new feature into our poll application."

**[46:29]** So, just like a really quick prompt

**[46:31]** here. And also showing you sub-agents

**[46:34]** because sub-agents is something that I

**[46:36]** use all of the time for research. If you

**[46:39]** aren't familiar, sub-agents is basically

**[46:42]** a way for you to spin up a uh

**[46:44]** sub-process, another agent that runs

**[46:47]** under the hood to go and look at a bunch

**[46:50]** of things or perform a bunch of work and

**[46:51]** then report back a summary to our main

**[46:54]** Claude code agent here. And it's really

**[46:56]** powerful for research because when we

**[46:59]** are exploring a code base or doing web

**[47:02]** research, we are loading in tens of

**[47:04]** thousands of tokens of information.

**[47:06]** Like, you can see that this one already

**[47:07]** loaded in 32,000 tokens. We are going to

**[47:10]** completely overwhelm our main agent if

**[47:14]** we had it do all of the research by

**[47:16]** itself.

**[47:17]** And with research, you really only need

**[47:18]** a quick summary at the end, right? Like,

**[47:20]** here are generally the files that we

**[47:22]** have to edit. Or if you're doing web

**[47:24]** research, like, here are the core

**[47:25]** articles that you should read that would

**[47:27]** help with um best practices for this

**[47:29]** tech stack. So, we've already used over

**[47:31]** 100,000 tokens here, but we only have a

**[47:34]** few thousand tokens that are returned

**[47:36]** back to our main agent. And so, yes,

**[47:39]** with Claude code, with we now have the 1

**[47:42]** million token limit with Opus, and there

**[47:44]** are a lot of other models through Codex

**[47:46]** and get out copilot and everything where

**[47:47]** you have 1 million tokens. But, here's

**[47:50]** the thing. Just because you can fit a

**[47:53]** million tokens into a large language

**[47:55]** model does not mean that you should,

**[47:57]** because they get overwhelmed just like

**[47:58]** people do. So, we want to deploy

**[48:01]** strategies for managing context well.

**[48:04]** Sub-agents is one of the best strategies

**[48:06]** for that.

**[48:07]** So, we just have to wait for these three

**[48:10]** exploration agents to finish, and then

**[48:12]** our main agent will get back a summary,

**[48:14]** so it can reason. We can see that these

**[48:15]** are all done now. So, it'll reason about

**[48:17]** what the sub-agents did, and then it'll

**[48:19]** provide me a final output here with its

**[48:22]** recommendation for how we can handle

**[48:24]** this Jira ticket.

**[48:27]** And so, at this point, going back to our

**[48:29]** diagram here, we're still at this

**[48:31]** initial exploration, right? Like, we're

**[48:33]** going to explore ideas, architecture,

**[48:35]** concepts, tech stack. I'm not going to

**[48:37]** go through each one of these things

**[48:38]** right now for the sake of speed.

**[48:41]** But, this is our chance to ask

**[48:42]** questions. Or, like we did when we

**[48:44]** created the PRD, have it ask us

**[48:47]** questions as well. Because it's

**[48:49]** important to remove assumptions going

**[48:50]** into writing the actual code. It might

**[48:52]** even be more Well, probably not more

**[48:53]** important than assumptions in the PRD,

**[48:56]** cuz the PRD is so high-stakes, but it it

**[48:58]** is very important as well. So, we go

**[49:00]** through this process where once we feel

**[49:02]** confident that we're on the same page

**[49:04]** with the coding agent, then we'll run a

**[49:07]** command that'll create a structured

**[49:08]** markdown document for our plan. We want

**[49:11]** again, we we want the output of our

**[49:14]** planning process to be a single

**[49:16]** artifact, and that artifact is going to

**[49:19]** contain all of the information that the

**[49:21]** coding agent needs to do the actual

**[49:24]** implementation.

**[49:26]** And so, I'll show what that looks like

**[49:28]** in a little bit, but first I want to

**[49:30]** actually invoke the command to create

**[49:32]** the plan, and then I'll explain more how

**[49:34]** it works, just so that we can have

**[49:35]** things move along well for us here.

**[49:38]** So, here's a synthesis with real

**[49:40]** decisions to make. Here's what we know,

**[49:42]** okay, and three decisions worth making

**[49:44]** before coding. So, it's asking me some

**[49:46]** questions here. I'm going to blitz past

**[49:49]** these for the sake of demonstration.

**[49:51]** But, it is worth taking the time with

**[49:52]** this usually. So, I'll do plan.

**[49:55]** This is my command where I can now

**[49:57]** describe the feature that I want to

**[50:00]** build. So, I'm just going to say here go

**[50:02]** with your

**[50:03]** recommendations and create the plan for

**[50:07]** AT-22.

**[50:09]** So, I'm just going to give it permission

**[50:10]** here to just pick whatever it wants.

**[50:12]** Usually though, it would be worth taking

**[50:14]** your time and answering these things and

**[50:16]** having it ask you more questions as

**[50:18]** well. So, while this planning command

**[50:21]** runs, not to be confused with the plan

**[50:23]** mode in Claude code, this is a separate

**[50:24]** command that I have created right here.

**[50:26]** It's very similar to the create PRD

**[50:28]** plan.

**[50:30]** Where we have phases laid out like

**[50:31]** here's the research you should do

**[50:33]** initially, explore the code base, make

**[50:35]** sure you have full understanding for how

**[50:37]** we're going to implement it, then create

**[50:39]** the plan file. So, just like we created

**[50:41]** a PRD.md,

**[50:43]** we're now creating a plan.md.

**[50:45]** And it has our structure. So, we want a

**[50:47]** summary, a user story. It's going to be

**[50:50]** similar to the PRD, but now we're

**[50:53]** getting into the weeds of how we're

**[50:54]** actually going to implement it. And so,

**[50:56]** for example, one thing that we

**[50:57]** definitely didn't have in our PRD

**[51:00]** command

**[51:01]** is the patterns to follow. Like here's

**[51:04]** here's how we're coding things. Here are

**[51:06]** the files that need to be changed.

**[51:08]** Here's the task order, everything we're

**[51:10]** going to execute down to the individual

**[51:12]** level of the files that we're going to

**[51:13]** create and update or maybe the commands

**[51:16]** that we're going to run for testing. So,

**[51:18]** also laying out out front. How do we

**[51:20]** want our coding agent to validate its

**[51:22]** own work?

**[51:24]** Because when we get into the

**[51:26]** implementation, we're going to send this

**[51:27]** plan into the coding agent. We are going

**[51:30]** to delegate all of the coding to the

**[51:33]** coding agent. And the only reason that

**[51:35]** I'm comfortable doing that is because I

**[51:37]** still find myself in the driver's seat

**[51:39]** because I'm a part of the planning

**[51:40]** process. I'm iterating on the plan. I'm

**[51:43]** doing the exploration and having it ask

**[51:45]** the right questions. And so, we'll have

**[51:47]** it write the code, and then we'll also

**[51:49]** have it do some of the validation,

**[51:51]** right? Like, we can have the coding

**[51:53]** agent, right after it does the

**[51:54]** implementation, we can have it write the

**[51:56]** unit tests, write the integration tests,

**[51:58]** do the linting and the type checking,

**[52:00]** and take care of all of these things.

**[52:02]** Not that it's going to be perfect, but

**[52:04]** the point is we want it to take care of

**[52:05]** as much validation as possible, so that

**[52:08]** by the time control passes back to us

**[52:10]** for our human validation, there's less

**[52:13]** that needs to be corrected. Right? We

**[52:15]** want to reduce us being the bottleneck

**[52:17]** for actually shipping the code that

**[52:19]** we're creating with the help of our

**[52:21]** coding agents.

**[52:22]** And so, I'll jump back over to the code

**[52:24]** base here, and we can see that our plan

**[52:26]** file is created. I'll take a look at

**[52:28]** this really quick. Uh just another one

**[52:30]** of those things that I don't want to

**[52:31]** spend the time iterating on too much

**[52:33]** right now, but we have the summary of

**[52:35]** our work.

**[52:36]** Uh we have the decisions that we've

**[52:38]** locked in. These are the things that we

**[52:39]** would have been working with the coding

**[52:40]** agent to establish. And then, um we even

**[52:44]** have like the individual files that need

**[52:46]** to be created

**[52:47]** and updated, and then we have the task

**[52:49]** list.

**[52:51]** So, usually the task list, you don't

**[52:53]** create Azure tickets, right? Cuz this is

**[52:55]** like so granular that this is for a

**[52:57]** single coding agent implementation. So,

**[52:59]** you let the coding agent handle an

**[53:01]** internal task list as it is writing the

**[53:04]** code. And then, we have the

**[53:06]** self-validation.

**[53:07]** So, it's going to be running the type

**[53:08]** checking and linting and unit testing.

**[53:10]** We can also have it do end-to-end

**[53:11]** testing if we wanted to use browser

**[53:13]** automation tools with um

**[53:15]** you know, the agent browser CLI, for

**[53:17]** example. So, that's actually one of the

**[53:18]** skills that I have for you guys here. It

**[53:20]** can spin up the browser and navigate

**[53:22]** through it and like create polls and and

**[53:24]** vote on the polls just like a user

**[53:26]** would.

**[53:27]** And so, for the sake of speed, I won't

**[53:29]** do that, but you can have coding agents

**[53:30]** do very, very end-to-end testing. You

**[53:32]** want it to validate as much as possible.

**[53:36]** So, the important thing here is once you

**[53:37]** have iterated on the plan and you're

**[53:39]** confident in everything,

**[53:41]** you actually don't do the implementation

**[53:44]** right here.

**[53:45]** We want to start a brand new session

**[53:47]** with Claude code. So, I'm going to open

**[53:49]** up a a fresh blank slate with Claude.

**[53:53]** The reason that I want to do this

**[53:56]** is because when you are working with AI

**[53:58]** coding assistants, you want to make sure

**[54:00]** that they are as focused as possible.

**[54:03]** And it's important to be focused in

**[54:05]** order to be focused to do your planning

**[54:07]** and implementing in separate sessions.

**[54:09]** Because also, the coding agent has

**[54:11]** probably built up a lot of bias

**[54:13]** throughout this conversation as you've

**[54:14]** been working with it. We want it to have

**[54:16]** a fresh set of eyes on the problem going

**[54:18]** into implementation.

**[54:20]** And so, of course, I have an execute

**[54:22]** command. And so, all I have to do is

**[54:25]** {slash} implement and then I give it the

**[54:26]** path to the plan that I created in the

**[54:29]** prior session. And the whole point of

**[54:30]** this markdown artifact is that it has

**[54:34]** all of the context that the coding agent

**[54:36]** needs to implement cuz it has the

**[54:37]** summary, it has the recommended files to

**[54:39]** change, and the task list, and the

**[54:40]** validation strategy. There's no reason

**[54:42]** for us to stay within this other context

**[54:44]** window in the first place. So, I can

**[54:46]** send off this command. It's going to

**[54:48]** read the plan, and then it's going to

**[54:49]** walk through the process I have in the

**[54:51]** implement command to do the

**[54:53]** implementation and the validation. And

**[54:56]** this um command that I have for

**[54:58]** implementation is actually very very

**[55:01]** concise.

**[55:02]** It's uh only like uh a couple of hundred

**[55:04]** lines long here because really it's the

**[55:06]** the plan that guides the entire

**[55:08]** development.

**[55:10]** The main thing that I'm walking it

**[55:12]** through here is just the process of, you

**[55:14]** know, loading the plan, preparing the

**[55:16]** implementation, like maybe making a new

**[55:18]** Git branch for example, like any kind of

**[55:20]** of uh process that you have in your

**[55:22]** usual software develop life cycle for

**[55:23]** how you want an engineer to work, we're

**[55:25]** just encoding that into the command

**[55:27]** here.

**[55:28]** We want to make sure that we're uh

**[55:30]** verifying any kinds of assumptions. So,

**[55:31]** we're also sort of doing like a second

**[55:33]** pass on the plan before we go into to

**[55:35]** implementation.

**[55:36]** So, yeah, then describing how we want to

**[55:38]** do validation, for example, when we want

**[55:40]** to pass control back to the user,

**[55:42]** outlining all of that for the agent.

**[55:45]** And so, going back to our diagram here,

**[55:47]** we're in this step right now. Right? We

**[55:49]** we've cut a fresh session, sent the plan

**[55:51]** into implementation,

**[55:53]** and then we'll wait for it to write the

**[55:55]** code, do all of its own validation, and

**[55:57]** then we'll also step in and we'll do a

**[55:59]** code review. Right? And it's not like

**[56:02]** you have to do this.

**[56:03]** Uh some people are are a big fan of just

**[56:07]** shipping the code right to production

**[56:08]** and having the coding agent do its own

**[56:10]** work. I'm I'm not a fan of that myself.

**[56:12]** I still the engineer in me still wants

**[56:14]** to review all the code. So, for any like

**[56:16]** serious production coding that I'm

**[56:17]** doing, I still am reviewing all of the

**[56:19]** code myself and then also doing manual

**[56:22]** testing. And so, we can see that after

**[56:24]** we do the implementation, like I'll

**[56:25]** refresh the page here and we'll we'll

**[56:27]** check out this new feature. Like we'll

**[56:28]** see the QR code that's generated and

**[56:30]** we'll make sure that's all working

**[56:32]** before we would actually be confident

**[56:34]** to, you know, merge that pull request

**[56:35]** into our main branch, for example, or

**[56:37]** whatever that looks like for your

**[56:39]** software development life cycle going

**[56:40]** into production.

**[56:42]** So, that review is important.

**[56:44]** And um you know, while we wait for the

**[56:47]** coding agent to run through everything

**[56:49]** here, you can see that it created its

**[56:51]** internal task list based on the plan.

**[56:53]** It's writing the code, doing all the

**[56:54]** testing. It's actually going to get

**[56:55]** through this feature pretty quick cuz I

**[56:57]** purposely built a simple one. Uh but as

**[56:59]** it is doing this, I want to quickly talk

**[57:02]** about the last part of the system here.

**[57:05]** Um and then of course, after this, we'll

**[57:07]** we'll quickly get into time for Q&A with

**[57:10]** uh

**[57:10]** with Lior, too.

**[57:12]** So, the last thing I want to talk about

**[57:14]** is system evolution.

**[57:16]** So, when whenever we do a pivot

**[57:19]** it is very very far from guaranteed

**[57:23]** that the implementation will be perfect.

**[57:26]** Coding agents are not perfect. They are

**[57:28]** non-deterministic by nature. Even if we

**[57:31]** work super super hard to align with it

**[57:34]** in the planning phases, there are still

**[57:36]** going to be mistakes.

**[57:39]** But the powerful part of this system is

**[57:41]** we don't have to just treat the bug as a

**[57:44]** one-off fix that we address and then

**[57:46]** move on to the next pivot loop or move

**[57:48]** on to that next ticket. We can spend

**[57:50]** some time to fix to also fix the system

**[57:54]** that allowed the bug.

**[57:55]** And what I mean by that is we can have a

**[57:58]** sort of, you know, retroactive session

**[58:00]** with the coding agent where we say,

**[58:01]** "Okay, Claude, you allowed this problem

**[58:04]** to creep into my code base. I want you

**[58:07]** to dive into your AI layer.

**[58:10]** Like take a look at the at your rules.

**[58:12]** Take a look at your commands and skills,

**[58:14]** the process, the workflow that I brought

**[58:16]** you through, and I want you to identify

**[58:18]** things that we could improve there so

**[58:21]** that this kind of issue doesn't happen

**[58:22]** again.

**[58:24]** Like for example, maybe it broke

**[58:26]** something in the polling here where

**[58:29]** um

**[58:30]** I don't know. Let's say that like all of

**[58:31]** a sudden the website looks really ugly

**[58:34]** when it when it built this new feature

**[58:35]** cuz it didn't like create the same like

**[58:38]** it didn't create the component in the

**[58:39]** same style as the rest of our code base.

**[58:41]** Well, maybe that means that there's

**[58:42]** something in our global rules that we

**[58:43]** have to update for like our style

**[58:45]** conventions.

**[58:47]** Or maybe we need to build something into

**[58:48]** our our validate workflow where whenever

**[58:51]** we validate a code base, we make sure

**[58:53]** that like any new front-end component

**[58:55]** that we build is in compliance with the

**[58:57]** styles of our other components that are

**[58:59]** already in the code base. Just kind of a

**[59:02]** random example I'm giving you there, but

**[59:03]** the point is generally when your coding

**[59:05]** agent does something wrong, there's

**[59:07]** going to be something in the context you

**[59:09]** give it that you can improve to not

**[59:12]** necessarily for sure fix the problem,

**[59:14]** but you're using it as an opportunity to

**[59:16]** continue to evolve your AI layer, making

**[59:19]** your rules more specific over time,

**[59:21]** making your workflows more reliable. And

**[59:23]** the best part of this is when you use

**[59:25]** every single Jira ticket as a

**[59:28]** potentially an opportunity to improve

**[59:29]** your system, you get to improve the

**[59:32]** whole process for everybody. Because you

**[59:34]** can check in your rules and commands and

**[59:37]** skills into source control just like

**[59:38]** your code base, the entire team can

**[59:40]** reuse these things and you can even

**[59:42]** create pull requests to update commands

**[59:45]** just like you create pull requests to

**[59:47]** update your code base. So, you can do

**[59:49]** code reviews making sure that everyone's

**[59:51]** in line with the changes you're making.

**[59:53]** I know that sounds like a decent amount

**[59:55]** of work, but it's so high leverage.

**[59:57]** Because every single time you improve a

**[59:59]** command or a skill, it might save

**[1:00:01]** engineers dozens and dozens of hours

**[1:00:03]** going forward because you've now made

**[1:00:04]** the validation process more reliable or

**[1:00:07]** you've made the style conventions

**[1:00:09]** respected more often, whatever that

**[1:00:11]** might end up looking like.

**[1:00:12]** And so, really like the four things that

**[1:00:15]** I generally improve over time in a code

**[1:00:18]** base is my commands, my on-demand

**[1:00:20]** context. This could also even mean like

**[1:00:22]** things in Confluence. You just, you

**[1:00:24]** know, optimize your documents in

**[1:00:25]** Confluence for AI understanding.

**[1:00:28]** Your global rules and then also of

**[1:00:29]** course like your plan and PRD templates.

**[1:00:32]** You might want to define and fix gaps in

**[1:00:34]** those over time.

**[1:00:35]** And so, for every single code base, I'm

**[1:00:38]** constantly doing this.

**[1:00:40]** Right? Like if I have a pivot loop where

**[1:00:41]** there is some kind of major issue, I

**[1:00:43]** step outside of the pivot loop to do

**[1:00:46]** this system evolution.

**[1:00:49]** I will update things that I created up

**[1:00:51]** front and then I'll go into the next

**[1:00:53]** pivot loop.

**[1:00:54]** And uh if if actually there are no

**[1:00:56]** issues at all and the coding agent

**[1:00:58]** completely rocked that Jira ticket, then

**[1:01:01]** literally you just go loop right back,

**[1:01:02]** right? You go through the planning

**[1:01:03]** process, you load that next Jira ticket,

**[1:01:05]** and you go through the process. So, it

**[1:01:07]** becomes very, very cyclical. There's

**[1:01:09]** basically two loops here. You have the

**[1:01:10]** inner loop when everything's working

**[1:01:12]** well and you're just chugging through

**[1:01:13]** the work with the help of your coding

**[1:01:14]** agent. And then you have the outer loop

**[1:01:17]** when you're taking some time to reflect

**[1:01:19]** and make your your better.

**[1:01:21]** So, it's not like you always have to do

**[1:01:22]** the outer loop, but I encourage you to

**[1:01:25]** do it pretty often. Because not only are

**[1:01:28]** you improving your your commands in

**[1:01:30]** other parts of your system here, but you

**[1:01:32]** are also customizing your process to

**[1:01:35]** your specific code base over time. It's

**[1:01:37]** like what I said, all of the commands

**[1:01:39]** and skills that I have for you guys

**[1:01:40]** here, they're a starting point, but

**[1:01:42]** they're more general, right? Like if you

**[1:01:43]** want to really optimize something for

**[1:01:45]** your process, you're going to start with

**[1:01:47]** these, find opportunities to make them

**[1:01:49]** more specific to your validation

**[1:01:51]** strategy or your planning strategy,

**[1:01:53]** whatever that might be.

**[1:01:55]** So, I hope that makes sense. I mean,

**[1:01:56]** that really is the whole process at a

**[1:01:58]** high level here. And uh so, I'm going to

**[1:02:00]** head back to Claude here and see where

**[1:02:02]** we are at. Okay, so the implementation

**[1:02:04]** is complete. We did it in a branch cuz

**[1:02:07]** our implementation command told it to.

**[1:02:09]** We ran all of our validation here. Here

**[1:02:11]** are the files that are changed. It's

**[1:02:13]** giving us a summary of everything that

**[1:02:14]** was done. It says that the

**[1:02:16]** implementation matched the plan. So, I

**[1:02:17]** also have a part of the process here.

**[1:02:19]** This is actually something I did

**[1:02:20]** recently for my system evolution where

**[1:02:22]** after it does the implementation, it

**[1:02:24]** looks at the code and compares it to the

**[1:02:26]** plan to make sure that we didn't

**[1:02:27]** deviate. And then it also used the uh

**[1:02:31]** MCP server from Atlassian to update the

**[1:02:34]** ticket. So, there's a lot of the admin

**[1:02:35]** work that we did as well, you know,

**[1:02:37]** creating the branch, creating the pull

**[1:02:38]** request, updating the Jira ticket. We

**[1:02:41]** don't have to have the developer spend

**[1:02:42]** their time doing that stuff

**[1:02:43]** retroactively. So, now if I go back and

**[1:02:46]** I refresh my page here in Jira,

**[1:02:48]** we can see that uh everything is to do

**[1:02:50]** except for this one piece of work that

**[1:02:52]** we picked up here. And I believe I think

**[1:02:54]** I think it also said there was even a

**[1:02:56]** comment. Yep, here we go. So, it also

**[1:02:58]** posted a comment with full details. And

**[1:03:00]** maybe this is more, you know, context

**[1:03:03]** than we'd really want as a comment on a

**[1:03:04]** Jira ticket, but if you have a problem

**[1:03:07]** with this, then that would, you know,

**[1:03:08]** also be an opportunity for system

**[1:03:10]** evolution where you just specify in the

**[1:03:11]** implement command, once you're done with

**[1:03:13]** the implementation, here Here a more

**[1:03:15]** concise version of context that I'd want

**[1:03:17]** you to comment on the Jira ticket. So

**[1:03:19]** now we can have this going into a code

**[1:03:20]** review, send it off to, you know, your

**[1:03:23]** VP to go and review, or you know,

**[1:03:24]** whatever that is.

**[1:03:25]** So pretty cool. And then we can also

**[1:03:27]** test this in the application here.

**[1:03:29]** So I'm going to refresh here. I'll

**[1:03:31]** create a new poll. Um let's say what's

**[1:03:34]** for lunch. And we'll just say

**[1:03:36]** um spicy mango

**[1:03:39]** chicken

**[1:03:40]** or spicy mango beef. All right, cool. So

**[1:03:43]** I'll create this poll.

**[1:03:44]** And uh I don't actually see the QR code.

**[1:03:46]** I might need to restart the application.

**[1:03:48]** I think that might be why. So let me go

**[1:03:49]** back here and say uh all right, I want

**[1:03:52]** you to restart the application and then

**[1:03:54]** use the agent browser skill so you can

**[1:03:57]** visit it and make sure we have the QR

**[1:03:58]** code. And then let let me know like how

**[1:04:00]** I can see the QR code myself.

**[1:04:03]** All right, so I yeah, I think I just

**[1:04:04]** have a stale version of the application.

**[1:04:07]** Um yeah, so

**[1:04:09]** I also I mean if I want to like look at

**[1:04:11]** more context, I can literally just go to

**[1:04:12]** the ticket here.

**[1:04:15]** So we have a server helper. I mean, this

**[1:04:16]** is like a bit more technical. Like

**[1:04:18]** honestly, I I would probably rather have

**[1:04:19]** a higher level overview of what was

**[1:04:21]** actually built. Uh again, something you

**[1:04:22]** could just change in the command.

**[1:04:25]** Um but yeah, so let me go ahead and jump

**[1:04:29]** back over, see what Claude said.

**[1:04:32]** Um

**[1:04:34]** code utility. There's no consumer of it

**[1:04:36]** yet. Oh, I got it. Okay, so it built out

**[1:04:39]** the code, but we need to actually make

**[1:04:42]** it so that the front end consumes it. Um

**[1:04:45]** I want you to quickly uh implement the

**[1:04:47]** consumer. Just really fast. No

**[1:04:49]** validation, no Jira ticket. Just go and

**[1:04:50]** add this right now so that I can see it

**[1:04:52]** live.

**[1:04:53]** Okay, so that that's my bad. I didn't

**[1:04:55]** catch the fact that this was just

**[1:04:56]** getting the pipe the piping in place.

**[1:04:59]** And then it is that follow-up issue that

**[1:05:01]** we're originally looking at that does

**[1:05:02]** the presentation. So that's on me. So

**[1:05:05]** every everything is working as intended,

**[1:05:07]** but we just have to

**[1:05:09]** Okay, so So, created a QR demo page.

**[1:05:12]** So we can we can quickly look at that.

**[1:05:14]** So, we'll see that in a second once it

**[1:05:16]** um

**[1:05:17]** once it uh does its own validation. So,

**[1:05:19]** I I'm also showing a live demonstration

**[1:05:21]** of the agent browser

**[1:05:23]** where we can see it open up the website.

**[1:05:25]** And uh it'll even like take a screenshot

**[1:05:28]** to and vi- validate things visually,

**[1:05:29]** too. And then of course, in parallel, we

**[1:05:31]** can do the exact same thing. So, I'll go

**[1:05:33]** back to the application and then I'll

**[1:05:35]** just do QR demo.

**[1:05:37]** Pretty cool. So, yeah, I know that uh

**[1:05:39]** this is just a placeholder here, but I

**[1:05:41]** told it to build something quick to

**[1:05:42]** validate to the piping that we put in

**[1:05:44]** place. And so then when we go on to the

**[1:05:46]** next issue, the one that was depending

**[1:05:48]** on this, then that's when we build in

**[1:05:49]** the full presentation view and actually

**[1:05:51]** use the the QR code for real. And again,

**[1:05:53]** the point of this isn't to show the full

**[1:05:55]** application, but just the process that

**[1:05:57]** uh builds these kinds of things.

**[1:06:00]** So,

**[1:06:01]** all right. Uh that that is that is

**[1:06:03]** really the process as a whole. We've

**[1:06:05]** covered it We've covered it all from

**[1:06:06]** planning all the way to system evolution

**[1:06:09]** and creating those pull requests,

**[1:06:10]** getting that code into production.

**[1:06:13]** And uh I do want to reiterate that like

**[1:06:15]** this process takes a good amount of

**[1:06:16]** time.

**[1:06:18]** It's It's not like you're going to blitz

**[1:06:19]** through something as fast as me. It It

**[1:06:22]** can be if you want, but uh the important

**[1:06:24]** thing is even if you do take a lot of

**[1:06:26]** time iterating on the plans and

**[1:06:27]** validating the code, it's still going to

**[1:06:28]** save you so many hours of work creating

**[1:06:32]** those documents, updating things in

**[1:06:33]** Jira, writing the code. You The The days

**[1:06:35]** are gone now of going to Stack Overflow

**[1:06:38]** in order to uh get your questions

**[1:06:40]** answered. You don't have to

**[1:06:42]** copy and paste and be a Stack Overflow

**[1:06:44]** warrior anymore.

**[1:06:46]** So, yeah, there you go. That is the full

**[1:06:48]** process for AI coding. It's foundational

**[1:06:51]** and simple enough where you can take

**[1:06:52]** this and mold it to whatever your

**[1:06:55]** software development process is,

**[1:06:56]** standardizing things across your team

**[1:06:58]** with the AI layer as well.
