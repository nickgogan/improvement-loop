# Transcript: Claude Fable 5 Just Built the Ultimate Agent Harness

**URL:** https://www.youtube.com/watch?v=HhWwllcbc2g
**Segments:** 594
**Channel:** Pat Simmons
**Duration:** 19:21
**Uploaded:** 2026-07-07

---

## Full Text

AI agents are everywhere. But there are two problems. First, pick one and you're stuck with it inside their model or inside their platform. Second, it is complete chaos. You might have a pile of chat windows inside different apps like Telegram and Slack, different repos inside Cloud Code and Codeex, and absolutely no system to any of it. If you're using an agent platform, the context switching alone is killing your productivity. But what if I told you there's one app that will run all of them? Any agent, any model, all in a single place? That is exactly what we're going to build today. And no, this isn't Hermes or Open Claw. It runs on the subscriptions you already pay for. We're not going to get into any toos gray areas and all of your agents, all of your chat windows can be accessed inside this platform we're about to build. So, in this video, I'll show you how to build out this agent harness completely from scratch with Fable 5. We'll get it running in a single command. And by the end, you'll have the whole system ready to start building out your own team of agents, even if you've never built an agent before. So, not wasting any more time, let's dive right in to the build. But first, let me explain what I'm envisioning for this harness. So here is the mockup I sketched out. Please ignore the chicken scratch. But the basic idea is we have a category on the left for each one of these agents. A good category could be say YouTube. And under the category we have different agents assigned to different parts of YouTube. The first agent could be a script writer agent. This second agent could be a motion graphic creator agent. Another agent might monitor analytics. And the big idea here is if I select an agent, once I select that agent under the category, then I can open tabs here almost like Chrome browser tabs. And each one of these will be a terminal session that will allow me to connect to different models, whether it's Opus, GPT, or any open- source model. And each one of these terminal tabs could be three different scripts I'm working on at one time. I, for one, I'm incredibly scatterrained. You might be, too. And I want a system that can keep all of the different things I'm working on nice and organized because typically I'm working on multiple scripts at a time. And the same will probably be true for editing or motion graphics for analytics as well. So that's the basic premise and this is not a whole lot different than how they've architected codecs. If we look at codecs, we could in theory in these projects organize it in a way where each project has a folder assigned to each agent. However, we still run into issues when I want to create new tabs at the top. The tabs are on the lefth hand side here instead and I could be chatting with different agents at one time. But if I have say, I don't know, 15 agents, it starts to get really cumbersome when I have all the different projects I have to scroll through. If that's confusing at all, let me show you a few examples that get closer to what I'm thinking. They are called ADES or agentic development environments. There are a bunch of them. Semox is a good example. The way they have architected this is they have these repos or agent tabs on the left and then they have tabs within each agent. However, these tabs are kind of all over the place. It it starts to get really confusing, but this is more like the general premise. There is another healthc conductor.build that to me is a little less confusing. Agents on the left, tabs at the top. But each of these still feel more like aic coding environments. And a lot of these agents that I want to build out aren't necessarily focused on coding. So, we're going to take pieces from each of these. And the beauty is they are open source. So, I can go to their GitHub repos and start to duct tape my own customized version together into something that I'm actually happy with. So, that being said, let's now go back to Fable and start brainstorming this. So, we will open up a new session in terminal here with Fable 5 model Fable. I'm going to paste in this prompt. I will put it on screen. Essentially what I am saying is I'm building an ADE. I run agents for everything. Writing, content, coding. I want one app where all of them will live. I give some examples like the ones we discussed. I say start from superset actually because I take that back as I looked further into this. Conductor.build is not open source. So what we're going to do is we're going to use superset instead which is very similar looking. Here is superset. Same kind of idea. They have an open source repo I can pull from. And then I'm going to take some screenshots from the actual conductor interface, paste that into Fable as well. And then the rest of the prompt is basically just describing what I already went through. So the rails, the terminal tabs, each workspace is its own repo. And I talked about onboarding as well, which we'll get into once we actually get the the UI set up. But the basic idea of onboarding is I want it to be as simple as possible for the user. So the minute they open the application, they are asked to create agents, agent categories, and then agents under those categories. So that's the idea. And what we're doing as well is we're using a fable orchestration skill that I put together based on this anthropic documentation here titled prompting fable 5. They get into a lot of the details around this. So I fed this into a separate agent and we built out a skill based on this and that skill can be found here. I will include this in the description below but it is more or less what anthropic details and their docs here just organize into a nice easy use skill for an agent. And in about 20 minutes, we have our first mockup alive. Interestingly, it used colada artifacts here. I'm not exactly sure why. Maybe that's a fable thing, but I mean, it should work just as well as a local host. So, if we go to this link here, and here it is. It's looking pretty good. I fed it a screenshot of conductor. And you can see how similar it is to conductor. We have categories on the left. Under those, the actual agents, these emojis, of course, are obnoxious. I don't think we need changes. It basically just matched exactly what I gave it the screenshot. So, it added changes, checks, run terminal setup. We don't need all of that. A lot of this is superfluous. It also added a light mode, so that needs to be fixed. These emojis, of course, are driving me absolutely nuts, but I like the little tab here. I like the loading indicators. It's organized by agents. We can add a new category. We can name it, but create category. And that actually works. Nice. And then you can add an agent test. Cool. And you can go different models, which we will get into setting up. So, this is not a bad first pass. I'm going to give it feedback. One big thing that I see is it's not actually showing terminal, which it needs to actually connect to a terminal window, as in it needs to run directly through the CLI. And it looks like it's just like its own interface right now, especially when I go light mode. You can see it's like got its own little interface. So, I'm going to give Fable all of that feedback and then we'll come back for version two. And just in case you're curious, here is the follow-up feedback that I gave. I will put this on screen now, but it's basically describing exactly what I said. Getting rid of emojis and ability to add a profile photo, connecting the CLIs, stripping back some of these extraneous designs and functions here. And while that builds, Claude and I just thought of the name of this application, which is going to be Damon, D- A M O N, which comes from a play off of Demon, Dae M O N, which if you're not familiar, is a computer program that runs in the background as an independent process. And actually back in the day they came up with this term based on the Greek for d aim o n which in Greek was a supernatural entity often seen as a guardian or spirit. So it's kind of like a like a little helper which is fitting for this agent application. Anyway, back to the build and v3 is now live. So let's check out this latest version. It is looking pretty good. Looks like most of my feedback is in agent files on the right. We've got these tabs at the top. We've got our categories and then under that is agents. We have these nice little loading indicators. New category. Upload photo. Oh, does this actually work. Just use this random photo for my Fable 5 video game. Uh test. Oh yeah, look at that. Works. Okay, cool. So, we are all set up, ready to go. I'm going to go back to this agent and tell it now to build this out into a proper Mac application. Okay. And in about I'd say an hour and a half of building, we have something ready to go. A Mac application of this agents platform for us to react to. Fable is not fast, but it is incredibly thorough. It had spawned a ton of different agents and just went through this entire build process. So let's see what this app is looking like. It's telling me to run this install command. I'm just going to say, can you run this yourself? Okay, so it looks like we have our Mac app up and running. We've migrated over from that mockup. So, let's check how the Mac app is looking. How do I see this? And here it is. So, it's looking pretty good. It's pretty bare bones, but we should be able to add teams here. What I was calling category before. Upload a photo. We're going to do YouTube first. I have this image YouTube. We're going to call this YouTube. Create a category. And then we have an ability to under this exactly like I described. Looks like this is working. Adding a new agent. We'll call this uh it's a good script writer name. Then I can just add a photo here. Just going to do a random photo of something. Here we go. This uh video game screenshot for my Unreal Engine MCP video. Good enough. And then right now it's only working for Claude. So the runtime is going to be Clawed as in we're using our Claude subscription. And this actually didn't even ask for this. Maybe this came from Conductor or Superset. But this is really nice because you can if you'd like bring in an existing GitHub repository. Say you have an agent living in a GitHub repository. Maybe you already have agents and they're not in GitHub yet. You could theoretically put those in the cloud on GitHub, then upload them directly from here with this URL and just clone them and automatically upload them into our Damon app here. So I'm just going to do new empty repo and then I believe it's going to create a folder locally. Oh wow. Okay, it already opens up claude. So okay, yeah, here is the folder that it's opening up locally. ad default agents and then it's just this string and then /worktree and I can go yes I trust this folder and boom so we have earnest our script writing agent all set up you can also go new tab create a new session here another session with nest we should be able to if I go command I yep change the name of this so say this is a video about AI tools and then and this other one could be about say codecs so we have two different scripts being written we've got Earnest our script writing agent all in there we keep track of this we can another agent in a new empty repo. And then we have all of our agents here assigned to different tasks related to YouTube. And the way it does that is if I just go command T. It's just doing the claw dangerously skip permissions command. This is just a terminal here and I'm already logged into my cloud subscription. So it automatically just opens this up. So if you were to open this up yourself, you just need to a one time and it'll allow you to do the same. At the end of the video, I'll get into onboarding and actually setting this up from scratch to make sure that people have access to this and can start this up themselves. But for now, this is looking good. And this is the beauty of Fable, by the way. You give it feedback and it just does it. There have been no revisions off camera. All it took was what, three iterations to get here. It is very fun working with such a capable model like this. Now, the problem with this is we're only able to access Claude code like I just showed. And the whole point was running any model I want as well as my Claude subscription. So, how do I get any model I want accessible within our Damon agent application? Well, honestly, I don't even know. So, we're going to go back to Fable and we're going to tell Fable. All right, this is looking good. Everything is approved. Now, what I want to do is have an ability to add my chatbt subscription as well and log into I guess it would be technically codecs and use GPT55 within this as well as any open- source model. And so, I don't know exactly how we can set it up with these different open- source models. I'm assuming the easiest way to do this is through an open router API key, but I want an ability to when I open up the application, press that new tab button. Below the tabs, there should be an ability to select GBT, Collad of course, then OpenAI logo, then some popular open source models like Kimmy K27, Miniax M3, and GLM52 with their logos as well. So I can just click those and it will automatically open a session with that open source model. And so I think to get those open source models, the easiest way to do this is to just use an open router API key and we can just select all of these. I'll let you be the judge of all of this. Let's go ahead and spawn agents and do this next. All right, our new build is live. So, we have an ability now to choose from different models. Claude, OpenAI, Kimmy, Miniax, GLM, and we should have little indicators, little icons to actually choose from these. So, let's check this out. Okay, looking pretty good. We've got the actual icons here to choose from. Miniax. Can't actually see that logo. Change that. GLM 5.2. Not sure if that's the right logo. Need to change that. But what we can do, let's see if this actually works. Give me K. Okay. So nice. We have this. Enter your Open Router API key. So I'm going to do that now. This should work the exact same way once you download this application, which again we're going to get into how to actually do that. But if I just go here, if I go to Open Router right now, sign up for Open Router if you haven't already, but I'm going to assume that you're signed up. Go to workspaces, API keys. I just blurred that out, but I went create new API key. Hit create. Make sure you've got some credits added. And then I can go back to our application. Kimmy K. paste in my open router API key. Save and launch. And then it automatically will do this to where it will connect. So we're using the anthropic base URL. So this is loaded in the cloud code harness. This is the easiest way to do it. And I don't want to get too in the weeds here, but what it's doing is it's just pointing to the open router API endpoint. We have our open router API key that I just added. And then it's calling this model moonshot give me K27 via Open Router. And then I can say, hey, and it looks like I'm running into an issue here. 41 missing authentication header. Not sure what's going on there. I just went back to Fable, asked Fable to figure this out, and I'll fix this quickly. Also, while Fable's at it, can you change the Miniax logo to be white mode? Find the logo. All right, some quick revisions to the model pickers. We have updated logos here. And we should now have an ability apparently to open up any model here. KimK27. Hey, what model are you? Cool. I'm running with the Kimk 27 coder model backend. So now we have an ability to use any model with any agent whether it's claude codeex or an open- source one straight through open router except now we've introduced another problem which is if I close a tab the agent's not going to remember anything. We haven't set up the proper markdown files yet instructing the agent on who it is and what it does and have some sort of memory system and self-improving system that makes this truly agentic. So that's what we're going to set up next and it's going to be stored in this file section here. This is why I created this drawer here to have a quick ability to click through and see exactly how we've configured this agent. So that's what we got next. We're going to go back to Fable and explain. Perfect. All approved. Now what I need is for us to build out agents files. So agents.mmd a memory.mmd and anything else that Hermes does. I need you to go through the Hermes GitHub repo here, determine how they have their agents self-improving, and then I want you to just fork Hermes and bring it right over. And that will be our agent structure. So, it's easier for me to just use something that already exists. I know Hermes has probably the best agent memory that they've configured. And the beauty of this is it's fully open source. So, I can give this to my agent, have it parse through, find how they've structured the memory, and kind of self-improving system with their harness, and use this for our own agents. All right. So, Fable grabbed the Hermes GitHub repo, brought over exactly how they structure this agent.mmd, userd, memory.mmd, and this should now be set up in our application. So if we go back to our AD, we should now have this set up. Yeah. So we have these files here, claw.md, and then we also have these agent files here. And so each one of these are a markdown file, which essentially makes up the agent. By the way, if any of this is confusing at all on the files that actually make up an agent or you just want to learn more on how to build your own agents from scratch, you can check out this video. I'll link it above. It's a full course on building out AI agents. I'll also link another video above which is zero to your first AI agent in like 10 minutes. It'll give you a complete walkthrough on all of this. But these are essentially the files that make up our agent. And we pulled this directly from Hermes. So we have our agent.mmd which just tells the agent who they are and what their role is. So you're earnest. This is just a template it looks like. So it's saying you're an autonomous coding agent which is incorrect. And then here's the operating brief on how to actually access the rest of these files and update the rest of these files. For example, memory.mmd updating those as well which it should do automatically after each session. But now we have an agent that is actually up and running. And what I would suggest you doing because there is some optimizations. Like I said this is just a template. So, what you can do is just open up your agent here. I'm going to open this up in Claude and just say, "Hey, I want to update your agent.MD. You are earnest a script writer for my YT channel. Need you to help me with hooks and and outlines." And so, it's updating. It's agent.mmd. And then you can continue to chat with it. And as you work with it, it's just going to get better over time. All right. So, we now have an agent configured with the proper markdown files from an agent.mmd identifying what it is to a memory. And this ADE is about built. So the last part of this is actually showing you how to set this up yourself because I've been building this with Fable, but we now have a public GitHub repo for you to access and download yourself. So that's exactly what I'm going to walk through next. Okay, so I need to make this accessible in a public GitHub repo for people to download. Make sure that you strip away all the secret keys and whatnot. Organize this, make it nice and clean, have a walkthrough guide, and it should just download this Electron app, right? Do we need to do anything with the Electron app to get the set up properly? make sure this is super easy for people and we go through that exact same onboarding that we had previously where we can, you know, create categories, create agents, add profile photos, all of that. Okay, so Fable has set up our GitHub repo and an ability to download this application yourself. So, we're going to do that now by going to this link here, which I of course will include in the description. We've got this GitHub repo and I can install this. So download the signed DMG from the latest release. Open it and then just click this DMG here. It'll download. Also, sorry Windows users. This is only for Mac, but feel free to still clone this repo and you should be able to with Claude build out a proper Windows application relatively easily. Okay. And then just open this download here. Here's the DMG. A nice little icon here. Just drag this into your applications. Then go to applications. Look for AD here. Here it is. It's going to ask you to open it. And you will see a blank screen exactly like we saw when we first set this up. So you can create a new team here. Test. Add a photo. Let's just call this YouTube again. Add a photo. Create category aka team. A bunch of these are just agents I was experimenting with. They're creating out. So you can ignore those. They should be blank for you. This like the whole thing should be blank for you. And then all you need to do is create an agent. So we're going to say earnest use a random image. There we go. Simmons bench badge. Create agent. And it'll just automatically open up claude. And then if you want to open up say Codex or anything like that, you just click there. You'll ask to sign into your Codex subscription or your OpenAI subscription and then you'll be able to access that as well. So that is setup. You can see really simple to do. We have our agent files here and work with your agent on what you want the agent to do. But that's how simple setup is as well. Now I could keep going with this and building out more agents because we've really only scratched the surface on the different categories, the different types of agents that you could build, but that is beyond the scope of this video. So, what I'm going to do is I'm going to create a separate full walkthrough on building out more of these agents yourself and turning this into a proper quote agentic operating system. And in that video, I'll go through every agent I actually use from script writing to ones that help me with content, newsletters, all of that cuz I have a ton. That was also the purpose of this video was creating an AD for myself to run all these agents to actually orchestrate all these agents. But for now, this is more than enough to get you started building your own ADE and start getting agents running completely for free using your existing subscriptions. Anyway, that is going to do it for this one and I'll see you in the next

