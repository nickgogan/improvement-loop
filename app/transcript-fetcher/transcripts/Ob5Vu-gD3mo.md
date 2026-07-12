# Transcript: Claude Managed Agents Just Dropped, And It Kills n8n

**URL:** https://www.youtube.com/watch?v=Ob5Vu-gD3mo
**Segments:** 567
**Channel:** Nick Saraev
**Duration:** 16:31
**Uploaded:** 2026-04-08

---

## Full Text

Anthropic just released manage agents, which is their take on automating the process of automating processes. In this video, I'm going to show you guys how manage agents works. I'm going to build you guys a quick little demo flow so you can see how it actually works in production. And then going to connect that to a front end so you guys could see how to build these sorts of flows both on the back end and the front end. And then I'm also going to run through literally every button in this new little dashboard interface so you guys know everything that you need in order to build these sorts of agents yourselves. So, what I'm going to do next is I'm going to build a very simple system, one that I've built for many of my clients many, many times. It's a system where you can basically just paste in a transcript after a sales call, and then it'll go into your project management tool, whatever it is. In my case, uh it'll be ClickUp or maybe Notion, and then it'll populate it with a bunch of tasks that you or your team members have to do. So, I could just write all that stuff out, or I could literally just hold down like a voice transcript tool and say, "Hi, my goal is to build a simple system where I provide a transcript. You take that transcript and use it to create a bunch of tasks in my project management system of choice. The project management system I'm going to use for this example is ClickUp. I'm going to press enter. And now it's going to walk me through the process of building an agent. The first thing it's going to do is define what this agent is going to look like. So it's going to call it the transcript to ClickUp tasks. So I'm going to parse the meeting transcripts and create structured tasks in ClickUp based on action items and so on and so on and so forth. So I'm going to click create this agent. What it'll do is it'll take this schema, the spec, and it'll turn it into my agent. But my agent isn't enough. If you think about the way that most automations work, uh, you know, we have the the actual implementation details, but then you also have to host that implementation somewhere. And so what this does is this is hosting implementation details directly on Anthropic's back end, as in Anthropic is going to spin up a server and then give me a uh reusable little box that always has the exact same parameters and everything like that for me with limited networking for safety reasons. that will allow me to then test and then roll this thing out to, you know, within my own business or or for companies or for clients or whatever. And because I said I wanted ClickUp here, what it's doing is it's saying, "Hey, Nick, you're going to have to add some form of, you know, credential or information in order to do this." And so what I'm going to do is I'm going to create a new vault to store all this. You can see it's now going to pull up pull in the ClickUp credential over here, which is pretty wild. And then I'm going to go over here and say I acknowledge this credential is shared and that I'm responsible for its storage and use. that has OOTH built in. Then I'm just going to click connect. What it'll do next is actually open up some information. So I'm going to connect to my little leftclick workspace. And then I can actually just do the the whole connection and integration without me having to touch API keys at all. And this is fantastic for people that do automation and whatnot because a big barrier to entry is just dealing with API keys and stuff like that. I'm then going to click test run. Now we're going to have uh the ability to paste in a brief transcript. And as you can see there's a test sort of filled out here that says use a transcript from our team standup. Alice will set up the staging environment by Friday. Bob needs to review the API design doc and send feedback and so on and so forth. What I'm going to do is I'm going to click send and I'm just going to show you guys what happens, how easy it is to test end to end. Obviously, this sort of transcript is not about as long as an actual kickoff call transcript or a project management meeting might realistically be. Um, but hopefully it shows you guys just how the interface works. You have two panels here. One called transcript, which is basically just a view of your entire conversation with the agent. Then you have debug, which shows it in sort of like code form. So you can go click in a little bit more and see the type and the process stat and stuff like that. What we're doing now is equivalent to just having a conversation with like Claude normally. It's just we're doing this within this sort of like this uh very standardized container for testing purposes. Now if I click out of that you can see that we have a much larger log here where here's the transcript. The model then starts it's thinking. I've identified five action items from the transcript. Three input 409 output 27,044 cache rights probably a big chunk of its system prompt. And now it's giving it to us. So, I've identified these items. Could you tell me which list or space I should create these in? Are they all their names in ClickUp and stuff like that for the purposes of this demo um because I want to move quickly here and show you guys the rest of how this whole thing works. I'm just going to say put this in example builds/crm. Uh don't do any assignees or anything like that. This is just a demo. And from here on out, um it can now basically do the the API call to ClickUp in order to get that sorted. If there are any issues or it can't complete it for whatever reason, I can now do uh you know my my debugging. I have every raw API event over here. So I can literally see when the model starts, when it ends. There's full interpretability and accountability here, which is obviously great for us automators. And you can see that it's now created all five of these tasks in parallel. So Bob to review the API design doc, Carol to update, and and so on and so on and so forth. We've even received true. And if I go back to my ClickUp here, you can actually see all the tasks that were just generated. set up the staging environment, review the API design doc, send feedback to the team, and so on and so on and so forth. And because I gave it that constraint, obviously it didn't do this um using assignees. It just did it using a bunch of um um text. After you're done testing, it says the run went smoothly. What do you want to do? So, I'm going to uh based off of your conversation with the agent in sort of the transcript and testing, it'll actually say, hey, what do you want to do? Um do you want to modify it a little bit by adding a default ClickUp list or space to the system? So, that's what I'm going to do. I'm also going to add some assigne mapping guidance. And then I'm going to enter. That's now going to actually go back and change the configuration itself. So it's going to ask me some questions. I'll just say example build and then I'll say CRM. As you can see here, we just changed the actual system prompt itself. And now that it's done, all I need to do is say create this agent. And then it'll ask you to test it and so on and so forth, which you can do all the way until you're done. After that, you'll click on the integrate button or you could just tell it literally, hey, I want to integrate. And now it'll basically run you through a step-by-step guide on how to connect this to whatever other platform you want. Now, in my case, I mean, I'm not going to connect this to another platform because I just want this to be a quick little app that I could copy and paste something into or it'll sort of know or understand. But hopefully you guys see how simple it would be to maybe like spin up a quick little front-end app where it's like, hey, you know, an action item generator. You could also connect this directly over to, I don't know, maybe some sort of like proposal or transcript platform. is you click in on specific sessions. That's what I'm doing over here. In the top right hand corner, you can see there's now an ask claude button. And so what I'm going to do just as a demo is I'll say, hey, this uh agent works perfectly. What I want to do next is I want to spin up a front end and then I want to connect that front end little chat window directly to this agent. So when I chat with the window, I'm basically chatting a pass through to this specific transcript agent. That way I can share it amongst my team and anybody can quickly paste in a transcript to very quickly set up um you know ClickUp tasks and stuff. How do I do this? Uh can you do this for me? So on and so forth. The value here is you know you basically have a non- sandbox version of cloud which is just your own. This is a lot more limited than you know running cla code um on your end because you're both limited in terms of your ability to use like fast mode and stuff like that and then obviously I'm pretty sure this is locked into sonnet 4.6 six at least as the time of this recording, but something that can be pretty valuable. And yeah, just to make a long story short, if you can't see cuz of my big fat head, this is just like spitting out a bunch of the uh bunch of the code and whatnot. So, what I'll say, which you can't see, is just give me a prompt I can feed into Claude code to set this up in 30 seconds. Assume I have Netlfi and everything else ready. And now it's going to generate me that prompt ahead. While I'm waiting, I'm just going to move over to anti-gravity and then basically get all the stuff ready. And I'm just going to paste it in over here. And I'll actually have it build a front end for me just for the uh purposes of a fun little demo. And now I have this uh this whole prompt, right? Which is pretty cool. So I can just copy this. There's a little copy modal. Paste this in. And then I'm just going to open this up and show you guys what that looks like. Oh, and then also for speed purposes, I'm just going to go fast mode, which here I can do just by going to one of my many instances, clicking fast, then pressing enter. It'll go back here, stop this, and say fast. And now what it'll do is just generate a very quick website for me. Okay. And after about 30 seconds, we've now uh done a bunch of coding and basically spun up a front end. It's going to check the entropic API key and everything like that. And I just said, I want to run this so I can test this. So now it's going to spin me up a server. Cool. Here's my little chat. And what I'm going to do is I'm going to ask it to quickly whip me up a test that I could use to verify that this works. So I'll say, give me a brief test transcript to verify this works. Now, it's actually testing this alongside me, which is quite nice. And as you can see, it's now generating me a test transcript. Okay, team. three things from yesterday's client review. What I'm going to do is I'm just going to move over here, copy this, and then I'll paste this send. Press send. As you can see, this is now extracting the action items. And you know, obviously I could improve this UX however much I want if we wanted them to chat with this as opposed to maybe Claude. But what it's doing is it's now actually going through and creating those action items. So if I go back to ClickUp, which is right over here, and then I add a date column. So you could see when we created the task, then we sort you can see that we've now write a one pager on new pricing tiers for the sales call. That's what we just did a moment ago. And now all I have to do is literally just push it to production. Voila. We we just created an app. And we didn't just create the app like hardcore mode. Actually going out grabbing the ENV uh the API keys, the credentials, setting up our own environment, all that stuff. We're doing it all entirely on Anthropics infrastructure. I guess aside from our front end, but um this is an unprecedented level of ease with which we just went through that whole process. This is something that if you showed to, you know, somebody that was designing drag and drop interfaces just a couple years ago, they'd probably raise an eyebrow and think that you'd smoked a little bit too much of Brian Johnson's DMT. So, with that out of the way, let's talk a little bit more about this dashboard. The managed agent section, okay, appears over here on platform.claw.com/workspaces/default. And then right now, we're in the agent quickart route, but uh we can just click on any one of these and you can see that route change. And this is basically offered as part of their claude or anthropic API service. And so this is the same like playground that you would jump in if you were doing some sort of API integration or whatnot. Anybody that's done that is probably a little bit more familiar. There's also a build section up here. And then down over here there's some other sections like analytics, there's cloud code, there's manage and stuff, but for now I'll just run you through everything here. Obviously we've already seen the quick start section. Let's move over to the agents where you could see a list of all of the different agents that you have running. Um, you can also archive these at any point in time by clicking these three dots and pressing that archive agent feature. And then you can go directly into, you know, the proposal generator flow in this case or transcript to clickup tasks agent. Uh, and then poke around both the agent view and then the sessions view. Now the agent view is the highle configuration including the MCPs, tools, platforms, and then any additional skills that you've added. Whereas the session view shows you the independent conversations, basically runs that you've had with that agent. And if you click in on that session, you can see that we actually have that that conversation on that test run that I showed you guys earlier where we've created those five tasks. You're kind of talking back and forth with the agent and so on and so forth. You can click on debug in order to get much more information about what the actual API calls and stuff look like. Then you can even filter based off of specific uh requests. So maybe I only want to filter the actual agent messages that have been sent to me. Maybe I only want to look at, I don't know, the thinking sections so I can like look over and see how long the thinking sessions actually took or something. they provide this really cool visual view of what parts of the conversation uh are dedicated to which type of task. And so in this case, the agentthinking only occurred in two small little segments. But if I close this out, you can see there are a bunch of other um sort of checkpoints. This one was running, then I sent a message, then the model started, then it did some thinking, then it stopped, then it was idle, you know, sessions began running, message, and so on and so forth. They typically appear in clusters like this. I want to zoom in a little bit over here because there's a lot more sort of hidden underneath the view. They they put a tremendous amount of work in to make sure that this interface is something you could actually use for work. Notice how here we have the agent view again, which is what that little sort of route looks like. But if you click here now, you actually have your cloud environment. So this is the environment that we just span up. The scope of my environment is the organization. The created time was 10 minutes ago. And here you can actually see the permissions that you've given that environment. This environment, okay, can connect to mcp.clickup.com. It has no packages. It has MCP access enabled and its type is highly limited because obviously this can only really chat internally between it uh and then mcp.clickup.com. This is the sort of security stuff that allows you to work mid-market and then enterprise and build systems like this for real people or use internally in your own business. They've done a really good job of disambiguating between like serious business use cases and then kind of that old school like open claw just give it all your API keys and and have fun. Over here you actually have the uh vault and the vault is their uh way to basically share credentials across organizations and stuff like that. So you can see that it's stored it and given us this nice little modal. We can go to vault which I will do in a moment. And then you also have some additional information like wall clock time since created the total number of tokens in and out which is obviously good for cost and tracking transparency. Then the amount of time it's been since this thing has essentially been set up. Okay. So realistically, as you build more and more agents and then use them across all of your apps, whether they're little chat apps or direct integration, um your sessions will accumulate. But what's cool is you have total overview and oversight capability just by heading over here to this tab. On that environments front, as we saw earlier, I set up a bunch of other proposal generators here as demos as demos. Um I should note that when you archive an agent, okay, you're not actually archiving the environment. So you kind of have to do both. So I'm going to head over here, archive this proposal generator agent just as a demo. go back here to this environment and then I can either archive or delete. Okay, in my case I'm going to delete a bunch of these because I don't want these consuming any resources. So I'll do that here. The simplest and easiest way to set all of this stuff up so far I found is not to use this environment tab to create dedicated environments. But basically use either the quick start or the agents tab to create an agent and then alongside the creation of the agent you will create the environment and the credential vault if necessary. Otherwise it'll just have a bunch of additional environments per one agent. Uh and you know eventually this sort of thing is going to be priced in pretty hard. So make sure to get good use price reduction strategies uh earlier. And then obviously you have those vaults. So I'm just going to archive those so that we don't have to look at them anymore. Okay. Next up, you can check your analytics. And I mean this is build just like API access is. So I mean in my case it looks like I've sent two two uh 2.3 million tokens in and 20,412 tokens out. I did all of that today because I was just testing this feature. You can see the rate limited requests here. Opus 4.6 six caching and input tokens and so on and so forth. This combines um usage across all of your workspaces and your managed agents. So, as you begin populating more usage and you know running this in both your own company and then potentially other people's, you'll see all of that stuff calculated over here. Obviously, that ties into cost of which I've spent $2.40 today to do some testing. You can see most of that was Sonnet 4.6, but there was a little bit of Opus 4.6 as well. And this is sorted month-toate wise. In my case, I spent a fair amount on tokens last month, about $24 in total. Uh, most of that was situated kind of in the middle of the month when I was doing much of Opus stuff for a client of mine. You also have access logs. You can go really deep into every single request you've made. And so, this includes, as mentioned, those managed agents. So, I think the logical thing to ask is where the heck is this going? And where this is going is very quickly, my prediction is that Anthropic is going to build in a visual sort of accompaniment to this sort of communication tool that we have here. Because the big issue right now is we're sort of limited by our own ability to understand systems that are laid out as text bullet points and stuff like that. Uh the main advantage that no code drag and drop platforms like naden, make.com and zap year have over something like cloud manage agents right now is you can literally just like open it up and then you could see the way the system works visually. You could see like this node connects to that node connects to that node. And human brains just work really good like that. you know, we can uh uh see in one picture what would have taken us a thousand words worth of reading in order to really like understand. That's where that idea of like a picture is worth a thousand words comes from. And you know, I I think that the second that Anthropic cracks that, and they're probably already working on this, um we will essentially have like a full replacement for that sort of automation infra. And then either service providers like ourselves or companies that have the knowhow and the technical ability to build stuff like that will basically be able to use this managed infrastructure to do all of their knowledge process automation because like cloud is great and cloud code is like a coding harness is also awesome but you need to go one step further to like the infrastructure layer if you really want to start automating things at scale standardizing inputs and standardizing outputs. Hope you guys appreciated this video. Had a lot of fun putting it together. If you guys have any questions about this just drop it down below. If you guys have ideas for future videos, then please let me know in the comments. I actually get most of my ideas from you guys at this point. So, anything you guys want to see, let me know of. Last big ask is please subscribe to the channel. Something like 70% of people that watch my content regularly aren't for whatever reason. And my goal is to hit a million subscribers before the end of the year. You'd be doing me a big solid by doing so. All right, I'll catch you all in next