---

## Timestamped Segments

**[0:00]** AI agents are everywhere. But there are

**[0:02]** two problems. First, pick one and you're

**[0:04]** stuck with it inside their model or

**[0:06]** inside their platform. Second, it is

**[0:08]** complete chaos. You might have a pile of

**[0:10]** chat windows inside different apps like

**[0:11]** Telegram and Slack, different repos

**[0:13]** inside Cloud Code and Codeex, and

**[0:15]** absolutely no system to any of it. If

**[0:17]** you're using an agent platform, the

**[0:18]** context switching alone is killing your

**[0:20]** productivity. But what if I told you

**[0:22]** there's one app that will run all of

**[0:24]** them? Any agent, any model, all in a

**[0:26]** single place? That is exactly what we're

**[0:28]** going to build today. And no, this isn't

**[0:29]** Hermes or Open Claw. It runs on the

**[0:31]** subscriptions you already pay for. We're

**[0:33]** not going to get into any toos gray

**[0:34]** areas and all of your agents, all of

**[0:36]** your chat windows can be accessed inside

**[0:38]** this platform we're about to build. So,

**[0:40]** in this video, I'll show you how to

**[0:41]** build out this agent harness completely

**[0:42]** from scratch with Fable 5. We'll get it

**[0:44]** running in a single command. And by the