---

## Timestamped Segments

**[0:00]** Anthropic just released manage agents,

**[0:02]** which is their take on automating the

**[0:04]** process of automating processes. In this

**[0:06]** video, I'm going to show you guys how

**[0:07]** manage agents works. I'm going to build

**[0:09]** you guys a quick little demo flow so you

**[0:10]** can see how it actually works in

**[0:12]** production. And then going to connect

**[0:13]** that to a front end so you guys could

**[0:14]** see how to build these sorts of flows

**[0:16]** both on the back end and the front end.

**[0:17]** And then I'm also going to run through

**[0:18]** literally every button in this new

**[0:20]** little dashboard interface so you guys

**[0:21]** know everything that you need in order

**[0:23]** to build these sorts of agents

**[0:24]** yourselves. So, what I'm going to do

**[0:25]** next is I'm going to build a very simple

**[0:27]** system, one that I've built for many of

**[0:28]** my clients many, many times. It's a

**[0:30]** system where you can basically just

**[0:32]** paste in a transcript after a sales

**[0:34]** call, and then it'll go into your

**[0:35]** project management tool, whatever it is.

**[0:37]** In my case, uh it'll be ClickUp or maybe

**[0:38]** Notion, and then it'll populate it with

**[0:40]** a bunch of tasks that you or your team