**[0:46]** end, you'll have the whole system ready

**[0:47]** to start building out your own team of

**[0:49]** agents, even if you've never built an

**[0:50]** agent before. So, not wasting any more

**[0:52]** time, let's dive right in to the build.

**[0:54]** But first, let me explain what I'm

**[0:55]** envisioning for this harness. So here is

**[0:57]** the mockup I sketched out. Please ignore

**[0:59]** the chicken scratch. But the basic idea

**[1:02]** is we have a category on the left for

**[1:05]** each one of these agents. A good

**[1:06]** category could be say YouTube. And under

**[1:09]** the category we have different agents

**[1:11]** assigned to different parts of YouTube.

**[1:13]** The first agent could be a script writer

**[1:15]** agent. This second agent could be a

**[1:17]** motion graphic creator agent. Another

**[1:20]** agent might monitor analytics. And the

**[1:22]** big idea here is if I select an agent,

**[1:25]** once I select that agent under the

**[1:27]** category, then I can open tabs here

**[1:29]** almost like Chrome browser tabs. And

**[1:31]** each one of these will be a terminal

**[1:33]** session that will allow me to connect to

**[1:36]** different models, whether it's Opus,

**[1:38]** GPT, or any open- source model. And each

**[1:41]** one of these terminal tabs could be

**[1:43]** three different scripts I'm working on

**[1:44]** at one time. I, for one, I'm incredibly

**[1:46]** scatterrained. You might be, too. And I

**[1:48]** want a system that can keep all of the

**[1:50]** different things I'm working on nice and

**[1:52]** organized because typically I'm working

**[1:54]** on multiple scripts at a time. And the

**[1:56]** same will probably be true for editing

**[1:59]** or motion graphics for analytics as

**[2:01]** well. So that's the basic premise and

**[2:03]** this is not a whole lot different than

**[2:05]** how they've architected codecs. If we

**[2:07]** look at codecs, we could in theory in

**[2:09]** these projects organize it in a way

**[2:11]** where each project has a folder assigned

**[2:14]** to each agent. However, we still run

**[2:16]** into issues when I want to create new

**[2:18]** tabs at the top. The tabs are on the

**[2:20]** lefth hand side here instead and I could

**[2:22]** be chatting with different agents at one

**[2:24]** time. But if I have say, I don't know,

**[2:26]** 15 agents, it starts to get really

**[2:28]** cumbersome when I have all the different

**[2:29]** projects I have to scroll through. If

**[2:31]** that's confusing at all, let me show you

**[2:32]** a few examples that get closer to what

**[2:35]** I'm thinking. They are called ADES or

**[2:37]** agentic development environments. There

**[2:39]** are a bunch of them. Semox is a good

**[2:41]** example. The way they have architected

**[2:42]** this is they have these repos or agent

**[2:46]** tabs on the left and then they have tabs

**[2:48]** within each agent. However, these tabs

**[2:50]** are kind of all over the place. It it

**[2:52]** starts to get really confusing, but this

**[2:53]** is more like the general premise. There

**[2:55]** is another healthc conductor.build that

**[2:57]** to me is a little less confusing. Agents

**[2:59]** on the left, tabs at the top. But each

**[3:01]** of these still feel more like aic coding

**[3:04]** environments. And a lot of these agents

**[3:06]** that I want to build out aren't

**[3:07]** necessarily focused on coding. So, we're

**[3:09]** going to take pieces from each of these.

**[3:11]** And the beauty is they are open source.

**[3:13]** So, I can go to their GitHub repos and

**[3:15]** start to duct tape my own customized

**[3:17]** version together into something that I'm

**[3:19]** actually happy with. So, that being

**[3:20]** said, let's now go back to Fable and

**[3:23]** start brainstorming this.

**[3:26]** So, we will open up a new session in

**[3:29]** terminal here with Fable 5 model Fable.

**[3:32]** I'm going to paste in this prompt. I

**[3:34]** will put it on screen. Essentially what

**[3:36]** I am saying is I'm building an ADE. I

**[3:39]** run agents for everything. Writing,

**[3:41]** content, coding. I want one app where

**[3:43]** all of them will live. I give some

**[3:45]** examples like the ones we discussed. I

**[3:47]** say start from superset actually because

**[3:49]** I take that back as I looked further

**[3:51]** into this. Conductor.build is not open

**[3:53]** source. So what we're going to do is

**[3:54]** we're going to use superset instead

**[3:56]** which is very similar looking. Here is

**[3:58]** superset. Same kind of idea. They have