**[0:42]** members have to do. So, I could just

**[0:44]** write all that stuff out, or I could

**[0:45]** literally just hold down like a voice

**[0:46]** transcript tool and say, "Hi, my goal is

**[0:49]** to build a simple system where I provide

**[0:51]** a transcript. You take that transcript

**[0:53]** and use it to create a bunch of tasks in

**[0:54]** my project management system of choice.

**[0:56]** The project management system I'm going

**[0:58]** to use for this example is ClickUp. I'm

**[1:00]** going to press enter. And now it's going

**[1:03]** to walk me through the process of

**[1:04]** building an agent. The first thing it's

**[1:06]** going to do is define what this agent is

**[1:09]** going to look like. So it's going to

**[1:10]** call it the transcript to ClickUp tasks.

**[1:12]** So I'm going to parse the meeting

**[1:13]** transcripts and create structured tasks

**[1:15]** in ClickUp based on action items and so

**[1:17]** on and so on and so forth. So I'm going

**[1:19]** to click create this agent. What it'll

**[1:20]** do is it'll take this schema, the spec,

**[1:22]** and it'll turn it into my agent. But my

**[1:25]** agent isn't enough. If you think about

**[1:26]** the way that most automations work, uh,

**[1:28]** you know, we have the the actual

**[1:30]** implementation details, but then you