**[4:00]** an open source repo I can pull from. And

**[4:02]** then I'm going to take some screenshots

**[4:03]** from the actual conductor interface,

**[4:05]** paste that into Fable as well. And then

**[4:07]** the rest of the prompt is basically just

**[4:09]** describing what I already went through.

**[4:10]** So the rails, the terminal tabs, each

**[4:12]** workspace is its own repo. And I talked

**[4:14]** about onboarding as well, which we'll

**[4:16]** get into once we actually get the the UI

**[4:18]** set up. But the basic idea of onboarding

**[4:20]** is I want it to be as simple as possible

**[4:21]** for the user. So the minute they open

**[4:23]** the application, they are asked to

**[4:26]** create agents, agent categories, and

**[4:28]** then agents under those categories. So

**[4:30]** that's the idea. And what we're doing as

**[4:31]** well is we're using a fable

**[4:33]** orchestration skill that I put together

**[4:36]** based on this anthropic documentation

**[4:38]** here titled prompting fable 5. They get

**[4:40]** into a lot of the details around this.

**[4:42]** So I fed this into a separate agent and

**[4:44]** we built out a skill based on this and

**[4:46]** that skill can be found here. I will

**[4:49]** include this in the description below

**[4:50]** but it is more or less what anthropic

**[4:52]** details and their docs here just

**[4:54]** organize into a nice easy use skill for

**[4:57]** an agent.

**[4:59]** And in about 20 minutes, we have our

**[5:01]** first mockup alive. Interestingly, it

**[5:04]** used colada artifacts here. I'm not

**[5:05]** exactly sure why. Maybe that's a fable

**[5:07]** thing, but I mean, it should work just

**[5:09]** as well as a local host. So, if we go to

**[5:12]** this link here, and here it is. It's

**[5:14]** looking pretty good. I fed it a

**[5:16]** screenshot of conductor. And you can see

**[5:17]** how similar it is to conductor. We have

**[5:20]** categories on the left. Under those, the

**[5:22]** actual agents, these emojis, of course,

**[5:25]** are obnoxious. I don't think we need

**[5:27]** changes. It basically just matched

**[5:29]** exactly what I gave it the screenshot.

**[5:31]** So, it added changes, checks, run

**[5:34]** terminal setup. We don't need all of

**[5:35]** that. A lot of this is superfluous. It

**[5:37]** also added a light mode, so that needs

**[5:39]** to be fixed. These emojis, of course,

**[5:41]** are driving me absolutely nuts, but I

**[5:43]** like the little tab here. I like the

**[5:45]** loading indicators. It's organized by

**[5:47]** agents. We can add a new category. We

**[5:49]** can name it, but create category. And

**[5:51]** that actually works. Nice. And then you

**[5:52]** can add an agent test. Cool. And you can

**[5:54]** go different models, which we will get

**[5:56]** into setting up. So, this is not a bad

**[5:59]** first pass. I'm going to give it

**[6:01]** feedback. One big thing that I see is

**[6:02]** it's not actually showing terminal,

**[6:04]** which it needs to actually connect to a

**[6:06]** terminal window, as in it needs to run

**[6:08]** directly through the CLI. And it looks

**[6:10]** like it's just like its own interface

**[6:12]** right now, especially when I go light

**[6:13]** mode. You can see it's like got its own

**[6:14]** little interface. So, I'm going to give

**[6:16]** Fable all of that feedback and then

**[6:17]** we'll come back for version two. And

**[6:19]** just in case you're curious, here is the

**[6:21]** follow-up feedback that I gave. I will

**[6:23]** put this on screen now, but it's

**[6:25]** basically describing exactly what I

**[6:26]** said. Getting rid of emojis and ability

**[6:28]** to add a profile photo, connecting the

**[6:29]** CLIs, stripping back some of these

**[6:32]** extraneous designs and functions here.

**[6:34]** And while that builds, Claude and I just

**[6:36]** thought of the name of this application,

**[6:37]** which is going to be Damon, D- A M O N,

**[6:39]** which comes from a play off of Demon,

**[6:42]** Dae M O N, which if you're not familiar,

**[6:45]** is a computer program that runs in the

**[6:46]** background as an independent process.

**[6:48]** And actually back in the day they came

**[6:51]** up with this term based on the Greek for

**[6:54]** d aim o n which in Greek was a

**[6:57]** supernatural entity often seen as a

**[6:59]** guardian or spirit. So it's kind of like

**[7:01]** a like a little helper which is fitting

**[7:03]** for this agent application. Anyway, back

**[7:06]** to the build and v3 is now live. So

**[7:08]** let's check out this latest version. It

**[7:10]** is looking pretty good. Looks like most

**[7:13]** of my feedback is in agent files on the

**[7:15]** right. We've got these tabs at the top.

**[7:18]** We've got our categories and then under

**[7:20]** that is agents. We have these nice

**[7:22]** little loading indicators. New category.

**[7:24]** Upload photo. Oh, does this actually

**[7:26]** work. Just use this random photo for my

**[7:29]** Fable 5 video game. Uh test. Oh yeah,

**[7:32]** look at that. Works. Okay, cool. So, we

**[7:35]** are all set up, ready to go. I'm going

**[7:36]** to go back to this agent and tell it now

**[7:38]** to build this out into a proper Mac

**[7:40]** application.

**[7:43]** Okay. And in about I'd say an hour and a

**[7:45]** half of building, we have something

**[7:48]** ready to go. A Mac application of this

**[7:50]** agents platform for us to react to.

**[7:52]** Fable is not fast, but it is incredibly

**[7:54]** thorough. It had spawned a ton of

**[7:56]** different agents and just went through

**[7:57]** this entire build process. So let's see

**[8:00]** what this app is looking like. It's