**[1:31]** also have to host that implementation

**[1:33]** somewhere. And so what this does is this

**[1:35]** is hosting implementation details

**[1:37]** directly on Anthropic's back end, as in

**[1:39]** Anthropic is going to spin up a server

**[1:41]** and then give me a uh reusable little

**[1:44]** box that always has the exact same

**[1:45]** parameters and everything like that for

**[1:46]** me with limited networking for safety

**[1:48]** reasons. that will allow me to then test

**[1:50]** and then roll this thing out to, you

**[1:53]** know, within my own business or or for

**[1:54]** companies or for clients or whatever.

**[1:56]** And because I said I wanted ClickUp

**[1:58]** here, what it's doing is it's saying,

**[1:59]** "Hey, Nick, you're going to have to add

**[2:01]** some form of, you know, credential or

**[2:03]** information in order to do this." And so

**[2:05]** what I'm going to do is I'm going to

**[2:06]** create a new vault to store all this.

**[2:08]** You can see it's now going to pull up

**[2:10]** pull in the ClickUp credential over

**[2:12]** here, which is pretty wild. And then I'm

**[2:13]** going to go over here and say I

**[2:14]** acknowledge this credential is shared

**[2:16]** and that I'm responsible for its storage

**[2:17]** and use. that has OOTH built in. Then

**[2:19]** I'm just going to click connect. What

**[2:20]** it'll do next is actually open up some

**[2:22]** information. So I'm going to connect to

**[2:24]** my little leftclick workspace. And then

**[2:26]** I can actually just do the the whole

**[2:27]** connection and integration without me

**[2:28]** having to touch API keys at all. And

**[2:30]** this is fantastic for people that do

**[2:32]** automation and whatnot because a big

**[2:33]** barrier to entry is just dealing with

**[2:35]** API keys and stuff like that. I'm then

**[2:37]** going to click test run. Now we're going

**[2:40]** to have uh the ability to paste in a

**[2:41]** brief transcript. And as you can see

**[2:43]** there's a test sort of filled out here

**[2:44]** that says use a transcript from our team

**[2:46]** standup. Alice will set up the staging

**[2:47]** environment by Friday. Bob needs to

**[2:49]** review the API design doc and send

**[2:50]** feedback and so on and so forth. What

**[2:52]** I'm going to do is I'm going to click

**[2:53]** send and I'm just going to show you guys

**[2:54]** what happens, how easy it is to test end

**[2:56]** to end. Obviously, this sort of

**[2:57]** transcript is not about as long as an

**[2:59]** actual kickoff call transcript or a

**[3:01]** project management meeting might

**[3:03]** realistically be. Um, but hopefully it

**[3:05]** shows you guys just how the interface

**[3:06]** works. You have two panels here. One

**[3:08]** called transcript, which is basically

**[3:09]** just a view of your entire conversation

**[3:11]** with the agent. Then you have debug,

**[3:13]** which shows it in sort of like code

**[3:15]** form. So you can go click in a little

**[3:16]** bit more and see the type and the

**[3:18]** process stat and stuff like that. What

**[3:20]** we're doing now is equivalent to just

**[3:21]** having a conversation with like Claude

**[3:23]** normally. It's just we're doing this

**[3:24]** within this sort of like this uh very

**[3:26]** standardized container for testing

**[3:27]** purposes. Now if I click out of that you

**[3:29]** can see that we have a much larger log

**[3:31]** here where here's the transcript. The

**[3:32]** model then starts it's thinking. I've

**[3:34]** identified five action items from the

**[3:36]** transcript. Three input 409 output

**[3:38]** 27,044

**[3:40]** cache rights probably a big chunk of its

**[3:42]** system prompt. And now it's giving it to

**[3:44]** us. So, I've identified these items.

**[3:46]** Could you tell me which list or space I

**[3:47]** should create these in? Are they all

**[3:50]** their names in ClickUp and stuff like

**[3:51]** that for the purposes of this demo um

**[3:53]** because I want to move quickly here and

**[3:54]** show you guys the rest of how this whole

**[3:56]** thing works. I'm just going to say put

**[3:58]** this in example builds/crm.

**[4:01]** Uh don't do any assignees or anything

**[4:02]** like that. This is just a demo.

**[4:05]** And from here on out, um it can now

**[4:07]** basically do the the API call to ClickUp

**[4:10]** in order to get that sorted. If there

**[4:11]** are any issues or it can't complete it

**[4:14]** for whatever reason, I can now do uh you

**[4:16]** know my my debugging. I have every raw

**[4:17]** API event over here. So I can literally

**[4:19]** see when the model starts, when it ends.

**[4:21]** There's full interpretability and

**[4:22]** accountability here, which is obviously

**[4:23]** great for us automators. And you can see

**[4:25]** that it's now created all five of these

**[4:26]** tasks in parallel. So Bob to review the

**[4:28]** API design doc, Carol to update, and and

**[4:30]** so on and so on and so forth. We've even

**[4:32]** received true. And if I go back to my

**[4:33]** ClickUp here, you can actually see all

**[4:34]** the tasks that were just generated. set

**[4:36]** up the staging environment, review the

**[4:37]** API design doc, send feedback to the

**[4:39]** team, and so on and so on and so forth.

**[4:41]** And because I gave it that constraint,

**[4:42]** obviously it didn't do this um using

**[4:43]** assignees. It just did it using a bunch

**[4:45]** of um um text. After you're done

**[4:47]** testing, it says the run went smoothly.

**[4:49]** What do you want to do? So, I'm going to

**[4:51]** uh based off of your conversation with

**[4:53]** the agent in sort of the transcript and

**[4:55]** testing, it'll actually say, hey, what

**[4:56]** do you want to do? Um do you want to

**[4:57]** modify it a little bit by adding a

**[4:59]** default ClickUp list or space to the

**[5:00]** system? So, that's what I'm going to do.

**[5:02]** I'm also going to add some assigne

**[5:03]** mapping guidance. And then I'm going to

**[5:04]** enter. That's now going to actually go

**[5:06]** back and change the configuration

**[5:08]** itself. So it's going to ask me some

**[5:10]** questions. I'll just say example build

**[5:12]** and then I'll say CRM. As you can see

**[5:14]** here, we just changed the actual system

**[5:15]** prompt itself. And now that it's done,

**[5:18]** all I need to do is say create this

**[5:19]** agent. And then it'll ask you to test it

**[5:21]** and so on and so forth, which you can do

**[5:22]** all the way until you're done. After

**[5:24]** that, you'll click on the integrate

**[5:25]** button or you could just tell it

**[5:27]** literally, hey, I want to integrate. And

**[5:29]** now it'll basically run you through a

**[5:31]** step-by-step guide on how to connect

**[5:33]** this to whatever other platform you

**[5:35]** want. Now, in my case, I mean, I'm not

**[5:37]** going to connect this to another

**[5:39]** platform because I just want this to be

**[5:41]** a quick little app that I could copy and

**[5:42]** paste something into or it'll sort of

**[5:44]** know or understand. But hopefully you

**[5:46]** guys see how simple it would be to maybe

**[5:47]** like spin up a quick little front-end

**[5:49]** app where it's like, hey, you know, an

**[5:51]** action item generator. You could also

**[5:53]** connect this directly over to, I don't

**[5:54]** know, maybe some sort of like proposal

**[5:56]** or transcript platform. is you click in

**[5:58]** on specific sessions. That's what I'm

**[5:59]** doing over here. In the top right hand

**[6:01]** corner, you can see there's now an ask

**[6:02]** claude button. And so what I'm going to

**[6:04]** do just as a demo is I'll say, hey, this

**[6:07]** uh agent works perfectly. What I want to

**[6:09]** do next is I want to spin up a front end

**[6:11]** and then I want to connect that front

**[6:12]** end little chat window directly to this

**[6:14]** agent. So when I chat with the window,

**[6:16]** I'm basically chatting a pass through to

**[6:18]** this specific transcript agent. That way

**[6:21]** I can share it amongst my team and

**[6:22]** anybody can quickly paste in a

**[6:23]** transcript to very quickly set up um you

**[6:26]** know ClickUp tasks and stuff. How do I

**[6:27]** do this? Uh can you do this for me? So

**[6:29]** on and so forth. The value here is you