**[8:02]** telling me to run this install command.

**[8:04]** I'm just going to say, can you run this

**[8:06]** yourself? Okay, so it looks like we have

**[8:08]** our Mac app up and running. We've

**[8:10]** migrated over from that mockup. So,

**[8:13]** let's check how the Mac app is looking.

**[8:15]** How do I see this? And here it is. So,

**[8:19]** it's looking pretty good. It's pretty

**[8:20]** bare bones, but we should be able to add

**[8:23]** teams here. What I was calling category

**[8:25]** before. Upload a photo. We're going to

**[8:27]** do YouTube first. I have this image

**[8:30]** YouTube. We're going to call this

**[8:32]** YouTube. Create a category. And then we

**[8:34]** have an ability to under this exactly

**[8:36]** like I described. Looks like this is

**[8:38]** working. Adding a new agent. We'll call

**[8:40]** this uh it's a good script writer name.

**[8:43]** Then I can just add a photo here. Just

**[8:45]** going to do a random photo of something.

**[8:47]** Here we go. This uh video game

**[8:48]** screenshot for my Unreal Engine MCP

**[8:51]** video. Good enough. And then right now

**[8:53]** it's only working for Claude. So the

**[8:55]** runtime is going to be Clawed as in

**[8:56]** we're using our Claude subscription. And

**[8:58]** this actually didn't even ask for this.

**[9:00]** Maybe this came from Conductor or

**[9:02]** Superset. But this is really nice

**[9:03]** because you can if you'd like bring in

**[9:06]** an existing GitHub repository. Say you

**[9:08]** have an agent living in a GitHub

**[9:09]** repository. Maybe you already have

**[9:11]** agents and they're not in GitHub yet.

**[9:12]** You could theoretically put those in the

**[9:14]** cloud on GitHub, then upload them

**[9:16]** directly from here with this URL and

**[9:18]** just clone them and automatically upload

**[9:20]** them into our Damon app here. So I'm

**[9:23]** just going to do new empty repo and then

**[9:25]** I believe it's going to create a folder

**[9:26]** locally. Oh wow. Okay, it already opens

**[9:29]** up claude. So okay, yeah, here is the

**[9:30]** folder that it's opening up locally. ad

**[9:33]** default agents and then it's just this

**[9:35]** string and then /worktree and I can go

**[9:38]** yes I trust this folder and boom so we

**[9:40]** have earnest our script writing agent

**[9:42]** all set up you can also go new tab

**[9:44]** create a new session here another

**[9:46]** session with nest we should be able to

**[9:48]** if I go command I yep change the name of

**[9:50]** this so say this is a video about AI

**[9:53]** tools and then and this other one could

**[9:54]** be about say codecs so we have two

**[9:57]** different scripts being written we've

**[9:58]** got Earnest our script writing agent all

**[10:00]** in there we keep track of this we can

**[10:02]** another agent in a new empty repo. And

**[10:04]** then we have all of our agents here

**[10:05]** assigned to different tasks related to

**[10:07]** YouTube. And the way it does that is if

**[10:09]** I just go command T. It's just doing the

**[10:11]** claw dangerously skip permissions

**[10:13]** command. This is just a terminal here

**[10:14]** and I'm already logged into my cloud

**[10:16]** subscription. So it automatically just

**[10:18]** opens this up. So if you were to open

**[10:19]** this up yourself, you just need to a one

**[10:22]** time and it'll allow you to do the same.

**[10:24]** At the end of the video, I'll get into

**[10:25]** onboarding and actually setting this up

**[10:27]** from scratch to make sure that people

**[10:28]** have access to this and can start this

**[10:30]** up themselves. But for now, this is

**[10:32]** looking good. And this is the beauty of

**[10:33]** Fable, by the way. You give it feedback

**[10:35]** and it just does it. There have been no

**[10:37]** revisions off camera. All it took was

**[10:39]** what, three iterations to get here. It

**[10:41]** is very fun working with such a capable

**[10:43]** model like this. Now, the problem with

**[10:44]** this is we're only able to access Claude

**[10:48]** code like I just showed. And the whole

**[10:49]** point was running any model I want as

**[10:51]** well as my Claude subscription. So, how

**[10:52]** do I get any model I want accessible

**[10:54]** within our Damon agent application?

**[10:56]** Well, honestly, I don't even know. So,

**[10:58]** we're going to go back to Fable and

**[10:59]** we're going to tell Fable. All right,

**[11:01]** this is looking good. Everything is

**[11:02]** approved. Now, what I want to do is have

**[11:04]** an ability to add my chatbt subscription

**[11:07]** as well and log into I guess it would be

**[11:09]** technically codecs and use GPT55 within

**[11:12]** this as well as any open- source model.

**[11:14]** And so, I don't know exactly how we can

**[11:16]** set it up with these different open-

**[11:18]** source models. I'm assuming the easiest

**[11:19]** way to do this is through an open router

**[11:21]** API key, but I want an ability to when I

**[11:25]** open up the application, press that new

**[11:27]** tab button. Below the tabs, there should

**[11:29]** be an ability to select GBT, Collad of

**[11:32]** course, then OpenAI logo, then some

**[11:35]** popular open source models like Kimmy

**[11:37]** K27, Miniax M3, and GLM52 with their

**[11:40]** logos as well. So I can just click those

**[11:42]** and it will automatically open a session

**[11:44]** with that open source model. And so I

**[11:46]** think to get those open source models,

**[11:47]** the easiest way to do this is to just

**[11:49]** use an open router API key and we can

**[11:52]** just select all of these. I'll let you

**[11:53]** be the judge of all of this. Let's go

**[11:54]** ahead and spawn agents and do this next.

**[11:57]** All right, our new build is live. So, we

**[12:01]** have an ability now to choose from