**[6:32]** know you basically have a non- sandbox

**[6:35]** version of cloud which is just your own.

**[6:37]** This is a lot more limited than you know

**[6:38]** running cla code um on your end because

**[6:40]** you're both limited in terms of your

**[6:42]** ability to use like fast mode and stuff

**[6:44]** like that and then obviously I'm pretty

**[6:45]** sure this is locked into sonnet 4.6 six

**[6:47]** at least as the time of this recording,

**[6:48]** but something that can be pretty

**[6:49]** valuable. And yeah, just to make a long

**[6:51]** story short, if you can't see cuz of my

**[6:52]** big fat head, this is just like spitting

**[6:53]** out a bunch of the uh bunch of the code

**[6:55]** and whatnot. So, what I'll say, which

**[6:56]** you can't see, is just give me a prompt

**[6:59]** I can feed into Claude code to set this

**[7:01]** up in 30 seconds. Assume I have Netlfi

**[7:05]** and everything else ready. And now it's

**[7:08]** going to generate me that prompt ahead.

**[7:09]** While I'm waiting, I'm just going to

**[7:10]** move over to anti-gravity and then

**[7:11]** basically get all the stuff ready. And

**[7:13]** I'm just going to paste it in over here.

**[7:14]** And I'll actually have it build a front

**[7:15]** end for me just for the uh purposes of a

**[7:17]** fun little demo. And now I have this uh

**[7:20]** this whole prompt, right? Which is

**[7:21]** pretty cool. So I can just copy this.

**[7:22]** There's a little copy modal. Paste this

**[7:24]** in. And then I'm just going to open this

**[7:26]** up and show you guys what that looks

**[7:27]** like. Oh, and then also for speed

**[7:29]** purposes, I'm just going to go fast

**[7:30]** mode, which here I can do just by going

**[7:32]** to one of my many instances, clicking

**[7:34]** fast, then pressing enter. It'll go back

**[7:36]** here, stop this, and say fast. And now

**[7:39]** what it'll do is just generate a very

**[7:40]** quick website for me. Okay. And after

**[7:42]** about 30 seconds, we've now uh done a

**[7:44]** bunch of coding and basically spun up a

**[7:46]** front end. It's going to check the

**[7:48]** entropic API key and everything like

**[7:50]** that. And I just said, I want to run

**[7:51]** this so I can test this. So now it's

**[7:52]** going to spin me up a server. Cool.

**[7:54]** Here's my little chat. And what I'm

**[7:55]** going to do is I'm going to ask it to

**[7:56]** quickly whip me up a test that I could

**[7:58]** use to verify that this works. So I'll

**[8:00]** say, give me a brief test transcript to

**[8:03]** verify this works. Now, it's actually

**[8:05]** testing this alongside me, which is

**[8:06]** quite nice. And as you can see, it's now

**[8:08]** generating me a test transcript. Okay,

**[8:09]** team. three things from yesterday's

**[8:11]** client review. What I'm going to do is

**[8:12]** I'm just going to move over here, copy

**[8:14]** this, and then I'll paste this send.

**[8:15]** Press send. As you can see, this is now

**[8:17]** extracting the action items. And you

**[8:18]** know, obviously I could improve this UX

**[8:20]** however much I want if we wanted them to

**[8:22]** chat with this as opposed to maybe

**[8:23]** Claude. But what it's doing is it's now

**[8:25]** actually going through and creating

**[8:26]** those action items. So if I go back to

**[8:27]** ClickUp, which is right over here, and

**[8:29]** then I add a date column. So you could

**[8:30]** see when we created the task, then we

**[8:32]** sort you can see that we've now write a

**[8:35]** one pager on new pricing tiers for the

**[8:37]** sales call. That's what we just did a

**[8:38]** moment ago. And now all I have to do is

**[8:40]** literally just push it to production.

**[8:41]** Voila. We we just created an app. And we

**[8:43]** didn't just create the app like hardcore

**[8:46]** mode. Actually going out grabbing the

**[8:47]** ENV uh the API keys, the credentials,

**[8:50]** setting up our own environment, all that

**[8:51]** stuff. We're doing it all entirely on

**[8:53]** Anthropics infrastructure. I guess aside

**[8:55]** from our front end, but um this is an

**[8:57]** unprecedented level of ease with which

**[8:59]** we just went through that whole process.

**[9:01]** This is something that if you showed to,

**[9:03]** you know, somebody that was designing

**[9:04]** drag and drop interfaces just a couple

**[9:05]** years ago, they'd probably raise an

**[9:06]** eyebrow and think that you'd smoked a

**[9:07]** little bit too much of Brian Johnson's

**[9:09]** DMT. So, with that out of the way, let's

**[9:10]** talk a little bit more about this

**[9:12]** dashboard. The managed agent section,

**[9:14]** okay, appears over here on

**[9:16]** platform.claw.com/workspaces/default.

**[9:20]** And then right now, we're in the agent

**[9:21]** quickart route, but uh we can just click

**[9:24]** on any one of these and you can see that

**[9:26]** route change. And this is basically

**[9:27]** offered as part of their claude or

**[9:30]** anthropic API service. And so this is

**[9:32]** the same like playground that you would

**[9:33]** jump in if you were doing some sort of

**[9:35]** API integration or whatnot. Anybody

**[9:37]** that's done that is probably a little

**[9:38]** bit more familiar. There's also a build

**[9:40]** section up here. And then down over here

**[9:42]** there's some other sections like

**[9:43]** analytics, there's cloud code, there's

**[9:45]** manage and stuff, but for now I'll just

**[9:46]** run you through everything here.

**[9:48]** Obviously we've already seen the quick

**[9:49]** start section. Let's move over to the

**[9:51]** agents where you could see a list of all

**[9:52]** of the different agents that you have

**[9:54]** running. Um, you can also archive these

**[9:55]** at any point in time by clicking these

**[9:57]** three dots and pressing that archive

**[9:58]** agent feature. And then you can go

**[10:00]** directly into, you know, the proposal

**[10:01]** generator flow in this case or

**[10:04]** transcript to clickup tasks agent. Uh,

**[10:06]** and then poke around both the agent view

**[10:08]** and then the sessions view. Now the

**[10:10]** agent view is the highle configuration

**[10:12]** including the MCPs, tools, platforms,

**[10:16]** and then any additional skills that

**[10:17]** you've added. Whereas the session view

**[10:18]** shows you the independent conversations,

**[10:21]** basically runs that you've had with that

**[10:22]** agent. And if you click in on that

**[10:24]** session, you can see that we actually

**[10:26]** have that that conversation on that test

**[10:27]** run that I showed you guys earlier where

**[10:29]** we've created those five tasks. You're

**[10:31]** kind of talking back and forth with the

**[10:32]** agent and so on and so forth. You can

**[10:34]** click on debug in order to get much more

**[10:36]** information about what the actual API

**[10:37]** calls and stuff look like. Then you can

**[10:39]** even filter based off of specific uh

**[10:41]** requests. So maybe I only want to filter

**[10:43]** the actual agent messages that have been

**[10:44]** sent to me. Maybe I only want to look

**[10:46]** at, I don't know, the thinking sections

**[10:47]** so I can like look over and see how long

**[10:50]** the thinking sessions actually took or

**[10:51]** something. they provide this really cool

**[10:53]** visual view of what parts of the

**[10:56]** conversation uh are dedicated to which

**[11:00]** type of task. And so in this case, the

**[11:02]** agentthinking only occurred in two small

**[11:04]** little segments. But if I close this

**[11:06]** out, you can see there are a bunch of

**[11:07]** other um sort of checkpoints. This one

**[11:09]** was running, then I sent a message, then

**[11:11]** the model started, then it did some

**[11:12]** thinking, then it stopped, then it was

**[11:14]** idle, you know, sessions began running,

**[11:16]** message, and so on and so forth. They

**[11:18]** typically appear in clusters like this.

**[11:20]** I want to zoom in a little bit over here

**[11:22]** because there's a lot more sort of

**[11:23]** hidden underneath the view. They they

**[11:24]** put a tremendous amount of work in to

**[11:26]** make sure that this interface is

**[11:27]** something you could actually use for

**[11:29]** work. Notice how here we have the agent

**[11:31]** view again, which is what that little

**[11:32]** sort of route looks like. But if you

**[11:34]** click here now, you actually have your

**[11:35]** cloud environment. So this is the

**[11:37]** environment that we just span up. The

**[11:39]** scope of my environment is the

**[11:40]** organization. The created time was 10

**[11:42]** minutes ago. And here you can actually

**[11:43]** see the permissions that you've given

**[11:45]** that environment. This environment,

**[11:47]** okay, can connect to mcp.clickup.com.

**[11:49]** It has no packages. It has MCP access

**[11:51]** enabled and its type is highly limited

**[11:53]** because obviously this can only really

**[11:54]** chat internally between it uh and then

**[11:57]** mcp.clickup.com. This is the sort of

**[11:59]** security stuff that allows you to work

**[12:01]** mid-market and then enterprise and build

**[12:03]** systems like this for real people or use

**[12:05]** internally in your own business. They've

**[12:06]** done a really good job of disambiguating

**[12:08]** between like serious business use cases

**[12:10]** and then kind of that old school like

**[12:12]** open claw just give it all your API keys

**[12:14]** and and have fun. Over here you actually

**[12:16]** have the uh vault and the vault is their

**[12:19]** uh way to basically share credentials

**[12:21]** across organizations and stuff like

**[12:22]** that. So you can see that it's stored it

**[12:24]** and given us this nice little modal. We

**[12:25]** can go to vault which I will do in a

**[12:27]** moment. And then you also have some

**[12:28]** additional information like wall clock

**[12:30]** time since created the total number of

**[12:32]** tokens in and out which is obviously

**[12:33]** good for cost and tracking transparency.

**[12:35]** Then the amount of time it's been since

**[12:37]** this thing has essentially been set up.

**[12:39]** Okay. So realistically, as you build

**[12:41]** more and more agents and then use them

**[12:42]** across all of your apps, whether they're

**[12:44]** little chat apps or direct integration,

**[12:46]** um your sessions will accumulate. But

**[12:48]** what's cool is you have total overview

**[12:50]** and oversight capability just by heading

**[12:52]** over here to this tab. On that

**[12:54]** environments front, as we saw earlier, I

**[12:56]** set up a bunch of other proposal

**[12:57]** generators here as demos as demos. Um I

**[13:00]** should note that when you archive an

**[13:02]** agent, okay, you're not actually

**[13:04]** archiving the environment. So you kind

**[13:05]** of have to do both. So I'm going to head

**[13:06]** over here, archive this proposal

**[13:07]** generator agent just as a demo. go back

**[13:09]** here to this environment and then I can