**[12:03]** different models. Claude, OpenAI, Kimmy,

**[12:05]** Miniax, GLM, and we should have little

**[12:08]** indicators, little icons to actually

**[12:10]** choose from these. So, let's check this

**[12:11]** out. Okay, looking pretty good. We've

**[12:14]** got the actual icons here to choose

**[12:16]** from. Miniax. Can't actually see that

**[12:17]** logo. Change that. GLM 5.2. Not sure if

**[12:20]** that's the right logo. Need to change

**[12:21]** that. But what we can do, let's see if

**[12:23]** this actually works. Give me K. Okay. So

**[12:25]** nice. We have this. Enter your Open

**[12:27]** Router API key. So I'm going to do that

**[12:28]** now. This should work the exact same way

**[12:30]** once you download this application,

**[12:31]** which again we're going to get into how

**[12:32]** to actually do that. But if I just go

**[12:34]** here, if I go to Open Router right now,

**[12:36]** sign up for Open Router if you haven't

**[12:38]** already, but I'm going to assume that

**[12:40]** you're signed up. Go to workspaces, API

**[12:42]** keys. I just blurred that out, but I

**[12:44]** went create new API key. Hit create.

**[12:46]** Make sure you've got some credits added.

**[12:48]** And then I can go back to our

**[12:49]** application. Kimmy K. paste in my open

**[12:52]** router API key. Save and launch. And

**[12:54]** then it automatically will do this to

**[12:56]** where it will connect. So we're using

**[12:58]** the anthropic base URL. So this is

**[13:00]** loaded in the cloud code harness. This

**[13:02]** is the easiest way to do it. And I don't

**[13:03]** want to get too in the weeds here, but

**[13:04]** what it's doing is it's just pointing to

**[13:06]** the open router API endpoint. We have

**[13:08]** our open router API key that I just

**[13:09]** added. And then it's calling this model

**[13:11]** moonshot give me K27 via Open Router.

**[13:13]** And then I can say, hey, and it looks

**[13:15]** like I'm running into an issue here. 41

**[13:17]** missing authentication header. Not sure

**[13:18]** what's going on there. I just went back

**[13:20]** to Fable, asked Fable to figure this

**[13:21]** out, and I'll fix this quickly. Also,

**[13:23]** while Fable's at it, can you change the

**[13:26]** Miniax logo to be white mode? Find the

**[13:29]** logo. All right, some quick revisions to

**[13:31]** the model pickers. We have updated logos

**[13:34]** here. And we should now have an ability

**[13:35]** apparently to open up any model here.

**[13:37]** KimK27. Hey, what model are you? Cool.

**[13:40]** I'm running with the Kimk 27 coder model

**[13:42]** backend. So now we have an ability to

**[13:45]** use any model with any agent whether

**[13:47]** it's claude codeex or an open- source

**[13:49]** one straight through open router except

**[13:51]** now we've introduced another problem

**[13:53]** which is if I close a tab the agent's

**[13:55]** not going to remember anything. We

**[13:56]** haven't set up the proper markdown files

**[13:58]** yet instructing the agent on who it is

**[14:01]** and what it does and have some sort of

**[14:02]** memory system and self-improving system

**[14:04]** that makes this truly agentic. So that's

**[14:06]** what we're going to set up next and it's

**[14:08]** going to be stored in this file section

**[14:10]** here. This is why I created this drawer

**[14:12]** here to have a quick ability to click

**[14:14]** through and see exactly how we've

**[14:16]** configured this agent. So that's what we

**[14:18]** got next. We're going to go back to

**[14:19]** Fable and explain. Perfect. All

**[14:21]** approved. Now what I need is for us to

**[14:24]** build out agents files. So agents.mmd a

**[14:26]** memory.mmd and anything else that Hermes

**[14:29]** does. I need you to go through the

**[14:30]** Hermes GitHub repo here, determine how

**[14:32]** they have their agents self-improving,

**[14:34]** and then I want you to just fork Hermes

**[14:36]** and bring it right over. And that will

**[14:37]** be our agent structure. So, it's easier

**[14:39]** for me to just use something that

**[14:41]** already exists. I know Hermes has

**[14:42]** probably the best agent memory that

**[14:44]** they've configured. And the beauty of

**[14:46]** this is it's fully open source. So, I

**[14:47]** can give this to my agent, have it parse

**[14:49]** through, find how they've structured the

**[14:51]** memory, and kind of self-improving

**[14:53]** system with their harness, and use this

**[14:54]** for our own agents.

**[14:58]** All right. So, Fable grabbed the Hermes

**[15:00]** GitHub repo, brought over exactly how

**[15:02]** they structure this agent.mmd, userd,

**[15:04]** memory.mmd, and this should now be set

**[15:07]** up in our application. So if we go back

**[15:09]** to our AD, we should now have this set

**[15:11]** up. Yeah. So we have these files here,

**[15:13]** claw.md, and then we also have these

**[15:14]** agent files here. And so each one of

**[15:16]** these are a markdown file, which

**[15:17]** essentially makes up the agent. By the

**[15:19]** way, if any of this is confusing at all

**[15:20]** on the files that actually make up an

**[15:21]** agent or you just want to learn more on

**[15:23]** how to build your own agents from

**[15:25]** scratch, you can check out this video.

**[15:26]** I'll link it above. It's a full course

**[15:28]** on building out AI agents. I'll also

**[15:30]** link another video above which is zero

**[15:31]** to your first AI agent in like 10

**[15:33]** minutes. It'll give you a complete

**[15:34]** walkthrough on all of this. But these

**[15:35]** are essentially the files that make up

**[15:36]** our agent. And we pulled this directly

**[15:38]** from Hermes. So we have our agent.mmd

**[15:40]** which just tells the agent who they are

**[15:41]** and what their role is. So you're

**[15:43]** earnest. This is just a template it

**[15:44]** looks like. So it's saying you're an

**[15:45]** autonomous coding agent which is

**[15:47]** incorrect. And then here's the operating

**[15:48]** brief on how to actually access the rest

**[15:49]** of these files and update the rest of

**[15:51]** these files. For example, memory.mmd

**[15:52]** updating those as well which it should

**[15:54]** do automatically after each session. But

**[15:57]** now we have an agent that is actually up

**[15:59]** and running. And what I would suggest

**[16:01]** you doing because there is some

**[16:02]** optimizations. Like I said this is just

**[16:04]** a template. So, what you can do is just

**[16:06]** open up your agent here. I'm going to

**[16:08]** open this up in Claude and just say,

**[16:10]** "Hey, I want to update your agent.MD.

**[16:13]** You are earnest a script writer for my

**[16:16]** YT channel. Need you to help me with

**[16:19]** hooks and and outlines." And so, it's

**[16:22]** updating. It's agent.mmd. And then you

**[16:24]** can continue to chat with it. And as you

**[16:25]** work with it, it's just going to get

**[16:26]** better over time. All right. So, we now

**[16:28]** have an agent configured with the proper

**[16:30]** markdown files from an agent.mmd

**[16:32]** identifying what it is to a memory. And

**[16:35]** this ADE is about built. So the last

**[16:37]** part of this is actually showing you how

**[16:39]** to set this up yourself because I've

**[16:40]** been building this with Fable, but we

**[16:42]** now have a public GitHub repo for you to

**[16:45]** access and download yourself. So that's

**[16:47]** exactly what I'm going to walk through

**[16:48]** next. Okay, so I need to make this

**[16:51]** accessible in a public GitHub repo for

**[16:53]** people to download. Make sure that you

**[16:54]** strip away all the secret keys and

**[16:55]** whatnot. Organize this, make it nice and

**[16:57]** clean, have a walkthrough guide, and it

**[16:59]** should just download this Electron app,

**[17:01]** right? Do we need to do anything with

**[17:02]** the Electron app to get the set up

**[17:03]** properly? make sure this is super easy

**[17:05]** for people and we go through that exact

**[17:07]** same onboarding that we had previously

**[17:08]** where we can, you know, create

**[17:09]** categories, create agents, add profile

**[17:11]** photos, all of that.

**[17:14]** Okay, so Fable has set up our GitHub

**[17:17]** repo and an ability to download this

**[17:19]** application yourself. So, we're going to

**[17:20]** do that now by going to this link here,

**[17:23]** which I of course will include in the

**[17:25]** description. We've got this GitHub repo

**[17:27]** and I can install this. So download the

**[17:30]** signed DMG from the latest release. Open

**[17:32]** it and then just click this DMG here.

**[17:35]** It'll download. Also, sorry Windows

**[17:37]** users. This is only for Mac, but feel

**[17:39]** free to still clone this repo and you

**[17:40]** should be able to with Claude build out

**[17:42]** a proper Windows application relatively

**[17:44]** easily. Okay. And then just open this

**[17:45]** download here. Here's the DMG. A nice

**[17:47]** little icon here. Just drag this into

**[17:49]** your applications. Then go to

**[17:51]** applications. Look for AD here. Here it

**[17:54]** is. It's going to ask you to open it.

**[17:56]** And you will see a blank screen exactly

**[17:58]** like we saw when we first set this up.

**[18:00]** So you can create a new team here. Test.

**[18:03]** Add a photo. Let's just call this

**[18:04]** YouTube again. Add a photo. Create

**[18:06]** category aka team. A bunch of these are

**[18:08]** just agents I was experimenting with.

**[18:10]** They're creating out. So you can ignore

**[18:11]** those. They should be blank for you.

**[18:12]** This like the whole thing should be

**[18:14]** blank for you. And then all you need to

**[18:15]** do is create an agent. So we're going to

**[18:16]** say earnest use a random image. There we

**[18:19]** go. Simmons bench badge. Create agent.

**[18:21]** And it'll just automatically open up

**[18:23]** claude. And then if you want to open up

**[18:24]** say Codex or anything like that, you

**[18:26]** just click there. You'll ask to sign

**[18:27]** into your Codex subscription or your

**[18:29]** OpenAI subscription and then you'll be

**[18:31]** able to access that as well. So that is

**[18:32]** setup. You can see really simple to do.

**[18:34]** We have our agent files here and work

**[18:36]** with your agent on what you want the

**[18:37]** agent to do. But that's how simple setup

**[18:39]** is as well. Now I could keep going with

**[18:41]** this and building out more agents

**[18:42]** because we've really only scratched the

**[18:43]** surface on the different categories, the

**[18:45]** different types of agents that you could

**[18:46]** build, but that is beyond the scope of

**[18:47]** this video. So, what I'm going to do is

**[18:49]** I'm going to create a separate full

**[18:50]** walkthrough on building out more of

**[18:52]** these agents yourself and turning this

**[18:54]** into a proper quote agentic operating

**[18:56]** system. And in that video, I'll go

**[18:57]** through every agent I actually use from

**[18:59]** script writing to ones that help me with

**[19:01]** content, newsletters, all of that cuz I

**[19:03]** have a ton. That was also the purpose of

**[19:05]** this video was creating an AD for myself

**[19:07]** to run all these agents to actually

**[19:09]** orchestrate all these agents. But for

**[19:10]** now, this is more than enough to get you

**[19:12]** started building your own ADE and start

**[19:14]** getting agents running completely for

**[19:15]** free using your existing subscriptions.

**[19:17]** Anyway, that is going to do it for this

**[19:18]** one and I'll see you in the next