**[13:10]** either archive or delete. Okay, in my

**[13:13]** case I'm going to delete a bunch of

**[13:14]** these because I don't want these

**[13:15]** consuming any resources. So I'll do that

**[13:16]** here. The simplest and easiest way to

**[13:18]** set all of this stuff up so far I found

**[13:20]** is not to use this environment tab to

**[13:22]** create dedicated environments. But

**[13:23]** basically use either the quick start or

**[13:25]** the agents tab to create an agent and

**[13:27]** then alongside the creation of the agent

**[13:29]** you will create the environment and the

**[13:30]** credential vault if necessary. Otherwise

**[13:32]** it'll just have a bunch of additional

**[13:33]** environments per one agent. Uh and you

**[13:35]** know eventually this sort of thing is

**[13:36]** going to be priced in pretty hard. So

**[13:38]** make sure to get good use price

**[13:40]** reduction strategies uh earlier. And

**[13:42]** then obviously you have those vaults. So

**[13:43]** I'm just going to archive those so that

**[13:44]** we don't have to look at them anymore.

**[13:45]** Okay. Next up, you can check your

**[13:47]** analytics. And I mean this is build just

**[13:49]** like API access is. So I mean in my case

**[13:53]** it looks like I've sent two two uh 2.3

**[13:56]** million tokens in and 20,412 tokens out.

**[13:59]** I did all of that today because I was

**[14:01]** just testing this feature. You can see

**[14:03]** the rate limited requests here. Opus 4.6

**[14:05]** six caching and input tokens and so on

**[14:07]** and so forth. This combines um usage

**[14:10]** across all of your workspaces and your

**[14:11]** managed agents. So, as you begin

**[14:13]** populating more usage and you know

**[14:15]** running this in both your own company

**[14:17]** and then potentially other people's,

**[14:18]** you'll see all of that stuff calculated

**[14:20]** over here. Obviously, that ties into

**[14:21]** cost of which I've spent $2.40 today to

**[14:24]** do some testing. You can see most of

**[14:25]** that was Sonnet 4.6, but there was a

**[14:27]** little bit of Opus 4.6 as well. And this

**[14:30]** is sorted month-toate wise. In my case,

**[14:32]** I spent a fair amount on tokens last

**[14:34]** month, about $24 in total. Uh, most of

**[14:37]** that was situated kind of in the middle

**[14:38]** of the month when I was doing much of

**[14:39]** Opus stuff for a client of mine. You

**[14:41]** also have access logs. You can go really

**[14:43]** deep into every single request you've

**[14:45]** made. And so, this includes, as

**[14:46]** mentioned, those managed agents. So, I

**[14:48]** think the logical thing to ask is where

**[14:49]** the heck is this going? And where this

**[14:51]** is going is very quickly, my prediction

**[14:54]** is that Anthropic is going to build in a

**[14:55]** visual sort of accompaniment to this

**[14:58]** sort of communication tool that we have

**[15:00]** here. Because the big issue right now is

**[15:02]** we're sort of limited by our own ability

**[15:04]** to understand systems that are laid out

**[15:06]** as text bullet points and stuff like

**[15:08]** that. Uh the main advantage that no code

**[15:10]** drag and drop platforms like naden,

**[15:11]** make.com and zap year have over

**[15:13]** something like cloud manage agents right

**[15:14]** now is you can literally just like open

**[15:16]** it up and then you could see the way the

**[15:17]** system works visually. You could see

**[15:19]** like this node connects to that node

**[15:20]** connects to that node. And human brains

**[15:22]** just work really good like that. you

**[15:23]** know, we can uh uh see in one picture

**[15:26]** what would have taken us a thousand

**[15:28]** words worth of reading in order to

**[15:29]** really like understand. That's where

**[15:30]** that idea of like a picture is worth a

**[15:32]** thousand words comes from. And you know,

**[15:34]** I I think that the second that Anthropic

**[15:36]** cracks that, and they're probably

**[15:37]** already working on this, um we will

**[15:38]** essentially have like a full replacement

**[15:40]** for that sort of automation infra. And

**[15:42]** then either service providers like

**[15:44]** ourselves or companies that have the

**[15:46]** knowhow and the technical ability to

**[15:47]** build stuff like that will basically be

**[15:49]** able to use this managed infrastructure

**[15:50]** to do all of their knowledge process

**[15:52]** automation because like cloud is great

**[15:54]** and cloud code is like a coding harness

**[15:56]** is also awesome but you need to go one

**[15:58]** step further to like the infrastructure

**[16:00]** layer if you really want to start

**[16:01]** automating things at scale standardizing

**[16:03]** inputs and standardizing outputs. Hope

**[16:04]** you guys appreciated this video. Had a

**[16:06]** lot of fun putting it together. If you

**[16:07]** guys have any questions about this just

**[16:08]** drop it down below. If you guys have

**[16:10]** ideas for future videos, then please let

**[16:12]** me know in the comments. I actually get

**[16:13]** most of my ideas from you guys at this

**[16:14]** point. So, anything you guys want to

**[16:16]** see, let me know of. Last big ask is

**[16:18]** please subscribe to the channel.

**[16:20]** Something like 70% of people that watch

**[16:21]** my content regularly aren't for whatever

**[16:23]** reason. And my goal is to hit a million

**[16:24]** subscribers before the end of the year.

**[16:26]** You'd be doing me a big solid by doing

**[16:28]** so. All right, I'll catch you all in

**[16:29]** next
